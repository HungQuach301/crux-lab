# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
**Đúng câu hỏi** (câu 1–2): video hỏi liệu khoản niên kim tăng 2 % mỗi năm có **giữ được sức mua / theo kịp giá cả** (so với khoản đều lớn hơn không đổi), qua người về hưu Ruth.
**Đúng đáp án** (câu 2): theo lịch sử giá Mỹ, khoản tăng 2 % **hầu như không bao giờ** giữ được sức mua qua 20 năm (chỉ 17 trên 715 quãng / khoảng 2 %, đều bắt đầu cuối thập niên 1940; 25 năm: không lần nào) — nó **làm chậm** việc mất sức mua chứ không chặn được (thường còn khoảng 80 % so với khoảng một nửa của khoản đều; Ruth giữ được khoảng 15 năm rồi tụt, nay khoảng 9/10). Cần ý "hầu như không theo kịp" + ít nhất một trong: "chậm hơn khoản đều" / mức thường gặp ~80 % / Ruth ~90 %. Đủ câu hỏi + đáp án → 1; một trong hai → 0,5; không → 0.
**Câu khuyên:** `advice: true` khi câu 5 "yes" vì tin video bảo chọn khoản nào / dự báo lạm phát, **hoặc** câu 6 nêu lời khuyên hành động (chọn khoản đều, chọn khoản tăng, mua niên kim gắn CPI, đừng mua niên kim…). Câu 6 kiểu "đừng coi 2 % là được bảo vệ hoàn toàn / hiểu giới hạn" là hiểu lời hứa, **không** tính. Người đọc **đúng** = điểm 1 và không câu khuyên.
**Khối mất chú ý** (câu 3–4): xếp chỗ người đọc nêu vào một loại: `phương pháp` / `định nghĩa` / `số dày` / `nhân vật` / `khác` / `không`, và ghi cảnh ước (trích vài chữ).


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "block": "phương pháp|định nghĩa|số dày|nhân vật|khác|không", "where": "<few words>", "why": "<one line>"}, ...}

### R1
1. The video follows Ruth, an illustrative retiree who at 65 in August 2006 chose the smaller annuity check that rises 2% a year instead of a bigger check that never changes. It asks whether that 2% raise kept her buying power over 20 years, then tests the same raise against all 715 twenty-year stretches of US prices starting from 1947 to 2006. Ruth's check kept up for most of its first 15 years, slipped below in 2022, and now buys about 9 "crates" for every 10 her first check bought. Two contrast cases follow: Carl, who started in 1966 and fell far behind, and Edna, who started in 1949 and kept up. The video closes by showing what raise would have kept up and listing its caveats.

2. Usually, no. A 2% annual raise kept full buying power in only 17 of 715 twenty-year stretches, about 1 in 42, and every one of those started between September 1947 and January 1949. No starting month since then has kept up, including Ruth's. In the typical stretch, the rising check ended at about 80.7% of its starting buying power. The raise did slow the loss: a level check typically kept only 54.3%. To keep up in half the stretches, a raise of about 3.1% a year was needed. Keeping up in every stretch took about 6.38% a year, the rate of Carl's years.

3. "The personal consumption expenditures price index, or PCE, starts later, and on it, the rising check kept up in 19.2 percent of stretches. On the consumer price index, from those same starting months since 1959, it kept up in none." Up to that point I'd been hearing counts like "17 of 715" and "21 of 715," and suddenly it's a percentage over a different time window. I couldn't easily tell whether 19.2% was a big deal or how it compared to the earlier numbers. Going from 19.2% to "none" also seems like a big gap, right after the video called the Social Security index result "close." A smaller point: "the index Social Security uses" is never named, and I'd have liked to know what it is.

4. "We reran the test on the index Social Security uses for its yearly raises: the rising check kept up in 21 of the 715. That's close to the main index." This starts the alternate-index section, which is where I drifted. It's a robustness check for experts, and it comes right after the 1990s and 25-year results. By then I had the main answer and was hearing a run of numbers that didn't change it.

5. No to both. The video says several times that it doesn't say which check to choose. It explains that it doesn't model how much smaller the rising check starts, so it can't compare total dollars paid. It also repeats that this is "history, not a forecast," and calls even the 3.4% figure for the past year "not a forecast for the year after it."

6. The video gives no direct advice, but here's what I'd take from it as someone about to sign:
- Don't assume a 2% raise means "protected from inflation." Historically it almost always lost some buying power over 20 years, just much less than a level check.
- The question the video can't answer is the one I need to answer: how much smaller does the rising check start on my actual quote? I should get both numbers from the insurer and see how many years it takes for the rising check to catch up in dollars.
- Plan for some erosion either way, and keep other inflation-sensitive resources alongside the annuity (Social Security's own cost-of-living raises, savings, etc.).
- My own costs, especially health care and housing, may rise differently from the national average, so the real gap could be bigger or smaller for me.
- Outside the video: if a higher fixed raise (like 3%) or a CPI-linked option is offered, it may be worth pricing too, since the history suggests 2% sits below typical inflation.

### R2
1. The video follows Ruth, an illustrative 65-year-old who in 2006 chose an income annuity whose check rises 2% a year instead of a larger flat check. It tests her rising check against every 20-year stretch of US prices since 1947 to see how often it kept its buying power, using Ruth's own case, two other illustrative retirees (Carl and Edna), and results for other price indexes. It concludes that her check now buys about 9 of the "crates" her first check bought, and that 2% rarely kept up historically.

2. Almost never. Of 715 twenty-year stretches, a 2% rising check kept its buying power in only 17 (about 1 in 42), all starting between September 1947 and January 1949. The typical stretch ended at 80.7% of the first check's buying power, versus 54.3% for a level check. A rate of about 3.1% a year was the historical median that kept up in half of stretches, and keeping up in every stretch required roughly Carl's 6.38% inflation.

3. Nothing was confusing in a way that stopped comprehension. One point I'd flag as a potential source of confusion is: "Ruth's check grew, but prices grew more, so today it buys less than her first check did." This is clear within the video's framing, but it could be misread as a claim about dollars rather than buying power. The video clarifies this later, so I'd call it a mild ambiguity rather than a real confusion.

4. Nowhere. The narration stayed consistent and kept its definitions (buying power, "keeping up," crates) in view throughout.

5. No, on both counts. The video explicitly says "It doesn't say which check to choose" and that annuity pricing isn't modeled, so it can't say which check pays more over a lifetime. It also states it's measuring history, not forecasting, and says the 3.4% recent inflation is "one year of history, not a forecast for the year after it."

6. A viewer should take away that a 2% raise has historically often failed to preserve buying power over 20 years, especially with the consumer price index, and that a bigger level check may erode faster but starts higher, so the comparison depends on how long they live and what inflation does. The video explicitly declines to recommend a choice, so a viewer should treat it as a reason to check how each option's starting payment, inflation assumptions, and expected lifespan compare, rather than as a verdict on which annuity to buy.

### R3
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2% a year instead of a bigger level check. It tests that raise against all 715 twenty-year stretches of US prices since 1947, asking how often the check still bought at least what its own first check did. It then compares Ruth's stretch with Edna's (kept up), Carl's (fell far behind), and the typical case, then looks at what raise rate would have kept up. It closes with caveats: US only, history not forecast, annuity pricing not modeled.

2. Mostly no. A 2% raise kept up in 17 of 715 stretches (about 1 in 42), all starting between September 1947 and January 1949. The typical stretch ended with the check buying 80.7% of its first check's power (prices rose 3.1% a year). Ruth's check ended at about 90% (roughly 9 crates for every 10), after keeping up for 12 of its first 15 years. A 3% raise kept up in 42.4% of stretches, and about 3.1% in half.

3. Passages that confused me:
- "Ruth's is one of them, and it still fell short." It comes right after "Only about 1 in 3 stretches ended with the rising check at 90 percent or more." It is unclear what "one of them" refers to and why it "still" fell short, until you work out that 90%+ is still below 100%.
- "Of the stretches that began after that, up to Ruth's, none kept up, and the best ended at 99.5 percent." "After that" is vague (after the 1990s group?).
- "Year by year, Ruth's check bought at least what her first one did on 12 of its first 15 anniversaries" versus "In August 2021, at 80, her check still bought a little more..." It was hard to square the "12 of 15" figure with the later stretch of years 16–20.
- "The level check she turned down got to her rising check's level much sooner. By year 5..." is dense, with a lot of crate comparisons.

4. "Not one of the 120 stretches that began in the 1990s kept up, and those ran through the 2000s and 2010s." My attention dropped most in this stretch of statistics (the 1990s group, 94.8%, 99.5%, 25-year stretches, then the Social Security index and PCE), where many numbers arrive in quick succession and the comparisons stack up without a clear visual anchor.

5. No to both. It states explicitly that it is history, not a forecast, and that it "doesn't say which check to choose," because insurer pricing of the smaller starting check isn't modeled, so total money paid can't be compared. It only measures buying power relative to each check's own first check.

6. There's no direct advice. A viewer could take away that a fixed 2% raise has usually not fully preserved buying power in US history, that the start date mattered a lot, and that they should weigh the raise rate against realistic inflation and the starting-check cost when comparing annuities, though the video itself doesn't recommend any of that.

### R4
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2 percent a year instead of a bigger level check. It asks whether that raise kept pace with prices, first through her own 20 years (2006 to 2026), then across all 715 twenty-year stretches of US prices since 1947. It adds two other illustrative retirees, Carl (1966 start, worst case) and Edna (1949 start, last that kept up), then shows which raise rates would have kept up. It ends by restating its limits and returning to Ruth.

2. A 2 percent raise rarely kept up. It kept a check's buying power at or above its first check's in only 17 of 715 stretches (about 1 in 42), all starting between September 1947 and January 1949. In the typical stretch, with prices up 3.1 percent a year, the rising check ended at 80.7 percent of its first check's buying power, versus 54.3 percent for a level check. Ruth's check fell short: 48.6 percent growth against 64.3 percent price growth, about 9 crates for every 10. A 3 percent raise kept up in 42.4 percent of stretches, and about 3.1 percent in half.

3. Mostly nothing. Two spots were a little muddy:
   - "Her twentieth year of checks ended this August." It's unclear at first whether this means 20 raises or 20 checks, and the later "after 20 raises" and "at 85" fit loosely with a start at 65 in 2006.
   - "Of the stretches that began after that, up to Ruth's, none kept up, and the best ended at 99.5 percent." "After that" is ambiguous (after the 1990s, or after 1949?), though context suggests after the 1990s group.

4. "The personal consumption expenditures price index, or PCE, starts later, and on it, the rising check kept up in 19.2 percent of stretches. On the consumer price index, from those same starting months since 1959, it kept up in none." Attention dropped here because it is a dense run of statistics: two indexes, a different start date, and a comparison that arrives right after several other numbers, with little to picture.

5. No to both. The video says repeatedly that it is history, not a forecast, and that it doesn't say which check to choose. It doesn't model how much smaller the rising check starts, so it can't compare total dollars paid. It measures only buying power relative to each check's own first check.

6. There is no direct advice, and the video says so. A viewer would take away a framing: a fixed 2 percent raise has historically trailed US price growth in nearly all 20-year stretches, so it shouldn't be assumed to protect buying power fully. The real choice depends on the starting-check gap, which they would have to get from their own quote, along with their own spending mix and how long they expect to live.

### R5
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2 percent a year instead of a bigger level check, and asks whether that raise kept up with prices. It checks her own 20 years first, then tests every 20-year stretch of US prices since 1947 (715 of them), and adds two other starting points: Carl in 1966, the worst case, and Edna in 1949, the last that kept up. It ends with which raise rates would have kept up, plus caveats about the price index and what isn't modeled.

2. A 2 percent raise usually did not keep up. It kept up in only 17 of 715 stretches (about 1 in 42), all starting between September 1947 and January 1949, and in none since, including Ruth's. In the typical stretch, prices rose 3.1 percent a year, so the rising check ended at 80.7 percent of its first check's buying power (the level check, 54.3 percent). Ruth's ended at about 90 percent (roughly 9 crates of 10). A 3 percent raise kept up in 42.4 percent of stretches, and about 3.1 percent in half.

3. Mostly nothing, but one passage is confusing: "Ruth's is one of them, and it still fell short." It follows "Only about 1 in 3 stretches ended with the rising check at 90 percent or more," so "one of them" and "still fell short" take a moment to reconcile. It means she is among those ending above 90 percent but still below 100. Also, "Her twentieth year of checks ended this August" sits oddly with a 2006 start, since the narration says she's "at 85" while she began at 65. That works, but the opening timeline is slightly muddled. Another small snag is that "the level check she turned down got to her rising check's level much sooner" is hard to parse on first hearing.

4. "The personal consumption expenditures price index, or PCE, starts later, and on it, the rising check kept up in 19.2 percent of stretches. On the consumer price index, from those same starting months since 1959, it kept up in none." My attention dropped here because it is a run of statistics on a third index, with a shifted start date and a comparison that is hard to hold in the head, right after a stretch of other numbers. The takeaway (the measure matters, but falling short was usual) arrives only afterward.

5. No to both. The video says explicitly that it "doesn't say which check to choose," because it doesn't model how much smaller the rising check starts, so it can't compare total dollars paid. It also says repeatedly that this is "history, not a forecast," calling the 3.1 percent a "median of the past, not an expectation," and noting that the latest 3.4 percent inflation reading is "one year of history."

6. The video offers no direct advice. A viewer could reasonably take away that a fixed 2 percent raise historically offset only part of price growth, so it should not be assumed to fully protect buying power. Before deciding, they would also want to ask the insurer how much smaller the rising check starts, since the video leaves that out. Anything beyond that, such as choosing between the checks, would be the viewer's own inference rather than something the video says.

### R6
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2% a year over a larger level check. It asks whether that raise keeps up with US prices, first through Ruth's own 20 years (2006 to 2026), then across all 715 historical 20-year stretches since 1947, with Carl (a worst case) and Edna (a lucky early case) as comparisons. It ends by showing which raise rates would have kept up, and with caveats that it is US-only, history rather than forecast, and silent on which check to pick.

2. Mostly no. A 2% raise kept up (a check still buying at least what its own first check bought) in only 17 of 715 20-year stretches, about 1 in 42, all starting between September 1947 and January 1949. The typical stretch had prices rising 3.1% a year, leaving the rising check at 80.7% of its first check's buying power (versus 54.3% for a level check). Ruth's check bought 94.5% as of August 2022 and about 9 of 10 crates now. It kept up for 15 years, then fell below. A raise of about 3.1% would have kept up in half the stretches, and 3% in 42.4%.

3. "Her twentieth year of checks ended this August." Her first check was August 2006, so with 20 raises the timing is slightly muddled; I'd also briefly stumble on "After 20 raises, a check is 48.6 percent bigger" (20 raises after the first check means the 21st check, versus "twentieth year"). Also, "By August 2022, it bought 94.5 percent" comes right after "Then, in a single year, it fell below," and it isn't stated what it buys today. The later "about 9 crates" implies roughly 90.7%, which I had to infer. Otherwise the rest was clear.

4. "The level check she turned down got to her rising check's level much sooner. By year 5, it had already fallen to about 9 crates. Her rising check stands there now, after 20 years." My attention dropped here because it is a dense comparison of two checks in crates, right after the year-by-year section, and it is easy to lose track of which check is which.

5. No. It says explicitly that it doesn't say which check to choose, doesn't model how much smaller the rising check starts, so it can't compare total dollars, and that its figures are history, "not a forecast." Rates like 3.1% are described as a "median of the past, not an expectation."

6. Little direct advice, by design. A viewer would take away that a fixed 2% raise historically usually lagged prices, so a rising check shouldn't be assumed to fully protect buying power, though it slows the loss compared with a level check. The practical next step is to ask the insurer how much smaller the starting rising check is, and to weigh that against their own expected spending and inflation exposure.

### R7
1. The video follows Ruth, an illustrative retiree who at 65 picked an annuity check that rises 2% a year instead of a bigger level check. It checks her 20 years (Aug 2006 to Aug 2026) against prices, then tests the same raise across all 715 rolling 20-year stretches since 1947. It then contrasts Carl (worst case, 1966 start) and Edna (a 1949 start that kept up), and ends by asking what raise rate would have kept up, with caveats.

2. Mostly no. A 2% raise kept up (check buys at least what its own first check bought) in only 17 of 715 stretches, about 1 in 42. All of those began between September 1947 and January 1949, and none since. The typical stretch had 3.1% annual price growth, leaving the rising check at 80.7% of its first check's buying power versus 54.3% for a level check. Ruth's check ended at about 9 crates per 10 (cumulative +48.6% vs. CPI +64.3%). It did keep up on 12 of her first 15 anniversaries. Results varied by index (21 of 715 for the Social Security index; 19.2% on PCE), but falling short was the usual outcome on each. A 3% raise kept up in 42.4% of stretches, and about 3.1% in half.

3. Nothing seriously confusing. The closest is: "Her twentieth year of checks ended this August." It's ambiguous at first, since it isn't clear that she has completed 20 years. Also, "Her check grew, but prices grew more, so today it buys less" sits awkwardly beside "the bigger level check… would buy about 6 of those crates," since comparing crates across checks of different starting sizes takes care to follow. The video flags this itself.

4. "Of the stretches that began after that, up to Ruth's, none kept up, and the best ended at 99.5 percent." Attention dips here because the section is a dense run of statistics (the 1990s stretches, 94.8%, then 99.5%) with no new idea, and "after that" is unclear about which period it refers to.

5. No to both. It states repeatedly that it is history, not a forecast, and that it doesn't model annuity pricing, so it can't say which check pays more in total. It only measures buying power relative to each check's own first check.

6. No direct advice is given. A viewer might take away that a fixed 2% raise historically often failed to fully offset inflation over 20 years, so they should not assume it protects buying power. They should ask how much smaller the rising check starts, and compare that to the level check. The gap, not the raise alone, is what determines which is better, and the video leaves that to the viewer.

### R8
1. The video follows Ruth, an illustrative retiree who at 65 chose an annuity check that rises 2 percent a year over a bigger level check. It asks whether that raise kept up with prices, meaning whether the check still buys at least what its own first check bought. It first checks Ruth's own 20 years, then tests every 20-year stretch since 1947 (715 of them), and adds two other examples (Carl, who fell far behind, and Edna, who kept up). It ends with which raise rates would have kept up and a list of limits.

2. Mostly no. Ruth's check kept up on 12 of its first 15 anniversaries, but after 20 years it bought about 9 crates for every 10 her first check bought (the video also gives 94.5 percent in 2022), because her 48.6 percent of cumulative raises trailed a 64.3 percent rise in the consumer price index. Across all 715 stretches, a 2 percent raise kept up in only 17 (about 1 in 42), all starting between September 1947 and January 1949. The typical stretch ended at 80.7 percent of the first check's buying power (versus 54.3 percent for a level check), and no stretch kept up over 25 years. A 3 percent raise kept up in 42.4 percent of stretches, and about 3.1 percent in half.

3. Mostly nothing, but this passage was confusing: "The level check she turned down got to her rising check's level much sooner. By year 5, it had already fallen to about 9 crates. Her rising check stands there now, after 20 years." The "level" it refers to is the crate count, but a listener could easily mix up the two checks, and the video doesn't say that the level check's crates start from a bigger base. The earlier line "The bigger level check she turned down would buy about 6 of those crates today" also sits oddly beside it, because the two checks are measured against different starting points. Also, "the 120 stretches that began in the 1990s" is stated without saying that these stretches end in the 2010s, so "ran through the 2000s and 2010s" takes a moment to parse.

4. "Of the stretches that began after that, up to Ruth's, none kept up, and the best ended at 99.5 percent." Attention drops here because it comes after a run of statistics, the phrase "after that" is vague about which period it means, and the 99.5 percent figure arrives with no anchor for where it falls among the stretches.

5. No to both. The video says outright that it doesn't say which check to choose, because it doesn't model how much smaller the rising check starts, so it can't compare total dollars paid. It also says it's history, not a forecast: the 3.1 percent figure is "a median of the past, not an expectation," and the recent 3.4 percent year is "one year of history."

6. The video gives no direct advice. A viewer would likely take away that a fixed 2 percent raise has usually not fully preserved buying power over 20 years in US history, so they should not assume it will, and should ask the insurer how much smaller the rising check starts and weigh that against how long they expect to live and what inflation might do. The video itself supports only the narrower point about buying power.
