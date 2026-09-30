"""retire-3: purchasing power lost by a fixed (no cost-of-living raise) pension over retirement-length windows since 1947. Reads data/ only."""
import csv, json, statistics
c = {r[0]: float(r[1]) for r in list(csv.reader(open('data/CPIAUCNS.csv')))[1:] if r[1] not in ('', '.')}
def add(d, months):
    y, m = int(d[:4]), int(d[5:7]) - 1 + months
    return f'{y + m // 12}-{m % 12 + 1:02d}-01'
def windows(years):
    out = []
    d = '1947-01-01'
    while add(d, 12 * years) <= '2026-08-01':
        e = add(d, 12 * years)
        if d in c and e in c:
            out.append((1 - c[d] / c[e], d))
        d = add(d, 1)
    return out
w25, w30 = windows(25), windows(30)
l25 = [x for x, _ in w25]
mn = min(w25)
out = {
    'windows_25y': len(w25),
    'min_loss_25y_pct': round(mn[0] * 100, 2),
    'min_loss_25y_start_yyyymm': int(mn[1][:4] + mn[1][5:7]),
    'median_loss_25y_pct': round(statistics.median(l25) * 100, 2),
    'max_loss_25y_pct': round(max(l25) * 100, 2),
    'share_25y_over_half_pct': round(sum(1 for x in l25 if x > 0.5) / len(l25) * 100, 2),
    'min_loss_30y_pct': round(min(w30)[0] * 100, 2),
    'median_loss_30y_pct': round(statistics.median([x for x, _ in w30]) * 100, 2),
}
print(json.dumps(out))
