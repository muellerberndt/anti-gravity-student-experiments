# Build 02: Acoustic Cymbal Bench Rig

## Purpose

This is the larger student build. It should be run as a bench force platform, with no rider and no free-flight claim.

The rig uses cymbals, pot lids, stainless bowls, or similar thin metal dishes
as resonant acoustic radiators. Piezo or Langevin transducers drive the dishes.
The students map conventional near-field acoustic force first, then use the same
apparatus as a larger coherent-body test article.

The OPH purpose is the same as the small plate: build an observer-like
self-reading article. The rig needs bounded geometry, top and bottom read zones,
records, live feedback, and scorebook receipts before residual-force discussion
uses OPH language.

Primary goal:

Measure force versus frequency, phase, drive amplitude, and standoff distance, then test whether a sign-reversible coherent state produces any residual in a closed weighed article.

The included cymbal hoverboard source is useful for geometry and first-light
drive ideas. The included antigravity survey treats the pot-lid result as small
bench-scale conventional acoustic force.

The three-transducer dish layout is a useful acoustic radiator. The OPH stage
adds separately instrumented upper and lower zones, independent `S_hat_top` and
`S_hat_bottom` estimates, and live record-conditioned feedback.

`P ~= 1.6309682` gives the cymbal rig its OPH geometry ruler. Students record
which dimensionless dish, standoff, port-spacing, top/bottom-zone, or `K_port`
coupling ratio is held near `P`, how it is measured, and which detuned geometry
tests the same mass and power path with the ratio shifted.

Use this default encoding unless the supervisor approves a written replacement:

```text
R_P = dish_active_radius_mm / transducer_ring_radius_mm
target: R_P = 1.6309682
confirmation tolerance: <= 1.0 percent
```

Measure `dish_active_radius_mm` from the dish center to the usable driven
radius or marked acoustic boundary. Place the transducer ring at:

```text
transducer_ring_radius_mm = dish_active_radius_mm / 1.6309682
```

Examples:

| Dish active diameter | Active radius | P-coded transducer ring radius |
| --- | --- | --- |
| 200.00 mm | 100.00 mm | 61.31 mm |
| 240.00 mm | 120.00 mm | 73.58 mm |
| 300.00 mm | 150.00 mm | 91.97 mm |

For the default detuned control, keep the same dish type, transducers,
electronics, power envelope, and logging, but use:

```text
R_detuned = dish_active_radius_mm / transducer_ring_radius_mm = 1.50
```

On a 200 mm active dish, that puts the detuned ring at 66.67 mm radius. The
detuned ratio must be at least 5 percent away from `P`.

Student model:

- A dish or cymbal acts like a loud mechanical speaker.
- Close to a reflector, it can push on air in the gap and create ordinary measurable force.
- In B0, the dish and reflector are measured separately so students can learn the ordinary acoustic force.
- In B0-net, the dish, reflector, frame, electronics, battery, and enclosure sit on one common force sensor. Ordinary internal push-pull forces should cancel in that whole-object reading.
- Any OPH-style test starts only after the rig has top and bottom self-read zones and passes the same live, replay, dummy, and flip controls as the small plate.

Physics intuition:

A dish works like a shallow bell. The center, rim, and transducer ring move with
different phases depending on frequency. Close to a reflector, the air gap acts
like a spring and pump. Small changes in gap can create large changes in force,
especially below one millimeter. This is useful because it gives students a
strong conventional signal to calibrate. It is also why B0-net weighs the whole
bounded article when looking for a residual.

## Build Stages

### Stage B0: Conventional Single-Dish Calibration Station

Build this before the four-dish platform.

| Item | First build target |
| --- | --- |
| Dish | 200 mm aluminum pot lid, stainless bowl, or small cymbal |
| Transducers | 3 to 12 piezo discs or bolt-on transducers |
| Layout | Ring at `dish_active_radius / P`, about 61.31 percent radius |
| Drive | Phase-locked channels from one MCU |
| Measurement | Driven dish on its own load cell or overhead force gauge, above an independent reflector |
| Standoff | 0.05 to 5 mm for broad scans. 0.02 to 0.2 mm for true squeeze-film studies only with fine-gap metrology |
| Output | Force curves and resonance maps |

Correct measurement geometry:

- The driven dish is supported by an overhead force gauge, a dish-side load cell, or a frame independent of the reflector plate.
- The reflector plate sits on its own support or on a separate load cell if the equal-and-opposite reaction is also being measured.
- Support the dish and reflector on separate force readouts for B0 conventional
  calibration. Internal action and reaction forces cancel on one common scale.
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

Ordinary acoustic forces between dish and reflector should cancel inside the
weighed boundary. A residual claim belongs in B0-net.

Keep this rule absolute. Subtracting two large conventional acoustic force
readings can create a small difference through sensor phase lag, alignment, gap
drift, thermal drift, or calibration mismatch. A real net external force should
be visible on the whole bounded article.

B0-net also needs a sealed or well-characterized acoustic boundary. If sound, airflow, or vibration leaves the fixture and pushes on the room, the room becomes the reaction mass. Log external microphones or accelerometers and run an open/closed enclosure comparison.

### Stage B1: Four-Dish Bench Platform

Build this after B0 is stable.

| Item | First build target |
| --- | --- |
| Dishes | 4 x 200 to 300 mm stainless bowls or pot lids |
| Optional larger dishes | 4 x 400 to 510 mm cymbals for expanded bench work |
| Transducers | 3 per dish, 12 total |
| Placement | 120 degrees apart on `dish_active_radius / P`, about 61.31 percent radius |
| Orientation | Bell or convex focus downward, aimed at reflector plate |
| Frame | Square frame, 600 to 800 mm side length for large dishes, smaller for bowls |
| Tilt | 0 degrees for pure vertical force maps. Optional 10 to 15 degrees outward for steering studies |
| Drive | 12 phase-locked channels |
| Measurement | B0 conventional: overhead load cells, corner load cells, or separate reflector load cells. B0-net: all hardware on one common weighed platform |
| Test surface | Smooth glass, polished aluminum, or polished concrete |

Expected conventional force:

- milligram-force to gram-force class for a first student pot-lid or bowl fixture,
- possibly larger sub-newton force only with a well-coupled squeeze-film geometry and suitable actuators,
- expected range stays far below human-scale lift.

Build tips:

- Make a paper or cardboard circle with the P-coded ring radius before drilling.
- Mark the center, active radius, P-coded ring, detuned ring, and port IDs.
- Start with removable tape or light clamps for mode-finding when the dish allows it.
- Measure the bare dish modes before adding transducers.
- Measure modes again after bolting or bonding. Added mass moves resonances.
- Keep the first standoff scans slow. Gap drift and heating can move the force curve.
- Photograph the ring radius measurement with a ruler in frame.

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
- Battery pack for self-contained runs.
- Temperature sensors on transducers and dishes.
- Load cells at support points or a separate reflector reaction measurement.
- Shielding, remote kill switch, and acoustic enclosure if available.

## Mechanical Build

1. Mark each dish at `dish_active_radius / P`, about 61.31 percent radius.
2. Place three transducers 120 degrees apart on each dish.
3. Avoid the rim and exact center. The rim is fragile and the center is a poor first location for many modes.
4. If drilling thin metal, use a center punch and step drill. Clamp the dish gently to avoid deformation.
5. Use rubber gaskets for bolt holes where acoustic sealing matters.
6. Route wires along the dish and frame. Strain-relieve every cable.
7. Add a pickup piezo or accelerometer to each dish. Add vertically separated or face-separated sensors if the run claims `S_hat_top` and `S_hat_bottom`.
8. Put a temperature sensor near at least one transducer per dish.
9. Build the standoff fixture so the gap to the reflector plate can be set repeatably. The squeeze-film scan needs sub-millimeter control.
10. Measure dish mode shape before permanent transducer placement. Keep the P-coded ring placement removable until a nodal map confirms it is useful for the chosen mode.
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

One pickup sensor per dish supports resonance locking and acoustic mapping. An
OPH top/bottom scalar needs upper and lower read zones. In the manifest, use:

```yaml
geometry:
  mode: acoustic_B0
  zone_definition: none
  oph_vertical_scalar_claim: false
  p_target_status: p_integrated
  p_target_value: 1.6309682
  p_geometry_ratio: dish_active_radius_mm / transducer_ring_radius_mm
  p_geometry_ratio_measured: 1.6309682
  p_geometry_ratio_tolerance_pct: 1.0
  p_geometry_elements: dish active radius, transducer ring radius, port angular positions
  p_geometry_file: geometry/dish-p-coded-ring-measurement.md
  p_detuned_control_id: dish_port_ring_detuned_control
  p_detuned_control_ratio: 1.50
  p_detuned_control_geometry_file: geometry/dish-detuned-ring-measurement.md
```

Set `oph_vertical_scalar_claim: true` after the article has upper and lower
instrumented zones and an accepted scorebook. Keep `p_target_status:
p_integrated` for B0 and B0-net. A B0 run can report conventional force mapping
as its strongest claim while carrying the P-coded geometry.

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
10. Use shorter force windows and declared cool-down periods when fine-gap heating moves resonance or load-cell zero during a block.
11. Start a new run series after a modal jump, plastic deformation, solder failure, or permanent center displacement.

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
6. Use the whole B0-net article on one weighed platform for the candidate force test.
7. Use separate scorebooks for conventional B0/NFAL mapping, B0-net residual testing, and optional OPH self-read force testing.

## Claim Boundary

This rig can demonstrate conventional near-field acoustic force. That measurement is a valid student result.

Human-carrying hover is outside scope. The source material itself contains a
correction: human-scale free-air acoustic hover is blocked by acoustic intensity,
wavelength, and safety limits. The realistic cymbal/pot-lid first-light result
is small bench-scale deflection.

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

The expected student result is a resonance map, a conventional acoustic force
or upper bound, and a clear artifact ledger.

## Safety

- No rider, no standing on the platform, no hands between dish and reflector plate.
- Start at low power and short duty cycles.
- Keep a hard kill switch within reach.
- Use hearing protection. Harmonics can be loud even when the drive frequency seems harmless.
- Shield the rig. Cymbals, bowls, and piezos can crack under overdrive.
- Never sand, drill, grind, or cut PZT. Discard cracked piezo parts in a sealed labeled container.
- Wash hands after handling PZT. Keep food and drink away from the bench.
- Clean ceramic fragments with wet methods or a suitable HEPA procedure. Keep
  compressed air away from PZT fragments.
- Stop if any transducer reaches 60 C.
- Use current-limited supplies.
- Keep loose objects, dust, paper, and uncovered sensors away from high-amplitude tests.
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
