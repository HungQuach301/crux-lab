# debt-1 recalculation notes
Data: FRED MORTGAGE30US CSV, 2896 obs 1971-04-02..2026-09-24, no missing values. Rates -> integer hundredths (half-up). Rounding to 0.1 uses half-up.
- share_3y_1pt = 48.3: horizon 1096 days; success if min over weeks in (t, t+1096d] <= rate(t) - 100 hundredths.
- n_weeks_3y = 2739: eligible weeks with t+1096d <= 2026-09-24.
- share_2y_1pt = 39.9: horizon round(730.5) = 730 days (Python banker's rounding; 731 would be half-up; took Python round() as literal; checked: 731 gives the same 39.9 and 2791).
- n_weeks_2y = 2791: same eligibility rule, 730-day horizon.
- share_5y_1pt = 61.9: horizon round(1826.25) = 1826 days.
- n_weeks_5y = 2635.
- share_3y_1pt_falling_era = 60.2: start weeks 1981-10-09..2020-12-31 inclusive (all also satisfy the horizon-eligibility rule); future weeks allowed past 2020.
- n_weeks_3y_falling_era = 2048.
- latest_rate = 7.03: last observation 2026-09-24.
