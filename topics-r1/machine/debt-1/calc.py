"""debt-1: $500/month extra toward a 3.00% mortgage vs. into 3-month Treasury bills, Jan 2022 - Aug 2026.
Reads data/TB3MS.csv only. Prints one JSON object {id: value}."""
import csv, json

RATE = 3.00          # mortgage note rate, percent
EXTRA = 500.0        # dollars added at the start of each month
START, END = '2022-01-01', '2026-08-01'

rows = [(r[0], float(r[1])) for r in list(csv.reader(open('data/TB3MS.csv')))[1:] if r[1] not in ('', '.')]
months = [(d, v) for d, v in rows if START <= d <= END]


def bey(disc_pct):
    """3-month bill discount rate (percent) -> bond-equivalent yield (percent), 91-day bill."""
    d = disc_pct / 100
    return 100 * 365 * d / (360 - 91 * d)


def tbill_value(tax):
    a = 0.0
    for _, v in months:
        a = (a + EXTRA) * (1 + bey(v) * (1 - tax) / 1200)
    return a


def prepay_value():
    b = 0.0
    for _ in months:
        b = (b + EXTRA) * (1 + RATE / 1200)
    return b


out = {}
out['n_months'] = len(months)
out['contributed'] = round(EXTRA * len(months))
pv = prepay_value()
out['prepay_value'] = round(pv)
for t in (0, 22, 24, 32):
    tv = tbill_value(t / 100)
    out[f'tbill_value_tax{t}'] = round(tv)
    out[f'gap_tax{t}'] = round(tv - pv)
out['avg_bey'] = round(sum(bey(v) for _, v in months) / len(months), 2)
out['months_aftertax22_above_rate'] = sum(bey(v) * 0.78 > RATE for _, v in months)
run = 0
for _, v in reversed(months):
    if bey(v) * 0.78 < RATE:
        run += 1
    else:
        break
out['recent_run_aftertax22_below_rate'] = run
out['months_pretax_below_rate'] = sum(bey(v) < RATE for _, v in months)
lo, hi = 0.0, 0.9
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if tbill_value(mid) > pv else (lo, mid)
out['breakeven_tax_rate'] = round(100 * lo, 1)
out['last_tb3ms'] = months[-1][1]
print(json.dumps(out))
