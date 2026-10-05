"""Tập 3: tải lại dữ liệu FRED đã ghim (coed=2026-08-01) và kiểm SHA-256 với hồ sơ retire-4.
Dữ liệu không commit (E1-A2/E2-A1). `--verify`: chỉ kiểm file đã có. `--retire3`: thêm GS1, GS5 (chỉ để kiểm đặc tả dùng lại).
C5 (S03/S04): chuỗi đối chiếu DTB3 (lãi bill 3 tháng theo ngày, H.15, coed=2026-08-31) ghim SHA; data/DTB3_monthly.csv = trung bình
các ngày có số của mỗi tháng (cùng cách H.15 tính TB3MS), so với TB3MS trong contract.json data.crosscheck."""
import hashlib, json, os, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'raw')
PIN = {'TB3MS': 'ebf04b1ae5bc5729ba3bb2b35dbb0e0c5e22dace36bea0c02632782d625ae6ab',
       'CPIAUCNS': 'f79e3a78837142293449cee4a1a9b1da7be677fb3e989ffb2ef48e8e7cf4cdd7'}
EXTRA = ['GS1', 'GS5']
CROSS = {'DTB3': 'b2681e0a9a26da1cf15c2d9c7b6803e1976fa9fb5aaa046a4993aa698e8d3b1b'}
URL_DAILY = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id={}&coed=2026-08-31'
URL = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id={}&coed=2026-08-01'


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def main():
    os.makedirs(RAW, exist_ok=True)
    ids = list(PIN) + list(CROSS) + (EXTRA if '--retire3' in sys.argv else [])
    ok = True
    for s in ids:
        p = os.path.join(RAW, f'{s}.csv')
        if '--verify' not in sys.argv or not os.path.exists(p):
            urllib.request.urlretrieve((URL_DAILY if s in CROSS else URL).format(s), p)
        h = sha(p)
        good = {**PIN, **CROSS}.get(s, h) == h
        ok &= good
        print(s, h, 'OK' if good else 'SHA KHÁC BẢN ĐÓNG BĂNG')
    # K3.7 contract paths (model.params.roll/deflator.file = data/<series>.csv): same bytes as raw/, not committed
    import shutil
    for k in list(PIN) + list(CROSS):
        shutil.copyfile(os.path.join(RAW, f'{k}.csv'), os.path.join(HERE, f'{k}.csv'))
    # monthly mean of the daily cross-check series (days with a value only; "." / empty = no observation)
    import csv
    days = {}
    for r in list(csv.reader(open(os.path.join(RAW, 'DTB3.csv'))))[1:]:
        if r[1] not in ('', '.'):
            days.setdefault(r[0][:7] + '-01', []).append(float(r[1]))
    with open(os.path.join(HERE, 'DTB3_monthly.csv'), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['observation_date', 'DTB3_mean', 'days'])
        for k in sorted(days):
            w.writerow([k, f'{sum(days[k]) / len(days[k]):.6f}', len(days[k])])
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
