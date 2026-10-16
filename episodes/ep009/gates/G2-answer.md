# G2 — câu trả lời của chủ dự án (Tập 9, 17/10) — chép nguyên văn

> G2 Tập 9 — chủ dự án 17/10:
> 1 Content ID "Origami": 0 claim — bản xem 720p tải lên YouTube Studio riêng tư 17/10, "Kiểm tra ban đầu": Bản quyền "Không phát hiện vấn đề nào", Nguyên tắc cộng đồng "Không phát hiện vấn đề nào". Điều kiện G2 đạt; ghi AUTHORSHIP + RIGHTS dòng nhạc.
> 2 đổi "about 3 out of 4 times" (lời + nhãn hình) + S14.2 "many of the piles dipped below where they started".
> 3 thêm ", in dollars of the day" vào S04.2.
> 4 giữ độ dài, ghi ngoại lệ F07 do chủ dự án quyết (không độn; 2 mid-roll).
> 5 không cần (chọn 6a).
> 6 cắt a + b + c, KHÔNG xem lại (tôi xem bản phát hành ở G3).
> 7 giữ "Last time".
> 8 giữ cine d1 tắt, không vòng 3.
> 9 duyệt SH1 (chỉnh mốc theo 6c).
> L3: chủ dự án không chấm ở G2 (để trống; chấm ở G3).
> Chép vào gates/G2-answer.md, taste-ledger, AUTHORSHIP, ledger; commit, push, đóng chặng.
> M6 (phiên mới, lượt phiên này > 150): một lượt 1080p duy nhất gộp mọi sửa câu 2–6 + S07 (gắn claim 14 số trên hình) + C07 (tường cột, hàng đống tràn khung) + V03/V11 nhãn + ghi lại transitions.json từ splice.py --transitions; sinh lại giọng các câu đổi (kiểm EL trước); checks đủ bộ 1080p (cache A29); Short SH1; gói chữ (mô tả có ghi công "Origami" đúng mẫu tác giả + nguồn French/Shiller); giao nhánh tạm như ep008-delivery (kèm 720p xem trước) → G3.
> Trần chi M6 $8 cứng. Ghi vào lessons cho Tổng kết: (i) giờ máy thật của cine (1080p ≈ 12 h, checks ≈ 8 h); (ii) V12 543 mẫu, 9/10 thấp nhất ở đoạn có lớp; (iii) "chỗ muốn tua" trượt 2 tập liền vì lời → thêm câu "chỗ muốn tua" vào kiểm mù kịch bản C2.
> Ràng buộc giữ nguyên: không in hay ghi khoá ra đâu; headless khoá Console, 0 agent con (kể cả bên trong headless); dừng bằng PID đã xem trong ps (không pkill -f/pgrep -f); việc > 1,5 h chạy tiếp được (RESUME=1); push sau mỗi bước lớn; không thumbnail tự dựng; không nhà cung cấp video/ảnh/nhạc AI.

## Bảng quyết định → việc (M6)
| # | Quyết định | Việc ở M6 |
|---|---|---|
| 1 | Content ID "Origami": **0 claim** (17/10, riêng tư, "Kiểm tra ban đầu" bản quyền + nguyên tắc cộng đồng không vấn đề) — điều kiện G2 ĐẠT | RIGHTS M-BUCKLEY-ORIGAMI (đã ghi) · AUTHORSHIP · ghi công đúng mẫu ở mô tả |
| 2 | S02.2 "about **3 out of 4** times" (lời + nhãn "with cash: buyer ahead about 3 out of 4" + bảng điểm) · S14.2 "**many of the piles** dipped below where they started" | sửa script.md + numbers/claims display; sinh lại S02, S14 |
| 3 | S04.2 thêm "**, in dollars of the day**" | sinh lại S04 (take dẫn xuất lặng neo `anchor_gap.py` chạy lại) |
| 4 | **Giữ 8:44 — ngoại lệ F07 do chủ dự án quyết** (không độn; 2 mid-roll) | ghi ngoại lệ ở gói G3 + M6-checks |
| 5 | không cần (S18.4 bỏ theo 6a) | — |
| 6 | cắt **a** (bỏ S18.4) + **b** (S24.1 "The rest of the limits are on the card: US only, no taxes on gains or on the home, and renters who never skip a month.") + **c** (S14.4–S14.5 → "The replay assumes every renting twin kept investing; one who sells in a crash is not on this street."); **không xem lại** (xem bản phát hành ở G3) | sinh lại S14, S18, S24; tính lại mid-roll MR2, nhạc, spine |
| 7 | giữ "Last time" S13.1 | — |
| 8 | giữ `cine` d1 tắt, không vòng 3 | — |
| 9 | duyệt SH1, chỉnh mốc theo 6c | `episode.yaml shorts` from/to sau khi lời S14 đổi |
| L3 | không chấm ở G2 (chấm ở G3) | gói G3 có phiếu L3 |
| M6 | một lượt 1080p gộp câu 2–6 + S07 (claim 14 số) + C07 (tường cột, hàng đống) + V03/V11 nhãn + `splice.py --transitions`; kiểm EL trước; checks đủ bộ 1080p (cache A29); Short SH1; gói chữ (ghi công "Origami" + nguồn French/Shiller); giao nhánh tạm (+ 720p) → G3; **trần M6 $8 cứng** | phiên mới "Chạy Tập 9" |
