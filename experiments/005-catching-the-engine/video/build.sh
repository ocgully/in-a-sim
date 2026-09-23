#!/usr/bin/env bash
# Assemble the 16:9 and 9:16 animatic rough cuts from shots.json.
# Run from the experiment folder (or via `make videos` at the repo root).
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$(cd ../.. && pwd)"
python3 "$ROOT/shared/lib/animatic.py" video/shots.json
python3 "$ROOT/shared/lib/animatic.py" video/shots.json --vertical
