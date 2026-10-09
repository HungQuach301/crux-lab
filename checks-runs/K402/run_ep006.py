"""K4.0.2 — kind fixed-raise-vs-index-windows trên dữ liệu thật Tập 6: S01 (mọi khoá của out/model.json) và mọi claim của numbers.md (S05-style, giá trị
chưa làm tròn của file mô hình so với bản tính lại của máy kiểm, sai số của kind) + bất biến.
  python3 checks-runs/K402/run_ep006.py <gốc ep006 (worktree origin/ep006, đã chạy data/fetch.py --verify)> [--out checks-runs/K402/ep006-kind.json]"""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'checks', 'py'))
import common, r_model  # noqa: E402,E401

root = os.path.abspath(sys.argv[1])
ep = os.path.join(root, 'episodes', 'ep006')
ctx = common.Ctx(ep, cache=os.path.join('/tmp', 'k402-cache'), contract=os.path.join(HERE, 'contract-ep006-draft.json'))
params = ctx.cfield('model', 'params')
out = json.load(open(os.path.join(ep, 'out', 'model.json')))
checked, bad, unrec = r_model.frw_compare(ctx, params, out)
inv = r_model.frw_invariants(ctx, params)
# claims: every row of numbers.md "| `id` | value | …" ; the model value of the id (raw key or derived key) vs the kind's value()
claims = []
for ln in open(os.path.join(ep, 'numbers.md'), encoding='utf-8'):
    m = re.match(r'^\| `([^`]+)` \| ([^|]+) \|', ln)
    if m:
        claims.append((m.group(1), m.group(2).strip()))
res, n_ok, n_bad, notkind = [], 0, 0, []
for cid, shown in claims:
    for k in [x.strip() for x in cid.split('/')]:
        try:
            v, tol = r_model.frw_value(ctx, params, k)
        except common.Missing as e:
            notkind.append(k)
            continue
        raw = out['raw'].get(k)
        if raw is None and k not in out['raw']:     # derived key: compare with numbers.md's written value (rounded): tolerance of the display
            try:
                w = float(re.sub(r'[^0-9.\-]', '', shown.split('/')[0]))
            except ValueError:
                w = shown
            if isinstance(v, r_model.Exact):
                ok = v.same(w)
            elif isinstance(v, r_model.Month):
                ok = r_model.ym(shown.split('/')[0].strip()) == int(v)
            else:
                dec = len(shown.split('.')[1].split()[0].rstrip('%')) if '.' in shown.split()[0] else 0
                ok = abs(w - v) <= 0.5 * 10 ** -dec + 1e-9
            how = 'numbers.md (rounded)'
        elif isinstance(v, r_model.Exact):
            ok, how = v.same(raw), 'raw'
        elif isinstance(v, r_model.Month):
            ok, how = r_model.ym(raw) == int(v), 'raw'
        else:
            ok, how = abs(float(raw) - v) <= max(tol, 0) + 1e-12, 'raw'
        res.append({'claim': k, 'kind': (str(v.v) if isinstance(v, r_model.Exact) else r_model.ym_str(v) if isinstance(v, r_model.Month) else v),
                    'model': raw if how == 'raw' else shown, 'against': how, 'ok': bool(ok)})
        n_ok += bool(ok); n_bad += (not ok)
rep = {'root': ep, 'sha': {f: subprocess.run(['sha256sum', os.path.join(ep, 'data', 'raw', f)], capture_output=True, text=True).stdout.split()[0]
                           for f in sorted(os.listdir(os.path.join(ep, 'data', 'raw'))) if f.endswith('.csv')},
       'S01': {'checked': checked, 'mismatches': bad, 'notRecomputed': unrec},
       'claims': {'rows': len(claims), 'compared': len(res), 'ok': n_ok, 'mismatch': n_bad, 'notKind': notkind, 'detail': res},
       'invariants': [{k: m[k] for k in ('name', 'value', 'pass')} for m in inv]}
print(json.dumps({'S01': {'checked': checked, 'mismatches': len(bad), 'notRecomputed': len(unrec)}, 'claims': {k: rep['claims'][k] for k in ('rows', 'compared', 'ok', 'mismatch', 'notKind')},
                  'invariants': f"{sum(m['pass'] for m in inv)}/{len(inv)}"}, ensure_ascii=False))
for b in bad[:30]:
    print('S01', b)
for r in res:
    if not r['ok']:
        print('CLAIM', r)
for m in inv:
    if not m['pass']:
        print('INV', m['name'], m['value'])
if '--out' in sys.argv:
    json.dump(rep, open(sys.argv[sys.argv.index('--out') + 1], 'w'), indent=1, ensure_ascii=False, default=str)
