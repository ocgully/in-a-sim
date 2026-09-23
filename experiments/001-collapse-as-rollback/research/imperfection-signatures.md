# Experiment 001: Imperfection Signatures of a "Rollback" Collapse

*Compiled 2026-09-23. This is a thought experiment. Nothing here claims we live in a simulation. The question is narrow: **if** wave-function collapse were an optimization in a distributed simulation (a probabilistic engine mode that rolls back and re-runs into one timeline when an observation needs a committed answer), where might that optimization show seams, and what has experiment already ruled out?*

**How citations were checked.** Every entry below was checked against at least one primary record: Crossref DOI metadata, arXiv API metadata, PubMed, or the publisher's page. Where we give a number (a delay, a mass, a bound), we read it in the paper itself, using text extracted from the arXiv or open-access PDF. Numbers we worked out ourselves are marked "(our arithmetic)". Anything we could not confirm is listed under **5. Unverified leads**.

---

## Summary table

| Signature | Best experimental bound | Source |
|---|---|---|
| **Finite rollback window** (a randomised choice made *after* the first detection) | No failure seen with the choice made **≈ 450 µs** after the system photon's interferometer events, with the two labs **144 km** apart (La Palma to Tenerife). The authors call this a record by more than 5 orders of magnitude over earlier quantum erasers. | Ma et al. 2013, *PNAS* |
| **Finite rollback window** (first detection, then the entangled partner measured much later) | Ion–photon entanglement fidelity of **0.81(4) after 10 s** of storage. The photon was detected before storage began, and a fidelity above 0.5 shows entanglement. Separately, a **Bell violation (S = 2.36 ± 0.14) after 1 s** of storage, with the partner photon detected first. | Drmota et al. 2023, *PRL*; Wang et al. 2021, *PRL* |
| **Finite rollback window** (Wheeler-type, choice made while the photon is in flight) | Interferometer spanning satellite to ground: slant ranges **1264–1771 km**, propagation distance "up to 3500 km", round-trip time "of the order of 10 ms" | Vedovato et al. 2017, *Sci. Adv.* |
| **Size / complexity threshold** (matter-wave interference) | Sodium nanoparticles with **> 7,000 atoms and > 170,000 Da**, macroscopicity **μ = 15.5** | Pedalino et al. 2026, *Nature* |
| **Size / complexity threshold** (mechanical cat state) | Effective mass **16.2 µg (~10¹⁷ atoms)**, superposed over **2.1 × 10⁻¹⁸ m** | Bild et al. 2023, *Science* |
| **Size threshold** (how long a superposition lasts) | Atoms held in a spatial superposition for **70 s** | Panda et al. 2024, *Nat. Phys.* |
| **Side effects** (spontaneous X-rays) | White-noise CSL: **λ/r_C² < 3.0 × 10⁻³ s⁻¹ m⁻²** (90% C.L.). The original GRW values are excluded (disfavoured at 9.1σ). Diósi–Penrose: **R₀ > 4.9 × 10⁻¹⁰ m** (90% C.L.). | XENONnT (Aprile et al.) 2026, *PRL* |
| **Side effects** (mechanical heating / force noise) | LISA Pathfinder: **λ_CSL ≤ (2.96 ± 0.12) × 10⁻⁸ s⁻¹** and **σ_DP ≥ 40.1 ± 0.5 fm** (original data). A preprint using updated data gives λ_CSL ≤ 8.3 × 10⁻¹¹ s⁻¹ at r_CSL = 10⁻⁷ m. | Helou et al. 2017, *PRD*; Dai et al. 2024 (arXiv preprint) |
| **Prior art for the "finite rollback window" test** | We found **no paper** proposing a maximum retrocausal or rollback span as a test. The closest analogues bound a *finite speed* of hidden influence, and a *finite collapse time* Tc under the "collapse locality loophole". | Salart et al. 2008; Yin et al. 2013; Bancal et al. 2012; Kent 2005/2020; Agüero et al. 2026 |

**Short version.** Standard quantum mechanics has held in every case: at a randomised delayed choice about half a millisecond after detection, over 144 km; with entanglement confirmed after 10 s of storage; and with objects of 170,000 Da in interference and 16 µg in cat states. Every loss of quantum correlation seen so far is explained by known decoherence. None needs a "buffer overflow".

---

## 1. Rollback window

### 1.1 What is being bounded

In the rollback picture, an early detection commits an outcome at time t₁. A later measurement at t₂, on an entangled partner or on the "choice" side of a delayed-choice setup, decides which correlation pattern the early record belongs to. If the engine only reconciles by rewinding, it must still hold whatever state it needs from t₁ when t₂ arrives. So the rollback buffer must be at least **Δ = t₂ − t₁**. If the buffer were finite (Δ_max), then experiments with Δ > Δ_max should show the late measurement *failing to correlate* with the early record. For example, CHSH S would fall to ≤ 2, or the conditional fringes in a quantum eraser would vanish, **beyond** what known decoherence of the storage medium explains.

Two caveats matter for the public write-up:

- **Standard quantum mechanics needs no rollback at all.** In every delayed-choice and eraser experiment, the early photon's own statistics never change. The later choice only decides how the already-recorded data can be *sorted* into sub-ensembles. Ma et al. 2013 do this sorting from time-tags "long after the experiment is finished". So these experiments bound a rollback window only *inside* the rollback model. They are not evidence for rollback.
- **Two kinds of experiment give different lower bounds.** (a) True delayed-choice experiments use a *random* choice made after the first detection, but their delays are short (ns to sub-ms). (b) Quantum-memory experiments detect one half of an entangled pair first and measure the other half seconds later, but the late measurement basis is set by a tomography schedule rather than a fast random choice. Both kinds constrain a "reconcile on the late measurement" engine.

### 1.2 Delayed-choice experiments (random choice after the first detection)

| Experiment | Δ between first detection and later choice or measurement | Distance | Notes |
|---|---|---|---|
| **Kim, Yu, Kulik, Shih & Scully 2000**, "Delayed 'Choice' Quantum Eraser", *PRL* 84, 1–5. doi:10.1103/PhysRevLett.84.1 (arXiv:quant-ph/9903047) | "at least 8 ns" | ≈ 2.5 m extra optical path | The "choice" is made passively by beam splitters, not by a random number generator. |
| **Ma, Zotter, Kofler, Ursin, Jennewein, Brukner & Zeilinger 2012**, "Experimental delayed-choice entanglement swapping", *Nat. Phys.* 8, 479–484. doi:10.1038/nphys2294 (arXiv:1203.4834) | Victor's choice falls "14 ns to 313 ns later" than Alice's and Bob's measurements. His measurement is 485 ns later. | 104 m fibre (520 ns) for photons 2 and 3. Alice and Bob's photons travel 7 m (35 ns). | Whether the earlier-measured photons count as entangled or separable is decided after they are measured. The choice comes from a quantum random number generator. |
| **Megidish, Halevy, Shacham, Dvir, Dovrat & Eisenberg 2013**, "Entanglement Swapping between Photons that have Never Coexisted", *PRL* 110, 210403. doi:10.1103/PhysRevLett.110.210403 (arXiv:1209.4191) | Photon 1 is detected *before* photon 4 is created. The delay line spans eight laser pulses. | 31.6 m free-space delay (105 ns) | Entanglement between photons whose lifetimes never overlapped. |
| **Ma, Kofler, Qarry, Tetik, Scheidl, Ursin, Ramelow, Herbst, Ratschbacher, Fedrizzi, Jennewein & Zeilinger 2013**, "Quantum erasure with causally disconnected choice", *PNAS* 110, 1221–1226. doi:10.1073/pnas.1213201110 (arXiv:1206.6578) | **Canary Islands:** in one arrangement the choice event "happens approximately 450 µs after" the system photon's interferometer events (in the source frame). The authors call this "a record to the amount of delay by more than 5 orders of magnitude" compared with Kim et al. 2000. The environment photon's flight time is ≈ 479 µs. The choice-to-emission offsets used were −721 µs, 0 µs and 454 µs. **Vienna:** 55 m fibre (275 ns). | **144 km** free space (La Palma to Tenerife). Link attenuation is about 33 dB in the main text and 35 dB in the supplement. | **Longest randomised post-detection delay we could verify.** Results were "similar to the Vienna experiment" after background subtraction. |

### 1.3 Wheeler-type delayed choice (choice made after the photon enters, but before it is detected)

These tests do not put a detection *before* the choice, so a rollback engine could simply defer. We list them because they hold the distance records.

- **Jacques, Wu, Grosshans, Treussart, Grangier, Aspect & Roch 2007**, "Experimental Realization of Wheeler's Delayed-Choice Gedanken Experiment", *Science* 315, 966–968. doi:10.1126/science.1136303 (arXiv:quant-ph/0610241). The interferometer is 48 m long, a time of flight of about 160 ns. The switch changes state in about 40 ns. The choice, from a quantum random number generator, is space-like separated from the photon's entry.
- **Vedovato, Agnesi, Schiavon, Dequal, Calderaro, Tomasin, Marangon, Stanco, Luceri, Bianco, Vallone & Villoresi 2017**, "Extending Wheeler's delayed-choice experiment to space", *Sci. Adv.* 3, e1701180. doi:10.1126/sciadv.1701180 (arXiv:1704.01911). Photons bounced off the Beacon-C satellite (slant range 1264–1376 km) and the Starlette satellite (1454–1771 km). The paper reports "a propagation distance up to 3500 km" and "a rtt [round-trip time] of the order of 10 ms". The measurement choice was made after reflection from the satellite and is space-like separated from it. Visibility was about 40%, "at least 8σ" above the 9% particle-like bound.

### 1.4 Quantum memories: first detection, then the partner measured seconds later

| Experiment | Δ (early detection to late measurement) | What survived | Notes |
|---|---|---|---|
| **Wang, Yang, Sun, Jing, Li, Zhou, Bao & Pan 2021**, "Cavity-Enhanced Atom-Photon Entanglement with Subsecond Lifetime", *PRL* 126, 090501. doi:10.1103/PhysRevLett.126.090501 (arXiv:2101.01988) | **1 s**. The write-out photon is detected first and heralds the event. The atomic excitation is read out 1 s later. | **Bell violation S = 2.36 ± 0.14** (2.57 standard deviations) | Cold-atom ensemble. The memory lifetime is 458(19) ms, so this is past the 1/e point. |
| **Drmota, Main, Nadlinger, Nichol, Weber, Ainley, et al. 2023**, "Robust Quantum Memory in a Trapped-Ion Quantum Network Node", *PRL* 130, 090803. doi:10.1103/PhysRevLett.130.090803 (arXiv:2210.11447) | **10 s**. The attempt loop runs "until a single photon is detected", and the ion qubit is then stored before tomography. | **Ion–photon entanglement fidelity 0.81(4)** | Fidelity above 0.5 with a Bell state witnesses entanglement. **This is the best verified lower bound on Δ.** |

**Best verified lower bound on a rollback window: Δ ≥ 10 s** (entanglement witnessed, Drmota et al. 2023). With a Bell violation, the bound is **Δ ≥ 1 s** (Wang et al. 2021). With a randomised post-detection choice, it is **Δ ≥ ~450 µs over 144 km** (Ma et al. 2013).

**Why these do not yet make a clean test.** In every memory experiment, correlations *do* decay with storage time. The authors attribute the decay to known mechanisms, such as dephasing and atomic motion, and suppress it with dynamical decoupling, lattices and similar techniques. A buffer limit would show up as a decay that **does not respond** to better memory engineering. Or it would be a sharp cutoff at the same Δ across very different platforms (atoms, ions, rare-earth crystals). Nobody has looked for that pattern.

### 1.5 Nearby results that are *not* rollback-window bounds, and technology that could extend them

- **Entangled states that last for hours, measured all at once.** Xu et al. 2025 (arXiv:2507.13320, preprint) report a "coherence time above two hours for a logical qubit encoded in the decoherence-free subspace" of two-ion entangled states. Both ions are measured together at the end, so there is no early committed record. This bounds how long entanglement can *persist*, not Δ.
- **Photonic memory lasting minutes (single qubits, not entanglement).** Lv, Zhu, Zhou, Li & Guo 2025, "Minute-Scale Photonic Quantum Memory" (arXiv:2511.12537, preprint) report a 1/e storage lifetime of 27.6 ± 0.5 s, 88.0 ± 2.1% fidelity for time-bin qubits at 5.6 s, and single-photon-level storage for 42 s. Storing *one half of an entangled pair* in such a device would push Δ toward a minute.
- **A proposed delayed-choice eraser using memory.** Ohwada 2025 (arXiv:2511.22827, theory preprint) proposes a multimode quantum memory to give "a controlled and verifiable delay" so that the choice comes "strictly after the observation event". It does not discuss a maximum delay.
- **Long-lived remote memory–memory entanglement.** Liu et al. 2026, "Long-lived remote ion–ion entanglement for scalable quantum repeaters", *Nature* 652, 51–57, doi:10.1038/s41586-026-10177-4, shows entanglement over 10 km of spooled fibre "surviving beyond the average entanglement establishment time". The abstract gives no storage duration. See Unverified leads.

---

## 2. Size / complexity threshold

In the rollback picture, an engine that forces a commit above some mass, number of particles or "complexity" would look like a spontaneous-collapse model. So the experimental record on large superpositions, together with the excluded collapse-model parameters, is the relevant bound.

### 2.1 Largest superpositions and interference

- **Fein, Geyer, Zwick, Kiałka, Pedalino, Mayor, Gerlich & Arndt 2019**, "Quantum superposition of molecules beyond 25 kDa", *Nat. Phys.* 15, 1242–1245. doi:10.1038/s41567-019-0663-9. Functionalised oligoporphyrins "with masses beyond 25,000 Da and consisting of up to 2,000 atoms", in a 2-m Talbot–Lau interferometer. De Broglie wavelengths go down to 53 fm, fringes reach "more than 90% of the expected visibility", and macroscopicity is **14.1**.
- **Pedalino, Ramírez-Galindo, Ferstl, Hornberger, Arndt & Gerlich 2026**, "Probing quantum mechanics with nanoparticle matter-wave interferometry", *Nature* 649, 866–870. doi:10.1038/s41586-025-09917-9. Sodium nanoparticles "which can each contain more than 7,000 atoms at masses greater than 170,000 Da", in "a Schrödinger cat state with a macroscopicity of μ = 15.5" (μ = 15.45 in the Methods). The authors say this surpasses previous experiments "by an order of magnitude". The centre of mass is delocalised "over a distance exceeding the diameter of the particle by more than an order of magnitude". The clusters are about 8 nm across, and the grating period is 133 nm. **This is the current matter-wave record we could verify.**
- **Bild, Fadel, Yang, von Lüpke, Martin, Bruno & Chu 2023**, "Schrödinger cat states of a 16-microgram mechanical oscillator", *Science* 380, 274–278. doi:10.1126/science.adf7553 (arXiv:2211.00449). **Verified.** A bulk acoustic resonator mode with effective mass 16.2 µg, "corresponding to ∼10¹⁷ atoms, delocalized over a distance of 2.1 · 10⁻¹⁸ m". This is a very heavy object superposed over a tiny distance. Pedalino et al. describe the two results as complementary regimes.
- **Kovachy, Asenbaum, Overstreet, Donnelly, Dickerson et al. 2015**, "Quantum superposition at the half-metre scale", *Nature* 528, 530–533. doi:10.1038/nature16155. Single atoms delocalised over about half a metre.
- **Panda, Tao, Egelhoff, Ceja, Xu & Müller 2024**, "Coherence limits in lattice atom interferometry at the one-minute scale", *Nat. Phys.* 20, 1234–1239. doi:10.1038/s41567-024-02518-9 (arXiv:2210.07289). "A spatial superposition state that is maintained for as long as 70 seconds." This matters for the rollback model: the engine left this superposition uncommitted for more than a minute.

### 2.2 LIGO-mirror scale (quantum effects, not superpositions)

- **Yu, McCuller, Tse, Kijbunchoo, Barsotti, Mavalvala et al. 2020**, "Quantum correlations between light and the kilogram-mass mirrors of LIGO", *Nature* 583, 43–47. doi:10.1038/s41586-020-2420-8 (arXiv:2002.01519). Quantum correlations between 200 kW beams and the **40 kg** mirrors give a joint uncertainty "a factor of 1.4 (3 dB) below the SQL" (the standard quantum limit).
- **Whittle, Hall, Dwyer, Mavalvala, Sudhir et al. 2021**, "Approaching the motional ground state of a 10-kg object", *Science* 372, 1333–1336. doi:10.1126/science.abh2634 (arXiv:2102.12665). A 10 kg effective oscillator cooled to an average phonon occupation of **10.8** (77 nK).
- Neither is a spatial superposition of the mirror. They show that quantum back-action and correlations persist at kilogram scale. They do not show a kilogram-scale cat state.

### 2.3 Excluded collapse-model parameter regions (beyond Carlesso et al. 2022)

Carlesso et al. 2022 (*Nat. Phys.* 18, 243–250, already cited in `prior-art.md`) is the standard review. Newer or additional bounds:

- **XENONnT: Aprile et al. 2026**, "Challenging Spontaneous Quantum Collapse with the XENONnT Dark Matter Detector", *PRL* 136, 120201. doi:10.1103/2jm3-4976 (arXiv:2506.05507). For the Markovian (white-noise) CSL model: **λ/r_C² < 3.0 × 10⁻³ s⁻¹ m⁻²** at 90% C.L. (3.7 × 10⁻³ at 95%). That is about 135 times better than the Majorana Demonstrator and the most stringent limit for r_C ≲ 10⁻⁵ m. The GRW parameter set (r_C = 10⁻⁷ m, λ = 10⁻¹⁶ s⁻¹) "deviates from the best-fit result by 9.1σ … for the first time, this allows to experimentally exclude CSL model parameter values in the range originally proposed by GRW". For Diósi–Penrose: **R₀ > 4.9 × 10⁻¹⁰ m** at 90% C.L., about five times better than Majorana. (Our arithmetic: at r_C = 10⁻⁷ m the CSL limit corresponds to λ < 3 × 10⁻¹⁷ s⁻¹.)
- **Vinante, Carlesso, Bassi, Chiasera, Varas & Falferi 2020**, "Narrowing the Parameter Space of Collapse Models with Ultracold Layered Force Sensors", *PRL* 125, 100404. doi:10.1103/PhysRevLett.125.100404 (arXiv:2002.09782). A bound at r_C = 10⁻⁷ m that improves on earlier mechanical experiments "by more than one order of magnitude" and is "explicitly challenging a well-motivated region of the CSL parameter space proposed by Adler".
- **Altamura, Vinante & Carlesso 2025**, "Improved bounds on collapse models from rotational noise of LISA Pathfinder", *PRA* 111, L020203. doi:10.1103/PhysRevA.111.L020203 (arXiv:2501.08971). The rotational data give a tighter constraint than translational data.
- **Di Bartolomeo & Carlesso 2024**, "Experimental bounds on linear-friction dissipative collapse models from levitated optomechanics", *New J. Phys.* 26, 043006 (arXiv:2401.04665). For dissipative CSL, "the entire parameter space is excluded for values of the temperature lower than 6 × 10⁻⁹ K".
- **Important caveat.** The X-ray bounds, including XENONnT, assume *white* collapse noise. Coloured noise with a frequency cutoff below X-ray frequencies can escape them. Mechanical bounds, which work at mHz to kHz, are robust to such a cutoff. A 2026 proposal (Zeng, Bassi, … Nägerl, arXiv:2609.07195, preprint) projects λ_c ≃ 1.8 × 10⁻¹¹ s⁻¹ at r_c = 10⁻⁷ m. That would be "an order of magnitude below the strongest existing constraint that remains robust against a cutoff". It is a projection, not a measurement.

---

## 3. Side effects (spontaneous radiation and heating)

A commit that happens stochastically and physically, rather than as pure bookkeeping, generically jiggles particles. Charged particles then radiate, and bulk matter heats up. That is the "side effect" signature.

### 3.1 Spontaneous X-ray / γ emission

| Year | Result | Bound |
|---|---|---|
| 1995 | **Collett, Pearle, Avignone & Nussinov**, "Constraint on collapse models by limit on spontaneous x-ray emission in Ge", *Found. Phys.* 25, 1399–1412. doi:10.1007/BF02057460 | An early Ge-detector bound (metadata verified; we did not read the numbers) |
| 1997 | **Fu**, "Spontaneous radiation of free electrons in a nonrelativistic collapse model", *PRA* 56, 1806–1811. doi:10.1103/PhysRevA.56.1806 | The founding calculation of the radiation rate (metadata verified) |
| 1999 | **Pearle, Ring, Collar & Avignone**, "The CSL Collapse Model and Spontaneous Radiation: An Update", *Found. Phys.* 29, 465–480. doi:10.1023/A:1018879201822 | Update (metadata verified) |
| 2017 | **Piscicchia, Bassi, Curceanu, Del Grande, Donadi et al.**, "CSL Collapse Model Mapped with the Spontaneous Radiation", *Entropy* 19, 319. doi:10.3390/e19070319 | Gran Sasso Ge-detector bound |
| 2021 | **Donadi, Piscicchia, Del Grande, Curceanu, Laubenstein et al.**, "Novel CSL bounds from the noise-induced radiation emission from atoms", *Eur. Phys. J. C* 81, 773. doi:10.1140/epjc/s10052-021-09556-0 | Includes emission from bound atoms |
| 2021 | **Donadi et al.**, *Nat. Phys.* 17, 74–78 (already cited) | Rules out "the natural parameter-free version of the Diósi-Penrose model" |
| 2022 | **Arnquist et al. (Majorana Collaboration)**, "Search for Spontaneous Radiation from Wave Function Collapse in the Majorana Demonstrator", *PRL* 129, 080401. doi:10.1103/PhysRevLett.129.080401. **Erratum** *PRL* 130, 239902 (2023) (arXiv:2202.01343) | No signal in 19–100 keV with 37.5 kg·y of enriched Ge. A "factor of 40–100 improvement" for white CSL. The DP bound is "almost an order of magnitude" better. |
| 2026 | **XENONnT**, *PRL* 136, 120201 (see §2.3) | The current best: CSL λ/r_C² < 3.0 × 10⁻³ s⁻¹ m⁻²; DP R₀ > 4.9 × 10⁻¹⁰ m. First model accounting for electron–proton cancellation in xenon. |
| 2026 | **Manti, Bortolotti, Diósi, Piscicchia & Curceanu**, "Atomic correlation effects in collapse-induced spontaneous radiation" (arXiv:2608.07205, theory preprint) | Refines the predicted rates for Ge and Xe. No new data. |

### 3.2 Heating and force noise (mechanical / gravitational-wave hardware)

- **Carlesso, Bassi, Falferi & Vinante 2016**, "Experimental bounds on collapse models from gravitational wave detectors", *PRD* 94, 124036. doi:10.1103/PhysRevD.94.124036. Bounds from LIGO, AURIGA and LISA Pathfinder.
- **Helou, Slagmolen, McClelland & Chen 2017**, "LISA Pathfinder appreciably constrains collapse models", *PRD* 95, 084054. doi:10.1103/PhysRevD.95.084054 (arXiv:1606.03637). From 5.2 fm s⁻²/√Hz of acceleration noise: **λ_CSL ≤ (2.96 ± 0.12) × 10⁻⁸ s⁻¹** and **σ_DP ≥ 40.1 ± 0.5 fm**, which is "larger than the size of any nucleus".
- **Vinante, Mezzena, Falferi, Carlesso & Bassi 2017**, "Improved Noninterferometric Test of Collapse Models Using Ultracold Cantilevers", *PRL* 119, 110401. doi:10.1103/PhysRevLett.119.110401.
- **Vinante et al. 2020**, *PRL* 125, 100404 (see §2.3).
- **Altamura, Vinante & Carlesso 2025**, *PRA* 111, L020203 (LISA Pathfinder rotational noise; see §2.3).
- **Dai, Miao & Ma 2024**, "Updating the constraint on the quantum collapse models via kilogram masses" (arXiv:2411.17588, **preprint**). Using updated LISA Pathfinder data: **λ_CSL ≤ 8.3 × 10⁻¹¹ s⁻¹** at r_CSL = 10⁻⁷ m, and σ_DP ~ 285.5 fm.
- The XENONnT exclusion plot also shows a bound from bulk heating in CUORE and astrophysical bounds (lunar thermal emission, white-dwarf cooling). We did not open those primary sources; see Unverified leads.

**Reading for the rollback model.** If "commit" were a physical event with a random kick, these bounds cap how often and how sharply the engine can commit ordinary matter. If the commit is pure bookkeeping, with no kick, the model predicts **no** side effects, and these experiments are silent on it. That is a real fork for the write-up: a perfect optimization leaves no heat.

---

## 4. Prior art for the "finite rollback window" test

### 4.1 What we found

**No source proposes a *maximum retrocausal span* or a *finite rollback buffer* as an experimental test**, whether in the simulation literature or in the retrocausality literature. The closest ideas bound a different finite resource:

1. **Finite *speed* of hidden influence (the spatial twin of our idea).**
   - **Salart, Baas, Branciard, Gisin & Zbinden 2008**, "Testing the speed of 'spooky action at a distance'", *Nature* 454, 861–864. doi:10.1038/nature07121. It drew a published comment (Kofler, Ursin, Brukner & Zeilinger, arXiv:0810.4452) and a reply (arXiv:0810.4607).
   - **Yin, Cao, Yong, Ren, Liang, Liao et al. 2013**, "Lower Bound on the Speed of Nonlocal Correlations without Locality and Measurement Choice Loopholes", *PRL* 110, 260407. doi:10.1103/PhysRevLett.110.260407 (arXiv:1303.0614). A 12-hour continuous Bell violation gives a lower bound of "four orders of magnitude of the speed of light", given their assumption about Earth's speed.
   - **Bancal, Pironio, Acín, Liang, Scarani & Gisin 2012**, "Quantum non-locality based on finite-speed causal influences leads to superluminal signalling", *Nat. Phys.* 8, 867–870. doi:10.1038/nphys2460. A theoretical no-go for finite-speed models.
   - *Relevance:* a finite-speed server sync is ruled out in much the same way a finite-*duration* rollback could be. Nobody has run the temporal version.
2. **Finite *collapse time* Tc (the collapse locality loophole).**
   - **Kent 2005**, "Causal quantum theory and the collapse locality loophole", *PRA* 72, 012107. doi:10.1103/PhysRevA.72.012107.
   - **Kent 2020**, "Stronger tests of the collapse locality loophole in Bell experiments", *PRA* 101, 012102. doi:10.1103/PhysRevA.101.012102 (arXiv:1807.08791). He notes that an Earth-diameter separation (≈ 40 ms × c) is feasible. Testing collapses tied to human perception, with reaction times of about 100–200 ms, would need a participant "at least ≈ 2–5 × 10⁴ km from Earth".
   - **Salart, Baas, van Houwelingen, Gisin & Zbinden 2008**, "Spacelike Separation in a Bell Test Assuming Gravitationally Induced Collapses", *PRL* 100, 220404. doi:10.1103/PhysRevLett.100.220404.
   - **Agüero, Bourdieu, Hnilo, Kovalsky, Nonaka et al. 2026**, "Test of the essential collapse-locality loophole" (arXiv:2603.24909, preprint).
   - *Relevance:* this is the closest conceptual neighbour. It asks whether a commit takes a finite time. Ours asks whether a commit can be *revised* only within a finite time. These are different quantities, but both are finite time parameters of the collapse process that experiments can bound.
3. **Timing-order tests.** **Stefanov, Zbinden, Gisin & Suarez 2002**, "Quantum Correlations with Spacelike Separated Beam Splitters in Motion: Experimental Test of Multisimultaneity", *PRL* 88, 120404. doi:10.1103/PhysRevLett.88.120404. This tested whether correlations depend on which measurement comes "first" in each detector's frame. They do not.
4. **Simulation-hypothesis tests.** **Beane, Davoudi & Savage 2014**, "Constraints on the universe as a numerical simulation", *Eur. Phys. J. A* 50, 148. doi:10.1140/epja/i2014-14148-0, looks for lattice-spacing artefacts in cosmic rays, a finite *spatial* resolution. Campbell et al. 2017 (already in `prior-art.md`) propose delayed-choice experiments under a "render when data becomes available" reading, but set no maximum delay.
5. **Ma et al. 2013** describe their 450 µs delay as a *record*, but give no hypothesis under which a longer delay could fail.

**Verdict:** the "finite rollback window" test, meaning an attempt to find a Δ_max beyond which delayed choice or delayed partner measurement stops reproducing quantum correlations, **appears unproposed** in the literature we could search. It shares its form with the finite-speed tests (1) and the collapse-locality tests (2). The write-up should credit those as its structural ancestors.

### 4.2 Searches run

The general web-search budget for this session ran out partway through. The later searches used the arXiv API, the Crossref API and the Hacker News Algolia API directly.

- Web search: "Ma 2013 PNAS quantum erasure causally disconnected choice Canary Islands 144 km"; "Vedovato 2017 Science Advances extending Wheeler's delayed-choice experiment to space"; "Ma 2012 Nature Physics experimental delayed-choice entanglement swapping delay fiber"; "Jacques 2007 Science … 48 m"; "Megidish 2013 PRL … never coexisted delay"; "delayed-choice quantum eraser quantum memory storage long delay"; "delayed-choice entanglement swapping quantum memory … 2019 2020 2021"; "Drmota 2023 PRL robust quantum memory …"; "atom-photon entanglement stored memory time record seconds … Bell violation after storage"; "Körber 2018 Nature Photonics …"; "'Long-lived remote ion–ion entanglement …' Nature 2026"; "entanglement stored hours quantum memory record 2025 2026"; "Kim Yu Kulik Shih Scully 2000 … 8 ns"; "delayed-choice experiment record longest delay after detection …".
- arXiv API (abstract search): `"simulation hypothesis" AND "delayed choice"` (0 hits); `"simulation hypothesis" AND retrocausal` (0); `retrocausal AND "delayed choice" AND delay AND limit` (1 hit, unrelated: Parrochia 2019); `"delayed choice" AND "arbitrarily long"` (0); `"simulation hypothesis" AND test AND quantum` (0); `retrocausality AND "time scale" AND bound` (0); `"delayed choice" AND "quantum memory" AND delay` (3 hits: Ohwada 2025 proposal, a sneakernet resource estimate, room-temperature ensembles, none about a maximum delay); `"collapse model" AND (bound OR bounds OR constraint)`, sorted by date (40 most recent, screened); `ti:"collapse locality loophole"`; `ti:"speed of spooky action"`.
- Hacker News (Algolia, comments): "delayed choice rollback", "quantum eraser rollback", "delayed choice buffer simulation", "retrocausal buffer", "delayed choice lag compensation", "quantum eraser netcode", "simulation delayed choice how long delay". We then pulled about 200 comments for "delayed choice quantum eraser simulation", "quantum eraser simulation" and "delayed choice simulation" and screened them for rollback, rewind, buffer, lag compensation, netcode or window. **No relevant hits.**

---

## 5. Unverified leads

- **Dong et al. 2020**, "Temporal Wheeler's delayed-choice experiment based on cold atomic quantum memory", *npj Quantum Inf.* 6, 72, doi:10.1038/s41534-020-00301-1. The metadata is verified. A search-engine snippet said atomic excitations were retrieved "750 nanoseconds after" creation, but we could not confirm the delay in the paper.
- **Liu et al. 2026**, *Nature* 652, 51–57 (ion–ion entanglement over 10 km of fibre). We could not read the storage duration or post-storage fidelity (paywalled). This may beat 10 s if one node is measured well before the other.
- **Xu et al. 2025** (arXiv:2507.13320). A two-ion entangled logical qubit with more than two hours of coherence. It is a preprint, and we did not check its journal status. It is not a Δ bound (see §1.5).
- **IGEX data in the early CSL X-ray bounds.** Collett et al. 1995 and Pearle et al. 1999 have IGEX-affiliated co-authors (Avignone, Collar), but we did not confirm that IGEX data specifically were used, and we did not read their numerical bounds.
- **CUORE bulk-heating bound and astrophysical bounds** (lunar thermal emission, cooling of the white dwarf J1251+4403). These appear in the XENONnT exclusion figure; we did not open the primary sources.
- **The Kovachy et al. 2015 separation.** We verified "half-metre scale" from the title. We did not read the exact separation in cm in the paper.
- **Longer-lived photon–matter entanglement.** Examples include SiV or NV nuclear-spin registers and rare-earth memories storing one half of a pair for longer than 10 s. These were not searched exhaustively, and a longer verified Δ may exist.
- **Stas et al. 2022**, "Robust multi-qubit quantum network node with integrated error detection" (*Science*). A possible long-storage electron–photon entanglement result; not checked.
