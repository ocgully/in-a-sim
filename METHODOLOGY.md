# Methodology

## The one rule

**Observe, model, compare. Do not conclude.** Nothing in this project claims we are, or are not,
in a simulation. The thesis is a catalogue of *resemblances and mismatches* between physics and
computing, each with a runnable demonstration and a matching counterargument.

## Claim labels

Every non-trivial sentence in a write-up, post, or script carries one of these tags, at least in the
source markdown. (Social posts can drop the tags, but the post must be traceable to a tagged line.)

| tag | meaning | evidence needed |
|---|---|---|
| **[PHYS]** | established, measured physics | peer-reviewed source or standard textbook |
| **[CS]** | established computer science / game engineering | spec, paper, or shipped system (e.g. Source engine docs) |
| **[SIM]** | a result of *our* code | the sim file + the number it prints |
| **[ANALOGY]** | a structural mapping between the two | explicit mapping table; say where it breaks |
| **[SPEC]** | speculation / our hypothesis | labelled as such, always |
| **[COUNTER]** | the strongest case against | source, or clear reasoning |

## Evidence rules

1. **Citations are verified or they're out.** Anything unverified goes under "Unverified leads" in
   `research/prior-art.md` and cannot appear in public material.
2. **Sims must print the numbers they support.** A figure without a printed, reproducible number is
   decoration.
3. **A demonstration is not a proof about reality.** A sim shows that a mechanism *can* produce a
   pattern. It says nothing about whether nature uses that mechanism.
4. **Every analogy lists its breaking point.** If we can't find where it breaks, we haven't looked.
5. **Prior art first.** Before calling an idea novel, record the searches run. "No prior art found"
   is a statement about our search, not about the world.
6. **Each experiment ends with a scoreboard, not a verdict.** It lists what fits, what doesn't, and
   what could tell the two apart.

## Public-content rules (social + video)

- Every post that makes a "looks like a simulation" point also includes a counterpoint, in the same
  post or the next one in the thread.
- No "scientists prove…" framing. Say "here's a model", "here's a measurement", "here's where it breaks".
- Keep numbers exactly as the sims or sources print them. No rounding up for drama.
- Credit prior art by name when the idea isn't ours.
