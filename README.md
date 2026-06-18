# Anti-Gravity Student Experiments

Status: student lab package, research draft  
Prepared: 2026-06-18  
Audience: Krit's student project group at Chiang Mai University

This repository gives students two concrete lab builds for testing small force effects from coherent vibration systems. The files in the root directory are the working instructions. The `reference/` folder contains background papers, source articles, and supplemental theory material.

## Build Path

Start with the small plate. Move to the acoustic bench rig after the measurement and control discipline is solid.

1. [Project Brief](project-brief.md)  
   Short explanation of the idea, claim boundaries, student goals, and expected deliverables.

2. [Build 01: Piezo-Crystal Plate Pendulum](build-01-piezo-crystal-plate-pendulum.md)  
   Cheap, safe at low voltage, quick to instrument, and the best place to learn the control protocol. This build measures pendulum deflection from a self-reading resonant plate.

3. [Build 02: Acoustic Cymbal Hoverboard Bench Rig](build-02-acoustic-cymbal-hoverboard-bench.md)  
   Bench-scale cymbal, pot-lid, or bowl rig. The required entry stage is a single-dish calibration station. The four-dish platform comes after force curves, resonance maps, standoff maps, and safety checks are complete.

4. [Controls And Data Protocol](controls-and-data-protocol.md)  
   Sham runs, dummy runs, sign reversal, physical flips, thermal controls, artifact rejection, and data columns.

5. [Templates](templates/)  
   `run_manifest_template.yaml` and `data_columns.csv` give students a fixed logging format.

The same documents are compiled as PDFs in [pdf/](pdf/).

## Basic Idea

The experiments drive resonant plates or dishes in controlled phase patterns, read back their vibrational state, and compare active states against sham, dummy, sign-reversed, and physically flipped controls.

Ordinary acoustic and vibration effects are expected. The experiment asks a narrower question: after those effects are mapped and rejected, is there any repeatable residual force that tracks the self-read coherent state and reverses sign under the planned controls?

## Claim Boundaries

- Conventional acoustic force is expected and useful. Piezo plates, pot lids, bowls, cymbals, and ultrasonic arrays can produce measurable radiation pressure, squeeze-film forces, vibration coupling, heat, and electrostatic artifacts.
- The OPH `chi_nu` effect is a hypothesis under test. This package makes no positive force claim.
- Human-carrying anti-gravity is outside the student scope. The cymbal build is a bench force platform and coherence-body test article. It is not a rider vehicle.

## Background References

Use the root build guides as the lab manuals. Use [reference/](reference/) for source material and context.

- [Reference guide](reference/README.md)
- [Hacking the Simulation: Anti-Gravity Exploit PDF](reference/build-source/hacking-the-simulation-anti-gravity-exploit.pdf)
- [Antigravity Devices survey](reference/build-source/antigravity_devices.html)
- [DIY hoverboard cymbal source](reference/build-source/diy-hoverbike-four-cymbals.pdf)
- [Supplemental theory papers](reference/supplemental-theory/)

Public links:

- [Blog article](https://blog.floatingpragma.io/hacking-the-simulation-anti-gravity-exploit)
- [Public overview](https://omega.floatingpragma.io/antigravity)
- [NotebookLM for questions](https://notebooklm.google.com/notebook/d5249760-6ce8-44a0-927b-ccf90402711a)
