import csv, json, statistics
from decimal import Decimal, ROUND_HALF_UP
def rd(x,q): return float(Decimal(repr(x)).quantize(Decimal(q),rounding=ROUND_HALF_UP))
def load(f):
    d={}
    for r in csv.DictReader(open(f)):
        k=list(r)[1]
        v=r[k].strip()
        d[r['observation_date']]=float(v) if v not in('','.') else None
    return d
tb=load('data/TB3MS.csv'); cpi=load('data/CPIAUCNS.csv')
months=sorted(tb)
def add(m,n):
    y,mo=int(m[:4]),int(m[5:7]); t=y*12+mo-1+n; return f"{t//12:04d}-{t%12+1:02d}-01"
starts=[];M={}
for i,s in enumerate(months):
    ws=[add(s,k) for k in range(240)]
    if all(tb.get(w) is not None for w in ws):
        p=1.0
        for w in ws: p*=1+tb[w]/1200
        starts.append(s); M[s]=p
vals=[M[s] for s in starts]
s90=[s for s in starts if s>='1990-01-01']
real=[s for s in starts if cpi.get(s) is not None and cpi.get(add(s,240)) is not None]
rv=[100*2.0*cpi[s]/cpi[add(s,240)] for s in real]
res={
 "starts":len(starts),"first_start":starts[0],"last_start":starts[-1],
 "share_tbills_above_double_pct":rd(100*sum(v>2.0 for v in vals)/len(vals),'0.1'),
 "median_tbill_multiple_20y":rd(statistics.median(vals),'0.001'),
 "min_tbill_multiple_20y":rd(min(vals),'0.001'),
 "max_tbill_multiple_20y":rd(max(vals),'0.001'),
 "share_tbills_above_double_starts_since_1990_pct":rd(100*sum(M[s]>2.0 for s in s90)/len(s90),'0.1'),
 "latest_tbill_multiple_20y":rd(M['2006-09-01'],'0.001'),
 "doubling_rate_pct_per_year":rd(100*(2**(1/20)-1),'0.01'),
 "real_windows":len(real),
 "share_double_beat_prices_pct":rd(100*sum(v>=100 for v in rv)/len(rv),'0.1'),
 "median_real_value_double_pct":rd(statistics.median(rv),'0.1'),
 "tb3ms_latest_pct":tb['2026-08-01'],
}
json.dump(res,open('result.json','w'),indent=1)
print(res, len(s90), statistics.median(vals), statistics.median(rv), [s for s in starts if add(s,240) not in cpi or cpi[add(s,240)] is None][:5])
