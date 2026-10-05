Money you won't touch for 20 years: a Series EE savings bond that the U.S. Treasury tops up to double at year 20, or 3-month Treasury bills rolled over and over? We replayed every 20-year roll of T-bills that history allows, start months from January 1934 to September 2006, and asked one question of each: did the roll end above double?

What the replay shows (history, not a forecast; US only):
- Across all 873 start months, the roll ended above double 52.3% of the time, about half. For starts from 1950 to 1989 it was 93.1%, nearly always; for starts from 1990 on, 5.0%, almost never; starts from 1934 to 1949 never got there.
- The bond's current promise only began with bonds issued in May 2005. For every earlier start, the replay imagines today's promise had existed. The 17 start months with the real promise (May 2005 to September 2006) are a small sample from one era: none of those rolls reached double (1.378 to 1.388 times the money).
- Double is a promise about dollars, not buying power: the doubled amount kept up with consumer prices in 58.7% of starts and fell behind in 41.3%, the last of those starting in January 1981; the worst start, January 1966, ended with a double that bought 58.0% of what the original money had bought.
- The line to clear: for the roll to beat double, the 3-month bill rate has to average about 3.47% a year over all 20 years (the bond's doubling measured the way bill rates are quoted). The average since 1934 was 3.42%.

This is not a recommendation to buy either one; it is what history did with this pair of rules. Nobody knows the bill rate of the next 20 years.

The bond as of October 2026: Series EE bonds issued May to October 2026 earn a fixed 2.40% a year; the rate for new bonds is reset every May and November. The double applies at 20 years to bonds held electronically; a bond cashed before 5 years gives up 3 months of interest.

How we built it:
- Monthly average 3-month bill rate (secondary market, discount basis) from the Federal Reserve Board's H.15 release via FRED (series TB3MS), compounded monthly, through August 2026. Cross-checked against the daily series DTB3 (monthly means match to 0.01 points, 1954 to 2026).
- Buying power: CPI-U, all items, not seasonally adjusted (U.S. Bureau of Labor Statistics via FRED, series CPIAUCNS).
- Taxes ignored: bills are taxed federally each year, EE interest is tax-deferred, and both are exempt from state income tax. Purchase limits ignored. Full 20-year hold.
- The 873 start months overlap, so together they amount to about 4 separate 20-year periods, not 873 independent tries; 6 start months end within 0.5% of double.
- Bond terms: 31 CFR 351.34(a) and 351.35(f)(2); current rate as published by TreasuryDirect.

Chapters
{scene:S01} The question
{scene:S02} The bond's promise
{scene:S03} Rolling T-bills
{scene:S04} Replaying every start month
{scene:S06} Why the eras differ
{scene:S07} What double buys
{scene:S08} The line to clear
{scene:S09} How we built it, and what it shows
