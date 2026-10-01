# tax-2 V3 recalculation notes

All 14 downloaded files match declared SHA-256 (data/sha.json). Rounding: Decimal half-up. CPIAUCNS has a blank 2025-10-01 value (skipped; not used).

- growth_los_angeles = 4.3004: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_los_angeles_usd = 151500: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- growth_san_diego = 4.0404: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_san_diego_usd = 164500: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- growth_san_francisco = 2.9305: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_san_francisco_usd = 259000: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- growth_san_jose = 2.9652: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_san_jose_usd = 254400: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- growth_seattle = 3.7779: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_seattle_usd = 180000: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- growth_boston = 3.2089: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_boston_usd = 226400: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- growth_new_york = 3.3558: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_new_york_usd = 212200: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- growth_miami = 5.3601: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_miami_usd = 114700: miami of 12 unrounded metro thresholds, rounded to $100; SHA match yes; no ambiguity
- growth_denver = 3.1961: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_denver_usd = 227700: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- growth_phoenix = 3.7903: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_phoenix_usd = 179200: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- growth_dallas = 3.3189: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_dallas_usd = 215600: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- growth_chicago = 2.3392: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_chicago_usd = 373400: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- growth_us = 3.0536: index(2026-04-01) / mean(2000 Q1-Q4 index values), rounded 4dp; SHA match yes; no ambiguity
- threshold_joint_us_usd = 243500: 500000/(g-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- threshold_single_us_usd = 121700: 250000/(g_us-1), unrounded g, rounded to $100; SHA match yes; no ambiguity
- threshold_joint_min_usd = 114700: min of 12 unrounded metro thresholds, rounded to $100; SHA match yes; no ambiguity
- threshold_joint_max_usd = 373400: max of 12 unrounded metro thresholds, rounded to $100; SHA match yes; no ambiguity
- metros_threshold_under_200k = 5: count of 12 unrounded metro thresholds strictly below cutoff (Seattle 179,991 and Phoenix 179,192 near-ish but clearly below 200k); SHA match yes; no ambiguity
- metros_threshold_under_300k = 11: count of 12 unrounded metro thresholds strictly below cutoff (Seattle 179,991 and Phoenix 179,192 near-ish but clearly below 200k); SHA match yes; no ambiguity
- cpi_1997_05 = 160.1: read directly from CPIAUCNS.csv; SHA match yes; no ambiguity
- cpi_2026_08 = 334.98: read directly from CPIAUCNS.csv; SHA match yes; no ambiguity
- excl_joint_1997_in_2026_usd = 1046000: 500000*334.980/160.100 = 1,046,159.28, rounded to $1,000; SHA match yes; no ambiguity
