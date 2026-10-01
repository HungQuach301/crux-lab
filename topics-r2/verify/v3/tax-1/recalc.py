import csv, json, statistics
from decimal import Decimal, ROUND_HALF_UP
def load(p):
    d={}
    for r in csv.DictReader(open(p)):
        k=list(r.keys())[1]; v=r[k].strip()
        if v in ('','.'): continue
        y,mo,_=r['observation_date'].split('-'); d[(int(y),int(mo))]=float(v)
    return d
F=load('data/FII10.csv'); C=load('data/CPIAUCNS.csv')
def add(m,n):
    t=m[0]*12+m[1]-1+n; return (t//12,t%12+1)
def lab(m): return f"{m[0]:04d}-{m[1]:02d}"
def rnd(x,q): return float(Decimal(repr(x)).quantize(Decimal(q),ROUND_HALF_UP))
ref=lambda x: C.get(add(x,-3))
res=[]; skipped=[]
m=(2003,1)
while m<=(2016,11):
    y=F[m]/100
    refs=[ref(add(m,12*j)) for j in range(11)]
    if any(r is None for r in refs): skipped.append(lab(m)); m=add(m,1); continue
    Wt=Wi=1.0; P=1.0
    for k in range(10):
        f=refs[k+1]/refs[k]; g=(1+y)*f
        Wt*=1+0.76*(g-1); Wi*=g; P*=f
    rt=Wt/P; ri=Wi/P
    res.append(dict(m=lab(m),y=y,rt=rt,ri=ri,at=rt**0.1-1,ai=ri**0.1-1))
    m=add(m,1)
N=len(res)
gaps=[(r['ai']-r['at'])*100 for r in res]
worst=min(res,key=lambda r:r['at']); best=max(res,key=lambda r:r['at'])
neg_t=sum(r['at']<0 for r in res)
out={'windows':N,'windows_skipped_missing_cpi':len(skipped),
 'first_purchase':res[0]['m'],'last_purchase':res[-1]['m'],
 'taxable_negative_real_count':neg_t,
 'taxable_negative_real_share_pct':rnd(neg_t/N*100,'0.1'),
 'ira_negative_real_count':sum(r['ai']<0 for r in res),
 'median_gap_pctpts':rnd(statistics.median(gaps),'0.01'),
 'max_gap_pctpts':rnd(max(gaps),'0.01'),'min_gap_pctpts':rnd(min(gaps),'0.01'),
 'worst_taxable_real_pct':rnd(worst['at']*100,'0.01'),'worst_purchase_month':worst['m'],
 'worst_ira_real_pct':rnd(worst['ai']*100,'0.01'),
 'best_taxable_real_pct':rnd(best['at']*100,'0.01'),'best_purchase_month':best['m'],
 'median_end_real_usd_taxable':int(rnd(10000*statistics.median(r['rt'] for r in res),'1')),
 'median_end_real_usd_ira':int(rnd(10000*statistics.median(r['ri'] for r in res),'1'))}
a22=C[(2022,10)]/C[(2021,10)]-1
c22=max(F[(2022,1)],0.125)/100
out['inflation_accrual_2022_pct']=rnd(a22*100,'0.01')
out['tax_2022_usd']=rnd(0.24*10000*(c22+a22),'0.01')
out['coupon_cash_2022_usd']=rnd(10000*c22,'0.01')
ph=0;yrs=0
for Y in range(2003,2025):
    c=max(F[(Y,1)],0.125)/100; a=C[(Y,10)]/C[(Y-1,10)]-1; yrs+=1
    if 0.24*10000*(c+a)>10000*c: ph+=1
out['phantom_years']=ph; out['phantom_years_total']=yrs
# diagnostics
print('skipped',skipped,'ira==y check',max(abs(r['ai']-r['y']) for r in res))
print('a22 raw',a22,'tax raw',0.24*10000*(c22+a22))
json.dump(out,open('result.json','w'),indent=1); print(json.dumps(out,indent=1))
