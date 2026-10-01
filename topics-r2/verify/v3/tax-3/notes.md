# tax-3 V3 recalculation notes
SHA-256: both downloads (CPIAUCNS, MEHOINUSA646N) match declared sha256. Rounding: ROUND_HALF_UP via Decimal.
- cpi_1987_avg = 113.625: mean of 12 monthly 1987 CPIAUCNS values, rounded 0.001.
- cpi_2025_avg = 321.943: mean of 11 non-empty 2025 values (2025-10 blank in CSV), rounded 0.001.
- cpi_2025_months = 11: count of non-empty 2025 observations.
- price_factor_1987_2025 = 2.8334: rounded cpi_2025_avg / rounded cpi_1987_avg, rounded 0.0001. Alternative (unrounded means) gives 2.83338 -> 2.8334; no downstream value changes.
- start_in_2025_dollars = 283300: 100000*k (k=2.8334) to nearest 100.
- end_in_2025_dollars = 425000: 150000*k to nearest 100.
- cap_in_2025_dollars = 70800: 25000*k to nearest 100.
- start_real_value_pct_of_1987 = 35.3: 100/k rounded 0.1.
- median_1987 = 26060: FRED value 1987-01-01.
- median_2025 = 87460: FRED value 2025-01-01.
- start_over_median_1987 = 3.84: 100000/26060.
- start_over_median_2025 = 1.14: 100000/87460.
- end_over_median_2025 = 1.72: 150000/87460.
- start_if_tracked_median_2025 = 335600: 100000*87460/26060 = 335610.1 -> nearest 100.
- income_in_1987_dollars = 45900: 130000/k = 45881 -> nearest 100.
- allowance_at_income = 10000: 25000 - 0.5*30000.
- allowance_at_income_if_cpi_indexed = 70800: 130000 < 100000k so no reduction; 25000k = 70835 -> 70800.
