# Batch A: fact check and prior-art pass ("moving through the map")

*Compiled 2026-09-23 for the thought-experiment repo. Nothing here claims we live in a simulation.
Scope: ROADMAP Batch A, covering (1) FTL and causality under a global host clock, (2) warp drives in the
Episode 2 "space-lag" model, (3) wormholes and portals, and (4) gravitational-lensing time delays.*

**How citations were checked.** WebSearch was unavailable because the session budget was exhausted
(200/200, first query refused). Every entry under "Verified facts" was checked against at least one primary
record: Crossref DOI metadata (`api.crossref.org/works?query.bibliographic=…`), the OpenAlex record with its
abstract (`api.openalex.org/works/doi:…`), the arXiv abstract page (`arxiv.org/abs/…`; the arXiv *API* was
throttled), the Stanford Encyclopedia of Philosophy, or the maintainer's own page. Quoted numbers come from
the abstract text unless another location is given. **Numbers not found in a source I read are in
"Unverified leads".** Tags follow the repo convention: [PHYS] is established physics, [ANALOGY] is a
CS/engine mapping, [SPEC] is speculation, and [COUNTER] is a counterpoint.

Queries run (all recorded):
- WebSearch: `simulation hypothesis faster than light preferred frame global clock no causality paradox` (refused: budget).
- Crossref / OpenAlex / arXiv-abs: one lookup per citation below (author + title keywords).
- OpenAlex full-text search: `simulation hypothesis faster than light causality`; `simulation hypothesis preferred frame`;
  `simulated universe superluminal signalling preferred frame`; `absolute simultaneity tachyons preferred frame causal paradox`;
  `tachyons preferred frame no causal paradox`; `floating origin large virtual worlds`; `Casimir energy density negative warp drive wormhole`.
- HN Algolia (stories + comments): `simulation hypothesis faster than light preferred frame`; `simulation global clock faster than light causality`;
  `universe simulation tick FTL paradox`; `server authoritative tick faster than light relativity`; `simulation preferred frame`;
  `simulation hypothesis causality FTL`; `FTL preferred frame paradox`; `simulation hypothesis speed of light tick`;
  `simulation hypothesis relativity absolute time`; `simulation hypothesis instantaneous entanglement tick`; `warp drive floating origin`;
  `warp drive game engine`; `warp drive moves space not ship`; `Alcubierre endless runner`; `Alcubierre drive treadmill`;
  `endless runner world moves player stationary`; `floating origin Kerbal`; `wormhole Portal game non-euclidean`; `non-euclidean portals game engine`.
- Physics StackExchange API: `search/advanced` for `simulation preferred frame faster than light`, `simulated universe faster than light causality`,
  `preferred frame FTL no paradox`, `tachyon preferred frame causality paradox`, `warp drive negative energy expansion contraction`,
  `universe simulation global time`; `intitle` for `preferred frame faster than light`, `absolute simultaneity faster than light`,
  `FTL causality preferred frame`, `simulation hypothesis`, `tachyon causality`, `Alcubierre negative energy`, `preferred frame`, `tachyon`, `FTL`.

---

## A1. FTL and causality in a simulation with a global clock

**The author's claim, restated.** FTL signalling causes time-travel paradoxes only because special relativity
has no preferred frame, so "faster than light" in one frame is "backwards in time" in another, and two such
legs can close a loop. A simulation with an authoritative server tick *has* a preferred frame (host order). If
FTL messages are always delivered in host order, no loop can close. The price is that FTL would reveal the
preferred frame.

**Verdict in short:** the physics of the claim is correct and well known in the physics and philosophy
literature (Liberati–Sonego–Visser 2002; Rembieliński 1997; Babichev–Mukhanov–Vikman 2008; Hossenfelder 2015;
Bohmian mechanics' preferred foliation). **The simulation framing ("the server tick is the preferred frame")
has no formal prior statement that I could find**, though one 2023 HN comment comes close in a game-design
setting. The strongest counterpoints are experimental: no preferred frame has shown up in any Lorentz test,
and Bancal et al. (2012) show that a hidden influence of *finite* speed in a preferred frame would allow
signalling.

### Verified facts

(a) FTL + Lorentz invariance ⇒ causal loops
- [PHYS] **Benford, G. A., Book, D. L. & Newcomb, W. A. (1970), "The Tachyonic Antitelephone", *Phys. Rev. D*
  2, 263–265. doi:10.1103/PhysRevD.2.263.** Abstract: "The problem of detecting faster-than-light particles is
  reconsidered in relation to Tolman's paradox. It is shown that some of the experiments … must either yield
  negative results or give rise to causal contradictions." (OpenAlex abstract.)
- [PHYS] **Tolman's paradox.** The Benford et al. abstract names it. Wikipedia's "Tachyonic antitelephone" (read
  2026-09-23) attributes the thought experiment to Einstein (1907), Einstein & Sommerfeld (1910, "to telegraph
  into the past") and R. C. Tolman (1917), *The Theory of the Relativity of Motion* (University of California
  Press). The book's existence is confirmed by a 1919 review in *Science* 49, 148 (doi:10.1126/science.49.1258.148-a).
  The exact Tolman page is **not** verified.
- [PHYS] **The loop needs two FTL legs in different frames.** A single warp drive has no closed timelike curves
  (CTCs), but two can create them, because the laws are Lorentz invariant. This is Everett, A. E. (1996),
  "Warp drive and causality", *Phys. Rev. D* 53, 7365–7368, doi:10.1103/PhysRevD.53.7365 (metadata verified;
  content as summarised in the Physics SE answers under Q705208). The wormhole version is Morris, Thorne &
  Yurtsever (1988), "Wormholes, Time Machines, and the Weak Energy Condition", *PRL* 61, 1446–1449,
  doi:10.1103/PhysRevLett.61.1446. Abstract: a maintainable wormhole "can be converted into a time machine with
  which causality might be violatable." See also Hawking (1992), "Chronology protection conjecture", *PRD*
  46, 603–611, doi:10.1103/PhysRevD.46.603.

(b) Preferred-frame / neo-Lorentzian readings where FTL is paradox-free
- [PHYS] **Liberati, S., Sonego, S. & Visser, M. (2002), "Faster-than-c Signals, Special Relativity, and
  Causality", *Annals of Physics* 298, 167–185. doi:10.1006/aphy.2002.6233; arXiv:gr-qc/0107091.** (The published
  title says "Faster-than-c", not "Faster-than-light".) Abstract: "special relativity can easily accommodate —
  indeed, does not exclude — faster-than-c signalling at the kinematical level … it is impossible to make
  statements of general validity [about causality] without specifying at least some features of the tachyonic
  propagation." For the Scharnhorst effect (faster-than-c photons between Casimir plates), "the faster-than-c
  aspects are 'benign' and … do not automatically lead to causality violations." **This is the closest
  physics analogue of the author's argument.** The Casimir plates supply the preferred frame, as the host
  tick would.
- [PHYS] **Rembieliński, J. (1997), "Tachyons and Preferred Frames", *Int. J. Mod. Phys. A* 12, 1677–1709.
  doi:10.1142/S0217751X97001122.** (Metadata verified; abstract not read, so the content description is from memory.) A tachyon theory built on a
  preferred frame and absolute synchronization.
- [PHYS] **Babichev, E., Mukhanov, V. & Vikman, A. (2008), "k-Essence, superluminal propagation, causality and
  emergent geometry", *JHEP* 2008(02), 101. doi:10.1088/1126-6708/2008/02/101; arXiv:0708.0561.** Abstract: "in
  spite of the superluminal propagation the causal paradoxes do not arise in these theories and in this respect
  they are not less safe than General Relativity." Here the background field defines the preferred frame.
- [PHYS] **Hossenfelder, S. (2015), "Does faster-than-light travel lead to a grandfather paradox?"**, blog
  *Backreaction*, <https://backreaction.blogspot.com/2015/06/does-faster-than-light-travel-lead-to.html>.
  Quote: "superluminal travel in and by itself is not inconsistent … What leads to causal paradoxa is allowing
  travel against the arrow of time." She names the frame used to fix "forward in time" as "a preferred frame".
  Physics SE Q638012 (2021) discusses her follow-up video. The top answer argues it "can never work" without
  breaking the principle of relativity; the second answer restates her position as CMB-frame FTL with "only
  apparent" paradoxes.
- [PHYS] **Bohmian mechanics needs a preferred foliation.** Dürr, D., Goldstein, S., Norsen, T., Struyve, W. &
  Zanghì, N. (2014), "Can Bohmian mechanics be made relativistic?", *Proc. R. Soc. A* 470, 20130699,
  doi:10.1098/rspa.2013.0699; arXiv:1307.1714. Abstract: "In relativistic space-time, Bohmian theories can be
  formulated by introducing a privileged foliation of space-time." They propose deriving the foliation
  covariantly from the wave function. SEP, "Bohmian Mechanics" (Goldstein; first published 2001-10-26, revised
  2025-09-20), describes a foliation "along which nonlocal effects are transmitted".
- [PHYS] **Hardy, L. (1992), "Quantum mechanics, local realistic theories, and Lorentz-invariant realistic
  theories", *PRL* 68, 2981–2984. doi:10.1103/PhysRevLett.68.2981.** If "elements of reality" of
  Lorentz-invariant observables are themselves Lorentz invariant, this contradicts QM. In other words, realistic
  theories push toward a preferred frame.
- [PHYS] **Maudlin, T., *Quantum Non-Locality and Relativity*** (Wiley-Blackwell). Editions verified on Crossref:
  2002, doi:10.1002/9780470752166, and 3rd ed. 2011, doi:10.1002/9781444396973. The book-length treatment of
  whether Bell nonlocality needs a preferred frame. (The first edition was 1994; see Unverified leads.)
- [PHYS] **Peacock, K. A. (2014), "Would Superluminal Influences Violate the Principle of Relativity?",
  *Lato Sensu* 1(1). doi:10.20416/lsrsps.v1i1.33.** Argues that superluminal influences need not imply a
  distinguished frame or detectable absolute motion. **This is a counterpoint to the author's "the cost is
  revealing the frame".**
- [PHYS] **Craig, W. L. & Smith, Q. (eds.) (2007/2008), *Einstein, Relativity and Absolute Simultaneity*,
  Routledge. doi:10.4324/9780203700051** (metadata only). The philosophers' neo-Lorentzian case.

(c) Experimental bounds on a preferred frame
- [PHYS] **SME data tables.** Kostelecký, V. A. & Russell, N., "Data Tables for Lorentz and CPT Violation",
  *Rev. Mod. Phys.* 83, 11 (2011), doi:10.1103/RevModPhys.83.11. arXiv:0801.0287 is updated every year and was
  at v19 when checked.
- [PHYS] **Modern Michelson–Morley.** Nagel, M. et al. (2015), "Direct terrestrial test of Lorentz symmetry in
  electrodynamics to 10⁻¹⁸", *Nat. Commun.* 6, 8174, doi:10.1038/ncomms9174. Abstract: orientation-dependent
  Δν/ν = **9.2 ± 10.7 × 10⁻¹⁹** (95% CI), "finding no significant violations of Lorentz symmetry". The earlier
  result is Herrmann, S. et al. (2009), "Rotating optical cavity experiment testing Lorentz invariance at the
  10⁻¹⁷ level", *PRD* 80, 105011, doi:10.1103/PhysRevD.80.105011, and before that Herrmann et al. (2005), *PRL*
  95, 150401, doi:10.1103/PhysRevLett.95.150401.
- [PHYS] **Preferred-frame effects in gravity.** Shao, L. & Wex, N. (2012), *CQG* 29, 215018,
  doi:10.1088/0264-9381/29/21/215018. They test PPN α₁, α₂ with pulsar–white-dwarf binaries "by assuming the
  isotropic cosmic microwave background to single out a preferred frame". Their α̂₂ limit is "three orders of
  magnitude weaker than the best Solar system limit". The review is Will, C. M. (2014), *Living Rev. Relativ.*
  17, 4, doi:10.12942/lrr-2014-4 (see Unverified leads for the numbers).
- [PHYS] **The CMB rest frame is the natural candidate.** Planck 2013 XXVII, "Doppler boosting of the CMB:
  Eppur si muove", *A&A* 571, A27 (2014), doi:10.1051/0004-6361/201321556. Abstract: accepted dipole
  "v/c = 1.23 × 10⁻³, or v = 369 km s⁻¹"; aberration measured independently as 384 ± 78 (stat) ± 115 (syst)
  km/s toward (l,b) = (264°, 48°). Planck 2018 I gives 369.82 ± 0.11 km/s (cross-checked in
  `batch-BCD-prior-art.md`).
- [PHYS] **Lattice simulations would show up as anisotropy.** Beane, S. R., Davoudi, Z. & Savage, M. J.
  (2014), "Constraints on the universe as a numerical simulation", *EPJ A* 50, 148,
  doi:10.1140/epja/i2014-14148-0; arXiv:1210.1847. Abstract: inverse lattice spacing "b⁻¹ ≳ 10¹¹ GeV" from the
  cosmic-ray cutoff; a lattice could show up as "rotational symmetry breaking" in the highest-energy cosmic rays.
- [PHYS] **Discreteness does not require a preferred frame.** Bombelli, L., Henson, J. & Sorkin, R. D. (2009),
  "Discreteness without symmetry breaking: a theorem", *Mod. Phys. Lett. A* 24, 2579–2587,
  doi:10.1142/S0217732309031958 (causal sets; metadata verified).

(d) "Speed of spooky action" in a preferred frame
- [PHYS] **Salart, D., Baas, A., Branciard, C., Gisin, N. & Zbinden, H. (2008), "Testing the speed of 'spooky
  action at a distance'", *Nature* 454, 861–864. doi:10.1038/nature07121; arXiv:0808.3316.** The test ran for
  24 hours over 18 km on an east–west baseline, using Earth's rotation to scan all candidate frames: "if such a
  privileged reference frame exists and is such that the Earth's speed in this frame is less than 10⁻³ that of
  the speed of light, then the speed of this spooky influence would have to exceed that of light by at least 4
  orders of magnitude." **Note:** the Sun's CMB speed (1.23 × 10⁻³ c) is just *above* that 10⁻³ condition.
- [PHYS] **Scarani, V., Tittel, W., Zbinden, H. & Gisin, N. (2000), "The speed of quantum information and the
  preferred frame: analysis of experimental data", *Phys. Lett. A* 276, 1–7. doi:10.1016/S0375-9601(00)00609-5;
  arXiv:quant-ph/0007008.** This is the CMB-frame analysis: "lower bound for the speed of quantum information in
  this frame at 1.5 × 10⁴ c."
- [PHYS] **Yin, J. et al. (2013), *PRL* 110, 260407. doi:10.1103/PhysRevLett.110.260407; arXiv:1303.0614.**
  **Watch the title:** the published title is "Lower Bound on the Speed of Nonlocal Correlations without
  Locality and Measurement Choice Loopholes". "Bounding the speed of 'spooky action at a distance'" is the arXiv
  title. From a 12-hour continuous Bell violation, the bound is "4 orders of magnitude of the speed of light if
  Earth's speed in any inertial reference frame was less than 10⁻³ times the speed of light."
- [PHYS] **Bancal, J.-D., Pironio, S., Acín, A., Liang, Y.-C., Scarani, V. & Gisin, N. (2012), "Quantum
  non-locality based on finite-speed causal influences leads to superluminal signalling", *Nature Physics* 8,
  867–870. doi:10.1038/nphys2460; arXiv:1110.3795.** "for any finite speed v with c < v < ∞, such models predict
  correlations that can be exploited for faster-than-light communication … we exclude any possible explanation
  of quantum correlations in terms of influences propagating at any finite speed." (The argument is multipartite.)

(e) Engine / CS side
- [ANALOGY] **Authoritative server.** Gambetta, G., "Client-Server Game Architecture",
  <https://www.gabrielgambetta.com/client-server-game-architecture.html> (read 2026-09-23): "the one and only
  authority regarding everything that happens in the world is the server."
- [ANALOGY] **Logical clocks.** Lamport, L. (1978), "Time, clocks, and the ordering of events in a distributed
  system", *CACM* 21(7), 558–565, doi:10.1145/359545.359563.
- [PHYS/ANALOGY] **Update order can be hidden from the inside.** Gorard, J. (2020), "Some Relativistic and
  Gravitational Properties of the Wolfram Model", *Complex Systems* 29(2), 599–654,
  doi:10.25088/complexsystems.29.2.599; arXiv:2004.14810. Abstract: "causal invariance (namely, the requirement
  that all causal graphs be isomorphic, irrespective of the choice of hypergraph updating order) is equivalent to
  a discrete version of general covariance … This fact then allows one to deduce a discrete analog of Lorentz
  covariance." Also Wolfram, S. (2020), *Complex Systems* 29(2), 107–536, doi:10.25088/complexsystems.29.2.107.

### Prior art for the simulation framing
- **Physics claim ("a preferred frame removes FTL paradoxes"): ANTICIPATED.** See Liberati–Sonego–Visser 2002,
  Rembieliński 1997, Babichev et al. 2008, Hossenfelder 2015 and the Bohmian foliation papers. The author should
  cite these and not present the point as new.
- **Simulation framing ("the server tick *is* that preferred frame, so FTL is delivered in host order"):
  OVERLAPPING / NONE FORMAL.** The closest item is HN comment 37128472 (user *javajosh*, 2023-08-15) on
  designing a relativistic space game: "Nothing stops us from arbitrarily designating a particular reference
  frame as 'preferred' in a simulation; SR merely says that such a choice is truly arbitrary." That comment is
  about game bookkeeping, not about FTL paradoxes. HN comment 13344682 (2017) connects the Bohmian preferred
  foliation and simulation talk only in passing. No paper found in OpenAlex, HN or Physics SE argues "simulation
  hypothesis ⇒ global tick ⇒ FTL without paradox ⇒ FTL would expose the host frame." The nearest formal work
  goes the *opposite* way: Beane et al. 2014 (a lattice sim would show preferred directions) and Gorard 2020
  (update order can be made unobservable).
- Physics SE Q721557 ("Can the cosmic speed limit be used to disprove the simulation hypothesis?", 2022) is
  about light-speed latency and has no preferred-frame content.

### Strongest counterpoints
- [COUNTER] **No preferred frame is seen.** Lorentz tests reach ~10⁻¹⁸ in the photon sector (Nagel 2015),
  and the SME tables list null results across sectors. A host frame that FTL could reveal must be invisible to
  everything else we have measured.
- [COUNTER] **Bancal et al. 2012.** If entanglement were carried by a *finite-speed* message in the host frame,
  it would already allow signalling. A global tick escapes this only if nonlocal updates finish *within one
  tick* (effectively v = ∞ in host time). That is a real constraint on the engine design, and it's the useful
  link back to Experiment 001.
- [COUNTER] **Hiding the frame versus using it.** Quantum nonlocality in Bohmian or GRW-flash form can use a
  preferred foliation while no-signalling hides it completely. A usable FTL *channel* would make it visible.
  The author's "cost" is right, but it means the engine currently shows no evidence of such a channel.
- [COUNTER] **Peacock 2014** disputes that superluminal influences must reveal a distinguished frame at all.
- [COUNTER] **Relativity of simultaneity is still observed.** With FTL in host order, a moving observer would
  see some FTL messages "arrive before they are sent" in their own frame, even though no loop exists. That is
  apparent retro-causation, which the first Physics SE answer to Q638012 treats as a principle-of-relativity
  violation. It's a feature of the prediction, not a paradox, but it has to be stated.
- [COUNTER] **Causal invariance (Gorard 2020).** An engine can have a global update order that is
  *unobservable* inside. So "a simulation has a preferred frame" doesn't follow automatically. It holds only if
  the engine lets physics depend on the order.

### Unverified leads
- Einstein 1907 (*Jahrbuch der Radioaktivität und Elektronik* 4, 411–462) as the first FTL-paradox argument.
  Only a secondary source (Wikipedia) was read.
- Tolman (1917) page numbers for the paradox.
- Yin et al. 2013's specific bound "1.38 × 10⁴ c". Only the abstract's "4 orders of magnitude" was confirmed.
- Maudlin's first edition (Blackwell, 1994).
- PPN preferred-frame bounds (α₁ ≈ 10⁻⁵, α₂ ≈ 10⁻⁹): the values were not read in Will 2014.
- J. S. Bell's remark in Davies & Brown, *The Ghost in the Atom* (CUP, 1986) that the "cheapest" resolution of
  nonlocality is a return to a Lorentzian preferred frame. The book's existence is confirmed by reviews (*Am. J.
  Phys.* 55, 957, doi:10.1119/1.14920; *Isis* 80, 339), but the quote was not read. Bell, "How to teach special
  relativity" (1976; reprinted in World Scientific collections, doi:10.1142/9789812386540_0009) is the
  Lorentzian-pedagogy source (metadata only).
- Valentini, A. (2002), "Signal-locality in hidden-variables theories", *Phys. Lett. A* 297, 273–278,
  doi:10.1016/S0375-9601(02)00438-3 (metadata only). This is quantum non-equilibrium, where the preferred frame
  *becomes* usable. A candidate "how the host frame could leak" source.
- Valve's Yahn Bernier (2001), "Latency Compensating Methods in Client/Server In-game Protocol Design and
  Optimization" (the Valve developer wiki page was behind a bot check).

---

## A2. Warp drives in the "space-lag" model

**The proposed reading, restated.** Alcubierre contracts space ahead and expands it behind. In tile terms
that means deleting tiles ahead and inserting them behind. Under Episode 2's 1:1 rule (a region that has *more*
space also ticks *slower*), removing space needs a region "cheaper than empty space" (ticking faster than
vacuum). That amounts to negative energy density, which matches GR's requirement.

**Verdict in short:** half right. It's right that warp drives need negative energy (or at least violate the
energy conditions) in GR, and the "negative mass ⇒ faster ticks *and* less space" reading is the correct sign
in the static weak-field (γ = 1) regime. But three facts undercut the tile story as stated: (i) Alcubierre's
metric has **no time dilation** (lapse = 1), so its bubble involves no "lag" at all; (ii) Natário (2002) built a
warp drive with **zero expansion**, so "delete ahead, insert behind" is not what makes a warp drive work; and
(iii) the negative energy in Alcubierre sits in a **ring around the bubble wall, perpendicular to the motion**,
not in the contracting region ahead (see the equation note below).

### Verified facts
- [PHYS] **Alcubierre, M. (1994), "The warp drive: hyper-fast travel within general relativity", *Class.
  Quantum Grav.* 11(5), L73–L77. doi:10.1088/0264-9381/11/5/001.** Confirmed: volume 11, page L73. Abstract: "By
  a purely local expansion of spacetime behind the spaceship and an opposite contraction in front of it, motion
  faster than the speed of light as seen by observers outside the disturbed region is possible … exotic matter
  will be needed."
- [PHYS] **Pfenning, M. J. & Ford, L. H. (1997), "The unphysical nature of 'warp drive'", *CQG* 14,
  1743–1751. doi:10.1088/0264-9381/14/7/011.** Quantum-inequality limits give a "bubble wall thickness … on the
  order of only a few hundred Planck lengths", and "the total integrated energy density needed … is physically
  unattainable." The quantum inequalities themselves are Ford, L. H. & Roman, T. A. (1995), *PRD* 51,
  4277–4286, doi:10.1103/PhysRevD.51.4277.
- [PHYS] **Everett, A. E. & Roman, T. A. (1997), "Superluminal subway: The Krasnikov tube", *PRD* 56,
  2100–2108. doi:10.1103/PhysRevD.56.2100** (metadata verified). The Krasnikov-tube alternative also needs
  large negative energy.
- [PHYS] **The horizon / steering problem.** Krasnikov, S. V. (1998), "Hyperfast travel in general relativity",
  *PRD* 57, 4760–4766, doi:10.1103/PhysRevD.57.4760 (metadata verified).
- [PHYS] **Semiclassical instability.** Finazzi, S., Liberati, S. & Barceló, C. (2009), "Semiclassical
  instability of dynamical warp drives", *PRD* 79, 124017, doi:10.1103/PhysRevD.79.124017 (metadata verified).
- [PHYS] **Lowering the energy.** Van Den Broeck, C. (1999), "A 'warp drive' with more reasonable total energy
  requirements", *CQG* 16, 3973, doi:10.1088/0264-9381/16/12/314. Abstract: "total negative mass needed is of
  the order of a few solar masses."
- [PHYS] **Zero-expansion warp drive.** Natário, J. (2002), "Warp drive with zero expansion", *CQG* 19,
  1157–1165, doi:10.1088/0264-9381/19/6/308. Abstract: "It is commonly believed that Alcubierre's warp drive
  works by contracting space in front … We show that this contraction/expansion is but a marginal consequence of
  the choice made by Alcubierre and explicitly construct a similar spacetime where no contraction/expansion
  occurs." **This is the key counterpoint to the tile-insertion picture.**
- **The 2021 "positive-energy warp" claims and their status:**
  - Lentz, E. W. (2021), "Breaking the warp barrier: hyper-fast solitons in Einstein–Maxwell-plasma theory",
    *CQG* 38, 075015, doi:10.1088/1361-6382/abe692. Claims solitons "sourced by purely positive energy densities".
  - Fell, S. D. B. & Heisenberg, L. (2021), "Positive energy warp drive from hidden geometric structures", *CQG*
    38, 155020, doi:10.1088/1361-6382/ac0e47. Claims "positive semi-definite energy"; example energy "four
    orders of magnitude smaller than the solar mass".
  - Bobrick, A. & Martire, G. (2021), "Introducing physical warp drives", *CQG* 38, 105009,
    doi:10.1088/1361-6382/abdf6e. Their *positive-energy* solutions are **subluminal**; superluminal ones still
    need exotic matter but can "satisfy quantum inequalities". "Any warp drive requires propulsion." Note: they
    "introduce a warp drive spacetime in which space capacity and the rate of time can be chosen in a controlled
    manner". **That is directly relevant to the author's lag + space model.** Follow-up: Fuchs, J., Helmerich, C.,
    Bobrick, A., Sellers, L. et al. (2024), "Constant velocity physical warp drive solution", *CQG* 41, 095013,
    doi:10.1088/1361-6382/ad26aa (metadata verified; subluminal per its title and the Bobrick lineage).
  - **Rebuttal:** Santiago, J., Schuster, S. & Visser, M. (2022), "Generic warp drives violate the null energy
    condition", *PRD* 105, 064038, doi:10.1103/PhysRevD.105.064038. The positive-energy claims check only
    Eulerian observers, but "the WEC requires all timelike observers to see positive energy density … all
    physically reasonable warp drives will certainly violate the WEC … Under plausible subsidiary conditions the
    null energy condition is also violated." **Status: the consensus position is that superluminal warp needs
    energy-condition violation. The positive-energy results cover either Eulerian observers only or subluminal
    cases.**
- [PHYS] **Casimir effect.** Lamoreaux, S. K. (1997), "Demonstration of the Casimir Force in the 0.6 to 6 μm
  Range", *PRL* 78, 5–8, doi:10.1103/PhysRevLett.78.5. Abstract: the effect was "conclusively demonstrated …
  Agreement with theory at the level of 5%." The review is Lamoreaux (2005), *Rep. Prog. Phys.* 68, 201–236,
  doi:10.1088/0034-4885/68/1/R04. For negative energy density in QFT and the energy conditions, see Kontou,
  E.-A. & Sanders, K. (2020), "Energy conditions in general relativity and quantum field theory", *CQG* 37,
  193001, doi:10.1088/1361-6382/ab8fcf. Note: Lamoreaux measured the **force**. That the energy density between
  the plates is negative relative to the vacuum is the standard theory behind it, not the measured quantity.
- [ANALOGY] **Floating origin / world-scrolling.** Thorne, C. (2005), "Using a floating origin to improve
  fidelity and performance of large, distributed virtual worlds", *Proc. Int. Conf. on Cyberworlds (CW'05)*,
  doi:10.1109/CW.2005.94. (Crossref lists the author as "C. Thome", probably an OCR error for Thorne.) Abstract:
  the method "floats the world's origin with the viewpoint", so the viewpoint moves without its coordinates
  changing.

**Equation note (from memory, flagged for verification):** Alcubierre's line element is
ds² = −dt² + (dx − v_s f(r_s) dt)² + dy² + dz². The lapse is 1, so a clock inside the bubble keeps coordinate
time. The Eulerian energy density is ∝ −v_s² (y² + z²)/r_s² · (df/dr_s)², which is negative and concentrated in
a torus around the wall. The volume expansion is θ ∝ v_s (x_s/r_s)(df/dr_s): positive behind, negative ahead.
So the negative energy and the "tile deletion" sit in *different places*.

### Prior art for the simulation / game framing
- **"Warp = moving the map, not the player": NONE FOUND in formal literature.** HN has many comments with
  the lay version, "the warp drive moves space, not the ship" (e.g. 14764552, 2017; 17430626, 2018). None ties
  it to floating origin, endless runners or world-scrolling. Queries: `Alcubierre endless runner`,
  `Alcubierre drive treadmill`, `endless runner world moves player stationary` and `warp drive floating origin`
  all returned 0 relevant hits.
- **Kerbal Space Program's floating origin ("Krakensbane").** HN comment 26938812 (2021) says KSP moves "the
  entire universe" whenever the craft gets more than 2 km from the origin, to defeat the floating-point
  "Deep-Space Kraken". This is secondary; the KSP wiki page did not load (see Unverified leads).
- **"1:1 lag/space rule ⇒ negative energy ⇒ faster ticks": NONE FOUND** as a simulation argument. The physics
  sign is standard: in linearised GR, negative mass flips the potential. Bobrick & Martire's controllable
  "space capacity and the rate of time" is the nearest formal neighbour.

### Strongest counterpoints
- [COUNTER] **Alcubierre has no lag.** Lapse = 1 means the space-lag model's "time half" is absent. The warp
  lives entirely in the shift vector (a frame-dragging "flow"), which the Episode 2 static model doesn't
  represent. The 1:1 rule is a static, weak-field (PPN γ = 1) statement and doesn't govern warp metrics.
- [COUNTER] **Natário 2002.** Warp drives exist with zero expansion, so "delete tiles ahead, insert behind" is
  a feature of one gauge choice and not the mechanism.
- [COUNTER] **Where the negative energy sits.** In Alcubierre it's a ring around the wall, not the contracting
  region ahead (equation note above). "Cheaper-than-vacuum tiles where space is removed" is therefore not
  literally GR's picture.
- [COUNTER] **Quantum inequalities (Pfenning & Ford 1997; Ford & Roman 1995).** Even with Casimir-type
  negative energy, its magnitude × duration × extent is tightly limited, which makes warp walls
  Planck-thin and the total energy unattainable.
- [COUNTER] **Horizon problem (Krasnikov 1998).** A crew inside a superluminal bubble can't signal the front of
  the wall, so they can't create or steer the bubble. In tile terms, the engine would have to edit tiles ahead
  of any signal the ship can send. Is that allowed? It's the same question as A1.
- [COUNTER] **Warp ⇒ CTCs (Everett 1996).** Two warp drives make a time machine in a Lorentz-invariant world.
  The A1 argument (a host tick prevents loops) applies here too, and it predicts that warp drives would pick
  out the host frame.

### Unverified leads
- Pfenning & Ford's commonly quoted "energy ≈ 10 orders of magnitude more than the mass of the visible
  universe". Not in the abstract; read the paper before quoting.
- The Alcubierre equation forms and locations above (from memory; check eqs. in the 1994 paper).
- Casimir, H. B. G. (1948), "On the attraction between two perfectly conducting plates", *Proc. K. Ned. Akad.
  Wet.* 51, 793–795. There's no DOI; the record was not found in Crossref/OpenAlex.
- The Casimir energy density formula ρ = −π²ħc/(720 a⁴): standard, but not read in a source this pass.
- KSP's "Krakensbane" floating origin and 2 km threshold: secondary (HN) only.
- Lentz 2023 MG16 proceedings, "Hyper-fast positive energy warp drives", doi:10.1142/9789811269776_0061
  (metadata only). Any direct Lentz reply to Santiago–Schuster–Visser was not found.

---

## A3. Wormholes and portals

### Verified facts
- [PHYS] **Einstein, A. & Rosen, N. (1935), "The Particle Problem in the General Theory of Relativity", *Phys.
  Rev.* 48, 73–77. doi:10.1103/PhysRev.48.73.**
- [PHYS] **Morris, M. S. & Thorne, K. S. (1988), "Wormholes in spacetime and their use for interstellar travel:
  A tool for teaching general relativity", *Am. J. Phys.* 56, 395–412. doi:10.1119/1.15620.** Abstract: the
  throat material must have a radial tension exceeding its mass-energy density (τ₀ > ρ₀c²). "No known material
  has this … property, and such material would violate all the 'energy conditions'," though "quantum field
  theory gives tantalizing hints that such material might, in fact, be possible." The throat must have "no
  horizon".
- [PHYS] **Morris, Thorne & Yurtsever (1988), *PRL* 61, 1446** (see A1): a traversable wormhole can be made
  into a time machine.
- [PHYS] **ER = EPR.** Maldacena, J. & Susskind, L. (2013), "Cool horizons for entangled black holes",
  *Fortschr. Phys.* 61, 781–811, doi:10.1002/prop.201300020. Abstract: two-sided black holes joined by an
  Einstein–Rosen bridge "can be interpreted as maximally entangled states of two black holes … We suggest that
  similar bridges might be present for more general entangled states."
- [ANALOGY] ***Portal*** **is a 2007 video game** (Wikipedia infobox, read 2026-09-23; its development section
  lists the precursor *Narbacular Drop*). HN comments (e.g. 42662525, 2025; 18811499, 2019) note
  that **portal rendering** is an old engine technique (the Unreal engine, *Prey*) and that "non-Euclidean"
  levels are built from portals (e.g. 34241634 on *The Stanley Parable*).

### Prior art for the simulation framing
- **"Wormhole = extra edge in the level graph / portal": OVERLAPPING (informal only).** HN comments treat
  game portals as non-Euclidean level geometry but don't tie them to Morris–Thorne or to exotic matter. No
  formal source was found. Physics SE Q128075 ("How would wormhole-based FTL violate causality?") covers the
  physics side.
- **ER = EPR as a link to Experiment 001:** it's the authors' own idea (Maldacena–Susskind); no
  simulation-framed version was found.

### Strongest counterpoints
- [COUNTER] **An extra graph edge is free in code but costs exotic matter in GR** (Morris–Thorne τ₀ > ρ₀c²). A
  portal model that doesn't charge a negative-energy "price" for the edge isn't modelling GR wormholes.
- [COUNTER] **ER = EPR bridges are not traversable** (standard reading; see Unverified leads). They can't carry
  signals, which matches no-signalling in Experiment 001 but means they aren't "portals".
- [COUNTER] **Wormholes plus relative motion make time machines** (Morris–Thorne–Yurtsever 1988), unless
  chronology protection holds (Hawking 1992). This is the same issue as A1: the host tick would forbid it, and
  forbidding it would reveal the frame.

### Unverified leads
- Traversable-wormhole follow-ups: Gao–Jafferis–Wall (2017) and the 2022 *Nature* "wormhole on a quantum
  processor" experiment (Jafferis et al.) and its critiques. Not checked in this pass.
- *Antichamber* (2013) release date and developer: not checked.

---

## A4. Gravitational lensing time delays

### Verified facts
- [PHYS] **Refsdal, S. (1964), "On the Possibility of Determining Hubble's Parameter and the Masses of Galaxies
  from the Gravitational Lens Effect", *MNRAS* 128, 307–310. doi:10.1093/mnras/128.4.307.** Abstract: for a
  supernova behind a galaxy, the path difference "Δt … can amount to a couple of months or more, and may be
  measurable"; H₀ and the lens mass follow from Δt, the redshifts, the image luminosities and the separation.
- [PHYS] **The first lensed quasar.** Walsh, D., Carswell, R. F. & Weymann, R. J. (1979), "0957 + 561 A, B:
  twin quasistellar objects or gravitational lens?", *Nature* 279, 381–384, doi:10.1038/279381a0.
- [PHYS] **Its time delay.** Kundić, T. et al. (1997), *ApJ* 482, 75–82, doi:10.1086/304147. Best-fit delay
  **417 ± 3 days** (95% CI). The "long delay" near 540 days was rejected. H₀ = 64 ± 13 km/s/Mpc (95%, Ω = 1).
- [PHYS] **SN Refsdal.** Kelly, P. L. et al. (2015), "Multiple images of a highly magnified supernova formed by
  an early-type cluster galaxy lens", *Science* 347, 1123–1126, doi:10.1126/science.aaa3350. Four images in an
  Einstein cross around a z = 0.54 cluster galaxy in MACS J1149.6+2223; the host is at z = 1.49.
  - Kelly, P. L. et al. (2016), "Déjà vu all over again: the reappearance of supernova Refsdal", *ApJL* 819, L8,
    doi:10.3847/2041-8205/819/1/L8. First images seen 2014 Nov 10; the predicted new image found 2015 Dec 11,
    "the first time the appearance of a SN at a particular time and location in the sky was successfully
    predicted in advance".
  - Kelly, P. L. et al. (2023), "Constraints on the Hubble constant from supernova Refsdal's reappearance",
    *Science* 380, eabh1322, doi:10.1126/science.abh1322. Blinded result: **H₀ = 64.8 (+4.4/−4.3)** with eight
    models, and **66.6 (+4.1/−3.3) km/s/Mpc** with the two best models.
- [PHYS] **H0LiCOW / TDCOSMO (lensed quasars).**
  - Wong, K. C. et al. (2020), "H0LiCOW – XIII. A 2.4 per cent measurement of H0 from lensed quasars: 5.3σ
    tension between early- and late-Universe probes", *MNRAS* 498, 1420–1439, doi:10.1093/mnras/stz3094:
    **H₀ = 73.3 (+1.7/−1.8)** from six lenses, flat ΛCDM.
  - Birrer, S. et al. (2020), "TDCOSMO IV: Hierarchical time-delay cosmography …", *A&A* 643, A165,
    doi:10.1051/0004-6361/202038861. With the mass-sheet degeneracy kept free: **74.5 (+5.6/−6.1)**
    (TDCOSMO only) and **67.4 (+4.1/−3.2)** (TDCOSMO + SLACS).
  - TDCOSMO Collaboration (Birrer et al.) (2025), "TDCOSMO 2025: Cosmological constraints from strong lensing
    time delays", *A&A* 704, A63, doi:10.1051/0004-6361/202555801. Eight lensed quasars plus Pantheon+ Ωm,
    flat ΛCDM: **H₀ = 71.6 (+3.9/−3.3)**, with ~4.6% precision once the SLACS and SL2S samples are added.

### Prior art for the simulation framing
- The ROADMAP model ("ray-marching through slow + extra-space tiles gives images and delays") is an [ANALOGY]
  for the standard Fermat-potential picture. The lens time delay is geometric path difference plus
  Shapiro-type delay, which Refsdal 1964 already frames as path lengths. **No simulation-framed prior art
  searched specifically** (low novelty stakes: this item is a demonstration, not a claim).

### Strongest counterpoints
- [COUNTER] Time-delay H₀ depends on the lens mass model. The **mass-sheet degeneracy** moves H₀ by several
  km/s/Mpc (TDCOSMO IV: 74.5 → 67.4 depending on the prior). A tile engine that reproduces delays for a
  *given* mass model tests the engine rule, not H₀.
- [COUNTER] Episode 2's 1:1 rule is exactly what makes lensing and Shapiro delays come out right (γ = 1). So
  the lensing demo can't *distinguish* the engine from GR. It can only fail to match it.

### Unverified leads
- SN H0pe (JWST, 2023–2025) lensed-supernova H₀: no Crossref record found. Only a *Physics Today* news item
  (doi:10.1063/pt.6.1.20230524a) turned up, and it may be about SN Refsdal instead; not read.
- Liu & Oguri (2025), *PRD* 111, 123506 (doi:10.1103/v857-ylw5), and *PRD* 112 (doi:10.1103/6gfm-11rr): SN
  Refsdal H₀ re-analyses (metadata only).
