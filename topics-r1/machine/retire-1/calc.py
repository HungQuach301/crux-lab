"""retire-1: level annuity payment vs a payment that rises 2% a year, tested on every 20-year (and 25-year) window of
US consumer prices since January 1947. Reads data/CPIAUCNS.csv only. History, not a forecast."""
import csv, json, statistics

cpi = {}
for row in list(csv.reader(open('data/CPIAUCNS.csv')))[1:]:
    if row[1] not in ('', '.'):
        cpi[row[0]] = float(row[1])


def add_months(d, n):
    y, m = int(d[:4]), int(d[5:7])
    k = y * 12 + (m - 1) + n
    return f'{k // 12:04d}-{k % 12 + 1:02d}-01'


STEP = 0.02
months = sorted(d for d in cpi if d >= '1947-01-01')


def windows(years):
    out = []
    for s in months:
        e = add_months(s, 12 * years)
        if e in cpi:
            out.append((s, e, cpi[e] / cpi[s]))
    return out


w20 = windows(20)
w25 = windows(25)
step20 = (1 + STEP) ** 20
step25 = (1 + STEP) ** 25
kept20 = [x for x in w20 if step20 >= x[2]]
kept25 = [x for x in w25 if step25 >= x[2]]
real_step20 = [100 * step20 / x[2] for x in w20]
real_level20 = [100 / x[2] for x in w20]
infl20 = [100 * (x[2] ** (1 / 20) - 1) for x in w20]
worst = min(w20, key=lambda x: step20 / x[2])
latest = [x for x in w20 if x[0] == '2006-08-01'][0]

out = {
    'windows_20y': len(w20),
    'share_2pct_kept_up_20y_pct': round(100 * len(kept20) / len(w20), 1),
    'windows_2pct_kept_up_20y': len(kept20),
    'windows_25y': len(w25),
    'share_2pct_kept_up_25y_pct': round(100 * len(kept25) / len(w25), 1),
    'median_inflation_20y_pct_per_year': round(statistics.median(infl20), 2),
    'median_real_value_2pct_payment_after_20y_pct': round(statistics.median(real_step20), 1),
    'median_real_value_level_payment_after_20y_pct': round(statistics.median(real_level20), 1),
    'worst_real_value_2pct_payment_after_20y_pct': round(100 * step20 / worst[2], 1),
    'worst_window_start_year': int(worst[0][:4]),
    'latest_window_real_value_2pct_payment_pct': round(100 * step20 / latest[2], 1),
    'latest_window_real_value_level_payment_pct': round(100 / latest[2], 1),
}
print(json.dumps(out))
