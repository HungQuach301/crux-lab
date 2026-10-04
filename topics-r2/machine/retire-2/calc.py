"""retire-2: give down-payment money to an adult child now, or keep it in rolling 3-month T-bills and give it later.
Coverage = T-bill growth / national home price growth over the wait: the share of the same home's price the delayed gift
still matches. Home prices: USSTHPI (all-transactions house price index, U.S., quarterly, NSA, from 1975 Q1).
Reads data/*.csv only. Taxes ignored. History, not a forecast."""
import csv, json, statistics


def load(name):
    d = {}
    for row in list(csv.reader(open(f'data/{name}.csv')))[1:]:
        if row[1] not in ('', '.'):
            d[row[0]] = float(row[1])
    return d


def add_months(d, n):
    y, m = int(d[:4]), int(d[5:7])
    k = y * 12 + (m - 1) + n
    return f'{k // 12:04d}-{k % 12 + 1:02d}-01'


hpi, tb = load('USSTHPI'), load('TB3MS')


def tbill_growth(s, months):
    g = 1.0
    for i in range(months):
        g *= 1 + tb[add_months(s, i)] / 1200
    return g


def windows(years):
    n = 12 * years
    rows = []
    for s in sorted(hpi):
        e = add_months(s, n)
        if e in hpi:
            rows.append((s, tbill_growth(s, n) / (hpi[e] / hpi[s])))
    return rows


out = {}
w = windows(10)
cov = [c for _, c in w]
out['starts_10y'] = len(w)
out['first_start_10y'] = w[0][0]
out['last_start_10y'] = w[-1][0]
out['share_gift_buys_less_10y_pct'] = round(100 * sum(c < 1 for c in cov) / len(cov), 1)
out['median_coverage_10y_pct'] = round(100 * statistics.median(cov), 1)
out['min_coverage_10y_pct'] = round(100 * min(cov), 1)
out['max_coverage_10y_pct'] = round(100 * max(cov), 1)
since90 = [c for s, c in w if s >= '1990-01-01']
out['starts_since_1990_10y'] = len(since90)
out['share_gift_buys_less_10y_since_1990_pct'] = round(100 * sum(c < 1 for c in since90) / len(since90), 1)
out['latest_coverage_10y_pct'] = round(100 * w[-1][1], 1)
w20 = windows(20)
out['starts_20y'] = len(w20)
out['share_gift_buys_less_20y_pct'] = round(100 * sum(c < 1 for _, c in w20) / len(w20), 1)
out['latest_coverage_20y_pct'] = round(100 * w20[-1][1], 1)
q = len(hpi) - 1  # quarters 1975-01-01 .. 2026-04-01
out['home_price_growth_annual_pct'] = round(100 * ((hpi['2026-04-01'] / hpi['1975-01-01']) ** (4 / q) - 1), 2)
out['tbill_growth_annual_pct'] = round(100 * (tbill_growth('1975-01-01', 3 * q) ** (4 / q) - 1), 2)
print(json.dumps(out))
