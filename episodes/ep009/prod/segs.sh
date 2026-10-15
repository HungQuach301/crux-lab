#!/usr/bin/env bash
# Tập 9 · dựng từng đoạn thế giới (build_seg) theo thứ tự, CHẠY TIẾP khi một đoạn trượt verify; tóm tắt cuối. Dùng cache cảnh của render_shots.
#   CRUX_GREY=1 bash episodes/ep009/prod/segs.sh <res> <tên đoạn…>   (mặc định cả 6)
cd "$(dirname "$0")/../../.."
res=${1:-540}; shift || true
segs=${@:-a-s01-s03 b-s04-s06 c-s08-s13 d-s14-s18 e-s19-s21 f-s22-s25}
mkdir -p episodes/ep009/work/segs
for s in $segs; do
  python3 toolkit/factory/world/build_seg.py episodes/ep009/world/seg/$s --res $res --out episodes/ep009/work/segs/$s.mp4 --workers 4 --music episodes/ep009/work/factory/music/bed.wav > episodes/ep009/work/segs/$s.log 2>&1
  echo "$s rc=$? $(grep -E 'BLOCK|TRƯỢT|ERROR|Error' episodes/ep009/work/segs/$s.log | head -6 | tr '\n' ' ')"
done
