"""K4.2 — kind term-pair-weekly-replay trên dữ liệu thật Tập 7: S01 (mọi khoá của out/model.json, eras, series) và mọi claim của numbers.md
(S05-style: giá trị ghi ở numbers.md so với bản tính lại của máy kiểm, sai số S05 của kind) + 8 bất biến.
  python3 checks-runs/K42/run_ep007.py <gốc worktree origin/ep007 (đã chạy data/fetch.py --verify)> [--out checks-runs/K42/ep007-kind.json]"""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'checks', 'py'))
import common, r_model  # noqa: E402,E401

root = os.path.abspath(sys.argv[1])
ep = os.path.join(root, 'episodes', 'ep007')
ctx = common.Ctx(ep, cache=os.path.join('/tmp', 'k42-cache'), contract=os.path.join(HERE, 'contract-ep007-draft.json'))
params = ctx.cfield('model', 'params')
out = json.load(open(os.path.join(ep, 'out', 'model.json')))
checked, bad, unrec = r_model.tpw_compare(ctx, params, out)
inv = r_model.tpw_invariants(ctx, params)
claims = []
for ln in open(os.path.join(ep, 'numbers.md'), encoding='utf-8'):
    m = re.match(r'^\| `([^`]+)` \| ([^|]+) \|', ln)
    if m:
        claims.append((m.group(1), m.group(2).strip()))
res, notkind = [], []
for cid, written in claims:
    try:
        v, tol = r_model.tpw_value(ctx, params, cid)
    except common.Missing:
        notkind.append(cid)
        continue
    if isinstance(v, r_model.Exact):
        ok, mine = v.same(written), v.v
    else:
        ok, mine = abs(float(written) - v) <= tol + 1e-9, v
    res.append({'claim': cid, 'numbers.md': written, 'kind': mine, 'tol': tol, 'ok': bool(ok)})
raw = os.path.join(ep, 'data', 'raw')
rep = {'root': ep, 'sha': {f: subprocess.run(['sha256sum', os.path.join(raw, f)], capture_output=True, text=True).stdout.split()[0]
                           for f in sorted(os.listdir(raw)) if f.endswith('.csv')},
       'S01': {'checked': checked, 'mismatches': bad, 'notRecomputed': unrec},
       'claims': {'rows': len(claims), 'compared': len(res), 'ok': sum(r['ok'] for r in res), 'mismatch': sum(not r['ok'] for r in res), 'notKind': notkind, 'detail': res},
       'invariants': [{k: m[k] for k in ('name', 'value', 'pass')} for m in inv]}
print(json.dumps({'S01': {'checked': checked, 'mismatches': len(bad), 'notRecomputed': len(unrec)},
                  'claims': {k: rep['claims'][k] for k in ('rows', 'compared', 'ok', 'mismatch', 'notKind')},
                  'invariants': f"{sum(m['pass'] for m in inv)}/{len(inv)}"}, ensure_ascii=False))
for b in bad[:30]:
    print('S01', b)
for u in unrec:
    print('UNREC', u)
for r in res:
    if not r['ok']:
        print('CLAIM', r)
for m in inv:
    if not m['pass']:
        print('INV', m['name'], m['value'])
if '--out' in sys.argv:
    json.dump(rep, open(sys.argv[sys.argv.index('--out') + 1], 'w'), indent=1, ensure_ascii=False, default=str)
