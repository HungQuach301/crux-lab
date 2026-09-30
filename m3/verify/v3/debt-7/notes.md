# debt-7 recalculation notes
Common: HPI restricted to 1975Q1-2026Q2 (206 quarters; no gaps). Rate quarter = mean of all weekly MORTGAGE30US obs whose date month falls in that quarter (2026Q2 fully covered). Threshold test implemented as drop >= thr - 1e-9. Median = statistics.median (average of two middle values for even counts). Rounding = Python round() (half-to-even; no ties hit at 0.1).
- n_windows_4q_1pt: 27. Start quarters q0 such that q0+4 is within HPI data; no ambiguity.
- share_payment_fell_4q_1pt: 100.0. Strict < 0.
- median_payment_change_4q_1pt: -8.2.
- median_offset_share_4q_1pt: 38.7. Offset = HPI growth / rate relief, all windows included (relief > 0 in every kept window).
- n_windows_4q_halfpt: 65.
- share_payment_fell_4q_halfpt: 96.9.
- median_payment_change_4q_halfpt: -5.6.
- median_offset_share_4q_halfpt: 45.1 (not stated in the claim; computed per definition).
- n_windows_8q_1pt: 57.
- share_payment_fell_8q_1pt: 91.2.
- median_payment_change_8q_1pt: -9.6.
- median_offset_share_8q_1pt: 53.0.
