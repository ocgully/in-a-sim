# Episode 001 (v2): "You Were Never Behind Cover"

A lay-audience explainer. The story is carried by rendered game scenes, with no charts. The viewer
experiences the "died behind cover" moment, sees each player's screen, watches the server rewind,
and then watches the rewind rewrite the victim's own memory. The double-slit and delayed-choice
experiments are then acted out in a neon lab, as the same pattern in physics.

## Pipeline

```
prep_textures.py   → build/tex/…          animated detector-screen textures (physics from sims/)
scenes.py          → build/frames/<shot>/  headless Blender (EEVEE) renders + meta.json timing
episode.json       → story beats: narration, which frames to play/rewind/hold, HUD overlays
shared/engine/compose.py → build/episode/episode.mp4 (+ _vertical.mp4)
```

```bash
./render_all.sh                        # all shots (~25 min on Apple silicon); or: ./render_all.sh arena_server
python3 ../../../../shared/engine/compose.py episode.json              # 16:9, draft voice + captions
python3 ../../../../shared/engine/compose.py episode.json --vertical   # 9:16 for Shorts / Reels / TikTok
python3 ../../../../shared/engine/compose.py episode.json --no-vo --only=server_rewind   # iterate on one beat
```

Needs Blender (tested 3.4, `BLENDER=` to override the path), ffmpeg, Python with numpy + Pillow, and macOS `say`.

## Notes

- **Voice:** the narration comes from macOS `say` (voice "Daniel"). It's a *timing draft*. For release,
  record a human voiceover or use a better TTS voice, and keep each segment's `vo` text as the script.
  Segment lengths adapt automatically to the narration length.
- **Captions** are burned in, since most social video plays muted.
- **Accuracy:** timings match `sims/lag_compensation.py` (6 m/s sprint, 150 ms view lag, 50 ms / 40 ms
  one-way latency). Screen patterns come from the same two-slit model as `sims/delayed_choice_eraser.py`.
- The "memory is rewritten too" beat is the author's hypothesis, and the narration presents it as a thought
  experiment ("imagine a game where…"), not as established physics.
