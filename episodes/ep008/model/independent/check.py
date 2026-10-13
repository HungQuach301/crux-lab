import csv, datetime, statistics
from collections import defaultdict

D = "episodes/ep008/data/raw/"

def read(name):
    out = []
    with open(D + name + ".csv") as f:
        r = csv.reader(f)
        next(r)
        for d, v in r:
            if v.strip() not in ("", "."):
                out.append((datetime.date.fromisoformat(d), float(v)))
    return out

def mi(y, m): return y * 12 + m - 1
def ms(i): return "%04d-%02d" % (i // 12, i % 12 + 1)
def midx(d): return mi(d.year, d.month)

HPI = {midx(d): v for d, v in read("HPIPONM226N")}
CPI = {midx(d): v for d, v in read("CUUR0000SEHA")}
TB = {midx(d): v for d, v in read("TB3MS")}
wk = read("MORTGAGE30US")
acc = defaultdict(list)
for d, v in wk: acc[midx(d)].append(v)
RATE = {k: sum(v) / len(v) for k, v in acc.items()}
CPI[mi(2025, 10)] = (CPI[mi(2025, 9)] * CPI[mi(2025, 11)]) ** 0.5

P = 400000.0
ref = CPI[mi(2026, 7)] / HPI[mi(2026, 7)]

def run(s, H, y0=0.05, tb=False):
    e = s + 12 * H
    if s not in RATE: return None
    for m in range(s, e + 1):
        if m not in HPI or m not in CPI: return None
    if tb:
        for m in range(s, e):
            if m not in TB: return None
    x = RATE[s] / 1200
    L = 0.8 * P
    pay = L * x / (1 - (1 + x) ** -360)
    bal = L
    y = y0 * (CPI[s] / HPI[s]) / ref
    rent0 = y * P / 12
    pot = 0.23 * P
    for k in range(12 * H):
        own = 0.025 / 12 * P * HPI[s + k] / HPI[s]
        out = pay + own
        rent = rent0 * CPI[s + k] / CPI[s]
        pot += out - rent
        if tb: pot *= 1 + TB[s + k] / 1200
        bal = bal * (1 + x) - pay
    eq = 0.94 * P * HPI[e] / HPI[s] - bal
    return dict(s=s, adv=eq - pot, chg=(HPI[e] / HPI[s] - 1) * 100, rate=RATE[s],
                ratio=rent0 / (pay + 0.025 / 12 * P))

def windows(H, **kw):
    r = []
    for s in range(mi(1991, 1), max(HPI) + 1):
        o = run(s, H, **kw)
        if o: r.append(o)
    return r

def share(w, lo=None, hi=None):
    if lo: w = [o for o in w if lo <= o["s"] <= hi]
    return round(100 * sum(o["adv"] > 0 for o in w) / len(w), 1), len(w)

def p(k, v): print(k, "=", v)

W = {}
for H in (5, 10, 15):
    w = W[H] = windows(H)
    t = "%dy" % H
    p("n_" + t, len(w)); p("first_" + t, ms(w[0]["s"])); p("last_" + t, ms(w[-1]["s"]))
    p("share_buyer_ahead_" + t, share(w)[0])
    p("median_adv_" + t, round(statistics.median(o["adv"] for o in w)))
    b = max(w, key=lambda o: o["adv"]); c = min(w, key=lambda o: o["adv"])
    p("best_start_" + t, ms(b["s"])); p("best_adv_" + t, round(b["adv"]))
    p("worst_start_" + t, ms(c["s"])); p("worst_adv_" + t, round(c["adv"]))
    p("n_renter_ahead_" + t, sum(o["adv"] <= 0 for o in w))

w = W[10]
lo = min(w, key=lambda o: o["chg"]); hi = max(w, key=lambda o: o["chg"])
p("worst_price_change_10y", "%.1f (start %s)" % (lo["chg"], ms(lo["s"])))
p("best_price_change_10y", "%.1f (start %s)" % (hi["chg"], ms(hi["s"])))
b = max(w, key=lambda o: o["adv"]); c = min(w, key=lambda o: o["adv"])
p("worst_rate_10y (rate at worst-advantage start)", "%.2f" % c["rate"])
p("best_rate_10y (rate at best-advantage start)", "%.2f" % b["rate"])
p("min_rate_over_10y_windows", "%.2f" % min(o["rate"] for o in w))
p("max_rate_over_10y_windows", "%.2f" % max(o["rate"] for o in w))
for a, bb in ((mi(1991, 1), mi(1999, 12)), (mi(2002, 1), mi(2007, 12)), (mi(2009, 1), mi(2016, 7))):
    sh, n = share(w, a, bb)
    p("era_share_%s..%s_10y" % (ms(a), ms(bb)), "%s (n=%d)" % (sh, n))
r = [o for o in w if o["adv"] <= 0]
p("renter_first_10y", ms(r[0]["s"]) if r else None)
p("renter_last_10y", ms(r[-1]["s"]) if r else None)
t = windows(10, tb=True)
p("share_tbills_10y", "%s (n=%d)" % share(t))
for nm, y in (("yield4pct", .04), ("yield6pct", .06), ("census1579", 12 * 1579 / 339100), ("census1464", 12 * 1464 / 363800)):
    p("share_%s_10y" % nm, "%s (n=%d)" % share(windows(10, y0=y)))

last = wk[-1][0]
rm = midx(last) if (last + datetime.timedelta(days=7)).month != last.month else midx(last) - 1
p("rate_month_latest", ms(rm)); p("rate_latest", "%.2f" % RATE[rm])
x = RATE[rm] / 1200
pay = 0.8 * P * x / (1 - (1 + x) ** -360)
ob = pay + 0.025 / 12 * P
rent = 0.05 * P / 12
p("today_buyer_month1", round(ob)); p("today_rent_month1", round(rent))
p("today_rent_to_outlay", round(100 * rent / ob, 1))
m = min(w, key=lambda o: o["ratio"])
p("lowest_month1_rent_to_outlay_10y", "%.4f at %s" % (m["ratio"], ms(m["s"])))
