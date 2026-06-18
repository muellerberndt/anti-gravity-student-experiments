# Build 02: Acoustic Cymbal Bench Rig

## Purpose

This is the larger student build. It should be run as a bench force platform, with no rider and no free-flight claim.

The rig uses cymbals, pot lids, stainless bowls, or similar thin metal dishes as resonant acoustic radiators. Piezo or Langevin transducers drive the dishes. The students map conventional near-field acoustic force first, then use the same apparatus as a larger coherent-body test article.

Primary goal:

Measure force versus frequency, phase, drive amplitude, and standoff distance, then test whether a sign-reversible coherent state produces any residual after conventional acoustic effects are subtracted.

The included cymbal hoverboard source is useful for geometry and first-light drive ideas, but its human-carrying lift claim is not adopted here. The included antigravity survey corrects that claim and treats the pot-lid result as small bench-scale conventional acoustic force.

## Build Stages

### Stage B0: Single-Dish Calibration Station

Build this before the four-dish platform.

| Item | First build target |
| --- | --- |
| Dish | 200 mm aluminum pot lid, stainless bowl, or small cymbal |
| Transducers | 3 to 12 piezo discs or bolt-on transducers |
| Layout | Ring at about 60 percent radius |
| Drive | Phase-locked channels from one MCU |
| Measurement | Driven dish on its own load cell or overhead force gauge, above an independent reflector |
| Standoff | 0.05 to 5 mm for squeeze-film scans. 5 to 30 mm only for acoustic leakage and reflector-distance scans |
| Output | Force curves and resonance maps |

Correct measurement geometry:

- The driven dish is supported by an overhead force gauge, a dish-side load cell, or a frame independent of the reflector plate.
- The reflector plate sits on its own support or on a separate load cell if the equal-and-opposite reaction is also being measured.
- Do not put both dish and reflector plate on the same scale. Internal action and reaction forces will cancel in the reading.
- Report dish-side force and reflector-side force separately. Their sum should be close to zero for ordinary acoustic interaction inside one closed bench fixture.

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
| Measurement | Overhead load cells, corner load cells, or separate reflector load cells |
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
7. Add a pickup piezo or accelerometer to each dish.
8. Put a temperature sensor near at least one transducer per dish.
9. Build the standoff fixture so the gap to the reflector plate can be set repeatably. The squeeze-film scan needs sub-millimeter control.
10. Add a transparent shield before high-amplitude sweeps.

## Drive Architecture

Minimum:

- one MCU generates phase-locked PWM or DAC waveforms,
- one amplifier channel per transducer,
- one pickup sensor per dish,
- frequency sweep and resonance-lock mode,
- fixed state schedules written to the log.

Drive states:

| State | Behavior |
| --- | --- |
| `OFF` | No drive. Sensors and logger only. |
| `SHAM` | Same average power, incoherent or phase-scrambled drive. |
| `ACTIVE_PLUS` | Coherent multichord drive with intended sign. |
| `ACTIVE_MINUS` | Same power, reversed phase gradient or dish zoning. |
| `DUMMY` | Matched non-coherent dish or mechanically damped dish. |

Start with one frequency at a time. Add multichord drive only after the single-frequency force curves are understood.

## Measurement Plan

### Conventional Acoustic Force Map

For each dish:

1. Set standoff distance: 0.05, 0.1, 0.2, 0.5, 1, 2, and 5 mm for the squeeze-film scan if the fixture can do this safely.
2. Add 10, 20, and 30 mm only as a reflector-distance or acoustic-leakage scan.
3. Sweep frequency around measured resonances.
4. Sweep drive amplitude at fixed frequency.
5. Record dish acceleration, transducer temperature, load-cell force, supply voltage, current, and acoustic level if available.
6. Repeat on different surfaces: glass, aluminum, polished concrete, and a lossy surface such as foam or carpet.

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

## Claim Boundary

This rig can demonstrate conventional near-field acoustic force. That measurement is a valid student result.

A human-carrying hoverboard is outside scope. The source material itself contains a correction: human-scale free-air acoustic hover is blocked by acoustic intensity, wavelength, and safety limits, and the realistic cymbal/pot-lid first-light result is small bench-scale deflection. The bench should not be presented as a scaled-down working hoverboard.

Treat any residual force claim as provisional until:

- the conventional force map is complete,
- the residual survives standoff changes,
- the residual reverses with `ACTIVE_MINUS`,
- the residual reverses under physical flip or rotation,
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
