import csv, json, os
from decimal import Decimal, ROUND_HALF_UP
D=os.path.dirname(os.path.abspath(__file__))
R=3000.0
def load(name, ffill=False):
    out={}; last=None
    for row in csv.DictReader(open(os.path.join(D,'data',name+'.csv'))):
        y,m,_=row['observation_date'].split('-'); v=row[name].strip()
        if v and v!='.': last=float(v); out[(int(y),int(m))]=last
        elif ffill and last is not None: out[(int(y),int(m))]=last
    return out
def months(Y):
    # k=1..11 -> Feb..Dec of Y; k=12 -> Jan Y+1; k=13 (balance 12/12) -> Feb Y+1
    return [((Y,m),min(m-1,12)) for m in range(2,13)]+[((Y+1,1),12),((Y+1,2),12)]
def cost(Y,ser,ffill_from=None):
    tot=0.0
    for (ym,k) in months(Y):
        if ffill_from is not None:
            keys=[x for x in ffill_from if x<=ym]; r=ffill_from[max(keys)]
        else: r=ser[ym]
        tot+=R*k/12*r/100/12
    return tot
def rc(x): return float(Decimal(repr(x)).quantize(Decimal('0.01'),ROUND_HALF_UP))
tb=load('TB3MS'); sn=load('SNDR'); cc=load('TERMCBCCALLNS')
years=range(2000,2026)
tbv={Y:cost(Y,tb) for Y in years}
ccv={Y:cost(Y,None,ffill_from=cc) for Y in years}
res={
 'balance_months_per_dollar': sum(k for _,k in months(2025))/12,
 'tbill_2025_usd': rc(tbv[2025]),
 'savings_avg_2025_usd': rc(cost(2025,sn)),
 'card_2025_usd': rc(ccv[2025]),
 'tbill_mean_2000_2025_usd': rc(sum(tbv.values())/26),
 'tbill_max_usd': rc(max(tbv.values())),
 'tbill_max_year': max(tbv,key=tbv.get),
 'tbill_min_usd': rc(min(tbv.values())),
 'tbill_min_year': min(tbv,key=tbv.get),
 'tbill_years_under_10usd': sum(1 for v in tbv.values() if v<10),
 'card_mean_2000_2025_usd': rc(sum(ccv.values())/26),
 'card_min_usd': rc(min(ccv.values())),
 'card_max_usd': rc(max(ccv.values())),
}
json.dump(res,open(os.path.join(D,'result.json'),'w'),indent=1)
print(json.dumps(res,indent=1))
print({Y:round(v,4) for Y,v in tbv.items()}); print({Y:round(v,4) for Y,v in ccv.items()})
