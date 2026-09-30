# tax-1 recalculation notes
Parameters verified from fetched official text: 26 USC 164(b)(7)(A) cap $40,400 (2026), $10,000 (after 2029), phasedown threshold $505,000 (2026); 163(h)(2)(D) quote present; IRS IR-2025-103: std deduction $32,200 MFJ, 22% bracket $100,800-$211,400 MFJ.
- mortgage_rate_pct: last non-missing row of data/MORTGAGE30US.csv (2026-09-24 = 7.03). No ambiguity.
- median_price_usd: last row of data/MSPUS.csv (2026-04-01 = 410700). No ambiguity.
- loan_usd: 0.80 x price = 328560.00, rounded to cents.
- first_year_interest_usd: exact amortization per definition, payment not rounded to cents (literal reading); sum rounded to cents = 22992.20.
- benefit_salt5k_usd: 0.22 x [max(32200,S+I)-max(32200,S)], S=min(5000,40400), I unrounded; result rounded to cents.
- benefit_salt15k_usd: same, S=15000.
- benefit_salt25k_usd: same, S=25000.
- benefit_salt40k_usd: same, S=40400 (=0.22 x I).
- benefit_salt40k_cap10k_usd: S=min(40400,10000)=10000, std deduction kept at 32200 per definition.
- breakeven_salt_usd: 32200 - I using unrounded I, rounded to cents (identical to using rounded I at cent precision: 9207.80).
