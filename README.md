# We Are In A Simulation — a thought experiment, in public

This project asks one question over and over from different angles:

> **If our universe were a program, what would the engineering look like — and does anything we measure resemble it?**

It draws **no conclusions**. Each experiment sets out an observation, builds a small runnable model
(the "proof", meaning a demonstration and not a claim of truth), lists the prior art, and gives
the strongest case *against* it next to the case for it. The goal is to explain physics through
**video-game engineering and computer science**, not just philosophy, and to publish everything in
a form that can be turned into social posts and explainer videos.

## Layout (monorepo: each folder is a self-contained "repo")

```
.
├── METHODOLOGY.md                 claim labels, evidence rules, the "no conclusions" rule
├── shared/
│   ├── lib/simviz.py              common visual style + video/figure helpers
│   └── templates/                 experiment / social / video templates
├── experiments/
│   ├── 001-collapse-as-rollback/  wave-function collapse vs lag-compensation rollback;
│   │                              Many-Worlds vs collapse vs deterministic replay
│   └── 002-gravity-as-compute-load/  gravity & time dilation as regional processing lag
└── thesis/
    ├── report/                    the final thesis + literature survey + evidence ledger
    ├── video/                     long-form final explainer
    └── social/                    series-level posts
```

Every experiment has the same shape:

| path | what it is |
|---|---|
| `README.md` | the observation, the analogy table, what each sim shows, findings |
| `research/prior-art.md` | who has said this before, what's novel, verified citations |
| `sims/*.py` | runnable models; each prints its key numbers |
| `output/` | generated figures (`.png`) and clips (`.mp4`) |
| `social/posts.md` | thread / short-form / long-form post drafts |
| `video/script.md` | narrated explainer script with shot list |
| `video/build.sh` | assembles an animatic rough cut from the generated clips |

## Run it

Requirements: Python 3.10+, `numpy`, `matplotlib`, `ffmpeg` (for clips).

```bash
make all            # run every sim in every experiment (figures + clips)
make exp001         # just one experiment
NO_VIDEO=1 make all # figures only, fast
make videos         # assemble animatic rough cuts
```

## Experiments

| # | question | status |
|---|---|---|
| [001](experiments/001-collapse-as-rollback/) | Is wave-function collapse like an FPS server rewinding to resolve a shot? How do Many-Worlds, collapse, and a deterministic replay compare as engine designs? | sims + write-up drafted |
| [002](experiments/002-gravity-as-compute-load/) | Is gravity what processing lag would look like from inside? | sims + write-up drafted |

Backlog of future experiments: [`thesis/report/BACKLOG.md`](thesis/report/BACKLOG.md).
