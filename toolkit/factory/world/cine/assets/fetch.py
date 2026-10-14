"""F-17 · tài sản CC0 của lớp cine (Poly Haven, polyhaven.com — mọi tài sản CC0). Chép rnd-hybrid/v4/assets/fetch.py, đổi chỗ chứa.
  python3 toolkit/factory/world/cine/assets/fetch.py          → tải tệp còn thiếu, kiểm SHA-256 với manifest.json (lệch = dừng, thoát 1)
  python3 toolkit/factory/world/cine/assets/fetch.py --verify → chỉ kiểm SHA-256 mọi tệp (không tải)
Tệp ≤ 2 MB (`commit: true`) nằm trong git ở cc0/; tệp lớn hơn tải lúc dựng vào dl/ (.gitignore) và cine.js đọc từ đó. RIGHTS.md §F9."""
import hashlib, json, os, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); MAN = json.load(open(os.path.join(HERE, 'manifest.json')))
LIMIT = 2_000_000


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


if __name__ == '__main__':
    bad = 0
    for k, m in MAN.items():
        if m['commit'] != (m['bytes'] <= LIMIT): sys.exit(f'{k}: cờ commit sai với cỡ {m["bytes"]}')
        p = os.path.join(HERE, 'cc0' if m['commit'] else 'dl', m['file'])
        if not os.path.exists(p):
            if '--verify' in sys.argv: print('THIẾU', k); bad += 1; continue
            os.makedirs(os.path.dirname(p), exist_ok=True); urllib.request.urlretrieve(m['url'], p + '.part'); os.replace(p + '.part', p)
        h = sha(p)
        if h != m['sha256']: print('SHA-256 LỆCH', k, h); bad += 1; continue
        print(k, m['bytes'], h[:16])
    sys.exit(1 if bad else 0)
