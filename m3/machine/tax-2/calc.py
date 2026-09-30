"""tax-2: tax year 2026, married couple filing jointly, two children under 13, $15,000 of child care, all income is wages.
Path FSA: $7,500 through a dependent care assistance program (excluded from wages; credit limit becomes 0).
Path CREDIT: no FSA; child and dependent care credit on $6,000. Compares income tax after all credits + employee payroll tax.
Also: what the $6,000 expense cap (unchanged since tax year 2003) would be in current prices. Reads data/ only."""
import csv, json, math, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

BRK = [(24800, .10), (100800, .12), (211400, .22), (403550, .24), (512450, .32), (768700, .35), (float('inf'), .37)]
STD = 32200
FICA = 0.0765
CTC, ACTC_MAX, KIDS = 2200, 1700, 2
EITC_MAX, EITC_IN, EITC_PO_START, EITC_PO_RATE = 7316, 18290, 31160, 0.2106  # two children, joint
FSA, CAP2 = 7500, 6000

def income_tax(ti):
    tax, lo = 0.0, 0.0
    for hi, r in BRK:
        if ti > lo:
            tax += (min(ti, hi) - lo) * r
        lo = hi
    return tax

def cdcc_rate(agi):
    r = 50 - max(0, math.ceil((agi - 15000) / 2000))
    r = max(r, 35)
    r -= max(0, math.ceil((agi - 150000) / 4000))
    return max(r, 20) / 100

def eitc(earned, agi):
    phase_in = EITC_MAX / EITC_IN
    c = min(EITC_MAX, phase_in * earned)
    return max(0.0, c - EITC_PO_RATE * max(0.0, max(agi, earned) - EITC_PO_START))

def net_cost(wages, use_fsa):
    earned = wages - (FSA if use_fsa else 0)
    agi = earned
    tax = income_tax(max(0.0, agi - STD))
    exp_cap = max(0, CAP2 - (FSA if use_fsa else 0))
    cdcc = min(tax, cdcc_rate(agi) * exp_cap)
    tax -= cdcc
    ctc_total = KIDS * CTC  # AGI far below the 400,000 phase-out in the range studied
    nonref = min(tax, ctc_total)
    tax -= nonref
    actc = min(ctc_total - nonref, KIDS * ACTC_MAX, 0.15 * max(0.0, earned - 2500))
    return tax - actc - eitc(earned, agi) + FICA * earned

adv = {w: net_cost(w, True) - net_cost(w, False) for w in range(40000, 300001, 500)}  # >0: credit path costs less
wins = [w for w, a in adv.items() if a > 0]
# contiguous range containing 100000
lo = hi = 100000
while lo - 500 in adv and adv[lo - 500] > 0: lo -= 500
while hi + 500 in adv and adv[hi + 500] > 0: hi += 500

rows = [r for r in csv.reader(open(os.path.join(D, 'CPIAUCSL.csv')))][1:]
cpi = {r[0]: float(r[1]) for r in rows if r[1] not in ('', '.')}
avg2003 = sum(v for k, v in cpi.items() if k.startswith('2003-')) / 12
last12 = [cpi[k] for k in sorted(cpi)[-12:]]

out = {
    'credit_2026_usd_at_100k': round(cdcc_rate(100000) * CAP2, 2),
    'fsa_saving_usd_at_100k_12pct': round(FSA * (0.12 + FICA), 2),
    'advantage_credit_usd_at_100k': round(adv[100000], 2),
    'advantage_credit_usd_at_80k': round(adv[80000], 2),
    'advantage_fsa_usd_at_40k': round(-adv[40000], 2),
    'advantage_fsa_usd_at_180k': round(-adv[180000], 2),
    'credit_wins_from_wages_usd': lo,
    'credit_wins_to_wages_usd': hi,
    'cap_6000_in_current_prices_usd': round(6000 * sum(last12) / 12 / avg2003, 0),
}
print(json.dumps(out))
