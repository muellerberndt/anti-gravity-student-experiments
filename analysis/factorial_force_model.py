#!/usr/bin/env python3
"""Estimate the preregistered orientation x proxy x live interaction."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np


G0 = 9.80665


def safe_float(value: str | None) -> float | None:
    if value is None or str(value).strip() == "":
        return None
    try:
        number = float(value)
    except ValueError:
        return None
    if math.isnan(number) or math.isinf(number):
        return None
    return number


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def design_rows(rows: list[dict[str, str]]) -> tuple[np.ndarray, np.ndarray]:
    x_rows = []
    y_rows = []
    for row in rows:
        balance = safe_float(row.get("balance_mg"))
        delta = safe_float(row.get("delta_S_hat"))
        q = safe_float(row.get("physical_orientation_q"))
        if balance is None or delta is None or q is None:
            continue
        state = row.get("state")
        live = 1.0 if state == "LIVE" else 0.0
        replay = 1.0 if state in {"OPEN_LOOP_REPLAY", "YOKED_SHUFFLE_REPLAY"} else 0.0
        temp = safe_float(row.get("temperature_c")) or 0.0
        dtemp = safe_float(row.get("dtemp_dt_c_per_s")) or 0.0
        power = safe_float(row.get("drive_real_power_w")) or safe_float(row.get("drive_power_w")) or 0.0
        accel = safe_float(row.get("accel_z_g")) or 0.0
        battery = safe_float(row.get("battery_v")) or 0.0
        force_n = -G0 * balance * 1e-6
        interaction = q * delta
        x_rows.append([1.0, live * interaction, replay * interaction, temp, dtemp, power, accel, battery])
        y_rows.append(force_n)
    if len(x_rows) < 8:
        raise ValueError("not enough rows for factorial fit")
    return np.asarray(x_rows, dtype=float), np.asarray(y_rows, dtype=float)


def fit(rows: list[dict[str, str]]) -> dict[str, float]:
    x, y = design_rows(rows)
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    residual = y - x @ beta
    dof = max(len(y) - x.shape[1], 1)
    sigma2 = float((residual @ residual) / dof)
    cov = sigma2 * np.linalg.pinv(x.T @ x)
    se = np.sqrt(np.diag(cov))
    k_live = float(beta[1])
    k_replay = float(beta[2])
    contrast = k_live - k_replay
    contrast_se = float(math.sqrt(cov[1, 1] + cov[2, 2] - 2 * cov[1, 2]))
    return {
        "K_live": k_live,
        "K_live_se": float(se[1]),
        "K_replay": k_replay,
        "K_replay_se": float(se[2]),
        "K_live_minus_K_replay": contrast,
        "K_live_minus_K_replay_se": contrast_se,
        "rows_used": int(len(y)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = fit(load_rows(args.data))
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
