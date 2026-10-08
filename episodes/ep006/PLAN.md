# PLAN Tập 6 — Does a 2% Annuity Raise Really Keep Up With Prices?  (≤ 1 trang; viết lại khi đóng phiên)

**Nhánh:** `ep006` · **Đề tài:** #12 · **Format:** `101` · **Phiên hiện hành:** P2 (`session_01VWvKx3ATmgiMnpR3FiPq12`) — đóng ở C3 · lịch sử: `archive/PLAN-history.md`

## 1. Trạng thái
**C3 chờ** (gói `gates/C3.md`, issue: xem §7). G1 áp (b): C2 v3 1.279 từ nói, ước 8:27, check ĐẠT không cờ; mid-roll đủ điều kiện theo ước (chốt thật ở P3). Kiểm mù lời v3: đúng 6/6, **khuyên 5/6 chấm gốc / 1/6 chấm trộn (v2 cũng 1/6)** → chủ dự án quyết. N1 hàng 10 thùng: S07/S24/S27 ĐẠT (vòng 2), **S29 trượt sau 3 vòng** (khuyên 1/2, giữ v2). Nhạc hiệu A/B + khúc đóng. 0 CHẶN mở; REVIEWER gói: `gates/REVIEW-C3.md`.

## 2. Việc tiếp (≤ 3) và việc treo
1. Chép câu trả lời C3 → `gates/C3-answer.md`; ghi sổ gu, AUTHORSHIP, ledger; áp (S29, nhạc, kiểm mù/S04.2, EL).
2. **Chặn C4:** `main` chưa có khoá K gồm kind Tập 6 (K4.0.1 LOCK 79aeec0d đã merge, KINDS 6 loại cũ → S01/S05 MISSING). Có khoá → merge `main`, chạy S01/S05, viết `contract.json`. Không có → không mở C4, làm việc không phụ thuộc K (giọng cả tập nếu EL duyệt, đo độ dài thật ≥ 8:10, nhà máy F-12 trên `factory-*`).
3. P3: giọng cả tập (`story/voice_scenes.py`, chỉ cảnh chưa có take) → độ dài thật trên timeline ≥ 8:10 (thiếu → sửa trước render) → C4 → C5 (≥ 8:00, mid-roll hợp lệ) → G2.
- Treo: phiên K (kind Tập 6 + sửa luật cũ, `K-brief.md` có claim mới `worst_window_years_2pct_fell_20y`). Hàng chờ C4: lượt đạo diễn (S24 10–19 s đứng, S27 thanh thời gian thiếu mốc năm, S29 nhấn "month"), đồng bộ S24 5/7 · S27 7/8 · S29 4/7, C14 trên 1080p, 4 PHỤ `REVIEW-C2v3.md`. Lịch sử `ep006` có ≈ 265 MB WAV (df9c2d4) — chủ dự án quyết xoá.

## 3. Quyết định đã có (chủ dự án)
- 08/10 G1: L1 sửa · H-B + C2 v2 · `101` (b) ≥ 1.275 từ, ≤ 1 số mới · T1 · bài học T6-1 (đích 8:25 ước / 8:10 thật / 8:00 C5; dòng mid-roll ở G1) → `gates/G1-answer.md`.
- 08/10 lệnh P2: merge K4.0 ngay, không chờ phiên K; P3 không mở C4 khi `main` chưa có khoá K gồm kind Tập 6.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| G1 b | S16, S24, S27, S29 | độ dài 7:50 < 8:00 (mid-roll) | +93 từ: Carl/Edna theo năm bằng thùng; 1 số mới (20/20) | check ĐẠT, 8:27 | dư 4 từ |
| REVIEWER | S27.5 | CHÍNH-1 nghe sai nhân quả | "came at the end of her stretch … and at the start of his" | check ĐẠT | CHÍNH-3 S04.2 → C3 |
| C3 r1→r2 | N1 ×4 | khuyên 8/8 (tưởng khoản đều) | séc lớn lên ×1,02^k cạnh hàng | khuyên 1/8, nghĩa 8/8 | S29 |
| C3 r3 | S29 | khuyên 1/2 | trục tháng bắt đầu + séc cùng cỡ | khuyên 2/2 → loại | giữ r2, chủ dự án chọn |

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập **15** triệu. EL ≤ 6.000 (dùng **2.446**; cả tập ước 7.256 → hỏi ở C3) · agent con **12/40**.
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless (trần) | Giờ render |
|---|---|---|---|---|---|---|---|
| P1 | 2026-10-08 14:57 | 0,16 | 0,62 | 20,48 | **0,78** | 0,11 (23 lượt) | 0 |
| P2 | 2026-10-08 16:28 | 0,30 | 1,01 | 47,60 | **1,31** | 0,28 (30 lượt) | 0,37 h |
Log phiên (`list_events` kinds=result, `modelUsage` tích luỹ gồm agent con); lượt sau 16:28 (vòng 3, đạo diễn, REVIEWER gói, đóng) cộng ở P3. Cộng tập ≈ 2,5 / 15 triệu.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/quality-framework.md` 4. `episodes/ep006/PLAN.md` 5. `episodes/ep006/ledger.md` 6. `episodes/ep006/gates/C3.md` 7. `episodes/ep006/gates/C3-answer.md` (phiên kế tạo) 8. `playbook/prompts/P3.md`

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 6, phiên P3. Nhánh ep006 (@ <SHA> hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep006`; đọc mục 6 của episodes/ep006/PLAN.md.
Gói đã gửi: episodes/ep006/gates/C3.md (issue #<N>). Việc đầu tiên: chép câu trả lời dưới đây vào episodes/ep006/gates/C3-answer.md, commit, push; ghi taste-ledger.md, AUTHORSHIP.md, ledger.
KHÔNG mở C4 khi main chưa có khoá K mới gồm kind Tập 6 (KINDS trong checks/py/r_model.py; K4.0.1 LOCK 79aeec0d chưa có). Có khoá → merge main vào ep006, chạy S01/S05, viết contract.json rồi mới C4. Chưa có → chỉ làm việc không phụ thuộc K (áp C3, giọng cả tập nếu EL được duyệt, đo độ dài thật ≥ 8:10, nhà máy F-12 trên factory-*), rồi dừng và báo.
Chặng này: áp C3 → giọng cả tập → độ dài thật trên timeline ≥ 8:10 → C4 → C5 (≥ 8:00, mid-roll hợp lệ) → Shorts → G2 (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên").
Câu trả lời C3:
<<DÁN CÂU TRẢ LỜI C3 Ở ĐÂY>>
```
