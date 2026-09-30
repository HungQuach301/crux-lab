"""debt-5: years until mortgage insurance could end on a 5%-down 30-year fixed loan: legal schedule (balance vs original value)
vs national home-value appreciation (balance vs current value). Reads data/ only."""
import csv, json, statistics as st
from collections import defaultdict
def load(s):
    return [(r[0], float(r[1])) for r in list(csv.reader(open(f'data/{s}.csv')))[1:] if r[1] not in ('', '.')]
def qkey(d):
    return d[:4] + 'Q' + str((int(d[5:7]) - 1) // 3 + 1)
wk = defaultdict(list)
for d, v in load('MORTGAGE30US'):
    wk[qkey(d)].append(v)
H = [(qkey(d), v) for d, v in load('USSTHPI')]

def cohort(i, rule):
    q, h0 = H[i]
    rate = st.mean(wk[q]) / 1200
    pay = 95 * rate / (1 - (1 + rate) ** -360)
    bal, sched, app = 95.0, None, None
    for m in range(1, 361):
        bal = bal * (1 + rate) - pay
        if sched is None and bal <= 80: sched = m
        if m % 3 == 0 and app is None and i + m // 3 < len(H):
            ltv = bal / (100 * H[i + m // 3][1] / h0)
            lim = 0.80 if rule == 'simple' else (None if m < 24 else 0.75 if m < 60 else 0.80)
            if lim is not None and ltv <= lim: app = m
    return sched, app

out = {}
for rule in ('simple', 'seasoned'):
    res = []
    for i, (q, _) in enumerate(H):
        if q not in wk: continue
        sched, app = cohort(i, rule)
        if i + (sched + 2) // 3 >= len(H): continue   # schedule date must be inside the value data
        res.append((q, sched / 12, app / 12 if app else None))
    out[f'{rule}_n_cohorts'] = len(res)
    out[f'{rule}_median_years_schedule'] = round(st.median(s for _, s, _ in res), 2)
    out[f'{rule}_median_years_value'] = round(st.median(a if a is not None else 1e9 for _, _, a in res), 2)
    out[f'{rule}_share_value_faster_3y'] = round(100 * sum(1 for _, s, a in res if a is not None and s - a >= 3) / len(res), 1)
    out[f'{rule}_share_value_not_faster'] = round(100 * sum(1 for _, s, a in res if a is None or a >= s) / len(res), 1)
print(json.dumps(out))
