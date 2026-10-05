"""retire-1: prepay a funeral at today's price vs keep the same money in rolling 3-month T-bills until it is needed.
Funeral prices: CPI-U 'funeral expenses' index (CUUR0000SEGD03, monthly, NSA, from 1997-12). T-bills: TB3MS.
For every start month and horizon N (5, 10, 15 years): coverage = T-bill growth / funeral price growth.
Reads data/*.csv only. Taxes and fees ignored. History, not a forecast."""
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


fun, tb, cpi = load('CUUR0000SEGD03'), load('TB3MS'), load('CPIAUCNS')


def tbill_growth(s, months):
    g = 1.0
    for i in range(months):
        g *= 1 + tb[add_months(s, i)] / 1200
    return g


def windows(years):
    n = 12 * years
    rows = []
    for s in sorted(fun):
        e = add_months(s, n)
        if e in fun:
            rows.append((s, tbill_growth(s, n) / (fun[e] / fun[s])))
    return rows


out = {}
for yrs in (5, 10, 15):
    w = windows(yrs)
    cov = [c for _, c in w]
    out[f'starts_{yrs}y'] = len(w)
    out[f'share_savings_fell_short_{yrs}y_pct'] = round(100 * sum(c < 1 for c in cov) / len(cov), 1)
    if yrs == 10:
        out['first_start_10y'] = w[0][0]
        out['last_start_10y'] = w[-1][0]
        out['median_coverage_10y_pct'] = round(100 * statistics.median(cov), 1)
        out['min_coverage_10y_pct'] = round(100 * min(cov), 1)
        out['max_coverage_10y_pct'] = round(100 * max(cov), 1)
        out['latest_coverage_10y_pct'] = round(100 * w[-1][1], 1)
months = 344  # 1997-12-01 .. 2026-08-01
out['funeral_price_growth_annual_pct'] = round(100 * ((fun['2026-08-01'] / fun['1997-12-01']) ** (12 / months) - 1), 2)
out['all_items_price_growth_annual_pct'] = round(100 * ((cpi['2026-08-01'] / cpi['1997-12-01']) ** (12 / months) - 1), 2)
out['tbill_growth_annual_pct'] = round(100 * (tbill_growth('1997-12-01', months) ** (12 / months) - 1), 2)
out['tb3ms_latest_pct'] = tb['2026-08-01']
print(json.dumps(out))
