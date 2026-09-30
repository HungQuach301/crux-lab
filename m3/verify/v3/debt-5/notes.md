# debt-5 recalculation notes
Data: USSTHPI (1975Q1-2026Q2) and MORTGAGE30US downloaded from the pinned FRED URLs into ./data/ on 2026-09-30. Rounding: half-up. Median of 173 values = middle value.
- simple_n_cohorts = 173: kept cohorts 1975Q1-2018Q1; "inside the HPI data" read as q+ceil(sched/3) <= index of 2026Q2.
- simple_median_years_schedule = 11.58: schedule month = first m in 1..360 with b_m <= 80.
- simple_median_years_value = 3.0: value months searched at m = 3,6,...,360 while q+k is within the HPI data; m=0 not considered (b_0 = 95 > 80 anyway).
- simple_share_value_faster_3y = 89.0: condition s/12 - v/12 >= 3 (equivalently s - v >= 36 months). The claim's 87.9% matches the seasoned variant, not this one.
- seasoned_median_years_value = 4.0: LIMIT none for m<24, 0.75 for 24<=m<=59, 0.80 for m>=60.
- seasoned_share_value_faster_3y = 87.9: same condition as simple, seasoned limits.
- seasoned_share_value_not_faster = 2.9: 5 cohorts (2005Q2, 2005Q3, 2005Q4, 2006Q1, 2007Q1), all reached but with value months >= schedule months; none 'not reached'. Note 2006Q2-2006Q4 are not in this set, so "the 2005-2007 buyers" describes a subset of that span, not all of it.
