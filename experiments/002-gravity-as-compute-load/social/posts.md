# Social drafts: Experiment 002 (Gravity as Compute Load)

Rules: credit Whitworth (2008/2010) and Alagoz (2010) whenever the core idea is stated. Our part is the
models and the scoreboard. Numbers must match sim output.

---

## X / Threads / Bluesky thread (9 posts)

**1/**
Is gravity just lag?
More stuff in a region → more to compute → that region updates slower → time runs slow there.
It's an old idea (Whitworth 2008, Alagoz 2010). I built four small simulations to see how far it goes. 🧵

**2/**
First, this isn't crazy. EVE Online literally does it. When a battle overloads a server node, it slows
that star system's clock, down to 10%.
In my toy battle, pilots in the fight live 33.5 game-minutes while 90 pass at home.
A twin paradox, caused by server load.
[img: tidi_clocks.png]

**3/**
But TiDi is per-server: a step, not a smooth field. Gravity falls off as 1/r.
So I gave every region one rule: set your clock rate to the average of your neighbours', minus your own load.
Result: the lag falls off as 1/r. Log-log slope −1.000.
[img: lagfield_profile.png]

**4/**
Honest caveat: any "average your neighbours + sources" rule gives this. It's Poisson's equation, the
same one Newtonian gravity obeys. So it reproduces gravity's shape by construction, not by discovery.

**5/**
Next question: does a lag gradient make things FALL?
I gave a quantum particle only one rule: tick your internal clock at the local rate. No force anywhere in the code.
It fell 16.00 units. Newton says ½gt² = 16.00.
[vid: tick_fall.mp4]

**6/**
This part is real physics, not speculation. Objects fall toward where time runs slower.
On Earth the difference is about 1 part in 10¹⁶ per metre. That's what keeps you on the floor.

**7/**
Then light. Slower clocks also slow light, so it bends toward heavy regions. ✅
But lag alone bends starlight at the Sun by 0.876″.
Measured: 1.75″.
Exactly half. That's Einstein's 1911 mistake, fixed in 1915 by curving space too.
[img: light_bending.png]

**8/**
So "the universe lags" isn't enough. The grid itself would also have to stretch near mass.
And the hardest problem: gravity only cares about mass-energy, never complexity. A CPU and a steel
ball of equal mass fall and pull identically (to 1 part in 10¹⁵).

**9/**
Scoreboard:
✅ clocks slow near mass, and only relative rates are observable
✅ a neighbour-coupled scheduler gives a 1/r lag field
✅ a clock gradient alone makes things fall at g
❌ lag alone gets half the light bending
❓ why would cost track energy, not complexity?
No conclusions. Code + sources: [repo link]

---

## Short-form hooks
1. "EVE Online has a twin paradox." → TiDi clip + tidi_clocks
2. "I deleted gravity from the code and things still fell." → tick_fall.mp4
3. "If gravity were lag, starlight would bend exactly half as much. It doesn't." → light_bending
4. "Your feet are ageing slower than your head, by about 1 part in 10¹⁶ per metre."

## LinkedIn / long-form

**Is gravity processing lag? A thought experiment with code**

The idea that gravitational time dilation is "the universe lagging" under load goes back at least
to Whitworth (2008) and Alagoz (2010). I wanted to test it with runnable models instead of prose:

- **Precedent:** EVE Online's Time Dilation slows overloaded star systems. That's a real, shipped
  version of "more stuff → slower time".
- **Shape:** a scheduler where each region averages its neighbours' clock rates, minus its own
  load, produces a 1/r lag field (Poisson's equation). That matches gravity's shape, by construction.
- **Motion:** a particle whose only rule is "tick at the local rate" falls at exactly g. This is
  textbook GR: things fall toward slower time.
- **Light:** lag alone predicts half the measured light bending. Space itself has to be distorted too.
- **Open problem:** gravity couples only to mass-energy, never to complexity. A lag model has to
  explain why "cost" means energy.

It's a thought experiment, not a conclusion. Sources and code are in the repo.
