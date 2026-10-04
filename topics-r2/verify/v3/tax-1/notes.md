# tax-1 V3 recalculation notes
Data: FII10.csv SHA-256 5c396a03...35e0 MATCH; CPIAUCNS.csv SHA-256 234aefc8...6e9163 MATCH (downloaded via requests from pinned URLs). CPIAUCNS 2025-10 is blank in the file. Rounding: Decimal ROUND_HALF_UP on the float value; medians over 166 (even) use mean of the two middle values (statistics.median).
- windows = 166: purchase months 2003-01..2016-11 (167) minus those where any ref(m+12j), j=0..10, is missing; ref(x)=CPI(x-3).
- windows_skipped_missing_cpi = 1: only 2016-01 (its j=10 checkpoint needs CPI 2025-10).
- first_purchase = 2003-01: first simulated month.
- last_purchase = 2016-11: last simulated month (ref(m+120)=CPI 2026-08).
- taxable_negative_real_count = 64: W_{k+1}=W_k(1+0.76(g_k-1)), real end = W_10/prod f_k, annualized = ^(1/10)-1 < 0.
- taxable_negative_real_share_pct = 38.6: 64/166*100 rounded 0.1.
- ira_negative_real_count = 18: IRA annualized real return < 0 (numerically equals y to 1e-16; no y==0 ambiguity affected count).
- median_gap_pctpts = 0.8 (0.80): median of (IRA - taxable annualized)*100, rounded 0.01.
- max_gap_pctpts = 1.13; min_gap_pctpts = 0.39: same gap series.
- worst_taxable_real_pct = -1.18, worst_purchase_month = 2012-11, worst_ira_real_pct = -0.77.
- best_taxable_real_pct = 1.86, best_purchase_month = 2008-11.
- median_end_real_usd_taxable = 10658; median_end_real_usd_ira = 11480: 10000*median real ending value, rounded to dollar.
- inflation_accrual_2022_pct = 7.75: CPI(2022-10)/CPI(2021-10)-1 = 0.0774543.
- tax_2022_usd = 188.89: c=max(FII10 2022-01, 0.125)/100 = 0.00125 (FII10 2022-01 negative); 0.24*10000*(c+a) = 188.8903.
- coupon_cash_2022_usd = 12.5: 10000*c.
- phantom_years = 8: years 2003-2024 with 0.24*10000*(c_Y+a_Y) > 10000*c_Y, a_Y Oct(Y)/Oct(Y-1)-1.
- phantom_years_total = 22: 2003..2024.
Ambiguities: none material. Minor: "rounded to 0.01" applied as half-up on the float value; median of an even-length set taken as mean of the middle two.
