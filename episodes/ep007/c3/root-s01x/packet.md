# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" chép **nguyên văn** từ `beats.md` (`spans.json`). **Cờ khuyên theo rubric MỚI** (G1 câu 2, như Tập 6 C4): `advice_stated` (chính hình/chữ trên hình nêu/ngụ ý hành động: chọn 15/30 năm, trả thêm, đầu tư, trả tháng/năm, chờ/khoá lãi) → **trượt**; `advice_inferred` / `caution_only` chỉ báo, câu trích vào bảng. Người đọc đúng = nghĩa 1 và `advice_stated` false.


Muted read (đáp án đúng) theo hình:
- N1-s01-stack: A faceless figure by her house; a thin stack of bills appears beside the house and grows by one bundle on each beat, with a monthly price over it.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice_stated": true|false, "advice_inferred": true|false, "caution_only": true|false, "quote": "<reader words behind any flag, else empty>", "why": "<one line>"}, ...}

### R1 (strip N1-s01-stack)
1. **The idea:** The animation shows an illustrative homeowner, "Tessa", with a house and a growing stack of cash labeled "$120 a month". The header cites the Freddie Mac weekly mortgage survey. The last frame adds "$320,000 loan · week of Oct 8, 2026". The idea seems to be that a small monthly amount, tied to a $320,000 mortgage at current survey rates, builds up into a noticeable pile of money. The image doesn't say what the $120 is. It might be a monthly saving, an extra payment, or a payment difference.

2. **What changes:** Tessa and the house stay the same across the frames. A small gold bundle of cash appears next to the house in frame 2. It is a flat bundle in frames 2 and 3, then a taller stack in frames 4 to 6. The "$120 a month" label appears in frame 4. The loan and date caption appears in frame 6. The footer, "US only · history, not a forecast", and the "ILLUSTRATIVE" badge stay on every frame.

3. **What it means:** A modest recurring amount of $120 a month accumulates over time into a bigger sum. Anchoring it to a $320,000 loan and a specific week's rate survey suggests the amount comes from current mortgage-rate conditions. The footer warns that this reflects past data and not a prediction. The "ILLUSTRATIVE" labels say the figures and the character are not real results.

4. **Advice a viewer would take:** The animation gives no explicit advice. It doesn't say to pay extra on the mortgage, to invest, or to choose a 15-year loan over a longer one. A viewer might loosely take away that small monthly amounts add up. That is an inference and not something the animation tells them. It also doesn't answer whether to prepay the mortgage or invest the spare cash.

5. **Source of the takeaway:** The "small amounts add up" reading is my own interpretation of the growing stack. No on-screen text or picture states it or recommends any action. The only text that bears on how to read it is the disclaimer: "ILLUSTRATIVE" and "history, not a forecast".
