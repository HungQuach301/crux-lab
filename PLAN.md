# PLAN kênh Crux (≤ 1 trang) — cập nhật 13/10/2026 (tổng kết Tập 7 đã áp, D-013)

PLAN từng tập: `episodes/epNNN/PLAN.md` (mẫu `playbook/templates/PLAN-tap.md`). Thẩm quyền: `CHARTER.md` (v5) → `decisions/` (mới nhất D-013). Bản PLAN kênh trước khi dọn: `archive/PLAN-kenh-history.md`.

## Tập
| Tập | Đề tài | Format | Trạng thái |
|---|---|---|---|
| 3 · 5 · 6 | savings bond vs T-bills · #17 PMI 10 % · #12 annuity 2 % | `lab` · `101` · `101` | đã đăng (Tập 6: tổng kết áp, `tongket-t6/ANSWER.md`) |
| 4 | #3 giới hạn $500,000 | — | **không đăng** (chủ dự án 09/10, sổ gu) |
| 7 | #13 "30-Year Mortgage Paid Off in 15 Years: What It Really Costs" | `lab` 10:06,7 | **đã đăng 13/10**; `main` squash `c735828`, bản đủ ở nhánh `ep007`; link chờ điền `episodes/ep007/audience.md` |
| **8** | **#20 thuê vs mua — phát lại lịch sử thật** | `lab` | **sau G1 (13/10): M2 xong** — cold open v3, kiểm mù lời 6/6 · 0 khuyên, giọng cả tập, animatic xám 10:26, cổng gốc 19/24 (±5 %, 0 khuyên); **M3–M5 đang chạy** (nhánh `ep008`, `episodes/ep008/PLAN.md`) |

## Tiếp
1. **Tổng kết Tập 7 đã áp (D-013, chủ dự án 13/10: 1a · 2b · 3a):** mô hình xưởng 6 mốc, `playbook/prompts/CHAY-TAP-N.md`, 1 Short, 0 thumbnail, footage ngoài (`RIGHTS.md` §F), SFX CC0/CC BY, công thức mở–chương–kết (`story.md`). **Tập 8 vào mô hình mới sau G1** (P1 đang chạy mẫu cũ); bộ lấy mẫu trang chạy **trước G2** dù mẫu nào.
2. **Lô K Tập 8:** A34–A37 + A38 (1 Short, 0 thumbnail) + A39 (quyền footage, trước M3 Tập 8 nếu dùng footage) + A40 (nguyên tắc, duyệt) + A41a; A32, A33, A29 mang sang. `ep008` đổi số khiếu nại của mình thành A42–A45.
3. **Đường thử trên tập cũ** (`factory-t7lab`, `tongket-t7/REPORT.md` §6b): animatic S21/S25, hiệu chuẩn "nhớ lại", J/L-cut + màu hồi + SFX thật, checks nháp vs 1080p — song song P1 Tập 8, không chạm `ep008`. Nhạc người sáng tác CC BY: xét ở G1 Tập 9.

## Việc treo
- Nhà máy (`toolkit/factory/BACKLOG.md`): J/L-cut qua biên đoạn ở `splice.py`; `api.sh` không chặn agent con trong headless (Tập 7 C5); đồ dùng ngoài git khi container mới (bed.wav, three `node_modules`, FRED, PyAV < 15 — TONGKET-INPUT p); F-14 đóng TRƯỢT (12/10), Tập 8 `lab`.
- Thị trường: `analyze.py`/`report.py` đọc `OWN_CHANNELS` rồi chạy lại q01, q17 (lessons T6-12).
- EL: dư 66.164 / 144.034 (13/10), làm mới 01/11; khoá dùng chung với dự án khác — đọc hạn mức ở P1.
- Chủ dự án: xoá nhánh `ep007-delivery`, `ep006-delivery` sau khi tải (proxy chặn xoá).

## Hàng chờ phiên K (`checks-appeal.md`, mục "Hàng chờ lô K kế tiếp (F-14 đóng, 12/10)")
1. A32 hiệu chuẩn cổng gốc (biên nhiễu) — trước khi cổng gốc quyết một vòng sửa.
2. A33 sửa luật THAM KHẢO hỏng (A12, A13, R01).
3. A29 cache trang theo cảnh (`checks-k43` @3a00e91, chưa đạt tiêu chí so byte).
4. A34–A37 (Tập 7 giao với các CHẶN này, chủ dự án chấp nhận).
5. A38–A41 (tổng kết Tập 7). Còn mở cũ: A5, A7, A8, A11. LOCK hiện hành `dc4981b3…` (K4.2b).
