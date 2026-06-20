# Build 02: Acoustic Cymbal Bench Rig

## Purpose

This is the larger student build. It should be run as a bench force platform, with no rider and no free-flight claim.

The rig uses cymbals, pot lids, stainless bowls, or similar thin metal dishes as resonant acoustic radiators. Piezo or Langevin transducers drive the dishes. The students map conventional near-field acoustic force first, then use the same apparatus as a larger coherent-body test article.

The OPH purpose is the same as the small plate: instantiate an observer-like
self-reading article. The rig needs bounded geometry, top and bottom read
zones, records, live feedback, and scorebook receipts before any residual-force
discussion is OPH-style rather than conventional acoustics.

Primary goal:

Measure force versus frequency, phase, drive amplitude, and standoff distance, then test whether a sign-reversible coherent state produces any residual in a closed weighed article.

The included cymbal hoverboard source is useful for geometry and first-light drive ideas, but its human-carrying lift claim is not adopted here. The included antigravity survey corrects that claim and treats the pot-lid result as small bench-scale conventional acoustic force.

The three-transducer dish layout is a useful acoustic radiator. By itself, it is not a vertical OPH proxy scalar. Any OPH-style stage needs separately instrumented upper and lower zones, independent `S_hat_top` and `S_hat_bottom` estimates, and live record-conditioned feedback.

It also needs a declared P integration. `P ~= 1.6309682` is not a force
coefficient for the cymbal rig. It is a geometry/readback tuning target: the
students must state which dimensionless dish, standoff, port-spacing,
top/bottom-zone, or `K_port` coupling ratio is held near `P`, how it is
measured, and which detuned geometry tests the same mass and power path without
that ratio. Without that declaration, the rig is not inside the student
hardware spec.

Student model:

- A dish or cymbal acts like a loud mechanical speaker.
- Close to a reflector, it can push on air in the gap and create ordinary measurable force.
- In B0, the dish and reflector are measured separately so students can learn the ordinary acoustic force.
- In B0-net, the dish, reflector, frame, electronics, battery, and enclosure sit on one common force sensor. Ordinary internal push-pull forces should cancel in that whole-object reading.
- Any OPH-style test starts only after the rig has top and bottom self-read zones and passes the same live, replay, dummy, and flip controls as the small plate.

## Build Stages

### Stage B0: Conventional Single-Dish Calibration Station

Build this before the four-dish platform.

| Item | First build target |
| --- | --- |
| Dish | 200 mm aluminum pot lid, stainless bowl, or small cymbal |
| Transducers | 3 to 12 piezo discs or bolt-on transducers |
| Layout | Ring at about 60 percent radius |
| Drive | Phase-locked channels from one MCU |
| Measurement | Driven dish on its own load cell or overhead force gauge, above an independent reflector |
| Standoff | 0.05 to 5 mm for broad scans. 0.02 to 0.2 mm for true squeeze-film studies only with fine-gap metrology |
| Output | Force curves and resonance maps |

Correct measurement geometry:

- The driven dish is supported by an overhead force gauge, a dish-side load cell, or a frame independent of the reflector plate.
- The reflector plate sits on its own support or on a separate load cell if the equal-and-opposite reaction is also being measured.
- Do not put both dish and reflector plate on the same scale for B0 conventional calibration. Internal action and reaction forces cancel in that reading.
- Report dish-side force and reflector-side force separately. Their sum should be close to zero for ordinary acoustic interaction inside one closed bench fixture.

### Stage B0-net: Closed-System Force Test

Use this geometry after B0 characterizes the ordinary acoustic interaction.

| Item | First build target |
| --- | --- |
| Weighed boundary | dish, reflector, frame, electronics, battery, enclosure, and internal wiring on one common weighing platform |
| External contacts | only balance supports or load-cell supports |
| Power | onboard battery during force blocks |
| Readout | slow average balance or load-cell channel plus synchronized acceleration monitoring |
| Purpose | test whether the complete bounded article has a net external force |

Ordinary acoustic forces between dish and reflector should cancel inside the weighed boundary. A residual claim belongs in B0-net, not in the subtraction of two large B0 conventional forces.

Keep this rule absolute. Subtracting two large conventional acoustic force readings can create a small difference through sensor phase lag, alignment, gap drift, thermal drift, or calibration mismatch. A real net external force should be visible on the whole bounded article.

B0-net also needs a sealed or well-characterized acoustic boundary. If sound, airflow, or vibration leaves the fixture and pushes on the room, the room becomes the reaction mass. Log external microphones or accelerometers and run an open/closed enclosure comparison.

### Stage B1: Four-Dish Bench Platform

Build this after B0 is stable.

| Item | First build target |
| --- | --- |
| Dishes | 4 x 200 to 300 mm stainless bowls or pot lids |
| Optional larger dishes | 4 x 400 to 510 mm cymbals for later bench work |
| Transducers | 3 per dish, 12 total |
| Placement | 120 degrees apart, about 60 percent radius |
| Orientation | Bell or convex focus downward, aimed at reflector plate |
| Frame | Square frame, 600 to 800 mm side length for large dishes, smaller for bowls |
| Tilt | 0 degrees for pure vertical force maps. Optional 10 to 15 degrees outward for steering studies |
| Drive | 12 phase-locked channels |
| Measurement | B0 conventional: overhead load cells, corner load cells, or separate reflector load cells. B0-net: all hardware on one common weighed platform |
| Test surface | Smooth glass, polished aluminum, or polished concrete |

Expected conventional force:

- milligram-force to gram-force class for a first student pot-lid or bowl fixture,
- possibly larger sub-newton force only with a well-coupled squeeze-film geometry and suitable actuators,
- no expectation of human-scale lift.

## Bill Of Materials

Single-dish calibration:

- 1 aluminum pot lid, stainless mixing bowl, or cymbal.
- 3 to 12 piezo or Langevin transducers. Start with lower-power parts.
- M3 or M4 bolts, washers, and rubber gaskets if using bolt-on transducers.
- RP2040/RP2350/Teensy/ESP32-class controller.
- 3 to 12 class-D amplifier channels or MOSFET drive channels.
- Current-limited DC supply for bench calibration.
- Pickup piezo or accelerometer on the dish.
- Load cell plus HX711 or better ADC, or a lab scale with serial logging.
- Adjustable standoff fixture with micrometer, screw jack, or spacer set. Include thin shims for 0.05 to 1 mm gaps.
- Fine-gap stage, contact-zero method, and three-point or full-field gap measurement if claiming squeeze-film behavior below 0.2 mm.
- Acrylic shield or other fragment guard.
- Remote kill switch.
- Hearing protection.

Four-dish platform:

- 4 matching dishes.
- 12 transducers.
- Lightweight nonmagnetic frame.
- 12 drive channels, current-limited.
- MCU with phase-locked waveform generation.
- Per-dish pickup sensor or accelerometer.
- Battery pack for later self-contained runs.
- Temperature sensors on transducers and dishes.
- Load cells at support points or a separate reflector reaction measurement.
- Shielding, remote kill switch, and acoustic enclosure if available.

## Mechanical Build

1. Mark each dish at 60 percent radius.
2. Place three transducers 120 degrees apart on each dish.
3. Avoid the rim and exact center. The rim is fragile and the center is a poor first location for many modes.
4. If drilling thin metal, use a center punch and step drill. Clamp the dish gently to avoid deformation.
5. Use rubber gaskets for bolt holes where acoustic sealing matters.
6. Route wires along the dish and frame. Strain-relieve every cable.
7. Add a pickup piezo or accelerometer to each dish. Add vertically separated or face-separated sensors if the run claims `S_hat_top` and `S_hat_bottom`.
8. Put a temperature sensor near at least one transducer per dish.
9. Build the standoff fixture so the gap to the reflector plate can be set repeatably. The squeeze-film scan needs sub-millimeter control.
10. Measure dish mode shape before permanent transducer placement. Keep the 60 percent radius placement removable until a nodal map confirms it is useful for the chosen mode.
11. Add tilt and parallelism monitoring for the dish and reflector.
12. Add a transparent shield before high-amplitude sweeps.
13. Log bolt torque, preload, adhesive batch, adhesive mass, cure time, adhesive thickness, piezo capacitance before testing, and piezo capacitance after testing.
14. Record pre-test and post-test modal frequencies, Q estimates, and permanent center displacement.
15. Invalidate the run series after cymbal deformation, modal jump, solder failure, or transducer temperature above the declared limit.

## Drive Architecture

Minimum:

- one MCU generates phase-locked PWM or DAC waveforms,
- one amplifier channel per transducer,
- one pickup sensor per dish,
- frequency sweep and resonance-lock mode,
- fixed state schedules written to the log.

One pickup sensor per dish is conventional-only. It is fine for resonance locking and acoustic mapping. It is not enough for an OPH top/bottom scalar. In the manifest, use:

```yaml
geometry:
  mode: acoustic_B0
  zone_definition: none
  oph_vertical_scalar_claim: false
  p_target_status: p_integrated
  p_target_value: 1.6309682
  p_geometry_ratio: dish_port_ring_radius_mm / dish_active_radius_mm
  p_detuned_control_id: dish_port_ring_detuned_control
```

Change `oph_vertical_scalar_claim` to `true` only after the article has real upper/lower instrumented zones and an accepted scorebook.
Keep `p_target_status: p_integrated` for B0 and B0-net. A B0 run may still be
conventional-only in its strongest claim, but the device geometry must already
declare the P-coded ratio, measured value, tolerance, geometry file, and detuned
control before force data are viewed.

Drive states:

| State | Behavior |
| --- | --- |
| `OFF` | No drive. Sensors and logger only. |
| `SHAM` | Same average power, incoherent or phase-scrambled drive. |
| `ACTIVE_PLUS` | Coherent multichord drive with intended sign. |
| `ACTIVE_MINUS` | Same power, reversed phase gradient or dish zoning. |
| `LIVE` | Next drive packet computed from the latest self-read record. |
| `OPEN_LOOP_REPLAY` | Exact packet sequence from a named `LIVE` run, with current records measured and ignored. |
| `CAUSAL_SHUFFLE` | Block-shuffled or time-shifted records feed the controller, so the generated packet sequence may change. |
| `YOKED_SHUFFLE_REPLAY` | Exact packet sequence from a named `CAUSAL_SHUFFLE` run, replayed open-loop. |
| `DUMMY` | Matched non-coherent dish or mechanically damped dish. |

Start with one frequency at a time. Add multichord drive only after the single-frequency force curves are understood.

Drive calibration:

- measure terminal voltage and current on every channel,
- measure transducer capacitance after mounting,
- keep driver current below `I_rms ~= 2 * pi * f * C * V_rms`,
- calibrate channel phase at the transducer terminals,
- use filtered sine drive or log complete voltage, current, acceleration, and acoustic spectra during confirmation,
- make `SHAM` match RMS voltage, RMS current, real power, reactive power, harmonics, battery waveform, temperature, RF/logging activity, acoustic spectrum, and momentum direction as closely as the hardware allows.

Force readout:

- HX711-class ADCs are suitable only for slow average force channels.
- Add an analog anti-alias filter before a slow force ADC.
- Use a synchronized accelerometer or dynamic force sensor to measure kHz vibration and frame rectification.
- Run inert vibration-source calibrations to learn how the load cell and frame turn vibration into DC offsets.

## Measurement Plan

### Conventional Acoustic Force Map

For each dish:

1. Set standoff distance: 0.05, 0.1, 0.2, 0.5, 1, 2, and 5 mm for the broad near-field scan if the fixture can do this safely.
2. Add 10, 20, and 30 mm only as a reflector-distance or acoustic-leakage scan.
3. For true squeeze-film claims, add a fine-gap set such as 0.02, 0.05, 0.10, 0.15, and 0.20 mm with contact-zero, tilt, parallelism logs, and direct displacement measurement.
4. Classify each point as squeeze-film, near-field acoustic, or acoustic leakage using gap, frequency, radiator amplitude, and geometry.
5. Sweep frequency around measured resonances.
6. Sweep drive amplitude at fixed frequency.
7. Record dish acceleration, transducer temperature, load-cell force, supply voltage, current, and acoustic level if available.
8. Repeat on different surfaces: glass, aluminum, polished concrete, and a lossy surface such as foam or carpet.
9. For quantitative squeeze-film claims, record LDV, scanning vibrometry, or a calibrated displacement-sensor trace, three-point gap measurement, pre/post modal fingerprint, cool-down period, gap uncertainty, tilt uncertainty, displacement uncertainty, force-versus-pressure scaling, and force-versus-gap scaling.
10. Use shorter force windows and declared cool-down periods when fine-gap heating moves resonance or load-cell zero during a block. Do not use a universal 60-second stable window for high-power fine-gap work.
11. Invalidate later runs after a modal jump, plastic deformation, solder failure, or permanent center displacement.

Expected conventional signatures:

- force changes sharply with sub-millimeter standoff for squeeze-film coupling,
- force peaks at resonances,
- force grows with drive amplitude,
- force weakens on lossy surfaces,
- force follows thermal and acoustic leakage when artifacts dominate.

### Four-Dish Platform Map

After each dish has a force curve:

1. Drive all four dishes with the same amplitude and phase pattern.
2. Measure the dish-frame vertical reaction and, if instrumented, the reflector reaction.
3. Drive one dish at a time to calibrate corner contributions.
4. Test phase patterns that should cancel lateral components.
5. Test differential drive only as a lateral-force measurement.
6. Compare `ACTIVE_PLUS`, `ACTIVE_MINUS`, and `SHAM` at matched average power.

### OPH-Style Vertical Scalar Test

Use this only after the conventional maps are reproducible.

1. Add two physical vertical zones to the article: upper and lower dish layers, face-separated sensors, or another geometry that gives independent upper and lower records.
2. Freeze `scorebook.json` with formulas for `S_hat_top`, `S_hat_bottom`, proxy pass thresholds, exclusions, surrogate method, and uncertainty propagation.
3. Demonstrate a signed `S_hat_bottom - S_hat_top` that reverses between `ACTIVE_PLUS` and `ACTIVE_MINUS`.
4. Run `LIVE`, `OPEN_LOOP_REPLAY`, `CAUSAL_SHUFFLE`, and `YOKED_SHUFFLE_REPLAY` at matched power and timing where the replay states point to named source runs.
5. Move to B0-net only after the scalar and live ablation pass.
6. Do not use B0 subtraction as an anomaly estimate. The candidate force test is the whole B0-net article on one weighed platform.
7. Use separate scorebooks for conventional B0/NFAL mapping, B0-net residual testing, and optional OPH self-read force testing.

## Claim Boundary

This rig can demonstrate conventional near-field acoustic force. That measurement is a valid student result.

A human-carrying hoverboard is outside scope. The source material itself contains a correction: human-scale free-air acoustic hover is blocked by acoustic intensity, wavelength, and safety limits, and the realistic cymbal/pot-lid first-light result is small bench-scale deflection. The bench should not be presented as a scaled-down working hoverboard.

Treat any residual force claim as provisional until:

- the conventional force map is complete,
- the frozen scorebook passes on self-read data,
- `LIVE` separates from `OPEN_LOOP_REPLAY` and `YOKED_SHUFFLE_REPLAY`,
- the residual survives standoff changes,
- the residual reverses with `ACTIVE_MINUS`,
- the residual reverses under horizontal-axis physical inversion of the top/bottom article,
- the matched dummy rejects it,
- thermal, electrostatic, magnetic, acoustic, and vibration artifacts are rejected.

Expected result:

The expected student result is a resonance map, a conventional acoustic force or upper bound, and a clear artifact ledger. A positive residual is not expected.

## Safety

- No rider, no standing on the platform, no hands between dish and reflector plate.
- Start at low power and short duty cycles.
- Keep a hard kill switch within reach.
- Use hearing protection. Harmonics can be loud even when the drive frequency seems harmless.
- Shield the rig. Cymbals, bowls, and piezos can crack under overdrive.
- Never sand, drill, grind, or cut PZT. Discard cracked piezo parts in a sealed labeled container.
- Wash hands after handling PZT. Keep food and drink away from the bench.
- Clean ceramic fragments with wet methods or a suitable HEPA procedure. Do not use compressed air.
- Stop if any transducer reaches 60 C.
- Use current-limited supplies.
- Do not run high-amplitude tests near loose objects, dust, paper, or uncovered sensors.
- Treat sub-millimeter gaps as pinch and fracture hazards.
- Log every crack, deformation, desoldered joint, or temperature excursion.

## Student Deliverables

- Single-dish force curves.
- Resonance map for each dish.
- Standoff-force map.
- Surface-dependence map.
- Four-dish reaction-force curve.
- Raw logs and analysis scripts.
- Safety log.
- Residual or upper-bound report.
