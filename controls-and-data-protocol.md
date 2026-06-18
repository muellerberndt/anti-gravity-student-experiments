# Controls And Data Protocol

## Rule

A force reading is not interpretable until the test article has produced a self-read receipt. The order is:

1. declare the measurement geometry,
2. prove the active device has repeatable drive/read behavior,
3. freeze a machine-readable scorebook,
4. prove `ACTIVE_PLUS` and `ACTIVE_MINUS` produce opposite signed internal contrast,
5. prove `LIVE` separates from waveform-identical `REPLAY` and `SHUFFLED_RECORD`,
6. measure force with the device running from onboard power,
7. reject ordinary artifacts with sham, dummy, flip, thermal, electrostatic, magnetic, pressure, enclosure, and vibration controls.

Geometry declaration:

- Balance mode: top and bottom zones define the vertical support-force scalar.
- Pendulum mode: left/right or A/B zones define a horizontal force axis. Use this for acoustic recoil, artifact mapping, and pot-lid first-light measurements.
- Acoustic bench B0 mode: dish and reflector forces are measured as reaction pairs. A closed fixture should sum close to zero for ordinary acoustic interaction.
- Acoustic bench B0-net mode: dish, reflector, frame, electronics, battery, and enclosure sit on one common weighed platform. Internal acoustic forces should cancel.

## Required States

| State | Role |
| --- | --- |
| `OFF` | Baseline drift and environmental record. |
| `SHAM` | Same average power, heat, RF envelope, and timing as active mode, without the coherent self-read branch. |
| `ACTIVE_PLUS` | Coherent state with predicted positive sign along the declared force axis. |
| `ACTIVE_MINUS` | Same power and timing, reversed sign along the declared force axis. |
| `LIVE` | Next drive packet computed from the latest self-read record. |
| `REPLAY` | Identical prerecorded drive packets with live record updating disabled. |
| `SHUFFLED_RECORD` | Same power and timing while the controller receives block-shuffled or time-shifted records. |
| `FLIP` | Same physical device rotated or inverted so the internal command faces the opposite lab direction. |
| `DUMMY` | Matched artifact witness without a valid coherent self-read branch. |
| `HEATER_ONLY` | Same thermal envelope without resonant drive. |

## Self-Read Receipt

Before any force claim, save:

- port layout and photos,
- firmware hash,
- state schedule,
- declared geometry and force axis,
- frozen `scorebook.json` hash,
- frequency sweep,
- coupling matrix,
- ringdown or phase features,
- repeatability plot,
- shuffled-record prediction control,
- top/bottom or A/B signed contrast,
- dummy comparison,
- `LIVE`, `REPLAY`, and `SHUFFLED_RECORD` comparison.

Minimum pass:

- coupling matrix repeats within preregistered tolerance,
- held-out readouts are predicted better than shuffled records,
- signed contrast reverses between `ACTIVE_PLUS` and `ACTIVE_MINUS`,
- `LIVE` reduces the declared mismatch more than `REPLAY` and `SHUFFLED_RECORD`,
- dummy lacks the same signed contrast.

## Scorebook Lock

Use `templates/scorebook_template.json` as the starting point and freeze a run-specific `scorebook.json` before force data are viewed.

The scorebook must define:

- formulas for record stability, predictive boundary coupling, and coherent mismatch reduction,
- normalization ranges and pass thresholds,
- how ports combine into `S_top` and `S_bottom`,
- sign convention for `S_bottom - S_top`,
- handling of missing, saturated, or out-of-band ports,
- stopping rule for a settled state,
- prediction horizon,
- shuffle or block-shuffle method,
- uncertainty propagation,
- executable verifier and hash.

Discovery data may tune the scorebook. Confirmation data must use the frozen version.

## Exploration And Confirmation

Run two separate phases.

Exploration:

- find resonances, safe power levels, artifact regions, gap regimes, and useful sensor ranges,
- revise hardware and analysis as needed,
- do not use exploration force maxima as a confirmation claim.

Confirmation:

- lock operating point, scalar definition, run length, exclusions, and decision threshold,
- randomize balanced blocks of `ACTIVE_PLUS`, `ACTIVE_MINUS`, `SHAM`, `LIVE`, `REPLAY`, and `SHUFFLED_RECORD`,
- blind force-analysis labels when practical,
- use measured Allan deviation to set run length and sensitivity,
- correct for any search over frequency, gap, phase, surface, or geometry,
- base the candidate claim on an untouched dataset.

## Pendulum Protocol

Use for the piezo-crystal plate when the declared force axis is horizontal.

1. Measure moving mass `m`.
2. Measure pendulum length `L`.
3. Let the device thermally settle.
4. Record camera or laser baseline in `OFF`.
5. Run `SHAM`, `ACTIVE_PLUS`, `ACTIVE_PLUS`, `SHAM`.
6. Run `SHAM`, `ACTIVE_MINUS`, `ACTIVE_MINUS`, `SHAM`.
7. Rotate the device 180 degrees around the vertical suspension axis and repeat.
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

Do not use this as the primary vertical support-force test. Use the balance protocol for the top/bottom PoC described in the Hacking PDF.

Pendulum confirmation requirements:

- bifilar suspension, torsion balance, or two-fiducial camera tracking,
- calibration with known lateral forces at multiple heights,
- calibration with known torques with zero net force,
- acoustic field or momentum-flux map,
- enclosure-geometry variation,
- pressure dependence or reduced-pressure test,
- sealed whole-test-article configuration.

## Balance Protocol

Use for the plate vertical support-force test.

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
8. Include randomized `LIVE`, `REPLAY`, and `SHUFFLED_RECORD` blocks during confirmation.
9. For the direct vertical OPH-style test, invert the complete article 180 degrees about a horizontal axis so top and bottom exchange places in the lab frame.

ABBA estimator:

```text
delta_m_X = mean(X_1, X_2) - mean(SHAM_1, SHAM_2)
F_lift = -g * delta_m_X
```

Use kg for `delta_m_X` when converting to newtons.

## Acoustic Force Protocol

Use for the cymbal or dish rigs.

1. For B0 conventional calibration, keep the driven dish support independent of the reflector plate.
2. Sweep standoff: 0.05, 0.1, 0.2, 0.5, 1, 2, 5 mm for the broad near-field scan if the fixture is safe at those gaps.
3. Add a fine-gap set such as 0.02, 0.05, 0.10, 0.15, and 0.20 mm only with contact-zero, tilt, parallelism, and gap-metrology logs.
4. Add 10, 20, and 30 mm as acoustic leakage or reflector-distance scans.
5. Classify each point as squeeze-film, near-field acoustic, or acoustic leakage.
6. Sweep frequency around resonances.
7. Sweep drive amplitude.
8. Repeat on reflective and lossy surfaces.
9. Record temperature and acceleration at each dish.
10. Record dish-side and reflector-side load cells separately if both are instrumented.
11. Repeat `ACTIVE_PLUS`, `ACTIVE_MINUS`, and `SHAM` at matched power.
12. For B0-net anomaly testing, put dish, reflector, frame, electronics, battery, enclosure, and internal wiring on one common weighed platform.
13. Record slow average force with anti-alias filtering and synchronized high-bandwidth vibration diagnostics.

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
| Force-sensor rectification | kHz vibration aliases into a DC load-cell output | anti-alias filter, high-bandwidth accelerometer, inert vibration-source calibration |
| RF/EMI | drive electronics affect sensors | shielding, dummy electronics, spectrum check if available |
| Center of mass | moving parts or wires shift load | solid-state switching, no relays, pan-position test |
| Human handling | order and expectation bias | preregistered schedule, blind labels where possible |

## Decision Rules

Development signal:

- a repeatable force or deflection appears in one configuration.

Candidate residual:

- signal tracks the measured self-read scalar,
- `LIVE` separates from `REPLAY` and `SHUFFLED_RECORD`,
- `ACTIVE_MINUS` reverses sign,
- horizontal-axis physical inversion reverses the direct vertical test in lab coordinates,
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
  scorebook.json
  geometry.md
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
