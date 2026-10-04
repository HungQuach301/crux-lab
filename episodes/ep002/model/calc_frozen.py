"""debt-2: private student loan, 10-year repayment: 9.00% fixed vs. a variable rate starting at 7.50%,
replayed over every 120-month window of 3-month Treasury bill history since January 1954.
Reads data/TB3MS.csv only. Prints one JSON object {id: value}."""
import csv, json, statistics

P = 50000.0
N = 120
FIXED = 9.00
VAR0 = 7.50
FIRST_START = '1954-01-01'

rows = [(r[0], float(r[1])) for r in list(csv.reader(open('data/TB3MS.csv')))[1:] if r[1] not in ('', '.')]
dates = [d for d, _ in rows]
tb = [v for _, v in rows]
IDX_TODAY = tb[-1]              # latest 3-month bill rate (Aug 2026)
MARGIN = VAR0 - IDX_TODAY       # variable = margin + index; index starts at today's level


def total_interest(path):
    bal, tot, cur, pay = P, 0.0, None, 0.0
    for k, r in enumerate(path):
        if r != cur:
            x = r / 1200
            pay = bal * x / (1 - (1 + x) ** -(N - k))
            cur = r
        i = bal * r / 1200
        tot += i
        bal -= pay - i
    return tot


fixed_int = total_interest([FIXED] * N)
res = []
for s in range(len(tb)):
    if dates[s] < FIRST_START:
        continue
    if s + N > len(tb):
        break
    path = [round(MARGIN + max(0.0, IDX_TODAY + tb[s + k] - tb[s]), 6) for k in range(N)]
    vi = total_interest(path)
    res.append((dates[s], vi - fixed_int, max(path)))

diff = [x for _, x, _ in res]
early = [x for d, x, _ in res if d < '1981-01-01']
late = [x for d, x, _ in res if d >= '1981-01-01']
worst = max(res, key=lambda t: t[1])
out = {
    'n_starts': len(res),
    'first_start': res[0][0], 'last_start': res[-1][0],
    'fixed_total_interest': round(fixed_int),
    'share_variable_costlier': round(100 * sum(x > 0 for x in diff) / len(diff), 1),
    'median_variable_minus_fixed': round(statistics.median(diff)),
    'worst_variable_minus_fixed': round(worst[1]),
    'worst_start': worst[0],
    'best_variable_minus_fixed': round(min(diff)),
    'max_variable_rate_any_window': round(max(m for _, _, m in res), 2),
    'n_starts_1954_1980': len(early),
    'share_costlier_1954_1980': round(100 * sum(x > 0 for x in early) / len(early), 1),
    'n_starts_1981_on': len(late),
    'share_costlier_1981_on': round(100 * sum(x > 0 for x in late) / len(late), 1),
    'index_today': IDX_TODAY,
    'margin': round(MARGIN, 2),
}
print(json.dumps(out))
