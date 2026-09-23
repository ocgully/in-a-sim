# Experiment backlog

Candidate experiments, each framed as *observation → engine concept → runnable model → the counterpoint to beat*.
Prior art must be searched before any of these is described as new.

| id | observation | engine / CS concept | model idea | known counterpoint / prior art to check |
|---|---|---|---|---|
| 003 | Quantum tunnelling | **bullet-through-paper**: discrete collision checks miss thin walls at large timesteps | a particle vs. a barrier at varying tick size, compared with the real tunnelling probability's dependence on barrier width and mass | tunnelling is exponential in width × √mass and exists in continuous QM. Can a timestep model get the *functional form*? |
| 004 | Speed of light as a universal limit | max propagation per tick in a cellular automaton | CA light cones; show that "c" is a property of neighbour updates | Whitworth 2008; Fredkin; Wolfram. The hard part is **Lorentz invariance**, which lattices break (Beane–Davoudi–Savage bounds) |
| 005 | Special-relativistic time dilation | per-entity update budget split between moving and ticking internally | reproduce γ = 1/√(1−v²/c²) from a budget rule | Wolfram 2024 does this for motion. Credit and compare |
| 006 | Black holes & the Bekenstein bound | a storage cap per region; horizon = 100% saturation | frame-rate → 0 at saturation, and information scaling with area | holographic principle literature |
| 007 | Objective collapse = garbage collection under memory pressure | GC triggered by branch size | a GRW/CSL-like collapse rate ∝ mass; plot against current experimental bounds | GRW/CSL, Diósi–Penrose; underground and interferometry bounds |
| 008 | Randomness of quantum outcomes | seeded PRNG vs. true RNG | run statistical test batteries on public quantum RNG data vs. a PRNG; what *could* distinguish them? | no finite statistical test can prove true randomness. Kolmogorov complexity |
| 009 | Identical particles | object instancing / flyweight pattern | why every electron is identical; exchange statistics as "same instance" | Wheeler's one-electron universe |
| 010 | Conservation laws | invariants / checksums enforced by the engine | Noether's theorem vs. engine invariants | symmetry is the real origin (Noether). The analogy may be backwards |
| 011 | Planck scale as resolution | floating-point precision / fixed-point grid | precision loss far from origin ("far lands" in Minecraft) vs. homogeneous physics everywhere | the universe shows **no** preferred origin. A strong counterpoint |
| 012 | Arrow of time & entropy | append-only log; cheap forward / expensive reverse | irreversibility as a compute asymmetry | Landauer's principle; Bennett's reversible computing |
| 013 | Quantum Zeno effect | polling a state resets it ("a watched pot") | frequent measurement freezes evolution, like a polling loop re-committing state | well-established physics. Map carefully |
| 014 | Dark energy / expansion | memory allocation growing over time | toy "allocate new cells" universe vs. measured expansion history | pure analogy risk. Check whether it predicts anything |
