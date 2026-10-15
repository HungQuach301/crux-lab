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
1. The video follows Nina, a renter with $92,000 saved, who wonders whether renting and investing the difference beats buying a roughly $400,000 house. It replays every start month since 1991 as a "street" of houses, lit if the buyer ends ahead and dark if the renting twin's pile does. It first shows the result with the renter's money in cash, then in stocks, then at different horizons. Finally, it tests assumptions (no monthly saving, fees, and the rent level) and ends with a caveat-heavy summary.

2. With the pile in stocks over ten years, it's about a coin flip: the buyer ended ahead in 152 of 307 start months (about half). Over fifteen years, the buyer led in only about 1 in 5 of 247 starts. In cash, the buyer won about 3 in 4 at ten years and every time at fifteen. The result is sensitive to the assumed rent of 5% of price per year: the split sits near 5.1%, so the rent assumption tips it. Longer stays favored the renter's pile.

3. The passage that confused me: "Over a stay half as long, with the pile in stocks, the buyer was ahead a little more than half the time." It's unclear what "half as long" refers to (five years?), and it comes right after the ten-year result, so it reads as a contradiction. Also, "In this replay, the longer the stay, the more often the pile finished ahead" conflicts with the earlier line about the 2009 to 2016 starts, since the "stay" comparison is not shown cleanly. A second, smaller one: "Stocks outgrew the house almost nine times out of ten, yet buying still came out ahead in half" is explained later, but it's stated as a puzzle before the leverage explanation.

4. "Starts from 2009 through mid-2016 are lit nearly four times in five." That's where my attention dropped most. It's a dense run of date ranges and fractions with no new insight, and it follows several similar stretch-by-stretch descriptions of the street (1990s, 1999, 2002 to 2007, 2012), so it blurs together.

5. No. It says explicitly that it is "history, not a forecast," that it doesn't rank stocks above a house or the reverse, and it lists limits: US only, no taxes, renters who never skip a month. It doesn't predict home prices, rents, or stock returns, and it says nothing about what Nina should do.

6. A viewer would probably take away that "rent and invest the difference" is not a sure win: it was roughly a coin flip at ten years, and the renter wins more often the longer the stay. Staying a long time, investing the monthly gap consistently, and the local rent-to-price ratio all matter a lot. A viewer might also take away that the renter's advantage depends on discipline through market drops.

7. Mostly my own conclusion. The narration gives results and sensitivities, and it explicitly declines to recommend. The line "Longer stays favored the pile" is a finding, not advice. Takeaways like "stay longer" or "check local rent" are my inference.

8. Partly. My question was whether a renter who invests the difference ends up ahead. The answer was "about half the time at ten years, mostly yes at fifteen, and it depends on rent." That's a real answer for the median-price case. But it doesn't tell me which side of that rent line my own market is on, or how long I'll stay, so I can't apply it to my own decision. The sections on the ten-year street, the fifteen-year result, and the rent-tag sensitivity were the most useful.

### R2
1. The video follows Nina, a renter with $92,000 saved (a 20% down payment on a $400,000 home), who asks whether renting and investing the difference beats buying. It replays every 10-year start month from January 1991 to July 2016 (307 of them) as a street of houses, lit if the buyer ends ahead and dark if the renter does. It compares the renter's pile held in cash versus in the whole US stock market, then tests longer stays (15 years), no monthly investing, fees, and the assumed rent level. It closes by saying the result is a coin flip that the rent assumption tips.

2. With the renter's pile in stocks over 10 years, the buyer ended ahead in 152 of 307 start months, about half. Held in cash, the buyer won about 3 in 4. Over 15 years with stocks, the buyer won only about 1 in 5 of the 247 starts, while with cash the buyer won every time. The result is uneven: starts from 2002 to 2007 were all dark, and 2009 to mid-2016 were lit nearly 4 in 5. It also hinges on rent: at 5% of price per year the split is almost exact, with the break-even near 5.1%. Without the monthly gap invested, the buyer wins about 2 in 3, and a 1% annual fee on the pile raises the buyer's share to 55%.

3. Two passages confused me:
   - "A lot of rent-versus-buy math assumes one growth rate; this replays what actually happened, month by month." It is clear enough alone, but it sits oddly between the January 1991 example and the rent-tag explanation.
   - "Over a stay half as long, with the pile in stocks, the buyer was ahead a little more than half the time. In this replay, the longer the stay, the more often the pile finished ahead." The "half as long" stay is never defined, since it appears to mean 5 years, and it was not shown earlier. Also, the 10-year result is about half and the shorter stay is "a little more than half," so the comparison is thin.
   
   Also, "stocks outgrew homes almost nine times in ten" together with "the buyer led about half" seems contradictory at first. The video resolves it later, but the opening leaves the viewer puzzled for a while.

4. "Starts from 2009 through mid-2016 are lit nearly four times in five. So the half isn't spread evenly: whole stretches are lit, and one long stretch is dark." Attention dropped here because it follows a dense run of statistics and then immediately shifts to the shorter-stay point, so several numbers and time ranges pile up with little to anchor them. The opening hook and the later numeric stretches (the 307 count, the 152/80 switches) also drag, but this is the densest.

5. No. The video says outright that it is history, not a forecast, and that it "ranks" neither stocks nor houses. It makes no predictions about home prices, rents, or stock returns, and it lists limits: US only, no taxes, renters who never skip a month. It also notes that a home brings stability and control that numbers do not capture.

6. A viewer could take away that "rent and invest the difference" is not a sure win: over 10 years it was roughly a coin flip historically, and over longer stays the renter did better. Key sensitivities are the local rent-to-price ratio, how long you stay, fees, and whether you actually invest the monthly gap. Another takeaway is that buying works as leverage, since the house grows on the full price while the renter's pile starts at $92,000.

7. This is mostly my own conclusion. The narration reports counts and sensitivities and declines to recommend. Statements like "the longer the stay, the more often the pile finished ahead" and "the rent tag tips it" are findings from the replay, but turning them into "check your rent-to-price ratio and your horizon" is my inference.

8. Partly. It answered the historical question: with stocks, renting and investing the difference beat buying about half the time over 10 years and most of the time over 15, though the answer depends on the rent assumption. It did not say what will happen to me, which it said it could not do. It also did not settle how my own rent compares to the 5% assumption, so I would still have to check my local rent against the break-even near 5.1%.

### R3
1. The video follows Nina, a renter with $92,000 saved, who wonders whether renting and investing the difference beats buying a roughly $400,000 home with 20% down. It replays every start month since 1991 as a "street" of houses, lit if the buyer ends ahead and dark if the renting twin's pile ends ahead. It shows how the result changes with the pile held in cash versus stocks, the holding period (10 vs. 15 years), fees, whether the monthly gap is invested, and the assumed rent level. It ends by saying the answer depends on how long she stays and on the rent assumption.

2. Over ten years, with the renter's money fully invested in the US stock market (including the $92,000 and the monthly gap), the buyer ended ahead in 152 of 307 start months, about half. With cash, the buyer won about 3 in 4. Over fifteen years, the buyer won every time with cash but only about 1 in 5 with stocks. The result is sensitive to rent: the split is at about 5.1% of price per year, and at 5% it is nearly even. So the answer is "about a coin flip at ten years, and the renter usually ahead at fifteen, depending on rent," in historical US data only.

3. Mostly nothing, but a few lines were hard to follow:
   - "Stocks outgrew the house almost nine times out of ten, yet buying still came out ahead in half." It's resolved later by leverage, but it sounds contradictory when first heard.
   - "In this replay, the longer the stay, the more often the pile finished ahead." Combined with "Over a stay half as long... the buyer was ahead a little more than half the time," it is easy to lose track of which direction is which.
   - "Nina's own month isn't on the street." It's unclear at first why the street excludes her month, though the explanation (her ten years haven't happened yet) follows.
   - The ending, "Nina's answer: investing the difference made her street a coin flip, and her rent tag tips it," mixes a historical result with "her answer," which blurs what is established versus assumed.

4. "Most of the 1990s houses stay lit: about two in three of them. But the darkest house on the whole street is the very first one, January 1991." Attention dipped in the long stretch of year-by-year house stories (1990s, 1999, 2002–2007, 2006, 2012), where many dates and numbers come one after another and it was hard to keep track of which houses were lit or dark and why.

5. No. It explicitly says "It's history, not a forecast," and "None of this ranks stocks above a house, or a house above stocks." It lists its limits: US only, no taxes on gains or the home, renters who never skip a month. It makes no predictions about future prices, rents or returns, and it doesn't tell the viewer which to choose.

6. A viewer would take away a conditional lesson rather than a directive:
   - "Rent and invest the difference" is not a sure win. Historically it was roughly a coin flip over ten years.
   - Time horizon matters. The longer the stay, the more often the investing renter came out ahead.
   - The renter has to keep investing the monthly gap through downturns.
   - The local rent-to-price ratio matters a lot, so check it for your own market.
   - Fees and taxes, and non-financial factors like stability and control, also matter.

7. Mostly my own conclusion. The video states findings (the counts, the 5.1% rent threshold, the effect of the horizon) and explicitly refuses to rank renting versus buying. The practical points above, such as checking your own rent ratio and planning around your expected stay, are inferences I drew from those findings. The one place the narration comes close to advice is "the rent tag is the one assumption left to test," and the closing line about "her rent tag tips it."

8. Partly. It answered the historical question: with the money fully invested, the renter doesn't clearly come out ahead, and at ten years it was about a coin flip, with the renter pulling ahead at fifteen. It also explained why: the mortgage lets the house grow on the full $400,000, and the renter only catches up through monthly deposits and time. It did not answer what I should do in 2026, since it doesn't forecast, and the outcome depends on rent for my specific market and how long I'd stay, which I would still have to work out myself.

### R4
1. The video follows Nina, a renter with $92,000 saved, who wonders whether renting and investing the difference beats buying a roughly $400,000 house. It replays every start month since 1991 as a "street" of houses, lit if the buyer ends ahead of a renting twin and dark if not. It tests ten-year stays with the renter's pile in cash and in stocks, then a fifteen-year stay, then checks the assumptions (monthly savings, fees, and the rent level). It ends by saying the answer is roughly a coin flip, tipped by the rent assumption.

2. With the pile in stocks over ten years, the buyer ended ahead in 152 of 307 start months (about half). With cash, the buyer won about 3 in 4. Over fifteen years with stocks, the buyer won only about 1 in 5 (cash: every one of the 247 starts). The split is sensitive to rent: at 5% of price per year it is almost exactly half, and the tipping point is near 5.1%. If only the $92,000 is invested with no monthly savings, the buyer wins about 2 in 3. With a 1% annual fee on the pile, the buyer wins 55%.

3. "Over ten years, stocks outgrew homes almost nine times in ten." and the later "So how can stocks outgrow home prices about 9 in 10 times, and the buyer still finish ahead in half?" are only mildly confusing: "outgrew homes" compares price growth, not total outcomes, and that distinction takes a moment to land. Also, "Nina's answer: investing the difference made her street a coin flip" is slightly muddled, since Nina's own month isn't on the street. Otherwise nothing seriously confused me.

4. "Then the street goes dark, and stays dark. For starts from 2002 through 2007, the buyer ended ahead in none of them." is not where I lost attention; the dip came in the stretch of dense specifics: "April 2012 was the brightest house last time, and it still glows. With stocks, that buyer still ends $237,632 ahead." The cause is a run of individual named houses and dollar figures in a row (June 2006, the $54,310 pile, April 2012) that are hard to hold without a visual, and they don't change the overall conclusion.

5. No. The video says explicitly that it is history, not a forecast, and that it doesn't rank stocks above houses or the reverse. It also says a home brings stability and control that numbers don't count, and lists limits: US only, no taxes on gains or the home, and renters who never skip a month.

6. A viewer would take away that "rent and invest the difference" is not a sure win: it depends on the stay length, the rent-to-price ratio, discipline in investing every month, and fees. Longer stays and higher compounding favored the renter's pile, while lower rents, shorter stays, and purchases after price drops favored the buyer. Before deciding, check your local rent against the roughly 5.1% of price per year breakeven and be honest about how long you'll stay.

7. Mostly my own conclusion. The narration frames findings as conditional and avoids recommending a choice. The sensitivities (stay length, rent tag, fees) are presented, but turning them into a checklist is my inference.

8. Partly. My question was whether the renter who invests the difference ends up ahead. The video's answer is that it's a coin flip over ten years, mostly in the renter's favor over fifteen, and hinges on the rent assumption. The most useful parts were the ten- versus fifteen-year comparison and the rent breakeven near 5.1%. It didn't tell me which applies to my own market or timeline, which I would have to work out myself.

### R5
1. The video follows Nina, a renter with $92,000 saved, who asks whether renting and investing the difference beats buying a $400,000 home. It replays every start month since 1991 as a "street" of houses, lit if the buyer ends ahead and dark if not. It starts with a 10-year hold and the renter's pile in cash, then in stocks, then looks at 15 years, and then stress-tests assumptions (no monthly saving, 1% fees, the rent tag). It ends by saying the result is roughly a coin flip that depends on the assumed rent.

2. With the pile in stocks over 10 years, the buyer ended ahead in 152 of 307 start months (about half). With cash, the buyer won about 3 in 4. Over 15 years with stocks, the buyer won only about 1 in 5 (cash: all 247). The rent assumption decides it: at 5% of price per year the split is almost even, with a break-even near 5.1%.

3. Confusing passages:
- "Over ten years, stocks outgrew homes almost nine times in ten. So renting looks smart." The "So" assumes you already know the renter invests, and it's unclear why that leads to "smart."
- "Over a stay half as long, with the pile in stocks, the buyer was ahead a little more than half the time. In this replay, the longer the stay, the more often the pile finished ahead." It's hard to tell which stay length is the baseline and which is half as long, because the video's own order is confusing.
- "Longer stays favored the pile; the rent tag is the one assumption left to test." But the fee and no-saving tests came after, so "the one assumption left" doesn't match.
- "The renting twin's rent is an assumption, the tag on her door: 5 percent of the price a year, as of July 2026." The date sits oddly in a historical replay.
- The "brightest house last time" and "darkest house last time" lines refer to an earlier video I haven't seen.
- The 2009–2016 stretch is "lit nearly four times in five," but the overall figure is half and the 1990s are "two in three." It isn't obvious how the pieces add up.

4. Attention dropped most at: "The first house on that street is January 1991. With the renting twin's pile kept in cash, the buyer finished ten years $48,410 ahead. With the pile in stocks, the same buyer finished $485,063 behind." and the dense run of dollar figures and start-month ranges after it. The stretch of 1990s, 1999, 2002–2007, 2006 and 2012 houses piles up many dates and numbers in a row with little to anchor them. The "Nina's own month isn't on the street" aside also interrupted the flow.

5. No to both. It says explicitly that it's history, not a forecast, and that "none of this ranks stocks above a house, or a house above stocks." It says home ownership also brings stability and control. It doesn't predict prices, rents or returns.

6. A viewer would take away that the answer is conditional rather than a rule. Investing the difference makes renting competitive, but the outcome depends on local rent relative to price, how long you stay, your mortgage rate and entry price, fees and taxes, and above all whether you actually invest every month through downturns. Run your own numbers with your real rent-to-price ratio and time horizon.

7. Mostly my own conclusion. The narration frames findings and caveats ("the rent tag is an assumption," "the monthly habit did most of the catching up") but stops short of telling the viewer what to do. The closing line, "investing the difference made her street a coin flip, and her rent tag tips it," is the nearest it comes, and it's a finding, not advice.

8. Partly. I came in with "does renting and investing the difference beat owning?" and the video answered it directly: about half the time over 10 years, less often for the buyer over 15, and it hinges on the rent assumption. It doesn't tell me what happens in my own market or for my own stay length, which it admits.

### R6
1. The video is about Nina, a renter with $92,000 saved, who wonders whether renting and investing the difference beats buying a home. It replays every start month from January 1991 through July 2016 (307 ten-year windows) as a street of houses, lit if the buyer ends ahead and dark if the renter's pile does. A renting twin puts the $92,000 plus each month's cost gap into the total US stock market, and a buying twin takes a mortgage on the $400,000 house. It compares cash and stock piles, then tests stay length, a no-monthly-saving case, fees, and the assumed rent, and ends with the caveat that this is history, not a forecast.

2. With the pile in stocks, the buyer ended ahead in 152 of 307 ten-year windows, about half. Stocks outgrew homes in almost 9 in 10 windows, yet buying still won half, because the house grows on the full $400,000 while the pile starts at $92,000. With cash, the buyer won about 3 in 4 ten-year windows, and every fifteen-year window. With stocks over fifteen years, the buyer won only about 1 in 5. The result is sensitive to the rent assumption: the split sits near 5.1% of price per year, and the video uses 5%. So the answer is a coin flip at ten years that tips toward the renter with longer stays and depends on the rent tag.

3. "Over a stay half as long, with the pile in stocks, the buyer was ahead a little more than half the time." It's unclear what it is half as long as. The ten-year street is the main case, so I had to infer it means five years, and no earlier scene showed that number. Two other things confused me. The $92,000 is described as a 20% down payment, but 20% of $400,000 is $80,000, and the extra $12,000 (presumably closing costs) is never explained. And "June 2006 was the darkest house last time" and "April 2012 was the brightest house last time" refer to an earlier version I haven't seen.

4. "The rest of the limits are on the card: US only, history, not a forecast, no taxes on gains or on the home, and renters who never skip a month." It's a fast list of caveats that I can't see or check from the narration alone, and the point about forecasts had already been made. My attention also sagged a bit in the stretch of year ranges and percentages around 1999 and 2002–2007.

5. No. It says "None of this ranks stocks above a house, or a house above stocks," and repeatedly calls the results history, not a forecast. It gives no prediction of future home prices, rents or stock returns. The conclusion is only about what happened in past windows under stated assumptions.

6. There is no explicit advice. A viewer could take away that "rent and invest the difference" is not a sure win. The outcome depends on how long you stay, your rent relative to the price (about 5% a year is the tipping point), whether you actually invest every month through drops, and fees. It is not a verdict for either side.

7. The conclusion is my own. The narration carefully avoids telling anyone what to do. It supplies the factors (stay length, rent tag, monthly discipline), and I drew the practical lesson from them.

8. Partly. It answered the question as history: investing the difference made it roughly a coin flip at ten years, and the renter pulled ahead as stays got longer. That came from the street count, the 15-year result and the 5.1% rent break-even. It couldn't say whether I would come out ahead, because that depends on my local rent-to-price ratio, how long I'd stay, and the future, which it said it couldn't predict.
