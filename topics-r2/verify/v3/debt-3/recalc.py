import csv, json, statistics
from decimal import Decimal, ROUND_HALF_UP
rows=[(d[:7],Decimal(v)) for d,v in csv.reader(open('data/AHETPI.csv')) if d!='observation_date' and v not in ('.','')]
dates=[r[0] for r in rows]; W=[r[1] for r in rows]; n=len(W)
# check contiguous months
for i in range(1,n):
    y,m=map(int,dates[i-1].split('-')); y2,m2=map(int,dates[i].split('-'))
    assert (y2*12+m2)-(y*12+m)==1, dates[i]
K={}
for t in range(n):
    tgt=Decimal('1.25')*W[t]
    for k in range(0,n-t):
        if W[t+k]>=tgt: K[t]=k; break
ts=sorted(K); ks=[K[t] for t in ts]
def r(x,q): return float(Decimal(str(x)).quantize(Decimal(q),rounding=ROUND_HALF_UP))
def med(v):
    m=statistics.median(v); return int(m) if m==int(m) else float(m)
t90=[t for t in ts if dates[t]>='1990-01']; k90=[K[t] for t in t90]
mn=min(ks); mstart=next(t for t in ts if K[t]==mn)
sh=[Decimal(35)*W[t]/W[t+60] for t in range(n) if dates[t]>='1990-01' and t+60<n]
res={
 'n_starts':len(ts),'first_start':dates[ts[0]],'last_start':dates[ts[-1]],
 'median_months':med(ks),'min_months':mn,'min_start':dates[mstart],'max_months':max(ks),
 'share_le48':r(Decimal(sum(k<=48 for k in ks))/len(ks),'0.001'),
 'n_starts_1990':len(t90),'median_months_1990':med(k90),'min_months_1990':min(k90),
 'share_le48_1990':r(Decimal(sum(k<=48 for k in k90))/len(k90),'0.001'),
 'median_share_after60_1990':r(statistics.median(sh),'0.1'),'n_share5_1990':len(sh)}
json.dump(res,open('result.json','w'),indent=1); print(res)
print('raw median share',statistics.median(sh), 'n obs',n, dates[0],dates[-1])
