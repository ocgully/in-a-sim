# Experiment 001 — "Collapse as Rollback": Prior-Art Review

*Compiled 2026-09-23. Scope: a thought experiment exploring the simulation hypothesis. Nothing here argues that we live in a simulation. The review records who has said what, and which physics any such analogy has to respect.*

**How citations were checked:** Every entry in the bibliography was checked against a primary or authoritative record: arXiv API metadata, Crossref DOI metadata, the publisher's page, or the author's own blog or book listing. Where we quote a passage, we read it in the source text (PDF text extraction or a direct page fetch). Anything we could not verify is listed under **Unverified leads**. Hacker News comments were found through the public Algolia HN API, and their IDs and dates are given.

---

## 1. Summary verdict

### (a) Directly anticipated (clear prior art exists)

| Component of our idea | Prior art |
|---|---|
| Collapse / measurement read as "render on demand", "lazy evaluation" or "only compute what is observed" | Bostrom 2003 (details "filled in ad hoc" when someone looks through a microscope); Campbell's *My Big TOE* 2003; Campbell, Owhadi, Sauvageau & Watkinson 2017 (the main formal statement); Virk 2019; sigfpe 2008 blog; many Hacker News comments from 2013 onward. **This part of the idea is well trodden and not novel.** |
| A simulator that **rewinds and re-runs** to keep things consistent | **Bostrom 2003**: "the director could skip back a few seconds and rerun the simulation in a way that avoids the problem." Bostrom offers this as error correction for anomalies, **not** as a model of quantum measurement. |
| Bell nonlocality explained because the simulator is not bound by in-world distances (the "central server is inherently nonlocal" point) | **Campbell et al. 2017** make this point explicitly: "notions of locality and distance defined within the simulation do not constrain the action space of the system performing the simulation." An informal version appears in HN comment 6250144 (2013), which compares entanglement to "dereferencing a pointer". |
| A "VR server" doing internal computation before content is shown, and keeping the world consistent across players | Campbell et al. 2017, which uses the words "Virtual Reality server" and a "multi-player VR game". |
| Many-Worlds discussed in computational-resource terms | Deutsch 1997 ("where was the number factorized?"); Aaronson 2011/2013 rebuttal; Aaronson's blog on the exponential cost of simulating QM classically; Carroll 2014 and Vaidman (SEP) on the "extravagance" objection. |

### (b) Partially overlapping (the structure resembles ours, but nobody frames it as netcode)

- **Retrocausal and time-symmetric interpretations.** Cramer's transactional "handshake" (1986), Aharonov's two-state vector formalism (1964/2001), Price & Wharton (2015), Wharton & Argaman (2020) and Leifer & Pusey (2017) all fix outcomes using both past and future boundary conditions. That is structurally close to a server settling an event only after later information arrives. None of them uses a simulation or netcode framing.
- **Postselected closed timelike curves** (Lloyd et al. 2011) and **PostBQP = PP** (Aaronson 2005). "Discard the branches that turned out inconsistent" is formalised here, and its computational cost is known. This is the closest rigorous analogue to "rollback plus determination".
- **Optimistic distributed simulation, Time Warp** (Jefferson 1985). This is computer-science prior art for rollback in distributed simulation: processes run ahead speculatively, roll back when a message with an earlier timestamp arrives, and cancel side effects with "antimessages". We found nobody connecting it to quantum mechanics.
- **The FPS lag-compensation literature describes itself in time-travel language.** Bernier (Valve, GDC 2001) calls lag compensation "taking a step back in time, on the server" and says the victim is "transported backward in time and is hit". He explicitly acknowledges "paradoxes or inconsistencies". This vocabulary exists on the game side, but no physics link is drawn.
- **Campbell et al. 2017 on the delayed-choice eraser.** They propose that X (the screen hit) and R (erase or keep) are "realized at the moment the recorded data becomes available to the observer". That is **deferred joint resolution**, a lazy-evaluation reading. It is not rollback: nothing already rendered gets revised.

### (c) Appears novel (no prior art found)

After the searches below, we found **no source** that maps quantum measurement, delayed choice or entanglement onto:

- FPS **lag compensation / "favor the shooter"** (server-side rewind, a hit test at the shooter's timestamp, the victim's perspective overridden);
- **rollback netcode (GGPO-style)** or input prediction with re-simulation;
- **client-side prediction plus server reconciliation** as a model of decoherence, Wigner's friend or observer disagreement;
- **Time Warp / antimessages** as a model of retrocausal interpretations;
- a **netcode-style cost comparison** of "keep every speculative branch" (MWI) vs "keep a bounded rollback buffer and commit" (collapse) vs "lockstep deterministic replay" (superdeterminism).

**Searches run** (web search, plus the HN Algolia API over comments, plus arXiv): "lag compensation" + quantum / simulation hypothesis; "rollback netcode" + wave function / quantum / quantum eraser / universe; "netcode" + quantum / entanglement / wave function / simulation universe; "favor the shooter" + quantum; "client-side prediction" + quantum; "speculative execution" + quantum / retrocausality; "delayed choice" + netcode / rollback / server / rewind / video game; "hit registration" / "hitscan" + quantum; "Wigner's friend" + distributed systems / eventual consistency / consensus; wave function collapse + database transaction / commit / consensus; Time Warp / virtual time + quantum; "desync" + quantum; "relativity of simultaneity" + netcode; GGPO + superposition. HN Algolia returned **0 hits** for "rollback quantum eraser", "netcode entanglement", "rollback netcode physics universe" and "lag compensation universe simulation". The hits for "netcode quantum" were all about the *Photon Quantum* game engine, a name collision.

**Coverage caveats (important for public claims):**
1. Reddit could not be searched directly, because our tools' access to reddit.com is blocked.
2. YouTube and TikTok were searched only through the general web index. Transcripts were not searched.
3. Discord, X/Twitter and podcasts were not searched.

The netcode analogy is intuitive to gamers, so informal prior art in those venues is **likely enough that we should not claim priority**. The accurate public wording is: *"We found no published or indexed source making this specific mapping."* Do not say "this is new."

**One-line verdict:** Collapse as render-on-demand and the "server explains nonlocality" idea are well anticipated, chiefly by Bostrom 2003 and Campbell et al. 2017. Even "rewind and re-run" appears in Bostrom 2003. The specific **lag-compensation / rollback-netcode mapping**, and a netcode-style cost comparison of MWI, collapse and superdeterminism, have no indexed prior art that we could find. The physics also imposes a sharp constraint on that mapping (see §4, counterargument 1).

---

## 2. Annotated bibliography

### 2.1 Measurement as render-on-demand / lazy evaluation (simulation literature)

**Bostrom, N. (2003). "Are We Living in a Computer Simulation?" *The Philosophical Quarterly* 53(211): 243–255.** doi:10.1111/1467-9213.00309. PDF: https://simulation-argument.com/simulation.pdf
- *Summary:* This is the paper that introduced the simulation argument. In discussing computational cost, Bostrom says microscopic phenomena "could likely be filled in ad hoc". A simulator "could fill in sufficient detail ... on an as-needed basis". If errors occur, "the director could easily edit the states of any brains that have become aware of an anomaly ... Alternatively, the director could skip back a few seconds and rerun the simulation in a way that avoids the problem." (Quotes checked against the PDF text.)
- *Relevance:* This is the **earliest verified prior art for both render-on-demand and rollback-and-rerun** in a simulation context. It does not link rollback to quantum measurement. It is also the source of the "edit the observers' memories" alternative, which is a direct competitor to our rollback model.

**Campbell, T., Owhadi, H., Sauvageau, J., & Watkinson, D. (2017). "On Testing the Simulation Theory." *International Journal of Quantum Foundations* 3: 78–99.** arXiv:1703.00058. https://arxiv.org/abs/1703.00058 · IJQF PDF: https://users.cms.caltech.edu/~owhadi/index_htm_files/IJQF2017.pdf
- *Summary:* The authors assume a finite simulator that would, "as in a video game, render content (reality) only at the moment that information becomes available for observation by a player". Detection by a machine counts only as "internal computation performed by the Virtual Reality server". They argue that Bell nonlocality is simply explained because in-world distances do not constrain the simulator. They also say the VR must balance "preserving the consistency of the VR" against "avoiding detection". Finally, they propose variants of the double-slit and delayed-choice eraser experiments that would test whether "availability of which-way data" to an observer changes the outcome.
- *Relevance:* This is the **closest prior art overall.** It anticipates render-on-demand, the server framing and the Bell-nonlocality point. Its account of the delayed-choice eraser is **deferred joint realization**: X and R are realized together when the data becomes available. It is not a rewind-and-override. Our lag-compensation framing has to set itself apart from this paper explicitly.

**Campbell, T. (2003). *My Big TOE* (trilogy: *Awakening*, *Discovery*, *Inner Workings*). Lightning Strike Books.** ISBNs 9780972509404 / 9780972509428 / 9780972509442. https://www.my-big-toe.com/
- *Summary:* Campbell presents a consciousness-first model in which physical reality is a "virtual reality" rendered for conscious participants, with probabilistic outcomes resolved when experienced.
- *Relevance:* This is the popular source of the "rendered VR" reading of QM. It is not peer reviewed. We did not read the text of the books; the description comes from the publisher/author site and Campbell et al. 2017.

**Virk, R. (2019). *The Simulation Hypothesis: An MIT Computer Scientist Shows Why AI, Quantum Physics and Eastern Mystics All Agree We Are in a Video Game*. Bayview Books.** ISBN 978-0-9830569-0-4. (Expanded edition, Penguin Random House: https://www.penguinrandomhouse.com/books/774523/the-simulation-hypothesis-by-rizwan-virk/)
- *Summary:* Virk treats quantum indeterminacy and the observer effect as analogous to video-game rendering optimisations, "conditional rendering". He also discusses parallel universes as branches.
- *Relevance:* This is the most prominent popular book making the video-game/rendering analogy, so the render-on-demand framing is **not ours**. We found no evidence that Virk discusses netcode or lag compensation, but we have not read the full text (see Unverified leads).

**sigfpe (Dan Piponi) (2008-05-21). "Life in a Lazy Universe." *A Neighborhood of Infinity* (blog).** http://blog.sigfpe.com/2008/05/life-in-lazy-universe.html
- *Summary:* The post argues that a simulated universe could use lazy evaluation and compute only what observers demand. It focuses on computability and continuity rather than on quantum mechanics.
- *Relevance:* This is early programmer-community prior art for "lazy universe". It does not discuss rollback.

**Hacker News comments (checked through the HN Algolia API):**
- ID 6250144, *slacka*, 2013-08-21. Asks whether the universe is doing "lazy evaluation", and says "Quantum entanglement is like dereferencing a pointer to our universe's data". → informal prior art for **the shared-memory explanation of nonlocality**.
- ID 18026267, *jeletonskelly*, 2018-09-19. "Observing a quantum state forces evaluation."
- ID 41725523, *bwood*, 2024-10-02. "observer effect, quantum entanglement and wavefunction collapse --> lazy evaluation; speed of light --> speed of causality…"
- "Ask HN: Quantum physics observer effect = lazy evaluation?" https://news.ycombinator.com/item?id=9809295 (thread seen in search results; page fetch was rate-limited, so the date was not checked).
- *Relevance:* The lazy-evaluation analogy is folk knowledge among programmers. None of these comments mentions rollback, lag compensation or netcode.

**Irwin, K., Amaral, M., & Chester, D. (2020). "The Self-Simulation Hypothesis Interpretation of Quantum Mechanics." *Entropy* 22(2): 247.** doi:10.3390/e22020247
- *Summary:* The paper proposes that the universe is a self-simulating, code-theoretic system and relates this to quantum measurement. (Metadata checked through Crossref. The full text returned 403, so we did not read the argument in detail.)
- *Relevance:* This is another "QM as simulation" interpretation in a peer-reviewed venue, relevant to positioning. It does not appear to use netcode framing.

**Neukart, F., Indset, A., Pflitsch, M., & Perelshtein, M. (2022). "Do we live in a [quantum] simulation? Constraints, observations, and experiments on the simulation hypothesis." arXiv:2212.04921.** https://arxiv.org/abs/2212.04921
- *Summary:* The paper discusses computability constraints and nested simulations. It suggests that exhausting the resources of a simulation chain might force an observable intervention by the programmer.
- *Relevance:* This is recent context for proposed tests. It does not treat measurement as rollback.

### 2.2 Netcode / rollback / distributed simulation (the computer-science side of the analogy)

**Bernier, Y. W. (2001). "Latency Compensating Methods in Client/Server In-game Protocol Design and Optimization." *Proceedings of the Game Developers Conference 2001*, San Jose.** PDF: https://www.gamedevs.org/uploads/latency-compensation-in-client-server-protocols.pdf
- *Summary:* This is the canonical Valve write-up of client-side prediction and lag compensation (Half-Life, Counter-Strike). The server "move[s] the other players backwards in time to exactly where they were when the current player's user command was created", runs the hit test, then restores their positions. Bernier explicitly notes "paradoxes or inconsistencies": a lagged shooter can hit someone who, from their own view, had already ducked behind cover. That player is "transported backward in time and is hit".
- *Relevance:* This is the **primary source for the mechanism our analogy uses.** The game-side literature itself uses time-travel and paradox language. The inconsistency Bernier describes (the victim *sees* the contradiction) is exactly what quantum experiments do **not** show; see §4.

**GGPO (Pony / Tony Cannon), rollback networking SDK (2009; open-sourced 2019).** https://www.ggpo.net/
- *Summary:* Peer-to-peer rollback netcode. Each peer predicts remote inputs (it assumes they repeat), simulates ahead, and when real inputs arrive that differ, rolls back to the last confirmed frame and re-simulates.
- *Relevance:* This is the "rollback netcode" reference model. Note that GGPO requires a **deterministic** simulation, which is structurally closer to superdeterminism / 't Hooft than to collapse.

**Jefferson, D. R. (1985). "Virtual Time." *ACM Transactions on Programming Languages and Systems* 7(3): 404–425.** doi:10.1145/3916.3988
- *Summary:* This paper introduced the Time Warp optimistic synchronisation protocol for distributed simulation. Logical processes execute speculatively. A "straggler" message with an earlier timestamp causes a rollback, and messages sent in error are cancelled with antimessages.
- *Relevance:* This is the **formal computer-science ancestor of rollback netcode.** It gives exact vocabulary (straggler, rollback, antimessage, global virtual time / commit horizon) for a rigorous version of our analogy. "Global virtual time" is the point before which nothing can ever be rolled back, which maps onto "irreversible record / decoherence". No quantum link was found.

### 2.3 Retrocausal and time-symmetric interpretations (structural resemblance to rollback)

**Wheeler, J. A. (1978). "The 'Past' and the 'Delayed-Choice' Double-Slit Experiment." In A. R. Marlow (ed.), *Mathematical Foundations of Quantum Theory*, Academic Press, pp. 9–48.** doi:10.1016/B978-0-12-473250-6.50006-6
- *Summary:* Wheeler proposed choosing whether to measure "which way" or "both ways" after the photon has passed the slits or beam splitter. His conclusion was that one should not attribute a definite past path to an unobserved photon; it is not that the choice causes the past.
- *Relevance:* This is the origin of the "decide later" intuition behind our idea. As the Physics World piece below also notes, Wheeler himself did not endorse backward-in-time influence.

**Jacques, V., Wu, E., Grosshans, F., Treussart, F., Grangier, P., Aspect, A., & Roch, J.-F. (2007). "Experimental Realization of Wheeler's Delayed-Choice Gedanken Experiment." *Science* 315(5814): 966–968.** doi:10.1126/science.1136303; arXiv:quant-ph/0610241
- *Summary:* A single-photon realisation of Wheeler's experiment, with the choice to insert or remove the second beam splitter made randomly and space-like separated from entry. The results agree with quantum predictions.
- *Relevance:* This is the experimental anchor. The outcomes are standard QM, with no anomaly.

**Scully, M. O., & Drühl, K. (1982). "Quantum eraser: A proposed photon correlation experiment concerning observation and 'delayed choice' in quantum mechanics." *Physical Review A* 25: 2208–2213.** doi:10.1103/PhysRevA.25.2208
- *Summary:* The original quantum eraser proposal: which-path information stored in an entangled system can be "erased" to recover interference in *correlated subsets*.
- *Relevance:* Background for the delayed-choice eraser.

**Kim, Y.-H., Yu, R., Kulik, S. P., Shih, Y., & Scully, M. O. (2000). "Delayed 'Choice' Quantum Eraser." *Physical Review Letters* 84: 1–5.** doi:10.1103/PhysRevLett.84.1; arXiv:quant-ph/9903047 (posted 1999)
- *Summary:* This is the experiment usually cited. Signal photons hit D0. Their idler partners are routed, about 8 ns later (2.5 m of extra optical path), to detectors that either keep which-path information (D3, D4) or erase it (D1, D2). Interference appears **only in the joint-detection (coincidence) rates** R01 and R02. It does not appear in R03 or R04, and never in D0 alone.
- *Relevance:* This is the experiment our "rollback" intuition targets. The facts we must respect are in §3.

**Ma, X.-S., Zotter, S., Kofler, J., Ursin, R., Jennewein, T., Brukner, Č., & Zeilinger, A. (2012). "Experimental delayed-choice entanglement swapping." *Nature Physics* 8: 480–485.** doi:10.1038/nphys2294; arXiv:1203.4834
- *Summary:* This realises Peres's gedanken experiment. Victor's choice (a Bell-state measurement vs separable measurement, made by a quantum random number generator) is made **after** Alice and Bob have already registered their photons. Whether their already-recorded data shows entangled or separable correlations depends on Victor's later choice. The authors call this "quantum steering into the past", and quote Peres: quantum effects "mimic ... influence of future actions on past events, even after these events have been irrevocably recorded."
- *Relevance:* This is the **strongest experimental "rollback-looking" case.** Note again: Alice's and Bob's individual records never change. Only the *sorting* of the joint data into subsets depends on Victor.

**Ma, X.-S., Kofler, J., & Zeilinger, A. (2016). "Delayed-choice gedanken experiments and their realizations." *Reviews of Modern Physics* 88: 015005.** doi:10.1103/RevModPhys.88.015005; arXiv:1407.2930
- *Summary:* A comprehensive review of delayed-choice experiments and what they do and do not imply.
- *Relevance:* This is the best single reference for §3.

**Cramer, J. G. (1986). "The transactional interpretation of quantum mechanics." *Reviews of Modern Physics* 58: 647–687.** doi:10.1103/RevModPhys.58.647
- *Summary:* An emitter sends a retarded "offer wave", absorbers return advanced "confirmation waves", and a completed "transaction" (a handshake across spacetime) selects the outcome.
- *Relevance:* This is the **closest interpretation to a network handshake / commit protocol**, and it even uses the word "transaction". It is time-symmetric, not rollback: nothing is revised; the transaction is atemporal.

**Aharonov, Y., Bergmann, P. G., & Lebowitz, J. L. (1964). "Time Symmetry in the Quantum Process of Measurement." *Physical Review* 134: B1410–B1416.** doi:10.1103/PhysRev.134.B1410
**Aharonov, Y., & Vaidman, L. (2001/2008). "The Two-State Vector Formalism of Quantum Mechanics: an Updated Review." arXiv:quant-ph/0105101** (published in *Time in Quantum Mechanics*, Lecture Notes in Physics 734, Springer, 2008. The book chapter metadata was not independently checked.)
- *Summary:* A system between two measurements is described by a forward-evolving state (from preparation) and a backward-evolving state (from post-selection). The ABL rule gives the probabilities of intermediate outcomes.
- *Relevance:* This is formally like "the server knows the start state and the committed end state and fills in between". It is the most mathematically precise analogue of "decide once both ends are known".

**Price, H., & Wharton, K. (2015). "Disentangling the Quantum World." *Entropy* 17(11): 7752–7767.** doi:10.3390/e17117752; arXiv:1508.01140
**Wharton, K. B., & Argaman, N. (2020). "Colloquium: Bell's theorem and locally mediated reformulations of quantum mechanics." *Reviews of Modern Physics* 92: 021002.** doi:10.1103/RevModPhys.92.021002; arXiv:1906.04313
- *Summary:* These papers argue that retrocausal ("future-input-dependent") models can explain Bell correlations with local mediation, by dropping the assumption of statistical independence. Wharton favours "all-at-once" (Lagrangian, two-time boundary) accounts.
- *Relevance:* An "all-at-once" solution is the physics analogue of a server resolving an entire time window together. This is a strong structural match, but the authors frame it as block-universe constraint satisfaction, not simulation.

**Leifer, M. S., & Pusey, M. F. (2017). "Is a time symmetric interpretation of quantum theory possible without retrocausality?" *Proceedings of the Royal Society A* 473: 20160607.** doi:10.1098/rspa.2016.0607; arXiv:1607.07871
- *Summary:* Under certain realist assumptions, time symmetry implies retrocausality.
- *Relevance:* This is a formal reason why a time-symmetric "rollback-like" model may be forced to be retrocausal rather than just a replay.

**Friederich, S., & Evans, P. W. "Retrocausality in Quantum Mechanics." *Stanford Encyclopedia of Philosophy*** (first published 2019-06-03; substantive revision 2023-11-13). https://plato.stanford.edu/entries/qm-retrocausality/
- *Summary:* An authoritative survey covering the transactional interpretation, the two-state vector formalism, Wharton's two-time boundary models, Price and Leifer–Pusey arguments, and Bell's theorem.
- *Relevance:* The standard entry point. It cites nothing about simulation or netcode.

**Lloyd, S., Maccone, L., Garcia-Patron, R., Giovannetti, V., Shikano, Y., et al. (2011). "Closed Timelike Curves via Postselection: Theory and Experimental Test of Consistency." *Physical Review Letters* 106: 040403.** doi:10.1103/PhysRevLett.106.040403; arXiv:1005.2219
- *Summary:* This models closed timelike curves (CTCs) as teleportation plus postselection. Inconsistent histories (the grandfather paradox) are removed by postselection. It is contrasted with Deutsch's (1991, *Phys. Rev. D* 44: 3197) consistency-condition CTCs.
- *Relevance:* This is a **physics formalism for "run, then discard histories that fail a consistency check"**, which is essentially rollback with rejection.

### 2.4 Many-Worlds and computational cost

**Everett, H. (1957). "'Relative State' Formulation of Quantum Mechanics." *Reviews of Modern Physics* 29: 454–462.** doi:10.1103/RevModPhys.29.454
- *Summary:* Unitary evolution without collapse. Outcomes are relative to observer states.
- *Relevance:* This is the "keep all branches" baseline.

**Deutsch, D. (1985). "Quantum theory, the Church–Turing principle and the universal quantum computer." *Proc. R. Soc. Lond. A* 400: 97–117.** doi:10.1098/rspa.1985.0070. **Deutsch, D. (1997). *The Fabric of Reality*. Allen Lane / Penguin**, p. 217 (quoted by Aaronson 2011).
- *Summary:* Deutsch introduced the universal quantum computer. In *Fabric* he argues that Shor's algorithm uses "10^500 or so times the computational resources that can be seen to be present ... where was the number factorized?" and takes this as support for MWI.
- *Relevance:* This is **prior art for framing MWI in computational-resource terms.** For a simulator, it cuts the other way: if the substrate really does that much work, the simulator is paying for it whether or not "branches" are real.

**Aaronson, S. (2011; in *Computability: Turing, Gödel, Church, and Beyond*, MIT Press 2013). "Why Philosophers Should Care About Computational Complexity." arXiv:1108.1791**, §8.1 "Quantum Computing and the Many-Worlds Interpretation."
- *Summary:* Aaronson rebuts Deutsch. BQP ≠ BPP is unproven. And even granting vast resources, "parallel universes" language misleads: Holevo's theorem limits n qubits to n retrievable bits, and quantum computers do not "try all answers in parallel" (they need interference).
- *Relevance:* This is the key counterweight to naive "MWI is expensive / collapse is cheap" reasoning (see §4).

**Aaronson, S. (2012-08-18). "Why Many-Worlds is not like Copernicanism." *Shtetl-Optimized*.** https://scottaaronson.blog/?p=1103
**Aaronson, S. (2017-03-22). "Your yearly dose of is-the-universe-a-simulation." *Shtetl-Optimized*.** https://scottaaronson.blog/?p=3208
**Aaronson, S. (2017-10-03). "Because you asked: the Simulation Hypothesis has not been falsified; remains unfalsifiable." *Shtetl-Optimized*.** https://scottaaronson.blog/?p=3482
- *Summary:* In these posts Aaronson argues:
  - Quantum computers do not vindicate MWI.
  - A bounded region of spacetime has a finite-dimensional Hilbert space (about 10^122 qubits), so it can be simulated classically in principle, though perhaps at a cost of about 2^(10^122) steps.
  - The simulation hypothesis is unfalsifiable rather than falsified. Classical-hardness results such as Ringel & Kovrizhin do not rule it out, because the simulator could be quantum or simply slow.
- *Relevance:* Aaronson's position makes the MWI-vs-collapse "cost" comparison mostly about **storage and readout**, not dynamics. It also blocks any "exponential cost therefore not a simulation" argument.

**Aaronson, S. (2005). "Quantum computing, postselection, and probabilistic polynomial-time." *Proc. R. Soc. A* 461: 3473–3482.** doi:10.1098/rspa.2005.1546; arXiv:quant-ph/0412187
- *Summary:* Proves PostBQP = PP. A quantum computer that can postselect (discard all runs in which some event did not occur) is enormously more powerful than a standard one.
- *Relevance:* This is **critical for our cost framing.** A simulator that could "roll back and re-roll until the outcome is consistent" would have postselection power. Real physics does not seem to allow this: we cannot build PP solvers. So any rollback in the physics must not be usable for postselection. This is a strong, citable constraint.

**Carroll, S. (2014-06-30). "Why the Many-Worlds Formulation of Quantum Mechanics Is Probably Correct." *Preposterous Universe* (blog).** https://www.preposterousuniverse.com/blog/2014/06/30/why-the-many-worlds-formulation-of-quantum-mechanics-is-probably-correct/
**Vaidman, L. "Many-Worlds Interpretation of Quantum Mechanics." *Stanford Encyclopedia of Philosophy*** (first published 2002-03-24; latest revision 2026-06-17), §7.1. https://plato.stanford.edu/entries/qm-manyworlds/
- *Summary:* Carroll calls the "too many universes" objection "silly": "the capacity for describing multiple universes is *automatically there*", so nothing is added to the quantum state. Vaidman discusses the Occam's-razor objection and argues that MWI is economical in *laws*.
- *Relevance:* In simulator terms, MWI costs **nothing extra per step** over plain unitary evolution. The cost lies in never being allowed to *prune* branches. This reframes our "MWI vs collapse" cost comparison: collapse is a *garbage-collection* policy, not a cheaper physics engine.

### 2.5 Superdeterminism, deterministic substrates and Bell tests

**'t Hooft, G. (2016). *The Cellular Automaton Interpretation of Quantum Mechanics*. Fundamental Theories of Physics 185, Springer.** doi:10.1007/978-3-319-41285-6; arXiv:1405.1548
- *Summary:* Quantum mechanics as an emergent description of an underlying deterministic cellular automaton. Bell's theorem is evaded by relaxing statistical independence (superdeterminism).
- *Relevance:* This is the **closest mainstream-physicist analogue of "deterministic lockstep simulation"**, the GGPO-style deterministic core. It is written as physics, not as a simulation hypothesis.

**Hossenfelder, S., & Palmer, T. N. (2020). "Rethinking Superdeterminism." *Frontiers in Physics* 8: 139.** doi:10.3389/fphy.2020.00139; arXiv:1912.06462
- *Summary:* The paper argues that superdeterminism (a violation of statistical independence) is under-explored, not conspiratorial, and potentially testable through reduced randomness in rapidly repeated measurements.
- *Relevance:* This provides a test proposal for the deterministic-substrate branch of our cost comparison.

**Bell tests:**
- Aspect, A., Grangier, P., & Roger, G. (1982). *PRL* 49: 91–94. doi:10.1103/PhysRevLett.49.91.
- Hensen, B., et al. (2015). "Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres." *Nature* 526: 682–686. doi:10.1038/nature15759; arXiv:1508.05949.
- Giustina, M., et al. (2015). *PRL* 115: 250401. doi:10.1103/PhysRevLett.115.250401.
- Shalm, L. K., et al. (2015). *PRL* 115: 250402. doi:10.1103/PhysRevLett.115.250402.
- The BIG Bell Test Collaboration (2018). "Challenging local realism with human choices." *Nature* 557: 212–216. doi:10.1038/s41586-018-0085-3; arXiv:1805.04431.
- Nobel Prize in Physics 2022: Aspect, Clauser & Zeilinger, "for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science." https://www.nobelprize.org/prizes/physics/2022/press-release/
- *Relevance:* Local hidden variables are excluded, up to the superdeterminism and "free choice" assumptions; the BIG Bell Test used about 100,000 human participants to generate setting choices. A simulator explanation must be **nonlocal, retrocausal or superdeterministic**. Campbell et al. 2017 opt for nonlocal.

**Brassard, G., Cleve, R., & Tapp, A. (1999). "The cost of exactly simulating quantum entanglement with classical communication." *PRL* 83: 1874–1877.** doi:10.1103/PhysRevLett.83.1874
**Toner, B. F., & Bacon, D. (2003). "Communication Cost of Simulating Bell Correlations." *PRL* 91: 187904.** doi:10.1103/PhysRevLett.91.187904; arXiv:quant-ph/0304076
- *Summary:* Toner & Bacon show that the singlet-state correlations for projective measurements can be simulated exactly with shared randomness **plus one bit of classical communication** per pair.
- *Relevance:* This quantifies the **"central server" cost of Bell nonlocality.** Such a server would need only a tiny amount of hidden communication per entangled pair. It must also ensure that this channel can never be used for in-world signaling (no-signaling). This is the rigorous version of Campbell et al.'s nonlocality point, and a useful number for our cost framing.

### 2.6 Wigner's friend / observer disagreement (where "whose view wins" really matters)

- Frauchiger, D., & Renner, R. (2018). "Quantum theory cannot consistently describe the use of itself." *Nature Communications* 9: 3711. doi:10.1038/s41467-018-05739-8.
- Proietti, M., et al. (2019). "Experimental test of local observer independence." *Science Advances* 5: eaaw9832. doi:10.1126/sciadv.aaw9832; arXiv:1902.05080.
- Bong, K.-W., et al. (2020). "A strong no-go theorem on the Wigner's friend paradox." *Nature Physics* 16: 1199–1205. doi:10.1038/s41567-020-0990-x; arXiv:1907.05607.
- *Relevance:* These results constrain whether observers' outcomes can be treated as absolute, observer-independent "facts". This is the physics setting closest to "the victim's perspective gets overruled". Any "authoritative server decides whose view wins" model has to confront the local-friendliness no-go theorem (Bong et al.). We found no netcode framing here.

### 2.7 Measurement reversal ("un-collapse")

- Katz, N., et al. (2008). "Reversal of the weak measurement of a quantum state in a superconducting phase qubit." *PRL* 101: 200401. doi:10.1103/PhysRevLett.101.200401; arXiv:0806.3547 (arXiv title: "Uncollapsing of a quantum state…").
- Minev, Z. K., et al. (2019). "To catch and reverse a quantum jump mid-flight." *Nature* 570: 200–204. doi:10.1038/s41586-019-1287-z; arXiv:1803.00545.
- *Relevance:* Measurements *can* be undone, but only probabilistically, and only when the information has not leaked irreversibly into the environment or been read out. This lines up with the netcode rule that **a rollback is invisible only if nothing already shown to a player changes**. It is a useful, physically grounded constraint for the analogy.

### 2.8 Popular / low-authority sources seen (not prior art for the netcode idea)

These sources discuss render-on-demand or lazy evaluation generically. None mentions rollback, lag compensation or netcode (checked by fetch where possible):
- Déglon, P., "Are We in a Simulation? 2022 Nobel Physics Says Maybe," unscarcity.ai (updated Aug 2026), https://unscarcity.ai/a/simulation-science. Says explicitly that there is no proof.
- Blackwell, G. (2025-02-27), "Time Warp: Delayed-choice quantum erasure," Substack, https://drgblackwell.substack.com/p/time-warp-delayed-choice-quantum. A wave-only reinterpretation; no simulation framing. (HN discussion: item 43194434.)
- Medium posts by "Soulthreader", V. Boellis and A. K. Sand, and a LinkedIn post by J. Bartolo, all appearing in search results. These are generic render-on-demand framings, not individually verified.

---

## 3. Established physics facts we must respect

1. **The delayed-choice quantum eraser never shows interference in the raw signal-detector data.** In Kim et al. (2000), D0's total pattern is always the no-interference sum. Interference fringes appear **only** in coincidence-sorted subsets (R01 and R02), and R01 and R02 are shifted by π relative to each other (Kim et al. derive R01 ∝ sinc²·cos² and R02 ∝ sinc²·sin²), so the two subsets add back to the featureless pattern. Sources: Kim et al. 2000; Hossenfelder, "The delayed choice quantum eraser, debunked," *Backreaction*, 2021-10-30 (http://backreaction.blogspot.com/2021/10/the-delayed-choice-quantum-eraser.html); Carroll, "The Notorious Delayed-Choice Quantum Eraser," 2019-09-21 (https://preposterousuniverse.com/blog/2019/09/21/the-notorious-delayed-choice-quantum-eraser/); Qureshi, T. (2020), "Demystifying the delayed-choice quantum eraser," *Eur. J. Phys.* 41: 055403, doi:10.1088/1361-6404/ab923e, arXiv:1908.03920; Fankhauser, J. (2019), "Taming the Delayed Choice Quantum Eraser," *Quanta* 8: 44–56, arXiv:1707.07884.
2. **No signaling, and no message to the past.** Nobody at D0 can learn the later choice from D0's data alone. The correlation becomes visible only after classical records from both sides are brought together, which is limited by light speed. The same holds for delayed-choice entanglement swapping (Ma et al. 2012): Alice's and Bob's individual records are fixed, and Victor's later choice only changes which *subset* of the joint data shows entangled correlations.
3. **Standard QM predicts all these results without retrocausality** (Carroll 2019; Ma, Kofler & Zeilinger 2016; Violaris, M., "The quantum eraser doesn't rewrite the past – it rewrites observers," *Physics World*, 2025-05-27, https://physicsworld.com/a/the-quantum-eraser-doesnt-rewrite-the-past-it-rewrites-observers/). Retrocausal readings are *interpretations* that are empirically equivalent to standard QM; the experiments do not require them.
4. **Bell violations are experimentally established** with the main loopholes closed simultaneously (Hensen et al. 2015; Giustina et al. 2015; Shalm et al. 2015; BIG Bell Test 2018; Nobel 2022). Local hidden-variable models are ruled out unless one gives up statistical independence (superdeterminism) or allows retrocausality.
5. **Entanglement does not permit faster-than-light signaling** (the no-signaling theorem). Any "server" model has to hide its nonlocal channel completely from in-world users.
6. **Classically simulating Bell correlations costs communication** (Brassard–Cleve–Tapp 1999; about one bit per singlet for projective measurements, Toner & Bacon 2003). In general, classically simulating quantum dynamics is believed to require exponential resources, but that is unproven (BPP vs BQP; Aaronson 2011).
7. **Postselection is extraordinarily powerful** (PostBQP = PP; Aaronson 2005). Physics that let an agent "re-roll until satisfied" would allow efficient solution of PP-hard problems. Nothing observed suggests this is possible.
8. **Measurement reversal is possible only before information spreads irreversibly** (Katz et al. 2008; Minev et al. 2019).

---

## 4. Strongest counterarguments found

1. **The key disanalogy: in lag compensation the victim sees the contradiction. In quantum mechanics nobody ever does.** Bernier (2001) says plainly that lag compensation produces visible "paradoxes": the victim "was shot from around the corner". Quantum experiments show the opposite. No recorded outcome (D0 hits in Kim et al.; Alice's and Bob's clicks in Ma et al.) is ever revised, and all observers' records agree whenever they are compared (Facts 1–3). So if physics does "rollback", it must be a rollback that **never overrides a rendered observation**. That is closer to Time Warp's rule that nothing before the global-virtual-time horizon is ever revised, or to deferred joint resolution (Campbell et al.), than to "favor the shooter". The favor-the-shooter framing, taken literally, predicts observable inconsistencies that we do not see. *(Our synthesis from the cited sources.)*
2. **Nothing needs explaining: standard QM already predicts the delayed-choice results** without rollback or retrocausality (Carroll 2019; Hossenfelder 2021; Qureshi 2020; Ma, Kofler & Zeilinger 2016). A rollback mechanism adds machinery without adding predictions, which is Occam's razor against it.
3. **Collapse does not save the simulator the pre-measurement cost.** To produce correct interference *before* measurement, the simulator must already evolve the full superposition. Collapse only lets it discard data afterwards. MWI adds no extra per-step dynamics; it just never prunes (Carroll 2014; Vaidman, SEP §7.1). So "MWI is expensive" is really a claim about **storage and garbage collection**, not computation. *(Our synthesis; supported by Carroll and Aaronson.)*
4. **Rollback with re-roll equals postselection, which is too powerful** (Aaronson 2005). A universe that settled outcomes by retrying until something was consistent would hand in-world agents PP-level computing power unless it was very carefully hidden.
5. **The simulation hypothesis is unfalsifiable as usually stated** (Aaronson 2017, blog p=3482; Hossenfelder, "The Simulation Hypothesis is Pseudoscience," *Backreaction*, 2021-02-13, https://backreaction.blogspot.com/2021/02/the-simulation-hypothesis-is.html). Any analogy that makes no new predictions inherits this problem.
6. **Wigner's-friend no-go theorems** (Frauchiger & Renner 2018; Bong et al. 2020) show that "absolute observed events" combined with locality and free choice conflict with quantum predictions. A single authoritative server keeping one canonical history must give up one of the other assumptions. Nonlocality is the natural choice for a server model, and Campbell et al. 2017 accept it.
7. **Claims that the universe cannot be simulated at all** (Faizal, M., Krauss, L. M., Shabir, A., & Marino, F. (2025), "Consequences of Undecidability in Physics on the Theory of Everything," *Journal of Holography Applications in Physics* 5(2): 10–21; arXiv:2507.22950) argue from Gödel-type undecidability. This result is contested; see the response "Provability vs. Execution," arXiv:2512.11807 (listed in search results, not read). **We have not evaluated either paper in depth.**
8. **Classical-hardness arguments against simulation** (Ringel, Z., & Kovrizhin, D. L. (2017), "Quantized gravitational responses, the sign problem, and quantum complexity," *Science Advances* 3: e1701758, doi:10.1126/sciadv.1701758) were widely reported as refuting the simulation hypothesis. Aaronson (2017, p=3482) explains why they do not: the simulator could be quantum, or slow, and the hardness result is limited to specific algorithms.

---

## 5. Proposed experimental tests of the simulation hypothesis (quantum-related)

- **Campbell et al. 2017.** Variants of the double-slit and delayed-choice eraser experiments. Examples: destroy the which-way records unread versus keep them; delay erasure to macroscopic time scales; and a "predicting erasure" variant to test whether the *availability of which-way data to an observer* changes the outcome. Standard QM predicts no observer-dependence beyond the physical records. We found no published results of these specific tests (see Unverified leads).
- **Beane, S. R., Davoudi, Z., & Savage, M. J. (2014). "Constraints on the Universe as a Numerical Simulation." *Eur. Phys. J. A* 50: 148.** doi:10.1140/epja/i2014-14148-0; arXiv:1210.1847. Looks for lattice artefacts, such as anisotropy in the highest-energy cosmic rays near the GZK cutoff. This is not a measurement test, but it is the standard physics template for "look for the simulator's discretisation".
- **Hossenfelder & Palmer 2020.** Test superdeterminism by looking for reduced randomness when measurements are repeated fast on small, cold systems. This bears on the deterministic-substrate (lockstep) branch of our comparison.
- **Neukart et al. 2022.** Speculative proposals about observable programmer intervention under resource exhaustion.
- **Implication for our experiment (our synthesis):** a genuine rollback model predicts **something beyond standard QM** only if the rollback buffer is finite. Either delays longer than some window would stop showing the usual correlations, or there would be resource-dependent effects. Existing delayed-choice experiments with macroscopic delays and space-like separation (Jacques et al. 2007; Ma et al. 2012; BIG Bell Test 2018) found no such cutoff. That gives a lower bound on any buffer. It does not falsify the idea.

---

## 6. Unverified leads

- **Reddit** (r/SimulationTheory, r/AskPhysics, r/gamedev, r/Physics): we could not search it (our tools' access to reddit.com is blocked). Informal "quantum = netcode / lag compensation" posts are plausible and **may pre-date us**. Before any public priority claim, search manually for: "quantum netcode", "delayed choice lag compensation", "rollback netcode quantum".
- **YouTube:** we searched titles through the web index only. Candidates not checked for netcode content include PBS Space Time's quantum-eraser episodes (e.g. "We Were WRONG About the Quantum Eraser!", https://www.youtube.com/watch?v=sc7FlWUAnzA), Tom Campbell's lecture series, and Rizwan Virk interviews. No transcripts were searched.
- **Virk (2019) full text:** we have not checked whether the book mentions multiplayer synchronisation, servers or latency. It has a chapter on quantum indeterminacy and rendering (from summaries only).
- **Campbell *My Big TOE* (2003) full text:** not read; the "rendering" claims come from secondary descriptions and Campbell et al. 2017.
- **Campbell / Center for the Unification of Science and Consciousness (CUSAC):** reports of crowdfunded double-slit / delayed-choice tests after 2017. No published results were found or verified.
- **Daubois, A.** "Quantum Entanglement Isn't Telepathy. It's Just Shared Memory." *ITNEXT* (Medium). Seen in search results, fetch returned 403. It may be a programmer's shared-memory analogy for entanglement, possibly relevant to the "server explains nonlocality" point. Content, date and whether it addresses Bell's theorem are unverified.
- **"Provability vs. Execution: A Comment on 'Consequences of Undecidability…'"**, arXiv:2512.11807. Seen in search results; authors and content not checked.
- **Wolfram, S. (2020). "A Class of Models with the Potential to Represent Fundamental Physics." *Complex Systems* 29(2): 107–536; arXiv:2004.08210** (metadata verified). Its "multiway systems / branchial space" treats quantum branching as computational branching and may be relevant to the MWI-cost section. We have not verified whether it discusses pruning, cost or rollback.
- **Hanson, R. (2001). "How To Live In A Simulation." *Journal of Evolution and Technology* 7** (https://www.jetpress.org/volume7/simulation.pdf). Verified to exist; it is about how to behave if simulated. We have not checked whether it discusses cost-saving rendering or rollback.
- **Peres, A. (2000). "Delayed choice for entanglement swapping." *J. Mod. Opt.* 47: 139–143.** Cited by Ma et al. 2012; not independently checked.
- **The HN thread "Ask HN: Quantum physics observer effect = lazy evaluation?"** (item 9809295): date and author not checked because of rate limiting.
