#!/usr/bin/env bash
# F-15 (cine-lab #38, #67, #102; TONGKET Tập 7 h, i): chạy việc dài (build, checks, cổng gốc) bằng `setsid nohup` — sống qua trần 2 h của lệnh nền
# và qua lúc phiên ngắt; có tệp PID, log, mã thoát; dừng theo PID (nhóm tiến trình), KHÔNG `pkill -f` (#24, #41: tự giết shell của phiên).
#   bash toolkit/bg.sh start <tên> [--no-guard] -- <lệnh …>   kiểm ps (factory/guard.py) rồi chạy; in PID. Tên trùng mà còn chạy → từ chối (thoát 3)
#   bash toolkit/bg.sh status <tên>                             running <pid> | done <mã thoát> | missing
#   bash toolkit/bg.sh wait <tên> [giây-trần]                   chờ bằng vòng until (mặc định không trần); thoát bằng mã của lệnh
#   bash toolkit/bg.sh stop <tên>                               TERM cả nhóm (kill -- -PGID), 10 s sau KILL; ghi rc=143
#   bash toolkit/bg.sh list                                     mọi việc đã biết
# Thư mục trạng thái: $CRUX_BG (mặc định /var/tmp/crux-bg): <tên>.pid · <tên>.log · <tên>.rc · <tên>.cmd · <tên>.t0/.t1 (giờ máy).
# Trạng thái sống cùng container: mở phiên mới khi việc còn chạy = mất nó (cine-lab #109).
set -uo pipefail
D="${CRUX_BG:-/var/tmp/crux-bg}"; mkdir -p "$D"
HERE="$(cd "$(dirname "$0")" && pwd)"
cmd=${1:-}; name=${2:-}
alive() { [ -f "$D/$1.pid" ] && kill -0 "$(cat "$D/$1.pid")" 2>/dev/null && [ ! -f "$D/$1.rc" ]; }
case "$cmd" in
  start)
    [ -n "$name" ] || { echo "bg.sh start <tên> [--no-guard] -- <lệnh>"; exit 2; }
    shift 2; guard=1
    while [ $# -gt 0 ] && [ "$1" != "--" ]; do case $1 in --no-guard) guard=0;; esac; shift; done
    [ "${1:-}" = "--" ] && shift
    [ $# -gt 0 ] || { echo "bg.sh: thiếu lệnh sau --"; exit 2; }
    if alive "$name"; then echo "bg.sh: '$name' còn chạy (pid $(cat "$D/$name.pid"))"; exit 3; fi
    if [ $guard = 1 ]; then python3 "$HERE/factory/guard.py" >/dev/null || { python3 "$HERE/factory/guard.py"; echo "bg.sh: TỪ CHỐI — còn build/render/checks đang chạy"; exit 3; }; fi
    rm -f "$D/$name.rc" "$D/$name.t1"; printf '%q ' "$@" > "$D/$name.cmd"; date +%s > "$D/$name.t0"
    # nhóm mới (setsid) → stop giết đúng cây của việc này; mã thoát ghi khi lệnh xong (kể cả trượt)
    # setsid -f: luôn tách thành phiên/nhóm mới; chính tiến trình con ghi PID của nó (= PGID) — $! của lớp ngoài không đáng tin
    rm -f "$D/$name.pid"
    setsid -f nohup bash -c 'echo $$ > "$0.pid"; cd "$1"; shift; "$@"; rc=$?; date +%s > "$0.t1"; echo $rc > "$0.rc"' "$D/$name" "$PWD" "$@" > "$D/$name.log" 2>&1 < /dev/null
    for _ in $(seq 50); do [ -s "$D/$name.pid" ] && break; sleep 0.1; done
    echo "bg.sh: $name pid $(cat "$D/$name.pid") log $D/$name.log";;
  status)
    if alive "$name"; then echo "running $(cat "$D/$name.pid")"; elif [ -f "$D/$name.rc" ]; then echo "done $(cat "$D/$name.rc")"; else echo missing; fi;;
  wait)
    cap=${3:-0}; t=0
    until ! alive "$name"; do sleep 20; t=$((t + 20)); if [ "$cap" -gt 0 ] && [ $t -ge "$cap" ]; then echo "bg.sh: hết $cap s, '$name' còn chạy"; exit 124; fi; done
    rc=$(cat "$D/$name.rc" 2>/dev/null || echo 255); echo "bg.sh: $name xong, mã $rc"; exit "$rc";;
  stop)
    alive "$name" || { echo "bg.sh: '$name' không chạy"; exit 0; }
    p=$(cat "$D/$name.pid"); kill -TERM -- "-$p" 2>/dev/null || kill -TERM "$p"
    for _ in $(seq 10); do kill -0 -- "-$p" 2>/dev/null || break; sleep 1; done   # cả nhóm (con bỏ qua TERM vẫn bị KILL)
    kill -0 -- "-$p" 2>/dev/null && kill -KILL -- "-$p" 2>/dev/null
    [ -f "$D/$name.rc" ] || echo 143 > "$D/$name.rc"; date +%s > "$D/$name.t1"; echo "bg.sh: dừng $name (pid $p)";;
  list)
    for f in "$D"/*.pid; do [ -e "$f" ] || continue; n=$(basename "$f" .pid); printf '%-28s %s\n' "$n" "$("$0" status "$n")"; done;;
  *) sed -n '2,10p' "$0"; exit 2;;
esac
