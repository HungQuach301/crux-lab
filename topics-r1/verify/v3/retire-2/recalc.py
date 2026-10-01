import csv, json, hashlib, statistics, os
from decimal import Decimal, ROUND_HALF_UP
D = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(D, "data", "PCU623110623110.csv")
print("sha256", hashlib.sha256(open(path, "rb").read()).hexdigest())
rows = list(csv.reader(open(path)))[1:]
dates = [r[0] for r in rows]
vals = [float(r[1]) for r in rows]
assert all(r[1] not in ("", ".") for r in rows)
idx = {d: i for i, d in enumerate(dates)}

def rnd(x, q):  # half-up rounding
    return float(Decimal(repr(x)).quantize(Decimal(q), rounding=ROUND_HALF_UP))

s0, s1 = idx["1994-12-01"], idx["2006-03-01"]
P = []
for s in range(s0, s1 + 1):
    e = s + 240
    P.append(vals[e] / vals[s])
n = len(P)
g = [100 * (p ** (1 / 20) - 1) for p in P]
cov = lambda r: [100 * (1 + r) ** 20 / p for p in P]
c0, c3, c5 = cov(0), cov(0.03), cov(0.05)
full = 100 * ((vals[idx["2026-03-01"]] / vals[idx["1994-12-01"]]) ** (12 / 375) - 1)
res = {
    "windows_20y": n,
    "price_growth_full_period_pct_per_year": rnd(full, "0.01"),
    "price_growth_20y_min_pct_per_year": rnd(min(g), "0.01"),
    "price_growth_20y_median_pct_per_year": rnd(statistics.median(g), "0.01"),
    "price_growth_20y_max_pct_per_year": rnd(max(g), "0.01"),
    "coverage_no_option_median_pct": rnd(statistics.median(c0), "0.1"),
    "coverage_3pct_median_pct": rnd(statistics.median(c3), "0.1"),
    "coverage_3pct_min_pct": rnd(min(c3), "0.1"),
    "coverage_3pct_max_pct": rnd(max(c3), "0.1"),
    "share_3pct_kept_up_pct": rnd(100 * sum(c >= 100 for c in c3) / n, "0.1"),
    "coverage_5pct_median_pct": rnd(statistics.median(c5), "0.1"),
    "coverage_5pct_min_pct": rnd(min(c5), "0.1"),
    "share_5pct_kept_up_pct": rnd(100 * sum(c >= 100 for c in c5) / n, "0.1"),
}
raw = {"full": full, "gmin": min(g), "gmed": statistics.median(g), "gmax": max(g),
       "c0med": statistics.median(c0), "c3med": statistics.median(c3), "c3min": min(c3),
       "c3max": max(c3), "c3n": sum(c >= 100 for c in c3), "c5med": statistics.median(c5),
       "c5min": min(c5), "c5n": sum(c >= 100 for c in c5)}
print(json.dumps(raw, indent=1))
json.dump(res, open(os.path.join(D, "result.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
