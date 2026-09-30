"""retire-1: real and wage-relative value of the IRA contribution limit, 1982 vs 2026. Reads data/ only."""
import csv, json
def load(s):
    return {r[0]: float(r[1]) for r in list(csv.reader(open(f'data/{s}.csv')))[1:] if r[1] not in ('', '.')}
cpi = load('CPIAUCNS'); ahe = load('AHETPI')
def yavg(d, y): return sum(d[f'{y}-{m:02d}-01'] for m in range(1, 13)) / 12
LIM_1982, LIM_2026 = 2000.0, 7500.0
c82, c01, c_now = yavg(cpi, 1982), yavg(cpi, 2001), cpi['2026-08-01']
real82 = LIM_1982 * c_now / c82
out = {
    'limit1982_in_aug2026_dollars': round(real82, 2),
    'real_change_1982_to_2026_pct': round((LIM_2026 / real82 - 1) * 100, 2),
    'real_loss_1982_to_2001_pct': round((1 - c82 / c01) * 100, 2),
    'hours_of_pay_1982': round(LIM_1982 / yavg(ahe, 1982), 1),
    'hours_of_pay_2026': round(LIM_2026 / ahe['2026-08-01'], 1),
}
out['hours_change_pct'] = round((out['hours_of_pay_2026'] / out['hours_of_pay_1982'] - 1) * 100, 2)
print(json.dumps(out))
