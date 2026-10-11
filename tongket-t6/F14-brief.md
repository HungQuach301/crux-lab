# Đầu bài phiên nhà máy F-14 — nhịp hình trước khi kéo dài tập

**Chủ dự án mở song song phiên P1 Tập 7** (duyệt 11/10, tổng kết Tập 6 câu 1d; dùng thử 3 tập rồi hiệu chuẩn lại). P1 không làm F-14. Dán khối dưới vào phiên mới.

```
Phiên nhà máy F-14 (nhịp hình), nhánh `factory-f14` từ `main` mới nhất. CHARTER §2.3: việc không phải tập; giúp Tập 7–8 (`deep` chỉ mở được khi F-14 đạt đích trước G1 lô — episode.md §9).
Mở: `bash toolkit/verify.sh factory-f14`.
Đọc (≤ 8): CHARTER.md · playbook/lessons.md (T6-6) · toolkit/factory/BACKLOG.md (F-14) · toolkit/factory/README.md · toolkit/factory/world/README (nếu có) · toolkit/indicators/spine_pace.py · tongket-t6/REPORT.md §2 (d) · episodes/ep006/HUONG-DAN-DANG.md.
Việc (theo BACKLOG F-14):
 (a) chuyển động nền liên tục CÓ NGHĨA khi máy đứng yên: vật thể dữ liệu sống theo thời gian của câu (lịch lật, thùng sáng/mờ dần, séc lớn dần) — không trang trí (gen CHARTER §4: low-poly, màu kênh, không mặt, không chi tiết vô nghĩa); máy vẫn đứng yên ở từ khoá (quy tắc 2).
 (b) cờ `change: major|minor` + `anchor: true` trên spine; bước spine CẢNH BÁO quãng có lời > 8 s không có thay đổi `major`.
 (c) nhãn neo vào từ: mốc hiện nhãn = mốc từ trên spine ±0,2 s; quy tắc 7 chỉ giữ 5 s đầu.
Đo (ý đồ + ngưỡng ghi trước vào `toolkit/factory/f14/INTENT.md` trước khi chạy): dựng lại Tập 6 từ `main` (cùng kịch bản, giọng, nhạc) với F-14; đối chứng = master bản giao SHA-256 f96da0ea19e6426aa3b4bd37759f3e7c8fb9819e489a1fab317683fd5edcaa74 (tải theo `episodes/ep006/HUONG-DAN-DANG.md`, `sha256sum -c`). Đích: quãng tĩnh có lời > 8 s 7 → 0 (`spine_pace.py --labels`) · freezedetect 206 s → < 60 s · R07 70,3 % → ≥ 90 % · nhãn "3%" trễ 1,26 s → ≤ 0,2 s · cổng gốc không tụt (khoá nghĩa, 20/23 nhịp ĐẠT ở bản giao) · CHẶN 0. Thước spine chưa hiệu chuẩn (A23 đối chứng dương 2/4) → chỉ báo; freezedetect + R07 + cổng gốc là số chính.
Không sửa `checks/` (luật khoá; đề xuất → `checks-appeal.md`). Việc > 1,5 h tách lệnh chạy tiếp được (episode.md §11b). Việc nặng: headless khoá Console (`toolkit/api.sh`), 0 agent con trừ khi cần công cụ phiên. Trần chi cảnh báo $45.
Đóng: `toolkit/factory/f14/REPORT.md` (bảng đích/thật trên bản dựng lại vs đối chứng, ảnh trước/sau 3 quãng tĩnh dài nhất, chi phí, token) + REVIEWER headless. Đạt → báo phiên điều phối Tập 7 (phiên điều phối merge `main`, CHARTER §7). Trượt → báo số, không hạ đích. Không chạm tệp tập 7/8.
```
