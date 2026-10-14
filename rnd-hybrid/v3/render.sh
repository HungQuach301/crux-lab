#!/usr/bin/env bash
# R&D v3 bước 1: dựng 3 khung 1080p + đoạn lượn 6 s cho mỗi hướng bằng render_shots.js của nhà máy (không sửa). Chạy từ gốc repo.
set -euo pipefail
export NODE_PATH=$(npm root -g)
for d in h4 h3; do
  s=$(date +%s)
  node toolkit/factory/world/render_shots.js rnd-hybrid/v3/$d 1080 rnd-hybrid/work/v3/$d-x.mp4 --stills 0.5,1.5,2.5 --stills-dir rnd-hybrid/work/v3/stills
  m=$(date +%s)
  node toolkit/factory/world/render_shots.js rnd-hybrid/v3/$d 1080 rnd-hybrid/work/v3/$d-orbit.mp4 --workers 4 --cache rnd-hybrid/work/v3/cache/$d
  e=$(date +%s); echo "$d stills_s=$((m-s)) orbit_s=$((e-m))" | tee -a rnd-hybrid/work/v3/times.txt
done
