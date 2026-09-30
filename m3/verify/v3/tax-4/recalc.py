import csv, json
rows = [r for r in csv.reader(open("data/RIFLPBCIANM60NM.csv"))][1:]
obs = [(d, float(v)) for d, v in rows if v.strip() not in ("", ".")]
rate = obs[-1][1]
P, N = 10000.0, 60

def sched(r):
    i = r / 1200
    pay = P * i / (1 - (1 + i) ** -N)
    b, out = P, []
    for _ in range(N):
        it = b * i; out.append(it); b -= pay - it
    return out

s = sched(rate); tot = sum(s)
def ded(k): return sum(s[:k])

def equiv(t, k):
    target = tot - t * ded(k)
    lo, hi = 0.0, rate
    for _ in range(200):
        mid = (lo + hi) / 2
        if sum(sched(mid)) < target: lo = mid
        else: hi = mid
    return (lo + hi) / 2

res = {
 "loan_rate_pct": rate,
 "total_interest_per_10k_usd": tot,
 "deductible_share_start2026": ded(36) / tot,
 "deductible_share_start2027": ded(24) / tot,
 "deductible_share_start2028": ded(12) / tot,
 "tax_saving_per_10k_12pct_start2026_usd": 0.12 * ded(36),
 "equiv_rate_12pct_start2026_pct": equiv(0.12, 36),
 "equiv_rate_22pct_start2026_pct": equiv(0.22, 36),
 "equiv_rate_12pct_start2028_pct": equiv(0.12, 12),
 "equiv_rate_22pct_start2028_pct": equiv(0.22, 12),
}
print(json.dumps(res, indent=1))
