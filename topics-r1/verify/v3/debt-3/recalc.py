import csv,json,os,statistics
from decimal import Decimal,ROUND_HALF_UP
d=os.path.dirname(os.path.abspath(__file__))
def load(n):
    out={}
    with open(os.path.join(d,'data',n+'.csv')) as f:
        for r in csv.DictReader(f):
            v=r[n].strip()
            if v and v!='.': out[r['observation_date']]=Decimal(v)
    return out
a=load('RIFLPBCIANM60NM'); b=load('RIFLPBCIANM72NM')
dates=sorted(x for x in a if x in b and '2015-08-01'<=x<='2026-05-01')
q=lambda x,e: x.quantize(Decimal(e),rounding=ROUND_HALF_UP)
prem=[q(b[x]-a[x],'0.01') for x in dates]
mean=sum(prem)/len(prem)
med=Decimal(str(statistics.median(prem)))
def pay(P,r,n):
    x=r/1200; return P*x/(1-(1+x)**-n)
def intr(r,n): return pay(35000,r,n)*n-35000
r60=float(a['2026-05-01']); r72=float(b['2026-05-01']); m=float(mean)
R=lambda v: int(q(Decimal(repr(v)),'1'))
res={
 'n_months':len(dates),'first_month':dates[0],'last_month':dates[-1],
 'mean_premium':float(q(mean,'0.01')),'median_premium':float(q(med,'0.001')),
 'max_premium':float(max(prem)),'min_premium':float(min(prem)),
 'months_72_cheaper':sum(p<0 for p in prem),'months_72_not_higher':sum(p<=0 for p in prem),
 'months_premium_ge_050':sum(p>=Decimal('0.50') for p in prem),
 'rate60_latest':r60,'rate72_latest':r72,
 'pay60_latest':float(q(Decimal(repr(pay(35000,7.14,60))),'0.01')),
 'pay72_latest':float(q(Decimal(repr(pay(35000,6.97,72))),'0.01')),
 'int60_latest':R(intr(7.14,60)),'int72_latest':R(intr(6.97,72)),
 'extra_interest_72_latest':R(intr(6.97,72)-intr(7.14,60)),
 'term_effect':R(intr(7.14,72)-intr(7.14,60)),
 'extra_interest_72_avgpremium':R(intr(7.14+m,72)-intr(7.14,60)),
 'rate_effect_avgpremium':R(intr(7.14+m,72)-intr(7.14,72)),
}
json.dump(res,open(os.path.join(d,'result.json'),'w'),indent=1)
print(json.dumps(res,indent=1)); print('mean unrounded',mean)
print([(x,str(p)) for x,p in zip(dates,prem)])
print('raw', intr(6.97,72), intr(7.14,60), intr(7.14,72), intr(7.14+m,72))
