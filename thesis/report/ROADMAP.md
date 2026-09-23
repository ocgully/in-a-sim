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
| **Warp drive** | Alcubierre metric (1994): space contracts ahead of a bubble and expands behind it; the ship inside sits still on flat space; it requires **negative energy density** (verify) | **The world scrolls, not the player** (endless-runner games: the player stays put, the track moves). In **our Episode 2 rule** (energy adds tiles *and* slows ticks, 1:1): *adding* tiles behind the ship needs positive energy, but *deleting* tiles ahead needs a region **cheaper than empty space**, ticking *faster* than vacuum. That is negative energy, exactly GR's requirement, derived from the space-lag model | tile engine: delete rows ahead and insert rows behind a bubble; the ship never moves more than 1 tile/tick locally, yet its distance to the destination (in tiles) shrinks faster | can anything make a region cheaper than empty space? (Casimir effect: small, real negative energy relative to vacuum.) Quantum-inequality limits; the bubble can't be steered from inside |
| **Wormholes** | Einstein–Rosen bridges; traversable ones need exotic matter (Morris–Thorne 1988) (verify) | **Portals / non-Euclidean level design.** In *Portal*, *Antichamber* and similar games a doorway is an edge in the level graph, not a straight line in space; also pointer aliasing | a grid world with an extra graph edge: shortest-path light cones, lensing through the throat | exotic matter; stability; ER = EPR (entanglement ↔ wormholes, Maldacena–Susskind 2013) as a surprising link back to Experiment 001 |
| **FTL and causality** *(revised after the author's challenge)* | In relativity, FTL signals allow causal loops **only because there is no preferred frame**: different observers disagree about which event came first | A simulation with an **authoritative server tick has a preferred frame**: the host's update order. An FTL message is just delivered in fewer ticks, in host order, so **no paradox**. What FTL *would* do is **reveal the engine's global clock** (you could sync clocks absolutely). Same pattern as Experiment 001: the engine is nonlocal internally but never lets you use it to signal | two simulations: (1) peer-to-peer with only local clocks, where FTL creates an ordering contradiction; (2) server-authoritative, where FTL is harmless but exposes the server's frame | experimental bounds on a preferred frame / Lorentz violation (the CMB rest frame is the natural candidate); Bancal et al. 2012: any finite-speed hidden influence would allow signalling |
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

## Batch D: "What things are made of" (quarks, particles, fields)

| topic | physics to respect | engine / CS concept | model idea | counterpoint to beat |
|---|---|---|---|---|
| **Particles as patterns** | in quantum field theory, particles are excitations of fields; fields are the fundamental state | **Gliders in Conway's Life**: moving, self-sustaining patterns in a grid state; the grid is the data, the particle is a pattern in it | a cellular automaton whose stable moving patterns carry conserved "charges" | Fredkin, Wolfram and 't Hooft already use this (credit them); making Lorentz invariance emerge is the hard part |
| **Identical particles** | every electron is exactly identical, and swapping two changes nothing measurable | **Instancing / the flyweight pattern**: one class, many instances that differ only in state (position, spin) | show exchange symmetry as "same asset, different transform" | exchange statistics (bosons vs fermions) is richer than "same class" |
| **Quark confinement** | a quark is never seen alone; pull two apart and the energy creates a new quark–antiquark pair (string breaking) | **A validity constraint**: a state with a lone colour charge is invalid, so the engine spawns a pair to keep it valid, like a database enforcing referential integrity, or an ECS where a component can't exist without an entity | stretch a quark pair and watch the engine insert a new pair past a threshold | is "invalid state" doing any work beyond redescribing QCD? |
| **Where mass comes from** | about 99% of the proton's mass is the **energy of the churning gluon field inside it**, not the quarks' own mass (verify: Dürr et al. 2008) | **Mass = internal activity.** This directly supports Episode 2's "load = energy": most of your weight is literally the engine computing the inside of your protons | show the proton as a busy region whose "load" is its mass | strong fact; the interpretation stays an analogy |
| **Lattice QCD** | physicists already simulate quarks on a spacetime grid on supercomputers, and it's hard (the sign problem) | the most literal overlap between physics and "the universe as a grid simulation" | explain lattice spacing, and the Beane–Davoudi–Savage test of whether *we* are on a lattice | ties to the literature survey |

## Suggested order

1. **Batch C · Entropy / Landauer × collapse.** It ties Experiments 001 and 002 together, and there may be a testable number.
2. **Batch B · "By what clock?"** A great lay-audience episode, the physics is solid, and it covers cosmic-time dilation.
3. **Batch A · Warp and wormholes as "moving the map"** (floating origin, portals). Very visual.
4. **Batch C · Planck scale.** Mostly a strong counterpoint episode ("if there are pixels, where are they?").
5. **Batch A · FTL and causality** as race conditions (it bridges back to Experiment 001's no-signalling result).

Each batch needs a **prior-art pass first** (the session-1 web budget is exhausted; start a new session or raise
`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`).
