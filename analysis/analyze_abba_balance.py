#!/usr/bin/env python3
"""Compute a simple ABBA balance estimate from a run CSV."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from pathlib import Path


G_LOCAL = 9.80665


def safe_float(value: str | None) -> float | None:
    if value is None or str(value).strip() == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def mean_balance(rows: list[dict[str, str]], state: str) -> float | None:
    values = [
        safe_float(row.get("balance_mg"))
        for row in rows
        if row.get("state") == state and safe_float(row.get("balance_mg")) is not None
    ]
    if not values:
        return None
    return float(statistics.mean(values))


def estimate(rows: list[dict[str, str]], active_state: str) -> dict[str, float | str]:
    sham = mean_balance(rows, "SHAM")
    active = mean_balance(rows, active_state)
    if sham is None:
        raise ValueError("missing SHAM balance_mg rows")
    if active is None:
        raise ValueError(f"missing {active_state} balance_mg rows")
    delta_m_mg = active - sham
    force_n = -G_LOCAL * delta_m_mg * 1e-6
    return {
        "active_state": active_state,
        "mean_sham_mg": sham,
        "mean_active_mg": active,
        "delta_m_mg": delta_m_mg,
        "F_lift_n": force_n,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, type=Path)
    parser.add_argument("--active-state", default="ACTIVE_PLUS")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        result = estimate(load_rows(args.data), args.active_state)
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
