# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
**Đúng câu hỏi** (câu 1–2): video hỏi tiền thuê nhà của Nina (người thuê, minh hoạ) có "phí" không — **mua nhà hay tiếp tục thuê**, khi tính đủ chi phí sở hữu, qua hai người giống hệt (một mua, một thuê) phát lại trên lịch sử thật của Mỹ.
**Đúng đáp án** (câu 2): phát lại 307 tháng bắt đầu từ 1991 (giữ 10 năm), **người mua hơn ở khoảng 3/4** số tháng; **người thuê hơn ở một dãy tháng quanh 2001–2007** (tệ nhất June 2006, người mua kém khoảng $82,000); **và** kết quả **đổi theo tiền thuê giả định** (thẻ tiền thuê: thuê thấp hơn → ít tháng người mua hơn, cao hơn → nhiều hơn). Cần "khoảng 3/4 (hoặc đa số)" + ít nhất một trong: dãy 2001–2007/2006 / phụ thuộc tiền thuê giả định / kỳ hạn 5–15 năm. Đủ câu hỏi + đáp án → 1; một trong hai → 0,5; không → 0. Kể "mua luôn thắng" hay "video bảo nên mua" → không được 1.
**Câu khuyên (A28):** `advice_stated` khi câu 5 "yes" vì tin video bảo mua hay thuê / dự báo giá-thuê-lãi, **hoặc** câu 6–7 nêu lời khuyên hành động MÀ người đọc nói video gợi ra (mua, thuê, chờ, mua trước khi…, giữ ≥ 10 năm…). `advice_inferred`: người đọc tự suy, câu 7 "my own conclusion". `caution_only`: thận trọng chung (tự tính, hỏi chuyên gia). Người đọc **đúng** = điểm 1 và không `advice_stated`.
**Danh sách từ dễ đọc thành lời khuyên (luật tạm 13/10):** người chấm ghi `advice_words` = mọi cụm người đọc TRÍCH từ lời video làm căn cứ lời khuyên (vd "wins", "worth it", "the bar", "measured against").
**Khối mất chú ý** (câu 3–4): xếp chỗ người đọc nêu vào `phương pháp` / `định nghĩa` / `số dày` / `nhân vật` / `khác` / `không`, ghi cảnh ước (trích vài chữ).
**Câu hỏi mang tới** (câu 8): `answered_own`: true/false.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, "advice_words": ["..."], "attention_block": "phương pháp|định nghĩa|số dày|nhân vật|khác|không", "attention_scene": "<few words>", "answered_own": true|false, "why": "<one line>"}, ...}

### R1
1. The video follows Nina, a renter in September 2026 who has enough saved for a down payment and closing costs on a $400,000 home. Nina is deciding whether rent is wasted money. It replays a buying twin and a renting twin from every start month between January 1991 and July 2016 (307 months), each followed for ten years. The renter's savings sit in cash. A "street" of 307 houses lights up where the buyer ended ahead and goes dark where the renter did. It then varies the stay length (5, 10 and 15 years) and the assumed starting rent (4%, 5% or 6% of price per year), and ends by placing Nina's September 2026 first month beside the historical ones.

2. Over ten years, the buyer ended ahead in about 3 in 4 of the 307 start months, and the renter ended ahead in the other 75. Every renter win falls between April 2001 and December 2007. The buyer won in every 1990s start and every start from 2009 to mid-2016. The median buyer ended about $157,000 ahead, the best case (April 2012) about $484,000 ahead, and the worst (June 2006) $82,385 behind.
   - Five-year stays: the buyer won in 74.4% of starts.
   - Fifteen-year stays: the buyer won in every start month history allows.
   - Starting rent: 64.2% at 4%, 92.2% at 6%, and 73.6–87.3% across the Census range of 4.83–5.59%.
   - The majority flips to the renter only below about 2.4%.
   - Treasury-bill interest on the renter's cash drops the buyer's share to about 2 in 3.

   So the video's answer is that rent isn't wasted by rule. Renting cost more than buying in most historical starts, but how many depends on the timing, the length of stay and the assumed rent.

3. Quote: "Her assumed rent, $1,667, is 56.8 percent of that. That's lower than in any start month on the street; the lowest was 57.9 percent, in July 2006."
   - Why: it doesn't say what a lower ratio means for Nina. I couldn't tell whether it's good or bad for buying, only that it echoes the bad 2006 start. The video then disclaims that it doesn't make 2026 another 2006, which leaves the point hanging.
   - A smaller one is the closing line, "her rent isn't wasted by rule; renting cost more than buying in most start months." It reads slightly contradictory at first, since "rent isn't wasted" and "renting cost more" sound opposed.

4. Quote: "For reference, the Census Bureau's vacancy survey puts asking rents between 4.83 and 5.59 percent of asking prices a year in its latest reports. Those are different baskets of empty homes, so it's a reference range, not Nina's own rent."
   - Why: it comes right after the 4% and 6% results, and it's a dense run of survey names and decimals. Two overlapping percentage ranges (rent as a share of price, then the buyer-win share) are hard to hold at once.

5. No to both. The video says "Nothing here says whether to buy or to keep renting" and "history, not a forecast." It never predicts future prices, rents or rates. It only reports what happened in past 10-year windows and what Nina's first month looks like next to them.

6. No direct advice. A viewer could take away several things:
   - Outcomes depended heavily on the start month, with the 2001–2007 stretch being the bad one.
   - Longer stays favored buying, and 15 years never lost.
   - The answer is sensitive to the rent you assume, so check your own rent-to-price ratio.
   - "Rent is money thrown away" isn't a safe rule, and neither is "buying always wins."

7. Mostly my own conclusion. The narration explicitly refuses to advise. The framing does lean one way, though: the lit street, the "every start month" 15-year result and the closing line all nudge toward "buying usually came out ahead." One bias is stated plainly but easy to miss. The renter's savings sit in cash, not stocks, which favors the buyer, and the video says it isn't answering the invest-the-difference question.

8. Partly. My question was whether renting costs more than buying once interest, property tax, insurance and repairs are counted. The video answers that for the past: in about 3 in 4 historical ten-year windows, buying came out ahead even after those costs and the 6% selling cost. It doesn't answer it for me in 2026, because Nina's window hasn't played out. Its most relevant hint is that the first-month cost is high relative to rent, which it declines to interpret. It also doesn't say whether I'd do better investing the difference in stocks.

### R2
1. The video follows Nina, an illustrative renter in September 2026 who has saved a 20% down payment and closing costs for a $400,000 home. She wonders whether her rent is wasted. It replays a buying twin and a renting twin from every start month between January 1991 and July 2016 (307 months), each followed for ten years, using real US prices, rents and mortgage rates. It then varies the stay length (5, 10 and 15 years) and the assumed starting rent (4%, 5% and 6% of price per year), and ends with the limits of the method.

2. Over ten years, the buyer ended ahead in about 3 in 4 of the 307 start months, and the renter ended ahead in 75. Every renter win falls between April 2001 and December 2007. The median buyer was about $157,000 ahead. The range runs from +$484,000 (April 2012) to -$82,385 (June 2006). The share depends on the rent assumed: 64.2% at 4%, 92.2% at 6%, and 73.6 to 87.3% across the Census range of 4.83 to 5.59%. Over 5 years it is 74.4%, and over 15 years the buyer won in every start month history allows. The video's conclusion is that rent isn't wasted by rule, and that renting cost more than buying in most start months, with the count depending on the assumed rent.

3. Two passages confused me.
- "Her assumed rent, $1,667, is 56.8 percent of that. That's lower than in any start month on the street; the lowest was 57.9 percent, in July 2006." It doesn't say what a lower ratio means for who wins. It seems to hint at a 2006-like outcome and then disclaims it.
- "renting cost more than buying in most start months". The measure was net wealth after ten years, so "cost more" is looser than what was computed.

I also noticed a small rounding mismatch: $197,760 minus $115,374 is $82,386, not $82,385.

4. The drop came here: "The house is a national price index, not one home, and the starting rent is an assumption. The rent history comes from the consumer price index for rent, CPI, which follows sitting tenants and can understate how fast market rents grew. No income taxes, no mortgage interest deduction, no refinancing; US only, and history, not a forecast." It is a dense list of caveats, and several of them had already been said earlier.

5. No. The video says outright that "Nothing here says whether to buy or to keep renting," and repeats that this is "history, not a forecast." It also says a lit share is not a promise for any one month, and that a 2026 start isn't 2006 again.

6. A viewer would not get direct advice. The takeaways they might draw are:
- Don't assume rent is automatically wasted.
- The start month mattered a lot, and nobody can see it in advance.
- Stay length matters, since short stays are riskier.
- The result is sensitive to the rent you assume, so check your own rent-to-price ratio.

7. These are mostly my own conclusions. The video showed the patterns (the dark stretch, the 5/10/15-year comparison, the rent tag turning) but deliberately declined to recommend anything. The closing line, "rent isn't wasted by rule", comes closest to a verdict, but it is framed as a description of the historical record.

8. Partly. My question was whether renting costs more than buying once interest, tax, insurance and repairs are counted. The video answered that for history: usually not, since buyers came out ahead in most ten-year windows, with a notable exception around 2001 to 2007. It also showed how much that depends on assumed rent and stay length. Three gaps remain:
- It can't say how a 2026 start will end.
- It uses a cash-only renter, so it leaves open whether investing the difference would do better.
- It leaves out taxes and the mortgage interest deduction.

### R3
1. The video follows Nina, a renter with a 20% down payment saved for a $400,000 home, and asks whether her rent is wasted. It replays a buying twin and a renting twin from every start month since 1991 (307 start months, each held ten years), using real prices, rents and mortgage rates. A "street" of lit and dark doors shows where the buyer ended ahead and where the renter did. It then tests shorter and longer stays and different starting rents, and ends with Nina's first-month numbers and the limits.

2. Renting cost more than buying in most start months, but not all, and the share depends on assumptions. At a 10-year hold and a starting rent of 5% of price per year, the buyer ended ahead in about 3 in 4 of 307 starts (the renter in 75). All the renter wins fall between April 2001 and December 2007; the buyer won in only 6 of the 72 starts from 2002 to 2007. The median buyer was about $157,000 ahead, the best case (April 2012) about $484,000 ahead, and the worst (June 2006) $82,385 behind. At five years the buyer won in 74.4% of starts, and at 15 years in every one. At a 4% rent the buyer won in 64.2% of starts and at 6% in 92.2%. The Census range of 4.83–5.59% gives 73.6–87.3%. The majority flips to the renter only below about 2.4%, and with T-bill interest on the renter's cash the buyer's share falls to about 2 in 3.

3. Two passages confused me.
   - "Counted along the whole street, the picture is this. In about 3 in 4 of the 307 start months, the buyer ended ahead. In the other 75, the renter did." It's hard to square: 75 of 307 is about 24%, so "3 in 4" fits, but the listener has to do that arithmetic, and the 6-of-72 figure earlier makes the 75 feel hard to place.
   - "Her assumed rent, $1,667, is 56.8 percent of that. That's lower than in any start month on the street; the lowest was 57.9 percent, in July 2006." It's unclear why this ratio matters or which direction is good for her. The video only says it "doesn't make 2026 another 2006," which leaves the point ambiguous.
   
   Also, "the renting twin's savings sit in cash, not in stocks" next to "the cash earns Treasury bill interest" in "one variant" leaves unclear what the base case earns (apparently nothing).

4. "Here is the part most people picture differently: the renting twin's savings sit in cash, not in stocks." My attention dropped most in the dense setup passage that follows it, through "nobody refinances." It is a long run of assumptions and exclusions (cash, T-bills, moving costs, renter's insurance, taxes, deduction, refinancing) delivered quickly with no visuals to anchor them.

5. No on both counts. The video says "Nothing here says whether to buy or to keep renting," and repeats "history, not a forecast." It describes only what happened from 1991 onward and doesn't project prices, rents or rates.

6. A viewer would probably take away that renting is not automatically wasted money, since the outcome depended on the start month, the hold length and the assumed rent. The takeaways are that buying usually came out ahead over 10+ years in this history, that short stays and buying near a price peak were the risky cases, and that the answer is sensitive to the rent assumption.

7. Mostly my own conclusion. The narration stays descriptive and disclaims advice. But the closing line, "renting cost more than buying in most start months," plus the framing that 15 years never lost, nudges a viewer toward "buying usually wins if you stay long." The "stay long" advice is my inference, and the video even says it "says nothing about how long Nina stays."

8. Partly. My question was whether renting costs more than buying once interest, tax, insurance and repairs are counted. The video answers that directly: in most historical 10-year windows buying ended ahead, even with those costs and selling costs included, and it shows when it didn't (2001–2007 starts). It doesn't settle my own case. The result depends on an assumed rent, on cash earning nothing, and on omitted taxes and the mortgage interest deduction. It also can't say how a September 2026 start will end. Its first-month comparison for Nina is the closest it gets, but it isn't interpreted.

### R4
1. The video follows Nina, a renter in September 2026 with enough saved for a 20% down payment on a $400,000 home, who wonders if her rent is wasted. It replays history with two twins, one who buys and one who rents and keeps the savings in cash, starting in each month from January 1991 to July 2016 and following each for ten years. It counts how often the buyer ended ahead, then tests how the result changes with the stay length (5, 10, 15 years) and the assumed starting rent. It closes by placing Nina's own first-month numbers beside the historical ones.

2. Renting cost more than buying in most start months, but it depends on assumptions. With a starting rent of 5% of price per year and a ten-year stay, the buyer ended ahead in about 3 in 4 of 307 start months (the renter in 75). The middle case had the buyer about $157,000 ahead. Every loss for the buyer fell between April 2001 and December 2007, and the worst was June 2006 (buyer $82,385 behind). At five years the buyer led in 74.4% of starts, and at fifteen years in all of them. At a 4% rent the buyer led in 64.2%, at 6% in 92.2%, and across the Census range of 4.83–5.59% in 73.6–87.3%. The majority flips to renting only below about 2.4%, and if the renter's cash earns T-bill interest, the buyer's share falls to about 2 in 3. So: her rent isn't wasted by rule, and how often buying wins depends on the rent she assumes.

3. "Is her rent money wasted?" and the closing line are fine, but one passage confused me: "In one variant, the cash earns Treasury bill interest, and nothing more." It's unclear whether the main results assume zero interest on the cash or something else. The later line "if the renter's cash earns Treasury bill interest, the buyer's share falls to about 2 in 3" implies the baseline earns nothing, but that is never said directly. Also, "Counted along the whole street... about 3 in 4" versus "73.6 to 87.3 percent" is easy to blur, since the 5% baseline figure isn't stated as a percentage.

4. "Of the 72 start months from 2002 through 2007, the buyer ended ahead in just 6." Attention dropped around the dense run of month ranges and counts (April 2001, December 2007, 2002–2007, 72, 6, then 2009 to mid-2016). The numbers come fast and the narration didn't pause to say what they meant for Nina.

5. No on both counts. The video says explicitly "Nothing here says whether to buy or to keep renting" and "history, not a forecast." It uses past home prices, rents and mortgage rates, and it says the 2026 start can't be finished by history.

6. A viewer would likely take away that the answer depends on timing, how long they stay, and the rent they'd pay. Staying short or buying into a falling market hurts the buyer, long stays helped in every historical window, and "rent is wasted" is not a rule. A viewer might also lean toward "buying usually wins," though the video doesn't say that as advice.

7. Mostly my own conclusion. The narration gave findings and conditions, and its only conclusion is that rent isn't wasted by rule and renting cost more in most start months. Takeaways like "stay longer" or "avoid buying near a peak" are my inference from the charts and numbers, not something the video told me to do. Its closing line leans toward "buying won more often," which could nudge a viewer.

8. Partly. My question was whether renting costs more than buying once interest, tax, insurance and repairs are counted. The count of 3 in 4 start months, with those costs included, plus the sensitivity to rent and stay length, answers that for history. It doesn't answer whether Nina's own 2026 purchase would win, whether investing the difference in stocks would beat buying (it explicitly excludes this), or how taxes and the mortgage interest deduction would change things.

### R5
1. The video follows Nina, a renter in September 2026 who has saved a down payment on a $400,000 home and wonders if her rent is wasted. It replays a buying twin and a renting twin from every start month since 1991 (307 start months, each followed for ten years), using real US prices, rents and mortgage rates. The renter's savings sit in cash, and the starting rent is assumed at 5% of price per year. It then shows which months favored the buyer (lit doors) and which the renter (dark doors), tests shorter and longer stays, turns the rent assumption up and down, and compares Nina's first-month numbers to history.

2. Over ten years, the buyer ended ahead in about 3 in 4 of the 307 start months (the renter in 75). The buyer won every start through the 1990s and every start from 2009 to mid-2016. The renter's wins all fall between April 2001 and December 2007; the buyer won only 6 of the 72 starts from 2002 to 2007. The middle start month had the buyer about $157,000 ahead, ranging from +$484,000 (April 2012) to -$82,385 (June 2006). At five years the buyer won 74.4%, and at 15 years every possible start. The rent tag moves the result: 64.2% at 4%, 92.2% at 6%, and 73.6 to 87.3% across the Census range. The majority flips only below about 2.4%. With T-bill interest on the renter's cash, the buyer's share falls to about 2 in 3. So the answer is: renting cost more than buying in most start months, but how many depends on the rent assumed, and the stretch of 2001 to 2007 went the other way.

3. "Of the 72 start months from 2002 through 2007, the buyer ended ahead in just 6." It sits next to "Every house where the renting twin came out ahead sits between April 2001 and December 2007." The first covers 2002 to 2007, the second begins in April 2001, and I couldn't tell how the 75 dark doors split between them without doing arithmetic. Also, "In one variant, the cash earns Treasury bill interest, and nothing more" is slightly confusing because it's unclear what the main version assumes (zero interest?), and the figure only appears again near the end. And "the tag drops below about 2.4 percent" is hard to picture, since the tag was introduced as a rent assumption, not a threshold.

4. "For reference, the Census Bureau's vacancy survey puts asking rents between 4.83 and 5.59 percent of asking prices a year in its latest reports. Those are different baskets of empty homes, so it's a reference range, not Nina's own rent." Attention dropped here because it's a stack of precise numbers and caveats about survey baskets, with no clear payoff until the next line gives the 73.6 to 87.3 percent result.

5. No. The video says explicitly that nothing in it says whether to buy or keep renting, and that it is history, not a forecast. It doesn't predict prices, rents or rates. It says Nina's September 2026 start can't be finished by history, and that her lower rent-to-payment ratio (56.8% versus a low of 57.9% in July 2006) compares first months only and doesn't make 2026 another 2006.

6. A viewer would likely take away that rent isn't automatically wasted money, that the outcome depends heavily on the start date, the length of stay (longer favors buying) and the assumed rent, and that a buyer can't know which "house on the street" they're in. Some would also read it as "buying usually came out ahead historically, especially if staying 10 to 15 years."

7. Partly the narration, partly my own conclusion. The closing line ("renting cost more than buying in most start months") and the lit-door visuals lean toward "buying usually wins," while the disclaimers explicitly refuse to recommend. The advice to stay longer is my inference from the 5, 10 and 15-year comparison, and the video even cautions that it says nothing about how long Nina stays.

8. Mostly yes, for the historical question: counting interest, tax, insurance, repairs and selling costs, buying beat renting in about 3 in 4 start months over ten years, with a dark stretch in 2001 to 2007. Two parts remained unresolved for me. It doesn't tell me what happens for a 2026 start, which is the one I care about. And the answer depends on an assumed rent and on the renter's savings sitting in cash rather than being invested, so it doesn't settle whether renting and investing the difference would beat buying.

### R6
1. The video follows Nina, a renter with enough saved for a down payment on a $400,000 home, who wonders whether paying rent is money wasted. It replays history with a buying twin and a renting twin starting in each month from 1991 to 2016, using real US prices, rents and mortgage rates, and compares them after ten years. It walks a "street" of 307 houses, one per start month. Most light up (the buyer ended ahead), with a dark stretch from 2001 to 2007. It then shows how the result shifts with the length of stay and the assumed starting rent.

2. In about 3 of 4 of the 307 start months (232, with 75 going to the renter), the buyer ended ahead after ten years, after all costs. The middle case was about $157,000 ahead for the buyer, the best was April 2012 at about $484,000, and the worst was June 2006 at $82,385 behind. Over five years the buyer won 74.4% of the time, and over fifteen years in every start month history allows. At a starting rent of 4% of price the buyer won 64.2%, and at 6%, 92.2%. The renter wins the majority only if the rent assumption falls below about 2.4%. Nina's closing answer is that the rent isn't wasted "by rule", and that renting cost more than buying in most start months, with the exact share depending on the assumed rent.

3. "In one variant, the cash earns Treasury bill interest, and nothing more." I wasn't sure whether the main case earns zero interest or something else, so the later line that the buyer's share "falls to about 2 in 3" was hard to place. I was also unsure about "Her assumed rent, $1,667, is 56.8 percent of that. That's lower than in any start month on the street." It wasn't clear why that ratio matters, or whether lower is good or bad for Nina.

4. "For reference, the Census Bureau's vacancy survey puts asking rents between 4.83 and 5.59 percent of asking prices a year in its latest reports." Several close decimal figures arrived in a row, followed by a caveat about different baskets, and it felt like a detour from the story.

5. No. It says outright that "Nothing here says whether to buy or to keep renting" and that this is "history, not a forecast." It makes no predictions about prices, rents or rates. It only compares Nina's first-month payment with past first months.

6. Not a direct recommendation. A viewer could take away that the answer depends heavily on when you start, how long you stay, and what rent you assume, and that short stays and bad timing, like the mid-2000s, are where renting won. A viewer might also hear that buying usually came out ahead historically, especially over long stays.

7. The narration suggested only the conditional takeaways: timing, stay length and the rent assumption all matter. Anything stronger, like "buying is usually better", is my own conclusion, and the video explicitly disclaims it. The final line, "renting cost more than buying in most start months", leans that way without telling the viewer what to do.

8. Partly. I came with "is paying rent wasted money?" and the street of houses and the closing answer address that for historical US cases. It doesn't resolve it for Nina's actual September 2026 situation, which is unknowable, and it ignores the question of investing the difference.
