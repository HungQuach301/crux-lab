# Chạy Tập {N} — một phiên điều phối (D-008)

Chủ dự án mở phiên mới và gõ: **"Chạy Tập {N}"** (hoặc "Chạy Tập {N}, đề tài #k"). Một phiên điều phối chạy hết tập, **dừng ở G1 và G2** (và chờ G3 khi giao hàng). Trần token/agent do chủ dự án ghi khi mở (mặc định ≤ 1,5 triệu token, ≤ 25 agent mỗi lượt từ mở đến điểm dừng).

## Luật điều phối
- Mở bằng `bash toolkit/verify.sh ep{NNN}`; đọc `CHARTER.md`, `playbook/quality-framework.md`, `playbook/episode.md`, `episodes/ep{NNN}/PLAN.md` (mục "Phiên sau đọc"), `ledger.md`.
- Việc nặng (Việc 0, WRITER, dựng, checks, kiểm mù, REVIEWER) → **agent MỚI, đầu bài ngắn**; phiên chính chỉ đọc tóm tắt; không gọi lại agent cũ.
- **REVIEWER bắt buộc** trước mọi gói/issue gửi chủ dự án; không bỏ vì token — sắp chạm trần thì dừng hỏi.
- Mọi commit đẩy lên `ep{NNN}`; ghi token/agent thực vào `ledger.md` và PLAN §5.

## Chặng (nội dung chi tiết: `P1.md`, `P3.md`)
1. **Việc 0 → C1 → C2 → G1** (`P1.md`). Cần kind mới → giao phiên K; khoá K tự merge khi đủ điều kiện D-008 §2, không thì hỏi.
2. **Ký hiệu mới (≤ 2):** không có cổng C3 riêng — dựng bằng nhà máy, kiểm mù nghĩa trong lượt C4 (cổng gốc tự động), chủ dự án duyệt ở G2.
3. **C4 → C5 → Shorts → G2** (`P3.md` việc 1–4). Dừng ở G2.
4. Sau G2: áp quyết định, giao hàng, G3, merge `main` (`P3.md` việc 5–7).

Chủ dự án trả lời G1/G2/G3 ngay trong phiên; chỉ sang chat chiến lược khi có ngoại lệ hoặc vượt trần.
