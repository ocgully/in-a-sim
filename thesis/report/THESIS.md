# If the Universe Were a Program: An Engineering Reading of Physics

*A thought experiment in public. Working draft that grows with each experiment.*

---

## Abstract (living)

We ask a narrow, engineering-style question: **if our universe were computed, what design choices
would it reflect, and which measurements resemble those choices?** We don't try to decide whether
it *is* computed. Each chapter takes one observation, builds a runnable model from game-engine or
distributed-systems practice, sets the model against measured physics, and records a scoreboard of
fits, breaks and open questions. Verified prior art is credited throughout. The thesis ends with no
verdict, only a ledger of evidence.

## Framing

- **Why engineering, not philosophy.** Bostrom's trilemma (2003) and Chalmers' *Reality+* (2022)
  set the philosophical stage. They are summarised in the [literature survey](literature-survey.md).
  This thesis stays in the zone where claims can be *computed and compared*.
- **Rules of evidence.** See [METHODOLOGY](../../METHODOLOGY.md). Every claim is tagged
  [PHYS] / [CS] / [SIM] / [ANALOGY] / [SPEC] / [COUNTER].
- **The central caution.** A simulation that reproduces a phenomenon shows that a mechanism is
  *possible*. It does not show that nature *uses* it. Most of the fits below are "by construction",
  and we say so.

## Chapter 1: Collapse as Rollback ([Experiment 001](../../experiments/001-collapse-as-rollback/))

**Question.** Is quantum measurement like an authoritative game server resolving an event against a
past snapshot and committing it as the truth?

**Key results.**
- Lag compensation produces "retroactive truth" by design: death 223 ms after reaching cover [SIM].
- The delayed-choice eraser needs **no rewind**, only a joint record. The retroactive pattern lives
  only in the join of two logs, and the raw screen never changes (χ² 40.5 / 39 dof) [SIM].
- In the Bell test, pre-loaded answers cap at 2. A central server, a pre-scripted seed, and
  keep-every-branch all reach 2.83. The three big interpretations correspond to three engine
  architectures that can't be told apart from inside [SIM].
- Hosting cost: keep-every-branch doubles memory with each observation, while collapse behaves like
  garbage collection [SIM].

**Breaks.** Quantum branches interfere, and nature never shows an observer a contradiction.
**Open.** Why the Tsirelson cap (2√2)? Why amplitude-squared?
**Prior art.** Render-on-demand and server nonlocality are anticipated (Bostrom 2003; Campbell et al.
2017). We found no indexed source making the lag-compensation / rollback-netcode / Time Warp mapping.

## Chapter 2: Gravity as Compute Load ([Experiment 002](../../experiments/002-gravity-as-compute-load/))

**Question.** Is gravity what regional processing lag looks like from inside?

**Key results.**
- EVE Online's TiDi is a shipped precedent for load-driven regional time dilation [CS][SIM].
- A neighbour-averaging clock scheduler produces a 1/r lag field (Poisson). The shape is right, by construction [SIM].
- A clock-rate gradient alone makes matter fall at exactly g. That's textbook GR [SIM][PHYS].
- Lag alone gives **half** the measured light bending (0.876″ vs 1.751″). Space must also stretch [SIM][PHYS].

**Breaks.** The light-bending factor of 2, and gravity's indifference to complexity (equivalence principle).
**Open.** Why would compute cost be proportional to energy? (Candidate: mass is a clock, E = hf.)
**Prior art.** The core claim is anticipated (Whitworth 2008/2010; Alagoz 2010; Lee 2025). We found
no prior runnable models or quantitative confrontation with the measured constraints.

## Chapter N: *(future experiments, see [BACKLOG](BACKLOG.md))*

## Evidence ledger

The single table the final video and thesis conclusion are built from. Add a row per finding.

| # | exp | observation | type | fits / breaks / open | strength |
|---|---|---|---|---|---|
| 1 | 001 | Authoritative resolution against a past snapshot produces retroactive truth | [CS][SIM] | fits (analogy) | illustrative |
| 2 | 001 | Delayed-choice correlations appear only in the joined log; no rewind needed | [PHYS][SIM] | breaks "rollback", fits "joint record" | strong |
| 3 | 001 | Bell violation requires nonlocal state, a pre-scripted seed, or branching. All three are engine architectures | [PHYS][SIM] | fits | strong |
| 4 | 001 | Nature caps correlations at 2√2, though a no-signalling server could reach 4 | [PHYS][SIM] | open | strong |
| 5 | 001 | Keep-every-branch hosting cost grows 2ⁿ with observations; statistics are identical from inside | [SIM] | fits (if host is finite) | moderate |
| 6 | 001 | Quantum branches interfere; speculative game states don't | [PHYS] | breaks | strong |
| 7 | 002 | Load-driven regional time dilation is shipped in real MMOs | [CS] | fits (precedent) | illustrative |
| 8 | 002 | A neighbour-coupled load scheduler yields a 1/r lag field | [SIM] | fits (by construction) | weak–moderate |
| 9 | 002 | A tick-rate gradient alone reproduces free fall | [PHYS][SIM] | fits | strong (but it's standard GR) |
| 10 | 002 | Tick-rate lag alone gives half the measured light deflection | [PHYS][SIM] | breaks pure-lag | strong |
| 11 | 002 | Gravity couples to mass-energy only, not to complexity (~10⁻¹⁵) | [PHYS] | breaks naive load / open | strong |

## Conclusion

*Deliberately none.* The final section will present the ledger, group it by *fits / breaks / open*,
and list which future measurements could move any row.
