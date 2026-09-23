#!/usr/bin/env bash
# Render every Episode 002 shot with headless Blender.
set -euo pipefail
cd "$(dirname "$0")"
B="${BLENDER:-/Applications/Blender.app/Contents/MacOS/Blender}"
mkdir -p build
[ -f build/tex/schedule.json ] || python3 prep_textures.py
for s in ${@:-eve_battle tower_clocks tiles_ripple march light_race eclipse drop_test sync_space}; do
  echo "▶ rendering $s"
  rm -rf "build/frames/$s"
  "$B" -b -P scenes.py -- "$s" > "build/log_$s.txt" 2>&1 || { echo "FAILED $s (see build/log_$s.txt)"; exit 1; }
done
echo "done"
