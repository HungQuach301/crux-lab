import csv, json, statistics
from decimal import Decimal, ROUND_HALF_UP
def load(f):
    out = {}
    for r in list(csv.reader(open(f)))[1:]:
        if len(r) > 1 and r[1].strip() not in ('', '.'):
            out[r[0]] = float(r[1])
    return out
A = load('data/CUUR0000SETG01.csv'); L = load('data/CUUR0000SEHB.csv'); T = load('data/TB3MS.csv')
def ym(d): y, m = int(d[:4]), int(d[5:7]); return y*12 + m-1
def dt(k): return f"{k//12:04d}-{k%12+1:02d}-01"
Ak = {ym(k): v for k, v in A.items()}; Lk = {ym(k): v for k, v in L.items()}; Tk = {ym(k): v for k, v in T.items()}
def r(x, nd):
    q = Decimal(1).scaleb(-nd)
    return float(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))
def G(s, n):
    g = 1.0
    for k in range(s, s+n):
        g *= 1 + Tk[k]/1200   # KeyError if missing T-bill month
    return g
def P(kind, s, n):
    if kind == 'air': return Ak[s+n]/Ak[s]
    if kind == 'lodging': return Lk[s+n]/Lk[s]
    return 0.5*Ak[s+n]/Ak[s] + 0.5*Lk[s+n]/Lk[s]
def ok(kind, s, n):
    ser = {'air': [Ak], 'lodging': [Lk], 'trip': [Ak, Lk]}[kind]
    return all(s in d and s+n in d for d in ser) and all(k in Tk for k in range(s, s+n))
def windows(kind, n):
    keys = sorted(set(Ak) | set(Lk))
    return [(s, G(s, n)/P(kind, s, n)) for s in keys if ok(kind, s, n)]
res = {}
for kind in ['air', 'lodging', 'trip']:
    w = windows(kind, 120)
    res[f'{kind}_starts_10y'] = len(w)
    res[f'{kind}_first_start_10y'] = dt(w[0][0])
    assert dt(w[-1][0]) == '2016-08-01', dt(w[-1][0])
    res[f'{kind}_share_waiting_cost_more_10y_pct'] = r(100*sum(c < 1 for _, c in w)/len(w), 1)
    res[f'{kind}_median_coverage_10y_pct'] = r(statistics.median(100*c for _, c in w), 1)
    s = ym('2016-08-01'); res[f'{kind}_latest_coverage_10y_pct'] = r(100*G(s,120)/P(kind,s,120), 1)
w5 = windows('trip', 60)
res['trip_starts_5y'] = len(w5)
res['trip_share_waiting_cost_more_5y_pct'] = r(100*sum(c < 1 for _, c in w5)/len(w5), 1)
a, b = ym('1997-12-01'), ym('2026-08-01'); assert b-a == 344
res['air_price_growth_annual_pct'] = r(100*((Ak[b]/Ak[a])**(12/344)-1), 2)
res['lodging_price_growth_annual_pct'] = r(100*((Lk[b]/Lk[a])**(12/344)-1), 2)
res['tbill_growth_annual_pct'] = r(100*(G(a, 344)**(12/344)-1), 2)
# diagnostics
print('air first-start monthly-continuous from', dt(min(k for k in Ak if all(j in Ak for j in range(k, max(Ak)+1)))))
print('trip5 first', dt(w5[0][0]), 'last', dt(w5[-1][0]))
json.dump(res, open('result.json', 'w'), indent=1)
print(json.dumps(res, indent=1))
