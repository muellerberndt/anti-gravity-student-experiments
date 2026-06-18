# Analysis Verifier

This folder contains the executable receipt checks for confirmation runs.

Main command:

```bash
python analysis/verify_scorebook.py --manifest manifest.yaml --scorebook scorebook.json --data raw/device_log.csv --confirmation
```

Useful helpers:

- `compute_self_read_scalar.py`: recomputes the top/bottom scalar table from packet logs.
- `analyze_abba_balance.py`: computes the simple ABBA balance estimate.
- `allan_deviation.py`: computes non-overlapping Allan deviation for a numeric CSV column.
- `run_synthetic_tests.py`: checks one valid synthetic run and two failing synthetic runs.

The verifier fails confirmation runs when required manifest fields are blank, `REPLAY` is not waveform-identical to the referenced `LIVE` packet, the scalar table fails, exploration and confirmation data share a path, or ordinary artifact limits are exceeded.
