# Anti-Gravity Student Experiments

This repository gives students two concrete lab builds for testing small force effects from coherent vibration systems. The Markdown files in the root directory are the working instructions. The `reference/` folder contains background papers, source articles, and supplemental theory material.

The OPH part is the observer-like self-reading system: a bounded test article
with ports, local readback, records, live feedback, and a public receipt showing
whether its own boundary records predict subsequent boundary response.

## Build Path

Start with the small plate. Move to the acoustic bench rig after the measurement and control discipline is solid.

1. [Project Brief](project-brief.md)
   Short explanation of the idea, claim boundaries, student goals, and expected deliverables.

2. [Theory Branch](theory_branch.yaml)
   Versioned source of truth for the conditional force law used by this package. It separates the operational proxy `delta_S_hat` from the canonical scalar `delta_S_can`.

3. [Build 01: Piezo-Crystal Plate Balance And Pendulum](build-01-piezo-plate-balance-and-pendulum.md)
   Cheap, safe at low voltage, quick to instrument, and the best place to learn the control protocol. The analytical balance is the primary vertical support-force readout. The pendulum is a horizontal calibration and artifact-mapping readout.

4. [Build 02: Acoustic Cymbal Bench Rig](build-02-acoustic-cymbal-bench-rig.md)
   Bench-scale cymbal, pot-lid, or bowl rig. The required entry stage is a single-dish calibration station. The four-dish platform comes after force curves, resonance maps, standoff maps, and safety checks are complete.

5. [Controls And Data Protocol](controls-and-data-protocol.md)
   Sham runs, dummy runs, sign reversal, physical flips, thermal controls, artifact rejection, and data columns.

6. [Templates](templates/)
   `run_manifest_template.yaml`, `scorebook_template.json`, `scorebook_b0_nfal_template.json`, `scorebook_b0_net_template.json`, and `data_columns.csv` give students fixed logging and scoring formats.

7. [Analysis verifier](analysis/)
   Executable scorebook verifier, schemas, ABBA balance helper, Allan deviation helper, and synthetic test runs.

Read the root `.md` files directly in GitHub. Reference material and external source links appear under `reference/`.

## Basic Idea

The experiments drive resonant plates or dishes in controlled phase patterns, read back their vibrational state, and compare active states against sham, dummy, sign-reversed, replay, record-shuffled, and physically flipped controls.

The ordinary physics is simple. A piezo bends when voltage is applied. A plate
or dish has favorite vibration shapes. Near one of those shapes, a small drive
can make a much larger motion. That motion pushes on air, heats parts, shakes
supports, and can move a balance or pendulum through familiar mechanisms. The
first job is to map those familiar mechanisms clearly.

The first OPH task is a self-reading object. The device drives itself, reads its
own response, records that response, uses the record in live feedback, and
passes the frozen scorebook against replay and shuffled controls.

`P ~= 1.6309682` is mandatory because it gives every build the same OPH
geometry ruler. The ratio goes into the port layout or dish layout, then the
students measure it after assembly. The detuned twin uses the same mass, power,
and logging with the P ratio shifted. If the OPH geometry matters, the P-coded
article should produce a cleaner self-read receipt than the detuned twin.

Default encodings are fixed in the build guides. For the plate, set the active
body span divided by the in-plane P-port centroid separation to `P` on the top
and bottom faces. For the cymbal or dish, set the usable dish radius divided by
the transducer ring radius to `P`. Record the measured ratio and a detuned
control before force data are viewed.

Plain-language map:

- A piezo is an electrical part that bends a little when voltage is applied.
- A plate, lid, bowl, or cymbal has natural vibration patterns called modes.
- A coherent state means the ports are driven with controlled timing, like a small orchestra staying in phase.
- A self-read record means the same device also listens to its own vibration after each drive packet.
- Live feedback means the device uses that record to choose the next packet.
- The top/bottom score asks whether the lower side is more predictably self-reading than the upper side, or the other way around.
- The force test asks whether a balance reading follows that signed score after ordinary acoustic, thermal, electrical, and mechanical effects are removed.

The direct OPH-style force test is vertical. It requires separately measured upper and lower zones, a frozen proxy scalar for `S_hat_bottom - S_hat_top`, live record-conditioned feedback, and a physical inversion around a horizontal axis. Horizontal pendulum measurements remain useful for acoustic recoil, torque, and artifact mapping.

Ordinary acoustic and vibration effects are expected. A useful student result
is a conventional force map with clean controls or an upper bound on any
residual that tracks the self-read coherent state and reverses sign under the
planned controls.

## Claim Boundaries

- Conventional acoustic force is expected and useful. Piezo plates, pot lids, bowls, cymbals, and ultrasonic arrays can produce measurable radiation pressure, squeeze-film forces, vibration coupling, heat, and electrostatic artifacts.
- The OPH `chi_nu` effect is a hypothesis under test. This package makes no positive force claim.
- `P` sets the design and readback calibration. Balance data, live/replay
  separation, and artifact controls decide the force result.
- The package tests a downstream OPH `chi_nu` hypothesis. OPH and local gravity
  manipulation require separate evidence.
- Human-carrying acoustic hover is outside the student scope. The included antigravity survey marks human-scale free-air acoustic hover as excluded by acoustic intensity, wavelength, and safety limits. The cymbal build is a bench force platform and coherence-body test article.

## Background References

Use the root build guides as the lab manuals. Use [reference/](reference/) for source material and context.

- [Reference guide](reference/README.md)
- [Hacking the Simulation: Anti-Gravity Exploit](https://github.com/FloatingPragma/observer-patch-holography/blob/main/extra/hacking-the-simulation-anti-gravity-exploit.pdf)
- [Antigravity Devices survey](reference/build-source/antigravity_devices.html)
- [Main OPH paper PDFs](https://github.com/FloatingPragma/observer-patch-holography/tree/main/paper)
- [Supplemental OPH PDF papers](https://github.com/FloatingPragma/observer-patch-holography/tree/main/extra)

Core OPH papers for supervisors and motivated students:

- [Observers Are All You Need](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/observers_are_all_you_need.pdf)
- [Reality as Consensus Protocol](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/reality_as_consensus_protocol.pdf)
- [Screen Microphysics And Observer Synchronization](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/screen_microphysics_and_observer_synchronization.pdf)
- [Compact OPH Recovery Paper](https://github.com/FloatingPragma/observer-patch-holography/blob/main/paper/recovering_relativity_and_standard_model_structure_from_observer_overlap_consistency_compact.pdf)

Public links:

- [Blog article](https://blog.floatingpragma.io/hacking-the-simulation-anti-gravity-exploit)
- [Public overview](https://omega.floatingpragma.io/antigravity)
- [NotebookLM for questions](https://notebooklm.google.com/notebook/d5249760-6ce8-44a0-927b-ccf90402711a)

Legacy filenames redirect to the corrected build guides. Use the root build
guides as the lab manuals.
