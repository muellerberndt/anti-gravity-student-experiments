# Email Draft To Krit

Subject: Student project proposal: piezo/acoustic anti-gravity test rigs

Hi Krit,

I would like to send you a small student-project package around two bench experiments. The phrase "anti-gravity" here should be read in the engineering sense: build a coherent vibrating body, measure every ordinary force path carefully, and then ask whether any residual support-force signal survives the controls. The student version should make no new-force claim unless the controls survive.

The basic idea is simple. A piezo-driven plate or cymbal can store coherent vibration. Conventional physics predicts several real effects from that: acoustic radiation pressure, near-field squeeze-film lift close to a surface, thermal drift, electrostatics, and vibration coupling into the support. The OPH/chi_nu hypothesis adds one extra possibility: if the object is a self-reading bounded system, with drive/read ports, onboard records, and a sign-reversible top/bottom coherence contrast, the balance or pendulum might see a small support-force term outside ordinary acoustic bookkeeping.

That is the whole reason for the experiment. First we deliberately build the conventional signal and measure it. Then we run sign flips, physical flips, dummy devices, matched-power shams, and thermal/electrostatic controls to see whether anything remains.

I suggest two versions for students:

1. Piezo-crystal plate pendulum. This is the easier version. Use an 80 x 60 mm to 100 x 100 mm quartz, alumina, glass-ceramic, sapphire, or insulated aluminum plate with four or eight piezo discs. The device runs from onboard battery power and logs its own drive/read data. Suspend it as a 1.5 to 2 m pendulum and measure deflection with a camera or laser spot. Goal: demonstrate clean resonant modes, produce a sign-reversible phase pattern, and measure whether any pendulum deflection survives sham, phase flip, physical flip, and dummy controls.

2. Acoustic cymbal hoverboard bench rig. This is the larger version. Start with one 200 to 510 mm pot lid, bowl, or cymbal, then scale to four dishes in a square frame. Each dish has three piezo or Langevin transducers at roughly 60 percent radius, driven by phase-locked channels. Goal: map conventional near-field acoustic force versus frequency, amplitude, phase, and standoff distance, then use the same rig as a high-Q coherent-body test article. This should stay a bench force platform. I would not put a person on it.

I am attaching a compact package with concrete build notes, a bill of materials, run protocol, data columns, and decision rules. The best files to start with are:

- `project-brief.md`
- `build-01-piezo-crystal-plate-pendulum.md`
- `build-02-acoustic-cymbal-hoverboard-bench.md`
- `controls-and-data-protocol.md`

The longer background material is included for context. The most useful technical background is the "Hacking the Simulation: Anti-Gravity Exploit" PDF and the "Antigravity Devices" survey, because they separate buildable acoustic lift from the unproven chi_nu hypothesis and lay out the control logic. The live article is here:

https://blog.floatingpragma.io/hacking-the-simulation-anti-gravity-exploit

The public overview page is here:

https://omega.floatingpragma.io/antigravity

For questions while reading the package, I also set up a NotebookLM with the relevant material:

https://notebooklm.google.com/notebook/d5249760-6ce8-44a0-927b-ccf90402711a

If this fits a senior project or lab course, I can help supply starter firmware and an analysis script. A good outcome is either a candidate residual with clean controls or a published upper bound. A null result is useful if the measurement is clean.

Best,

Bernhard
