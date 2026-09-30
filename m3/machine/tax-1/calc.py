"""tax-1: value of the mortgage interest deduction for the same median-priced home under the tax year 2026 SALT cap,
by the couple's state and local tax (SALT) bill. Reads data/ only; prints {id: value}."""
import csv, json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def last(sid):
    rows = [r for r in csv.reader(open(os.path.join(D, sid + '.csv')))][1:]
    rows = [r for r in rows if r[1] not in ('', '.')]
    return rows[-1][0], float(rows[-1][1])

# rules, tax year 2026 (see provisions)
STD_MFJ = 32200          # standard deduction, married filing jointly
RATE = 0.22              # MFJ bracket for taxable income over 100,800 up to 211,400
SALT_CAP_2026 = 40400    # applicable limitation amount (MAGI below 505,000)
SALT_CAP_2030 = 10000    # amount current law sets for taxable years beginning after 2029
LTV = 0.80               # assumption: 20% down payment
N = 360                  # 30-year fixed

_, rate = last('MORTGAGE30US')
_, price = last('MSPUS')
loan = LTV * price
i = rate / 100 / 12
pmt = loan * i / (1 - (1 + i) ** -N)
bal, interest = loan, 0.0
for _ in range(12):
    it = bal * i
    interest += it
    bal -= pmt - it

def benefit(salt_paid, cap):
    s = min(salt_paid, cap)
    return RATE * (max(STD_MFJ, s + interest) - max(STD_MFJ, s))

out = {
    'mortgage_rate_pct': rate,
    'median_price_usd': price,
    'loan_usd': round(loan, 2),
    'first_year_interest_usd': round(interest, 2),
    'benefit_salt5k_usd': round(benefit(5000, SALT_CAP_2026), 2),
    'benefit_salt15k_usd': round(benefit(15000, SALT_CAP_2026), 2),
    'benefit_salt25k_usd': round(benefit(25000, SALT_CAP_2026), 2),
    'benefit_salt40k_usd': round(benefit(40400, SALT_CAP_2026), 2),
    'benefit_salt40k_cap10k_usd': round(benefit(40400, SALT_CAP_2030), 2),
    'breakeven_salt_usd': round(STD_MFJ - interest, 2),
}
print(json.dumps(out))
