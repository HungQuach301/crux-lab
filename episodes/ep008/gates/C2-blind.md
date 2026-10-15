# C2 — kiểm mù lời (ý đồ `gates/C2-intent.md`)

## Vòng 1 (13/10, C2 v1 + S04.3b; 6 đọc + 1 chấm, nguyên văn `c2/r1/`, bảng `c2/r1/tally.json`)
| Vai | Điểm | advice_stated | advice_inferred | Cụm trích làm căn cứ | Mất chú ý (loại · chỗ) | Trả lời câu mang tới |
|---|---|---|---|---|---|---|
| T | 1 | 0 | 1 | "renting cost more than buying in most start months" | số dày · Census 4.83–5.59 % | có |
| T | 1 | 0 | 1 | "rent isn't wasted by rule" | phương pháp · chuỗi giới hạn cuối | có |
| T | 1 | 0 | 1 | "renting cost more than buying in most start months" | phương pháp · tiền mặt/T-bill/thuế/tái cấp vốn | có |
| T | 1 | 0 | 1 | cả hai câu trên | số dày · dãy tháng + đếm (72, 6) | có |
| T | 1 | 0 | 1 | "renting cost more than buying in most start months" | số dày · dải Census | có |
| G | 1 | 0 | 1 | "renting cost more than buying in most start months" | số dày · Census 4.83–5.59 % | có |
**Đúng 6/6 (≥ 5/6 ĐẠT) · advice_stated 0/6 (ĐẠT) · mất chú ý: `số dày` 4/6 — TRƯỢT ngưỡng "không loại khối ≥ 4/6"; `phương pháp` 2/6 (≥ 2/6 → sửa, episode.md §2).** advice_inferred 6/6 (báo, không chặn — A28): 5/6 trích câu kết S32.3 → đưa vào vòng 2 (câu kết nghe như phán quyết "mua hơn").
`fix: picture` không áp (kiểm lời). Vòng 2: WRITER mới, đầu bài `briefs/writer-c2-r2.md`.

## Vòng 2 (13/10, C2 v2; 6 đọc mới + chấm mới — lượt chấm đầu chỉ trả R1, chạy lại `grade` toàn gói; `c2/r2/grade-try1-incomplete.json` giữ làm vết)
| Vai | Điểm | advice_stated | advice_inferred | Cụm trích | Mất chú ý | answered_own |
|---|---|---|---|---|---|---|
| T | 1 | 0 | 1 | — | nhân vật · Marcus/Priya | Partly (lịch sử có, 2026 không) |
| T | 1 | 0 | 1 | — | khác · chuỗi giới hạn mở đầu | Partly |
| G | 1 | 0 | 1 | "the dark doors thin out…" | phương pháp · tiền mặt | Partly |
| T | 1 | 0 | 1 | — | khác · dòng Census + giới hạn | Partly |
| T | 1 | 0 | 1 | — | số dày · 72 tháng, %, $ | Partly |
| T | 1 | 0 | 1 | "the dark doors thin out" | định nghĩa · 2,5 % | Partly |
**Đúng 6/6 · advice_stated 0/6 · không loại khối ≥ 2/6** (khác 2/6 — hai chỗ khác nhau) → **C2 ĐẠT ở vòng 2.** Câu kết S32.3 không còn bị trích làm căn cứ khuyên (v1: 5/6). advice_inferred vẫn 6/6 (báo): người đọc tự suy "giữ đủ lâu / tránh mua đỉnh" — nêu ở G1. `answered_own`: cả hai vòng người đọc đều trả "Partly" (lịch sử có, năm 2026 không) — người chấm v1 ghi true, v2 ghi false: lệch người chấm, không phải lệch nội dung.

## Lượt sau G1 (M2, 13/10) — một lượt duy nhất (G1 câu 2), ý đồ `gates/C2-intent.md` mục cuối
Mẫu `c2/sample-m2.txt` (cold open v3 + chương + kết bảng điểm), 6 người đọc headless Sonnet (5 T + 1 G) + 1 người chấm, rubric cũ `c2/rubric.md`; nguyên văn `c2/m2/` (khoá `key.json`, `label-key.json`).

| | Kết quả | Ngưỡng |
|---|---|---|
| Đúng | **6/6** (mọi người đọc: ≈ 3/4, dãy 2001–2007, June 2006, phụ thuộc thẻ tiền thuê) | ≥ 5/6 — ĐẠT |
| `advice_stated` | **0/6** | = 0 — ĐẠT |
| `advice_inferred` | 6/6 (người đọc tự ghi là kết luận của mình: "giữ lâu", "tự kiểm giả định") | chỉ báo |
| `advice_words` | 0 | — |
| Mất chú ý theo loại khối | **phương pháp 4/6** — cùng chỗ S06.1 "Most rent or buy math picks one growth rate…" · **nhân vật 2/6** — S23 Marcus/Priya "nhắc lại kết quả" | ≥ 2/6 → **ghi G2, không mở vòng** (chủ dự án: đúng một lượt) |

Cách xử lý không đổi lời: S06 (B06) và S23 (B23) là nhịp loại 1 — animatic/nháp cho chúng **đổi hình mạnh** (B06: đường giả định phẳng vẽ ra rồi bản ghi thật tích từng tháng; B23: hai người đứng trước hai căn sáng/tối thật trên phố), đo ở cổng gốc tắt tiếng; G2 nêu hai khối này kèm câu chữ đề xuất rút gọn nếu chủ dự án muốn (đổi lời đã duyệt = quyền chủ dự án). Chi: 7 lượt.
