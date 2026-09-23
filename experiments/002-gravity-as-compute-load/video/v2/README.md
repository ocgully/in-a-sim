# Episode 002 (v2): "Is Gravity Just Lag?"

A lay-audience story, told through rendered scenes (no charts):
EVE Online's time dilation → clocks at two heights → a floor where every tile is a clock →
a marching line that swings toward slow time (why things fall) → the light race through a gravity
well (Shapiro delay) → the 1919 eclipse (lag alone gets half) → extra space near mass, with a
"tick is a signal" engine that makes space and lag equal (1:1) → supercomputer vs steel ball.

Same pipeline as Episode 001:

```bash
python3 prep_textures.py      # tile-clock floor sequences (physics from sims/lag_field.py, exaggerated)
./render_all.sh               # Blender shots → build/frames/
python3 ../../../../shared/engine/compose.py episode.json [--vertical]
```

Claims map to: Sim G1 (1/r lag field), G2A (fall from clock rates), G2B + G4 (light bending and
echo delay, exchange rate 1:1), G3 (TiDi). The sync-signal mechanism and the "complexity cancels out"
idea are labelled on screen as speculation.
