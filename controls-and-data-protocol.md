# Controls And Data Protocol

## Rule

A force reading is not interpretable until the test article has produced a self-read receipt. The order is:

1. declare the measurement geometry,
2. prove the active device has repeatable drive/read behavior,
3. freeze a machine-readable scorebook,
4. prove `ACTIVE_PLUS` and `ACTIVE_MINUS` produce opposite signed internal contrast,
5. prove `LIVE` separates from `OPEN_LOOP_REPLAY` and `YOKED_SHUFFLE_REPLAY`, with `CAUSAL_SHUFFLE` testing the temporal record relation,
6. run the executable verifier on the manifest, scorebook, and packet log,
7. measure force with the device running from onboard power,
8. reject ordinary artifacts with sham, dummy, active twin, flip, thermal, electrostatic, magnetic, pressure, enclosure, and vibration controls.

Geometry declaration:

- Balance mode: top and bottom zones define the vertical support-force scalar.
- Pendulum mode: left/right or A/B zones define a horizontal force axis. Use this for acoustic recoil, artifact mapping, and pot-lid first-light measurements.
- Acoustic bench B0 mode: dish and reflector forces are measured as reaction pairs. A closed fixture should sum close to zero for ordinary acoustic interaction.
- Acoustic bench B0-net mode: dish, reflector, frame, electronics, battery, and enclosure sit on one common weighed platform. Internal acoustic forces should cancel.
- Acoustic B0 subtraction is not an anomaly estimate. A residual claim belongs in B0-net.

Student translation:

- A geometry declaration tells the reader which direction the experiment is testing.
- A self-read receipt proves that the device drove itself, listened to itself, stored the record, and used that record in the live controller.
- A sham keeps power and heat similar while removing the coherent self-read pattern.
- A dummy keeps mass, electronics, heat, and handling similar while removing the valid mechanical branch.
- A replay asks whether the same electrical waveform produces the same force when live record use is removed.
- A physical flip asks whether the sign follows the device's internal top/bottom direction rather than the room, the balance pan, or a cable path.

## Required States

| State | Role |
| --- | --- |
| `OFF` | Baseline drift and environmental record. |
| `SHAM` | Same average power, heat, RF envelope, and timing as active mode, without the coherent self-read branch. |
| `ACTIVE_PLUS` | Coherent state with predicted positive sign along the declared force axis. |
| `ACTIVE_MINUS` | Same power and timing, reversed sign along the declared force axis. |
| `LIVE` | Next drive packet computed from the latest self-read record. |
| `OPEN_LOOP_REPLAY` | Exact packet sequence from a named `LIVE` run, with current records measured and ignored. |
| `CAUSAL_SHUFFLE` | Block-shuffled or time-shifted records feed the controller, so the generated packet sequence may change. |
| `YOKED_SHUFFLE_REPLAY` | Exact packet sequence from a named `CAUSAL_SHUFFLE` run, replayed open-loop. |
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
- executable verifier hash,
- frequency sweep,
- coupling matrix,
- ringdown or phase features,
- repeatability plot,
- surrogate-record prediction control,
- top/bottom or A/B signed contrast,
- dummy comparison,
- `LIVE`, `OPEN_LOOP_REPLAY`, `CAUSAL_SHUFFLE`, and `YOKED_SHUFFLE_REPLAY` comparison.

Packet-level evidence:

- `drive_packet_hash`,
- `drive_vector_json_sha256`,
- `record_packet_hash`,
- `feedback_input_hash`,
- `terminal_voltage_trace_hash`,
- `terminal_current_trace_hash`,
- `mismatch_before`,
- `mismatch_after`,
- `live_update_accepted`,
- `replay_source_run_id`,
- `shuffle_seed`.
- `timing_hash`.

`OPEN_LOOP_REPLAY` must match the referenced `LIVE` packet at the electrical terminals. `YOKED_SHUFFLE_REPLAY` must match the referenced `CAUSAL_SHUFFLE` packet. Same script is not enough.

Minimum pass:

- coupling matrix repeats within preregistered tolerance,
- held-out readouts are predicted better than surrogate records that preserve autocorrelation while breaking causal alignment,
- signed contrast reverses between `ACTIVE_PLUS` and `ACTIVE_MINUS`,
- `LIVE` reduces the declared mismatch more than `OPEN_LOOP_REPLAY` and `YOKED_SHUFFLE_REPLAY`,
- dummy lacks the same signed contrast.

## Scorebook Lock

Use `templates/scorebook_template.json` as the starting point and freeze a run-specific `scorebook.json` before force data are viewed.

The scorebook must define:

- formulas for record stability, predictive boundary coupling, and coherent mismatch reduction,
- normalization ranges and pass thresholds,
- how ports combine into `S_hat_top` and `S_hat_bottom`,
- sign convention for `S_hat_bottom - S_hat_top`,
- handling of missing, saturated, or out-of-band ports,
- stopping rule for a settled state,
- prediction horizon,
- surrogate generation method,
- uncertainty propagation,
- executable verifier and hash.

The scorebook scalar is operational. It is `delta_S_hat`, not the canonical `delta_S_can` in the force law. `delta_S_hat` can classify a state and support an empirical coefficient `K_S_hat = F_residual / (q * delta_S_hat)`. It does not measure or bound canonical `chi_can` unless a public bridge `delta_S_can = kappa_S * delta_S_hat` is supplied.

For students: treat `delta_S_hat` like a lab score, not a fundamental constant. It says how strongly the logged device looks bottom-dominant or top-dominant under the frozen rules. A balance signal only becomes interesting if it follows that score and fails the ordinary-artifact checks.

Discovery data may tune the scorebook. Confirmation data must use the frozen version.

Run the verifier:

```bash
python analysis/verify_scorebook.py --manifest manifest.yaml --scorebook scorebook.json --data raw/device_log.csv --confirmation
```

The verifier must fail if confirmation-critical manifest fields are blank, if packet hashes do not prove waveform identity, if the scalar table cannot be recomputed from raw logs, or if ordinary artifact limits are exceeded.

## Exploration And Confirmation

Run two separate phases.

Exploration:

- find resonances, safe power levels, artifact regions, gap regimes, and useful sensor ranges,
- revise hardware and analysis as needed,
- do not use exploration force maxima as a confirmation claim.

Confirmation:

- lock operating point, scalar definition, run length, exclusions, and decision threshold,
- randomize balanced blocks of `ACTIVE_PLUS`, `ACTIVE_MINUS`, `SHAM`, `LIVE`, `OPEN_LOOP_REPLAY`, `CAUSAL_SHUFFLE`, and `YOKED_SHUFFLE_REPLAY`,
- blind force-analysis labels when practical,
- use measured Allan deviation to set run length and sensitivity,
- correct for any search over frequency, gap, phase, surface, or geometry,
- base the candidate claim on an untouched dataset.

Keep the file paths separate:

```text
runs/
  exploration/
  confirmation/
    locked_scorebook_hash_<hash>/
      run_001/
```

The verifier refuses a candidate claim from a confirmation path that contains exploration data.

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
F = m * g0 * x / L
```

Laser mirror force:

```text
F = m * g0 * s / (2 * D)
```

where `x` is bob displacement, `s` is laser spot displacement, and `D` is mirror-to-screen distance.

Do not use this as the primary vertical support-force test. Use the balance protocol for the top/bottom PoC described in the Hacking PDF.

A positive pendulum-only result is labeled development signal or conventional artifact lead. It is not a candidate OPH residual unless all pendulum confirmation requirements below pass.

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
8. Include randomized `LIVE`, `OPEN_LOOP_REPLAY`, `CAUSAL_SHUFFLE`, and `YOKED_SHUFFLE_REPLAY` blocks during confirmation.
9. For the direct vertical OPH-style test, invert the complete article 180 degrees about a horizontal axis so top and bottom exchange places in the lab frame.
10. Run both an electrical dummy and a mechanical active twin for confirmation.
11. Run inert-shaker balance rectification calibration with the same measured acceleration spectrum, amplitude, frequency, modulation, duty cycle, and pan positions.
12. Use a no-touch kinematic cradle or gimbal for inversion when feasible.
13. Repeat candidate settings across two mounting topologies and two pan positions.

ABBA estimator:

```text
delta_m_X = mean(X_1, X_2) - mean(SHAM_1, SHAM_2)
F_lift = -g0 * delta_m_X
```

Use kg for `delta_m_X` when converting to newtons.

Primary confirmation statistic:

```text
F_t = beta0
    + K_live * L_t * q_t * delta_S_hat_t
    + K_replay * (1 - L_t) * q_t * delta_S_hat_t
    + gamma^T X_t
    + block_effect
    + epsilon_t
```

The preregistered contrast is `K_live - K_replay`. `X_t` includes temperature, `dT/dt`, terminal power, vibration, acoustic level, magnetic field, electrostatic potential if measured, battery state, and time drift. A candidate needs the correct sign, a nonzero `LIVE` interaction, no comparable replay interaction, no comparable dummy interaction, and size above the measured systematic floor.

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
14. Add external microphones or accelerometers and compare open versus closed enclosure when sound, airflow, or vibration can leave the weighed boundary.
15. Treat B0 as a force-closure budget across dish, reflector, frame, contained air, and supports. Do not reduce it to a two-number subtraction.

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
| Feedback waveform artifact | `LIVE` differs electrically from `OPEN_LOOP_REPLAY` | packet hashes, terminal voltage/current trace hashes, replay source links |
| RF/EMI | drive electronics affect sensors | shielding, dummy electronics, spectrum check if available |
| Center of mass | moving parts or wires shift load | solid-state switching, no relays, pan-position test |
| Human handling | order and expectation bias | preregistered schedule, blind labels where possible |

## Decision Rules

Development signal:

- a repeatable force or deflection appears in one configuration.

Candidate residual:

- signal tracks the measured self-read scalar,
- `LIVE` separates from `OPEN_LOOP_REPLAY` and `YOKED_SHUFFLE_REPLAY`,
- `ACTIVE_MINUS` reverses sign,
- horizontal-axis physical inversion reverses the direct vertical test in lab coordinates,
- dummy, active twin, and sham reject the signal,
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
    scalar_table.json
    verifier_output.json
    plots/
    summary.md
  hashes.txt
```

The result lives in the bundle. A video without the bundle is outreach, not evidence.
