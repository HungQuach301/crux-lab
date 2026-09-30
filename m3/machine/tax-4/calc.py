"""tax-4: value of the 2025-2028 deduction for new-car loan interest, expressed as an equivalent cut in the loan rate.
Reads data/ only; prints {id: value}."""
import csv, json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
rows = [r for r in csv.reader(open(os.path.join(D, 'RIFLPBCIANM60NM.csv')))][1:]
rows = [r for r in rows if r[1] not in ('', '.')]
RATE = float(rows[-1][1])
P, N, LAST_YEAR = 10000.0, 60, 2028

def schedule(rate_pct):
    i = rate_pct / 1200
    pmt = P * i / (1 - (1 + i) ** -N)
    bal, out = P, []
    for _ in range(N):
        it = bal * i
        out.append(it)
        bal -= pmt - it
    return out

def deductible(start_year, rate_pct):
    """monthly payments start in January of start_year, 12 per calendar year; interest deductible in years <= 2028."""
    s = schedule(rate_pct)
    return sum(it for k, it in enumerate(s) if start_year + k // 12 <= LAST_YEAR), sum(s)

def equiv_rate(start_year, bracket):
    ded, tot = deductible(start_year, RATE)
    target = tot - bracket * ded
    lo, hi = 0.0, RATE
    for _ in range(100):
        mid = (lo + hi) / 2
        if sum(schedule(mid)) > target: hi = mid
        else: lo = mid
    return (lo + hi) / 2

d26, tot = deductible(2026, RATE)
d27, _ = deductible(2027, RATE)
d28, _ = deductible(2028, RATE)
out = {
    'loan_rate_pct': RATE,
    'total_interest_per_10k_usd': round(tot, 2),
    'deductible_share_start2026': round(d26 / tot, 4),
    'deductible_share_start2027': round(d27 / tot, 4),
    'deductible_share_start2028': round(d28 / tot, 4),
    'tax_saving_per_10k_12pct_start2026_usd': round(0.12 * d26, 2),
    'equiv_rate_12pct_start2026_pct': round(equiv_rate(2026, 0.12), 3),
    'equiv_rate_22pct_start2026_pct': round(equiv_rate(2026, 0.22), 3),
    'equiv_rate_12pct_start2028_pct': round(equiv_rate(2028, 0.12), 3),
    'equiv_rate_22pct_start2028_pct': round(equiv_rate(2028, 0.22), 3),
}
print(json.dumps(out))
