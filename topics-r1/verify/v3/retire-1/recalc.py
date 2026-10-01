import csv, json, statistics, hashlib
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
D = Path(__file__).parent
raw = (D/"data/CPIAUCNS.csv").read_bytes()
SHA_OK = hashlib.sha256(raw).hexdigest() == "f79e3a78837142293449cee4a1a9b1da7be677fb3e989ffb2ef48e8e7cf4cdd7"
cpi = {}
for row in csv.DictReader(open(D/"data/CPIAUCNS.csv")):
    v = row["CPIAUCNS"].strip()
    if v and v != ".":
        y, m, _ = row["observation_date"].split("-")
        cpi[(int(y), int(m))] = float(v)
def add(ym, k):
    t = ym[0]*12 + ym[1]-1 + k
    return (t//12, t%12+1)
def rnd(x, q): return float(Decimal(repr(x)).quantize(Decimal(q), rounding=ROUND_HALF_UP))
def windows(n):
    out = []
    for s in sorted(cpi):
        if s < (1947, 1): continue
        e = add(s, n)
        if e in cpi: out.append((s, cpi[e]/cpi[s]))
    return out
w20 = windows(240); w25 = windows(300)
g20 = 1.02**20; g25 = 1.02**25
kept20 = sum(1 for _, P in w20 if g20 >= P)
kept25 = sum(1 for _, P in w25 if g25 >= P)
r2 = [(100*g20/P, s) for s, P in w20]
worst = min(r2)
Plat = cpi[(2026, 8)]/cpi[(2006, 8)]
res = {
 "windows_20y": len(w20),
 "share_2pct_kept_up_20y_pct": rnd(100*kept20/len(w20), "0.1"),
 "windows_2pct_kept_up_20y": kept20,
 "windows_25y": len(w25),
 "share_2pct_kept_up_25y_pct": rnd(100*kept25/len(w25), "0.1"),
 "median_inflation_20y_pct_per_year": rnd(statistics.median([100*(P**(1/20)-1) for _, P in w20]), "0.01"),
 "median_real_value_2pct_payment_after_20y_pct": rnd(statistics.median([v for v, _ in r2]), "0.1"),
 "median_real_value_level_payment_after_20y_pct": rnd(statistics.median([100/P for _, P in w20]), "0.1"),
 "worst_real_value_2pct_payment_after_20y_pct": rnd(worst[0], "0.1"),
 "worst_window_start_year": worst[1][0],
 "latest_window_real_value_2pct_payment_pct": rnd(100*g20/Plat, "0.1"),
 "latest_window_real_value_level_payment_pct": rnd(100/Plat, "0.1"),
}
json.dump(res, open(D/"result.json", "w"), indent=1)
print(json.dumps(res, indent=1)); print("SHA_OK", SHA_OK)
print("w20 first/last", w20[0][0], w20[-1][0], "w25 last", w25[-1][0])
print("kept20 starts", [s for s, P in w20 if g20 >= P])
print("worst", worst)
print("raw unrounded", 100*kept20/len(w20), statistics.median([100*(P**(1/20)-1) for _, P in w20]), statistics.median([v for v,_ in r2]), statistics.median([100/P for _,P in w20]), 100*g20/Plat, 100/Plat)
