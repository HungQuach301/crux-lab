"""retire-5: an account that takes only required minimum distributions from age 73, invested at a constant real yield
equal to the 20-year TIPS yield: latest observation vs the series low. Reads data/ only."""
import csv, json
d = [(r[0], float(r[1])) for r in list(csv.reader(open('data/DFII20.csv')))[1:] if r[1] not in ('', '.')]
r_now = d[-1][1]
r_min = min(v for _, v in d)
# Uniform Lifetime Table, 26 CFR 1.401(a)(9)-9(c), ages 73-100
D = {73: 26.5, 74: 25.5, 75: 24.6, 76: 23.7, 77: 22.9, 78: 22.0, 79: 21.1, 80: 20.2, 81: 19.4, 82: 18.5, 83: 17.7, 84: 16.8,
     85: 16.0, 86: 15.2, 87: 14.4, 88: 13.7, 89: 12.9, 90: 12.2, 91: 11.5, 92: 10.8, 93: 10.1, 94: 9.5, 95: 8.9, 96: 8.4,
     97: 7.8, 98: 7.3, 99: 6.8, 100: 6.4}
def path(r_pct):
    r = r_pct / 100
    bal, balances, draws = 1.0, {}, {}
    for age in range(73, 101):
        balances[age] = bal
        draws[age] = bal / D[age]
        bal = (bal - draws[age]) * (1 + r)
    return balances, draws
bn, wn = path(r_now)
bm, wm = path(r_min)
peak_age = max(wn, key=lambda a: wn[a])
out = {
    'real_yield_now_pct': r_now,
    'real_yield_low_pct': r_min,
    'first_withdrawal_pct_of_start': round(wn[73] * 100, 2),
    'now_balance_at_90_pct_of_start': round(bn[90] * 100, 1),
    'now_withdrawal_at_90_pct_of_start': round(wn[90] * 100, 2),
    'now_peak_withdrawal_age': peak_age,
    'now_peak_withdrawal_pct_of_start': round(wn[peak_age] * 100, 2),
    'low_balance_at_90_pct_of_start': round(bm[90] * 100, 1),
    'low_withdrawal_at_90_pct_of_start': round(wm[90] * 100, 2),
    'low_years_withdrawal_rises_after_73': sum(1 for a in range(74, 101) if wm[a] > wm[a - 1]),
}
print(json.dumps(out))
