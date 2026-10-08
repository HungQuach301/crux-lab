# PLAN Tập 6 — Does a 2% Annuity Raise Really Keep Up With Prices?  (≤ 1 trang; viết lại khi đóng phiên)

**Nhánh:** `ep006` · **Đề tài:** #12 · **Format:** `101` · **Phiên hiện hành:** P3 (`session_01JVoRpJ84UMpxj63PnNqCJ6`) — đóng **trước C4** (chưa có khoá K) · lịch sử: `archive/PLAN-history.md`

## 1. Trạng thái
**C3 đã áp, C4 bị chặn.** Câu trả lời C3 → `gates/C3-answer.md`. Giọng cả tập xong (EL **7.699/7.700**, ASR 30/30 không mất từ khoá). **Độ dài thật trên timeline 8:56,6 (536,6 s) ≥ 8:10 ĐẠT** (`story/timeline_len.py`, phép tính nhà máy; kiểm ngược Tập 5 465,67 s); ±5 % quanh trần `101` 9:00 (−3,4 s) → nêu tên; tốc độ thật 2,40 từ/s (ước 2,52). Mid-roll ≈ 3:27,7 sau S12.4, cách cuối 329 s → hợp lệ. F-12 xong trên `factory-f12` @ 9b0fb2d (test 92 OK), **chưa vào `main`/`ep006`** (quyền phiên chặn push `main` và merge). `main` @ 2c5eacf: KINDS vẫn 6 loại cũ → S01/S05 MISSING.

## 2. Việc tiếp (≤ 3) và việc treo
1. **Chủ dự án/phiên có quyền:** merge `factory-f12` → `main` (chỉ thêm, mặc định tắt, trùng byte tập cũ), rồi `main` → `ep006` (xung đột 2 dòng: F-12 `BACKLOG.md`, W10 visual-library README → lấy bản `main`).
2. **Có khoá K gồm kind Tập 6 trên `main`** → merge `main` vào `ep006`, chạy S01/S05, viết `contract.json`, rồi C4 (animatic 720p; `episode.yaml` đủ cảnh/shot; `audio: {close_lift_db: 12, ident: {after: S03}}`; S03 tail 4,0, S12 tail 1,5, S31 5, S32 2). Hàng chờ C4: lượt đạo diễn (S24 10–19 s đứng; S27 mốc năm; S29 nhấn "month"), đồng bộ S24 5/7 · S27 7/8 · S29 4/7, C14 trên 1080p, 4 PHỤ `REVIEW-C2v3.md`. **Chốt C4:** kiểm mù bản có lời cả tập + riêng S29, khuyên sản phẩm = 0, chấm song song rubric cũ + ba cờ, 2 người chấm; S29 không đạt → hỏi chủ dự án.
3. **K4.1 (V11, F11, rubric khuyên) phải có trên `main` trước C5**; chưa có → dừng trước C5 và báo.
- Treo: phiên K (kind Tập 6, khoá K4.0.2; K4.1). P4 merge **squash** `ep006` → `main` (≈ 265 MB WAV ở df9c2d4).

## 3. Quyết định đã có (chủ dự án)
- 08/10 G1: L1 sửa · H-B + C2 v2 · `101` (b) · T1 · T6-1 (8:25 ước / 8:10 thật / 8:00 C5) → `gates/G1-answer.md`.
- 08/10 C3: N1 + séc lớn lên duyệt S07/S24/S27 (W10); S29 (a) ngoại lệ, chốt C4; nhạc hiệu A + khúc đóng A, +12 dB sau chữ cuối (−14 LUFS, ≤ −1 dBTP); kịch bản v3 (a), "hỏi báo giá" = thận trọng chung; EL ≈ 7.700; squash ở P4 → `gates/C3-answer.md`.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| G1 b | S16, S24, S27, S29 | 7:50 < 8:00 (mid-roll) | +93 từ, 1 số mới | 8:30 ước → **8:56,6 thật** | gần trần 9:00 |
| C3 r1→r2 | N1 ×4 | khuyên 8/8 (khoản đều) | séc lớn lên ×1,02^k | khuyên 1/8, nghĩa 8/8 | S29 → chốt C4 |
| P3 | F-12 | điểm chạm khúc đóng mất dưới −20 dB | `music.post()` +12 dB/0,5 s sau chữ cuối; ident A 3 s | −14,0 LUFS · −1,0 dBTP · A07 19,97 dB | chờ merge `main` |

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập **15** triệu. EL duyệt **7.700** (dùng **7.699**) · agent con **13/40** (+1 P3: nhà máy F-12).
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless (trần) | Giờ render |
|---|---|---|---|---|---|---|---|
| P1 | 2026-10-08 14:57 | 0,16 | 0,62 | 20,48 | **0,78** | 0,11 (23 lượt) | 0 |
| P2 | 2026-10-08 16:28 | 0,30 | 1,01 | 47,60 | **1,31** | 0,28 (30 lượt) | 0,34 h |
| P3 | 2026-10-08 23:46 | ≈ 0,03 | ≈ 0,25 | ≈ 8,20 | **≈ 0,28** (+ agent F-12 ≈ 0,18 chưa vào log lúc đó) | 0 | 0 |
P3 đọc từ `list_events` kết quả lượt 23:45 (`modelUsage` tích luỹ); lượt đóng và P2 sau 16:28 chưa cộng — cộng ở P4. Cộng tập ≈ 3,0 / 15 triệu.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/quality-framework.md` 4. `episodes/ep006/PLAN.md` 5. `episodes/ep006/ledger.md` 6. `episodes/ep006/gates/C3-answer.md` 7. `toolkit/factory/README.md` (F-12, sau merge) 8. `playbook/prompts/P3.md`

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 6, phiên P3b. Nhánh ep006 (@ 8a7c51b hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep006`; đọc mục 6 của episodes/ep006/PLAN.md.
C3 đã áp (gates/C3-answer.md); giọng cả tập xong, độ dài thật 8:56,6. Việc đầu tiên: nếu main chưa có F-12 thì merge factory-f12 → main (lấy bản main ở hai dòng xung đột), rồi main → ep006.
KHÔNG mở C4 khi main chưa có khoá K gồm kind Tập 6 (KINDS trong checks/py/r_model.py). Có khoá → chạy S01/S05, viết contract.json rồi C4. Chưa có → đóng phiên và báo.
K4.1 (V11, F11, rubric khuyên) phải có trên main trước C5; chưa có thì dừng trước C5 và báo.
Chặng này: C4 (chốt kiểm mù bản có lời cả tập + S29, khuyên sản phẩm = 0, rubric cũ + ba cờ, 2 người chấm) → C5 (≥ 8:00, mid-roll hợp lệ) → Shorts → G2 (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên").
Ghi chú thêm của chủ dự án (nếu có):
<<DÁN GHI CHÚ Ở ĐÂY>>
```
