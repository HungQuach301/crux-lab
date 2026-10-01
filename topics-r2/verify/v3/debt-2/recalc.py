import csv, json, statistics
from collections import defaultdict

def load(fn):
    out = []
    with open(fn) as f:
        r = csv.reader(f); next(r)
        for d, v in r:
            if v.strip() in ('', '.'): continue
            out.append((d, float(v)))
    return out

hpi = {d[:7]: v for d, v in load('data/HPIPONM226N.csv')}
months = sorted(hpi)
idx = {m: i for i, m in enumerate(months)}
wk = defaultdict(list)
for d, v in load('data/MORTGAGE30US.csv'):
    wk[d[:7]].append(v)
rate = {m: sum(v)/len(v) for m, v in wk.items()}

def bal(r, k):
    x = r/1200; p = 0.9*x/(1-(1+x)**-360)
    g = (1+x)**k
    return 0.9*g - p*(g-1)/x

def sched(r, t):
    for k in range(361):
        if bal(r, k) <= t: return k
    return None

def ltv(m, k):
    i = idx[m]
    return bal(rate[m], k) / (hpi[months[i+k]]/hpi[m])

def first_k(m, t=0.80):
    i = idx[m]
    for k in range(0, len(months)-i):
        if ltv(m, k) <= t: return k
    return None

res = {}
latest = max(rate)
res['rate_month_latest'] = latest
rl = rate[latest]
from decimal import Decimal, ROUND_HALF_UP
# exact decimal mean of weekly values, rounded half-up (float round() gives 6.862 due to binary repr / half-even)
rl_dec = sum(Decimal(str(v)) for v in wk[latest]) / len(wk[latest])
res['rate_latest'] = float(rl_dec.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
res['_rate_latest_exact'] = str(rl_dec)
res['sched80_months_latest'] = sched(rl, 0.80)
res['sched78_months_latest'] = sched(rl, 0.78)

A = [m for m in months if '1991-01' <= m <= '2024-07']
res['nA'] = len(A); res['firstA'] = A[0]; res['lastA'] = A[-1]
l24 = [ltv(m, 24) for m in A]
res['shareA_ltv24_le75'] = round(sum(v <= 0.75 for v in l24)/len(A), 3)
res['shareA_ltv24_le80'] = round(sum(v <= 0.80 for v in l24)/len(A), 3)

B = [m for m in months if '1991-01' <= m <= '2016-07']
res['nB'] = len(B); res['firstB'] = B[0]; res['lastB'] = B[-1]
fk = {m: first_k(m) for m in B}
assert all(v is not None for v in fk.values()), [m for m,v in fk.items() if v is None]
res['medianB_months_to80'] = statistics.median(fk.values())
res['shareB_over60'] = round(sum(v > 60 for v in fk.values())/len(B), 3)
mx = max(fk.values())
res['maxB_months_to80'] = mx
res['maxB_start'] = [m for m in B if fk[m] == mx][0]
res['_maxB_ties'] = [m for m in B if fk[m] == mx]
res['shareB_le_sched80'] = round(sum(fk[m] <= sched(rate[m], 0.80) for m in B)/len(B), 3)
print(json.dumps(res, indent=1))
res.pop('_maxB_ties'); res.pop('_rate_latest_exact')
json.dump(res, open('result.json', 'w'), indent=1)
print('weeks', wk[latest], 'rate', rl)
