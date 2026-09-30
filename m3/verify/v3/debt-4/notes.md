# debt-4 recalculation notes
- n_days: 2434 = dates where all three FRED CSVs have numeric values (107 blank holiday rows per series dropped), 2017-01-03..2026-09-29. No ambiguity.
- mean_ltv_gap: 0.065 (unrounded 0.065113). Mean of GT80_GE740 - LE80_GE740 over common dates.
- max_ltv_gap: 0.173 (float 0.17300000000000004; exact 3-decimal difference, rounding not borderline).
- mean_credit_gap: 0.343 (unrounded 0.343463). Mean of LE80_LT680 - LE80_GE740.
- credit_to_ltv_ratio: 5.3 (unrounded 5.2748), computed from unrounded means as defined.
- share_days_credit_gap_gt_ltv_gap: 99.2 (unrounded 99.219). Strict ">" used; ties count as not greater.
- latest_le80_ge740: 7.268 (raw value on 2026-09-29).
- latest_gt80_ge740: 7.331 (raw value on 2026-09-29).
- latest_le80_lt680: 7.529 (raw value on 2026-09-29).
