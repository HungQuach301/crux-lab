"""debt-2: cost of copying a 15-year mortgage by prepaying a 30-year one (the rate spread). Reads data/ only."""
import csv, json, statistics as st
def load(s):
    return {r[0]: float(r[1]) for r in list(csv.reader(open(f'data/{s}.csv')))[1:] if r[1] not in ('', '.')}
a, b = load('MORTGAGE30US'), load('MORTGAGE15US')
weeks = sorted(set(a) & set(b))
L = 100000.0

def pmt(rate, n):
    i = rate / 1200
    return L * i / (1 - (1 + i) ** -n)

def premium(r30, r15):
    """extra total interest ($ per $100k) of a 30-year loan at r30 paid with the 15-year payment at r15, vs the 15-year loan"""
    p = pmt(r15, 180)
    int15 = p * 180 - L
    bal, paid, i, m = L, 0.0, r30 / 1200, 0
    while bal > 1e-9:
        m += 1
        due = bal * (1 + i)
        pay = min(p, due)
        paid += pay
        bal = due - pay
    return paid - L - int15, m

last = weeks[-1]
prem, months = premium(a[last], b[last])
allp = [premium(a[w], b[w])[0] for w in weeks]
out = {
    'latest_r30': a[last], 'latest_r15': b[last], 'latest_spread': round(a[last] - b[last], 2),
    'latest_premium_per_100k': round(prem), 'latest_months_to_payoff': months,
    'mean_spread_all_weeks': round(st.mean(a[w] - b[w] for w in weeks), 3),
    'median_premium_all_weeks': round(st.median(allp)),
    'share_weeks_spread_ge_050': round(100 * sum(round((a[w] - b[w]) * 100) >= 50 for w in weeks) / len(weeks), 1),
    'n_weeks': len(weeks),
}
print(json.dumps(out))
