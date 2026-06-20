#!/usr/bin/env python3
"""Validate a run bundle against the frozen manifest and scorebook."""

from __future__ import annotations

import argparse
import csv
import datetime as _datetime
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import jsonschema
import yaml

import compute_self_read_scalar


SCRIPT_DIR = Path(__file__).resolve().parent
SCHEMA_DIR = SCRIPT_DIR / "schemas"
P_TARGET = 1.6309682

CONFIRMATION_FIELDS = [
    "repository.package_commit_hash",
    "analysis.scorebook_hash",
    "device.firmware_hash",
    "device.wiring_map_hash",
    "device.body_geometry_hash",
    "drive.state_schedule_hash",
    "drive.waveform_hash",
    "theory.selected_branch",
    "theory.theory_branch_file",
    "analysis.randomization_seed",
    "geometry.physical_flip_axis",
    "geometry.p_target_status",
    "geometry.p_target_value",
    "geometry.p_geometry_ratio",
    "geometry.p_geometry_elements",
    "geometry.p_detuned_control_id",
    "controls.horizontal_axis_inversion",
    "controls.dummy_run",
    "controls.live_replay_ablation",
    "controls.open_loop_replay_ablation",
    "controls.causal_shuffle_ablation",
    "controls.yoked_shuffle_replay_ablation",
    "controls.no_external_cables",
    "measurement.adc_calibration_file",
    "measurement.adc_saturation_margin_pct",
    "measurement.allan_deviation_file",
    "measurement.systematic_floor_n",
    "measurement.vibration_rectification_calibration_file",
    "measurement.blind_code_file",
    "analysis.analysis_environment_lockfile",
    "analysis.verifier_hash",
    "analysis.minimum_abs_force_n",
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open() as handle:
        return json.load(handle)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open() as handle:
        loaded = yaml.safe_load(handle)
    return normalize_yaml_scalars(loaded or {})


def normalize_yaml_scalars(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: normalize_yaml_scalars(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize_yaml_scalars(item) for item in value]
    if isinstance(value, (_datetime.date, _datetime.datetime)):
        return value.isoformat()
    return value


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def get_path(data: dict[str, Any], dotted: str, default: Any = None) -> Any:
    cursor: Any = data
    for part in dotted.split("."):
        if not isinstance(cursor, dict) or part not in cursor:
            return default
        cursor = cursor[part]
    return cursor


def is_blank(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() == ""
    return False


def schema_validate(name: str, value: dict[str, Any]) -> list[str]:
    schema = load_json(SCHEMA_DIR / name)
    validator = jsonschema.Draft202012Validator(schema)
    return [error.message for error in sorted(validator.iter_errors(value), key=str)]


def confirmation_requested(args: argparse.Namespace, manifest: dict[str, Any]) -> bool:
    if args.confirmation:
        return True
    if get_path(manifest, "analysis.phase") == "confirmation":
        return True
    run_directory = str(manifest.get("run_directory", ""))
    if "/confirmation/" in run_directory or run_directory.startswith("runs/confirmation/"):
        return True
    claim = str(get_path(manifest, "claims.strongest_allowed_claim", ""))
    return "candidate" in claim.lower()


def check_confirmation_fields(manifest: dict[str, Any]) -> list[str]:
    errors = []
    for dotted in CONFIRMATION_FIELDS:
        value = get_path(manifest, dotted)
        if is_blank(value):
            errors.append(f"confirmation field is blank: {dotted}")
    for dotted in [
        "controls.horizontal_axis_inversion",
        "controls.dummy_run",
        "controls.live_replay_ablation",
        "controls.open_loop_replay_ablation",
        "controls.causal_shuffle_ablation",
        "controls.yoked_shuffle_replay_ablation",
        "controls.inert_shaker_balance_rectification",
        "controls.two_mount_topologies",
        "controls.two_pan_positions",
        "controls.no_external_cables",
    ]:
        if get_path(manifest, dotted) is not True:
            errors.append(f"confirmation boolean must be true: {dotted}")
    if get_path(manifest, "geometry.oph_vertical_scalar_claim") is True:
        if get_path(manifest, "geometry.zone_definition") != "top_bottom":
            errors.append("OPH vertical scalar claim requires geometry.zone_definition: top_bottom")
        if get_path(manifest, "geometry.p_target_status") != "p_integrated":
            errors.append("OPH vertical scalar claim requires geometry.p_target_status: p_integrated")
        try:
            p_value = float(get_path(manifest, "geometry.p_target_value"))
            if abs(p_value - P_TARGET) > 1e-6:
                errors.append("geometry.p_target_value must match 1.6309682 for a P-integrated claim")
        except (TypeError, ValueError):
            errors.append("geometry.p_target_value must be numeric for a P-integrated claim")
        for dotted in (
            "geometry.p_geometry_ratio",
            "geometry.p_geometry_elements",
            "geometry.p_detuned_control_id",
        ):
            if is_blank(get_path(manifest, dotted)):
                errors.append(f"OPH vertical scalar claim requires {dotted}")
    if get_path(manifest, "measurement.blind_code_opened_after_lock") is not False:
        errors.append("blind code must remain closed until after analysis lock")
    if get_path(manifest, "analysis.canonical_scalar_claim") is not False:
        errors.append("analysis.canonical_scalar_claim must be false without a proxy-to-canonical bridge")
    return errors


def check_hashes(
    manifest: dict[str, Any],
    scorebook_path: Path,
    verifier_path: Path,
) -> list[str]:
    errors = []
    expected_scorebook = get_path(manifest, "analysis.scorebook_hash")
    if expected_scorebook and expected_scorebook != sha256(scorebook_path):
        errors.append("manifest scorebook_hash does not match scorebook file")
    expected_verifier = get_path(manifest, "analysis.verifier_hash")
    if expected_verifier and expected_verifier != sha256(verifier_path):
        errors.append("manifest verifier_hash does not match verify_scorebook.py")
    return errors


def check_vertical_scalar_instrumentation(manifest: dict[str, Any]) -> list[str]:
    if get_path(manifest, "geometry.oph_vertical_scalar_claim") is not True:
        return []
    transducers = get_path(manifest, "device.transducers", []) or []
    top = 0
    bottom = 0
    for item in transducers:
        zone = str((item or {}).get("face_or_zone", "")).strip().lower()
        if zone == "top":
            top += 1
        if zone == "bottom":
            bottom += 1
    errors = []
    if top < 2 or bottom < 2:
        errors.append("OPH vertical scalar claim requires at least two top and two bottom transducers")
    if get_path(manifest, "geometry.single_pickup_per_dish_is_conventional_only") is not True:
        errors.append("manifest must mark single pickup per dish as conventional-only")
    return errors


def check_theory_branch(manifest: dict[str, Any], scorebook: dict[str, Any]) -> list[str]:
    errors = []
    manifest_branch = get_path(manifest, "theory.selected_branch")
    scorebook_branch = scorebook.get("theory_branch")
    if manifest_branch != "oph_chi_nu_canonical_linear_v1":
        errors.append("selected theory branch must be oph_chi_nu_canonical_linear_v1")
    if scorebook_branch != manifest_branch:
        errors.append("scorebook theory_branch does not match manifest theory.selected_branch")
    if scorebook.get("canonical_scalar_claim") is not False:
        errors.append("scorebook must mark canonical_scalar_claim as false unless a bridge is supplied")
    bridge_status = get_path(scorebook, "proxy_scalar.canonical_bridge_status")
    if bridge_status != "absent":
        errors.append("non-absent canonical bridge requires a separate bridge verifier")
    return errors


def check_scorebook_force_threshold(scorebook: dict[str, Any]) -> list[str]:
    value = get_path(scorebook, "force_decision.candidate_threshold.minimum_abs_force_n")
    if value is None:
        return ["scorebook minimum_abs_force_n must be set from the measured systematic floor"]
    try:
        if float(value) <= 0:
            return ["scorebook minimum_abs_force_n must be positive"]
    except (TypeError, ValueError):
        return ["scorebook minimum_abs_force_n must be numeric"]
    return []


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def check_data_columns(data_path: Path) -> list[str]:
    schema = load_json(SCHEMA_DIR / "data_columns.schema.json")
    required = schema["required_columns"]
    with data_path.open(newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
    missing = [column for column in required if column not in header]
    return [f"data column missing: {column}" for column in missing]


def median_float(rows: list[dict[str, str]], column: str) -> float | None:
    values = [compute_self_read_scalar.safe_float(row.get(column)) for row in rows]
    clean = [value for value in values if value is not None]
    if not clean:
        return None
    return sorted(clean)[len(clean) // 2]


def check_packet_identity(rows: list[dict[str, str]]) -> list[str]:
    errors = []
    live_by_block: dict[str, dict[str, str]] = {}
    causal_shuffle_by_block: dict[str, dict[str, str]] = {}
    for row in rows:
        if row.get("state") == "LIVE":
            block_id = row.get("block_id", "")
            if block_id and block_id not in live_by_block:
                live_by_block[block_id] = row
        if row.get("state") == "CAUSAL_SHUFFLE":
            block_id = row.get("block_id", "")
            if block_id and block_id not in causal_shuffle_by_block:
                causal_shuffle_by_block[block_id] = row

    for row in rows:
        state = row.get("state")
        if state not in {"OPEN_LOOP_REPLAY", "YOKED_SHUFFLE_REPLAY", "CAUSAL_SHUFFLE"}:
            continue
        if state == "CAUSAL_SHUFFLE":
            if not row.get("shuffle_seed"):
                errors.append("CAUSAL_SHUFFLE row missing shuffle_seed")
            if not row.get("feedback_input_hash"):
                errors.append("CAUSAL_SHUFFLE row missing feedback_input_hash")
            continue
        source = row.get("replay_source_run_id", "")
        if not source:
            errors.append(f"{state} row missing replay_source_run_id")
            continue
        source_map = live_by_block if state == "OPEN_LOOP_REPLAY" else causal_shuffle_by_block
        source_label = "LIVE" if state == "OPEN_LOOP_REPLAY" else "CAUSAL_SHUFFLE"
        source_row = source_map.get(source)
        if source_row is None:
            errors.append(f"{state} row references missing {source_label} block: {source}")
            continue
        for column in [
            "drive_packet_hash",
            "drive_vector_json_sha256",
            "terminal_voltage_trace_hash",
            "terminal_current_trace_hash",
            "timing_hash",
        ]:
            if row.get(column) != source_row.get(column):
                errors.append(f"{state} packet is not waveform-identical for {column}")
    return errors


def check_environment(rows: list[dict[str, str]], scorebook: dict[str, Any]) -> list[str]:
    temps = [compute_self_read_scalar.safe_float(row.get("temperature_c")) for row in rows]
    clean_temps = [temp for temp in temps if temp is not None]
    if len(clean_temps) < 2:
        return []
    drift = max(clean_temps) - min(clean_temps)
    max_drift = get_path(scorebook, "exclusions.max_temperature_drift_c", 0.5)
    errors = []
    if drift > float(max_drift):
        errors.append(f"temperature drift exceeds scorebook limit: {drift:.3f} C")
    clipping_limit = float(get_path(scorebook, "exclusions.max_sensor_clipping_rate", 0.001))
    clipping = [
        compute_self_read_scalar.safe_float(row.get("sensor_clipping_rate"))
        for row in rows
    ]
    clean_clipping = [value for value in clipping if value is not None]
    if clean_clipping and max(clean_clipping) > clipping_limit:
        errors.append("sensor clipping rate exceeds scorebook limit")
    return errors


def check_run_directory(args: argparse.Namespace, manifest: dict[str, Any], confirmation: bool) -> list[str]:
    if not confirmation:
        return []
    paths = [str(manifest.get("run_directory", ""))]
    if args.run_root:
        paths.append(str(args.run_root))
    return [
        "confirmation run directory must not contain exploration data"
        for path in paths
        if "exploration" in Path(path).parts
    ]


def verify(args: argparse.Namespace) -> tuple[bool, list[str], dict[str, Any] | None]:
    errors: list[str] = []
    manifest = load_yaml(args.manifest)
    scorebook = load_json(args.scorebook)

    errors.extend(schema_validate("run_manifest.schema.json", manifest))
    errors.extend(schema_validate("scorebook.schema.json", scorebook))
    errors.extend(check_theory_branch(manifest, scorebook))
    errors.extend(check_scorebook_force_threshold(scorebook))

    confirmation = confirmation_requested(args, manifest)
    if confirmation:
        errors.extend(check_confirmation_fields(manifest))
        if args.data is None:
            errors.append("confirmation verification requires --data raw packet log")
    errors.extend(check_hashes(manifest, args.scorebook, Path(__file__).resolve()))
    errors.extend(check_vertical_scalar_instrumentation(manifest))
    errors.extend(check_run_directory(args, manifest, confirmation))

    scalar_result = None
    if args.data:
        errors.extend(check_data_columns(args.data))
        rows = load_rows(args.data)
        errors.extend(check_packet_identity(rows))
        errors.extend(check_environment(rows, scorebook))
        scalar_result = compute_self_read_scalar.compute_table(rows, scorebook)
        if confirmation:
            failed = [row for row in scalar_result["table"] if not row["pass"]]
            for row in failed:
                errors.append(f"scalar table failed for {row['zone']}: {row['fail_reason']}")

    return not errors, errors, scalar_result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--scorebook", required=True, type=Path)
    parser.add_argument("--data", type=Path)
    parser.add_argument("--run-root", type=Path)
    parser.add_argument("--confirmation", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    ok, errors, scalar_result = verify(args)
    payload = {"ok": ok, "errors": errors, "scalar_result": scalar_result}
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        if ok:
            print("verification ok")
        else:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
        if scalar_result is not None:
            print(json.dumps(scalar_result, indent=2, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
