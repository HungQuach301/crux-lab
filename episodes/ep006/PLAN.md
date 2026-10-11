# PLAN Tập 6 — Does a 2% Annuity Raise Really Keep Up With Prices?  (≤ 1 trang; viết lại khi đóng phiên)

**Nhánh:** `ep006` (đẩy cả `ep006` và `claude/gracious-brown-rccz2m`) → **merge squash vào `main` @ `MERGE_SHA`** · **Đề tài:** #12 · **Format:** `101` · **Phiên vừa đóng:** P4 giao file, chạy tiếp trong phiên P3c (`session_01QNrEnsRn8CMnf6J5ujL79c`, lệnh chủ dự án 11/10) · lịch sử: `archive/PLAN-history.md`

## 1. Trạng thái
**G3 chờ chủ dự án đăng** — G2 duyệt 11/10 (`gates/G2-answer.md`: L3 ≥ 4 cả 6 dòng, phát hành CÓ). Bản cuối không đổi → checks `run-c5d` (LOCK `4d688acd`) là của bản giao: Tập ĐẠT, CHẶN 36/36, CHÍNH 13/13. Giao: nhánh `ep006-delivery` @ `d4d8c48` — master nguyên byte `f96da0ea…` (13 phần 90 MB) + Shorts + thumbnail + phụ đề + mô tả; tải ngược `sha256sum -c` **22/22 OK**. Hướng dẫn: `HUONG-DAN-DANG.md` (link tải thẳng + SHA). Merge squash `ep006` → `main` (gồm F-13; không có WAV 265 MB của df9c2d4 — đã ngoài cây), LOCK trên main `4d688acd` khớp.

## 2. Việc tiếp (≤ 3) và việc treo
1. **Thumbnail ChatGPT** (chủ dự án gửi ảnh): kiểm chữ trên ảnh — không số tiền, không khuyên, ILLUSTRATIVE khi có nhân vật, "US only · history, not a forecast" → báo đạt/không; ghi ledger + `HUONG-DAN-DANG.md`.
2. **G3:** chủ dự án tải, đăng theo `HUONG-DAN-DANG.md`, ghi link + ngày vào `audience.md`; xoá nhánh `ep006-delivery` (proxy chặn → chủ dự án xoá: GitHub → Branches → Delete).
3. **Tổng kết Tập 6** — phiên riêng (P3.md việc 7); mốc 7 ngày: ảnh YouTube Studio → `audience.md`.
- Treo: lô K — `checks-appeal.md` A28; qc nhà máy đọc đối trọng master ở đoạn thế giới; REG không so run trước (REVIEWER G2 §7); nghi vấn "none since" che mép dải cảnh báo S15 (B15).

## 3. Quyết định đã có (chủ dự án)
G1 → `gates/G1-answer.md` · C3 → `gates/C3-answer.md` · F-13 trên `ep006` · C4 rubric MỚI → `gates/C4-answer.md` · **11/10 G2 → `gates/G2-answer.md`** (L3 ≥ 4 không điểm chi tiết, phát hành, giữ B01/B15, thumbnail ChatGPT nền thumb-1 / T&C 1, 2, 3 nếu bộ nhà máy, Shorts OK) · 11/10: P4 chạy trong phiên P3c; giao bằng nhánh tạm (không thử Release); merge squash.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C5–C5d | a–f, hợp đồng, mô tả | run-c5 TRƯỢT; B29 tụt; V11 S04 | xem `archive/PLAN-history.md` (PLAN đóng P3c §4) | run-c5d ĐẠT; cổng gốc 20/23 | — |
| P4 | — | — | không sửa (G2 giữ bản sau) | giao 22/22 OK | thumbnail ChatGPT |

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập **15** triệu. EL **7.699/7.700**. Agent con cả tập **23/40** (P3c, P4: 0).
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless | Giờ render |
|---|---|---|---|---|---|---|---|
| P3b | 2026-10-09 10:08 | 1,35 | 71,18 | 475,72 | 72,52 | 0,64 | ≈ 2,5 h |
| P3c | 2026-10-11 03:20 | 0,48 | 2,19 | 109,11 | 2,67 | xem chi API | 1080p ≈ 7,7 h · checks ≈ 10,3 h |
| P4 (trong phiên P3c) | 2026-10-11 03:52 | 0,03 | 0,11 | 7,71 | **0,14** | 0 | 0 (giao nguyên byte, không mã hoá lại) |
Cách đo: `python3 episodes/ep006/c5/session_tokens.py <phiên.jsonl>` (cộng dồn phiên) trừ dòng P3c. **Chi API Console: P3c ≈ $25,5 · P4 $0 · cộng ≈ $25,5 / trần $170.** Cộng tập ≈ 77,9 / 15 triệu (Tập 5 ≈ 85,4; D-009: chỉ cảnh báo).

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` (§8 KPI) 3. `episodes/ep006/PLAN.md` 4. `episodes/ep006/ledger.md` 5. `episodes/ep006/gates/G2-answer.md` 6. `episodes/ep006/HUONG-DAN-DANG.md` 7. `episodes/ep006/audience.md` 8. `playbook/prompts/P3.md` (việc 7)

Tệp lớn ngoài git: master + Shorts nằm trên nhánh `ep006-delivery` (tới khi xoá) và ở `out/` của container này; dựng lại theo lệnh ở `archive/PLAN-history.md` (PLAN đóng P3c §6), kiểm SHA `f96da0ea…`.

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Tập 6 đã giao (G3). Nhánh main (ep006 đã merge squash). Mở bằng `bash toolkit/verify.sh ep006`; đọc mục 6 của episodes/ep006/PLAN.md.
Việc: (1) nếu có ảnh thumbnail ChatGPT đính kèm: kiểm chữ trên ảnh (không số tiền, không khuyên, ILLUSTRATIVE khi có nhân vật, "US only · history, not a forecast"), báo đạt/không, ghi ledger + HUONG-DAN-DANG.md; (2) ghi link video + ngày đăng vào episodes/ep006/audience.md; (3) xoá nhánh ep006-delivery nếu tôi đã tải xong (proxy chặn → báo). Tổng kết Tập 6 là phiên riêng.
Thông tin đăng:
<<DÁN LINK VIDEO, NGÀY ĐĂNG, ẢNH THUMBNAIL Ở ĐÂY>>
```
