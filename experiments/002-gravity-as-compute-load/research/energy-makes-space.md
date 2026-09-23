# Exploration: "Energy makes space" (the author's hypothesis)

**Status:** worth pursuing · **Sim:** [`sims/space_time_exchange.py`](../sims/space_time_exchange.py) ·
**Novelty:** checked in [`prior-art-energy-makes-space.md`](prior-art-energy-makes-space.md). The physics (excess radius, the half/half γ split, one knob setting both clocks and rulers as in Dicke/Puthoff) is established. The "tick = sync signal crossing cells" engine rule and the AMR-as-gravity idea turned up no indexed prior art. c = cell/tick is an informal meme.

## The idea

[SPEC] Energy doesn't just make a region **lag** (tick slower). It also **adds space**, meaning more room or more
cells inside the region than its outside size suggests. The author's framing: mass-energy and space are linked,
so adding energy increases size.

## What physics already says (it's half right by default)

- [PHYS] General relativity does put **extra space** near mass. A sphere around a mass has more radius than its
  surface area implies. Feynman calls this the **excess radius**: (G/3c²)·M, where M is the mass *inside* the sphere (*Feynman
  Lectures on Physics*, Vol. II, §42-3, Eq. 42.3), roughly 1.5 mm for the Earth and half a kilometre for the Sun. He
  restates it as G/3c⁴ times the total **energy** content. There's no excess radius from matter outside the sphere.
- [PHYS] Light bending and radar echo delay (the Shapiro delay) both get **half their size from slowed time and
  half from stretched space**. That's the factor of 2 in Sim G2B.
- Correction to one earlier intuition: **energy is not massless as far as gravity is concerned.** Gravity couples
  to energy, not only to rest mass. A hot cup or a charged battery weighs very slightly more, and light itself
  both bends and gravitates. The accurate phrase is "gravity only sees energy."

## The quantitative test: the exchange rate

Per unit of Newtonian potential, write the lag coefficient as **a** and the extra-space coefficient as **b**.
Light moves one cell per tick locally, so from outside its effective slowdown scales with **a + b**.

| engine design | a | b | starlight bending at Sun | Earth–Mars radar echo delay | objects fall at g? |
|---|---|---|---|---|---|
| lag only | 1 | 0 | 0.876″ | 123.6 µs | yes |
| extra space only | 0 | 1 | 0.876″ | 123.6 µs | **no** |
| **lag + space, 1 : 1** | 1 | 1 | **1.751″** | **247.2 µs** | yes |
| space grows as volume | 1 | 3 | 3.502″ | 494.5 µs | yes |
| **measured** | | | 1.75″ | ≈250 µs, γ = 1 ± 2×10⁻⁵ | |

[SIM] Free fall fixes **a = 1** (Sim G2A). Light fixes **a + b = 2**. So **b / a = 1** to about 2 parts in
100,000. Nature's exchange rate is exactly one-for-one: every bit of lag comes with the same fraction of extra space.

## Does any engine design give 1:1 *naturally*?

Designs that don't:
- **"Extra cells cost extra compute, so the region lags."** In 3-D the number of cells grows as the volume, so the
  lag would scale roughly 3× the linear stretch (or some other power). That gives the wrong ratio.
- **Adaptive mesh refinement with the CFL rule** (timestep ∝ cell size). If the engine *subcycles*, the fine
  region keeps pace and there's no lag (b > 0, a = 0). If it doesn't, you get one factor, not two. Either way
  the ratio isn't forced to 1.

A design that does, by construction:
- [SPEC] **"The tick is a signal that has to cross the region."** Suppose a region's clock only advances once a
  sync signal has crossed its cells, like a clock-distribution network on a chip, or Einstein-style light-signal
  synchronization. Then adding space (more cells to cross) slows the tick **by exactly the same factor**. Lag and
  space are the same thing measured two ways, so a = b automatically, with no tuning.
- [SPEC] A corollary: locally, light always covers one cell per tick, so every observer measures the same c, and
  only an outside observer sees the lag. The "cosmic speed limit" would be the engine's
  **signal speed = cell / tick**, and it can't be seen from inside precisely because clocks and rulers are built
  from the same cells.

## Caveats

- [COUNTER] Splitting gravity into "time part" and "space part" depends on the choice of coordinates. The
  coordinate-independent content is the PPN parameter γ = 1. The a/b language is a teaching device, so don't
  over-read it.
- [COUNTER] This doesn't yet explain *why* load equals energy (see README §5), and a sync-signal model still has
  to produce gravitational waves at c.
- **The author's offset proposal** (extra computation → extra space → density restored, so complexity nets out)
  is consistent with the equivalence principle only if the offset is exact and the result depends on energy
  alone. That's worth modelling next.

## Prior art (checked)

See [`prior-art-energy-makes-space.md`](prior-art-energy-makes-space.md).
- "Energy makes space" and the half-and-half split: **anticipated / standard physics** (Feynman §42-3; Will's
  Living Reviews; Okun 2000 on Einstein's missing factor 2).
- One quantity that slows clocks *and* shrinks rulers together, giving the full 1.75″: **anticipated** by the
  *polarizable-vacuum* models (Wilson 1921, Dicke 1957, Puthoff 2002). Credit them.
- "Space flowing into matter" models (Cahill; the Hamilton–Lisle river model) run the *opposite* direction.
  Cite them only as a contrast.
- **"The tick is a sync signal that must cross the region's cells"**, and **extra cells near mass (AMR) as a
  model of gravity**: **no indexed prior art found** (arXiv, Crossref, OpenAlex and HN searched; Reddit, YouTube
  and Medium not covered). Nearest work: a 2026 preprint by Sano (phase synchronisation, not peer-reviewed), and
  quantum walks in curved spacetime (Di Molfetta et al. 2013).

## Verdict

**Interesting enough to feature.** The idea turns the "lag gets only half" failure into a precise, measured
requirement (b = a), and it suggests a simple engine rule that satisfies it. It becomes the Episode 002 cliffhanger
and gets a full prior-art check before publication.
