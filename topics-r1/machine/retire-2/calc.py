"""retire-2: long-term care daily benefit with no inflation option, 3% compound, or 5% compound, compared with nursing
care facility prices (producer price index, Dec 1994 = 100) over every 20-year window Dec 1994 .. Mar 2026.
Coverage = benefit growth / price growth over the window (a policy that covered 100% of the daily price at the start).
Reads data/PCU623110623110.csv only. History, not a forecast."""
import csv, json, statistics

ppi = {}
for row in list(csv.reader(open('data/PCU623110623110.csv')))[1:]:
    if row[1] not in ('', '.'):
        ppi[row[0]] = float(row[1])


def add_months(d, n):
    y, m = int(d[:4]), int(d[5:7])
    k = y * 12 + (m - 1) + n
    return f'{k // 12:04d}-{k % 12 + 1:02d}-01'


Y = 20
win = []
for s in sorted(ppi):
    e = add_months(s, 12 * Y)
    if e in ppi:
        win.append((s, e, ppi[e] / ppi[s]))


def cov(rate):
    return [100 * (1 + rate) ** Y / x[2] for x in win]


c0, c3, c5 = cov(0.0), cov(0.03), cov(0.05)
growth = [100 * (x[2] ** (1 / Y) - 1) for x in win]
first, last = sorted(ppi)[0], sorted(ppi)[-1]
nmon = (int(last[:4]) * 12 + int(last[5:7])) - (int(first[:4]) * 12 + int(first[5:7]))
out = {
    'windows_20y': len(win),
    'price_growth_full_period_pct_per_year': round(100 * ((ppi[last] / ppi[first]) ** (12 / nmon) - 1), 2),
    'price_growth_20y_min_pct_per_year': round(min(growth), 2),
    'price_growth_20y_median_pct_per_year': round(statistics.median(growth), 2),
    'price_growth_20y_max_pct_per_year': round(max(growth), 2),
    'coverage_no_option_median_pct': round(statistics.median(c0), 1),
    'coverage_3pct_median_pct': round(statistics.median(c3), 1),
    'coverage_3pct_min_pct': round(min(c3), 1),
    'coverage_3pct_max_pct': round(max(c3), 1),
    'share_3pct_kept_up_pct': round(100 * sum(c >= 100 for c in c3) / len(c3), 1),
    'coverage_5pct_median_pct': round(statistics.median(c5), 1),
    'coverage_5pct_min_pct': round(min(c5), 1),
    'share_5pct_kept_up_pct': round(100 * sum(c >= 100 for c in c5) / len(c5), 1),
}
print(json.dumps(out))
