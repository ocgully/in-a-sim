# Roadmap: future exploration batches

Each batch becomes one or more experiments (`shared/new-experiment.sh NNN-slug "Title"`), each with sims, a
prior-art pass, a scoreboard and a Blender episode. Every item follows the project rule:
**observation → engine / CS concept → runnable model → the counterpoint it must survive.**
Facts marked (verify) came from background knowledge and need a citation pass before use.

---

## Batch A: "Moving through the map" (FTL, wormholes, warp drives, lensing)

The engine question: **if the speed limit is one cell per tick, what would *moving space itself* look like
in code?**

| topic | physics to respect | engine / CS concept | model idea | counterpoint to beat |
|---|---|---|---|---|
| **Warp drive** | Alcubierre metric (1994): space contracts ahead of a region and expands behind it, and the region rides the wave; it needs negative energy density (verify) | **Floating origin / world-scrolling.** Big-world games (e.g. Kerbal Space Program) keep the ship at the origin and move the *universe* around it to avoid float precision loss (verify KSP detail). Also "moving the map, not the player" | tile engine where cells are inserted behind and deleted in front of a bubble; the object's local motion stays sub-light while its map position moves faster than 1 cell/tick | negative-energy requirement; horizon problem (the bubble can't be steered from inside); whether the engine's own rules allow cell insertion faster than signals |
| **Wormholes** | Einstein–Rosen bridges; traversable ones need exotic matter (Morris–Thorne 1988) (verify) | **Portals / non-Euclidean level design.** In *Portal*, *Antichamber* and similar games a doorway is an edge in the level graph, not a straight line in space; also pointer aliasing | a grid world with an extra graph edge: shortest-path light cones, lensing through the throat | exotic matter; stability; ER = EPR (entanglement ↔ wormholes, Maldacena–Susskind 2013) as a surprising link back to Experiment 001 |
| **FTL and causality** | FTL signalling plus relativity lets you build a time machine (causality paradox) | **Race conditions and Lamport clocks.** Distributed systems forbid reading a message before it's sent. FTL = a message delivered before its send event in some frame, i.e. a causality violation. The speed limit acts as the engine's consistency guarantee | a distributed sim with vector clocks: allow one FTL channel, show the inconsistency it creates | Experiment 001 already shows nature hides its nonlocality perfectly (no signalling): the engine may be nonlocal internally, but it never lets you *use* that |
| **Gravitational lensing** | Einstein rings, multiple images, time delays between images (a real measurement for lensed quasars and supernovae) (verify) | refraction through slow tiles plus extra space (Experiment 002's 1:1 rule); **ray-marching through a variable-speed medium** | the tile engine renders an Einstein ring and a two-image time delay | already covered quantitatively; the new part is multiple images and image time delays |

## Batch B: "The universe's clock" (Big Bang, cosmic age, expansion)

The engine question: **the universe is "13.8 billion years old", but by what clock?**

| topic | physics to respect | engine / CS concept | model idea | counterpoint to beat |
|---|---|---|---|---|
| **By what clock?** | The 13.8 Gyr age is **cosmic time**: the proper time of a clock at rest relative to the cosmic background (comoving). Earth's clock runs very close to it (our motion and local gravity barely shift it) | **Global tick counter vs each region's local clock.** A server's frame counter vs what each shard experiences | show several clocks (comoving, deep in a galaxy, near a black hole) all counting "the age of the universe" differently | none: this is a fun, accurate answer. The subtlety is that "universal time" exists only as a chosen slicing |
| **The early universe ran "slow" as seen from here** | Light from distant supernovae and quasars arrives **stretched in time by (1+z)**; very early quasars look like they're in slow motion (≈5× at z≈4) (verify: Goldhaber 2001; Blondin 2008; Lewis & Brewer 2023) | **Replay at a lower frame rate / stretched timestamps**: a stream whose packets arrive further apart because the network stretched en route | stretch a "supernova light curve" through an expanding tile map and recover 1/(1+z) | expansion predicts this exactly; a pure "lag" story must reproduce the same factor, not something else |
| **Expansion / dark energy** | the scale factor grows; expansion is accelerating | **Memory allocation**: the engine keeps adding cells between galaxies; connects to the author's "energy makes space" idea | a toy "allocate cells per tick" universe vs the measured expansion history | pure analogy risk: it must predict something (e.g. a rate), not only redescribe |
| **The Big Bang itself** | a hot, dense early state; the "start" of cosmic time; the low-entropy initial condition (the "past hypothesis") | **Boot / world initialisation**: a fresh, highly ordered initial state (low entropy = freshly allocated, zeroed memory) | show entropy growing from a tidy initial array | "what came before" is outside physics; don't overclaim |

## Batch C: "The bottom of the engine" (absolute zero, the Planck scale, entropy)

The engine question: **what happens at the engine's minimum values: minimum energy, minimum size,
minimum disorder?**

| topic | physics to respect | engine / CS concept | model idea | counterpoint to beat |
|---|---|---|---|---|
| **Absolute zero** | the Third Law: unreachable in finitely many steps; **zero-point motion** means even the ground state jitters; the coldest labs are at picokelvin (verify the record) | **The idle loop never stops.** A running engine always does minimum work per tick; there's no "0 Hz" state for a live object. A quantum ground state as "the cheapest update that still counts as running" | show that cooling steps give diminishing returns (a Third-Law curve), and that zero-point jitter persists | zero-point energy is standard QM and needs no engine; the analogy must *add* a prediction to be worth more than a metaphor |
| **Planck scale / "pixels"** | the Planck length ≈ 1.6×10⁻³⁵ m; **no sign of a grid** so far: Lorentz invariance holds, and photons of different energies from GRB 090510 arrive together (verify bound) | **Resolution, floating point, level of detail.** Minecraft's "Far Lands" show what precision loss looks like; a lattice picks preferred directions | a lattice engine that shows direction-dependent light speed at high energy, then compare with the measured bounds | **big counterpoint**: nature shows no preferred grid directions and no precision loss far from any origin. If there are pixels, they're hidden extremely well |
| **Quantum foam / tiny spaces** | at small scales, uncertainty grows; no experimental access near the Planck scale | **LOD and lazy evaluation**: detail is generated only when probed, and more probing energy means finer detail (links to Experiment 001's render-on-demand) | probe energy vs resolved detail | untestable at present; label as speculation |
| **Entropy and the arrow of time** | the Second Law; **Landauer's principle**: erasing one bit costs at least kT ln 2 of heat (measured, Bérut et al. 2012) (verify); reversible computing (Bennett) | **Append-only logs, garbage collection, and the cost of forgetting.** The engine can run forward cheaply, but deleting information costs something. Collapse (Experiment 001) *deletes branches*: does it pay Landauer's cost? | tie Experiment 001's "collapse = garbage collection" to Landauer: what would the heat bill of collapse be? (connects to the XENONnT "faint heat" bounds) | this one could become a genuine cross-experiment prediction: worth prioritising |

---

## Suggested order

1. **Batch C · Entropy / Landauer × collapse.** It ties Experiments 001 and 002 together, and there may be a testable number.
2. **Batch B · "By what clock?"** A great lay-audience episode, the physics is solid, and it covers cosmic-time dilation.
3. **Batch A · Warp and wormholes as "moving the map"** (floating origin, portals). Very visual.
4. **Batch C · Planck scale.** Mostly a strong counterpoint episode ("if there are pixels, where are they?").
5. **Batch A · FTL and causality** as race conditions (it bridges back to Experiment 001's no-signalling result).

Each batch needs a **prior-art pass first** (the session-1 web budget is exhausted; start a new session or raise
`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`).
