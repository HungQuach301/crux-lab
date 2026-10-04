# debt-1 V3 recalculation notes
Data: both CSVs downloaded from pinned URLs; SHA-256 match declared (MORTGAGE30US b2b254ff..., MORTGAGE15US 5533aa2f...). Rounding = half-up on the float value (Decimal).
- n_weeks: 1831 = count of dates present in both series within 1991-08-30..2026-09-24 (inclusive). No unmatched dates in window.
- first_week: 1991-08-30, first paired date.
- last_week: 2026-09-24, last paired date.
- rate30_latest: 7.03, MORTGAGE30US on 2026-09-24.
- rate15_latest: 6.42, MORTGAGE15US on 2026-09-24.
- pay15_latest: 2773.49 (unrounded 2773.4896), P=320000, x=6.42/1200, n=180.
- pay30on15_latest: 2881.62 (2881.6202), x=7.03/1200, n=180.
- pay30_latest: 2135.42 (2135.4192), x=7.03/1200, n=360.
- extra_month_latest: 108.13, unrounded difference then rounded.
- extra_total_latest: 19464 (19464.38), unrounded difference x 180.
- months_payoff_at_pay15: 192.9 (192.9001), n=-ln(1-P*x/pay15)/ln(1+x), x=7.03/1200, pay15 unrounded.
- spread_mean: 0.57 (0.57479), arithmetic mean of 30y-15y over 1831 weeks.
- spread_min: 0.2 (float noise removed before rounding).
- spread_max: 1.0.
- share_spread_ge_050: 0.629 (0.62916); same with or without 1e-9 float tolerance on >= 0.50.
- extra_total_median: 16594 (16593.76), median of weekly (pay(r30,180)-pay(r15,180))*180, unrounded payments.
- extra_total_min: 6097 (6097.496; close to the .5 boundary but rounds down under any standard rule).
- extra_total_max: 29502 (29502.03).
Ambiguities: none material. Weekly extras use unrounded payments (the "unrounded" rule is stated for the latest week only); using cent-rounded payments could move totals by up to about $1.80.
