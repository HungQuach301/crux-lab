import csv, json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
def last(fn):
    rows = [r for r in csv.reader(open(os.path.join(D, fn)))][1:]
    rows = [r for r in rows if r[1] not in ('', '.')]
    return float(rows[-1][1])
STD, CAP26, CAP30, RATE = 32200, 40400, 10000, 0.22   # from IRS IR-2025-103 and 26 USC 164(b)(7)
rate = last('MORTGAGE30US.csv'); price = last('MSPUS.csv')
L = 0.80 * price; i = rate / 1200
pmt = L * i / (1 - (1 + i) ** -360)
bal, I = L, 0.0
for _ in range(12):
    it = bal * i; I += it; bal -= pmt - it
def ben(salt, cap=CAP26):
    S = min(salt, cap)
    return RATE * (max(STD, S + I) - max(STD, S))
out = {
    "mortgage_rate_pct": rate, "median_price_usd": price, "loan_usd": round(L, 2),
    "first_year_interest_usd": round(I, 2),
    "benefit_salt5k_usd": round(ben(5000), 2), "benefit_salt15k_usd": round(ben(15000), 2),
    "benefit_salt25k_usd": round(ben(25000), 2), "benefit_salt40k_usd": round(ben(40400), 2),
    "benefit_salt40k_cap10k_usd": round(ben(40400, CAP30), 2),
    "breakeven_salt_usd": round(STD - I, 2),
}
print(json.dumps(out, indent=1))
