# tax-2 V3 recalculation notes
Data: TERMCBCCINTNS.csv downloaded from pinned URL; SHA-256 bb3976b1...81bf61 MATCHES declared. CSV is monthly-indexed with blanks; non-empty rows (Feb/May/Aug/Nov only) used.
- observations: count of non-empty values = 127.
- first_obs: 1994-11 (first non-empty date). last_obs: 2026-05.
- apr_last_pct: 22.15 (2026-05 value).
- tax_12_usd: 0.12*1000 = 120. tax_22_usd: 0.22*1000 = 220.
- months_12_last: smallest n with interest > 120 at 22.15% = 12 (n=12 interest 123.999). months_22_last: 22.
- interest_12mo_last_usd: 123.999... -> 124.00 (half-up to cents). interest_24mo_last_usd: 246.85. interest_6mo_last_usd: 65.59.
- apr_min_pct / apr_min_obs: 11.96 at 2003-02 (unique, no ties). months_12_at_min: 23.
- apr_max_pct / apr_max_obs: 23.37 at 2024-08 (unique). months_12_at_max: 11.
- months_12_median: 18; months_22_median: 33 (127 obs, odd count, so median is an actual observation; no averaging ambiguity).
- months_12_min/max: 11 / 23. months_22_min/max: 21 / 41.
Ambiguities: month formatted as YYYY-MM (could be YYYY-MM-01); strict ">" used for "exceed" (no exact equality occurred, interest at n=12 is 123.999 not 120). No other ambiguity.
