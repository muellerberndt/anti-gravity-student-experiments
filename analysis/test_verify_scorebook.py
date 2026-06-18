#!/usr/bin/env python3
"""Unit-test entry point for the evidence-bundle verifier."""

from __future__ import annotations

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_synthetic_tests


class VerifyScorebookFixtures(unittest.TestCase):
    def test_synthetic_valid_run_passes(self) -> None:
        self.assertTrue(run_synthetic_tests.run_fixture("synthetic_valid_run", True))

    def test_bad_shuffle_run_fails(self) -> None:
        self.assertTrue(run_synthetic_tests.run_fixture("synthetic_bad_shuffle_run", False))

    def test_thermal_artifact_run_fails(self) -> None:
        self.assertTrue(run_synthetic_tests.run_fixture("synthetic_thermal_artifact_run", False))


if __name__ == "__main__":
    unittest.main()
