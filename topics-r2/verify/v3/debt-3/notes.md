# debt-3 recalculation notes
Data: data/AHETPI.csv downloaded from pinned URL; SHA-256 bf666fc3...e1ca7a matches declared. 752 monthly obs 1964-01..2026-08, contiguous, no missing values. Exact Decimal arithmetic for the W[t+k] >= 1.25*W[t] test (avoids float edge cases). Dates reported as YYYY-MM.
- n_starts = 691: count of start months t with some k>=0 such that W[t+k] >= 1.25*W[t].
- first_start = 1964-01: earliest such start month.
- last_start = 2021-07: latest such start month.
- median_months = 82: statistics.median of k(t) over all 691 starts (odd count, no averaging).
- min_months = 34: min k(t).
- min_start = 1977-12: first start month attaining min k(t).
- max_months = 120: max k(t). Note: late starts are right-censored (dropped if not yet reached), so max/median are over completed spells only, per definition.
- share_le48 = 0.237: count(k<=48)/691, rounded half-up to 0.001.
- n_starts_1990 = 379: starts from 1990-01 with k defined.
- median_months_1990 = 86: median k over those 379 (odd count).
- min_months_1990 = 52: min k over those.
- share_le48_1990 = 0.0: no 1990+ start has k<=48.
- median_share_after60_1990 = 30.0: median of 35*W[t]/W[t+60] over 1990-01+ starts with t+60 in data (raw 29.9954), rounded to 0.1. Ambiguity: definition does not restrict this set to starts with k(t) defined; literal reading uses all starts with data 60 months later (does not require k defined).
- n_share5_1990 = 380: starts 1990-01..2021-08 (t+60 <= 2026-08).
