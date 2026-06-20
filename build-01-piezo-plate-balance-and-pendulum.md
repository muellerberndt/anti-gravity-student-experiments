# Build 01: Piezo-Crystal Plate Balance And Pendulum

## Purpose

This is the first build to give students. It is cheap, measurable, and hard to fool if the controls are taken seriously.

The device is a small plate with piezoelectric ports. It drives its own resonant modes, reads ringdown and cross-coupling through the same or co-located ports, logs the state onboard, and then goes onto a force readout.

The OPH purpose is to instantiate a small observer-like self-reading system.
The plate must be bounded, ported, driven, read back, recorded, and run with
live feedback before any balance signal is interpreted as an OPH-style force
test.

Primary goal:

Map ordinary vibration and acoustic forces, then test whether a sign-reversible vertical coherent state produces any residual force after sham, dummy, replay, record-shuffled, phase-flip, and physical-flip controls.

The analytical balance is the primary readout for a vertical support-force test, because the Hacking PDF defines the first PoC as a self-contained active object with a top/bottom coherence contrast on a balance. The pendulum is useful for horizontal force calibration, acoustic recoil, torque, and artifact mapping. Do not treat a single-sided horizontal pendulum as the vertical support-force experiment.

Student model:

- Think of the plate as a small instrument with several speakers and microphones attached to it.
- During a drive window, the piezos push on the plate.
- During a read window, the piezos or pickup sensors listen to how the plate rings.
- The controller compares the expected ringdown to the measured ringdown.
- In `LIVE`, that comparison changes the next drive packet.
- In replay controls, the device receives a recorded packet sequence while its new records are ignored.
- The balance checks vertical support force. The pendulum checks horizontal recoil and artifacts.

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
| Readout | Same-port ringdown preferred. Co-located pickup piezos acceptable if declared as logical self-read |
| Sensors | Temperature, accelerometer, magnetometer, battery voltage, drive monitor |
| Logger | MicroSD or onboard flash with timestamps |
| Suspension | 1.5 to 2.0 m nonconductive line |
| Force readout | 0.1 mg or 1 mg balance for vertical support force. Camera, laser spot, or optical position sensor for horizontal pendulum force |

P integration rule:

`P ~= 1.6309682` is the plate's declared geometry/readback tuning target for an
OPH-style run. Before bonding ports, choose one dimensionless ratio that the
build will hold near `P`, such as port spacing divided by active-zone span,
collar or spacer gap divided by plate thickness, top-zone scale divided by
bottom-zone scale, or a frozen `K_port` coupling/readback ratio. Record the
definition, intended value, measured value, tolerance, and geometry files in the
manifest. Build or identify a detuned control with the same mass, power path,
and handling but with that ratio shifted. If this is not done, label the run
`conventional_only` or `exploratory_no_p`.

## Bill Of Materials

Minimum active plate:

- 1 nonmagnetic plate, 80 x 60 mm to 100 x 100 mm.
- 4 to 12 PZT piezo discs, 20 to 27 mm. Cheap buzzer discs are fine for first read/write tests.
- Thin epoxy or cyanoacrylate for bonding piezos to the plate.
- RP2040, RP2350, Teensy, or ESP32-class microcontroller.
- 4 to 12 drive channels. Low-power first pass: MOSFET half-bridge or small H-bridge per port. Higher-power pass: class-D audio amplifier channels.
- Voltage-rated bidirectional solid-state switch to disconnect the driver during ringdown sensing.
- High-impedance voltage-mode or charge-amplifier piezo front end with mid-supply bias, input protection, discharge path, and defined bandpass.
- Per-channel terminal voltage and current monitoring for calibration runs.
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

Confirmation needs two controls:

- Electrical dummy: same battery, current draw, RF envelope, heat, and logging, with no coherent mechanical branch.
- Mechanical active twin: same mass, same transducers, and same measured acceleration, acoustic, and thermal envelope, with invalid self-read from record shuffle or deliberately broken feedback.

The mechanical active twin matters because a resistor-only dummy may fail to match acoustic leakage, force-sensor rectification, and thermal buoyancy.

## Mechanical Build

1. Declare the measurement geometry before bonding ports. Balance mode uses top and bottom zones relative to gravity. Pendulum mode uses left/right or A/B zones along the horizontal force axis.
2. Declare the P status before bonding ports. If the run is OPH-style, mark the P-coded ratio on the drawing and specify the detuned control geometry. If not, mark the run as conventional-only.
3. For balance mode, place matched ports or matched port groups on both faces, or use a laminate that gives separately measured top and bottom readouts. A single-sided plate can train the electronics, but it does not supply a true top/bottom scalar.
4. For pendulum mode, bond piezos in symmetric pairs across the horizontal axis. A four-port layout uses two ports on one side of the axis and two on the other. An eight-port or twelve-port layout gives better mode control.
5. Keep the center of mass on the balance contact point or suspension line. Add nonmagnetic trim mass if needed.
6. Route wires tightly against the plate. No dangling loops. During force measurements the plate must run from onboard power and logging.
7. Add a small mirror or optical fiducial near the center of mass for pendulum mode. If using a laser mirror, keep it light and centered.
8. Put the battery and logger on the moving test article, not on the bench.
9. Build the dummy with the same outside geometry and mass.

## Electronics

Each piezo port should support two modes:

- Drive window: the MCU commands a sine, square, or PWM waveform through a protected driver.
- Read window: the driver disconnects, the piezo sits behind a high impedance, and the ADC records ringdown and cross-coupled response.

Minimum same-port circuit:

- driver output through 47 to 220 ohm series resistance,
- voltage-rated bidirectional solid-state disconnect before ADC read,
- voltage-mode or charge-amplifier input with high impedance,
- mid-supply ADC bias so bipolar piezo ringdown swings around `VCC / 2`,
- input protection that does not rail-clip the signal during normal ringdown,
- defined discharge path and bandpass,
- firmware dead time between drive and read windows.

Do not use mechanical relays during force runs. Relay motion, magnetic fields, and contact bounce create center-of-mass and EMI artifacts.

Do not feed a bipolar piezo ringdown into a microcontroller ADC through only a divider and rail clamps. That clips the negative half-cycle and corrupts phase, Q, and cross-coupling. Keep the divider-plus-clamp approach for rough bench abuse tests only.

Drive calibration:

- measure terminal voltage and current at each port,
- measure each piezo capacitance after bonding,
- keep driver current below the capacitive estimate `I_rms ~= 2 * pi * f * C * V_rms`,
- calibrate electrical phase at the transducer terminals, not only at the MCU pins,
- use filtered sine drive or record the full voltage, current, acceleration, and acoustic spectra for confirmation,
- make `SHAM` match RMS voltage, RMS current, real power, reactive power, harmonics, battery waveform, temperature, RF/logging activity, acoustic spectrum, and momentum direction as closely as the hardware allows.

For a first student prototype, co-located transmit/receive pairs are acceptable if the geometry is fixed and documented. Label that as logical self-read. Strict same-port status belongs to reversible drive/sense ports.

## Firmware States

Implement fixed, timestamped state blocks:

| State | Behavior |
| --- | --- |
| `OFF` | Logger only. No drive. |
| `SHAM` | Same average power as active, with incoherent or phase-scrambled drive. |
| `ACTIVE_PLUS` | Coherent phase/amplitude pattern with the intended force-axis sign. |
| `ACTIVE_MINUS` | Same power and frequency set, reversed phase gradient or zone assignment. |
| `LIVE` | Next drive packet computed from the latest self-read record. |
| `OPEN_LOOP_REPLAY` | Exact packet sequence from a named `LIVE` run, with current records measured and ignored. |
| `CAUSAL_SHUFFLE` | Block-shuffled or time-shifted records feed the controller, so the generated packet sequence may change. |
| `YOKED_SHUFFLE_REPLAY` | Exact packet sequence from a named `CAUSAL_SHUFFLE` run, replayed open-loop. |
| `DUMMY` | Same schedule on the matched dummy. |

A practical `ACTIVE_PLUS` pattern:

- in balance mode, drive the top zone and bottom zone with a declared phase, handedness, or amplitude contrast,
- in pendulum mode, drive side A at phase 0 degrees and side B at phase +90 degrees, or with a defined amplitude lead,
- read every port after each drive packet,
- compute ringdown amplitude, phase, Q estimate, and cross-coupling matrix.

`ACTIVE_MINUS` reverses the phase gradient, handedness, or zone assignment. The power envelope must remain matched.

For a direct vertical test, compute `S_hat_top` and `S_hat_bottom` independently from the frozen scorebook. `ACTIVE_PLUS` means bottom-over-top by the declared proxy sign convention. `ACTIVE_MINUS` means top-over-bottom. A yaw rotation around the vertical suspension axis does not exchange top and bottom relative to gravity.

Closed-loop repair sequence:

1. drive all ports,
2. read the complete port-response vector,
3. calculate the declared mismatch score,
4. adjust the next phase/amplitude vector to reduce that mismatch,
5. save the accepted update and repeat until the frozen stopping rule is met.

Force runs must include `LIVE`, `OPEN_LOOP_REPLAY`, `CAUSAL_SHUFFLE`, and `YOKED_SHUFFLE_REPLAY` blocks. `OPEN_LOOP_REPLAY` keeps the physical waveform fixed from a prior live run. `CAUSAL_SHUFFLE` tests the temporal record relation. `YOKED_SHUFFLE_REPLAY` separates the shuffled waveform from live processing.

## Pre-Force Checkout

Do not put the device on a force readout for a claim until it has a self-read receipt.

Required checks:

1. Frequency sweep: identify stable plate modes from 100 Hz to 40 kHz.
2. Coupling matrix: drive each port, read all ports, and save amplitude, phase, and ringdown features.
3. Repeatability: repeat each state at least 20 times.
4. Prediction test: use records from cycle `t` to predict held-out readouts from later cycles. Compare against surrogate records that preserve autocorrelation while breaking causal alignment.
5. Sign test: show that `ACTIVE_PLUS` and `ACTIVE_MINUS` produce opposite signed feature contrast along the declared measurement axis.
6. Dummy rejection: dummy logs should not produce the same signed self-read scalar.
7. P-status check: for an OPH-style run, verify the measured P-coded ratio, the tolerance, and the detuned-control ID before force data are viewed.
8. Scorebook lock: freeze `templates/scorebook_template.json` or a run-specific derived `scorebook.json` before looking at force data.
9. Live ablation: prove `LIVE` reduces the declared mismatch relative to `OPEN_LOOP_REPLAY` and `YOKED_SHUFFLE_REPLAY`, with `CAUSAL_SHUFFLE` showing the temporal-record dependence.
10. Zone independence: show `top_drive -> top_read` is stronger than `top_drive -> bottom_read` by the declared margin, or supply the coupled-mode model that explains both.
11. Reverse zone independence: show `bottom_drive -> bottom_read` is stronger than `bottom_drive -> top_read` by the declared margin, or supply the coupled-mode model that explains both.
12. Support-loading test: prove the balance pan, pad, or cradle does not erase or invert the pre-balance scalar.
13. Port identity under inversion: prove horizontal-axis inversion exchanges lab top/bottom while preserving internal port identity.
14. Zone separability receipt: report `C_TT`, `C_TB`, `C_BT`, `C_BB`, cross-zone leakage, channel-swap sign stability, piezo-polarity sign stability, and mirrored-article sign stability if available.
15. Balance rectification calibration: drive an inert dummy with the same measured acceleration spectrum and measure any DC balance offset across frequency, amplitude, modulation, duty cycle, and pan position.

## Balance Measurement

Use this for a vertical support-force test.

Setup:

- Put a 0.1 mg or 1 mg analytical balance on stone or an anti-vibration table.
- Close the draft shield or put the balance inside a draft-free enclosure.
- Calibrate with known masses near the test-article mass.
- Run the active plate from onboard power and onboard logging only.
- Keep USB, power, and ground cables disconnected during force blocks.
- Let the active plate, dummy, and balance thermally settle before recording.
- Use a soft pad, three-point fixture, or symmetric cradle if the balance pan mechanically loads the bottom zone.
- Save pre-balance and on-balance self-read scalar files. A support-loaded scalar is not a confirmation scalar unless the loading is modeled and preregistered.
- Use a kinematic cradle or gimbal that rotates the article without changing pan contact points.
- Record physical orientation as `q = +1` or `q = -1`.
- Repeat at two mounting topologies and two pan positions before treating a residual as a candidate.
- Run a post-flip coupling matrix and modal check after every inversion.

Run sequence:

1. Record `OFF` for drift.
2. Run `SHAM`, `ACTIVE_PLUS`, `ACTIVE_PLUS`, `SHAM` in ABBA order.
3. Run `SHAM`, `ACTIVE_MINUS`, `ACTIVE_MINUS`, `SHAM`.
4. Physically invert the complete test article 180 degrees about a horizontal axis so the physical top and bottom exchange places in the lab frame, then repeat.
5. Run the matched dummy with the same schedule.
6. Run heater-only or resistor-only controls at the same average power.

Balance force:

```text
F_lift = -g0 * delta_m_apparent
```

where `delta_m_apparent` is the active-state apparent mass shift in kg relative to the matched sham windows. A lighter balance reading gives positive apparent lift by this convention.

## Pendulum Measurement

Setup:

- Hang the active plate from a 1.5 to 2.0 m line.
- Put the line on a rigid overhead point.
- Enclose the rig to block air currents.
- Let the system thermally settle before recording.
- Use a bifilar suspension, a torsion balance, or camera tracking of at least two separated fiducials. A single laser mirror can turn yaw torque into apparent translation.
- Track center-of-mass displacement with a camera, or track reflected laser spot displacement from a small mirror only after yaw has been calibrated.
- Use this mode for horizontal force calibration, acoustic recoil, and artifact mapping. It is not a substitute for the balance support-force test unless the theory axis and lab axis are deliberately declared as horizontal.

Direct camera formula:

```text
F_horizontal = m * g0 * x / L
```

where `m` is moving test-article mass, `L` is pendulum length, and `x` is center-of-mass displacement.

Laser mirror formula:

```text
F_horizontal = m * g0 * s / (2 * D)
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

Pendulum calibration:

- apply known lateral forces at multiple heights,
- apply known torques with zero net force,
- reconstruct translation and yaw separately,
- map acoustic field or momentum flux around the article,
- repeat with enclosure changes,
- use pressure dependence or reduced-pressure testing for any confirmatory pendulum result,
- use a sealed whole-test-article configuration before interpreting pendulum motion as anomalous thrust.

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
- reversed by horizontal-axis physical inversion for balance mode, or by the declared rotation test for pendulum mode,
- absent or much smaller in dummy and sham,
- absent or much smaller in the mechanical active twin,
- absent or much smaller in `OPEN_LOOP_REPLAY` and `YOKED_SHUFFLE_REPLAY`,
- not explained by temperature, battery voltage, vibration leakage, magnetometer changes, electrostatics, or operator timing.

Expected result:

The expected student result is no residual after controls. A useful report gives resonance maps, self-read quality, conventional force estimates, artifact regressions, and an upper bound.

## Safety

- Start below 24 Vpp and low duty cycle.
- Fuse the battery.
- Keep hands away during high-amplitude sweeps.
- Wear eye protection. PZT ceramic can crack.
- Never sand, drill, grind, or cut PZT. Commercial PZT contains lead zirconate titanate.
- Discard cracked piezo discs in a sealed labeled container.
- Wash hands after handling PZT. Keep food and drink away from the bench.
- Clean ceramic fragments with wet methods or a suitable HEPA procedure. Do not use compressed air.
- Do not use a power or USB cable during force measurements.
- Let piezos cool. Stop if any port exceeds 60 C.
- Treat a positive-looking result as an artifact until the dummy, flip, sham, and thermal controls are complete.
