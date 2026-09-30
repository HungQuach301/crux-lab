import csv, json, statistics
cpi = {}
with open("data/CPIAUCNS.csv") as f:
    for row in csv.DictReader(f):
        v = row["CPIAUCNS"].strip()
        if v and v != ".":
            y, m, _ = row["observation_date"].split("-")
            cpi[int(y)*12 + int(m)-1] = float(v)
start = 1947*12 + 0
last = 2026*12 + 7  # 2026-08

def losses(n):
    out = []
    s = start
    while s + n <= last:
        if s in cpi and (s+n) in cpi:
            out.append((s, 1 - cpi[s]/cpi[s+n]))
        s += 1
    return out

l25 = losses(300); l30 = losses(360)
v25 = [l for _, l in l25]; v30 = [l for _, l in l30]
smin = min(l25, key=lambda t: t[1])[0]
res = {
    "windows_25y": len(l25),
    "min_loss_25y_pct": min(v25)*100,
    "min_loss_25y_start_yyyymm": (smin//12)*100 + smin%12 + 1,
    "median_loss_25y_pct": statistics.median(v25)*100,
    "max_loss_25y_pct": max(v25)*100,
    "share_25y_over_half_pct": sum(1 for l in v25 if l > 0.5)/len(v25)*100,
    "min_loss_30y_pct": min(v30)*100,
    "median_loss_30y_pct": statistics.median(v30)*100,
}
print(json.dumps(res, indent=1))
