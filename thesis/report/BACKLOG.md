# Experiment backlog

Candidate experiments, each framed as *observation → engine concept → runnable model → the counterpoint to beat*.
Prior art must be searched before any of these is described as new.

| id | observation | engine / CS concept | model idea | known counterpoint / prior art to check |
|---|---|---|---|---|
| 003 | Quantum tunnelling | *reframed:* the barrier isn't an object, it's a **field** (an energy hill in mostly empty space), so bullet-through-paper is the wrong picture. Candidate: the engine stores a particle as a probability cloud and resolves its position by **sampling the cloud**; part of the cloud already sits past the hill | show the cloud "leaking" through the hill, with odds falling exponentially with width × √mass | needs a better engine analogy; open for discussion |
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
| 015 | Space "stretches" near mass (the other half of light bending) | energy allocates more space: adding energy grows the grid | measure the extra volume a toy engine adds per unit energy vs. GR's **excess radius** (Feynman Lectures II §42: δr ≈ GM/3c²) | author's idea: universe size as a function of energy. Relate to cosmic expansion carefully, since local excess radius ≠ cosmological expansion |
| 016 | Our universe is inside a black hole | a child simulation spawned inside a parent's saturated region | compare horizon/entropy scaling and the "cosmological natural selection" predictions | prior art: Pathria 1972; Smolin 1992; Popławski 2010 (verify all before use) |
| 017 | Dependency-scoped rollback (from 001 §4b) | Time Warp-style rollback limited to causally dependent processes | rollback cost vs. entanglement graph size and decoherence horizon | entanglement shows no distance decay, so scope must be graph-based |
