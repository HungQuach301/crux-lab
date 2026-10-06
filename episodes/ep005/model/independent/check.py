#!/usr/bin/env python3
"""Independent recomputation of ep005 claims from numbers.md definitions only.

Written from scratch; does not import or read model/*.py, out/model.json,
or the dossier calc.py/result.json. Reads data/raw/*.csv only.
Usage: python3 episodes/ep005/model/independent/check.py
"""
import csv, os, statistics, json
from collections import defaultdict
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.normpath(os.path.join(HERE, "..", "..", "data", "raw"))


def load(name):
    out = []
    with open(os.path.join(RAW, name + ".csv")) as f:
        r = csv.reader(f)
        next(r)
        for d, v in r:
            if v.strip() in ("", "."):
                continue
            out.append((date.fromisoformat(d), float(v)))
    return out


def ym(d):
    return (d.year, d.month)


def add_months(t, k):
    y, m = t
    n = y * 12 + (m - 1) + k
    return (n // 12, n % 12 + 1)


def ymstr(t):
    return f"{t[0]:04d}-{t[1]:02d}-01"


# ---------------- mortgage maths (price normalised to 1) ----------------
LOAN = 0.90
N = 360


def payment(rate_pct, loan=LOAN, n=N):
    r = rate_pct / 1200.0
    return loan * r / (1 - (1 + r) ** -n)


def balances(rate_pct, loan=LOAN, n=N):
    """B_0..B_n by explicit amortisation recursion."""
    r = rate_pct / 1200.0
    p = payment(rate_pct, loan, n)
    b = [loan]
    for _ in range(n):
        b.append(b[-1] * (1 + r) - p)
    return b


def sched(rate_pct, frac):
    b = balances(rate_pct)
    for k in range(1, N + 1):
        if b[k] <= frac + 1e-12:
            return k
    return None


# ---------------- data ----------------
pmms = load("MORTGAGE30US")
hpi = {ym(d): v for d, v in load("HPIPONM226N")}
cs = {ym(d): v for d, v in load("CSUSHPINSA")}
mspus = load("MSPUS")
ob = load("OBMMIC30YF")

weeks_by_month = defaultdict(list)
for d, v in pmms:
    weeks_by_month[ym(d)].append(v)
rate_m = {k: sum(v) / len(v) for k, v in weeks_by_month.items()}

# latest complete month: the month of the last weekly date is complete only if
# a later weekly date exists in a later month. With the last date 2026-10-01,
# 2026-10 is incomplete; latest complete = month before.
last_date = pmms[-1][0]
months_sorted = sorted(rate_m)
latest_complete = months_sorted[-2] if True else None  # last month is by construction incomplete
# sanity: verify via rule "next weekly date falls in a later month"
for i, (d, v) in enumerate(pmms[:-1]):
    pass
complete = set()
for i in range(len(pmms) - 1):
    if ym(pmms[i + 1][0]) != ym(pmms[i][0]):
        complete.add(ym(pmms[i][0]))
latest_complete = max(complete)
rate_latest = rate_m[latest_complete]

R = {}  # claim -> computed value (raw)
R["rate_month_latest"] = ymstr(latest_complete)
R["rate_latest"] = rate_latest
R["rate_latest_nweeks"] = len(weeks_by_month[latest_complete])
R["rate_partial"] = rate_m[ym(last_date)]
R["rate_partial_nweeks"] = len(weeks_by_month[ym(last_date)])
R["sched80_months_latest"] = sched(rate_latest, 0.80)
R["sched78_months_latest"] = sched(rate_latest, 0.78)
# calc.py warning: max-month rule picks 2026-10 (7.28)
R["warn_maxmonth_sched80"] = sched(R["rate_partial"], 0.80)
R["warn_maxmonth_sched78"] = sched(R["rate_partial"], 0.78)

# midpoint
R["midpoint_months"] = N // 2
bind = [(rate_m[t], t) for t in months_sorted if t in complete and sched(rate_m[t], 0.78) > 180]
R["midpoint_binding_rate_min"] = min(bind)[0]
R["midpoint_binding_rate_min_month"] = ymstr(min(bind)[1])
R["midpoint_last_binding_month"] = ymstr(max(t for _, t in bind))
# also: threshold rate where sched78 crosses 180 (continuous)
lo, hi = 5.0, 20.0
for _ in range(60):
    mid = (lo + hi) / 2
    if sched(mid, 0.78) > 180:
        hi = mid
    else:
        lo = mid
R["midpoint_threshold_rate_continuous"] = hi


def run_sets(H, tag):
    last_h = max(H)
    A = [t for t in sorted(H) if (1991, 1) <= t <= (2024, 7) and add_months(t, 24) in H]
    B = [t for t in sorted(H) if (1991, 1) <= t <= (2016, 7) and add_months(t, 120) in H]
    out = {}
    out["nA"] = len(A)
    out["nB"] = len(B)
    ltv24 = {}
    for t in A:
        b = balances(rate_m[t])
        ltv24[t] = b[24] / (H[add_months(t, 24)] / H[t])
    out["shareA_ltv24_le80"] = sum(v <= 0.80 for v in ltv24.values()) / len(A)
    out["shareA_ltv24_le75"] = sum(v <= 0.75 for v in ltv24.values()) / len(A)
    s80A = [sched(rate_m[t], 0.80) for t in A]
    out["sched80_min_A"], out["sched80_max_A"] = min(s80A), max(s80A)
    out["rateA_min"] = min(rate_m[t] for t in A)
    out["rateA_max"] = max(rate_m[t] for t in A)
    T = {}
    for t in B:
        b = balances(rate_m[t])
        k = 1
        T[t] = None
        while add_months(t, k) in H and k <= N:
            if b[k] / (H[add_months(t, k)] / H[t]) <= 0.80:
                T[t] = k
                break
            k += 1
    assert all(v is not None for v in T.values()), "some B month never reached 80%"
    vals = list(T.values())
    med = statistics.median(vals)
    out["medianB_months_to80"] = med
    out["minB_months_to80"] = min(vals)
    out["maxB_months_to80"] = max(vals)
    out["maxB_start"] = ymstr(min(t for t in B if T[t] == max(vals)))
    out["shareB_over60"] = sum(v > 60 for v in vals) / len(B)
    out["shareB_le_sched80"] = sum(T[t] <= sched(rate_m[t], 0.80) for t in B) / len(B)

    def buyer(t):
        b = balances(rate_m[t])
        return {
            "month": ymstr(t),
            "rate": rate_m[t],
            "T": T[t],
            "sched80": sched(rate_m[t], 0.80),
            "index_change_to_T": H[add_months(t, T[t])] / H[t] - 1,
            "ltv24": b[24] / (H[add_months(t, 24)] / H[t]),
        }

    # "ties -> latest year": take the latest calendar year among tied months,
    # then the earliest month in that year (literal reading: year, not month).
    # Alternative reading (latest tied month overall) is reported as fast_alt.
    ties_fast = [t for t in B if T[t] == min(vals)]
    ly = max(t[0] for t in ties_fast)
    fast = min(t for t in ties_fast if t[0] == ly)
    fast_alt = max(ties_fast)
    typical = max(t for t in B if T[t] == med)              # latest such month
    slow = min(t for t in B if T[t] == max(vals))           # earliest on ties
    out["buyer_fast"] = buyer(fast)
    out["buyer_fast_alt_latest_month"] = buyer(fast_alt)
    out["buyer_typical"] = buyer(typical)
    out["buyer_slow"] = buyer(slow)
    out["fast_ties"] = [ymstr(t) for t in B if T[t] == min(vals)]
    out["typical_ties"] = [ymstr(t) for t in B if T[t] == med]
    out["slow_ties"] = [ymstr(t) for t in B if T[t] == max(vals)]
    return out

R["fhfa"] = run_sets(hpi, "fhfa")
R["cs"] = run_sets(cs, "cs")

# example
R["mspus_latest"] = mspus[-1][1]
R["mspus_latest_date"] = mspus[-1][0].isoformat()
ex_price = (int(R["mspus_latest"]) // 100000) * 100000  # rounded down to round number
R["ex_price"] = ex_price
R["ex_loan"] = 0.90 * ex_price
R["ex_payment_pi"] = payment(rate_latest, R["ex_loan"])
R["ex_target80"] = 0.80 * ex_price
R["ex_target78"] = 0.78 * ex_price
bd = balances(rate_latest, R["ex_loan"])
R["ex_reach80"] = next(k for k in range(1, N + 1) if bd[k] <= R["ex_target80"])
R["ex_reach78"] = next(k for k in range(1, N + 1) if bd[k] <= R["ex_target78"])
R["ex_extra_down_for_20"] = 0.20 * ex_price - 0.10 * ex_price
R["nora_carla_gap_months"] = None
f = R["fhfa"]["buyer_fast"]["month"]; s = R["fhfa"]["buyer_slow"]["month"]
fy, fm = int(f[:4]), int(f[5:7]); sy, sm = int(s[:4]), int(s[5:7])
R["nora_carla_gap_months"] = abs((sy * 12 + sm) - (fy * 12 + fm))

# crosschecks
# (a) PMMS weekly vs Optimal Blue 7-day mean (dates in (d-7, d]); weeks from 2017-01-12
obd = dict(ob)
cc = []
for d, v in pmms:
    if d < date(2017, 1, 1):
        continue
    w = [obd[d - timedelta(days=i)] for i in range(7) if (d - timedelta(days=i)) in obd]
    if not w or (d - timedelta(days=7)) < ob[0][0]:
        continue
    cc.append(abs(v - sum(w) / len(w)))
R["xc_pmms_weeks"] = len(cc)
R["xc_pmms_within"] = sum(g <= 0.5 for g in cc)
R["xc_pmms_maxgap"] = max(cc)
R["xc_pmms_meangap"] = sum(cc) / len(cc)
# (b) HPI m/m vs CS m/m, 1991-02..2026-07
mm = []
for t in sorted(hpi):
    p = add_months(t, -1)
    if p in hpi and t in cs and p in cs:
        a = (hpi[t] / hpi[p] - 1) * 100
        c = (cs[t] / cs[p] - 1) * 100
        mm.append(abs(round(a, 2) - round(c, 2)) if False else abs(a - c))
R["xc_hpi_months"] = len(mm)
R["xc_hpi_within"] = sum(g <= 0.5 for g in mm)
R["xc_hpi_maxgap"] = max(mm)

# ---------------- comparison ----------------
F, C = R["fhfa"], R["cs"]
pct = lambda x: f"{100*x:.1f}%"
checks = [
    # (claim id, expected display string, computed display string)
    ("rate_month_latest", "2026-09-01", R["rate_month_latest"]),
    ("rate_latest (4 weeks)", "6.862 / 4", f"{R['rate_latest']:.3f} / {R['rate_latest_nweeks']}"),
    ("rate_partial (1 week)", "7.28 / 1", f"{R['rate_partial']:.2f} / {R['rate_partial_nweeks']}"),
    ("sched80_months_latest", "99", str(R["sched80_months_latest"])),
    ("sched78_months_latest", "114", str(R["sched78_months_latest"])),
    ("warning: max-month rule 80/78", "104/119", f"{R['warn_maxmonth_sched80']}/{R['warn_maxmonth_sched78']}"),
    ("midpoint_months", "180", str(R["midpoint_months"])),
    ("midpoint_binding_rate_min", "12.56", f"{R['midpoint_binding_rate_min']:.2f}"),
    ("midpoint last binding month", "1985-05-01", R["midpoint_last_binding_month"]),
    ("sched80_min_A / max_A", "58 / 132", f"{F['sched80_min_A']} / {F['sched80_max_A']}"),
    ("set A rate range", "2.68%–9.64%", f"{F['rateA_min']:.2f}%–{F['rateA_max']:.2f}%"),
    ("nA", "403", str(F["nA"])),
    ("shareA_ltv24_le80", "58.6%", pct(F["shareA_ltv24_le80"])),
    ("shareA_ltv24_le75", "15.6%", pct(F["shareA_ltv24_le75"])),
    ("nB", "307", str(F["nB"])),
    ("medianB_months_to80", "23", f"{F['medianB_months_to80']:g}"),
    ("minB_months_to80", "13", str(F["minB_months_to80"])),
    ("shareB_over60", "14.7%", pct(F["shareB_over60"])),
    ("maxB_months_to80", "112", str(F["maxB_months_to80"])),
    ("maxB_start", "2005-10-01", F["maxB_start"]),
    ("shareB_le_sched80", "90.6%", pct(F["shareB_le_sched80"])),
]
for key, name, exp in [
    ("buyer_fast", "Nora", ("2004-01-01", "5.71%", "13", "86", "+11.2%", "0.725")),
    ("buyer_typical", "Ben", ("2014-06-01", "4.16%", "23", "71", "+9.8%", "0.784")),
    ("buyer_slow", "Carla", ("2005-10-01", "6.07%", "112", "90", "-3.3%", "0.867")),
]:
    b = F[key]
    got = (b["month"], f"{b['rate']:.2f}%", str(b["T"]), str(b["sched80"]),
           f"{100*b['index_change_to_T']:+.1f}%", f"{b['ltv24']:.3f}")
    labels = ("month", "rate", "months to 80%", "schedule", "index change to T", "LTV at 24")
    for lab, e, g in zip(labels, exp, got):
        checks.append((f"{key}_* ({name}) {lab}", e, g))
checks += [
    ("Nora–Carla gap (months)", "21", str(R["nora_carla_gap_months"])),
    ("mspus_latest", "410700 (2026-04-01)", f"{R['mspus_latest']:.0f} ({R['mspus_latest_date']})"),
    ("ex_price", "400000", str(R["ex_price"])),
    ("ex_loan", "360000", f"{R['ex_loan']:.0f}"),
    ("ex_payment_pi", "2361.94", f"{R['ex_payment_pi']:.2f}"),
    ("ex_target80 / ex_target78", "320000 / 312000", f"{R['ex_target80']:.0f} / {R['ex_target78']:.0f}"),
    ("ex reached at payment 80/78", "99 / 114", f"{R['ex_reach80']} / {R['ex_reach78']}"),
    ("ex_extra_down_for_20", "40000", f"{R['ex_extra_down_for_20']:.0f}"),
    ("robust_cs_medianB", "23", f"{C['medianB_months_to80']:g}"),
    ("robust_cs_maxB (start)", "119 (2006-04-01)", f"{C['maxB_months_to80']} ({C['maxB_start']})"),
    ("robust_cs shareB_over60", "14.7%", pct(C["shareB_over60"])),
    ("robust_cs shareA <=80", "0.561", f"{C['shareA_ltv24_le80']:.3f}"),
    ("robust_cs shareA <=75", "0.233", f"{C['shareA_ltv24_le75']:.3f}"),
    ("xc PMMS vs OB 7-day: within/weeks", "508/508", f"{R['xc_pmms_within']}/{R['xc_pmms_weeks']}"),
    ("xc PMMS vs OB 7-day: max gap", "0.384", f"{R['xc_pmms_maxgap']:.3f}"),
    ("xc HPI vs CS m/m: within/months", "374/426", f"{R['xc_hpi_within']}/{R['xc_hpi_months']}"),
]

if __name__ == "__main__":
    ok = 0
    for cid, e, g in checks:
        m = (e == g)
        ok += m
        print(f"{'OK ' if m else 'XX '} {cid:45s} expected={e:22s} got={g}")
    print(f"\n{ok}/{len(checks)} matched")
    print("\nextra:", json.dumps({
        "midpoint_threshold_rate_continuous": R["midpoint_threshold_rate_continuous"],
        "midpoint_binding_rate_min_month": R["midpoint_binding_rate_min_month"],
        "fast_ties": F["fast_ties"], "typical_ties": F["typical_ties"], "slow_ties": F["slow_ties"],
        "cs_slow_ties": C["slow_ties"], "buyer_fast_alt_latest_month": F["buyer_fast_alt_latest_month"], "xc_pmms_meangap": R["xc_pmms_meangap"],
        "xc_hpi_maxgap": R["xc_hpi_maxgap"], "sept_weeks": weeks_by_month[latest_complete],
    }, indent=1))
