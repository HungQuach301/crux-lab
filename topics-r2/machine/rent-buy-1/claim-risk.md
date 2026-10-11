# rent-buy-1 claim risk

Every sentence with a number below is a statement in `statements.json` (checked by `calc.py --statement N`).

**Phrasings that would overstate the claim**
- "Buying always wins" or "renting is throwing money away." No: statement 7 (the renter came out ahead in 75 of 307 10-year windows) and statement 2 (June 2006 start, buyer $82,385 behind).
- "Buying wins three times out of four." Only with the assumed starting rent; statement 6 shows the share moving with that assumption and with T-bill interest on the renter's savings.
- "Your home will do what the index did." Statement 10: The home is the national FHFA index, not one house: in the worst window the national index rose 3.2%; a single home or city can do much better or worse.
- "Today looks like 2006, so renters will win." Statement 9 compares only the first-month cash gap; it is not a forecast and the replay cannot say how a 2026 start ends.

**What the episode must not say**
- No advice ("buy now", "keep renting"). Show both characters and the spread of outcomes; end with a question.
- No forecast of prices, rents or rates. Statement 11: History, not a forecast: the last window used ends in July 2026, the last month of the price index.
- The two people are ILLUSTRATIVE, not real households.

**Data limits**
- Starting rent level is an assumption (5% of price a year at July 2026), carried back by CPI rent / house price index; CPI rent follows sitting tenants and lags asking rents.
- Owner costs, closing and selling costs are fixed shares; no taxes (interest deduction, capital-gains exclusion), refinancing, moving costs or renter's insurance.
- The renter's savings sit in cash (or T-bills in a variant), never stocks: the "invest the difference" question is not answered.
- CPI rent for October 2025 was not published; filled with the geometric mean of the neighbouring months.
