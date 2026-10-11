# PLAN Tập 7 — 30-Year Mortgage Paid Off in 15 Years: What It Really Costs (≤ 1 trang)

**Nhánh:** `ep007` · **Đề tài:** #13 (debt-1) · **Format:** `lab` · **Phiên hiện hành:** P2 (`session_01X1ixSVAUdXqW3ZNBYE9qy9`) → C3 đã trả lời (11/10), sang P3 · Lịch sử: `archive/PLAN-history.md`

## 1. Trạng thái
**C3 đã trả lời** (`gates/C3-answer.md`: duyệt có điều kiện; **S21 lớp trả thêm không thấy bằng hình = CHÍNH**, C4 sửa + kiểm mù lại; 2, 4, 5 đồng ý; 3 a). `main` 76ef2b1 (K4.2 kind `term-pair-weekly-replay` Tập 7 + SH06; K4.2b A28/A31; A29 hoãn; LOCK dc4981b3) đã merge vào `ep007`. G1 lô áp (`gates/G1-answer.md`) · C2 v3.1 (mốc "October eighth", số S21/S23 lên hình) kiểm máy ĐẠT ước 9:54 · kiểm mù C2 vòng 3 rubric MỚI: đúng 6/6, `advice_stated` 0/6 · C3: 5 đoạn thế giới (the stack S01/S06, N1 Month track S21/S23, the bar S25), cổng gốc tắt tiếng vòng 3 **5/5 ĐẠT 2/2, stated 0** · REVIEWER C3 hai lượt ĐẠT có sửa (câu chữ đã áp; còn hàng chờ C4 bắt buộc §3 của gói).

## 2. Việc tiếp (≤ 3) và việc treo
1. **C4 mở được** (khoá K4.2/K4.2b có kind Tập 7 đã ở `ep007`). **S21 lớp trả thêm phải thấy bằng hình (CHÍNH, C3 câu 1) + kiểm mù lại.** Hàng chờ C4 bắt buộc khác: `gates/C3.md` §3 (S21 lớp trả thêm không thấy, S25 bóng "hoà mốc", S01 chồng lớn trong lời "$320,000" + bó sót ở cửa, S23 khối năm, Tessa đứng yên, lệch làm tròn $8,792/$8,796 và $2,949/$2,948, đồng bộ S06 2/5) + chốt kiểm mù bản có lời S23–S24 và S25 (§Anh chọn 2, 5).
2. Giọng cả tập: **đọc `GET /v1/user/subscription` trước**, báo ký tự còn (P2: 72.750 / 144.034, làm mới 01/11); ước ≈ 8.600; thiếu → dừng hỏi.
- Treo: F-14 (`factory-f14`, quyết `deep` Tập 8 trước C2 Tập 8); EL lệch ≈ 5.947 ký tự chưa rõ nguồn; ≈ 300 MB tệp trung gian `world/c3/out` đã vào lịch sử `ep007` (đã bỏ theo dõi).

## 3. Quyết định đã có (chủ dự án)
- 11/10 tổng kết Tập 6: `tongket-t6/ANSWER.md`. · 11/10 G1 lô: `gates/G1-answer.md` (#13 L1; #20 có điều kiện / #6; rubric khuyên MỚI; mốc ngày; `lab` ~9:53; T2; thumbnail "the stack" "$120 A MONTH?"; N1 duyệt; CHARTER §5 sửa; EL `user_read`).
- 11/10 C3: `gates/C3-answer.md`.
- 11/10 lệnh P2: lượt đạo diễn + REVIEWER headless khoá Console, 0 agent con, ≤ ~10 khung/lượt, không in/ghi khoá; đọc hạn mức EL trước khi sinh giọng cả tập.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C2 r3 | S21–S24 | số dày 3/6 | "195 months", "$8,792" chỉ trên hình | checker ĐẠT 9:54 | đo lại C4 |
| C3 r2 | S06 | chồng = "tiền để dành", không thấy thanh dâng | nhãn trước khi dâng, vạch 15 năm, lát bay từ đỉnh thanh, "extra paid" | 2/2 | — |
| C3 r3 | S01, S21, S23, S25 | REVIEWER: tiết kiệm 3/3, ô trễ sót, teal = "còn nợ", "guaranteed / has to beat" | bó từ cửa nhà, N1 `ink-muted`/`ink`/`warn`, gom 12 lớp, bóng đô la tách | 5/5 2/2 | §3 gói |
| lời | S21 | ASR "October eight" | "October eighth" | take mới | — |

## 5. Mức cảnh báo, token, chi (`episode.md` §8, `lab`: 15 triệu · Console $45)
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless (trần) | Console |
|---|---|---|---|---|---|---|---|
| P1 | 11/10 13:49 | 0,10 | 0,32 | 27,51 | **0,41 triệu** | 0,81 triệu | ≈ $8,9 |
| P2 | 11/10 15:32 (list_events, result cuối của tiến trình hiện tại; lượt đóng phiên chưa tính) | ≥ 0,08 | ≥ 0,28 | ≥ 34,79 | **≥ 0,36 triệu** | ≈ 0,5 triệu (đọc mù + cổng gốc + đạo diễn) | **≈ $22,3** (dựng 3 lượt $17,97 · REVIEWER $2,51 · cổng gốc $0,82 · đạo diễn $0,77 · kiểm mù $0,25) |
0 agent con · EL P2 1.843 ký tự (tổng tập 3.076) · giờ render C3 ≈ 25 phút máy (540p).

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/prompts/P3.md` 4. `episodes/ep007/PLAN.md` 5. `episodes/ep007/gates/C3.md` 6. `episodes/ep007/gates/C3-answer.md` (đã chép) 7. `episodes/ep007/world/c3/README.md` 8. `episodes/ep007/story/beats.md`

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 7, phiên P3 (C4 → C5 → Shorts → G2). Nhánh ep007. Mở bằng `bash toolkit/verify.sh ep007`; đọc mục 6 của episodes/ep007/PLAN.md.
C3 đã trả lời và đã chép (episodes/ep007/gates/C3-answer.md); main 76ef2b1 (khoá K4.2 kind Tập 7 + K4.2b) đã merge vào ep007 — merge main lần nữa nếu có khoá mới. Sửa D-011: nếu container còn tệp lớn của P2 (world/c3/out, vendor) thì chạy tiếp trong phiên đó sau /compact.
Chặng này: hàng chờ C4 bắt buộc (gates/C3.md §3; S21 lớp trả thêm thấy bằng hình = CHÍNH + kiểm mù lại; chốt C3-answer câu 2, 5) → đọc GET /v1/user/subscription của ElevenLabs, báo ký tự còn, rồi mới sinh giọng cả tập (thiếu → dừng hỏi) → C4 → C5 → Shorts → G2 (P3.md việc 1–4) → dừng ở G2 (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên").
Việc nặng: headless khoá Console (toolkit/api.sh; kiểm mù headless.sh), 0 agent con; lượt đạo diễn và REVIEWER xem tối đa ~10 khung mỗi lượt; không in hay ghi khoá ra đâu.
```
