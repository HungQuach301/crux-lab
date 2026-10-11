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
1. The video follows Tessa, an illustrative buyer borrowing $320,000 in an expensive city. She can just afford the 15-year payment, and she wants to be debt-free in 15 years. She is deciding between a true 15-year loan and a 30-year loan paid off in 15 years, which keeps a lower required payment for a bad month. It prices that "fallback" for her week: $120 a month, or $21,622 over 15 years. It then replays every week since 1991 (1,833 weeks) to see whether that price is normal. Last, it explains the "bar," meaning that an extra principal dollar earns the loan's own rate, and contrasts Tessa with Leo, who borrowed in January 2021.

2. The 30-year paid in 15 years is the 15-year loan plus a fallback, and the fallback has a price. For Tessa it is about $120 a month, because the 30-year rate is 7.40% against 6.73%, a gap of 0.67 point. Historically the price depends on that rate gap, not on the rate level. It ranged from $6,097 (Dec 2008) to $29,502 (Jan 2023), with a median of $16,631. Tessa's is high by history, but it isn't a mistake. Each extra dollar she pays earns 7.40% before taxes, as interest avoided. That is a bar any other use of the money would have to clear.

3. One passage confused me: "His fallback was cheaper: $13,231 over 15 years, about $74 a month. And it was bigger: his required payment sat about $793 a month below the 15-year's." Saying the fallback was both "cheaper" and "bigger" without explanation made me stop and work out that "bigger" means a larger payment cushion. The line "That makes Tessa's fallback expensive by history, not a mistake" was also slightly unclear, since "mistake" hadn't been raised before.

4. "In the 2000s, with rates near 6.18 percent, it cost about the same: $14,210." My attention dropped in the decade-by-decade run. Several similar dollar figures and rate levels came in a row, and the useful point (the gap matters, not the rate) only arrives a few lines later.

5. No to all three. The video says explicitly that it "won't say which loan to take, or whether to invest," and that "it's history, not a forecast." It does not predict future rates. It also says the gap has moved before and nothing in the data says where it goes next.

6. The advice is implicit. The 30-year paid in 15 years carries a quantifiable price for flexibility, so compare your own two rate offers to see what the fallback costs. Your extra-payment return equals your loan's rate, which is a benchmark for other uses of the money. Monthly extra payments beat a yearly lump sum on interest (about $8,200 less in Tessa's case). Paying the 15-year amount on a 30-year loan will not finish on time. The video also warns that money paid into the house is hard to get back in a bad month.

7. Partly. My question was whether to pay extra or invest the spare cash. The video gives a clear ruler for that: the 7.40% bar, plus the price of keeping flexibility. But it states that it does not test whether investments clear the bar, so the invest-versus-prepay comparison itself goes unanswered. The best-answered part was the 15-year versus 30-year-paid-in-15 comparison, with its $120 a month price tag.

### R2
1. The video follows Tessa, an illustrative buyer borrowing $320,000 in an expensive city. She is choosing between a true 15-year loan and a 30-year loan that she pays off in 15 years anyway. The video says the second option is the first plus a "fallback", the lower required payment she can drop to in a bad month, and it prices that fallback. It replays 1,833 weeks of real survey rates since 1991 to compare, then explains the "bar": the rate an extra dollar of principal effectively earns. It ends by contrasting Tessa (tall stack, high bar) with Leo (short stack, low bar).

2. The 30-year paid in 15 years is not the same loan as the 15-year. It costs more because the 30-year rate is higher, 0.67 point this week. For Tessa the 15-year payment is $2,828. Finishing the 30-year in 15 years takes $2,948, which is $120 a month more, or $21,622 over 15 years. That sum is the price of keeping a fallback payment of $2,216. Historically it has ranged from $6,097 to $29,502, with a median of $16,631. Tessa's price is high, with fewer than 1 week in 5 higher, but it is not a mistake. Each extra dollar of principal earns her 7.40% before tax, and the video says that is the bar any alternative must clear.

3. "And it was bigger: his required payment sat about $793 a month below the 15-year's." This confused me. "Bigger" follows "cheaper" with no setup, and it only becomes clear after a pause that it means Leo's cushion, the gap between his required payment and the 15-year payment, was larger. Also, the opening line, "Tessa's mortgage fallback costs $120 a month," uses "fallback" before it is defined. A second, smaller one is "the difference between those last two totals is exactly the stack." It is correct, but the stack metaphor has to be held in the head while three interest totals go by.

4. "Back to Tessa's own loan, and a shortcut many people reach for: pay the 30-year exactly what the 15-year would cost, and assume it ends on the same day." My attention dropped here because the video goes from the big historical picture back to one loan and then stacks several figures in a row: about 195 months, 15 months late, $733 extra, and then the annual-versus-monthly comparison. It also reads as a side topic, since it is not the main question and is only loosely tied to the bar and stack ideas.

5. No to all three, and the video says so more than once. It states that it won't say which loan to take or whether to invest, and that it is "history, not a forecast." It tests no investment return and makes no prediction of future rates or gaps. It describes Tessa's price as "expensive by history," but that is a description of the past, not a recommendation.

6. The video gives no explicit advice, but a viewer could take away these points:
- Paying a 30-year like a 15-year costs extra, and what you buy with it is flexibility.
- The 30-year does not end on schedule if you pay only the 15-year amount. You need the higher figure, $2,948 for Tessa.
- If you prepay, monthly beats a once-a-year lump sum, which costs about $8,200 more interest here.
- Your loan's own rate is the bar for any other use of the money.
- The price of the fallback depends on the gap between 15-year and 30-year rates, not on how high rates are.

7. Partly. My question was whether to pay extra on the mortgage or invest the spare cash, and the video answered only the mortgage side. It gave the bar, 7.40% before tax for Tessa's loan, as a ruler to hold an investment against, and it reframed my choice as "15-year versus 30-year plus a fallback." It explicitly declined to test whether any investment clears the bar. So I got the benchmark and the cost of flexibility, but not a verdict on investing.

### R3
1. The video follows Tessa, a hypothetical borrower taking out $320,000 in a high-cost city. She is weighing a true 15-year mortgage against a 30-year loan that she pays off in 15 years anyway. It prices the "fallback" (the option to drop to the lower required payment in a bad month) at $120 a month, or $21,622 over 15 years. It then replays 1,833 weeks of rates since 1991 to show that this price depends on the gap between 15-year and 30-year rates, not on the rate level. It ends by treating a loan's own rate as the "bar" any extra-principal alternative must clear.

2. The 30-year paid in 15 years is the 15-year loan plus a fallback, and the fallback has a price. For Tessa it is $120 a month more (about $2,948 vs $2,828), or $21,622 in total, because the 30-year rate is 0.67 point higher (7.40% vs 6.73%). By history that is expensive. The median week since 1991 was $16,631, and fewer than 1 in 5 weeks cost this much. Each extra dollar of principal "earns" her loan's rate, 7.40% before taxes, which only about 1 week in 5 has matched or beaten.

3. Quote: "And it was bigger: his required payment sat about $793 a month below the 15-year's."
It was unclear because "bigger" has no clear referent. I think it means the fallback was bigger, since the required payment was much lower, but it comes right after "cheaper." Two other spots were mildly confusing. "Tessa's mortgage fallback costs $120 a month" sits beside the $613 gap, which is also called "the fallback," so it takes a moment to see that $613 is the cushion and $120 is its price. The closing line, "Her answer:", also reads oddly, because Tessa never actually decides.

4. Quote: "What this leaves out is on the method card and in the description. This is US only, and it's history, not a forecast; it doesn't say which loan to take."
My attention dropped there because I'd already heard this caveat in nearly the same words near the start and again mid-video. By the end it read as boilerplate, and I was waiting for the conclusion. The decade-by-decade run of rates and dollar figures was also dense, but it was doing real work.

5. No to all three. It says outright that it won't say which loan to take, whether to invest, or where rates or the gap will go. It offers the 7.40% bar as a ruler for comparing other choices, but it does not test whether any investment clears it.

6. There is no direct advice, but a viewer could take away these points:
- Paying a 30-year at the 15-year's payment won't finish in 15 years. It runs about 15 months late.
- Paying the extra monthly beats paying it once a year, which costs about $8,200 more in interest.
- You can price the fallback by comparing that week's 15-year and 30-year offers.
- Your loan's rate is the guaranteed, pre-tax return on extra principal.
- Extra principal is hard to get back in a bad month, which is the cost of not having the fallback.

7. Partly. My question was whether to pay extra or invest, given that I can just afford the 15-year payment. The video answered the pay-extra side well. It showed what flexibility costs ($120 a month), what extra principal earns (my loan's rate, pre-tax), and how timing matters. It did not answer the invest side, since it never compares the bar to expected investment returns. It also didn't say whether the flexibility is worth $120 a month when I can only just afford the 15-year payment, so the final decision is left to me.

### R4
1. The video follows Tessa, an illustrative buyer borrowing $320,000 at this week's rates (6.73% for the 15-year, 7.40% for the 30-year). She is choosing between a true 15-year loan and a 30-year loan paid off in 15 years. It prices the 30-year's lower required payment, the "fallback", at $120 a month, or $21,622 over 15 years, because the 30-year rate is higher. It then replays every week since 1991 (1,833 weeks) to show that this price depends on the gap between the 30-year and 15-year rates, not on how high rates are. It ends by explaining that an extra principal dollar "earns" the loan's own rate, which is the bar any alternative has to clear.

2. The main question is "a 15-year, or a 30-year paid in 15?" Its answer is that the 30-year paid in 15 is the 15-year plus a fallback, and the fallback has a price. For Tessa that is $120 more per month, or $21,622 over 15 years, in exchange for a required payment about $612 lower in a bad month. By history that price is high: the median is $16,631, the range is $6,097 to $29,502, and fewer than 1 week in 5 was this expensive. It does not say whether the fallback is worth that price. Each extra dollar into the mortgage earns 7.40% before taxes for Tessa.

3. "Leo... His fallback was cheaper: $13,231 over 15 years, about $74 a month. And it was bigger: his required payment sat about $793 a month below the 15-year's." The word "bigger" is unclear at first. It means his cushion was larger, not his cost. Also, "fallback" means two things: the lower required payment (about $613 a month) and the cost of keeping it ($120 a month). The opening line, "Tessa's mortgage fallback costs $120 a month," uses the second meaning, but the video later calls the $613 gap "the fallback" too.

4. "What this leaves out is on the method card and in the description. This is US only, and it's history, not a forecast; it doesn't say which loan to take." My attention dropped here because the same disclaimer had already come up twice, near the start and in the middle. It is also a pointer to material off-screen, not new information.

5. No to all three. The video says it won't say which loan to take or whether to invest, and it calls its results history, not a forecast. It tells you what the fallback cost in past weeks, and it gives the loan's rate as a bar for comparison. The choice and the investment question are left to the viewer.

6. It gives no direct advice. The implied takeaways are:
- Price the fallback before choosing: compare the 15-year payment with the 30-year paid on a 15-year schedule.
- Look at the gap between the two rate offers, not just the level of rates.
- Extra principal earns your loan's rate, before taxes, with no risk.
- Paying the extra monthly beats a yearly lump sum on interest.
- Paying the 15-year payment amount on a 30-year loan won't finish in 15 years.
- Money paid into the house is hard to get back in a bad month.

7. Partly. My question was whether to pay extra or invest the spare cash. The video helped with the paying-extra side: it gave a concrete number for what extra principal earns (my loan's rate, here 7.40% pre-tax) and what the flexibility costs. It said clearly that it did not test whether investing beats that bar, and it also did not tell me whether to take the 15-year or the 30-year. So I leave with a ruler but not a verdict.

### R5
1. The video follows Tessa, an illustrative borrower taking a $320,000 mortgage, who is deciding between a true 15-year loan and a 30-year loan paid off in 15 years. It prices the 30-year's lower required payment (the "fallback") as the extra $120 a month, or $21,622 over 15 years, then replays every survey week since 1991 to see whether that price is typical. It shows the price depends on the gap between 15- and 30-year rates, compares Tessa to Leo (a 2021 borrower), and ends by framing each extra principal dollar as earning the loan's own rate, a "bar" other uses of money must clear.

2. The 30-year paid in 15 years is the 15-year loan plus a fallback, and the fallback has a price. For Tessa it is $120 a month ($2,948 vs. $2,828), or $21,622 over 15 years, equal to the interest difference between the two paid-off-in-15 loans ($210,691 vs. $189,069). By history that is expensive: the median is $16,631, the range is $6,097 to $29,502, and fewer than 1 in 5 weeks cost more. The driver is the rate gap (this week 0.67 point, typical 0.57), not the rate level. Extra principal earns her 7.40% before taxes, a high bar, in about the top fifth of weeks.

3. "Fewer than 1 in 5 weeks since 1991 put a price this high on it. That makes Tessa's fallback expensive by history, not a mistake" is mildly confusing, since "not a mistake" appears without anyone having called it one. Also, Leo's passage: "His fallback was cheaper: $13,231... And it was bigger: his required payment sat about $793 a month below the 15-year's." "Bigger" is unclear until you realize it means the payment cushion, not the cost. The $733 extra versus the $613 gap, and "the extra never lowers what the loan requires," also took a re-think.

4. "Any fixed-rate borrower can set their own pair beside hers. The bar is that loan's own rate, printed on the paperwork, and the stack depends on how far apart the 15-year and 30-year offers sit that week." Attention dipped there because it is abstract after the concrete Tessa/Leo comparison, and the "stack" and "bar" metaphors get heavy. The decade-by-decade run of figures (7.73%, 6.18%, 4.03%, $15,118, $14,210, $20,374) was also number-dense.

5. No, on all three. It states that it won't say which loan to take or whether to invest ("whether any investment clears it isn't tested here"), and it says it is history, not a forecast, noting the gap has moved before and nothing says where it goes.

6. There is no direct advice, but a viewer would take away a few things. Compare the 15-year and 30-year rate gap, since that sets what a fallback costs. Know your loan's own rate as the bar any extra-dollar use must clear. Remember that dollars paid into the house are hard to get back in a bad month. Monthly extra payments beat a once-a-year lump sum on interest (about $8,200 less).

7. Taking the likely question as "is paying a 30-year like a 15-year worth it versus just taking the 15-year?", it was answered in dollars: the fallback costs $120 a month this week, higher than usual, and it depends on the rate gap. The part that did it was the Tessa stack and the historical replay. It deliberately did not answer whether the fallback is worth that price to a given person.

### R6
1. The video follows Tessa, an illustrative buyer borrowing $320,000, who wants the house paid off in 15 years and is choosing between a true 15-year loan and a 30-year loan paid down on a 15-year schedule. It prices the difference. The 30-year paid in 15 years costs $120 a month more, or $21,622 over 15 years, because the 30-year rate is higher. In exchange, she keeps a lower required payment (about $613 a month less) for a bad month. It then replays every week since 1991 (1,833 weeks) to show that this price is high by historical standards and depends on the gap between the two rates, not the rate level. It ends by treating each extra dollar of principal as earning the loan's own rate, 7.40 percent for Tessa, as a bar that other choices must clear.

2. The video's answer is that the 30-year paid in 15 years is the 15-year loan plus a fallback, and this week that fallback costs Tessa $120 a month, or $21,622 in total. That stack is higher than the median of $16,631, and fewer than 1 in 5 weeks priced it this high. Her extra dollars of principal earn 7.40 percent before taxes, a bar reached in only about 1 week in 5. Whether the fallback is worth that price, the video says, it cannot measure.

3. The passage that confused me is "His fallback was cheaper: $13,231 over 15 years, about $74 a month. And it was bigger: his required payment sat about $793 a month below the 15-year's." Calling the same fallback "cheaper" and then "bigger" is jarring until you work out that "bigger" means the payment cushion. Also, "The bar moves with the rate a loan was taken at" took me a moment, because "the bar" is a coined term I had to hold in my head.

4. My attention dropped most here: "In the 2000s, with rates near 6.18 percent, it cost about the same: $14,210." It comes in the middle of a run of decade-by-decade rates and dollar figures. They are hard to hold in audio, and the real point (the gap matters, not the rate) only arrives a few sentences later.

5. No on all three. The video says explicitly that it "won't say which loan to take, or whether to invest," and that it is "history, not a forecast." It notes the rate gap has moved before and that nothing in the replay says where it goes. It also says it does not test whether any investment clears the 7.40 percent bar.

6. A viewer would take away a framework, not a directive:
- Price the fallback as the extra monthly cost of the 30-year paid in 15 years, compared with the 15-year loan.
- Look at the gap between the 15-year and 30-year offers that week, not just the rate level.
- Treat your loan's own rate as the bar for any extra dollar.
- Remember that money paid into the house is hard to get back in a bad month, which is what the fallback is for.
- Paying the extra annually instead of monthly costs about $8,200 more in interest in Tessa's case.

7. Partly. My question was whether to pay extra on the mortgage or invest the spare cash. The video gave me the benchmark, a guaranteed return equal to my loan rate, before taxes. It also showed what a 15-year commitment costs relative to keeping a lower required payment, which is directly relevant since I can only just afford the 15-year payment. But it deliberately stopped short of comparing that bar with investment returns, so the invest-versus-prepay question itself is left unanswered.
