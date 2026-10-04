import csv, json
from decimal import Decimal as D, ROUND_HALF_UP
def rnd(x, q): return float(D(str(x)).quantize(D(q), rounding=ROUND_HALF_UP))
def r100(x): return int((D(str(x))/100).quantize(D('1'), rounding=ROUND_HALF_UP)*100)
def load(f):
    out={}
    for row in csv.DictReader(open(f)):
        v=list(row.values())[1].strip()
        if v and v!='.': out[row['observation_date']]=D(v)
    return out
cpi=load('data/CPIAUCNS.csv'); med=load('data/MEHOINUSA646N.csv')
c87=[v for d,v in cpi.items() if d.startswith('1987-')]
c25=[v for d,v in cpi.items() if d.startswith('2025-')]
assert len(c87)==12
a87=rnd(sum(c87)/len(c87),'0.001'); a25=rnd(sum(c25)/len(c25),'0.001')
k=rnd(D(str(a25))/D(str(a87)),'0.0001')
K=D(str(k))
m87=int(med['1987-01-01']); m25=int(med['2025-01-01'])
res={
 'cpi_1987_avg':a87,'cpi_2025_avg':a25,'cpi_2025_months':len(c25),
 'price_factor_1987_2025':k,
 'start_in_2025_dollars':r100(100000*K),
 'end_in_2025_dollars':r100(150000*K),
 'cap_in_2025_dollars':r100(25000*K),
 'start_real_value_pct_of_1987':rnd(100/K,'0.1'),
 'median_1987':m87,'median_2025':m25,
 'start_over_median_1987':rnd(D(100000)/m87,'0.01'),
 'start_over_median_2025':rnd(D(100000)/m25,'0.01'),
 'end_over_median_2025':rnd(D(150000)/m25,'0.01'),
 'start_if_tracked_median_2025':r100(D(100000)*m25/m87),
 'income_in_1987_dollars':r100(D(130000)/K),
 'allowance_at_income':max(0,25000-0.5*max(0,130000-100000)),
 'allowance_at_income_if_cpi_indexed':r100(max(D(0),25000*K-D('0.5')*max(D(0),130000-100000*K))),
}
json.dump(res,open('result.json','w'),indent=1)
# sensitivity: unrounded k
ku=(sum(c25)/len(c25))/(sum(c87)/len(c87))
print(json.dumps(res,indent=1)); print('unrounded k',ku, 'start',r100(100000*ku),'end',r100(150000*ku),'cap',r100(25000*ku),'pct',rnd(100/ku,'0.1'),'inc87',r100(130000/ku))
