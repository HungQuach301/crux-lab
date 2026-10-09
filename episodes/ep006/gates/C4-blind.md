# C4 — kiểm mù bản có lời (B cả tập · C S29 · E đối chứng hình thật) — P3b 09/10

Ý đồ: `gates/C4-intent.md` (ghi trước, REVIEWER `gates/REVIEW-C4-intent.md`). Dữ liệu: `c4/voiced-r1/` (KEY, packet, rubric-key commit trước khi chấm; 2 người chấm headless `scores-g1/g2.json`). Animatic 720p @ 0af1076.

## Bảng tổng (gộp thận trọng: điểm thấp nhất, cờ nếu bất kỳ người chấm nào bật)
| Mẫu | Người đọc | Nghĩa = 1 | Khuyên (rubric cũ) | advice_stated (mới) | advice_inferred | caution_only | Câu 5 |
|---|---|---|---|---|---|---|---|
| ctrl/AUX-ep005-S06 | 3 | 3 | 0 | 0 | 0 | 0 | own, none, none |
| ctrl/NEG-S29 | 3 | 3 | 1 | 0 | 1 | 2 | own, own, own |
| ctrl/POS-S29 | 3 | 3 | 3 | 3 | 0 | 0 | video, video, video |
| ep006/S29 | 3 | 3 | 2 | 0 | 2 | 2 | own, own, own |
| ep006/WHOLE | 3 | 3 | 3 | 0 | 3 | 0 | own, own, own |

2 người chấm; gộp thận trọng (điểm thấp nhất, cờ nếu bất kỳ người chấm nào bật).

## Kết luận theo luật ghi trước
- **B (cả tập): câu khuyên theo rubric cũ 3/3 → TRƯỢT** (ngưỡng 0/3). Rubric mới: `advice_stated` **0/3** (cả 3 là `advice_inferred`, câu 5 "own"). Nghĩa 3/3.
- **C (S29): rubric cũ 2/3 → TRƯỢT** (ngưỡng 0/3). Rubric mới: `advice_stated` **0/3** (2 `advice_inferred`, 2 `caution_only`). Nghĩa 3/3.
- **E (đối chứng hình thật):** dương 3/3 `advice_stated` (câu 5 "video" 3/3) · âm (cặp khớp) 0/3 `advice_stated`, 1 `advice_inferred` · phụ Tập 5 S06 0/3. → **rubric mới phân biệt được** (dương ≥ 2/3, âm ≤ 1/3) **nhưng lệch rubric cũ trên bộ ứng viên** → theo K4.1 câu 3: **giữ rubric cũ** cho cổng; ghi `checks-appeal.md`.
- Theo ý đồ (B, C trượt → không đổi lời, không mở vòng sửa): **dừng, hỏi chủ dự án** kèm câu trích dưới.
- "Câu khuyên sản phẩm (chọn khoản gắn CPI/COLA)" theo đúng chữ của C3: **không câu nào** bảo chọn khoản gắn CPI/COLA; câu sát nhất: S29 *"ask whether a payout that rises each year would protect you better than a flat one"* (người đọc ghi là kết luận của mình).

## Từng lượt (nhãn hex · điểm g1/g2 · cờ g1 · g2: S stated, I inferred, C caution · câu 5 · câu trích)
| Mẫu | Hex | Điểm | Cờ | Câu 5 | Trích |
|---|---|---|---|---|---|
| ctrl/AUX-ep005-S06 | 4316b8c7 | 1/1 | — · — | own/own |  |
| ctrl/AUX-ep005-S06 | 10163e45 | 1/1 | — · — | none/none |  |
| ctrl/AUX-ep005-S06 | 1d1d6575 | 1/1 | — · — | none/none |  |
| ctrl/NEG-S29 | c7fbe277 | 1/1 | I · I | own/own | The viewer could weigh that when comparing the two payout options. |
| ctrl/NEG-S29 | 0b599bf6 | 1/1 | C · C | own/own | that suggests asking whether each option adjusts for inflation |
| ctrl/NEG-S29 | c5810be8 | 1/1 | C · C | own/own | it suggests asking whether each payout option adjusts for inflation |
| ctrl/POS-S29 | d5e21dcf | 1/1 | S · S | video/video | The narration said this directly: "So if you are choosing today, take the payout that is tied to inflation." |
| ctrl/POS-S29 | 8295a193 | 1/1 | S · S | video/video | The advice came from the video's narration, in its last line ("So if you are choosing today, take the payout that is tied to inflation") |
| ctrl/POS-S29 | 6e50a2ef | 1/1 | S · S | video/video | The video itself suggested this, through its narration: "So if you are choosing today, take the payout that is tied to inflation." |
| ep006/S29 | ada7b364 | 1/1 | C · I | own/own | the lesson is to ask how a payment would hold up if prices rise faster than expected |
| ep006/S29 | 6d7fe6d3 | 1/1 | C · C | own/own | that would mean checking whether either option adjusts for inflation |
| ep006/S29 | d54ed6e0 | 1/1 | I · I | own/own | ask whether a payout that rises each year would protect you better than a flat one |
| ep006/WHOLE | 87d48f85 | 1/1 | I · I | own/own | The takeaway is my own conclusion, not the video's. |
| ep006/WHOLE | 6f54399f | 1/1 | I · I | own/own | A viewer could compare the raise with what prices have done, and with how much smaller the starting check is. |
| ep006/WHOLE | 304743ea | 1/1 | I · I | own/own | Weigh the buying-power results against that dollar cost, with a professional if needed. |
