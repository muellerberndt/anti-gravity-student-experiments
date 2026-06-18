# Student Project Brief

## One-Sentence Project

Build a battery-powered, instrumented coherent vibration body, measure its ordinary acoustic forces, and test whether a sign-reversible self-read pattern produces any residual force after controls.

## Why It Might Work

Piezoelectric transducers convert voltage into strain. If they are bonded or bolted to a plate, lid, or cymbal, they can drive mechanical eigenmodes with repeatable phase and amplitude. Those modes produce real forces by ordinary physics:

- acoustic radiation pressure in air,
- squeeze-film pressure close to a nearby surface,
- direct mechanical vibration into supports,
- thermal convection and buoyancy,
- electrostatic and magnetic coupling.

The OPH/chi_nu idea asks for a stricter object than a vibrating plate. The object must be a bounded, self-reading test article: it drives a mode, reads the response through the same or co-located ports, records the response onboard, predicts later boundary response better than shuffled controls, and creates a signed top/bottom coherence contrast. The proposed residual force is then tested against that internally measured contrast.

No student build should assume the residual exists. A clean conventional force map plus an upper bound is a valid result.

## Recommended Versions

### Version 1: Piezo-Crystal Plate Pendulum

Best for a first student team. It uses low mass, low voltage, simple mechanics, and good measurement discipline.

Main deliverables:

- active plate with four or eight piezo drive/read ports,
- onboard battery and logger,
- resonance and coupling matrix,
- signed `ACTIVE+` and `ACTIVE-` phase patterns,
- pendulum or analytical-balance measurement,
- matched dummy plate and matched-power sham runs.

Expected conventional result:

The plate will show resonances, ringdown, cross-coupling, acoustic leakage, and thermal artifacts. A pendulum may deflect from acoustic radiation pressure or air motion. Those effects should track frequency, amplitude, orientation, and shielding in conventional ways.

Claim condition:

A candidate chi_nu residual requires sign reversal, physical flip reversal, dummy rejection, matched-power sham rejection, and no explanatory correlation with temperature, electrostatics, magnetics, vibration leakage, or handling.

### Version 2: Acoustic Cymbal Hoverboard Bench Rig

Best as a second project after Version 1. It is mechanically louder, stronger, and less forgiving.

Main deliverables:

- one-dish calibration rig,
- four-dish bench platform with no rider,
- twelve phase-locked drive channels,
- force versus standoff, frequency, phase, and amplitude curves,
- temperature and accelerometer logs,
- safety enclosure and remote kill switch.

Expected conventional result:

Near-field acoustic levitation can produce measurable force near a smooth reflecting surface. The strongest ordinary signal should depend sharply on standoff distance, drive amplitude, resonance, surface reflectivity, and acoustic leakage.

Claim condition:

The same residual criteria as Version 1 apply. The larger rig is valuable because it stores more coherent vibrational energy, but it also creates larger ordinary artifacts.

## Other Useful Combinations

- TinyLev first: a small 40 kHz standing-wave levitator is the cleanest classroom proof that acoustic radiation pressure is real. It teaches students what conventional lift looks like before they touch the OPH test article.
- Single-pot-lid pendulum: use a 200 mm aluminum pot lid with twelve piezos as a cheap bridge between Version 1 and Version 2.
- Analytical-balance variant: put the active plate on a 0.1 mg or 1 mg balance instead of a pendulum. This is cleaner for vertical force but more sensitive to heat, static charge, and vibration.
- Single-cymbal load-cell station: drive one cymbal or bowl over a ground plate mounted on a load cell. This is the right precursor to any four-cymbal frame.

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
