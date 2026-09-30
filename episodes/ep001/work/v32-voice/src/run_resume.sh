#!/bin/bash
# Chạy lại gen.py (chỉ sinh cảnh chưa có take); thử lại khi lỗi mạng proxy, nghỉ 2/4/8/16 s. Ghi log từng lần.
cd "$(dirname "$0")"
for d in 0 2 4 8 16; do
  sleep $d
  echo "=== $(date -u +%T) lần chạy (nghỉ trước ${d}s)" >> ../gen-resume.log
  python3 gen.py >> ../gen-resume.log 2>&1 && { echo "=== XONG $(date -u +%T)" >> ../gen-resume.log; exit 0; }
  tail -1 ../gen-resume.log
done
echo "=== THẤT BẠI sau 5 lần $(date -u +%T)" >> ../gen-resume.log; exit 1
