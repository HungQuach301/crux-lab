"""Independent recompute of ep006 numbers.md claims from definitions only."""
import csv, statistics as st, re, json, sys
from pathlib import Path
EP = Path(__file__).resolve().parents[2]
RAW = EP / "data/raw"

def load(name):
    d = {}
    with open(RAW / f"{name}.csv") as f:
        r = csv.reader(f); next(r)
        for row in r:
            if len(row) < 2 or row[1].strip() in ("", "."): continue
            y, m, _ = row[0].split("-"); d[(int(y), int(m))] = float(row[1])
    return d

def add(ym, k):
    t = ym[0] * 12 + ym[1] - 1 + k
    return (t // 12, t % 12 + 1)

def ds(ym): return f"{ym[0]:04d}-{ym[1]:02d}-01"

def windows(I, months, start=(1947, 1)):
    out = []; s = start; last = max(I)
    while add(s, months) <= last:
        e = add(s, months)
        if s in I and e in I: out.append((s, I[e] / I[s]))
        s = add(s, 1)
    return out

cpi, cpiw, pce = load("CPIAUCNS"), load("CWUR0000SA0"), load("PCEPI")
G20, G25 = 1.02 ** 20, 1.02 ** 25
w20 = windows(cpi, 240); w25 = windows(cpi, 300)
kept = [s for s, P in w20 if G20 >= P]
r2 = [(s, 100 * G20 / P) for s, P in w20]
lvl = {s: 100 / P for s, P in w20}
infl = [100 * (P ** (1 / 20) - 1) for s, P in w20]
worst = min(r2, key=lambda x: (x[1], x[0]))
last = max(cpi)
ls, lP = w20[-1]
med_r2 = st.median(v for _, v in r2)

gs = (2006, 8)
def g2(k): return 100 * 1.02 ** k / (cpi[add(gs, 12 * k)] / cpi[gs])
def gl(k): return 100 / (cpi[add(gs, 12 * k)] / cpi[gs])
gks = [k for k in range(1, 21) if add(gs, 12 * k) in cpi]
above = [k for k in gks if g2(k) >= 100]

def first_k(s, thr):
    for k in range(1, 21):
        e = add(s, 12 * k)
        if e in cpi and 100 / (cpi[e] / cpi[s]) <= thr: return k
    return None
fk = [first_k(s, med_r2) for s, _ in w20]
fk_r = [first_k(s, 80.7) for s, _ in w20]

dec = lambda d: [v for s, v in r2 if d <= s[0] < d + 10]
def share(ws, g): return 100 * sum(g >= P for _, P in ws) / len(ws)
wcw = windows(cpiw, 240); wpce = windows(pce, 240, (1959, 1))

mine = {
 "cpi_yoy_latest_pct": 100 * (cpi[last] / cpi[add(last, -12)] - 1),
 "index_last_month": ds(last),
 "windows_20y": len(w20),
 "windows_2pct_kept_up_20y": len(kept),
 "share_2pct_kept_up_20y_pct": 100 * len(kept) / len(w20),
 "kept_up_first_start_20y": ds(kept[0]),
 "kept_up_last_start_20y": ds(kept[-1]),
 "windows_25y": len(w25),
 "windows_2pct_kept_up_25y": sum(G25 >= P for _, P in w25),
 "median_inflation_20y_pct_per_year": st.median(infl),
 "median_real_value_2pct_payment_after_20y_pct": med_r2,
 "median_real_value_level_payment_after_20y_pct": st.median(lvl.values()),
 "worst_real_value_2pct_payment_after_20y_pct": worst[1],
 "worst_real_value_level_payment_after_20y_pct": lvl[worst[0]],
 "worst_window_start_year_20y": worst[0][0],
 "share_2pct_at_least_90_after_20y_pct": 100 * sum(v >= 90 for _, v in r2) / len(r2),
 "share_2pct_at_least_75_after_20y_pct": 100 * sum(v >= 75 for _, v in r2) / len(r2),
 "two_pct_growth_20y_pct": 100 * (G20 - 1),
 "latest_start / latest_end": f"{ds(ls)} / {ds(add(ls, 240))}",
 "latest_window_real_value_2pct_payment_pct": 100 * G20 / lP,
 "latest_window_real_value_level_payment_pct": 100 / lP,
 "latest_window_price_rise_pct": 100 * (lP - 1),
 "latest_window_inflation_pct_per_year": 100 * (lP ** (1 / 20) - 1),
 "guide_start": ds(gs),
 "guide_last_year_2pct_at_or_above_100": max(above),
 "guide_years_2pct_at_or_above_100": len(above),
 "guide_real_2pct_2022_pct": g2(16),
 "guide_real_level_2021_pct": gl(15),
 "guide_real_2pct_end_pct": g2(20),
 "guide_real_level_end_pct": gl(20),
 "guide_year_level_reaches_2pct_end": next(k for k in gks if gl(k) <= g2(20)),
 "median_year_level_reaches_2pct_end_median": st.median(k for k in fk if k is not None),
 "by_decade_1990_median_real_2pct": st.median(dec(1990)),
 "by_decade_2000_kept": sum(v >= 100 for v in dec(2000)),
 "by_decade_2000_max_real_2pct": max(dec(2000)),
 "by_decade_1960_median_real_2pct": st.median(dec(1960)),
 "raise_needed_half_20y_pct": st.median(infl),
 "raise_needed_all_20y_pct": max(infl),
 "raise_grid_3pct": share(w20, 1.03 ** 20),
 "robust_cpiw_share_kept_up_20y_pct": share(wcw, G20),
 "robust_pce_share_kept_up_20y_pct": share(wpce, G20),
 "cpiu_from_pce_start_kept_up_20y": sum(G20 >= P for s, P in w20 if s >= (1959, 1)),
 "robust_pce_median_real_2pct_pct": st.median(100 * G20 / P for _, P in wpce),
}
extra = {
 "guide_k15_2pct": g2(15), "guide_above_ks": above, "guide_level_k5": gl(5),
 "fk_none_count": fk.count(None), "fk_median_with_80.7": st.median(k for k in fk_r if k is not None),
 "fk_skipped_missing_anniv": sum(1 for s,_ in w20 for k in range(1,21) if add(s,12*k) <= last and add(s,12*k) not in cpi),
 "worst_start": ds(worst[0]), "max_infl_start": ds(w20[infl.index(max(infl))][0]),
 "n_1990": len(dec(1990)), "n_2000": len(dec(2000)), "n_cpiw": len(wcw), "kept_cpiw": sum(G20>=P for _,P in wcw),
 "n_pce": len(wpce), "kept_pce": sum(G20>=P for _,P in wpce), "n_cpiu_1959": sum(1 for s,_ in w20 if s>=(1959,1)),
 "first_last_20": (ds(w20[0][0]), ds(w20[-1][0])), "first_last_25": (ds(w25[0][0]), ds(w25[-1][0])),
 "decade_medians": {d: round(st.median(dec(d)), 1) for d in range(1940, 2010, 10)},
 "decade_kept": {d: sum(v >= 100 for v in dec(d)) for d in range(1940, 2010, 10)},
 "share_25y": share(w25, G25),
}

# compare against numbers.md
rows = []
for line in (EP / "numbers.md").read_text().splitlines():
    m = re.match(r"\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|", line)
    if m: rows.append((m.group(1), m.group(2)))
res = []
for cid, val in rows:
    v = mine.get(cid)
    if isinstance(v, str): mv, ok = v, v == val
    elif isinstance(v, int): mv, ok = str(v), str(v) == val
    else:
        dp = len(val.split(".")[1]) if "." in val else 0
        mv = f"{v:.{dp}f}"; ok = mv == val
    res.append((cid, val, mv, ok))
if __name__ == "__main__":
    print(f"{sum(r[3] for r in res)}/{len(res)} khớp")
    for r in res: print(*r, sep=" | ")
    print(json.dumps(extra, indent=1, default=str))

# 9 statements (statements.json), checked from values above
lvl_l = [lvl[s] for s, _ in w20]
STMTS = {
 1: len(w20) == 715 and w20[0][0] == (1947, 1) and w20[-1][0][0] == 2006 and f"{mine['share_2pct_kept_up_20y_pct']:.1f}" == "2.4" and len(kept) == 17 and all(1947 <= s[0] <= 1949 for s in kept),
 2: f"{extra['share_25y']:.1f}" == "0.0",
 3: f"{mine['median_inflation_20y_pct_per_year']:.1f}" == "3.1" and f"{med_r2:.1f}" == "80.7" and f"{st.median(lvl_l):.1f}" == "54.3",
 4: worst[0][0] == 1966 and f"{worst[1]:.1f}" == "43.1",
 5: ls == (2006, 8) and f"{mine['latest_window_real_value_2pct_payment_pct']:.1f}" == "90.4" and f"{mine['latest_window_real_value_level_payment_pct']:.1f}" == "60.9",
 6: all(v > lvl[s] for s, v in r2) and len(kept) / len(w20) < 0.05,
 7: all(extra["decade_kept"][d] == 0 and extra["decade_medians"][d] < 100 for d in range(1950, 2010, 10)) and all(v > lvl[s] for s, v in r2 if s >= (1950, 1)),
 8: len(kept) == 17 and len(w20) == 715 and kept[-1] <= (1949, 12),
 9: f"{mine['median_inflation_20y_pct_per_year']:.1f}" == "3.1" and w20[0][0][0] == 1947 and add(w20[-1][0], 240)[0] == 2026,
}
near = sorted(abs(v - 100) for _, v in r2)[:3]
if __name__ == "__main__":
    print("statements", STMTS, "closest-to-100 margins", near)
