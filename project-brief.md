# Student Project Brief

## One-Sentence Project

Build a battery-powered, instrumented coherent vibration body, measure its ordinary acoustic forces, and place an upper bound on any sign-reversible residual force after controls.

## Why It Might Work

Piezoelectric transducers convert voltage into strain. If they are bonded or bolted to a plate, lid, or cymbal, they can drive mechanical eigenmodes with repeatable phase and amplitude. Those modes produce real forces by ordinary physics:

- acoustic radiation pressure in air,
- squeeze-film pressure close to a nearby surface,
- direct mechanical vibration into supports,
- thermal convection and buoyancy,
- electrostatic and magnetic coupling.

The OPH/chi_nu idea asks for a stricter object than a vibrating plate. The object must be a bounded, self-reading test article: it drives a mode, reads the response through the same or co-located ports, records the response onboard, predicts later boundary response better than shuffled controls, and creates a signed top/bottom coherence contrast. The proposed residual force is then tested against that internally measured contrast.

No student build should assume the residual exists. A clean conventional force map plus an upper bound is the expected successful result.

## Does The Hardware Work?

Yes, for conventional measurements. The plate and cymbal rigs should produce resonant modes, ringdown, phase-dependent vibration, acoustic leakage, heat, and measurable artifact paths if the sensors are sensitive enough.

No positive OPH force receipt follows from the source material. The papers define a hypothesis and a control protocol. They do not establish that a student plate, pot lid, cymbal, or bowl produces a new force.

## Recommended Versions

### Version 1: Piezo-Crystal Plate Balance And Pendulum

Best for a first student team. It uses low mass, low voltage, simple mechanics, and good measurement discipline.

Main deliverables:

- active plate with four to twelve piezo drive/read ports,
- declared geometry: top/bottom zones for balance mode, or left/right zones for pendulum mode,
- onboard battery and logger,
- resonance and coupling matrix,
- signed `ACTIVE+` and `ACTIVE-` phase patterns,
- analytical-balance measurement for vertical support force,
- pendulum measurement for horizontal acoustic recoil and artifact mapping,
- matched dummy plate and matched-power sham runs.

Expected conventional result:

The plate will show resonances, ringdown, cross-coupling, acoustic leakage, and thermal artifacts. A pendulum may deflect from acoustic radiation pressure or air motion. A balance may show apparent mass changes from heat, electrostatics, vibration, and drift. Those effects should track frequency, amplitude, orientation, shielding, and temperature in conventional ways.

Claim condition:

A candidate chi_nu residual requires sign reversal, physical flip reversal, dummy rejection, matched-power sham rejection, and no explanatory correlation with temperature, electrostatics, magnetics, vibration leakage, or handling.

### Version 2: Acoustic Cymbal Bench Rig

Best as a second project after Version 1. It is mechanically louder, stronger, and less forgiving.

Main deliverables:

- one-dish calibration rig,
- four-dish bench platform with no rider and no free-flight claim,
- twelve phase-locked drive channels,
- force versus standoff, frequency, phase, and amplitude curves,
- temperature and accelerometer logs,
- safety enclosure and remote kill switch.

Expected conventional result:

Near-field acoustic levitation can produce measurable force close to a smooth reflecting surface. The strongest ordinary signal should depend sharply on standoff distance, drive amplitude, resonance, surface reflectivity, and acoustic leakage. Student hardware should be treated as milligram-force to gram-force class until measured. Literature-class squeeze-film systems can reach larger sub-newton forces, but that is not a promise for a pot lid or cymbal.

Claim condition:

The same residual criteria as Version 1 apply. The larger rig is valuable because it stores more coherent vibrational energy, and it creates larger ordinary artifacts.

## Other Useful Combinations

- TinyLev first: a small 40 kHz standing-wave levitator is the cleanest classroom proof that acoustic radiation pressure is real. It teaches students what conventional lift looks like before they touch the OPH test article.
- Single-pot-lid pendulum: use a 200 mm aluminum pot lid with twelve piezos as a cheap bridge between Version 1 and Version 2.
- Balance-first plate run: put the active plate on a 0.1 mg or 1 mg balance for the vertical support-force test. This is cleaner for vertical force and more sensitive to heat, static charge, and vibration.
- Single-cymbal load-cell station: drive one cymbal or bowl over an independent reflector plate, with dish-side and reflector-side forces measured separately if possible. This is the right precursor to any four-cymbal frame.

## Student-Level Success Criteria

A good student project does not require a positive anomaly. It requires:

- a working active test article,
- reproducible resonance and coupling data,
- a frozen run manifest,
- raw logs and analysis scripts,
- clean conventional force curves,
- a matched dummy,
- a reported residual or upper bound.

The publication-grade result is a receipt bundle, not a dramatic video.
