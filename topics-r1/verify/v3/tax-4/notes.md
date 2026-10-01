# tax-4 V3 recalculation notes
Source: data/AHETPI.csv downloaded from pinned FRED URL; SHA-256 de5ed1b8...0e1f MATCHES declared sha256.
- ahe_latest = 32.38: last non-missing row of AHETPI.csv. SHA match yes.
- ahe_date = 2026-06-01: observation_date of that row.
- regular_rate_usd = 32: round(32.38) to nearest dollar.
- ot_rate_usd = 48: 1.5 x 32.
- extra_pay_usd = 19200: 48 x 400.
- ot_premium_deduction_usd = 6400: 0.5 x 32 x 400 (below 12,500 cap; no phase-down applied per assumption).
- deductible_share_of_ot_pay_pct = 33.33: 100 x 6400/19200, 2 dp (claim text says "33%", consistent after rounding).
- ot_income_tax_on_extra_usd = 2816.00: T(66560+19200-16100-6400) - T(66560-16100) with 2026 single brackets; all increment in 22% bracket (base taxable 50,460 > 50,400). Cents.
- side_income_tax_on_extra_usd = 4224.00: same with D=0 (0.22 x 19200). Cents.
- payroll_tax_on_extra_usd = 1468.80: 0.0765 x 19200 (rounded to cents; exact anyway).
- ot_extra_take_home_usd = 14915.20: 19200 - 1468.80 - 2816.00.
- side_extra_take_home_usd = 13507.20: 19200 - 1468.80 - 4224.00.
- ot_advantage_usd = 1408.00: difference of take-homes.
- ot_total_tax_rate_on_extra_pct = 22.32: 100 x (1 - 14915.2/19200), 2 dp.
- side_total_tax_rate_on_extra_pct = 29.65: 100 x (1 - 13507.2/19200), 2 dp. Note: claim text says "29.6%"; 29.65 rounds half-up to 29.7 at 1 dp (exact value 29.65), so claim's 1-dp figure looks truncated/banker-rounded rather than half-up.
- side_breakeven_rate_usd = 53.00: bisection on [48, 144] for R with take_home(400R, D=0) = 14915.20 (target uses the cent-rounded OT take-home); exact R ~= 53.0035, rounds to 53.00. Increment stays in 22% bracket, so closed form 14915.2/(0.7035*400) agrees.
Ambiguities: (1) whether intermediate money values are cent-rounded before derived ratios (no effect here; all exact to cents). (2) Breakeven target taken from rounded ot_extra_take_home_usd (definition references that id); unrounded gives same 53.00.
