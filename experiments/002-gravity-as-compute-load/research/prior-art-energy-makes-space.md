# Experiment 002: "Energy makes space". Prior-art check

*Compiled 2026-09-23. This is a literature check for a thought experiment. It does not claim the universe is a simulation.
It is a companion to [`prior-art.md`](prior-art.md), which already covers Alagoz, Whitworth, Wolfram, Verlinde (2011),
Einstein 1911, the Cassini γ bound, Berger–Oliger AMR and parallel discrete-event simulation. Those sources are
cross-referenced here, not repeated.*

**Claims under review** (from [`energy-makes-space.md`](energy-makes-space.md)):

1. **Energy makes space.** Mass-energy adds proper volume ("extra space") to a region.
2. **The exchange rate.** Light bending and Shapiro delay get half their size from slowed time and half from
   stretched space (γ = 1), so γ reads as the ratio of "space stretch" to "time lag".
3. **The tick is a sync signal that has to cross the region.** More space means more cells to cross, so the tick is
   slower by exactly the same factor. Lag equals space (a = b) by construction, and local c is invariant because clocks
   and rulers are built from the same cells.
4. **Engine versions.** A simulated universe allocates more cells near mass (like adaptive mesh refinement), and the
   speed of light is the engine's CFL / cell-per-tick limit.

**Verification policy.** Every entry in §2 was checked against the primary text (full text where marked "read"),
arXiv, Crossref or OpenAlex metadata. Anything I could not check to that standard is in §4.

---

## 1. Summary verdict

| # | Claim | Verdict | Closest prior art |
|---|---|---|---|
| 1 | Energy adds proper space (excess radius) | **Anticipated. This is textbook GR.** | Feynman Vol. II §42–3 (Eq. 42.3). Feynman even writes the rule as "G/3c⁴ times the total energy content". |
| 1b | Gravity framed as space being *created* by energy | **Overlapping, opposite sign in the best-known models.** | Cahill's process physics and the Hamilton–Lisle river model have space flowing *into* matter ("matter acts as a sink for space, and never as a source"). Padmanabhan has space *emerging*, but cosmologically, not near mass. |
| 2 | Half from time, half from space; γ as "space per unit of time effect" | **Anticipated. This is standard pedagogy.** | Will (Living Rev. Relativ. 2014): the "1/2" part comes from the equivalence principle and the "γ/2" part from space curvature. Will's PPN table defines γ as "How much space-curvature produced by unit rest mass?". Okun (2000): Einstein 1911 "implicitly assum[ed] g_rr = 1" and so lost the factor 2. Ellingson (AJP 1987) is a paper titled after the space-curvature half. |
| 3a | One underlying quantity sets both clock rate and ruler length, so the ratio is fixed and local c is invariant | **Anticipated in physics (not in compute language).** | Wilson (1921) → Dicke (1957) → Puthoff (2002) polarizable-vacuum model: a single parameter K slows clocks and shrinks rods by the same factor. The measured c is renormalized to c, and the full 1.75″ bending follows. Feynman's hot-plate bug (§42–1, §42–6) makes the "you can't see it from inside because your rulers are made of the same stuff" point. |
| 3b | Time dilation *derived from* a synchronization signal that must cross the region's cells | **Overlapping; no indexed source found for this exact rule.** | Feynman §42–6 derives gravitational clock rates from light flashes crossing a rocket (a Doppler argument, not a latency one). Sano (2026 preprint) gets gravitational time dilation from a synchronization mechanism, a different one (phase-layer coupling, not signal crossing time). Causal sets (proper time = longest chain) and Chandy–Misra PDES (in `prior-art.md`) are structural cousins. |
| 4a | Speed of light = the engine's cell-per-tick / CFL limit | **Anticipated informally.** | Conway's Life "speed of light" c = one cell per generation (Poundstone 1985, via LifeWiki). A Hacker News comment (2013) explicitly maps von Neumann/CFL stability to the speed of light "unless the Universe is trying to minimize resource usage". |
| 4b | The engine allocates more cells near mass (AMR ↔ gravity) | **No indexed prior art found.** | Nearest: discrete quantum walks that reproduce Dirac fermions in curved spacetime by varying the walk's local coefficients (Di Molfetta et al. 2013). `prior-art.md` §6.4 already notes that real AMR runs refined regions with *more* substeps, not slower simulated time. |

**Bottom line.** The *physics* in claims 1 and 2 is textbook, and the "one knob controls both clocks and rulers, so
a = b" idea (3a) has a century-old physics precedent in the polarizable-vacuum line (Wilson → Dicke → Puthoff). What I
could not find in any indexed source is the specific **computational mechanism** (3b + 4b): a tick defined as a sync
signal crossing a variable number of cells, used to explain *why* γ = 1. Any public write-up should present Feynman,
Will and Puthoff/Dicke as the established background, and claim at most that the *engine rule* is a new framing of it.

Two corrections to feed back into `energy-makes-space.md`:
- Feynman's excess radius comes from the mass **inside** the sphere. Outside matter the *average* (Ricci) curvature is
  zero, so "extra space" lives where the energy is. The field around a mass is carried by the other curvature components.
  Feynman says this explicitly in §42–3.
- Direction of prior "flowing space" models: Cahill and the river model make matter a **sink** of space, not a source.
  "Energy makes space" runs the other way, so cite them as contrast, not support.

---

## 2. Annotated bibliography

### 2.1 Claim 1: energy adds space

**Feynman, R. P., Leighton, R. B. & Sands, M. (1964).** *The Feynman Lectures on Physics, Vol. II*, Ch. 42 "Curved
Space", §42–3 "Our space is curved". Online edition: https://www.feynmanlectures.caltech.edu/II_42.html (read in full
through a reader proxy, since the site returned 403 to direct fetches).
Eq. (42.3): "Radius excess = r_meas − √(A/4π) = (G/3c²)·M", stated for a sphere small enough that the density inside is
effectively constant. "The constant G/3c² is about 2.5×10⁻²⁹ cm per gram … the earth has 1.5 millimeters more radius
than it should have for its surface area." Footnote 4 adds "Approximately, because the density is not independent of
radius." Also, "the sun's radius is one-half a kilometer too long." In §42–9: "everybody … will, when he draws a sphere,
find that the excess radius is G/3c² times the total mass (or, better, G/3c⁴ times the total energy content) inside the
sphere." In §42–3: "the law says that the *average* curvature *above* the surface area of the earth is zero."
*Relevance:* **Chapter, formula and Earth figure are all verified.** This is the canonical "energy makes space" statement,
already phrased in terms of energy. The project's summary ("about GM/3c² for a uniform ball … roughly 1.5 mm for the
Earth") is accurate.

**Baez, J. C. & Bunn, E. F. (2005).** *The Meaning of Einstein's Equation.* American Journal of Physics 73(7),
644–652. DOI: 10.1119/1.1852541. arXiv:gr-qc/0103044 (read).
The paper puts Einstein's equation in plain English: a small ball of freely falling test particles, initially at rest,
begins to shrink at a rate proportional to its volume times energy density plus the three pressures. It derives Newton's
law from this.
*Relevance:* A pedagogical, energy-first statement of how energy changes volume. Note the framing is about the
**shrinking of a free-falling ball** (a spacetime, second-time-derivative statement). It is not about static extra
radius, so it complements Feynman and does not duplicate him.

**Cahill, R. T. (2002).** *Process Physics: Inertia, Gravity and the Quantum.* General Relativity and Gravitation 34,
1637–1656. DOI: 10.1023/A:1020120223326. arXiv:gr-qc/0110117 (read).
Space is an emergent, growing "process-space" of "gebits". Matter regions "act as net sinks for gebits … the space
effectively moves towards the matter: matter acts as a sink for space, and never as a source. Such a process would clearly
correspond to gravity." A later review is Cahill (2015), *Process Physics: Emergent Unified Dynamical 3-Space, Quantum
and Gravity: a Review*, Physics International 6, 51–67, DOI 10.3844/pisp.2015.51.67 (abstract read).
*Relevance:* The best-known "space flowing" model, and the **opposite sign** to "energy makes space". Cahill's broader
program (a preferred-frame "dynamical 3-space" with a measured absolute velocity) is outside mainstream physics. Cite it
only as contrast.

**Hamilton, A. J. S. & Lisle, J. P. (2008).** *The river model of black holes.* American Journal of Physics 76,
519–532. DOI: 10.1119/1.2830526 (abstract read).
"Space flows like a river through a flat background … the river of space falls into the black hole at the Newtonian
escape velocity, hitting the speed of light at the horizon."
*Relevance:* The mainstream, exact-GR version of "space flows into mass" (Gullstrand–Painlevé coordinates). Like
Cahill, it runs inward. It is a coordinate picture, not a claim that space is created or destroyed.

**Padmanabhan, T. (2012).** *Emergence and Expansion of Cosmic Space as due to the Quest for Holographic
Equipartition.* arXiv:1206.4916 (abstract read; OpenAlex lists it as an arXiv record, and I did not confirm a journal
version).
Cosmic expansion is recast as the *emergence* of space, dV/dt ∝ (N_sur − N_bulk).
*Relevance:* The closest mainstream "space generation" language, but it describes cosmological expansion, not extra
space near a mass.

**Van Raamsdonk, M. (2010).** *Building up spacetime with quantum entanglement.* General Relativity and Gravitation
42(10), 2323–2329. DOI: 10.1007/s10714-010-1034-0. (Also the Int. J. Mod. Phys. D 19, 2429–2435 essay, DOI
10.1142/S0218271810018529.) Metadata verified through Crossref, and the IJMPD abstract read.
*Relevance:* "Emergent space from entanglement". Connectivity of space comes from entanglement, not from energy density.
This is a different mechanism, and I list it only because the brief asked.

**Jacobson, T. (2016).** *Entanglement Equilibrium and the Einstein Equation.* Physical Review Letters 116, 201101.
DOI: 10.1103/PhysRevLett.116.201101 (abstract read).
The Einstein equation follows from maximizing entanglement entropy in small geodesic balls *at fixed volume*.
*Relevance:* A modern derivation in which the volume of small balls, and how matter perturbs geometry at fixed volume,
is central. It is adjacent to "energy changes the amount of space", but is framed as entropy, not creation.

**Verlinde, E. (2017).** *Emergent Gravity and the Dark Universe.* SciPost Physics 2, 016. DOI:
10.21468/SciPostPhys.2.3.016 (metadata verified). Verlinde (2011) is already in `prior-art.md` §2.3.
*Relevance:* Emergent-space program. It has no excess-radius or γ-split content that I checked.

### 2.2 Claim 2: the half/half split and γ as the "exchange rate"

**Will, C. M. (2014).** *The Confrontation between General Relativity and Experiment.* Living Reviews in Relativity 17,
4. DOI: 10.12942/lrr-2014-4. arXiv:1403.7377 (read).
§4.1.1: "the classic derivations of the deflection of light that use only the corpuscular theory of light (Cavendish
1784, von Soldner 1803), or the principle of equivalence (Einstein 1911), yield only the '1/2' part of the coefficient …
because of space curvature around the Sun, determined by the PPN parameter γ, local straight lines are bent relative to
asymptotic straight lines far from the Sun by just enough to yield the remaining factor 'γ/2'. The first factor '1/2'
holds in any metric theory, the second 'γ/2' varies from theory to theory." Shapiro delay is written as
δt ≈ ½(1+γ)[240 − 20 ln(d²/r)] µs. Cassini gives γ − 1 = (2.1 ± 2.3)×10⁻⁵. Table 2 glosses γ as **"How much
space-curvature produced by unit rest mass?"**
*Relevance:* **Directly anticipates the exchange-rate framing.** The half/half split is textbook. γ is *defined* as the
space-curvature coefficient, with the time part normalized to 1 by the Newtonian limit, so "b/a = γ" is the standard PPN
reading. Will's warning ("calculations that purport to derive the full deflection using the equivalence principle alone
are incorrect") is worth quoting.

**Okun, L. B. (2000).** *Photons and static gravity.* Modern Physics Letters A 15, 1941. arXiv:hep-ph/0010120 (read).
It derives the radar echo and light deflection from the coordinate velocity v = c(g₀₀/g_rr)^{1/2} = c(1 − r_g/r).
"Note that in 1911 by implicitly assuming that g_rr = 1 and, hence, using v = c(1 − r_g/2r) Einstein derived an
expression for the angle in which coefficient 2 was missing." It also says "the velocity of light in a locally inertial
reference frame is always equal to c."
*Relevance:* An explicit, short, citable statement that g₀₀ (time) and g_rr (space) each contribute half the coordinate
slowdown of light.

**Ellingson, J. G. (1987).** *The deflection of light by the Sun due to three-space curvature.* American Journal of
Physics 55(8), 759–760. DOI: 10.1119/1.15016.
*Relevance:* A pedagogical note devoted to the space-curvature half of the deflection. **Only the metadata was verified.**
I could not read the text, so do not quote its contents.

**Einstein (1911), Will (2015, CQG 32, 124001) and Evans, Nandi & Islam (1996)** are already in `prior-art.md` §2.4 and
§6.3. They cover the 0.83″/0.875″ half value and the refractive index n ≈ 1 + 2GM/rc², which has equal time and space
shares.

### 2.3 Claim 3: one quantity sets both clocks and rulers; ticks from signals

**Puthoff, H. E. (2002).** *Polarizable-Vacuum (PV) Approach to General Relativity.* Foundations of Physics 32,
927–943. DOI: 10.1023/A:1016011413407. arXiv:gr-qc/9909037 (read).
A single scalar, the vacuum "dielectric constant" K, sets the speed of light (c/K), clock rates (ticks lengthen with K,
Eq. 11) and rod lengths (atomic sizes shrink with K, Eq. 13; "there is no such thing as a perfectly rigid rod"). Measured
with the local, distorted rods and clocks, "the measured velocity of light … renormalizes from its 'true' value c/K to
the value c." With K = exp(2GM/rc²) it gets 1.75″ light deflection. Puthoff describes it as a heuristic teaching tool
that matches GR "to appropriate order".
*Relevance:* **The closest physics precedent for claim 3.** It uses the same logic as "lag and space are the same thing
measured two ways": one underlying quantity drives both, the ratio is fixed, the full deflection comes out, and local c
stays invariant because the measuring instruments are made of the same stuff. The project's engine rule is essentially a
computational reading of this model. Caveat: the PV model is not a full replacement for GR, so do not cite it as one.

**Dicke, R. H. (1957).** *Gravitation without a Principle of Equivalence.* Reviews of Modern Physics 29, 363–376. DOI:
10.1103/RevModPhys.29.363 (metadata verified; content known through Puthoff 2002's description).
**Wilson, H. A. (1921).** *An Electromagnetic Theory of Gravitation.* Physical Review 17, 54–59. DOI:
10.1103/PhysRev.17.54 (metadata verified).
*Relevance:* The origins of the variable-refractive-index / polarizable-vacuum picture. Credit them as the roots of 3a.
I did not read either original.

**Feynman Lectures Vol. II, Ch. 42 (as above), §42–1 and §42–6.**
§42–1's "hot plate" bug: rulers expand with temperature, so "the bug and any rulers he uses are all made of the same
material" and the bug infers curvature without ever seeing his rulers change. §42–6 connects this to clocks: "we have the
analog for clocks of the hot ruler … Heartbeats go faster, all processes run faster." It derives the clock-rate
difference in an accelerating rocket from light flashes sent between clocks at the head and tail.
*Relevance:* Anticipates the "invisible from inside because clocks and rulers are made of the same cells" corollary. The
flash argument is a *signal-based* derivation of gravitational clock rates, but it is Doppler-based, not a
crossing-latency mechanism.

**Sano, R. (2026).** *Time and Gravity from a Layered Phase Substrate: A Constructive Mechanism for Emergent Time and
Gravitational Time Dilation.* Research Square preprint, 4 May 2026. DOI: 10.21203/rs.3.rs-9529894/v1 (abstract read;
not peer-reviewed).
Time is identified with a macroscopic synchronized phase of N coupled phase-field layers. A non-uniform substrate near a
mass gives "a position-dependent tick rate that recovers weak-field general relativity" in a limit, and the paper includes
a 2-D simulation.
*Relevance:* **The nearest recent work to "tick = synchronization".** It is also a simulated, sync-based origin of
gravitational time dilation. It differs in mechanism (phase-coupling, not crossing latency) and, from the abstract, does
not address spatial stretch or γ.

**Bombelli, L., Lee, J., Meyer, D. & Sorkin, R. D. (1987).** *Space-time as a causal set.* Physical Review Letters 59,
521–524. DOI: 10.1103/PhysRevLett.59.521.
**Brightwell, G. & Gregory, R. (1991).** *Structure of random discrete spacetime.* Physical Review Letters 66,
260–263. DOI: 10.1103/PhysRevLett.66.260 (abstract read: builds a metric from the causal order alone).
*Relevance:* In causal-set theory, time and distance come from counting causal links. This is structurally close to "time
is how many signal hops fit". (The "proper time ∝ longest chain" result is widely attributed to this line of work. I
verified only the abstract, which says a metric is constructed from causal structure, so treat the exact statement as
unverified; see §4.)

**Lamport, L. (1978).** *Time, clocks, and the ordering of events in a distributed system.* Communications of the ACM
21(7), 558–565. DOI: 10.1145/359545.359563.
**Friedman, E. G. (2001).** *Clock distribution networks in synchronous digital integrated circuits.* Proceedings of the
IEEE 89(5), 665–692. DOI: 10.1109/5.929649.
*Relevance:* The computing analogues named in the brief: logical clocks advanced by messages (Lamport), and on-chip
clock-distribution trees whose delay and skew grow with the distance the clock has to travel (Friedman). Metadata
verified. These are analogies only, with no gravity claim. (Chandy–Misra and Fujimoto PDES are in `prior-art.md` §6.2.)

**Wolfram Physics Project and Gorard (2020)** are in `prior-art.md` §2.2. In that framework, time dilation comes from
causal-graph foliations, and Wolfram ties energy to *more* update activity. It does not use a sync-crossing mechanism.

### 2.4 Claim 4: CFL and speed of light; AMR and gravity

**Poundstone, W. (1985).** *The Recursive Universe.* p. 79, as quoted on LifeWiki, "Speed" (https://conwaylife.com/wiki/Speed_of_light,
read through a reader proxy).
"At very most, a pattern can grow one pixel per generation in any direction. This is the maximum speed at which any form
of information can be transmitted across the Life plane. It is the counterpart of the speed of light in the real world
and is often called by that name."
*Relevance:* The "c = one cell per tick" identification is decades old in cellular-automaton culture. The quote is
verified only through LifeWiki, not from the book itself.

**Hacker News comment by "slacka" (21 Aug 2013; reposted 16 Feb 2014).** https://news.ycombinator.com/item?id=6250144 and
https://news.ycombinator.com/item?id=7247099 (read through the Algolia API).
"In computer simulations, the criteria to achieve von Neumann stabilitiy is that no effect can propagate at a speed faster
than the size step divided by the time step. Interactions in our universe are also limited by the speed of light. … None
of this makes sense unless the Universe is trying to minimize resource usage."
*Relevance:* **Informal prior art for 4a.** A simulation-hypothesis reading of the CFL/von Neumann limit as c. Related
comments are "humanarity" (1 May 2015, item 9469362: "SOL limits rate of information propagation … computation limits of
the Universe computer") and "szvsw" (2 Oct 2024, item 41725592, which explicitly cites the "CFL condition" as the
numerical-methods analogue of the speed of light).

**Di Molfetta, G., Brachet, M. & Debbasch, F. (2013).** *Quantum walks as massless Dirac fermions in curved space-time.*
Physical Review A 88, 042301. DOI: 10.1103/PhysRevA.88.042301 (abstract read).
Space- and time-dependent discrete quantum walks whose continuum limit is a Dirac fermion "in an arbitrary gravitational
field", including a Schwarzschild example simulated numerically.
*Relevance:* The closest *technical* realization of "a lattice engine whose local update rule encodes curved spacetime".
Curvature is put in through position-dependent walk coefficients, not by adding cells (no AMR), so it does not anticipate
4b.

**Berger & Oliger (1984) and Berger & Colella (1989)** are in `prior-art.md` §6.4. No source I found uses AMR as a
*model of* gravity.

---

## 3. Searches run (2026-09-23)

**WebSearch** was unavailable: the first call returned "this session has used its web search budget (200 of 200)". Every
search below therefore went directly to APIs.

- **Feynman primary text:** direct WebFetch and curl of feynmanlectures.caltech.edu/II_42.html returned 403 (Cloudflare).
  The Wayback Machine has no snapshot. It was retrieved through the r.jina.ai reader proxy and searched for "excess radius",
  "G/3c", "1.5 millimeters" and the footnotes.
- **arXiv API** (export.arxiv.org): `all:"light deflection" AND all:"factor of two"`;
  `ti:deflection AND ti:light AND abs:"spatial curvature"`; `abs:"Shapiro delay" AND abs:"spatial curvature"`;
  `ti:"photons and static gravity"`; `abs:"excess radius"`; `abs:"simulation hypothesis" AND abs:gravity` (twice, both
  empty); `abs:"adaptive mesh" AND abs:"simulation hypothesis"` (empty); `abs:"light clock" AND abs:gravitational AND
  abs:"time dilation"`; `abs:"cellular automat*" AND abs:"time dilation"` (empty);
  `abs:simulation AND abs:universe AND abs:"speed of light" AND abs:computation`; `abs:"simulated universe"`; ID lookups
  for gr-qc/0103044, 1403.7377, hep-ph/0010120, gr-qc/0110117, gr-qc/9909037 and physics/9902044. For a period the API was
  rate-limited and returned nothing. The Cahill, Padmanabhan, Van Raamsdonk, Jacobson and Verlinde queries that hit that
  window were re-run through OpenAlex and Crossref.
- **Crossref:** "light deflection factor of two space curvature time dilation American Journal of Physics"; "bending of
  light half from time half from space pedagogical"; "Shapiro time delay contribution spatial curvature gravitational time
  dilation equal"; "excess radius curvature matter Feynman"; "Cahill process physics self-referential information gravity";
  "Cahill dynamical 3-space gravitational wave flow"; "Cahill Gravity as quantum foam in-flow"; Friedman clock
  distribution; Lamport 1978; Bombelli et al. 1987; Brightwell & Gregory 1991; Di Molfetta et al. 2013; Hamilton & Lisle
  2008; Dicke 1957; Puthoff 2002; Wilson 1921; Verlinde 2017; Lock & Fuentes 2019; plus DOI lookups for every §2 entry.
- **OpenAlex:** "deflection of light by the Sun due to three-space curvature"; "Time and Gravity from a Layered Phase
  Substrate"; "gravitational time dilation from signal propagation delay synchronization light clock derivation"; "light
  clock gravitational time dilation derivation"; "Cahill process physics gravity flowing space"; "Emergence and expansion of
  cosmic space holographic equipartition"; "Building up spacetime with quantum entanglement"; "Entanglement equilibrium and
  the Einstein equation"; "simulation hypothesis gravity adaptive mesh refinement"; "speed of light Courant-Friedrichs-Lewy
  condition universe computation"; "cellular automaton gravitational time dilation variable update rate"; "time dilation
  emergent from synchronization latency discrete spacetime"; "matter creates space gravity emergent space generation".
- **Semantic Scholar:** "Cahill process physics dynamical 3-space gravity flow" (HTTP 429, rate-limited, no results).
- **Hacker News (Algolia):** "speed of light CFL condition simulation"; "speed of light Courant condition universe
  simulation" (0); "gravity adaptive mesh refinement simulation universe" (0); "time dilation clock synchronization signal
  simulation gravity" (0); "mass creates more space simulation"; "speed of light is the simulation's tick rate cell per
  tick" (0); "speed of light processing speed simulation hypothesis"; "gravity higher resolution near mass simulation" (0);
  "mesh refinement gravity time dilation" (0); "time dilation level of detail simulation gravity"; "CFL condition speed of
  light"; "Courant number speed of light universe".
- **LifeWiki** "Speed of light" (403 direct; read through the reader proxy).

**Coverage gaps.** There was no general web search, so there was no Reddit, YouTube, Medium or Stack Exchange coverage.
Textbooks (Hartle, Schutz, MTW) could not be text-searched. Absence of AMR-as-gravity (4b) and sync-crossing (3b) sources
therefore means "none found in arXiv, Crossref, OpenAlex or HN", not "none exist".

---

## 4. Unverified leads

- **Hartle, *Gravity* (2003); Schutz, *A First Course in General Relativity* / *Gravity from the Ground Up*; Misner,
  Thorne & Wheeler, *Gravitation* (1973).** All very likely discuss the factor of 2 in light deflection as time plus space
  contributions, but I could not access their text to confirm a passage or page. Do not cite without checking.
- **Eddington, *Space, Time and Gravitation* (1920)**, which gives an early "equivalent refractive medium" account of light
  bending. Not checked.
- **Causal sets: "proper time = length of the longest chain".** This is commonly attributed to Bombelli et al. (1987),
  Brightwell & Gregory (1991) and related work. Only the abstracts were read, and they do not state it verbatim.
- **Tkemaladze, J. (2025–2026), "Ze" framework** (e.g., *Direct Derivation of Time Dilation from Ze Counters*, Longevity
  Horizon, DOI 10.65649/zbv88741; *A Direct Ze-Type Experiment*, DOI 10.65649/d5yt8606). OpenAlex abstracts say "proper
  time is … a count of effective information updates". The venue is unusual for physics, and the papers are unreviewed by
  me. If they are cited, it would only be as further informal prior art for "time = update count".
- **Byrne, M. (1999), *The Cause of Gravity*, arXiv:physics/9902044.** It quotes "Einstein's formulas for excess radius
  Re = GM/3C²" in a non-mainstream unification argument. It confirms that the formula circulates, but it is not a source to
  cite.
- **Lock, M. P. E. & Fuentes, I. (2019), *Quantum and classical effects in a light-clock falling in Schwarzschild
  geometry*, CQG 36, 175007 (DOI 10.1088/1361-6382/ab32b1)**, and Bravo, Rätzel & Fuentes (arXiv:2204.07869). These
  analyze light clocks in Schwarzschild. Only metadata was checked. They may contain the cleanest "light-clock tick =
  round-trip over proper length" statement for claim 3.
- **Informal simulation-hypothesis content** (Reddit, YouTube, Medium) saying "c is the simulation's processing speed" or
  "mass gets more resolution". It is very likely to exist given the HN hits, but was not searchable this session.
