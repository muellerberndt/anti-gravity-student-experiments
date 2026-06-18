#!/usr/bin/env python3
"""Run verifier checks against synthetic good and bad run bundles."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"
SCOREBOOK = ROOT / "templates" / "scorebook_template.json"
VERIFIER = ANALYSIS / "verify_scorebook.py"
TESTS = ANALYSIS / "tests"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_manifest(src: Path, dst: Path) -> None:
    text = src.read_text()
    text = text.replace("__SCOREBOOK_SHA256__", sha256(SCOREBOOK))
    text = text.replace("__VERIFIER_SHA256__", sha256(VERIFIER))
    dst.write_text(text)


def run_fixture(name: str, should_pass: bool) -> bool:
    fixture = TESTS / name
    with tempfile.TemporaryDirectory() as temp_dir:
        manifest = Path(temp_dir) / "manifest.yaml"
        write_manifest(fixture / "manifest.yaml", manifest)
        cmd = [
            sys.executable,
            str(VERIFIER),
            "--manifest",
            str(manifest),
            "--scorebook",
            str(SCOREBOOK),
            "--data",
            str(fixture / "device_log.csv"),
            "--confirmation",
        ]
        result = subprocess.run(cmd, text=True, capture_output=True)
    passed = result.returncode == 0
    if passed != should_pass:
        print(f"fixture {name} unexpected result", file=sys.stderr)
        print(result.stdout, file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        return False
    print(f"{name}: {'pass' if passed else 'expected failure'}")
    return True


def main() -> int:
    checks = [
        run_fixture("synthetic_valid_run", True),
        run_fixture("synthetic_bad_shuffle_run", False),
        run_fixture("synthetic_thermal_artifact_run", False),
    ]
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
