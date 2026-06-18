# Student Project Brief

## One-Sentence Project

Build a battery-powered, instrumented coherent vibration body, measure its ordinary acoustic forces, and place an upper bound on any sign-reversible residual force after controls.

## Why It Is Expected To Work

Piezoelectric transducers convert voltage into strain. If they are bonded or bolted to a plate, lid, or cymbal, they can drive mechanical eigenmodes with repeatable phase and amplitude. Those modes produce real forces by ordinary physics:

- acoustic radiation pressure in air,
- squeeze-film pressure close to a nearby surface,
- direct mechanical vibration into supports,
- thermal convection and buoyancy,
- electrostatic and magnetic coupling.

The OPH theory behind the lab is simple in words. OPH starts from finite observers with finite access. Each observer has a local patch, keeps records, compares only the boundary data exposed on overlaps, repairs mismatches, and settles into the public fixed point that survives those comparisons. That is the basic observer-overlap picture in the [OPH repository](https://github.com/FloatingPragma/observer-patch-holography), the [Observers Are All You Need source](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/observers_are_all_you_need.tex), and [Reality as Consensus Protocol](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/reality_as_consensus_protocol.tex).

The novel step for this student package is to ask whether a small lab object can implement the same primitive in hardware. The object has ports, internal modes, onboard records, and a repair loop. In OPH language, it is a tiny bounded patch carrier. The hardware discipline comes from [Federated Echosahedral Screen Microphysics](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/screen_microphysics_and_observer_synchronization.tex), which treats ports, records, repair interfaces, checkpoints, and public evidence bundles as the relevant engineering surface.

The OPH/chi_nu idea asks for a stricter object than a vibrating plate. **The object must be a bounded, self-reading test article: it drives a mode, reads the response through the same or co-located ports, records the response onboard, lets that record change later drive packets, predicts later boundary response better than shuffled controls, and creates a signed top/bottom coherence contrast.** The proposed residual force is then tested against that internally measured contrast.

The exact candidate effect is a downstream dark-sector continuation, described in the [OPH dark matter paper](https://github.com/FloatingPragma/observer-patch-holography/blob/main/extra/oph_dark_matter_paper.tex) and the [chi_nu susceptibility bounds source](https://github.com/FloatingPragma/observer-patch-holography/blob/main/extra/chi_nu_susceptibility_bounds.tex). It says that a vertical coherence contrast in a bounded article may couple to the local gravitational support channel:

```text
Delta S_coh = S_bottom - S_top
F_chi = (g^2 / (4 * pi * G)) * A_perp * chi_nu * Delta S_coh
```

`S_top` and `S_bottom` are scorebook values derived from the self-read records. Raw loudness, vibration amplitude, and acoustic pressure remain ordinary artifact channels. `A_perp` is the projected horizontal area, `g` is local gravitational acceleration, and `chi_nu` is the branch susceptibility discussed in the chi_nu bounds paper. The compact recovery stack that separates recovered OPH core claims from continuation claims is in the [compact technical source](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/recovering_relativity_and_standard_model_structure_from_observer_overlap_consistency_compact.tex).

In the lab, the students create the candidate effect by making the lower vertical zone settle into a higher self-read coherence score than the upper zone, then reversing that relation for `ACTIVE_MINUS`. The `LIVE` controller is important because the record changes the next drive packet. `REPLAY` and `SHUFFLED_RECORD` keep the same power and timing while breaking that causal record loop. The balance test asks whether a force tracks `Delta S_coh`, reverses under `ACTIVE_MINUS`, reverses when the article is inverted about a horizontal axis, and disappears in sham, dummy, replay, and shuffled-record controls.

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

A candidate chi_nu residual requires a frozen scorebook, `LIVE` versus `REPLAY` separation, `SHUFFLED_RECORD` rejection, sign reversal, horizontal-axis physical inversion for top/bottom exchange, dummy rejection, matched-power sham rejection, and no explanatory correlation with temperature, electrostatics, magnetics, vibration leakage, or handling.

### Version 2: Acoustic Cymbal Bench Rig

Best as a second project after Version 1. It is mechanically louder, stronger, and less forgiving.

Main deliverables:

- one-dish calibration rig,
- four-dish bench platform with no rider and no free-flight claim,
- twelve phase-locked drive channels,
- independent top and bottom self-read zones for any OPH-style force test,
- conventional B0 acoustic force geometry and closed-system B0-net geometry,
- force versus standoff, frequency, phase, and amplitude curves,
- temperature and accelerometer logs,
- safety enclosure and remote kill switch.

Expected conventional result:

Near-field acoustic levitation can produce measurable force close to a smooth reflecting surface. The strongest ordinary signal should depend sharply on standoff distance, drive amplitude, resonance, surface reflectivity, and acoustic leakage. Student hardware should be treated as milligram-force to gram-force class until measured. Literature-class squeeze-film systems can reach larger sub-newton forces, but that is not a promise for a pot lid or cymbal.

Claim condition:

The same residual criteria as Version 1 apply. The larger rig is valuable because it stores more coherent vibrational energy and creates larger ordinary artifacts. Its OPH-style stage requires separate upper and lower self-read zones plus a whole-article weighing platform that includes dish, reflector, frame, electronics, battery, and enclosure.

## Corrected Experiment Order

1. Conventional characterization: modal maps, electrical transfer functions, acoustic maps, thermal maps, and force-sensor rectification tests.
2. Valid OPH primitive: two physical vertical zones, reversible ports, live record-conditioned feedback, frozen scorebook, and a demonstrated signed `S_bottom - S_top`.
3. Causal self-read ablation: `LIVE` feedback versus waveform-identical `REPLAY` and `SHUFFLED_RECORD` controls.
4. Vertical force test: whole self-contained article on a balance, randomized blinded blocks, true top/bottom inversion, and no external cables.
5. Artifact escalation: pressure sweep, enclosure-geometry sweep, electromagnetic and thermal perturbations, and a matched active mechanical twin.
6. Independent replication: another balance type, another operator, another lab, and a second geometry with a preregistered area or scalar-scaling prediction.

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
- a frozen machine-readable scorebook,
- raw logs and analysis scripts,
- clean conventional force curves,
- a matched dummy,
- a reported residual or upper bound.

The publication-grade result is a receipt bundle, not a dramatic video.
