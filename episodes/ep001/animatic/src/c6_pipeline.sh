#!/bin/bash
# C6 (P): after render_c5.sh S06 S07 -> check.py -> assemble_c5.py --picture-only -> --mux-only -> K3.3 file rules (scratch copy of origin/main checks/).
# Resumable: every step is skipped when its output is newer than its inputs. Waits are capped; exits if the render queue died.
#   CHK=<scratch>/checks nohup animatic/src/c6_pipeline.sh > work/c5/logs/c6-pipeline.txt 2>&1 &
set -u
cd "$(dirname "$0")/../.."   # episode root
EP=$PWD; L=work/c5/logs; SCN=work/c5/scenes; PIC=work/c5/picture-1080.mp4; OUT=out/video.mp4; WAV=out/audio/master.wav
CHK=${CHK:?set CHK to a scratch copy of origin/main checks/}
source animatic/src/env.sh
m() { stat -c %Y "$1" 2>/dev/null || echo 0; }
log() { echo "$(date -u +%FT%TZ) $*"; }
FJ=animatic/build/film.js
# 1. wait for S06/S07 (cap 150 min); die if the queue is gone and a scene is not newer than film.js
for i in $(seq 1 900); do
  ok=1; for s in S06 S07; do [ $(m $SCN/$s.mp4) -gt $(m $FJ) ] && [ $(m $L/$s.json) -gt $(m $FJ) ] || ok=0; done
  [ $ok = 1 ] && break
  if ! pgrep -f "render_c5.sh" >/dev/null; then log "render queue not running and S06/S07 not up to date -> exit"; exit 2; fi
  sleep 10
done
[ $ok = 1 ] || { log "wait cap reached"; exit 3; }
log "render S06 S07 up to date"
# 2. self-checks (all 20 logs)
python3 animatic/src/check.py > $L/c6-check.txt 2>&1; rc=$?; tail -3 $L/c6-check.txt; [ $rc = 0 ] || { log "check.py rc=$rc"; exit 4; }
# 3. picture
if [ $(m $PIC) -gt $(m $SCN/S06.mp4) ] && [ $(m $PIC) -gt $(m $SCN/S07.mp4) ]; then log "picture up to date, skipped"
else log "picture start"; python3 animatic/src/assemble_c5.py --picture-only > $L/c6-assemble-picture.txt 2>&1 || { log "picture FAILED"; exit 5; }; cat $L/c6-assemble-picture.txt; cp $L/assemble.json $L/c6-assemble-picture.json; fi
# 4. mux with the current master
if [ $(m $OUT) -gt $(m $PIC) ] && [ $(m $OUT) -gt $(m $WAV) ]; then log "video up to date, skipped"
else log "mux start"; python3 animatic/src/assemble_c5.py --mux-only > $L/c6-assemble-mux.txt 2>&1 || { log "mux FAILED"; exit 6; }; cat $L/c6-assemble-mux.txt; fi
# 5. K3.3 file rules (writes out/checks/report-partial.*, tracked old file -> copy then restore)
log "file rules start"
python3 $CHK/py/run.py "$EP" --only F01,F02,F03,F04,F05,F06,F07,F08,F10,A01,A02,A04,A05,A06 --first > $L/c6-file-rules.txt 2>&1; echo "run.py rc=$?"
cp out/checks/report-partial.json $L/c6-file-rules.json; cp out/checks/report-partial.md $L/c6-file-rules.md
git checkout -- out/checks/report-partial.json out/checks/report-partial.md
cat $L/c6-file-rules.md
sha256sum $OUT $PIC $WAV | tee $L/c6-sha256.txt
log "pipeline end"
