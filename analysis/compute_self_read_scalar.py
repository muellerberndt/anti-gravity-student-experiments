#!/usr/bin/env python3
"""Compute the frozen OPH-style self-read scalar table from packet logs."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


ACTIVE_ROWS = {"ACTIVE_PLUS", "ACTIVE_MINUS", "LIVE"}


def safe_float(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip()
    if text == "":
        return None
    try:
        number = float(text)
    except ValueError:
        return None
    if math.isnan(number) or math.isinf(number):
        return None
    return number


def median(values: list[float]) -> float | None:
    clean = [value for value in values if value is not None and math.isfinite(value)]
    if not clean:
        return None
    return float(statistics.median(clean))


def mad(values: list[float]) -> float | None:
    center = median(values)
    if center is None:
        return None
    return median([abs(value - center) for value in values])


def clip(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path) -> dict[str, Any]:
    with path.open() as handle:
        return json.load(handle)


def get_nested(data: dict[str, Any], path: list[str], default: Any = None) -> Any:
    cursor: Any = data
    for key in path:
        if not isinstance(cursor, dict) or key not in cursor:
            return default
        cursor = cursor[key]
    return cursor


def zone_ports(scorebook: dict[str, Any]) -> dict[str, set[str]]:
    convention = get_nested(scorebook, ["geometry", "zone_convention"], {})
    return {
        "top": set(convention.get("top_zone", [])),
        "bottom": set(convention.get("bottom_zone", [])),
    }


def row_zone(row: dict[str, str], ports_by_zone: dict[str, set[str]]) -> str | None:
    explicit = (row.get("port_zone") or "").strip().lower()
    if explicit in {"top", "bottom"}:
        return explicit
    port_id = (row.get("port_id") or "").strip()
    for zone, ports in ports_by_zone.items():
        if port_id in ports:
            return zone
    return None


def quality_rows(rows: list[dict[str, str]], min_saturation_margin_pct: float) -> list[dict[str, str]]:
    result = []
    for row in rows:
        if safe_float(row.get("ringdown_amp")) is None:
            continue
        if safe_float(row.get("ringdown_phase_deg")) is None:
            continue
        if safe_float(row.get("q_estimate")) is None:
            continue
        saturation_margin = safe_float(row.get("adc_saturation_margin_pct"))
        if saturation_margin is not None and saturation_margin < min_saturation_margin_pct:
            continue
        result.append(row)
    return result


def stability_for_values(values: list[float], epsilon: float) -> float | None:
    center = median(values)
    spread = mad(values)
    if center is None or spread is None:
        return None
    return clip(1.0 / (1.0 + spread / max(abs(center), epsilon)))


def phase_stability(values: list[float]) -> float | None:
    spread = mad(values)
    if spread is None:
        return None
    return clip(1.0 / (1.0 + spread / 180.0))


def record_stability(rows: list[dict[str, str]], epsilon: float) -> tuple[float, list[str]]:
    by_port: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if (row.get("state") or "").strip() not in ACTIVE_ROWS:
            continue
        by_port[(row.get("port_id") or "").strip()].append(row)

    port_scores: list[float] = []
    for port_rows in by_port.values():
        amp = [safe_float(row.get("ringdown_amp")) for row in port_rows]
        phase = [safe_float(row.get("ringdown_phase_deg")) for row in port_rows]
        q_est = [safe_float(row.get("q_estimate")) for row in port_rows]
        scores = [
            stability_for_values([v for v in amp if v is not None], epsilon),
            phase_stability([v for v in phase if v is not None]),
            stability_for_values([v for v in q_est if v is not None], epsilon),
        ]
        clean = [score for score in scores if score is not None]
        if clean:
            port_scores.append(float(statistics.median(clean)))

    if not port_scores:
        return 0.0, ["no stable port feature rows"]
    return float(statistics.median(port_scores)), []


def prediction_coupling(rows: list[dict[str, str]], config: dict[str, Any]) -> tuple[float, list[str]]:
    epsilon = float(config.get("epsilon", 1e-9))
    min_shuffle_error = float(config.get("minimum_shuffle_error", 0.0))
    min_improvement = float(config.get("minimum_absolute_improvement", 0.0))

    live_rows = [row for row in rows if (row.get("state") or "").strip() == "LIVE"]
    live_error = median([safe_float(row.get("prediction_error")) for row in live_rows])
    shuffle_error = median([safe_float(row.get("shuffled_prediction_error")) for row in live_rows])
    if shuffle_error is None:
        shuffled_rows = [row for row in rows if (row.get("state") or "").strip() == "SHUFFLED_RECORD"]
        shuffle_error = median([safe_float(row.get("prediction_error")) for row in shuffled_rows])

    reasons = []
    if live_error is None:
        reasons.append("missing LIVE prediction_error")
    if shuffle_error is None:
        reasons.append("missing shuffled baseline error")
    if reasons:
        return 0.0, reasons
    if shuffle_error < min_shuffle_error:
        return 0.0, ["shuffled baseline already excellent"]

    improvement = shuffle_error - live_error
    if improvement < min_improvement:
        return 0.0, ["prediction improvement below absolute minimum"]
    return clip(improvement / max(shuffle_error, epsilon)), []


def mismatch_reduction(rows: list[dict[str, str]], config: dict[str, Any]) -> tuple[float, list[str]]:
    epsilon = float(config.get("epsilon", 1e-9))
    min_improvement = float(config.get("minimum_absolute_improvement", 0.0))
    min_live_improvement = float(config.get("minimum_live_absolute_improvement", 0.0))

    live_rows = [row for row in rows if (row.get("state") or "").strip() == "LIVE"]
    replay_rows = [row for row in rows if (row.get("state") or "").strip() == "REPLAY"]

    live_before = median([safe_float(row.get("mismatch_before")) for row in live_rows])
    live_after = median([safe_float(row.get("mismatch_after")) for row in live_rows])
    replay_after = median([safe_float(row.get("mismatch_after")) for row in replay_rows])

    reasons = []
    if live_before is None:
        reasons.append("missing LIVE mismatch_before")
    if live_after is None:
        reasons.append("missing LIVE mismatch_after")
    if replay_after is None:
        reasons.append("missing REPLAY mismatch_after")
    if reasons:
        return 0.0, reasons
    if replay_after <= epsilon:
        return 0.0, ["REPLAY mismatch denominator below epsilon"]
    if live_before - live_after < min_live_improvement:
        return 0.0, ["LIVE before-after improvement below absolute minimum"]

    improvement = replay_after - live_after
    if improvement < min_improvement:
        return 0.0, ["LIVE versus REPLAY improvement below absolute minimum"]
    return clip(improvement / max(replay_after, epsilon)), []


def zone_result(zone: str, rows: list[dict[str, str]], scorebook: dict[str, Any]) -> dict[str, Any]:
    scalar = get_nested(scorebook, ["scalar_formula"], {})
    min_ports = int(get_nested(scalar, ["self_read_gate", "minimum_required_ports_per_zone"], 2))
    min_saturation_margin_pct = float(
        get_nested(scorebook, ["exclusions", "minimum_adc_saturation_margin_pct"], 5.0)
    )

    valid = quality_rows(rows, min_saturation_margin_pct)
    ports = {row.get("port_id") for row in valid if row.get("port_id")}
    reasons: list[str] = []
    self_read_gate = 1 if len(ports) >= min_ports else 0
    if not self_read_gate:
        reasons.append("too few valid ports")

    r_config = get_nested(scalar, ["record_stability_R_U"], {})
    p_config = get_nested(scalar, ["predictive_boundary_coupling_P_U"], {})
    c_config = get_nested(scalar, ["coherent_mismatch_reduction_C_U"], {})

    r_u, r_reasons = record_stability(valid, float(r_config.get("epsilon", 1e-9)))
    p_u, p_reasons = prediction_coupling(valid, p_config)
    c_u, c_reasons = mismatch_reduction(valid, c_config)
    reasons.extend(r_reasons + p_reasons + c_reasons)

    thresholds = {
        "R_U": float(r_config.get("threshold", 0.0)),
        "P_U": float(p_config.get("threshold", 0.0)),
        "C_U": float(c_config.get("threshold", 0.0)),
    }
    if r_u < thresholds["R_U"]:
        reasons.append("R_U below threshold")
    if p_u < thresholds["P_U"]:
        reasons.append("P_U below threshold")
    if c_u < thresholds["C_U"]:
        reasons.append("C_U below threshold")

    s_zone = float(self_read_gate) * r_u * p_u * c_u
    uncertainty_values = [
        safe_float(row.get("delta_s_coh"))
        for row in valid
        if safe_float(row.get("delta_s_coh")) is not None
    ]
    uncertainty = 0.0
    if len(uncertainty_values) > 1:
        uncertainty = statistics.pstdev(uncertainty_values) / math.sqrt(len(uncertainty_values))

    return {
        "zone": zone,
        "self_read_gate": self_read_gate,
        "R_U": round(r_u, 6),
        "P_U": round(p_u, 6),
        "C_U": round(c_u, 6),
        "S_zone": round(s_zone, 6),
        "uncertainty": round(uncertainty, 6),
        "pass": not reasons,
        "fail_reason": "; ".join(reasons),
    }


def compute_table(rows: list[dict[str, str]], scorebook: dict[str, Any]) -> dict[str, Any]:
    ports_by_zone = zone_ports(scorebook)
    by_zone = {"top": [], "bottom": []}
    for row in rows:
        zone = row_zone(row, ports_by_zone)
        if zone in by_zone:
            by_zone[zone].append(row)

    top = zone_result("top", by_zone["top"], scorebook)
    bottom = zone_result("bottom", by_zone["bottom"], scorebook)
    delta = bottom["S_zone"] - top["S_zone"]

    delta_config = get_nested(scorebook, ["scalar_formula", "delta_s_coh"], {})
    plus_threshold = float(delta_config.get("plus_threshold", 0.0))
    minus_threshold = float(delta_config.get("minus_threshold", 0.0))
    delta_pass = (delta > plus_threshold) or (delta < minus_threshold)
    delta_row = {
        "zone": "delta_s_coh",
        "self_read_gate": min(top["self_read_gate"], bottom["self_read_gate"]),
        "R_U": None,
        "P_U": None,
        "C_U": None,
        "S_zone": round(delta, 6),
        "uncertainty": round(math.sqrt(top["uncertainty"] ** 2 + bottom["uncertainty"] ** 2), 6),
        "pass": delta_pass and top["pass"] and bottom["pass"],
        "fail_reason": "" if delta_pass else "delta_s_coh below signed threshold",
    }
    return {"table": [top, bottom, delta_row], "delta_s_coh": round(delta, 6)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, type=Path)
    parser.add_argument("--scorebook", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    result = compute_table(load_csv(args.data), load_json(args.scorebook))
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n")
    else:
        print(text)
    failed = [row for row in result["table"] if not row["pass"]]
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
