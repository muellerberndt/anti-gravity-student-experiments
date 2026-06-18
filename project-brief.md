# Student Project Brief

## One-Sentence Project

Build a battery-powered, instrumented coherent vibration body, measure its ordinary acoustic forces, and place an upper bound on any sign-reversible residual force after controls.

OPH's recovered core does not establish a coherent-matter force. The tested force law belongs to a conditional continuation branch, and existing internal program measurements are reported as null. These builds teach conventional force metrology and test an explicitly speculative continuation.

## Why It Is Expected To Work

Piezoelectric transducers convert voltage into strain. If they are bonded or bolted to a plate, lid, or cymbal, they can drive mechanical eigenmodes with repeatable phase and amplitude. Those modes produce real forces by ordinary physics:

- acoustic radiation pressure in air,
- squeeze-film pressure close to a nearby surface,
- direct mechanical vibration into supports,
- thermal convection and buoyancy,
- electrostatic and magnetic coupling.

The OPH theory behind the lab is simple in words. OPH starts from finite observers with finite access. Each observer has a local patch, keeps records, compares only the boundary data exposed on overlaps, repairs mismatches, and settles into the public fixed point that survives those comparisons. That is the basic observer-overlap picture in the [OPH repository](https://github.com/FloatingPragma/observer-patch-holography), the [Observers Are All You Need source](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/observers_are_all_you_need.tex), and [Reality as Consensus Protocol](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/reality_as_consensus_protocol.tex).

For this project, an observer does not mean a person watching the experiment. It means a physical system with limited information, local records, and boundaries where information can be compared. A lab object can imitate a tiny version of that structure if it has drive ports, read ports, memory, and a feedback rule.

The undergraduate picture is this:

1. The plate is driven, like tapping a bell in a controlled pattern.
2. The plate listens to its own ringdown through its ports.
3. The controller stores that response as a record.
4. The next drive packet depends on the stored record.
5. A scorebook checks whether those records predict later responses better than shuffled records.
6. Separate top and bottom zones are scored independently.
7. The balance asks whether any remaining force follows the signed top/bottom score.

The novel step for this student package is to ask whether a small lab object can implement the same primitive in hardware. The object has ports, internal modes, onboard records, and a repair loop. In OPH language, it is a tiny bounded patch carrier. The hardware discipline comes from [Federated Echosahedral Screen Microphysics](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/screen_microphysics_and_observer_synchronization.tex), which treats ports, records, repair interfaces, checkpoints, and public evidence bundles as the relevant engineering surface.

The OPH/chi_nu idea asks for a stricter object than a vibrating plate. **The object must be a bounded, self-reading test article: it drives a mode, reads the response through the same or co-located ports, records the response onboard, lets that record change later drive packets, predicts later boundary response better than shuffled controls, and creates a signed top/bottom coherence contrast.** The proposed residual force is then tested against that internally measured contrast.

The load-bearing theory branch for this package is versioned in [theory_branch.yaml](theory_branch.yaml). It uses the canonical linear top/bottom continuation described in the [OPH dark matter paper](https://github.com/FloatingPragma/observer-patch-holography/blob/main/extra/oph_dark_matter_paper.tex) and the [chi_nu susceptibility bounds source](https://github.com/FloatingPragma/observer-patch-holography/blob/main/extra/chi_nu_susceptibility_bounds.tex). It says that a canonical vertical coherence contrast in a bounded article may couple to the local gravitational support channel:

```text
delta_S_can = S_can_bottom - S_can_top
F_chi = (g0^2 / (4 * pi * G)) * A_perp * chi_can * delta_S_can
```

In words, the branch formula says that a signed top/bottom coherence contrast could contribute a small vertical support force. The effect would scale with the horizontal area of the bounded article, the local gravitational scale, the branch susceptibility, and the signed contrast. The sign comes from which side has the stronger self-read consistency.

The scorebook does not measure `delta_S_can`. It measures `delta_S_hat`, an operational self-read proxy. The proxy threshold of about `0.05` is a state-classification margin only. Without a public bridge `delta_S_can = kappa_S * delta_S_hat`, the quantitative output is `K_S_hat = F_residual / (q * delta_S_hat)`, not `chi_can`.

`delta_S_can` is the theory-side symbol. `delta_S_hat` is the lab-side measurement. Students measure `delta_S_hat` because it is built from real logs: port voltages, ringdown features, prediction errors, and live-feedback records. The experiment can report an empirical coefficient using `delta_S_hat`. It cannot report the canonical susceptibility `chi_can` unless a separate calibration bridge is supplied.

The mechanism is not one observer fooling another observer into thinking the object is lighter. In OPH language, the article is trying to become a small self-consistent patch. Its ports write and read a boundary record. The live controller repairs the next drive packet from that record. If the lower face and upper face settle into different record quality, the article has a vertical asymmetry in its own self-read consistency. The chi_nu continuation says that this asymmetry can load the local gravitational support channel. Bottom-more-coherent gives one sign of apparent support force. Top-more-coherent gives the opposite sign.

In ordinary lab language, the candidate effect would look like a tiny signed change in support force. It would have to follow the internal self-read score, reverse when top and bottom are swapped, and vanish when the same waveform is replayed without live record use. That last requirement matters because a replay keeps ordinary vibration and sound close to the live run while removing the causal self-read relation.

That is the OPH-specific part. Ordinary acoustics cares about pressure, momentum flux, heat, vibration, charge, and magnetic fields. The proposed OPH term cares about a causal self-read receipt: the record must predict the boundary, the record must change the next drive packet, and the signed top/bottom proxy score must survive the frozen scorebook.

`S_hat_top` and `S_hat_bottom` are scorebook proxy values derived from the self-read records. Raw loudness, vibration amplitude, and acoustic pressure remain ordinary artifact channels. `A_perp` is the projected horizontal area, `g0` is local gravitational acceleration, and `chi_can` is the branch susceptibility discussed in the chi_nu bounds paper. The compact recovery stack that separates recovered OPH core claims from continuation claims is in the [compact technical source](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/recovering_relativity_and_standard_model_structure_from_observer_overlap_consistency_compact.tex). The hover-disk energy-gradient and UFO vertex-sharing formulas remain exploratory context for this package unless a separate bridge is supplied.

In the lab, the students create the candidate state by making the lower vertical zone settle into a higher self-read proxy score than the upper zone, then reversing that relation for `ACTIVE_MINUS`. The `LIVE` controller is important because the record changes the next drive packet. `OPEN_LOOP_REPLAY` repeats a prior live waveform while ignoring the new records. `CAUSAL_SHUFFLE` feeds shuffled records into the live controller and allows the waveform to change. `YOKED_SHUFFLE_REPLAY` replays that shuffled waveform open-loop. The balance test asks whether a force tracks `q * delta_S_hat`, reverses under `ACTIVE_MINUS`, reverses when the article is inverted about a horizontal axis, and disappears in sham, dummy, open-loop replay, and yoked-shuffle replay controls.

No student build should assume the residual exists. A clean conventional force map plus an upper bound is the expected successful result.

Quick glossary:

- Port: one transducer channel that can drive the object, read the object, or both.
- Mode: a repeatable vibration shape of the plate, bowl, lid, or cymbal.
- Ringdown: the vibration left after a drive pulse stops.
- Record: the saved sensor response from a drive/read cycle.
- Live feedback: a controller rule where the next drive packet depends on the latest record.
- Replay: a recorded packet sequence sent again while new records are logged and ignored.
- Shuffled record: a control record with the order disturbed, so timing information is broken.
- Self-read score: the frozen scorebook number that says how well the article predicts its own later boundary response.
- Top/bottom contrast: lower-zone self-read score minus upper-zone self-read score.
- Residual force: the force left after the declared conventional effects and controls are accounted for.

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
- packet-level drive, record, and terminal voltage/current hashes,
- signed `ACTIVE+` and `ACTIVE-` phase patterns,
- analytical-balance measurement for vertical support force,
- pendulum measurement for horizontal acoustic recoil and artifact mapping,
- electrical dummy, mechanical active twin, and matched-power sham runs.

Expected conventional result:

The plate will show resonances, ringdown, cross-coupling, acoustic leakage, and thermal artifacts. A pendulum may deflect from acoustic radiation pressure or air motion. A balance may show apparent mass changes from heat, electrostatics, vibration, and drift. Those effects should track frequency, amplitude, orientation, shielding, and temperature in conventional ways.

Claim condition:

A candidate residual requires a frozen scorebook, `LIVE` versus `OPEN_LOOP_REPLAY` separation, `CAUSAL_SHUFFLE` and `YOKED_SHUFFLE_REPLAY` controls, sign reversal, horizontal-axis physical inversion for top/bottom exchange, electrical dummy rejection, mechanical active twin rejection, matched-power sham rejection, and no explanatory correlation with temperature, electrostatics, magnetics, vibration leakage, or handling. It is not a canonical chi-nu measurement without a proxy-to-canonical bridge.

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
2. Valid OPH primitive: two physical vertical zones, reversible ports, live record-conditioned feedback, frozen scorebook, and a demonstrated signed `S_hat_bottom - S_hat_top`.
3. Causal self-read ablation: `LIVE` feedback versus `OPEN_LOOP_REPLAY`, `CAUSAL_SHUFFLE`, and `YOKED_SHUFFLE_REPLAY` controls.
4. Verifier lock: scorebook hash, manifest hash, firmware hash, waveform hash, packet log schema, analysis lockfile, and executable verifier hash.
5. Vertical force test: whole self-contained article on a balance, randomized blinded blocks, true top/bottom inversion, and no external cables.
6. Artifact escalation: pressure sweep, enclosure-geometry sweep, electromagnetic and thermal perturbations, electrical dummy, and mechanical active twin.
7. Independent replication: another balance type, another operator, another lab, and a second geometry with a preregistered area or scalar-scaling prediction.

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
- a passing executable verifier output,
- raw logs and analysis scripts,
- clean conventional force curves,
- a matched dummy,
- a reported residual or upper bound.

The publication-grade result is a receipt bundle, not a dramatic video.
