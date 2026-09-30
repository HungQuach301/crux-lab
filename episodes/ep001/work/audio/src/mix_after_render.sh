#!/bin/bash
# Chạy bước mix (limiter, ~10 GB RAM) sau khi render hình xong, để tránh OOM (30/09: mix bị OOM-kill khi chạy cùng 4 hàng render).
# Chờ có trần: tối đa 3 giờ, hoặc thoát chờ khi không còn tiến trình render.
cd "$(dirname "$0")/../../../../.."   # gốc repo
L=episodes/ep001/work/audio/mix.log
end=$((SECONDS+10800))
echo "=== $(date -u +%T) chờ render xong" >> $L
while pgrep -f "node render.js" >/dev/null && [ $SECONDS -lt $end ]; do sleep 30; done
echo "=== $(date -u +%T) bắt đầu --stage mix" >> $L
for d in 0 30; do
  sleep $d
  python3 episodes/ep001/work/audio/src/mix.py --stage mix >> $L 2>&1 && { echo "=== XONG $(date -u +%T)" >> $L; exit 0; }
done
echo "=== THẤT BẠI $(date -u +%T)" >> $L; exit 1
