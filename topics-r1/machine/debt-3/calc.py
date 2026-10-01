"""debt-3: new-car loan, 60 vs 72 months: how much higher is the 72-month rate at banks, and where does the
extra interest on a $35,000 loan come from? Reads data/RIFLPBCIANM60NM.csv and data/RIFLPBCIANM72NM.csv."""
import csv, json, statistics

P = 35000.0


def load(f):
    return {r[0]: float(r[1]) for r in list(csv.reader(open(f)))[1:] if r[1] not in ('', '.')}


r60 = load('data/RIFLPBCIANM60NM.csv')
r72 = load('data/RIFLPBCIANM72NM.csv')
both = sorted(set(r60) & set(r72))
prem = [round(r72[d] - r60[d], 2) for d in both]


def pay(r, n):
    x = r / 1200
    return P * x / (1 - (1 + x) ** -n)


def interest(r, n):
    return pay(r, n) * n - P


last = both[-1]
a60, a72 = r60[last], r72[last]
i60, i72 = interest(a60, 60), interest(a72, 72)
i72_same = interest(a60, 72)          # 72 months at the 60-month rate: pure term effect
avg_p = statistics.mean(prem)
i72_avg = interest(a60 + avg_p, 72)   # 72 months at latest 60-month rate + average premium
out = {
    'n_months': len(both), 'first_month': both[0], 'last_month': last,
    'mean_premium': round(avg_p, 2),
    'median_premium': round(statistics.median(prem), 3),
    'max_premium': max(prem), 'min_premium': min(prem),
    'months_72_cheaper': sum(p < 0 for p in prem),
    'months_72_not_higher': sum(p <= 0 for p in prem),
    'months_premium_ge_050': sum(p >= 0.5 for p in prem),
    'rate60_latest': a60, 'rate72_latest': a72,
    'pay60_latest': round(pay(a60, 60), 2), 'pay72_latest': round(pay(a72, 72), 2),
    'int60_latest': round(i60), 'int72_latest': round(i72),
    'extra_interest_72_latest': round(i72 - i60),
    'term_effect': round(i72_same - i60),
    'extra_interest_72_avgpremium': round(i72_avg - i60),
    'rate_effect_avgpremium': round(i72_avg - i72_same),
}
print(json.dumps(out))
