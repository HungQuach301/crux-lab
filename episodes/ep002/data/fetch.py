"""Tải lại TB3MS (FRED) cho Tập 2. Dữ liệu thô KHÔNG commit (lessons A9).
python3 episodes/ep002/data/fetch.py [--verify]
--verify: tải từ URL ghim (coed = lastObservation) và kiểm SHA-256 với data/sources.json."""
import hashlib, json, os, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = json.load(open(os.path.join(HERE, 'sources.json')))

def get(url):
    for i in range(5):
        try:
            return urllib.request.urlopen(url, timeout=60).read()
        except Exception as e:
            if i == 4: raise
            time.sleep(2 ** (i + 1))

for f in SRC['files']:
    out = os.path.join(HERE, f['path'])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.exists(out) and '--verify' not in sys.argv:
        continue
    b = get(f['url'])
    h = hashlib.sha256(b).hexdigest()
    if h != f['sha256']:
        sys.exit(f"SHA lệch {f['path']}: {h} != {f['sha256']} (nguồn đã sửa số hoặc thêm quan sát)")
    open(out, 'wb').write(b)
    print('ok', f['path'], h[:12])

# chuẩn hoá cho checks S04 (data.crosscheck)
import csv, collections
norm = os.path.join(HERE, 'normalized'); os.makedirs(norm, exist_ok=True)
tb = [r for r in list(csv.reader(open(os.path.join(HERE, 'raw/TB3MS.csv'))))[1:] if r[1] not in ('', '.')]
with open(os.path.join(norm, 'tb3ms_monthly.csv'), 'w') as f:
    f.write('month,rate\n'); [f.write(f"{d[:7]},{v}\n") for d, v in tb]
dd = collections.defaultdict(list)
for d, v in list(csv.reader(open(os.path.join(HERE, 'raw/DTB3.csv'))))[1:]:
    if v not in ('', '.'): dd[d[:7]].append(float(v))
with open(os.path.join(norm, 'dtb3_monthly_mean.csv'), 'w') as f:
    f.write('month,rate\n'); [f.write(f"{m},{sum(v)/len(v):.6f}\n") for m, v in sorted(dd.items())]
print('normalized ok')
