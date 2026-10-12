#!/usr/bin/env bash
# F-14 · dựng lại Tập 6 1080p với bản F-14 của 6 đoạn (toolkit/factory/f14/ep006) trên bản sao làm việc (git worktree, $F14_WT) — episodes/ep006
# của nhánh không đổi. Mỗi bước chạy lại được (cache render theo cảnh; checks: RESUME/KEEP); chạy bằng công cụ nền của phiên (episode.md §11b).
#   bash toolkit/factory/f14/rebuild.sh build      # loop.sh setup + chép overlay → toolkit/build.sh (1080p, 0 ký tự EL) → build_inputs.py --out
#   bash toolkit/factory/f14/rebuild.sh checks     # checks khoá đủ bộ (bộ lấy mẫu trang + luật Python) → $F14_WT/../f14-checks/…/out/checks
#   bash toolkit/factory/f14/rebuild.sh measure    # spine_pace (+ chỉ cue cũ) · freezedetect ∩ lời · R07 (checks + bản sao cách đo) · "3%"
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../../.." && pwd)"; WT="${F14_WT:-$REPO/../crux-f14-wt}"; E=episodes/ep006
OUT="${F14_OUT:-$REPO/../f14-out}"; mkdir -p "$OUT"
case ${1:-} in
  build)
    bash "$REPO/toolkit/factory/f14/loop.sh" setup
    cd "$WT"
    bash toolkit/build.sh $E/episode.yaml --workers 4
    python3 $E/c4/build_inputs.py --out
    sha256sum $E/out/video.mp4 | tee "$OUT/video.sha256" ;;
  checks)
    cd "$WT"
    KEEP=${KEEP:-} RESUME=${RESUME:-} K_JOBS=${K_JOBS:-4} bash $E/c5/checks_split.sh "$OUT/checks-root" 2>&1 | tail -20
    cp "$OUT/checks-root/$E/out/checks/report.json" "$OUT/checks-report.json" ;;
  measure)
    cd "$WT"
    python3 toolkit/indicators/spine_pace.py $E/world/c4/*/spine.json --labels --json "$OUT/spine.json" | tail -3
    python3 toolkit/factory/f14/measure.py $E/out/video.mp4 $E/out/factory/timeline.json $E/world/c4 "$OUT/measure.json" --freeze "$OUT/freeze.txt"
    P="$OUT/checks-root/$E/out/checks/page.json"; [ -f "$P" ] || P="$OUT/checks-root/$E/out/checks/page.json.gz"
    python3 toolkit/factory/f14/r07_local.py $E/out/video.mp4 $E/world/c4 "$OUT/r07.json" --page "$P" ;;
  *) echo "bước: build | checks | measure"; exit 2;;
esac
