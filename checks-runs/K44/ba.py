"""K4.4 · trước/sau Tập 4–7: chạy một bộ luật của một cây checks/ trên gốc tạm (symlink tới tệp của tập; không ghi gì vào episodes/).
  python3 checks-runs/K44/ba.py <checks-dir> <tag> <out.json> [--rules A12,A13,...] [--eps ep004,...] [--override <ep>:<json-patch-file>]
page.json: out/checks/page.json của gốc tạm = bản lưu mới nhất của tập (run-c5*/page.json.gz) hoặc bản A29 --no-cache của K4.4 (Tập 6, 7) nếu có.
--override: patch JSON {"contract": {...merge...}, "claims_basis": "nominal"} áp lên BẢN SAO trong gốc tạm (giả lập việc bên dựng khai ở hợp đồng tập).
Thứ tự: mọi luật ghi vào out/checks của gốc tạm; cache ASR dùng chung qua K44_CACHE (mặc định /home/user/k44-cache/<ep>)."""
import gzip, json, os, shutil, sys, tempfile, time

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CHK, TAG, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
opt = lambda k, d=None: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
RULES = opt('--rules', 'A12,A13,R01,F11,P01,SH01,SH02,SH03,SH04,SH05,SH06,SH07,F13,F15,A14,S02,S07,S09').split(',')
EPS = opt('--eps', 'ep004,ep005,ep006,ep007').split(',')
OVR = {}
for i, a in enumerate(sys.argv):
    if a == '--override':
        ep, f = sys.argv[i + 1].split(':', 1)
        OVR[ep] = json.load(open(f))
sys.path.insert(0, os.path.join(os.path.abspath(CHK), 'py'))
import common, run as runner  # noqa: E402
R = {fn.rid: fn for fn in common.RULES}
A29 = '/home/user/a29-out'


def page_for(ep):
    p = os.path.join(A29, f'{ep}-nocache.json')
    if os.path.exists(p):
        return open(p, 'rb').read(), 'K4.4 A29 --no-cache (master bản giao)'
    E = os.path.join(REPO, 'episodes', ep, 'out', 'checks')
    runs = sorted(d for d in os.listdir(E) if d.startswith('run-c5') and os.path.exists(os.path.join(E, d, 'page.json.gz'))) if os.path.isdir(E) else []
    if runs:
        return gzip.open(os.path.join(E, runs[-1], 'page.json.gz')).read(), f'{runs[-1]}/page.json.gz'
    return None, None


def root_for(ep):
    E = os.path.join(REPO, 'episodes', ep)
    d = tempfile.mkdtemp(prefix=f'ba-{ep}-')
    for n in os.listdir(E):
        if n != 'out':
            os.symlink(os.path.join(E, n), os.path.join(d, n))
    os.mkdir(os.path.join(d, 'out'))
    for n in os.listdir(os.path.join(E, 'out')):
        if n != 'checks':
            os.symlink(os.path.join(E, 'out', n), os.path.join(d, 'out', n))
    cache = os.environ.get('K44_CACHE', f'/home/user/k44-cache/{ep}')
    os.makedirs(cache, exist_ok=True)
    os.makedirs(os.path.join(d, 'out', 'checks'))
    os.symlink(cache, os.path.join(d, 'out', 'checks', 'cache'))
    pg, src = page_for(ep)
    if pg:
        open(os.path.join(d, 'out', 'checks', 'page.json'), 'wb').write(pg)
    o = OVR.get(ep)
    if o:
        if 'contract' in o:
            c = json.load(open(os.path.join(E, 'contract.json')))
            for k, v in o['contract'].items():
                c[k] = {**c.get(k, {}), **v} if isinstance(v, dict) else v
            os.unlink(os.path.join(d, 'contract.json')); json.dump(c, open(os.path.join(d, 'contract.json'), 'w'))
        if 'claims_basis' in o:
            cj = json.load(open(os.path.join(E, 'out', 'claims.json')))
            lst = cj['claims'] if isinstance(cj, dict) else cj
            for c in lst:
                if '$' in str(c.get('display', '')) and c.get('basis') not in ('nominal', 'real'):
                    c['basis'] = o['claims_basis']
            os.unlink(os.path.join(d, 'out', 'claims.json')); json.dump(cj, open(os.path.join(d, 'out', 'claims.json'), 'w'))
    return d, src


res = {'checks': os.path.abspath(CHK), 'tag': TAG, 'overrides': OVR, 'episodes': {}}
for ep in EPS:
    d, src = root_for(ep)
    ctx = common.Ctx(d)
    row = {'page': src}
    for rid in RULES:
        if rid not in R:
            row[rid] = {'status': 'absent'}
            continue
        t0 = time.time()
        r = common.safe(R[rid], ctx)
        row[rid] = {'status': r['status'], 'fail': {m['name']: m['value'] for m in r.get('metrics', []) if not m['pass']},
                    'note': (r.get('note') or '')[:200], 'fingerprint': R[rid].meta['fingerprint'], 's': round(time.time() - t0, 1),
                    'details': json.loads(json.dumps(r.get('details'), default=str))[:3] if r['status'] != 'PASS' else None}
        print(ep, rid, row[rid]['status'], json.dumps(row[rid]['fail'], ensure_ascii=False)[:160], row[rid]['note'][:100], flush=True)
    res['episodes'][ep] = row
    shutil.rmtree(d, ignore_errors=True)
res['fingerprints'] = {fn.rid: fn.meta['fingerprint'] for fn in common.RULES}
json.dump(res, open(OUT, 'w'), indent=1, ensure_ascii=False)
