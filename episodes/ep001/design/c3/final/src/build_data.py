#!/usr/bin/env python3
"""C3 final: build src/data.js (NOT committed: holds FRED weekly values, E1-A2) from local data + the episode model.

Inputs: episodes/ep001/data/normalized/mortgage30_weekly.csv (re-create with data/fetch.py --verify),
        episodes/ep001/out/model.json, episodes/ep001/out/claims.json, episodes/ep001/model/refi.py.
Every number printed on screen comes from claims.json `display` (CL() in engine.js). Object sizes (heights, bar
lengths, the window's weeks) are recomputed here with model/refi.py and asserted against the claims.
"""
import csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(EP, 'model'))
import refi  # noqa: E402

model = json.load(open(os.path.join(EP, 'out', 'model.json')))
claims = {c['claimId']: c for c in json.load(open(os.path.join(EP, 'out', 'claims.json')))['claims']}
sc = model['scenario']
R_OLD, R_NEW, K = sc['oldRate'], sc['todayRate'], sc['paymentsMade']
disp = lambda i: claims[i]['display']
money = lambda v: f'${round(v):,}'


def paths(ch, new_rate=R_NEW, months=36):
    c = model['characters'][ch]
    L, cost = c['loan'], c['cost']
    B = refi.balance_after(L, R_OLD, 360, K)
    sav = refi.payment(L, R_OLD, 360) - refi.payment(B, new_rate, 360)
    old_paid = [B - refi.balance_after(L, R_OLD, 360, K + m) for m in range(months + 1)]
    new_paid = [B - refi.balance_after(B, new_rate, 360, m) for m in range(months + 1)]
    gap = [o - n for o, n in zip(old_paid, new_paid)]
    be = refi.break_even_balance(L, R_OLD, K, new_rate, cost)
    return dict(loan=L, cost=cost, sav=sav, oldPaid=old_paid, newPaid=new_paid, gap=gap, be=be,
                oldPayment=refi.payment(L, R_OLD, 360))


med, small, large = paths('median'), paths('small'), paths('large')
assert money(med['sav']) == disp('sav_median') and money(med['gap'][24]) == disp('gap24'), (med['sav'], med['gap'][24])
assert med['be'] == int(disp('be_bal_median')) and small['be'] == int(disp('be_bal_small')) and large['be'] == int(disp('be_bal_large'))
assert money(small['sav']) == disp('sav_small') and money(large['sav']) == disp('sav_large')
assert refi.break_even_months(med['cost'], med['sav']) == int(disp('be_simple_median'))
# net after 36 months (selling at year 3) = 36*sav - gap36 - cost
assert money(-(36 * small['sav'] - small['gap'][36] - small['cost'])) == disp('net36_small')
assert money(36 * large['sav'] - large['gap'][36] - large['cost']) == disp('net36_large')

# F1: weekly PMMS 2025-07 .. anchor week; the window = weeks at least 1 point below Nora's rate
rows = [(d, float(r)) for d, r in csv.reader(open(os.path.join(EP, 'data', 'normalized', 'mortgage30_weekly.csv'))) if d != 'date']
thr = R_OLD - float(claims['s10']['value'])
weeks = [{'d': d, 'r': r, 'in': r <= thr + 1e-9} for d, r in rows if '2025-07-01' <= d <= sc['todayWeek']]
low = min((w for w in weeks if w['d'] >= '2026-01-01'), key=lambda w: w['r'])
assert f"{low['r']:.2f}%" == disp('low2026') and low['d'] == claims['low2026_date']['value']
last_in = max(w['d'] for w in weeks if w['in'])
assert last_in == claims['cut1_last_2026']['value']
assert sum(1 for w in weeks if w['in'] and w['d'].startswith('2026')) == int(disp('weeks_below_r_old_minus_1'))
assert weeks[-1]['d'] == claims['anchor_date']['value'] and f"{weeks[-1]['r']:.2f}%" == disp('r_today')
# $459: the median borrower refinancing in the low week (k_low2026 payments made)
kl = int(disp('k_low2026'))
Bl = refi.balance_after(375000.0, R_OLD, 360, kl)
sav_low = refi.payment(375000.0, R_OLD, 360) - refi.payment(Bl, low['r'], 360)
assert money(sav_low) == disp('sav_low2026_median'), sav_low

# S11: a quarter-point cut, to the old loan's last payment
c025 = float(claims['s025']['value'])
q = paths('median', R_OLD - c025, 360 - K)
assert refi.break_even_months(q['cost'], q['sav']) == int(disp('be_simple_025')) and q['be'] is None
q_net = [m * q['sav'] - q['gap'][m] for m in range(len(q['gap']))]
assert max(q_net) < q['cost']

data = {
    'claims': {k: {'display': v['display'], 'illustrative': v.get('illustrative', False)} for k, v in claims.items()},
    'f1': {'weeks': weeks, 'rOld': R_OLD, 'thr': thr, 'lastIn': last_in, 'low': low['d'],
           'oldPayment': med['oldPayment'], 'savLow': sav_low},
    'median': med, 'small': small, 'large': large,
    'q025': {'sav': q['sav'], 'cost': q['cost'], 'net': q_net, 'months': len(q_net) - 1},
    'cuts': {'small': float(claims['cut36_small']['value']), 'median': float(claims['cut36_median']['value']),
             'large': float(claims['cut36_large']['value'])},
}
out = os.path.join(HERE, 'data.js')
open(out, 'w').write('window.DATA = ' + json.dumps(data) + ';\n')
print('wrote', out, len(weeks), 'weeks; low', low['d'], 'last in', last_in, 'sav_low', round(sav_low, 2))
print('median oldPaid24', round(med['oldPaid'][24]), 'newPaid24', round(med['newPaid'][24]), 'gap30', round(med['gap'][30]))
print('q025 sav', round(q['sav'], 2), 'max net', round(max(q_net)), 'at', q_net.index(max(q_net)), 'end net', round(q_net[-1]), 'months', len(q_net) - 1)
print('small gap36', round(small['gap'][36]), 'large gap36', round(large['gap'][36]))
