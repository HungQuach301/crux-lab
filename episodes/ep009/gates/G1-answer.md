# G1 — câu trả lời của chủ dự án (Tập 9, 15/10) — chép nguyên văn

> G1 Tập 9 — chủ dự án 15/10:
> 1 b, sửa: gửi thư hỏi French/CRSP song song, làm tiếp trên French; nếu chưa có trả lời trước M6 thì dùng (a) — chỉ số tổng hợp suy ra, ghi nguồn trên hình + mô tả, không phân phối lại tệp; ghi AUTHORSHIP + RIGHTS D-FRENCH.
> 2 a — vòng 2 khối "số dày" S10–S17 (bớt mốc năm nói, giữ hình phố) + kiểm mù lại trước khi sinh lời; độ dài: không độn, chỉ thêm chất có nguồn nếu cần.
> 3 b-Z — nhạc = Scott Buckley "Origami" (CC BY 4.0): ghi công ĐÚNG mẫu tác giả yêu cầu (tên bài, tác giả, link trang bài, giấy phép) trong mô tả; RIGHTS dòng nhạc + bản chụp trang giấy phép + SHA; sổ gu G-016 + quyết định mới; kiểm Content ID là điều kiện G2. Ngoại lệ animatic: dựng animatic 540p xám + cổng gốc là bước ĐẦU chặng sau, trước M3; trượt → trước/sau vào G2.
> Tiêu đề: T1 "Rent and Invest the Difference? We Replayed Every Start Month Since 1991".
> Chép vào gates/G1-answer.md, taste-ledger, AUTHORSHIP, ledger; commit, push, đóng chặng. Mở chặng sau bằng phiên mới (lượt phiên này gần 150). Trần chi chặng sau G1 → G2: $15 cứng. Kiểm hạn mức ElevenLabs trước khi sinh lời cả tập; còn < 15.000 ký tự → dừng, báo. Ràng buộc giữ nguyên (không in khoá, 0 agent con, dừng bằng PID đã xem trong ps, push sau mỗi bước lớn, không thumbnail tự dựng, không nhà cung cấp video/ảnh/nhạc AI).

## Sửa câu 1 (chủ dự án 15/10, chặng sau G1) — chép nguyên văn
> Chủ dự án 15/10 — SỬA G1 câu 1: KHÔNG gửi thư cho French/CRSP. Chọn (a): dùng Kenneth R. French Data Library, chỉ công bố kết quả suy ra (tỉ lệ, giá trị danh mục giả định), không phân phối lại tệp gốc; ghi nguồn trên hình + mô tả: "Stock returns: Kenneth R. French Data Library (Fama/French factors, total return); cross-checked with Robert Shiller data." Ghi vào gates/G1-answer.md (phần sửa), AUTHORSHIP.md, RIGHTS D-FRENCH; bỏ mục treo "thư French/CRSP" khỏi PLAN; xoá hoặc đánh dấu gates/thu-french-crsp.md là "không dùng". Không dừng việc đang chạy.

Việc: RIGHTS `D-FRENCH` (dòng sửa) · AUTHORSHIP (dòng 15/10 sửa câu 1) · PLAN bỏ mục treo thư · `gates/thu-french-crsp.md` đánh dấu KHÔNG DÙNG · dòng nguồn trên hình (thẻ phương pháp/giới hạn) + mô tả M6 dùng đúng câu trên. Câu 1 b trong bảng dưới **bị thay** bởi phần sửa này.

## Bảng quyết định → việc
| # | Quyết định | Việc | Trạng thái |
|---|---|---|---|
| 1 | **French: 1 b có sửa** — thư hỏi French/CRSP song song, làm tiếp trên French; chưa trả lời trước M6 → (a): chỉ số tổng hợp suy ra, ghi nguồn trên hình + mô tả, không phân phối lại tệp | thư nháp `gates/thu-french-crsp.md` (**chủ dự án gửi** — phiên không có hộp thư); RIGHTS `D-FRENCH`; AUTHORSHIP | ghi xong; thư chờ gửi |
| 2 | **Kịch bản 2 a** — vòng 2 `số dày` S10–S17 (bớt mốc năm nói, giữ hình phố) + kiểm mù lại **trước khi sinh lời**; không độn, chỉ thêm chất có nguồn | chặng sau, sau animatic; `--g1-short` khi độ dài vẫn < 9:00 | chặng sau |
| 3 | **Nhạc 3 b-Z = Scott Buckley "Origami" (CC BY 4.0)** — ghi công đúng mẫu tác giả trong mô tả; RIGHTS + bản chụp + SHA; G-016 + quyết định mới; **kiểm Content ID = điều kiện G2** | RIGHTS `M-BUCKLEY-ORIGAMI`; `decisions/D-014.md`; sổ gu G-016 · Tập 9; ghi công dưới đây; `episode.yaml audio.music` | ghi xong; dựng ở M3 |
| 3 | **Ngoại lệ animatic** — animatic 540p xám + cổng gốc là bước ĐẦU chặng sau, trước M3; trượt → trước/sau vào G2 | PLAN §2 mục 1 | chặng sau |
| T | **Tiêu đề T1** "Rent and Invest the Difference? We Replayed Every Start Month Since 1991" | dùng ở M6 | chốt |
| — | Chặng G1 → G2: **trần $15 cứng**; EL < 15.000 ký tự trước khi sinh lời cả tập → dừng, báo | PLAN §5 | chặng sau |

**Dòng ghi công trong mô tả (M6, mẫu tác giả + link trang bài + giấy phép):**
`Music: "Origami" by Scott Buckley — https://www.scottbuckley.com.au/library/origami/ — released under CC-BY 4.0 (https://creativecommons.org/licenses/by/4.0/). www.scottbuckley.com.au · Edited and mixed under narration.`
(Mẫu tác giả trên trang bài: "'Origami' by Scott Buckley - released under CC-BY 4.0. www.scottbuckley.com.au".)
