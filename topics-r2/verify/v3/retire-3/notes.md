# retire-3 V3 recalculation notes
Data: GS1, GS2, GS3, GS5 downloaded from pinned FRED URLs (download.py); SHA-256 matches the declared value for all 4 files.
Method (recalc.py): yields parsed as exact Decimals; call test r - y >= threshold done in exact decimal arithmetic (a float comparison gives identical call decisions, 0 differences at both thresholds); values/d computed in float; rounding half-up on the reported precision.
- starts = 821: GS5 months from 1953-04 with s+60 months <= 2026-08.
- first_start = "1953-04-01" (categorical date string).
- last_start = "2021-08-01" (categorical date string).
- share_called_pct = 73.2: 601/821 called at some anniversary k=1..4 with threshold 0.25.
- share_callable_ahead_pct = 37.9: 311/821 with d > 0 (no starts have d == 0 exactly).
- median_diff_pts_per_year = -0.22 (raw -0.2206); 821 is odd, so median is a single observation.
- mean_diff_pts_per_year = -0.34 (raw -0.3401).
- worst_diff_pts_per_year = -3.77 (raw -3.7720).
- best_diff_pts_per_year = 0.50 (raw 0.5000, a never-called start; d for never-called is slightly below/at 0.50 depending on r, max rounds to 0.50).
- share_ahead_when_called_pct = 15.1: called starts with d > 0 / 601 called starts.
- starts_since_2000 = 260 (2000-01 .. 2021-08).
- share_called_since_2000_pct = 80.8.
- share_callable_ahead_since_2000_pct = 30.8.
- share_called_thresh050_pct = 66.6: same model, call rule r - y >= 0.50. Ambiguity: the generic model text says 0.25; the number's specific definition (0.50) was followed.
- share_callable_ahead_thresh050_pct = 41.8: d > 0 under the 0.50 call rule.
- gs5_latest_pct = 4.38: GS5 at 2026-08-01 as published.
Ambiguities: GS2 fallback ((GS1+GS3)/2) applied whenever GS2 lacks a value for month t (only before 1976-06); signs of median/mean/worst kept negative as d is defined (claim text phrases them as "less").
