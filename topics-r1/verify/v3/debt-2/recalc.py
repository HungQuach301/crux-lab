import csv, json, statistics, hashlib
from decimal import Decimal, ROUND_HALF_UP
HERE = __file__.rsplit('/', 1)[0] or '.'
def rnd(x, nd=0):
    q = Decimal(1).scaleb(-nd)
    v = Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP)
    return int(v) if nd == 0 else float(v)
rows = list(csv.DictReader(open(f'{HERE}/data/TB3MS.csv')))
dates = [r['observation_date'] for r in rows]; tb = [float(r['TB3MS']) for r in rows]
assert dates[0] == '1934-01-01' and dates[-1] == '2026-08-01'
latest = tb[-1]; margin = 7.50 - latest
P, N = 50000.0, 120
def total_interest(rates):
    bal, tot, pay, prev = P, 0.0, None, None
    for k in range(N):
        r = rates[k] / 1200; rem = N - k
        if pay is None or rates[k] != prev:
            pay = bal / rem if r == 0 else bal * r / (1 - (1 + r) ** -rem)
            prev = rates[k]
        i = bal * r; tot += i; bal -= (pay - i)
    return tot, bal
fixed, fbal = total_interest([9.0] * N)
i0 = dates.index('1954-01-01'); starts = []
for s in range(i0, len(tb)):
    if s + N - 1 >= len(tb): break
    starts.append(s)
diffs = {}; maxrate = -1
for s in starts:
    rates = [margin + max(0.0, latest + tb[s + k] - tb[s]) for k in range(N)]
    maxrate = max(maxrate, max(rates))
    v, vb = total_interest(rates); assert abs(vb) < 1e-6
    diffs[s] = v - fixed
D = list(diffs.values())
early = [s for s in starts if dates[s] <= '1980-12-01']; late = [s for s in starts if dates[s] >= '1981-01-01']
share = lambda ss: rnd(100 * sum(diffs[s] > 0 for s in ss) / len(ss), 1)
worst = max(starts, key=lambda s: diffs[s])
res = {
 'n_starts': len(starts), 'first_start': dates[starts[0]], 'last_start': dates[starts[-1]],
 'fixed_total_interest': rnd(fixed), 'share_variable_costlier': share(starts),
 'median_variable_minus_fixed': rnd(statistics.median(D)),
 'worst_variable_minus_fixed': rnd(max(D)), 'worst_start': dates[worst],
 'best_variable_minus_fixed': rnd(min(D)), 'max_variable_rate_any_window': rnd(maxrate, 2),
 'n_starts_1954_1980': len(early), 'share_costlier_1954_1980': share(early),
 'n_starts_1981_on': len(late), 'share_costlier_1981_on': share(late),
 'index_today': latest, 'margin': rnd(margin, 2),
}
json.dump(res, open(f'{HERE}/result.json', 'w'), indent=1)
print(json.dumps(res, indent=1)); print('median raw', statistics.median(D), 'n even', len(D) % 2 == 0)
