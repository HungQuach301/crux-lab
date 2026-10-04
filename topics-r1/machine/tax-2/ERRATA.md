# tax-2 errata (dossier standard pass, 04/10/2026)

Sentences are left unchanged in the dossier. Each item below has a `statements.json` entry whose `check` records the expected output.

## E1: unsourced rule number (statement 19, claim-risk.md): APPLIED 2026-10-04 (owner order), `calc.py --statement 19` → True

- **Sentence:** "Single, surviving-spouse (2-year window) and partial-exclusion cases differ."
- **What is wrong:** "2-year" is a rule constant: a surviving spouse keeps the $500,000 limit for a sale within 2 years after the death. No provision in `sources.json` supports it, because `provisions` cites 26 U.S.C. 121(a), 121(b)(1), 121(b)(2)(A), the Pub. L. 105-34 effective-date note and 1014(a)(1) only. Under the V6(a) rule the digit is therefore an orphan. The number is not known to be wrong in law, but nothing in the dossier sources it.
- **Proposed correction (pick one):**
  1. Add the provision for 26 U.S.C. 121(b)(4) (special rule for certain sales by surviving spouses) to `sources.json` → `provisions`, with the quote copied verbatim from the statute page, then add the cite to `sources.json` and to the quantity `surviving_spouse_window_years` in `model.json`, and update check 19 in `calc.py` so it reads the quote; or
  2. Drop the parenthetical: "Single, surviving-spouse and partial-exclusion cases differ."
- **Applied 2026-10-04 by owner order (option 1; sentence unchanged):** `sources.json` → `provisions` now includes `26 U.S.C. 121(b)(4)` (https://www.law.cornell.edu/uscode/text/26/121), with the quote copied verbatim from that page: "... if such sale occurs not later than 2 years after the date of death of such spouse ...". The quote was found on the fetched page (2026-10-04, HTTP 200) after collapsing whitespace and normalizing curly quotes, as `verify/verify.py` `quote_in` does. `model.json` quantity `surviving_spouse_window_years` now has `provision: 26 U.S.C. 121(b)(4)` and the cite is added to `newKindNeeds.inputs.ruleConstants`. Check 19 in `calc.py` now asserts that the quote contains "not later than 2 years after the date of death of such spouse". `statements.json` 19 expects True.

## Note N1 (not a number error; statement 5 stays True): APPLIED 2026-10-04 (owner order)

- **Sentence:** "Gain above the limit is taxed as a long-term capital gain on a sale, while heirs who inherit the home take a basis equal to its value at death."
- The step-up half is sourced to 26 U.S.C. 1014(a)(1). The "long-term capital gain" half (holding period over one year) has no provision in `sources.json`, such as 26 U.S.C. 1222(3). The statement contains no digit, so the number check passes. Proposed fix: add the 1222(3) provision to `sources.json`, or soften the sentence to "Gain above the limit is taxable on a sale".
- **Applied 2026-10-04 by owner order (sentence unchanged):** `sources.json` → `provisions` now includes `26 U.S.C. 1222(3)` (https://www.law.cornell.edu/uscode/text/26/1222), quote verbatim from that page: "means gain from the sale or exchange of a capital asset held for more than 1 year, if and to the extent such gain is taken into account in computing gross income." (found with the same `quote_in` normalization). New `model.json` quantity `long_term_gain_rule` (rule constant) cites it. Statement 5 now `uses` it and `calc.py` asserts the quote; statement 5 gives True.
