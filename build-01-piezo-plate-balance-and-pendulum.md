# Build 01: Piezo-Crystal Plate Balance And Pendulum

## Purpose

This is the first build to give students. It is cheap, measurable, and hard to fool if the controls are taken seriously.

The device is a small plate with piezoelectric ports. It drives its own resonant modes, reads ringdown and cross-coupling through the same or co-located ports, logs the state onboard, and then goes onto a force readout.

Primary goal:

Map ordinary vibration and acoustic forces, then test whether a sign-reversible coherent state produces any residual force after sham, dummy, phase-flip, and physical-flip controls.

The analytical balance is the primary readout for a vertical support-force test, because the Hacking PDF defines the first PoC as a self-contained active object with a top/bottom coherence contrast on a balance. The pendulum is useful for horizontal force calibration, acoustic recoil, and artifact mapping. Do not treat a single-sided horizontal pendulum as the vertical support-force experiment.

## Target Specification

| Item | First build target |
| --- | --- |
| Plate size | 80 x 60 mm to 100 x 100 mm |
| Plate material | Quartz, alumina, glass-ceramic, sapphire, or insulated aluminum |
| Plate thickness | 1 to 3 mm |
| Active ports | 4 to 12 piezo discs, 20 to 27 mm diameter |
| Port layout | Top/bottom zones for balance mode. Left/right or A/B zones for pendulum mode |
| Drive range | Start 100 Hz to 40 kHz sweep |
| Drive voltage | Start below 24 Vpp. Increase only after thermal checks |
| Power | Onboard battery during force measurements |
| Readout | Same-port ringdown preferred. Co-located pickup piezos acceptable |
| Sensors | Temperature, accelerometer, magnetometer, battery voltage, drive monitor |
| Logger | MicroSD or onboard flash with timestamps |
| Suspension | 1.5 to 2.0 m nonconductive line |
| Force readout | 0.1 mg or 1 mg balance for vertical support force. Camera, laser spot, or optical position sensor for horizontal pendulum force |

## Bill Of Materials

Minimum active plate:

- 1 nonmagnetic plate, 80 x 60 mm to 100 x 100 mm.
- 4 to 12 PZT piezo discs, 20 to 27 mm. Cheap buzzer discs are fine for first read/write tests.
- Thin epoxy or cyanoacrylate for bonding piezos to the plate.
- RP2040, RP2350, Teensy, or ESP32-class microcontroller.
- 4 to 12 drive channels. Low-power first pass: MOSFET half-bridge or small H-bridge per port. Higher-power pass: class-D audio amplifier channels.
- Analog switch or relay network to disconnect the driver during ringdown sensing.
- ADC front end with input protection. Use a high-value divider, series resistance, and clamp diodes or TVS protection.
- MicroSD module or onboard flash.
- IMU/accelerometer, 3-axis magnetometer, and at least one temperature sensor.
- LiPo or Li-ion battery, regulator, fuse, and physical kill switch.
- Nonconductive suspension line, 1.5 to 2.0 m.
- Laser pointer and small mirror, or phone camera with a high-contrast fiducial.
- Shield box or transparent acrylic guard.

Matched dummy:

- Same plate outline and mass.
- Same battery mass and electronics envelope.
- Same external coating, tape, heat path, and handling.
- Broken coherent branch: replace piezos with matched capacitors/resistors, scramble phase, add damping, or run record-shuffled firmware.

## Mechanical Build

1. Declare the measurement geometry before bonding ports. Balance mode uses top and bottom zones relative to gravity. Pendulum mode uses left/right or A/B zones along the horizontal force axis.
2. For balance mode, place matched ports or matched port groups on both faces, or use a laminate that gives separately measured top and bottom readouts. A single-sided plate can train the electronics, but it does not supply a true top/bottom scalar.
3. For pendulum mode, bond piezos in symmetric pairs across the horizontal axis. A four-port layout uses two ports on one side of the axis and two on the other. An eight-port or twelve-port layout gives better mode control.
4. Keep the center of mass on the balance contact point or suspension line. Add nonmagnetic trim mass if needed.
5. Route wires tightly against the plate. No dangling loops. During force measurements the plate must run from onboard power and logging.
6. Add a small mirror or optical fiducial near the center of mass for pendulum mode. If using a laser mirror, keep it light and centered.
7. Put the battery and logger on the moving test article, not on the bench.
8. Build the dummy with the same outside geometry and mass.

## Electronics

Each piezo port should support two modes:

- Drive window: the MCU commands a sine, square, or PWM waveform through a protected driver.
- Read window: the driver disconnects, the piezo sits behind a high impedance, and the ADC records ringdown and cross-coupled response.

Minimum safe same-port circuit:

- driver output through 47 to 220 ohm series resistance,
- analog switch or relay disconnect before ADC read,
- ADC input through 1 Mohm / 100 kohm divider or similar,
- clamp diodes to ADC rails,
- firmware dead time between drive and read windows.

For a first student prototype, co-located transmit/receive pairs are acceptable if the geometry is fixed and documented. Label that as logical self-read. Strict same-port status belongs to reversible drive/sense ports.

## Firmware States

Implement fixed, timestamped state blocks:

| State | Behavior |
| --- | --- |
| `OFF` | Logger only. No drive. |
| `SHAM` | Same average power as active, with incoherent or phase-scrambled drive. |
| `ACTIVE_PLUS` | Coherent phase/amplitude pattern with the intended force-axis sign. |
| `ACTIVE_MINUS` | Same power and frequency set, reversed phase gradient or zone assignment. |
| `DUMMY` | Same schedule on the matched dummy. |

A practical `ACTIVE_PLUS` pattern:

- in balance mode, drive the top zone and bottom zone with a declared phase, handedness, or amplitude contrast,
- in pendulum mode, drive side A at phase 0 degrees and side B at phase +90 degrees, or with a defined amplitude lead,
- read every port after each drive packet,
- compute ringdown amplitude, phase, Q estimate, and cross-coupling matrix.

`ACTIVE_MINUS` reverses the phase gradient, handedness, or zone assignment. The power envelope must remain matched.

## Pre-Force Checkout

Do not put the device on a force readout for a claim until it has a self-read receipt.

Required checks:

1. Frequency sweep: identify stable plate modes from 100 Hz to 40 kHz.
2. Coupling matrix: drive each port, read all ports, and save amplitude, phase, and ringdown features.
3. Repeatability: repeat each state at least 20 times.
4. Prediction test: use records from cycle `t` to predict held-out readouts from later cycles. Compare against shuffled records.
5. Sign test: show that `ACTIVE_PLUS` and `ACTIVE_MINUS` produce opposite signed feature contrast along the declared measurement axis.
6. Dummy rejection: dummy logs should not produce the same signed self-read scalar.

## Balance Measurement

Use this for a vertical support-force test.

Setup:

- Put a 0.1 mg or 1 mg analytical balance on stone or an anti-vibration table.
- Close the draft shield or put the balance inside a draft-free enclosure.
- Calibrate with known masses near the test-article mass.
- Run the active plate from onboard power and onboard logging only.
- Keep USB, power, and ground cables disconnected during force blocks.
- Let the active plate, dummy, and balance thermally settle before recording.

Run sequence:

1. Record `OFF` for drift.
2. Run `SHAM`, `ACTIVE_PLUS`, `ACTIVE_PLUS`, `SHAM` in ABBA order.
3. Run `SHAM`, `ACTIVE_MINUS`, `ACTIVE_MINUS`, `SHAM`.
4. Physically flip or invert the plate so the same internal command faces the opposite lab-vertical direction, then repeat.
5. Run the matched dummy with the same schedule.
6. Run heater-only or resistor-only controls at the same average power.

Balance force:

```text
F_lift = -g * delta_m_apparent
```

where `delta_m_apparent` is the active-state apparent mass shift in kg relative to the matched sham windows. A lighter balance reading gives positive apparent lift by this convention.

## Pendulum Measurement

Setup:

- Hang the active plate from a 1.5 to 2.0 m line.
- Put the line on a rigid overhead point.
- Enclose the rig to block air currents.
- Let the system thermally settle before recording.
- Track center-of-mass displacement with a camera, or track reflected laser spot displacement from a small mirror.
- Use this mode for horizontal force calibration, acoustic recoil, and artifact mapping. It is not a substitute for the balance support-force test unless the theory axis and lab axis are deliberately declared as horizontal.

Direct camera formula:

```text
F_horizontal = m * g * x / L
```

where `m` is moving test-article mass, `L` is pendulum length, and `x` is center-of-mass displacement.

Laser mirror formula:

```text
F_horizontal = m * g * s / (2 * D)
```

where `s` is reflected spot displacement on a screen and `D` is mirror-to-screen distance. This assumes small angles.

Run sequence:

1. Record `OFF` for drift.
2. Run `SHAM`, `ACTIVE_PLUS`, `ACTIVE_PLUS`, `SHAM` in ABBA order.
3. Run `SHAM`, `ACTIVE_MINUS`, `ACTIVE_MINUS`, `SHAM`.
4. Physically rotate the plate 180 degrees around the vertical suspension axis and repeat.
5. Run the matched dummy with the same schedule.
6. Run heater-only or resistor-only controls at the same average power.

Use stable windows after a preregistered settling interval. Keep the raw video or optical position log.

## What Students Should Expect

Expected ordinary signals:

- resonance peaks,
- phase-dependent vibration,
- air motion near the plate,
- pendulum motion that tracks acoustic leakage,
- thermal drift after high-power states,
- static effects after handling.

Useful first result:

- a measured force curve or upper bound,
- a clean map of which artifacts dominate,
- a reproducible self-read scalar if the hardware is good enough.

Candidate residual threshold:

- same sign as the pre-force self-read scalar,
- reversed by `ACTIVE_MINUS`,
- reversed by physical flip or rotation along the declared measurement axis,
- absent or much smaller in dummy and sham,
- not explained by temperature, battery voltage, vibration leakage, magnetometer changes, electrostatics, or operator timing.

Expected result:

The expected student result is no residual after controls. A useful report gives resonance maps, self-read quality, conventional force estimates, artifact regressions, and an upper bound.

## Safety

- Start below 24 Vpp and low duty cycle.
- Fuse the battery.
- Keep hands away during high-amplitude sweeps.
- Wear eye protection. PZT ceramic can crack.
- Do not use a power or USB cable during force measurements.
- Let piezos cool. Stop if any port exceeds 60 C.
- Treat a positive-looking result as an artifact until the dummy, flip, sham, and thermal controls are complete.
