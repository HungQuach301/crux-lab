#!/usr/bin/env python3
"""Xoá số liệu thô YouTube quá 30 ngày (YouTube API Developer Policies III.E.4: số liệu API không giữ quá 30 ngày nếu không làm mới).

  python3 toolkit/market/purge.py            # xoá ~/market-cache/<ngày>/ cũ hơn 30 ngày
  python3 toolkit/market/purge.py --dry-run  # chỉ liệt kê

Làm mới = chạy lại discover.py / pull.py / analyze.py (tạo thư mục ngày mới). Việc 0 P1 gọi purge trước khi làm mới hồ sơ cầu.
Repo không chứa số liệu thô nên không có gì để xoá trong git; chỉ nhãn và kết luận định tính.
"""
import datetime as dt, pathlib, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from mcommon import CACHE_ROOT

MAX_DAYS = 30


def purge(dry=False, today=None):
    today = today or dt.date.today()
    gone = []
    for p in sorted(CACHE_ROOT.glob('20??-??-??')):
        try:
            d = dt.date.fromisoformat(p.name)
        except ValueError:
            continue
        if (today - d).days > MAX_DAYS:
            gone.append(p)
            if not dry:
                shutil.rmtree(p)
    return gone


if __name__ == '__main__':
    dry = '--dry-run' in sys.argv
    g = purge(dry)
    print(('sẽ xoá' if dry else 'đã xoá'), len(g), 'thư mục:', ', '.join(p.name for p in g) or '—')
