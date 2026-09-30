# tax-5 recalculation notes
Data: FRED MSPUS (to 2026-04-01), CSUSHPINSA (to 2026-06-01), CPIAUCSL (to 2026-08-01) downloaded 2026-09-30. Statute text (uscode.house.gov 121(b), 1(h)(1)(C)) checked: $250,000, $500,000, 15%.
- last_purchase_year_gain_over_250k = 2017: gain(q)=MSPUS(q)*(CS Jun-2026 / mean CS of q's 3 months - 1); no ambiguity.
- last_purchase_quarter_of_that_year = 1: quarter from MSPUS date month (2017-01-01 -> Q1).
- quarters_gain_over_500k = 0: strict >.
- gain_median_bought_1997q3_usd = 421964: no ambiguity.
- gain_median_bought_2000q1_usd = 387451: no ambiguity.
- taxable_gain_single_bought_1997q3_usd = 171964: rounded after max(0, gain-250000).
- tax_at_15pct_single_bought_1997q3_usd = 25795: 0.15 x unrounded taxable gain.
- quarters_gain_over_250k = 107: strict >; qualifying quarters 1987Q1-2005Q1 and 2008Q4-2017Q1 (not separately output).
- quarters_total = 158: quarters 1987Q1-2026Q2 with MSPUS and all 3 CS months.
- max_gain_any_quarter_usd = 439615: max occurs at 1987Q4.
- exclusion_250k_in_current_prices_usd = 513313: AMBIGUITY - CPIAUCSL Oct 2025 is blank on FRED (no BLS release), so the Sep 2025-Aug 2026 window holds only 11 values; I used the mean of those 11. Alternative "last 12 available values" (Aug 2025-Aug 2026 skipping Oct) gives 512494 (matches claim). 1997 denominator = mean of all 12 1997 months.
- exclusion_to_median_price_1997 = 1.72: 250000 / mean of 4 1997 MSPUS quarters.
- exclusion_to_median_price_latest = 0.61: latest MSPUS = 2026-04-01 (410700).
