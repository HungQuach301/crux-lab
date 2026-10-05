import csv, json, statistics, datetime as dt
from decimal import Decimal, ROUND_HALF_UP
D='/home/user/crux-lab/topics-r2/verify/v3/retire-2/'
def load(f):
    out={}
    for r in csv.DictReader(open(D+f)):
        k=list(r.keys())
        v=r[k[1]].strip()
        if v in ('','.'): continue
        out[dt.date.fromisoformat(r[k[0]])]=float(v)
    return out
H=load('data/USSTHPI.csv'); T=load('data/TB3MS.csv')
def rnd(x,q): return float(Decimal(repr(x)).quantize(Decimal(q),rounding=ROUND_HALF_UP))
def addm(d,n):
    m=d.year*12+d.month-1+n; return dt.date(m//12,m%12+1,1)
def G(s,n):
    g=1.0
    for i in range(n): g*=1+T[addm(s,i)]/1200
    return g
def windows(n):
    return [(s,G(s,n)/(H[addm(s,n)]/H[s])) for s in sorted(H) if addm(s,n) in H]
w10=windows(120); w20=windows(240)
C10=[c for _,c in w10]
w90=[(s,c) for s,c in w10 if s>=dt.date(1990,1,1)]
res={
 'starts_10y':len(w10),
 'first_start_10y':w10[0][0].isoformat(),
 'last_start_10y':w10[-1][0].isoformat(),
 'share_gift_buys_less_10y_pct':rnd(100*sum(c<1 for c in C10)/len(w10),'0.1'),
 'median_coverage_10y_pct':rnd(statistics.median([100*c for c in C10]),'0.1'),
 'min_coverage_10y_pct':rnd(min(100*c for c in C10),'0.1'),
 'max_coverage_10y_pct':rnd(max(100*c for c in C10),'0.1'),
 'starts_since_1990_10y':len(w90),
 'share_gift_buys_less_10y_since_1990_pct':rnd(100*sum(c<1 for _,c in w90)/len(w90),'0.1'),
 'latest_coverage_10y_pct':rnd(100*dict(w10)[dt.date(2016,4,1)],'0.1'),
 'starts_20y':len(w20),
 'share_gift_buys_less_20y_pct':rnd(100*sum(c<1 for _,c in w20)/len(w20),'0.1'),
 'latest_coverage_20y_pct':rnd(100*dict(w20)[dt.date(2006,4,1)],'0.1'),
 'home_price_growth_annual_pct':rnd(100*((H[dt.date(2026,4,1)]/H[dt.date(1975,1,1)])**(4/205)-1),'0.01'),
 'tbill_growth_annual_pct':rnd(100*(G(dt.date(1975,1,1),615)**(4/205)-1),'0.01'),
}
assert addm(dt.date(1975,1,1),614)==dt.date(2026,3,1)
json.dump(res,open(D+'result.json','w'),indent=1)
print(json.dumps(res,indent=1))
print('w20 range',w20[0][0],w20[-1][0], 'n90',len(w90))
# check near-1 and rounding-edge values
print([ (s,c) for s,c in w10+w20 if abs(c-1)<1e-4])
