import csv, json, os, statistics, math

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "raw")
if not os.path.isdir(BASE):
    BASE = "episodes/ep009/data/raw"


def mi(y, m):
    return y * 12 + m - 1


def lab(i):
    return "%04d-%02d" % (i // 12, i % 12 + 1)


def ym(datestr):
    return mi(int(datestr[:4]), int(datestr[5:7]))


def num(x):
    x = x.strip()
    if x in ("", ".", "NA"):
        return None
    return float(x)


def read_series(fn, col):
    d = {}
    with open(os.path.join(BASE, fn), newline="") as f:
        for row in csv.DictReader(f):
            v = num(row[col])
            d[ym(row["observation_date"])] = v
    return d


hpi = {k: v for k, v in read_series("HPIPONM226N.csv", "HPIPONM226N").items() if v is not None}
cpi_raw = read_series("CUUR0000SEHA.csv", "CUUR0000SEHA")
cpi = {k: v for k, v in cpi_raw.items() if v is not None}
oct25 = mi(2025, 10)
if oct25 not in cpi and (oct25 - 1) in cpi and (oct25 + 1) in cpi:
    cpi[oct25] = math.sqrt(cpi[oct25 - 1] * cpi[oct25 + 1])

wk = {}
with open(os.path.join(BASE, "MORTGAGE30US.csv"), newline="") as f:
    for row in csv.DictReader(f):
        v = num(row["MORTGAGE30US"])
        if v is not None:
            wk.setdefault(ym(row["observation_date"]), []).append(v)
rate = {k: sum(v) / len(v) for k, v in wk.items()}

ret = {}
with open(os.path.join(BASE, "ff3_monthly.csv")) as f:
    for line in f:
        if "Annual" in line:
            break
        parts = [p.strip() for p in line.split(",")]
        if len(parts) >= 5 and len(parts[0]) == 6 and parts[0].isdigit():
            ret[mi(int(parts[0][:4]), int(parts[0][4:]))] = (float(parts[1]) + float(parts[4])) / 100

P = 400000.0
ANCHOR = mi(2026, 7)
FIRST = mi(1991, 1)


def valid(s, H):
    e = s + 12 * H
    if s < FIRST or s not in rate:
        return False
    for m in range(s, e + 1):
        if m not in hpi or m not in cpi:
            return False
    for m in range(s, e):
        if m not in ret:
            return False
    return True


def advantage(s, H, mode, y0=0.05):
    e = s + 12 * H
    r = rate[s] / 1200.0
    L = 0.8 * P
    n = 360
    pay = L * r / (1 - (1 + r) ** -n) if r > 0 else L / n
    bal = L
    ys = y0 * (cpi[s] / hpi[s]) / (cpi[ANCHOR] / hpi[ANCHOR])
    pot = 0.23 * P
    for k in range(12 * H):
        m = s + k
        own = 0.025 / 12 * P * hpi[m] / hpi[s]
        outlay = pay + own
        rent = ys * P / 12 * cpi[m] / cpi[s]
        gap = outlay - rent
        if mode == "cash":
            pot += gap
        elif mode == "stocks":
            pot += gap
            pot *= 1 + ret[m]
        else:
            pot *= 1 + ret[m]
        bal = bal * (1 + r) - pay
    equity = 0.94 * P * hpi[e] / hpi[s] - bal
    return equity - pot


def windows(H):
    return [s for s in range(FIRST, max(hpi) + 1) if valid(s, H)]


def share(vals):
    return round(100.0 * sum(1 for v in vals if v > 0) / len(vals), 1) if vals else None


W10 = windows(10)
adv10 = {md: {s: advantage(s, 10, md) for s in W10} for md in ("cash", "stocks", "lump")}
res = {"n_windows_10y": len(W10), "first_start": lab(W10[0]), "last_start": lab(W10[-1])}
for md in adv10:
    v = list(adv10[md].values())
    res["share_buyer_ahead_" + md] = share(v)
    res["renter_ahead_count_" + md] = sum(1 for x in v if x <= 0)
    res["median_advantage_" + md] = round(statistics.median(v))
st = adv10["stocks"]
smin = min(st, key=st.get)
smax = max(st, key=st.get)
res["stocks_min"] = {"start": lab(smin), "value": round(st[smin])}
res["stocks_max"] = {"start": lab(smax), "value": round(st[smax])}
res["cash_ahead_stocks_not"] = sum(1 for s in W10 if adv10["cash"][s] > 0 and st[s] <= 0)

W15 = windows(15)
a15c = [advantage(s, 15, "cash") for s in W15]
a15s = [advantage(s, 15, "stocks") for s in W15]
res["h15"] = {"n": len(W15), "share_cash": share(a15c), "share_stocks": share(a15s)}

eras = {"1991-01..1999-12": (mi(1991, 1), mi(1999, 12)),
        "2002-01..2007-12": (mi(2002, 1), mi(2007, 12)),
        "2009-01..2016-07": (mi(2009, 1), mi(2016, 7))}
res["eras"] = {}
for name, (a, b) in eras.items():
    ss = [s for s in W10 if a <= s <= b]
    res["eras"][name] = {"n": len(ss),
                         "share_cash": share([adv10["cash"][s] for s in ss]),
                         "share_stocks": share([adv10["stocks"][s] for s in ss])}

res["point_advantages"] = {}
for lbl, s in (("2006-06", mi(2006, 6)), ("2012-04", mi(2012, 4)), ("1991-01", mi(1991, 1))):
    if s in adv10["cash"]:
        res["point_advantages"][lbl] = {"cash": round(adv10["cash"][s]), "stocks": round(adv10["stocks"][s])}
    else:
        res["point_advantages"][lbl] = None

cnt = 0
for s in W10:
    prod = 1.0
    for m in range(s, s + 120):
        prod *= 1 + ret[m]
    if prod < 1:
        cnt += 1
res["windows_stocks_dollar_below_1"] = cnt

res["share_stocks_y0_0.04"] = share([advantage(s, 10, "stocks", 0.04) for s in W10])
res["share_stocks_y0_0.06"] = share([advantage(s, 10, "stocks", 0.06) for s in W10])

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "result.json")
with open(out, "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))
