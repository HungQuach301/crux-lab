"""retire-3: a 5-year CD the bank can call (coupon = 5-year yield + 0.50) vs a non-callable 5-year CD (coupon = 5-year yield),
replayed for every monthly start from Apr 1953 to Aug 2021 with constant-maturity Treasury yields as the rate proxy.
Call rule: on anniversaries 1-4 the bank calls when the original 5-year rate minus the current yield for the remaining term
is at least THRESH; called money is reinvested in a non-callable CD for the remaining term at that yield.
Annual compounding. Reads data/GS1.csv, GS2.csv, GS3.csv, GS5.csv only. History, not a forecast."""
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


g1, g2, g3, g5 = load('GS1'), load('GS2'), load('GS3'), load('GS5')
PREMIUM = 0.50
LAST = '2026-08-01'


def remaining_yield(t, years):
    if years == 4:
        return (g3[t] + g5[t]) / 2
    if years == 3:
        return g3[t]
    if years == 2:
        return g2[t] if t in g2 else (g1[t] + g3[t]) / 2
    return g1[t]


def replay(thresh):
    rows = []
    for s in sorted(g5):
        if add_months(s, 60) > LAST:
            break
        r = g5[s]
        value, called = 1.0, None
        for k in range(1, 5):
            value *= 1 + (r + PREMIUM) / 100
            t = add_months(s, 12 * k)
            y = remaining_yield(t, 5 - k)
            if r - y >= thresh:
                called = k
                value *= (1 + y / 100) ** (5 - k)
                break
        else:
            value *= 1 + (r + PREMIUM) / 100
        locked = (1 + r / 100) ** 5
        diff = 100 * (value ** 0.2 - locked ** 0.2)
        rows.append((s, called, diff))
    return rows


rows = replay(0.25)
n = len(rows)
called = [x for x in rows if x[1]]
diffs = [x[2] for x in rows]
since2000 = [x for x in rows if x[0] >= '2000-01-01']
out = {
    'starts': n,
    'first_start': rows[0][0],
    'last_start': rows[-1][0],
    'share_called_pct': round(100 * len(called) / n, 1),
    'share_callable_ahead_pct': round(100 * sum(d > 0 for d in diffs) / n, 1),
    'median_diff_pts_per_year': round(statistics.median(diffs), 2),
    'mean_diff_pts_per_year': round(statistics.mean(diffs), 2),
    'worst_diff_pts_per_year': round(min(diffs), 2),
    'best_diff_pts_per_year': round(max(diffs), 2),
    'share_ahead_when_called_pct': round(100 * sum(x[2] > 0 for x in called) / len(called), 1),
    'starts_since_2000': len(since2000),
    'share_called_since_2000_pct': round(100 * sum(1 for x in since2000 if x[1]) / len(since2000), 1),
    'share_callable_ahead_since_2000_pct': round(100 * sum(x[2] > 0 for x in since2000) / len(since2000), 1),
}
alt = replay(0.50)
out['share_called_thresh050_pct'] = round(100 * sum(1 for x in alt if x[1]) / len(alt), 1)
out['share_callable_ahead_thresh050_pct'] = round(100 * sum(x[2] > 0 for x in alt) / len(alt), 1)
out['gs5_latest_pct'] = g5[LAST]
print(json.dumps(out))
