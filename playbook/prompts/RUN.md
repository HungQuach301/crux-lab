# Chạy Tập {N} — một phiên điều phối (D-008)

Chủ dự án mở phiên mới và gõ: **"Chạy Tập {N}"** (hoặc "Chạy Tập {N}, đề tài #k"). Một phiên điều phối chạy hết tập, **dừng ở G1, C3 (khi tập có hình mới) và G2** (và chờ G3 khi giao hàng). Token cả tập: **mức cảnh báo 3,0 triệu, phân bổ theo loại việc** (`episode.md` §8; D-009: chỉ cảnh báo, báo số thực, không cắt bước chất lượng). ≤ 40 agent con; kiểm mù không tính vào số agent (headless, ≤ 120 lượt).

## Luật điều phối
- Mở bằng `bash toolkit/verify.sh ep{NNN}`; đọc `CHARTER.md`, `playbook/quality-framework.md`, `playbook/episode.md`, `episodes/ep{NNN}/PLAN.md` (mục "Phiên sau đọc"), `ledger.md`.
- Việc nặng (Việc 0, WRITER, dựng, checks, REVIEWER) → **agent MỚI, đầu bài ngắn**; phiên chính chỉ đọc tóm tắt; không gọi lại agent cũ.
- **Kiểm mù → headless**, không agent con: `bash toolkit/blind/headless.sh <đầu-bài> <ra.json> [--read]` (≈ 10 nghìn token/lượt). Số người đọc, dừng sớm và vòng bỏ: `episode.md` §2.
- **Móc:** điều kiện M1–M5 đo trên table read trước G1 (`episode.md` §3.9).
- **Giọng:** take ở `episodes/ep{NNN}/voice-takes/` được commit, không sinh lại khi đổi container.
- **Chất lượng là ưu tiên tuyệt đối (D-009):** lỗi CHÍNH sửa trước G2; sửa nghĩa bằng hình trước, nhãn là cách cuối; G2 cần phiếu L3 ≥ 4 mọi dòng.
- **REVIEWER bắt buộc** trước mọi gói/issue gửi chủ dự án; không bỏ vì token — vượt mức cảnh báo thì báo số thực trong gói, không dừng bước chất lượng.
- **Lượt đạo diễn** (chẩn đoán) trên bản 540p trước render bản cuối, mọi đoạn có hình mới (`quality-framework.md` §10).
- Mọi commit đẩy lên `ep{NNN}`; ghi token/agent thực **theo loại việc** và **giờ render thực** vào `ledger.md` và PLAN §5.

## Chặng (nội dung chi tiết: `P1.md`, `P3.md`)
1. **Việc 0 → C1 → C2 → G1** (`P1.md`). Cần kind mới → giao phiên K; khoá K tự merge khi đủ điều kiện D-008 §2, không thì hỏi.
2. **Hình mới → C3** (D-009 b, không trần số): ký hiệu, vật thể 3D, hero object, mẫu chuyển cảnh dựng bằng nhà máy (`toolkit/factory/world/` cho đoạn thế giới), cổng gốc, rồi chủ dự án duyệt bằng **clip có chuyển động và âm**.
3. **C4 → C5 → Shorts → G2** (`P3.md` việc 1–4). Dừng ở G2.
4. Sau G2: áp quyết định, giao hàng, G3, merge `main` (`P3.md` việc 5–7).

Chủ dự án trả lời G1/C3/G2/G3 ngay trong phiên; chỉ sang chat chiến lược khi có ngoại lệ.
