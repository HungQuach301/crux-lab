import csv, json, statistics
from decimal import Decimal, ROUND_HALF_UP
rows=[]
for r in csv.DictReader(open('data/TERMCBCCINTNS.csv')):
    v=r['TERMCBCCINTNS'].strip()
    if v and v!='.': rows.append((r['observation_date'][:7], float(v)))
def interest(apr,n):
    i=apr/100/12
    p=1000*i/(1-(1+i)**-n)
    return n*p-1000
def months(apr,tax):
    n=1
    while interest(apr,n)<=tax: n+=1
    return n
def c(x): return float(Decimal(repr(x)).quantize(Decimal('0.01'),ROUND_HALF_UP))
tax12=0.12*1000; tax22=0.22*1000
last=rows[-1]; mn=min(rows,key=lambda r:r[1]); mx=max(rows,key=lambda r:r[1])
m12=[months(a,tax12) for _,a in rows]; m22=[months(a,tax22) for _,a in rows]
res={
 "observations":len(rows),"first_obs":rows[0][0],"last_obs":last[0],"apr_last_pct":last[1],
 "tax_12_usd":round(tax12,2),"tax_22_usd":round(tax22,2),
 "months_12_last":months(last[1],tax12),"months_22_last":months(last[1],tax22),
 "interest_12mo_last_usd":c(interest(last[1],12)),"interest_24mo_last_usd":c(interest(last[1],24)),
 "interest_6mo_last_usd":c(interest(last[1],6)),
 "apr_min_pct":mn[1],"apr_min_obs":mn[0],"months_12_at_min":months(mn[1],tax12),
 "apr_max_pct":mx[1],"apr_max_obs":mx[0],"months_12_at_max":months(mx[1],tax12),
 "months_12_median":statistics.median(m12),"months_22_median":statistics.median(m22),
 "months_12_min":min(m12),"months_12_max":max(m12),"months_22_min":min(m22),"months_22_max":max(m22)}
json.dump(res,open('result.json','w'),indent=1)
print(json.dumps(res,indent=1))
print('ties min',[r for r in rows if r[1]==mn[1]],'ties max',[r for r in rows if r[1]==mx[1]])
print('raw 12',interest(last[1],12),'6',interest(last[1],6),'24',interest(last[1],24))
print('months set', sorted(set(rows[k][0][5:] for k in range(len(rows)))))
