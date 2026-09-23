# Literature Survey: The Simulation Hypothesis

*Foundational survey for the "we-are-in-a-simulation" thought-experiment project.*
*Compiled 2026-09-23. This document reaches no conclusion. It records what has been argued, by whom, and what the standard replies are.*

**Verification policy.** Every item in the Annotated Bibliography was checked against a publisher page, arXiv, PhilPapers, or the author's own site in September 2026. Quotations marked "verbatim" were read from the primary text. Anything that could not be checked against a primary source is listed under **Unverified leads** and should not be cited as fact until it is checked.

**Terminology used here.**
- *Simulation argument* (SA): Bostrom's probabilistic trilemma. It does **not** claim we are simulated.
- *Simulation hypothesis* (SH): the claim that we actually are in a simulation.
- *Digital physics*: the separate claim that physics is, at bottom, discrete computation (Zuse, Fredkin, Wolfram). It is not about simulators, but it is often mixed up with SH.

---

## 1. Foundations

### 1.1 Historical precursors (brief)
- **Zhuangzi (late 4th c. BCE), the butterfly dream.** Zhuangzi dreams he is a butterfly and on waking cannot tell whether he is a man who dreamt of being a butterfly or a butterfly dreaming of being a man. Scholars read it as a story about perspective and transformation more than as a sceptical argument (SEP, "Zhuangzi").
- **Descartes, *Meditations on First Philosophy* (1641).** The dream argument and the "evil demon" (*genius malignus*) who could fake all sensory experience. This is the direct ancestor of the brain-in-a-vat scenario and of *The Matrix* (SEP, "Descartes' Epistemology").
- **Plato's cave** is often cited as well (e.g. Neukart et al. 2022), but it is an allegory about knowledge, not a sceptical scenario in the modern sense.

**Key difference.** The classical versions are *sceptical* (you cannot rule it out). Bostrom's version is *probabilistic* (given some assumptions, it may be likely).

### 1.2 Digital physics lineage
- **Konrad Zuse, *Rechnender Raum* (1969; MIT English translation *Calculating Space*, 1970).** This is the first book-length proposal that the universe is computed by a cellular automaton or other discrete machine. Zuse questioned whether physical law is continuous, and noted that classical entropy growth fits awkwardly with a deterministically computed universe.
- **Edward Fredkin, "Digital Mechanics" (Physica D 45, 1990).** Fredkin argued that one reversible, universal cellular automaton might model all of microscopic physics exactly. He called the idea "Finite Nature".
- **John A. Wheeler, "Information, Physics, Quantum: The Search for Links" (1989/1990).** This paper coined **"it from bit"**. Verbatim: "every it — every particle, every field of force, even the space-time continuum itself — derives its function, its meaning, its very existence entirely … from the apparatus-elicited answers to yes-or-no questions, binary choices, bits." Wheeler's "participatory universe" is an interpretive stance on quantum measurement. It does not claim that anyone is running a computer.
- **Stephen Wolfram.** *A New Kind of Science* (2002), and "A Class of Models with the Potential to Represent Fundamental Physics" (Complex Systems 29, 2020; arXiv:2004.08210). These propose hypergraph-rewriting models from which spacetime and quantum behaviour are meant to emerge.
- **Gerard 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016).** A Nobel laureate argues that quantum mechanics may be a tool for describing an underlying deterministic, classical (cellular-automaton-like) system. To stay consistent with Bell's theorem he has to invoke superdeterminism.

### 1.3 Mathematical universe
- **Max Tegmark, "The Mathematical Universe" (Found. Phys. 38, 2008; arXiv:0704.0646).** Tegmark argues that the External Reality Hypothesis implies the Mathematical Universe Hypothesis (MUH): physical reality *is* an abstract mathematical structure. He also floats the stronger "Computable Universe Hypothesis", that only computable or decidable structures exist. MUH is *not* the SH. Under MUH a simulation would be redundant, because the structure exists whether or not anyone computes it. It still sits in the same family of ideas, and Tegmark discusses simulation directly.

### 1.4 Moravec
- **Hans Moravec, "Pigs in Cyberspace" (Extropy #10, 1993; NASA NTRS copy) and "Simulation, Consciousness, Existence" (Telepolis, 1996).** These are early statements that future civilisations could run detailed simulations of minds and worlds, and that simulated beings would have no internal way to tell. They are the most direct precursor of Bostrom's framing. *(Note: some secondary sources date "Simulation, Consciousness, Existence" to 1995. Moravec's own publication list gives the Telepolis appearance as 1996.)*

### 1.5 Bostrom (2003): the trilemma, stated precisely
**Citation:** Nick Bostrom, "Are You Living in a Computer Simulation?", *Philosophical Quarterly* 53(211): 243–255 (2003). First version circulated in 2001.

**Verbatim abstract:** "at least one of the following propositions is true: (1) the human species is very likely to go extinct before reaching a 'posthuman' stage; (2) any posthuman civilization is extremely unlikely to run a significant number of simulations of their evolutionary history (or variations thereof); (3) we are almost certainly living in a computer simulation."

**Formal core (§IV).**
- Definitions:
  - *f_P* = fraction of human-level civilisations that reach a posthuman stage.
  - *f_I* = fraction of posthuman civilisations interested in running ancestor-simulations.
  - *N_I* = average number of ancestor-simulations run by an interested civilisation.
- Then: **f_sim = f_P·f_I·N_I / (f_P·f_I·N_I + 1)**.
- Because *N_I* is assumed to be astronomically large, at least one of these holds: *f_P ≈ 0*, *f_I ≈ 0*, or *f_sim ≈ 1*.

**Supporting premises.**
- *Substrate independence* (§II): the right computational structure is enough for consciousness.
- *Computational feasibility* (§III): simulating human history costs roughly **10^33–10^36 operations**. A planetary-mass computer could do about 10^42 operations per second.
- *Bland indifference principle* (§V): Cr(SIM | f_sim = x) = x, provided you have no evidence that singles you out.

**Details directly relevant to this project.** Bostrom himself uses what are now called game-engine ideas (§III):
- "Distant astronomical objects can have highly compressed representations." This is **level of detail (LOD)**.
- "The microscopic structure of the inside of the Earth can be safely omitted." This is **culling**.
- When a human is "about to make an observation of the microscopic world, it could fill in sufficient detail … on an as-needed basis." This is **render on demand / lazy evaluation**.
- "the director could skip back a few seconds and rerun the simulation in a way that avoids the problem." This is **rollback / save-state restore**, the concept behind experiment 001.

### 1.6 Chalmers, *Reality+* (2022)
**Citation:** David J. Chalmers, *Reality+: Virtual Worlds and the Problems of Philosophy* (W. W. Norton / Allen Lane, 25 Jan 2022).

- **Central thesis:** "virtual reality is genuine reality". Virtual objects are real, digital objects.
- **His version of the simulation argument** (from the author's *Précis*):
  1. If there are no *sim blockers*, most humanlike beings are sims.
  2. If most humanlike beings are sims, we are probably sims.
  3. So, if there are no sim blockers, we are probably sims.
- **What counts as a sim blocker:**
  - nonsims die first
  - nonsims choose not to make sims
  - intelligent or conscious sims are impossible
  - simulators avoid creating conscious sims
  - sims need too much computing power
- **His conclusion:** we cannot know that any sim blocker holds, so "we can't know that we are not in a simulation."
- **"It-from-bit creation hypothesis":** if we are simulated, then our world is made of bits and was created by a creator. On that view most ordinary beliefs remain *true*. The simulation hypothesis is not a sceptical hypothesis.
- Earlier statement of the non-sceptical view: Chalmers, "The Matrix as Metaphysics" (2003 web; in *Philosophers Explore the Matrix*, OUP 2005, pp. 132–176).

---

## 2. Arguments FOR (suggestive observations)

**Framing note.** None of the items below is *evidence* in the strict sense, meaning an observation that is more probable if SH is true than if it is false, with that likelihood ratio made explicit. Each is an observation that a simulation *could* explain. The standard meta-rebuttal applies to all of them: a feature that fits both "simulated" and "not simulated" equally well cannot shift the odds.

### 2.1 Finite speed of light as a maximum propagation/processing speed
- **Steelman.** Any computed world has a maximum rate at which information can move between cells. In a cellular automaton this is literally the "speed of light" of the automaton: one cell per tick. Whitworth (2008) says so directly: "The maximum speed a pixel in a virtual reality game can cross a screen is limited by the processing capacity… In our world, the fixed maximum that comes to mind is the speed of light." A universal, observer-independent speed limit looks like a hardware constant.
- **Rebuttal.**
  - Special relativity *derives* c as the invariant speed from symmetry: the Lorentz group and the relativity principle. It does not need a processor.
  - A lattice CA speed limit picks out a preferred frame, the rest frame of the grid. Our universe shows no preferred frame to very high precision (see 2.2).
  - Local causality with a finite signal speed is equally natural in non-computational field theories. So the likelihood ratio is about 1.

### 2.2 Planck scale as pixel/resolution
- **Steelman.** The Planck length (~1.6×10⁻³⁵ m) and Planck time (~5.4×10⁻⁴⁴ s) look like a minimum resolution and a tick rate. Several quantum-gravity programmes predict some kind of minimal length (Hossenfelder 2013 review).
- **Rebuttal.**
  - The Planck length is a dimensional combination of G, ħ and c. No experiment has shown that spacetime is *discrete* at that scale. It is the scale where current theories stop working, which is not the same as where pixels begin.
  - A naive pixel grid would break Lorentz invariance and give photons energy-dependent speeds. Fermi observations of GRB 090510 found no such dispersion, placing the linear-order scale above ~1.2 E_Planck (Abdo et al., *Nature* 2009).
  - Hossenfelder's review stresses that the minimal-length models that survive are carefully built so that they do *not* look like a simple grid.

### 2.3 Quantization
- **Steelman.** Energy, charge, angular momentum and spin come in discrete units. "If a world is virtual, everything in it must be digitized, and so discrete at the lowest level" (Whitworth 2008). Identical particles (every electron the same) look like instances of one class.
- **Rebuttal.**
  - In quantum mechanics, quantization comes from boundary conditions and operator spectra (eigenvalues) of continuous wave equations. A guitar string is "quantized" too.
  - Position, momentum and time remain continuous variables in standard QM.
  - Identical particles follow from quantum field theory, where particles are excitations of one field. No copy-paste is needed.

### 2.4 Quantum indeterminacy / measurement as "render on demand"
- **Steelman.** An unobserved system is described by a wavefunction, which looks like a compressed specification. A definite outcome appears only on measurement, which looks like rendering. Bostrom (2003) describes a simulator filling in microscopic detail "on an as-needed basis". Campbell, Owhadi, Sauvageau & Watkinson (2017) build a test programme on the idea that a resource-limited simulator would, "as in a video game, render content (reality) only at the moment that information becomes available for observation by a player." Quantum randomness has also been read as a call to an RNG (Whitworth 2008: "A random number function in the VR processor could provide the choices").
- **Rebuttal.**
  - "Observation" in QM means physical interaction or decoherence, not a conscious viewer. Detectors, air molecules and photons all "measure".
  - Keeping a full wavefunction is *more* expensive than keeping a definite classical state. For N entangled qubits it grows exponentially, 2^N amplitudes. Superposition therefore looks like the opposite of a cost-saving trick. This is essentially the Ringel–Kovrizhin point (§3.1).
  - Loophole-free Bell tests (Hensen et al., *Nature* 2015) rule out *local* hidden-variable schemes. Any "render" engine must be non-local, or superdeterministic in the manner of 't Hooft, which removes the naive game-engine picture.
  - Delayed-choice and quantum-eraser results are fully predicted by standard QM without any rendering step.

### 2.5 Fine-tuning
- **Steelman.** Many constants and initial conditions appear to fall inside narrow life-permitting ranges (Barnes 2012, *PASA* 29:529 reviews the cases). A designer or tuner, such as a simulator setting parameters, is one explanation.
- **Rebuttal.**
  - Other explanations exist: a multiverse plus anthropic selection, future deeper theories that fix the constants, or disputes over the probability measure (what counts as a "narrow" range is ill-defined without a prior).
  - Fine-tuning is equally an argument used for theism and for the multiverse. It does not favour SH over those alternatives.
  - Barrow (2007) turns the argument around: a simulator using approximations should produce *drifts* in constants and "glitches". Constants have been observed to be stable to high precision, which, if anything, counts slightly against a sloppy simulator.

### 2.6 The unreasonable effectiveness of mathematics (Wigner 1960)
- **Citation.** E. P. Wigner, "The Unreasonable Effectiveness of Mathematics in the Natural Sciences", *Comm. Pure Appl. Math.* 13(1), 1960. Wigner called it "something bordering on the mysterious".
- **Steelman.** If the world runs on code, it *must* be describable by compact mathematics. Simple laws are cheap to compute (Whitworth: "Calculations repeated at every point of a huge VR universe must be simple").
- **Rebuttal.**
  - Selection effects: we notice the phenomena that mathematics captures and relabel the rest as "complex systems".
  - Mathematics is partly developed *from* physics.
  - Tegmark's MUH explains the same fact *without* a simulator, and so does ordinary realism about laws.
  - Wigner himself drew no computational conclusion.

### 2.7 Holographic principle and information bounds
- **Background.**
  - Bekenstein (1981, *Phys. Rev. D* 23:287): there is a universal upper bound on entropy for a system of given energy and size.
  - 't Hooft (1993) and Susskind (1995, "The World as a Hologram", *J. Math. Phys.* 36:6377): the information in a volume scales with its boundary *area*, about one degree of freedom per Planck area.
  - Lloyd (2002, *PRL* 88:237901): the observable universe has performed at most ~10^120 operations on ~10^90 bits (~10^120 including gravitational degrees of freedom).
- **Steelman.** Reality has a finite information capacity and a finite total "compute budget". That is what you would expect of a finite machine. Holography looks like data compression, a 3-D world stored on a 2-D surface.
- **Rebuttal.**
  - These bounds are *derived inside* ordinary physics (thermodynamics, general relativity, quantum theory). They describe how much information a physical region can hold, not that some external device holds it.
  - Lloyd's paper models the universe *as* a computer as a way of counting, not as evidence that it is run by one.
  - Finite information is also predicted by non-simulation quantum gravity. Likelihood ratio about 1.

### 2.8 Error-correcting codes in supersymmetry (S. James Gates Jr.)
- **What he actually showed.** Doran, Faux, Gates, Hübsch, Iga & Landweber (arXiv:0806.0051, 2008) proved that classifying certain off-shell representations of N-extended supersymmetry (drawn as **adinkras**, graph diagrams) is equivalent to classifying quotients of N-cubes. Those quotients correspond to **doubly-even binary linear error-correcting codes**.
- **What he said publicly.** In "Symbols of Power" (*Physics World* 23(6), June 2010), Gates wrote (verbatim) that codes "play a previously unsuspected role in equations that possess the property of supersymmetry. This unsuspected connection suggests that these codes may be ubiquitous in nature, and could even be embedded in the essence of reality." He added that "we might have something in common with the Matrix science-fiction films". He also proposed that one might "Try to detect the presence of codes in the laws that describe physics." He appeared on the 2016 Asimov Memorial Debate panel "Is the Universe a Simulation?"
- **Precision check.** Popular accounts say Gates "found computer code in string theory" or "proved we live in a simulation". He did neither. The codes appear in the *mathematical classification* of supersymmetry representations. He framed the simulation link as a speculative musing, not a claim.
- **Rebuttal.**
  - Supersymmetry has *not* been observed experimentally, including at the LHC to date.
  - Binary codes are combinatorial objects that turn up wherever hypercube-like structures do. Their appearance in a classification problem does not mean anything is *performing* error correction.
  - The codes are a feature of the mathematical bookkeeping, not a demonstrated physical mechanism.

### 2.9 Vopson: information physics and "infodynamics"
- **Claims.** Vopson has published a series of papers in *AIP Advances*:
  1. the **mass–energy–information equivalence principle** (2019, 9:095206): a stored bit has mass, ~3.19×10⁻³⁸ kg at 300 K
  2. a **second law of information dynamics** (with Lepadatu, 2022, 12:075310): information entropy in some systems stays constant or *decreases* over time
  3. "The second law of infodynamics and its implications for the simulated universe hypothesis" (2023, 13:105308), which argues that the law operates across genetics, atomic physics, symmetry and cosmology, and reads it as data compression or optimisation "underpinning" SH
  4. "Is gravity evidence of a computational universe?" (2025, 15:045035), which derives Newtonian-like attraction as information-entropy minimisation
- **Steelman.** If the universe minimises information content in the way a compressor or optimiser does, that is a signature of a computational substrate. Gravity as "compute optimisation" is directly relevant to this project's experiment 002.
- **Rebuttal.**
  - The papers are single-author or small-group work in an open-access journal and have not been independently replicated.
  - Hossenfelder publicly criticised the 2025 gravity paper in a May 2025 video, saying it contains mathematical problems and misuses "information". Vopson published a rebuttal (IPI Letters, 2025).
  - A "Thermocontextual Reformulation" (*Entropy*, PMC11765112) reworks the second law of infodynamics.
  - Physicists broadly note that the Shannon entropy of a *chosen encoding* is not a physical entropy. A decrease in one does not, on its own, show optimisation by a computer.
  - The mass-of-information claim is experimentally *untested* (see §4.3).

---

## 3. Arguments AGAINST

### 3.1 Ringel & Kovrizhin (2017): the sign problem and quantum complexity
- **Citation.** Z. Ringel & D. L. Kovrizhin, "Quantized gravitational responses, the sign problem, and quantum complexity", *Science Advances* 3(9): e1701758 (27 Sep 2017).
- **What it shows.** Quantum Monte Carlo (QMC) works efficiently only when the partition function can be written without signs. The authors show that systems with **quantized gravitational responses**, such as a quantized thermal Hall conductance (related to chiral central charge), are obstructed from any *local* sign-free QMC formulation. This backs the belief that some quantum systems cannot be simulated efficiently with classical methods.
- **How media overstated it.** The paper **does not mention** the simulation hypothesis (checked against the PMC full text). Headlines such as the Daily Mail's "Researchers claim to have found proof we are NOT living in a simulation" were misreadings. Scott Aaronson ("Because you asked: the Simulation Hypothesis has not been falsified; remains unfalsifiable", 3 Oct 2017) listed why:
  1. the result concerns one classical method (local sign-free QMC), not all classical algorithms, and is not a formal hardness result
  2. even if it were fully general, it would limit only *classical* simulation
  3. the simulator could use a *quantum* computer
  4. a simulator could simply run slowly, since we could not notice time dilation in the host
- **Fair takeaway.** The paper is a real constraint on *cheap classical* simulation of our physics. It is not a disproof of simulation.

### 3.2 Hossenfelder: "pseudoscience"
- **Sources.**
  - "No, we probably don't live in a computer simulation" (Backreaction, 15 Mar 2017)
  - "The Simulation Hypothesis is Pseudoscience" (Backreaction, 13 Feb 2021)
- **Arguments.**
  1. Nobody knows how to reproduce general relativity and the Standard Model with a computer algorithm. Discretised algorithms typically break the symmetries of special and general relativity. "Nobody currently knows how to put General Relativity on a quantum computer."
  2. You cannot generally throw away short-distance physics and still get long-distance physics right. Coarse-graining ("render only what's observed") needs validation against the real thing, which a hypothetical programmer does not have.
  3. A simulator would need code to detect conscious observers and their intentions and fill in detail without visible inconsistencies. SH proponents offer no mechanism.
  4. A claim that makes big assumptions about physics without explaining how they would work is closer to religion than to science. Hence "pseudoscience", unless proponents specify the algorithm.
- **Standard counter-reply.** Hossenfelder's objections apply to *naive* discretisations. A simulator in a host universe with different physics is not bound by our known algorithms (Aaronson's point 3 and 4, and Chalmers).

### 3.3 Carroll: "The Resolution Conundrum" (self-undermining typicality)
- **Source.** Sean Carroll, "Maybe We Do Not Live in a Simulation: The Resolution Conundrum", Preposterous Universe blog, 22 Aug 2016.
- **Argument.**
  1. The SA assumes simulating civilisations is easy, and assumes we are *typical* observers.
  2. Each simulation level has fewer resources than its parent, so nested hierarchies "bottom out" in civilisations too resource-poor to run their own simulations.
  3. Most observers are therefore at the bottom level. A typical observer should find itself *unable* to simulate civilisations, which contradicts the premise that it is easy.
  4. One premise must be false. Carroll suspects premise 1 (ease) and especially the typicality assumption. He calls typicality "a fake kind of humility" when the ensemble is heterogeneous and we know specifics about our situation.
- **Related critiques of the indifference step.**
  - Weatherson, "Are You a Sim?" (*Phil. Quarterly* 53(212): 425–431, 2003), and Bostrom's "Reply to Weatherson" (2005).
  - Kipping, "A Bayesian Approach to the Simulation Argument" (*Universe* 6(8):109, 2020). Using Bayesian model averaging, Kipping finds P(sim) is slightly **below 50%** and approaches ½ only in the limit.

### 3.4 Faizal, Krauss, Shabir & Marino (2025): undecidability
- **Citation, verified.** M. Faizal, L. M. Krauss, A. Shabir, F. Marino, "Consequences of Undecidability in Physics on the Theory of Everything", *Journal of Holography Applications in Physics* 5(2): 10–21 (2025), DOI 10.22128/jhap.2025.1024.1118; arXiv:2507.22950. JHAP is published by Damghan University, Iran (jhap.du.ac.ir).
- **Claim.** Using Gödel incompleteness, Tarski undefinability and Chaitin incompleteness, the authors argue that a fully algorithmic Theory of Everything, and specifically quantum gravity, is impossible. Some physical truths are "computationally undecidable and can be accessed only through non-algorithmic understanding". They conclude that the universe *cannot be a simulation*. Coverage in late 2025 (UBC Okanagan press release, ScienceDaily, phys.org) presented this as a "mathematical proof".
- **Critiques.**
  - Evan Redden, "Provability vs. Execution" (arXiv:2512.11807, Nov 2025): undecidability limits what a formal system can *prove*, not what an algorithm can *execute*. Conway's Game of Life has undecidable properties yet is trivially simulable. Without evidence of *hypercomputation* in nature, incompleteness does not block simulation.
  - The same category-error objection appears in several blog responses: "a simulation does not need to prove theorems about itself."
  - The argument also assumes that the host universe is limited to Turing computation.

### 3.5 Energy and computational cost
- **Vazza (2025).** F. Vazza, "Astrophysical constraints on the simulation hypothesis for this Universe: why it is (nearly) impossible that we live in a simulation", *Frontiers in Physics* 13 (17 Apr 2025), DOI 10.3389/fphy.2025.1561873; arXiv:2504.08461. Using information–energy links (Landauer/holographic bounds), Vazza estimates the energy needed to simulate three cases:
  1. the whole visible universe
  2. Earth alone
  3. a low-resolution Earth consistent with high-energy neutrino observations

  All three are "entirely incompatible with physics or (literally) astronomically large", *if the host shares our physics*.
- **Lloyd (2002)** gives the scale: about 10^120 operations have occurred in our universe's history.
- **Bostrom's reply, built into the SA.** Only what observers perceive needs simulating (10^33–10^36 operations). Detail is filled in on demand.
- **Counter-reply.** On-demand filling must stay consistent with every later observation, including telescopes, particle detectors and quantum computers, which pushes cost back up. That is Hossenfelder's coarse-graining objection.
- **Loophole.** The host need not share our physics or our energy constraints. That loophole is also why SH resists testing (§3.6).
- **Neukart, Indset, Pflitsch & Perelshtein** (arXiv:2212.04921, 2022) argue that nested simulations under identical physics would exhaust resources, and discuss experiments to probe a "simulation chain".

### 3.6 Unfalsifiability
- If the simulator can edit memories, roll back, render on demand, and run on unknown host physics (all allowed by Bostrom 2003 §III), then no observation is ruled out. Aaronson's 2017 post title states the position: SH "remains unfalsifiable".
- Chalmers (2016 Asimov debate, as reported by *Space.com* and *Scientific American*) notes that a perfect simulation gives no information about the outside. Only a buggy or interactive one would.
- **Consequence for this project.** Only *restricted* versions of SH are testable. These are versions that name a specific architecture (lattice, finite resources, a render policy). Tests constrain those versions, never SH in general.

### 3.7 Other philosophical objections (brief)
- **Substrate independence could be false.** Chalmers lists "conscious sims are impossible" as a sim blocker.
- **Schwitzgebel (2024).** E. Schwitzgebel, "Let's Hope We're Not Living in a Simulation", *Phil. Phenomenol. Res.* 109: 1042–1048, a symposium reply to Chalmers. If we are sims, we should give real weight to the simulation being *small or brief*. His own credence in SH is about 0.1–1%.

---

## 4. Proposed empirical tests

### 4.1 Beane, Davoudi & Savage (2012/2014): lattice artefacts
- **Citation.** S. R. Beane, Z. Davoudi, M. J. Savage, "Constraints on the Universe as a Numerical Simulation", *Eur. Phys. J. A* 50: 148 (2014); arXiv:1210.1847 (Oct 2012).
- **Assumption.** The simulator uses a cubic spacetime lattice, like today's lattice QCD, specifically unimproved Wilson fermions.
- **Signatures considered.**
  - Muon g−2.
  - Discrepancies between determinations of the fine-structure constant α.
  - Most strongly, the **high-energy cutoff of the cosmic-ray spectrum**. This gives an inverse lattice spacing **b⁻¹ ≳ 10^11 GeV**.
- **Distinctive prediction.** Near the lattice cutoff, the arrival directions of the highest-energy cosmic rays should break rotational symmetry and show **cubic anisotropy**, with preferred lattice axes.
- **Status.** The Pierre Auger Collaboration has reported a large-scale *dipole* anisotropy above 8×10^18 eV (*Science* 357:1266, 2017), which it attributes to extragalactic sources. That is not a cubic lattice pattern. No dedicated published search for lattice-axis anisotropy was found (see Unverified leads).
- **Caveats.**
  - The GZK suppression from interactions with the cosmic microwave background already explains a spectral cutoff, so the cutoff alone cannot distinguish a lattice.
  - A more advanced simulator could use improved or randomised discretisations with no visible axes.

### 4.2 Campbell, Owhadi, Sauvageau & Watkinson (2017): observer-dependent rendering
- **Citation.** T. Campbell, H. Owhadi, J. Sauvageau, D. Watkinson, "On Testing the Simulation Theory", *International Journal of Quantum Foundations* (published online 17 Jun 2017; volume/issue not verified); arXiv:1703.00058.
- **Idea.** A finite simulator would render reality when information becomes available *to a player*, not when a machine inside the simulation records it. The authors propose variants of the double-slit and delayed-choice quantum-eraser experiments where which-path information is recorded but then destroyed or never viewed by a conscious observer. They look for deviations from standard QM.
- **Status and critique.**
  - Standard QM predicts outcomes that depend only on whether which-path information *exists physically*, not on whether anyone looks. Every existing experiment agrees with standard QM.
  - A positive result would contradict quantum mechanics itself.
  - No completed run with a published result was found (see Unverified leads).

### 4.3 Vopson's proposals
- "Experimental protocol for testing the mass–energy–information equivalence principle" (*AIP Advances* 12:035311, 2022). Vopson proposes that electron–positron annihilation should release the particles' "information content" as two extra low-energy infrared photons alongside the two 511 keV gamma photons.
- This is a test of the *information-has-mass* conjecture, which Vopson links to SH, not a direct test of SH. It is untested as of this survey.

### 4.4 Holographic-noise search (Fermilab Holometer)
- A. S. Chou et al., "First Measurements of High Frequency Cross-Spectra from a Pair of Large Michelson Interferometers", *PRL* 117:111102 (2016); arXiv:1512.01216.
- The experiment tested a proposed Planck-scale "holographic noise" (jitter from finite spacetime information). The predicted signal was **not seen**.
- It was not designed as a simulation test, but it probes the "finite resolution" intuition of §2.2 and §2.7.

### 4.5 Lorentz-invariance tests
- Fermi GRB 090510 (Abdo et al., *Nature* 462:331, 2009) found no energy-dependent speed of light up to about the Planck scale. Later bursts, such as GRB 221009A, tightened this further.
- These tests constrain naive "pixelated spacetime" versions of SH.

### 4.6 Barrow's "glitch" signatures
- J. D. Barrow, "Living in a simulated universe", in B. Carr (ed.), *Universe or Multiverse?* (CUP, 2007).
- If a simulator's approximations accumulate error, we might see sudden glitches, slow drifts in "constants", or places where the laws need "patching".
- The testable proxy is precision tests of the stability of α, μ = m_p/m_e, and similar constants.

### 4.7 Assessment of the test literature
- Every test constrains a *specific* simulator design: a lattice, finite classical resources, a render policy, or accumulating error.
- No test has produced a positive signal.
- All are consistent with no simulation *and* with a sufficiently capable simulator.

---

## 5. CS / game-engine analogies found in the literature

| Analogy | Physics mapping proposed | Who used it (verified) | Notes |
|---|---|---|---|
| **Level of detail (LOD)** | Distant objects stored at low fidelity | Bostrom 2003 §III ("Distant astronomical objects can have highly compressed representations") | Idea present; the term "LOD" is ours |
| **Culling / occlusion** | Unobserved interiors not simulated | Bostrom 2003 §III ("inside of the Earth can be safely omitted") | Vazza 2025 costs a "low-resolution Earth" |
| **Render on demand / lazy evaluation** | Measurement = rendering | Bostrom 2003; Campbell et al. 2017 ("as in a video game, render content… only at the moment… available for observation by a player"); Virk 2019 (popular) | The core of most "quantum = rendering" claims |
| **Rollback / rewind / state edit** | Undo glitches; edit memories | Bostrom 2003 ("skip back a few seconds and rerun"; "edit the states of any brains") | Directly relevant to experiment 001 |
| **Max processing rate** | Speed of light | Whitworth 2008 (pixel crossing a screen) | See §2.1 |
| **Processing load / lag** | Mass curves spacetime; time dilation as local overload | Whitworth 2008 ("Relativity effects could then arise from local processing overloads"); Vopson 2025 (gravity as compute optimisation) | Directly relevant to experiment 002 |
| **Frame rate / discrete ticks** | Quantum transitions; Planck time | Whitworth 2008 ("like the frames of a film"); Zuse 1969; Fredkin 1990 (CA time steps) | |
| **Pixels / grid / lattice** | Planck length; lattice spacing | Beane et al. 2014 (cubic lattice, testable); Zuse; Wolfram | Only Beane et al. give a quantitative bound |
| **RNG** | Quantum randomness | Whitworth 2008 ("random number function in the VR processor") | Seeded vs. true RNG is untested; see leads |
| **Class instances** | Identical particles | Whitworth 2008 ("Every digital object created by the same code is identical") | |
| **Cellular automata** | Local update rules generate physics | Zuse 1969; Fredkin 1990; Wolfram 2002/2020; 't Hooft 2016 | Serious research programmes, but not SH per se |
| **Boot-up** | Big Bang | Whitworth 2008 ("every virtual system must be booted up") | |
| **Error-correcting codes** | Codes in SUSY representations | Gates 2010 | See §2.8 |
| **Data compression / optimisation** | Infodynamics, gravity | Vopson 2023, 2025 | |
| **Game character vs. OS** | Limits of inferring host physics | Tegmark, 2016 Asimov Debate (reported by *Space.com*) | |
| **Floating-point precision** | Precision limits or drift of constants | *No verified scholarly source found* | Barrow's "drift" is the nearest (approximation error); see leads |
| **Procedural generation / seeds** | Initial conditions as a seed; compressible universe | *No verified scholarly source found* | Conceptually close to Wolfram (simple rule → complexity) and Tegmark (low-information laws) |

---

## 6. Annotated bibliography

*Each entry gives the citation, a URL, and a two-line summary. All were verified September 2026.*

**Foundations and philosophy**

1. **Bostrom, N. (2003).** "Are You Living in a Computer Simulation?" *Philosophical Quarterly* 53(211): 243–255. https://simulation-argument.com/simulation.pdf
   The trilemma: extinction before posthumanity, disinterest in ancestor-simulations, or we are almost certainly simulated. Includes the f_sim formula, the bland indifference principle, and render-on-demand and rollback cost-saving ideas.
2. **Bostrom, N. (2005).** "The Simulation Argument: Reply to Weatherson." *Philosophical Quarterly* (2005; vol/pages not verified). PhilPapers: https://philpapers.org/rec/NICTSA-4 ; https://simulation-argument.com/weathersonreply.pdf
   Defends the indifference principle against Weatherson's objections.
   Clarifies what the SA does and does not claim.
3. **Weatherson, B. (2003).** "Are You a Sim?" *Philosophical Quarterly* 53(212): 425–431. https://philpapers.org/rec/WEAAYA
   Argues that Bostrom's indifference principle is ambiguous. None of four readings supports his conclusion.
4. **Chalmers, D. J. (2022).** *Reality+: Virtual Worlds and the Problems of Philosophy.* W. W. Norton. https://wwnorton.com/books/9780393635805 (précis: https://consc.net/papers/realityprecis.pdf)
   Virtual reality is genuine reality. We cannot know that we are not sims unless a "sim blocker" holds.
   If simulated, we live in an "it-from-bit" created world and most ordinary beliefs stay true.
5. **Chalmers, D. J. (2005).** "The Matrix as Metaphysics." In *Philosophers Explore the Matrix* (OUP), 132–176. https://consc.net/papers/matrix.pdf
   Argues that the Matrix hypothesis is a metaphysical hypothesis rather than a sceptical one.
   Envatted beliefs are mostly true.
6. **Schwitzgebel, E. (2024).** "Let's Hope We're Not Living in a Simulation." *Phil. & Phenomenological Research* 109: 1042–1048. https://onlinelibrary.wiley.com/doi/10.1111/phpr.13125
   A reply to Chalmers: if simulated, we should expect small or brief sims. That is existentially bad news.
7. **Moravec, H. (1993).** "Pigs in Cyberspace." *Extropy* #10. https://frc.ri.cmu.edu/~hpm/project.archive/general.articles/1992/CyberPigs.html
   An early vision of minds and worlds running in cyberspace, and of simulated beings unable to detect their status.
   Also see "Simulation, Consciousness, Existence" (Telepolis 1996), listed at https://frc.ri.cmu.edu/~hpm/hpm.pubs.html.
8. **Descartes, R. (1641).** *Meditations on First Philosophy.* Overview: https://plato.stanford.edu/entries/descartes-epistemology/
   Dream argument and evil-demon hypothesis: the classic sceptical precursor.
9. **Zhuangzi (c. 4th c. BCE).** Butterfly dream. Overview: https://plato.stanford.edu/entries/zhuangzi/
   Uncertainty about which state is "real". Traditionally read as being about transformation rather than scepticism.
10. **Kipping, D. (2020).** "A Bayesian Approach to the Simulation Argument." *Universe* 6(8): 109. https://doi.org/10.3390/universe6080109
    Bayesian model averaging over the SA gives P(sim) just under 50%.
    The probability approaches ½ only with infinitely many simulations.

**Digital physics and information**

11. **Zuse, K. (1969/1970).** *Rechnender Raum* / *Calculating Space* (MIT Project MAC translation). https://philpapers.org/rec/ZUSRR
    The first proposal that the universe is computed by a cellular automaton, questioning the continuity of physical law.
12. **Fredkin, E. (1990).** "Digital Mechanics: An Informational Process Based on Reversible Universal Cellular Automata." *Physica D* 45: 254–270. https://doi.org/10.1016/0167-2789(90)90186-S
    Hypothesises that a single reversible universal CA underlies all microscopic physics ("Finite Nature").
13. **Wheeler, J. A. (1989/1990).** "Information, Physics, Quantum: The Search for Links." In *Proc. 3rd Int. Symp. Foundations of QM* / *Complexity, Entropy and the Physics of Information*. https://philpapers.org/archive/WHEIPQ.pdf
    Coins "it from bit". Physical reality arises from answers to yes/no questions: a participatory, information-first view.
14. **Tegmark, M. (2008).** "The Mathematical Universe." *Foundations of Physics* 38: 101–150. https://arxiv.org/abs/0704.0646
    Physical reality is a mathematical structure (MUH). Tegmark also floats that only computable structures exist.
15. **Wolfram, S. (2020).** "A Class of Models with the Potential to Represent Fundamental Physics." *Complex Systems* 29: 107–536. https://arxiv.org/abs/2004.08210
    Hypergraph-rewriting models from which spacetime, relativity and quantum-like behaviour are claimed to emerge.
16. **'t Hooft, G. (2016).** *The Cellular Automaton Interpretation of Quantum Mechanics.* Springer FTP 185. https://link.springer.com/book/10.1007/978-3-319-41285-6
    Quantum mechanics as a tool for describing an underlying deterministic CA. Addresses Bell via superdeterminism.
17. **Whitworth, B. (2008).** "The Physical World as a Virtual Reality." arXiv:0801.0337. https://arxiv.org/abs/0801.0337
    The most explicit catalogue of VR/game analogies: max processing rate = c, load = gravity/time dilation, RNG = quantum randomness, frames = quantum transitions.
    Speculative and not peer-reviewed physics.
18. **Lloyd, S. (2002).** "Computational Capacity of the Universe." *Phys. Rev. Lett.* 88: 237901. https://link.aps.org/doi/10.1103/PhysRevLett.88.237901
    The universe has performed at most ~10^120 operations on ~10^90 bits (10^120 with gravity). Sets the scale for cost arguments.
19. **Bekenstein, J. D. (1981).** "Universal upper bound on the entropy-to-energy ratio for bounded systems." *Phys. Rev. D* 23: 287. https://link.aps.org/doi/10.1103/PhysRevD.23.287
    Finite entropy (information) for any bounded system of given energy and size. Black holes saturate the bound.
20. **Susskind, L. (1995).** "The World as a Hologram." *J. Math. Phys.* 36: 6377–6396. https://arxiv.org/abs/hep-th/9409089
    Develops 't Hooft's holographic idea: 3-D physics encoded on a 2-D boundary at about one degree of freedom per Planck area.
21. **Wigner, E. P. (1960).** "The Unreasonable Effectiveness of Mathematics in the Natural Sciences." *Comm. Pure Appl. Math.* 13(1): 1–14. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/wigner.pdf
    Mathematics works in physics with a precision "bordering on the mysterious". Often recruited, without Wigner's endorsement, as a pro-SH observation.
22. **Barnes, L. A. (2012).** "The Fine-Tuning of the Universe for Intelligent Life." *PASA* 29(4): 529–564. https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/finetuning-of-the-universe-for-intelligent-life/222321D5D4B5A4D68A3A97BBE46AEE45
    A technical review of fine-tuning cases and criticisms. Neutral on the explanation.

**Suggestive-for items**

23. **Gates, S. J. Jr. (2010).** "Symbols of Power: Adinkras and the Nature of Reality." *Physics World* 23(6). https://physicsworld.com/a/symbols-of-power-how-adinkras-could-lead-to-fresh-insights-into-supersymmetry/ (reprint: https://onbeing.org/blog/symbols-of-power-adinkras-and-the-nature-of-reality/)
    A popular account of error-correcting codes inside supersymmetry representations. Speculates, explicitly as a musing, about a Matrix-like reality.
24. **Doran, C. F., Faux, M. G., Gates, S. J. Jr., Hübsch, T., Iga, K. M., Landweber, G. D. (2008).** "Relating Doubly-Even Error-Correcting Codes, Graphs, and Irreducible Representations of N-Extended Supersymmetry." arXiv:0806.0051. https://arxiv.org/abs/0806.0051
    The technical result: classifying adinkras is equivalent to classifying doubly-even binary codes.
25. **Vopson, M. M. (2019).** "The mass-energy-information equivalence principle." *AIP Advances* 9: 095206. https://pubs.aip.org/aip/adv/article/9/9/095206/1076232
    Proposes that stored information has mass (~3.19×10⁻³⁸ kg/bit at 300 K). Untested.
26. **Vopson, M. M. & Lepadatu, S. (2022).** "Second law of information dynamics." *AIP Advances* 12: 075310. https://pubs.aip.org/aip/adv/article/12/7/075310/2819368
    Claims that information entropy stays constant or decreases in some systems (digital storage, RNA genomes).
27. **Vopson, M. M. (2023).** "The second law of infodynamics and its implications for the simulated universe hypothesis." *AIP Advances* 13: 105308. https://pubs.aip.org/aip/adv/article/13/10/105308/2915332
    Extends the "law" to atoms, symmetry and cosmology, and reads it as data compression consistent with SH.
28. **Vopson, M. M. (2025).** "Is gravity evidence of a computational universe?" *AIP Advances* 15: 045035. https://pubs.aip.org/aip/adv/article/15/4/045035/3345217
    Derives gravity-like attraction as information-entropy minimisation. Publicly criticised by Hossenfelder, and Vopson replied.
29. **Barrow, J. D. (2007).** "Living in a simulated universe." In Carr (ed.), *Universe or Multiverse?* CUP. https://simulation-argument.com/barrowsim.pdf
    Simulators using approximations should leave glitches and drifting constants, giving a potential observational signature.

**Against**

30. **Ringel, Z. & Kovrizhin, D. L. (2017).** "Quantized gravitational responses, the sign problem, and quantum complexity." *Science Advances* 3(9): e1701758. https://www.science.org/doi/10.1126/sciadv.1701758
    Systems with quantized thermal-Hall-type responses block local sign-free QMC. The paper says nothing about the simulation hypothesis; the media overread it.
31. **Aaronson, S. (2017).** "Because you asked: the Simulation Hypothesis has not been falsified; remains unfalsifiable." Shtetl-Optimized, 3 Oct 2017. https://scottaaronson.blog/?p=3482
    Explains why Ringel–Kovrizhin does not refute SH: it concerns one classical method, and the simulator could be quantum or slow.
32. **Hossenfelder, S. (2021).** "The Simulation Hypothesis is Pseudoscience." Backreaction, 13 Feb 2021. https://backreaction.blogspot.com/2021/02/the-simulation-hypothesis-is.html
    No known algorithm reproduces GR and the Standard Model with their symmetries, and coarse-graining is not free. Without a mechanism, SH is faith.
33. **Hossenfelder, S. (2017).** "No, we probably don't live in a computer simulation." Backreaction, 15 Mar 2017. http://backreaction.blogspot.com/2017/03/no-we-probably-dont-live-in-computer.html
    An earlier version of the argument, focused on the unexplained code needed to detect observers and fill in detail consistently.
34. **Hossenfelder, S. (2013).** "Minimal Length Scale Scenarios for Quantum Gravity." *Living Reviews in Relativity* 16: 2. https://arxiv.org/abs/1203.6191
    A review of minimal-length models. Relevant to the "Planck pixel" claim and to why naive grids conflict with Lorentz symmetry.
35. **Carroll, S. (2016).** "Maybe We Do Not Live in a Simulation: The Resolution Conundrum." Preposterous Universe blog, 22 Aug 2016. https://www.preposterousuniverse.com/blog/2016/08/22/maybe-we-do-not-live-in-a-simulation-the-resolution-conundrum/
    Nested simulations bottom out in resource-poor levels, so typical observers cannot simulate, which contradicts the SA's premise. Carroll also questions typicality itself.
36. **Faizal, M., Krauss, L. M., Shabir, A., Marino, F. (2025).** "Consequences of Undecidability in Physics on the Theory of Everything." *J. Holography Applications in Physics* 5(2): 10–21. https://jhap.du.ac.ir/article_488.html (arXiv:2507.22950)
    Gödel, Tarski and Chaitin arguments that quantum gravity is non-algorithmic, and therefore that the universe cannot be simulated.
37. **Redden, E. (2025).** "Provability vs. Execution: A Comment on 'Consequences of Undecidability…'." arXiv:2512.11807. https://arxiv.org/abs/2512.11807
    Undecidability limits proof, not execution; the Game of Life is the counterexample. Faizal et al.'s conclusion needs hypercomputation in nature.
38. **Vazza, F. (2025).** "Astrophysical constraints on the simulation hypothesis for this Universe: why it is (nearly) impossible that we live in a simulation." *Frontiers in Physics* 13. https://doi.org/10.3389/fphy.2025.1561873
    The energy costs of simulating the universe, Earth, or even a low-resolution Earth are astronomically prohibitive *under our physics*.
39. **Neukart, F., Indset, A., Pflitsch, M., Perelshtein, M. (2022).** "Do we live in a [quantum] simulation? Constraints, observations, and experiments on the simulation hypothesis." arXiv:2212.04921. https://arxiv.org/abs/2212.04921
    A survey plus proposals. Resource exhaustion in nested simulations under identical physics, and experiments targeting "simulation chains".

**Tests and constraints**

40. **Beane, S. R., Davoudi, Z., Savage, M. J. (2014).** "Constraints on the Universe as a Numerical Simulation." *Eur. Phys. J. A* 50: 148. https://arxiv.org/abs/1210.1847
    Lattice-QCD-style simulator. The cosmic-ray cutoff bounds the inverse lattice spacing at ≳10^11 GeV, and the paper predicts cubic anisotropy in UHE cosmic rays.
41. **Campbell, T., Owhadi, H., Sauvageau, J., Watkinson, D. (2017).** "On Testing the Simulation Theory." *Int. J. Quantum Foundations* (2017; vol. not verified). https://ijqf.org/archives/4105 ; https://arxiv.org/abs/1703.00058
    "Render only for players" hypothesis. Proposes double-slit and eraser variants where recorded-but-unviewed which-path data might behave differently.
42. **Vopson, M. M. (2022).** "Experimental protocol for testing the mass–energy–information equivalence principle." *AIP Advances* 12: 035311. https://pubs.aip.org/aip/adv/article/12/3/035311/2819739
    Predicts extra infrared photons from e⁺e⁻ annihilation if information has mass. Not yet performed.
43. **Chou, A. S. et al. (Holometer) (2016).** "First Measurements of High Frequency Cross-Spectra from a Pair of Large Michelson Interferometers." *PRL* 117: 111102. https://arxiv.org/abs/1512.01216
    Searched for Planck-scale holographic spacetime noise and found none. Constrains "finite-resolution spacetime" ideas.
44. **Abdo, A. A. et al. (Fermi) (2009).** "A limit on the variation of the speed of light arising from quantum gravity effects." *Nature* 462: 331. https://www.nature.com/articles/nature08574
    No energy-dependent photon speed from GRB 090510. Linear Lorentz violation is excluded below ~1.2 E_Planck.
45. **Hensen, B. et al. (2015).** "Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres." *Nature* 526: 682–686. https://www.nature.com/articles/nature15759
    Rules out local realism, so any "render engine" for quantum outcomes must be non-local or superdeterministic.
46. **Pierre Auger Collaboration (2017).** "Observation of a large-scale anisotropy in the arrival directions of cosmic rays above 8×10^18 eV." *Science* 357: 1266–1270. https://www.science.org/doi/10.1126/science.aan4338
    A dipole anisotropy of extragalactic origin. It is the relevant dataset for, but not a test of, the Beane et al. lattice-axis prediction.

**Public debate**

47. **American Museum of Natural History (2016).** *2016 Isaac Asimov Memorial Debate: Is the Universe a Simulation?* (5 Apr 2016; Tyson, Chalmers, Davoudi, Gates, Randall, Tegmark). https://www.amnh.org/explore/videos/isaac-asimov-memorial-debate/2016
    Physicists and a philosopher debate SH. The source of the widely quoted Tegmark "game character" and Chalmers "only a buggy sim is detectable" remarks.

---

## 7. Unverified leads (do NOT cite until checked)

- **Chalmers' "at least 25%" credence.** Widely reported (e.g. Built In, press coverage) as his estimate in *Reality+*. The précis confirms "non-negligible probability" but the exact figure was not checked in the book text.
- **Tyson's "50-50" odds** at the 2016 Asimov debate. Reported by *Space.com* and *Scientific American*; not checked against the video transcript.
- **Elon Musk, 2016 Code Conference, "one in billions" chance we are in base reality.** Commonly quoted; not verified.
- **Faizal and JHAP editorial ties.** Some online commentary suggests an editorial relationship between an author and the journal. Not verified. Check the JHAP editorial board before mentioning.
- **A dedicated search of Auger or Telescope Array data for Beane-style *cubic* lattice anisotropy.** None found. Ask a cosmic-ray physicist, or search the Auger and TA publication lists.
- **Completed runs of the Campbell et al. (2017) experiments.** Campbell's organisation has announced crowdfunded experiments. No peer-reviewed results found.
- **Floating-point / precision-limit analogies in scholarly literature.** Not found in verified sources. Popular blogs use them, and Barrow's constant-drift idea is the closest peer-reviewed analogue.
- **Procedural generation / RNG-seed analogies.** Likely in Virk (2019, *The Simulation Hypothesis*, Bayview Books), which was verified to exist and to centre on video-game rendering. Specific passages not checked.
- **Tegmark, *Our Mathematical Universe* (Knopf, 2014); Deutsch, *The Fabric of Reality* (1997, virtual-reality chapter); Greene, *The Hidden Reality* (2011, simulated-multiverse chapter).** Probably relevant; bibliographic details not verified here.
- **Critiques of Vopson's infodynamics beyond Hossenfelder's video.** One reformulation was located (*Entropy*, PMC11765112, "The Second Law of Infodynamics: A Thermocontextual Reformulation"). Author and venue details need confirming. No formal published "Comment" in *AIP Advances* was located.
- **Chalmers, "Taking the simulation hypothesis seriously"** (https://consc.net/papers/simserious.pdf), apparently his reply in the PPR symposium. Venue and year not confirmed.
- **Constant-drift limits (α, μ) as Barrow-glitch tests.** Specific current bounds, for example from atomic clocks and quasar spectra, should be pulled from a recent review before citing numbers.
