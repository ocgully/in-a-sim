#!/usr/bin/env bash
# Scaffold a new experiment:  shared/new-experiment.sh 003-tunnelling-as-bullet-through-paper "Tunnelling as Bullet-Through-Paper"
set -euo pipefail
slug="$1"; title="${2:-$1}"
root="$(cd "$(dirname "$0")/.." && pwd)"
dir="$root/experiments/$slug"
[ -e "$dir" ] && { echo "exists: $dir"; exit 1; }
mkdir -p "$dir"/{research,sims,output,social,video}
id="${slug%%-*}"
sed -e "s/{{ID}}/$id/" -e "s/{{TITLE}}/$title/" "$root/shared/templates/EXPERIMENT_README.md" > "$dir/README.md"
printf '# Experiment %s: prior art\n\n## 1. Summary verdict\n\n## 2. Annotated bibliography\n\n## 3. Physics we must respect\n\n## 4. Strongest counterarguments\n\n## 5. Unverified leads\n' "$id" > "$dir/research/prior-art.md"
printf '# Social drafts: Experiment %s\n' "$id" > "$dir/social/posts.md"
printf '# Video %s: %s\n' "$id" "$title" > "$dir/video/script.md"
printf '{\n  "title": "%s",\n  "shots": []\n}\n' "$title" > "$dir/video/shots.json"
cp "$root/experiments/001-collapse-as-rollback/video/build.sh" "$dir/video/build.sh"
echo "created $dir. Add it to the Makefile and the root README table."
