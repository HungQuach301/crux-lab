#!/usr/bin/env bash
# Tập 8 · dựng animatic xám cả tập: từng đoạn (chạy tiếp khi trượt) rồi build.sh ghép (trúng cache). PID ở logs/m2/animatic.pid
cd "$(dirname "$0")/../../.."
echo $$ > episodes/ep008/logs/m2/animatic.pid
export CRUX_GREY=${CRUX_GREY-1}
bash episodes/ep008/prod/segs.sh ${RES:-540}
if grep -q "rc=[1-9]" <(for s in a-s01-s03 b-s04-s07 c-s08-s14 d-s15-s22 e-s23-s28 f-s29-s33; do echo "rc=$(grep -c 'TRƯỢT' episodes/ep008/work/segs/$s.log)"; done); then echo "SEG FAIL"; exit 1; fi
bash toolkit/build.sh episodes/ep008/episode.yaml --workers 4 --no-shorts > /dev/null 2>&1; echo "build rc=$?"
