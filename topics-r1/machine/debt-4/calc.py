"""debt-4: pay 1 point to cut a 30-year rate from 7.00% to 6.75%? Break-even month count, and how often in history
the 30-year rate fell far enough to make a refinance likely before that break-even.
Reads data/MORTGAGE30US.csv only. Rates handled in integer hundredths of a point."""
import csv, json, math, statistics, datetime as dt

D = dt.date.fromisoformat
NOTE, BOUGHT, POINTS = 7.00, 6.75, 1.0
REFI_GAP = 100        # refinance trigger: market rate at least 1.00 point below the borrower's note rate


def pmt(r, n=360, p=100.0):
    x = r / 1200
    return p * x / (1 - (1 + x) ** -n)


save = pmt(NOTE) - pmt(BOUGHT)            # per $100 of loan, per month
be_months = POINTS / save                 # points cost = 1.0 per $100 of loan
H = math.ceil(be_months)                  # horizon in months

rows = [(D(r[0]), round(float(r[1]) * 100)) for r in list(csv.reader(open('data/MORTGAGE30US.csv')))[1:]
        if r[1] not in ('', '.')]
last = rows[-1][0]


def add_months(d, m):
    y, mo = divmod(d.month - 1 + m, 12)
    return dt.date(d.year + y, mo + 1, min(d.day, [31, 29 if (d.year + y) % 4 == 0 and ((d.year + y) % 100 != 0 or (d.year + y) % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][mo]))


drop_needed = round((NOTE - BOUGHT) * 100) + REFI_GAP   # market must fall this far below the start-week rate
res = []
for i, (d, r) in enumerate(rows):
    end = add_months(d, H)
    if end > last:
        break
    hit = next((e for (e, x) in rows[i + 1:] if e <= end and x <= r - drop_needed), None)
    res.append((d, r, hit))

n = len(res)
hits = [(d, h) for d, _, h in res if h]
near = [(d, r, h) for d, r, h in res if 650 <= r <= 750]
out = {
    'monthly_saving_per_100k': round(save * 1000, 2),
    'breakeven_months': round(be_months, 1),
    'horizon_months': H,
    'drop_needed_pts': drop_needed / 100,
    'n_weeks': n,
    'first_week': str(res[0][0]), 'last_week': str(res[-1][0]),
    'share_refi_before_breakeven': round(100 * len(hits) / n, 1),
    'median_months_to_trigger': round(statistics.median((h - d).days / 30.4375 for d, h in hits), 1),
    'n_weeks_6_5_to_7_5': len(near),
    'share_refi_before_breakeven_6_5_to_7_5': round(100 * sum(1 for *_, h in near if h) / len(near), 1),
    'latest_rate': rows[-1][1] / 100,
}
print(json.dumps(out))
