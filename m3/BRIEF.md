# M3 — đầu bài chung (giống hệt cho bên máy và bên đối chứng)

Khối "BRIEF" dưới đây được đưa **nguyên văn** cho cả hai bên. Bên đối chứng (GPT-5.5) chỉ nhận khối này và vai "10 phút, không tra cứu". Bên máy nhận khối này và phải tự mang dữ liệu (DESIGN.md §"Hồ sơ luận điểm máy").

```BRIEF
Channel: a US personal-finance YouTube channel in the data-explainer genre, 8-15 minute episodes, faceless. Positioning: "a lab for financial decisions" - each episode answers one concrete financial decision with a full simulation on real data, with sources and methods shown. US only. The channel never gives personal advice and never forecasts markets; when it uses historical data it says "history, not a forecast".

Pillar for this request: {pillar}

Task: propose {n} distinct theses for episodes in this pillar. A thesis is a specific, checkable claim that a viewer facing a real decision would care about, and that overturns a common belief.

Write each thesis as a card with exactly two fields:
- thesis: one sentence, 20 to 28 words.
- overturns: the common belief it contradicts, one sentence in double quotes, 10 to 16 words.

Card rules (strict, checked by machine):
- No digits, no % or $ signs, no years.
- No numbers written as words (for example one, two, ten, hundred, half, double, twice, triple, quarter, third, dozen, percent).
- No names of data sources, datasets, series codes, laws, acts or code sections (write "workplace retirement plan", not a plan's code name).
- One sentence per field.
```

Tên trụ (tiếng Anh, điền vào `{pillar}`):
- `debt` → "Borrowing and debt (mortgages, refinancing, student loans, auto loans, credit cards, paying down debt)"
- `retire` → "Retirement and long-term investing (saving for retirement, retirement accounts, Social Security timing, long-horizon investing through history)"
- `tax` → "Taxes and policy (federal tax rules, tax-advantaged accounts, credits and deductions, the measurable impact of policy on households)"

Phân bổ (chủ dự án duyệt 2026-09-30): debt 7 · retire 7 · tax 6.
