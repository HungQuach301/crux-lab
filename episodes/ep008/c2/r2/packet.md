# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
**Đúng câu hỏi** (câu 1–2): video hỏi tiền thuê nhà của Nina (người thuê, minh hoạ) có "phí" không — **mua nhà hay tiếp tục thuê**, khi tính đủ chi phí sở hữu, qua hai người giống hệt (một mua, một thuê) phát lại trên lịch sử thật của Mỹ.
**Đúng đáp án** (câu 2): phát lại 307 tháng bắt đầu từ 1991 (giữ 10 năm), **người mua hơn ở khoảng 3/4** số tháng; **người thuê hơn ở một dãy tháng quanh 2001–2007** (tệ nhất June 2006, người mua kém khoảng $82,000); **và** kết quả **đổi theo tiền thuê giả định** (thẻ tiền thuê: thuê thấp hơn → ít tháng người mua hơn, cao hơn → nhiều hơn). Cần "khoảng 3/4 (hoặc đa số)" + ít nhất một trong: dãy 2001–2007/2006 / phụ thuộc tiền thuê giả định / kỳ hạn 5–15 năm. Đủ câu hỏi + đáp án → 1; một trong hai → 0,5; không → 0. Kể "mua luôn thắng" hay "video bảo nên mua" → không được 1.
**Câu khuyên (A28):** `advice_stated` khi câu 5 "yes" vì tin video bảo mua hay thuê / dự báo giá-thuê-lãi, **hoặc** câu 6–7 nêu lời khuyên hành động MÀ người đọc nói video gợi ra (mua, thuê, chờ, mua trước khi…, giữ ≥ 10 năm…). `advice_inferred`: người đọc tự suy, câu 7 "my own conclusion". `caution_only`: thận trọng chung (tự tính, hỏi chuyên gia). Người đọc **đúng** = điểm 1 và không `advice_stated`.
**Danh sách từ dễ đọc thành lời khuyên (luật tạm 13/10):** người chấm ghi `advice_words` = mọi cụm người đọc TRÍCH từ lời video làm căn cứ lời khuyên (vd "wins", "worth it", "the bar", "measured against").
**Khối mất chú ý** (câu 3–4): xếp chỗ người đọc nêu vào `phương pháp` / `định nghĩa` / `số dày` / `nhân vật` / `khác` / `không`, ghi cảnh ước (trích vài chữ).
**Câu hỏi mang tới** (câu 8): `answered_own`: true/false.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, "advice_words": ["..."], "attention_block": "phương pháp|định nghĩa|số dày|nhân vật|khác|không", "attention_scene": "<few words>", "answered_own": true|false, "why": "<one line>"} — grade ALL labels R1..R6, ...}

### R1
1. The video follows Nina, a renter in September 2026 who has saved a 20% down payment plus closing costs on a $400,000 home. It asks whether her rent is wasted. It replays history with twins, one who buys with a 30-year fixed mortgage and one who rents and holds cash, for every start month from January 1991 to July 2016, each followed for ten years. It shows the results as a street of 307 houses that light up when the buyer ends ahead and go dark when the renter does. It then varies the stay length (5, 10, 15 years), the assumed starting rent (4%, 5%, 6% of price), and the cash return, and ends by placing Nina's first-month cost beside the historical ones.

2. The answer is "not by any rule." Over ten years, the buyer ended ahead in about 3 of 4 start months (232 of 307; the renter won 75). All 75 renter wins fall between April 2001 and December 2007, and only 6 of the 72 starts from 2002 to 2007 favored the buyer. The median start left the buyer about $157,000 ahead. The best start (April 2012) left the buyer about $484,000 ahead, and the worst (June 2006) left the buyer $82,385 behind. Longer stays favor the buyer: at five years the buyer was ahead in 74.4% of starts, and at fifteen years in every start month. A higher assumed rent helps the buyer (64.2% at 4% rent, 92.2% at 6%). If the renter's cash earns T-bill interest, the buyer's share drops to about 2 in 3. Nina's own 2026 start can't be resolved because its ten years haven't happened.

3. Two passages confused me.
- "Nina's own month sits past the end of the street, in the fog, because its ten years haven't happened." This is fine on its own, but the later comparison is harder: "Her assumed rent, $1,667, is 56.8 percent of that. That's lower than in any start month on the street; the lowest was 57.9 percent, in July 2006." I had to work out that this is rent as a share of the buyer's first-month cost, and the video also says it doesn't make 2026 another 2006. It's unclear what I'm meant to conclude, except that Nina's rent looks relatively cheap compared with buying.
- "In one variant, the cash earns Treasury bill interest, and nothing more." It isn't stated plainly that in the main version the cash earns zero interest.
I also noticed that 2008 start months are never described, though the dark stretch ends in 2007 and the lit stretch begins in 2009.

4. The place where my attention dropped most was the Marcus and Priya passage: "Same rent tag, same costs, same street; only the month was different." It restates the best and worst houses I had just heard, so it added little.

5. No to both. The video says "Nothing here says whether to buy or to keep renting," and "history, not a forecast." It uses real past prices, rents and mortgage rates and makes no projection of where any of them go next.

6. A viewer could take away that the answer depends on when you start, how long you stay, and what rent you assume. Five years is risky, since the cost of buying and selling isn't covered, and fifteen years was never a loss in this record. Calling rent "wasted" is too simple, because the renter lost in some periods. And the 3-in-4 result is a historical count, not a promise for any one month.

7. Mostly my own conclusion. The video states the dependence on start month and rent ("it depends on the month she starts and the rent she assumes") and warns against reading it as advice. The points about stay length and avoiding short horizons are my inferences from the 5/10/15-year numbers, since the video says nothing about how long Nina stays.

8. Partly. It answered the historical question: counting interest, tax, insurance, repairs and transaction costs, renting came out ahead in only about 1 in 4 start months, all in 2001–2007. It did not answer whether renting costs more for me in 2026, since that outcome is unknown. It also isn't a full rent-versus-buy answer, because the renter's money sits in cash rather than stocks, a few costs are left out, and it covers only the national index, not a single city.

### R2
1. The video follows Nina, a renter in September 2026 who has saved a 20% down payment on a $400,000 home, and asks whether her rent is wasted. It replays a buying twin and a renting twin from every start month since 1991 (307 start months, each followed for ten years), using real US prices, rents and mortgage rates, with the renter's savings held in cash. The buyer ended ahead in about 3 in 4 start months, with a dark stretch from April 2001 to December 2007. It then varies the stay length and the assumed starting rent, and ends by saying the answer depends on the start month and the rent assumed.

2. Renting does not reliably cost more than buying. Over ten years, the buyer ended ahead in about 75% of start months (232 of 307), and renting came out ahead in the other 75, all between April 2001 and December 2007. The median buyer was about $157,000 ahead, the best case (April 2012) was about $484,000 ahead, and the worst (June 2006) was $82,385 behind. Over five years the buyer led in 74.4% of starts, and over 15 years in every start. With a 4% starting rent the buyer led in 64.2%, and with 6% in 92.2%. If the renter's cash earns T-bill interest, the share falls to about 2 in 3. Nina's own answer: "not by any rule", it depends on start month and rent.

3. Mostly nothing, but two spots were muddy. First: "Whatever renting saves each month is added to the same pile. In one variant, the cash earns Treasury bill interest, and nothing more." I couldn't tell whether the main run earns zero interest, and the "variant" only shows up again much later. Second: "Her assumed rent, $1,667, is 56.8 percent of that. That's lower than in any start month on the street; the lowest was 57.9 percent, in July 2006." It isn't clear what the comparison means for me, and the video says it doesn't make 2026 another 2006, yet it sets them side by side.

4. "Nina and her twin are illustrative; the home prices, rents and mortgage rates are real. US only, and history, not a forecast. Nothing here says whether to buy or to keep renting." My attention dipped here because it is a block of disclaimers before I know what the video is about, and the later repeats ("The limits are on the card...") are similar. The other low point was the stretch of precise figures around the 15-year and 5-year cases, where the numbers came fast.

5. No to both. It says outright that nothing in it says whether to buy or keep renting, and that it is history, not a forecast. It doesn't project future prices, rents or rates. It shows only what happened from each past start month, and it notes that Nina's own month can't be finished by history.

6. A viewer would take away that the outcome depends heavily on timing, on how long you stay, and on the rent you assume, so no simple rule holds. They might also take away that a short stay (five years) is riskier for a buyer, that buying costs plus a price slump can sink a purchase, and that the "rent is wasted" idea isn't reliably true. The video doesn't tell them what to do.

7. This is mostly my own conclusion. The narration frames the lessons as observations ("the lights move with the tag," "the picture is…") and avoids recommendations. The pattern that longer stays favor buying is clearly shown (five, ten, fifteen years), but turning that into "stay longer if you buy" is my inference, not something it says.

8. Partly. My question was whether renting costs more than buying once interest, tax, insurance and repairs are counted. The count of lit versus dark houses, the inclusion of those costs, and the $157,000 median answer it for history: usually not, but sometimes yes. It doesn't answer it for me today, because the renter's savings sit in cash rather than invested, which the video says is a different question, and it can't say how a 2026 start will end.

### R3
1. The video follows Nina, an illustrative person with enough saved for a down payment on a $400,000 home, who wonders whether her rent is wasted money. It replays the choice for every start month from 1991 to mid-2016, with one twin buying and one renting, and compares them after ten years using real US prices, rents, and mortgage rates. It shows the results as a "street" of houses that light up when buying won and go dark when renting won. It then tests other stay lengths and rent assumptions, and finally compares Nina's first-month costs to past months.

2. Not by any rule. Buying ended ahead in about 3 in 4 of the 307 start months (renting won in 75), with a median buyer lead of about $157,000. Every dark door falls between April 2001 and December 2007, and the buyer won only 6 of the 72 starts from 2002 to 2007. The extremes were April 2012 (buyer +$484,000) and June 2006 (buyer −$82,385). The answer depends on the start month and the assumed rent. At 4% starting rent the buyer won 64.2% of the time, at 6% it was 92.2%, and with Treasury-bill interest on the renter's cash it was about 2 in 3. Over five years the buyer won 74.4% of starts, and over fifteen years the buyer won every one.

3. "Nina's own month sits past the end of the street, in the fog" is only mildly unclear on a first listen. The part that actually confused me is this: "Her assumed rent, $1,667, is 56.8 percent of that. That's lower than in any start month on the street; the lowest was 57.9 percent, in July 2006." It isn't obvious why this ratio matters or what it implies, and the video says it doesn't predict anything. Also, "Nina pays rent again" in the opening line is odd, and "the card lists them" refers to something I couldn't see.

4. "So whether investing the difference would have done better is a different question, and this episode doesn't answer it." My attention dropped in the whole stretch about the renter's savings sitting in cash. It is a dense run of method detail (the pile, Treasury interest, the left-out costs), and the sentence reads as a disclaimer rather than something I could use.

5. No. The video says outright that it doesn't tell Nina whether to buy or rent, and that it is "history, not a forecast." It replays past months with real data and doesn't project future prices, rents, or rates. It also stresses that a national index is not any one house or city.

6. A viewer would likely take away that the outcome depends heavily on timing and on the rent assumed, that a short stay (about five years) is riskier for buyers, and that a longer stay has historically favored buying. That is a reading of the results, since the video gives no advice.

7. Mostly my own conclusion. The narration presents the shorter-versus-longer pattern as a finding ("the dark doors thin out, and then they're gone"), but it explicitly declines to advise and says the fifteen-year result "says nothing about how long Nina stays." Turning that into guidance is my inference.

8. Partly. I came for "is renting wasted money versus buying?" It answered that with the historical distribution: buying usually won over ten years, but not in 2001–2007 starts. Its refusal to give a verdict, and the unanswered question about investing the difference, left me without a firm answer.

### R4
1. The video follows Nina, a renter in September 2026 with enough saved for a 20% down payment on a $400,000 home. It asks whether her rent is wasted money. It replays 307 monthly start dates from 1991 to 2016, each with a buying twin and a renting twin, using real US prices, rents and mortgage rates. After ten years, each start month is judged by whether the buyer's equity (after selling costs) beat the renter's cash pile. It then varies the assumptions (holding period, starting rent, what the cash earns) and ends by comparing Nina's first-month costs with past starts.

2. Its answer is that renting does not cost more than buying "by any rule." It depends on the start month and the assumed rent. Over ten years the buyer ended ahead in about 3 in 4 of the 307 start months. The median gap was about $157,000, ranging from +$484,000 (April 2012) to -$82,385 (June 2006). Almost all the renter wins fall between April 2001 and December 2007. The buyer share moves with the assumptions:
   - It is 64.2% with a 4% starting rent and 92.2% with a 6% starting rent.
   - It is about 2 in 3 if the renter's cash earns T-bill interest.
   - It is 74.4% over five years, and every start month ends with the buyer ahead over 15 years.

3. "Her assumed rent, $1,667, is 56.8 percent of that. That's lower than in any start month on the street; the lowest was 57.9 percent, in July 2006." I couldn't tell whether a lower ratio is good or bad for renting, and the video says only that it "compares first months only." The earlier line "the renting twin's savings sit in cash, not in stocks" also made me stop, because I had to work out that the comparison isn't "rent and invest" versus "buy."

4. "The Census Bureau's public figures sit inside the range we turned, and they're a reference, not Nina's own rent." My attention dropped here because it gives no number or conclusion I can use. The disclaimers around it (the limits on the card, US only, history not a forecast) also felt repetitive.

5. No. It says outright that "nothing here says whether to buy or to keep renting," and that this is "history, not a forecast." It doesn't predict prices, rents or rates. It only shows how past start months turned out.

6. A viewer could take away that renting isn't automatically "wasted money" and buying isn't automatically a win. The result depends on timing, how long you stay, and what rent you assume. Staying longer made the buyer's side look much safer, and five years looked risky. A cautious viewer would test their own rent and time horizon before deciding.

7. That advice is mostly my own conclusion. The narration gave findings (shares, dollar gaps, how they shift with horizon and rent) and repeatedly declined to say what Nina should do. The "stay longer" point is an inference from the 5/10/15-year numbers, and the video even says the street "says nothing about how long Nina stays."

8. Partly. My question was whether renting costs more once interest, tax, insurance and repairs are counted. The video answered that buying came out ahead in about 3 in 4 historical start months even with those costs, but with a clear dark stretch from 2001 to 2007. It didn't answer it for a 2026 start, which can't be known. The renter's cash earning only T-bill interest, and some left-out costs, also limit how far I can apply it. The most useful parts were the horizon comparison and the rent-assumption sensitivity.

### R5
1. The video follows Nina, a renter in September 2026 who has saved a 20% down payment on a $400,000 home, and asks whether her rent is wasted. It replays a "buying twin" and a "renting twin" starting in every month from January 1991 to July 2016 (307 start months), each followed for ten years. The renter's savings sit in cash, and a house "lights up" if the buyer's equity after selling costs beats the renter's cash. It then varies the stay length, the starting rent, and the cash's interest rate, and ends by comparing Nina's first-month cost to past starts.

2. Not by any rule. Over ten years the buyer ended ahead in about 3 in 4 of the 307 start months, and the renter in the other 75. All the renter wins fall between April 2001 and December 2007; only 6 of 72 starts from 2002 to 2007 favored the buyer. The median buyer was about $157,000 ahead, the best case (April 2012) about $484,000 ahead, and the worst (June 2006) $82,385 behind. Results shift with the assumptions:
   - Stay length: five years gives the buyer 74.4%, and fifteen years gives every start month.
   - Starting rent: 4% of price gives the buyer 64.2%, and 6% gives 92.2%.
   - Cash earning T-bill interest: the buyer's share falls to about 2 in 3.

3. "Nina's answer: not by any rule; it depends on the month she starts and the rent she assumes, and the lights are history." It's an abrupt close, and "the lights are history" is metaphorical. Also confusing: "Her assumed rent, $1,667, is 56.8 percent of that. That's lower than in any start month on the street; the lowest was 57.9 percent, in July 2006." The "of that" refers back to $2,933, and the point of the comparison only arrives in the next sentence. Another is "In one variant, the cash earns Treasury bill interest, and nothing more," because the base case's cash treatment is never stated plainly. Also unclear: "Those buyers started from lower prices and lower mortgage rates," which sits oddly with the 2012 claim that "national prices more than doubled over the window," since that could mean either more or less than the stated cause.

4. "Counted along the whole street, the picture is this. In about 3 in 4 of the 307 start months, the buyer ended ahead. In the other 75, the renter did." My attention dropped in the stretch of statistics that follows (the 72 start months, 6 of them, and the dense run of percentages and dollar figures for best, worst, and median months). Many numbers arrive in quick succession, with the visual street doing little to anchor them.

5. No. The video says outright that nothing in it says whether to buy or keep renting, and it calls its results "history, not a forecast." Its prices, rents and mortgage rates come from the real record, but it does not project any of them forward, and it says a 2026 start can't be assumed to end like a 2006 one.

6. A viewer would likely take away that the buy-vs-rent result depends heavily on timing, stay length, and the rent assumed, so a single break-even answer is unreliable. Buying looks safer the longer you stay (fifteen years never lost in this record, five years is risky), and a short stay or a start near a price peak with high rates has been the worst case. A viewer might also check their own rent against the price, since that assumption moves the answer a lot.

7. Mostly my own conclusion. The narration describes the pattern and its sensitivities but avoids recommending anything, and even the final line says the answer is not by any rule. The "longer stays are safer" idea comes from the five-, ten- and fifteen-year comparison, which the video presents as findings, not advice, and it adds that this "says nothing about how long Nina stays."

8. Partly. My question was whether renting costs more than buying once interest, tax, insurance and repairs are counted. The video does answer that for history: with those costs included, renting cost more in about 3 in 4 ten-year starts but not in the 2001 to 2007 starts, and the share depends on stay length and rent. It does not give me a single answer for my own situation, because it leaves out the investment alternative (stocks), keeps the renter's savings in cash, and says nothing about 2026's outcome. The most useful parts were the ten-year street, the rent-tag sensitivity, and the comparison of Nina's first-month cost to past starts.

### R6
1. The video follows Nina, a renter in September 2026 who has saved a 20% down payment on a $400,000 home, and her illustrative twins, one who buys and one who rents. It replays that choice from every start month between January 1991 and July 2016 using real US prices, rents and mortgage rates, comparing the buyer's equity after selling costs to the renter's cash pile after ten years. It shows the results as a street of 307 houses, lit when the buyer wins and dark when the renter wins. It then tests how the picture changes with the length of stay, the assumed starting rent, and what the renter's cash earns, and ends by placing Nina's own first month beside the historical ones.

2. The answer is "not by any rule; it depends on the month she starts and the rent she assumes." Specifically, over ten years the buyer ended ahead in about 3 of 4 of the 307 start months (232 of 307, with the renter ahead in 75). Every renter win falls between April 2001 and December 2007; the buyer won only 6 of the 72 starts from 2002 through 2007. The median buyer was about $157,000 ahead, ranging from +$484,000 (April 2012) to -$82,385 (June 2006). The share moves with the assumptions:
   - At a 5-year horizon it is 74.4%, and every 15-year start had the buyer ahead.
   - At a 4% starting rent it is 64.2%, and at 6% it is 92.2%.
   - With the renter's cash earning T-bill interest it falls to about 2 in 3.

   So renting did cost more than buying in most historical windows, but not in all, and the answer is conditional.

3. Nothing seriously confused me, but two passages made me pause:
   - "In one variant, the cash earns Treasury bill interest, and nothing more." It's unclear at that point what the base case is, since it's said the cash "sits in cash" and then a variant is mentioned. I assume the base case earns zero interest, but it isn't stated outright.
   - "Her assumed rent, $1,667, is 56.8 percent of that. That's lower than in any start month on the street..." It takes a moment to work out that this is rent as a share of the buyer's first-month cost, and that a lower ratio is meant as a caution.

4. "Property tax, insurance and repairs come to 2.5 percent of the home's value a year. The twin who rents moves into an equivalent home and keeps the same savings." My attention dipped slightly in the dense cost-definition run, because several assumptions arrive in quick succession without a visual anchor in the narration alone. It wasn't a strong drop, and the later paragraph on the rent tag is the next-densest spot.

5. No on both counts. The video says "Nothing here says whether to buy or to keep renting," and repeats "history, not a forecast." It also says it doesn't answer whether investing the difference would have done better, and it notes that the national index is not any single home or city.

6. A viewer would take away that the answer depends on the start month, the holding period, and the assumed rent. Longer stays make buying look better in this history, and a five-year stay left little time to cover buying and selling costs. A viewer might reasonably conclude they should test their own rent, horizon and local prices rather than trust a single rent-versus-buy verdict. The video does not tell them what to do.

7. That is largely my own conclusion. The narration observes patterns (five years leaves little time to cover the costs, the dark doors thin out by fifteen years) and says the answer varies with the month and the rent, but it avoids prescribing action. The "test your own assumptions" advice is my inference from the sensitivity results.

8. Partly. I came asking whether renting costs more than buying once interest, property tax, insurance and repairs are counted. The video answers that for the historical record: in about 3 in 4 start months the buyer ended ahead, with those costs and the costs of buying and selling included. It does not settle it for a 2026 start, because Nina's ten years haven't happened, and it says its comparison of first-month costs doesn't predict how 2026 ends. So I got a clear historical answer, but not a verdict for my own situation.
