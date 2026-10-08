#!/usr/bin/env bash
# Crux factory: one command from episode.yaml to master + parts + Shorts + qc (toolkit/factory/build.py).
#   bash toolkit/build.sh episodes/epNNN/episode.yaml [--workers 4] [--fmt jpeg|rgba] [--no-cache]
# An toàn chạy nền (tổng kết Tập 5 mục 12; cine-lab #38, #67; playbook/episode.md §11b):
#   - chạy bằng CÔNG CỤ NỀN của phiên (Bash run_in_background) — không `&`, không nohup: tiến trình `&` không được theo dõi, mất khi
#     phiên/máy khởi động lại, và phiên tưởng build đã dừng;
#   - trước khi dựng: không còn build/render nào khác (`toolkit/factory/guard.py`, thoát 3 nếu còn);
#   - log ra `<tập>/work/factory/build.log` qua tee; mã thoát lấy từ PIPESTATUS[0] (mã của build.py, không phải của tee).
set -euo pipefail
[ $# -ge 1 ] || { echo "usage: toolkit/build.sh <episode.yaml> [options]"; exit 2; }
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/factory/guard.py" >/dev/null || { python3 "$HERE/factory/guard.py" >&2; echo "build.sh: TỪ CHỐI — còn build/render đang chạy" >&2; exit 3; }
LOG="${CRUX_BUILD_LOG:-$(dirname "$1")/work/factory/build.log}"
mkdir -p "$(dirname "$LOG")"
set +e
python3 "$HERE/factory/build.py" "$@" 2>&1 | tee "$LOG"
rc=${PIPESTATUS[0]}
set -e
echo "build.sh: build.py thoát $rc (log $LOG)" >&2
exit "$rc"
