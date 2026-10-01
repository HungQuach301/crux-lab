# retire-1 recalculation notes
Data: CPIAUCNS.csv downloaded from pinned FRED URL; SHA-256 f79e3a78...cdd7 MATCHES declared. Blank 2025-10-01 skipped. Rounding: Decimal ROUND_HALF_UP on float repr (no value lies on a .5 boundary, so half-even would give the same results). Medians are over an odd count (715), so no averaging of two middle values.
- windows_20y = 715: starts 1947-01..2006-08 (716 months) minus start 2005-10 (end 2025-10 blank).
- share_2pct_kept_up_20y_pct = 2.4: 100*17/715 = 2.3776 -> 2.4.
- windows_2pct_kept_up_20y = 17: 1.02^20 >= P; starts 1947-09 through 1949-01.
- windows_25y = 655: starts 1947-01..2001-08 (656) minus start 2000-10 (end 2025-10 blank).
- share_2pct_kept_up_25y_pct = 0.0: no 25y window had 1.02^25 >= P.
- median_inflation_20y_pct_per_year = 3.1 (raw 3.0987 -> 3.10 at 0.01; stored as number 3.1).
- median_real_value_2pct_payment_after_20y_pct = 80.7 (raw 80.7116).
- median_real_value_level_payment_after_20y_pct = 54.3 (raw 54.3166).
- worst_real_value_2pct_payment_after_20y_pct = 43.1 (raw 43.1142), window starting 1966-01.
- worst_window_start_year = 1966.
- latest_window_real_value_2pct_payment_pct = 90.4: CPI 2026-08 334.980 / 2006-08; raw 90.4486.
- latest_window_real_value_level_payment_pct = 60.9 (raw 60.8693).
Ambiguities: none material. Alternative: the 1.02^20 compounding could be read as 20 monthly-offset raises, but the definition specifies 1.02^20 literally, so it was used as is.
