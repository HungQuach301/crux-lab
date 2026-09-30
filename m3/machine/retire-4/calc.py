"""retire-4: realized real return of a 10-year Treasury note bought at par and held to maturity. Reads data/ only."""
import csv, json
def load(s): return {r[0]: float(r[1]) for r in list(csv.reader(open(f'data/{s}.csv')))[1:] if r[1] not in ('', '.')}
g, c = load('GS10'), load('CPIAUCNS')
def add(d, months):
    y, m = int(d[:4]), int(d[5:7]) - 1 + months
    return f'{y + m // 12}-{m % 12 + 1:02d}-01'
res = []
for s in sorted(g):
    e = add(s, 120)
    if e > '2026-08-01': break
    if s not in c or e not in c: continue
    nominal = (1 + g[s] / 200) ** 20
    res.append((s, (nominal / (c[e] / c[s])) ** 0.1 - 1))
neg = [r for r in res if r[1] < 0]
sub = [r for r in res if '2014-02-01' <= r[0] <= '2016-08-01']
since08 = [r for r in res if r[0] >= '2008-01-01']
out = {
    'purchase_months': len(res),
    'share_negative_pct': round(len(neg) / len(res) * 100, 2),
    'late_lowrate_months': len(sub),
    'late_lowrate_negative': sum(1 for r in sub if r[1] < 0),
    'late_lowrate_worst_real_pct_per_year': round(min(r[1] for r in sub) * 100, 2),
    'late_lowrate_mean_real_pct_per_year': round(sum(r[1] for r in sub) / len(sub) * 100, 2),
    'share_negative_since_2008_pct': round(sum(1 for r in since08 if r[1] < 0) / len(since08) * 100, 2),
    'worst_real_pct_per_year': round(min(r[1] for r in res) * 100, 2),
}
print(json.dumps(out))
