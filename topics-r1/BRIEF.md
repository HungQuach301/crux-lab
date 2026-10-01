# topics-r1 — đầu bài chung (giống hệt cho bên máy và bên đối chứng)

Thẩm quyền: `decisions/D-004.md`. Khối "BRIEF" dưới đây được đưa **nguyên văn** cho cả hai bên (thay `{pillar}` và `{n}`). Bên đối chứng (GPT-5.5) chỉ nhận khối này và vai "không tra cứu". Bên máy nhận khối này **cộng** phần dữ liệu ở `topics-r1/DESIGN.md` §"Bên máy" — đó là phần khác duy nhất.

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
