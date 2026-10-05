# C6 — tóm tắt AI (chấm độc lập, mù tập)

**v2 (bản cuối `103ff99e…`) ở dưới cùng; v1 chấm trên bản render 1 `41212734…` (trước các sửa C5 — nhận xét "some text overlaps" thuộc bản đó).**

## v1 — bản `41212734…`

Một agent mới (sonnet), không ngữ cảnh dự án, chỉ mở `narration.txt` (lời bản cuối, có mốc giờ) và một tờ khung hình (1 khung / 24 s của bản xem 720p). L2/L3 tham khảo — không thay chủ dự án (quality-framework §2.6). Nguyên văn:

> (a) Dana, a 40-something saver, must choose for 20-year money between rolling 3-month T-bills and a Series EE bond guaranteed to double. The video replays 873 historical 20-year rolls since 1934 and finds the roll beat double 52.3% of the time, but 93.1% for starts 1950-1989 and 5.0% since 1990. It ends by giving a break-even line (bill rate averaging about 3.47%) and declining to pick a side.
>
> (b) Honestly, little actionable advice, and that is deliberate. The most advice-like lines: "That is not a reason to pick either path", "The line doesn't say which to pick; it says what the roll has to do to beat the promise", "History doesn't choose for her", "US only, and history, not a forecast." A viewer might loosely take away "today's bill rate isn't a guide" and "double is in dollars, not buying power". Nobody leaves knowing what to do.
>
> (c)
> 1 Hook: 2. Dana's setup is gentle, with no stakes or tension beyond "which path?".
> 2 Story: 3. Clear setting, person and question, with a tidy answer, but Dana vanishes for six minutes and the answer is "it depends".
> 3 Pictures: 4. Dot-histograms, era colors, the doubling gate and the buying-power bar carry meaning. The same frame repeats for long stretches, and some text overlaps.
> 4 Pacing: 3. The opening is slow and caveat-heavy. I would skip 0:42-1:16 and 2:36-3:07, and the 6:10-7:00 inflation block. Late stats come densely.
> 6 Next episode: 3. Rigorous and trustworthy, but dry.
>
> (d)
> - 2:42-2:57: "bill rates quoted on a scale where the doubling line sits a little lower" and why 3.72% can't be compared with the bond.
> - 5:31-5:55: "average bill rate ended below the rate in the starting month 87.6%". The chart is hard to read and the link to the outcome is indirect.
> - 7:06-7:55: 3.42% average versus the 3.47% line, and the rule that "matched the result in every one" of the 873 starts. It is unclear whether the line is a rate, a forecast or a test. The 17 "real" rolls versus the "pretend" ones (1:04, 5:02) also muddle the headline stat.


## v2 — bản cuối `103ff99e…` (agent mới, cùng lời giao, cùng 2 file đầu vào dựng từ bản cuối)

> (a) Dana has 20-year money in 3-month T-bills and weighs a Series EE bond guaranteed to double in 20 years. The video replays 873 historical 20-year bill rolls (1934-2006) and finds the roll beat double 52.3% of the time: 0% for 1934-49, 93.1% for 1950-89, 5.0% for 1990 on. It ends by saying history can't choose for her, and that the bill rate has to average about 3.47% to beat the bond.
>
> (b) A viewer would take away little actionable advice, and the video says so: "That is not a reason to pick either path" and "History doesn't choose for her." The nearest thing to a rule is "the bill rate averages above that line over all 80 bills." The forecast disclaimers are explicit: "Nobody can say where that average will land" and "US only, and history, not a forecast." A viewer probably leaves thinking "it depends on rates, nobody knows."
>
> (c)
> 1 Emotional hook: 2. Dana is a thin, generic figure and the stakes are never felt.
> 2 Story: 3. The setting, problem and answer are all there, but Dana is a framing device and the journey is a stats readout.
> 3 Pictures: 3. The bars, histogram and era split are clear and consistent. The 1966 purchasing-power and path-of-rates charts need the narration to make sense.
> 4 Pacing: 3. It is steady but dense. I'd skip 1:56-2:49 (rate-measurement caveats) and 7:55-8:16.
> 6 Next episode: 2. It is rigorous and honest, but dry.
>
> (d)
> - 0:42-1:04: "pretend" guarantee before May 2005. It's unclear which results are real and which are what-if.
> - 2:42-2:57: rates "measured differently" and the "discount basis" scale. It's abstract, and 3.72% versus 3.47% looks contradictory.
> - 5:31-5:55: "average ended below the first month" over the next 20 years. The overlaid line chart is hard to read and the logic is opaque.
