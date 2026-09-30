import csv, json
from decimal import Decimal, ROUND_HALF_UP

def load(fn, sid):
    out = {}
    with open(fn) as f:
        for row in csv.DictReader(f):
            v = row[sid].strip()
            try:
                out[row['observation_date']] = Decimal(v)
            except Exception:
                pass  # '.' or blank = missing
    return out

va = load('data/OBMMIVA30YF.csv', 'OBMMIVA30YF')
cv = load('data/OBMMIC30YFLVLE80FGE740.csv', 'OBMMIC30YFLVLE80FGE740')
dates = sorted(d for d in set(va) & set(cv) if '2017-01-03' <= d <= '2026-09-29')

def rnd(x, q):
    return float(Decimal(str(x)).quantize(Decimal(q), rounding=ROUND_HALF_UP))

def below(ds):  # compare in thousandths (integers)
    return sum(1 for d in ds if int(va[d]*1000) < int(cv[d]*1000))

res = {}
res['n_days'] = len(dates)
res['share_days_va_below_best_conv'] = rnd(Decimal(below(dates))*100/len(dates), '0.1')
w = [d for d in dates if d >= '2023-04-07']
res['n_days_since_20230407'] = len(w)
res['share_days_va_below_since_20230407'] = rnd(Decimal(below(w))*100/len(w), '0.1')
rv = sum(va[d] for d in w)/len(w)
rc = sum(cv[d] for d in w)/len(w)
gap = sum(cv[d]-va[d] for d in w)/len(w)
res['mean_va_since_20230407'] = rnd(rv, '0.001')
res['mean_conv_since_20230407'] = rnd(rc, '0.001')
res['mean_gap_since_20230407'] = rnd(gap, '0.001')

rv, rc = float(rv), float(rc)
def pay(r):
    i = r/1200
    return 100000*i/(1-(1+i)**-360)
def bal(r, m):
    i = r/1200; p = pay(r); b = 100000.0
    for _ in range(m):
        b = b*(1+i) - p
    return b
FEE = 0.0125*100000
ds = pay(rc) - pay(rv)
res['monthly_saving_per_100k'] = rnd(ds, '0.01')
res['breakeven_months_payment_only'] = rnd(FEE/ds, '0.1')
be = None
for m in range(1, 361):
    if m*ds + (bal(rc, m) - bal(rv, m)) >= FEE:
        be = m; break
res['breakeven_months_net'] = be
res['net_gain_10y_per_100k'] = int(rnd(120*ds + bal(rc,120) - bal(rv,120) - FEE, '1'))
print(json.dumps(res, indent=1))
