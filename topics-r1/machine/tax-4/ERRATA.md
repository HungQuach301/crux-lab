# tax-4 errata (topic-dossier standard, 04/10/2026)

Sentences are NOT edited in place. Each entry: sentence, what is wrong, proposed correction. The matching
`statements.json` entry carries `"expected": false` and `calc.py --statement N` prints `False` until the owner
accepts a correction.

## E1 — claim-risk.md, statement 21 (`calc.py --statement 21 → False`)

**Sentence:** "The general rule is an extra 5 dollars an hour at the 22% bracket with a 1.5x overtime rate."

**What is wrong (scope):** the 5 is `breakeven_markup_usd` = `side_breakeven_rate_usd` − `ot_rate_usd`
= 53.00 − 48 = 5.00, which belongs to the $32 modeled worker only. It is not a general rule at the 22% bracket:
the markup is premium × 22% ÷ (1 − 7.65% − 22%) per hour = 0.5W × 0.22 / 0.7035 ≈ 0.156 × W (≈ 10.4% of
the overtime rate). Another 22%-bracket worker at W = $40 (all extra pay still in the 22% bracket) needs about
$6.25 an hour more, not $5 (`calc.py` claim `markup_is_general_at_22pct` fails). Same error class as debt-2 /
lessons M3v2: a number from one object (this example) presented with a wider scope (all 22% workers).

**Proposed correction:** "For this example the side job must pay about $5 an hour more than the overtime rate.
The general rule at the 22% bracket with a 1.5x overtime rate is about a tenth more than the overtime rate
(premium x 22% / (1 - 7.65% - 22%) per hour)."
(If adopted, "a tenth" and the rule constants need quantities: add `breakeven_markup_share_of_ot_rate_pct`
= 100 × markup / ot_rate (10.42 here) under `--statement`, and `EMPLOYEE_PAYROLL_PCT` = 7.65 with cites
26 U.S.C. 3101(a), 3101(b)(1).)

## Advisory (number checks True; wording scope, not counted as an erratum)

- **A1 — result.json answer, statement 5** ("the typical production/nonsupervisory wage, $32.38 in June
  2026"): `ahe_latest` is defined as AVERAGE hourly earnings (AHETPI), and claim-risk.md says "national average".
  "Typical" can be read as median. Suggest "the average production/nonsupervisory wage". The calc.py docstring
  uses the same word.
- **A2 — result.json limits, statement 33** ("tax years 2025-2028"): 2028 is backed by 26 U.S.C. 225(g) in
  sources.json; 2025 is a year (V6a exemption) but no provision quote in sources.json states the first year.
  Suggest adding the effective-date provision of the enacting law to sources.json.
