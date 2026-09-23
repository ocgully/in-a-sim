# Final long-form video: "If the Universe Were a Program" (outline)

**Target:** 20–30 min, 16:9, chaptered. Built from each experiment's clips and figures; narration
adapted from each experiment's `video/script.md`.

1. **Cold open (1 min).** Dying behind the wall (`001/output/lagcomp_three_views.mp4`) cut against
   EVE Online's time dilation (`002/output/tidi_clocks.png`). "Two things game servers do. Physics
   seems to do them too. Or does it?"
2. **The rules of this video (1 min).** No conclusions. Every "whoa" gets a "but". Prior art is credited on screen.
3. **Why ask the question at all (3 min).** Bostrom's trilemma in one slide; engineering instead of
   philosophy; what a demonstration can and can't show. Source: `report/literature-survey.md`.
4. **Chapter 1: Collapse as Rollback (8 min).** Condensed from `001/video/script.md`.
5. **Chapter 2: Gravity as Compute Load (8 min).** Condensed from `002/video/script.md`.
6. **Chapter N: future experiments.**
7. **The ledger (3 min).** Animated fits / breaks / open table, generated from the evidence ledger in `THESIS.md`.
8. **Close (1 min).** "We didn't find out whether we're in a simulation. We found out which parts of
   physics look like engineering, and exactly where the resemblance stops."

**Production notes**
- All charts share the `shared/lib/simviz.py` style, so cuts between experiments look like one series.
- A build script for this video (concatenating per-experiment animatics + ledger cards) comes once 3+ experiments are done.
