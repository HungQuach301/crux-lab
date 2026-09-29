#!/usr/bin/env python3
"""H3: build src/data.js (NOT committed: holds FRED weekly values, E1-A2) from the episode's local data + model.

Inputs: episodes/ep001/data/normalized/mortgage30_weekly.csv (re-create with data/fetch.py --verify),
        episodes/ep001/out/model.json, episodes/ep001/out/claims.json.
Every number printed on screen comes from claims.json `display`; the rest (bar lengths, block heights) is recomputed
here with the model's amortisation convention and asserted against the claims.
"""
import csv, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
model = json.load(open(os.path.join(EP, 'out', 'model.json')))
claims = {c['claimId']: c for c in json.load(open(os.path.join(EP, 'out', 'claims.json')))['claims']}
sc = model['scenario']
R_OLD, R_NEW = sc['oldRate'], sc['todayRate']


def pmt(P, r, n):
    r /= 1200
    return P * r / (1 - (1 + r) ** -n)


def bal(P, r, n, k):
    """balance after k payments of a level-payment loan"""
    p, b, r = pmt(P, r, n), P, r / 1200
    for _ in range(k):
        b = b * (1 + r) - p
    return b


def char_paths(ch, months=36):
    c = model['characters'][ch]
    B = c['balance']
    po, pn = pmt(B, R_OLD, 360 - sc['paymentsMade']), pmt(B, R_NEW, 360)
    sav = po - pn
    assert abs(sav - c['monthlySavings']) < 0.01, (ch, sav)
    gap = [bal(B, R_NEW, 360, k) - bal(B, R_OLD, 360 - sc['paymentsMade'], k) for k in range(months + 1)]
    be = next(k for k in range(1, 400) if k * sav - (bal(B, R_NEW, 360, k) - bal(B, R_OLD, 360 - sc['paymentsMade'], k)) >= c['cost'])
    assert be == c['withBalance'], (ch, be)
    return {'cost': c['cost'], 'sav': sav, 'gap': gap, 'be': be, 'loan': c['loan']}


# F1: weekly PMMS 2025-12 .. anchor; savings if the median borrower refinanced that week (k payments made, k35 rule)
rows = [(d, float(r)) for d, r in csv.reader(open(os.path.join(EP, 'data', 'normalized', 'mortgage30_weekly.csv'))) if d != 'date']
weeks = [(d, r) for d, r in rows if '2025-12-01' <= d <= sc['todayWeek']]
L = model['characters']['median']['loan']
old_p = pmt(L, R_OLD, 360)
f1 = []
for d, r in weeks:
    y, m = int(d[:4]), int(d[5:7])
    k = (y - 2023) * 12 + m - 10
    B = bal(L, R_OLD, 360, k)
    f1.append({'d': d, 'r': r, 'sav': old_p - pmt(B, r, 360)})
low = min(f1, key=lambda w: w['r'])
assert low['d'] == claims['low2026']['value'] if isinstance(claims['low2026']['value'], str) else True
assert f'${round(low["sav"]):,}' == claims['sav_low2026_median']['display'], low
assert f'{low["r"]:.2f}%' == claims['low2026']['display']
thr = R_OLD - 1
last_in = max(w['d'] for w in f1 if w['r'] <= thr + 1e-9)
assert last_in == claims['cut1_last_2026']['value'], (last_in, claims['cut1_last_2026']['value'])

med = char_paths('median')
assert f'${round(med["gap"][24]):,}' == claims['gap24']['display']
data = {
    'claims': {k: {'display': v['display'], 'illustrative': v.get('illustrative', False)} for k, v in claims.items()},
    'f1': {'weeks': f1, 'rOld': R_OLD, 'thr': thr, 'lastIn': last_in, 'low': low['d']},
    'median': med, 'small': char_paths('small'), 'large': char_paths('large'),
}
out = os.path.join(HERE, 'data.js')
open(out, 'w').write('window.DATA = ' + json.dumps(data) + ';\n')
print('wrote', out, len(f1), 'weeks; low', low['d'], round(low['sav'], 1), '; last in window', last_in,
      '; be', med['be'], data['small']['be'], data['large']['be'])
for ch in ('small', 'large'):
    d = data[ch]
    print(ch, 'filled at 36:', round((36 * d['sav']) / (d['cost'] + d['gap'][36]), 3))
