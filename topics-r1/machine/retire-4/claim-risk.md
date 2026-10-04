# retire-4 claim risk: savings bonds that double in 20 years vs rolling T-bills

Every sentence with a number below has an entry in `statements.json` (`calc.py --statement N` → True).

Analyst's guess before running the data: rolling T-bills would beat double in most 20-year windows, because the average bill rate since 1934 (3.42%) sits near the 3.53% doubling rate. Actual: 52.3% overall, but only 5.0% of starts from 1990 on.

## The guarantee is hypothetical before May 2005 (must be said in words and on screen from the first result)
- Today's doubling-in-20-years terms apply to bonds issued from May 2005 on; earlier bonds had other terms, so every earlier start is hypothetical ('if this guarantee had existed then').
- Do not say "there was no guarantee before 2005" (earlier EE bonds had other guaranteed terms) or "savings bonds have beaten T-bills since 1990" (most of those starts are hypothetical).
- The only real (non-hypothetical) starts are May 2005 to Sep 2006 (`ans-6`): a small, single-era sample, not a separate proof.

## Phrasings that overstate the claim
- "T-bills will fall short" or "rates will drop": the result depends on the path of rates, which the episode does not forecast.
- "Doubling protects you from inflation." Double kept up with consumer prices in only 58.7% of starts.
- Comparing today's 3.72% T-bill rate directly with the 3.53% doubling rate as if it settles the question.

## The episode must not
- Recommend buying savings bonds or T-bills, or name brokers.
- Predict short-term rates or inflation over the next 20 years.

## Data limits
- Monthly average 3-month bill rate (discount basis) divided by 12, compounded monthly: an approximation of a bill roll.
- 6 start months end within 0.5% of double, so the shares can shift by a start or two under another bill-rate convention.
- Taxes ignored (bills taxed yearly at the federal level; savings bonds tax-deferred; both state-tax exempt), purchase limits ignored, full 20-year hold assumed (early redemption earns only the stated rate).
- The data from 1934 to 2026 hold only 4 separate 20-year periods; the 873 overlapping windows are not 873 independent results. History, not a forecast.
