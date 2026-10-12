#!/usr/bin/env bash
# F-14 · vòng nháp nhanh trên bản sao làm việc (git worktree, episodes/ep006 của nhánh không đổi):
#   bash toolkit/factory/f14/loop.sh setup                  # worktree $F14_WT (mặc định ../crux-f14-wt) + three + timeline/nhạc nền khô (0 ký tự EL)
#   bash toolkit/factory/f14/loop.sh seg <đoạn…> [--res 360] # chép bản F-14 (toolkit/factory/f14/ep006/world) đè lên worktree → spine.py → render nháp
#   bash toolkit/factory/f14/loop.sh measure [--res 360]    # ghép 6 đoạn nháp → master nháp → spine_pace + r07_local + freezedetect ∩ lời
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../../.." && pwd)"; WT="${F14_WT:-$REPO/../crux-f14-wt}"; OV="$REPO/toolkit/factory/f14/ep006/world"
SEGS="a-s01-s03 b-s04-s08 c-s09-s12 d-s13-s23 e-s24-s29 f-s30-s32"
cmd=$1; shift; RES=360; ARGS=()
while [ $# -gt 0 ]; do case $1 in --res) RES=$2; shift;; *) ARGS+=("$1");; esac; shift; done
D="$WT/episodes/ep006/work/f14/draft-$RES"; export NODE_PATH="$(npm root -g)"
sync() { cp "$OV/c4kit.py" "$OV/c4kit.js" "$WT/episodes/ep006/world/"; for s in $SEGS; do cp "$OV/c4/$s/spine.py" "$OV/c4/$s/scene.js" "$WT/episodes/ep006/world/c4/$s/"; done
         cp "$REPO"/toolkit/factory/world/*.py "$REPO"/toolkit/factory/world/*.js "$WT/toolkit/factory/world/"; cp "$REPO"/toolkit/factory/f14/*.py "$WT/toolkit/factory/f14/" 2>/dev/null || true; }
case $cmd in
  setup)
    [ -d "$WT" ] || git -C "$REPO" worktree add --detach "$WT" HEAD
    ln -sfn "$REPO/toolkit/factory/world/vendor/node_modules" "$WT/toolkit/factory/world/vendor/node_modules"
    mkdir -p "$WT/toolkit/factory/f14"; sync
    (cd "$WT" && python3 episodes/ep006/c4/build_inputs.py >/dev/null && python3 episodes/ep006/c4/build_inputs.py --timeline | tail -2) ;;
  seg)
    sync; mkdir -p "$D"
    for s in "${ARGS[@]}"; do
      (cd "$WT" && python3 episodes/ep006/world/c4/$s/spine.py | tail -2)
      (cd "$WT" && node toolkit/factory/world/render_shots.js episodes/ep006/world/c4/$s $RES "$D/$s.mp4" --workers 4 --cache "$D/cache/$s" | tail -1)
    done ;;
  measure)
    sync; ( for s in $SEGS; do echo "file '$D/$s.mp4'"; done ) > "$D/concat.txt"
    ffmpeg -v error -y -f concat -safe 0 -i "$D/concat.txt" -c copy "$D/master.mp4"
    mkdir -p "$D/logs"; for s in $SEGS; do cp "$D/$s.log.json" "$D/logs/$s.log.json"; done
    cd "$WT"
    python3 toolkit/indicators/spine_pace.py episodes/ep006/world/c4/*/spine.json --labels | tail -8
    python3 toolkit/factory/f14/r07_local.py "$D/master.mp4" episodes/ep006/world/c4 "$D/r07.json" --logs "$D/logs"
    rm -f "$D/freeze.txt"; python3 toolkit/factory/f14/measure.py "$D/master.mp4" episodes/ep006/out/factory/timeline.json episodes/ep006/world/c4 "$D/measure.json" --freeze "$D/freeze.txt" ;;
esac
