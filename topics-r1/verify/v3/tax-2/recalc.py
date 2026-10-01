import csv, json, os
from decimal import Decimal, ROUND_HALF_UP
base = os.path.dirname(os.path.abspath(__file__))

def load(sid):
    out = {}
    with open(os.path.join(base, "data", sid + ".csv")) as f:
        for row in csv.DictReader(f):
            v = row[sid].strip()
            if v not in ("", "."):
                out[row["observation_date"]] = Decimal(v)
    return out

def rnd(x, q):  # half-up to multiple q
    return float((Decimal(x) / Decimal(q)).quantize(Decimal(1), ROUND_HALF_UP) * Decimal(q))

def r4(x):
    return float(Decimal(x).quantize(Decimal("0.0001"), ROUND_HALF_UP))

metros = {"los_angeles": "ATNHPIUS31084Q", "san_diego": "ATNHPIUS41740Q",
          "san_francisco": "ATNHPIUS41884Q", "san_jose": "ATNHPIUS41940Q",
          "seattle": "ATNHPIUS42644Q", "boston": "ATNHPIUS14454Q",
          "new_york": "ATNHPIUS35614Q", "miami": "ATNHPIUS33124Q",
          "denver": "ATNHPIUS19740Q", "phoenix": "ATNHPIUS38060Q",
          "dallas": "ATNHPIUS19124Q", "chicago": "ATNHPIUS16984Q"}

def growth(sid):
    s = load(sid)
    base2000 = sum(s[d] for d in ["2000-01-01", "2000-04-01", "2000-07-01", "2000-10-01"]) / 4
    return s["2026-04-01"] / base2000

res = {}
thr = {}
for m, sid in metros.items():
    g = growth(sid)
    res["growth_" + m] = r4(g)
    t = Decimal(500000) / (g - 1)
    thr[m] = t
    res["threshold_joint_%s_usd" % m] = rnd(t, 100)
gu = growth("USSTHPI")
res["growth_us"] = r4(gu)
res["threshold_joint_us_usd"] = rnd(Decimal(500000) / (gu - 1), 100)
res["threshold_single_us_usd"] = rnd(Decimal(250000) / (gu - 1), 100)
res["threshold_joint_min_usd"] = rnd(min(thr.values()), 100)
res["threshold_joint_max_usd"] = rnd(max(thr.values()), 100)
res["metros_threshold_under_200k"] = sum(1 for t in thr.values() if t < 200000)
res["metros_threshold_under_300k"] = sum(1 for t in thr.values() if t < 300000)
cpi = load("CPIAUCNS")
res["cpi_1997_05"] = float(cpi["1997-05-01"])
res["cpi_2026_08"] = float(cpi["2026-08-01"])
res["excl_joint_1997_in_2026_usd"] = rnd(Decimal(500000) * cpi["2026-08-01"] / cpi["1997-05-01"], 1000)
for k, v in list(res.items()):
    if isinstance(v, float) and v.is_integer() and not k.startswith(("growth", "cpi")):
        res[k] = int(v)
json.dump(res, open(os.path.join(base, "result.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
print({m: float(t) for m, t in thr.items()})
