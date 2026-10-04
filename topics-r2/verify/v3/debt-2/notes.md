# debt-2 V3 recalculation notes
SHA-256: HPIPONM226N.csv and MORTGAGE30US.csv both match declared sha256 (downloaded via requests, default UA).
- rate_month_latest: latest calendar month with weekly MORTGAGE30US obs = 2026-09 (weeks 09-04/11/18/24: 6.71, 6.76, 6.95, 7.03).
- rate_latest: exact mean = 6.8625 (a rounding tie). Rounded half-up -> 6.863 (reported). Alternative: half-even / Python float round() -> 6.862 (the claim's value). Schedule results identical either way.
- sched80_months_latest: first k in 0..360 with B_k <= 0.80 at unrounded rate 6.8625 -> 99 (same at 6.862/6.863).
- sched78_months_latest: first k with B_k <= 0.78 -> 114 (same at 6.862/6.863).
- nA / firstA / lastA: HPI months 1991-01..2024-07 -> 403, 1991-01, 2024-07.
- shareA_ltv24_le75: share of set A with B_24/(HPI[m+24]/HPI[m]) <= 0.75, round 0.001 -> 0.156.
- shareA_ltv24_le80: same with <= 0.80 -> 0.586.
- nB / firstB / lastB: months 1991-01..2016-07 -> 307, 1991-01, 2016-07.
- medianB_months_to80: first k>=0 with index LTV <= 0.80, searched through last HPI obs (2026-07); all 307 reached it; median (odd n) -> 23.
- shareB_over60: share with first k > 60 -> 0.147.
- maxB_months_to80: 112.
- maxB_start: 2005-10. Ambiguity: tie, 2005-11 also has 112; reported earliest.
- shareB_le_sched80: share where index first k <= scheduled 80% month at that purchase month's unrounded monthly rate -> 0.906.
Monthly rates use unrounded means of weekly values throughout.
