# Chạy Tập N — prompt mẫu duy nhất (D-013; thay RUN.md, P1–P3.md — lưu ở `archive/prompts-v4/` — và "prompt phiên kế" tự viết ở PLAN tập §7)

Chủ dự án dán **nguyên khối dưới**, chỉ đổi số tập và (nếu có) dán câu trả lời cổng. Phiên tự đọc trạng thái, không cần prompt dài. Quy trình: `episode.md` §1.

```
Chạy Tập {N}.
<<Nếu đang trả lời cổng: dán "G1: …" / "G2: …" / "G3: đã đăng <link>". Trống = mốc kế theo PLAN tập.>>
```

## Phiên làm gì với dòng đó (luật cố định, không chép vào prompt)
1. Mở: `bash toolkit/verify.sh ep{NNN}` (nhánh chưa có → tạo từ `origin/main`). Đọc `CHARTER.md`, `playbook/episode.md`, `playbook/story.md`, `episodes/ep{NNN}/PLAN.md` (nếu có) — PLAN tập mục 1 ghi **mốc hiện tại M1–M6** và mục 6 ghi ≤ 8 tệp cần đọc.
2. Có câu trả lời cổng → chép nguyên văn vào `gates/G{x}-answer.md`, sổ gu, `AUTHORSHIP.md`, ledger; commit + push.
3. Chạy **đúng một chặng** tới điểm dừng chờ chủ dự án kế tiếp:
   - chưa có tập → M1 + M2 → **G1** (kịch bản + vật thể/animatic + tiêu đề nháp);
   - sau G1 → M3 + M4 + M5 → **G2** (phiếu L3 trên nháp);
   - sau G2 → M6 (1080p một lần, 1 Short, gói chữ không thumbnail) → **G3**; sau G3 → merge `main` (squash), PLAN kênh.
4. Việc nặng: headless khoá Console (`toolkit/api.sh`), **0 agent con**; một vai = một lượt headless, thoát ngay. Lệnh > 1,5 h chạy tiếp được (`RESUME=1`, cache). Dừng tiến trình bằng PID đã lưu. **Commit + push sau mỗi bước lớn** (≤ 2 h không push).
5. Mỗi lỗi ≤ 2 vòng; vòng chỉ được giữ khi vượt bản tốt nhất ngoài biên nhiễu; hết vòng → trước/sau vào gói. Line producer ghi sổ chi theo mốc; vượt 150 % ngân sách mốc → báo trong gói, không cắt bước chất lượng.
6. Đóng chặng: PLAN tập ≤ 1 trang (mục 1 = mốc kế, mục 5 = 4 số token + đọc cache + lượt + $ + giờ máy + lượt chạm), REVIEWER headless soát gói G1, ý đồ kiểm định trước M5, gói G2, commit, push, báo đường dẫn gói. **Dừng.**
7. Ngoài G1/G2/G3 chỉ hỏi khi gặp ngoại lệ CHARTER §5 (đổi kịch bản đã duyệt, số không xác minh, quyền/pháp lý, chi tiêu mới).
