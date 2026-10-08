# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
Ba ý: (b) quyết định là chọn giữa **khoản niên kim đều (lớn hơn, không đổi)** và **khoản nhỏ hơn tăng 2 % mỗi năm**, xét theo **sức mua / theo kịp giá cả**; (c) trả lời bằng **lịch sử giá tiêu dùng thật của Mỹ** (chỉ số giá), thử trên **mọi / nhiều quãng 20 năm** từ cuối thập niên 1940; (d) đáp án là **khoản tăng 2 % giữ được bao nhiêu sức mua / bao lâu thì theo kịp** (mức thường gặp và trường hợp xấu), để người xem tự hiểu "tăng 2 %" bảo vệ tới đâu. Đủ ba → 1; đủ hai → 0,5; ≤ một → 0.
**Cờ `overclaim`** (báo riêng, không tính ngưỡng): người đọc kể thành "video bảo chọn khoản nào / niên kim nào tốt hơn" / "video dự báo lạm phát" / "2 % là lựa chọn tồi".
**Câu khuyên:** `advice: true` khi câu 4 "yes" vì tin video sẽ bảo chọn khoản nào hoặc dự báo lạm phát, **hoặc** câu 5 nêu lời khuyên hành động (chọn khoản đều, chọn khoản tăng, mua niên kim gắn CPI…). Câu 5 kiểu "đừng coi 2 % là được bảo vệ hoàn toàn / hiểu giới hạn của khoản tăng" là hiểu lời hứa, **không** tính. Người đọc **đúng** = điểm 1 và không câu khuyên.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "overclaim": true|false, "why": "<one line>"}, ...}

### R1
1. The video is for people around 65 weighing an annuity, and it looks at a choice between a larger fixed check and a smaller one that rises 2% a year. It answers by replaying every 20-year stretch of US consumer prices since 1947 to see how much buying power the rising check kept: how often it kept up, in a typical stretch, and in the worst one.

2. By the end I expect to know how often, historically, a 2%-a-year raise matched rising prices over 20 years, and how big the shortfall was in a typical case and the worst case.

3. Nothing. The one phrase that could be a little loose is "kept up," since it isn't defined, but the surrounding text makes the meaning clear enough (the check's buying power holding steady).

4. No. The description says outright that it is "history, not a forecast," and that it "won't tell you which check to pick or what inflation will do." It limits itself to measuring past outcomes.

5. Little direct advice. A viewer might take away that a 2% raise shouldn't be assumed to keep pace with prices, and that they should check the historical record before relying on that assumption. The choice itself is left to them, and the national price index may not match their own spending.

### R2
1. The video is for people around retirement age who are weighing an income annuity: a larger flat monthly check versus a smaller one that rises 2% a year. It asks whether a 2% annual raise really keeps up with prices. To answer, it replays every 20-year stretch of US consumer prices since 1947 and measures how much buying power the rising check kept, looking at how often it kept up, a typical stretch, and the worst one.

2. I expect to know how well a 2%-a-year raise has preserved buying power over past 20-year periods, including how often it held up and how badly it did at worst.

3. Nothing. One small point: "kept up" isn't defined precisely (fully matched prices versus roughly matched), but the context makes the meaning clear enough.

4. No. The description says outright that it is history, not a forecast, and that it won't tell you which check to pick or what inflation will do. It also notes the price index is a national average, not any one retiree's own spending.

5. Probably no direct advice to choose one option. A viewer would take away a better-informed view of the assumption that 2% roughly keeps up with inflation, using historical evidence about how often it held and how badly it failed. They would still have to weigh that against their own situation, spending, and other income, and could use it as a prompt for questions to ask when comparing the quote.

### R3
1. This video is for someone like me, about to retire, who is weighing an income annuity with a flat payment against a smaller one that rises 2% a year. It takes a woman who retired at 65 in August 2006 and chose the rising check, then tests that 2% raise against every 20-year stretch of US consumer prices since 1947. It counts how often the raise kept up with prices, how much buying power it usually kept, and why her own stretch ended below where it started.

2. I expect to know how often, in past history, a 2% annual raise preserved buying power over 20 years, and by how much.

3. Nothing is really confusing. The one phrase I'd want explained is "ended below where it started," since it's not clear whether that means her buying power dropped after 15 years or by year 20. I'd also note that "kept up with prices" for 15 years but then fell short is a slightly surprising setup, but the video seems to promise an explanation.

4. No. The description says outright that it is "History, not a forecast" and that it "won't tell you which check to choose." It only looks at what happened in past 20-year periods, so it neither recommends a payout option nor predicts future inflation.

5. A viewer would take no direct advice on which check to pick. What they could take is a better sense of how a fixed 2% raise has held up against actual price changes historically, including the risk that it falls short in some stretches. They would still need to weigh that against their own spending, health, other income, and how much smaller the starting check is. The national average caveat also tells them their own costs might differ.

### R4
1. The video is for someone choosing between a pension-style annuity that pays a smaller check rising 2% a year and a larger check that stays flat. It looks at whether the 2% raise actually protects buying power. It does this by testing the raise against every 20-year stretch of US consumer prices since 1947, and by following one retiree who started in August 2006.

2. By the end I'd know how often, and by how much, a 2% annual raise kept up with US consumer prices over 20-year periods, and why the 2006 retiree's stretch ended below where it started.

3. Nothing is badly confusing, but two phrases are loose. "Why her stretch ended below where it started" is unclear: it doesn't say whether "below" means buying power, and a 20-year test applied to someone who has had about 15 years might need explaining. Also, "how much it usually kept" is vague about whether that means a share of the original buying power or a dollar amount.

4. No. The description says outright that it is "history, not a forecast" and that it "won't tell you which check to choose," so it neither recommends a check nor predicts future inflation.

5. Little direct advice. A viewer might take away that a fixed 2% raise has not always matched real inflation, and that the answer depends on when you retire and on your own spending. They would still need to weigh the choice against their own situation, since the price index is a national average and not their own shopping basket.

### R5
1. This video is for people about to retire, around 65, who are weighing an income annuity that pays either a larger fixed check or a smaller one that grows 2% a year. It looks at whether that 2% raise really keeps up with rising prices. To answer, it replays every 20-year stretch of US consumer prices since 1947 and measures how much buying power the growing check kept.

2. By the end I expect to know how often, in a typical stretch, and in the worst case, a 2%-a-year raise preserved buying power over 20 years of past US inflation.

3. Nothing is really confusing. The one phrase I'd want unpacked is "how much buying power the rising check really kept," since I'd want to know whether that's shown as a percentage or in dollars, but the meaning is clear enough from context.

4. No. The description says outright that it's "History, not a forecast," so it won't predict inflation, and that it "won't tell you which check to pick," so it won't make the choice for me.

5. Little direct advice, since it says it won't pick for me. A viewer would likely take away that they shouldn't assume a 2% raise automatically keeps pace with prices, and that they should check how it held up historically, while remembering that their own spending may differ from the national average and the future may differ from the past.

### R6
1. This video is for someone near retirement, like a 64-year-old weighing an income annuity, who must pick between a smaller check that rises 2% a year and a larger flat check. It looks at whether that 2% raise has actually kept up with prices. It answers by testing the raise against every 20-year stretch of US consumer prices since 1947, counting how often it held buying power and by how much, and examining why one retiree's stretch (starting August 2006) ended below where it began.

2. I expect to know how often, historically, a 2% annual raise preserved purchasing power over 20 years, and how much it typically preserved.

3. Nothing is truly confusing. The one phrase I'd pause on is "why her stretch ended below where it started," since it's not obvious whether "ended" means a stretch cut off before 20 years, and "below where it started" doesn't say below in what terms (buying power, presumably). Also, "She" appears without being introduced beyond "a retiree," but that's minor.

4. No. The description says outright that it is "History, not a forecast" and that it "won't tell you which check to choose." It looks backward at past price data, so it neither recommends an option nor predicts future inflation.

5. Little direct advice. A viewer might take away that a 2% raise has a track record they can check against history, and that outcomes depend on the inflation of the particular stretch, so it's worth being cautious about assuming it will keep up. They'd also note that a national average may not match their own spending. The actual choice stays with them, likely alongside their own situation and possibly a professional's input.
