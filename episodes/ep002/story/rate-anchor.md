# Rate anchor for the "7.50% variable / 9.00% fixed" pair (ep002)

Researched 2026-10-01. Scenario: $50,000 private graduate loan, 10-year repayment.

**Access caveat (read this first).** The egress proxy blocked every lender domain (sofi.com, salliemae.com,
earnest.com, collegeave.com, citizensbank.com, ascentfunding.com, elfi.com) and every aggregator tried
(credible.com, nerdwallet.com, bankrate.com, cnbc.com, money.com, lendedu.com, thecollegeinvestor.com,
savingforcollege.com, studentchoice.org, umass.edu). Only consumerfinance.gov loaded.
So almost every lender number below is **via search snippet only**. The search engine wrote those snippets
from pages it had indexed, and some of them disagree with each other. Before anything goes on screen,
someone has to open each page in a browser and check it.
Tags: [READ] = read directly; [SNIPPET] = via search snippet only; UNKNOWN = not found.

---

## Option A: anchor to dated, published lender tables

### A1. Lender graduate-loan rate tables (all [SNIPPET] unless marked)

| Lender | Fixed APR (grad) | Variable APR (grad) | "As of" | Index | Variable cap | Margin rule | URL |
|---|---|---|---|---|---|---|---|
| Sallie Mae | 2.08%-14.99% | 3.75%-14.48% | "As of July 2026" (variable figure) | 30-day avg SOFR | "will never exceed 25.000%" | "margin between 0.250% and 10.125%" + SOFR, rounded up to 1/8% (from a LASD PDF, date UNKNOWN) | salliemae.com/student-loans/graduate-student-loans/graduate-school-loan/ ; salliemae.com/content/dam/slm/writtencontent/termsandconditions/SOSL-LASD-Degree-Grad-SMB.pdf |
| SoFi | 2.45%-14.83% (another snippet: 2.99%-14.83%) | 4.39%-15.86% (another: 4.64%-15.86%) | "current as of 8/25/2026" | 30-day avg SOFR | "will never exceed 17.95%" (from an UNDERGRAD variable ASD; grad cap UNKNOWN) | "margin between 4.64% and 16.24%" (same undergrad doc) | sofi.com/private-student-loans/graduate-student-loans/ ; sofi.com/public-doc-proxy/api/in-school/asd/UNDERGRAD_VARIABLE_LTHT |
| Earnest | from 2.79% | from 4.99% | UNKNOWN | 30-day avg SOFR (snippet quoted refinance wording) | Snippet says 8.95% (term ≤10y) / 9.95% / 11.95%. **Doubtful**: probably the refinance product or old text. Do not use. | UNKNOWN | earnest.com/student-loans/graduate |
| College Ave | 1.97%-17.99% | 3.89%-17.99% (one snippet gives grad variable 4.24%-14.49%) | "as of August 2026" (not clearly grad-specific) | UNKNOWN | UNKNOWN | UNKNOWN | collegeave.com/graduate-student-loans/ |
| Citizens | 4.24%-14.10% | 5.99%-15.10% | "September 2026" (attributed by the snippet, not seen on the page) | 30-day avg SOFR, rounded up to 1/8% | "greater of 21.00% or Prime Rate plus 9.00%" | UNKNOWN | citizensbank.com (disclosure PDF; see search result) |
| Ascent | 6.75%-15.81% (snippet looks garbled) | 4.64%-15.99% / "3.60%-16.01%" (conflicting) | UNKNOWN | 30-day avg SOFR | "capped at 17.95%" (may be confused with SoFi) | UNKNOWN | ascentfunding.com/grad-school-funding-calculator/ |
| ELFI | from 2.99% | from 6.75% | "current as of 7/7/26" | UNKNOWN | "will never exceed 18%" (term-specific; product unclear) | UNKNOWN | elfi.com/student-loans/graduate-school-loans/ |
| Navient | UNKNOWN (not searched successfully) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

Short verbatim quotes, as the search snippets gave them [SNIPPET]. The exact page wording is unverified:
- Sallie Mae: "Although the rate will vary after you are approved, it will never exceed 25.000% (the maximum allowable for this loan)."
- SoFi: "The interest rate will never exceed 17.95% (the maximum allowable for this loan)."
- Citizens: "the maximum rate on the Student Loan is the greater of 21.00% or Prime Rate plus 9.00%."
- ELFI: "Interest rates are current as of 7/7/26 and may be different based on the term of your loan..."

### A2. Neutral/aggregate sources
- **Credible marketplace** [SNIPPET]: "Average 10-year fixed private loan: 8.20% and average 5-year variable private loan: 6.84%".
  The date, the population (grad or all) and the credit tier are all UNKNOWN. The terms also differ (10-year fixed vs
  5-year variable), so this is not a like-for-like gap. A second snippet gives Credible figures of 14.59% (10-yr fixed)
  and 17.78% (5-yr variable) for the 600-639 credit band, from "prequalified borrowers ... in July 2026".
  URL: credible.com/student-loans/apr-trends (blocked).
- Credible marketplace ranges [SNIPPET]: "fixed-rate APRs currently range from 1.94% to 17.99%, and variable-rate loans
  range from 3.5% to 17.99%." URL: credible.com/student-loans
- CFPB: no 2026 average rates found. Reg Z §1026.47 [READ] requires disclosure of "any limitations on the
  interest rate adjustments, or lack thereof" (§1026.47(a)(1)(iii)). It also requires that variable-rate ranges "reflect the
  rate or rates calculated based on the index and margin" (comment 47(a)(1)(i)-3). https://www.consumerfinance.gov/rules-policy/regulations/1026/47/
- Federal Reserve: no private-student-loan fixed/variable average series found (UNKNOWN).
- Context [SNIPPET]: federal 2026-27 graduate Direct Unsubsidized 8.07% fixed and Direct PLUS 9.07% fixed.
  A 9% fixed figure sits next to the federal PLUS rate, and viewers may connect the two.

### A3. Is 7.5% variable / 9% fixed a typical published pair?
- **Not in the published lender ranges.** In every 2026 grad table seen via snippet, the fixed range *starts below*
  the variable range. Fixed-minus-variable gaps, computed from the snippet figures (my arithmetic):

| Lender | Gap at minimums | Gap at midpoints |
|---|---|---|
| Sallie Mae | -1.67 pt | -0.58 pt |
| SoFi | -1.94 pt | -1.49 pt |
| Citizens | -1.75 pt | -1.38 pt |
| College Ave | -1.92 pt | -0.96 pt |
| Earnest | -2.20 pt | n/a |
| ELFI | -3.76 pt | n/a |

  So the typical 2026 table gap is about **-1 to -2 points** (fixed *lower*). That is the reverse of +1.5.
- **Only one source points the other way**: the Credible averages (8.20% fixed 10-yr vs 6.84% variable 5-yr = +1.36 pt).
  Its date, population and credit tier are UNKNOWN and its terms differ, so it is a weak anchor.
- Both 7.5% and 9.0% fall inside every lender's range, so each figure is *possible* on its own for a mid-credit
  borrower. Nothing published presents them as a pair, though.
- Conclusion: **no dated published source was found where 7.5% variable / 9% fixed is shown as a typical pair.**

### A4. Rights and brand use
- Sallie Mae Terms of Use [SNIPPET]: "You may not copy, reproduce, distribute, display, ... publish, ... or otherwise
  use the Content for public or commercial purposes without express authorization." (salliemae.com/legal/terms/partners)
- SoFi Terms of Use [SNIPPET]: "for your personal private non-commercial use only. You may not modify, republish,
  post or transmit anything you obtain from this website unless you first obtain consent of SoFi."
  (sofi.com/terms-of-use/)
- The other lenders' terms: UNKNOWN. No explicit permission to quote rate figures in a video was found.
  A bare rate number is a fact. Copyright likely does not protect it, but whether it does is a legal question that is
  UNKNOWN here and is not legal advice. Restating one figure with attribution differs from reproducing the page.
- The channel shows no third-party logos or brands. Even a text-only citation ("Lender X, as of date") names
  a brand, so Option A would need an exception to that rule or an unnamed "published lender range" wording.

---

## Option B: label the pair ILLUSTRATIVE

On-screen tag: "Illustrative rates, not a quote or offer".

Draft narration (descriptive only, no advice and no forecast):
> "These are an illustrative pair of offers: a variable rate that starts at 7.5 percent, and a fixed rate of 9 percent, on the same $50,000 ten-year loan."

Optional context line, drawn only from published facts. It needs verification before use:
> "In published 2026 lender ranges, both figures sit inside the advertised spread for graduate loans."

---

## Variable-rate caps (for the 12/15/18% cap grid)

| Source | Cap | Status |
|---|---|---|
| Sallie Mae grad LASD | 25.000% | [SNIPPET] |
| Citizens student loan ASD | greater of 21.00% or Prime + 9.00% | [SNIPPET] |
| ELFI | 18% | [SNIPPET] |
| SoFi (undergrad variable ASD) | 17.95% | [SNIPPET] |
| Ascent | 17.95% | [SNIPPET, possibly conflated with SoFi] |
| Earnest | 8.95% / 9.95% / 11.95% by term | [SNIPPET, likely refinance or old; unreliable] |
| Generic article statement | "often falling between 18% and 25%" | [SNIPPET] |
| Reg Z §1026.47(a)(1)(iii) | lender must disclose limits "or lack thereof" | [READ] |

Implication for the grid: 18% matches the low end of published in-school caps. 12% and 15% sit *below* every
in-school cap found, so the video should present them as hypothetical sensitivity cases, not as real caps.
An optional 25% row would match the highest published cap found (Sallie Mae).

## To verify before publishing (in a browser, not here)
1. The exact grad fixed and variable ranges and "as of" dates on each lender page (the snippets conflict for SoFi, Ascent and College Ave).
2. The source and date of the Credible "8.20% / 6.84%" averages.
3. Earnest's and Ascent's actual in-school caps.
4. The terms-of-use clauses on each site, read in full.
