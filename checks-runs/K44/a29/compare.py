"""K4.4.1 · A29: so page.json của lượt có cache (cold: cache trống → điền; warm: cache đầy) với lượt --no-cache, cùng trang + cùng master + cùng mã (b0e529ae).
Trường bỏ qua: chỉ hai trường đo lượt chạy — `seconds` (giờ máy) và `sceneCacheHits` (số cảnh lấy từ cache). Chuẩn hoá: URL `blob:null/<uuid>` →
`blob:null/*` (trang một-file nạp module qua blob: UUID ngẫu nhiên mỗi lần nạp trang — hai lượt --no-cache cũng khác ở đây). Mọi thứ khác phải trùng
từng byte (json.dumps sort_keys, separators gọn).
  python3 checks-runs/K44/a29/compare.py <a29-out dir> <out.json>"""
import hashlib, json, os, re, sys
D, OUT = sys.argv[1], sys.argv[2]
RUN = ('seconds', 'sceneCacheHits')
canon = lambda p: re.sub(r'blob:null/[0-9a-f-]{36}', 'blob:null/*', json.dumps({k: v for k, v in json.load(open(p)).items() if k not in RUN}, sort_keys=True, separators=(',', ':'), ensure_ascii=False))
runs = [json.loads(l) for l in open(os.path.join(D, 'runs.jsonl')) if l.startswith('{')]
res = {'ignored': RUN, 'runs': runs, 'episodes': {}}
for ep in ('ep006', 'ep007'):
    base = os.path.join(D, f'{ep}-nocache.json')
    if not os.path.exists(base):
        continue
    b = canon(base); r = {'nocache_sha256': hashlib.sha256(b.encode()).hexdigest()}
    for tag in ('cold', 'warm'):
        p = os.path.join(D, f'{ep}-{tag}.json')
        if os.path.exists(p):
            c = canon(p); raw = json.load(open(p))
            r[tag] = {'sha256': hashlib.sha256(c.encode()).hexdigest(), 'identical': c == b, 'sceneCacheHits': raw.get('sceneCacheHits'),
                      'sceneJobs': raw.get('sceneJobs'), 'seconds': raw.get('seconds')}
            if c != b:   # first differing key
                A, B = json.loads(b), json.loads(c)
                r[tag]['diffKeys'] = [k for k in sorted(set(A) | set(B)) if A.get(k) != B.get(k)][:20]
    r['nocache_seconds'] = json.load(open(base)).get('seconds')
    res['episodes'][ep] = r
json.dump(res, open(OUT, 'w'), indent=1)
print(json.dumps(res['episodes'], indent=1))
