"""retire-4: travel now vs later. Does money set aside for trips and kept in rolling 3-month T-bills keep pace with travel prices?
Coverage = T-bill growth / price growth over the wait. Prices: CPI-U airline fares (CUUR0000SETG01, from 1963-12) and
lodging away from home (CUUR0000SEHB, from 1997-12); 'trip' = half airfare, half lodging at the start.
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


air, lodge, tb = load('CUUR0000SETG01'), load('CUUR0000SEHB'), load('TB3MS')


def tbill_growth(s, months):
    g = 1.0
    for i in range(months):
        g *= 1 + tb[add_months(s, i)] / 1200
    return g


def growth(kind, s, e):
    if kind == 'air':
        return air[e] / air[s] if s in air and e in air else None
    if kind == 'lodging':
        return lodge[e] / lodge[s] if s in lodge and e in lodge else None
    if s in air and e in air and s in lodge and e in lodge:
        return 0.5 * air[e] / air[s] + 0.5 * lodge[e] / lodge[s]
    return None


def windows(kind, years):
    n = 12 * years
    base = air if kind == 'air' else lodge
    rows = []
    for s in sorted(base):
        p = growth(kind, s, add_months(s, n))
        if p is not None:
            rows.append((s, tbill_growth(s, n) / p))
    return rows


out = {}
for kind in ('air', 'lodging', 'trip'):
    w = windows(kind, 10)
    cov = [c for _, c in w]
    out[f'{kind}_starts_10y'] = len(w)
    out[f'{kind}_first_start_10y'] = w[0][0]
    out[f'{kind}_share_waiting_cost_more_10y_pct'] = round(100 * sum(c < 1 for c in cov) / len(cov), 1)
    out[f'{kind}_median_coverage_10y_pct'] = round(100 * statistics.median(cov), 1)
    out[f'{kind}_latest_coverage_10y_pct'] = round(100 * w[-1][1], 1)
w5 = windows('trip', 5)
out['trip_starts_5y'] = len(w5)
out['trip_share_waiting_cost_more_5y_pct'] = round(100 * sum(c < 1 for _, c in w5) / len(w5), 1)
months = 344  # 1997-12-01 .. 2026-08-01
out['air_price_growth_annual_pct'] = round(100 * ((air['2026-08-01'] / air['1997-12-01']) ** (12 / months) - 1), 2)
out['lodging_price_growth_annual_pct'] = round(100 * ((lodge['2026-08-01'] / lodge['1997-12-01']) ** (12 / months) - 1), 2)
out['tbill_growth_annual_pct'] = round(100 * (tbill_growth('1997-12-01', months) ** (12 / months) - 1), 2)
print(json.dumps(out))
