# retire-4 recalc notes
Data: TB3MS.csv SHA-256 ebf04b1a... matches declared; CPIAUCNS.csv SHA-256 f79e3a78... matches declared (downloaded via python requests, default UA). Rounding: Decimal ROUND_HALF_UP on repr of float.
- starts = 873: TB3MS months s with non-blank values for all of s..s+239.
- first_start = 1934-01-01: earliest such month.
- last_start = 2006-09-01: latest such month (window ends 2026-08-01).
- share_tbills_above_double_pct = 52.3: 100*count(M>2.0)/873, M = prod(1+TB3MS/1200) over 240 months.
- median_tbill_multiple_20y = 2.097: statistics.median of 873 M values (even-n issue n/a; n odd), raw 2.09668.
- min_tbill_multiple_20y = 1.129: min M.
- max_tbill_multiple_20y = 4.612: max M.
- share_tbills_above_double_starts_since_1990_pct = 5.0: starts 1990-01..2006-09 (201 months), share with M>2.0.
- latest_tbill_multiple_20y = 1.378: M(2006-09-01).
- doubling_rate_pct_per_year = 3.53: 100*(2^(1/20)-1)=3.5265.
- real_windows = 871: starts with non-blank CPIAUCNS at s and s+240; excluded 2005-10 (2025-10 blank) and 2006-09 (2026-09 not in file).
- share_double_beat_prices_pct = 58.7: share of 871 windows with 2*CPI(s)/CPI(s+240) >= 1.
- median_real_value_double_pct = 107.3: median of 100*2*CPI(s)/CPI(s+240) over 871 windows (n odd), raw 107.29.
- tb3ms_latest_pct = 3.72: TB3MS 2026-08-01 as published.
Ambiguities: none material; ">" vs ">=" for M>2.0 used as defined (no exact ties possible in practice).
