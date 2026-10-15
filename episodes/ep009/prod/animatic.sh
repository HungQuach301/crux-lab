#!/usr/bin/env bash
# Tập 9 · M2 animatic xám cả tập (take khô, 0 ký tự EL): từng đoạn (chạy tiếp khi trượt) rồi build.sh ghép theo animatic.yaml (trúng cache).
cd "$(dirname "$0")/../../.."
mkdir -p episodes/ep009/logs/m2; echo $$ > episodes/ep009/logs/m2/animatic.pid
export CRUX_GREY=${CRUX_GREY-1}
bash episodes/ep009/prod/segs.sh ${RES:-540} ${SEGS:-}
bash toolkit/build.sh episodes/ep009/animatic.yaml --workers 4 --no-shorts > episodes/ep009/work/segs/build.log 2>&1; echo "build rc=$?"
