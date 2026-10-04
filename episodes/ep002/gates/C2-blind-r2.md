# C2 vòng 2 — Kết quả kiểm mù (script v3; nguyên văn; ý đồ `gates/C2-intent-r2.md`)

8 agent mới (sonnet). Khoá `review-c2/key.json` (vòng 1: `review-c2/v2-blind/key.json`).

| Chỉ số | Vòng 1 (v2) | **Vòng 2 (v3)** | Mục tiêu |
|---|---|---|---|
| "Đúng" vai đích | 5/5 | **5/5** (+ phổ thông 1/1) | ≥ 4/5 |
| Đọc thành chỉ định/dự báo | 0/6 | **0/6** | 0 |
| Đối chứng yếu M1b hiểu đáp án | 3/3 | 2/2 | (không phân biệt được ở "hiểu") |
| Đoạn phương pháp = chỗ mất chú ý | 5/6 | **6/6** | ≤ 2/6 — **không đạt** |
| Dãy số khoảng chênh (1,5/2/3 điểm) nặng | 5/6 | **5/6** | ≤ 2/6 — **không đạt** |
| Từ chỉ hình lọt vào lời | 5/6 | **0/6** | ≤ 2/6 — đạt |
| Biên/chỉ số thay thế khó hiểu | 5/6 | 3/6 | ≤ 2/6 — gần |
| **Mới:** "1 in 30" vs "3.5%" (cùng số, hai dạng ở hai đoạn) gây nghi ngờ | — | **4/6** | — |
| Nghịch lý "3 trong 4 / 1 trong 7" khó tới khi giải thích | 5/6 | 6/6 | có chủ đích |

**Đọc kết quả:** hết 2 vòng sửa–kiểm (§5.6). Hiểu đạt; hai chỗ mất chú ý (phương pháp, dãy số) **không giảm** qua sửa câu chữ → là vấn đề **vị trí/cấu trúc**, đưa phương án lên chủ dự án ở gói C2, không lặp vòng 3.

## Nguyên văn

**4e98f561** · mẫu cand · vai G

> 1. Summary: The video follows Leah, an illustrative new grad student who can no longer get Grad PLUS loans from July 2026 and has two private offers for $50,000 over 10 years: 9% fixed, or a variable rate starting at 7.5%. It asks how much lower a variable rate must start (the "head start") for the risk to be worth it. It replays the loan through every 10-year stretch of US rates since 1954, using the 3-month Treasury bill rate as a stand-in. It measures how often the variable loan cost more in total interest, and by how much at worst. Then it moves the head start from 3 points under to 1 point over to show where history changes, and stresses that this is history, not a forecast.
> 
> 2. Answer: It depends on which kind of history you get. From 1981 on, a 2-point head start was enough every time (no stretch cost more). From 1954 to 1980, even 3 points was not enough: 10.5% of those starts still cost more, the worst by $6,033. Leah's 1.5-point head start falls short of the 2-point mark. At 1.5 points, about 1 in 7 stretches overall cost more (28.4% of 1954-1980 starts, 3.5% of later ones), and the worst (April 1977) cost $11,219 more, 43% on top of the fixed loan's $26,005 interest. The reason it is not a certain loss: rates rose above 9% in about 3 in 4 stretches, but the early savings build a "cushion" that rates must erode first.
> 
> 3. Confusing passages:
> - "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." This is confusing at first because it sounds contradictory. The cushion explanation that follows resolves it.
> - "That's more than 1 in 4 for starts from 1954 to 1980 and about 1 in 30 from 1981 on" versus later "28.4%" and "3.5%". The numbers are consistent (3.5% is about 1 in 29) but the switch between fractions and percentages made me double-check.
> - "Same lender, same amount, two kinds of rate." and the terms "head start" and "point" took a moment, though they are defined.
> 
> 4. Attention dropped most at the paragraph on the replay mechanics: "A real variable rate is the lender's own index plus a fixed margin, and the replay needs a much longer record than that index has... Neighbouring stretches share most of their years, so they are not independent tries, and the data is US only." It is a dense methodology and caveat block that comes right after the interesting result. The run of head-start percentages ("At 2 points... At 3 points...") is also number-heavy when only spoken.
> 
> 5. No. The video does not say which loan to take and does not predict rates. It says repeatedly "This is history, not a forecast," "Which kind of history comes next is something no replay can show," and "The line doesn't say which offer is better." It only shows what each head start meant in each kind of history, and notes real offers have caps, fees, grace periods and the borrower's budget.

**d55ea836** · mẫu cand · vai T

> 1. The video follows Leah, an illustrative new grad student who can no longer get Grad PLUS loans (after July 1, 2026) and has two private offers on $50,000 over 10 years: 9% fixed, or a variable rate starting at 7.5%. It asks how much lower a variable rate must start to be "worth" the risk. It replays her loan through every 10-year stretch of US rates since 1954, using 3-month Treasury bills as a stand-in index. It first shows a surprising result, then a worst case (April 1977), then moves the starting gap ("head start") to see where history changes.
> 
> 2. Worth it is defined as how often the variable loan cost more in total interest than the fixed loan, and by how much at worst. At Leah's 1.5-point head start, the variable loan cost more in about 1 in 7 stretches. That was 28.4% of 1954-1980 starts and 3.5% of 1981-on starts, and the worst case cost $11,219 more. With a 2-point head start, none of the 1981-on starts cost more, but 20.4% of 1954-1980 starts still did (worst $9,472). With 3 points, none of the 1981-on starts cost more, but 10.5% of 1954-1980 starts did (worst $6,033). So 2 points was enough every time from 1981 on, but even 3 points was not enough in 1954-1980. Which era comes next can't be known.
> 
> 3. Confusing: "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." It reads as a contradiction until the cushion explanation later. Also: "Which kind of history comes next is something no replay can show." and "where stretches from both halves of history still cost more". Both are abstract. A smaller point: "more than 1 in 4 for starts from 1954 to 1980 and about 1 in 30 from 1981 on" are given before the later 28.4% and 3.5% figures, and they sit awkwardly beside the "1 in 7" overall figure.
> 
> 4. Attention dropped in the method paragraph: "A real variable rate is the lender's own index plus a fixed margin, and the replay needs a much longer record than that index has... Neighbouring stretches share most of their years, so they are not independent tries, and the data is US only." It is dense technical caveating with no payoff for a borrower. The run of percentages and dollar figures at the head-start comparison ("At Leah's 1.5 points, 28.4%... At 2 points... At 3 points...") also got heavy to follow in audio.
> 
> 5. No. It states "This is history, not a forecast" and "The line doesn't say which offer is better." It gives no recommendation and no rate prediction. It only shows what each head start meant in past eras, and it says real offers have caps, fees, grace periods and your own budget, which it leaves out.

**4141e0b3** · mẫu cand · vai T

> 1. Summary
> The video follows Leah, an illustrative new grad student who can no longer get Grad PLUS loans (after July 1, 2026) and has two private offers for $50,000 over 10 years: 9% fixed, or a variable rate starting at 7.5%. It asks how much lower a variable rate must start before the risk is "worth it." It replays her loan through every 10-year stretch of US rates since 1954, using 3-month Treasury bill rates as a stand-in, and defines "worth it" as how often, and by how much, the variable loan cost more in total interest than the fixed one. Then it varies the starting gap (the "head start") from 3 points under to 1 point over, and ends with a line any real offer can be compared against. It stresses that this is history, not a forecast.
> 
> 2. The video's answer
> It gives two answers, depending on which kind of history you get. From 1981 on, a 2-point head start was enough every time: no stretch cost more. From 1954 to 1980, even a 3-point head start was not enough: 10.5% of those starts still cost more, the worst by $6,033. At Leah's 1.5 points, 28.4% of the 1954-1980 starts and 3.5% of the later ones cost more, and the worst (April 1977) cost $11,219 more, about 43% more interest than the fixed loan's $26,005. Which kind of history comes next "no replay can show." Leah's offer is short of the 2-point mark.
> 
> 3. Confusing passages
> - "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." This sounds contradictory at first. The video explains it afterward with the "cushion" idea, but I had to wait for that.
> - "That's more than 1 in 4 for starts from 1954 to 1980 and about 1 in 30 from 1981 on." Later the video gives 28.4% and 3.5% for the same split. 3.5% is about 1 in 29, so they match, but the shifting fractions and percentages made me check.
> - "A real variable rate is the lender's own index plus a fixed margin, and the replay needs a much longer record than that index has." I could not tell what index my own offer would use or how closely it would track Treasury bills.
> - "Neighbouring stretches share most of their years, so they are not independent tries." I understood this only vaguely: it seems to mean the percentages are less reliable than they look.
> 
> 4. Where attention dropped most
> "Here's how the replay works. A real variable rate is the lender's own index plus a fixed margin... The first replay starts in January 1954 and runs for 10 years, and the next starts one month later, and so on, up to September 2016." This is methodology with no stakes for me, and it comes right after the hook. The paragraph with the head-start percentages ("At 2 points, none... At 3 points...") was also a dense run of numbers that was hard to hold in my head without a table.
> 
> 5. Does it tell me which loan to take or predict rates?
> No. It says "This is history, not a forecast" twice and "The line doesn't say which offer is better." It says "which kind of history comes next is something no replay can show." It gives a way to compare any offer's head start against past outcomes. It also lists what it leaves out (the real index, rate cap, grace period, fees, my own budget), so the choice stays with me.

**59d00ede** · mẫu cand · vai T

> 1. The video is about Leah, an illustrative new grad student who can no longer use Grad PLUS (after July 1, 2026) and has two private offers on $50,000 over 10 years: 9% fixed, or a variable rate starting at 7.5%. The problem is how much lower a variable rate must start to be worth the risk. It replays her loan through every 10-year stretch of US rates since 1954 (using 3-month T-bills as a stand-in), counts how often the variable loan cost more in total interest and by how much at worst, then shifts the starting gap (the "head start") from 3 points under to 1 point over the fixed rate. It ends with a line any real offer can be compared against, stressing it is history and not a forecast.
> 
> 2. With "worth it" defined as how often the variable loan cost more in interest than the 9% fixed loan, and how much more at worst: from 1981 on, a 2-point head start was enough every time (none cost more), while from 1954 to 1980 even 3 points was not enough. At 3 points, 10.5% of the 1954-1980 starts still cost more, the worst by $6,033. Leah's 1.5 points falls short: 28.4% of 1954-1980 starts and 3.5% of later ones cost more, worst case $11,219 more (April 1977 start, 43% extra interest, payment up to $863.36). Which kind of history comes next can't be shown.
> 
> 3. Confusing passages:
> - "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." It sounds contradictory at first; the explanation (the "cushion") comes a paragraph later.
> - "A point here means one percentage point of interest." Fine, but it sits next to "head start" and "points" and the 1954-1980 vs 1981-on splits, so many numbers pile up.
> - "That's more than 1 in 4 for starts from 1954 to 1980 and about 1 in 30 from 1981 on" versus later "28.4% ... and 3.5%". The figures are consistent but are given in different forms, so I had to convert between them.
> - "Neighbouring stretches share most of their years, so they are not independent tries." The statistical caveat is unclear for a lay listener.
> 
> 4. My attention dropped most in the methodology paragraph: "A real variable rate is the lender's own index plus a fixed margin, and the replay needs a much longer record than that index has. So it uses a stand-in with a long US record, the rate on 3-month Treasury bills, and sets the margin so that Leah's rate starts at 7.5%..." and "...up to September 2016." It is technical and date-heavy, with little for me to act on. The run of percentages in "At Leah's 1.5 points, 28.4%... At 2 points... At 3 points..." is also dense.
> 
> 5. No. The video does not tell me which loan to take: it says "The line doesn't say which offer is better; it shows what each head start meant in each kind of history." It does not predict rates either: it repeats "This is history, not a forecast" and "Which kind of history comes next is something no replay can show." It also notes real offers have caps, fees, grace periods and the borrower's budget that the replay leaves out.

**0826b4c6** · mẫu cand · vai T

> 1. Summary
> The video follows Leah, an illustrative new grad student who, after the end of federal Grad PLUS loans for new borrowers on July 1, 2026, has two private offers for $50,000 over 10 years: 9% fixed, or a variable rate starting at 7.5%. It asks how much lower a variable rate must start before the risk is "worth it," defined as how often the variable loan cost more total interest than the fixed loan and by how much at worst. It replays the loan through every 10-year stretch of US rates since 1954, using 3-month Treasury bills as a stand-in. It shows the worst case (April 1977) and then varies the starting gap (the "head start") from 3 points under to 1 point over. It ends with a line to compare real offers against, stressing it is history and not a forecast.
> 
> 2. The video's answer
> It gives two answers depending on which history repeats. From 1981 on, a 2-point head start was enough every time: no stretch cost more. For starts from 1954 to 1980, even a 3-point head start was not enough: 10.5% of those stretches cost more, and the worst cost $6,033 more. Leah's 1.5-point head start falls short of the 2-point mark. At 1.5 points, 28.4% of the 1954-1980 starts and 3.5% of the later ones cost more, and the worst case cost $11,219 more (43% more interest than the fixed loan's $26,005). Which kind of history comes next can't be known.
> 
> 3. Confusing passages
> - "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." It is a deliberately paradoxical claim and I had to wait for the cushion explanation. The "1 in 7" overall figure is also never reconciled with the later 28.4% and 3.5% figures. I had to infer it is a blend of the two eras.
> - "about 1 in 30 from 1981 on" (line 9) versus "3.5% of the later ones" at Leah's 1.5 points (line 19). These look inconsistent (1 in 30 is about 3.3%), and the video doesn't say they are rounding differences.
> - "Real offers differ: a head start can be... negative." It is not clear how I would measure the head start on a real variable offer, because the video says a real rate is the lender's index plus a margin, and it doesn't say how to compare that with a fixed rate.
> - "sets the margin so that Leah's rate starts at 7.5%" is jargon-heavy for a non-finance viewer.
> 
> 4. Attention drop
> Lines 13 and 15, the methodology paragraph: "A real variable rate is the lender's own index plus a fixed margin... Neighbouring stretches share most of their years, so they are not independent tries, and the data is US only." It is dense with caveats and mechanics, and a stack of dates and figures follows ("peaked at 16.3% in May 1981... best stretch began in August 1981... $15,295 less"). These didn't affect my decision.
> 
> 5. Does it tell me which loan to take or predict rates?
> No. It says outright "This is history, not a forecast" and "The line doesn't say which offer is better; it shows what each head start meant in each kind of history." It also says "Which kind of history comes next is something no replay can show." It lists things it leaves out (the real index, rate cap, grace period, fees, my budget) that I would have to weigh myself.

**1c9c1fa6** · mẫu cand · vai T

> 1. Summary
> The video follows Leah, an illustrative new grad student who can no longer use Grad PLUS (ended July 2026 for new borrowers). She has two private offers on $50,000 over 10 years: 9% fixed, or a variable rate starting at 7.5%. The question is how much lower a variable rate must start (the "head start") to be worth the risk. The video replays the loan through every 10-year stretch of US rates since 1954, using 3-month Treasury bills as a stand-in. It measures how often the variable loan cost more in total interest than the fixed one, and by how much at worst. It then varies the head start from 3 points under to 1 point over.
> 
> 2. The answer
> Measured by how often the variable loan cost more in total interest than the 9% fixed loan, and the worst-case extra cost:
> - From 1981 on, a 2-point head start was enough every time (0% cost more). At Leah's 1.5 points, 3.5% of later starts cost more.
> - From 1954 to 1980, even 3 points was not enough. 10.5% of those starts still cost more, the worst by $6,033.
> - At 2 points, 20.4% of 1954-80 starts cost more (worst $9,472). At 1.5 points, 28.4% did (worst $11,219, starting April 1977).
> - Overall, at Leah's 1.5 points, the variable loan cost more in about 1 in 7 stretches. The worst case was $11,219 more, 43% extra interest.
> - Leah's 1.5 points sits short of the 2-point mark.
> - Which kind of history comes next can't be known.
> 
> 3. Confusing passages
> - "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." It is explained afterward with the "cushion", but it was hard to follow on first hearing.
> - "That's more than 1 in 4 for starts from 1954 to 1980 and about 1 in 30 from 1981 on." Later the video says 28.4% and 3.5%. "1 in 30" is about 3.3%, so the figures are close but not obviously the same, and the fractions and percentages are mixed.
> - "A point here means one percentage point of interest." and "head start can be... negative" were a bit abstract.
> - "A real variable rate is the lender's own index plus a fixed margin... sets the margin so that Leah's rate starts at 7.5%." The stand-in Treasury-bill logic is dense.
> 
> 4. Attention drop
> The paragraph beginning "Here's how the replay works..." through "...the data is US only." It is methodological detail about indexes, margins, monthly start dates and non-independent overlapping stretches. It has no direct payoff for my own loan decision. The numbers-heavy stretch at the end of paragraph 19 (28.4%, 3.5%, 20.4%, 10.5%, with several dollar figures) is a second dip, because the percentages arrive too quickly to hold in my head.
> 
> 5. Does it tell me which loan to take or predict rates?
> No. It says explicitly "This is history, not a forecast", "Which kind of history comes next is something no replay can show", and "The line doesn't say which offer is better." It only shows what each head start meant in each kind of history. It also lists what it leaves out (the lender's real index, rate caps, grace periods, fees, my own budget).

**38101327** · mẫu weak · vai T

> 1. The video follows Maya, who borrowed $375,000 at the October 2023 peak of 30-year mortgage rates and is now weighing a refinance that costs $5,124. It also follows two other borrowers, Dan ($115,000) and Priya ($1,005,000), at the same rate, to show how loan size changes the result. It first shows that the standard calculator answer (closing cost divided by monthly savings, 24 months) leaves out the slower balance paydown on a fresh 30-year loan. It then tests all 13 drops of at least 1 point since 1971 and ends with how big a rate cut is needed for each loan size.
> 
> 2. The question is how far rates must fall before a refinance pays for itself. For a loan like Maya's, counting both the monthly savings and the extra balance still owed, a cut of 0.5 points pays it back within 36 months. Dan, with a small loan, needs 1.12 points. Priya, with a large loan, needs 0.2 points. Today's cut is 0.59 points. For Maya, that means break-even at 30 months (not the 24 the simple division gives), and a loss if she sells before then. The rest depends on loan size, loan age, and how long she keeps the house.
> 
> 3. Confusing passage: "Below 0.5 points, the fresh start can swallow the savings entirely." and "Counting the balance, Maya never catches up before her old loan would have been paid off." It is not obvious why a lower payment never pays back. I had to work out that restarting the 30-year schedule means paying mostly interest again. Also confusing: "Maya's old loan already has 35 payments behind it" next to "borrowed in October 2023". The timeline of when she would refinance versus when she borrowed was unclear. Also "a drop counts when the monthly average falls at least 1 point from a peak before rising 1 point from its low" in the method section, which is dense.
> 
> 4. Attention dropped in the historical section: "We found every fall of at least 1 point in the 30-year rate since 1971: 13 of them... The biggest fall began after the peak of 18.63% in 1981. A refinance 2 months later paid back in 13 months..." and the 1984 example with "the next drop of 1 point came 7 months later". Many dates and month counts from decades ago, with 1980s rates that feel irrelevant to me. The closing method paragraph (Freddie Mac, FRED, Optimal Blue, HMDA filters) also lost me, though it is clearly reference material.
> 
> 5. No. The video does not say which loan to take or whether to refinance. It describes the trade-off and gives break-even thresholds by loan size. It says outright that "the rates here are history, not a forecast" and "nothing here says where rates go next." It also does not cover taxes or the return on cash. It is also about mortgage refinancing, not the private graduate loans I care about, so I would have to translate the idea (size of the cut, age of the loan, how long I hold it) to student loans myself.

**0258ece8** · mẫu weak · vai T

> 1. Summary: The video follows "Maya," an illustrative borrower who took a $375,000 mortgage at the October 2023 peak rate (7.62%) and now asks whether paying a median $5,124 in closing costs to refinance at about 7.03% is worth it. It compares her with Dan (small $115k loan) and Priya (large $1.005M loan), shows that the usual "closing cost / monthly saving" calculator answer (24 months) understates break-even (30 months) because a refinance restarts the 30-year amortization and leaves more principal owed. It then replays all 13 rate drops of 1+ point since 1971 and ends with a rule of thumb based on size of rate cut, loan age and how long you stay.
> 
> 2. Answer: How far must rates fall for a refinance to pay back within 36 months? For a Maya-sized loan, counting the balance still owed, a cut of 0.5 points. Dan (small loan) needs 1.12 points; Priya (large loan) needs 0.2. Today's 0.59-point cut means Maya breaks even at 30 months (not 24); she is behind if she sells earlier, $1,039 ahead at 3 years and $8,093 ahead at 7. Cuts under 0.5 points can be swallowed by the restart of the loan. Historically, simple loans took 10-20 months to break even, and Dan-like small loans took 18-39 months.
> 
> 3. Confusing passages:
> - "Below 0.5 points, the fresh start can swallow the savings entirely." and "At a cut of 0.25 points, the division would promise 38 months. Counting the balance, Maya never catches up before her old loan would have been paid off." The "fresh start" / balance-difference idea is hard to grasp when spoken once, with no visual.
> - "Counting what was still owed, break-even took between 10 and 20 months. The simple division would have said between 10 and 21. Nearly the same, because those loans were only months old..." This is dense, and it seems to conflict with the earlier "division understates" point until the loan-age explanation lands.
> - "Maya's old loan already has 35 payments behind it" versus "She borrowed in October 2023" and "today's rate": the timeline is not obviously reconciled, and the 7.62% vs 7.03% rate and the "cut of 0.59" (not 0.59 = 7.62-7.03, as the video says about "today's cut") took me a moment.
> - "A drop counts when the monthly average falls at least 1 point from a peak before rising 1 point from its low." This is jargon-heavy and fast.
> 
> 4. Attention drop: the long run of numbers for Dan and Priya ("If Dan sells after 3 years, the refinance leaves him $1,777 behind. After 7 years, he is only $386 ahead. Priya saves $593 a month... $11,482 ahead; after 7, $30,387."), and especially the method paragraph near the end ("Method. Rates are Freddie Mac's weekly survey via FRED, checked against the Optimal Blue index since 2017... HMDA loan-level data..."). It is a stream of figures and data-source names with no consequence for my decision, so I tuned out.
> 
> 5. Does it tell me which loan to take or predict rates? No. It explicitly says "The rates here are history, not a forecast" and "nothing here says where rates go next." It does not compare loan products or lenders. It only gives a break-even framework (size of cut, age of loan, how long you stay). It is also about refinancing a mortgage, not graduate student loans, so it does not address my private-loan situation at all.

