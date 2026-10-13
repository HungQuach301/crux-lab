# Đầu bài sửa C5 Tập 7 — vòng 1, phần B (S16–S33) (P3, 12/10). KHÔNG render

Nhánh `ep007`. Làm trong `/home/user/crux-lab`, sửa tệp; **không commit, không push**. Không in, không ghi khoá API.
**Chỉ sửa tệp trong `episodes/ep007/world/c4/{d-s16-s20,e-s21-s24,f-s25-s28,g-s29-s33}/`** (một phiên khác đang sửa các đoạn còn lại song song). **Không sửa `world/c4kit.*`, `obj7.js`, `c3kit.*`, `derive.py`, claims, `episode.yaml`.** Cần kit → dừng, mô tả. Lệnh kiểm: lệnh đơn, không `cd … &&`.

## Đã sửa gì, vì sao (PLAN §4)
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C4 v1–v4 | cả tập | hàng chờ C3 §3, bố cục, S21 | `briefs/builder-c4-*.md` | cổng gốc 16/21 (`gates/C4-result.md`) | G2 nêu |
| C5 đạo diễn ×2 | cả tập | ≈ 100 nhận xét lặp, điểm 2–3/5 | vòng này: đúng-số + CHÍNH (chủ dự án 12/10) | | PHỤ ghi lại |

## Đọc
`episodes/ep007/c5/director-merged.md` (nhận xét lặp ở cả hai lượt, đã loại ý trái quyết định chủ dự án), `gates/C4-answer.md`, `gates/C4-result.md`, `story/beats.md`, `story/script.md`, tệp của các đoạn được giao, `world/c4kit.js` (chỉ đọc). Khung thật bản C4 r4: `out/video.mp4` (trích ≤ 10 khung bằng `ffmpeg -v error -y -ss <t> -i <mp4> -frames:v 1 <png>`).

## Sửa
- **S30 (đúng số, CHẶN):** "fallback about $793 a month" đang gắn cột trong suốt (sai nghĩa) → ngoặc V6 `cushion` có độ rộng = khoảng $793 dưới khoản 15 năm của Leo (rộng hơn ngoặc ~$613 của Tessa, cùng thang), nhãn trên ngoặc; thanh không đè đầu Leo; sửa vật liệu đầu đen.
- **Lời đổi (chủ dự án 12/10, `gates/C4-answer.md`):** S25.5 nay "How any investment compares, once risk and taxes count, isn't tested here."; S31.3 nay "The bar isn't the whole story: …"; take mới S25 29,84 s, S31 23,28 s (timeline 603,0 s). Chạy lại `spine.py` của f, g; cue nào neo vào từ đã bỏ ("clears", "Clearing") → neo sang từ mới gần nhất; giữ ±0,2 s.
- **S21–S24, S25:** không đổi loại hình nữa (hết vòng, G2 nêu trước/sau); chỉ sửa bố cục/đồng bộ nếu nhận xét lặp nêu.
- **Mọi nhận xét lặp cấp [CHÍNH] của các cảnh S16–S33** trong `c5/director-merged.md`, bằng hình trước, nhãn cuối. Nhận xét cấp [PHỤ]: làm nếu rẻ và không rủi ro, còn lại liệt kê.
- Giữ quyết định chủ dự án: nhãn giá S01 ở 5,94 s (C3 câu 3 a); S25 bóng tách, không cầm sát thanh; thẻ góc nguồn + "US only · history, not a forecast" + ILLUSTRATIVE là luật kênh; "ILLUSTRATIVE" hai lần (huy hiệu + tên) là chủ ý; không thêm chữ khuyên; số chỉ qua claim; ≥ 5 s đầu ở thế giới; số/nhãn so sánh chỉ ở đồ thị.
- Tổng timeline phải khớp `out/factory/timeline.json` sau khi chạy `python3 episodes/ep007/c4/build_inputs.py --timeline` (phiên chính đã cập nhật take); mọi cue ±0,2 s; không vượt trần 6 sfx/10 s.

## Kiểm (bắt buộc chạy)
`python3 toolkit/tests/comment_guard.py episodes/ep007/world`; `python3 episodes/ep007/world/c4/<đoạn>/spine.py` mỗi đoạn được giao; smoke mỗi đoạn (`node --import ./episodes/ep007/c4/smoke/register.mjs episodes/ep007/c4/smoke/run.mjs <đoạn>`): 0 lỗi, 0 chồng chữ, 0 ra mép, 0 quy tắc 1, 0 số ngoài claim.

## Trả về (≤ 25 dòng)
Mỗi cảnh: nhận xét CHÍNH nào đã sửa, thế nào; PHỤ đã/chưa làm (đếm); kết quả kiểm; rủi ro.
