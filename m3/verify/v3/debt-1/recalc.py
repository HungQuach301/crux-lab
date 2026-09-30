import csv, json
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP

END = date(2026, 9, 24)
rows = []
with open("data/MORTGAGE30US.csv") as f:
    for r in csv.DictReader(f):
        v = r["MORTGAGE30US"].strip()
        if v in ("", "."):
            continue
        d = date.fromisoformat(r["observation_date"])
        if date(1971, 4, 2) <= d <= END:
            rows.append((d, int((Decimal(v) * 100).to_integral_value(ROUND_HALF_UP))))
rows.sort()

def r1(x):
    return float(Decimal(str(x)).quantize(Decimal("0.1"), ROUND_HALF_UP))

def share(years, start=None, stop=None):
    h = round(365.25 * years)
    succ = n = 0
    for i, (d, v) in enumerate(rows):
        hend = d + timedelta(days=h)
        if hend > END:
            continue
        if start and d < start: continue
        if stop and d > stop: continue
        fut = [x for (dd, x) in rows[i+1:] if dd <= hend]
        n += 1
        if fut and min(fut) <= v - 100:
            succ += 1
    return r1(succ / n * 100), n

out = {}
for y, k in [(3, "3y"), (2, "2y"), (5, "5y")]:
    s, n = share(y)
    out[f"share_{k}_1pt"] = s
    out[f"n_weeks_{k}"] = n
s, n = share(3, date(1981, 10, 9), date(2020, 12, 31))
out["share_3y_1pt_falling_era"] = s
out["n_weeks_3y_falling_era"] = n
out["latest_rate"] = rows[-1][1] / 100
print(json.dumps(out, indent=1))
