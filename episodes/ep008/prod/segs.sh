#!/usr/bin/env bash
# Tập 8 · dựng từng đoạn thế giới (build_seg) theo thứ tự, CHẠY TIẾP khi một đoạn trượt verify; tóm tắt cuối. Dùng cache cảnh của render_shots.
#   CRUX_GREY=1 bash episodes/ep008/prod/segs.sh <res> <tên đoạn…>   (mặc định cả 6)
cd "$(dirname "$0")/../../.."
res=${1:-540}; shift || true
segs=${@:-a-s01-s03 b-s04-s07 c-s08-s14 d-s15-s22 e-s23-s28 f-s29-s33}
mkdir -p episodes/ep008/work/segs
for s in $segs; do
  python3 toolkit/factory/world/build_seg.py episodes/ep008/world/seg/$s --res $res --out episodes/ep008/work/segs/$s.mp4 --workers 4 --music episodes/ep008/work/factory/music/bed.wav > episodes/ep008/work/segs/$s.log 2>&1
  echo "$s rc=$? $(grep -E 'BLOCK|TRƯỢT|ERROR|Error' episodes/ep008/work/segs/$s.log | head -6 | tr '\n' ' ')"
done
