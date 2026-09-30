import csv, json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
def load(sid):
    out = {}
    with open(os.path.join(D, sid + '.csv')) as f:
        for row in csv.DictReader(f):
            v = row[sid].strip()
            if v not in ('', '.'):
                out[row['observation_date']] = float(v)
    return out
def year_mean(s, y):
    vals = [s[f'{y}-{m:02d}-01'] for m in range(1, 13)]
    return sum(vals) / 12
cpi = load('CPIAUCNS'); ahe = load('AHETPI')
c82 = year_mean(cpi, 1982); c01 = year_mean(cpi, 2001); c26 = cpi['2026-08-01']
lim = 2000 * c26 / c82
h82 = round(2000 / year_mean(ahe, 1982), 1)
h26 = round(7500 / ahe['2026-08-01'], 1)
print(json.dumps({
    'limit1982_in_aug2026_dollars': lim,
    'real_change_1982_to_2026_pct': (7500 / lim - 1) * 100,
    'real_loss_1982_to_2001_pct': (1 - c82 / c01) * 100,
    'hours_of_pay_1982': h82,
    'hours_of_pay_2026': h26,
    'hours_change_pct': (h26 / h82 - 1) * 100,
}, indent=1))
