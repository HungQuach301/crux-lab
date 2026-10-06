# Script — Episode 4 (C2 round 2 (+ V7 fallback S18.3, P1), WRITER, 2026-10-05)

Working title: *Bought Your Home in 2000? The $500,000 Tax-Free Limit May Not Cover It*

Format: `Sxx.n | narration | claim IDs (or —) | visual note`. Narration is US English for Eric (`eleven_v3`), generated **per scene** (each scene ≤ ~900 narration characters). Emotion tags sit at the start of the line (**6** in the episode, key beats only). No break tags, no "...", no speed. Holds written as *(hold n s)* in the visual note are silence in the edit, not narration.
S01 is hook **H2** ("Cú sốc con số", `[stake]`), chosen by the round-robin pair test (5/6, `hook-rr/RESULT.md`); H1/H3 stay in `hooks.md`. Round 2 (C2-blind): anti-advice counterweight tightened in S15.5/S17.4; "like … average" once per scene; S14 numbers moved to screen; S08 gets a why-it-matters line; S18 rules merged.

**Characters.** Rosa and Frank are an **ILLUSTRATIVE** couple (badge on screen whenever they or their numbers appear; names are taste, C3). The $200,000 and $300,000 purchase prices are ILLUSTRATIVE (claim-risk); every visual note that carries them says so. Every gain, crossing quarter, threshold or metro count is said for a home rising **"like … average"** (round 2: once per scene that states a threshold, gain, crossing quarter or metro count; other sentences drop the phrase), never for a specific house, and never turned into a tax bill.

**Counterweight against advice (C1 blind signal, 5/6 readers drew "check your taxes / see a tax pro before selling"):** said right after the promise (S02.1), after the Act 1 result (S07.4), at the answer (S15.5: "The video measures one line; it says nothing about what anyone does next.") and in the limits (S17.1, S17.4): a line for an average-like home, not anyone's tax bill, not a reason to sell or keep; the video does not say what anyone should do. No imperative, no "professional" as a next step anywhere.

**Fixed forms (said once at the claim, later recalled in words only):**
- the cap: "$500,000" (joint) · "$250,000" (single)
- "almost 3.8 times" (Phoenix growth, claim 3.7903); Miami "×5.4" and Chicago "×2.3" appear on screen only
- "about $558,100" (Phoenix gain at $200,000) · "about $1,046,000 in August 2026 dollars" (1997 cap in consumer prices)
- "about $179,200" (Phoenix threshold) · "about $114,700" (Miami) · "about $373,400" (Chicago) · "about $243,500" (national) · "about $121,700" (national, single)
- "5 of them" ($200,000 crossed) · "11 of the 12" ($300,000 crossed) · "every city except Chicago" (threshold under $300,000; words, not a count)
- quarters always "the second quarter of 2022" (no "Q2"); end point always "the second quarter of 2026"

**Number density convention:** a "new number" is any figure not said earlier (dollar amounts, ratios, counts, years/quarters). Max 2 new per scene, ≥ ~8 s apart; each decisive number gets a ≥ 1 s hold.

**Claim not yet in `numbers.md`:** `metro_count` = 12 (said in S09.1, S10.2, S14.1; marked `metro_count` in the claim column). Everything else maps to an existing claim ID.

**Counts:** after the P1 V7 fallback (S18.3 removed) narration **1,121 words**, runtime ≈ 9:13 est. (round-2 WRITER counter before fallback: 1,149 words (≈ 1,262 read out), 75 lines, 19 scenes. Speech ≈ 9:00 + holds 22.4 s → **runtime ≈ 9:23** before the end screen (≈ 9:40 with it). `check_script.py`: ĐẠT (its own estimate ~8.7 min uses no holds).

**Mid-rolls (for `episode.yaml` → `midrolls`, est.):**
- **MR1 ≈ 3:29**, end of Act 1, inside the 1.5 s hold after S07.6 (question "Is Phoenix unusual?" left open).
- **MR2 ≈ 6:41**, end of Act 2, inside the 1.5 s hold after S14.5 (the cap "read a third way").
Both at act boundaries, in a hold ≥ 1 s, after 2:00 and before the last two minutes (start ≈ 7:23).

**Time-share vs `lab` template (story.md §4, reference):**

| Part | Scenes | Est. time | Share | Template | Δ (pts) |
|---|---|---|---|---|---|
| Hook + promise + constraints | S01–S02 | 0:00–0:56 (56 s) | 9.9 % | 8 % (≤ 0:50) | +1.9 (ends 0:56, past the 0:50 guide: the anti-advice counterweight S02.1 sits here) |
| Context + characters | S03–S05 | 0:56–2:14 (78 s) | 13.9 % | 15 % | −1.1 |
| Journey (replay on real data) | S06–S14 | 2:14–6:41 (267 s) | 47.4 % | 45 % | +2.4 |
| Answer + viewer threshold | S15–S17 | 6:41–8:34 (113 s) | 20.1 % | 20 % | +0.1 |
| Limits + method card + outro | S18–S19 | 8:34–9:23 (49 s) | 8.7 % | 12 % | −3.3 |

No part off by more than ±5 points.

**Act questions / turns:**
- Act 1 (S01–S07): *Has Rosa and Frank's gain passed the cap?* Turn: the flat line stands still while their gain line climbs over it (KEY-2).
- Act 2 (S08–S14): *Is Phoenix unusual, and what 2000 price does it take elsewhere?* Turn: flip from "when" to "what price" — the ladder (KEY-6).
- Act 3 (S15–S19): answers the cold-open question with the same words ("fully tax-free") and the same street and flat line, then the limits.
- Core number (the $500,000 cap) returns with new meaning: fact (S01/S03) → comparison, flat vs consumer prices (S08) → a 2000 price the viewer can look up (S14.6), recalled in words only.

---

## S01 — Hook H2: a paper gain bigger than the tax-free cap · 335 chars, 60 words

S01.1 | [serious] About $558,100 in paper profit, more than a couple can take tax-free. | gain_at_200k_phoenix, excl_joint_limit_usd, illustrative_price_200k_usd | `[stake]` KEY-1. Black screen; the number "≈ $558,100 gain (on paper)" builds digit by digit, ILLUSTRATIVE badge beside it; then a flat line slides in just under it, label "tax-free cap". Purchase price ILLUSTRATIVE ($200,000, shown small under the number).
S01.2 | That's Rosa and Frank, an illustrative Phoenix couple who bought in 2000, if their home rose like the average. | buy_year, gain_at_200k_phoenix, growth_phoenix, illustrative_price_200k_usd | Pull back: the number sits at the end of a gain line rising from "2000"; the couple and house appear (ILLUSTRATIVE badge; tag "$200,000 · 2000", ILLUSTRATIVE).
S01.3 | You'll know, city by city, the 2000 price where a home that rose like its metro area's average passes that cap, to check yours against. | buy_year, threshold_joint_min, threshold_joint_max | Title card. Behind it, a ghost of the ladder (KEY-6) with 12 unlabeled rungs and an empty slot marked "your 2000 price". Small tag "US only".

## S02 — Constraints, right after the promise · 332 chars, 64 words

S02.1 | It's a line for a home like the average: not anyone's tax bill, and not a reason to sell or keep. | — | Under the ghost ladder, one line of text: "a line, not a tax bill · not a reason to sell or keep".
S02.2 | This is US only: federal tax, with state taxes not modeled. | ctx_us_only | Tag "US federal tax only · state tax not modeled".
S02.3 | Every couple here is illustrative, and assumed to have owned and lived in the home two of the five years before selling. | ownership_use_test | ILLUSTRATIVE badge pulses on the couple. Chip: "Owned and lived in it 2 of the last 5 years (assumed)".
S02.4 | And every price you'll see is history, not a forecast. | ctx_history | Tag "History, not a forecast" settles in the corner. *(hold 0.8 s)*

## S03 — What the cap is a cap on · 339 chars, 62 words

S03.1 | When you sell, your gain is the sale price, less what you paid, and less what you spent improving the place. | — | Three blocks: tall "sale price" bar; "what you paid" block and "improvements" block lift off it; what remains glows as "gain". No numbers.
S03.2 | A married couple filing jointly can leave up to $500,000 of that gain off their taxes, and a single seller can leave out $250,000. | excl_joint_limit_usd, excl_single_limit_usd | The cap line drops onto the gain block at "$500,000 · married, joint"; a second, lower dashed tick "$250,000 · single" (`ink-muted`, thinner).
S03.3 | Those caps took effect in May 1997. | exclusion_effective_month | Time axis appears under the line, starting "May 1997". *(hold 1 s)*
S03.4 | They are plain dollar amounts, and they haven't changed since. | excl_joint_limit_usd, exclusion_effective_month | The line draws left to right along the axis, perfectly flat, to the right edge. No end label yet.

## S04 — Rosa and Frank, and the sentence Frank always says · 279 chars, 54 words

S04.1 | Back to Frank and Rosa. | — | The couple returns (ILLUSTRATIVE badge).
S04.2 | In 2000, they paid $200,000 for a house in Phoenix. | buy_year, illustrative_price_200k_usd | Price tag on the door: "$200,000 · 2000" with ILLUSTRATIVE badge.
S04.3 | Their kids have moved out, and on weekends they both look at smaller places. |  | Phone in Rosa's hand scrolling small-home listings (no prices visible).
S04.4 | Whenever selling comes up, Frank says the same thing: at least the profit is tax-free. | — | Speech bubble from Frank: "At least it's tax-free."
S04.5 | [thoughtful] Is it? Has their gain passed the cap? | excl_joint_limit_usd | The bubble gets a question mark. Flat cap line above the house again. *(hold 1 s)*

## S05 — How the house is replayed (one mechanism sentence) · 255 chars, 46 words

S05.1 | We can't see their house, so we let its value rise exactly like the Phoenix area home price index from the Federal Housing Finance Agency, an average of many sales. | growth_phoenix | The house becomes a dot riding on a thin blue line (`accent` = market index), label "Phoenix-area home price index (FHFA)".
S05.2 | We follow it quarter by quarter, from 2000 to the second quarter of 2026, the latest data. | buy_year, sale_quarter | Axis ticks one per quarter, labels only "2000" and "2nd quarter 2026". Small source line "FHFA via FRED".

## S06 — Act 1 journey: the flat line and the climbing line · 450 chars, 84 words

S06.1 | Here's the cap: a flat line at $500,000, the same in every quarter. | excl_joint_limit_usd | KEY-2. V3: fixed line (`ink-muted`) across the full axis, label "$500,000 cap".
S06.2 | And here's their gain on paper, for a home that rose like the average: the $200,000, grown with the index, less the $200,000 they paid. | gain_at_200k_phoenix, illustrative_price_200k_usd | ILLUSTRATIVE $200,000. The gain line (`ink`, diamond particle) starts at zero in 2000 and begins drawing left to right. Small inset: "value minus $200,000 paid" (ILLUSTRATIVE badge).
S06.3 | For most of these years, it sits well under the line. | cross_quarter_at_200k_phoenix | The gain line rises, falls, and rises, always under the cap; the gap stays visible.
S06.4 | Then, in the second quarter of 2022, it crosses. | cross_quarter_at_200k_phoenix | The part above the cap turns `warn`. Marker "2nd quarter 2022". *(hold 1 s)*
S06.5 | It slips back under for a while. | stay_quarter_at_200k_phoenix | The line dips just under the cap; the `warn` segment ends.
S06.6 | From the second quarter of 2023, it has stayed above. | stay_quarter_at_200k_phoenix, sale_quarter | Second marker "2nd quarter 2023 → stayed above". The line ends above the cap at the right edge. Frame holds in this end state. *(hold 1 s)*

## S07 — The size of it, and what it is not · 471 chars, 85 words

S07.1 | [serious] So, on paper, if their home rose like the Phoenix average, this is the gain from the opening. | gain_at_200k_phoenix | ILLUSTRATIVE $200,000 purchase. The end of the gain line gets the label from the opening, "≈ $558,100 gain" (ILLUSTRATIVE badge), sitting visibly above "$500,000 cap". *(hold 1.2 s)*
S07.2 | That's past the cap. | gain_at_200k_phoenix, excl_joint_limit_usd | ILLUSTRATIVE $200,000 purchase. The sliver between the two labels glows `warn`. No number on it.
S07.3 | Phoenix area prices are now almost 3.8 times their 2000 level. | growth_phoenix, buy_year | Small ratio bar beside the chart: "×3.8 since 2000" (rounded label; claim 3.7903).
S07.4 | And it's a gain, not a tax bill: improvements and selling costs would both shrink it. | — | Two small blocks ("improvements", "selling costs") press down on the end of the gain line; it lowers a little; no new number.
S07.5 | The cap stood still while their gain climbed past it. | excl_joint_limit_usd | Pull back to the full chart: flat line, climbing line, `warn` tail.
S07.6 | So is Phoenix unusual, or would the same thing happen in other cities? | — | The chart shrinks to one tile among 12 blank tiles. *(hold 1.5 s — **MR1**)*

## S08 — Act 2 opens: why the line is flat · 306 chars, 58 words

S08.1 | First, why is the line flat? | — | Back to the flat cap line alone over the May 1997 → 2026 axis.
S08.2 | The cap is written as a plain dollar amount, and it has never been adjusted. | excl_joint_limit_usd, exclusion_effective_month | The line stays dead flat.
S08.3 | If $500,000 from May 1997 had kept up with consumer prices, it would be about $1,046,000 in August 2026 dollars. | excl_joint_limit_usd, excl_joint_1997_in_now, cpi_base, cpi_now, exclusion_effective_month, sale_quarter | KEY-3. New symbol N1: a dashed "inflation shadow" line (`ink-muted`, dashed) rises from the cap's start point to "≈ $1,046,000 (Aug 2026 dollars)" at the right edge; the solid cap stays flat below it. Footnote "consumer prices (CPI-U), not house prices". *(hold 1.2 s)*
S08.4 | It's everyday prices, not house prices, but it shows why a cap that never moves covers less and less of a long-held home's gain. | cpi_base, cpi_now | The footnote enlarges for 2 s.

## S09 — Twelve couples, the same $200,000 · 299 chars, 55 words

S09.1 | Now run the same replay in 12 big metro areas: illustrative couples, each paying $200,000 in 2000 for a home that rose like its metro area's average. | metro_count, metros_crossed_at_200k, buy_year, illustrative_price_200k_usd | ILLUSTRATIVE $200,000. KEY-4. The 12 tiles fill, each a mini V3 chart (flat cap + gain line), city name on top, one shared ILLUSTRATIVE badge for the grid.
S09.2 | By the second quarter of 2026, the gain is past the cap in 5 of them. | metros_crossed_at_200k, sale_quarter | ILLUSTRATIVE $200,000. Five tiles' lines end above the cap; their tails turn `warn`. Counter "5 of 12". *(hold 1 s)*
S09.3 | Los Angeles, San Diego, Seattle, Miami and Phoenix. | cross_quarter_at_200k_los_angeles, cross_quarter_at_200k_san_diego, cross_quarter_at_200k_seattle, cross_quarter_at_200k_miami, cross_quarter_at_200k_phoenix | The five names brighten in turn.

## S10 — Raise the price to $300,000 · 279 chars, 50 words

S10.1 | Now give every couple $300,000 instead. | gain_at_300k_phoenix, metros_crossed_at_300k, illustrative_price_300k_usd | ILLUSTRATIVE $300,000. All tiles redraw: the price tag on the grid changes to "$300,000"; every gain line steepens. *(hold 1 s)*
S10.2 | This time, for homes that rose like their metro area's average, the gain is past the cap in 11 of the 12. | metros_crossed_at_300k, metro_count, sale_quarter | ILLUSTRATIVE $300,000. Tails turn `warn` in 11 tiles. Counter "11 of 12". *(hold 1.2 s)*
S10.3 | Boston, New York, Denver, Dallas and both Bay Area markets join the first five. | cross_quarter_at_300k_boston, cross_quarter_at_300k_new_york, cross_quarter_at_300k_denver, cross_quarter_at_300k_dallas, cross_quarter_at_300k_san_francisco, cross_quarter_at_300k_san_jose | Names brighten.
S10.4 | Only Chicago hasn't reached the cap, at either price. | cross_quarter_at_300k_chicago, cross_quarter_at_200k_chicago | The Chicago tile stays plain; its line ends under the cap.

## S11 — Crossing isn't a one-way trip: Miami · 315 chars, 58 words

S11.1 | [curious] And crossing isn't always a one-way trip. | — | KEY-5. The Miami tile fills the screen (V3, $300,000, ILLUSTRATIVE badge).
S11.2 | In Miami, a $300,000 home that rose like the average first passed the cap in the fourth quarter of 2006. | cross_quarter_at_300k_miami, illustrative_price_300k_usd | ILLUSTRATIVE $300,000. The line pokes above the cap: marker "4th quarter 2006", short `warn` segment.
S11.3 | Then it fell back under, and has only stayed above since the second quarter of 2019. | stay_quarter_at_300k_miami | ILLUSTRATIVE $300,000. The line drops below the cap; the `warn` segment goes grey; later it rises again, marker "2nd quarter 2019 → stayed above". *(hold 1 s)*
S11.4 | Being past the line once, on paper, didn't mean staying past it. | — | Both markers stay; end state held.

## S12 — Not just the coasts; flip the question · 240 chars, 44 words

S12.1 | So Phoenix isn't unusual, and it isn't only the coasts: Dallas and Denver crossed too. | cross_quarter_at_300k_dallas, cross_quarter_at_300k_denver | Small US outline; Phoenix, Dallas, Denver dots light inland next to coastal ones. No numbers.
S12.2 | So flip the question. | — | Tiles rotate away.
S12.3 | What 2000 purchase price would put a home that rose like its metro area's average exactly at the cap now? | buy_year, threshold_joint_phoenix | A blank price slider under the Phoenix chart; the gain line's end slides down toward the cap as the slider moves. *(hold 0.8 s)*

## S13 — Phoenix's line · 271 chars, 50 words

S13.1 | In Phoenix, for a home that rose like the average, that price is about $179,200. | threshold_joint_phoenix | The slider stops: the gain line ends exactly on the cap; label "2000 price ≈ $179,200". *(hold 1.2 s)*
S13.2 | Rosa and Frank paid more than that, and that's why their line crossed. | gain_at_200k_phoenix, threshold_joint_phoenix | A dot "Rosa & Frank · $200,000" (ILLUSTRATIVE) appears just above the threshold mark on a vertical price ruler.
S13.3 | Below that price, a Phoenix home is still under the cap; above it, it's over. | threshold_joint_phoenix | The ruler splits: below the mark tinted neutral "under the cap", above it `warn` "over the cap".

## S14 — The ladder: twelve cities, one price each · 525 chars, 102 words

S14.1 | Do that for all 12 metro areas, each for a home that rose like its metro area's average, and you get a ladder of prices. | metro_count, threshold_joint_min, threshold_joint_max | KEY-6. New symbol N2 ("threshold ladder"): one vertical price ruler, 12 city rungs placed at their 2000 threshold prices, national rung dashed. Rungs drop in one by one.
S14.2 | Miami sits at the bottom of the ladder, and Chicago at the top. | threshold_joint_min, threshold_joint_min_metro, threshold_joint_max, threshold_joint_max_metro | Bottom rung labelled "Miami ≈ $114,700", top rung "Chicago ≈ $373,400" (on screen only, not spoken). *(hold 1.2 s)*
S14.3 | The faster an area's prices rose, the lower its rung: Miami's rose the most, Chicago's the least. | growth_miami, growth_chicago | Each rung carries a thin growth bar pointing left; the longest bars sit at the bottom. Screen labels only: "×5.4" Miami, "×2.3" Chicago (claims 5.3601, 2.3392).
S14.4 | Every city except Chicago sits under $300,000. | metros_threshold_under_300k, metros_threshold_under_300k_names, illustrative_price_300k_usd | Reference line at the ILLUSTRATIVE $300,000 price. A horizontal line at "$300,000" crosses the ladder; 11 rungs sit below it, Chicago alone above. No count on screen.
S14.5 | That's the cap, read a third way: not as a flat line, but as a price paid in 2000 that anyone can look up. | excl_joint_limit_usd, buy_year | The small Act 1 chart (flat line, climbing line) shrinks into the ladder's header; ladder title appears: "2000 price where gain reaches the $500,000 cap". End state held. *(hold 1.5 s — **MR2**)*

## S15 — Act 3: the answer, in the cold open's words · 527 chars, 102 words

S15.1 | So, back to the opening question: is selling a home bought in 2000 still fully tax-free? | buy_year | KEY-7. Same night street and lit house as S01; the "For sale" sign half-raised.
S15.2 | [serious] For Rosa and Frank, if their house rose like its metro area's average, not fully: part of their gain sits above the cap. | gain_at_200k_phoenix, excl_joint_limit_usd | The Phoenix V3 chart returns behind the house: flat line, `warn` tail. ILLUSTRATIVE badge.
S15.3 | For you, it may come down to one comparison: your 2000 price against your city's rung. | threshold_joint_min, threshold_joint_max, buy_year | Ladder slides in; the empty slot "your 2000 price" from S01 reappears beside it.
S15.4 | Above that rung, a home like that has already passed the cap. Below it, it hasn't. | — | The slot moves above a rung (tail `warn`), then below (neutral).
S15.5 | Below the rung isn't proof of no tax, and above it isn't proof of a large one. The video measures one line; it says nothing about what anyone does next. | — | The slot fades to an outline. No number.

## S16 — Your side of the comparison · 370 chars, 67 words

S16.1 | Your side of it is what you paid plus improvements, which count toward what the gain is measured from. | — | The slot fills as a stack: "what you paid" + "improvements".
S16.2 | Selling costs, like agent fees, come off the gain too. | — | A small "selling costs" block lowers the gain on a mini chart.
S16.3 | Outside these cities, the national index puts the line, for a home like the average, at about $243,500. | threshold_joint_us | Dashed national rung lights: "US ≈ $243,500". *(hold 1 s)*
S16.4 | For a single seller, with the $250,000 cap, the national line is about $121,700. | threshold_single_us, excl_single_limit_usd | Second dashed rung, lower: "US, single ≈ $121,700". *(hold 1 s)*

## S17 — What the line is not · 376 chars, 74 words

S17.1 | None of this is anyone's tax bill. | — | The ladder dims; a plain card "Not a tax bill".
S17.2 | Gain above the cap is taxed as a long-term capital gain, since the home was held more than a year, at a rate that depends on income and state. | long_term_gain_rule, ctx_us_only | Card line: "Above the cap → long-term capital gain (owned > 1 year)". Second line: "rate depends on your income · state not modeled".
S17.3 | And the average is not your home: your street, your remodel and your purchase month can put you far from your rung. | — | Around one rung, a spread of faint dots (individual homes, schematic, no values) scatters above and below.
S17.4 | The line is a measurement, not a next step; this video doesn't weigh selling, keeping or waiting. | — | Card "This video measures the line. It doesn't say whether to sell." *(hold 0.8 s)*

## S18 — Limits and method card (S18.3 moved to the V7 card, P1 fallback)

S18.1 | How we built this is on screen and in the description. | surviving_spouse_window_years, basis_at_death_rule | V7 method card "How we know this" (+ line "Not covered: surviving spouse · heirs (value at death)"): FHFA all-transactions indexes via FRED (metro divisions where they exist) · 2000 = average of its four quarters; sale at 2nd quarter 2026 · gain = price × index growth − price; no improvements, no selling costs · married, joint, use test assumed met · CPI-U May 1997 → Aug 2026 · indexes revised every quarter. Card held ≥ 1 s per 3 words of its longest line.
S18.2 | The price indexes are revised every quarter, so these lines can move a little with the next release. | — | Card line "revised every quarter" highlighted.
<!-- S18.3 rút khỏi lời (dự phòng C2 ghi trước: cảnh mất chú ý 5/6 → 1 câu lời + thẻ V7 + mô tả; phiên P1 áp, 2026-10-05). Nội dung chuyển lên thẻ phương pháp S18.1 và mô tả video: "Not covered: surviving spouse (joint cap for a limited window after a death; 26 U.S.C. 121(b)(4)) · heirs (basis = value at death; 26 U.S.C. 1014(a)(1))". Lời gốc: "Two rules sit outside this test: a surviving spouse keeps the joint cap for a limited time, and heirs measure gain from the home's value at death." -->

## S19 — Outro: the flat line, the house under it · 219 chars, 44 words

S19.1 | This is history, not a forecast: where prices went from 2000 to the second quarter of 2026, not where they, or the cap, go next. | ctx_history, buy_year, sale_quarter | The Phoenix V3 chart, full width, ends at the right edge; no line extends past it.
S19.2 | [thoughtful] The cap is still the same flat line it was in 1997. | excl_joint_limit_usd, exclusion_effective_month | Pull back: the flat line spans the whole axis from May 1997.
S19.3 | What moved is the house underneath it. | — | The lit house from S01 sits under the line, its gain line rising behind it past the cap. *(hold 2 s)*, then end screen.
