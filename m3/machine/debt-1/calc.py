"""debt-1: how often did a refinance-sized drop (>= 1.00 point) in the 30-year fixed rate arrive within H years of a given week?
Reads data/MORTGAGE30US.csv only. Rates handled in integer hundredths of a point to avoid float ties."""
import csv, json, datetime as dt
D = dt.date.fromisoformat
rows = [(D(r[0]), round(float(r[1]) * 100)) for r in list(csv.reader(open('data/MORTGAGE30US.csv')))[1:] if r[1] not in ('', '.')]
last = rows[-1][0]

def share(h_years, drop_bp, start=None, end_start=None):
    n = k = 0
    for i, (d, r) in enumerate(rows):
        if start and d < start: continue
        if end_start and d > end_start: break
        end = d + dt.timedelta(days=round(365.25 * h_years))
        if end > last: break
        fut = [x for (e, x) in rows[i + 1:] if e <= end]
        n += 1
        k += min(fut) <= r - drop_bp
    return n, k / n

out = {}
for h in (2, 3, 5):
    n, p = share(h, 100)
    out[f'share_{h}y_1pt'] = round(100 * p, 1)
    out[f'n_weeks_{h}y'] = n
n, p = share(3, 100, start=D('1981-10-09'), end_start=D('2020-12-31'))
out['share_3y_1pt_falling_era'] = round(100 * p, 1)
out['n_weeks_3y_falling_era'] = n
out['latest_rate'] = rows[-1][1] / 100
print(json.dumps(out))
