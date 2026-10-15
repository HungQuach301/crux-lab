# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
**Đúng câu hỏi** (câu 1–2): video hỏi nếu Nina (người thuê, minh hoạ) **thuê và đầu tư phần chênh** (cọc + chênh hằng tháng) vào cổ phiếu Mỹ thì có hơn **mua nhà** không, qua hai người giống hệt phát lại trên lịch sử thật của Mỹ.
**Đúng đáp án** (câu 2): với quỹ ở cổ phiếu, người mua còn hơn ở **khoảng một nửa** số tháng bắt đầu (so với khoảng 3/4 khi để tiền mặt); **và** ít nhất một trong: 15 năm thì người thuê-đầu-tư hơn phần lớn (người mua chỉ ~1/5) / dãy 2002–2007 tối hết / kết quả **đổi theo tiền thuê giả định** (thẻ 5 %, ngưỡng ~5,1 %) / không để dành chênh hằng tháng thì người mua hơn ~2/3 / lý do đòn bẩy (nhà lớn lên trên cả giá, quỹ bắt đầu từ $92,000). Đủ câu hỏi + đáp án → 1; một trong hai → 0,5; không → 0. Kể "đầu tư luôn thắng" / "mua luôn thắng" hay "video bảo nên…" → không được 1.
**Câu khuyên (A28):** `advice_stated` khi câu 5 "yes" vì tin video bảo mua/thuê/đầu tư hoặc dự báo, **hoặc** câu 6–7 nêu lời khuyên hành động MÀ người đọc nói video gợi ra. `advice_inferred`: người đọc tự suy (câu 7 "my own conclusion"). `caution_only`: thận trọng chung. Người đọc **đúng** = điểm 1 và không `advice_stated`.
**Danh sách từ dễ đọc thành lời khuyên:** `advice_words` = mọi cụm người đọc TRÍCH từ lời video làm căn cứ lời khuyên.
**Khối mất chú ý** (câu 3–4): xếp vào `phương pháp` / `định nghĩa` / `số dày` / `nhân vật` / `khác` / `không`, ghi cảnh ước (trích vài chữ).
**Câu hỏi mang tới** (câu 8): `answered_own`: true/false/partly.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, "advice_words": ["..."], "attention_block": "phương pháp|định nghĩa|số dày|nhân vật|khác|không", "attention_where": "<few words>", "answered_own": "true|false|partly", "why": "<one line>"}, ...}

### R1
1. The video follows Nina, a renter with $92,000 saved, who wonders whether renting and investing the difference beats buying a roughly $400,000 house. It replays twin scenarios (one buys, one rents) from every start month since 1991, first with the renter's money in cash, then in the whole US stock market, with each start month shown as a lit or dark house on a street. It then tests variations: shorter and longer stays, no monthly gap invested, fees, and the assumed rent level. It ends by saying the result depends heavily on holding period and on the rent assumption.

2. With a ten-year stay and the renter's pile in stocks, the buyer ended ahead in 152 of 307 start months, about half. With cash, the buyer led about 3 in 4. Over fifteen years with stocks, the buyer led only about 1 in 5 (cash: every time). Over a stay half as long, the buyer led a little over half. Results cluster: starts from 2002 to 2007 were all dark, while 2009 to mid-2016 were lit nearly 4 in 5. The split sits near a 5.1 percent annual rent-to-price assumption, so the answer is essentially a coin flip at ten years that the rent assumption tips. Only investing the $92,000 (no monthly gap) puts the buyer ahead in about 2 in 3; 1 percent fees raise the lit share to 55 percent.

3. "Over a stay half as long, with the pile in stocks, the buyer was ahead a little more than half the time. A short stay is close to a coin toss; longer stays tilt toward the pile." This is confusing because "half as long" is never stated as five years, and it sits right after a ten-year result that is also "about half," so the two halves blur together. Also: "Longer stays favored the pile; the rent tag is the one assumption left to test." This wording is odd because earlier the video had already listed several other assumptions (fees, no monthly gap) and "one assumption left" is unclear. And "the buyer's house grows on all $400,000 of it" is stated without the price being introduced earlier.

4. "Every cost of owning stays the same, and the card lists each one." My attention dropped there because it refers to an on-screen card whose contents the narration doesn't say, so listeners get no actual information, and it comes between more interesting results. The following "The rest of the limits are on the card" has the same issue.

5. No. The video says explicitly that it is history, not a forecast, and that "None of this ranks stocks above a house, or a house above stocks." It mentions that a home also gives stability and control, which the numbers don't count. It makes no predictions of future prices, rents or returns.

6. A viewer could take away several cautions, not a directive. "Rent and invest the difference" is not a sure win; at ten years it was roughly a coin flip historically. The longer you stay, the better the stock pile has done relative to the house. The result is sensitive to the local rent-to-price ratio (about 5.1 percent was the tipping point), to when you buy, and to whether you actually invest the monthly gap without stopping in downturns. Fees and taxes would shift things.

7. Mostly my own conclusion. The narration presents these as findings and limits, and explicitly declines to rank buying versus investing. The lines closest to guidance are "A short stay is close to a coin toss; longer stays tilt toward the pile" and "the monthly habit, not the one big deposit, did most of the renter's catching up," which are observations about the historical replay, but the video doesn't tell the viewer what to do.

8. Partly. My question was whether a renter who invests the difference ends up ahead of a buyer. The video answered that for historical data: at ten years, about half the time, with strong dependence on start date, stay length (more favorable to renting at 15 years) and the rent assumption. It did not settle the question for a 2026 renter, since it says Nina's own month isn't on the street and results aren't a forecast. The part that answered most directly was the 152 of 307 count and the fifteen-year result; the part that left it open was the rent-tag sensitivity.

### R2
1. The video follows Nina, a renter with $92,000 saved, and asks whether renting and investing the difference beats buying a $400,000 house. It replays twin renters and buyers from every start month since 1991, with the renter putting her $92,000 plus each month's cost gap into the total US stock market. It compares outcomes at 10 and 15 years, with the pile in cash versus stocks, then tests how sensitive the result is to saved gaps, fees, and the assumed rent. It ends by saying the street is a coin flip at ten years and that the rent tag tips it.

2. At ten years, with the pile in stocks, the buyer ended ahead in 152 of 307 start months (about half), even though stocks outgrew home prices about 9 in 10 times. With cash, the buyer was ahead about 3 in 4 times. Over fifteen years, stocks left the buyer ahead only about 1 in 5 times, versus every time with cash. The result depends on the assumed rent (5% of price per year); the split is near 5.1%, so it is a coin flip at ten years and favors the renter's pile over longer stays.

3. "Over ten years, stocks outgrew home prices about 9 in 10 times. So you'd expect renting and investing to come out ahead of buying a house." It's not confusing so much as it sets up a puzzle the video only resolves much later (leverage on $400,000 versus $92,000). A second spot: "Nina's own month isn't on the street; its ten years are still ahead of her." That sentence is a bit abstract on first hearing. Also, "Over a stay half as long... A short stay is close to a coin toss" is slightly muddled, since the 5-year result appears with little setup.

4. "Every cost of owning stays the same, and the card lists each one." My attention dropped there because the narration points to an on-screen card without saying what is on it, so listeners get no information from audio alone. The assumptions section is also a dense stretch.

5. No. It states it is history, not a forecast, and that it doesn't rank stocks above a house or the reverse. It notes home ownership brings stability and control that numbers don't capture, and it makes no predictions about future prices, rents, or returns.

6. Mostly conditional lessons: the answer depends on how long you'd stay, whether you actually invest the monthly gap and never stop, fees, and the local rent-to-price ratio. A viewer might take away that "rent and invest the difference" is not a sure win at ten years, that longer stays favor the pile, and that rent level matters most. The advice is implicit; the video does not state it.

7. It is mostly my own conclusion. The narration presents findings and caveats, and it explicitly declines to rank the options, so the takeaways above are inferred from the results.

8. Partly. It answered whether she "really ends up ahead": historically, not reliably. It is a coin flip at ten years and usually ahead at fifteen, with the rent assumption deciding the near-even case. It did not tell me what to do or what will happen in my own market, so for my situation it gave a framework rather than a verdict.

### R3
1. The video follows Nina, a renter with $92,000 saved, and the choice between buying a house and renting while investing the difference. It replays "twins" (one buys, one rents and puts the down payment plus each month's cost gap into US stocks) from every start month since 1991. It shows each ten-year start as a lit or dark house on a street: lit if the buyer ends ahead, dark if the renter does. It then walks through the eras, tests a few assumptions (no monthly savings, fees, the rent level, stay length), and ends on the point that the result hinges on the assumed rent.

2. Over ten years with the renter's money in stocks, the buyer came out ahead in 152 of 307 start months, about half, so it is a coin flip. Other results:
   - With the renter's pile in cash, the buyer won about 3 in 4.
   - Over fifteen years with stocks, the buyer won only about 1 in 5.
   - Over five years with stocks, the buyer won a little more than half the time.
   - If the renter invests only the $92,000 and no monthly gap, the buyer wins about 2 in 3.
   - With a 1% annual fee on the renter's pile, the buyer wins 55%.
   - The result flips near a rent of about 5.1% of the price per year; at the assumed 5% the street splits almost exactly in half.

   Renting and investing doesn't reliably win, even though stocks beat home prices about 9 in 10 times. The mortgage lets the house grow on the full $400,000 rather than on $92,000.

3. "A lot of rent-versus-buy math assumes one growth rate; this replays the real record, month by month." It is a clear idea, but it came out of nowhere between scenes. Other spots that confused me:
   - "June 2006 was the darkest house last time" and "April 2012 was the brightest house last time." I didn't know what "last time" referred to, since I hadn't seen an earlier video.
   - $92,000 is called the down payment, yet the house is "all $400,000 of it," and 20% of $400,000 is $80,000. The gap is never explained (maybe closing costs).
   - "Every cost of owning stays the same, and the card lists each one." The card is on screen, so the narration alone doesn't tell me what's on it.

4. "A few years later, the market itself stalled. In a short run of start months around March 1999, a dollar in stocks was worth less than a dollar ten years on." My attention dropped here because the walk through individual eras felt like trivia about narrow windows. It didn't connect to my own situation, and it came right after the first-house example had already made the point.

5. No. The video says outright that it is "history, not a forecast" and that "none of this ranks stocks above a house, or a house above stocks." It makes no prediction about future home prices, rents or stock returns, and it notes that stability and control aren't counted.

6. A viewer could take away several things:
   - "Rent and invest the difference" is not a sure win.
   - The result depends heavily on how much cheaper renting is than owning, so check your own local rent against the price.
   - Stay length matters: short stays are close to a coin toss, and longer stays have historically favored the stock pile.
   - The renter has to keep investing every month through crashes, since the monthly gap did most of the work.
   - Fees and taxes shift things toward buying.

7. It's mostly my own conclusion. The video states findings and caveats, such as "longer stays tilt toward the pile" and "her rent tag tips it," but it never says what a viewer should do. I turned those findings into the checklist in answer 6.

8. Partly. It answered "does she end up ahead?" with "about half the time over ten years, and more often renting over fifteen." That is a useful, honest answer, and the bit about leverage explained why the stock-beats-houses headline doesn't settle it. It didn't answer it for me specifically, because it can't know my rent, my price, or how long I'll stay. It also left me with a rent-to-price threshold of about 5.1% but no easy way to check it against real local numbers.

### R4
1. The video is about Nina, a renter with $92,000 saved who is deciding whether to buy a $400,000 house or keep renting and invest the difference. It replays two "twins", one who buys and one who rents and puts the savings and the monthly cost gap into the whole US stock market. It does this for every start month since 1991 and shows each as a lit door (buyer ahead) or dark door (renter ahead). It first shows that stocks beat home prices about 9 in 10 times over ten years, yet the buyer still ends ahead in about half the start months. It then explains why (the mortgage lets the house grow on the full $400,000), tests longer stays and other assumptions, and ends on the rent assumption as the tiebreaker.

2. Over ten years, with the renter's pile in stocks, the buyer ended ahead in 152 of 307 start months, about half, so it's roughly a coin flip. With the pile in cash, the buyer won about 3 in 4 times. Over five years the buyer was ahead a little more than half the time. Over fifteen years the buyer was ahead in only about 1 in 5 starts, versus every time with cash. The result depends on the rent assumption: at 5% of the price per year the split is almost exactly even, and the tipping point is about 5.1%.

3. Several passages confused me:
- "With Nina's renting twin holding cash, the buyer ended ahead about 3 in 4 times." Nina was just introduced as a renter, and then a "twin" appears without explanation.
- "June 2006 was the darkest house last time" and "April 2012 was the brightest house last time, and it still glows." "Last time" refers to something I haven't seen, and "still glows" is unclear.
- "The renting twin's rent is an assumption, the tag on her door: 5 percent of the price a year, as of July 2026, and later, that tag decides." The "as of July 2026, and later" is hard to parse.
- "Over a stay half as long... the buyer was ahead a little more than half the time." I had to work out that this means five years, and it's unclear why it appears after the ten-year walk-through.
- "Half a street, lit in stretches; now, a longer stay." This is cryptic as a transition.
- The 15-year result is stated twice, early and later, which made me wonder whether they were different findings.

4. "Every cost of owning stays the same, and the card lists each one." My attention dropped because it points to a visual card without saying what's on it, so a listener gets nothing from it. It also comes right after a line about one growth rate versus the real record that didn't land for me.

5. No. It says "It's history, not a forecast," and "None of this ranks stocks above a house, or a house above stocks." It also notes that a home brings stability and control that numbers don't capture. It makes no predictions about future prices, rents or returns.

6. There's no direct advice. The takeaways a viewer could draw are conditional:
- The outcome depends heavily on how long you stay (longer favors renting and investing).
- It depends on your actual rent relative to the home price.
- It depends on whether you really invest the monthly gap every month, including through crashes.
- Real costs like fees and taxes shift results.
- Don't assume stocks beating houses means renting wins.

7. Mostly my own conclusion. The narration frames findings (such as "longer stays favored the pile" and "the rent tag tips it") but explicitly declines to say what to do. Turning those into a checklist for my own decision is my interpretation.

8. Partly. My question was whether renting and investing the difference beats owning. The video answered that for this scenario: about a coin flip at ten years, worse for the buyer at fifteen, and dependent on the rent assumption. It didn't answer for my own situation, since it can't know my stay length, rent-to-price ratio, mortgage rate or discipline. The "9 in 10 yet half" explanation about the mortgage's leverage was the clearest part.

### R5
1. The video follows Nina, a renter with $92,000 saved, who wonders whether renting and investing the difference beats buying a roughly $400,000 house. It replays twin scenarios (one buys, one rents and invests everything in US stocks monthly) from every start month since 1991 and marks each as lit (buyer ahead) or dark (renter ahead). It shows how the result shifts with the renter's pile in cash vs. stocks, with the stay length (10 vs. 15 years), and with assumptions like fees and the rent level. It ends by saying the outcome hinges on how long she stays and on her rent assumption.

2. Over ten years, with the pile in stocks, the buyer ended ahead in 152 of 307 start months (about half), so it's a coin flip. Over fifteen years, the buyer led only about 1 in 5 times (cash: every time). With no monthly investing of the gap, the buyer led about 2 in 3. With 1% annual fees, the buyer led 55%. The split sits near a rent of 5.1% of price per year; at 5% it's about even. Short answer: investing the difference makes her roughly even over ten years and likely ahead over longer stays, but the rent assumption tips it.

3. "Over fifteen years, cash kept the buyer ahead every time; stocks, only about 1 in 5." Not confusing in itself, but it appears in the opening before the setup, so the terms (cash vs. stocks pile, twins) aren't defined yet. More genuinely confusing: "Those houses stay lit: the pile lost ground while the buyer kept paying down her loan." and "Nina's own month isn't on the street; its ten years are still ahead of her." The latter is clear only on rereading. Also, "Over a stay half as long, with the pile in stocks, the buyer was ahead a little more than half the time" sits oddly against the earlier "about half," and "Dark doors don't mean the renting twins had an easy ride" is slightly cryptic until the next sentence. Also the final line, "Nina's answer: investing the difference made her street a coin flip, and her rent tag tips it," is a bit abstract, since her actual rent isn't given.

4. "A lot of rent-versus-buy math assumes one growth rate; this replays the real record, month by month." Attention dropped there: it's a brief methodological aside that interrupts the story just as the result is landing. A second dip: "Every cost of owning stays the same, and the card lists each one." The viewer is told about a card without any of its content being narrated.

5. No. The video says explicitly "It's history, not a forecast" and "None of this ranks stocks above a house, or a house above stocks," and it doesn't predict prices, rents or returns. It counts what happened in past start months and notes that a home also brings stability and control.

6. A viewer would take away that "rent and invest the difference" is not a sure win: it depends on the stay length (longer favors renting and investing), on the actual rent-to-price ratio, on never skipping monthly investing through drops, and on fees. Over a short stay it's close to a coin toss, and over a long one the pile tends to win. Her own rent and expected stay should drive the decision.

7. Mostly my own synthesis. The narration supplies the conditional findings (stay length, rent tag, fees, discipline), but it declines to give advice and explicitly disclaims ranking. The "longer stay favors renting and investing" line comes close to a lesson ("Longer stays favored the pile"), but it is framed as a historical count.

8. Partly. It answers "does she really end up ahead?" with: about half the time over ten years, mostly yes over fifteen, and it depends on rent. It doesn't give a verdict for Nina's own case, since her rent, stay and future market are unknown, and the ten-year result depends on an assumed rent. The most useful parts were the stay-length comparison and the finding that the monthly investing of the gap, not the $92,000, did most of the catching up.

### R6
1. The video follows Nina, a renter with $92,000 saved, who wonders whether "rent and invest the difference" beats buying a roughly $400,000 house. It replays twin buyers and renters from every start month since 1991, with the renter putting her savings and the monthly cost gap into the whole US stock market. Each start month is a lit house (buyer ends ahead) or a dark one (renter ahead). It then tests how the result changes with the holding period, fees, no monthly saving, and the assumed rent.

2. Over ten years with the renter's pile in stocks, the buyer ended ahead in 152 of 307 start months, about half. Over fifteen years the buyer led in only about 1 in 5 of 247 starts. With the pile in cash, the buyer led about 3 in 4 times over ten years and every time over fifteen. The result is sensitive to the assumed rent: at 5% of price per year the street splits almost exactly in half, and the tipping point is near 5.1%. So at ten years it's a coin flip that the rent tag tips, and longer stays favor the renter.

3. Nothing seriously confused me, but a few lines were a little slippery:
 - "Over ten years, stocks outgrew home prices about 9 in 10 times. So you'd expect renting and investing to come out ahead of buying a house." It sets up the paradox cleanly, but "the dark house got darker" and "lit/dark" are easy to mix up with the earlier "cash" version.
 - "Nina's own month isn't on the street; its ten years are still ahead of her." This is clear once read, but on first hearing it's a bit abrupt.

4. Where my attention dropped most: "Most of the 1990s houses stay lit: about two in three of them. But the darkest house on the whole street is the very first one, January 1991. Its renting twin caught the long stock boom from its first month." This starts a long run of start-month by start-month anecdotes (1991, 1999, 2002–2007, 2006, 2012) with many numbers, and the thread of the main question gets harder to hold.

5. No on both counts. The video says outright that it "ranks" neither stocks nor housing, that it's "history, not a forecast," and that a home also offers stability and control that numbers don't count. It doesn't predict home prices, rents or stock returns, and it doesn't tell the viewer to buy or rent.

6. Only conditional, cautious takeaways: don't assume "rent and invest the difference" automatically wins; the outcome depends on how long you'd stay, your actual rent-to-price ratio, fees and taxes, and whether you'd really keep investing every month through drops. A viewer would likely conclude that for a short stay it's close to a toss-up, while for a long stay the investing renter has historically done better.

7. Mostly the narration itself, which states these dependencies directly ("longer stays tilt toward the pile," "the answer sits on the rent tag," the monthly habit did most of the catching up). The practical advice in my answer to Q6 is my own light synthesis, since the video explicitly avoids telling anyone what to do.

8. Largely yes. My question was whether a renter who invests the difference really ends up ahead. The answer, "about half at ten years, mostly yes at fifteen, and it hinges on the rent tag," came in the 152-of-307 count, the fifteen-year result, and the rent-sensitivity section. It's less complete on my personal situation, since it can't say how long I'd stay or what my actual rent would be relative to a house price.
