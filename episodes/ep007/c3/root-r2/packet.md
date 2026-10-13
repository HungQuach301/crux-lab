# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" chép **nguyên văn** từ `beats.md` (`spans.json`). **Cờ khuyên theo rubric MỚI** (G1 câu 2, như Tập 6 C4): `advice_stated` (chính hình/chữ trên hình nêu/ngụ ý hành động: chọn 15/30 năm, trả thêm, đầu tư, trả tháng/năm, chờ/khoá lãi) → **trượt**; `advice_inferred` / `caution_only` chỉ báo, câu trích vào bảng. Người đọc đúng = nghĩa 1 và `advice_stated` false.


Muted read (đáp án đúng) theo hình:
- N1-s06-stack: The 30-year bar is raised to finish in 15 years and ends just above the 15-year bar; the sliver above becomes bills that drop onto the stack, month after month, until it stands at its full height.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, "quote": "<reader words behind any flag, else empty>", "why": "<one line>"}, ...}

### R1 (strip N1-s06-stack)
1. **The idea.** The animation compares a 15-year mortgage with a 30-year mortgage for a character called Tessa. It labels itself "ILLUSTRATIVE" and "US only · history, not a forecast," and it cites the Freddie Mac weekly mortgage survey. It shows that a 30-year loan paid off in 15 years takes a bit more per month than a true 15-year loan. The extra money adds up to a stack of gold.

2. **What changes over time.**
   - Frame 1 shows Tessa, a house, and two blank bars.
   - Frame 2 labels the bars. The 15-year bar is "$2,828 a month" and the 30-year bar is "required: $2,216 a month."
   - Frame 3 raises the 30-year bar by a gold slice, "+$120 a month." The label reads "30-year paid in 15: $2,948 a month."
   - Frames 4 and 5 show the gold slices dropping off and building into a stack beside the house.
   - Frame 6 shows the full stack, labeled "the stack: $21,622 extra paid over 15 years."

3. **What it means.** Paying the 30-year loan at a 15-year pace costs $2,948 a month. That is $120 more than the $2,828 for the 15-year loan. Over 15 years, the $120 a month totals $21,622 of extra payments. The animation doesn't say why the amounts differ. A likely reason is the 30-year loan's higher interest rate, but that is my inference. The animation also doesn't say whether the $21,622 is extra interest or something else.

4. **Advice a viewer might take.** The animation gives no direct advice. A viewer might infer that a true 15-year loan costs less overall than a 30-year loan paid off early. They might also infer that the 30-year loan's lower required payment ($2,216) offers flexibility. Neither point is stated.

5. **Source of the conclusion.** The advice in 4 is my own conclusion. The animation shows only the numbers and the labels "illustrative" and "history, not a forecast." It never tells the viewer to choose one loan or to pay extra rather than invest. It also doesn't address your question about investing the spare cash.

### R2 (strip N1-s06-stack)
1. **The idea:** The animation compares two ways to pay off a home loan in 15 years. One is a 15-year mortgage. The other is a 30-year mortgage where the borrower pays extra each month so it's paid off in 15 years. A character named Tessa, labeled "illustrative," stands in for the borrower. The label "Freddie Mac weekly mortgage survey" suggests the rates come from that survey.

2. **What changes across the frames:**
   - Frame 1 shows Tessa, a house, and two blank bars.
   - Frame 2 labels the bars. The 15-year bar is $2,828 a month. The 30-year bar says "required: $2,216 a month."
   - Frame 3 adds a small gold "+$120 a month" slice on top of the 30-year bar. It is captioned "30-year paid in 15: $2,948 a month."
   - Frames 4 and 5 show gold pieces coming off the 30-year bar and building a gold stack next to the house.
   - Frame 6 shows the finished stack, labeled "the stack: $21,622 extra paid over 15 years."

3. **What it means:** A 30-year loan paid off in 15 years costs $120 more each month than a true 15-year loan ($2,948 against $2,828). Over 15 years that adds up to about $21,622 extra paid. The 30-year loan's rate is evidently higher than the 15-year rate, so the same payoff date costs more. The animation doesn't say that outright. The gold stack is the cost of choosing the 30-year loan and prepaying it.

4. **Advice a viewer might take:** The animation gives no explicit advice. A viewer might infer that if they're sure they'll pay off in 15 years, a true 15-year loan is cheaper than a 30-year loan with extra payments. The 30-year loan's lower required payment ($2,216) is the flexibility you'd be paying for. The frames don't address investing the spare cash instead. They also include the caveat "US only · history, not a forecast."

5. **Where the conclusion came from:** The numbers and the gold stack come from the animation. The advice is my own inference. The animation shows the cost comparison but never tells the viewer what to do.
