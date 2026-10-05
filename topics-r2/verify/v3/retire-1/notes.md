# retire-1 V3 recalc notes
Data: all 3 series downloaded from pinned URLs (download.py); SHA-256 matches declared for CUUR0000SEGD03, TB3MS, CPIAUCNS. F and CPIAUCNS have a blank value at 2025-10-01 (no BLS release); TB3MS complete.
- starts_10y = 224: start months s in F with both F(s) and F(s+120) non-missing; 1997-12..2016-08 is 225 months, s=2015-10 dropped because F(2025-10) is blank. Alternative (counting 2015-10 by interpolating) would give 225; literal reading excludes it.
- first_start_10y = 1997-12-01: first element of the start list.
- last_start_10y = 2016-08-01: last element (ends 2026-08-01).
- share_savings_fell_short_10y_pct = 91.5: 100*count(C<1)/224, half-up to 0.1.
- median_coverage_10y_pct = 83.9: statistics.median of 100*C (even n, mean of two middle values; unrounded 83.925), to 0.1.
- min_coverage_10y_pct = 75.2: min 100*C, to 0.1.
- max_coverage_10y_pct = 108.4: max 100*C, to 0.1.
- latest_coverage_10y_pct = 80.3: G over TB3MS 2016-08..2026-07, P = F(2026-08)/F(2016-08).
- starts_5y = 284: same rule, n=60 (1997-12..2021-08 = 285, minus s=2020-10 whose end is blank 2025-10).
- share_savings_fell_short_5y_pct = 88.7: unrounded 88.732.
- starts_15y = 164: n=180 (1997-12..2011-08 = 165, minus s=2010-10).
- share_savings_fell_short_15y_pct = 100.0: all 164 windows C<1.
- funeral_price_growth_annual_pct = 3.31: (F(2026-08)/F(1997-12))^(12/344)-1, to 0.01.
- all_items_price_growth_annual_pct = 2.58: same with CPIAUCNS.
- tbill_growth_annual_pct = 2.15: G over 344 months 1997-12..2026-07, annualized ^(12/344).
- tb3ms_latest_pct = 3.72: TB3MS 2026-08-01 as published.
Rounding: Decimal ROUND_HALF_UP on repr of float. No value was near a rounding boundary.
