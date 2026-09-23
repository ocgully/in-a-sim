# Social drafts: Experiment 001 (Collapse as Rollback)

Rules (from METHODOLOGY): every "looks like a sim" point has a counterpoint in the same post or thread,
numbers match the sim output exactly, and prior art gets credited.

---

## X / Threads / Bluesky thread (9 posts)

**1/**
You've died behind a wall in a shooter. You *saw* yourself reach cover.
The server disagreed, and the server is the truth.
I built a small simulation of why that happens, then put quantum physics through the same test. 🧵
[img: lagcomp_spacetime.png]

**2/**
How lag compensation works:
• the enemy's screen shows you ~150 ms in the past
• they shoot that ghost
• the server REWINDS everyone to that moment, checks the hit, commits it
In my sim you're told you're dead 223 ms after reaching cover, 1.34 m behind the wall.

**3/**
It isn't rare. If you're exposed for half a second and the shooter has 100 ms ping, ~48% of deaths
happen "behind cover" from your point of view. It's the design, not a bug.
[img: lagcomp_behind_cover.png]

**4/**
Physics has a "decided later" experiment: the delayed-choice quantum eraser (Kim et al., 1999).
A photon hits a screen. Its entangled twin gets measured LATER. Sort the old hits by what happened
to the twins, and an interference pattern shows up.
[vid: eraser_relabel.mp4]

**5/**
Looks like a server rewind. But:
• the raw screen never changes (my sim: χ² = 40.5 on 39 dof, no trace of the later choice)
• the pattern only exists when you JOIN the two logs
• my sim produces it strictly in time order, with no rewind at all
Nature doesn't seem to need a rollback. It needs a joint record.

**6/**
Then the Bell test. I made 6 "engine architectures" play it:
❌ pre-loaded answers (client-side prediction): max 2
✅ central server that sees both sides: 2.83
✅ one seed pre-scripts everything: 2.83
✅ keep every branch (Many-Worlds): 2.83
Reality measures ≈ 2.83.
[img: bell_scoreboard.png]

**7/**
Two things stood out:
1) A game server is nonlocal for free. It doesn't care how far apart two players are.
2) The same server could score 4 without ever leaking a message. Nature stops at 2.83 (Tsirelson's bound). Nobody fully knows why.

**8/**
Hosting bill: keep every branch and memory doubles per observation, 4,194,304 numbers after 14
observations of 8 qubits. Collapse keeps it at 256. The lab notebooks from inside look identical.
Collapse looks like garbage collection.
Counterpoint: that only matters if someone's paying for the server.
[img: branching_memory.png]

**9/**
Scoreboard:
✅ one canonical outcome everyone agrees on
✅ correlations that act like shared server state
❌ quantum branches interfere, game predictions don't
❌ nature never shows the victim a contradiction
❓ why 2.83, why amplitude²
No conclusions. Code + sources: [repo link]

---

## Short-form video hooks (TikTok / Reels / Shorts)

1. "You died behind the wall. Physics does something similar, sort of." → 60 s vertical cut
2. "The quantum eraser isn't a time machine. Here's what it actually shows, with code."
3. "Three ways to build a universe that passes the Bell test. One of them is how every MMO works."
4. "Many-Worlds is expensive. Here's the server bill."

## LinkedIn / long-form post

**What netcode can (and can't) teach us about quantum measurement**

Competitive shooters resolve hits with lag compensation. The server rewinds to where the shooter
saw the target, tests the shot against that snapshot, and commits the result. That's why you can die
behind a wall.

I wanted to know how far the analogy with quantum measurement goes, so I built four small simulations:

1. **Lag compensation:** the victim is told they're dead 223 ms after reaching cover.
2. **Delayed-choice quantum eraser:** the "retroactive" pattern appears only when two logs are joined.
   A time-ordered sampler with **no rewind** reproduces it exactly. The better analogy is a joint
   authoritative record, not a rollback.
3. **Bell test:** client-side prediction caps at 2. A central server, a pre-scripted seed, and
   keep-every-branch all reach the measured 2.83. Those are the three big interpretations.
4. **Hosting cost:** keep-every-branch doubles memory with each observation. Collapse behaves like
   garbage collection.

Where it breaks: quantum branches interfere, and nature never shows any observer a contradiction.
Where it's open: why correlations cap at 2√2 when a server could do better.

It's a thought experiment, not a conclusion. Code and verified sources are in the repo.
