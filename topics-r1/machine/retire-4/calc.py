"""retire-4: a savings bond guaranteed to reach double its price after 20 years vs rolling 3-month T-bills for 20 years,
every monthly start Jan 1934 .. Aug 2006 (end months up to Aug 2026). Also checks the doubling against consumer prices.
Reads data/TB3MS.csv and data/CPIAUCNS.csv only. Taxes ignored. History, not a forecast."""
import csv, json, statistics


def load(name):
    d = {}
    for row in list(csv.reader(open(f'data/{name}.csv')))[1:]:
        if row[1] not in ('', '.'):
            d[row[0]] = float(row[1])
    return d


tb, cpi = load('TB3MS'), load('CPIAUCNS')
dates = sorted(tb)
idx = {d: i for i, d in enumerate(dates)}
# growth index: each month earns TB3MS/12 percent (simple monthly roll of the quoted 3-month bill rate)
grow = [1.0]
for d in dates:
    grow.append(grow[-1] * (1 + tb[d] / 1200))

N = 240
rows = []
for i, s in enumerate(dates):
    if i + N > len(dates):
        break
    tbill = grow[i + N] / grow[i]
    e = dates[i + N] if i + N < len(dates) else None
    rows.append((s, tbill))

won = [r for r in rows if r[1] > 2.0]
since90 = [r for r in rows if r[0] >= '1990-01-01']
latest = rows[-1]


def add_months(d, n):
    y, m = int(d[:4]), int(d[5:7])
    k = y * 12 + (m - 1) + n
    return f'{k // 12:04d}-{k % 12 + 1:02d}-01'


real = []
for s, _ in rows:
    e = add_months(s, N)
    if s in cpi and e in cpi:
        real.append((s, 2.0 * cpi[s] / cpi[e]))
out = {
    'starts': len(rows),
    'first_start': rows[0][0],
    'last_start': latest[0],
    'share_tbills_above_double_pct': round(100 * len(won) / len(rows), 1),
    'median_tbill_multiple_20y': round(statistics.median(r[1] for r in rows), 3),
    'min_tbill_multiple_20y': round(min(r[1] for r in rows), 3),
    'max_tbill_multiple_20y': round(max(r[1] for r in rows), 3),
    'share_tbills_above_double_starts_since_1990_pct': round(100 * sum(r[1] > 2.0 for r in since90) / len(since90), 1),
    'latest_tbill_multiple_20y': round(latest[1], 3),
    'doubling_rate_pct_per_year': round(100 * (2 ** (1 / 20) - 1), 2),
    'real_windows': len(real),
    'share_double_beat_prices_pct': round(100 * sum(r[1] >= 1.0 for r in real) / len(real), 1),
    'median_real_value_double_pct': round(100 * statistics.median(r[1] for r in real), 1),
    'tb3ms_latest_pct': tb['2026-08-01'],
}
print(json.dumps(out))
