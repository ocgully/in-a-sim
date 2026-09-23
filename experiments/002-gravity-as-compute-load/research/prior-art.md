# Experiment 002: Gravity as Compute Load. Prior-art review

*Compiled 2026-09-23. This is a literature review for a thought experiment. It makes observations and gathers evidence. It does not claim the universe is a simulation or that the idea below is true.*

**The idea under review.** Gravity is a processing bottleneck. The more "stuff" a region contains, the longer that region takes to compute. Things in the region therefore tick and propagate more slowly (gravitational time dilation is read as regional lag, or a lower local tick rate), and what we experience as gravity is that slowdown.

**Verification policy.** Every citation in the annotated bibliography was checked against a publisher page, arXiv, ADS, PubMed, or the primary source (author, year, title, venue, URL). Where I could read only a search-engine snippet or an abstract, the entry says so. Anything I could not verify is under [Unverified leads](#5-unverified-leads).

---

## 1. Summary verdict

### (a) Directly anticipated: the core claim is not new

The central claim ("more matter or activity in a region → less processing per event → local time runs slow → this is gravitational time dilation, and its gradient is gravity") has been put in print at least three times. It also circulates widely in informal form.

1. **Alagoz (2010)**, *Open Universe Modeling: Information Layer and Time Dilation* (arXiv:1010.2365), is the closest match. Each volume of space has a **fixed total "information transmission capacity"** shared by all the activity in it. Extra activity (motion, or the "gravitational effects of massive objects") reduces each process's share, so "an observer living outside of this volume will detect a time dilation inside this volume." Alagoz then argues that **an imbalance (gradient) of capacity allocation produces a force**, and that light bends because it "move[s] faster in the side of space volume which is further from a mass." That is essentially the user's idea, including the "gradient → attraction" step, 16 years earlier.
2. **Whitworth (2008)**, *The Physical World as a Virtual Reality* (arXiv:0801.0337), lists "processing load effects": "a high matter concentration may constitute a high processing demand, so a massive body could slow down the information processing of space-time, causing space to 'curve' and time to slow … Relativity effects could then arise from local processing overloads." **Whitworth (2010)**, *Simulating Space and Time* (Prespacetime Journal 1(2); arXiv:1011.5499), develops this further: virtual time "slows down with processing load," the "processing load differential of gravity" bends light, and an on-screen avatar "sees no difference, as they themselves also slow down."
3. **Lee (2025)**, *Computational Universe Model (UCS) and Information-induced Time Dilation (ITD)* (Zenodo preprint, DOI 10.5281/zenodo.18027729). This independent-researcher preprint proposes that information density acts as a "computational load" that "lags" the local clock. It adds an information term to GR and proposes an Sr-87 optical-clock test. It was posted to Hacker News as "Is gravitational time dilation a form of computational latency?", where it drew little engagement and one comment criticising the missing mathematics.
4. **Informal and popular versions** clearly exist. They include Medium essays (Petersen, "Gravity & the Simulation Hypothesis (I)"; Giannakopoulos, "Time Dilation as Buffer Saturation"), a Quora question ("Could time dilation be processing lag…?"), and at least one explicit rebuttal essay (Kassiantchouk, "Simulation Hypothesis Fails the Physics of Time"), which says: "Proponents of the Simulation Hypothesis have pointed out that time dilation is the ultimate 'smoking gun' — the Universe slowing its frame rate…". In short, "time dilation is lag" is a known meme in simulation-hypothesis circles.

### (b) Partially overlapping

- **Wolfram Physics Project.** This is the closest *mainstream-adjacent* framework. Time dilation from **motion** is explained exactly as a budget effect: moving an object "takes up a certain number of rewritings, leaving fewer for the intrinsic evolution of the object itself, and thus causing time to effectively 'run slower'" (Wolfram 2024). For **gravity**, though, Wolfram ties energy and mass to *greater* update activity and writes that this "leads to more rewritings, causing 'time to run faster' for any object in that region of space (corresponding to the traditional 'gravitational redshift')." Wolfram's gravity comes from curvature of the causal graph (Gorard 2020 derives a discrete Einstein equation), not from a shortage of compute. So the mechanism overlaps with ours for velocity and differs for gravity.
- **Vopson (2025)**, *Is gravity evidence of a computational universe?* (AIP Advances 15, 045035). This is **not** the same idea. Vopson argues that gravity is *information compression*: merging many objects into fewer reduces information entropy and is "computationally more effective." It is an entropic-force derivation of Newton's law, related to Verlinde's. It does not describe time dilation as lag or a tick-rate deficit. It shares the "gravity is a computational optimisation" framing but uses a different mechanism.
- **Verlinde (2011) and Jacobson (1995)** also treat gravity as emergent from information and thermodynamics, but not from processing throughput.
- **"Gravity is mostly time dilation"** is established physics. In the weak field, falling is governed almost entirely by g₀₀. Gould (2016, AJP) says "it is primarily the warping of time, not space, that causes a ball to fall." Czarnecka & Czarnecki (2021, AJP) derive free fall as de Broglie waves refracting toward regions where clocks run slower. Epstein (1983) devotes a chapter to the idea that "slow time makes gravity." So the step "a gradient in tick rate produces attraction" is textbook physics, with no new mechanism needed. The speculative part is only *why* the tick rate varies.
- **Game and server analogs.** EVE Online's Time Dilation (2011/2012) and Second Life's region "time dilation" (`llGetRegionTimeDilation`) literally slow a region's simulation clock under load. These are real-world instances of the analogy, not physics claims.
- **Singh & Friedrich (arXiv:2304.01263)** obtain Schwarzschild-like time dilation and a Newtonian-like force from systems coupled to a shared quantum clock. This is adjacent in spirit: gravity emerging from how systems couple to "time."

### (c) What may still be novel (with searches run)

I found **no prior work** that does any of the following:
1. Builds an **executable toy simulation** in which a load-dependent local tick-rate field (computed from, e.g., particle count or update cost per cell) is the *only* ingredient, and then *measures* whether wave packets or particles fall toward loaded regions and with what force law.
2. Confronts the load-lag idea **quantitatively** with the specific constraints in §3. These are: the dilation must track *gravitational potential*, not local density; it must couple to *energy only*, not to information or complexity (equivalence principle to ~10⁻¹⁵); it must give the **full** light deflection (γ = 1 to ~10⁻⁵), not only the half (Einstein-1911) value that a pure time-lag field gives.
3. Uses **EVE Online's TiDi** (or Second Life region dilation) as an explicit worked analogy for gravitational time dilation in a published source. Many people have probably drawn the comparison informally, but I found no citable source that makes it.
4. Resolves the **sign problem** head-on: physical compute capacity rises with energy (Margolus–Levitin), so "more stuff → less compute" is the reverse of what known physics implies about computing resources. None of Alagoz, Whitworth or Lee addresses it.

Novelty is therefore **low for the core claim** and **possibly moderate for a rigorous, falsifiable, simulated treatment**. Any public write-up should credit Alagoz (2010) and Whitworth (2008, 2010) as prior statements of the idea.

**Searches run (Sept 2026, web search + fetch):** "Vopson 2025 AIP Advances gravity computational universe"; "gravity time dilation simulation lag processing power theory"; "Wolfram Physics Project gravitational time dilation causal graph update rate"; "Wolfram physics time dilation more activity/more updating"; "reddit time dilation lag simulation hypothesis gravity processing"; "gravity is lag simulation computational load time dilation blog OR video"; "computational time dilation frame rate universe simulation more matter slower tick rate arXiv"; "Information-Induced Time Dilation"; "physics stackexchange time dilation computational lag"; "youtube time dilation simulation lag processing power"; "r/SimulationTheory gravity time dilation server lag"; "time dilation processing load OR processing bottleneck digital physics gravity network capacity"; "Brian Whitworth physical world virtual reality processing load"; "arXiv gravitational time dilation computational processing rate information universe model"; "simulation hypothesis gravity rendering time dilation Virk OR Campbell"; "cellular automaton variable clock rate emergent gravity refraction toy model"; "gravity simulation lag EVE Online time dilation analogy"; "Second Life time dilation simulator region overload"; plus targeted verification searches for every citation below. Reddit and YouTube could not be searched directly, since results were dominated by generic explainers, so coverage of those platforms is incomplete (see §5).

---

## 2. Annotated bibliography

### 2.1 Direct prior art: the "time dilation = processing lag" idea

**Alagoz, B. B. (2010).** *Open Universe Modeling: Information Layer and Time Dilation.* OncuBilim Algorithm and Systems Labs, Vol. 10, Art. No. 01; arXiv:1010.2365 (submitted 12 Oct 2010).
URL: https://arxiv.org/abs/1010.2365
The paper posits an "information processing layer" of the universe with a fixed total transmission capacity per volume, shared among all "activities." Added activity (motion, gravity) reduces each process's allocation and slows events, which appears as time dilation to an outside observer. A spatial *imbalance* of capacity allocation is argued to produce a force and to bend light toward the mass. The model uses a "universal clock signal."
*Relevance:* **This is the most direct prior statement of the user's idea**, including the gradient-produces-force step. It is qualitative and does not derive 1/r², the equivalence principle, or the correct light bending. It was published in a non-mainstream venue. Verified from the full arXiv PDF text.

**Whitworth, B. (2008).** *The Physical World as a Virtual Reality.* arXiv:0801.0337 (v1 2 Jan 2008, v2 5 Jan 2008), Massey University.
URL: https://arxiv.org/abs/0801.0337
This is a general essay arguing that physics may be a virtual reality generated by information processing. Point 5, "Processing load effects," says a massive body could "slow down the information processing of space-time," and that "relativity effects could then arise from local processing overloads."
*Relevance:* **The explicit "matter = processing demand = slower time" claim, stated in 2008.** It is a brief conjecture with no model. Verified from the arXiv PDF.

**Whitworth, B. (2010).** *Simulating Space and Time.* Prespacetime Journal 1(2), March 2010; arXiv:1011.5499.
URL: https://arxiv.org/abs/1011.5499
The paper proposes a processing grid in which "time is processing cycles." Its summary table says virtual time "slows down with processing load," and that the "processing load differential of gravity" bends light by skewing transfers between grid nodes. It notes an avatar cannot see its own slowdown, although distributed observers can compare clocks.
*Relevance:* **This is the fuller version of the same idea, including light bending from a load gradient** and the argument that the lag is locally undetectable (which the user's framing needs too). Verified from the arXiv PDF.

**Lee, J. (2025).** *Computational Universe Model (UCS) and Information-induced Time Dilation (ITD).* Zenodo preprint v2.0.0, 23 Dec 2025. DOI: 10.5281/zenodo.18027729.
URL: https://zenodo.org/records/18027729 · HN discussion: https://news.ycombinator.com/item?id=46364111
The preprint models the universe as a "Universal Computing System." It proposes that information density causes extra time dilation through finite computational resources, adds an information-entropy term to the stress-energy tensor, and suggests Sr-87 lattice-clock tests.
*Relevance:* **A recent, near-identical proposal** that also makes a testable prediction (dilation from information and not only mass-energy). That prediction is in tension with equivalence-principle bounds (§3). On HN it was criticised for lacking an explicit form of its T^info term. Verified from the Zenodo record; the full text was not reviewed.

**Kassiantchouk, A.** *Simulation Hypothesis Fails the Physics of Time.* Medium, "Time Matters" publication.
URL: https://medium.com/timematters/simulation-hypothesis-fails-the-physics-of-time-261fc5134088
According to search-engine excerpts, the essay rebuts the "time dilation = system lag" meme. It argues that distant, *less* populated regions of the universe show strong (cosmological) time dilation, which a rendering-load account cannot explain.
*Relevance:* This documents that the idea is already a popular trope and gives an existing (if imperfect) counterargument. Cosmological (1+z) time dilation comes from expansion, not from a local clock rate, so the rebuttal is weaker than it sounds. *Partially verified:* title, author and URL are confirmed through the search index, but Medium returned HTTP 403, so the content comes from snippets and the date is unverified.

**Petersen, D.** *Gravity & the Simulation Hypothesis (I).* Medium.
URL: https://medium.com/@davmandy_jp/gravity-the-simulation-hypothesis-i-f6128825e83d
Search excerpts suggest it frames gravitational time dilation as a way for simulators to "reduce computational burden" in strong-field regions.
*Relevance:* This is a popular version of the idea. The direction may differ: dilation as a deliberate *optimisation* rather than involuntary lag. *Partially verified* (403 on fetch; snippets only).

**Giannakopoulos, B.** *Time Dilation as Buffer Saturation: A Computational Ontology of Relativity.* Medium.
URL: https://medium.com/@bill.giannakopoulos/time-dilation-as-buffer-saturation-a-computational-ontology-of-relativity-43d84b805c9e
Search excerpts say massive objects "consume more computational buffering locally," so clocks near them tick slower because they "have less capacity available to compute their internal updates."
*Relevance:* A popular restatement that is almost word-for-word the user's idea. *Partially verified* (403 on fetch; snippets only).

**Quora question.** "Could time dilation be processing lag that's similar to my computer when it can't handle the amount or speed of information?"
URL: https://www.quora.com/Could-time-dilation-be-processing-lag-thats-similar-to-my-computer-when-it-cant-handle-the-amount-or-speed-of-information
*Relevance:* Shows that lay people ask the question independently. *Existence verified through the search index; content not readable (403).*

### 2.2 Computational-universe frameworks (Wolfram, Vopson, Zuse, Fredkin, Lloyd, Schmidhuber)

**Wolfram, S. (2024).** *On the Nature of Time.* Stephen Wolfram Writings, 8 Oct 2024.
URL: https://writings.stephenwolfram.com/2024/10/on-the-nature-of-time/
Wolfram explains motion-induced time dilation as a rewrite-budget effect (quoted in §1b). For gravity he says energy-momentum is "greater activity in the underlying hypergraph," which "leads to more rewritings, causing 'time to run faster' for any object in that region of space (corresponding to the traditional 'gravitational redshift')." He also writes that "it's roughly the density of events in the hypergraph that determines the density of energy (and mass)."
*Relevance:* **The key contrast.** In Wolfram's model, mass *is* extra computation, not a drain on a fixed budget, and gravity comes from causal-graph curvature. The user's "fixed budget, more stuff → less per item" mechanism matches Wolfram's account of *kinematic* dilation, not his account of gravity. (The quote above is verbatim. How Wolfram's "time runs faster" maps onto clocks running slow deeper in a potential is his framing and is not explained further in that passage.)

**Wolfram, S. (2020).** *Finally We May Have a Path to the Fundamental Theory of Physics… and It's Beautiful.* Stephen Wolfram Writings, April 2020.
URL: https://writings.stephenwolfram.com/2020/04/finally-we-may-have-a-path-to-the-fundamental-theory-of-physics-and-its-beautiful/
This is the announcement of the project: "energy corresponds to the flux of causal edges through spacelike hypersurfaces," and gravity is geodesic deflection by curvature arising from that flux.
*Relevance:* It gives the "energy = update activity" identification that any compute-load model has to engage with.

**Wolfram Physics Project technical introduction, §8 "Matter, Energy and Gravitation."**
URL: https://www.wolframphysics.org/technical-introduction/potential-relation-to-physics/matter-energy-and-gravitation/
"The number of causal edges that cross spacelike hypersurfaces would correspond to energy"; rest mass is associated with "local collections of nodes … that allow repeated updating events to occur."
*Relevance:* Same as above; this is the primary technical statement.

**Gorard, J. (2020).** *Some Relativistic and Gravitational Properties of the Wolfram Model.* Complex Systems 29(2), 599–654; arXiv:2004.14810.
URL: https://arxiv.org/abs/2004.14810
The paper shows that causal invariance is equivalent to a discrete general covariance, derives discrete Lorentz covariance, defines discrete Ricci curvature on hypergraphs, and obtains a discrete Einstein field equation.
*Relevance:* This is the most rigorous "gravity from a computational substrate" result available, and it works **without** a compute-shortage mechanism. It is a benchmark for what a serious version of the user's idea would need (reproduce the Einstein equations, not only redshift).

**Vopson, M. M. (2025).** *Is gravity evidence of a computational universe?* AIP Advances 15(4), 045035. Published 25 Apr 2025. DOI: 10.1063/5.0264945.
URL: https://pubs.aip.org/aip/adv/article/15/4/045035/3345217/Is-gravity-evidence-of-a-computational-universe
Abstract (per the Portsmouth research portal): "Using the second law of information dynamics and the mass–energy–information equivalence principle, we show that gravitational attraction manifests as a requirement to reduce the information entropy of matter objects in space." It derives Newton's force as an "entropic information force" and describes gravity as data compression or computational optimisation. It was an Editor's Pick.
*Relevance:* This is the most prominent recent "gravity is computation" paper, **but the mechanism is different** (compression or entropy reduction, not lag or tick rate). It should be cited as related work, not as prior art for the lag mechanism. The exact title is verified.

**Vopson, M. M. (2025).** *Response to Sabine Hossenfelder's Commentary on Vopson's Paper: Is gravity evidence of a computational universe?* IPI Letters 3(3), 30 May 2025. DOI: 10.59973/ipil.212.
URL: https://ipipublishing.org/index.php/ipil/article/view/212
This is Vopson's reply to a YouTube video critique by Sabine Hossenfelder (released 28 May 2025 according to the reply; the transcript is in the reply's appendix). Hossenfelder reportedly argued the paper contains errors and "shouldn't have been published."
*Relevance:* It records that computational-gravity claims in mainstream journals get strong pushback. The Hossenfelder video itself was not located (see §5).

**Vopson, M. M. (2023).** *The second law of infodynamics and its implications for the simulated universe hypothesis.* AIP Advances 13(10), 105308.
URL: https://pubs.aip.org/aip/adv/article/13/10/105308/2915332/The-second-law-of-infodynamics-and-its
The paper argues that information entropy stays constant or decreases over time and applies this to biology, atomic physics and cosmology as evidence for a computational universe.
*Relevance:* Background for Vopson (2025). It is a "universe optimises storage" idea, not a "universe runs out of cycles" idea.

**Vopson, M. M. & Lepadatu, S. (2022).** *Second law of information dynamics.* AIP Advances 12(7), 075310.
URL: https://pubs.aip.org/aip/adv/article/12/7/075310/2819368/Second-law-of-information-dynamics
This is the original statement of the "second law of infodynamics" (verified through the search index; the publisher page returned 403).
*Relevance:* Background.

**Vopson, M. M. (2019).** *The mass-energy-information equivalence principle.* AIP Advances 9(9), 095206. DOI: 10.1063/1.5123794.
URL: https://pubs.aip.org/aip/adv/article/9/9/095206/1076232/The-mass-energy-information-equivalence-principle
The paper proposes that a stored bit has mass, m = k_B T ln2 / c² ≈ 3.19×10⁻³⁸ kg at 300 K, and that a full hard drive should weigh more than an erased one.
*Relevance:* If information had mass it would gravitate. But the proposed mass is tiny and is *energy* (§3), so it does not turn "complexity" into a separate source of gravity.

**Vopson, M. M. (2022).** *Experimental protocol for testing the mass–energy–information equivalence principle.* AIP Advances 12(3), 035311. DOI: 10.1063/5.0087175.
URL: https://pubs.aip.org/aip/adv/article/12/3/035311/2819739/Experimental-protocol-for-testing-the-mass-energy
The paper predicts that electron–positron annihilation should emit, besides the two 511 keV photons, two ~50 µm infrared photons from the erasure of the particles' information.
*Relevance:* This is the main proposed test of "information has mass." I found no report of the experiment having been done (see §5).

**Zuse, K. (1969).** *Rechnender Raum.* Schriften zur Datenverarbeitung, Bd. 1. Braunschweig: Friedr. Vieweg & Sohn. English: *Calculating Space*, MIT Technical Translation AZT-70-164-GEMIT (Project MAC), Feb 1970.
URL: https://philpapers.org/rec/ZUSRR (PhilArchive also hosts a PDF: https://philpapers.org/archive/ZUSRR.pdf)
This is the founding text of digital physics: the universe as a cellular automaton.
*Relevance:* The origin of the "universe computes itself locally" framing that the user's idea assumes. I did not locate a Zuse passage tying gravity to compute load.

**Fredkin, E. (2003).** *An Introduction to Digital Philosophy.* International Journal of Theoretical Physics 42, 189–247. DOI: 10.1023/A:1024443232206.
URL: https://link.springer.com/article/10.1023/A:1024443232206
This paper presents "Digital Philosophy": state is bits, and evolution is a digital informational process like processor circuitry.
*Relevance:* Background framing. Fredkin's models are reversible cellular automata with a *uniform* update rate, which is the opposite of load-dependent ticking.

**Lloyd, S. (2000).** *Ultimate physical limits to computation.* Nature 406, 1047–1054. DOI: 10.1038/35023282.
URL: https://www.nature.com/articles/35023282
The "ultimate laptop" paper: the speed of computation is limited by energy (Margolus–Levitin) and memory by degrees of freedom (entropy). A maximally compressed computer is a black hole.
*Relevance:* **Cuts against the idea.** Concentrating mass-energy *raises* the local compute ceiling. Lloyd's analysis also includes gravitational time dilation as seen from outside, which is a useful quantitative bridge between the two concepts.

**Lloyd, S. (2002).** *Computational capacity of the universe.* Physical Review Letters 88, 237901. DOI: 10.1103/PhysRevLett.88.237901.
URL: https://link.aps.org/doi/10.1103/PhysRevLett.88.237901
The paper bounds the universe's history at ~10¹²⁰ operations on ~10⁹⁰ bits (10¹²⁰ including gravitational degrees of freedom).
*Relevance:* This sets the scale of any "universe as computer" budget. The budget is set by energy, which again points the wrong way for "more stuff = less compute."

**Schmidhuber, J. (1997).** *A computer scientist's view of life, the universe, and everything.* In Freksa, Jantzen & Valk (eds.), *Foundations of Computer Science*, LNCS 1337, pp. 201–208. Springer. DOI: 10.1007/BFb0052088.
URL: https://link.springer.com/chapter/10.1007/BFb0052088 (author page: https://people.idsia.ch/~juergen/everything/)
The paper applies Kolmogorov complexity to the set of possible universes and argues it may be cheaper to compute all computable universes than one.
*Relevance:* Background. Schmidhuber's later "Speed Prior" (2002) weights universes by computation *time*, which is a conceptual cousin of "computational cost shapes physics." It is not a gravity model.

### 2.3 Adjacent physics: emergent, thermodynamic and holographic gravity

**Verlinde, E. (2011).** *On the origin of gravity and the laws of Newton.* JHEP 2011(04), 029. arXiv:1001.0785. DOI: 10.1007/JHEP04(2011)029.
URL: https://link.springer.com/article/10.1007/JHEP04(2011)029
Newton's law is derived as an entropic force from changes in information associated with the positions of bodies on holographic screens. A relativistic version gives the Einstein equations.
*Relevance:* The leading "gravity from information" paper, which Vopson (2025) builds on. It concerns information *content* and entropy, not processing throughput.

**Kobakhidze, A. (2011).** *Gravity is not an entropic force.* Physical Review D 83, 021502. arXiv:1009.5414. (Follow-up: *Once more: gravity is not an entropic force*, arXiv:1108.4161.)
URL: https://link.aps.org/doi/10.1103/PhysRevD.83.021502
The paper argues that ultracold-neutron quantum bound states and neutron interferometry in Earth's gravity are inconsistent with Verlinde-type entropic gravity, because an entropic force would destroy quantum coherence.
*Relevance:* A template counterargument. Any "gravity from X" mechanism must preserve the coherent, phase-level behaviour of quantum matter in gravity (COW-type interferometry; atom interferometers). A noisy "lag" mechanism faces the same problem.

**Jacobson, T. (1995).** *Thermodynamics of Spacetime: The Einstein Equation of State.* Physical Review Letters 75, 1260–1263. arXiv:gr-qc/9504004. DOI: 10.1103/PhysRevLett.75.1260.
URL: https://link.aps.org/doi/10.1103/PhysRevLett.75.1260
The Einstein equation is derived from δQ = T dS applied to local Rindler horizons, with entropy proportional to area.
*Relevance:* This shows that the full Einstein equation can emerge from coarse-grained, information-like considerations. It is the standard a compute-load idea would have to meet.

**Bekenstein, J. D. (1981).** *Universal upper bound on the entropy-to-energy ratio for bounded systems.* Physical Review D 23, 287. DOI: 10.1103/PhysRevD.23.287.
URL: https://link.aps.org/doi/10.1103/PhysRevD.23.287
S/E ≤ 2πR/(ħc), and black holes saturate the bound.
*Relevance:* Memory capacity per region is bounded by energy × size. Like Margolus–Levitin, more energy means more capacity, not less.

**Bousso, R. (2002).** *The holographic principle.* Reviews of Modern Physics 74, 825–874. arXiv:hep-th/0203101. DOI: 10.1103/RevModPhys.74.825.
URL: https://link.aps.org/doi/10.1103/RevModPhys.74.825
A review of the covariant entropy bound (≈1.4×10⁶⁹ bits/m² of boundary area) and holography.
*Relevance:* This gives a physical "resolution limit" per region, useful if the project wants to connect a "compute budget" to known bounds. It limits storage, not tick rate.

**Margolus, N. & Levitin, L. B. (1998).** *The maximum speed of dynamical evolution.* Physica D 120, 188–195. arXiv:quant-ph/9710043. DOI: 10.1016/S0167-2789(98)00054-2.
URL: https://www.sciencedirect.com/science/article/pii/S0167278998000542
A system with mean energy E above its ground state can pass through at most 2E/(πħ) orthogonal states per second, so each joule adds at most ~3×10³³ ops/s.
*Relevance:* **The strongest single argument against the naive idea.** In real physics, a region with more mass-energy can compute *faster*, not slower. The subtlety: seen from far away, a system's energy is redshifted (E_∞ = E_local·√(−g₀₀)), so its Margolus–Levitin rate *as seen from infinity* is reduced by exactly the gravitational time-dilation factor. The bound is consistent with gravitational time dilation, but the dilation is caused by *where* the system sits in a potential, not by how much is being computed there.

**Singh, A. & Friedrich, O. (2023, rev. 2025).** *Emergence of Gravitational Potential and Time Dilation from Non-interacting Systems Coupled to a Global Quantum Clock.* arXiv:2304.01263 (the arXiv page lists it as accepted in Foundations of Physics).
URL: https://arxiv.org/abs/2304.01263
In a Page–Wootters setting, coupling to a shared quantum clock gives Schwarzschild-consistent time dilation and a Newtonian-like interaction between particles.
*Relevance:* Adjacent to the idea that "gravity comes from how systems share a clock," though done in quantum mechanics, not compute.

### 2.4 "Objects fall because time runs slower below": the g₀₀ fact and the optical analogy

**Carroll, S. M. (1997).** *Lecture Notes on General Relativity.* arXiv:gr-qc/9712019 (later expanded as *Spacetime and Geometry*, Addison-Wesley, 2004).
URL: https://arxiv.org/abs/gr-qc/9712019
Chapter 4, "the Newtonian limit," shows that for slow particles in a weak static field the geodesic equation reduces to Newton's law with **h₀₀ = −2Φ**, that is, g₀₀ ≈ −(1 + 2Φ/c²). Only the time-time component of the metric enters.
*Relevance:* This is the textbook basis for "Newtonian gravity is (almost entirely) gravitational time dilation." Verified in the PDF text.

**Gould, R. R. (2016).** *Why does a ball fall?: A new visualization for Einstein's model of gravity.* American Journal of Physics 84(5), 396–402. DOI: 10.1119/1.4939927.
URL: https://pubs.aip.org/aapt/ajp/article-abstract/84/5/396/1040243/
The paper uses a world map as an analogue of spacetime near Earth: "it is primarily the warping of time, not space, that causes a ball to fall." (A published Comment by Rębilas appeared in AJP 85, 66, 2017.)
*Relevance:* This is a citable, peer-reviewed source for the claim that the user's "gravity is a time-rate gradient" is the correct weak-field reading of GR.

**Czarnecka, A. & Czarnecki, A. (2021).** *Gravitational time dilation, free fall, and matter waves.* American Journal of Physics 89, 634–638. arXiv:2007.13851.
URL: https://arxiv.org/abs/2007.13851
"A de Broglie wave of a particle in a gravitational field turns towards the region of a smaller gravitational potential" because clocks run slower there, just as ocean waves turn toward a beach in shallower water. Free fall follows from elementary algebra, with no geodesics needed.
*Relevance:* **This is the mechanism that turns "lag" into "attraction."** A slower local tick rate makes wavefronts refract toward the slow region. Any compute-load model gets attraction for free *if* matter behaves like waves whose phase advances at the local tick rate. It is the key building block for a toy simulation.

**Epstein, L. C. (1983).** *Relativity Visualized.* San Francisco: Insight Press. ISBN 0-935218-05-X.
URL: https://archive.org/details/relativityvisual00epst
A popular, diagram-based book with a chapter on the idea that slow time makes gravity. Objects fall toward the region where time is "warped" slower.
*Relevance:* A popular-level precedent for the time-rate-gradient picture. Verified as existing, with the relevant chapter confirmed by secondary descriptions (the full text is on archive.org but was not read end to end).

**Okun, L. B., Selivanov, K. G. & Telegdi, V. L. (2000).** *On the interpretation of the redshift in a static gravitational field.* American Journal of Physics 68, 115–119. arXiv:physics/9907017.
URL: https://arxiv.org/abs/physics/9907017
The paper argues that the correct explanation of gravitational redshift is that *clocks* run at different rates at different potentials. The explanation in which "photons lose energy climbing out" is misleading.
*Relevance:* It supports framing redshift as a clock-rate phenomenon, which is the framing a tick-rate model uses.

**Evans, J., Nandi, K. K. & Islam, A. (1996).** *The optical-mechanical analogy in general relativity: New methods for the paths of light and of the planets.* American Journal of Physics 64(11), 1404–1415. (Companion: *…Exact Newtonian forms for the equations of motion of particles and photons*, Gen. Rel. Grav. 28, 1996, DOI 10.1007/BF02105085.)
URL: https://pubs.aip.org/aapt/ajp/article-abstract/64/11/1404/1054741/
For many metrics, gravity acts as an optical medium with an effective refractive index. For Schwarzschild in isotropic coordinates this is n ≈ 1 + 2GM/(rc²) in the weak field. Photon and particle paths follow from Fermat's and Maupertuis's principles.
*Relevance:* This is the "gravity as refraction" formalism. **Caution:** the factor 2 in n ≈ 1 + 2GM/(rc²) has equal contributions from g₀₀ (time) and from the spatial metric (space). A model with *only* a slower tick rate gives n ≈ 1 + GM/(rc²) and therefore only half the observed light bending (§3).

**de Felice, F. (1971).** *On the gravitational field acting as an optical medium.* General Relativity and Gravitation 2, 347–357. DOI: 10.1007/BF00758153.
URL: https://link.springer.com/article/10.1007/BF00758153
Maxwell's equations in curved spacetime can be rewritten as flat-space equations in an equivalent optical medium.
*Relevance:* This is the formal basis for the refractive-index picture.

**Einstein, A. (1911).** *Über den Einfluß der Schwerkraft auf die Ausbreitung des Lichtes.* Annalen der Physik 35, 898–908. DOI: 10.1002/andp.19113401005.
URL: https://onlinelibrary.wiley.com/doi/abs/10.1002/andp.19113401005
Using only the equivalence principle and gravitational time dilation (a variable speed of light), Einstein predicted a solar light deflection of ~0.83″, half of the later GR value of ~1.75″.
*Relevance:* **Historical proof that a "time-rate only" model gives exactly half the light bending.** This is the most useful quantitative test for the project: a pure lag field reproduces Einstein 1911, which observation rules out.

### 2.5 "Mass is a clock": Compton frequency

**Lan, S.-Y., Kuan, P.-C., Estey, B., English, D., Brown, J. M., Hohensee, M. A. & Müller, H. (2013).** *A Clock Directly Linking Time to a Particle's Mass.* Science 339, 554–557. DOI: 10.1126/science.1230767.
URL: https://www.science.org/doi/10.1126/science.1230767
This "Compton clock" uses an atom interferometer and frequency comb to reference time to a caesium atom's Compton frequency, ω = mc²/ħ.
*Relevance:* This supports the "every massive particle is a clock ticking at a rate ∝ its mass-energy" picture. In compute terms, mass is literally an internal update rate. Note the direction again: more mass means *faster* internal ticking.

**Müller, H., Peters, A. & Chu, S. (2010).** *A precision measurement of the gravitational redshift by the interference of matter waves.* Nature 463, 926–929. DOI: 10.1038/nature08776.
URL: https://www.nature.com/articles/nature08776
The paper reinterprets atom-gravimeter data as a redshift test at the Compton frequency, claiming a 10,000× improvement.
*Relevance:* This is the origin of the "matter wave = clock in a potential" experimental framing.

**Wolf, P., Blanchet, L., Bordé, C. J., Reynaud, S., Salomon, C. & Cohen-Tannoudji, C. (2011).** *Does an atom interferometer test the gravitational redshift at the Compton frequency?* Classical and Quantum Gravity 28, 145017. DOI: 10.1088/0264-9381/28/14/145017.
URL: https://iopscience.iop.org/article/10.1088/0264-9381/28/14/145017
The paper argues that no, atom gravimeters test the universality of free fall, not the redshift. The two sides exchanged a Comment and Reply in CQG in 2012.
*Relevance:* This is an important caveat. The "mass is a clock" framing is *contested* as an interpretation of experiments, so the project should present it carefully.

### 2.6 Game-engine and computing analogues

**CCP Veritas (2011).** *Introducing Time Dilation (TiDi).* EVE Online dev blog, 22 Apr 2011.
URL: https://www.eveonline.com/news/view/introducing-time-dilation-tidi
This is the design blog. When a solar-system node is overloaded, the server slows the game clock so that "a large majority of the load … tied to the clock" is spread out, instead of dropping or delaying commands. It gives an illustrative big-fight scenario in which dilation drops to ~5%, sits around 30% during combat, then recovers to 100%.
*Relevance:* **This is the best real-world analogue.** A region's simulated time slows in proportion to its computational load, while players inside experience consistent, if slow, physics.

**CCP Veritas (2012).** *Time Dilation – How's That Going?* EVE Online dev blog, 10 Feb 2012.
URL: https://www.eveonline.com/news/view/time-dilation-hows-that-going
It confirms that "Time Dilation (TiDi) was activated fully on Jan 18th" (2012).
*Relevance:* This gives the deployment date. **Accurate summary:** announced April 2011, fully activated on the Tranquility server on 18 Jan 2012.

**EVE University Wiki.** *Time dilation.*
URL: https://wiki.eveuniversity.org/Time_dilation
"The maximum time dilation speed is 10%, making one second in game become ten seconds in real time." TiDi applies per server *node* (hardware hosting one or more solar systems).
*Relevance:* This is the source for the **10% floor**, a community wiki rather than a CCP document. Per-node, uniform dilation is also a key *disanalogy* (§4): there is no gradient inside a system, so no "force" pulls ships toward busy systems.

**Purbrick, J. (2014).** *Beyond Time Dilation?* The Creation Engine No. 2 (blog), 29 Jan 2014.
URL: http://jimpurbrick.com/2014/01/29/beyond-time-dilation/
A former Linden Lab and CCP developer discusses TiDi's limits. The basic problem is O(n²) (n players each need to see n others), and he proposes interest filtering.
*Relevance:* It points out that simulation cost scales with *interactions* (∝ n²), not with mass. A compute-load gravity would then scale nonlinearly with the amount of matter, whereas gravity is linear in mass (superposition) in the weak field.

**Second Life Wiki.** *llGetRegionTimeDilation.*
URL: https://wiki.secondlife.com/wiki/LlGetRegionTimeDilation
Time dilation is "a method the server uses to cope with simulator lag … Physics and script generated lag can result in time dilation." It returns 0.0 to 1.0, the ratio of script time to real time. A related wiki page describes "Time Dilation" as the physics simulation rate relative to real time.
*Relevance:* This is a second, independent virtual-world implementation of per-region load-driven time dilation, predating EVE's (the exact introduction date was not verified).

**Improbable, SpatialOS documentation.** *Workers and load balancing* (SDK 13.x).
URL: https://docs.improbable.io/reference/13.7/shared/concepts/workers-load-balancing
The virtual world is split into spatial regions, each assigned to a server-worker. Strategies include rectangular or hexagonal grids and entity-ID sharding, with hysteresis to prevent authority "thrashing" at boundaries.
*Relevance:* This is the alternative to slowing time: an engine can *add compute* to dense regions (spatial partitioning) rather than dilate. Reality, if it were an engine, would be using the dilation strategy, not the rebalancing one.

**Jefferson, D. R. (1985).** *Virtual Time.* ACM Transactions on Programming Languages and Systems 7(3), 404–425. DOI: 10.1145/3916.3988.
URL: https://dl.acm.org/doi/10.1145/3916.3988
This introduces virtual time and the Time Warp protocol for parallel discrete-event simulation. Each logical process advances its own local virtual time at its own pace, with rollbacks when causality is violated.
*Relevance:* This is the computer-science formalism for "different regions of one simulation run at different local clock rates yet stay causally consistent." It is useful for designing the project's toy simulation, and it links to Experiment 001 (rollback).

**Aarseth (1963) individual time steps; McMillan (1986) and Makino (1991) block time steps.** These are described in, e.g., Pelupessy, Jänes & Portegies Zwart (2012), *N-body integrators with individual time steps from Hierarchical splitting*, New Astronomy (2012), DOI 10.1016/j.newast.2012.05.009; arXiv:1205.5668.
URL: https://arxiv.org/abs/1205.5668
In collisional N-body codes, particles in dense or fast regions get *smaller* time steps, quantised to powers of two.
*Relevance:* **An instructive inversion.** Real simulation codes spend *more* wall-clock time per unit of simulated time in dense regions, but they keep simulated time globally consistent, so there is no dilation visible inside the simulation. The "lag" is visible only to the operator. (The original Aarseth 1963 and Makino 1991 papers were not individually verified; see §5.)

**Springel, V. (2005).** *The cosmological simulation code GADGET-2.* MNRAS 364, 1105–1134. arXiv:astro-ph/0505010. DOI: 10.1111/j.1365-2966.2005.09655.x.
URL: https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2966.2005.09655.x
The code uses individual adaptive timesteps on a power-of-two hierarchy of "rungs," so dense regions take more, finer steps.
*Relevance:* Same inversion as above, in a widely used production code.

### 2.7 Constraints on simulation-type hypotheses

**Beane, S. R., Davoudi, Z. & Savage, M. J. (2014).** *Constraints on the universe as a numerical simulation.* European Physical Journal A 50, 148. arXiv:1210.1847. DOI: 10.1140/epja/i2014-14148-0.
URL: https://link.springer.com/article/10.1140/epja/i2014-14148-0
If spacetime were a lattice, the GZK cosmic-ray cutoff bounds the inverse lattice spacing at b⁻¹ ≳ 10¹¹ GeV, and lattice anisotropy could appear in the directions of the highest-energy cosmic rays.
*Relevance:* This is the model for how to turn a "simulation" idea into a falsifiable, bounded prediction. The project should aim for the same.

**Okołów, A. (2020).** *Does time always slow down as gravity increases?* European Journal of Physics (2020); arXiv:1906.09405.
URL: https://arxiv.org/abs/1906.09405
The paper gives stationary-observer examples that contradict "time slows down as gravity increases." Dilation tracks potential and observer setup, not local field strength.
*Relevance:* This supports the counterargument that dilation is *not* a function of local density or local "load."

**Lewis, G. F. & Brewer, B. J. (2023).** *Detection of the cosmological time dilation of high-redshift quasars.* Nature Astronomy 7, 1265–1269. arXiv:2306.04053.
URL: https://www.nature.com/articles/s41550-023-02029-2
The paper detects (1+z) time dilation in the variability of 190 quasars (early-universe events appear up to ~5× slower).
*Relevance:* This is the data behind Kassiantchouk's anti-lag argument. It shows that time dilation also arises from expansion, with no local "load," so a compute-load story would need a separate account of it.

---

## 3. Established physics facts we must respect

1. **In the weak field, Newtonian gravity comes from g₀₀.** For slow bodies, g₀₀ ≈ −(1 + 2Φ/c²) and the geodesic equation gives **a = −∇Φ** (Carroll 1997, ch. 4, h₀₀ = −2Φ). Equivalently, the fractional clock rate is dτ/dt ≈ 1 + Φ/c², and falling is motion toward slower clocks (Gould 2016; Czarnecka & Czarnecki 2021). *This is the part of the idea that is simply correct:* a tick-rate gradient does produce Newtonian attraction for slow matter.

2. **The time-rate field alone gives only half the light bending.** Einstein (1911), with time dilation only, predicted ~0.83″. GR, which also has spatial curvature, predicts ~1.75″. Light deflection and Shapiro delay measure the PPN parameter γ. Cassini gives **γ = 1 + (2.1 ± 2.3)×10⁻⁵** (Bertotti, Iess & Tortora 2003, Nature 425, 374; https://www.nature.com/articles/nature01997). A pure "lag" model has γ = 0 for light and is excluded by a wide margin unless it also warps spatial distances.

3. **Gravitational redshift is measured with extreme precision and at tiny heights.**
   - Pound & Rebka (1960), *Apparent Weight of Photons*, PRL 4, 337 (https://link.aps.org/doi/10.1103/PhysRevLett.4.337): 22.5 m tower, Mössbauer ¹⁴·⁴ keV γ-rays.
   - Chou, Hume, Rosenband & Wineland (2010), *Optical Clocks and Relativity*, Science 329, 1630 (https://www.science.org/doi/10.1126/science.1192720): a 33 cm height change is resolved, with fractional shift (4.1 ± 1.6)×10⁻¹⁷.
   - Bothwell et al. (2022), *Resolving the gravitational redshift across a millimetre-scale atomic sample*, Nature 602, 420–424 (https://www.nature.com/articles/s41586-021-04349-7): a linear redshift gradient is measured *within* a ~1 mm strontium cloud, with a measurement uncertainty of 7.6×10⁻²¹.
   - *Implication:* the dilation is a smooth function of height (potential) down to the millimetre scale and ~10⁻²¹ fractional precision, with no granularity, jitter or dependence on how busy the lab is. A compute-lag model has to reproduce this smoothness.

4. **GPS confirms the potential-dependence operationally.** Ashby (2002), *Relativity and the Global Positioning System*, Physics Today 55(5), 41 (DOI 10.1063/1.1485583), and Ashby (2003), Living Reviews in Relativity 6, 1 (https://link.springer.com/article/10.12942/lrr-2003-1). Satellite clocks are given a pre-launch "factory offset" of −4.4645×10⁻¹⁰ (Ashby 2002). That is ≈ 38.6 µs/day (4.4645×10⁻¹⁰ × 86 400 s): a gravitational blueshift minus a velocity time dilation. The commonly quoted split is ~45.7 µs/day minus ~7.1 µs/day; I checked only the net figure against Ashby's text, and the split is a common textbook figure not confirmed in the source. Satellite clocks sit in *emptier* space yet run *faster*, which fits "potential" and not "local load."

5. **Universality of free fall (weak equivalence principle).** Gravity accelerates all compositions identically.
   - MICROSCOPE final result: **η(Ti, Pt) = [−1.5 ± 2.3 (stat) ± 1.5 (syst)] × 10⁻¹⁵** (Touboul et al. 2022, PRL 129, 121102; https://link.aps.org/doi/10.1103/PhysRevLett.129.121102; arXiv:2209.15487).
   - Eöt-Wash torsion balance: η(Be–Ti) = (0.3 ± 1.8)×10⁻¹³ (Schlamminger et al. 2008, PRL 100, 041101; https://link.aps.org/doi/10.1103/PhysRevLett.100.041101).
   - *Implication:* titanium and platinum differ greatly in nuclear structure, binding energy fraction, electron count and "internal complexity," yet they fall identically to ~10⁻¹⁵. If the local lag depended on information content, complexity or update cost *per unit of mass-energy*, different materials would fall differently.

6. **Gravity couples to total energy, including binding energy, and the source side obeys the same universality.**
   - Lunar laser ranging tests the strong equivalence principle, where gravitational self-energy also falls universally: Δ(M_G/M_I)_SEP = (−2.0 ± 2.0)×10⁻¹³ (Williams, Turyshev & Boggs 2004, PRL 93, 261101; https://link.aps.org/doi/10.1103/PhysRevLett.93.261101).
   - Active and passive gravitational mass are equal: Kreuzer (1968), Phys. Rev. 169, 1007 (https://link.aps.org/doi/10.1103/PhysRev.169.1007), with later LLR tests (PRL 131, 021401, 2023; authors not individually verified).
   - *Implication:* what *sources* gravity is mass-energy (the stress-energy tensor), not "number of objects," "number of interactions" or "information." Any "load" must equal energy density up to ~10⁻¹³ or better.

7. **Superposition and linearity.** In the weak field, the potentials of separate masses add linearly. Simulation cost typically scales with *pairwise interactions* (O(n²), Purbrick 2014) or with the number of objects. A "load" that tracks cost, not mass, would give nonlinear gravity.

8. **Dilation depends on potential, not local density or field strength.** A clock at the centre of a uniform spherical shell (or at the centre of the Earth) feels zero net gravitational force yet is *maximally* time-dilated relative to infinity. A clock in empty space near a planet is dilated though no "stuff" is present locally. (Standard GR; see Okołów 2020 for related counterexamples.)

9. **Information stored as energy weighs only its energy.** Vopson's proposed information mass is m = k_B T ln2 / c² (≈3×10⁻³⁸ kg per bit at 300 K). That is the mass-equivalent of an *energy* and is fully covered by E = mc². No experiment has shown a separate gravitational effect of information. Vopson's annihilation test (2022) remains a proposal as far as I found.

10. **Physical compute capacity rises with energy.** Margolus–Levitin (1998): ops/s ≤ 2E/(πħ). Bekenstein (1981): storage ≤ 2πRE/(ħc ln2) bits. Lloyd (2000, 2002). The Compton frequency (Lan et al. 2013) makes the same point: the internal clock rate ∝ mass-energy.

11. **Local invisibility of dilation.** No local experiment detects one's own gravitational time dilation: the Einstein equivalence principle and local position invariance, tested by redshift experiments. This is *compatible* with a lag model, since an avatar can't see its own frame rate (Whitworth 2010), and should be listed as a point of consistency, not a problem.

12. **Quantum coherence in gravity.** Neutron and atom interferometers show that gravity produces coherent, deterministic phase shifts in quantum matter. Any mechanism that adds noise, jitter or coarse-graining (entropic or lag-based) is constrained (Kobakhidze 2011).

---

## 4. Strongest counterarguments

1. **The sign problem (energy = compute, not a drain on it).** In every physical theory of computation, more energy in a region means *more* operations per second (Margolus–Levitin, Lloyd, Compton frequency). Even Wolfram's hypergraph identifies mass with *more* update activity. "More stuff → less compute per item" requires an external, fixed-capacity host whose budget is independent of the simulated energy. That is unobservable in principle and so hard to falsify. The observed dilation is instead exactly what you get from redshifting the (increased) local energy by the potential.

2. **Dilation tracks potential, not load.** The centre of the Earth (maximum dilation, zero force, and not the densest "busiest" region relative to its dilation), empty space near a mass, and the GPS satellites that run fast in emptier space all show that dilation is a *non-local* field (Φ, solving ∇²Φ = 4πGρ), not a function of local contents. A load model would need load to "leak" outward as 1/r. That amounts to inventing the gravitational potential again under a different name.

3. **Composition independence (MICROSCOPE, 10⁻¹⁵).** If "load" meant information, complexity, number of particles or update cost, different materials with the same mass-energy would source and feel gravity differently. They don't, to parts in 10¹³–10¹⁵. So the "load" has to be *exactly* mass-energy. Saying "gravity is compute load" then reduces to a relabelling of "gravity is sourced by energy," with no extra predictive content unless it predicts a deviation, and every predicted deviation so far (e.g., Lee's ITD) runs into these bounds.

4. **Half the light bending.** A scalar tick-rate field reproduces Newtonian falling but predicts γ = 0 light bending (Einstein 1911, 0.83″). Observation gives γ = 1 to 2×10⁻⁵. The lag model must add a second ingredient (spatial "stretching") that the processing-load story does not naturally supply. Alagoz (2010) and Whitworth (2010) claim light bending qualitatively but do not get the factor 2.

5. **Linearity and superposition.** Real compute cost scales with interactions (≈n² for naive all-pairs, n log n with trees, and cost depends on algorithm, not physics). Gravity is linear in mass in the weak field, which would be an odd coincidence for a cost function.

6. **Smoothness and precision.** Clock comparisons resolve redshift gradients across 1 mm at the 10⁻²¹ level (Bothwell 2022) with no sign of quantisation, jitter or load fluctuations. Game-server TiDi is stepwise, noisy and reactive. A physical "lag" would need to be perfectly deterministic and smooth, which is again just a smooth field.

7. **No gradient in the analogue.** EVE's TiDi slows a whole node uniformly and exerts no "pull." Players are not attracted to lagging systems. The analogy supports *dilation from load* but not *attraction from a dilation gradient*. Attraction needs an extra ingredient: wave-like propagation whose phase advances at the local tick rate (Czarnecka & Czarnecki 2021). That ingredient comes from known physics, not from the analogy.

8. **Real simulators don't do this.** Production N-body codes (Aarseth, Makino, GADGET-2) spend *more* host time on dense regions while keeping simulated time globally consistent, and MMO engines prefer to rebalance (SpatialOS) rather than dilate. A universe-scale engine that dilated dense regions would be choosing a strategy that engineers use only as a last resort. This is an argument from design plausibility, not a physics refutation, and should be presented as such.

9. **Cosmological time dilation without local load.** Distant quasars and supernovae appear time-dilated by (1+z) (Lewis & Brewer 2023), and the cause is expansion. A load model would need a separate explanation. (This is a weak argument on its own because the effect has a different origin in GR; it mainly shows that "time dilation" has several sources, only one of which a load model addresses.)

10. **Unfalsifiability risk.** If the host's budget is invisible and the load is defined to equal mass-energy, the hypothesis makes no new predictions. To be scientific, the project must state a deviation, such as dependence on complexity, granularity at some scale, saturation in extreme density, or anisotropy, and check it against the bounds above.

---

## 5. Unverified leads

These came up during the search but could not be verified to the standard of §2. They should be checked before being cited.

- **Hossenfelder's video critique of Vopson (2025).** Its existence and date (28 May 2025) are stated in Vopson's IPI Letters reply. I did not locate the YouTube video's exact title or URL.
- **"Information Without Substance: Structural Limits of Mass-Energy-Information Equivalence."** A ResearchGate item (https://www.researchgate.net/publication/391663834) described in search snippets as a rebuttal of Vopson's principle (including a claimed divergence of bit-mass as T→0). Author, venue and date are unverified.
- **Whether Vopson's positron-annihilation experiment (2022 protocol) has been performed.** I found no report, but absence of evidence from web searches is not conclusive.
- **Reddit (r/SimulationTheory, r/AskPhysics, r/Physics) and YouTube** threads and videos saying "time dilation is lag" or "gravity is the universe lagging." These almost certainly exist, given the Quora question and the Medium essays, but I could not retrieve specific, dated, verifiable posts through the available search tools. A manual search on those platforms is recommended if the project wants to cite the earliest informal instance.
- **Medium essays by Petersen, Kassiantchouk and Giannakopoulos.** URLs and authors are confirmed through the search index, but full text and publication dates could not be fetched (HTTP 403). The summaries above rely on search snippets.
- **Tom Campbell, *My Big TOE* (2003), and Rizwan Virk, *The Simulation Hypothesis* (2019).** Both are popular simulation-hypothesis books that may discuss relativity as rendering or processing effects. I did not verify any specific passage about gravity or time dilation as compute load.
- **Whitworth's later "Quantum Realism" chapters on gravity** (brianwhitworth.com; ResearchGate "Quantum Realism Chapter 2: Creating Space and Time (2025)"). These may contain a fuller "processing load → gravity" derivation. Not reviewed.
- **Alagoz (2010) venue.** "OncuBilim Algorithm and Systems Labs, Vol. 10, Art. No. 01" appears on the PDF header. I could not confirm whether this is a peer-reviewed journal.
- **Primary N-body time-step papers:** Aarseth, S. J. (1963), MNRAS 126, 223, and Makino, J. (1991), PASJ 43, 859 / ApJ 369, 200. These are cited through secondary sources only. Exact volume and page numbers are not independently verified.
- **LLR test of active = passive mass (2023, PRL 131, 021401).** The paper was found in a search listing, but its authors were not verified.
- **The date Second Life introduced region time dilation.** Not verified; it is presumed to be in the 2000s.
- **The "EVE TiDi floor at 0.1%" wording** in one automated summary of the 2011 dev blog was *not* confirmed and conflicts with the 10% floor documented by EVE University. Treat it as a probable misreading and do not cite it.
- **"The time-dilation Effect as a Computational Resource" (arXiv:0907.1579)** and **Hsu, "Information, information processing and gravity" (arXiv:0704.1154).** Both appeared in searches and look relevant to "gravity limits computation" (the reverse direction). Not reviewed.
