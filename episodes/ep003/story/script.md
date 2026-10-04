# Script — Episode 3 (C2 draft v1, WRITER, 2026-10-04)

Working title (C1, A1): *Money You Won't Touch for 20 Years: Savings Bond or T-Bills?*

Format: `Sxx.n | narration | claim IDs | visual note`. Narration is US English for Eric (`eleven_v3`), generated **per scene**. Emotion tags are marked at the start of the line (7 in the episode). No break tags, no "...", no speed.
Character count per scene = narration characters only (tags and line IDs excluded); each scene ≤ ~900.
Dana is an **ILLUSTRATIVE** character (badge on screen whenever she appears; name is taste, C3).
Every result window before May 2005 carries the fixed screen label **"IF today's guarantee had existed"**; the 17 real-guarantee start months are drawn differently (solid, outlined, own label "REAL guarantee").
`NC-n` = number waiting in `needs-claims.md` (not usable until P adds a claim).

---

## S01 — Cold open (Dana, the two paths, the what-if rule, the promise) · ~805 chars

S01.1 | [curious] Dana is in her forties, and she has a chunk of savings she has promised herself she won't touch for 20 years. | viewer_age_decade, horizon_years | Dana (ILLUSTRATIVE badge), kitchen-table moment; a jar/envelope marked "20 years". No numbers yet.
S01.2 | Right now it sits in 3-month Treasury bills, and every time one matures, the money rolls into the next one. | bill_term_months | Money moves into a short bill, bill matures, money hops to the next bill (the "chain of bills" begins; KEY-1).
S01.3 | Then she reads about a US savings bond with a much simpler promise: held for 20 years, it is worth at least double what was paid. | ctx_guarantee, horizon_years | Second path appears: one long bar ending at a gate marked "×2 at year 20".
S01.4 | So which path would have left her better off, the promise or the roll? | — | Two paths side by side; Dana between them. Hold.
S01.5 | One catch before we look back: the doubling promise in its current form only began with bonds issued in May 2005, and earlier bonds had different terms. | ctx_guarantee, guarantee_from, ctx_hypothetical | Timeline 1934 → 2026 slides in; a short solid segment from May 2005 lights up (KEY-2).
S01.6 | So for every year before that, we simply pretend today's promise already existed, and you'll see that marked every time it applies. | ctx_hypothetical | Everything left of May 2005 gets a hatched wash + the fixed label "IF today's guarantee had existed" (this label then stays on every pre-2005 window all episode).
S01.7 | By the end, you'll know how often history let the roll beat double, when it fell short, and where the line sits that your own 20 years would have to clear. | — | Title card A1. "US only" small tag.

## S02 — The two rules · ~795 chars

S02.1 | Start with the bond. | — | The gate path from S01 comes forward.
S02.2 | For bonds issued May to October 2026, a Series EE bond earns a fixed 2.40 percent a year, and the rate for new bonds is reset every May and November. | ctx_ee_rate | Text on screen: "2.40% fixed — for bonds issued May to October 2026" (≥ 40 px). Small calendar ticks May / Nov.
S02.3 | That rate alone would not double the money in 20 years, so at the 20-year mark the Treasury tops it up to at least double. | ctx_ee_rate, ctx_guarantee | Bar grows slowly, falls short of the gate, then a top-up block snaps it to the "×2" gate.
S02.4 | Doubling in 20 years works out to 3.53 percent a year, compounded once a year. | doubling_rate_pct_per_year | Label on the gate: "= 3.53% a year (compounded yearly)".
S02.5 | The double only arrives at 20 years: a bond cashed earlier earns just its fixed rate, and one cashed before five years also gives up 3 months of interest. | ctx_penalty, horizon_years | Gate is only open at year 20; earlier exits drawn as side doors with smaller payoff.
S02.6 | The T-bill side makes no promise past three months. | bill_term_months | The chain of bills: links of different heights, only the first one visible.
S02.7 | Over 20 years the money rolls through 80 bills, each paying whatever rate the market sets at the time. | bills_per_horizon, horizon_months | Chain extends to 80 links; links beyond the first are grey "?" (unknown heights).
S02.8 | In August 2026, the 3-month bill paid 3.72 percent. | tb3ms_latest_pct, tb3ms_latest_month | Only link 1 gets a height: "3.72% · Aug 2026". Not placed next to 3.53 on screen yet.

## S03 — Why today's rate doesn't settle it · ~690 chars

S03.1 | [thoughtful] It's tempting to put that 3.72 next to the bond's 3.53 and call it settled. | tb3ms_latest_pct, doubling_rate_pct_per_year | The two numbers slide toward each other… and a "≠" stamp + note appear: "measured differently" / "one month vs 20 years" (KEY-3). The two numbers are never shown together without this note.
S03.2 | But they aren't measured the same way, and on the scale bill rates are quoted in, the doubling line actually sits a little lower. | — | The 3.53 gate re-expressed on the bill-rate scale: line moves slightly down, no new number here (number comes in S07).
S03.3 | The bigger problem is time: 3.72 is one month's rate, and the roll lives on 80 of them. | bills_per_horizon | Link 1 lit, 79 grey links.
S03.4 | What decides the race is the bill rate across all 20 years, and that is exactly what nobody knows in advance, us included. | horizon_years | Grey links stay grey. No forecast curve drawn.
S03.5 | So instead of guessing, we went back and replayed history. | — | Timeline from S01 returns, pre-2005 hatch + label still on.

## S04 — The replay (one mechanism sentence) · ~630 chars

S04.1 | We took the actual 3-month bill rate for every month since 1934 and started a 20-year roll in each month from January 1934 to September 2006, the last start whose 20 years are complete. | first_start, last_start, horizon_years, latest_window_end | One roll drawn as a chain sliding along the timeline; then it repeats, start month by start month.
S04.2 | That's 873 start months, each one a saver like Dana putting money in and leaving it alone. | starts | Counter "873 start months"; tiny chains stacking. Pre-2005 label on.
S04.3 | They overlap a lot, so together they amount to a few long stretches of history, not 873 separate tries. | starts, nonoverlap_periods | Overlapping chains shown as bands; no number for "few" in voice (4 goes on the method card).
S04.4 | For each one, there's a single question: did the roll end above double? US only, and history, not a forecast. | ctx_hypothetical | Each finished chain becomes one dot dropping onto a horizontal "money multiple" axis with the ×2 gate (new symbol: finish-line swarm). "US only" tag.

## S05 — The answer, and the only real-guarantee starts · ~880 chars

S05.1 | Across all of them, the roll ended above double 52.3 percent of the time, about half. | share_tbills_above_double_pct, starts, ctx_hypothetical | KEY-4. Swarm: all 873 dots, ~half right of the ×2 gate. Big "52.3%" + label "IF today's guarantee had existed".
S05.2 | But for starts from 1950 to 1989 it was 93.1 percent, nearly always, and for starts from 1990 on, just 5.0 percent, almost never. | share_above_double_1950_1989_pct, share_tbills_above_double_starts_since_1990_pct, mid_from, mid_to, since_1990_from | Swarm splits into era rows. Middle row piles right of the gate, bottom row piles left. Numbers on screen next to each row; voice reads these two only.
S05.3 | [surprised] Starts from 1934 to 1949 never got there at all, so "about half" is really separate eras stitched together. | share_above_double_1934_1949_pct, early_from, early_to | Top row (1934–1949) all left of the gate, "0.0%" on screen only.
S05.4 | [serious] Now, the only starts where the promise was real rather than pretend: the 17 months from May 2005 to September 2006. | starts_with_guarantee, guarantee_from, last_start | KEY-5. 17 dots at the end of the bottom row switch from hatched to solid outlined, label "REAL guarantee". "52.3% overall" stays visible in the corner through S05.6.
S05.5 | Not one of those 17 rolls reached double; they ended between 1.378 and 1.388 times the money. | share_above_double_guarantee_starts_pct, min_multiple_guarantee_starts, max_multiple_guarantee_starts | The 17 solid dots sit in a tight cluster left of the gate; "0 of 17" + "1.378–1.388×".
S05.6 | But that is a small sample from a single era, so it shows what happened once, not what a guarantee does in general. | starts_with_guarantee | Tag on the cluster: "small sample · one era". Hold ≥ 1 s.

## S06 — What separated the eras · ~595 chars

S06.1 | What separated those eras was the path bill rates took after each start. | — | Swarm stays; extremes labelled on screen only: best "4.612× · start May 1972", worst "1.129× · start Jan 1934" (claims max/min; screen only, not voiced).
S06.2 | For starts from 1990 on, the average bill rate over the next 20 years ended below the rate in the starting month 87.6 percent of the time. | share_since_1990_avg_below_start_pct, since_1990_from | For one from-1990 start: a starting-month marker, then the 20-year average marker landing below it; repeat quickly across starts; "87.6%" on screen.
S06.3 | In other words, the rate on the day you start has been a poor guide to the twenty years that follow. | — | Link 1 of the chain (S02) next to the 80-link average: they don't match.
S06.4 | That is not a reason to pick either one; it is what history did with these two rules. | — | Counterweight line on screen (≤ 8 words): "Not a pick. What history did." Swarm settles, hold ≥ 1 s.

## S07 — Double is a promise about dollars · ~610 chars

S07.1 | [thoughtful] There's one more thing double never promised: what the money will buy. | — | KEY-6. New symbol "price shadow": the ×2 bar, and behind it a ghost bar = what the original money bought, growing with consumer prices over the same 20 years.
S07.2 | Measured against consumer prices, the doubled amount kept its buying power in 58.7 percent of starts. | share_double_beat_prices_pct, real_windows, ctx_hypothetical | Across the starts, the ×2 bar ends above its shadow in 58.7% (counter on screen), below in the rest. Label "IF today's guarantee had existed".
S07.3 | The worst start, January 1966, ended with a double that bought only 58.0 percent of what the original money had bought. | worst_real_value_double_pct, worst_real_start | Zoom on Jan 1966: the shadow towers over the ×2 bar; "58.0% of the original buying power".
S07.4 | So double is a promise about dollars, not about groceries, and the bill roll lives with the same prices, which this replay doesn't score. | — | Both paths under the same price shadow; small note "bill roll: not scored against prices".

## S08 — The line your own 20 years would have to clear · ~690 chars

S08.1 | [warm] So where would your own 20 years fall? | — | KEY-7. A bill-rate gauge (horizontal scale, bill-rate basis).
S08.2 | Here is the line to measure them against: if the bill rate sat at one level for all 20 years, the roll would need about 3.47 percent just to reach double. | NC-1 (steady_breakeven_tb3ms_pct), horizon_years | Line on the gauge: "≈ 3.47% for 20 years = ×2". (Fallback if NC-1 rejected: see needs-claims.)
S08.3 | Averaged over every month since 1934, the bill rate was 3.42 percent, just under that line, and history sat right on the edge. | mean_tb3ms_all_pct, first_start, tb3ms_latest_month | Marker "3.42% · average since 1934" lands just left of the line.
S08.4 | For money like Dana's, the question isn't today's rate; it's roughly where the bill rate averages over all 80 bills. | bills_per_horizon, NC-2 | The 80-link chain from S02 collapses into one average marker that can land either side of the line (animated both ways, no end side chosen).
S08.5 | Nobody can say where that average will land, and today's rate can't either. | — | Today's 3.72% shown as a single small dot labelled "one month", fading. Not placed against 3.53.
S08.6 | The line doesn't say which to pick; it says what the roll has to do to beat the promise. | — | Counterweight on screen: "What the roll must do. Not a pick."

## S09 — How we know this (method card, V7) · ~150 chars

S09.1 | How the replay was built, and what it leaves out, like taxes and purchase limits, is on screen and in the description. | — | V7 card "How we know this" (≥ 40 px, hold long enough to read): (1) monthly average 3-month bill rate (discount basis) ÷ 12, compounded monthly; (2) taxes ignored: bills taxed federally each year, EE tax-deferred, both state-tax exempt; (3) full 20-year hold, purchase limits ignored; (4) overlapping windows ≈ 4 separate 20-year periods; (5) 6 start months end within 0.5% of double; (6) every start before May 2005 = IF today's guarantee had existed. Source lines: "Federal Reserve Board (H.15) via FRED" · "U.S. Bureau of Labor Statistics via FRED". Claims on card: nonoverlap_periods, near_double_starts, near_double_band_pct, guarantee_from, ctx_hypothetical.

## S10 — Back to Dana · ~690 chars

S10.1 | [warm] Back at Dana's table, the two paths look the same as they did at the start: a promise of double, or a roll with no promise past three months. | ctx_guarantee, bill_term_months | Dana (ILLUSTRATIVE) between the gate path and the chain path, as in S01.
S10.2 | History doesn't choose for her. | — | Hold on Dana; no path highlighted.
S10.3 | What it shows is a roll that beat double about half the time, nearly always for starts from 1950 to 1989 and almost never for starts since 1990, with today's promise imagined for every start before May 2005. | ctx_hypothetical | Recall in words only (no numbers repeated); swarm rows return small behind Dana with the hypothetical label.
S10.4 | It shows that double was a promise about dollars, not about what they buy. | — | Price shadow returns small.
S10.5 | The rest depends on a path of rates that nobody can see yet. US only, and history, not a forecast. | — | Grey future links. "US only · history, not a forecast" on screen.

## S11 — End screen (15–20 s) · ~110 chars

S11.1 | That's the replay. The next one, another question about money and time, is on screen now. | — | End-screen layout (C3/E1-style): next-episode slot + channel slot; music carries the remaining ~12 s. No imperatives.

---

### Counts (computed with the helper at the end of drafting; see beats/summary)
See `beats.md` header for totals.
