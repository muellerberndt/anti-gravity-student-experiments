# Anti-Gravity Student Experiments

Status: student lab package, research draft
Prepared: 2026-06-18
Audience: Krit's student project group at Chiang Mai University

This repository gives students two concrete lab builds for testing small force effects from coherent vibration systems. The Markdown files in the root directory are the working instructions. The `reference/` folder contains background papers, source articles, and supplemental theory material.

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

Read the root `.md` files directly in GitHub. PDF files appear under `reference/` as source papers and background material.

## Basic Idea

The experiments drive resonant plates or dishes in controlled phase patterns, read back their vibrational state, and compare active states against sham, dummy, sign-reversed, replay, record-shuffled, and physically flipped controls.

The direct OPH-style force test is vertical. It requires separately measured upper and lower zones, a frozen proxy scalar for `S_hat_bottom - S_hat_top`, live record-conditioned feedback, and a physical inversion around a horizontal axis. Horizontal pendulum measurements remain useful for acoustic recoil, torque, and artifact mapping.

Ordinary acoustic and vibration effects are expected. A positive new-force result is not expected from these student builds. The useful result is either a conventional force map with clean controls or an upper bound on any residual that tracks the self-read coherent state and reverses sign under the planned controls.

## Claim Boundaries

- Conventional acoustic force is expected and useful. Piezo plates, pot lids, bowls, cymbals, and ultrasonic arrays can produce measurable radiation pressure, squeeze-film forces, vibration coupling, heat, and electrostatic artifacts.
- The OPH `chi_nu` effect is a hypothesis under test. This package makes no positive force claim.
- The package tests a downstream OPH `chi_nu` hypothesis. It does not prove OPH or local gravity manipulation.
- Human-carrying acoustic hover is outside the student scope. The included antigravity survey marks human-scale free-air acoustic hover as excluded by acoustic intensity, wavelength, and safety limits. The cymbal build is a bench force platform and coherence-body test article.

## Background References

Use the root build guides as the lab manuals. Use [reference/](reference/) for source material and context.

- [Reference guide](reference/README.md)
- [Hacking the Simulation: Anti-Gravity Exploit PDF](reference/build-source/hacking-the-simulation-anti-gravity-exploit.pdf)
- [Antigravity Devices survey](reference/build-source/antigravity_devices.html)
- [DIY cymbal source](reference/build-source/diy-hoverbike-four-cymbals.pdf)
- [Supplemental theory papers](reference/supplemental-theory/)

Public links:

- [Blog article](https://blog.floatingpragma.io/hacking-the-simulation-anti-gravity-exploit)
- [Public overview](https://omega.floatingpragma.io/antigravity)
- [NotebookLM for questions](https://notebooklm.google.com/notebook/d5249760-6ce8-44a0-927b-ccf90402711a)

Legacy filenames redirect to the corrected build guides. Do not use old pendulum-first or hoverboard-framed instructions.
