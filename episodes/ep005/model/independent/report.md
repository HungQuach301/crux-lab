# ep005 independent number check

Script: `episodes/ep005/model/independent/check.py` (written from `numbers.md` definitions only; reads `data/raw/*.csv`; did not read `model/*.py`, `out/model.json`, dossier `calc.py`/`result.json`). Run: `python3 episodes/ep005/model/independent/check.py`.

## Result: 55/55 matched (at displayed rounding)

Checked: rate_month_latest, rate_latest (6.862, 4 weeks: 6.71/6.76/6.95/7.03), rate_partial (7.28, 1 week), sched80/78_latest (99/114), calc.py max-month warning (104/119 at 7.28), midpoint_months (180), midpoint_binding_rate_min (12.56; last binding month 1985-05), sched80 min/max over set A (58/132) and set A rate range (2.68–9.64%), nA 403, shareA ≤80 58.6%, ≤75 15.6%, nB 307, medianB 23, minB 13, shareB_over60 14.7%, maxB 112, maxB_start 2005-10, shareB_le_sched80 90.6%, all six fields for each of Nora / Ben / Carla (month, rate, T, schedule, index change to T, LTV at 24), Nora–Carla gap 21 months, mspus_latest 410,700 (2026-04-01), ex_price/loan/payment 2361.94/targets 320,000/312,000 reached at 99/114/extra down 40,000, Case-Shiller robustness (median 23, max 119 from 2006-04, over60 14.7%, shareA ≤80 0.561, ≤75 0.233), crosschecks PMMS vs Optimal Blue 508/508 max gap 0.384 and FHFA vs Case-Shiller m/m 374/426.

## Mismatches

None in the final run. One first-pass mismatch came from reading the definition, not from the numbers:

- `buyer_fast_*`: 10 set-B months tie at T = 13 (2003-06, 2004-01..2004-09). Rule "ties → latest year". At first I read this as "latest tied month", which gives **2004-09** (5.75%, schedule 87, index +11.0%, LTV24 0.763), not numbers.md's **2004-01** (5.71%, 86, +11.2%, 0.725), and a Nora–Carla gap of 13 months instead of 21. Read literally (latest *year* = 2004, then the earliest month in that year), it gives 2004-01, and all fields match. The rule should say "latest year, earliest month within it". The "21 months apart" story depends on that choice.

## Ambiguities in definitions (all resolved to the numbers.md values)

1. Fast-buyer tie rule (above): this is the only one that changes a displayed value.
2. Set B is described as ">120 later index months", but 2016-07 has exactly 120 (HPI ends 2026-07). nB = 307 needs ≥120.
3. Index-LTV search starts at k = 1. "Index change to that month" = H[t+T]/H[t] − 1.
4. `midpoint_binding_rate_min` = the lowest complete-month mean rate with sched78 > 180 (month 1980-08). The continuous threshold is about 12.544%, so the claim is a data minimum, not the threshold.
5. Optimal Blue "7 ngày" read as the mean of OB daily values dated in (d−7, d] for PMMS week d ≥ 2017-01-12. HPI m/m gap measured unrounded with ≤0.5 pp. Both reproduce the counts.
6. ex_price "MSPUS rounded down to a round number" read as floor to $100,000.

## Not computed

- `pmi_premium` (none, by design: no source).
- `midpoint_months` statute reading: taken as 360/2 = 180 (a rule, not data).
- Narrative-only items (names, claim-risk language).
