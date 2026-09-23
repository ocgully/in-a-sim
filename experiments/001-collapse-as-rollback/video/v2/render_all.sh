#!/usr/bin/env bash
# Render every Episode 001 shot with headless Blender (≈20–30 min on an M-series Mac).
set -euo pipefail
cd "$(dirname "$0")"
B="${BLENDER:-/Applications/Blender.app/Contents/MacOS/Blender}"
python3 prep_textures.py
for s in ${@:-arena_game arena_shooter arena_runner arena_server arena_committed lab_stripes lab_observed lab_delayed racks}; do
  echo "▶ rendering $s"
  rm -rf "build/frames/$s"
  "$B" -b -P scenes.py -- "$s" > "build/log_$s.txt" 2>&1 || { echo "FAILED $s (see build/log_$s.txt)"; exit 1; }
done
echo "done"
