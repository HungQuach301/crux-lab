# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
**Đúng câu hỏi** (câu 1–2): video hỏi liệu khoản niên kim tăng 2 % mỗi năm có **giữ được sức mua / theo kịp giá cả** (so với khoản đều lớn hơn không đổi), qua người về hưu Ruth.
**Đúng đáp án** (câu 2): theo lịch sử giá Mỹ, khoản tăng 2 % **hầu như không bao giờ** giữ được sức mua qua 20 năm (chỉ 17 trên 715 quãng / khoảng 2 %, đều bắt đầu cuối thập niên 1940; 25 năm: không lần nào) — nó **làm chậm** việc mất sức mua chứ không chặn được (thường còn khoảng 80 % so với khoảng một nửa của khoản đều; Ruth giữ được khoảng 15 năm rồi tụt, nay khoảng 9/10). Cần ý "hầu như không theo kịp" + ít nhất một trong: "chậm hơn khoản đều" / mức thường gặp ~80 % / Ruth ~90 %. Đủ câu hỏi + đáp án → 1; một trong hai → 0,5; không → 0.
**Câu khuyên:** `advice: true` khi câu 5 "yes" vì tin video bảo chọn khoản nào / dự báo lạm phát, **hoặc** câu 6 nêu lời khuyên hành động (chọn khoản đều, chọn khoản tăng, mua niên kim gắn CPI, đừng mua niên kim…). Câu 6 kiểu "đừng coi 2 % là được bảo vệ hoàn toàn / hiểu giới hạn" là hiểu lời hứa, **không** tính. Người đọc **đúng** = điểm 1 và không câu khuyên.
**Khối mất chú ý** (câu 3–4): xếp chỗ người đọc nêu vào một loại: `phương pháp` / `định nghĩa` / `số dày` / `nhân vật` / `khác` / `không`, và ghi cảnh ước (trích vài chữ).


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "block": "phương pháp|định nghĩa|số dày|nhân vật|khác|không", "where": "<few words quoted>", "why": "<one line>"}, ...}

### R1
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2 percent a year instead of a bigger level check. It tests that raise against every 20-year stretch of US prices since 1947 (715 stretches), asking whether the check still buys at least what its own first check bought. Ruth's check fell just short after 20 years, and the video contrasts her with Edna (kept up) and Carl (fell far behind) to show that the starting month drove the outcome. It closes by noting which raise rates would have kept up, with repeated caveats that this is history, not a forecast or a recommendation.

2. Mostly no. A 2 percent raise kept up in only 17 of 715 stretches (about 1 in 42), all starting between September 1947 and January 1949. The typical stretch had prices rising 3.1 percent a year, leaving the rising check at 80.7 percent of its first check's buying power, versus 54.3 percent for a level check. Ruth's check bought 94.5 percent of its first after 20 years (about 9 of 10 crates). Over 25 years, no stretch kept up. A raise of about 3.1 percent would have kept up in half the stretches, and 3 percent in 42.4 percent.

3. Nothing is truly confusing, but two spots are slightly muddled:
- "Her twentieth year of checks ended this August." It conflicts a bit with "Ruth, at 85" and with the August 2021 / August 2022 framing, so the timeline of anniversaries is hard to follow.
- "Twenty years later, her check still bought at least what her first one did. ... Her 20 years ended a few years into Carl's. The same few years of prices that ended her stretch with all 10 crates lit began his." Edna starting in 1949 and ending around 1969 is easy to lose track of when stated this way.

4. "Ruth took her first rising check in August 2006. Her reasoning was simple: prices go up, and her check goes up too." Attention dips here because it's a brief, slow setup after the numbers had already been introduced. A close second is the long caveats paragraph ("The consumer price index is a national average, not a retiree's own basket...") which is dense and repeats earlier disclaimers.

5. No on both. The video says repeatedly that it doesn't say which check or raise to choose, and that it's history, not a forecast. It also doesn't model annuity pricing, so it can't compare lifetime dollars paid. The 3.4 percent latest-year inflation is explicitly called one year of history.

6. There's no explicit advice, but a viewer could take away that a fixed 2 percent raise has historically not fully protected buying power over 20+ years in most periods, and that outcomes depend heavily on when you start. As a 64-year-old looking at a quote, I'd take it as a reason to ask the insurer how much smaller the rising check starts, since the video can't compare the dollars, and to weigh that against how much inflation protection matters to me.

### R2
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2 percent a year instead of a bigger level check. It asks whether that raise kept up with US prices, measuring buying power against each check's own first check. It checks Ruth's 20 years (she ends at about 94.5 percent), then all 715 twenty-year stretches since 1947, then contrasts Carl (1966, the worst) and Edna (1949, the last that kept up). It closes by noting what raise rate would have kept up and listing the limits of the analysis.

2. A 2 percent raise rarely kept up: it did in 17 of 715 twenty-year stretches (about 1 in 42), all starting between September 1947 and January 1949, and none since, including Ruth's. In the typical stretch, prices rose 3.1 percent a year, so the rising check ended at 80.7 percent of its first check's buying power (the level check, 54.3 percent). Ruth's check bought 94.5 percent of its start after 20 years. Over 25 years, no stretch kept up. A 3 percent raise kept up in 42.4 percent of stretches, and about 3.1 percent in half.

3. "Measured against its own start, the level check she turned down fell that far much sooner." Slightly confusing: "that far" refers back to 94.5 percent, and "measured against its own start" is easy to lose. Also "In crates, the typical rising check ended with most of its 10 still lit" is a bit vague, since "lit" is a visual cue I can't see. Otherwise it's mostly clear.

4. "The 715 stretches overlap, so they're not 715 separate tests." Attention dipped in the closing caveats stretch generally, and this line is the sharpest drop: it's abstract and statistical, and comes after the emotional story is resolved. A close second: "We also ran it on the index Social Security uses for its yearly raises, with about the same result; on a gentler price measure, the raise kept up more often but still fell short in most stretches." It is a dense aside with no numbers.

5. No. The video says repeatedly that it doesn't say which check to choose, and that it's history, not a forecast. It doesn't model the starting size difference between the checks, so it can't compare lifetime dollars. The 3.4 percent latest-year inflation is explicitly called one year of history, not a prediction.

6. The video gives no explicit advice, but a viewer would reasonably take away that a flat 2 percent raise has historically not preserved buying power over 20+ years, so they shouldn't assume it protects against inflation. They'd also see that outcomes depend heavily on the starting period, and that the real choice involves how much smaller the rising check starts, which they'd need to get from the insurer's quote and weigh themselves. As a 64-year-old looking at my own quote, I'd ask what the initial-payout gap is and judge it against these buying-power results.

### R3
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2 percent a year and wanted to know if that would keep up with prices. It shows her 20 years: her check ended up buying about 9 of every 10 "crates" her first check did. It then tests the 2 percent raise against all 715 twenty-year stretches since 1947, compares her with Carl (worst case) and Edna (a lucky early start), and ends by showing which raise rates would have kept up.

2. A 2 percent annual raise rarely kept up. It held buying power in only 17 of 715 stretches (about 1 in 42), all starting between September 1947 and January 1949. In the typical stretch, prices rose 3.1 percent a year, so the check ended at 80.7 percent of its first check's buying power (versus 54.3 percent for a level check). No stretch kept up over 25 years. Ruth's check kept up for most of 15 years, dipped below in 2022, and sits at about 90 percent of her first check's buying power at 85. A 3 percent raise kept up in 42.4 percent of stretches, and about 3.1 percent in half.

3. "Her twentieth year of checks ended this August." This is mildly confusing. It's unclear whether it means the twentieth check or twenty full years, and later lines say she's 85 and the 2006 start was at 65, so the timing takes some working out. Also, "The level check she turned down got to her rising check's level much sooner. By year 5, it had already fallen to about 9 crates." That is hard to follow on first listen because it compares two checks against different baselines.

4. "The 715 stretches overlap, so they're not 715 separate tests." My attention dropped here because the closing caveats arrive as a dense list right before the ending, and this one is a statistical point that is abstract when only heard. It also follows a long run of numbers.

5. No. The video says explicitly, more than once, that it doesn't say which check to choose and that it's history, not a forecast. It doesn't model how much smaller the rising check starts, so it can't compare total dollars. The rates it cites (like 3.1 percent) are described as a median of the past, not an expectation.

6. There's no direct advice, but a viewer would likely take away that a fixed 2 percent raise has historically trailed US price growth in nearly all 20-year periods, so they shouldn't assume a modest raise fully protects buying power. They would also likely see that the outcome depends heavily on when you start. The viewer would still need to weigh the starting-check difference and their own situation, which the video leaves out.

### R4
1. The video follows Ruth, an illustrative retiree who at 65 chose a smaller annuity check that rises 2% a year instead of a bigger level check. It asks whether that raise kept up with prices, using Ruth's own 20 years and then every 20-year stretch of US prices since 1947 (715 of them). Ruth's check ended up buying about 9 crates for every 10 her first check bought. Two other illustrative retirees, Carl and Edna, show the range: Carl fell far behind, while Edna's start was among the few where the raise kept up. It closes with which raise rates would have kept up, plus caveats.

2. A 2% raise rarely kept up. It kept its first-check buying power in 17 of 715 stretches (about 1 in 42), all starting between September 1947 and January 1949. The typical stretch had prices rising 3.1% a year, so the rising check typically bought 80.7% of its first check's buying power after 20 raises. For Ruth specifically, her check is up 48.6% while prices rose 64.3%, and it fell below her first check's buying power in August 2022 (94.5%). Over 25 years, no stretch kept up. The level check did worse, typically keeping 54.3%. A 3% raise kept up in 42.4% of stretches, and about 3.1% in half.

3. Mostly nothing. Two small spots:
- "If her first check bought 10 crates of everything the index tracks, her check today buys about 9." The "crates" image is clear, but the narration says 94.5% in one place and "about 9" in another, and a viewer may not connect the two (the 94.5% was for August 2022, the 9 crates is today).
- "The level check she turned down got to her rising check's level much sooner. By year 5, it had already fallen to about 9 crates." It is a little hard to follow on first hearing because it compares two checks' timelines in one breath.

4. "Year by year, Ruth's check bought at least what her first one did on 12 of its first 15 anniversaries." My attention dipped here because it is a dense count with no payoff yet. The "12 of 15" statistic is abstract, and it is followed immediately by more date-by-date detail (2021, 2022) before the story picks up again.

5. No to both. The video explicitly says it doesn't say which check to choose, because it doesn't model how much smaller the rising check starts, so it can't compare total dollars. It also says it's history, not a forecast, and the 3.4% recent inflation and the "median of the past" are framed as descriptions, not expectations.

6. There is no direct advice, by design. A viewer would take away that a fixed 2% raise has historically often lagged US consumer prices over 20 years, that the outcome depended heavily on the starting decade (1960s bad, late 1940s fine), and that the raise slows the loss of buying power rather than preventing it. The sensible follow-up is to ask the insurer how much smaller the rising check starts, and to weigh that against their own expected spending, health care costs, and other income sources, rather than treating the video as a verdict.

### R5
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2 percent a year over a bigger level check. It asks whether that raise keeps pace with prices. It checks Ruth's own 20 years (her check ended up buying about 9 crates for every 10 her first one did), then tests all 715 twenty-year stretches since 1947. Carl (1966, worst) and Edna (1949, last success) show the range, and it closes by noting which raise rates would have kept up. It is US-only history, not a forecast.

2. Mostly no. A 2 percent raise kept up (bought at least what the first check bought) in only 17 of 715 stretches, about 1 in 42, all starting between September 1947 and January 1949. In the typical stretch, prices rose 3.1 percent a year, so the rising check bought 80.7 percent of its first check's power after 20 raises, versus 54.3 percent for a level check. Over 25 years, none kept up. Ruth's check bought 94.5 percent of its first at 81 and about 90 percent at 85. A 3 percent raise kept up in 42.4 percent of stretches.

3. Mostly nothing, but two spots were mildly confusing:
 - "Her twentieth year of checks ended this August." This is a little ambiguous, because the story opens with her at 65 and then jumps to the present. I had to work out that she is now 85.
 - "The level check she turned down got to her rising check's level much sooner. By year 5, it had already fallen to about 9 crates." The comparison is dense. It means the level check lost as much buying power in 5 years as the rising check did in 20, and it's easy to miss that this is relative to each check's own start.

4. "That index is a national average of what urban households pay for, from rent to medical care to gasoline, not any one person's own basket." My attention dipped here. It is a definitional aside in the middle of the numbers, and the point is repeated in the closing caveats. The repeated disclaimers near the end ("The 715 stretches overlap...") also felt like a lull.

5. No to both. The video says outright that it doesn't model how much smaller the rising check starts, so it can't say which pays more in total. It also says repeatedly that it is "history, not a forecast," and that rates like 3.1 percent are "a median of the past, not an expectation." It measures only buying power relative to each check's own first check.

6. There is no explicit advice, and the video says so. A viewer could still take away that:
 - A fixed 2 percent raise historically did not protect against inflation in nearly all 20-year stretches.
 - It did better than a level check.
 - The outcome depended heavily on the start date and on later inflation.
 
 A viewer would want to compare the actual initial-payment gap in a real quote before deciding.

### R6
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2% a year instead of a bigger level check. It asks whether that raise kept pace with prices, first for Ruth's own 20 years (2006 to 2026), then across all 715 20-year stretches since 1947. It adds Carl (worst case, 1966) and Edna (last success, 1949), then looks at which raise rates would have kept up. It stresses throughout that this is US history, not a forecast, and not advice on which check to pick.

2. Mostly no. A 2% raise kept up (the check still buying at least what its first check bought) in only 17 of 715 20-year stretches, about 1 in 42, all starting between September 1947 and January 1949. In the typical stretch, prices rose 3.1% a year, so the rising check bought about 80.7% of its first check's buying power after 20 years, versus 54.3% for a level check. Ruth's check bought at least its first for most of the first 15 years, then dipped below in 2022 and now buys about 9 crates for every 10 originally. Over 25 years, no stretch kept up. A 3% raise kept up in 42.4% of stretches, and about 3.1% in half.

3. "The level check she turned down got to her rising check's level much sooner. By year 5, it had already fallen to about 9 crates. Her rising check stands there now, after 20 years." This is confusing because it compares two checks measured against different starting points (the level check started bigger), and the "crates" unit is switching between each check's own baseline. Earlier the video said the level check would buy about 6 crates today, so "9 crates" at year 5 for the level check needs a moment to untangle. Also, "Ruth's check bought at least what her first one did on 12 of its first 15 anniversaries" is slightly hard to square with "slipped under in a few early years" without a visual.

4. "Here, keeping up means a check still buys at least what its own first check bought. Ruth is an illustrative retiree, built on real US prices, and today her check falls short of that." Attention dropped most in the dense run of caveats and definitions early on, right after the hook, where several disclaimers stack ("US only," "history, not a forecast," "doesn't say which check to choose," "doesn't model it") before the story really starts. The later repeated disclaimers near the end also feel redundant, but the early stack is where the pace stalls.

5. No to both. The video explicitly says it doesn't say which check to choose, because it doesn't model how much smaller the rising check starts and so can't compare total dollars. It also says repeatedly that it's history, not a forecast: the 3.1% "typical" rate is a median of the past, and the 3.4% last-12-month figure is one year, not a prediction.

6. There's no explicit advice, but a viewer would likely take away that a fixed 2% annual raise has historically been unlikely to fully preserve buying power over 20 years, so they shouldn't assume it protects against inflation. Practically, they would want to ask the insurer how much smaller the starting check is, consider how long they may live, think about their own spending mix (health care, housing), and weigh other inflation protection. As a 64-year-old, I'd come away seeing the raise as a partial cushion that slows the loss, not a guarantee, and I would still need to compare the actual quotes myself.

### R7
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2 percent a year instead of a bigger level check. It tests whether that raise kept its buying power against every 20-year stretch of US prices since 1947, using Ruth's own stretch as the starting case. It then compares Edna (kept up), Ruth (fell short late), and Carl (fell far behind) to show that the start month drove the outcome. It closes by showing which raise rates would have kept up, with repeated caveats that it is history and not a forecast, and does not recommend a choice.

2. Mostly no. A 2 percent raise kept up (bought at least what its own first check bought) in only 17 of 715 20-year stretches, about 1 in 42, all starting between Sept 1947 and Jan 1949. The typical stretch had 3.1 percent annual price growth, leaving the rising check at 80.7 percent of its first check's buying power (level check: 54.3 percent). Over 25 years, none kept up. Ruth's own check ended at about 94.5 percent after 20 years, having kept up for 12 of its first 15 anniversaries. A raise of about 3.1 percent would have kept up in half of stretches, and 3 percent in 42.4 percent.

3. Nothing seriously confusing, but a few spots are slightly muddled:
   - "Her twentieth year of checks ended this August." Together with "Twenty years ago, Ruth asked…" and "at 85," it is a little unclear on timing and age, since she started at 65 in 2006 and the video says "at 80" in 2021.
   - "Ruth took her first rising check in August 2006" versus "Ruth isn't the worst case" sits next to "her stretch… the most recent." These are fine, but the "94.5 percent" figure for August 2022 versus "about 9 of 10" today needs the viewer to track which date is meant.
   - "Her answer: for 15 years, mostly yes" reads oddly against "12 of its first 15 anniversaries."

4. Closest to a drop: "The 715 stretches overlap, so they're not 715 separate tests. And because annuity pricing isn't modeled, nothing here compares the dollars both checks pay out over a lifetime." It's a dense caveat block after the story's payoff, and it repeats earlier disclaimers, so it's more list-like and less engaging.

5. No on both. The video says explicitly that it "doesn't say which check to choose" and that it is "history, not a forecast." It does not model how much smaller the rising check starts, so it cannot compare lifetime dollars. The one-year 3.4 percent inflation figure is labeled as not predictive.

6. There is no direct advice. A viewer might take away that a fixed 2 percent raise historically often did not fully protect buying power over 20 years, that the start date mattered heavily, and that a rising check slows loss more than a level one against its own start. Any decision would still need the actual quote, the size of the initial payout gap, and the viewer's own situation.

### R8
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2 percent a year instead of a bigger level check. It asks whether that raise keeps up with prices, first by tracing her own 20 years (2006–2026), then by testing every 20-year stretch of US prices since 1947. It adds two other illustrative retirees, Carl (1966 start, worst case) and Edna (1949 start, last success), to show how much the starting month mattered. It closes with what raise rates would have kept up, and with caveats.

2. A 2 percent annual raise rarely kept a check's buying power at or above its first check's over 20 years: it did so in 17 of 715 stretches (about 1 in 42), all starting between September 1947 and January 1949, and in none over 25 years. The typical stretch ended at 80.7 percent of the first check's buying power (prices rising 3.1 percent a year), versus 54.3 percent for a level check. Ruth's check, after 20 raises, bought about 94.5 percent (roughly 9 of 10 crates). It kept up for most of her first 15 years and then fell below in 2022. A raise of about 3.1 percent would have kept up in half the stretches, and 3 percent in 42.4 percent of them.

3. Nothing seriously confusing. Mildly: "Ruth's check climbed back in her early years; Carl's never did" is clear, but "The same few years of prices that ended her stretch with all 10 crates lit began his" is a bit tangled. The "crates lit" imagery assumes a visual I couldn't see. Also, "94.5 percent" in August 2022 versus "about 9" crates today with the 20-year ending in August 2026 is slightly hard to line up, since the exact present figure is never stated as a percent (48.6/64.3 implies about 92 percent).

4. "The 715 stretches overlap, so they're not 715 separate tests." This is where attention dropped most: the closing caveat run (CPI as national average, overlap, annuity pricing not modeled) is a dense list of disclaimers after the story had resolved, and it delivers them in a flat, procedural way.

5. No to both. The video explicitly says it doesn't say which check to choose (it doesn't model how much smaller the rising check starts, so it can't compare lifetime dollars), and it repeatedly says it's history, not a forecast, including the 3.4 percent latest-year inflation figure.

6. Not a recommendation to choose any particular check. The takeaways a viewer could reasonably draw: a fixed 2 percent raise has historically not preserved buying power over 20 years in most periods, so a viewer shouldn't assume it "keeps up" with inflation; the outcome depends heavily on when you start, which you can't control; and when comparing annuity options, they should weigh the starting-payment difference, which this video leaves out, and possibly other sources of inflation protection.

### R9
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2% a year over a larger level check. It tests whether that raise kept up with US prices, first in her own 20 years (2006 to 2026), then across all 715 twenty-year stretches since 1947. It then shows contrasting cases (Edna, who kept up; Carl, who fell far behind), asks what raise would have kept up, and closes with caveats. It explicitly measures buying power against each check's own first check, not total dollars paid.

2. Mostly no. A 2% raise kept up in only 17 of 715 twenty-year stretches (about 1 in 42), all starting between September 1947 and January 1949. In the typical stretch, prices rose 3.1% a year, so the rising check ended at about 80.7% of its first check's buying power, versus 54.3% for a level check. Ruth's check bought at least its first check's power in 12 of its first 15 years, then fell below in 2022 and now buys about 9 of every 10 "crates". Over 25 years, no stretch kept up. A 3% raise kept up in 42.4% of stretches, about 3.1% in half, and only Carl's rate (6.38%) in all.

3. Nothing seriously confused me. The closest is "The level check she turned down got to her rising check's level much sooner. By year 5, it had already fallen to about 9 crates." It's a bit tangled: it compares the level check's buying power to the rising check's end point, and the "crates" metaphor is easy to lose against the percentages.

4. "The 715 stretches overlap, so they're not 715 separate tests." The caveat paragraph is dense, and this statement arrives abstractly, with no illustration of why overlap matters. The listener has just heard a long run of caveats and stats, so attention drifts.

5. No to both. The video says repeatedly that it doesn't say which check or raise to choose, and that it's history, not a forecast. It doesn't model how much smaller the rising check starts, so it can't compare total dollars. The medians (3.1%, 3%) are described as past data, not expectations. It does note the latest 12-month inflation (3.4%) but labels it one year, not a prediction.

6. The video offers no explicit advice. A viewer might reasonably conclude that a fixed 2% raise has historically not protected buying power in most 20-year periods, though it did better than a level check. That makes the starting size of the rising check and the insurer's pricing the key unknowns to ask about. But that is an inference, not something the video says, and the video is clear that it doesn't tell anyone which to pick.

### R10
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2 percent a year, and asks whether that raise kept up with prices. It checks her own 20 years (her check ended up buying about 9 of her first check's 10 "crates"), then every 20-year stretch of US prices since 1947 (715 of them), then compares her with Carl (a bad start in 1966) and Edna (a good start in 1949). It ends by showing which raise rates would have kept up and listing its limits.

2. In this history, a 2 percent raise almost never kept up. It held buying power in 17 of 715 stretches (about 1 in 42), all starting between September 1947 and January 1949, and in none over 25 years. The typical stretch had prices rising 3.1 percent a year, leaving the rising check at 80.7 percent of its first check's buying power (the level check at 54.3 percent). Ruth's check ended at about 94.5 percent, Carl's at 43.1 percent, and Edna's kept up. A 3 percent raise kept up in 42.4 percent of stretches, and about 3.1 percent in half.

3. Nothing is truly confusing, but one passage took effort: "Measured against its own start, the level check she turned down fell that far much sooner. By year 5, it was already down to about 9 in 10. Her rising check stands there now, after 20 years." It is easy to lose the thread that each check is compared only to its own first check, not to the other check's dollars. Also, the closing line "at 85, her check buys about 9 crates for every 10" sits slightly oddly against the earlier "94.5 percent" figure, since 9 is a rounded number.

4. "Ruth took her first rising check in August 2006. Her reasoning was simple: prices go up, and her check goes up too." My attention dipped less here than in the dense stretch of repeated disclaimers, such as "These rates describe what prices did; this video doesn't say which check, or which raise, to choose," which restates points already made several times. The disclaimers are repetitive.

5. No on both counts. It says explicitly that it doesn't say which check or raise to choose, because it doesn't model how much smaller the rising check starts, so it can't compare lifetime dollars. It also says it's history, not a forecast, and even the 3.4 percent latest-year figure is "one year of history, not a forecast."

6. There's no direct advice, but a viewer would take a cautionary lesson: a fixed 2 percent raise has historically not preserved buying power over 20 years, and outcomes depend heavily on when you start. For me at 64, the practical step would be to ask the insurer how much smaller the rising check starts and what an inflation-linked option would cost, since the video leaves that comparison out.

### R11
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2% a year instead of a bigger level check. It asks whether that raise kept up with US prices, first through Ruth's own 20 years (2006 to 2026), then across all 715 twenty-year stretches since 1947. It adds two other illustrative retirees, Carl (worst case, 1966 start) and Edna (last case that kept up, 1949 start), then shows which raise rates would have kept up. It closes with caveats: CPI is a national average, the stretches overlap, annuity pricing isn't modeled, and it's history, not a forecast.

2. A 2% raise almost never kept up. It held buying power at least equal to the first check in only 17 of 715 stretches (about 1 in 42), all starting between September 1947 and January 1949. In the typical stretch, prices rose 3.1% a year, so after 20 raises the rising check bought about 80.7% of what its first check did. The typical level check kept 54.3%. Ruth's check, up 48.6% against prices up 64.3%, buys about 9 crates per 10 at the start; it stayed above water for 12 of its first 15 anniversaries, then fell below in 2022. Over 25 years, no stretch kept up. Raises that did better: 3% kept up in 42.4% of stretches, about 3.1% in half, and keeping up in every stretch needed roughly Carl's 6.38%.

3. One passage confused me: "Ruth's check rises every year, and it buys less than her first one." It's fine on its own, but the next scene says she "chose" the check at 65 and "asked one thing," which reads as if she's deciding now, while the video later says her twentieth year just ended. The tense shifts between a present decision and a finished 20 years took a moment to untangle. Also, "Ruth took her first rising check in August 2006" combined with "At 65" and later "at 85" and "at 80" in 2021 is a little inconsistent in timing (80 in 2021 implies 65 in 2006, which fits), so mostly it's just the tense. Otherwise, nothing serious.

4. "The level check she turned down got to her rising check's level much sooner. By year 5, it had already fallen to about 9 crates. Her rising check stands there now, after 20 years." Attention dropped there because the comparison is dense: it mixes two checks, two timelines, and the crate unit right after the "about 6 crates" line, and it's easy to lose which check is at which level. The later "about year 8" version of the same idea adds to the number-juggling.

5. No to both. The video says repeatedly that it doesn't say which check to choose, since it doesn't model how much smaller the rising check starts, so it can't compare total money. It also says it's history, not a forecast; the 3.4% latest-year figure is described as one year, and the 3.1% is "a median of the past, not an expectation."

6. No explicit advice is given, and a careful viewer shouldn't take a "choose X" conclusion. What they could reasonably take: a fixed 2% raise has historically often fallen short of inflation over 20 years, so it shouldn't be assumed to fully protect buying power. When comparing quotes, they should ask how much smaller the starting check is, and think about whether that gap is worth the partial protection. Timing and inflation path matter a lot and can't be known in advance.

### R12
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2 percent a year instead of a larger level check. It asks whether that raise kept up with prices over her 20 years, and she ends at about 94.5 percent of her first check's buying power. It then tests the same raise over all 715 starting months from 1947 to 2006, and compares Ruth with Edna (kept up) and Carl (fell far behind). It closes with which raise rates would have kept up and a list of limits.

2. A 2 percent raise rarely kept up over 20 years. It kept up in 17 of 715 stretches (about 1 in 42), all starting between September 1947 and January 1949. In the typical stretch, prices rose 3.1 percent a year, so the rising check ended with 80.7 percent of its first check's buying power. The level check typically kept 54.3 percent. Over 25 years, no stretch kept up. A 3 percent raise kept up in 42.4 percent of stretches, and about 3.1 percent kept up in half.

3. Mildly confusing: "Her 20 years ended a few years into Carl's. The same few years of prices that ended her stretch with all 10 crates lit began his." I had to work out the dates myself (Edna starts January 1949, so she ends in 1969, while Carl starts in January 1966). Also "Keeping up in every stretch took the rate of Carl's years" doesn't give the number at that point, and I had to recall the 6.38 percent from earlier.

4. "This is US only, and it's history, not a forecast." It is said at the start, in the limits section, and again at the end. By the third time I'd stopped listening, since I'd already absorbed it.

5. No to both. The video says outright that it doesn't say which check or raise to choose, and that the results are history, not a forecast. It doesn't model the starting size of the rising check, so it can't compare lifetime dollars. The 3.1 percent figure is described as a median of the past, not an expectation.

6. The video gives no direct advice, but I'd take a few things from it. A fixed 2 percent raise has historically lost ground in nearly every 20-year stretch, though it lost less than a level check. A raise doesn't guarantee that buying power holds. The missing piece is the dollar cost: I'd have to ask the insurer how much smaller the rising check starts, and that number, plus my own health and spending needs, would decide it. This video is only one input.
