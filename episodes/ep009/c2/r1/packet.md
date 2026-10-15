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
1. The video follows Nina, a renter with $92,000 saved, who wants to know whether renting and investing the difference beats buying a $400,000 home. It replays two "twins", a buyer and a renter, from every start month since 1991 with real home prices, rents, mortgage rates and stock returns. Each house on the "street" is lit if the buyer ends ahead and dark if the renter does. It starts from the earlier cash-pile result (buyer ahead most of the time), then moves the renter's pile into stocks and tests the assumptions that could change the outcome.

2. The answer is that it is about a coin flip, and it depends on the assumed rent. With stocks over ten years, the buyer ended ahead in 152 of 307 start months, about half. 80 months flipped from buyer to renter and none flipped the other way. The lit share is 78 percent for starts from 2009 to mid-2016, and zero of 72 for 2002 to 2007. Over fifteen years, only about 1 in 5 starts left the buyer ahead. If the renter doesn't save the monthly gap and invests only the $92,000, the buyer leads in about 2 in 3 months. With a 1 percent annual fee, the buyer leads in 55 percent of months. At a 5 percent rent-to-price tag the street splits almost exactly in half. Above about 5.1 percent, most houses are lit (the buyer wins), and below it most go dark.

3. One passage confused me: "Above about 5.1 percent, most houses light up; below it, most go dark. Public asking-rent data from the Census Bureau put the tag on both sides of that line, and the card shows the range." It doesn't say which side is more plausible for a typical renter, so I can't tell where my own rent falls. A smaller point is the lit/dark metaphor, which I had to keep translating as "buyer ahead" or "renter ahead" until it settled in. "Half a street, lit in stretches; now, a longer stay" also read as a fragment.

4. My attention dropped most here: "The renting twin's rent comes from one assumption, the tag on her door: a year's rent equal to 5 percent of the price, as of July 2026. Her stocks earn their returns before fees and taxes, with dividends reinvested." It's a dense stack of assumptions delivered in a row, with no number I could compare to my own situation. It also comes right after a similar paragraph on the buyer's costs.

5. No to both. The video says "It's history, not a forecast," that "None of this ranks stocks above a house, or a house above stocks," and that Nina's own ten years are still ahead of her. It also lists its limits: US only, no taxes on gains or on the home, and renters who never skip a month.

6. There is no direct advice. A viewer could take away that "rent and invest the difference" is not a sure win. It depends on the rent-to-price ratio where they live, on whether they invest every month, on fees and taxes, and on how long they will stay. A viewer might also conclude that the monthly saving habit matters more than the lump sum, and that a longer stay favors the investing renter in this data.

7. Mostly my own conclusion. The narration deliberately declines to recommend anything. It does point to which levers matter (rent tag, monthly discipline, fees, horizon), so the takeaway about what to check follows from its emphasis, but the "what to do" part is mine.

8. Partly. It answered the question as asked. No, she doesn't reliably end up ahead: stocks beat home prices almost every time, yet the buyer still came out ahead in half of the ten-year windows, because the mortgage lets the house grow on the full $400,000. It did not tell me what to do in my own case. It never says where a typical rent tag falls relative to 5.1 percent, how taxes and the mortgage interest deduction would change things, or how long I should plan to stay. The ending hands the decision back to the rent tag, which is the one number I would have to look up myself.

### R2
1. The video follows Nina, a renter with $92,000 saved, who is deciding whether to buy a $400,000 home or keep renting and invest the difference. It replays two "twins" (a buyer and a renter) across 307 start months from 1991 to 2016, using actual home prices, rents, mortgage rates and stock returns. With the renter's pile in cash, the buyer mostly comes out ahead. With the pile in stocks, the buyer wins only about half the time, and over fifteen years the renter mostly wins. It then explains why, tests a few assumptions (no monthly saving, fees, rent level), and ends on the caveats.

2. Investing the difference makes it roughly a coin flip. Over ten years, the buyer was ahead in 152 of 307 start months (about half), and 80 months flipped from buyer to renter versus none the other way. Over fifteen years, the buyer led in only about 1 in 5 of 247 starts. The result is sensitive to the rent assumption: at 5% of price per year the street splits evenly, above about 5.1% most buyers win, below it most renters win. Stocks beat home prices in about 9 in 10 ten-year windows, yet buying still wins half the time because the mortgage lets the house grow on all $400,000, while the pile starts at $92,000.

3. "Nina rents, with $92,000 saved and one twin for each choice." It was hard to parse on a first listen. It introduces the twins in the middle of a sentence about Nina's savings, and the "cash vs. stocks" comparison arrives before I knew what was being compared. Also: "Half a street, lit in stretches; now, a longer stay." The phrasing is clipped and the transition is cryptic. And "lit" and "dark" are never defined until partway through, so the opening statistics (3 in 4, half, 1 in 5) were hard to anchor.

4. "A lot of rent-versus-buy math picks one growth rate for stocks and one for homes, then lets them run. That gives a single, tidy answer, and it hides the order in which the good and bad years arrived." My attention dropped here because it is a methodological aside, and it interrupts the story of the street and the houses just as the results were building.

5. No. It says explicitly that it is history, not a forecast, and that it doesn't rank stocks above a house or the reverse. It says the half is "a count of what already happened, not a promise about Nina's month." It also notes that stability and control aren't counted, and lists limits: US only, no taxes on gains or the home, and renters who never skip a month.

6. A viewer would take away that "rent and invest the difference" is not a sure win: it depends on the rent-to-price ratio, on how long you stay, on whether you invest the monthly savings consistently, on fees, and on when you start. A viewer might also conclude to check their own local rent-to-price ratio and expected time horizon before deciding.

7. That is my own conclusion. The video states no advice and ends on "investing the difference made her street a coin flip, and her rent tag tips it." That is a finding, not a recommendation. The takeaways about checking rent ratio and time horizon are inferences I drew from the sensitivity tests.

8. Partly. It answered the "does she really end up ahead" question: not reliably, about a coin flip over ten years, and the renter tends to win over fifteen. It also explained why the intuition "stocks beat homes, so renting wins" fails: leverage on the larger base. It did not tell me what would happen for my own situation. It never says where Nina's rent tag falls, only that Census data put it on both sides of the 5.1% line, so my specific answer depends on my local rent and how long I'd stay.

### R3
1. The video follows Nina, a renter with $92,000 saved, who wonders whether renting and investing the difference beats buying a $400,000 home. It replays "twins" (one buys, one rents and invests) from every start month since 1991, using real home prices, rents, mortgage rates and stock returns. With the renter's money in cash, the buyer mostly wins. With it in stocks, the result is about a coin flip over ten years, and mostly favors the renter over fifteen. It then tests which assumptions swing the outcome: no monthly saving, fees, and the rent level.

2. Over ten years, stocks outgrew home prices almost every time, yet the buyer still came out ahead in 152 of 307 start months, about half. 80 start months flipped from buyer to renter when the pile moved from cash to stocks, and none flipped the other way. The split is uneven. Starts from 2002 through 2007 were all renter wins (the buyer led in 0 of 72), and starts from 2009 to mid-2016 were 78 percent buyer wins. Over fifteen years only about 1 in 5 starts favored the buyer. The result hinges on the rent assumption: at 5 percent of price the street splits about evenly, above roughly 5.1 percent most buyers win, and below it most renters win.

3. Nothing really blocked me, but a few spots were muddy:
- "lit" and "dark" are used well before they are defined. The first use is "turned the first house from lit to dark", and the definition comes much later with "After ten years, a house is lit if the buying twin's equity..."
- "Nina rents, with $92,000 saved and one twin for each choice." The twin framing is introduced abruptly.
- "Nina's answer: investing the difference made her street a coin flip, and her rent tag tips it." This is odd because Nina doesn't have an answer yet. The video says her own month isn't on the street.

4. "Everything else is as it was last time on this street." My attention dropped here and in the paragraph after it. It refers to an earlier video I haven't seen, and it is followed by a list of assumptions (down payment, closing costs, taxes, insurance, repairs, 6 percent selling cost) that I could only take on trust.

5. No. The video says outright that it is "history, not a forecast," and that "none of this ranks stocks above a house, or a house above stocks." It also says homeownership brings stability and control that numbers don't capture. It does not predict future prices, rents or returns.

6. There is no direct instruction, but a viewer could reasonably take these points:
- "Rent and invest the difference" is not a sure win, even though stocks usually outgrew homes.
- The mortgage lets the house grow on a much bigger base, which is why the buyer often stays competitive.
- The outcome depends on your own rent-to-price ratio, how long you will stay, whether you invest every month through drops, and whether you pay fees and taxes.
- Check your local rent against the roughly 5.1 percent line, and be honest about whether you would really keep investing in a crash.

7. That advice is my own conclusion. The narration presented findings and sensitivities, and it deliberately avoided recommending anything. The closest it came was pointing to the rent tag as the swing factor, and it called that tag "an assumption."

8. Partly. It answered "does she end up ahead?" as a historical base rate: about half the time over ten years, more often over fifteen, and highly sensitive to rent. That is more useful than "it depends." It did not answer what happens in my own case. The ten years starting in 2026 are unknown, my local rent-to-price ratio isn't worked out, and it doesn't say how to weigh my own time horizon. The sensitivity section on rent, fees and monthly saving was the most useful part.

### R4
1. The video follows Nina, a renter with $92,000 saved, who is deciding whether to buy a $400,000 home or rent and invest the difference. It replays history for every start month since 1991, giving each month a buying twin and a renting twin, and counts how often the buyer ends up ahead. With the renter's money in cash the buyer usually wins, but with it in stocks the result is about a coin flip at ten years. At fifteen years, stocks win most of the time. It then shows what shifts the outcome (monthly saving, fees, the rent assumption) and closes without telling Nina what to do.

2. The video says that investing the difference does not reliably put the renter ahead. Over ten years the buyer finished ahead in 152 of 307 start months (about half), and 80 months flipped from buyer to renter when the pile moved from cash to stocks. Over fifteen years the buyer led in only about 1 in 5. The reasons it gives are leverage and the rent assumption:
   - The house grows on the full $400,000 while the pile starts at $92,000, so stocks beating home prices doesn't settle it.
   - The result depends heavily on the rent tag. Above about 5.1% of the price most houses favor the buyer, and below it most favor the renter.
   - Investing only the $92,000, with no monthly deposits, leaves the buyer ahead in about 2 in 3 months.
   - A 1% annual fee raises the buyer's share to 55%.

3. "So one change, stocks instead of cash, turned the first house from lit to dark."
   "Lit" and "dark" are used here before they're defined. The definition only arrives much later ("After ten years, a house is lit if the buying twin's equity, after selling costs, is bigger than the renting twin's pile."). I could guess the meaning from context, but I wasn't sure at that point. Two other lines were a little unclear: "Nina's own month isn't on the street," and the references to "last time on this street," which assume I saw an earlier video.

4. "Everything else is as it was last time on this street. The buying twin's $92,000 becomes the down payment and closing costs on a $400,000 home. She pays the mortgage, property tax, insurance and repairs, and 6 percent to sell when the ten years end. Same costs, same street, one change: the pile now rides the market."
   My attention dropped here because it's a list of assumptions with no payoff yet, and it leans on a video I haven't seen. The stretch of year-by-year counts after it (the 1990s, 1999, 2002–2007) also felt dense.

5. No. It says outright that this is "history, not a forecast" and that "none of this ranks stocks above a house, or a house above stocks." It makes no predictions about future home prices, rents or stock returns, and it notes that Nina's own ten years are still ahead of her.

6. There is no explicit advice, but a viewer could take away a few things:
   - "Rent and invest the difference" is not a sure win.
   - The outcome depends on the rent-to-price ratio, on whether you really invest every month, on fees, and on how long you stay.
   - Check your own rent against about 5% of the home price.

7. That is my own conclusion. The narration deliberately avoids recommending anything and ends with "her rent tag tips it." That points to the rent-to-price ratio as the thing to check, but it never says to act on it.

8. Partly. My question was whether renting and investing leaves you ahead of buying. The video says "not reliably": it's roughly 50/50 over ten years, and the renter is favored over longer stays. What it can't tell me is the answer for my own situation, because that depends on my actual rent, how long I'd stay, and future returns. It also leaves open that the 5.1% threshold sits within the range of real rent data, so the answer rests on an assumption.

### R5
1. The video is about Nina, a renter with $92,000 saved who is weighing renting and investing the difference against buying a $400,000 home. It replays two "twins" (one buys, one rents) from every start month since 1991 and counts how often the buyer ends up ahead, calling those start months "lit" and the renter-ahead ones "dark." With the renter's money in cash the buyer usually wins, but with it in the stock market the buyer wins about half the time over ten years, and only about 1 in 5 over fifteen. It then tests which assumptions tip the result: saving the monthly gap, fees, and especially the rent level.

2. With stocks, the buyer came out ahead in 152 of 307 ten-year start months, about half. That was a big drop from cash, where the buyer led about 3 in 4. Over fifteen years the buyer led in only about 1 in 5 starts. It's a coin flip at ten years that tilts toward renting and investing at fifteen, and the ten-year split depends heavily on the rent assumption. At 5 percent of price it's an even split, above about 5.1 percent most buyers win, and below it most renters win. Stocks beat home prices almost every time, yet the buyer still wins half the time because the mortgage lets the house grow on $400,000 while the renter's pile starts at $92,000.

3. "So one change, stocks instead of cash, turned the first house from lit to dark." This confused me because "lit" and "dark" are used here before the video explains that lit means the buyer is ahead. I only worked it out later, at "After ten years, a house is lit if the buying twin's equity..." Also, "Everything else is as it was last time on this street" assumes I saw an earlier video.

4. "The buying twin's $92,000 becomes the down payment and closing costs on a $400,000 home. She pays the mortgage, property tax, insurance and repairs, and 6 percent to sell when the ten years end." My attention dropped here because it's a list of setup details and percentages with no payoff yet. The same stretch of assumptions and counts (307 houses, 67.6 percent, 16 start months, 72) also felt dense.

5. No. The video says it's "history, not a forecast," makes no predictions about prices, rents or stock returns, and says "None of this ranks stocks above a house, or a house above stocks." It also notes that stability and control aren't counted.

6. The video gives no direct advice. A viewer might take away that "rent and invest the difference" is not a sure win, that the result depends on the rent-to-price ratio, how long you stay, and whether you invest every month, and that they should check their own numbers. That is my reading, not something the video states.

7. It's my own conclusion. The narration deliberately avoids recommending anything. The closest it comes is "the answer sits on the rent tag, and the tag is an assumption," which points to what matters without telling me what to do.

8. Partly. The question was whether Nina ends up ahead by renting and investing the difference, and the video answers that in aggregate: about half of the time over ten years, with the answer hinging on the rent tag. It can't say what happens for Nina's own month or how long she will stay, and it says so at the end.

### R6
1. The video follows Nina, a renter with $92,000 saved, who is deciding whether to buy a $400,000 home or keep renting and invest the difference. It replays a buying twin and a renting twin from every start month since 1991, using real home prices, rents, mortgage rates and stock returns. The renter's pile is the $92,000 plus every month's gap between owning costs and rent, all put into the US stock market. It first shows that cash left the buyer ahead most of the time. Then it shows that stocks made it about half, tests which assumptions move that half (horizon, the monthly deposits, fees, the rent level), and ends on Nina's own case.

2. Over ten years, with the renter's pile in stocks, the buyer finished ahead in 152 of 307 start months (about half). With the pile in cash, the buyer was ahead about 3 in 4 times, and 80 months switched from buyer to renter with none going the other way. Over fifteen years, the buyer was ahead only about 1 in 5 times with stocks. The result is lumpy: starts from 2002 to 2007 were all renter wins, and 2009 to mid-2016 starts were 78% buyer wins. It also depends heavily on the rent assumption of 5% of price per year. Above about 5.1% most buyers win, and below it most renters win. So the answer is roughly a coin flip over ten years that the rent level tips, and renting and investing wins more often the longer the stay.

3. "Over fifteen years, the street turns over." and "Longer stays favored the pile; one assumption is still untouched." Both are cryptic transitions, and I couldn't tell what "turns over" or "untouched" was pointing to until later. "June 2006 was the darkest house last time" and "April 2012 was the brightest house last time" also assume I saw a previous video. The "lit/dark" metaphor is also only defined partway through, after the opening already used its results. "Half a street, lit in stretches; now, a longer stay." is a fragment that I had to read twice.

4. "Everything else is as it was last time on this street. The buying twin's $92,000 becomes the down payment and closing costs on a $400,000 home." My attention dropped here. It is a stretch of setup detail (mortgage, tax, insurance, repairs, 6% selling cost, rent tag, fees) delivered as a list with no new insight, and it leans on a previous video.

5. No. The video says it is "history, not a forecast." It says "None of this ranks stocks above a house, or a house above stocks." It also notes that stability and control are not counted. It never predicts future prices, rents or returns, and it names its limits: US only, no taxes on gains or on the home, and renters who never skip a month.

6. The video gives no direct advice. A viewer could take away that "rent and invest the difference" is not a sure win, because buying came out ahead about half the time even when stocks beat home prices nearly every time. The result depends on the rent-to-price ratio, how long you stay, and whether you really invest every month. A viewer might therefore check their own rent against the cost of owning, and consider their time horizon.

7. That takeaway is my own conclusion. The narration deliberately avoids recommending anything, though "the answer sits on the rent tag" points the viewer toward checking their own rent.

8. Partly. It answered the question for past data: renting and investing does not reliably beat buying, and over ten years it was about even. It explained why, since the mortgage lets the house grow on all $400,000 while the pile starts at $92,000. It could not say whether I would come out ahead, because the answer depends on rent level, my stay, and future markets. The rent-tag section and the fifteen-year section gave me the most useful guidance for my own case.

### R7
1. The video follows Nina, a renter with $92,000 saved, who is deciding between buying a $400,000 home with 20% down and renting while investing the difference. It replays both choices as "twins" over every start month since 1991, using real US home prices, rents, mortgage rates, and stock returns. It shows the results as "lit" houses (the buyer ends ahead) and "dark" houses (the renter ends ahead), first over ten years, then fifteen, and finally tests how the answer changes with different assumptions.

2. Not reliably. Over ten years with the renter's savings in stocks, the buyer finished ahead in 152 of 307 start months (about half), and the renter finished ahead in the other 155. Over fifteen years, the buyer finished ahead in only about 1 in 5 of 247 starts. The main sensitivities are the monthly savings (without them, the buyer leads about 2 in 3 times), fees and taxes (a 1% annual cost lifts the buyer's share to 55%), and the rent-to-price ratio (the split sits near 5%, and above about 5.1% most houses favor the buyer).

3. Yes, a few things:
- "and turned the first house from lit to dark." "Lit" and "dark" appear here before the video defines them a few paragraphs later with "a house is lit if the buying twin's equity... is bigger than the renting twin's pile."
- "The stock series and its source are on the card." The narration never says what "the card" is, so a listener can't tell what the reference is.
- "Public asking-rent data from the Census Bureau put the tag on both sides of that line... and the tag is an assumption." It isn't clear whether the rent tag is an observed number or a modeling choice, and the sentences seem to pull in both directions.

4. I can't measure my own attention, so I can't identify a real drop. The passage where I'd most expect a listener to lose the thread is the metaphor-heavy setup: "Each start month is a house on one long street, with the same twins inside."

5. No. The video says "It's history, not a forecast," that its numbers are "a count of what already happened, not a promise about Nina's month," and that "None of this ranks stocks above a house, or a house above stocks." It makes no prediction about future prices, rents, or returns, and it doesn't recommend a choice. It does describe what happened historically and summarize that as "investing the difference made her street a coin flip, and her rent tag tips it."

6. A careful viewer could reasonably take these points:
- The rent-to-price ratio is the key input, so compare the annual rent with 5% of the home price.
- If renting and investing is the plan, the monthly savings do most of the work, so saving the gap every month matters.
- Fees and taxes move the result toward buying, so they need to be included.
- Selling during a crash removes the renter from the favorable paths.
A less careful viewer might turn "most fifteen-year windows favored the renter" into "renting is better," which the video explicitly doesn't claim.

7. Mostly the narration, but not all of it. The narration states the 5% rent threshold, the 1% fee result, the monthly-savings result, and the closing "coin flip" line. The advice in answer 6 is my own synthesis. The video itself says nothing about what a viewer should do. I have only the narration text, so I can't say what the animation showed.

8. Partly. The video answered the historical version of the question, and it did so clearly: over ten years it's about a coin flip, and over fifteen years the renter usually came out ahead, with the rent tag and monthly saving deciding much of the outcome. It didn't answer whether this will hold for Nina's own start month, since it explicitly excludes that. It also doesn't address the non-financial value of owning, which it names but doesn't measure.
