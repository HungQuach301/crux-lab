# tax-6 recomputation notes
Data: FRED CPIAUCNS and SUUR0000SA0 downloaded 2026-09-30 (last obs 2026-08-01 match input). Provision texts not fetched: all tax parameters (brackets, std deduction, EITC max) are stated explicitly in the definitions.
- cpiu_growth_2016_2025_pct: A(y) = mean of Sep(y-1)..Aug(y) monthly NSA values; no ambiguity.
- ccpiu_growth_2016_2025_pct: same with SUUR0000SA0 as currently on FRED (final values, not initial as published at the time).
- gap_2016_base_pct: ratio of ratios minus 1, x100; g16 kept unrounded for downstream use.
- gap_2017_base_pct: same with 2017 window (Sep 2016-Aug 2017); g17 unrounded.
- gap_per_year_pp: 9 years (2016->2025), literal formula.
- top12_mfj_under_cpiu_usd: rounded to nearest dollar (Python round, banker's rounding irrelevant here).
- extra_tax_mfj_agi100k_usd: T = AGI - 32,200 (standard deduction unchanged); hypothetical limits unrounded (no $50 rounding); unrounded dollar difference reported.
- extra_tax_mfj_agi200k_usd: same.
- extra_tax_mfj_agi300k_usd: same.
- eitc_max3_under_cpiu_usd: rounded to nearest dollar.
- eitc_max3_shortfall_usd: unrounded 8231 x g16.
- eitc_shortfall_share_of_25k_earnings_pct: unrounded; plateau assumption taken as given.
- extra_tax_share_of_agi200k_pct: uses unrounded extra_tax_mfj_agi200k_usd.
