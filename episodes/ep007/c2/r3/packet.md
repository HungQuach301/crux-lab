# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
**Đúng câu hỏi** (câu 1–2): video hỏi giữa **khoản vay 15 năm** và **khoản 30 năm trả hết trong 15 năm** (giữ khoản trả tối thiểu thấp hơn làm đường lui), qua người mua Tessa.
**Đúng đáp án** (câu 2): khoản 30 năm trả trong 15 năm = khoản 15 năm **cộng một đường lui có giá**: tuần này khoảng **$120/tháng, $21,622 qua 15 năm**; theo lịch sử từ 1991 giá này dao động (khoảng $6,100–$29,500, trung vị khoảng $16,600; tuần này đắt — ít hơn 1/5 số tuần cao bằng), theo **chênh lãi** 30 vs 15 năm; **và/hoặc** mỗi đô la trả thêm "được" đúng **lãi khoản vay (7.40%)** — mốc cách dùng tiền khác phải vượt. Cần ý "đường lui có giá bằng đô la" + ít nhất một trong: con số tuần này / dải lịch sử / mốc = lãi khoản vay. Đủ câu hỏi + đáp án → 1; một trong hai → 0,5; không → 0.
**Câu khuyên (rubric MỚI, G1 câu 2 — như Tập 6 C4; câu 6 + câu 8):**
- `advice_stated`: true khi câu trả lời cho thấy **CHÍNH VIDEO** (lời) nêu hay ngụ ý một hành động tài chính — chọn 15 năm / chọn 30 năm, trả thêm, đầu tư, trả theo tháng thay vì năm, chờ/khoá lãi, dự báo lãi — kể cả câu 5 "yes" vì tin video bảo vậy, hoặc câu 8 = "video" kèm câu trích là lời video. **TÍNH: ≥ 1 → TRƯỢT.**
- `advice_inferred`: true khi người đọc **TỰ SUY** hành động từ số (câu 8 = "own", "my own conclusion", "the video doesn't say"). Chỉ báo, REVIEWER đọc câu trích.
- `caution_only`: true khi chỉ có thận trọng chung (tự kiểm số của mình, hỏi bên cho vay/chuyên gia, so lãi khoản vay với cách dùng tiền khác, biết giá của đường lui). Không tính.
- `quote`: trích nguyên văn câu của người đọc làm căn cứ cho cờ (rỗng nếu không cờ).
Người đọc **đúng** = điểm 1 và `advice_stated` = false.
**Khối mất chú ý** (câu 3–4): xếp chỗ người đọc nêu vào một loại: `phương pháp` / `định nghĩa` / `số dày` / `nhân vật` / `khác` / `không`, và ghi cảnh ước (trích vài chữ).
**Câu hỏi mang tới** (câu 7): `answered_own`: true/false — người đọc nói video có trả lời câu hỏi họ mang tới không.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, "quote": "...", "attention": "<loại>: <cảnh ước>", "answered_own": true|false, "why": "<one line>"}, ...}

### R1
1. The video follows Tessa, an illustrative buyer with a $320,000 mortgage, who is choosing between a true 15-year loan and a 30-year loan she pays off in 15 years. It prices the difference using the October 8, 2026 survey rates (6.73% for the 15-year, 7.4% for the 30-year). The 30-year paid in 15 costs $120 a month more, or $21,622 over 15 years, and that buys her a lower required payment to fall back on in a bad month. It then compares that price with every week since 1991, shows that it tracks the gap between the 15- and 30-year rates, and ends by explaining that an extra principal dollar "earns" the loan's own rate (7.4% for Tessa, 2.65% for Leo).

2. The main question is "a 15-year, or a 30-year paid in 15?" The answer is that the 30-year paid in 15 is the 15-year plus a fallback, and for Tessa at the October 8, 2026 rates that fallback costs $120 a month ($21,622 total). Historically that price is high: the median is $16,631, the range is $6,097 to $29,502, and fewer than 1 in 5 weeks were as expensive. Her extra principal earns a before-tax 7.4%, a bar only about 1 week in 5 has matched. The video does not say which loan to pick.

3. Nothing was truly confusing, but a few passages were muddy:
- "That extra never lowers what the loan requires: the required payment stays where it was, and the loan simply ends sooner." The wording is a bit tangled, though I think I get it.
- The opening line, "Tessa's mortgage fallback costs $120 a month," uses "fallback" before it is defined.
- "Stack" and "bar" take a moment to map onto cost and return.

4. The yearly-payment tangent: "Tessa has another practical question: could she send the extra once a year instead of every month?" My attention dropped there because it veers from the main question into a side detail (the $8,792 and the extra $8,200 of interest), and the video itself says it isn't a verdict.

5. No to all three. The video says explicitly, "It won't say which loan to take, or whether to invest," and "it's history, not a forecast." It also says whether any investment clears the bar "isn't tested here."

6. A viewer would take away a framework rather than a directive:
- Treat "30-year paid like a 15-year" as a 15-year plus a priced fallback.
- Check how far apart the 15- and 30-year offers are, since that gap sets the price.
- Remember that extra principal earns your loan's own rate before taxes, and that money paid into the house is hard to get back.

7. Partly. I came wondering whether to pay extra or invest. The video gave me the benchmark, which is that extra principal earns the loan's rate (7.4% for Tessa) with no risk. It also told me the cost of keeping flexibility. It deliberately did not compare that with investing, which was the half I most wanted.

8. Video. The advice comes from this sentence: "The bar is that loan's own rate, printed on the paperwork, and the stack depends on how far apart the 15-year and 30-year offers sit that week."

### R2
1. The video follows Tessa, an illustrative US buyer with a $320,000 mortgage who is choosing between a true 15-year loan and a 30-year loan paid off in 15 years. It prices the 30-year's lower required payment as a "fallback" and compares it with every weekly mortgage survey since 1991. It then shows how the cost varies with the gap between 30-year and 15-year rates, contrasts Tessa with Leo (January 2021), and explains that an extra principal dollar earns the loan's own rate. It closes by repeating that this is US-only history, not a forecast or a recommendation.

2. The 30-year paid in 15 years is the 15-year loan plus a fallback, and at the October 8, 2026 rates that fallback costs Tessa $120 a month. That is $2,948 against $2,828, or $21,622 over 15 years. By history this is expensive: the median week since 1991 was $16,631, the range ran from $6,097 to $29,502, and fewer than 1 in 5 weeks cost this much. The cost tracks the gap between the 30-year and 15-year rates, not the level of rates. Each extra dollar of principal earns the loan's rate, 7.4% before tax for Tessa, and that is the bar any investment would have to beat.

3. Nothing confused me badly, but one passage was abstract: "That extra never lowers what the loan requires: the required payment stays where it was, and the loan simply ends sooner." It took a second pass to see that the point is the fallback stays available. Also, "the difference between those last two totals is exactly the stack" is hard to follow by ear because three interest totals come in quick succession.

4. The yearly-extra passage: "Tessa has another practical question: could she send the extra once a year instead of every month? At the October 8 rates, that's $8,792 once a year, the same total as the monthly extra." Attention dropped because it is a side branch with more figures ($8,792, four months, $8,200), and it doesn't change the main answer.

5. No. The video says outright that it "won't say which loan to take, or whether to invest," and that it is "history, not a forecast." It only prices the fallback and states the bar for comparison.

6. The takeaway is a way to frame the choice, not an instruction. Treat the 30-year paid in 15 as the 15-year plus a fallback and ask whether that fallback is worth its monthly price. Compare your own stack (the cost of the rate gap) with your own bar (your loan's rate), and weigh that against how hard it would be to get money back out of the house in a bad month.

7. Partly. I came asking whether to pay extra on the mortgage or invest the spare cash. The video answered the first half: what extra payments earn (the loan's rate, 7.4% for Tessa) and what the fallback costs. It did not answer the investing half, because it explicitly leaves out whether any investment clears the bar after risk and taxes.

8. Video. The framing comes from this sentence: "Any fixed-rate borrower can set their own pair beside hers." It is reinforced by "Clearing the bar isn't the whole story: a dollar paid into the house is hard to get back in a bad month, which is exactly what the fallback is for."

### R3
1. The video follows Tessa, an illustrative buyer borrowing $320,000 in an expensive city, who is choosing between a 15-year mortgage and a 30-year mortgage paid off in 15 years. It prices the difference using the October 8, 2026 survey rates (6.73% for the 15-year, 7.4% for the 30-year). It then compares that price with every week of US survey rates since 1991, adds Leo (who borrowed in January 2021) as a contrast, and ends with what an extra principal dollar earns. It repeatedly says it is US-only history, not a forecast, and not a recommendation.

2. The 30-year paid in 15 years is the 15-year loan plus a fallback, meaning the lower required payment kept for a bad month, and that fallback has a price. For Tessa it is $120 a month ($2,948 vs $2,828), or $21,622 over 15 years. By history that is expensive: the median week was $16,631, the range was $6,097 to $29,502, and fewer than 1 in 5 weeks cost more. The price is driven by how far the 30-year rate sits above the 15-year rate, not by the level of rates. Separately, each extra principal dollar "earns" the loan's own rate, 7.4% pre-tax for Tessa, and about 1 week in 5 since 1991 had a rate that high.

3. "That extra never lowers what the loan requires: the required payment stays where it was, and the loan simply ends sooner. Each extra dollar does cut the next month's interest; the payment just stays fixed, so more of it goes to principal. That's why the fallback is still there years later, if a month goes wrong." It's a dense passage heard once, and the "stack" and "bar" metaphors make the logic harder to follow by ear. A smaller point is that the opening line, "Tessa's mortgage fallback costs $120 a month," uses "fallback" before it is defined.

4. "Tessa has another practical question: could she send the extra once a year instead of every month?" My attention dropped here because it is a tangent. The yearly-lump-sum detail ($8,792, four months later, about $8,200 more interest) doesn't feed into the main question or the conclusion.

5. No. The video explicitly says it "won't say which loan to take, or whether to invest," and that it is "history, not a forecast." It says again that whether any investment clears the bar "isn't tested here."

6. The video gives no direct advice. A viewer could take away a method:
- Get both the 15-year and 30-year quotes.
- Price the fallback as the cost of the 30-year paid on a 15-year schedule minus the real 15-year loan.
- Treat your loan's own rate as the pre-tax bar for any use of extra cash.
- Remember that money paid into the house is hard to get back in a bad month.

7. Only partly. The question I came with was whether to pay extra on the mortgage or invest the spare cash. The video does give the guaranteed pre-tax return of extra payments, which is the loan's rate (7.4% for Tessa), and notes the liquidity cost. But it doesn't compare that with investing, and it spends most of its time on 15-year vs 30-year-paid-in-15, which is a different question.

8. Video. The method is the video's own suggestion: "Any fixed-rate borrower can set their own pair beside hers. The bar is that loan's own rate, printed on the paperwork, and the stack depends on how far apart the 15-year and 30-year offers sit that week." The caution about liquidity comes from "a dollar paid into the house is hard to get back in a bad month, which is exactly what the fallback is for."

### R4
1. The video follows Tessa, an illustrative borrower of $320,000, who is deciding between a 15-year mortgage and a 30-year mortgage paid off in 15 years. It prices the 30-year's lower required payment (the "fallback") at $120 a month, or $21,622 over 15 years, then replays 1,833 weeks of US mortgage rates to show whether that price is normal. It finds the price depends on the gap between 30-year and 15-year rates, compares Tessa to Leo (who borrowed in January 2021), and ends by explaining that each extra principal dollar earns the loan's own rate, which is 7.4 percent for Tessa.

2. The answer is that the 30-year paid in 15 years is the 15-year loan plus a fallback, and the fallback has a price. For Tessa, in the week of October 8, 2026, it costs $120 a month ($2,948 versus $2,828), or $21,622 over 15 years. That is expensive by history: the typical week since 1991 was $16,631, the range was $6,097 to $29,502, and fewer than 1 in 5 weeks cost this much. The driver is the rate gap (0.67 point for Tessa), not the level of rates.

3. "That extra never lowers what the loan requires: the required payment stays where it was, and the loan simply ends sooner. Each extra dollar does cut the next month's interest; the payment just stays fixed, so more of it goes to principal." The passage was hard to follow because it first says the extra has no effect on the loan and then says each dollar does cut interest, so I had to work out that these refer to different things (the required payment versus the interest charged). Also, "$733 a month on top of the required payment" sits oddly beside the earlier "$120 a month more than the 15-year loan," and the connection between those two numbers was not explained clearly.

4. "Back to Tessa's own loan, and a shortcut many people reach for: pay the 30-year exactly what the 15-year would cost, and assume it ends on the same day." My attention dropped there because the video had just reached its main conclusion about decades and gaps, and this section started a new set of numbers (195 months, 15 months late, $733, $8,792 once a year, $8,200 more in interest) that felt like a side track before the final question.

5. No. The video says outright that it won't say which loan to take or whether to invest, and that it is history, not a forecast. It only prices the fallback in past weeks and says the bar for any alternative use of a dollar is the loan's own rate, without testing whether investments clear it. It also says "nothing here says where [the gap] goes."

6. Little direct advice. A viewer might take away that if they plan to pay a 30-year like a 15-year, they should recognize that the keep-the-fallback option has a price that depends on the gap between the two rates in the week they borrow, and that they can compare that price to what a lower required payment is worth to them in a bad month. They might also remember that extra principal earns the loan's own rate, before taxes, and use that as the bar for other uses of the money.

7. I came without a specific question beyond the premise, which was whether a 15-year loan or a 30-year paid in 15 is better. The video answered a narrower version of it: it didn't say which is better, but it priced the difference clearly, in the section where Tessa's $120 a month and $21,622 stack are shown and then compared with the history of weekly gaps.

8. Own. The video explicitly declines to give advice, and my conclusion in 6 is my inference from its framing. The closest sentence is: "Clearing the bar isn't the whole story: a dollar paid into the house is hard to get back in a bad month, which is exactly what the fallback is for."

### R5
1. The video follows Tessa, an illustrative buyer borrowing $320,000 who is choosing between a true 15-year mortgage and a 30-year mortgage paid off in 15 years. It prices the 30-year's lower required payment (the "fallback") by comparing the two loans at the real survey rates of every week since 1991. It shows that Tessa's fallback costs $120 a month ($21,622 over 15 years), which is high by historical standards because the gap between 30-year and 15-year rates is wide. It also explains that extra principal "earns" the loan's own rate (7.4% for Tessa, before taxes), and contrasts her with Leo, who took a loan in January 2021 at a low rate.

2. The 30-year paid in 15 years is the 15-year loan plus a fallback, and the fallback has a price. At the October 8, 2026 rates (15-year 6.73%, 30-year 7.4%), Tessa pays $2,948 a month versus $2,828, so $120 more a month. That adds up to $21,622 over 15 years, which is higher than the typical week (median $16,631) and higher than about 4 in 5 weeks since 1991. Each extra dollar of principal earns 7.4% before taxes, which is the bar any other use of the money must beat.

3. "The 15-year loan charges $189,069, and the difference between those last two totals is exactly the stack." It is confusing because "those last two totals" has to be worked out. The two totals before it are $477,622 and $210,691, but the sentence just gave a third figure, $189,069. The stack is $210,691 minus $189,069 = $21,622, so the reference is to the last two (15-year paid in 15 versus the true 15-year), but it is easy to misread.

   A second spot: "Tessa's gap on October 8 sits a little above that average." It follows 0.57 and 0.67, but the viewer is never told the gap explicitly, so it requires inference.

4. "Back to Tessa's own loan, and a shortcut many people reach for: pay the 30-year exactly what the 15-year would cost, and assume it ends on the same day." Attention dropped here because the video switches from the price of the fallback to a new tangent about payoff timing, with a string of numbers (195 months, 15 months late, $733 extra) before the point about the required payment staying fixed becomes clear. The annual-payment segment right after it also felt like a detour.

5. Yes, it says no to all three. It says explicitly: "It won't say which loan to take, or whether to invest," and "it's history, not a forecast." It also says "Whether any investment clears it, once risk and taxes count, isn't tested here." The video limits itself to pricing the fallback and describing the return on extra principal, and it does not recommend a loan, say whether to invest, or predict rates.

6. A viewer would take away a framework rather than a directive. Treat "30-year paid like a 15-year" as a 15-year plus a purchased fallback, check the gap between current 15- and 30-year rates to see what that fallback costs, and compare the loan's own rate (the bar) against what they could earn elsewhere after risk and taxes. They should also remember that money sent to the mortgage is hard to get back in a bad month, which is what the fallback is for.

7. Partly. My question was whether to pay extra on the mortgage or invest the spare cash. The video answered the first half of the underlying issue: extra principal earns the loan's rate (7.4% before taxes) and the fallback has a price, so it gives the benchmark. It does not answer whether investing would beat that, since it explicitly leaves that untested. The loan-choice parts (stack, history, Leo comparison) were useful context but not what I came for.

8. Video. The framework in 6 comes from these sentences: "That rate is the bar any other use of that dollar gets measured against, before taxes," and "Clearing the bar isn't the whole story: a dollar paid into the house is hard to get back in a bad month, which is exactly what the fallback is for."

### R6
1. The video follows Tessa, an illustrative US buyer with a $320,000 mortgage, who is deciding between a 15-year loan and a 30-year loan paid off in 15 years. It reframes the 30-year paid in 15 as "the 15-year plus a fallback" (the lower required payment kept for a bad month). It prices that fallback using every weekly US mortgage survey since 1991 (1,833 weeks). It compares Tessa's week to history and to Leo, who borrowed in January 2021, and then explains what an extra principal dollar earns (the loan's own rate, before taxes).

2. The answer is that the 30-year paid in 15 is not the same as the 15-year; it costs more for the fallback. At the October 8, 2026 rates (15-year 6.73%, 30-year 7.4%), Tessa pays $2,948 a month instead of $2,828, which is $120 more a month and $21,622 over 15 years. Historically the fallback cost ranged from $6,097 to $29,502, with a median of $16,631. Tessa's is more expensive than all but fewer than 1 in 5 weeks. Each extra dollar of principal earns 7.4% before taxes, the loan's rate. The video doesn't say which choice is better.

3. "Paid on its own 30-year schedule, her loan would charge $477,622 in interest. Paid in 15 years, it charges $210,691." This was confusing because the two figures are presented without noting that $477,622 is a different scenario than the stack, and the jump to "the difference between those last two totals is exactly the stack" refers to $210,691 and $189,069, which takes a moment to track. Also, "That extra never lowers what the loan requires" is a bit unclear at first, and the $733 versus $120 extra figures (the shortcut paying $2,828 versus the $2,948 needed) are easy to mix up.

4. "Any fixed-rate borrower can set their own pair beside hers. The bar is that loan's own rate, printed on the paperwork, and the stack depends on how far apart the 15-year and 30-year offers sit that week." Attention dropped here because it's an abstract generalization after several concrete examples, and the stack/bar metaphor is stretched to a viewer's own situation without numbers.

5. No on all three, and the video says so itself. It states "It won't say which loan to take, or whether to invest," that it's "history, not a forecast," and that the gap "has moved before, and nothing here says where it goes." It also says whether any investment clears the bar "isn't tested here."

6. A viewer might take away that a 30-year paid like a 15-year costs extra for the flexibility (here $120 a month for Tessa), so they should compare that price against how much they value the fallback. They'd also learn that paying extra principal earns the loan's own rate, before taxes, which is the bar any alternative use of the money has to beat. They'd also see that the gap between 15- and 30-year rates drives the price, not the rate level.

7. Partly. The question I came with was whether to pay extra or invest the spare cash. The video gave me the bar (7.4%, before taxes) for the pay-extra side, which is the useful part, but it explicitly doesn't test investing, so it doesn't settle the question. It focused more on 15-year versus 30-year paid in 15.

8. Video. The advice in 6 follows from: "So the 30-year paid in 15 isn't the same loan as the 15-year: it's the 15-year plus a fallback, and the fallback has a price." and "That rate is the bar any other use of that dollar gets measured against, before taxes." The suggestion to weigh the price against the fallback's value is partly my own synthesis, though the video notes "a dollar paid into the house is hard to get back in a bad month, which is exactly what the fallback is for."
