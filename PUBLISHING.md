# Publishing checklist and known debt

Nothing gets shared publicly until its row is clear.

## Known debt (blocks sharing)

| item | affects | status |
|---|---|---|
| **Voiceover is a draft** (macOS `say`, "Daniel") | Ep 001 v2, Ep 002 | open. Recast before sharing (options below) |
| Repo link placeholders `[repo link]` in social drafts | 001, 002 `social/posts.md` | open → `https://github.com/ocgully/in-a-sim` |
| Prior-art check for "energy makes space / tick = sync signal" | 002 exploration, Ep 002 beat 7 | open (web-search budget exhausted in session 1) |
| Music / sound design | all episodes | open (currently narration only) |

## Voiceover options (recast = recompose only, no re-render)

`shared/engine/tts.py` supports three providers. Audition with `python3 shared/engine/voice_bakeoff.py`
(keys go in a gitignored `.env`).

| option | quality / control | cost | notes |
|---|---|---|---|
| macOS `say` (current) | robotic; fine for timing | free | draft only |
| **OpenAI speech API** (`gpt-4o-mini-tts`, voices incl. `cedar` / `marin`) | natural; steerable with a written style brief | low per episode | closest API option to ChatGPT's voice; the app's own voice isn't offered 1:1 |
| **ElevenLabs** (your subscription) | very natural; voice library, cloning, emotion tags, pronunciation control | counts against your monthly characters (~3–4k per episode) | best control for a recurring "series narrator" |
| **Your own voice** | most authentic | your time | record per segment using `SCRIPT.md`, then drop the wavs into `build/vo_cache` via a `"provider": "file"` backend (easy to add) |

## Per-release checklist

- [ ] VO recast (not `say`)
- [ ] every on-screen claim traceable to a tagged line in the experiment README
- [ ] prior art credited on screen where the idea isn't ours
- [ ] numbers match sim output
- [ ] captions proofread
- [ ] 16:9 + 9:16 exported to `video/releases/<version>/` with `SCRIPT.md`
