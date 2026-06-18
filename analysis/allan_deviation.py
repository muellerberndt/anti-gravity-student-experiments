#!/usr/bin/env python3
"""Compute non-overlapping Allan deviation for one numeric CSV column."""

from __future__ import annotations

import argparse
import csv
import math
import statistics
import sys
from pathlib import Path


def safe_float(value: str | None) -> float | None:
    if value is None or str(value).strip() == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def load_values(path: Path, column: str) -> list[float]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        values = [safe_float(row.get(column)) for row in reader]
    return [value for value in values if value is not None]


def allan(values: list[float], block: int) -> float | None:
    if block <= 0:
        return None
    means = []
    for start in range(0, len(values) - block + 1, block):
        chunk = values[start : start + block]
        if len(chunk) == block:
            means.append(statistics.mean(chunk))
    if len(means) < 2:
        return None
    diffs = [(means[index + 1] - means[index]) ** 2 for index in range(len(means) - 1)]
    return math.sqrt(0.5 * statistics.mean(diffs))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, type=Path)
    parser.add_argument("--column", default="balance_mg")
    parser.add_argument("--blocks", default="1,2,4,8,16,32")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    values = load_values(args.data, args.column)
    rows = ["block_samples,allan_deviation"]
    for text in args.blocks.split(","):
        block = int(text.strip())
        value = allan(values, block)
        if value is not None:
            rows.append(f"{block},{value}")
    output = "\n".join(rows) + "\n"
    if args.output:
        args.output.write_text(output)
    else:
        print(output, end="")
    return 0 if len(rows) > 1 else 1


if __name__ == "__main__":
    sys.exit(main())
