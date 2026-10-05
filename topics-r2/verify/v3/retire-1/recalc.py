import csv, json, os, statistics
from decimal import Decimal, ROUND_HALF_UP
d=os.path.dirname(os.path.abspath(__file__))
def load(n):
    out={}
    for r in csv.DictReader(open(os.path.join(d,'data',n+'.csv'))):
        v=r[n].strip()
        if v not in ('','.'): out[r['observation_date']]=float(v)
    return out
F=load('CUUR0000SEGD03'); TB=load('TB3MS'); CPI=load('CPIAUCNS')
allF=[r['observation_date'] for r in csv.DictReader(open(os.path.join(d,'data','CUUR0000SEGD03.csv')))]
def add(m,k):
    y,mo=int(m[:4]),int(m[5:7]); t=y*12+mo-1+k
    return f"{t//12:04d}-{t%12+1:02d}-01"
def rnd(x,p): return float(Decimal(repr(x)).quantize(Decimal(p),rounding=ROUND_HALF_UP))
def G(s,n):
    g=1.0
    for k in range(n): g*=1+TB[add(s,k)]/1200
    return g
def C(s,n): return G(s,n)/(F[add(s,n)]/F[s])
res={}; win={}
for yrs,n in ((5,60),(10,120),(15,180)):
    starts=[s for s in allF if s in F and add(s,n) in F]
    cs=[C(s,n) for s in starts]; win[yrs]=(starts,cs)
    res[f'starts_{yrs}y']=len(starts)
    res[f'share_savings_fell_short_{yrs}y_pct']=rnd(100*sum(c<1 for c in cs)/len(cs),'0.1')
s10,c10=win[10]
res['first_start_10y']=s10[0]; res['last_start_10y']=s10[-1]
res['median_coverage_10y_pct']=rnd(statistics.median([100*c for c in c10]),'0.1')
res['min_coverage_10y_pct']=rnd(min(100*c for c in c10),'0.1')
res['max_coverage_10y_pct']=rnd(max(100*c for c in c10),'0.1')
res['latest_coverage_10y_pct']=rnd(100*C('2016-08-01',120),'0.1')
res['funeral_price_growth_annual_pct']=rnd(100*((F['2026-08-01']/F['1997-12-01'])**(12/344)-1),'0.01')
res['all_items_price_growth_annual_pct']=rnd(100*((CPI['2026-08-01']/CPI['1997-12-01'])**(12/344)-1),'0.01')
res['tbill_growth_annual_pct']=rnd(100*(G('1997-12-01',344)**(12/344)-1),'0.01')
res['tb3ms_latest_pct']=TB['2026-08-01']
order=['starts_10y','first_start_10y','last_start_10y','share_savings_fell_short_10y_pct','median_coverage_10y_pct','min_coverage_10y_pct','max_coverage_10y_pct','latest_coverage_10y_pct','starts_5y','share_savings_fell_short_5y_pct','starts_15y','share_savings_fell_short_15y_pct','funeral_price_growth_annual_pct','all_items_price_growth_annual_pct','tbill_growth_annual_pct','tb3ms_latest_pct']
json.dump({k:res[k] for k in order},open(os.path.join(d,'result.json'),'w'),indent=1)
print(json.dumps({k:res[k] for k in order},indent=1))
# diagnostics: alternative including missing-end handling, raw values
print('unrounded median', statistics.median([100*c for c in c10]), 'n10 if missing F counted as start-excluded only:', len(s10))
print('5y raw', 100*sum(c<1 for c in win[5][1])/len(win[5][1]), '15y n', len(win[15][0]), 'first/last 5y', win[5][0][0], win[5][0][-1])
