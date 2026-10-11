# PLAN kênh Crux (≤ 1 trang) — cập nhật 11/10/2026 (P1 Tập 7: G1 lô Tập 7–8)

PLAN của từng tập: `episodes/epNNN/PLAN.md` (mẫu `playbook/templates/PLAN-tap.md`). PLAN Tập 1 cũ: `archive/ep001-v1/PLAN.md`. Thẩm quyền: `CHARTER.md` → `decisions/` (mới nhất D-012).

## Tập hiện hành
| Tập | Đề tài | Format | Nhánh | Trạng thái |
|---|---|---|---|---|
| 3 | savings bond vs T-bills | `lab` | — | **đã đăng 09/10** |
| 4 | #3 giới hạn $500,000 khi bán nhà | — | — | **KHÔNG đăng** (chủ dự án 09/10: không đủ chất lượng — hình nghèo, nhiều chữ; sổ gu) |
| 5 | #17 PMI 10 % trả trước | `101` | — (đã merge `main` 6e0ae01) | **đã đăng 09/10**; tổng kết `tongket-t5/` áp xong (D-011) |
| 6 | #12 "Does a 2% Annuity Raise Really Keep Up With Prices?" | `101` | — (merge squash `main` 99e90d4) | **G3: chờ chủ dự án đăng**; tổng kết `tongket-t6/` đã trả lời + áp (`ANSWER.md`) |
| **7** | **#13 15 năm vs 30 năm trả trong 15** (D-012) | `lab` (F-14 chưa đạt trước G1) | `ep007` | **G1 lô chờ** (`episodes/ep007/gates/G1.md`); phiên kế P2 (C3): prompt `episodes/ep007/PLAN.md` mục 7 |
| 8 | #20 thuê vs mua — phát lại lịch sử thật (dự phòng #6) | `lab` (đề xuất G1 lô) | — | hồ sơ `topics-r2/machine/rent-buy-1/` §4 ĐẠT; chờ G1 lô (điều kiện tỉ lệ thuê/giá có nguồn) |

**Tiếp Tập 7:** phiên mới, dán prompt `episodes/ep007/PLAN.md` mục 7 + câu trả lời G1.

## Việc treo
- **F-14 nhịp hình**: đầu bài `tongket-t6/F14-brief.md` (chủ dự án mở `factory-f14` song song); **lô K Tập 7**: `episodes/ep007/K-brief.md` (kind mới) + A29–A31, trước C4. Hồ sơ q01/q17 + §4: xong 11/10. **EL:** khoá thiếu `user_read` (hạn mức chưa đọc được).
- **Phiên K lô (tongket-t5 §4, D-011 Q3):** chạy **song song Tập 6 P1**, merge `main` **trước C3** Tập 6 (hàng chờ dưới).
- **Nhạc hiệu kênh** (episode.md §5b): dựng ở Tập 6, chủ dự án duyệt **bằng clip có âm ở C3 Tập 6**.
- **Thước chỉ báo** (episode.md §2b, `toolkit/indicators/`): báo ở Tập 6, chưa là ngưỡng; thước xếp sai thứ tự hiệu chuẩn đã bỏ.
- **M4 phải hiệu chuẩn lại ở G1 Tập 6:** ngưỡng móc đặt trên trục 2,4 từ/s; ở hằng mới 2,75 từ/s kịch bản Tập 5 đã duyệt cho M4 = 13,5 s (TRƯỢT) — G1 Tập 6 nêu tên.
- Nhà máy: `toolkit/factory/BACKLOG.md` (giữa tập chỉ sửa CHẶN + CHÍNH của tập đang làm; việc khác gom đầu tập, nhánh `factory-*`).

## Hàng chờ phiên K (`checks-appeal.md`, thứ tự Phiên T5)
0. **K4.2 (11/10, lô K Tập 7): kind `term-pair-weekly-replay` + SH06 (A30)** — chỉ thêm, tự merge (D-008 §2), LOCK trong commit khoá; S01 Tập 7 59 mục 0 lệch, 57/57 claim, 8/8 bất biến. Tập 7 khai khối `model` như `checks-runs/K42/contract-ep007-draft.json`. **Chờ chủ dự án:** gói `checks-runs/K42/GOI-chu-du-an.md` (A28 rubric khuyên mặc định; A31 độ dài/mid-roll theo format — cần trước C5 nếu tập `deep`). A29 hoãn tới container dựng.
0. **K4.0.2 (09/10): kind `fixed-raise-vs-index-windows` cho Tập 6** — LOCK `1b83d940…`; S01 Tập 6 89 khoá 0 lệch, 45/45 claim, 8/8 bất biến. Tập 6 khai `model.kind` + `index.name: "cpiu"` (mẫu `checks-runs/K402/contract-ep006-draft.json`). **K4.1 đã lên main (09/10, LOCK `4d688acd…`)**: V11 glyph/plate (REVIEWER đọc `plateOverGraphics` mỗi C5), F11 nhà máy (phải ĐẠT trên cây C5 thật Tập 6 trước G2, trượt → K2), rubric khuyên chạy thử C4 Tập 6 (`tally` mặc định rubric cũ).
1. Hỏi chủ dự án một gói (sửa luật cũ): **A22** V11 glyph/plate → **A10 + A16** F11/F12 đọc từ nhà máy → **A9 + A21** rubric khuyên.
2. ~~Chỉ thêm (D-008 §2): A20 → A17, A14, A18 → A13, A19, A24 → A23 → A25, A26~~ — **XONG, khoá K4.0 → K4.0.1** (LOCK `79aeec0d…`, 08/10; K4.0.1 = sửa theo REVIEWER): S19 CHẶN; S20, S21 CHÍNH; V14, R07, R08, T4, V15, V17, S22 THAM KHẢO (chỉ báo, chưa hiệu chuẩn). Selftest Python 324/324, trang 64/64; 89/89 luật cũ trùng trước/sau trên Tập 3–5. A12 xong.
3. Báo cáo/chữ: A15, A12. Còn mở: A5, A7, A8, A11.
