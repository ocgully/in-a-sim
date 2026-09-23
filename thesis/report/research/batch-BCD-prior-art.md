# Batches B, C, D: fact check and prior-art pass

*Compiled 2026-09-23 for the thought-experiment repo. Nothing here claims we live in a simulation.
Scope: ROADMAP Batch B ("by what clock?"), Batch C (entropy × collapse, absolute zero, the Planck scale)
and a new item D1 (quarks and subatomic particles).*

**How citations were checked.** WebSearch was unavailable because the session budget was exhausted
(200/200). Every entry below was checked against at least one primary record: Crossref DOI metadata, the
OpenAlex or Semantic Scholar record, the arXiv abstract page, PubMed, or the publisher's or maintainer's page.
Where we quote a number we read it in the source text (arXiv PDF or abstract), and we give the location.
Numbers we worked out ourselves are marked **(our arithmetic)**, with their inputs. Anything we could not
confirm is listed under **Unverified leads**. Tags follow the repo convention: [PHYS] is established physics,
[ANALOGY] is a CS/engine mapping, and [SPEC] is speculation.

---

## B1. "By what clock is the universe 13.8 billion years old?"

### Verified facts

- [PHYS] **Cosmic time is the proper time of comoving ("fundamental") observers.** In the FLRW models,
  spacetime is a stack of spatial slices Σ(t) "labeled by values of the cosmic time t". The worldlines of
  fundamental observers, "defined as at rest with respect to matter, are orthogonal to these surfaces, and the
  cosmic time corresponds to the proper time measured by the fundamental observers."
  Smeenk, C. & Ellis, G., "Philosophy of Cosmology", *Stanford Encyclopedia of Philosophy*, first published
  2017-09-26. <https://plato.stanford.edu/entries/cosmology/>
- [PHYS] **The age is 13.787 ± 0.020 Gyr for Planck + lensing + BAO.** Planck Collaboration (Aghanim et al.)
  2020, "Planck 2018 results. VI. Cosmological parameters", *A&A* 641, A6. doi:10.1051/0004-6361/201833910
  (arXiv:1807.06209). Table 2, row "Age [Gyr]", has three data combinations:
  TT,TE,EE+lowE gives **13.800 ± 0.024**, adding lensing gives **13.797 ± 0.023**, and adding BAO as well
  gives **13.787 ± 0.020** (68% intervals). The same 13.787 ± 0.020 appears in "Planck 2018 results. I"
  (arXiv:1807.06205, *A&A* 641, A1). The age is a **model-dependent inference** that assumes base ΛCDM. The
  number is not measured directly. Quote it as "13.787 ± 0.020 Gyr (Planck 2018, ΛCDM, CMB + BAO)".
- [PHYS] **Our speed relative to the CMB.** Planck 2018 I (arXiv:1807.06205, §on the dipole) gives the
  Sun–CMB velocity as β = (1.23357 ± 0.00036) × 10⁻³, "or v = (369.82 ± 0.11) km s⁻¹". The same section gives
  the Local Group's speed as about 620 ± 15 km s⁻¹. So "~370 km/s" is correct for the **Sun** (Earth's orbital
  motion adds or subtracts up to about 30 km/s over a year).
- **Why our clock ≈ cosmic time (our arithmetic).** Special-relativistic lag: γ − 1 ≈ β²/2 = **7.6 × 10⁻⁷**.
  Gravitational terms: the Sun's potential at 1 AU gives GM☉/(r c²) = **9.9 × 10⁻⁹**, and Earth's surface
  potential gives **7.0 × 10⁻¹⁰**. So a clock on Earth ticks slower than a comoving clock at the same place by
  roughly one part in a million. Illustration only: if the whole 13.787 Gyr had been spent at 370 km/s,
  the lag would be about **10,500 years**, less than 0.0001% of the age. (The Milky Way's own potential well
  is probably of order 10⁻⁶ as well, but we have not verified a source for it. See Unverified leads.)
- [PHYS] **Cosmological time dilation is observed.**
  - **Goldhaber et al. 2001**, "Timescale Stretch Parameterization of Type Ia Supernova B-Band Light Curves",
    *ApJ* 558, 359–368. doi:10.1086/322460 (arXiv:astro-ph/0104382). Light-curve widths are fitted with a
    time-axis factor w ≡ s(1 + z), and the (1+z) stretch is found in the data.
  - **Blondin et al. 2008**, "Time Dilation in Type Ia Supernova Spectra at High Redshift", *ApJ* 682,
    724–736 (arXiv:0804.3595). Spectral ageing of 13 high-z SNe Ia gives "an apparent aging rate consistent
    with the 1/(1+z) factor". It is "unambiguously excluding models that predict no time dilation, such as
    Zwicky's 'tired light' hypothesis". (DOI not retrieved from Crossref, which was rate-limited. Metadata
    comes from the arXiv journal-ref.)
  - **Lewis & Brewer 2023**, "Detection of the cosmological time dilation of high-redshift quasars",
    *Nature Astronomy* 7, 1265–1269. doi:10.1038/s41550-023-02029-2 (arXiv:2306.04053). The sample is 190
    quasars over about two decades, covering "z ∼ 0.2 → 4.0". Fitting (1+z)ⁿ gives
    **n = 1.28 (+0.28/−0.29)**, "consistent with the expected cosmological expansion of space".
  - **Wording check on "~5× slower".** The phrase **does not appear in the paper** (we searched the arXiv full
    text). It comes from press coverage. Space.com (2023-07-06, "quasar-clocks-universe-time-dilation") says:
    "time in these quasars appears to run five times slower than it does for us". It follows from
    1 + z ≈ 5 at the sample's upper end, z ≈ 4 (our arithmetic). Safe wording: "at redshift ~4, quasar
    variability appears stretched about five-fold, as (1+z) predicts".

### Prior art for the simulation framing ("global tick counter vs each region's local clock")

- **Overlapping (serious literature): Wolfram 2020**, "A Class of Models with the Potential to Represent
  Fundamental Physics", *Complex Systems* 29(2), 107–536. doi:10.25088/complexsystems.29.2.107
  (arXiv:2004.08210). Here, "each choice of how to assign updates to steps in effect defines a foliation", and
  relativistic **time dilation** is presented as the "effect of different foliations of the causal graph"
  (full text, §on causal foliations and §relativity). This is close to the repo's framing, with one key
  difference. Wolfram explicitly has **no privileged global step**: any causal foliation is valid. The repo's
  "server frame counter" would be one chosen foliation, the comoving one.
- **Overlapping (informal):** Hacker News comments frame time dilation as simulation lag. Item 36579194
  (2023-07-03) talks of "instance-shard transition due to cell crossing (special relativity) or inter-node lag
  due to spatial density (general relativity)". Item 30875229 (2022-04-01) lists "gravitational time
  dilation" as one of the universe's "optimizations". Neither mentions cosmic time or the comoving frame.
- **Not found:** anyone pairing **cosmic time (comoving proper time)** specifically with a simulation's
  global tick. OpenAlex `"simulation hypothesis" AND ("cosmic time" OR "cosmological time")` returned **0**
  records.

### Counterpoints

- [PHYS] Cosmic time is a **chosen slicing**, not an observable global clock. It exists because the FLRW
  symmetry picks out the comoving observers, and real, lumpy regions only approximate it. A server tick
  would be a *hidden* preferred frame. No experiment has found one (Lorentz invariance; see C3).
- The (1+z) stretch is fully predicted by expansion. A "network lag" story has to reproduce exactly (1+z)
  (Blondin: the exponent is consistent with 1; Lewis & Brewer: n = 1.28 +0.28/−0.29) and has to exclude
  tired light, as the data do.

---

## C1. Entropy × collapse: does collapse pay Landauer's cost?

### Verified facts

- [PHYS] **Landauer 1961**, "Irreversibility and Heat Generation in the Computing Process", *IBM J. Res.
  Dev.* 5, 183–191. doi:10.1147/rd.53.0183.
- [PHYS] **Bérut, Arakelyan, Petrosyan, Ciliberto, Dillenschneider & Lutz 2012**, "Experimental verification
  of Landauer's principle linking information and thermodynamics", *Nature* 483, 187–189.
  doi:10.1038/nature10872 (PMID 22398556). A colloidal particle in a modulated double well. "The mean
  dissipated heat saturates at the Landauer bound in the limit of long erasure cycles."
- [PHYS] **Jun, Gavrilov & Bechhoefer 2014**, "High-Precision Test of Landauer's Principle in a Feedback
  Trap", *PRL* 113, 190601. doi:10.1103/PhysRevLett.113.190601 (arXiv:1408.5089). Reducing the number of
  macroscopic states by a factor of 2 "requires work of at least kT ln2". Control manipulations that don't
  reduce the number of states "can be done reversibly". In individual cycles the work can dip below the
  bound, consistent with the Jarzynski equality.
- [PHYS] **Bennett 1973**, "Logical Reversibility of Computation", *IBM J. Res. Dev.* 17, 525–532.
  doi:10.1147/rd.176.0525. **Bennett 1982**, "The thermodynamics of computation—a review", *Int. J. Theor.
  Phys.* 21, 905–940. doi:10.1007/BF02084158. **Bennett 2003**, "Notes on Landauer's principle, reversible
  computation, and Maxwell's Demon", *Stud. Hist. Phil. Mod. Phys.* 34, 501–510.
  doi:10.1016/S1355-2198(03)00039-X. (Metadata verified. The widely known thesis is that *copying and measurement* can be
  done reversibly and only *erasure* must dissipate. We verified the metadata, not specific page quotes.)
- [PHYS] **Sagawa & Ueda 2009**, "Minimal Energy Cost for Thermodynamic Information Processing: Measurement
  and Information Erasure", *PRL* 102, 250602. doi:10.1103/PhysRevLett.102.250602 (arXiv:0809.4098). They
  derive lower bounds on the energy cost of measurement and of erasure separately. The erasure bound
  "validates Landauer's principle for a symmetric memory; for other cases, the bound indicates the breakdown
  of the principle". The cost can be moved between the two steps. Only their *sum* is bounded.
- [PHYS] **Measurement has a real resource cost in quantum thermodynamics.** Guryanova, Friis & Huber 2020,
  "Ideal Projective Measurements Have Infinite Resource Costs", *Quantum* 4, 222.
  doi:10.22331/q-2020-01-13-222 (arXiv:1805.11899). Deffner, Paz & Zurek 2016, "Quantum work and the
  thermodynamic cost of quantum measurements", *PRE* 94, 010103. doi:10.1103/PhysRevE.94.010103. Linpeng
  et al. 2022, "Energetic Cost of Measurements Using Quantum, Coherent, and Thermal Light", *PRL* 128, 220506.
  doi:10.1103/PhysRevLett.128.220506. These papers cost the *measurement apparatus* within unitary quantum
  mechanics. None costs a physical collapse.
- **Critique of Landauer (counterpoint literature):** Norton 2005, "Eaters of the lotus: Landauer's
  principle and the return of Maxwell's demon", *Stud. Hist. Phil. Mod. Phys.* 36, 375–411.
  doi:10.1016/j.shpsb.2004.12.002 (metadata verified).
- **Collapse models already have a thermodynamics literature.**
  - The CSL/GRW heating rate for a body of mass M is dE/dt = (3/4) λ ħ² M / (r_C² m_N²). Source: Bassi,
    Lochan, Satin, Singh & Ulbricht 2013, "Models of wave-function collapse, underlying theories, and
    experimental tests", *Rev. Mod. Phys.* 85, 471 (arXiv:1204.4325), Eq. (224), citing Adler 2007. The λ
    symbol was lost in PDF text extraction, and we restored it by dimensional analysis. Check it against the
    typeset PDF before quoting. The same review says the heating is "negligible for all practical purposes"
    and quotes an IGM-heating bound of "λ should be smaller than about 10⁻⁸".
  - Dissipative fixes introduce a **finite-temperature collapse noise**. Smirne, Vacchini & Bassi 2014, *PRA*
    90, 062135. doi:10.1103/PhysRevA.90.062135 (arXiv:1408.6115): "The finite asymptotic energy is naturally
    associated to a collapse noise with a finite temperature." Smirne & Bassi 2015, "Dissipative Continuous
    Spontaneous Localization (CSL) model", *Sci. Rep.* 5, 12518. doi:10.1038/srep12518.
  - **Entropy production in collapse models:** Artini, Lo Monaco, Donadi & Paternostro 2025,
    "Nonequilibrium thermodynamics of gravitational objective-collapse models", *Phys. Rev. Research* 7
    (doi:10.1103/7hqd-zf96, arXiv:2502.03173). "The original DP model induces unbounded heating, producing
    dynamics consistent with the Second Law … only under the assumption of an infinite-temperature noise
    field." The follow-up is Melo, Paraguassú, Artini, Lo Monaco & Donadi 2026, arXiv:2606.06259 (**preprint**):
    dissipative DP/CSL settles into a non-equilibrium steady state, and its "thermodynamic validity" is
    confirmed through Wigner entropy production.
  - Bahrami, Bassi, Donadi, Ferialdi & León 2015, "Irreversibility and Collapse Models", Springer chapter
    doi:10.1007/978-3-319-10446-1_6 (metadata only). te Vrugt, Tóth & Wittkowski 2021, *J. Comput.
    Electron.* 20, 2209 (doi:10.1007/s10825-021-01804-6, arXiv:2106.00137) tested Albert's proposal that
    GRW collapses produce thermodynamic irreversibility. The result: "GRW-type perturbations do not lead to
    thermodynamic behavior".
- **Experimental heating bounds already in the repo** (not re-verified here): XENONnT 2026 (*PRL* 136,
  120201) and LISA Pathfinder (Helou et al. 2017). See `experiments/001-collapse-as-rollback/research/imperfection-signatures.md`.
- [PHYS] **Decoherence rates exist, as timescales.** Schlosshauer 2019, "Quantum Decoherence", *Phys. Rep.*
  831, 1–57 (doi:10.1016/j.physrep.2019.10.001, arXiv:1911.06282), Table 1 gives collisional decoherence
  times for Δx equal to the object's size. For a **dust grain** (Δx = 10⁻³ cm): CMB **1 s**, room-temperature
  photons **10⁻¹⁸ s**, best lab vacuum **10⁻¹⁴ s**, air **10⁻³¹ s**. For a **large molecule** (Δx = 10⁻⁶ cm):
  10²⁴ s, 10⁶ s, 10⁻² s and 10⁻¹⁹ s respectively.

### Numbers (our arithmetic; k_B = 1.380649 × 10⁻²³ J/K)

| quantity | value |
|---|---|
| kT ln 2 at 2.725 K (CMB) | **2.61 × 10⁻²³ J** (1.6 × 10⁻⁴ eV) |
| kT ln 2 at 300 K | **2.87 × 10⁻²¹ J** (0.018 eV) |
| CSL heating per kg at GRW values (λ = 10⁻¹⁶ s⁻¹, r_C = 10⁻⁷ m), Eq. 224 | **3.0 × 10⁻¹⁷ W/kg** |
| same, at the XENONnT limit λ ≈ 3 × 10⁻¹⁷ s⁻¹ (r_C = 10⁻⁷ m) | **8.9 × 10⁻¹⁸ W/kg** |
| that heating in Landauer units, GRW values | about **1.0 × 10⁴ bits/s/kg** at 300 K, or **1.1 × 10⁶ bits/s/kg** at 2.725 K |
| energy per GRW "hit" on one nucleon (from Eq. 224 with M = m_N, divided by λ) | **5.0 × 10⁻²⁸ J**, about **2 × 10⁻⁵ × kT ln 2 at 2.7 K** |
| GRW hits per second per kg (λ = 10⁻¹⁶ s⁻¹ × 6.0 × 10²⁶ nucleons) | **6 × 10¹⁰ s⁻¹** |
| "one erased bit per decoherence time", dust grain in air, 300 K | 10³¹ s⁻¹ × 2.87 × 10⁻²¹ J = **3 × 10¹⁰ W per grain** |

How to read the table:
1. **Each GRW hit deposits far less than one Landauer quantum.** If every collapse hit had to pay
   kT ln 2 *locally*, even into a 2.7 K reservoir, a collapse model would heat matter at least about
   **5 × 10⁴ times** more than standard CSL does at the same λ. So heating bounds on λ would tighten by
   roughly that factor for such a "Landauer-paying" variant. This is a candidate *testable number*, but it
   depends on unsettled choices: which reservoir temperature applies, and whether a hit on one nucleon erases
   a whole bit.
2. **The last row is a reductio.** The claim "every decoherence event erases a bit, paid in-universe" gives
   absurd heat: 30 GW per dust grain. A decoherence *time* is not a count of bits. And standard decoherence
   is unitary: the environment *copies* which-path information rather than erasing it (the Bennett point
   above). So **no source supports a figure for "bits erased per second by decoherence"**, and we leave that
   question open.

### Prior art: is "collapse pays Landauer" open, answered or anticipated?

**Verdict: anticipated as a framing in unrefereed preprints. Not answered in peer-reviewed literature. The
quantitative comparison with collapse-model heating bounds is open.**

- **Anticipated (unrefereed, Zenodo):**
  - **Yaman, S. H. 2026**, "Wavefunction Collapse as Algorithmic Garbage Collection: Deriving the Born Rule
    from the Bennett-Landauer Bound", Zenodo preprint, 2026-03-17. doi:10.5281/zenodo.19057971. It calls
    collapse "a mandatory thermodynamic memory-management protocol" that is triggered when "the local
    Bennett-Landauer processing cost exceeds the local holographic energy budget". v2 was retitled "The Zeno
    Threshold: Wavefunction Collapse and the Emergence of Time via Landauer Erasure Limits"
    (doi:10.5281/zenodo.19057970 / 19079576 / 19120401). It explicitly "re-defines wavefunction collapse as
    an automated algorithmic 'garbage collection'" and treats time as "the thermodynamic exhaust generated by
    Landauer erasure events". **This is the repo's exact metaphor, published six months earlier.** The
    abstract does **not** compare the heat with the XENONnT, LISA Pathfinder or CSL heating bounds.
  - **Dudaš, D. 2026**, "Wave Function Collapse as Minimum Information Cost", Zenodo.
    doi:10.5281/zenodo.19358485. The realised outcome "minimizes the total Landauer erasure energy", and the
    paper predicts "measurement cost scales as kT·H(p)".
  - **Wen, C. C. 2026**, "The Primordial Activation Source Hypothesis (PASH) and Landauer-Induced
    Wavefunction Collapse", OSF (osf.io/br4uk) and Zenodo doi:10.5281/zenodo.19394088. It claims a collapse
    rate Γ(T) = (k_B ln2/ħ)·T and a "state-dependent calorimetric dissipation" test.
  - Daou, R. 2026, Zenodo doi:10.5281/zenodo.19760879. An optomechanics protocol for "non-thermal
    transients" at collapse, built on Vopson's mass–energy–information principle.
  - None of these is peer-reviewed. Treat them as evidence that the *idea* is out there, not as physics.
- **Adjacent peer-reviewed work (simulation + information thermodynamics):** Vopson 2023, "The second law of
  infodynamics and its implications for the simulated universe hypothesis", *AIP Advances* 13, 105308
  (doi:10.1063/5.0173278). Vopson 2019, "The mass-energy-information equivalence principle", *AIP Advances* 9
  (doi:10.1063/1.5123794). Neither is about collapse or branch deletion. (The article number 105308 was not
  shown by Crossref. Confirm it before quoting.)
- **Adjacent peer-reviewed work (collapse thermodynamics without Landauer):** Smirne–Bassi, Artini et al.
  2025, Melo et al. 2026 and te Vrugt et al. 2021 (above). They treat collapse noise as a heat bath with a
  temperature, not as bit erasure.
- **Not found:** any peer-reviewed paper that (a) assigns a Landauer cost to the discarded branches of a
  physical collapse **and** (b) compares it with CSL/DP heating or X-ray bounds. This is the part the repo
  could still contribute. Word it as "we found no indexed peer-reviewed source". Do not call it new.

### Counterpoints

- **The bill may be paid in the host.** In a simulation, deleting branch data is a logically irreversible
  step on the *host's* memory, at the *host's* temperature. Landauer then predicts heat in the host's world,
  not ours, and no in-universe signature is required. This is the strongest objection to calling it a
  "testable number".
- **In-universe, collapse need not erase anything.** Measurement and copying can be reversible (Bennett), and
  the Sagawa–Ueda bound applies only to measurement plus erasure *together*. Taking a pure state to a pure
  state reduces no thermodynamic entropy, so Landauer's many-to-one argument does not obviously apply.
- **Collapse-model heating is a different mechanism.** In CSL it is momentum diffusion from the noise, not
  erasure heat. The two costs should not be added naively.
- Landauer's principle itself has critics (Norton 2005). Its experimental support is for classical bits in
  colloidal systems (Bérut 2012; Jun 2014).

---

## C2. Absolute zero

### Verified facts

- [PHYS] **Third Law (unattainability).** Masanes & Oppenheim 2017, "A general derivation and quantification
  of the third law of thermodynamics", *Nat. Commun.* 8, 14538. doi:10.1038/ncomms14538 (arXiv:1412.3828).
  Their abstract calls it "the first derivation of a general unattainability principle, which applies to
  arbitrary cooling processes, even those exploiting the laws of quantum mechanics". It finds that "the
  obtainable temperature can scale as an inverse power of the cooling time". The derivation "relies on the
  heat capacity of the bath being positive". The paper also bounds "the speed at which information can be
  erased", which is a direct bridge to C1.
- [PHYS] **Link between Landauer and Nernst:** Taranto, Bakhshinezhad, Blühm, Silva, Friis et al. 2023,
  "Landauer Versus Nernst: What is the True Cost of Cooling a Quantum System?", *PRX Quantum* 4, 010332.
  doi:10.1103/PRXQuantum.4.010332. It connects "the third law of thermodynamics with Landauer's principle".
  Producing a pure state (a perfectly erased bit) and reaching T = 0 are the same impossibility.
- [PHYS] **Coldest temperatures.** Deppner et al. 2021, "Collective-Mode Enhanced Matter-Wave Optics",
  *PRL* 127, 100401. doi:10.1103/PhysRevLett.127.100401. It lowers "the total internal kinetic energy of a
  BEC comprising 101(37) thousand atoms in three dimensions to 3/2 k_B · **38 (+6/−7) pK**". **Caveat:** 38 pK
  is a kinetic-energy-equivalent temperature of a matter-wave-lensed BEC, not an equilibrium thermodynamic
  temperature. The earlier benchmark is Leanhardt et al. 2003, "Cooling Bose-Einstein Condensates Below 500
  Picokelvin", *Science* 301, 1513–1515. doi:10.1126/science.1088827, with a kinetic temperature of
  "450 ± 80 picokelvin". Safe wording: "atoms have been slowed to an effective 38 pK".
- (Our arithmetic) kT ln 2 at 38 pK = **3.6 × 10⁻³⁴ J**. Erasing a bit gets cheap near absolute zero, but
  reaching zero would take infinite resources.
- [PHYS] **Zero-point energy** (ground-state motion ½ħω per mode) is textbook quantum mechanics. We cite no
  specific paper here. The repo already cites Whittle et al. 2021 (a 10 kg object at 10.8 phonons) as an
  example of approaching the motional ground state.

### Prior art for the simulation framing ("the idle loop never stops")

- No indexed source was found framing zero-point motion as an engine's "minimum update" or idle loop.
  Queries were run on OpenAlex (`"simulation hypothesis"` combined with the terms below). Treat the idea as
  unclaimed but low-value until it predicts something.
- The Landauer ↔ Nernst link (Taranto 2023; Masanes & Oppenheim 2017) is a real bridge. "Resetting memory
  to all zeros" and "cooling to absolute zero" are the same unreachable limit. That is the strongest
  CS-physics point for this episode, and it is **mainstream physics, not new**.

### Counterpoints
- Zero-point energy and the Third Law follow from standard quantum mechanics and thermodynamics. An engine
  story adds nothing unless it predicts a deviation, such as a floor above the quantum ground state.

---

## C3. Planck scale and "pixels"

### Verified facts

- [PHYS] **GRB 090510 (Fermi).** Abdo et al. 2009, "A limit on the variation of the speed of light arising
  from quantum gravity effects", *Nature* 462, 331–334. doi:10.1038/nature08574 (arXiv:0908.1832). From the
  text: for linear LIV (n = 1), using the 31 GeV photon (conservatively 28.0 GeV at z = 0.900), all limits
  (a)–(g) in Table 2 "are all above M_Planck". The most conservative limit is **M_QG,1/M_Planck > 1.19**, and
  the least conservative, (e), is **> 102**. "Models with n > 1 are not significantly constrained." So the
  repo's statement is **correct for linear energy dependence only**. Quadratic (n = 2) LIV is not excluded
  at the Planck scale.
- [PHYS] **An updated limit:** Vasileiou et al. 2013, "Constraints on Lorentz invariance violation from
  Fermi-Large Area Telescope observations of gamma-ray bursts", *PRD* 87, 122001.
  doi:10.1103/PhysRevD.87.122001 (arXiv:1305.3463). From GRB 090510, E_QG,1 > **7.6 E_Pl** (95% C.L.,
  subluminal) and E_QG,2 > **1.3 × 10¹¹ GeV** (quadratic).
- [PHYS] **Beane, Davoudi & Savage 2014**, *Eur. Phys. J. A* 50, 148. doi:10.1140/epja/i2014-14148-0
  (arXiv:1210.1847). The abstract says the "most stringent bound on the inverse lattice spacing of the
  universe, b⁻¹ ≳ 10¹¹ GeV, is derived from the high-energy cut off of the cosmic ray spectrum". A lattice
  could show up as "rotational symmetry breaking" in the highest-energy cosmic rays.
- **Minecraft "Far Lands": the repo's current wording needs a correction.** The Minecraft Wiki
  (<https://minecraft.wiki/w/Far_Lands>, read 2026-09-23) says the Far Lands "are a terrain generation bug …
  that appear when noise generators responsible for terrain shape malfunction due to **integer overflow**".
  The low-noise generator breaks at **12,550,824** blocks. The Far Lands "were fixed in Beta 1.8 Pre-release
  in Java Edition". The same page separates this from a **floating-point** effect: "Precision loss errors are
  not caused by the Far Lands … this is purely a floating-point bug", which grows gradually "at each power of
  2", with 16,777,216 given as an example. **ROADMAP.md says "Minecraft's 'Far Lands' show what precision
  loss looks like". Change that to "integer overflow in the terrain noise (Far Lands) plus separate
  floating-point jitter far from the origin".** Both are useful analogies, and they are different bugs. (A
  community wiki is a weak source, but it is the maintained reference for game mechanics.)

### Prior art for the simulation framing
- **Anticipated:** lattice artefacts as a test of simulation (Beane et al. 2014). Floating-origin and
  precision-loss analogies are common in game development. We found no indexed physics paper that uses the
  Far Lands. OpenAlex `"simulation hypothesis" AND ("floating point" OR "floating-point")` returned only 4
  unrefereed Zenodo items, none about the Far Lands.

### Counterpoints
- There is no sign of a preferred lattice direction or of energy-dependent light speed at linear order,
  beyond the Planck scale. There is also no position-dependent precision loss: physics is the same
  everywhere, with no origin. Quadratic effects and a lattice spacing below 10⁻¹¹ GeV⁻¹ (b⁻¹ above 10¹¹ GeV)
  remain allowed, so "no pixels found" means "none at the scales probed".

---

## D1. What are quarks and subatomic particles "in a simulation"?

### Verified facts

- [PHYS] **Most of the proton's mass is not quark rest mass.** PDG 2024 (Navas et al., Particle Data Group,
  *Phys. Rev. D* 110, 030001, 2024; quark summary table rpp2024-sum-quarks.pdf) gives **m_u = 2.16 ± 0.07
  MeV** and **m_d = 4.70 ± 0.07 MeV** (MS-bar scheme). Our arithmetic: 2m_u + m_d = 9.02 MeV, which is
  **0.96%** of m_p = 938.27 MeV. For the neutron, m_u + 2m_d is 1.2%. So "~99% is not valence-quark rest
  mass" holds.
- [PHYS] **Dürr et al. 2008**, "Ab Initio Determination of Light Hadron Masses", *Science* 322, 1224–1227.
  doi:10.1126/science.1163233 (arXiv:0906.3599). A lattice-QCD calculation of proton, neutron and other light
  hadron masses that "completely agree[s] with experimental observations". The abstract says protons and
  neutrons "are much heavier than their quark and gluon constituents". **The abstract does not state "99%
  from binding energy".** Its "more than 99%" refers to protons and neutrons making up the mass of the
  *visible universe*. Don't misattribute it.
- [PHYS] **Yang et al. 2018**, "Proton Mass Decomposition from the QCD Energy Momentum Tensor", *PRL* 121,
  212001. doi:10.1103/PhysRevLett.121.212001 (arXiv:1808.08677). In MS-bar at 2 GeV: quark energy **32(4)(4)%**,
  gluon field energy **36(5)(4)%**, a quarter of the trace anomaly **23(1)(1)%**, and u, d, s quark scalar
  condensates **9(2)(1)%**. **Nuance:** the quark-mass-related term (sigma terms, including strange) is about
  9%, not about 1%. The 1% figure is the naive sum of valence masses. A precise line: "about 1% is the bare
  quark masses; nearly all the rest is the energy of the quark and gluon fields."
- [PHYS] **Lattice QCD literally puts quarks on a spacetime grid.** Wilson 1974, "Confinement of quarks",
  *PRD* 10, 2445–2459. doi:10.1103/PhysRevD.10.2445 (metadata verified). Dürr et al. used three lattice
  spacings and extrapolated to the continuum (their abstract).
- [PHYS] **String breaking is seen on the lattice.** Bali, Neff, Düssel, Lippert & Schilling 2005,
  "Observation of string breaking in QCD", *PRD* 71, 114513. doi:10.1103/PhysRevD.71.114513
  (arXiv:hep-lat/0505012). They resolve "the transition of the static quark-antiquark string into a
  static-light meson-antimeson system", with n_f = 2. Pulling the pair apart makes a new pair, and you get
  two mesons, never a free quark.
- [PHYS] **Identical particles: prior art from physics itself.** In his 1965 Nobel lecture ("The Development
  of the Space-Time View of Quantum Electrodynamics", nobelprize.org), Feynman recounts Wheeler's phone call:
  "Feynman, I know why all electrons have the same charge and the same mass … Because, they are all the same
  electron!" This is the "one-electron universe".

### Prior art for the simulation/CS framings

| framing | status | source |
|---|---|---|
| particles as persistent patterns ("gliders") in a discrete update rule | **anticipated** | Fredkin 1990, "An informational process based on reversible universal cellular automata", *Physica D* 45, 254–270, doi:10.1016/0167-2789(90)90186-S (metadata only); Wolfram 2020, §8.9 "Elementary Particles": particles "would correspond to structures in the hypergraph that are locally stable under the application of rules", with rule 110's "localized structures" as the analogy; 't Hooft 2016, *The Cellular Automaton Interpretation of Quantum Mechanics*, Springer FTP 185, doi:10.1007/978-3-319-41285-6 (metadata) |
| identical particles as one shared object (flyweight / instancing) | **physics analogue anticipated** by Wheeler's one-electron idea (Feynman 1965). **No indexed source found** for the explicit flyweight/instancing mapping | OpenAlex "identical particles flyweight pattern" gave nothing relevant; HN comments "electrons flyweight" and "identical particles instancing simulation" gave nothing relevant |
| confinement as a data-validity or "no orphan objects" constraint | **none found** | OpenAlex `"simulation hypothesis" AND (quark OR confinement OR "identical particles")` returned 4 records: one SSRN paper (Macleod 2017, "The Mathematical Electron…", doi:10.2139/ssrn.2531429, not about confinement) and 3 unrefereed Zenodo items |
| lattice QCD ⇒ a universe simulated on a grid | **anticipated** | Beane et al. 2014 (C3) build their argument on lattice QCD |

### Counterpoints
- Mass from field energy and confinement follow from QCD with no engine assumptions, and lattice QCD
  reproduces them. A CS reading is a redescription unless it predicts something, such as lattice-direction
  artefacts (bounded, see C3).
- Particle identity in quantum field theory comes from particles being excitations of one field. That is
  already "one object, many instances", so a flyweight analogy adds vocabulary, not content.

---

## Unverified leads

- **Blondin et al. 2008 DOI.** Crossref was rate-limited. The journal-ref (ApJ 682, 724–736) comes from arXiv.
- **Vopson 2023 article number 105308.** Not shown in the Crossref output. The DOI 10.1063/5.0173278 is verified.
- **Milky Way potential term** for the Earth-clock vs cosmic-time comparison (probably ~10⁻⁶). We found no
  source.
- **CUORE bulk-heating and astrophysical (white-dwarf, lunar) collapse bounds.** We didn't open these. They
  would be the right comparison for a "Landauer-paying collapse" variant.
- **The λ in Bassi et al. 2013 Eq. (224)** was restored by dimensional analysis. Check the typeset equation.
- **Bennett (1973, 1982, 2003) and Norton (2005)** are cited for their well-known theses, with metadata
  verified only.
- **Dudaš, Wen and Daou** Zenodo items: abstract-level only. Yaman's GitHub companion repos
  (srdrymn/atr-verify-wavefunction-collapse, srdrymn/atr-wavefunction-collapse) were not inspected.
- **Space.com "five times slower"** quote: we read the page text; the author and byline were not extracted.

## Queries run (record)

WebSearch was attempted once and refused (budget of 200/200 used). All queries below are logged in
`scratchpad/queries.log`, and the main ones are listed here.
- **Crossref** (DOI lookups): 10.1147/rd.53.0183, 10.1038/nature10872, 10.1103/PhysRevLett.113.190601,
  10.1147/rd.176.0525, 10.1007/BF02084158, 10.1103/PhysRevLett.102.250602, 10.1038/ncomms14538,
  10.1103/PhysRevLett.127.100401, 10.1038/nature08574, 10.1126/science.1163233, 10.1103/PhysRevLett.121.212001,
  10.1103/PhysRevD.10.2445, 10.1038/s41550-023-02029-2, 10.1051/0004-6361/201833910,
  10.1140/epja/i2014-14148-0, 10.1007/978-3-319-10446-1_6, 10.1103/7hqd-zf96.
- **Crossref** (bibliographic searches): Bérut 2012; Goldhaber 2001; Blondin 2008; Planck 2018 I/VI; Kogut
  dipole; Fixsen 2009; Fredkin 1990; Bali 2005; Leanhardt 2003; 't Hooft 2016; Vasileiou 2013; Bennett 2003;
  Norton 2005; Toyabe 2010; Vopson 2019/2023; Wolfram 2020.
- **arXiv abs pages or PDFs:** 2306.04053, 0908.1832, 0906.3599, 0804.3595, 1412.3828, 1807.06209v4,
  1807.06205, 1204.4325, 1911.06282, 1210.1847, 2004.08210, 2606.06259, 2502.03173. (The arXiv API returned
  HTTP 429, so we used abs pages instead.)
- **OpenAlex search:** "Landauer principle wave function collapse"; "collapse model Landauer erasure";
  "thermodynamics collapse models dissipative GRW energy"; "Landauer bound quantum measurement erasure cost";
  "Hemmo Shenker GRW thermodynamics Maxwell demon"; "quantum heat measurement Elouard Auffeves"; "ideal
  quantum measurements require infinite resources"; "Bedingham Maroney collapse models time symmetry";
  "energy increase space collapse models"; "dissipative extension GRW"; "simulation hypothesis Landauer
  principle"; "simulation hypothesis garbage collection quantum"; "cosmic time global clock simulation
  hypothesis"; "identical particles flyweight pattern"; "simulation hypothesis floating point precision
  physics"; "quark confinement simulation hypothesis".
- **OpenAlex boolean (title_and_abstract):** `landauer AND "wave function collapse"` (35 hits, mostly Zenodo);
  `landauer AND "collapse model"` (15); `landauer AND "spontaneous collapse"` (3, irrelevant);
  `landauer AND "objective collapse"` (19); `landauer AND "many-worlds"` (18, irrelevant);
  `landauer AND (GRW OR "continuous spontaneous localization")` (14, irrelevant);
  `thermodynamics AND "collapse models" AND entropy` (4); `"thermodynamic cost" AND "quantum measurement"`
  (13); `landauer AND decoherence AND "measurement problem"` (17); `"simulation hypothesis" AND landauer` (5,
  all Zenodo); `"simulation hypothesis" AND ("cosmic time" OR "cosmological time")` (0);
  `"simulation hypothesis" AND (quark OR confinement OR "identical particles")` (4);
  `"simulation hypothesis" AND ("floating point" OR "floating-point")` (4);
  `"garbage collection" AND ("many worlds" OR "wave function" OR "wavefunction")` (8, which found Yaman 2026).
- **Semantic Scholar:** DOI lookups for Lewis & Brewer, Goldhaber, Abdo, Deppner, Yang, and Masanes &
  Oppenheim. Keyword searches mostly failed with rate limits. "thermodynamics of collapse models entropy"
  returned Artini 2025, Melo 2026 and Bahrami 2015.
- **HN Algolia:** stories for "quasar time dilation five times slower", "early universe five times slower",
  "time dilation simulation lag", "simulation hypothesis time dilation processing", "wave function collapse
  garbage collection", "Landauer simulation hypothesis", "Far Lands floating point physics", "one electron
  universe" and "simulation hypothesis quarks". Comments for "electrons flyweight", "identical particles
  instancing simulation", "time dilation simulation lag", "collapse landauer simulation" and "cosmic time tick
  simulation".
- **Other sources:** PubMed (Bérut abstract), Zenodo API (Yaman records 19057971, 19079576 and 19120401),
  SEP "Philosophy of Cosmology", minecraft.wiki "Far_Lands", nobelprize.org Feynman 1965 lecture, PDG 2024
  quark summary, and Space.com.
