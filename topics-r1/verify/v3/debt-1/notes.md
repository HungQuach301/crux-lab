# debt-1 V3 recalculation notes
Data: data/TB3MS.csv downloaded from pinned FRED URL; SHA-256 ebf04b1a...ae6ab MATCHES declared. 56 obs 2022-01..2026-08; BEY = 100*365*d/(360-91*d).
- n_months = 56: count of observations 2022-01-01..2026-08-01 (asserted 56).
- contributed = 28000: 500*56.
- prepay_value = 30090: B=(B+500)*(1+0.03/12) x56, unrounded 30089.61, rounded.
- tbill_value_tax0 = 31091: A=(A+500)*(1+BEY/1200) per month, unrounded 31091.40.
- gap_tax0 = 1002: unrounded difference 1001.79 rounded (note: rounded-minus-rounded would give 1001; definition says unrounded, used that).
- tbill_value_tax22 = 30374; gap_tax22 = 285 (unrounded diff, rounded).
- tbill_value_tax24 = 30310; gap_tax24 = 221.
- tbill_value_tax32 = 30056; gap_tax32 = -34.
- avg_bey = 4.08: simple mean of 56 BEY values, round 0.01.
- months_aftertax22_above_rate = 37: count BEY*0.78 > 3.00 (strict).
- recent_run_aftertax22_below_rate = 9: consecutive months from 2026-08 backward with BEY*0.78 < 3.00.
- months_pretax_below_rate = 8: count BEY < 3.00 (strict).
- breakeven_tax_rate = 30.9: bisection [0,0.9], 60 iters, lo kept where tbill(mid) > prepay (unrounded); lo=0.30927 -> 30.9. No ambiguity.
- last_tb3ms = 3.72: raw TB3MS 2026-08-01.
Ambiguities: none material; Python round() is banker's rounding but no value fell on an exact .5.
