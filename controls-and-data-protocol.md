# Controls And Data Protocol

## Rule

A force reading is not interpretable until the test article has produced a self-read receipt. The order is:

1. prove the active device has repeatable drive/read behavior,
2. prove `ACTIVE_PLUS` and `ACTIVE_MINUS` produce opposite signed internal contrast,
3. measure force with the device running from onboard power,
4. reject ordinary artifacts with sham, dummy, flip, thermal, electrostatic, magnetic, and vibration controls.

## Required States

| State | Role |
| --- | --- |
| `OFF` | Baseline drift and environmental record. |
| `SHAM` | Same average power, heat, RF envelope, and timing as active mode, without the coherent self-read branch. |
| `ACTIVE_PLUS` | Coherent state with predicted positive sign along the declared force axis. |
| `ACTIVE_MINUS` | Same power and timing, reversed sign along the declared force axis. |
| `FLIP` | Same physical device rotated or inverted so the internal command faces the opposite lab direction. |
| `DUMMY` | Matched artifact witness without a valid coherent self-read branch. |
| `HEATER_ONLY` | Same thermal envelope without resonant drive. |

## Self-Read Receipt

Before any force claim, save:

- port layout and photos,
- firmware hash,
- state schedule,
- frequency sweep,
- coupling matrix,
- ringdown or phase features,
- repeatability plot,
- shuffled-record prediction control,
- top/bottom or A/B signed contrast,
- dummy comparison.

Minimum pass:

- coupling matrix repeats within preregistered tolerance,
- held-out readouts are predicted better than shuffled records,
- signed contrast reverses between `ACTIVE_PLUS` and `ACTIVE_MINUS`,
- dummy lacks the same signed contrast.

## Pendulum Protocol

Use for the piezo-crystal plate.

1. Measure moving mass `m`.
2. Measure pendulum length `L`.
3. Let the device thermally settle.
4. Record camera or laser baseline in `OFF`.
5. Run `SHAM`, `ACTIVE_PLUS`, `ACTIVE_PLUS`, `SHAM`.
6. Run `SHAM`, `ACTIVE_MINUS`, `ACTIVE_MINUS`, `SHAM`.
7. Rotate the device 180 degrees and repeat.
8. Run the dummy with the same schedule.
9. Run heater-only or resistor-only at the same average power.

Direct camera force:

```text
F = m * g * x / L
```

Laser mirror force:

```text
F = m * g * s / (2 * D)
```

where `x` is bob displacement, `s` is laser spot displacement, and `D` is mirror-to-screen distance.

## Balance Protocol

Use for the plate if a 0.1 mg or 1 mg balance is available.

1. Put the balance on stone or an anti-vibration table.
2. Close the draft shield.
3. Calibrate with known masses.
4. Run only battery-powered devices on the pan. No USB, power, or ground cable.
5. Use same-object ABBA blocks:

```text
SHAM_1, ACTIVE_PLUS_1, ACTIVE_PLUS_2, SHAM_2
SHAM_1, ACTIVE_MINUS_1, ACTIVE_MINUS_2, SHAM_2
```

6. Discard the preregistered settling interval from every state.
7. Save raw balance CSV, not only screenshots.

ABBA estimator:

```text
delta_m_X = mean(X_1, X_2) - mean(SHAM_1, SHAM_2)
F_lift = -g * delta_m_X
```

## Acoustic Force Protocol

Use for the cymbal or dish rigs.

1. Keep the driven dish support independent of the ground-plate load cell.
2. Sweep standoff: 0.5, 1, 2, 5, 10, 20, 30 mm.
3. Sweep frequency around resonances.
4. Sweep drive amplitude.
5. Repeat on reflective and lossy surfaces.
6. Record temperature and acceleration at each dish.
7. Repeat `ACTIVE_PLUS`, `ACTIVE_MINUS`, and `SHAM` at matched power.

Conventional acoustic force should change with standoff, surface, resonance, and drive amplitude. A residual that ignores those variables needs extra scrutiny, then flip and dummy tests.

## Artifact Table

| Artifact | Mechanism | Required control |
| --- | --- | --- |
| Air currents | heating drives convection | closed shield, thermal settling, heater-only run |
| Buoyancy | density change near device | temperature log, matched dummy, regression against temperature |
| Thermal radiation | asymmetric heating of pan or shield | emissivity match, IR check, same-power sham |
| Electrostatics | charged surfaces pull on pan or frame | discharge protocol, Faraday shield, handling log |
| Magnetics | currents or steel parts couple to environment | nonmagnetic fixtures, magnetometer log, rotation test |
| Cable forces | wires act as springs | onboard battery and logging, no cables during force run |
| Acoustic leakage | sound pushes air or nearby surfaces | enclosure, microphone/accelerometer log, standoff map |
| Vibration | mechanical coupling into supports | anti-vibration table, accelerometer log, dummy |
| RF/EMI | drive electronics affect sensors | shielding, dummy electronics, spectrum check if available |
| Center of mass | moving parts or wires shift load | solid-state switching, no relays, pan-position test |
| Human handling | order and expectation bias | preregistered schedule, blind labels where possible |

## Decision Rules

Development signal:

- a repeatable force or deflection appears in one configuration.

Candidate residual:

- signal tracks the measured self-read scalar,
- `ACTIVE_MINUS` reverses sign,
- physical flip reverses sign in lab coordinates,
- dummy and sham reject the signal,
- temperature, battery, acoustic leakage, vibration, electrostatic, and magnetic logs do not explain it.

Publishable upper bound:

- no candidate residual,
- force sensitivity and artifact controls are documented,
- raw logs and analysis scripts are included,
- the null is stated as a bound for that hardware, not as a universal disproof.

## Evidence Bundle

Save one directory per run:

```text
run_id/
  manifest.yaml
  firmware/
  photos/
  raw/
    balance.csv
    pendulum_position.csv
    load_cell.csv
    device_log.csv
    environment.csv
  analysis/
    analysis_script.py
    frozen_config.yaml
    plots/
    summary.md
  hashes.txt
```

The result lives in the bundle. A video without the bundle is outreach, not evidence.
