#!/bin/bash
# C6 cuối: chờ mix nhạc C xong → mux → ghi SHA. Chờ có trần (90 phút) và thoát nếu mix chết không ra master mới.
cd "$(dirname "$0")/../.."     # episodes/ep001
L=work/c5/logs/c6-final.txt; echo "=== $(date -u +%T) bắt đầu" >> $L
end=$((SECONDS+5400))
while pgrep -f "^python3 .*audio/src/mix.py" >/dev/null && [ $SECONDS -lt $end ]; do sleep 20; done
if ! grep -q '"master"' <(tail -1 work/audio/mix.log) || [ out/audio/master.wav -ot work/c5/c6_final.sh ]; then echo "=== $(date -u +%T) mix không xong — dừng" >> $L; exit 1; fi
echo "=== $(date -u +%T) mux" >> $L
python3 animatic/src/assemble_c5.py --mux-only >> $L 2>&1 || { echo "=== mux lỗi" >> $L; exit 1; }
sha256sum out/video.mp4 out/audio/master.wav >> $L
echo "=== XONG $(date -u +%T)" >> $L
