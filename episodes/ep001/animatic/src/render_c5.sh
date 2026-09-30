#!/bin/bash
# C5 final picture: render scenes one after another through render.js (1080p30, resumable: an up-to-date scene is skipped).
#   nohup animatic/src/render_c5.sh S10 S06 ... > work/c5/logs/queue-1.txt 2>&1 &     (2-3 queues in parallel on 4 CPUs)
# Per scene: work/c5/logs/<S>.txt (progress), <S>.json (render log for check.py), work/c5/scenes/<S>.mp4. Failures: logs/failed.txt.
cd "$(dirname "$0")"
LOG=../../work/c5/logs; mkdir -p $LOG
export NODE_PATH=${NODE_PATH:-/opt/node22/lib/node_modules} PLAYWRIGHT_BROWSERS_PATH=${PLAYWRIGHT_BROWSERS_PATH:-/opt/pw-browsers}
for s in "$@"; do
  echo "$(date -u +%FT%TZ) start $s"
  if node render.js $s > $LOG/$s.txt 2>&1; then echo "$(date -u +%FT%TZ) done $s"; else echo "$(date -u +%FT%TZ) FAILED $s" | tee -a $LOG/failed.txt; fi
done
echo "$(date -u +%FT%TZ) queue end"
