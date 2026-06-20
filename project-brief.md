# Student Project Brief

## One-Sentence Project

Build a battery-powered, instrumented coherent vibration body, measure its ordinary acoustic forces, and place an upper bound on any sign-reversible residual force after controls.

OPH's recovered core leaves coherent-matter force as work in progress. The
tested force law belongs to a conditional continuation branch. Existing
internal program measurements are reported as null. These builds teach
conventional force metrology and test an explicitly speculative continuation.

The OPH differentiator in this package is the instantiation of an
observer-like self-reading system. The test article must be bounded, drive and
read its own boundary response, store records, use those records in live
feedback, and expose a receipt that can be checked against replay, shuffled,
dummy, and flip controls.

## Why It Is Expected To Work

Piezoelectric transducers convert voltage into strain. Bond one to a plate, lid,
or cymbal, and the part becomes a small driven instrument. Some frequencies
ring cleanly because the object has natural modes. Near those modes, a small
electrical signal can create a larger mechanical motion.

That motion produces ordinary forces by ordinary physics:

- acoustic radiation pressure in air,
- squeeze-film pressure close to a nearby surface,
- direct mechanical vibration into supports,
- thermal convection and buoyancy,
- electrostatic and magnetic coupling.

Students should expect to see those effects first. A good first week in the lab
is a resonance map, a temperature log, and a force curve that changes with
frequency, standoff, and drive amplitude.

The OPH theory behind the lab is simple in words. OPH starts from finite observers with finite access. Each observer has a local patch, keeps records, compares only the boundary data exposed on overlaps, repairs mismatches, and settles into the public fixed point that survives those comparisons. That is the basic observer-overlap picture in the [OPH repository](https://github.com/FloatingPragma/observer-patch-holography), [Observers Are All You Need](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/observers_are_all_you_need.pdf), and [Reality as Consensus Protocol](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/reality_as_consensus_protocol.pdf).

For this project, an observer is a physical system with limited information,
local records, and boundaries where information can be compared. A lab object
can imitate a tiny version of that structure if it has drive ports, read ports,
memory, and a feedback rule.

The undergraduate picture is this:

1. The plate is driven, like tapping a bell in a controlled pattern.
2. The plate listens to its own ringdown through its ports.
3. The controller stores that response as a record.
4. The next drive packet depends on the stored record.
5. A scorebook checks whether those records predict subsequent responses better than shuffled records.
6. Separate top and bottom zones are scored independently.
7. The balance asks whether any remaining force follows the signed top/bottom score.

The useful mental model is a musical instrument with a notebook. The drive
packet is the tap. The ringdown is the sound. The controller writes down what
happened and chooses the next tap. The scorebook checks whether the notebook
actually helps predict the instrument.

The novel step for this student package is to ask whether a small lab object can implement the same primitive in hardware. The object has ports, internal modes, onboard records, and a repair loop. In OPH language, it is a tiny bounded patch carrier. The hardware discipline comes from [Screen Microphysics And Observer Synchronization](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/screen_microphysics_and_observer_synchronization.pdf), which treats ports, records, repair interfaces, checkpoints, and public evidence bundles as the relevant engineering surface.

The OPH/chi_nu idea needs a bounded, self-reading test article. The object
drives a mode, reads the response through the same or co-located ports, records
the response onboard, lets that record change following drive packets, predicts
subsequent boundary response better than shuffled controls, and creates a signed
top/bottom coherence contrast. The proposed residual force is tested against
that internally measured contrast.

`P ~= 1.6309682` gives the build a fixed OPH geometry ruler. The idea is simple:
build one article with the P ratio in the port or dish layout, then build a
matched detuned article with the ratio shifted. If P matters, the P-coded
article should give a cleaner self-read receipt under the same power, mass, and
logging. The manifest records the exact ratio, measured value, tolerance,
geometry file, and detuned control.

Use these defaults unless the supervisor approves a different written P ratio:

- Plate: `active_body_long_span_mm / p_port_centroid_separation_mm = P`.
  On a 100 mm long plate, put the in-plane P-port centroids 61.31 mm apart on
  each instrumented face. On an 80 mm long plate, put them 49.05 mm apart.
- Cymbal or dish: `dish_active_radius_mm / transducer_ring_radius_mm = P`.
  On a 200 mm diameter dish with 100 mm usable radius, place the transducer ring
  at 61.31 mm radius.

The detuned control must move the same ratio at least 5 percent away from `P`
while keeping mass, drive electronics, power, handling, and logging as similar
as practical. A simple default is ratio `1.50`, which gives 66.67 mm P-port
centroid separation for a 100 mm plate and 66.67 mm ring radius for a 200 mm
dish.

Any P-dependent residual claim has to pass an extra check: the force residual
tracks the P-coded self-read contrast and weakens or vanishes in the detuned
geometry, replay, shuffled-record, dummy, and physical flip controls. The
background number `exp(-P/12) ~= 0.873` is a theoretical coupling ceiling inside
the continuation branch. Student balance results use measured force data.

The load-bearing theory branch for this package is versioned in [theory_branch.yaml](theory_branch.yaml). It uses the canonical linear top/bottom continuation described in the [OPH dark matter paper](https://github.com/FloatingPragma/observer-patch-holography/blob/main/extra/oph_dark_matter_paper.pdf) and the [chi_nu susceptibility bounds paper](https://github.com/FloatingPragma/observer-patch-holography/blob/main/extra/chi_nu_susceptibility_bounds.pdf). It says that a canonical vertical coherence contrast in a bounded article may couple to the local gravitational support channel:

```text
delta_S_can = S_can_bottom - S_can_top
F_chi = (g0^2 / (4 * pi * G)) * A_perp * chi_can * delta_S_can
```

In words, the branch formula says that a signed top/bottom coherence contrast could contribute a small vertical support force. The effect would scale with the horizontal area of the bounded article, the local gravitational scale, the branch susceptibility, and the signed contrast. The sign comes from which side has the stronger self-read consistency.

The scorebook measures `delta_S_hat`, an operational self-read proxy. The proxy
threshold of about `0.05` is a state-classification margin. A public bridge
`delta_S_can = kappa_S * delta_S_hat` is required before the result can be
reported as the canonical susceptibility `chi_can`. The lab output is
`K_S_hat = F_residual / (q * delta_S_hat)`.

`delta_S_can` is the theory-side symbol. `delta_S_hat` is the lab-side
measurement. Students measure `delta_S_hat` because it is built from real logs:
port voltages, ringdown features, prediction errors, and live-feedback records.
The experiment can report an empirical coefficient using `delta_S_hat`. A
canonical susceptibility claim needs a separate calibration bridge.

In OPH language, the article is a small self-consistent patch. Its ports write
and read a boundary record. The live controller repairs the next drive packet
from that record. If the lower face and upper face settle into different record
quality, the article has a vertical asymmetry in its own self-read consistency.
The chi_nu continuation says that this asymmetry can load the local
gravitational support channel. Bottom-more-coherent gives one sign of apparent
support force. Top-more-coherent gives the opposite sign.

In ordinary lab language, the candidate effect looks like a tiny signed change
in support force. It follows the internal self-read score, reverses when top and
bottom are swapped, and vanishes when live record use is removed from the same
waveform. The replay is useful because it keeps ordinary vibration and
sound close to the live run while removing the causal self-read relation.

The OPH-specific receipt is causal self-read: the record predicts the boundary,
the record changes the next drive packet, and the signed top/bottom proxy score
survives the frozen scorebook. Ordinary pressure, momentum flux, heat,
vibration, charge, and magnetic fields are measured as artifact channels.

`S_hat_top` and `S_hat_bottom` are scorebook proxy values derived from the
self-read records. Raw loudness, vibration amplitude, and acoustic pressure
remain ordinary artifact channels. `A_perp` is the projected horizontal area,
`g0` is local gravitational acceleration, and `chi_can` is the branch
susceptibility discussed in the chi_nu bounds paper. The compact recovery stack
separates recovered OPH core claims from continuation claims. The hover-disk
energy-gradient and UFO vertex-sharing formulas are exploratory context for
this package.

In the lab, the students create the candidate state by making the lower vertical zone settle into a higher self-read proxy score than the upper zone, then reversing that relation for `ACTIVE_MINUS`. The `LIVE` controller is important because the record changes the next drive packet. `OPEN_LOOP_REPLAY` repeats a prior live waveform while ignoring the new records. `CAUSAL_SHUFFLE` feeds shuffled records into the live controller and allows the waveform to change. `YOKED_SHUFFLE_REPLAY` replays that shuffled waveform open-loop. The balance test asks whether a force tracks `q * delta_S_hat`, reverses under `ACTIVE_MINUS`, reverses when the article is inverted about a horizontal axis, and disappears in sham, dummy, open-loop replay, and yoked-shuffle replay controls.

A clean conventional force map plus an upper bound is the expected successful
result.

Quick glossary:

- Port: one transducer channel that can drive the object, read the object, or both.
- Mode: a repeatable vibration shape of the plate, bowl, lid, or cymbal.
- Ringdown: the vibration left after a drive pulse stops.
- Record: the saved sensor response from a drive/read cycle.
- Live feedback: a controller rule where the next drive packet depends on the latest record.
- Replay: a recorded packet sequence sent again while fresh records are logged and ignored.
- Shuffled record: a control record with the order disturbed, so timing information is broken.
- Self-read score: the frozen scorebook number that says how well the article predicts its own subsequent boundary response.
- Top/bottom contrast: lower-zone self-read score minus upper-zone self-read score.
- Residual force: the force left after the declared conventional effects and controls are accounted for.

## Does The Hardware Work?

Yes, for conventional measurements. The plate and cymbal rigs should produce resonant modes, ringdown, phase-dependent vibration, acoustic leakage, heat, and measurable artifact paths if the sensors are sensitive enough.

The source material defines a hypothesis and a control protocol. Student plates,
pot lids, cymbals, and bowls produce a new-force result only with a passing
receipt bundle.

## Recommended Versions

### Version 1: Piezo-Crystal Plate Balance And Pendulum

Best for a first student team. It uses low mass, low voltage, simple mechanics, and good measurement discipline.

Main deliverables:

- active plate with four to twelve piezo drive/read ports,
- declared geometry: top/bottom zones for balance mode, or left/right zones for pendulum mode,
- declared P status: P-coded ratio plus detuned control for every build,
- onboard battery and logger,
- resonance and coupling matrix,
- packet-level drive, record, and terminal voltage/current hashes,
- signed `ACTIVE+` and `ACTIVE-` phase patterns,
- analytical-balance measurement for vertical support force,
- pendulum measurement for horizontal acoustic recoil and artifact mapping,
- electrical dummy, mechanical active twin, and matched-power sham runs.

Expected conventional result:

The plate will show resonances, ringdown, cross-coupling, acoustic leakage, and
thermal artifacts. A pendulum may deflect from acoustic radiation pressure or
air motion. A balance may show apparent mass changes from heat, electrostatics,
vibration, and drift. Those effects should track frequency, amplitude,
orientation, shielding, and temperature in conventional ways.

Claim condition:

A candidate residual requires a frozen scorebook, `LIVE` versus
`OPEN_LOOP_REPLAY` separation, `CAUSAL_SHUFFLE` and `YOKED_SHUFFLE_REPLAY`
controls, sign reversal, horizontal-axis physical inversion for top/bottom
exchange, electrical dummy rejection, mechanical active twin rejection,
matched-power sham rejection, and no explanatory correlation with temperature,
electrostatics, magnetics, vibration leakage, or handling. Canonical chi-nu
measurement requires a proxy-to-canonical bridge.

### Version 2: Acoustic Cymbal Bench Rig

Best as a second project after Version 1. It is mechanically louder, stronger, and less forgiving.

Main deliverables:

- one-dish calibration rig,
- four-dish bench platform with no rider and no free-flight claim,
- twelve phase-locked drive channels,
- independent top and bottom self-read zones for any OPH-style force test,
- declared P-coded geometry/readback ratio and detuned control before any
  OPH-style residual-force claim,
- conventional B0 acoustic force geometry and closed-system B0-net geometry,
- force versus standoff, frequency, phase, and amplitude curves,
- temperature and accelerometer logs,
- safety enclosure and remote kill switch.

Expected conventional result:

Near-field acoustic levitation can produce measurable force close to a smooth
reflecting surface. The strongest ordinary signal should depend sharply on
standoff distance, drive amplitude, resonance, surface reflectivity, and
acoustic leakage. Student hardware should be treated as milligram-force to
gram-force class until measured. Literature-class squeeze-film systems can
reach larger sub-newton forces. A pot lid or cymbal needs its own force curve.

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

A good student project requires:

- a working active test article,
- reproducible resonance and coupling data,
- a frozen run manifest,
- a frozen machine-readable scorebook,
- a passing executable verifier output,
- raw logs and analysis scripts,
- clean conventional force curves,
- a matched dummy,
- a reported residual or upper bound.

The publication-grade result is a receipt bundle. A video is outreach.
