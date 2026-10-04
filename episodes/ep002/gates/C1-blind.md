# C1 — Kết quả kiểm mù (nguyên văn; chấm theo `gates/C1-intent.md`)

Ngày 2026-10-01. 30 agent mới (sonnet), mỗi agent một file hex. Khoá: `review-c1/key.json`. P-ep002 chấm "kể đúng".

## Tóm tắt

| Mẫu | Kể đúng (vai đích) | Phổ thông | Câu 4 "sẽ chỉ định/dự báo?" | Chỗ khó hiểu chính |
|---|---|---|---|---|
| **A** "người như tôi" | **5/5** | 1/1 | 0/6 "yes" | "head start" chưa định nghĩa (4/5); "every 10-year stretch" trừu tượng (3/5) |
| **B** nghịch lý | **5/5** | 1/1 | 0/6 "yes" | câu "one in four… one in thirty" dày, "cost more" so với gì (5/5). **3/5 đọc thành "variable usually/rarely…"** — sát gen cấm "variable is safe" |
| **W** đối chứng yếu | 5/5 | 1/1 | 0/6 "yes" | thuật ngữ 6/6 ("TB3MS", "753 overlapping windows", "amortizing"); không rõ T-bill thành lãi thả nổi thế nào 5/6 |

**Đọc kết quả:** qua cổng cả A và B (≥ 4/5). Đối chứng yếu cũng được kể lại 5/5 (đúng dự đoán M3: hiểu là điều kiện cần) nhưng **có chỗ khó hiểu ở 6/6** so với A (chỉ một từ "head start") → bộ đo **phân biệt được** ở tín hiệu chính (chỗ khó hiểu).

## So cặp tiêu đề (THAM KHẢO)

| Ứng viên vs X "Fixed vs Variable Student Loans Explained" | Thắng | Theo vai |
|---|---|---|
| **A1** "Need Private Grad Loans? Variable vs Fixed Through History" | **4/4** | T, S, P, C mỗi vai 1/1 |
| **D** "7.5% Variable or 9% Fixed? Grad Loans Through History" | **4/4** | T, S, P, C mỗi vai 1/1 |
| **B1** "Why a Variable Loan Can Rise Above Fixed and Still Cost Less" | **0/4** | thua ở cả 4 vai |

Lệch vị trí: chọn "1" 6/12, "2" 6/12 (không lệch). Lý do lặp lại: A1/D thắng vì "speaks directly to private grad loans", "concrete rates"; B1 thua vì "confusing", "niche, counterintuitive claim", "specific puzzle". Khớp packaging §6.1 (Tập 1: nghịch lý thua "người như tôi").

## Nguyên văn — kể lại

### Mẫu A

**c149f2f8** · vai T · chấm: ✓ · khó hiểu: "head start" chưa định nghĩa

> 1. This video is for grad students who now have to borrow privately because Grad PLUS is gone and the federal loan has a yearly cap. It looks at whether to take a variable-rate or fixed-rate private loan, using a $50,000, 10-year example (7.5% variable vs 9% fixed). It answers by replaying that loan through every 10-year stretch of US interest rates since 1954 and counting how often the cheaper start ended up costing more.
> 
> 2. I expect to know how often, historically, the variable loan's lower starting rate ended up costing more than the fixed one, how bad the worst case was, and how a bigger or smaller rate gap changes that.
> 
> 3. Nothing is really confusing. The one phrase I would want explained is "the answer changes when the head start is bigger, smaller, or zero", because "head start" is not defined and I had to guess it means the rate gap at the start.
> 
> 4. No. The description says it is "History, not a forecast", so it will show what happened in past periods rather than predict rates. It also reads as laying out how often and how badly each choice did, not telling me which loan to pick.

**b6286d50** · vai T · chấm: ✓ · khó hiểu: "head start", "every 10-year stretch"

> 1. The video is for grad students who need private loans on top of the federal limit, now that Grad PLUS is gone. It looks at whether to take a variable rate (7.5%, starting lower) or a fixed rate (9%) on a sample $50,000, 10-year loan. It answers by replaying that loan through every 10-year stretch of US rates since 1954, to see how often the variable loan cost more overall, how bad the worst case was, and what changes if the head start is bigger, smaller, or zero.
> 
> 2. By the end I expect to know how often, and by how much, the cheaper variable start has ended up costing more than fixed in past rate history.
> 
> 3. Nothing really. The only terms I'd want spelled out are "head start" (I read it as the gap between 7.5% and 9%) and "every 10-year stretch" (I read it as rolling 10-year windows).
> 
> 4. No. The description says "History, not a forecast," so it won't predict rates. It shows how the choice would have turned out in the past, which I can use to judge my own risk. It doesn't say it will tell me which to pick.

**2a7e8ea0** · vai T · chấm: ✓ · khó hiểu: không (nhẹ: "the lower start ended up costing more in total")

> 1. This video is for grad students who now need private loans because Grad PLUS is gone and the federal loan has a yearly cap. It looks at whether to take a variable rate that starts lower or a fixed rate that stays put. It takes one example loan ($50,000 over 10 years, 7.5% variable vs. 9% fixed) and replays it through every 10-year stretch of US interest rates since 1954 to see how often the variable loan cost more, how bad the worst case was, and what happens if the starting gap is bigger, smaller, or zero.
> 
> 2. By the end I expect to know how often, historically, the cheaper-starting variable loan turned out to cost more than the fixed one, and how much it hurt in the worst case.
> 
> 3. Nothing. (The only mildly vague phrase is "the lower start ended up costing more in total", but I can follow it.)
> 
> 4. No. The description says "History, not a forecast", so it will not predict rates, and it shows past outcomes under different head-start sizes rather than telling me which option to pick.

**2f697d46** · vai T · chấm: ✓ · khó hiểu: "every 10-year stretch", "head start"

> 1. This video is for grad students who now have to borrow privately because Grad PLUS is gone and the federal loan has a yearly cap. It looks at one decision: take a variable-rate private loan that starts lower (7.5%) or a fixed-rate one (9%), using an example $50,000 10-year loan. It answers by replaying that loan through every 10-year stretch of US interest rates since 1954 to see how often the variable loan ended up costing more and how bad the worst case was.
> 
> 2. By the end I expect to know how often, historically, the cheaper-looking variable rate turned out more expensive than the fixed rate, how much worse the worst case was, and how that changes with a bigger, smaller or zero head start.
> 
> 3. Nothing really. The only things I would need explained are "every 10-year stretch" (I assume rolling windows starting at different dates) and "head start" (the gap between the starting rates).
> 
> 4. No. The description says "History, not a forecast," so it will not predict rates. It also reads as showing how often and how badly each choice would have turned out, not telling me which to pick, so the decision stays with me.

**ce369f9c** · vai T · chấm: ✓ · khó hiểu: "replays it through every 10-year stretch" trừu tượng; "head start"

> 1. This video is for grad students who need private loans on top of the federal cap, now that Grad PLUS is gone. It looks at whether to take a variable rate that starts lower or a fixed rate. It uses one example loan ($50,000, 10 years, 7.5% variable vs 9% fixed) and runs it through every 10-year stretch of past US interest rates since 1954. That shows how often variable cost more, how bad the worst case was, and what changes if the head start is bigger, smaller or zero.
> 
> 2. I expect to know how often, historically, the lower variable rate ended up costing more than the fixed one, and how the answer shifts with the size of the rate gap.
> 
> 3. Nothing really. The phrase "replays it through every 10-year stretch of US interest rates" is a bit abstract until I see it, and "head start" is not defined, though I can guess it means the starting rate gap.
> 
> 4. No. The description says it is "History, not a forecast", so it will show what happened in past periods rather than say which to pick or predict future rates.

**5432d6a8** · vai G · chấm: ✓ · khó hiểu: không (nhẹ: "head start")

> 1. The video is for new grad students who can no longer get federal Grad PLUS loans (since July 1, 2026) and may need a private loan. It looks at whether to take a variable rate that starts lower or a fixed rate that never changes. It answers by taking one example loan ($50,000, 10 years, 7.5% variable vs 9% fixed) and replaying it through every 10-year stretch of US interest rates since 1954. That shows how often the variable loan ended up costing more, how bad the worst case was, and how the answer shifts if the head start is bigger, smaller, or zero.
> 
> 2. I expect to know how often, and by how much, the cheaper-starting variable loan would have lost to the fixed one in past rate history.
> 
> 3. Nothing. (Minor: "head start" is only implied to mean the gap between the two starting rates, but the context makes it clear enough.)
> 
> 4. No. The description says "History, not a forecast," so it will not predict where rates go. It also only reports how often the variable rate lost and how badly, using an illustrative loan. It does not say which one you should choose.

### Mẫu B

**79fc742d** · vai T · chấm: ✓ — nhưng đọc thành "usually cost less" · khó hiểu: "it cost more far less often…" ("it" là gì, so với gì)

> 1. This video is for grad students weighing a variable-rate private loan against a fixed-rate one. It takes a $50,000, 10-year variable loan that starts at 7.5% and replays it through every 10-year stretch of US rates since 1954, comparing it with a 9% fixed loan. It walks through one example loan, including the worst stretch (starting April 1977), to show how the variable rate can pass 9% often and still usually cost less overall.
> 
> 2. I expect to understand why a variable loan can go above the fixed rate at some point and still not cost more in total, and how that played out historically.
> 
> 3. Something was a little confusing: "it cost more far less often — in more than one in four stretches that began before 1981, and about one in thirty after." It is not clear what "it" is (the variable loan, I assume) or what "cost more" is measured against (I assume the 9% fixed loan). "Both facts" also takes a moment to work out.
> 
> 4. No. It says "History, not a forecast," so it will not predict rates. It also sounds like it will show how the two outcomes compare, with the best and worst past cases, and not tell me which loan to choose.

**83381176** · vai T · chấm: ✓ · khó hiểu: câu "one in four… one in thirty" dày; so với gì

> 1. This video is for someone like me who may need private grad loans and is weighing a variable rate that starts at 7.5% against a 9% fixed rate. It replays one example $50,000, 10-year variable loan through every 10-year stretch of US rates since 1954. It checks how often the variable rate went above 9% and how often the variable loan cost more in total, and it walks through the worst stretch (starting April 1977) to explain why those two numbers differ so much.
> 
> 2. By the end I expect to understand why a variable rate can pass the fixed rate fairly often yet still cost more overall only in a minority of historical cases.
> 
> 3. Nothing really, though "it cost more far less often — in more than one in four stretches that began before 1981, and about one in thirty after" is a bit dense on first read, and it doesn't say what the variable loan is being compared against until you infer it is the 9% fixed loan.
> 
> 4. No. The description says "History, not a forecast," so it won't predict rates. It also only shows how often the variable loan did worse in the past. It doesn't tell me which option to choose.

**41b2d239** · vai T · chấm: ✓ — nhưng đọc thành "rarely costs more" · khó hiểu: "cost more" đo so với gì

> 1. This video is for someone like me who may need private grad loans and is weighing a variable rate (starting at 7.5%) against a 9% fixed rate. It replays a $50,000, 10-year variable loan through every 10-year window of US rate history since 1954, including the worst one, which began in April 1977. It uses that to show how two facts can both be true: the variable rate often rises above 9% at some point, yet the variable loan rarely costs more in total.
> 
> 2. By the end I expect to understand why a variable rate can spike above the fixed rate and still usually cost less overall, based on history.
> 
> 3. Nothing was really confusing. The one part I'd want explained is "it cost more far less often", where I'd want to know what "cost more" is measured against (total interest paid versus the 9% fixed loan, I assume).
> 
> 4. No. The description says "History, not a forecast", so it won't predict rates. It also reads as an illustration of what happened in past periods, not a recommendation of which loan to choose.

**66c5657d** · vai T · chấm: ✓ · khó hiểu: "it cost more far less often…" khó theo

> 1. The video is for grad students who may need private loans and are weighing a variable-rate loan (starting at 7.5%) against a 9% fixed rate. It replays one example $50,000, 10-year variable loan through every 10-year stretch of US rates since 1954, including the worst one, which began in April 1977. It uses that history to show two facts that seem to clash but can both be true: the variable rate often goes above 9% at some point, yet the variable loan usually costs less in total.
> 
> 2. By the end I expect to know how often a variable loan's rate topped the fixed rate, and how often it actually cost more overall, in past rate history.
> 
> 3. Nothing is truly confusing, but "it cost more far less often — in more than one in four stretches that began before 1981, and about one in thirty after" took me a moment to follow. It is not clear at first what "it" and the comparison refer to. I assume "it" is the variable loan and the comparison is against the 9% fixed loan.
> 
> 4. No. The description says "History, not a forecast," so it will not predict where rates are headed. It also only shows how often each option did better in the past, using one illustrative loan, and does not tell me which one to choose.

**0e273988** · vai T · chấm: ✓ — nhưng đọc thành "usually not cost more" · khó hiểu: so sánh "three of four" với "one in four… one in thirty"

> 1. This video is for someone like me who may need private grad loans and is weighing a variable-rate loan against a fixed one. It takes a sample variable loan that starts at 7.5% and replays it through every 10-year stretch of US interest rates since 1954, comparing it to a 9% fixed rate. It walks through one example $50,000, 10-year loan, including the worst stretch (starting April 1977), to explain how the variable rate can often rise above 9% and yet usually not cost more overall.
> 
> 2. By the end I expect to understand why a variable rate can spike above a fixed rate fairly often while still costing less in total most of the time, and how that has played out historically.
> 
> 3. Nothing is really confusing. The only slightly hard part is the "three of every four stretches" versus "more than one in four ... before 1981, and about one in thirty after" comparison, which takes a moment to follow.
> 
> 4. No. The description says outright "History, not a forecast," so it will not predict where rates are headed. It also sounds like it will show how past outcomes played out rather than tell me which option to pick.

**ef582ed4** · vai G · chấm: ✓ · khó hiểu: "cost more" so với gì

> 1. The video is for someone weighing a variable-rate grad loan against a 9% fixed-rate loan. It asks whether the variable loan is the riskier or costlier choice. It answers by replaying one example $50,000, 10-year loan that starts at 7.5% through every 10-year stretch of US interest rates since 1954. It looks closely at both the typical stretches and the worst one, which began in April 1977.
> 
> 2. By the end I expect to understand how a variable loan's rate can rise above the fixed rate in most historical stretches and yet still cost more overall only occasionally.
> 
> 3. Nothing is hard to follow. The only slightly ambiguous wording is "cost more far less often — in more than one in four stretches that began before 1981, and about one in thirty after". It is not clear what "cost more" is compared against, though I assume the 9% fixed loan.
> 
> 4. No. The description says "History, not a forecast", so it will not predict interest rates. It also only shows how both facts can be true in past data, rather than recommending one loan, so the viewer is left to decide.

### Mẫu W

**dddd0249** · vai T · chấm: ✓ · khó hiểu: "753 overlapping 120-month windows", "TB3MS", "distribution…", "amortizing", T-bill → lãi thả nổi?

> 1. This video is for someone like me, a grad student who needs private loans on top of the federal cap, and it looks at whether a variable-rate loan (7.5%) or a fixed-rate loan (9%) costs less in total interest over 10 years. It answers by replaying history: it takes the 3-month T-bill rate from many past 10-year periods, works out what a variable loan would have cost in each one, and compares that with the fixed loan.
> 
> 2. By the end I expect to know how often, and by how much, the variable loan would have cost more than the fixed one in past 10-year periods.
> 
> 3. Confusing parts: "753 overlapping 120-month windows", "TB3MS", "start months 1954–2016", "distribution of total-interest differences" and "amortizing loan". Also, it doesn't say how the T-bill rate gets turned into the variable loan's rate (a margin or cap?). Otherwise it is readable.
> 
> 4. No. It reports historical results (the share of windows where variable costs more, the median difference, the maximum difference), which describe the past. It doesn't say it will recommend a loan or forecast future rates.

**cba84bf4** · vai T · chấm: ✓ · khó hiểu: "753 overlapping…", "TB3MS", "distribution…", "amortizing", margin/index?

> 1. This video looks at people who need a private grad loan and are choosing between a 7.5% variable rate and a 9% fixed rate over 10 years. It takes historical short-term Treasury bill rates, runs the loan through hundreds of overlapping 10-year periods from 1954 onward, and compares total interest paid under each option.
> 
> 2. By the end I expect to know how often, and by how much, the variable loan would have cost more than the fixed one in past history.
> 
> 3. Confusing: "753 overlapping 120-month windows", "3-month Treasury bill rate (TB3MS, start months 1954–2016)", "distribution of total-interest differences", "amortizing". It is also unclear how a T-bill rate gets turned into my loan's variable rate (what margin or index is assumed).
> 
> 4. No. It reports the share of windows where variable costs more, the median difference and the maximum difference. That is historical evidence for me to weigh, not a pick. It is a backtest of past data, so it does not forecast future rates.

**b3811a49** · vai T · chấm: ✓ · khó hiểu: "753 overlapping…", "TB3MS", margin/index?

> 1. This video is for someone taking out a big private grad-school loan who has to choose between a variable rate (7.5% to start) and a fixed rate (9%). It takes historical short-term Treasury bill rates and replays a 10-year repayment period starting in each month from 1954 to 2016, which gives 753 overlapping windows. In each window it works out how much more or less total interest the variable loan would have cost than the fixed one, then reports how often the variable loan lost, the median difference and the worst-case difference.
> 
> 2. By the end I expect to know how often, in past history, the cheaper-looking variable loan ended up costing more than the fixed one, and by how much in a typical case and in the worst case.
> 
> 3. Confusing or hard to follow: "753 overlapping 120-month windows" and "TB3MS" are jargon I would need explained. I also can't tell how the Treasury bill rate turns into my loan's variable rate (what margin or index is assumed). Otherwise nothing.
> 
> 4. No. It sounds like a historical backtest that shows what would have happened in past windows, with the share of times the variable loan cost more and the median and maximum gaps. It does not say it will recommend an option or forecast future rates. Past results are only a guide, and the choice is still mine.

**1c5131ac** · vai T · chấm: ✓ · khó hiểu: "753…", "TB3MS", "total-interest differences", T-bill → lãi của tôi?

> 1. This video is for someone like me who needs private student loans and has to choose between a variable rate (7.5% to start) and a fixed rate (9%) on a 10-year loan. It looks at whether the variable loan would end up costing more in total interest than the fixed one. It answers this by replaying history: it takes every 10-year stretch of 3-month Treasury bill rates from the 1950s to the 2010s and compares what each loan would have cost in each stretch.
> 
> 2. I expect to know in how many past 10-year periods the variable loan cost more than the fixed one, and by how much, both typically and in the worst case.
> 
> 3. Quotes: "753 overlapping 120-month windows", "TB3MS, start months 1954–2016", "total-interest differences". The jargon is hard to follow. I don't know what TB3MS is, what "overlapping windows" means, or why 120 months equals a 10-year loan. Also unclear: how a Treasury bill rate turns into my variable loan rate.
> 
> 4. No. It sounds like a historical look back that reports the share of past periods where variable cost more, the median difference and the maximum difference. It doesn't say it will tell me which to pick or forecast future rates. It gives past evidence and leaves the decision to me.

**ea901590** · vai T · chấm: ✓ · khó hiểu: "TB3MS", "overlapping 120-month windows", "amortizing", margin/cap?

> 1. This video is for someone weighing a private grad loan: a variable rate that starts lower (7.5%) or a fixed rate that is higher (9%). It takes historical 3-month Treasury bill rates and replays 753 overlapping 10-year repayment periods, starting every month from 1954 to 2016. For each period it works out how much total interest the variable loan would have cost compared with the fixed one.
> 
> 2. By the end I expect to know how often in history the variable loan would have cost more than the fixed one, and the typical (median) and worst-case (maximum) difference in total interest.
> 
> 3. Nothing is exactly unclear, but some phrases are jargon that I would want explained: "TB3MS", "overlapping 120-month windows", and "amortizing". I also can't tell how the variable rate is tied to the T-bill rate, for example what margin or cap is assumed, since the description only says 7.5% variable.
> 
> 4. No. It sounds like it only reports what happened in past periods (share of windows where variable costs more, median and maximum difference). It doesn't say which loan to choose, and a backtest of history is not a forecast of future interest rates.

**dd065832** · vai G · chấm: ✓ · khó hiểu: "TB3MS", "overlapping 120-month windows", "total-interest differences"

> 1. The video seems aimed at someone choosing between a lower-rate variable loan (7.5%) and a higher-rate fixed loan (9%), probably a borrower on a 10-year amortizing loan. It looks at whether the variable loan ends up costing more in total interest. To answer, it replays history: it takes 753 overlapping 10-year windows of 3-month Treasury bill rates (starting 1954-2016) and compares the total interest paid under each loan in every window.
> 
> 2. By the end I expect to know how often, historically, the variable loan cost more than the fixed one, along with the typical (median) and worst-case (maximum) difference in interest.
> 
> 3. Nothing is truly confusing, but these phrases are jargon-heavy and unexplained: "TB3MS", "overlapping 120-month windows", and "total-interest differences". It also does not say how the T-bill rate is turned into the variable loan's rate.
> 
> 4. No. It describes a backtest of past outcomes: the share of windows where variable cost more, the median and the maximum. That gives historical evidence, not a recommendation, and it makes no forecast of future interest rates.

## Nguyên văn — so cặp tiêu đề

**e9041907** · 1 = A1, 2 = X · vai S

> **Answer: 1**
> 
> Video 1 spells out that it is about private grad loans and compares variable vs fixed rates through history, which is exactly what I would want to know when weighing grad programs. Video 2 looks like a more generic explainer, so 1 feels more relevant and specific to me.

**898dc7dc** · 1 = A1, 2 = X · vai T

> 1
> 
> The title speaks directly to someone who needs private grad loans and promises a historical comparison of variable versus fixed rates, which is the decision I would actually be facing. Video 2 sounds like a more generic explainer.

**0a731f37** · 1 = B1, 2 = X · vai C

> 2
> 
> Since I have no student loans, I would pick the more general title, "Fixed vs Variable Student Loans Explained", because it reads like a plain overview of the basics. The other title is more of a specific puzzle that would matter less to me.

**8ca7472b** · 1 = B1, 2 = X · vai P

> 2
> 
> It is a plain, direct explainer of fixed vs variable student loans, which is exactly the choice I need to understand as a co-signer. Video 1 sounds like it assumes I already know the basics and argues a narrower point.

**037798dc** · 1 = D, 2 = X · vai C

> **Answer: 1**
> 
> The title names specific rates (7.5% variable vs 9% fixed) and a history angle, so it looks like a concrete comparison that would teach me how interest rates actually behave over time. Video 2 sounds like a generic explainer aimed at student borrowers, which matters less to me.

**f0a87869** · 1 = D, 2 = X · vai T

> 1
> 
> The title names concrete rates (7.5% variable vs 9% fixed) and frames the exact tradeoff I face with private grad loans, so it looks more useful than the generic "explained" title of video 2.

**0aca1411** · 1 = X, 2 = A1 · vai P

> 2
> 
> The title speaks directly to private grad loans and compares variable vs fixed rates through history, which is exactly the decision I face as a possible co-signer. Video 1 looks more generic, and both have the same length.

**4a65aa77** · 1 = X, 2 = A1 · vai C

> 2
> 
> I would click 2 because "Need Private Grad Loans? Variable vs Fixed Through History" speaks to a specific situation and promises a look at how rates have moved over time, which fits my curiosity about interest rates. Video 1 is a more generic student-loan explainer, and I have no student loans.

**c7d39d92** · 1 = X, 2 = B1 · vai S

> 1
> 
> The title "Fixed vs Variable Student Loans Explained" is a clear, straightforward overview of exactly what I would be trying to understand when comparing loan options for grad school. Video 2's title is more confusing and sounds like a niche, counterintuitive claim, so I would start with the basic explainer.

**42625fb7** · 1 = X, 2 = B1 · vai T

> 1
> 
> The thumbnails and lengths are identical, so I went by title. "Fixed vs Variable Student Loans Explained" is the clear, basic overview I would want first when comparing private loan options.

**818c13fb** · 1 = X, 2 = D · vai P

> 2
> 
> The title gives me concrete numbers (7.5% variable vs 9% fixed) and a real decision to weigh, plus the history angle for grad loans, which tells me exactly what I'd learn before co-signing. Video 1 is a generic "explained" title that feels like a basic overview.

**615feebe** · 1 = X, 2 = D · vai S

> 2
> 
> The title with concrete numbers (7.5% variable vs 9% fixed) tells me it will actually help me compare real grad loan options, and the history angle makes it feel more substantive than a generic explainer.

