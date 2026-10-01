import csv, json, os, statistics
from decimal import Decimal, ROUND_HALF_UP
d=os.path.dirname(os.path.abspath(__file__))
def load(f):
    out={}
    for row in csv.DictReader(open(os.path.join(d,'data',f))):
        k=list(row.keys())
        try: out[row[k[0]][:7]]=float(row[k[1]])
        except ValueError: pass
    return out
tb=load('TB3MS.csv'); cpi=load('CPIAUCNS.csv')
def r(x,q): return float(Decimal(repr(x)).quantize(Decimal(q),rounding=ROUND_HALF_UP))
def G(y):
    g=1.0
    for m in range(1,13): g*=1+tb[f"{y}-{m:02d}"]/100/12
    return g
P=7500.0
starts=list(range(1934,2017))
roth={};tax={}
for Y in starts:
    a=b=P
    for y in range(Y,Y+10):
        g=G(y); a*=g; b*=1+0.78*(g-1)
    f=cpi[f"{Y}-01"]/cpi[f"{Y+10}-01"]
    roth[Y]=a*f; tax[Y]=b*f
diff={Y:roth[Y]-tax[Y] for Y in starts}
n=len(starts)
rl=sum(roth[Y]<P for Y in starts); tl=sum(tax[Y]<P for Y in starts)
mx=max(starts,key=lambda Y:diff[Y])
yrs=range(1934,2026)
infl={y:cpi[f"{y}-12"]/cpi[f"{y-1}-12"]-1 for y in yrs}
res={
 "windows":n,
 "roth_real_loss_windows":rl,
 "taxable_real_loss_windows":tl,
 "roth_real_loss_share_pct":r(rl/n*100,'0.1'),
 "taxable_real_loss_share_pct":r(tl/n*100,'0.1'),
 "median_real_end_roth_usd":r(statistics.median(roth.values()),'0.01'),
 "median_real_end_taxable_usd":r(statistics.median(tax.values()),'0.01'),
 "median_diff_usd":r(statistics.median(diff.values()),'0.01'),
 "max_diff_usd":r(diff[mx],'0.01'),
 "max_diff_start":mx,
 "latest_start":max(Y for Y in starts if f"{Y+10}-01" in cpi and f"{Y+9}-12" in tb),
 "latest_real_end_roth_usd":r(roth[2016],'0.01'),
 "latest_real_end_taxable_usd":r(tax[2016],'0.01'),
 "calendar_years":len(yrs),
 "years_beat_inflation_untaxed":sum(G(y)-1>infl[y] for y in yrs),
 "years_beat_inflation_after_tax":sum(0.78*(G(y)-1)>infl[y] for y in yrs),
}
json.dump(res,open(os.path.join(d,'result.json'),'w'),indent=1)
print(json.dumps(res,indent=1))
# sensitivity
import sys
print('median-window roth/tax years:',sorted(starts,key=lambda Y:roth[Y])[41],sorted(starts,key=lambda Y:tax[Y])[41])
print('near-ties:',[(y,G(y)-1,infl[y]) for y in yrs if abs(G(y)-1-infl[y])<1e-4 or abs(0.78*(G(y)-1)-infl[y])<1e-4])
print('near 7500:',[(Y,roth[Y],tax[Y]) for Y in starts if abs(roth[Y]-P)<1 or abs(tax[Y]-P)<1])
