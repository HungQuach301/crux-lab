# tax-3 recalculation notes
Data: the orchestrator placed data/CPIAUCSL.csv and data/MEHOINUSA646N.csv (from the pinned URLs); my own FRED downloads failed at the proxy. Statute text data/usc_25A.html was fetched by me: 25A(b)(1) max = $2,000 + 25% x $2,000 = $2,500; 25A(d)(1) joint phase-out starts at $160,000 and runs over $20,000. These match the credit formula.
- cpi_factor_2009_to_last12 = 1.536124: CPIAUCSL has a blank value for 2025-10. The definition and the assumption fix the window to Sep 2025-Aug 2026, so I averaged the 11 values present in that window, divided by the 2009 average of 12 values. Other reading: the last 12 non-missing values (Aug 2025-Aug 2026, skipping Oct) give 1.533675, which is the claim's 1.534. With that factor the next three numbers would be $245,388, $276,061 and $3,834, and both credits would still be 0.
- start_160k_in_current_prices_usd = 245780: round(160000 x unrounded factor).
- end_180k_in_current_prices_usd = 276502: round(180000 x factor).
- max_credit_2500_in_current_prices_usd = 3840: round(2500 x factor).
- credit_for_that_couple_now_usd = 0: MAGI = 160000 x factor (not rounded) is above 180000.
- couple_160k_2009_grown_with_median_income_usd = 281109: 160000 x 87460/49780.
- credit_for_median_growth_couple_now_usd = 0: MAGI 281109 is above 180000.
- start_as_multiple_of_median_income_2009 = 3.21: 160000/49780.
- start_as_multiple_of_median_income_latest = 1.83: 160000/87460 (2025).
- median_income_latest_year = 2025: date of the last MEHOINUSA646N row (2025-01-01).
