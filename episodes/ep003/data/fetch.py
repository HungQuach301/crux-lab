"""Tập 3: tải lại dữ liệu FRED đã ghim (coed=2026-08-01) và kiểm SHA-256 với hồ sơ retire-4.
Dữ liệu không commit (E1-A2/E2-A1). `--verify`: chỉ kiểm file đã có. `--retire3`: thêm GS1, GS5 (chỉ để kiểm đặc tả dùng lại)."""
import hashlib, json, os, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'raw')
PIN = {'TB3MS': 'ebf04b1ae5bc5729ba3bb2b35dbb0e0c5e22dace36bea0c02632782d625ae6ab',
       'CPIAUCNS': 'f79e3a78837142293449cee4a1a9b1da7be677fb3e989ffb2ef48e8e7cf4cdd7'}
EXTRA = ['GS1', 'GS5']
URL = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id={}&coed=2026-08-01'


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def main():
    os.makedirs(RAW, exist_ok=True)
    ids = list(PIN) + (EXTRA if '--retire3' in sys.argv else [])
    ok = True
    for s in ids:
        p = os.path.join(RAW, f'{s}.csv')
        if '--verify' not in sys.argv or not os.path.exists(p):
            urllib.request.urlretrieve(URL.format(s), p)
        h = sha(p)
        good = PIN.get(s, h) == h
        ok &= good
        print(s, h, 'OK' if good else 'SHA KHÁC BẢN ĐÓNG BĂNG')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
