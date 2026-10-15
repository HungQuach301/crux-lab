# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
**Đúng câu hỏi** (câu 1–2): video hỏi nếu Nina (người thuê, minh hoạ) **thuê và đầu tư phần chênh** (cọc + chênh hằng tháng) vào cổ phiếu Mỹ thì có hơn **mua nhà** không, qua hai người giống hệt phát lại trên lịch sử thật của Mỹ.
**Đúng đáp án** (câu 2): với quỹ ở cổ phiếu, người mua còn hơn ở **khoảng một nửa** số tháng bắt đầu (so với khoảng 3/4 khi để tiền mặt); **và** ít nhất một trong: 15 năm thì người thuê-đầu-tư hơn phần lớn (người mua chỉ ~1/5) / dãy 2002–2007 tối hết / kết quả **đổi theo tiền thuê giả định** (thẻ 5 %, ngưỡng ~5,1 %) / không để dành chênh hằng tháng thì người mua hơn ~2/3 / lý do đòn bẩy (nhà lớn lên trên cả giá, quỹ bắt đầu từ $92,000). Đủ câu hỏi + đáp án → 1; một trong hai → 0,5; không → 0. Kể "đầu tư luôn thắng" / "mua luôn thắng" hay "video bảo nên…" → không được 1.
**Câu khuyên (A28):** `advice_stated` khi câu 5 "yes" vì tin video bảo mua/thuê/đầu tư hoặc dự báo, **hoặc** câu 6–7 nêu lời khuyên hành động MÀ người đọc nói video gợi ra. `advice_inferred`: người đọc tự suy (câu 7 "my own conclusion"). `caution_only`: thận trọng chung. Người đọc **đúng** = điểm 1 và không `advice_stated`.
**Danh sách từ dễ đọc thành lời khuyên:** `advice_words` = mọi cụm người đọc TRÍCH từ lời video làm căn cứ lời khuyên.
**Khối mất chú ý** (câu 3–4): xếp vào `phương pháp` / `định nghĩa` / `số dày` / `nhân vật` / `khác` / `không`, ghi cảnh ước (trích vài chữ).
**Câu hỏi mang tới** (câu 8): `answered_own`: true/false/partly.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, "advice_words": ["..."], "attention_block": "phương pháp|định nghĩa|số dày|nhân vật|khác|không", "attention_where": "<quote>", "answered_own": "true|false|partly", "why": "<one line>"}, ...}

### R1
1. The video follows Nina, a renter with $92,000 saved, who is weighing buying a roughly $400,000 house against renting and investing the difference. It replays every start month from 1991 to July 2016 (307 ten-year windows) as a street of houses, lit if the buyer ends ahead and dark if the renting twin does. The renter's pile is the $92,000 plus each month's gap between owning costs and rent, invested in the whole US stock market. The result is that buying wins about half the time over ten years, far less over fifteen years, and the answer hinges on an assumed rent of 5% of price per year.

2. Over ten years, with the renter's pile in stocks, the buyer finished ahead in 152 of 307 start months (about half). With the pile in cash, the buyer won about 3 in 4. Over fifteen years with stocks, the buyer won only about 1 in 5 of 247 starts, while with cash the buyer won every time. If only the $92,000 is invested and no monthly gap, the buyer wins about 2 in 3. With 1% annual fees, the lit share rises to 55%. The split sits near a 5.1% rent tag, so the verdict is essentially a coin flip that the rent-to-price assumption tips.

3. Two passages confused me:
- "Over ten years, stocks outgrew homes almost nine times in ten." This sounds like renting should nearly always win, and the video only resolves that much later (the mortgage leverage point). Until then it felt contradictory.
- "Last time, with the pile in cash, the darkest house was one bought near the top." and "The brightest house last time still glows." They refer to an earlier video or scene I haven't seen, so I didn't know what "last time" meant.
- Also mildly confusing: "Every house that changed sides went from the buyer to the renter, never the other way." I had to think about what "changed sides" compared against (cash versus stocks).

4. "Last time, with the pile in cash, the darkest house was one bought near the top. With stocks, that buyer ends more than a quarter of a million dollars behind. The dark house got darker." My attention dropped here because it relies on a "last time" I don't have, and it's a single-house anecdote after a long stretch of the street metaphor, so I couldn't picture or place it.

5. No. The video says explicitly that it is history and not a forecast, that it doesn't rank stocks above a house or the reverse, and that the half is "a count of what already happened, not a promise about Nina's month." It also lists limits: US only, no taxes, renters who never skip a month. It doesn't predict home prices, rents or stock returns.

6. There is no direct advice. A viewer could take away that "rent and invest the difference" isn't a sure win, since historically it was about even over ten years. Longer stays favored the renter's invested pile, so how long you'd stay matters. The monthly habit of investing the gap did most of the catching up, and your local rent compared with roughly 5% of the home price decides the outcome. For a $400,000 home that tag is about $20,000 a year, or around $1,667 a month.

7. That is my own conclusion. The narration stayed descriptive and even disclaimed advice ("None of this ranks stocks above a house"). Its closing line, "her rent tag tips it," points to what matters but doesn't tell anyone what to do.

8. Partly. It answered "does she really end up ahead?" with "not reliably: about half the time over ten years, less often over fifteen, and it depends on the rent tag." That is a useful correction to the slogan. It didn't give me a verdict for my own situation, because it can't say how long I'll stay, what my local rent-to-price ratio is, or whether I'd really invest every month through crashes. The most useful parts were the leverage explanation (the house grows on the full $400,000, the pile on $92,000) and the sensitivity to the rent assumption.

### R2
1. The video follows Nina, a renter with $92,000 saved, who wonders whether renting and investing the difference beats buying. It compares a "buying twin" with a "renting twin" across every start month since 1991, drawn as a street of houses that are lit if the buyer ends ahead and dark if not. It first shows that the renter's pile is the down payment plus every monthly savings gap, then that outcomes depend on the era, the length of stay, and the assumed rent. It ends by saying the result is roughly a coin flip, with the rent assumption tipping it.

2. Over 10 years, with the renter's money in the whole US stock market, the buyer ended ahead in 152 of 307 start months (about half). With the pile in cash, the buyer won about 3 in 4. Over 15 years, with stocks, the buyer won only about 1 in 5 of 247 starts, and with cash, in all of them. The result is sensitive to the assumptions:
   - Rent set at 5% of the price per year splits the street almost exactly in half, with the break-even near 5.1%.
   - Investing only the $92,000, with no monthly gap, puts the buyer ahead in about 2 in 3 start months.
   - A 1% annual fee on the renter's pile raises the buyer's lit share to 55%.
   
   So investing the difference does not reliably leave you ahead.

3. Several passages confused me:
   - "Last time, with the pile in cash, the darkest house was one bought near the top." Also "The brightest house last time still glows." They refer to a previous video I haven't seen.
   - "For a short run of start months, a dollar in stocks was worth less than a dollar ten years on." It reads backwards, and I had to reinterpret it as stocks being lower after ten years.
   - The $92,000 is described as a 20% down payment on a roughly $400,000 house, but 20% would be $80,000. The extra $12,000 (presumably closing costs) is never explained.
   - "Those houses stay lit" and "the street goes dark" are hard to track alongside "about two in three of the 1990s houses stay lit" and "the darkest house is the very first one."

4. "The rest of the limits are on the card: US only, history, not a forecast, no taxes on gains or on the home, and renters who never skip a month." My attention dropped there because it's a rapid list of disclaimers that depends on an on-screen card, so spoken alone it blurs.

5. No. It says outright that this is "history, not a forecast." It also says "None of this ranks stocks above a house, or a house above stocks," and that stability and control aren't counted. It makes no predictions about prices, rents, or returns.

6. The video gives no direct advice. A viewer could take away that "rent and invest the difference" is not a sure win. The outcome depends on:
   - the local rent-to-price ratio;
   - how long you'll stay;
   - whether you really invest the monthly gap through crashes;
   - fees and taxes.
   
   The best use is to plug your own rent and time horizon into a calculator.

7. That advice is my own conclusion. The narration lays out the findings and the sensitivities, such as "the answer sits on the rent tag, and the tag is an assumption." It never tells the viewer what to do.

8. Partly. It answered "does she really end up ahead?" with: not reliably, about half the time over 10 years and mostly not over 15 years when the buyer has the mortgage leverage. It explained why with the point that the house grows on the full $400,000 while the pile starts at $92,000. It did not tell me what happens for my own city's rent-to-price ratio or for how long I'd stay, so I'd have to work that out myself.

### R3
1. The video follows Nina, a renter with $92,000 saved, who asks whether renting and investing the difference beats buying a $400,000 house with 20% down. It replays every start month from 1991 to July 2016 (307 ten-year windows) as a street of houses, lit if the buyer ends ahead and dark if the renting twin's pile does. It first shows cash vs. stocks for the pile, then walks the street by era, then tests stay length, the monthly-saving habit, fees, and the rent assumption. It ends by saying the result is close to a coin flip and hinges on the rent tag.

2. Specifically: with the renter's money in stocks (all deposits invested monthly, no fees or taxes), the buyer ended ahead in 152 of 307 ten-year starts, about half. With cash, the buyer won about 3 in 4. Over fifteen years with stocks, the buyer won only about 1 in 5 (cash: all 247). The answer is "it depends": roughly a coin flip at 10 years, and it tips on the assumed rent of 5% of price per year (the split sits near 5.1%). Stocks beat home prices about 9 in 10 times, yet the buyer still won half, because the mortgage leverages a $400,000 house against the renter's $92,000 start.

3. "Over ten years, stocks outgrew homes almost nine times in ten." followed by "Stocks outgrew the house almost nine times out of ten, yet buying still came out ahead in half." This is confusing at first because it sounds contradictory, though it gets resolved later with the leverage explanation. Also confusing: "Nina's own month isn't on the street; its ten years are still ahead of her," which is a bit cryptic, and "Every house that changed sides went from the buyer to the renter," which assumes I remember the cash version. "Last time" is also referenced repeatedly, as if there was a previous video I didn't see.

4. "Dark doors don't mean the renting twins had an easy ride. Along the way, many of the stock piles dipped below where they started. One renting twin's pile sank to $54,310, and she kept investing." My attention dropped there because it's a side note about the emotional side of investing in the middle of the main tally, and the numbers pile up quickly. The "Last time..." passages, which rely on a video I haven't seen, also lose me.

5. No. It explicitly says it's history, not a forecast, that it doesn't rank stocks above a house or the reverse, and that a home also offers stability and control which numbers don't capture. It lists limits: US only, no taxes, renters who never skip a month.

6. A cautious viewer would take away: "rent and invest the difference" is not a sure win; it works only with discipline (investing every month, even through drops), a long horizon, and a rent that's low enough relative to home price. If the rent is well under about 5% of the price annually, renting and investing looks better, and if above, buying does. Staying longer favored the renter's pile in stocks, while shorter stays or a cash pile favored the buyer. Check your own local rent-to-price ratio.

7. Mostly my own conclusion. The narration avoids recommending anything and frames the result as a coin flip. But the closing line, "her rent tag tips it," and the 5.1% threshold strongly imply the "check your rent-to-price ratio" takeaway, so that is a light nudge from the video, while the specific advice is my inference.

8. Partly. My question was whether a renter who invests the difference really ends up ahead. The video answered that historically it's about 50/50 at ten years, better for the renter at fifteen years, and sensitive to rent level, which is a useful, honest answer. It didn't give me a definite yes, and it can't tell me about my own market, taxes, or timing. The strongest parts were the stock-vs-house leverage explanation and the "no monthly saving" test showing that the monthly habit did most of the renter's catching up.

### R4
1. **Summary:** The video follows Nina, a renter with $92,000 saved, who wonders whether renting and investing the difference beats buying a $400,000 home. It replays every start month from January 1991 to July 2016, 307 ten-year windows, as houses on a street. A house is lit if the buyer ends ahead and dark if the renting twin's pile does. It compares the renter holding cash, holding stocks, and then tests other stay lengths and assumptions (no monthly investing, 1% fees, different rents). The conclusion is that with stocks the result is about a coin flip, and the assumed rent decides it.

2. **The answer:** It depends, and by history it is roughly even. Over ten years with the pile in stocks, the buyer ended ahead in 152 of 307 start months (about half). With the pile in cash, the buyer won about 3 in 4. Over fifteen years, the buyer won every time against cash and only about 1 in 5 times against stocks. The result is sensitive to the assumptions:
   - Investing only the $92,000, with no monthly gap, puts the buyer ahead about 2 in 3 times.
   - A 1% annual fee on the pile raises the buyer's lit share to 55%.
   - The split is almost exactly 50/50 at a rent of 5% of price per year, with the break-even near 5.1%.

3. **Confusing passages:**
   - "Over ten years, stocks outgrew homes almost nine times in ten." This is followed by "the buyer led only about half the time." On first hearing it sounds contradictory. The explanation (leverage, a $400,000 base versus $92,000) only comes near the end.
   - "Last time, with the pile in cash, the darkest house was one bought near the top. With stocks, that buyer ends more than a quarter of a million dollars behind." It refers to a previous video I haven't seen. It also sits oddly next to the earlier claim that the first house, at $485,063 behind, is the darkest on the street.
   - "The split sits near 5.1 percent, and public rent data from the Census Bureau falls on both sides of it." It never says which real rents fall on which side, so I can't tell where I land.
   - "no taxes on gains or on the home" is vague about whether property tax and mortgage interest are included.

4. **Attention drop:** "The rest of the limits are on the card: US only, history, not a forecast, no taxes on gains or on the home, and renters who never skip a month." It is a quick spoken list that points to an on-screen card, and it follows several abstract passages in a row, so it was easy to tune out.

5. **Buy/rent/invest advice or predictions:** No. It says "None of this ranks stocks above a house, or a house above stocks," and it labels the work "history, not a forecast." It does not predict home prices, rents, or stock returns. It says a home also brings stability and control, which numbers don't capture.

6. **Advice a viewer might take:**
   - "Rent and invest the difference" is not a guaranteed win. It was roughly a coin flip over ten years and favored the investor over longer stays.
   - Check your local rent-to-price ratio against about 5% a year.
   - Think about how long you will stay.
   - Rent-and-invest only works if you keep investing every month, even through drops, and the monthly habit did most of the work.
   - Fees and taxes tilt things toward buying.

7. **Source of the advice:** It is my own conclusion. The narration avoids recommending anything and presents only the levers (rent tag, horizon, monthly investing, fees). The final line, "investing the difference made her street a coin flip, and her rent tag tips it," is a finding, not a recommendation.

8. **Did it answer my question?** Partly. It answered "does she really end up ahead?": not reliably. Historically it was about half the time over ten years, and more often over fifteen. It did not tell me what to do, and it can't say whether my rent falls above or below the break-even without my own rent and price figures. The best parts were the explanation of why buying holds up (the house grows on the full price, not just the down payment) and the test showing that the monthly investing habit matters most.

### R5
1. **Summary.** The video follows Nina, a renter with $92,000 saved, who asks whether renting and investing the difference beats buying a roughly $400,000 house. It replays every start month from 1991 through July 2016 (307 ten-year windows) as a street of houses. A house is lit if the buyer ends ahead and dark if the renter does. It first shows the renter holding cash, where the buyer mostly wins. Then it puts the renter's money in the whole US stock market, where the street splits roughly in half. It finishes by testing the longer stay, fees, no monthly saving, and the rent assumption.

2. **The answer.** It depends, and on a ten-year stay it is close to a coin flip.
   - **Ten years, stocks:** the buyer was ahead in 152 of 307 start months, about half.
   - **Ten years, cash:** the buyer was ahead in about 3 in 4.
   - **Fifteen years, stocks:** the buyer was ahead in only about 1 in 5. With cash, the buyer was ahead in all 247 windows.
   - **Why the split:** stocks beat home prices about 9 times in 10, but the mortgage lets the house grow on the full $400,000 while the renter starts with $92,000. The renter catches up through monthly investing and time.
   - **What tips it:** the rent assumption of 5% of price per year. The break-even is near 5.1%.
   - **Other tests:** no monthly saving puts the buyer ahead in about 2 in 3 windows, and a 1% fee puts the lit share at 55%.

3. **Confusing passages.**
   - "For a short run of start months, a dollar in stocks was worth less than a dollar ten years on." It's unclear whether this means stocks lost money over ten years, and whether that is in real or nominal terms.
   - "Last time, with the pile in cash, the darkest house was one bought near the top." Also "The brightest house last time still glows." I haven't seen a previous video, so these references to "last time" mean nothing to me.
   - "The split sits near 5.1 percent, and public rent data from the Census Bureau falls on both sides of it." This doesn't tell me which side I'm likely on.
   - $92,000 saved against a $400,000 house isn't explained, since 20% down would be $80,000. I assume the rest covers closing costs, but it isn't said.

4. **Where attention dropped most.** "Last time, with the pile in cash, the darkest house was one bought near the top. With stocks, that buyer ends more than a quarter of a million dollars behind. The dark house got darker." The "last time" callbacks lean on a video I haven't seen. The walkthrough of individual houses is also long and pulls me away from the central question.

5. **Does it advise or predict?** No. It says directly that it is "history, not a forecast." It says "None of this ranks stocks above a house, or a house above stocks," and it lists its limits: US only, no taxes, and renters who never skip a month. It describes what happened and does not say what will happen.

6. **Advice a viewer could take.**
   - Don't assume "rent and invest the difference" automatically wins. Historically it was roughly even over ten years.
   - The renter's edge comes mostly from investing the monthly gap consistently, and from a longer horizon.
   - Check how your own rent compares with about 5% of the home price per year.
   - Remember that fees, taxes, and stopping during a crash all hurt the renter.
   - Non-financial factors like stability and control also matter.

7. **Source of the advice.** Mostly my own conclusion. The video states facts and conditions: longer stays favored the pile, the rent tag decides, and the monthly habit did most of the work. It avoids telling the viewer what to do, so the practical takeaways are my inference.

8. **Did it answer my question?** Partly. It answered "does the renter really end up ahead?" with "about half the time at ten years, usually yes at fifteen, depending on rent." That is a clear, honest answer to the general question, and the explanation of why a slower-growing house keeps up was the most useful part. It didn't answer it for my situation, because it never helps me work out whether my local rent-to-price ratio is above or below 5.1%. It also doesn't say how long I should expect to stay.

### R6
1. The video follows Nina, a renter with $92,000 saved, who asks whether renting and investing the difference beats buying a roughly $400,000 house. It replays every start month since 1991 as a street of houses, lit if the buyer ends ahead and dark if the renter does. It first shows the result with the renter's money in cash, then in stocks, and then tests longer stays, no monthly saving, fees, and the assumed rent. The conclusion is that with stocks the street is about half lit, and the rent assumption tips it.

2. Over ten years, with the renter investing the $92,000 plus the monthly cost gap in the whole US stock market, the buyer ended ahead in 152 of 307 start months, about half. With cash the buyer won about 3 in 4. Over fifteen years with stocks, the buyer won only about 1 in 5 of 247 starts, while cash left the buyer ahead every time. The answer hinges on the assumed rent of 5% of price per year; the split sits near 5.1%.

3. "Over fifteen years, cash kept the buyer ahead every time; stocks, only about 1 in 5." comes in the opening before the setup is explained, so the numbers float without context. Also "Last time, with the pile in cash, the darkest house was one bought near the top" and "The brightest house last time still glows" refer to a previous video I haven't seen. Also "Every house that changed sides went from the buyer to the renter" is a bit abstract without a visual. And "Over a shorter stay... the buyer was ahead a little more than half the time" is unclear: shorter than what, and it contradicts the preceding sense that the half is the ten-year result.

4. "The brightest house last time still glows. With stocks, that buyer still ends well ahead. She bought after prices had fallen, and her house rose on its whole price, not just on her $92,000." My attention dropped there because it depends on the prior video, and it interrupts the walk along the street with a side detail about one house.

5. No. It says explicitly that it "ranks neither stocks above a house nor a house above stocks," that it is history and not a forecast, and it lists limits such as US only, no taxes, and renters who never skip a month. It makes no predictions of home prices, rents or stock returns.

6. The takeaway is mostly "it depends": the answer is close to a coin flip at a ten-year horizon and is sensitive to the rent-to-price ratio, how long you stay, and whether you actually invest the monthly gap. A viewer might conclude that they should check their own local rent against price, expect to stay long if renting and investing, and that the buyer's leverage on the whole house is the reason buying holds up. Nothing is prescribed.

7. This is largely my own conclusion. The narration frames findings and says outright that it isn't advising, though its final line, "investing the difference made her street a coin flip, and her rent tag tips it," points toward checking one's own rent, which is as close as it comes to a suggestion.

8. Yes, mostly. I came wanting to know whether renting and investing the difference beats owning, and the ten-year result (about half), the fifteen-year result (mostly renter), and the rent sensitivity answered that directly. It did not tell me what Nina should do, since her stay length and actual rent are unknown.
