# C2 — Kết quả kiểm mù bản chép lời (nguyên văn; chấm theo `gates/C2-intent.md`)

9 agent mới (sonnet), mỗi agent một file hex. Khoá `review-c2/key.json`. Ứng viên = `review-c2/transcript.txt` (script v2, CO-A). Đối chứng yếu = M1b Tập 1.

## Tóm tắt

| | Ứng viên (vai đích) | Ứng viên (phổ thông) | Đối chứng yếu M1b (vai đích) |
|---|---|---|---|
| "Đúng" (tóm tắt + đáp án hai thời kỳ + câu 5 "no") | **5/5** | 1/1 | 3/3 hiểu đáp án của M1b |
| Câu 5 "sẽ chỉ định / dự báo?" | 0/6 "yes" | — | 0/3 |
| Đọc thành "variable is safe/usually better" không kèm thời kỳ | 0/6 | — | — |

**Đọc kết quả:** ứng viên qua (5/5 ≥ 4/5). Đối chứng yếu cũng được hiểu 3/3 → chỉ số "hiểu" **không phân biệt được** (đúng bài học M3); báo chủ dự án. Tín hiệu phân biệt nằm ở câu 3–4:

| Chỗ khó hiểu / mất chú ý (ứng viên, 6 người đọc) | Số người nêu | Xử lý đề xuất |
|---|---|---|
| **Đoạn phương pháp** (S04: chỉ số thay thế, sàn 0, không ân hạn/phí/trần, 753 cửa sổ chồng nhau) — chỗ mất chú ý nhiều nhất | **5/6** | rút lời; giới hạn chuyển sang thẻ phương pháp trên hình + mô tả; giữ một câu "US only", một câu chồng nhau |
| **Dãy số ở thanh trượt** (S08: 79%, 42%, 20.4%, 10.5%, $16,566, $9,472, $6,033) | **5/6** | số chuyển lên hình; lời chỉ nói 2 mốc (2 điểm và 3 điểm) |
| "token", "bin" — từ chỉ hình lọt vào lời | **5/6** | bỏ khỏi lời (chỉ là ghi chú hình) |
| "plus a fixed 3.78 points" (biên) không giải thích | 5/6 | nói bằng lời thường hoặc bỏ số |
| Nghịch lý "3 trong 4 / 1 trong 7" gây khó hiểu cho tới đoạn "đệm" | 5/6 | **có chủ đích** (căng thẳng → giải đáp); có thể rút ngắn khoảng cách |
| Trộn phân số và phần trăm (1 in 4, 1 in 30, 79%, 20.4%) | 3/6 | thống nhất một dạng trong đoạn kết quả |
| Câu phủ định kép "never fell to zero, even where none…" | 1/6 | viết lại |

Đối chứng yếu M1b: mất chú ý ở đoạn lịch sử nhiều ngày tháng (3/3) và thấy không liên quan tới mình (2/3) — đúng như dự đoán.

## Nguyên văn

**84243579** · mẫu cand · vai G

> 1. Summary
> The video follows Leah, an illustrative new grad student who can no longer get Grad PLUS loans (ended July 2026). She has two private offers for $50,000 over 10 years: 9% fixed, or a variable rate starting at 7.5%. The question is how much lower a variable rate must start to be "worth" the risk. The video replays her loan through every 10-year stretch of US Treasury bill rates since 1954 (753 start months). It counts how often the variable loan cost more in total interest than the fixed one, and by how much at worst. It then slides the starting gap ("head start") from 3 points under to 1 over, and ends with a line any real offer can be compared against.
> 
> 2. The answer
> It gives two answers, depending on which history you assume. For starts from 1981 on, no stretch cost more once the head start reached 2 points. For starts from 1954 to 1980, even a 3-point head start left 10.5% of stretches costlier, with the worst $6,033 more. Leah's 1.5-point head start is short of the 2-point mark. At her point, more than 1 in 4 of the 1954-1980 starts and about 1 in 30 of the later ones cost more, and the worst case (April 1977) cost $11,219 more, or 43% on top of the fixed loan's $26,005 interest. Overall, about 1 in 7 stretches cost more, even though her rate went above 9% at some point in about 3 in 4. The reason is the "cushion": early savings from the lower rate, on the biggest balance, must be used up before the variable loan costs more overall.
> 
> 3. Confusing passages
> - "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." It is the central puzzle, and it was confusing until the cushion explanation later.
> - "Each start month becomes one token, sorted into the bin under the half of history where it began." "Token" and "bin" refer to visuals I could not follow from the narration alone.
> - "Leah's 7.5% is that rate plus a fixed 3.78 points" and the zero floor. This is a dense methods stretch, and it is not obvious why a stand-in index is needed.
> - "More than 1 in 4 ... and about 1 in 30" is given without saying which half is which at first mention, and many stats come close together.
> 
> 4. Where attention dropped
> "Here's how the replay works. A real variable rate follows the lender's own index, and the replay needs a much longer record than that index has... The stretches overlap, so they are not 753 independent tries, and the data is US only." This is a long block of methodology, with many numbers and caveats and no story. The slider paragraph ("At 2 points... At 3 points...") is also a dense run of percentages and dollar figures.
> 
> 5. Does it recommend a loan or predict rates?
> No. It says repeatedly "This is history, not a forecast" and "Which kind of history comes next is something no replay can show." It also says the line "doesn't say which offer is better." It only shows what each head start meant in each kind of past, and it lists what real offers add (real index, cap, grace period, fees, your budget).

**d471145d** · mẫu cand · vai T

> 1. Summary
> The video follows Leah, an illustrative new grad student who, because Grad PLUS ended for new borrowers on July 1, 2026, has two private offers for $50,000 over 10 years: 9% fixed, or a variable rate starting at 7.5%. The problem is how much lower a variable rate must start (the "head start") for the risk to have been worth it. It replays her loan through every 10-year stretch of US rates since 1954, using 3-month Treasury bills as a stand-in index, and counts how often the variable loan cost more in total interest than the fixed one, and by how much at worst. It then slides the head start from 0 to 3 points to show where history changes, and ends by saying it is history, not a forecast.
> 
> 2. The video's answer
> It gives two answers by era. For starts from 1981 on, no stretch cost more once the head start reached 2 points. For starts from 1954 to 1980, even 3 points left 10.5% of stretches costlier, the worst by $6,033. Leah's 1.5-point head start falls short of the 2-point mark. At her offer, more than 1 in 4 of the 1954-1980 starts cost more, and about 1 in 30 of the later ones did. The worst case (April 1977) cost $11,219 more, 43% on top of the fixed loan's $26,005 interest. With no head start, 79% of the early starts and 42% of the later ones cost more, and the worst was $16,566 more. Overall, Leah's variable rate topped 9% in about 3 in 4 stretches, but the variable loan cost more in only about 1 in 7. This is because early savings build a cushion that later higher rates must use up first. The video does not give a single "worth it" number, because it depends on which kind of history comes next.
> 
> 3. Confusing passages
> - "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." This confused me at first because it sounds contradictory. The cushion explanation a few lines later resolves it.
> - "Each start month becomes one token, sorted into the bin under the half of history where it began." The "token" and "bin" language refers to visuals I can't see in a transcript, so it is vague.
> - "Leah's 7.5% is that rate plus a fixed 3.78 points" and "If history would push the index below zero, the replay stops it at zero" are dense technical detail for a general viewer.
> - "That's more than 1 in 4 for starts from 1954 to 1980 and about 1 in 30 from 1981 on" is stated before the era split is explained. "1 in 7" is a blend of the two, and that is not obvious.
> 
> 4. Attention drop
> Paragraph 7, from "Here's how the replay works. A real variable rate follows the lender's own index..." through "...the data is US only." It is a long run of method detail (stand-in index, 3.72%, zero floor, 753 start months, overlap caveats) with no new result for the viewer. The slider paragraph (many percentages in a row: 79%, 42%, 20.4%, 10.5%, $9,472, $6,033) is also dense, but I could follow it. The method paragraph is where I would drift.
> 
> 5. Does it tell me which loan to take or predict rates?
> No. It says outright "This is history, not a forecast" and "The line doesn't say which offer is better; it shows what each head start meant in each kind of history." It also says "Which kind of history comes next is something no replay can show." It lists what it leaves out (the real index, rate cap, grace period, fees, my budget). It gives a way to compare any offer against a historical line, not a recommendation.

**e9dcf3b1** · mẫu cand · vai T

> 1. Summary
> The video follows Leah, an illustrative new grad student who can no longer use Grad PLUS (ended July 1, 2026) and has two private offers on $50,000 over 10 years: 9% fixed, or a variable rate starting at 7.5%. It asks how much lower a variable rate has to start to be worth the risk. It replays her loan through every 10-year stretch of US rates since 1954 (753 start months, using 3-month T-bill rates as a stand-in index). It first resolves an apparent contradiction (the rate went above 9% in about 3 in 4 stretches, yet the variable loan cost more in only about 1 in 7), then walks through the worst case (April 1977), and then slides the starting gap from 3 points under to 1 over to show where the history changes.
> 
> 2. The video's answer
> It gives two answers, one per kind of history. For starts from 1981 on, no stretch cost more than the fixed loan once the head start reached 2 points. For starts from 1954-1980, even a 3-point head start left 10.5% of stretches costlier, with the worst $6,033 more. Leah's 1.5 points is short of the 2-point mark. At her offer, more than 1 in 4 of the 1954-80 starts and about 1 in 30 of the later ones cost more, and the worst case cost $11,219 more (43% more interest than the fixed loan's $26,005). With no head start, the variable loan cost more in 79% of the early starts and 42% of the later ones. Overall her loan cost more in about 1 in 7 stretches. The explanation is a "cushion" of early savings that later high rates have to use up before the variable loan costs more.
> 
> 3. Confusing passages
> - "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." I was confused until the cushion explanation came later. The answer arrives a paragraph after the puzzle.
> - "Measured the way this video measures it ... history gives two answers." I wanted one number, and this left me unsure what "worth it" means in practice.
> - "Leah's 7.5% is that rate plus a fixed 3.78 points." The "rate plus margin" idea is introduced very briefly. I wasn't sure whether my own offer would work this way.
> - The several percentages in the slider paragraph (79%, 42%, 20.4%, 10.5%) are hard to track with no visual in the transcript.
> - "the share that cost more never fell to zero, even where none of the 1981-on starts did." This is a double negative and takes work to parse.
> 
> 4. Attention drop
> The slider paragraph: "With no head start, both loans starting at 9%, the variable loan cost more in 79% of the 1954-to-1980 starts and 42% from 1981 on. The worst of those stretches cost $16,566 more. Leah's 1.5 points brings that to ... At 2 points ... 20.4% ... $9,472 ... At 3 points ... 10.5% ... $6,033." It is a dense run of near-identical numbers in spoken form. The setup paragraph about how the replay works (index, zero floor, no cap, 753 overlapping starts) also dragged a little.
> 
> 5. Does it tell me which loan to take or predict rates?
> No. It says "This is history, not a forecast" and "The line doesn't say which offer is better; it shows what each head start meant in each kind of history." It also says "Which kind of history comes next is something no replay can show." It also lists what it leaves out: the lender's real index, rate caps, grace periods, fees and my own budget. So I get a yardstick (compare my own head start to the 2-point and 3-point marks) but no recommendation and no rate prediction.

**7ff64c93** · mẫu cand · vai T

> 1. Summary
> The video follows Leah, an illustrative new grad student who can no longer use Grad PLUS (new borrowers after July 1, 2026) and has two private offers for $50,000 over 10 years: 9% fixed, or a variable rate starting at 7.5%. It asks how much lower a variable rate must start (the "head start") before the risk is worth it. It replays her loan through every 10-year stretch of US 3-month Treasury bill rates since 1954 (753 start months), first showing the puzzle that the rate rose above 9% in about 3 in 4 stretches yet cost more in total interest in only about 1 in 7. It then explains the "cushion" mechanism, shows the worst case (April 1977), and slides the head start from 3 points below to 1 point above the fixed rate to see where history changes.
> 
> 2. The video's answer
> "Worth it" is defined as how often the variable loan cost more total interest than the 9% fixed loan, and how much more at worst. History gives two answers. For starts from 1981 on, none cost more once the head start reached 2 points. For starts from 1954-1980, even 3 points left 10.5% of stretches costlier, the worst by $6,033. At Leah's 1.5 points: more than 1 in 4 (1954-1980 starts) and about 1 in 30 (1981 on) cost more, the worst by $11,219 (about 43% more interest than the fixed loan's $26,005). With no head start: 79% (1954-1980) and 42% (1981 on) cost more, worst $16,566. Bigger head start means fewer costlier stretches and a smaller worst case; it never reached zero for the 1954-1980 starts. So there is no single threshold; it depends on which kind of history comes next.
> 
> 3. Confusing passages
> - "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." Confusing at first because it sounds contradictory; it is resolved later by the cushion explanation, but I had to wait for that.
> - "Each start month becomes one token, sorted into the bin under the half of history where it began." The "token" and "bin" language refers to visuals I cannot see in narration, so it is unclear.
> - "Leah's 7.5% is that rate plus a fixed 3.78 points." Mildly confusing as to why the index matters to a real borrower; it is jargon-heavy.
> - "more than 1 in 4 ... about 1 in 30 ... 1 in 7" mixes fractions and percentages (79%, 20.4%, 10.5%), making comparisons hard.
> 
> 4. Where attention dropped
> Paragraph 7 ("Here's how the replay works..."): "Repayment starts right away, with no grace period, no fees and no rate cap. The replay adds up the interest... up to September 2016, the last start with a full 10 years of data." It is a dense methodology stretch with many numbers and caveats. The slider paragraph (15) also became a run of percentages and dollar figures that blurred together.
> 
> 5. Does it tell you which loan to take or predict rates?
> No. It says explicitly "This is history, not a forecast" and "The line doesn't say which offer is better; it shows what each head start meant in each kind of history." It also says which kind of history comes next cannot be shown by any replay, and notes that real offers have their own index, caps, grace periods, fees, and the borrower's own budget. It gives a way to compare an offer (head start vs. history), not a recommendation.

**a76103d3** · mẫu cand · vai T

> 1. Summary
> The video is about Leah, an illustrative new grad student who can no longer get Grad PLUS loans after July 1, 2026. She holds two private offers for $50,000 over 10 years: 9% fixed, or a variable rate that starts at 7.5%. The question is how much lower a variable rate must start (the "head start") for the risk to have been worth it. The video replays her loan through every 10-year stretch of US rates since 1954, using 3-month Treasury bills as a stand-in index. It counts how often the variable loan cost more in total interest than the fixed loan, and by how much at worst. It then slides the head start from 0 to 3 points to show how that changes. It stresses that this is history, not a forecast.
> 
> 2. The video's answer
> There is no single number, only two answers depending on which history you assume.
> - For starts from 1981 on, no stretch cost more once the head start reached 2 points.
> - For starts from 1954 to 1980, even a 3-point head start left 10.5% of stretches costlier, with the worst $6,033 more.
> - At Leah's 1.5 points, more than 1 in 4 of the 1954-1980 starts and about 1 in 30 of the later ones cost more. Overall about 1 in 7 cost more, and the worst (April 1977) cost $11,219 more, 43% on top of the fixed loan's $26,005 interest.
> - With no head start (both at 9%), the variable loan cost more in 79% of 1954-1980 starts and 42% of 1981-on starts, with the worst at $16,566 more.
> - A bigger head start means fewer costlier stretches and a smaller worst case.
> - The apparent contradiction: her rate rose above 9% in about 3 in 4 stretches, yet the loan cost more in only about 1 in 7. The early low-rate savings build a "cushion" on the biggest balance, and rates must rise early and stay high for years to use it up.
> 
> 3. Confusing passages
> - "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7. That's more than 1 in 4 for starts from 1954 to 1980 and about 1 in 30 from 1981 on..." It packs many fractions into a few sentences, and "that's" doesn't clearly say which figure it refers to.
> - "Each start month becomes one token, sorted into the bin under the half of history where it began." This is visual-chart jargon (tokens, bins) that I can't see in audio alone.
> - "Leah's 7.5% is that rate plus a fixed 3.78 points." I had to work out that this is a margin over the Treasury bill rate (3.72 + 3.78 = 7.5), and the video doesn't say that real lenders add a margin like this.
> - "Her payment reaches $863.36 a month..." Fine on its own, but the early "$593.51" first payment against "$633.38" arrives in a dense run of numbers.
> 
> 4. Where attention dropped
> Paragraph 7: "A real variable rate follows the lender's own index, and the replay needs a much longer record than that index has... If history would push the index below zero, the replay stops it at zero... Repayment starts right away, with no grace period, no fees and no rate cap... That's 753 starting months. The stretches overlap, so they are not 753 independent tries." This is a long methodology and caveat dump with no payoff for a borrower. The section of slider numbers in paragraph 15 (79%, 42%, 20.4%, 10.5%, $16,566, $9,472, $6,033) also blurs together when spoken.
> 
> 5. Does it tell me which loan to take or predict rates?
> No. It says outright "This is history, not a forecast," "Which kind of history comes next is something no replay can show," and "The line doesn't say which offer is better; it shows what each head start meant in each kind of history." It gives a way to compare an offer's head start with past outcomes. It leaves the choice and the rate outlook to me, and it notes that real offers have their own index, cap, grace period, fees and budget.

**21f56419** · mẫu cand · vai T

> 1. Summary
> The video follows Leah, an illustrative new grad student who can no longer use Grad PLUS after July 1, 2026. She holds two private offers on $50,000 over 10 years: 9% fixed, or a variable rate starting at 7.5%. The video asks how much lower a variable rate must start to be "worth it". It replays her loan through every 10-year stretch of US rates since 1954, using 3-month T-bill rates as a stand-in index. It then slides the starting gap (the "head start") from 3 points under the fixed rate to 1 point over, and reports how often, and by how much, the variable loan cost more.
> 
> 2. The answer
> It gives two answers, depending on which history repeats.
> - Starts from 1981 on: none cost more once the head start reached 2 points.
> - Starts from 1954 to 1980: even 3 points left 10.5% of stretches costlier, with the worst $6,033 more.
> - Leah's 1.5 points falls short. More than 1 in 4 of the 1954-1980 starts and about 1 in 30 of the later starts cost more. The worst case is $11,219 more, in April 1977, a 43% increase in interest.
> - With no head start, 79% of the 1954-1980 starts and 42% of later starts cost more. A bigger head start meant fewer costly stretches and a smaller worst case.
> - For 1954-1980 starts, the share that cost more never reached zero at any head start tested.
> 
> 3. Confusing passages
> - "Leah's variable rate rose above 9% at some point in about 3 in 4 stretches. Yet it cost more in total interest in about 1 in 7." I had to wait for the cushion explanation in paragraph 9 to see why this isn't a contradiction.
> - "Each start month becomes one token, sorted into the bin under the half of history where it began." "Token" and "bin" are visual jargon that I can't picture from the narration alone.
> - "Leah's 7.5% is that rate plus a fixed 3.78 points." The spread idea is introduced quickly and without explanation.
> - "more than 1 in 4 ... about 1 in 30" is repeated several times with the split between periods, which was a lot to track by ear. "Head start" is also a coined term, though it is defined.
> 
> 4. Attention drop
> The methodology paragraph: "A real variable rate follows the lender's own index, and the replay needs a much longer record ... Repayment starts right away, with no grace period, no fees and no rate cap ... That's 753 starting months. The stretches overlap, so they are not 753 independent tries..." It is dense with setup and caveats. The T-bill stand-in, zero floor, start months and overlap caveat arrive back to back, with little payoff for a borrower. The run of percentages and dollar figures at the 0, 1.5, 2 and 3 point stops (paragraph 15) was also heavy.
> 
> 5. Does it tell me which loan to take or predict rates?
> No. It says explicitly "This is history, not a forecast" and "The line doesn't say which offer is better; it shows what each head start meant in each kind of history." It says which kind of history comes next can't be shown. It lists what real offers add that the replay omits: the lender's real index, rate cap, grace period, fees and the borrower's budget. It gives a benchmark to compare an offer against, but not a recommendation.

**f8f090e5** · mẫu weak · vai T

> 1. Summary
> The video follows Maya, who took a $375,000 mortgage in October 2023 at the 30-year rate peak (7.62%), and asks when the roughly $5,124 cost of refinancing pays for itself now that the average rate is 7.03%. It compares her with Dan (a $115,000 loan) and Priya (a $1,005,000 loan) to show that loan size changes the answer. It then shows that the usual calculator method (closing costs divided by monthly savings) understates the time, because refinancing restarts a 30-year schedule and leaves a higher balance. Finally it tests this against all 13 drops of 1 point or more in the 30-year rate since 1971, and ends with limits and a method note.
> 
> 2. The answer
> Counting both the monthly savings and the extra balance still owed, a refinance like Maya's (a 35-payment-old loan) pays back within 36 months if the rate falls about 0.5 points. Dan, with a small loan, would need 1.12 points, and Priya, with a large loan, only 0.2. Today's cut is 0.59 points. For Maya, the calculator says 24 months, but the balance-aware answer is 30 months. She is ahead if she keeps the house past that and behind if she sells before it. Her gain is $1,039 after 3 years and $8,093 after 7. In the historical drops, break-even took 10 to 20 months for young loans. The answer depends on the size of the cut, the loan size, the loan's age and how long the house is kept.
> 
> 3. Confusing passages
> - "A drop counts when the monthly average falls at least 1 point from a peak before rising 1 point from its low." This is hard to follow when spoken. It is unclear how peaks and lows are paired.
> - "Counting what she still owes, break-even is not 24 months. It is 30." and "Priya saves $593 a month, and is even after 11 months." I had to work out why the balance difference matters, and the video does not explain it simply.
> - "In 3 of those drops, the rate fell another 1 point before the first refinance had paid for itself... In the other 10, the first refinance was the one that mattered." The 1984 example ("needed 19 months... next drop came 7 months later") is dense with dates. I could not tell whether the second refinance was recommended or just noted.
> - "The biggest fall began after the peak of 18.63% in 1981. A refinance 2 months later paid back in 13 months." The 1981 rate is so far from today's that I could not tell how it applies to me.
> - "Below 0.5 points, the fresh start can swallow the savings entirely" and "Maya never catches up" at 0.25 points. This was surprising, and the reason was only briefly stated.
> 
> 4. Where my attention dropped
> The long run of numbers in the historical section, starting at "We found every fall of at least 1 point in the 30-year rate since 1971: 13 of them" and running through "...the next drop of 1 point came 7 months later." The video lists many ranges (10 to 20, 10 to 21, 18 to 39 months, 6 months) and dates, with little to anchor them. Another low point was the closing "Method" paragraph, which is a fast list of sources and definitions. The Dan and Priya dollar figures ($1,777 behind, $386 ahead, $11,482, $30,387) also blur together.
> 
> 5. Does it tell me which loan to take or predict rates?
> No. It says outright that the rates are "history, not a forecast" and that "nothing here says where rates go next". It gives no recommendation to refinance or not. It offers a framework of three questions (how big the cut, how old the loan, how long the stay) and shows break-even results. It also lists its limits: it ignores taxes and the return on cash, assumes costs are paid up front, and uses medians.
> 
> Caveat for my situation: the video is about refinancing a mortgage. It says nothing about graduate-school private loans beyond the federal limit, so I could only borrow the general lesson of weighing an upfront cost against savings over time.

**22ad856c** · mẫu weak · vai T

> 1. Summary
> The video follows Maya, who borrowed $375,000 in October 2023 at 7.62% and is weighing a refinance that costs the median $5,124 in closing costs. It also follows two other borrowers, Dan ($115,000) and Priya ($1,005,000). It asks when a refinance pays for itself. It first shows the usual calculator answer, which divides the closing costs by the monthly saving and gives 24 months for Maya. It then corrects that figure by counting the extra balance still owed on a fresh 30-year loan, which gives 30 months. It then checks the 13 historical rate drops of at least 1 point since 1971 and works out how big a rate cut each borrower needs.
> 
> 2. The video's answer
> Simple division understates the real break-even time, because a refinance restarts the loan and leaves a higher balance. For a loan like Maya's, counted by what is still owed, a cut of 0.5 points pays back within 36 months. Dan needs 1.12 points and Priya needs 0.2. Today's cut is 0.59 points, so Maya is ahead after 30 months and behind if she sells before then. Maya is $1,039 ahead after 3 years and $8,093 ahead after 7. Dan is $1,777 behind after 3 years and $386 ahead after 7. Priya is ahead by $11,482 after 3 years and $30,387 after 7. The takeaway is that three things decide the outcome: how big the cut is, how old the loan is, and how long you stay. A cut below 0.5 points can be swallowed entirely by the fresh start.
> 
> 3. Confusing passages
> - "Below 0.5 points, the fresh start can swallow the savings entirely." It is not obvious what "the fresh start" means until you work out that it means restarting the 30-year amortization.
> - "A drop counts when the monthly average falls at least 1 point from a peak before rising 1 point from its low." This is dense and hard to follow by ear.
> - "In 3 of those drops, the rate fell another 1 point before the first refinance had paid for itself... In the other 10, the first refinance was the one that mattered." It then gives July 1984 as an example with 19 and 7 months, which is a lot of numbers to track at once.
> - "Counting the balance, Maya never catches up before her old loan would have been paid off" at 0.25 points. This sits right beside the "38 months" figure, and the two are hard to reconcile at first.
> - "Maya's own drop began in October 2023. A cut of 1 point first arrived in August 2024." It is unclear why this matters when her current cut is 0.59.
> 
> 4. Where attention dropped most
> The historical section: "We found every fall of at least 1 point in the 30-year rate since 1971: 13 of them... The biggest fall began after the peak of 18.63% in 1981. A refinance 2 months later paid back in 13 months..." It is a stream of dates, ranges and percentages from eras that feel unrelated to my own loan. The method paragraph near the end ("Rates are Freddie Mac's weekly survey via FRED... HMDA loan-level data...") also dragged, though it reads as reference material.
> 
> 5. Does it tell you which loan to take or predict rates?
> No. It says explicitly that "The rates here are history, not a forecast" and "nothing here says where rates go next". It gives no lender or product recommendation. It only gives a framework of cut size, loan age and how long you stay, plus break-even figures for three example borrowers. It also covers only refinancing a mortgage. It says nothing about graduate student loans or private loan choices, so it does not address my situation directly beyond the general idea of weighing an up-front cost against savings.

**9f3f7fe9** · mẫu weak · vai T

> 1. Summary
> The video is about Maya, a borrower who took a $375,000 30-year mortgage in October 2023 at 7.62%, and about two other borrowers, Dan ($115,000) and Priya ($1,005,000). They are all weighing a refinance now that the average rate is 7.03%. The problem is when the $5,124 median closing cost is paid back. The video starts with the simple calculation (bill divided by monthly saving) and then adds the balance still owed on a fresh 30-year loan. It then tests the question against 13 historical rate drops since 1971 and ends with how big a rate cut each borrower needs.
> 
> 2. The answer
> Counting both the monthly savings and the larger balance still owed on the new loan, a refinance like Maya's pays back within 36 months if the rate falls about 0.5 points. Dan, with a small loan, needs 1.12 points, and Priya, with a large loan, needs 0.2.
> - Today's cut is 0.59 points. For Maya, the simple division says 24 months, but the balance-aware break-even is 30 months. She is behind if she sells before then.
> - Dan's break-even is 75 months, not 55. Priya's is about 11 months.
> - Cuts under 0.5 points can be wiped out by the fresh-start effect.
> - The answer depends on the cut, the loan size, how old the loan is, and how long the borrower keeps the house.
> 
> 3. Confusing passages
> - "Below 0.5 points, the fresh start can swallow the savings entirely." and "At a cut of 0.25 points, ... Maya never catches up before her old loan would have been paid off." The "fresh start" and "balance" ideas are explained quickly, so I had to infer that restarting the 30-year clock slows principal paydown.
> - "Counting what was still owed, break-even took between 10 and 20 months. The simple division would have said between 10 and 21." This is confusing because the two methods barely differ, and the video explains why only afterwards.
> - "A drop counts when the monthly average falls at least 1 point from a peak before rising 1 point from its low." This is dense and hard to follow by ear.
> - The mix of "ahead after 30 months" and "$1,039 ahead after 3 years" is hard to hold together. A 3-year stay is 36 months, past the 30-month break-even, but it is not stated that these are the same calculation.
> 
> 4. Where attention dropped
> The historical section: "We found every fall of at least 1 point in the 30-year rate since 1971: 13 of them... In the drop that began in July 1984, the refinance came in November 1984. It needed 19 months to pay back, and the next drop of 1 point came 7 months later." It is a run of dates and month counts for situations unlike mine (rates of 18%, 1980s). That makes it feel less relevant to a graduate student with loans, and the numbers are hard to keep track of.
> 
> 5. Does it tell me which loan to take or predict rates?
> No. It says explicitly that "The rates here are history, not a forecast" and "nothing here says where rates go next." It also covers only a mortgage refinance, not a graduate or private student loan. It gives a framework (size of the cut, age of the loan, length of stay) and leaves the decision to the viewer. It is not about private student loans at all, so as a grad-school borrower I could only reuse the general idea that upfront costs, the fresh-start effect and time horizon matter.

