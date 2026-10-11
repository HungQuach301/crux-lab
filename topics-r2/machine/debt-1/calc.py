"""debt-1: 15-year mortgage vs a 30-year mortgage paid off on a 15-year schedule, $320,000 loan.
Reads data/MORTGAGE30US.csv and data/MORTGAGE15US.csv (weekly average rates). Prints one JSON {id: value}."""
import csv, json, math, statistics

P = 320000.0


def load(f):
    return {r[0]: float(r[1]) for r in list(csv.reader(open(f)))[1:] if r[1] not in ('', '.')}


def pay(r, n):
    x = r / 1200
    return P * x / (1 - (1 + x) ** -n)


m30 = load('data/MORTGAGE30US.csv')
m15 = load('data/MORTGAGE15US.csv')
weeks = sorted(set(m30) & set(m15))
spread = [m30[w] - m15[w] for w in weeks]
# extra cost of paying the 30-year loan off in 15 years (180 level payments at the 30-year rate) vs a true 15-year loan
extra_total = [(pay(m30[w], 180) - pay(m15[w], 180)) * 180 for w in weeks]

last = weeks[-1]
r30, r15 = m30[last], m15[last]
p15 = pay(r15, 180)
p30_15 = pay(r30, 180)
p30 = pay(r30, 360)
x = r30 / 1200
months_at_p15 = -math.log(1 - P * x / p15) / math.log(1 + x)
out = {
    'n_weeks': len(weeks), 'first_week': weeks[0], 'last_week': last,
    'rate30_latest': r30, 'rate15_latest': r15,
    'pay15_latest': round(p15, 2), 'pay30on15_latest': round(p30_15, 2), 'pay30_latest': round(p30, 2),
    'extra_month_latest': round(p30_15 - p15, 2),
    'extra_total_latest': round((p30_15 - p15) * 180),
    'months_payoff_at_pay15': round(months_at_p15, 1),
    'spread_mean': round(statistics.mean(spread), 2),
    'spread_min': round(min(spread), 2), 'spread_max': round(max(spread), 2),
    'share_spread_ge_050': round(sum(s >= 0.5 - 1e-9 for s in spread) / len(spread), 3),
    'extra_total_median': round(statistics.median(extra_total)),
    'extra_total_min': round(min(extra_total)), 'extra_total_max': round(max(extra_total)),
}
print(json.dumps(out))


# --statement N (topic-dossier.md §3): recompute the numbers of statements.json sentence N from the data above; prints True/False
import sys  # noqa: E402
if '--statement' in sys.argv:
    o = out
    gap = pay(r15, 180) - pay(r30, 360)
    checks = {
        1: o['last_week'] == '2026-09-24' and (r30, r15) == (7.03, 6.42) and round(p15, 2) == 2773.49,
        2: round(p30_15, 2) == 2881.62 and round(p30_15 - p15, 2) == 108.13 and round((p30_15 - p15) * 180) == 19464,
        3: round(months_at_p15, 1) == 192.9 and 0.9 <= (months_at_p15 - 180) / 12 <= 1.2,
        4: round(p30, 2) == 2135.42 and round((p30_15 - p15) * 180) == 19464,
        5: (o['n_weeks'], o['first_week'][:7], o['spread_min'], o['spread_max'], o['spread_mean'], round(100 * o['share_spread_ge_050'], 1),
            o['extra_total_min'], o['extra_total_max'], o['extra_total_median']) == (1831, '1991-08', 0.2, 1.0, 0.57, 62.9, 6097, 29502, 16594),
        6: round(p30_15 - p15) == 108 and abs((p30_15 - p15) * 180 - 19500) < 100 and abs(min(extra_total) - 6100) < 50,
        7: abs(gap - 640) < 5,
        8: abs(gap - 640) < 5,
        9: o['last_week'] == '2026-09-24' and (o['extra_total_min'], o['extra_total_max']) == (6097, 29502),
        10: (o['spread_min'], o['spread_max']) == (0.2, 1.0) and o['first_week'][:4] == '1991',
        11: min(extra_total) > 6000,
    }
    print(checks[int(sys.argv[sys.argv.index('--statement') + 1])])
