import csv, json, math, statistics
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
D = Path(__file__).parent
P = 320000.0
def rnd(v, q):  # half-up rounding of the float's shortest repr
    r = Decimal(repr(v)).quantize(Decimal(q), rounding=ROUND_HALF_UP)
    return int(r) if q == '1' else float(r)
def load(f, col):
    out = {}
    for row in csv.DictReader(open(D / 'data' / f)):
        v = row[col].strip()
        if v not in ('', '.'):
            out[row['observation_date']] = float(v)
    return out
def pay(rate, n):
    x = rate / 1200
    return P * x / (1 - (1 + x) ** -n)
r30 = load('MORTGAGE30US.csv', 'MORTGAGE30US'); r15 = load('MORTGAGE15US.csv', 'MORTGAGE15US')
weeks = sorted(d for d in r30 if d in r15 and '1991-08-30' <= d <= '2026-09-24')
last = weeks[-1]; a, b = r30[last], r15[last]
p15 = pay(b, 180); p30on15 = pay(a, 180); p30 = pay(a, 360)
x = a / 1200
nmon = -math.log(1 - P * x / p15) / math.log(1 + x)
spreads = [r30[d] - r15[d] for d in weeks]
extras = [(pay(r30[d], 180) - pay(r15[d], 180)) * 180 for d in weeks]
res = {
 'n_weeks': len(weeks), 'first_week': weeks[0], 'last_week': last,
 'rate30_latest': a, 'rate15_latest': b,
 'pay15_latest': rnd(p15, '0.01'), 'pay30on15_latest': rnd(p30on15, '0.01'), 'pay30_latest': rnd(p30, '0.01'),
 'extra_month_latest': rnd(p30on15 - p15, '0.01'), 'extra_total_latest': rnd((p30on15 - p15) * 180, '1'),
 'months_payoff_at_pay15': rnd(nmon, '0.1'),
 'spread_mean': rnd(statistics.fmean(spreads), '0.01'),
 'spread_min': rnd(round(min(spreads), 10), '0.01'), 'spread_max': rnd(round(max(spreads), 10), '0.01'),
 'share_spread_ge_050': rnd(sum(1 for s in spreads if s >= 0.5 - 1e-9) / len(spreads), '0.001'),
 'extra_total_median': rnd(statistics.median(extras), '1'),
 'extra_total_min': rnd(min(extras), '1'), 'extra_total_max': rnd(max(extras), '1'),
}
json.dump(res, open(D / 'result.json', 'w'), indent=1)
# diagnostics
print(json.dumps(res, indent=1))
print('unrounded', p15, p30on15, p30, nmon, statistics.fmean(spreads), statistics.median(extras), min(extras), max(extras))
print('share strict (no tolerance)', sum(1 for s in spreads if s >= 0.5) / len(spreads))
print('weeks with 15 but not 30 / 30 not 15 in window', [d for d in r15 if d not in r30 and d<='2026-09-24'][:5])
