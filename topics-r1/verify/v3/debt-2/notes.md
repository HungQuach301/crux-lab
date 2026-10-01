# debt-2 V3 recalculation notes
Data: data/TB3MS.csv downloaded from pinned FRED URL; SHA-256 ebf04b1a...ae6ab MATCHES declared value. 1934-01..2026-08, last value 3.72.
Method: each month k=0..119, interest = bal*rate/1200; payment recomputed as level payment over 120-k remaining months when the rate changes (variable balance ends at ~0). Rounding: half-up via Decimal.
- n_starts = 753: every month 1954-01..last s with s+119 in data (2016-09).
- first_start = 1954-01-01.
- last_start = 2016-09-01 (derived from data, matches definition).
- fixed_total_interest = 26005: 9.00% fixed, 120 level payments, summed interest.
- share_variable_costlier = 14.2: share of 753 starts with variable-fixed > 0.
- median_variable_minus_fixed = -3832: median of 753 differences (odd count, raw -3832.20).
- worst_variable_minus_fixed = 11219: max difference.
- worst_start = 1977-04-01.
- best_variable_minus_fixed = -15295: min difference.
- max_variable_rate_any_window = 20.6 (20.60): max over all windows of 3.78 + max(0, 3.72 + TB[s+k] - TB[s]).
- n_starts_1954_1980 = 324.
- share_costlier_1954_1980 = 28.4.
- n_starts_1981_on = 429.
- share_costlier_1981_on = 3.5.
- index_today = 3.72 (2026-08-01 observation).
- margin = 3.78 (7.50 - 3.72).
Ambiguities: none material. Margin used unrounded as 7.50 - 3.72 in floats; "recompute when rate changes" is equivalent to recomputing every month. Rounding half-up vs banker's does not affect any value here.
