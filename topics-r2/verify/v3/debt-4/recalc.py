import csv,json,statistics
from decimal import Decimal,ROUND_HALF_UP
def rd(v,q): return float(Decimal(repr(v)).quantize(Decimal(q),rounding=ROUND_HALF_UP))
def load(f):
    d={}
    for row in csv.DictReader(open(f)):
        k,v=list(row.values())
        if v not in ('','.'): d[k[:7]]=float(v)
    return d
rate=load('data/RIFLPBCIANM60NM.csv'); cpi=load('data/CUUR0000SETA01.csv')
def pay(P,r):
    x=r/1200; return P*x/(1-(1+x)**-60)
pairs=[]
for a in sorted(rate):
    y,m=a.split('-'); b=f"{int(y)+1}-{m}"
    if b in rate and a in cpi and b in cpi:
        now=pay(35000,rate[a]); wait=pay(35000*cpi[b]/cpi[a],rate[b])
        pairs.append(dict(a=a,dr=rate[b]-rate[a],dp=wait-now,pc=(cpi[b]/cpi[a]-1)*100))
fell=[p for p in pairs if p['dr']<0]
lm=max(rate)
res={
 "n_pairs":len(pairs),
 "first_pair":pairs[0]['a'],
 "last_pair":pairs[-1]['a'],
 "share_payment_lower":rd(sum(p['dp']<0 for p in pairs)/len(pairs),'0.001'),
 "median_payment_change":rd(statistics.median(p['dp'] for p in pairs),'0.01'),
 "n_rate_fell":len(fell),
 "share_lower_when_rate_fell":rd(sum(p['dp']<0 for p in fell)/len(fell),'0.001'),
 "largest_rate_drop":rd(min(p['dr'] for p in pairs),'0.01'),
 "largest_rate_rise":rd(max(p['dr'] for p in pairs),'0.01'),
 "best_payment_change":rd(min(p['dp'] for p in pairs),'0.01'),
 "median_price_change":rd(statistics.median(p['pc'] for p in pairs),'0.01'),
 "rate_latest_month":lm,
 "rate_latest":rate['2026-05'],
 "pay_latest":rd(pay(35000,rate['2026-05']),'0.01'),
 "one_point_effect":rd(pay(35000,7.14)-pay(35000,6.14),'0.01'),
}
json.dump(res,open('result.json','w'),indent=1)
print(json.dumps(res,indent=1))
