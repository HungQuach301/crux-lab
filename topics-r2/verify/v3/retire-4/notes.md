# retire-4 recalculation notes
Data: all 3 pinned FRED CSVs downloaded to data/; SHA-256 matches declared for CUUR0000SETG01, CUUR0000SEHB, TB3MS (yes/yes/yes).
Data gaps: airfare quarterly/semiannual before 1969 (45 blank months incl. 1968-07/08/10/11); both CPI series blank at 2025-10-01 (shutdown). Windows with a blank at s or s+n are excluded (literal "values at s and s+n"); this drops 10y starts 2015-10 and 5y start 2020-10. TB3MS complete.
- air_starts_10y = 588: count of s in airfare series with A(s), A(s+120) present (1963-12..2016-08, gaps excluded).
- air_first_start_10y = 1963-12-01: first such s. Last = 2016-08-01 (asserted).
- air_share_waiting_cost_more_10y_pct = 43.2: 100*count(C<1)/588, half-up to 0.1.
- air_median_coverage_10y_pct = 103.3: median of 100*G/P (even-count median = mean of middle two), rounded 0.1.
- air_latest_coverage_10y_pct = 109.7: s=2016-08, G over 2016-08..2026-07 TB3MS, P=A(2026-08)/A(2016-08). (Not stated in claim text.)
- lodging_starts_10y = 224: 1997-12..2016-08 = 225 months minus 2015-10 (end blank).
- lodging_first_start_10y = 1997-12-01.
- lodging_share_waiting_cost_more_10y_pct = 65.2.
- lodging_median_coverage_10y_pct = 96.6.
- lodging_latest_coverage_10y_pct = 106.1 (not stated in claim text).
- trip_starts_10y = 224: both A and L present at s and s+120.
- trip_first_start_10y = 1997-12-01.
- trip_share_waiting_cost_more_10y_pct = 52.2.
- trip_median_coverage_10y_pct = 99.1.
- trip_latest_coverage_10y_pct = 107.8: P = 0.5*A ratio + 0.5*L ratio.
- trip_starts_5y = 284: 1997-12..2021-08 = 285 minus 2020-10.
- trip_share_waiting_cost_more_5y_pct = 45.1.
- air_price_growth_annual_pct = 1.63: (A(2026-08)/A(1997-12))^(12/344)-1, rounded 0.01.
- lodging_price_growth_annual_pct = 2.38: same for L.
- tbill_growth_annual_pct = 2.15: G over 344 months 1997-12..2026-07.
Ambiguities: (1) "start months" could be read to include interpolated 2025-10 values or early airfare gap months; literal reading excludes them. (2) "every month of the price series" for airfare starts at 1963-12 even though early data are sparse (only non-blank months count). (3) Rounding: half-up decimal on float repr; no tie cases observed to matter.
