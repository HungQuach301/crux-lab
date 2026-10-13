# PLAN kênh Crux (≤ 1 trang) — cập nhật 13/10/2026 (P4 Tập 7: đã đăng → Tập 8)

PLAN của từng tập: `episodes/epNNN/PLAN.md` (mẫu `playbook/templates/PLAN-tap.md`). PLAN Tập 1 cũ: `archive/ep001-v1/PLAN.md`. Thẩm quyền: `CHARTER.md` → `decisions/` (mới nhất D-012).

## Tập hiện hành
| Tập | Đề tài | Format | Nhánh | Trạng thái |
|---|---|---|---|---|
| 3 | savings bond vs T-bills | `lab` | — | **đã đăng 09/10** |
| 4 | #3 giới hạn $500,000 khi bán nhà | — | — | **KHÔNG đăng** (chủ dự án 09/10: không đủ chất lượng — hình nghèo, nhiều chữ; sổ gu) |
| 5 | #17 PMI 10 % trả trước | `101` | — (đã merge `main` 6e0ae01) | **đã đăng 09/10**; tổng kết `tongket-t5/` áp xong (D-011) |
| 6 | #12 "Does a 2% Annuity Raise Really Keep Up With Prices?" | `101` | — (merge squash `main` 99e90d4) | **G3: chờ chủ dự án đăng**; tổng kết `tongket-t6/` đã trả lời + áp (`ANSWER.md`) |
| 7 | #13 "30-Year Mortgage Paid Off in 15 Years: What It Really Costs" | `lab` 10:06,7 | — (merge squash `main`, bản đầy đủ ở nhánh `ep007`) | **đã đăng 13/10** (G3); tổng kết: `episodes/ep007/TONGKET-INPUT.md` (a–q) — phiên tổng kết riêng |
| **8** | **#20 thuê vs mua — phát lại lịch sử thật** | `lab` (f14 opt-in) | `ep008` | **G1 chờ chủ dự án** (`episodes/ep008/gates/G1.md`): điều kiện G1 lô tỉ lệ thuê/giá ĐẠT (Census HVS 4,83–5,59 % chờ xác minh PDF + độ nhạy) → giữ #20; C2 6/6; cần C3 (P2); lô K Tập 8 + kind mới trước C4 |

**Tiếp:** phiên tổng kết Tập 7 (`episodes/ep007/TONGKET-INPUT.md`; chủ dự án duyệt trước khi sửa playbook/checks) → lô K Tập 8 (`checks-appeal.md` A34–A37 + kind Tập 8) → **"Chạy Tập 8"** (P1). Bài học P4 cần áp trước Tập 8: bộ lấy mẫu trang chạy ở C4/C5 trước G2 (TONGKET o).

## Việc treo
- **F-14 nhịp hình**: đầu bài `tongket-t6/F14-brief.md` (chủ dự án mở `factory-f14` song song); **lô K Tập 7**: `episodes/ep007/K-brief.md` (kind mới) + A29–A31, trước C4. Hồ sơ q01/q17 + §4: xong 11/10. **EL:** `user_read` bật; còn 72.750 / 144.034 ký tự (11/10, làm mới 01/11).
- **Phiên K lô (tongket-t5 §4, D-011 Q3):** chạy **song song Tập 6 P1**, merge `main` **trước C3** Tập 6 (hàng chờ dưới).
- **Nhạc hiệu kênh** (episode.md §5b): dựng ở Tập 6, chủ dự án duyệt **bằng clip có âm ở C3 Tập 6**.
- **Thước chỉ báo** (episode.md §2b, `toolkit/indicators/`): báo ở Tập 6, chưa là ngưỡng; thước xếp sai thứ tự hiệu chuẩn đã bỏ.
- **M4 phải hiệu chuẩn lại ở G1 Tập 6:** ngưỡng móc đặt trên trục 2,4 từ/s; ở hằng mới 2,75 từ/s kịch bản Tập 5 đã duyệt cho M4 = 13,5 s (TRƯỢT) — G1 Tập 6 nêu tên.
- Nhà máy: `toolkit/factory/BACKLOG.md` (giữa tập chỉ sửa CHẶN + CHÍNH của tập đang làm; việc khác gom đầu tập, nhánh `factory-*`).

## Hàng chờ phiên K (`checks-appeal.md`, thứ tự Phiên T5)
0. **K4.2 (11/10, lô K Tập 7): kind `term-pair-weekly-replay` + SH06 (A30)** — chỉ thêm, tự merge (D-008 §2), LOCK K4.2 `d9a694e5…` → K4.2b `dc4981b3…`; S01 Tập 7 59 mục 0 lệch, 57/57 claim, 8/8 bất biến. Tập 7 khai khối `model` như `checks-runs/K42/contract-ep007-draft.json`. **K4.2b (11/10, gói 1a, 2b):** F07 theo format (101 8–9 · lab 9–11 · deep 14–17 phút, CHÍNH), S14 deep 2–3 mid-roll cách ≥ 180 s, S15 sàn deep 840 s; `packets.py tally` mặc định rubric mới. A29 hoãn tới container dựng.
0. **K4.0.2 (09/10): kind `fixed-raise-vs-index-windows` cho Tập 6** — LOCK `1b83d940…`; S01 Tập 6 89 khoá 0 lệch, 45/45 claim, 8/8 bất biến. Tập 6 khai `model.kind` + `index.name: "cpiu"` (mẫu `checks-runs/K402/contract-ep006-draft.json`). **K4.1 đã lên main (09/10, LOCK `4d688acd…`)**: V11 glyph/plate (REVIEWER đọc `plateOverGraphics` mỗi C5), F11 nhà máy (phải ĐẠT trên cây C5 thật Tập 6 trước G2, trượt → K2), rubric khuyên chạy thử C4 Tập 6 (`tally` mặc định rubric cũ).
1. Hỏi chủ dự án một gói (sửa luật cũ): **A22** V11 glyph/plate → **A10 + A16** F11/F12 đọc từ nhà máy → **A9 + A21** rubric khuyên.
2. ~~Chỉ thêm (D-008 §2): A20 → A17, A14, A18 → A13, A19, A24 → A23 → A25, A26~~ — **XONG, khoá K4.0 → K4.0.1** (LOCK `79aeec0d…`, 08/10; K4.0.1 = sửa theo REVIEWER): S19 CHẶN; S20, S21 CHÍNH; V14, R07, R08, T4, V15, V17, S22 THAM KHẢO (chỉ báo, chưa hiệu chuẩn). Selftest Python 324/324, trang 64/64; 89/89 luật cũ trùng trước/sau trên Tập 3–5. A12 xong.
3. Báo cáo/chữ: A15, A12. Còn mở: A5, A7, A8, A11.
