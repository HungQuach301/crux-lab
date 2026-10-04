# tax-4 V3 recalculation notes
Data: TB3MS and CPIAUCNS downloaded from the pinned URLs (fetch.py). SHA-256 matches the declared value for both series.
Rounding: Decimal ROUND_HALF_UP applied to the float repr. No value falls near a rounding boundary or a near-tie (checked: no window within $1 of $7,500, no year within 1e-4 of inflation).
- windows: count of start years 1934..2016 = 83.
- roth_real_loss_windows: 120 monthly factors (1+TB3MS/1200), times CPI(Jan Y)/CPI(Jan Y+10), < 7500 -> 39.
- taxable_real_loss_windows: each calendar year balance *= 1+0.78*(G-1), same deflator, < 7500 -> 47.
- roth_real_loss_share_pct: 39/83*100 rounded to 0.1 -> 47.0.
- taxable_real_loss_share_pct: 47/83*100 rounded to 0.1 -> 56.6.
- median_real_end_roth_usd: median of 83 values (an odd count, so a single middle value, from the 2000 window) -> 7644.89.
- median_real_end_taxable_usd: median of 83 (the 1948 window) -> 7098.09. Note: the two medians come from different windows.
- median_diff_usd: median of per-window (Roth - taxable), not the difference of the medians (7644.89-7098.09=546.80) -> 578.37.
- max_diff_usd: max per-window gap -> 1874.21.
- max_diff_start: 1980.
- latest_start: latest Y with TB3MS through Dec Y+9 and CPI Jan Y+10 -> 2016.
- latest_real_end_roth_usd: 2016 window -> 6790.14.
- latest_real_end_taxable_usd: 2016 window -> 6477.33.
- calendar_years: 1934..2025 = 92.
- years_beat_inflation_untaxed: G-1 > CPI(Dec Y)/CPI(Dec Y-1)-1 (strict) -> 52. Dec 1933 CPI is available, so 1934 is included.
- years_beat_inflation_after_tax: 0.78*(G-1) > inflation -> 40.
