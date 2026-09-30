"""retire-7: rolling 3-month Treasury bills for ten years vs buying a 10-year Treasury note and holding it. Reads data/ only."""
import csv, json
def load(s): return {r[0]: float(r[1]) for r in list(csv.reader(open(f'data/{s}.csv')))[1:] if r[1] not in ('', '.')}
g, t = load('GS10'), load('TB3MS')
def add(d, months):
    y, m = int(d[:4]), int(d[5:7]) - 1 + months
    return f'{y + m // 12}-{m % 12 + 1:02d}-01'
res = []
for s in sorted(g):
    months = [add(s, k) for k in range(120)]
    if any(m not in t for m in months): continue
    bills = 1.0
    for m in months: bills *= 1 + t[m] / 1200
    note = (1 + g[s] / 200) ** 20
    res.append((s, bills / note))
def share(rows): return round(sum(1 for _, x in rows if x > 1) / len(rows) * 100, 2)
r6070 = [r for r in res if '1960-01-01' <= r[0] <= '1979-12-01']
r80 = [r for r in res if r[0] >= '1980-01-01']
out = {
    'purchase_months': len(res),
    'first_purchase_yyyymm': int(res[0][0][:4] + res[0][0][5:7]),
    'last_purchase_yyyymm': int(res[-1][0][:4] + res[-1][0][5:7]),
    'share_bills_won_pct': round(share(res), 2),
    'share_bills_won_1960_1979_pct': share(r6070),
    'share_bills_won_since_1980_pct': share(r80),
    'best_bills_advantage_pct': round((max(x for _, x in res) - 1) * 100, 1),
    'best_note_advantage_pct': round((1 / min(x for _, x in res) - 1) * 100, 1),
}
print(json.dumps(out))
