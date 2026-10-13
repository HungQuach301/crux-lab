# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
Ba ý: (b) quyết định là chọn giữa **khoản vay 15 năm** và **khoản vay 30 năm nhưng trả hết trong 15 năm** (trả thêm gốc), kèm câu hỏi **trả thêm hay để tiền làm việc khác/đầu tư**; (c) trả lời bằng **lịch sử lãi vay thế chấp thật của Mỹ**, **mọi tuần / nhiều năm từ 1991**; (d) đáp án là **giá bằng đô la của sự linh hoạt** (khoản trả tối thiểu thấp hơn của khoản 30 năm) **và/hoặc** **mỗi đô la trả thêm "được" đúng bằng lãi khoản vay** — mức mà cách dùng tiền khác phải vượt. Đủ ba → 1; đủ hai → 0,5; ≤ một → 0.
**Cờ `overclaim`** (báo riêng, không tính ngưỡng): người đọc kể thành "video bảo chọn khoản vay nào / bảo trả thêm hay đầu tư" / "video dự báo lãi vay".
**Câu khuyên:** `advice: true` khi câu 4 "yes" vì tin video sẽ bảo chọn khoản vay nào, bảo trả thêm hay đầu tư, hoặc dự báo lãi, **hoặc** câu 5 nêu lời khuyên hành động (chọn 15 năm, chọn 30 năm, trả thêm, đầu tư…). Câu 5 kiểu "biết cái giá của sự linh hoạt / so lãi khoản vay với cách dùng tiền khác" là hiểu lời hứa, **không** tính. Người đọc **đúng** = điểm 1 và không câu khuyên.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "overclaim": true|false, "why": "<one line>"}, ...}

### R1
1. The video is for someone buying a home with roughly a $320,000 mortgage who can afford 15-year payments. It looks at whether to take a 15-year loan at 6.73% or a 30-year loan at 7.40% that you pay off in 15 years anyway, keeping the lower required payment as a safety net. It will replay every week of US mortgage rates since 1991 to put a dollar price on that safety net and to show what each extra dollar of principal earns.

2. I expect to know roughly what the 30-year's flexibility costs in dollars, and what return paying down principal gives, which is the bar any alternative use of the money must beat.

3. Mostly clear, but a few phrases are fuzzy. "put a dollar price on that fallback" is vague: I'm not sure if it means the extra interest from the higher rate or something else. "what each extra dollar of principal actually earns" is also a bit abstract, though I can guess it means a guaranteed return equal to the loan rate. "the bar any other use of that money has to clear" is slightly jargony.

4. No. The description says outright that it is "History, not a forecast," so it won't predict rates. It also says it "won't tell you which loan to take, or whether to invest." It sounds like it will supply numbers (the fallback's cost and the return on prepaying) for me to decide with.

5. Little direct advice, by design. A viewer would likely take away a way of thinking: treat the 30-year as a 15-year plus an option to pay less, weigh what that option costs against how much you value it, and compare any investment's expected return to the guaranteed return from prepaying. The decision itself stays with the viewer.

### R2
1. The video is for a home buyer borrowing about $320,000 who is choosing between a 15-year mortgage at 6.73% and a 30-year at 7.40% that they plan to pay off in 15 years anyway. It looks at what the 30-year's lower required payment, which works as a fallback, is worth in dollars. It answers this by replaying every week of US mortgage rates since 1991, and it also shows what each extra dollar of principal earns, which is the bar any other use of that money has to clear.

2. By the end I expect to know roughly what the 30-year's payment flexibility would have cost or been worth historically, and what return paying down principal gives.

3. Mostly nothing, but a few phrases are vague. "Put a dollar price on that fallback" doesn't say how the price is measured (extra interest paid, or the value of an option). "The bar any other use of that money has to clear" is a bit abstract until it's tied to the loan rate. "Replay every week" doesn't say what is being replayed, such as the rate gap between the two loans or a refinancing path.

4. No. The description says outright that it is "history, not a forecast" and that it "won't tell you which loan to take, or whether to invest." It will give figures to compare against, not a recommendation or a rate prediction.

5. Little direct advice. A viewer would take a way of thinking: treat the 30-year's lower required payment as an option with a price, and treat paying down principal as earning a return that other uses of the money must beat. They would still have to decide for themselves.

### R3
1. The video is for a homebuyer borrowing about $320,000 who can afford 15-year payments and is deciding between a 15-year loan at 6.73% and a 30-year loan at 7.40% that they pay off in 15 years. It takes every week of US mortgage rates since 1991 and replays the choice, measuring what the 30-year's lower required payment (the fallback) has cost and how high a return an investment would have needed to beat prepaying.

2. By the end I expect to know how much the 30-year's flexibility has historically cost compared with the 15-year, and how often investing could have cleared the loan-rate bar.

3. Nothing is badly confusing, but two phrases are a little vague: "the 30-year's lower fallback payment" (I infer it means the smaller required monthly payment you can drop to if money gets tight) and "how high the prepayment bar has been" (I infer it means the return an investment must beat to be better than paying extra).

4. No. The description says "History, not a forecast: no loan or investment pick," so it won't recommend a loan, tell me whether to invest, or predict future rates.

5. Little direct advice beyond the framing that paying extra on a mortgage earns a guaranteed return equal to the loan's rate, so any investment has to be compared against that rate. A viewer would take away a way to think about the decision, not an answer, and would still have to decide for themselves.

### R4
1. The video is for a home buyer borrowing about $320,000 who can afford 15-year payments and is choosing between two paths: a 15-year loan at 6.73%, or a 30-year at 7.40% that they pay off in 15 years by making extra payments. It uses every week of US mortgage rates since 1991 to look at what the 30-year's lower required payment (the fallback) has cost and how high the return needed from investing instead of prepaying has been. It treats this as a historical look, not a forecast or a recommendation.

2. By the end I expect to know how the cost of keeping the 30-year's flexibility, and the return an investment would need to beat prepaying, have varied across past mortgage-rate environments.

3. Nothing is badly confusing, but a few phrases are vague: "what the 30-year's lower fallback payment has cost" (it isn't clear what "cost" is measured in, such as the rate gap or total interest), and "how high the prepayment bar has been" (the "bar" is only implied to be the loan rate that investing must beat). "Each extra dollar of principal earns exactly the loan's rate" is clear once you think about it, but it is dense for a first read.

4. No. The description says outright "History, not a forecast: no loan or investment pick." It sets up a historical replay of past rates, so it won't predict future rates, name the better loan, or tell you whether to invest.

5. Little direct advice. A viewer might take away the framing that prepaying earns a guaranteed return equal to the loan's rate, so any investment has to beat that rate to be worth it. They might also learn how much the 30-year's flexibility has historically cost. The decision itself stays with the viewer.

### R5
1. This video is for someone taking out a roughly $320,000 mortgage who is deciding between a 15-year loan at 6.73% and a 30-year loan at 7.40% that they would pay off early in 15 years. It looks at whether paying extra toward the mortgage beats investing the money instead, since each extra dollar of principal earns the loan's rate. To answer, it replays every week of US mortgage rates since 1991 and shows what the 30-year's lower required payment would have cost and how high the bar for prepaying has been.

2. By the end I expect to know how the 30-year-with-prepayment option would have compared to the 15-year loan historically, and what return an investment would have needed to beat paying down the loan.

3. Nearly everything is followable, but a few phrases are vague: "what the 30-year's lower fallback payment has cost" (it's unclear what "fallback" means, though I'd guess it means the lower required payment you can drop back to if money gets tight) and "how high the prepayment bar has been" (I'd guess "bar" means the return an investment must beat, but it isn't defined).

4. No. The description says outright that it is "History, not a forecast: no loan or investment pick." It's a look back at past rates, so it won't recommend a loan, tell you whether to invest, or predict where rates are headed.

5. Little direct advice, by design. A viewer would mainly take away the framework: paying extra on a mortgage gives a guaranteed return equal to the loan's rate, so any investing alternative should be compared against that rate. They would also see how much the 30-year's flexibility has historically cost. The decision itself stays with them.

### R6
1. The video is for a homebuyer borrowing about $320,000 who can afford a 15-year payment and is choosing between two loans. One is a 15-year mortgage at 6.73%. The other is a 30-year at 7.40% that the buyer pays off in 15 years anyway, keeping the lower required payment as a safety net. It will replay every week of US mortgage rates since 1991 to put a dollar value on that safety net and to show what each extra dollar of principal earns.

2. I expect to know roughly what the flexibility of a 30-year loan costs compared with a 15-year loan, and what return paying down principal gives, which is the bar any alternative use of the money has to beat.

3. Mostly clear. Two phrases are a bit vague: "put a dollar price on that fallback" (I assume it means the extra interest paid for the 30-year's flexibility, but it isn't spelled out) and "what each extra dollar of principal actually earns" (I assume it means the effective return from the interest rate avoided, but the description doesn't say).

4. No. The description says outright: "History, not a forecast: it won't tell you which loan to take, or whether to invest." So it won't recommend a loan, tell me whether to invest, or predict future rates. It's a historical analysis meant to give me numbers to decide with.

5. A viewer would likely take away a way to think about the choice, not a verdict. Paying extra principal earns a known, risk-free return equal to the loan rate, so any investment has to beat that after accounting for risk. The lower required payment of a 30-year loan has a measurable cost, which can be weighed against how much I value that flexibility. The video wouldn't tell me which to choose.
