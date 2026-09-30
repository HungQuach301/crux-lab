# debt-2 recalculation notes
- latest_r30: read directly from MORTGAGE30US at 2026-09-24 (7.03); no ambiguity.
- latest_r15: read directly from MORTGAGE15US at 2026-09-24 (6.42); no ambiguity.
- latest_spread: 7.03 - 6.42 rounded to 0.01 (0.61); no ambiguity.
- latest_premium_per_100k: final month taken as the first month where balance*(1+i30) <= P, paying balance*(1+i30); P not rounded to cents; result rounded to nearest dollar (11181).
- latest_months_to_payoff: count of payments including final partial one, same loop (193).
- mean_spread_all_weeks: common weeks = date intersection of both CSVs (missing "." values dropped; none found); mean of raw float differences, rounded to 0.001 (0.575).
- median_premium_all_weeks: n=1831 is odd, so median is the middle value, no averaging needed; rounded to dollar (8860).
- share_weeks_spread_ge_050: round() applied to spread*100 to avoid float error, as defined (Python banker's rounding; spreads are 2-dp so no .5 ties arise); 62.9.
- n_weeks: 1831 (1991-08-30 through 2026-09-24).
