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
1. The video follows Nina, who rents and has $92,000 saved, through the question of whether renting and investing the difference beats buying a house. It replays a buying twin and a renting twin from every start month since 1991, shown as a street of houses that are lit if the buyer ends ahead and dark if not. It first shows that with the renter's money in cash the buyer usually wins, then switches to stocks, where the ten-year result is about half lit. It then explains why (the mortgage lets the house grow on a much bigger base) and tests the assumptions (no saved gap, fees, the rent level, longer stays). It ends by saying Nina's answer is a coin flip that the rent level tips.

2. The answer is "about half, and it depends." Over ten years with the pile in stocks, the buyer finished ahead in 152 of 307 start months. With cash, the buyer was ahead about 3 in 4 times. Over fifteen years, the buyer was ahead only about 1 in 5 times with stocks, and every time with cash. Over a stay half as long as ten years, the buyer was ahead 53.4% of the time. The break-even rent is about 5.1% of the price a year, and Nina's answer hinges on that rent assumption and on how long they stay.

3. Quote: "With cash, 6 of them had stayed lit; with stocks, those lights go out too."
It confused me because the passage says the buyer ended ahead in none of 72 starts, yet earlier the cash case was described as mostly lit. Six lit out of 72 is a surprisingly small number, so I couldn't tell whether "lit" or "dark" was meant. A second, smaller confusion: "Over a stay half as long" never says half of what, so I had to infer five years.

4. Quote: "Every cost of owning stays the same, and the card lists each one."
My attention dropped here because the narration points at an on-screen card without saying what is on it. For a listener the sentence carries no content, and it comes right after the dense explanation of the renter's pile.

5. No. The video says outright that it is "history, not a forecast," and that "None of this ranks stocks above a house, or a house above stocks." It makes no prediction about future home prices, rents or stock returns. It also says a home brings stability and control that numbers don't capture.

6. A viewer wouldn't get a direct instruction. The implied takeaways are that the answer is not obvious, so don't assume investing the difference automatically wins. It turns mostly on three things: how long you'll stay (longer favors the renter), your actual rent relative to the home price, and whether you really invest the monthly gap every month, even through crashes. A viewer could use those as things to check for their own situation.

7. That is my own conclusion. The narration never tells the viewer what to do. It does point at the hinges (stay length, rent tag, the monthly habit), but turning those into advice is my inference.

8. Partly. The question I came with was whether renting and investing the difference beats owning, and the video answered it for the historical record: a toss-up at ten years, favoring the renter at fifteen, and favoring the buyer if the money sits in cash. It could not answer it for any one person, because the result depends on Nina's rent and how long they stay, which the video says it doesn't know.

### R2
1. The video follows Nina, a renter with $92,000 saved, and asks whether renting and investing the difference beats buying. It replays "twins" (one buys, one rents and invests) from every start month since 1991, drawn as a street of houses that are lit if the buyer ends ahead and dark if not. It first shows that with the renter's money in cash the buyer mostly wins, then that with the money in stocks it's about half, and over 15 years mostly the renter. It then tests the assumptions (monthly savings, fees, the rent level) and closes with caveats.

2. Over 10 years, with the renter's pile fully invested in US stocks every month, the buyer ended ahead in 152 of 307 start months, about half. Over 5 years the buyer led 53.4% of the time, and over 15 years only about 1 in 5 starts. With cash instead of stocks, the buyer won about 3 in 4 over 10 years and every time over 15. The result is sensitive to rent. At 5% of price per year the street splits almost exactly in half, and the tipping point is near 5.1%. So the answer is that it's roughly a coin flip, and the rent level decides it.

3. Several passages confused me:
- "Every cost of owning stays the same, and the card lists each one." I couldn't tell what the card contains from the narration alone.
- "The split sits near 5.1 percent, and public rent data from the Census Bureau falls on both sides of it." It isn't clear what that means for someone's own rent.
- "all $400,000 of it" doesn't match the numbers elsewhere. $92,000 as a 20% down payment implies a price of about $460,000.
- "June 2006 was the darkest house last time" and "April 2012 was the brightest house last time" refer to a previous video I haven't seen.

4. "A lot of rent-versus-buy math assumes one growth rate; this replays the real record, month by month." My attention dropped here because it's an abstract methodological aside sandwiched between the action and the next item, and it leans on a visual card I can't see.

5. No. The video says outright "None of this ranks stocks above a house, or a house above stocks," and calls its results "history, not a forecast." It makes no predictions about future prices, rents or returns. It only describes what happened in past windows and which assumptions matter.

6. The video doesn't give direct advice. A viewer could reasonably take away four things:
- Don't assume "rent and invest the difference" automatically wins.
- Time horizon matters, since longer stays favored the renter's invested pile.
- The monthly investing habit mattered more than the lump sum.
- Check your own rent-to-price ratio against the roughly 5% tipping point.

7. Mostly my own conclusion. The video deliberately avoids prescribing and even says a home brings stability and control that numbers can't count. The closest it comes is pointing at the rent tag and the stay length as the things that decide the outcome, which nudges a viewer toward checking those.

8. Partly. It answered whether a renter who invests the difference ends up ahead: not reliably, about half the time over 10 years, mostly yes over 15 years, and heavily dependent on rent. It did not answer it for my situation in 2026, because Nina's own start month isn't on the street and I don't know my local rent-to-price ratio or how long I'd stay. The $92,000 versus $400,000 mismatch also leaves me unsure what price the model assumes.

### R3
1. The video follows Nina, a renter with $92,000 saved, who asks whether renting and investing the difference beats buying a roughly $400,000 house. It replays twin buyers and renters from every start month since 1991, using the whole US stock market for the renter's money. It shows that with the renter's pile in cash the buyer usually wins, with stocks the result is about half and half over ten years, and over fifteen years the renter usually wins. It then tests assumptions (no monthly savings, fees, rent level) and closes by saying the answer hinges on the rent assumption and on how long Nina stays.

2. Over ten years, with the renter investing the $92,000 plus the monthly gap in stocks, the buyer ended ahead in 152 of 307 start months (about half). Over fifteen years, the buyer was ahead in only about 1 in 5 of 247 starts. At a ten-year stay, the split depends on rent: at 5% of price per year it's an even split, with the break-even near 5.1%. Cash instead of stocks flips this, with the buyer ahead about 3 in 4 times at ten years and every time at fifteen. In short: "a coin flip, and her rent tag tips it," with longer stays favoring the renter.

3. Nothing seriously confusing, but a few lines were murky:
   - "Nina's own month isn't on the street; its ten years are still ahead of her." It is a bit cryptic about why her start month is excluded (not enough data yet).
   - "Over a stay half as long, with the pile in stocks, the buyer was ahead 53.4 percent of the time." "Half as long" is ambiguous; I inferred it means five years, but that was not stated, and it conflicts with the ten-year framing.
   - "Nina's answer: investing the difference made her street a coin flip" reads as though Nina has reached a verdict, when the video only has a historical count.

4. "The first house on that street is January 1991. With the renting twin's pile kept in cash, the buyer finished ten years $48,410 ahead. With the pile in stocks, the same buyer finished $485,063 behind." Several precise dollar figures arrive in quick succession, and the later figures ($261,689, $237,632, $54,310) similarly blur together. My attention dipped most in the stretch of scenes giving per-house stats (June 2006, April 2012, the 183-of-307 dip count), because the numbers pile up without a clear takeaway for each.

5. No on both counts. The video explicitly says "It's history, not a forecast" and "None of this ranks stocks above a house, or a house above stocks." It does not predict future home prices, rents or stock returns, and it does not say whether to buy or rent. It describes what happened in past start months under stated assumptions.

6. A viewer would likely take away that "rent and invest the difference" is not a sure win. It depends on how long you stay, the rent-to-price ratio where you live, whether you really invest every month through downturns, and costs like fees and taxes. The viewer would also see that longer stays and disciplined investing favor renting, and that a short stay or a cheaper-rent-gap-poor market favors buying.

7. Mostly my own conclusion. The narration deliberately avoids prescribing, and it states facts such as counts, sensitivities and caveats. Lines like "A short stay is close to a coin toss; longer stays tilt toward the pile" and "the monthly habit... did most of the renter's catching up" come close to implying advice, but the practical takeaways in item 6 are my inference.

8. Partly. My question was whether a renter who invests the difference ends up ahead of a buyer. The video answers that with "about half the time at ten years, and mostly yes at fifteen," in the sections on the 152-of-307 count and the fifteen-year result. It doesn't give a definitive yes or no for me, since the answer depends on rent level and time horizon, and it doesn't tell me how my own local rent compares with the 5% tag. That part is left for me to work out.

### R4
1. The video follows Nina, a renter with $92,000 saved, who is deciding whether to buy a roughly $400,000 house or keep renting and invest the difference. It replays twin buyers and renters in every start month since 1991, shown as a street of houses lit if the buyer ends ahead and dark if not. It tests ten-year stays with the renter's pile in cash versus stocks, then checks fifteen-year stays, a no-monthly-savings case, fees, and the rent assumption. It closes by saying the result is a coin flip that the rent assumption tips.

2. With the pile in stocks, the buyer ended ahead in 152 of 307 ten-year start months (about half). Stocks outgrew the house about 9 in 10 times, yet buying still won half, because the mortgage lets the house grow on the full $400,000 while the renter starts with $92,000. A 5-year stay (the "half as long" case) favored the buyer 53.4% of the time, and over fifteen years the buyer led only about 1 in 5 times. The result is sensitive to rent: the split sits near 5.1% of price per year, and the video uses 5%. Results by period vary: 2002–2007 starts were all dark, and 2009–mid-2016 starts were 78% lit.

3. One passage confused me: "Over a stay half as long, with the pile in stocks, the buyer was ahead 53.4 percent of the time." Half of ten years is five, but the video never says "five years," and it appears without setup. A second one: "Over ten years, stocks outgrew home prices about 9 in 10 times. So you'd expect renting and investing to come out ahead..." is fine, but "With Nina's renting twin holding cash, the buyer ended ahead about 3 in 4 times" arrives before the cash and stock cases are explained.

4. "The first house on that street is January 1991. With the renting twin's pile kept in cash, the buyer finished ten years $48,410 ahead. With the pile in stocks, the same buyer finished $485,063 behind." Attention drops most around the stretch of dense statistics that follows ("Most of the 1990s houses stay lit: 67.6 percent... 16 start months around March 1999... 72... 6 of them... $261,689..."), where many figures arrive in a row. The most exact place is: "Then the street goes dark, and stays dark. For starts from 2002 through 2007, the buyer ended ahead in none of 72." The numbers pile up and the cash-versus-stocks comparisons start to blur.

5. No. The video says outright that it is history, not a forecast, and that it does not rank stocks above a house or the reverse. It names the limits: US only, no taxes on gains or on the home, renters who never skip a month, and an assumed rent. It also says homes bring stability and control that numbers don't count.

6. A viewer would take away that "rent and invest the difference" is not a sure win. Historically it was roughly a coin flip at ten years, favored the renter with longer stays, and favored the buyer at shorter stays. It depends heavily on local rent relative to price (around 5% a year), on actually investing every month, on low fees, and on how long you will stay. The practical advice is to check your own rent-to-price ratio and expected stay length.

7. That is mostly my own conclusion. The narration gives findings and sensitivities and refuses to say what to do. The closing line ("investing the difference made her street a coin flip, and her rent tag tips it") is a summary of the result, not a recommendation. Pointing the viewer to their own rent ratio and stay length is my inference from the sensitivity tests.

8. Partly. The question was whether a renter who invests the difference ends up ahead of a buyer. The video answers that for the past: about half the time over ten years, and mostly not over fifteen, with the exact balance depending on the rent assumption. It does not say what will happen for a 2026 start, and it does not use Nina's real local rent. Its answer on "rent and invest the difference" is therefore "not reliably, and it depends," not a yes or no.

### R5
1. The video follows Nina, a renter with $92,000 saved, who wonders whether renting and investing the difference beats buying a roughly $400,000 house. It replays twin buyers and renters from every start month since 1991, shown as a street of houses that are lit if the buyer ends ahead and dark if not. It first shows that moving the renter's pile from cash to stocks flips many outcomes. Then it counts the results at 10 and 15 years and tests three assumptions: no monthly saving, 1% fees, and the rent level. It closes by saying the answer hinges on the rent assumption.

2. Over 10 years with the pile in stocks, the buyer ended ahead in 152 of 307 start months (about half), so it's a coin flip. With cash, the buyer led about 3 in 4 times. Over 15 years, stocks left the buyer ahead only about 1 in 5 times, versus every time with cash. The result is sensitive to rent: the split sits near 5.1% of price per year, and the video assumes 5%. Without monthly reinvestment of the gap, the buyer leads about 2 in 3. With 1% fees, the buyer leads 55%. The video's answer is "about half over 10 years, tilting to the renter with longer stays, and tipped by the rent level."

3. "Over a stay half as long, with the pile in stocks, the buyer was ahead 53.4 percent of the time." It's confusing because "half as long" isn't tied to a number until you work out that the main window is 10 years, so this means 5 years. It also appears in the middle of the street walk-through, which follows the 10-year result. A second confusing bit is "Over fifteen years, cash kept the buyer ahead every time," which comes in the opening before the cash/stock distinction has been explained. A third is "80 start months switched from the buyer to the renter," since it isn't clear what the starting condition is (cash) until you infer it.

4. "Starts from 2009 through mid-2016 are 78 percent lit. So the half isn't spread evenly: whole stretches are lit, and one long stretch is dark." Attention dropped here because the sequence of percentages, date ranges and counts comes in quick succession (67.6%, 16 of them, 72 of them, 183 of 307, 152 of 307, 78%, 53.4%), and these lines add one more stat without a new idea. The opening also loads many figures and "3 in 4 / half / every time / 1 in 5" in a few sentences.

5. No. The video says outright that it's history, not a forecast, and that it doesn't rank stocks above a house or a house above stocks. It also leaves out taxes, non-US markets, and non-financial value such as stability and control. The rent tag is called an assumption, and the stock return is a replay of what happened.

6. A viewer would probably take away that "rent and invest the difference" is not a sure win, because it depends on how long you stay, on rent relative to the price, on whether you keep investing every month, and on fees. A viewer might also conclude that longer stays favor investing and shorter stays are close to a coin toss. The "stocks outgrew homes 9 in 10 times" statistic alone doesn't settle it, since leverage and the monthly gap matter.

7. Mostly my own conclusion. The narration states findings, such as "longer stays favored the pile" and "the answer sits on the rent tag," but it avoids telling anyone what to do. The takeaways about checking your own rent-to-price ratio and holding period are inferences from those findings.

8. Partly, yes. It answered the question for 10-year and 15-year windows: no, she doesn't reliably come out ahead, and it's about 50/50 at 10 years, more likely the renter's favor at 15. It didn't tell me whether I, with my own rent and plans, would end up ahead. It said that depends on the rent tag and how long I stay, so the closing "coin flip, tipped by rent" is the usable part, but I'd need to check my own numbers.

### R6
1. The video follows Nina, a renter with $92,000 saved, and asks whether renting and investing the difference beats buying a roughly $400,000 house. It replays twin buyers and renters from every start month since 1991, shown as a "street" of houses lit if the buyer ends ahead and dark if not. It first shows that cash-holding renters lose to buyers, then that stock-holding renters make it about a coin flip over ten years, and mostly favor the renter over fifteen. It closes by testing assumptions (no monthly investing, 1% fees, the rent tag) and noting the answer hinges on the assumed rent.

2. Over ten years with the pile in stocks, the buyer ended ahead in 152 of 307 start months (about half). The share was 53.4% over five years, about 1 in 5 over fifteen years (cash: every time), 78% for 2009 to mid-2016 starts, and 0 of 72 for 2002 to 2007 starts. So "rent and invest the difference" is roughly a coin flip at ten years, wins more often with longer stays, and depends on the assumed rent (5% of price a year; the split sits near 5.1%). It's history, not a forecast.

3. "Over a stay half as long, with the pile in stocks, the buyer was ahead 53.4 percent of the time." It's confusing because the video never says "five years" and "half as long" follows a ten-year frame, so the viewer must work out the horizon. It also sounds like a lit share rising slightly from half, which needs a moment to reconcile with "a short stay is close to a coin toss." Also, "Over ten years, stocks outgrew home prices about 9 in 10 times... buyer led only about half the time" is early and compressed. And "80 start months switched from the buyer to the renter" (switched from what comparison?) is unclear until you infer it means cash versus stocks.

4. "Dark doors don't mean the renting twins had an easy ride. In 183 of the 307 windows, the stock pile dipped below the $92,000 it started with." Attention drops because it's a stack of counts and a tangent right after the street walk, and it arrives before the payoff. The lines about 307 houses and "Most of the 1990s houses stay lit: 67.6 percent" are also number-dense.

5. No on both counts. The video says "None of this ranks stocks above a house, or a house above stocks," says it's "history, not a forecast," and lists limits (US only, no taxes, renters who never skip a month). It reports what happened and which assumptions matter without recommending or predicting prices, rents, or returns.

6. A viewer would take away that "rent and invest the difference" is not a sure win: over ten years it was about even, it favors the renter more with longer stays, and the result is sensitive to the rent-to-price ratio, fees, and whether the renter actually invests the monthly gap. A sensible takeaway is to compare your own local rent and price and expected stay length rather than trust the slogan.

7. That advice is largely my own conclusion. The narration frames the evidence and sensitivities ("the tag decides," "how long Nina herself will stay") and explicitly declines to recommend, though it does lean toward implying that horizon and rent level matter, which makes my takeaway a fairly natural reading.

8. Partly yes. It directly answered whether the renter ends up ahead: about half the time over ten years, mostly yes over fifteen, mostly no with cash, and dependent on rent. It did not give Nina a verdict, since it says her own month isn't on the street and its outcome is unknown. The most useful parts were the stocks-versus-cash comparison and the explanation that the mortgage lets the house grow on the whole $400,000 base while the pile starts at $92,000.
