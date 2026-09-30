# retire-1 recomputation notes
- limit1982_in_aug2026_dollars = 6942.5907: 2000 x CPIAUCNS(2026-08, 334.980) / 12-month 1982 mean (96.5). No ambiguity; the blank 2025-10 CPI value is skipped and is not used.
- real_change_1982_to_2026_pct = 8.0288: uses the unrounded value above, as the definition says.
- real_loss_1982_to_2001_pct = 45.5008: 1 - mean1982/mean2001, both 12-month NSA means.
- hours_of_pay_1982 = 254.3: 2000 / mean of the 12 AHETPI values for 1982, rounded to 0.1.
- hours_of_pay_2026 = 230.6: 7500 / AHETPI(2026-08) = 7500/32.53, rounded to 0.1.
- hours_change_pct = -9.3197: computed from the rounded hours (230.6/254.3 - 1), as the definition says.
- Provisions were not fetched: the constants 2000 and 7500 are given in the definitions, so no provision text was needed for any calculation.
