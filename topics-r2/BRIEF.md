# topics-r2 — đầu bài chung (giống hệt cho bên máy và bên đối chứng)

Thẩm quyền: `decisions/D-004.md`. Khối "BRIEF" dưới đây được đưa **nguyên văn** cho cả hai bên (thay `{pillar}` và `{n}`). Bên đối chứng (GPT-5.5) chỉ nhận khối này và vai "không tra cứu". Bên máy nhận khối này **cộng** phần dữ liệu ở `topics-r2/DESIGN.md` §"Bên máy" — đó là phần khác duy nhất.

```BRIEF
Channel: a US personal-finance YouTube channel in the data-explainer genre, 8-15 minute episodes, faceless. Positioning: "a lab for financial decisions" - each episode answers one concrete financial decision with a full simulation on real data, with sources and methods shown. US only. The channel never gives personal advice and never forecasts markets or rates; when it uses historical data it says "history, not a forecast".

Pillar for this request: {pillar}

Task: propose {n} distinct episode topics in this pillar. Start from a decision that a specific group of viewers is facing, not from a statistic. A good topic is one where the answer could change what that viewer decides, or differs from what they would guess.

Write each topic as a card with exactly five fields:
- viewer: who the episode is for, in terms the viewer would recognize as "people like me"; one sentence, at most 25 words.
- decision: the yes/no or A-versus-B decision that viewer faces; one question ending with a question mark, at most 20 words.
- promise: what the episode promises to answer, without giving away the answer; one sentence, at most 25 words.
- title: the YouTube title, at most 60 characters including spaces.
- thumbnail: one line: the main object in the image (at most 12 words), then " / ", then the on-image text in double quotes (at most 4 words).

Card rules (strict, checked by machine):
- Numbers that identify the viewer are allowed only in viewer and decision: for example a year, the rate they pay or are offered, a loan term, an age, a loan or balance size, an income level.
- promise, title and thumbnail may only repeat numbers that already appear in viewer or decision. No other numbers anywhere, in digits or in words (for example one, two, ten, half, double, twice, third, dozen, percent): no results such as savings, break-even points, shares of people or percentages of outcomes.
- viewer and decision must not state a result (no "saves", "loses", "break even", "comes out ahead" next to a number).
- No names of data sources, datasets, agencies, series codes, laws, acts, bills or code sections. Common account names are allowed: 401(k), 403(b), 457(b), IRA, Roth IRA, HSA, 529 plan.
- The promise answers a question with data; it does not tell the viewer what to do and does not predict markets or rates.
- One sentence per field.
```

Tên trụ (tiếng Anh, điền vào `{pillar}`) — giữ như M3:
- `debt` → "Borrowing and debt (mortgages, refinancing, student loans, auto loans, credit cards, paying down debt)"
- `retire` → "Retirement and long-term investing (saving for retirement, retirement accounts, Social Security timing, long-horizon investing through history)"
- `tax` → "Taxes and policy (federal tax rules, tax-advantaged accounts, credits and deductions, the measurable impact of policy on households)"

Phân bổ (D-004): máy 4/trụ (12), đối chứng 2/trụ (6).

## Khối loại trùng (vòng 2; đưa nguyên văn cho cả hai bên, nối sau khối BRIEF)

Chủ dự án yêu cầu thẻ vòng 2 là đề tài **mới**: không trùng `topics/queue.md`, 6 thẻ đối chứng vòng 1, và đề tài Tập 1 (bài học M3v2 R2). Khối dưới không đổi luật thẻ, chỉ liệt kê quyết định đã dùng; áp như nhau cho hai bên. Thẻ trùng (cùng lõi quyết định) bị loại trước khi đóng băng; bên đối chứng gọi lại theo luật sai khuôn.

```EXCLUDE
Already covered - do not propose a topic whose core decision is the same as any of these (all pillars):
- Whether to refinance a mortgage taken at a high rate, and how big a rate cut makes refinancing pay back its costs.
- Take a 7.5% variable rate or lock in 9% fixed for a 10-year payoff?
- Work those 8 hours as overtime at $48 an hour, or at a second job paying $48 an hour?
- Sell the house we bought in 2000 now, or keep it, given the $500,000 tax-free limit on home-sale gains?
- Keep over-withholding for a $3,000 refund, or adjust withholding for bigger paychecks instead?
- Take the 72-month loan for the lower payment, or stick with 60 months?
- Is the 3% compound inflation option enough, or is the pricier 5% option worth paying for?
- Should I lock money in savings bonds that double in 20 years, or keep rolling T-bills instead?
- Sell now at the short-term tax rate, or wait a month for the lower long-term rate?
- Pay one point to cut my rate from 7% to 6.75%, or skip it?
- When a 1-year CD pays more than a 5-year CD, should I keep rolling the 1-year or lock the 5-year?
- Should my spare $500 a month go toward the 3% mortgage or into T-bills?
- At 65, should I take the bigger level annuity check or the smaller check that rises 2% a year?
- Refinance the 7% mortgage to 6.5%, or keep the loan?
- Take the 0% transfer with a 4% fee, or stay on the old card?
- Should you pause 401(k) contributions beyond the match to pay cards faster?
- Should you claim Social Security early or wait?
- Should you spend 529 money before claiming a college tax credit?
- Should you make pre-tax Solo 401(k) contributions instead of Roth contributions?
```

