# Resource Manifest

This manifest maps the repository contents. The concrete experiment designs are the root Markdown documents. The source papers and articles live under `reference/`.

## Lab Instructions

- [project-brief.md](project-brief.md)
  Short project framing, claim boundaries, and student deliverables.

- [theory_branch.yaml](theory_branch.yaml)
  Versioned source of truth for the conditional force branch used by the student package.

- [build-01-piezo-plate-balance-and-pendulum.md](build-01-piezo-plate-balance-and-pendulum.md)
  Primary student build. Use this for the low-voltage plate, self-read schedule, balance support-force measurement, pendulum artifact mapping, dummy, sham, sign reversal, and physical flip controls.

- [build-02-acoustic-cymbal-bench-rig.md](build-02-acoustic-cymbal-bench-rig.md)
  Larger bench build. Use the single-dish calibration station before the four-dish platform.

- [controls-and-data-protocol.md](controls-and-data-protocol.md)
  Shared control logic, artifact rejection, run naming, and data protocol.

- [Run manifest template](templates/run_manifest_template.yaml), [OPH proxy scorebook](templates/scorebook_template.json), [B0/NFAL scorebook](templates/scorebook_b0_nfal_template.json), [B0-net scorebook](templates/scorebook_b0_net_template.json), and [data columns template](templates/data_columns.csv)
  Fixed logging templates for each run.

- [analysis/](analysis/)
  Executable verifier, scalar computation, ABBA balance helper, Allan deviation helper, schemas, and synthetic verifier tests.

Read the root `.md` files directly in GitHub. PDF files appear under `reference/` as source papers and background material.

## Included Build Background

- [Hacking the Simulation PDF](reference/build-source/hacking-the-simulation-anti-gravity-exploit.pdf)
  Self-reading PoC logic, plate build, balance protocol, dummy design, and artifact controls.

- [Antigravity Devices HTML](reference/build-source/antigravity_devices.html)
  Claim boundaries across conventional acoustic lift, ion-wind lift, refuted claims, and the open `chi_nu` hypothesis.

- [DIY Cymbal Source PDF](reference/build-source/diy-hoverbike-four-cymbals.pdf)
  Cymbal geometry and pot-lid precursor: four dishes, three transducers per dish, 60 percent radius placement, and phase-locked drive. The human-carrying lift claim is background only and is not adopted by the lab plan.

- [Hover Disk HTML](reference/build-source/hover_disk.html)
  Materials and coherent-substrate background.

- [How To Build A UFO HTML](reference/build-source/how_to_build_a_ufo.html) and [controlled-motion PDF](reference/build-source/how-to-build-a-ufo-controlled-motion.pdf)
  Broad architecture and motivation. Use as background after the lab plan.

## Included Supplemental Theory

- [OPH dark matter paper](reference/supplemental-theory/oph_dark_matter_paper.pdf)
- [Compact OPH paper](reference/supplemental-theory/recovering_relativity_and_standard_model_structure_from_observer_overlap_consistency_compact.pdf)
- [chi_nu susceptibility bounds paper](reference/supplemental-theory/chi_nu_susceptibility_bounds.pdf)

## Public Links

- [Blog article](https://blog.floatingpragma.io/hacking-the-simulation-anti-gravity-exploit)
- [Public overview](https://omega.floatingpragma.io/antigravity)
- [NotebookLM for questions](https://notebooklm.google.com/notebook/d5249760-6ce8-44a0-927b-ccf90402711a)
- [TinyLev acoustic levitator paper](https://doi.org/10.1063/1.4989995)

## External Technical References

- [RP2040 datasheet](https://pip.raspberrypi.com/documents/RP-008371-DS-rp2040-datasheet.pdf)
  ADC input constraints and front-end design checks.

- [TI piezo sensor conditioning note](https://www.ti.com/lit/an/sloa033a/sloa033a.pdf)
  Voltage-mode and charge-amplifier piezo front-end examples.

- [HX711 datasheet](https://cdn.sparkfun.com/datasheets/Sensors/ForceFlex/hx711_english.pdf)
  Slow load-cell readout data rates and saturation behavior.

- [Controlled near-field acoustic levitation study](https://mediatum.ub.tum.de/doc/1740166/document.pdf)
  Example of fine-gap acoustic force metrology.

- [PZT material background](https://www.physikinstrumente.com/en/expertise/technology/piezo-technology/piezoelectric-materials)
  Safety context for lead zirconate titanate piezoceramics.

## First Reading Order

Point students to these root files first:

```text
README.md
project-brief.md
theory_branch.yaml
build-01-piezo-plate-balance-and-pendulum.md
build-02-acoustic-cymbal-bench-rig.md
controls-and-data-protocol.md
templates/run_manifest_template.yaml
templates/scorebook_template.json
templates/data_columns.csv
analysis/verify_scorebook.py
analysis/compute_self_read_scalar.py
analysis/run_synthetic_tests.py
```
