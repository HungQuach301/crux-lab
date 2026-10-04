# debt-4 recalc notes
SHA-256: both downloads match declared hashes (RIFLPBCIANM60NM 9ad2b525..., CUUR0000SETA01 abbc46cf...). Rounding: decimal half-up on repr(float). Pairs = months a with non-blank rate where the same calendar month of year+1 also has a rate and CPI exists at both (fetch.py downloads, recalc.py computes).
- n_pairs: count of such pairs = 76. No ambiguity.
- first_pair: earliest a = 2006-08 (dates as YYYY-MM).
- last_pair: latest a = 2025-05 (2026-05 rate exists, 2027-05 does not).
- share_payment_lower: count(wait payment - buy-now payment < 0)/76 = 0.382.
- median_payment_change: statistics.median (even n: mean of two middle values) of payment changes = 1.17.
- n_rate_fell: count rate[b] < rate[a] (strict) = 50.
- share_lower_when_rate_fell: among those 50, share with payment change < 0 = 0.52 (0.520).
- largest_rate_drop: min(rate[b]-rate[a]) = -1.08 (signed, as defined; claim text expresses magnitude 1.08).
- largest_rate_rise: max(rate[b]-rate[a]) = 2.96.
- best_payment_change: min payment change = -27.82 (signed; "saved $27.82" is magnitude).
- median_price_change: median of (CPI[b]/CPI[a]-1)*100 = 0.54 (even-n median = mean of middle two).
- rate_latest_month: last non-blank rate observation = 2026-05 (2026-05-01).
- rate_latest: 7.14 (as published, unrounded).
- pay_latest: annuity payment on 35,000, 60 mo, 7.14% = 695.36.
- one_point_effect: pay(7.14%) - pay(6.14%) on 35,000, rounded after subtracting unrounded payments = 16.43.
