# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
**Đúng câu hỏi** (câu 1–2): video hỏi giữa **khoản vay 15 năm** và **khoản 30 năm trả hết trong 15 năm** (giữ khoản trả tối thiểu thấp hơn làm đường lui), qua người mua Tessa.
**Đúng đáp án** (câu 2): khoản 30 năm trả trong 15 năm = khoản 15 năm **cộng một đường lui có giá**: tuần này khoảng **$120/tháng, $21,622 qua 15 năm**; theo lịch sử từ 1991 giá này dao động (khoảng $6,100–$29,500, trung vị khoảng $16,600; tuần này đắt — ít hơn 1/5 số tuần cao bằng), theo **chênh lãi** 30 vs 15 năm; **và/hoặc** mỗi đô la trả thêm "được" đúng **lãi khoản vay (7.40%)** — mốc cách dùng tiền khác phải vượt. Cần ý "đường lui có giá bằng đô la" + ít nhất một trong: con số tuần này / dải lịch sử / mốc = lãi khoản vay. Đủ câu hỏi + đáp án → 1; một trong hai → 0,5; không → 0.
**Câu khuyên:** `advice: true` khi câu 5 "yes" vì tin video bảo chọn khoản vay nào / bảo trả thêm hay đầu tư / dự báo lãi, **hoặc** câu 6 nêu lời khuyên hành động (chọn 15 năm, chọn 30 năm, trả thêm, đầu tư, trả theo tháng thay vì năm…). Câu 6 kiểu "so lãi khoản vay với cách dùng tiền khác / biết giá của đường lui" là hiểu lời hứa, **không** tính. Người đọc **đúng** = điểm 1 và không câu khuyên.
**Khối mất chú ý** (câu 3–4): xếp chỗ người đọc nêu vào một loại: `phương pháp` / `định nghĩa` / `số dày` / `nhân vật` / `khác` / `không`, và ghi cảnh ước (trích vài chữ).
**Câu hỏi mang tới** (câu 7): `answered_own`: true/false — người đọc nói video có trả lời câu hỏi họ mang tới không.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "block": "phương pháp|định nghĩa|số dày|nhân vật|khác|không", "scene": "<few words>", "answered_own": true|false, "why": "<one line>"}, ...}

### R1
1. The video follows Tessa, an illustrative borrower taking a $320,000 mortgage, who wants to pay it off in 15 years but is torn between a true 15-year loan and a 30-year loan paid down on a 15-year schedule. It shows that the 30-year paid in 15 costs $120 a month more ($21,622 over 15 years) than the real 15-year, and that this extra is the price of keeping a lower required payment as a fallback. It then replays every survey week since 1991 to show this week's price is high by history (driven by the gap between 30- and 15-year rates, not the rate level). Finally it covers side questions (matching the 15-year payment, yearly vs. monthly extras) and the "bar": an extra principal dollar earns the loan's own rate, 7.40% pre-tax for Tessa.

2. The answer: the 30-year paid in 15 is the 15-year loan plus a fallback, and this week that fallback costs Tessa $120 a month, or $21,622 in total interest difference ($210,691 vs. $189,069). That price is higher than typical: the median since 1991 is $16,631, the range is $6,097 to $29,502, and fewer than 1 in 5 weeks cost more. The price tracks the 30-vs-15 rate gap (0.67 point this week vs. a 0.57 average), not the rate level. The fallback itself is a roughly $613 monthly drop in required payment.

3. "The bigger payment fits her budget today, but only just" is mildly confusing, since it's not obvious at first whether "bigger payment" means the 15-year's $2,828 or the $2,948 paid-early version. Also "His fallback was cheaper: $13,231 over 15 years, about $74 a month. And it was bigger: his required payment sat about $793 a month below..." reads oddly because "cheaper" and "bigger" refer to different things (price vs. size of the payment cushion). Lastly, "the difference between those last two totals is exactly the stack" is slightly muddled because the list of three interest totals comes before it and "last two" isn't obvious on first hearing.

4. "The bar moves with the rate a loan was taken at. Since 1991, it has stood as high as 9.25 percent, in November 1994." Attention dipped in the stretch of decade-by-decade figures and rate extremes, where several similar numbers stack up (7.73, 6.18, 4.03, and $15,118, $14,210, $20,374) and are hard to hold in mind by ear. The most notable drop was the lengthy disclaimer paragraph: "How this was built is on the method card and in the description. The rates are weekly US survey averages for borrowers with strong credit and a large down payment..." because it's a dense list of caveats with no new narrative.

5. No on all three. The video explicitly says it is US only, history rather than a forecast, and that it won't say which loan to take or whether to invest. It prices the fallback and states the bar (the loan's rate, pre-tax) without comparing it to any market return, and it says the value of a lower payment in a emergency isn't measured.

6. A viewer wouldn't get a directive, but they could take away: if you plan to pay a 30-year like a 15-year, you're buying a fallback, so ask what it costs in your week's actual rate pair; look at the gap between 30- and 15-year offers, not just the rate level; extra principal earns your loan's own rate before taxes, which is the bar other uses of money must clear; and monthly extras beat a yearly lump sum on interest, though that's a cash-flow choice.

7. Yes, for the question the video itself posed: how much the fallback costs, whether that's normal, and what an extra principal dollar earns. The pricing and history sections (the $120 a month, $21,622 stack, and the median/range comparison) answered it most directly. It did not answer the question of which loan to choose, which it said up front it wouldn't.

### R2
1. The video follows Tessa, an illustrative buyer borrowing $320,000 this week at 6.73% for 15 years or 7.40% for 30 years. She wants to be debt-free in 15 years but also wants a cheaper required payment for a bad month. It prices that "fallback" as the extra cost of a 30-year paid like a 15-year versus a true 15-year: $120 a month, or $21,622 over 15 years. It then replays 1,833 weeks of rate history since 1991 to show whether that price is normal, and explains that an extra dollar of principal "earns" the loan's own rate, which it calls the bar.

2. The video says a 30-year loan paid off in 15 years is not the same as a 15-year loan. It is the 15-year plus a fallback, and this week the fallback costs Tessa about $120 a month. The cost comes from the 30-year rate being 0.67 point higher than the 15-year rate. Across history the price ranged from $6,097 (Dec 2008) to $29,502 (Jan 2023), with a median of $16,631. Tessa's price is expensive by history but not a mistake. For the "pay extra vs. invest" part, the answer is that each extra dollar earns 7.40% a year pre-tax for her. That is the bar any alternative use must clear, and it is high, since only about 1 week in 5 had a bar that high.

3. Two passages confused me.
- "And it was bigger: his required payment sat about $793 a month below the 15-year's." The "it" is unclear. It seems to mean Leo's fallback (the cushion) was bigger even though its price was smaller, but that took me a moment to work out.
- The word "fallback" is used for two things: the $613 a month gap in required payments, and its price of $120 a month. The opening line, "Tessa's mortgage fallback costs $120 a month," is fine once you know this, but I had to sort it out.

I was also briefly thrown by "Her answer: the 30-year paid in 15 is the 15-year plus a fallback," because Tessa never actually decides anything.

4. My attention dropped most in the caveats paragraph: "The rates are weekly US survey averages for borrowers with strong credit and a large down payment; real offers differ in points, fees and terms. Payments here are principal and interest only: no property taxes, no homeowners insurance, no private mortgage insurance, no tax deductions." It is a long run of exclusions in one flat list, after the story had already peaked, so it reads as a legal disclaimer. The decade-by-decade comparison (medians, rates, gaps) was also number-heavy, but it had a payoff, which was that lower rates did not mean a cheaper fallback.

5. No to all three, and the video says so explicitly. It states it won't say which loan to take or whether to invest, and that it is "history, not a forecast." It also notes that the bar "isn't compared with any market return here." It only prices the fallback and states the bar.

6. The video gives no direct advice, but a viewer could take away these points:
- Compare your own pair of offers. The price of flexibility depends on the gap between the 15-year and 30-year rates that week.
- An extra dollar of principal earns your loan's own rate, pre-tax, and that is the number to beat.
- A lower rate does not mean a cheaper fallback, because a wider gap does.
- Paying the 30-year at the 15-year's payment amount ends late, and a lump sum once a year costs more interest than monthly extras.
- Money paid into the house is hard to get back in a bad month, which is what the fallback is for.

7. Partly. I came wondering whether to pay extra or invest. The video answered the first half: paying extra earns exactly the loan's rate (7.40% pre-tax for Tessa), and it showed what keeping flexibility costs ($120 a month). It did not answer the invest half, since it never says what investments might return or whether to prefer them. I left with the bar to beat but without a decision.

### R3
1. The video follows Tessa, an illustrative buyer borrowing $320,000 at this week's rates: 6.73% for the 15-year loan and 7.40% for the 30-year. She is deciding between a true 15-year loan and a 30-year loan that she pays off in 15 years. The 30-year keeps a lower required payment ($2,216 vs $2,828) as a fallback for a bad month. The video prices that fallback at $120 a month, or $21,622 over 15 years, then compares it with every week's rates since 1991 (1,833 weeks). It ends by reframing extra principal payments as earning the loan's own rate, 7.40% before tax for Tessa, and uses Leo's 2021 loan at 2.65% as a contrast.

2. Its answer is that a 30-year paid in 15 is the 15-year loan plus a fallback, and the fallback has a price. This week it costs Tessa $120 a month, or $21,622 in extra interest. That is high by history: the median week was $16,631, the range was $6,097 (Dec 2008) to $29,502 (Jan 2023), and fewer than 1 in 5 weeks cost this much. The driver is the gap between the 30-year and 15-year rates (0.67 point now, against a 0.57 average), not the level of rates. Each extra principal dollar earns the loan's own rate (7.40% pre-tax for Tessa), and that rate is the bar any alternative must clear.

3. One passage confused me: "And it was bigger: his required payment sat about $793 a month below the 15-year's." "It" is unclear. I think it means his fallback in monthly protection was bigger, while its dollar cost was smaller, but that comes right after "His fallback was cheaper," so it reads like a contradiction. A smaller point is the opening line, "Tessa's mortgage fallback costs $120 a month," which uses "fallback" before it is defined. I also wasn't sure why Leo's stack was only $13,231 when his required payment sat $793 below the 15-year's, which was a bigger gap than Tessa's.

4. My attention dropped most in the disclaimer paragraph, especially: "The rates are weekly US survey averages for borrowers with strong credit and a large down payment; real offers differ in points, fees and terms. Payments here are principal and interest only: no property taxes, no homeowners insurance, no private mortgage insurance, no tax deductions." It is a long run of exclusions in one block with no new idea. The decade-by-decade run of medians and rates was also dense with numbers.

5. No to all three, and the video says so explicitly: "It won't say which loan to take, or whether to invest," and "it's history, not a forecast." It prices the fallback and states the 7.40% bar, but it deliberately doesn't compare that bar with any market return or say what the lower payment is worth to the viewer.

6. The video gives no direct advice. A viewer could take away a few things:
- Ask what the lower-payment fallback costs.
- Compare your own loan rate, which is the bar, with what else you could do with the money.
- Remember that money paid into the house is hard to get back in a bad month.
- Treat the rate gap between the 15-year and 30-year offers as the main driver of the price.

7. Partly. I came wondering whether to pay extra or invest instead. The video answers the paying-extra side well: an extra dollar earns the loan's rate, 7.40% pre-tax, and keeping the fallback costs $120 a month this week. It does not answer the invest side, because it never compares the bar with an investment return. It also doesn't say what to do given that I can only just afford the 15-year payment, so I'm left to make that judgment myself.

### R4
1. The video follows Tessa, an illustrative buyer borrowing $320,000 in an expensive city. She can just afford a 15-year loan, and she wonders whether to take a 30-year loan and pay it off in 15 years, keeping the lower required payment as a fallback. It prices that fallback at this week's rates: $120 a month, or $21,622 over 15 years. It then compares that price with every week since 1991 and shows it depends on the gap between the 15-year and 30-year rates. It ends by explaining that an extra dollar of principal "earns" the loan's own rate, which it calls the bar. It uses Leo, who borrowed in January 2021, as a contrast.

2. The main question is whether to take a 15-year loan or a 30-year paid in 15. Its answer is that the 30-year paid in 15 is the 15-year loan plus a fallback, and this week that fallback costs Tessa $120 a month. The extra interest is $210,691 versus $189,069, a difference of $21,622. By history that is expensive. The median week is $16,631, the range runs from $6,097 to $29,502, and fewer than 1 in 5 weeks cost more. The price tracks the 30-year-over-15-year rate gap (0.67 point now, against an average of 0.57), not the level of rates. Her bar for extra principal is 7.40% before taxes, which is high: only about 1 week in 5 had a bar that high.

3. "And it was bigger: his required payment sat about $793 a month below the 15-year's." Right after saying Leo's fallback was cheaper, "it was bigger" has no clear referent until the rest of the sentence arrives. It means the payment cushion was bigger, not the cost, and that was hard to follow by ear. I was also briefly unsure about the opening line, "Tessa's mortgage fallback costs $120 a month," because "fallback" isn't defined until later. It resolved itself.

4. "The rates are weekly US survey averages for borrowers with strong credit and a large down payment; real offers differ in points, fees and terms." This sits in the long disclaimer paragraph near the end. It is a dense run of caveats (no taxes, insurance, PMI, deductions, no market comparison, and so on) delivered in a flat list right after the emotional payoff of Leo and the bar. The attention drop is from the density and from there being no new information to follow.

5. No to all three. The video says outright that it "won't say which loan to take, or whether to invest," and that it's "history, not a forecast." It says the gap has moved before and nothing in it says where the gap goes. It only prices the fallback and states the bar.

6. The video gives no direct advice, but a viewer could take away these points:
- The fallback has a dollar price, and it depends on the 15-year/30-year rate gap, so compare both offers.
- Paying the 15-year amount on a 30-year doesn't finish in 15 years. It ends about 15 months late, and she'd need $733 extra a month.
- Monthly extra payments cost less interest than one yearly lump sum, by about $8,200 here.
- Your own loan rate is the bar that any other use of the money has to clear.
- A dollar paid into the house is hard to get back in a bad month.

7. Partly. My question was whether to pay extra or invest, with a 15-year payment I can barely afford. It answered the 15-year versus 30-year-paid-in-15 part well: the fallback costs $120 a month, and that is high by history. It also gave the bar, 7.40% before taxes, for extra principal. It never compared that bar with any investment return, and it declined to say what the fallback is worth in a bad month. So the invest-versus-prepay half of my question went unanswered.

### R5
1. The video follows Tessa, an illustrative buyer borrowing $320,000 at this week's rates (6.73% for 15 years, 7.40% for 30). She is choosing between a true 15-year loan and a 30-year loan paid off in 15 years. It replays every week since 1991 (1,833 weeks) to price the difference. The 30-year paid in 15 costs $120 a month more, or $21,622 over 15 years, and that is the price of keeping a lower required payment as a fallback. It then shows that the price depends on the gap between the 15-year and 30-year rates, and that an extra dollar of principal earns the loan's own rate, which is the "bar" any alternative use of the money must clear.

2. The main answer is that a 30-year paid in 15 is the 15-year loan plus a fallback, and this week the fallback costs Tessa about $120 a month. Her required payment would be $2,216 instead of $2,828, a cushion of roughly $612 a month in a bad month. Her price is high by history: the median across all weeks is $16,631, the range is $6,097 to $29,502, and fewer than 1 in 5 weeks cost more. Her extra principal earns 7.40% a year before taxes, which is high compared with history (about 1 week in 5 had a bar that high).

3. Several spots confused me:
- "And it was bigger: his required payment sat about $793 a month below the 15-year's." It follows "His fallback was cheaper," and "bigger" doesn't say what is bigger. I had to infer that it means the payment cushion.
- "That makes Tessa's fallback expensive by history, not a mistake." No one suggested a mistake, so "not a mistake" comes out of nowhere.
- "Same plan, a different week, and it means something else." This is vague.
- "Her answer: the 30-year paid in 15 is the 15-year plus a fallback..." This is framed as Tessa's answer, but earlier the video said it won't say which loan to take, so it reads like a conclusion nobody reached.
- A small mismatch: the payments given ($2,828 and $2,216) differ by $612, but the narration says "about $613."

4. My attention dropped most in the closing caveats: "How this was built is on the method card and in the description. The rates are weekly US survey averages for borrowers with strong credit and a large down payment; real offers differ in points, fees and terms." It is a long run of disclaimers in a flat list, said right after the interesting Leo comparison. Some of it repeats the intro's "US only, history, not a forecast."

5. No to all three, and the video says so itself. It states it "won't say which loan to take, or whether to invest," and that it is "history, not a forecast." It also says the bar "isn't compared with any market return here." It describes and prices a tradeoff but never recommends or forecasts.

6. There is no explicit advice, but a viewer could take away these points:
- Price the fallback for your own loan by looking at the gap between that week's 15-year and 30-year rates.
- Treat your own loan's rate as the bar. Extra principal earns that rate, before taxes, with certainty.
- Don't assume paying the 15-year amount on a 30-year loan ends it in 15 years. It ran about 15 months late in Tessa's case.
- Extra payments don't lower the required payment, so the cushion stays.
- Paying extra monthly beats one lump sum a year, which cost about $8,200 more in interest.
- Money paid into the house is hard to get back in a bad month, and the video doesn't value that.

7. Only partly. My question was whether to pay extra on the mortgage or invest the spare cash. The video answers a neighboring question well: what it costs to keep a lower required payment while paying like a 15-year borrower. It also gives the key number for the invest-versus-prepay comparison, the 7.40% pre-tax bar. But it deliberately doesn't compare that bar with investment returns, taxes, or risk, so it never answers the invest-or-prepay question. Because I can just afford the 15-year payment, the fallback-cost framing is useful to me, but I'd have to do the investing comparison myself.

### R6
1. The video follows Tessa, an illustrative buyer borrowing $320,000 in an expensive city. She is choosing between a true 15-year mortgage and a 30-year loan she pays off in 15 years anyway, which keeps a lower required payment as a fallback. It prices that fallback at this week's rates ($120 a month, $21,622 over 15 years), then replays every week since 1991 to show whether that price is typical. It also explains that an extra dollar of principal "earns" the loan's own rate, which is 7.40 percent for Tessa. It compares her with Leo, who borrowed at 2.65 percent in 2021, and ends with caveats.

2. The main question is "a 15-year, or a 30-year paid in 15?" The video's answer is that the 30-year paid in 15 is the 15-year plus a fallback, and the fallback has a price. For Tessa that is $120 a month more, or $21,622 over 15 years: $2,948 versus $2,828 a month, and $210,691 versus $189,069 in interest. By history that price is high. The median across 1,833 weeks is $16,631, and fewer than 1 in 5 weeks cost this much. The price depends on the gap between the 30-year and 15-year rates (0.67 point now, against a 0.57 average), not on the rate level. Her bar for any other use of the money is 7.40 percent before taxes, and only about 1 week in 5 had a bar that high.

3. Two spots confused me.
- The opening line, "Tessa's mortgage fallback costs $120 a month." Later, "That gap, about $613 a month, is the fallback." The word "fallback" is used for both the $613 cushion and the $120 price, so I had to work out which was which.
- "His fallback was cheaper: $13,231 over 15 years, about $74 a month. And it was bigger: his required payment sat about $793 a month below the 15-year's." "Cheaper and bigger" reads like a contradiction until you see that it means a lower price for a larger cushion.

4. The place where my attention dropped most was the caveat block: "The rates are weekly US survey averages for borrowers with strong credit and a large down payment; real offers differ in points, fees and terms. Payments here are principal and interest only: no property taxes, no homeowners insurance, no private mortgage insurance, no tax deductions." It is a long run of disclaimers with no new story, and it repeats the earlier "US only, history, not a forecast" line.

5. No. It says outright that it won't say which loan to take or whether to invest, and it calls the replay "history, not a forecast," saying "nothing here says where it goes." It also notes that the bar "isn't compared with any market return here" and that the value of a lower payment in a job loss or emergency isn't measured.

6. It gives no directive advice, only things to take away:
- If you plan to pay a 30-year like a 15-year, you are paying for a fallback, so look at what it costs you.
- That price depends on the spread between the 30-year and 15-year offers, which you can check for your own loan.
- Extra principal earns your loan's own rate, before taxes. That is the bar any alternative use of the money has to clear.
- Extra payments don't lower the required payment, they only end the loan sooner.
- Monthly extras are cheaper than one yearly lump sum, by about $8,200 in interest here.
- Money paid into the house is hard to get back.

7. Partly. I came wondering whether to pay extra or invest the spare cash. The video answers the cost side well: what the extra payment costs, what it earns (7.40 percent, a guaranteed before-tax saving), and how that compares with history. It deliberately doesn't compare that bar with investment returns, so the "invest instead" half is left to me. It also doesn't weigh my tight budget against the safety of the lower payment, although it frames that as the tradeoff.
