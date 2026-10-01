import csv, json, math, calendar, statistics, hashlib
from datetime import date
from decimal import Decimal, ROUND_HALF_UP

def rnd(x, q):
    return float(Decimal(repr(x)).quantize(Decimal(q), rounding=ROUND_HALF_UP))

def pmt(p, rate):
    x = rate / 1200
    return p * x / (1 - (1 + x) ** -360)

res = {}
saving = pmt(100000, 7.00) - pmt(100000, 6.75)
res["monthly_saving_per_100k"] = rnd(saving, "0.01")
be = 1.0 / (saving / 1000)  # point = $1 per $100; saving per $100
res["breakeven_months"] = rnd(be, "0.1")
H = math.ceil(be)
res["horizon_months"] = H
res["drop_needed_pts"] = rnd((7.00 - 6.75) + 1.00, "0.01")
DROP = 125

rows = []
with open("data/MORTGAGE30US.csv") as f:
    for r in csv.DictReader(f):
        v = r["MORTGAGE30US"].strip()
        if v in ("", "."):
            continue
        d = date.fromisoformat(r["observation_date"])
        if date(1971, 4, 2) <= d <= date(2026, 9, 24):
            rows.append((d, int(round(float(v) * 100))))
LAST = date(2026, 9, 24)

def add_months(d, m):
    y, mo = divmod(d.month - 1 + m, 12)
    y += d.year; mo += 1
    return date(y, mo, min(d.day, calendar.monthrange(y, mo)[1]))

elig = []
for i, (d, r) in enumerate(rows):
    he = add_months(d, H)
    if he > LAST:
        continue
    hit_days = None
    for d2, r2 in rows[i + 1:]:
        if d2 > he:
            break
        if r2 <= r - DROP:
            hit_days = (d2 - d).days
            break
    elig.append((d, r, hit_days))

res["n_weeks"] = len(elig)
res["first_week"] = elig[0][0].isoformat()
res["last_week"] = elig[-1][0].isoformat()
hits = [e for e in elig if e[2] is not None]
res["share_refi_before_breakeven"] = rnd(len(hits) / len(elig) * 100, "0.1")
res["median_months_to_trigger"] = rnd(statistics.median([e[2] / 30.4375 for e in hits]), "0.1")
band = [e for e in elig if 650 <= e[1] <= 750]
res["n_weeks_6_5_to_7_5"] = len(band)
res["share_refi_before_breakeven_6_5_to_7_5"] = rnd(sum(e[2] is not None for e in band) / len(band) * 100, "0.1")
res["latest_rate"] = [r for d, r in rows if d == LAST][0] / 100

json.dump(res, open("result.json", "w"), indent=1)
print(json.dumps(res, indent=1))
print("unrounded saving", saving, "be", be, "hits", len(hits), "band hits", sum(e[2] is not None for e in band))
print("sha", hashlib.sha256(open("data/MORTGAGE30US.csv","rb").read()).hexdigest())
