"""K4.2 — đối chứng nhiễu: mỗi nhiễu một khoá của out/model.json Tập 7 → S01 phải báo đúng khoá đó (và chỉ khoá đó).
  python3 checks-runs/K42/perturb_ep007.py <gốc worktree origin/ep007> [--out checks-runs/K42/ep007-perturb.json]"""
import copy, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'checks', 'py'))
import common, r_model  # noqa: E402,E401

ep = os.path.join(os.path.abspath(sys.argv[1]), 'episodes', 'ep007')
ctx = common.Ctx(ep, cache=os.path.join('/tmp', 'k42-cache'), contract=os.path.join(HERE, 'contract-ep007-draft.json'))
params = ctx.cfield('model', 'params')
base = json.load(open(os.path.join(ep, 'out', 'model.json')))


def q(k, v):
    def f(d):
        d['quantities'][k]['value'] = v
    return f


def era(i, f_, v):
    def f(d):
        d['eras'][i][f_] = v
    return f


def ser(col, i, v):
    def f(d):
        d['series'][col][i] = v
    return f


CASES = [  # (name, change, the key S01 must name, why)
    ('fallback_gap from rounded payments', q('fallback_gap_now', 612.54), 'fallback_gap_now', '2828.16 − 2215.62 (rounded inputs; brief: round only at output)'),
    ('interest_30on15 from rounded payment', q('interest_30on15_now', 210690), 'interest_30on15_now', '2948.28 × 180 − 320000'),
    ('interest_30full from rounded payment', q('interest_30full_now', 477623), 'interest_30full_now', '2215.62 × 360 − 320000'),
    ('yearly_lump from rounded need', q('yearly_lump', 8792.04), 'yearly_lump', '12 × 732.67'),
    ('months_at_pay15 as a payment count', q('months_at_pay15_now', 195), 'months_at_pay15_now', 'continuous formula 194.6, not 195 payments'),
    ('era2020 median r30 shown 6.3', q('era2020_median_r30', 6.3), 'era2020_median_r30', 'median 6.275: 6.28 / 6.27 are its roundings, 6.3 is display'),
    ('share_r30_ge_now strict >', q('share_r30_ge_now', 0.18), 'share_r30_ge_now', 'share ≥ now, rounded'),
    ('r30_min_week the last tie', q('r30_min_week', '2021-01-14'), 'r30_min_week', 'first week of the min'),
    ('yearly_lump_months 183', q('yearly_lump_months', 183), 'yearly_lump_months', 'simulation count'),
    ('era weeks 437', era(0, 'weeks', 437), 'eras[0].weeks', 'paired weeks of the 1990s era'),
    ('series extra_total one week', ser('extra_total', 100, 99999), 'series.extra_total[100]', 'one element of the weekly series'),
    ('series r15 one week', ser('r15', 5, 8.0), 'series.r15[5]', 'one rate of the weekly series'),
]
rows = []
for name, change, want, why in CASES:
    d = copy.deepcopy(base)
    change(d)
    _, bad, unrec = r_model.tpw_compare(ctx, params, d)
    keys = [b[0].split(' (')[0] for b in bad]
    rows.append({'case': name, 'why': why, 'want': want, 'got': keys, 'ok': keys == [want] and not unrec})
_, bad0, unrec0 = r_model.tpw_compare(ctx, params, base)
rep = {'baseline': {'mismatches': len(bad0), 'notRecomputed': len(unrec0)}, 'cases': rows, 'pass': f"{sum(r['ok'] for r in rows)}/{len(rows)}"}
print(json.dumps({'baseline': rep['baseline'], 'pass': rep['pass']}))
for r in rows:
    if not r['ok']:
        print('FAIL', r)
if '--out' in sys.argv:
    json.dump(rep, open(sys.argv[sys.argv.index('--out') + 1], 'w'), indent=1, ensure_ascii=False)
