import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
# Uniform Lifetime Table, 26 CFR 1.401(a)(9)-9(c) (as quoted in input.json provisions)
ULT = {73:26.5,74:25.5,75:24.6,76:23.7,77:22.9,78:22.0,79:21.1,80:20.2,81:19.4,82:18.5,
       83:17.7,84:16.8,85:16.0,86:15.2,87:14.4,88:13.7,89:12.9,90:12.2,91:11.5,92:10.8,
       93:10.1,94:9.5,95:8.9,96:8.4,97:7.8,98:7.3,99:6.8,100:6.4}
rows = []
with open(os.path.join(HERE, "data", "DFII20.csv")) as f:
    for r in csv.DictReader(f):
        v = r["DFII20"].strip()
        if v in ("", "."): continue
        rows.append((r["observation_date"], float(v)))
now_date, now = rows[-1]
low = min(v for _, v in rows)

def sim(r):
    B, W = {73: 1.0}, {}
    for a in range(73, 101):
        W[a] = B[a] / ULT[a]
        B[a+1] = (B[a] - W[a]) * (1 + r/100)
    return B, W

Bn, Wn = sim(now); Bl, Wl = sim(low)
peak = max(range(73, 101), key=lambda a: Wn[a])
out = {
 "real_yield_now_pct": now,
 "real_yield_low_pct": low,
 "first_withdrawal_pct_of_start": Wn[73]*100,
 "now_balance_at_90_pct_of_start": Bn[90]*100,
 "now_withdrawal_at_90_pct_of_start": Wn[90]*100,
 "now_peak_withdrawal_age": peak,
 "now_peak_withdrawal_pct_of_start": Wn[peak]*100,
 "low_balance_at_90_pct_of_start": Bl[90]*100,
 "low_withdrawal_at_90_pct_of_start": Wl[90]*100,
 "low_years_withdrawal_rises_after_73": sum(1 for a in range(74, 101) if Wl[a] > Wl[a-1]),
}
print(json.dumps(out, indent=1))
