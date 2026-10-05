"""debt-4: car shoppers waiting a year for a lower loan rate. $35,000, 60 months. Reads data/RIFLPBCIANM60NM.csv (bank
new-car 60-month rate, reported quarterly) and data/CUUR0000SETA01.csv (consumer price index, new vehicles, not
seasonally adjusted). Prints one JSON {id: value}."""
import csv, json, statistics

P = 35000.0


def load(f):
    return {r[0]: float(r[1]) for r in list(csv.reader(open(f)))[1:] if r[1] not in ('', '.')}


def pay(p, r, n=60):
    x = r / 1200
    return p * x / (1 - (1 + x) ** -n)


rate = load('data/RIFLPBCIANM60NM.csv')
cpi = load('data/CUUR0000SETA01.csv')
pairs = []
for a in sorted(rate):
    y, mo = int(a[:4]), a[5:7]
    b = f'{y + 1}-{mo}-01'
    if b in rate and a in cpi and b in cpi:
        p1 = P * cpi[b] / cpi[a]
        d = pay(p1, rate[b]) - pay(P, rate[a])
        pairs.append((a, rate[b] - rate[a], cpi[b] / cpi[a] - 1, d))
fell = [p for p in pairs if p[1] < 0]
last = max(rate)
out = {
    'n_pairs': len(pairs), 'first_pair': pairs[0][0], 'last_pair': pairs[-1][0],
    'share_payment_lower': round(sum(p[3] < 0 for p in pairs) / len(pairs), 3),
    'median_payment_change': round(statistics.median(p[3] for p in pairs), 2),
    'n_rate_fell': len(fell),
    'share_lower_when_rate_fell': round(sum(p[3] < 0 for p in fell) / len(fell), 3),
    'largest_rate_drop': round(min(p[1] for p in pairs), 2),
    'largest_rate_rise': round(max(p[1] for p in pairs), 2),
    'best_payment_change': round(min(p[3] for p in pairs), 2),
    'median_price_change': round(statistics.median(p[2] for p in pairs) * 100, 2),
    'rate_latest_month': last, 'rate_latest': rate[last],
    'pay_latest': round(pay(P, rate[last]), 2),
    'one_point_effect': round(pay(P, rate[last]) - pay(P, rate[last] - 1), 2),
}
print(json.dumps(out))
