# retire-3 V3 recalculation notes
Data: GS1.csv and GS5.csv downloaded from pinned FRED URLs (coed=2026-08-01) via fetch.py; SHA-256 match declared values for both (GS1 d6dc7506..., GS5 66e94ca2...). Rounding: ROUND_HALF_UP via Decimal.
- starts_all = 833: GS5 months >= 1953-04-01 with GS1 present at s, s+12..s+48; first 1953-04-01, last 2022-08-01. No Lock==Roll ties.
- first_start_year = 1953; last_start_year = 2022 (from computed first/last start).
- share_lock_ahead_all_pct = 65.2: 100*count(Lock>Roll)/833, rounded 0.1.
- starts_inverted = 132: strict GS1(s)>GS5(s). 6 start months have GS1==GS5 exactly and are excluded (strict reading per definition).
- share_lock_ahead_inverted_pct = 64.4: rounded 0.1.
- inversion_episodes = 23: runs of consecutive calendar months among inverted starts.
- episodes_lock_ahead_majority = 14: strict >half; note 2019-01..2019-10 episode is exactly 5/10 (not counted; a ">= half" reading would give 15).
- median_lock_vs_roll_inverted_pct = 2.5 (raw 2.5014; 132 values, even count -> mean of two middle values via statistics.median).
- best_lock_vs_roll_inverted_pct = 22.05; worst_lock_vs_roll_inverted_pct = -13.93: max/min of 100*(Lock/Roll-1), rounded 0.01.
- gs1_latest_pct = 4.03; gs5_latest_pct = 4.38: values at 2026-08-01 as published.
