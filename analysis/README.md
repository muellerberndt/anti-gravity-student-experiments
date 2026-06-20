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
- `factorial_force_model.py`: estimates the locked `K_live - K_replay` interaction from `q * delta_S_hat`.
- `run_synthetic_tests.py`: checks one valid synthetic run and two failing synthetic runs.

The verifier fails confirmation runs when required manifest fields are blank, `OPEN_LOOP_REPLAY` differs from the referenced `LIVE` packet, `YOKED_SHUFFLE_REPLAY` differs from the referenced `CAUSAL_SHUFFLE` packet, the proxy scalar table fails, exploration and confirmation data share a path, or ordinary artifact limits are exceeded.
