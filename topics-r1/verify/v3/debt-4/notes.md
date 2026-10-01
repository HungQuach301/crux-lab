# debt-4 V3 recalculation notes
SHA-256 of data/MORTGAGE30US.csv = b2b254ffbdb7210029ada9e99feb345e124f6aeed7f20bdfbd7e5eff04f37a8a (matches declared). 2896 obs 1971-04-02..2026-09-24, no missing values. Rounding: Decimal ROUND_HALF_UP.
- monthly_saving_per_100k = 16.70: pmt(100000,7.00) - pmt(100000,6.75) = 16.7044, rounded to cents.
- breakeven_months = 59.9: 1.0 / (unrounded saving per $100 = 0.0167044) = 59.864. Ambiguity: using the cent-rounded saving (16.70) gives 59.88 -> also 59.9.
- horizon_months = 60: ceil(59.864).
- drop_needed_pts = 1.25: 0.25 + 1.00.
- n_weeks = 2635: start weeks with (t + 60 calendar months, day clipped to month end) <= 2026-09-24. Horizon fixed at 60 months as stated in definition (equals horizon_months).
- first_week = 1971-04-02.
- last_week = 2021-09-23 (horizon end 2026-09-23).
- share_refi_before_breakeven = 53.1: 1400 hits / 2635; hit = any w with t < w <= horizon end and rate(w) <= rate(t) - 125 (integer hundredths).
- median_months_to_trigger = 18.9: median over 1400 hits of days(t -> first qualifying w)/30.4375 (even count: mean of two middle values).
- n_weeks_6_5_to_7_5 = 362: eligible weeks with 650 <= rate(t) <= 750 inclusive.
- share_refi_before_breakeven_6_5_to_7_5 = 52.2: 189/362.
- latest_rate = 7.03: value on 2026-09-24.
