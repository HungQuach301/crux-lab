"""debt-3: rate premium of a 72-month vs a 60-month new-car loan at commercial banks, and where the extra interest comes from."""
import csv, json, statistics as st
def load(s):
    return {r[0]: float(r[1]) for r in list(csv.reader(open(f'data/{s}.csv')))[1:] if r[1] not in ('', '.')}
a, b = load('RIFLPBCIANM60NM'), load('RIFLPBCIANM72NM')
months = sorted(set(a) & set(b))
prem = {d: b[d] - a[d] for d in months}
last = months[-1]

def interest(rate, n, bal=30000.0):
    i = rate / 1200
    return bal * i / (1 - (1 + i) ** -n) * n - bal

mp = st.mean(prem.values())
r60 = a[last]
term_effect = interest(r60, 72) - interest(r60, 60)
rate_effect = interest(r60 + mp, 72) - interest(r60, 72)
out = {
    'n_months': len(months),
    'mean_premium_72_vs_60': round(mp, 3),
    'share_months_72_le_60': round(100 * sum(round(b[d] * 100) <= round(a[d] * 100) for d in months) / len(months), 1),
    'max_premium': round(max(prem.values()), 2),
    'latest_r60': a[last], 'latest_r72': b[last],
    'term_effect_30k': round(term_effect), 'rate_effect_30k': round(rate_effect),
    'rate_share_of_extra_interest': round(100 * rate_effect / (term_effect + rate_effect), 1),
}
print(json.dumps(out))
