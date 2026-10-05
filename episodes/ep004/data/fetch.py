"""Tập 4 (Việc 0): tải lại dữ liệu FRED đúng URL ghim trong hồ sơ topics-r1/machine/tax-2/sources.json và kiểm SHA-256
với bản đóng băng của hồ sơ. Dữ liệu không commit (như Tập 3). `--verify`: chỉ kiểm file đã có.
SHA khác → in "SHA KHÁC BẢN ĐÓNG BĂNG" (FHFA sửa số hằng quý) và thoát 1; số mới vẫn được tính lại để so (numbers.md ghi lệch)."""
import hashlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
DOSSIER = os.path.join(ROOT, 'topics-r1', 'machine', 'tax-2', 'sources.json')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def main():
    src = json.load(open(DOSSIER))['series']
    ok = True
    for s in src:
        p = os.path.join(HERE, f"{s['id']}.csv")
        if '--verify' not in sys.argv or not os.path.exists(p):
            # curl qua proxy phiên (urllib bị proxy ngắt kết nối 2026-10-05); thử lại 4 lần
            subprocess.run(['curl', '-sSfL', '--retry', '4', '--retry-all-errors', '-o', p, s['url']], check=True)
        h = sha(p); pin = s.get('sha256')
        good = pin == h
        ok &= good
        print(s['id'], h[:16], 'OK' if good else f'SHA KHÁC BẢN ĐÓNG BĂNG (hồ sơ {str(pin)[:16]})')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
