# tax-1 V3 recalculation notes
Data: fetched by fetch.py (requests, default UA); SHA-256 match for all 3 series (TB3MS, TERMCBCCALLNS, SNDR). Rounding: half-up to cents via Decimal.
- balance_months_per_dollar = 7.5: sum of min(k,12)/12 over 13 months (k=1..11 Feb-Dec Y, 12 for Jan and Feb Y+1) = 66/12+2. No ambiguity.
- tbill_2025_usd = 72.25: sum 3000*k/12*TB3MS_m/100/12 over Feb 2025-Feb 2026 (unrounded 72.2521). SHA match.
- savings_avg_2025_usd = 7.40: same with SNDR Feb 2025-Feb 2026. SHA match.
- card_2025_usd = 396.46: same with TERMCBCCALLNS forward-filled from latest non-empty obs <= month (blank cells treated as missing). Unrounded 396.4563.
- tbill_mean_2000_2025_usd = 35.10: mean of 26 unrounded per-year T-bill costs.
- tbill_max_usd = 106.76, tbill_max_year = 2000 (106.7562).
- tbill_min_usd = 0.50, tbill_min_year = 2014 (0.5042; 2011 is next at 0.6583).
- tbill_years_under_10usd = 10 (2009-2016, 2020, 2021).
- card_mean_2000_2025_usd = 268.93: mean of unrounded per-year card costs.
- card_min_usd = 222.71 (2013, 222.7125). card_max_usd = 404.04 (2024, 404.0375).
Ambiguities: none material; alternative of rounding per-year values before mean/extremes not used (definition says unrounded). Card forward fill for Feb 2000 uses Feb 2000 obs itself (series starts Feb 1999).
