# retire-2 V3 recalculation notes
SHA-256: USSTHPI c02d4187... match yes; TB3MS ebf04b1a... match yes (downloaded with requests, default UA).
Method: C(s)=G/P, G=prod over months s..s+n-1 of (1+TB3MS/1200), P=H(s+n)/H(s); starts = every H quarter with H(s+n) present. Rounding: ROUND_HALF_UP on Decimal(repr(x)); no window had |C-1|<1e-4, so C<1 counts are not edge-sensitive.
- starts_10y: count of 10y windows = 166 (1975-01-01 .. 2016-04-01).
- first_start_10y: 1975-01-01.
- last_start_10y: 2016-04-01 (ends 2026-04-01).
- share_gift_buys_less_10y_pct: 100*#(C<1)/166 = 44.6.
- median_coverage_10y_pct: median of 100*C (even count -> mean of two middle values, statistics.median) = 103.9.
- min_coverage_10y_pct: 53.3.
- max_coverage_10y_pct: 148.1.
- starts_since_1990_10y: windows with s>=1990-01-01 = 106.
- share_gift_buys_less_10y_since_1990_pct: 69.8.
- latest_coverage_10y_pct: s=2016-04-01, TB months 2016-04..2026-03 = 64.8.
- starts_20y: 126 (1975-01-01 .. 2006-04-01).
- share_gift_buys_less_20y_pct: 53.2.
- latest_coverage_20y_pct: s=2006-04-01 = 71.6.
- home_price_growth_annual_pct: (H(2026-04-01)/H(1975-01-01))^(4/205)-1 = 4.97.
- tbill_growth_annual_pct: G over 615 months 1975-01..2026-03, ^(4/205) = 4.37.
Ambiguities: none material. Median of an even-count set (166) taken as the mean of the two middle values; picking the lower or upper middle value instead was not checked.
