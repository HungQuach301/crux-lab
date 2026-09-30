"""debt-7: when the 30-year rate fell, did national home-price gains cancel the payment relief? Reads data/ only."""
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
def f(rate):
    i = rate / 1200
    return i / (1 - (1 + i) ** -360)

out = {}
for lag, thr, tag in ((4, 1.0, '4q_1pt'), (4, 0.5, '4q_halfpt'), (8, 1.0, '8q_1pt')):
    ch, off, qs = [], [], []
    for i in range(len(H) - lag):
        (q0, h0), (q1, h1) = H[i], H[i + lag]
        r0, r1 = st.mean(wk[q0]), st.mean(wk[q1])
        if r0 - r1 < thr - 1e-9: continue
        relief = 1 - f(r1) / f(r0)
        ch.append(h1 * f(r1) / (h0 * f(r0)) - 1)
        off.append((h1 / h0 - 1) / relief)
        qs.append(q0)
    out[f'n_windows_{tag}'] = len(ch)
    out[f'share_payment_fell_{tag}'] = round(100 * sum(c < 0 for c in ch) / len(ch), 1)
    out[f'median_payment_change_{tag}'] = round(100 * st.median(ch), 1)
    out[f'median_offset_share_{tag}'] = round(100 * st.median(off), 1)
print(json.dumps(out))
