# retire-2 recalculation notes (V3)

Data: PCU623110623110.csv downloaded from pinned URL (FRED, coed=2026-03-01), 376 monthly obs 1994-12-01..2026-03-01, no missing values. SHA-256 48158621...2484638f MATCHES declared.
Method notes common to all: windows s = 1994-12-01..2006-03-01 by month index, e = s+240 rows (series is contiguous monthly); P = PPI(e)/PPI(s). Median of an even count (136) = mean of the two middle values (statistics.median). Rounding = half-up via Decimal on the float value (no value sat on a rounding boundary).

- windows_20y = 136: count of start months Dec 1994..Mar 2006 inclusive.
- price_growth_full_period_pct_per_year = 3.52 (raw 3.5203): 100*((294.813/100)^(12/375)-1).
- price_growth_20y_min_pct_per_year = 2.78 (raw 2.7778): min of 100*(P^(1/20)-1).
- price_growth_20y_median_pct_per_year = 3.10 (raw 3.0995): median of annualized growth; written as 3.1 in JSON. Alternative (median of P then annualize) gives same up to monotonicity, identical for odd/even-mean only approximately; not material.
- price_growth_20y_max_pct_per_year = 3.61 (raw 3.6087).
- coverage_no_option_median_pct = 54.3 (raw 54.308): median of 100/P.
- coverage_3pct_median_pct = 98.1 (raw 98.087): median of 100*1.03^20/P.
- coverage_3pct_min_pct = 88.9 (raw 88.883).
- coverage_3pct_max_pct = 104.4 (raw 104.413).
- share_3pct_kept_up_pct = 44.1: 60 of 136 windows have coverage >= 100 (44.12%).
- coverage_5pct_median_pct = 144.1 (raw 144.096).
- coverage_5pct_min_pct = 130.6 (raw 130.576).
- share_5pct_kept_up_pct = 100.0: 136 of 136 windows >= 100.

Ambiguities: none material. Minor: even-count median convention (mean of middle two used); median-of-annualized vs annualized-median-P (would only differ via the averaging of the two middle values, negligible at 0.01).
