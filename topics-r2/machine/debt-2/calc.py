"""debt-2: buyers putting 10% down; how long until mortgage insurance could come off, by the original schedule and by the
home-price index. Reads data/HPIPONM226N.csv (monthly purchase-only house price index, not seasonally adjusted) and
data/MORTGAGE30US.csv (weekly 30-year fixed rate). Prints one JSON {id: value}."""
import csv, json, statistics


def load(f):
    return {r[0]: float(r[1]) for r in list(csv.reader(open(f)))[1:] if r[1] not in ('', '.')}


hpi = load('data/HPIPONM226N.csv')
wk = load('data/MORTGAGE30US.csv')
by_month = {}
for d, v in wk.items():
    by_month.setdefault(d[:7] + '-01', []).append(v)
rate = {m: statistics.mean(v) for m, v in by_month.items()}   # monthly average of weekly rates

L0 = 0.90   # loan = 90% of price (10% down)


def balance(r, k):
    """Balance after k monthly payments, as a fraction of the purchase price; 30-year level payment."""
    x = r / 1200
    p = L0 * x / (1 - (1 + x) ** -360)
    return L0 * (1 + x) ** k - p * ((1 + x) ** k - 1) / x


def sched(r, thr):
    return next(k for k in range(361) if balance(r, k) <= thr + 1e-12)


months = sorted(hpi)
idx = {m: i for i, m in enumerate(months)}


def ltv_index(start, k):
    """Balance after k payments divided by the purchase price grown by the index."""
    return balance(rate[start], k) / (hpi[months[idx[start] + k]] / hpi[start])


# A: LTV on index value at month 24 (purchase months with 24 months of index data after them)
startsA = [m for m in months if m in rate and idx[m] + 24 < len(months)]
ltv24 = [ltv_index(m, 24) for m in startsA]
# B: months until LTV on index value first <= 80% (purchase months with >= 120 months of data after them)
startsB = [m for m in months if m in rate and idx[m] + 120 < len(months)]
hit = []
for m in startsB:
    k = next((k for k in range(0, len(months) - idx[m]) if ltv_index(m, k) <= 0.80 + 1e-12), None)
    hit.append(k)
latest_rate_month = max(rate)
r_now = rate[latest_rate_month]
worst = max(range(len(startsB)), key=lambda i: hit[i])
out = {
    'rate_month_latest': latest_rate_month, 'rate_latest': round(r_now, 3),
    'sched80_months_latest': sched(r_now, 0.80), 'sched78_months_latest': sched(r_now, 0.78),
    'nA': len(startsA), 'firstA': startsA[0], 'lastA': startsA[-1],
    'shareA_ltv24_le75': round(sum(v <= 0.75 for v in ltv24) / len(ltv24), 3),
    'shareA_ltv24_le80': round(sum(v <= 0.80 for v in ltv24) / len(ltv24), 3),
    'nB': len(startsB), 'firstB': startsB[0], 'lastB': startsB[-1],
    'medianB_months_to80': statistics.median(hit),
    'shareB_over60': round(sum(h > 60 for h in hit) / len(hit), 3),
    'maxB_months_to80': hit[worst], 'maxB_start': startsB[worst],
    'shareB_le_sched80': round(sum(h <= sched(rate[m], 0.80) for h, m in zip(hit, startsB)) / len(hit), 3),
}
print(json.dumps(out))
