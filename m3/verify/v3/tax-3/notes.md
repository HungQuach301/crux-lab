# tax-3 recalculation notes
BLOCKER: both FRED downloads (CPIAUCSL, MEHOINUSA646N) failed every attempt (retries 2/4/8/16 s, 2 full rounds, timeout 120 s): agent proxy returned "Unable to connect to proxy / RemoteDisconnected" for fred.stlouisfed.org only (uscode.house.gov fetched fine). No values were taken from input.json lastObservation or the claim. All numbers are null. Re-run recalc.py once data/*.csv exist.
Statute check (data/usc_25A.html, 26 USC 25A): (b)(1) 100% of first $2,000 + 25% of next $2,000 = $2,500 max; (d)(1) phase-out over $160,000 joint across $20,000 ($80,000 / $10,000 others). Matches the credit formula in the definitions.
- cpi_factor_2009_to_last12: null (no CPIAUCSL). Planned: mean(Sep 2025-Aug 2026)/mean(2009 Jan-Dec), unrounded; asserts window is exactly Sep 2025-Aug 2026.
- start_160k_in_current_prices_usd: null. Planned round(160000*factor).
- end_180k_in_current_prices_usd: null. Planned round(180000*factor).
- max_credit_2500_in_current_prices_usd: null. Planned round(2500*factor).
- credit_for_that_couple_now_usd: null. Planned 2500*clamp((180000-160000*factor)/20000), MAGI unrounded.
- couple_160k_2009_grown_with_median_income_usd: null (no MEHOINUSA646N). Planned round(160000*latest/2009).
- credit_for_median_growth_couple_now_usd: null. Planned same formula at the rounded grown MAGI.
- start_as_multiple_of_median_income_2009: null. Planned round(160000/2009 value, 2).
- start_as_multiple_of_median_income_latest: null. Planned round(160000/latest value, 2).
- median_income_latest_year: null. Planned year of last non-missing observation.
