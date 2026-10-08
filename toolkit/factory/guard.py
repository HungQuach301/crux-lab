"""An toàn chạy nền cho build (tổng kết Tập 5 mục 12; cine-lab BAI-HOC-LL #38, #67, #70).
#67: P tưởng build đã dừng, chạy lượt thứ hai → hai build ghi chồng một thư mục (x264 hai lượt hỏng tệp thống kê, đọc tệp dở).
Trước mỗi build (`build.py`, `world/build_seg.py`): kiểm KHÔNG còn tiến trình build/render nào khác đang chạy (`ps`), bỏ qua chính
tiến trình này và mọi tiến trình cha của nó (shell, `build.sh`, `build.py` gọi `build_seg.py`). Còn → từ chối, thoát 3, in PID + lệnh.
    python3 toolkit/factory/guard.py            # kiểm tay: thoát 0 khi rảnh, 3 khi còn build/render
"""
import os, re, subprocess, sys

PATTERNS = [r'toolkit/build\.sh', r'factory/build\.py', r'world/build_seg\.py', r'world/render_shots\.js', r'factory/render\.js',
            r'world/shorts\.py', r'world/splice\.py']
BUSY_EXIT = 3


def processes():
    out = subprocess.run(['ps', '-eo', 'pid=,ppid=,args='], capture_output=True, text=True).stdout
    P = {}
    for ln in out.splitlines():
        m = re.match(r'\s*(\d+)\s+(\d+)\s+(.*)', ln)
        if m:
            P[int(m[1])] = (int(m[2]), m[3])
    return P


def ancestors(P, pid):
    seen = set()
    while pid in P and pid not in seen and pid > 1:
        seen.add(pid)
        pid = P[pid][0]
    return seen


def busy(pid=None):
    """[(pid, lệnh)] tiến trình build/render khác (không phải mình, không phải cha của mình, không phải con của mình)."""
    P = processes()
    me = pid or os.getpid()
    mine = ancestors(P, me)
    rx = re.compile('|'.join(PATTERNS))
    res = []
    for p, (pp, args) in P.items():
        if p in mine or rx.search(args) is None:
            continue
        if me in ancestors(P, p):          # con của chính build này (vd render_shots.js do build_seg gọi)
            continue
        if re.match(r'^(grep|rg|ps)\b', args):
            continue
        res.append((p, args[:160]))
    return res


def assert_idle(what='build'):
    B = busy()
    if B:
        lines = '\n'.join(f'  pid {p}: {a}' for p, a in B)
        print(f'{what}: TỪ CHỐI — còn tiến trình build/render đang chạy (cine-lab #67: hai build ghi chồng nhau):\n{lines}\n'
              f'Chờ lượt đó xong (thông báo của công cụ nền), hoặc dừng hẳn nó rồi dựng lại sạch.', file=sys.stderr, flush=True)
        raise SystemExit(BUSY_EXIT)


if __name__ == '__main__':
    B = busy()
    for p, a in B:
        print(f'pid {p}: {a}')
    print('rảnh' if not B else f'{len(B)} tiến trình build/render')
    sys.exit(BUSY_EXIT if B else 0)
