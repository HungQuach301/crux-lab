# C2 vòng 3 — kiểm mù đoạn đã sửa S04–S12 (v4 vs đối chứng v3; ý đồ `gates/C2-intent-r3.md`)

| Chỉ số (ứng viên v4: 5 vai đích + 1 phổ thông) | v4 | Đối chứng v3 (3) | Ngưỡng ghi trước | Kết quả |
|---|---|---|---|---|
| "Đúng" (vai đích) | **5/5** (+1/1) | 3/3 | ≥ 4/5 | đạt |
| Đoạn phương pháp là chỗ mất chú ý | **6/6** (5 lần là chỗ số 1) | 3/3 | ≤ 2/6 | **không đạt** |
| Dãy số theo khoảng chênh nặng | **3/6** | 2/3 | ≤ 2/6 | **không đạt (sát)** — giảm từ 5/6 |
| Hai dạng của cùng tỉ lệ (1 in 30 vs 3.5%) | **0/6** | 3/3 | ≤ 2/6 | đạt |
| Lặp bộ số của Leah | **0/6** | — | ≤ 2/6 | đạt |
| *Mới:* "43% on top of that" không rõ 43% của cái gì | 5/6 | — | — | sửa câu |
| *Mới:* không rõ 28.4%/3.5% là hai phần của 14.2% | 3/6 | — | — | sửa câu |

**Đọc kết quả:** dời đoạn phương pháp ra sau không làm người đọc bớt mất chú ý; lý do họ nêu nhất quán: *"methodology with no payoff for my decision"*, *"comes after the answer"*. Đây là vấn đề **có nói đoạn này bằng lời hay không**, không phải vị trí. Không lặp vòng 4 (theo ý đồ) → đưa phương án lên chủ dự án.

## Nguyên văn

**6044fb99** · mẫu cand · vai G

> 1. Summary: The excerpt follows Leah, an illustrative graduate student choosing between a 9% fixed private loan and a variable loan that starts at 7.5%. It replays her loan through every 10-year stretch of US history since 1954, using the 3-month Treasury bill rate to move her rate. It first shows a puzzle: her rate went above 9% in 76.2% of stretches, yet the variable loan cost more in only 14.2%. It explains this with the head-start "cushion", and it splits history into a climbing-rates half (1954-1980) and a falling-rates half (1981 on). It then tests bigger and smaller head starts, explains how the replay was built, and ends by saying real offers can be compared to the results.
> 
> 2. Answer to the main question ("how much lower does a variable rate have to start before the risk has been worth it?"): It gives two answers, depending on which history repeats. For starts from 1981 on, a 2-point head start was enough every time (0% cost more). For starts from 1954 to 1980, even a 3-point head start was not enough: 10.5% of those stretches still cost more, and the worst cost $6,033 more. At 2 points, 20.4% of the 1954-1980 starts cost more (worst $9,472 more). Leah's 1.5-point head start gave 28.4% of the early starts and 3.5% of the later starts costing more, and the worst was April 1977 at $11,219 more.
> 
> 3. Confusing passages:
> - "That's 28.4%, more than 1 in 4, for starts from 1954 to 1980, and 3.5%, about 1 in 30, from 1981 on." I couldn't tell at first that the 28.4% and 3.5% split the 14.2%. The sentence follows the 14.2% figure without saying so.
> - "Leah's variable loan charges 43% on top of that, the worst stretch in the whole replay." This is unclear because 43% of $26,005 is about $11,200. That matches the $11,219 from earlier, but the video never says so. "On top of that" is also ambiguous.
> - "Leah's illustrative offer sits at 1.5 points, short of that 2-point mark." Earlier the video says 7.5% against 9%, and that is a 1.5-point head start. But the intro line says the head start ranges "from 3 points under the fixed rate to one 1 point over it". I had to work out that the head start is the fixed rate minus the variable rate.
> 
> 4. Attention dropped most in the "how the replay was built" paragraph: "A real variable rate is the lender's own index plus a fixed margin, and the replay needs a much longer record than that index has. So it uses the rate on 3-month Treasury bills..." It is a dense methods passage with technical terms (index, margin, stand-in). It also comes after the main answer, so it feels like a technical footnote. The cushion paragraph is also fairly abstract, but I found it useful.
> 
> 5. No. It does not tell the viewer which loan to take, and it does not predict rates. It says repeatedly "This is history, not a forecast" and "Which kind of history comes next is something no replay can show". It also says "The line doesn't say which offer is better; it shows what each head start meant in each kind of history." It lists what a real offer has that the replay ignores, such as a rate cap, fees and the borrower's budget.

**0bcb56bb** · mẫu cand · vai T

> 1. Summary: The excerpt is about Leah, an illustrative grad student weighing a 9% fixed private loan against a variable loan starting at 7.5%. The video replays her loan through every 10-year stretch of US history since 1954, moving her rate with the 3-month Treasury bill, and asks how often the variable loan cost more in total interest and by how much at worst. It first resolves an apparent paradox: her rate went above 9% in about 3 in 4 stretches, yet the variable loan cost more in only about 1 in 7. It then shows the worst case (April 1977), varies the head start, and ends with a line any real offer can be compared to, plus how the replay was built.
> 
> 2. Answer: Overall the variable loan cost more in 14.2% of stretches (28.4% for starts 1954-1980, 3.5% for 1981 on). The worst case, April 1977, cost $11,219 more (43% more interest than the fixed loan's $26,005). The best, August 1981, cost $15,295 less. With a 2-point head start, no start from 1981 on cost more, but 20.4% of 1954-1980 starts did (worst +$9,472). At 3 points, 10.5% of 1954-1980 starts still cost more (worst +$6,033). So: from 1981 on, a 2-point head start was enough every time; for 1954-1980, even 3 points wasn't. Leah's 1.5 points falls short of the 2-point mark. Which kind of history comes next can't be shown.
> 
> 3. Confusing: "Leah's variable loan charges 43% on top of that, the worst stretch in the whole replay." I wasn't sure whether 43% referred to interest or the $11,219 (it works out to roughly 43% of $26,005, but that isn't stated). Also, "That's 28.4%, more than 1 in 4, for starts from 1954 to 1980, and 3.5%..." came right after 14.2%, and the sentence structure made me briefly lose track of what "that's" referred to. Also "a head start... from a variable rate 3 points under the fixed rate to one 1 point over it" is slightly confusing, since Leah's gap is 1.5 points, not a whole number, and the 2- and 3-point cases are described relative to her.
> 
> 4. Attention dropped most in the methods paragraph: "A real variable rate is the lender's own index plus a fixed margin, and the replay needs a much longer record than that index has. So it uses the rate on 3-month Treasury bills..." through "Neighbouring stretches share most of their years, so they are not independent tries." It's technical, comes after the answer, and doesn't affect my decision directly. The dense run of percentages and dollar figures in the head-start paragraph ("At 2 points... At 3 points...") also got hard to hold in my head.
> 
> 5. No. It explicitly says "History, not a forecast" and "The line doesn't say which offer is better," and it says which kind of history comes next can't be shown. It gives a comparison framework, not a recommendation or a rate prediction. It also notes that real offers have caps, fees, grace periods and the borrower's own budget, which the replay omits.

**f8bd419b** · mẫu cand · vai T

> 1. Summary
> The excerpt is about Leah, an illustrative grad student choosing between a 9% fixed private loan and a variable loan starting at 7.5%. The problem is how often the variable loan would have cost more in total interest than the fixed one, and by how much at worst. The video replays her loan through every 10-year stretch of US history since 1954, using the 3-month Treasury bill rate as a stand-in for the index. First it shows the apparent paradox: her rate rose above 9% in most stretches, but the total cost was higher in only a minority. It explains this with the "cushion" from the early low-rate months. It then splits history at the 1981 rate peak, walks through the worst case (April 1977), tests different head starts, and ends with a method note and a reminder that this is history, not a forecast.
> 
> 2. Answer to the main question
> The question is how much lower a variable rate has to start before the risk is worth it, measured as how often it cost more and how much more at worst.
> - Leah's 1.5-point head start: the variable loan cost more in 14.2% of stretches overall. That is 28.4% for starts from 1954 to 1980 and 3.5% from 1981 on. The worst case was April 1977, at $11,219 more.
> - 2-point head start: none of the 1981-on starts cost more, but 20.4% of the 1954-to-1980 starts still did, the worst by $9,472.
> - 3-point head start: still none from 1981 on, and 10.5% of the 1954-to-1980 starts cost more, the worst by $6,033.
> - Conclusion: from 1981 on, a 2-point head start was enough every time. From 1954 to 1980, even 3 points was not enough. Which kind of history comes next is unknown.
> 
> 3. Confusing passages
> - "Leah's variable loan charges 43% on top of that, the worst stretch in the whole replay." It is unclear whether 43% means 43% more interest than the fixed loan's $26,005 (about $11,200, which matches the earlier $11,219) or something else. I had to work that out myself.
> - "Leah's illustrative offer sits at 1.5 points, short of that 2-point mark..." The 2-point mark is only defined as where 1981-on starts stopped costing more. The same sentence then says stretches "from both halves of history" still cost more at 1.5 points. That is a little muddled.
> - "Leah's 1.5 points gives the split already heard." The video said 7.5% versus 9%, which is 1.5 points, but the line earlier in the excerpt called it a "head start", so it is mildly confusing.
> - "28.4%, more than 1 in 4 ... 3.5%, about 1 in 30" arrives right after the 14.2% figure. The overall number looks like it should sit between the two but is stated before the split is explained.
> 
> 4. Where my attention dropped
> The method paragraph: "A real variable rate is the lender's own index plus a fixed margin, and the replay needs a much longer record than that index has. So it uses the rate on 3-month Treasury bills..." It is dense with technical detail (margin, index, overlapping stretches not being independent) that doesn't change what I would do. It is also the part furthest from my own loan decision.
> 
> 5. Does it tell me which loan to take or predict rates?
> No. It says outright "This is history, not a forecast," and that "the line doesn't say which offer is better." It says no replay can show which kind of history comes next. It also lists what the replay leaves out: the real index, a rate cap, a grace period, fees, and my own budget. It gives a way to compare an offer against past outcomes and leaves the choice and the rate outlook to me.

**902e1a65** · mẫu cand · vai T

> 1. Summary: The excerpt is about Leah, an illustrative grad student weighing a 9% fixed private loan against a variable loan starting at 7.5%. The video replays her loan through every 10-year window of US history since 1954, with her rate tracking the 3-month T-bill. It asks how often the variable loan cost more in total interest than the fixed one, and by how much at worst. It first resolves an apparent paradox: her rate went above 9% in 76.2% of windows, yet total cost was higher in only 14.2%, because the early head start builds a cushion. It then splits history at 1981, and varies the head start (1.5, 2 and 3 points) to build a comparison line. It ends with how the replay was built and what it leaves out.
> 
> 2. Answer to the main question ("how much lower must a variable rate start before the risk is worth it?"): Measured as how often it cost more and by how much at worst, history gives two answers. From 1981 on, a 2-point head start was enough every time (0% cost more). From 1954 to 1980, even 3 points wasn't: 10.5% of starts still cost more, the worst by $6,033. At Leah's 1.5 points, 14.2% of all windows cost more (28.4% for 1954-1980 starts, 3.5% from 1981), and the worst, from April 1977, cost $11,219 more (43% extra interest on $26,005). The best case, from August 1981, saved $15,295. At 2 points, 20.4% of the early starts still cost more, the worst by $9,472. The worst window began in April 1977 at every head start tested. Which kind of history comes next is unknown.
> 
> 3. Confusing passages:
> - "That's 28.4%, more than 1 in 4, for starts from 1954 to 1980, and 3.5%, about 1 in 30, from 1981 on." It's dropped in with no lead-in and no label saying these split the 14.2%, so I had to infer it. The "1.5 points" head start is also never explained here (7.5 vs 9), which is a bit jarring.
> - "Leah's variable loan charges 43% on top of that, the worst stretch in the whole replay." It is unclear whether 43% is on top of $26,005 (about $11,200, which matches the earlier figure only by inference).
> - "Neighbouring stretches share most of their years, so they are not independent tries." Plausible but abstract. I don't know how much it weakens the percentages.
> - Line 3 mentions "a line that any real offer can be held up against", but the "line" is never clearly shown. It seems to mean the 2-point threshold, and that only becomes clear at the end.
> 
> 4. Attention dropped most: the paragraph at "So far, every result has been for one pair of rates... At 2 points, none of the starts from 1981 on cost more, but 20.4%... At 3 points, still none... 10.5%... $6,033." Many near-identical percentages and dollar figures are read in a row in audio with nothing visual to hold them, so they blur together. The build-method paragraph ("A real variable rate is the lender's own index plus a fixed margin...") also lost me, being technical and less relevant to my decision.
> 
> 5. No. It does not tell me which loan to take and makes no rate prediction. It says "History, not a forecast," "Which kind of history comes next is something no replay can show," and "The line doesn't say which offer is better." It gives a way to compare my own offer's head start against past outcomes, and lists what it leaves out (real index, cap, grace period, fees, my budget).

**7476cf3c** · mẫu cand · vai T

> 1. Summary: The narration follows Leah, an illustrative grad student choosing between a 9% fixed private loan and a variable loan starting at 7.5%. It replays her loan through every 10-year stretch of US history since 1954, using the 3-month Treasury bill rate as a stand-in for how her rate would move. It asks how often the variable loan cost more in total interest than the fixed one, and by how much at worst. It then shifts the variable loan's head start from 3 points below the fixed rate to 1 point above it, and ends by saying the result is a yardstick for real offers, not a forecast.
> 
> 2. Answer: The variable rate went above 9% at some point in 76.2% of stretches, but it cost more in total interest in only 14.2%. For starts in 1954-1980 that figure was 28.4%, and for starts from 1981 on it was 3.5%. The worst case, a loan started in April 1977, cost $11,219 more (43% more interest on top of $26,005). The best case, August 1981, cost $15,295 less. The head start builds a cushion of savings that later high rates must use up first. A 2-point head start was enough every time from 1981 on. From 1954-1980, even 3 points was not: 20.4% of those starts still cost more at 2 points, and 10.5% at 3 points, with a worst case of $6,033 more. Leah's 1.5-point head start falls short of that 2-point mark. Which kind of history comes next can't be known.
> 
> 3. Confusing: "Leah's variable loan charges 43% on top of that, the worst stretch in the whole replay." It is unclear whether that 43% matches the $11,219 figure, and the "on top of that" wording is awkward. Also: "Neighbouring stretches share most of their years, so they are not independent tries" is statistical jargon, and I don't know what it means for the percentages. "A real variable rate is the lender's own index plus a fixed margin" is only briefly explained. I also had to hold many numbers at once in the middle section.
> 
> 4. Attention dropped most in the build-method paragraph: "Here's how the replay was built. A real variable rate is the lender's own index plus a fixed margin, and the replay needs a much longer record than that index has..." It is technical, comes after the answer, and doesn't change what I'd do. The head-start paragraph, with its stacked percentages for each split (2 points, 3 points, 1954-1980 versus 1981 on), also tired me.
> 
> 5. No. It doesn't say which loan to take. It says the line "doesn't say which offer is better," and it lists things it leaves out: fees, a rate cap, grace period, my budget. It also doesn't predict rates: "This is history, not a forecast" and "no replay can show" what comes next. It does give a way to compare an offer against past outcomes, which is useful to me.

**99ba14d6** · mẫu cand · vai T

> 1. Summary
> The excerpt is about Leah, an illustrative grad student choosing between a 9% fixed private loan and a variable loan starting at 7.5%. The video replays her loan through every 10-year stretch of US history since 1954, with her rate moving as the 3-month Treasury bill rate did. It asks how often the variable loan ended up costing more than the fixed one, and by how much at worst. It first shows a puzzle: her rate went above 9% in 76.2% of stretches, yet the variable loan cost more in only 14.2%. It explains this with the "cushion" built by early savings. It then splits history at 1981 and varies the head start (1.5, 2 and 3 points). It ends by saying history is not a forecast, and that a real offer has other features the replay ignores.
> 
> 2. Answer to the main question
> The question is how much lower a variable rate must start before the risk has been worth it.
> - From 1981 on, a 2-point head start was enough every time. No stretch cost more at 2 or 3 points. At Leah's 1.5 points, 3.5% of stretches cost more.
> - From 1954 to 1980, even 3 points was not enough. At 3 points, 10.5% of stretches still cost more, and the worst cost $6,033 more. At 2 points, 20.4% cost more, and the worst cost $9,472 more.
> - Leah's 1.5-point head start falls short of the 2-point mark. 28.4% of the 1954-to-1980 stretches cost more, and the worst (April 1977) cost $11,219 more. Her variable payment rose to $863.36 a month against $633.38 fixed.
> - So the answer depends on which era repeats, and the video says that can't be known.
> 
> 3. Confusing passages
> - "Leah's variable loan charges 43% on top of that, the worst stretch in the whole replay." It is unclear whether 43% is 43% of $26,005 (about $11,200). That would match the $11,219 earlier, but the video never says so.
> - "That's 28.4%, more than 1 in 4, for starts from 1954 to 1980, and 3.5%, about 1 in 30, from 1981 on" is dense, and it is not obvious how these split figures combine into the 14.2% overall.
> - "Leah's 1.5 points" and "7.5% against 9%" are two ways of stating the same gap, so the shift in terminology slows me down.
> - "Leah's illustrative offer sits at 1.5 points, short of that 2-point mark, where stretches from both halves of history still cost more." This is confusing because at 2 points, no post-1981 stretches cost more. It seems to mean "at 1.5 points," but the wording says "that 2-point mark."
> - "The line doesn't say which offer is better; it shows what each head start meant in each kind of history." I'm not sure which "line" this refers to, since no chart is visible in the narration. The earlier "there's a line that any real offer can be held up against" has the same problem.
> 
> 4. Where attention dropped
> The "Here's how the replay was built" paragraph, starting "A real variable rate is the lender's own index plus a fixed margin, and the replay needs a much longer record than that index has." It is methodology (index, margin, overlapping windows, "not independent tries"), and it comes after the conclusion. It matters less to my decision than the results do.
> 
> 5. Does it tell me which loan to take or predict rates?
> No. It says "This is history, not a forecast," "Which kind of history comes next is something no replay can show," and "The line doesn't say which offer is better." It gives a way to compare an offer (the head start) against how often and how badly it would have lost historically. It leaves out the real index, a cap, a grace period, fees and my own budget, so I still have to weigh those myself.

**d65fd464** · mẫu v3 · vai T

> 1. Summary: The excerpt is about Leah, an illustrative grad student choosing between a 9% fixed private loan and a variable loan starting at 7.5%. The problem is how much lower a variable rate must start before the risk is "worth it", meaning how often it cost more in total interest than the fixed loan, and by how much at worst. The video replays every 10-year stretch of US rates since 1954, using 3-month Treasury bills as a stand-in for the index. It explains the "cushion" idea, shows the worst case (April 1977, $11,219 more), then varies the head start (1.5, 2, 3 points) and ends by saying history gives two answers and no replay can say which comes next.
> 
> 2. Answer: Measured as above, it depends on which era. For starts from 1981 on, a 2-point head start was enough every time (0% cost more). For 1954-1980 starts, even 3 points was not enough: 10.5% still cost more, worst by $6,033. At Leah's 1.5 points, 28.4% of the 1954-1980 starts and 3.5% of later ones cost more, worst by $11,219. Overall, the variable rate rose above 9% in about 3 in 4 stretches but cost more in total in about 1 in 7. Leah's 1.5-point offer falls short of the 2-point mark.
> 
> 3. Confused me:
> - "Yet it cost more in total interest in about 1 in 7. That's more than 1 in 4 for starts from 1954 to 1980 and about 1 in 30 from 1981 on." This is dense. The 1-in-7 and the era splits arrive before I know there are two eras. Later the 1.5-point figures are 28.4% and 3.5%, which I had to match to "more than 1 in 4" and "about 1 in 30" myself.
> - "From then on, her rate rises and falls exactly as much as the Treasury bill rate did." The margin and index idea is compressed, and I wasn't sure how this maps to a real private loan index.
> - "Neighbouring stretches share most of their years, so they are not independent tries." It's unclear what that means for how much to trust the percentages.
> 
> 4. Attention dropped: "A real variable rate is the lender's own index plus a fixed margin, and the replay needs a much longer record than that index has. So it uses a stand-in..." through "...up to September 2016." This is methodology with no payoff for my decision, and it comes right after the engaging cushion explanation. The paragraph on the three head-start tiers with many percentages and dollar figures in a row was also a close second.
> 
> 5. No. It says it is history, not a forecast ("Which kind of history comes next is something no replay can show"), and it says the line "doesn't say which offer is better". It gives a way to hold my own offer against past outcomes. It does not pick fixed or variable, and it does not predict rates. It also notes what it leaves out: the real index, caps, fees, grace period and my own budget.

**b752063c** · mẫu v3 · vai T

> 1. Summary: The excerpt is about Leah, an illustrative grad student weighing a 9% fixed private loan against a variable loan that starts at 7.5%. The problem is how much lower a variable rate must start before the risk is "worth it", meaning how often it cost more in total interest than the fixed loan, and how much more at worst. The video replays the loan over every 10-year stretch of US history since 1954, using the 3-month Treasury bill rate as a stand-in. It shows that the variable loan cost more in only about 1 in 7 stretches, even though the rate went above 9% in about 3 in 4. It then walks through the worst case (April 1977) and reruns the test with different head starts.
> 
> 2. Answer: It gives two answers, depending on which era repeats. From 1981 on, a 2-point head start (variable starting at 7% against 9% fixed) was enough every time, with no stretch costing more. From 1954 to 1980, even a 3-point head start was not enough: 10.5% of starts cost more, the worst by $6,033. At 2 points, 20.4% of the early starts cost more, the worst by $9,472. At Leah's 1.5 points, 28.4% of early starts and 3.5% of later ones cost more, the worst by $11,219. The reason it works is the "cushion" of early savings, which rising rates must use up first. Which era comes next is unknowable.
> 
> 3. Confusing: "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." This is confusing at first because it seems contradictory. The next paragraph on the cushion resolves it. Also confusing: "At Leah's 1.5 points, 28.4% of the 1954-to-1980 starts and 3.5% of the later ones cost more", because I had to remember that the "head start" is the gap below 9%, and the earlier "about 1 in 30" for later starts doesn't obviously match 3.5%. 1 in 30 is about 3.3%, so they roughly agree. The jump from 3-points-under to "1 point over" in the intro is also unclear, since the excerpt never shows the 1-point-over results. The "$11,219 more, 43% on top" is also slightly unclear: I wasn't sure whether 43% is of total interest.
> 
> 4. Attention dropped: Most in the "Here's how the replay works" paragraph, especially "Neighbouring stretches share most of their years, so they are not independent tries, and the data is US only." The method detail (index plus margin, Treasury bill stand-in, start and end dates) is dense and technical, and I had to take it on trust. The long run of dollar figures in the April 1977 paragraph ($863.36, $633.38, $26,005) also made me skim.
> 
> 5. No on both counts. It does not tell me which loan to take: it says "The line doesn't say which offer is better", and it lists what a real offer adds (real index, cap, grace period, fees, my budget). It does not predict rates either: it says "This is history, not a forecast" and "Which kind of history comes next is something no replay can show."

**9c1aff6a** · mẫu v3 · vai T

> 1. Summary: The excerpt is about Leah, an illustrative grad student weighing a 9% fixed private loan against a variable loan starting at 7.5%. The video replays her loan through every 10-year window of US rates since 1954, using 3-month Treasury bills as a stand-in for the variable index. It counts how often the variable loan cost more total interest than the fixed one, and by how much at worst. It then changes the head start (variable rate 3 points under to 1 point over the fixed rate) to show where the history changes. It ends by saying a real offer can be placed on that line, and that this is history, not a forecast.
> 
> 2. Answer: How much lower must a variable rate start to be "worth the risk"? For Leah's 1.5-point head start, the variable loan cost more in about 1 in 7 windows. That was 28.4% of 1954-1980 starts and 3.5% of 1981-on starts, and the worst case was $11,219 more (April 1977 start, 43% on top of the fixed loan's $26,005 interest). At 2 points, no 1981-on start cost more, but 20.4% of 1954-1980 starts did (worst $9,472). At 3 points, none from 1981 on, and 10.5% of 1954-1980 starts still cost more (worst $6,033). So from 1981 on, 2 points was always enough. For 1954-1980, even 3 points was not. Which era comes next is unknowable.
> 
> 3. Confusing: "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." This looked contradictory at first. The "cushion" explanation resolves it, but I had to work through it. Also "That's more than 1 in 4 for starts from 1954 to 1980 and about 1 in 30 from 1981 on" confused me because the 1 in 7 overall figure and the later 3.5% (about 1 in 29) and 28.4% figures only fit together after I thought about how many windows are in each era. The phrase "sets the margin so that Leah's rate starts at 7.5%" is also a bit jargony (index plus margin).
> 
> 4. Attention drop: Paragraph on method: "A real variable rate is the lender's own index plus a fixed margin... Neighbouring stretches share most of their years, so they are not independent tries, and the data is US only." It is technical, with no stakes for my own loan. The stacked percentages at line 15 ("At Leah's 1.5 points, 28.4%... At 2 points... At 3 points...") also became a wall of numbers.
> 
> 5. No. It never tells me which loan to take or what rates will do. It says "This is history, not a forecast" and "no replay can show" which era comes next. It gives a line to compare my own offer against, and it notes the replay omits the real index, caps, grace periods, fees and my budget.

