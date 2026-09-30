import csv, json, math, statistics
from decimal import Decimal, ROUND_HALF_UP
def rd(x, nd):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP))
def qkey(d):
    y, m = int(d[:4]), int(d[5:7]); return (y, (m-1)//3+1)
hpi = []
for r in csv.DictReader(open("data/USSTHPI.csv")):
    v = r["USSTHPI"].strip()
    if v and v != ".": hpi.append((qkey(r["observation_date"]), float(v)))
hpi.sort(); qs = [k for k,_ in hpi]; H = [v for _,v in hpi]
rates = {}
for r in csv.DictReader(open("data/MORTGAGE30US.csv")):
    v = r["MORTGAGE30US"].strip()
    if v and v != ".": rates.setdefault(qkey(r["observation_date"]), []).append(float(v))
N = len(H)
def lim_simple(m): return 0.80
def lim_seas(m): return None if m < 24 else (0.75 if m < 60 else 0.80)
def run(limf):
    out = []
    for q in range(N):
        if qs[q] < (1975,1): continue
        rate = sum(rates[qs[q]])/len(rates[qs[q]]); i = rate/1200
        P = 95*i/(1-(1+i)**-360)
        b = 95.0; bal = [b]; sched = None
        for m in range(1, 361):
            b = b*(1+i) - P; bal.append(b)
            if sched is None and b <= 80: sched = m
        if sched is None or q + math.ceil(sched/3) >= N: continue
        val = None
        for m in range(3, 361, 3):
            k = m//3
            if q+k >= N: break
            L = limf(m)
            if L is None: continue
            if bal[m] / (100*H[q+k]/H[q]) <= L: val = m; break
        out.append((qs[q], sched, val))
    return out
def med_val(c): return statistics.median([v/12 if v is not None else math.inf for _,_,v in c])
def share3(c): return 100*sum(1 for _,s,v in c if v is not None and s/12 - v/12 >= 3)/len(c)
S = run(lim_simple); T = run(lim_seas)
res = {
 "simple_n_cohorts": len(S),
 "simple_median_years_schedule": rd(statistics.median([s/12 for _,s,_ in S]),2),
 "simple_median_years_value": rd(med_val(S),2),
 "simple_share_value_faster_3y": rd(share3(S),1),
 "seasoned_median_years_value": rd(med_val(T),2),
 "seasoned_share_value_faster_3y": rd(share3(T),1),
 "seasoned_share_value_not_faster": rd(100*sum(1 for _,s,v in T if v is None or v >= s)/len(T),1),
}
import sys
if "-v" in sys.argv:
    print(S[0][0], S[-1][0], [(c,s,v) for c,s,v in T if v is None or v>=s], file=sys.stderr)
print(json.dumps(res))
