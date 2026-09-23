# Experiments 003 and 005, and ROADMAP Batch E: fact check and prior-art pass

*Compiled 2026-09-23. Scope: every item marked "(verify)" in `experiments/003-when-does-it-decide/README.md`,
`experiments/005-catching-the-engine/README.md` and `thesis/report/ROADMAP.md` (Batch E), plus five prior-art
questions. Nothing here claims that we live in a simulation.*

**How we checked.** WebSearch was not used because the session budget was exhausted. Every citation was
checked against at least one primary record: the arXiv API (`https://export.arxiv.org/api/query`), Crossref DOI
metadata, OpenAlex, PubMed/PMC, or the publisher's page. We read quoted numbers in the source text (the arXiv
PDF via `pdftotext`, the PMC full text, or the abstract) and give their location. Numbers we computed
ourselves are marked **(our arithmetic)**, with their inputs. We computed cosmological times with
`astropy.cosmology.Planck18`. Tags: [PHYS] established physics, [ANALOGY] a CS/engine mapping, [SPEC]
speculation.

---

## 1. Checklist

| # | claim (where) | verdict | source |
|---|---|---|---|
| 1a | Quasar light "still interferes between separate telescopes" after travelling for billions of years (003 §2, 005 T2) | **confirmed**, and a stronger example exists | GRAVITY Collab. 2018 *Nature* 563, 657 (3C 273); GRAVITY+ 2024 *Nature* 627, 281 (J0920, z = 2.325, ~11 Gyr) |
| 1b | "≥ ~7.6×10¹⁶ s (~2.4 billion years)" for that quasar light (003 §2, `sims/pending_state.py` line 76) | **corrected**: 3C 273 is at z = 0.158, so the light-travel time is **≈ 2.0 Gyr ≈ 6.4×10¹⁶ s**. The best current example gives ≈ 11 Gyr ≈ 3.5×10¹⁷ s | GRAVITY 2018 (z = 0.158, "550 mega-parsecs"); Planck18 lookback (our arithmetic) |
| 1c | "A timeout shorter than the flight time would wipe out that interference" (003) | **needs a caveat**: this is true only for a timeout that commits the photon's *path or landing point* (which telescope). A timeout that commits its *position* along the way would not remove the fringes (van Cittert–Zernike) | §2.1 below |
| 1d | "≥ 10 s (entangled ion–photon in memory)" (003, 005 T2) | **confirmed** | Drmota et al. 2023 *PRL* 130, 090803: fidelity 0.81(4) after 10 s |
| 2a | Fundamental time step bound (Wendel, Martínez & Bojowald 2020 PRL) (005 T1) | **confirmed**, with a caveat: T_C < 10⁻³³ s, and the bound depends on the model | *PRL* 124, 241301 (2020) |
| 2b | Detector timing jitter is "ps scale" (005 T1) | **confirmed** | Korzh et al. 2020 *Nat. Photon.* 14, 250: 2.7 ± 0.2 ps (400 nm), 4.6 ± 0.2 ps (1550 nm) |
| 3a | GPS.DM, Roberts et al. 2017 (005 T6) | **confirmed**, but the wording needs a caveat (a *global* stall can't be detected) | *Nat. Commun.* 8, 1195 (2017) |
| 3b | Optical clock network searches, Wcisło et al. | **confirmed** | *Nat. Astron.* 1, 0009 (2016); *Sci. Adv.* 4, eaau4869 (2018) |
| 4 | "No preferred frame to ~10⁻¹⁸ (Nagel 2015)" (005 T4) | **corrected**: 10⁻¹⁸ bounds the **orientation** dependence of light speed. The **boost** (velocity, preferred-frame) coefficients in the same paper are bounded at the **~10⁻¹⁴** level | *Nat. Commun.* 6, 8174 (2015), Table 1 |
| 5 | Fine-structure constant: "contested dipole claims (Webb et al.)" (005 T8) | **confirmed**; status summarised in §2.5 | Webb 2011 *PRL* 107, 191101; King 2012 *MNRAS*; Whitmore & Murphy 2015; Wilczynska 2020; Murphy 2022 |
| 6a | "QRNGs pass standard test batteries; no finite test proves true randomness" (005 T9) | **confirmed** | Herrero-Collantes & Garcia-Escartin 2017 *RMP* 89, 015004, §XII |
| 6b | Randomness certified by Bell tests (Pironio 2010) | **confirmed**, with a caveat: certification assumes no superdeterminism, and a simulator that sets the measurement settings breaks exactly that assumption | *Nature* 464, 1021 (2010); Acín & Masanes 2016 *Nature* 540, 213 |
| 7a | Quantum inequalities, "borrow then repay quickly" (Ford & Roman) (Batch E) | **confirmed**; "quantum interest" is the exact term | Ford & Roman 1995 *PRD* 51, 4277; 1997 *PRD* 55, 2082; 1999 *PRD* 60, 104018 |
| 7b | ALPHA-g 2023: antimatter "falls down" | **confirmed**: a = (0.75 ± 0.13 ± 0.16) g, and repulsion is ruled out | Anderson et al. 2023 *Nature* 621, 716 |
| 7c | "Antimatter has positive mass" (attributed to ALPHA-g) | **reword**: ALPHA-g measures the gravitational acceleration, not the "mass sign". Say "falls down" | §2.7 |
| 7d | Bullet Cluster lensing mass offset from gas (Clowe et al. 2006) | **confirmed**: an 8σ offset | *ApJ* 648, L109 (2006) |
| 7e | Sakharov conditions (1967); "the known CP violation is too small" | **confirmed** | Sakharov, JETP Lett. 5, 24 (1967), reprinted Sov. Phys. Usp. 34, 392 (1991); Canetti, Drewes & Shaposhnikov 2012 *NJP* 14, 095012 |

---

## 2. Details

### 2.1 Quasar interferometry after cosmological travel (003; 005 T2)

**Verified sources**

- [PHYS] GRAVITY Collaboration (Sturm, E., Dexter, J., Pfuhl, O. et al.) 2018, "Spatially resolved rotation of
  the broad-line region of a quasar at sub-parsec scale", *Nature* 563, 657–660. doi:10.1038/s41586-018-0731-9,
  arXiv:1811.11195. From the text: GRAVITY at the VLTI "coherently combines the light of the four 8 m telescopes
  to form interferometric amplitudes and phases on each of the 6 baselines". The observations are of the
  redshifted Paschen-α line at λ ≈ 2.17 µm (**near-IR K band**, so not optical). The source is at "z = 0.158 (550
  mega-parsecs)". It gives "a spatial resolution of ten micro-arcseconds" via **differential phase**
  (spectro-astrometry), and "the continuum dust emission was partially resolved (diameter ~0.3
  milli-arcseconds)".
- [PHYS] GRAVITY Collaboration (Abuter, R. et al.) 2024, "A dynamical measure of the black hole mass in a
  quasar 11 billion years ago", *Nature* 627, 281–285. doi:10.1038/s41586-024-07053-4, arXiv:2401.14567.
  The source is SDSS J092034.17+065718.0 at z = 2.325, observed with GRAVITY+. Differential phases are
  measured on all six baselines, with a 40 µas offset between the red and blue photocentres. The authors quote a
  look-back time of 11 billion years.
- [PHYS] **Older, single-aperture version of the same argument:** Lieu, R. & Hillman, L. W. 2003, "The phase
  coherence of light from extragalactic sources: direct evidence against first-order Planck-scale fluctuations
  in time and space", *ApJ* 585, L77. doi:10.1086/374350, arXiv:astro-ph/0301184. They use HST Airy rings of
  PKS 1413+135, "located at a distance of 1.2 Gpc". Also Ragazzoni, Turatto & Gaessler 2003, *ApJ* 587, L1
  (doi:10.1086/375046), who use SN 1994D and an HDF galaxy at z = 5.34. Perlman et al. 2015, *ApJ* 805, 10
  (doi:10.1088/0004-637X/805/1/10) reassess this approach for spacetime foam. **This is prior art for our
  "timeout" bound:** people have used the survival of phase coherence over cosmological paths to bound
  decoherence-like new physics since 2003.

**Numbers (our arithmetic, astropy Planck18)**

| source | z | light-travel (look-back) time |
|---|---|---|
| 3C 273 | 0.158 | **2.04 Gyr = 6.4×10¹⁶ s** (not 2.4 Gyr / 7.6×10¹⁶ s) |
| J0920 (GRAVITY+) | 2.325 | **10.97 Gyr = 3.5×10¹⁷ s** |
| HDF galaxy (Ragazzoni) | 5.34 | 12.7 Gyr |

Where the "2.4" likely came from: 3C 273's comoving distance is ≈ 2.2 Gly and its luminosity distance is
≈ 780 Mpc ≈ 2.5 Gly. Neither is the travel time.

**What "interference" means here**

- The measurement is amplitude (Michelson) interferometry. Light collected by separate 8 m telescopes, tens to
  ~130 m apart, is combined coherently. The fringe amplitude (visibility) and phase depend on the source's
  angular structure. The quasar is almost unresolved on these baselines, so the fringes are high-visibility. The
  science signal is a tiny phase shift between wavelengths.
- **Photon regime (our arithmetic, order of magnitude):** assume K ≈ 10 mag (our assumption for 3C 273; not
  checked), a K-band zero point of ≈ 4.5×10⁻¹⁰ W m⁻² µm⁻¹, a 50 m² collecting area and a 0.0044 µm spectral
  channel. That gives ~10⁵ photons/s, with a coherence time of λ²/(cΔλ) ≈ 3.7 ps, so ≈ **4×10⁻⁷ photons per
  coherence time**. This is deep in the single-photon regime. Each detected photon's contribution to the fringe
  comes from its own amplitude arriving via both telescopes. So the path superposition across the baseline is a
  **single-photon** property, not a many-photon wave effect.
- **Caveat 1 (van Cittert–Zernike).** The source is spatially *incoherent*. The coherence across the baseline
  **builds up during propagation**: a source of size w at distance D gives a coherence width ≈ λD/w at Earth.
  So the fringes don't show that the photon kept a coherent phase *relative to other photons*. They show that
  each photon's wavefront stayed coherent over ≈ 100 m at arrival, and that nothing along the way recorded
  *which telescope* it would reach.
- **Caveat 2 (what kind of timeout is ruled out).** A "force-commit" that fixed the photon's **landing point**
  (which telescope, or a direction finer than ~λ/B ≈ 3.5 mas for B = 130 m) before arrival would destroy the
  fringes. That is excluded. A force-commit that only localised the photon's **position** somewhere along its path
  would *not* destroy them. The photon would re-expand from the commit point, which then acts as a new, tiny
  source. At D ≈ 1 Gly, localising to anything smaller than λD/B ≈ 5 pc still leaves full visibility (our
  arithmetic). So the bound applies to the *path/direction* degree of freedom, which is the one 003 calls
  "pending".
- **Fair inference?** Yes for "whatever the photon's path superposition across the telescopes is, it was not
  committed or recorded during ~2 Gyr (3C 273), or ~11 Gyr (J0920) of flight". No for "any timeout of any kind
  on pending state must be ≥ billions of years".

**Corrected wording for 003 §2 (timeout bullet):**
> [SIM/PHYS] Lower bounds on any "force-commit after T" rule: ≥ 10 s (an entangled ion–photon pair kept in
> memory; Drmota et al. 2023), and **≥ ~6×10¹⁶ s (~2 billion years)** from quasar 3C 273, whose near-infrared light
> still forms interference fringes between the four 8 m VLT telescopes (GRAVITY Collaboration 2018). GRAVITY+
> has since done the same for a quasar whose light travelled **~11 billion years** (≈3.5×10¹⁷ s; GRAVITY
> Collaboration 2024). The light arrives roughly one photon at a time, so each photon's path across the telescopes
> stays undecided for the whole trip. Caveat: this rules out a timeout that commits *which way the photon goes*.
> A timeout that only pins down *where it is* along the way would not erase the fringes.

**Corrected wording for 003 scoreboard:** `⚠️ bound | Any timeout that commits an isolated photon's path must be
≥ ~2 Gyr (3C 273) or ≥ ~11 Gyr (GRAVITY+ 2024) | [PHYS]`, with "(verify)" removed.
**005 T2:** `≥ 10 s (ion–photon memory, Drmota 2023); ≥ ~10¹⁰ yr for the path state of isolated photons (GRAVITY+ 2024)`.
**`sims/pending_state.py` line 76:** change `2.4e9 * YEAR` → `2.0e9 * YEAR` ("3C 273, z = 0.158"), or use
`1.1e10 * YEAR` (J0920).

### 2.2 Fundamental time step and detector jitter (005 T1)

- [PHYS] Wendel, G., Martínez, L. & Bojowald, M. 2020, "Physical implications of a fundamental period of time",
  *PRL* 124, 241301. doi:10.1103/PhysRevLett.124.241301, arXiv:2005.11572. Abstract: "A strong upper bound
  T_C < 10⁻³³ s of the fundamental period of time, several orders of magnitude below any direct time
  measurement". The derivation (p. 5) models time as a fundamental oscillator coupled to every evolving system.
  It uses atomic-clock precision σ ≈ 10⁻¹⁹ at a system period T_S ≈ 2 fs (the Sr 698 nm line). **Caveat:** the
  bound is **model-dependent**, since it assumes their specific coupling. The authors call it indirect.
- [PHYS] Korzh, B. A. et al. 2020, "Demonstration of sub-3 ps temporal resolution with a superconducting
  nanowire single-photon detector", *Nat. Photon.* 14, 250–255. doi:10.1038/s41566-020-0589-x,
  arXiv:1804.06839. The resolution is 2.7 ± 0.2 ps at 400 nm and 4.6 ± 0.2 ps at 1550 nm (a FWHM-type
  figure). The earlier state of the art was "below 15 ps".
- **Our arithmetic:** the sim's jitter is a Gaussian σ, and FWHM 2.7 ps corresponds to σ ≈ 1.15 ps. The sim's
  5σ threshold of 2.2σ therefore corresponds to direct sensitivity to ticks of **≳ 2.5 ps**. This is 21 orders of
  magnitude above the model-dependent indirect bound.

**Corrected wording for 005 T1 (bound column):** `direct test reaches ticks ≳ ~2.5 ps (2.2× the ~1 ps timing
jitter of the best SNSPDs, Korzh et al. 2020); an indirect, model-dependent bound is T < 10⁻³³ s (Wendel,
Martínez & Bojowald 2020, PRL)`.

### 2.3 Correlated clock glitches (005 T6)

- [PHYS] Roberts, B. M., Blewitt, G., Dailey, C., Murphy, M. et al. 2017, "Search for domain wall dark matter with
  atomic clocks on board global positioning system satellites", *Nat. Commun.* 8, 1195.
  doi:10.1038/s41467-017-01440-4, arXiv:1704.06844. They mined "16 years of archival GPS data" for clock glitches
  "that propagate through the GPS satellite constellation at galactic velocities ~300 km/s" and found "no
  evidence".
- [PHYS] Wcisło, P. et al. 2016, "Experimental constraint on dark matter detection with optical atomic clocks",
  *Nat. Astron.* 1, 0009. doi:10.1038/s41550-016-0009.
- [PHYS] Wcisło, P. et al. 2018, "New bounds on dark matter coupling from a global network of optical atomic
  clocks", *Sci. Adv.* 4, eaau4869. doi:10.1126/sciadv.aau4869, arXiv:1806.04762. The network used Yb and Sr
  clocks "at four laboratories on three continents" and reports "a two orders of magnitude improvement in
  constraints on transient variations of the fine-structure constant".
- **Important caveat for the analogy.** These searches look for a glitch that sweeps **across** the network at a
  finite speed, or that hits clocks of different sensitivity differently. A **global** host stall that froze
  every clock and every process together would be undetectable from inside: every comparison would still agree.
  Only a *local* or *propagating* stall leaves a signature.

**Corrected wording for 005 T6 (signature and bound):** `a glitch that sweeps across a network of atomic clocks
(a global stall that freezes everything at once would be invisible from inside) | GPS and optical-clock networks
already search for such sweeping glitches, from dark-matter "domain walls": none seen (Roberts et al. 2017;
Wcisło et al. 2016, 2018)`.

### 2.4 Lorentz invariance "~10⁻¹⁸" (005 T4)

- [PHYS] Nagel, M., Parker, S. R., Kovalchuk, E. V., Stanwix, P. L. et al. 2015, "Direct terrestrial test of
  Lorentz symmetry in electrodynamics to 10⁻¹⁸", *Nat. Commun.* 6, 8174. doi:10.1038/ncomms8174,
  arXiv:1412.6954. They constrain "orientation-dependent relative frequency changes Δν/ν to 9.2 ± 10.7×10⁻¹⁹
  (95% confidence interval)". Table 1 caption: "Values for κ̃e− are given in 10⁻¹⁸, κ̃o+ in 10⁻¹⁴ and κ̃tr in
  10⁻¹⁰". Here κ̃e− are the **rotation/orientation** anisotropies, κ̃o+ the **boost** (velocity-dependent)
  terms, and κ̃tr the isotropic shift. Boost sensitivity is suppressed by Earth's orbital speed (β ≈ 10⁻⁴).
- So "no preferred frame to 10⁻¹⁸" overstates the result. A preferred *rest frame* shows up through boost terms,
  which are bounded at ~10⁻¹⁴ in this experiment.

**Corrected wording for 005 T4 (bound column):** `light speed doesn't depend on direction to ~10⁻¹⁸, and
doesn't depend on our velocity (boost terms) to ~10⁻¹⁴ (Nagel et al. 2015, photon sector)`.

### 2.5 Fine-structure constant spatial variation (005 T8): current status

- [PHYS] Webb, J. K., King, J. A., Murphy, M. T., Flambaum, V. V. et al. 2011, "Indications of a spatial variation
  of the fine structure constant", *PRL* 107, 191101. doi:10.1103/PhysRevLett.107.191101, arXiv:1008.3907.
  The Keck and VLT data combined fit "a spatial dipole, significant at the 4.2-sigma level", and the paper says
  "the pattern could be due to as yet undetected systematic effects". The full analysis is King et al. 2012,
  *MNRAS* 422, 3370 (doi:10.1111/j.1365-2966.2012.20852.x).
- [PHYS] Whitmore, J. B. & Murphy, M. T. 2015, "Impact of instrumental systematic errors on fine-structure
  constant measurements with quasar spectra", *MNRAS* (doi:10.1093/mnras/stu2420, arXiv:1409.4467).
  Wavelength-scale distortions are "ubiquitous and substantial", and the spurious Δα/α they produce "closely
  match important aspects of the VLT–UVES quasar results".
- [PHYS] Wilczynska, M. R., Webb, J. K. et al. 2020, "Four direct measurements of the fine-structure constant 13
  billion years ago", *Sci. Adv.* 6, eaay9672. doi:10.1126/sciadv.aay9672, arXiv:2003.07627. At z = 5.5–7.1 they
  find Δα/α = (−2.18 ± 7.27)×10⁻⁵, meaning "no evidence for a temporal change". Combined with earlier data, a
  spatial variation is "marginally preferred … at the 3.7 sigma level". This comes from the same group.
- [PHYS] Murphy, M. T., Molaro, P. et al. 2022, "Fundamental physics with ESPRESSO: Precise limit on variations in
  the fine-structure constant towards the bright quasar HE 0515−4414", *A&A* 658, A123.
  doi:10.1051/0004-6361/202142257, arXiv:2112.05819. They measure Δα/α = 1.3 ± 1.3 (stat) ± 0.4 (sys) ppm, with
  a laser-frequency-comb calibration that "effectively removed wavelength calibration errors".
- [PHYS] Milaković, D. 2023 (arXiv:2310.01071, conference review): the ~300-measurement sample "provides hints …
  in a form of a spatial dipole … although systematic effects could dominate", and new instruments and methods
  "promise" a systematics-free test.
- **Status (our summary):** there is no accepted detection. The dipole (~4σ in 2011, 3.7σ in 2020) comes from
  one group's combined sample, and calibration systematics can mimic it. The cleanest modern single-sight-line
  measurements (ESPRESSO, ppm level) agree with no variation. The dipole is still open, but it counts as
  "tentative and widely attributed to systematics", not as evidence.

**Corrected wording for 005 T8 (bound column):** `searches for spatial variation of the fine-structure constant: a
tentative ~4σ dipole (Webb et al. 2011) that is widely suspected to be calibration systematics (Whitmore &
Murphy 2015); modern laser-comb measurements find no change at the ppm level (Murphy et al. 2022)`.

### 2.6 Quantum randomness testing (005 T9)

- [PHYS] Herrero-Collantes, M. & Garcia-Escartin, J. C. 2017, "Quantum random number generators", *Rev. Mod.
  Phys.* 89, 015004. doi:10.1103/RevModPhys.89.015004, arXiv:1604.03304. §XII: "there is no way to check a
  finite sequence is truly random … Apart from the uncomputable Kolmogorov complexity … there is no way to deduce
  that a random string is really random, but there are methods to detect suspicious sequences". The standard
  suites are NIST SP 800-22, TestU01 and DieHard/DieHarder.
- [PHYS] Pironio, S., Acín, A., Massar, S., Boyer de la Giroday, A. et al. 2010, "Random numbers certified by
  Bell's theorem", *Nature* 464, 1021. doi:10.1038/nature09008, arXiv:0911.3427. They used two entangled atoms
  about 1 m apart, and the Bell violation "guarantees that 42 new random numbers are generated with 99%
  confidence".
- [PHYS] Acín, A. & Masanes, Ll. 2016, "Certified randomness in quantum physics", *Nature* 540, 213–219.
  doi:10.1038/nature20119, arXiv:1708.00265. Two key passages. First, the "memory-stick attack": pre-generated
  numbers "will pass any statistical test and look random" but are predictable. Second, "the generation of
  randomness from scratch is impossible. This follows from the unfalsifiable hypothesis of the existence of a
  super-deterministic model in which everything … was pre-determined in advance". Device-independent protocols
  also need an initial random seed for the measurement settings.
- **Relevance:** a simulator that generates the measurement *settings* as well as the outcomes is exactly the
  superdeterministic case. So even Bell-certified randomness cannot exclude a host PRNG. It excludes a PRNG
  that is *independent of* the setting choices. T9 can only catch a *bad* PRNG.

**Corrected wording for 005 T9 (bound column):** `QRNGs pass the standard NIST/TestU01/DieHarder batteries; no
finite test can prove a sequence random (Herrero-Collantes & Garcia-Escartin 2017). Bell tests can certify
randomness (Pironio et al. 2010), but only if the measurement settings are independent of the source, and an
engine that sets both breaks that assumption (Acín & Masanes 2016)`.

### 2.7 Batch E

**Negative energy / quantum inequalities.**
- [PHYS] Ford, L. H. & Roman, T. A. 1995, "Averaged energy conditions and quantum inequalities", *PRD* 51,
  4277. doi:10.1103/PhysRevD.51.4277 (gr-qc/9410043).
- [PHYS] Ford & Roman 1997, "Restrictions on negative energy density in flat spacetime", *PRD* 55, 2082.
  doi:10.1103/PhysRevD.55.2082 (gr-qc/9607003). This is "an uncertainty principle-type limitation on the
  magnitude and duration of the negative energy density".
- [PHYS] Ford & Roman 1999, "The quantum interest conjecture", *PRD* 60, 104018. doi:10.1103/PhysRevD.60.104018
  (gr-qc/9901074). "A pulse of negative energy must not only be followed by a compensating pulse of positive
  energy, but … the temporal separation between the pulses is inversely proportional to their amplitude … a
  positive energy pulse must overcompensate". **The ROADMAP's "borrow, then repay quickly" is the authors' own
  "quantum interest" framing, so cite it.**
- Also: Ford 1978, *Proc. R. Soc. A* 364, 227 (doi:10.1098/rspa.1978.0197), the origin of the idea. Ford & Roman
  1996, *PRD* 53, 5496 (doi:10.1103/PhysRevD.53.5496) applies quantum inequalities to wormholes, which links to
  Batch A.

**Antimatter.**
- [PHYS] Anderson, E. K. et al. (ALPHA-g) 2023, "Observation of the effect of gravity on the motion of
  antimatter", *Nature* 621, 716–722. doi:10.1038/s41586-023-06527-1 (PMC10533407). "Repulsive 'antigravity' is
  ruled out in this case". The local acceleration is "(0.75 ± 0.13 (statistical + systematic) ± 0.16
  (simulation)) g", which is "consistent with a downward gravitational acceleration of 1g".
- **Wording:** ALPHA-g shows antihydrogen *falls down*. "Positive mass" is true, from standard QFT and pair
  production energetics, but it isn't what ALPHA-g measured.
- **Physics caveat for the "sign bits" analogy (ours, standard physics):** charge conjugation C alone is *not* an
  exact symmetry, because weak interactions violate C and CP. The exact mirror is CPT. So "the same class with
  charge fields negated" is a fair first picture, but the true exact partner also flips parity and time.

**Dark matter / Bullet Cluster.**
- [PHYS] Clowe, D., Bradač, M., Gonzalez, A. H., Markevitch, M. et al. 2006, "A direct empirical proof of the
  existence of dark matter", *ApJ* 648, L109–L113. doi:10.1086/508162, astro-ph/0608407. The cluster is 1E0657-558
  at z = 0.296. There is "an 8-sigma significance spatial offset of the center of the total mass from the center
  of the baryonic mass peaks", and the potential "approximately traces the distribution of galaxies".

**Matter–antimatter asymmetry.**
- [PHYS] Sakharov, A. D. 1967, *Pisma ZhETF* 5, 32 [*JETP Lett.* 5, 24], reprinted in *Sov. Phys. Usp.* 34,
  392–393 (1991), doi:10.1070/PU1991v034n05ABEH002497. We verified the reprint on ufn.ru. The original journal
  pages come from Canetti et al.'s reference list; the 1967 scan itself was not checked.
- [PHYS] Canetti, L., Drewes, M. & Shaposhnikov, M. 2012, "Matter and antimatter in the universe", *New J. Phys.*
  14, 095012. doi:10.1088/1367-2630/14/9/095012, arXiv:1204.4186. §I: the SM "in principle fulfills all three
  Sakharov conditions … [but] the values of the CP-violating Kobayashi-Maskawa phase and mass of the Higgs
  particle … make it extremely unlikely that successful baryogenesis is possible within the SM. The CP violation
  and deviation from equilibrium during electroweak symmetry breaking are both too small." Conclusion: the
  asymmetry (~10⁻¹⁰) "cannot be explained within the Standard Model".

**Corrected wording for ROADMAP Batch E:**
- Negative energy row: `(Ford & Roman 1995, 1997; their "quantum interest" result, 1999: the negative pulse must
  be repaid, with interest, sooner the larger it is)`.
- Antimatter row: `antimatter is **not** negative energy: it falls *down* like matter (ALPHA-g 2023, Nature:
  0.75 ± 0.13 ± 0.16 g; repulsion ruled out). It is matter with its **charges flipped** (exactly: its CPT
  mirror)`, and in the open-question cell: `(… the Standard Model's CP violation and departure from equilibrium
  are both too small; Canetti, Drewes & Shaposhnikov 2012; Sakharov conditions 1967)`.
- Dark matter row: `(Clowe et al. 2006, ApJ 648 L109: 8σ offset)`.

---

## 3. Prior art

| question | verdict | closest hits |
|---|---|---|
| (a) tick / same-tick batching in quantum-event timestamps as a simulation test | **no direct hit found** | Campbell et al. 2017 (simulation tests, but "render on observation", not ticks); Wendel et al. 2020 (indirect time-step bound); Khrennikov & Volovich 2003 (a "time quant" conjecture, theory only) |
| (b) dark matter as uncollapsed branches / hidden computation | **anticipated** (physics: Mensky 2011, Weingarten 2023/2025; simulation framing: fringe preprints) | Mensky arXiv:1105.3696; Weingarten *Found. Phys.* 55, 55 (2025); Martila 2021 viXra; counterpoint Page & Geilker 1981 |
| (c) antimatter as "sign bit" / charge-conjugate instance | **no hit found** as a simulation analogy (only fringe Zenodo noise) | physics anchors: CPT; Feynman–Stueckelberg (not re-verified here) |
| (d) decoherence as replication/commit | **partly anticipated**: "redundancy" and "consensus" are standard quantum-Darwinism vocabulary; the explicit "commit" wording appears only in a 2026 non-peer-reviewed Zenodo preprint | Zurek 2009 *Nat. Phys.* 5, 181; Chisholm, Innocenti & Palma 2023 *Quantum* 7, 1074; Lund 2026 Zenodo |
| (e) entanglement as a future/promise | **informal only**: "lazy evaluation" analogies are common on HN; "promise/future" specifically not found. The physics anchor is Toner & Bacon 2003 | HN 2015 item 10431947, 2024 item 41725523; Toner & Bacon *PRL* 91, 187904 |

### (a) Same-tick batching
Queries: arXiv `abs:"simulation hypothesis" AND abs:test`; `abs:"discrete time" AND abs:"simulation hypothesis"`
(0 hits); `abs:"time discreteness" AND (abs:experiment OR abs:bound)` (hits are numerical analysis, plus
Khrennikov & Volovich 2003, quant-ph/0309012); `abs:chronon AND abs:experimental`; `abs:"simulated universe" AND
(abs:test OR abs:signature)`. OpenAlex `"simulation hypothesis" test experiment`; title filter `simulation
hypothesis + time`; `discrete time periodicity photon detection timestamps Planck test`. HN `simulation tick
quantum events timestamps` (0), `planck time tick simulation detect` (0).
- Campbell, T., Owhadi, H., Sauvageau, J. & Watkinson, D. 2017, "On testing the simulation theory",
  arXiv:1703.00058 (preprint). It proposes wave/particle experiments built on "render only when observed by a
  player", not timestamp combs.
- Verdict: **folding timestamps of independent quantum events on a candidate tick, and looking for excess exact
  coincidences between unrelated detectors, was not found as a published simulation test.** Treat it as novel
  in framing only, since timestamp-periodicity analysis itself is standard. It needs to cite Wendel et al.
  (indirect, far tighter) and Beane et al. 2014 (already in batch-BCD).

### (b) Dark matter as uncollapsed branches / hidden computation
Queries: OpenAlex title filters `dark matter + many worlds` (only junk), `dark matter + parallel universe`,
`dark matter + simulation hypothesis`, `dark matter + everett`; abstract filters `everett branches + dark matter`,
`many-worlds + dark matter`, `simulation hypothesis + dark matter`. arXiv `abs:"many-worlds" AND abs:"dark
matter"` (6 hits). HN `dark matter simulation hidden computation`, `dark matter uncollapsed branches` (0),
`"simulation" "dark matter" "many worlds"` (0).
- **Mensky, M. B. 2011**, "Phenomenology of 'dark matter' from the Everett's quantum cosmology",
  arXiv:1105.3696. We found no journal record via Crossref. It argues that semiclassical Everett-type gravity
  makes matter in the other "alternative realities (Everett's worlds) which remain «invisible»" act as dark
  matter. **This is the direct physics precedent for "uncollected pending state gravitates".**
- **Weingarten, D. 2023/2025**, "Vacuum Branching, Dark Energy, Dark Matter", *Found. Phys.* 55, 55.
  doi:10.1007/s10701-025-00864-z, arXiv:2308.05569. Vacuum branches with "no observable particle content" would
  appear as "a combination of dark energy and dark matter densities".
- Martila, D. 2021, "Simulation Hypothesis and Dark Matter", viXra 2103.0133. Abstract: "Dark Matter is presented
  as a consequence of the hypothesis of simulation, in particular of augmented reality (AR)". This is not peer
  reviewed.
- HN comment 2025-12-29 (item 46427673): "Gravity = computational lag … Dark matter = hidden (emergent)
  complexity". This is an informal precedent for both Episode 2's "gravity as lag" and dark matter as hidden
  compute.
- Nikolić, H. 2017, "Interpretation miniatures", *Int. J. Quantum Inf.* 15, 1740001 (arXiv:1703.08341). It
  compares Bohmian particles with dark matter (both detected only indirectly). This is a loose analogy only.
- **Counterpoint to cite:** Page, D. N. & Geilker, C. D. 1981, "Indirect Evidence for Quantum Gravity", *PRL* 47,
  979. doi:10.1103/PhysRevLett.47.979. Abstract (OpenAlex): "An experiment gave results inconsistent with the
  simplest alternative to quantum gravity, the semiclassical Einstein equations". In semiclassical gravity the
  *expectation value*, meaning all branches together, sources gravity. That is the mechanism "branches gravitate"
  needs, and this lab experiment disfavours it. We did not re-read the experimental setup details.
- Verdict: **anticipated.** The ROADMAP should say "dark matter as the gravity of other branches has been
  proposed (Mensky 2011; Weingarten 2025); the simplest version conflicts with Page & Geilker 1981; the
  simulation framing appears only in non-peer-reviewed sources".

### (c) Antimatter as a sign bit
Queries: HN `antimatter "sign bit"` (0), `antimatter simulation negative flag` (0), `antimatter "negative"
simulation bit flip` (0). OpenAlex title filter `antimatter + simulation hypothesis` (0); abstract filter
`antimatter + sign bit` (14 hits, all unrelated or fringe 2026 Zenodo uploads).
Verdict: **no prior art found** for this specific analogy. Its physics must respect C/CP violation and CPT, as in
§2.7.

### (d) Decoherence as replication/commit
Queries: HN `decoherence commit replication` (0), `decoherence "eventual consistency"` (0), `quantum "eventual
consistency"` (4, none on point), `quantum darwinism consensus` (none on point). OpenAlex abstract filters
`quantum darwinism + consensus` (42), `decoherence + two-phase commit` (33, mostly noise).
- **Physics anchor:** Zurek, W. H. 2009, "Quantum Darwinism", *Nat. Phys.* 5, 181–188. doi:10.1038/nphys1202.
  Pointer-state information is copied redundantly into the environment, and observers read the copies.
- Chisholm, D. A., Innocenti, L. & Palma, G. M. 2023, "The meaning of redundancy and consensus in quantum
  objectivity", *Quantum* 7, 1074. doi:10.22331/q-2023-08-03-1074. "Redundancy" and "consensus" are already
  terms of the art, which is close to our "replicated to enough readers".
- Lund, T. P. 2026, "Race all the way down, race all the way up: a unifying vocabulary for bounded-commit dynamics
  …", Zenodo doi:10.5281/zenodo.20457814 (not peer reviewed). It explicitly frames decoherence and einselection
  as "one irreversible commit".
- Verdict: **partly anticipated.** Credit Zurek's quantum Darwinism as the physics this analogy redescribes. Our
  database-replication wording (a write committed once replicated to N readers) is a restatement of redundancy
  (R_δ), not new physics.

### (e) Entanglement as a future/promise
Queries: HN `entanglement promise future lazy` (0), `entanglement "promise" javascript` (0), `entanglement shared
pointer future` (0), `entanglement future async await` (0), `"quantum entanglement" "promise"` (3, not on point),
`entangled particles "lazy evaluation"` (1), `wavefunction collapse "lazy evaluation"` (7). OpenAlex abstract
filters `entanglement + lazy evaluation` (12, mostly 2026 Zenodo), `wavefunction collapse + lazy evaluation` (13),
title filter `quantum + futures and promises` (0).
- HN 2015-10-22 (item 10431947): "QM is like lazy evaluation. The result is not computed until someone actually
  forces it". HN 2024-10-02 (item 41725523): "observer effect, quantum entanglement and wavefunction collapse →
  lazy evaluation". Yamagishi 2026 (Zenodo doi:10.5281/zenodo.21413628, not peer reviewed): "Lazy Evaluation
  Objects".
- **Physics anchor:** Toner, B. F. & Bacon, D. 2003, "The communication cost of simulating Bell correlations", *PRL*
  91, 187904. doi:10.1103/PhysRevLett.91.187904. Local hidden variables "augmented by just one bit of classical
  communication" reproduce singlet correlations exactly. Our shared promise, "resolved using the first reader's
  angle", is such a model: the engine must pass the first setting (or its effect) to the other side. That is a
  nonlocal channel hidden from users, which is why S = 2.84 and no-signalling can coexist.
- Verdict: **the lazy-evaluation version is common informal prior art. "Promise/future" wording as such was not
  found.** Cite Toner & Bacon for why a shared future beats S = 2 (it carries hidden communication).

---

## 4. Other corrections to existing wording

- 003 §2 says "optical" implicitly ("quasar light … between separate telescopes"). GRAVITY works in the
  **near-infrared K band (~2.2 µm)**; say "near-infrared".
- 003 "Informal prior art: a 2013 HN comment compares entanglement to 'dereferencing a pointer'": we didn't
  re-check it in this pass, so it is still unverified. Add the verified 2015 and 2024 HN lazy-evaluation comments
  above.
- ROADMAP line 6 lists verified research files. Add this file.

## 5. Unverified leads

- K-band magnitude of 3C 273 (≈ 10 was assumed only for the photon-rate estimate) and the exact VLTI UT baseline
  range (~47–130 m). Not checked against ESO pages.
- Page & Geilker 1981 experimental setup (radioactive-decay-controlled source masses): from background knowledge.
  Only the abstract and metadata were verified.
- Ng, Christiansen & van Dam 2003 critique of Lieu & Hillman (*ApJ* 591, L87?): not checked.
- Feynman–Stueckelberg interpretation (antiparticles as particles moving backwards in time) as an anchor for (c):
  not checked.
- Mensky 2011: no peer-reviewed version found (Crossref query returned only other Mensky works).
- The 2013 HN "dereferencing a pointer" comment cited in 003.
- Later GPS.DM results (e.g. a 2022 "results of the search for topological dark matter using … GPS" talk,
  doi:10.26226/m.6275705c66d5dcf63a31159e): a conference abstract only, not read.
