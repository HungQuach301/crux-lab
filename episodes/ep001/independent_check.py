"""Independent check ("kiểm độc lập") of Episode 1's model claims against the K2 checker's own re-computation.

    python3 episodes/ep001/data/fetch.py --verify      # the FRED files are not in the repo
    python3 episodes/ep001/independent_check.py        # writes out/checks/independent.json + .md

1. Runs the number rules of the locked checker that need no video or voice (checks/py/run.py --only S01,S03,S04,S05,S06,S16,F11,
   T1,L1,V04,V09 on this episode root) -> out/checks/report-partial.json/.md (the checker writes them).
2. Compares EVERY model claim of out/claims.json (claims with a `model` field, and the claims the contract maps in model.claims) with
   a quantity computed by the checker's functions (checks/py/r_model.py: payment, balance_after, be_simple, be_balance, net_after,
   cut_for, history). Only the aggregation over the checker's history (min, max, counts, the example episode) is written here; every
   month, rate, balance and break-even comes from the checker. The builder's model/refi.py is not imported. checks/ is only read.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'checks', 'py'))
import common  # noqa: E402  (checker, read only)
import r_model as R  # noqa: E402

RULES = 'S01,S03,S04,S05,S06,S07,S08,S09,S10,S11,S12,S13,S14,S15,S16,A13,A15,R02,F11,T1,L1,V04,V09'
WHY_MISSING = {
    'S06': 'needs out/checks/page.json (page sampler on the rendered page: yearsTrack/casesTrack); no page yet (M2)',
    'S07': 'needs out/checks/page.json (numbers on screen)', 'S08': 'needs out/checks/page.json', 'S09': 'needs out/checks/page.json',
    'S11': 'needs out/checks/page.json', 'S12': 'needs out/checks/page.json', 'S14': 'needs out/video.mp4 (master silences)', 'A15': 'needs out/video.mp4 (ASR on the master)',
    'V04': 'page rule: needs out/checks/page.json (rendered page)',
    'V09': 'page rule: needs out/checks/page.json (rendered page)',
    'T1': 'needs the stems and out/video.mp4; on the animatic stems (scratch root) still MISSING: out/video.mp4',
    'L1': 'needs the stems; on the animatic stems (scratch root, out/checks/animatic-T1-L1.json): PASS, 29.2 dB, 0 key words lost',
}


def months_between(a, b):
    return (int(b[:4]) - int(a[:4])) * 12 + int(b[5:7]) - int(a[5:7])


def checker_values(ctx, P):
    sc, chars, h = P['scenario'], P['characters'], P['history']
    n, k, r0, rt = int(sc['termMonths']), int(sc['paymentsMade']), float(sc['oldRate']), float(sc['todayRate'])
    v = {}
    for name in chars:
        for f in ('loan', 'cost', 'monthlySavings', 'simple', 'withBalance', 'net36', 'net84', 'cut36'):
            v[f'{name}.{f}'] = R.refi_value(ctx, P, f'{name}.{f}')
    L, C = float(chars['median']['loan']), float(chars['median']['cost'])
    bal = R.balance_after(L, r0, n, k)
    s_ = R.be_simple(L, r0, bal, rt, C, n)
    v['gap'] = (R.balance_after(bal, rt, n, s_) - R.balance_after(L, r0, n, k + s_), 0.5)
    for cut, key in ((0.25, '025'), (0.5, '05'), (1.0, '10')):
        v[f'simple@{key}'] = (R.be_simple(L, r0, bal, r0 - cut, C, n), 0)
        v[f'bal@{key}'] = (R.be_balance(L, r0, k, bal, r0 - cut, C, n), 0)
    hist, _, _ = R.history(ctx, h)
    one = [(e, c) for e in hist for c in e['cases'] if c['spread'] == 1.0 and c['reached']]
    bes = [c['breakEvenMonths'] for _, c in one if c['breakEvenMonths']]
    further = [(e, c) for e, c in one if c['beforeBreakEvenAnotherDrop']]
    ex_e, ex_c = further[-1]
    e23 = next(c for e, c in one if e['peak'] == '2023-10')
    e81 = next(c for e, c in one if e['peak'].startswith('1981'))
    v.update({'n_eps': (len(hist), 0), 'beh_min': (min(bes), 0), 'beh_max': (max(bes), 0),
              'behs_min': (min(c['breakEvenSimple'] for _, c in one), 0), 'behs_max': (max(c['breakEvenSimple'] for _, c in one), 0),
              'n_further': (len(further), 0), 'n_nofurther': (len(one) - len(further), 0), 'ex_be': (ex_c['breakEvenMonths'], 0),
              'ex_gap': (months_between(ex_c['refiMonth'], ex_c['beforeBreakEvenAnotherDrop']), 0), 'be23': (e23['breakEvenMonths'], 0),
              'm81': (e81['monthsOnOldLoan'], 0), 'be81': (e81['breakEvenMonths'], 0)})
    # the same history with the cost share of the small band (by year) and of the large conforming band (HMDA 2025 only -> every year)
    hs = dict(h, spreads=[1.0], costShares=dict(h['costShares'], filter={'purpose': 'refinance (31)', 'loanSize': 'under $150k'}))
    bs = [c['breakEvenMonths'] for e in R.history(ctx, hs)[0] for c in e['cases'] if c['reached'] and c['breakEvenMonths']]
    hl = dict(h, spreads=[1.0], costShares={'file': 'data/normalized/hmda_refi31_conforming.csv', 'filter': {'purpose': 'refinance (31)', 'loanSize': '$600k-<$720k, conforming (C)'},
                                            'yearColumn': 'year', 'shareColumn': 'cost_p50_pct'})
    bl = [c['breakEvenMonths'] for e in R.history(ctx, hl)[0] for c in e['cases'] if c['reached'] and c['breakEvenMonths']]
    v.update({'behd_min': (min(bs), 0), 'behd_max': (max(bs), 0), 'behl_max': (max(bl), 0)})
    # the median character refinancing at the 2026 low (claims *_low2026_median): the checker's functions with that week's rate and k.
    # The week and its rate are read here from the weekly CSV (plain csv module; the builder's refi.py is not imported).
    import csv
    rows = [(r['date'], float(r['rate'])) for r in csv.DictReader(open(os.path.join(HERE, 'data', 'normalized', 'mortgage30_weekly.csv')))]
    lo = min((x for x in rows if x[0][:4] == '2026'), key=lambda x: x[1])
    k26 = months_between('2023-10', lo[0][:7])
    b26 = R.balance_after(L, r0, n, k26)
    v.update({'sav_low2026_median': (R.payment(L, r0, n) - R.payment(b26, lo[1], n), 0.5),
              'be_simple_low2026_median': (R.be_simple(L, r0, b26, lo[1], C, n), 0),
              'be_bal_low2026_median': (R.be_balance(L, r0, k26, b26, lo[1], C, n), 0)})
    return v


def key_of(cid, contract):
    mapped = contract['model']['claims']
    if cid in mapped:
        return mapped[cid]
    for pre, suf in (('be_simple_', 'simple@'), ('be_bal_', 'bal@')):
        if cid.startswith(pre) and cid[len(pre):] in ('025', '05', '10'):
            return suf + cid[len(pre):]
    return {'gap24': 'gap'}.get(cid, cid)


def main():
    out = subprocess.run([sys.executable, os.path.join(REPO, 'checks', 'py', 'run.py'), HERE, '--only', RULES], capture_output=True, text=True)
    print(out.stdout[-1500:], out.stderr[-1500:])
    rep = json.load(open(os.path.join(HERE, 'out', 'checks', 'report-partial.json')))
    ctx = common.Ctx(HERE)
    contract = json.load(open(os.path.join(HERE, 'contract.json')))
    P = contract['model']['params']
    vals = checker_values(ctx, P)
    claims = json.load(open(os.path.join(HERE, 'out', 'claims.json')))['claims']
    model_claims = [c for c in claims if c.get('model') or c['claimId'] in contract['model']['claims']]
    rows, bad = [], []
    for c in model_claims:
        key = key_of(c['claimId'], contract)
        if key not in vals:
            bad.append({'claim': c['claimId'], 'ours': c['value'], 'checker': None, 'why': f'no checker quantity for key {key}'})
            continue
        mine, tol = vals[key]
        tol = max(tol, 0.005) if key.endswith('cut36') else tol  # claims show the cut rounded to 2 decimals
        ours = c['value']
        ok = (ours is None and mine is None) or (ours is not None and mine is not None and abs(float(ours) - float(mine)) <= tol + 1e-9)
        rows.append({'claim': c['claimId'], 'key': key, 'ours': ours, 'checker': round(mine, 4) if isinstance(mine, float) else mine, 'tolerance': tol, 'match': ok})
        if not ok:
            bad.append(rows[-1])
    n_ok = sum(r['match'] for r in rows)
    res = {r['id']: {'status': r['status'], 'failing': [f"{m['name']} = {m['value']}" for m in r['metrics'] if not m['pass']], 'note': r.get('note')} for r in rep['results']}
    for rid, why in WHY_MISSING.items():
        if res.get(rid, {}).get('status') == 'MISSING':
            res[rid]['why'] = why
    if res.get('F11', {}).get('status') == 'FAIL':
        res['F11']['why'] = 'every CONTRACT.md release file is declared in artefacts.M3; the video, voice, stems and render files are not produced yet (M3)'
    s01 = next(r for r in rep['results'] if r['id'] == 'S01')
    report = {'lock': rep['lock'], 'root': 'episodes/ep001', 'contract': 'episodes/ep001/contract.json',
              'modelClaims': {'total': len(model_claims), 'match': n_ok, 'pct': round(100 * n_ok / len(model_claims), 1), 'mismatches': bad},
              'S01': {m['name']: m['value'] for m in s01['metrics']}, 'rules': res, 'claims': rows}
    json.dump(report, open(os.path.join(HERE, 'out', 'checks', 'independent.json'), 'w'), indent=1, ensure_ascii=False, default=str)
    with open(os.path.join(HERE, 'out', 'checks', 'independent.md'), 'w') as f:
        f.write(f"# Episode 1: independent check (K2 lock `{rep['lock'][:8]}`)\n\n"
                f"Model claims vs the checker's re-computation (checks/py/r_model.py): **{n_ok}/{len(model_claims)} match ({report['modelClaims']['pct']}%)**. "
                f"S01 on out/model.json: {report['S01']}.\n\n| rule | status | failing | why |\n|---|---|---|---|\n")
        for rid, r in res.items():
            f.write(f"| {rid} | {r['status']} | {'; '.join(r['failing']) or ''} | {r.get('why') or r.get('note') or ''} |\n")
        f.write('\n## Mismatches\n\n' + ('\n'.join(f"- {b['claim']}: ours {b['ours']}, checker {b['checker']}" for b in bad) or 'none') + '\n')
        f.write('\n## Claims\n\n| claim | checker key | ours | checker | match |\n|---|---|---|---|---|\n')
        for r in rows:
            f.write(f"| {r['claim']} | {r['key']} | {r['ours']} | {r['checker']} | {'yes' if r['match'] else 'NO'} |\n")
    print(json.dumps({k: report['modelClaims'][k] for k in ('total', 'match', 'pct')}), {k: v['status'] for k, v in res.items()})
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
