"""tax-4: a single hourly worker paid the typical production/nonsupervisory wage (rounded to whole dollars) can add
8 hours a week for 50 weeks either as overtime at time-and-a-half or at a second W-2 job paying the same hourly
amount. Federal income tax (2026 single brackets, standard deduction, overtime-premium deduction) plus employee
payroll tax on each path; break-even side-job rate. Reads data/ only; prints one JSON object {id: value}."""
import csv, json, os

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# 2026 rules (single filer), quoted in sources.json provisions
STD = 16100
BRACKETS = [(0, 0.10), (12400, 0.12), (50400, 0.22), (105700, 0.24), (201775, 0.32), (256225, 0.35), (640600, 0.37)]
OT_CAP = 12500           # overtime-premium deduction cap (single)
OT_PHASE_START = 150000  # MAGI where the cap starts to phase down (not reached here)
FICA = 0.062 + 0.0145    # employee social security + medicare (wage base not reached)

HOURS_YEAR = 2080        # 40 h x 52 weeks
EXTRA_H = 8 * 50         # 8 extra hours a week, 50 weeks

rows = [r for r in list(csv.reader(open(os.path.join(D, 'AHETPI.csv'))))[1:] if len(r) > 1 and r[1] not in ('', '.')]
ahe_date, ahe = rows[-1][0], float(rows[-1][1])
W = float(round(ahe))    # regular hourly rate used for the viewer


def income_tax(taxable):
    t = 0.0
    for i, (lo, r) in enumerate(BRACKETS):
        hi = BRACKETS[i + 1][0] if i + 1 < len(BRACKETS) else float('inf')
        if taxable > lo:
            t += (min(taxable, hi) - lo) * r
    return t


base = W * HOURS_YEAR
tax_base = income_tax(max(0.0, base - STD))


def extra_net(extra_pay, ot_premium):
    agi = base + extra_pay
    ded = min(ot_premium, OT_CAP)  # MAGI below phase-down start in all cases here
    assert agi <= OT_PHASE_START
    tax = income_tax(max(0.0, agi - STD - ded))
    return extra_pay - FICA * extra_pay - (tax - tax_base), tax - tax_base


ot_rate = 1.5 * W
ot_pay = ot_rate * EXTRA_H
premium = 0.5 * W * EXTRA_H
ot_net, ot_itax = extra_net(ot_pay, premium)
side_net, side_itax = extra_net(ot_pay, 0.0)

lo, hi = ot_rate, 3 * ot_rate  # side-job hourly rate giving the same extra take-home as overtime
for _ in range(200):
    mid = (lo + hi) / 2
    if extra_net(mid * EXTRA_H, 0.0)[0] < ot_net:
        lo = mid
    else:
        hi = mid

out = {
    'ahe_latest': ahe,
    'ahe_date': ahe_date,
    'regular_rate_usd': W,
    'ot_rate_usd': ot_rate,
    'extra_pay_usd': ot_pay,
    'ot_premium_deduction_usd': premium,
    'deductible_share_of_ot_pay_pct': round(100 * premium / ot_pay, 2),
    'ot_income_tax_on_extra_usd': round(ot_itax, 2),
    'side_income_tax_on_extra_usd': round(side_itax, 2),
    'payroll_tax_on_extra_usd': round(FICA * ot_pay, 2),
    'ot_extra_take_home_usd': round(ot_net, 2),
    'side_extra_take_home_usd': round(side_net, 2),
    'ot_advantage_usd': round(ot_net - side_net, 2),
    'ot_total_tax_rate_on_extra_pct': round(100 * (1 - ot_net / ot_pay), 2),
    'side_total_tax_rate_on_extra_pct': round(100 * (1 - side_net / ot_pay), 2),
    'side_breakeven_rate_usd': round(hi, 2),
}
print(json.dumps(out))
