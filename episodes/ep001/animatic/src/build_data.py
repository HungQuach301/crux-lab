#!/usr/bin/env python3
"""C4 animatic (from C3 final build_data.py, extended): build src/data.js (NOT committed: holds FRED weekly values, E1-A2) from local data + the episode model.

Inputs: episodes/ep001/data/normalized/mortgage30_weekly.csv (re-create with data/fetch.py --verify),
        episodes/ep001/out/model.json, episodes/ep001/out/claims.json, episodes/ep001/model/refi.py.
Every number printed on screen comes from claims.json `display` (CL() in engine.js). Object sizes (heights, bar
lengths, the window's weeks) are recomputed here with model/refi.py and asserted against the claims.
"""
import csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.normpath(os.path.join(HERE, '..', '..'))
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

# ---------------- C4 additions ----------------
def curve(ch, cut, months):
    p = paths(ch, R_OLD - cut, months)
    net = [m * p['sav'] - p['gap'][m] for m in range(months + 1)]  # compare with cost; >= cost = paid back
    be = next((m for m in range(1, months + 1) if net[m] >= p['cost'] - 1e-9), None)
    return dict(sav=p['sav'], cost=p['cost'], net=net, be=be, months=months, simple=refi.break_even_months(p['cost'], p['sav']))

c05, c10 = curve('median', float(claims['s05']['value']), 60), curve('median', float(claims['s10']['value']), 60)
assert c05['be'] == int(disp('be_bal_05')) and c10['be'] == int(disp('be_bal_10')), (c05['be'], c10['be'])
assert c05['simple'] == int(disp('be_simple_05')) and c10['simple'] == int(disp('be_simple_10'))
# the real offer (0.59) at 36 months, for S13 (not printed)
creal = curve('median', R_OLD - R_NEW, 60)
assert creal['be'] == int(disp('be_bal_median'))
# Walt to month 80 (S15 break-even 75), Anjali/Walt 36 months already in small/large
small80 = paths('small', R_NEW, 80)
assert small80['be'] == int(disp('be_bal_small'))
# S20: Nora's position after m months (net = savings - extra owed - fees), to 96 months
med96 = paths('median', R_NEW, 96)
pos = [m * med96['sav'] - med96['gap'][m] - med96['cost'] for m in range(97)]
assert money(pos[36]) == disp('net36_median') and money(pos[84]) == disp('net84_median'), (pos[36], pos[84])
# S10: the first payment of each loan split into interest and principal (drawn, not printed)
B = refi.balance_after(375000.0, R_OLD, 360, K)
p_old, p_new = refi.payment(375000.0, R_OLD, 360), refi.payment(B, R_NEW, 360)
split = {'old': {'interest': B * R_OLD / 1200, 'principal': p_old - B * R_OLD / 1200},
         'new': {'interest': B * R_NEW / 1200, 'principal': p_new - B * R_NEW / 1200}}
# S03: 2023 weekly rates; peak 7.79% in October 2023
w23 = [{'d': d, 'r': r} for d, r in rows if '2023-01-01' <= d <= '2023-12-31']
pk = max(w23, key=lambda w: w['r'])
assert f"{pk['r']:.2f}%" == disp('peak2023') and pk['d'].startswith('2023-10'), pk
# S07/S19: 2025 refinance (31) bills, all sizes: p25 / p50 / p75 (HMDA, normalized)
hm = [r for r in csv.DictReader(open(os.path.join(EP, 'data', 'normalized', 'hmda_refi_costs.csv')))
      if r['year'] == '2025' and r['purpose'] == 'refinance (31)' and r['loanSize'] == 'all sizes'][0]
bills = {'p25': float(hm['cost_p25_usd']), 'p50': float(hm['cost_p50_usd']), 'p75': float(hm['cost_p75_usd'])}
assert money(bills['p25']) == disp('cost_p25') and money(bills['p75']) == disp('cost_p75') and money(bills['p50']) == disp('cost_median')
data.update({'c05': c05, 'c10': c10, 'creal': creal, 'small80': small80, 'pos96': pos, 'split': split,
             'w23': {'weeks': w23, 'peak': pk['d']}, 'bills': bills, 'k': K})
open(out, 'w').write('window.DATA = ' + json.dumps(data) + ';\n')
print('C4 additions ok: be05', c05['be'], 'be10', c10['be'], 'walt be', small80['be'], 'peak', pk, 'bills', bills)
