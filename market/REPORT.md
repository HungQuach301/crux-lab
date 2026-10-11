# Báo cáo thị trường — tài chính cá nhân Mỹ trên YouTube (Phiên Thị trường `market-r1`, 11/10/2026)

**Định tính.** Không số liệu thô của kênh khác (Developer Policies III.E.4; số thô ở `~/market-cache/2026-10-11/` ngoài git, xoá/làm mới sau 30 ngày bằng `toolkit/market/purge.py`). Mọi nhãn và tỉ lệ dưới đây là **tự tính, không phải chỉ số YouTube**. Phạm vi: 21 đề tài (19 dòng hàng đợi + 2 "từ hạt giống"), 67 lượt search (30/90 ngày, US, tiếng Anh, 4–20 phút), 58 kênh ứng viên kéo 24 tháng video dài, 34 kênh giữ sau phân loại (`CHANNELS.md`), 35 video lấy bình luận (50 bình luận/video, relevance), 30 thumbnail vượt trội. Hồ sơ từng đề tài: `market/topics/<id>.md`. Cách tính: đầu mỗi tệp `toolkit/market/*.py`.

## 1. Đề tài theo cầu (trừ thời sự)

| Cầu | Đề tài (dòng hàng đợi) | Khoảng trống dữ liệu thật |
|---|---|---|
| **cao** | #13 15 năm vs 30 năm trả trong 15 · #3 giới hạn $500,000 khi bán nhà · #20 thuê vs mua (hạt giống) · #21 nhà cho thuê vs quỹ chỉ số (hạt giống) · #6 bảo hiểm chăm sóc dài hạn 3 % vs 5 % · #11 vay 3 % vs T-bill · #18 du lịch sớm hay chờ khi nghỉ hưu | **cao**: #13, #3 · **vừa**: #20, #21, #6 · **thấp**: #11, #18 |
| **vừa** | #1 vay sau đại học thả nổi/cố định · #5 xe 60 vs 72 tháng · #9 mua điểm lãi · #12 niên kim tăng 2 % · #14 35 % lương cho nhà · #15 khẩn cấp: 401(k) hay thẻ · #16 lỗ cho thuê trên lương $130,000 | cao: #5, #9, #12, #14, #15, #16 · vừa: #1 |
| **thấp** | #2 tăng ca vs việc thứ hai · #4 hoàn thuế $3,000 · #7 trái phiếu tiết kiệm vs T-bill · #8 bán ở tháng 11 · #10 CD 1 năm vs 5 năm · #17 PMI 10 % · #19 chờ lãi xe giảm | cao: #2, #4, #8, #10, #19 · vừa: #17 · thấp: #7 |

- **Cầu** = trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài. **Nhà ở chiếm đỉnh**: 5/7 đề tài cầu cao xoay quanh nhà (vay, mua/thuê, bán, cho thuê). Thuế ngắn hạn và tiền mặt (CD, trái phiếu, hoàn thuế) cầu thấp.
- **Hồi tố:** Tập 3 (#7) và Tập 5 (#17) — hai tập đã đăng — đều rơi vào cầu **thấp**; Tập 6 (#12) **vừa**. Đối chiếu lượt xem 28 ngày ở `market/CALIBRATION.md` (mốc 06/11) là phép thử đầu tiên của nhãn.
- 10/21 đề tài chưa có bình luận đã lọc (video đầu bảng ít bình luận hoặc gắn đề tài lỏng) — câu hỏi khán giả ở các hồ sơ đó ghi "SUY TỪ ĐỀ TÀI", làm mới ở Việc 0.

## 2. Khoảng trống "chưa ai làm bằng dữ liệu"
Haiku đọc 6 video đầu bảng mỗi đề tài: phần lớn là **giả định cố định** (một lãi suất, một lợi suất chạy đều N năm) hoặc **ý kiến không tính**. Phát lại lịch sử thật gần như vắng:
- **Không video đầu bảng nào dùng lịch sử thật (khoảng trống cao):** #13 15 vs 30 năm, #3 bán nhà, #5 xe, #9 điểm lãi, #12 niên kim, #14 35 % lương, #15 401(k) vs thẻ, #16 lỗ cho thuê, #2, #4, #8, #10, #19.
- **Một video có lịch sử thật (vừa):** thuê vs mua, nhà cho thuê vs chỉ số, bảo hiểm chăm sóc dài hạn, vay sau đại học.
- **Đã có ≥ 2 (thấp):** #11 vay 3 % vs T-bill, #18 du lịch khi nghỉ hưu, #7 trái phiếu tiết kiệm.
- **Đối thủ hạt giống cũng giả định cố định** (Logical Money: cổ phiếu ~10 %, nhà ~3–4 %/năm; `teardowns/logical-money.md`). Câu hỏi khán giả nặng nhất ở hai đề tài hạt giống chính là **"kết quả đổi thế nào nếu đổi giả định / năm bắt đầu?"** — đúng thứ chỉ phát lại lịch sử nhiều cửa sổ trả lời được.

## 3. Mẫu đóng gói thắng (vượt trội ≥ 3× so với video thường, cùng kênh)
### Khuôn tiêu đề
1. **"X vs Y: The N-Year Scorecard"** — so sánh hai lựa chọn với một khung thời gian cụ thể (kiểu "một căn cho thuê vs quỹ chỉ số: bảng điểm 15 năm"). Crux: "…Replayed Through Real History".
2. **"Same Start, Different Choice: X vs Y Over N Years"** — lời hứa hai nhân vật xuất phát giống hệt (cụm Logical Money, vượt trội rất cao).
3. **"Is [ngưỡng] Actually Enough? …"** — thử một con số ai cũng nghe (vd "$1 triệu có đủ nghỉ hưu"). Crux: "…Every Start Year Since [năm]".
4. **"[Người như tôi]? What N Years of History Say"** — gọi đúng nhóm người xem + hứa đáp án (khớp bài học Tập 1, `playbook/packaging.md` §6.1).
5. **"What Happens After [ngưỡng]?"** — ngưỡng có tên (cụm Jack Explains Money: $10,000 đầu tiên).
- Đặc trưng tiêu đề (vượt trội so với thường, tự tính): **có số nhiều hơn một chút**, có từ VIẾT HOA nhấn nhiều hơn, độ dài như nhau (~60 ký tự), dấu hỏi và "vs" **không** giúp; năm trong tiêu đề hiếm ở cả hai nhóm. Đuôi "The Real Math" đã bão hoà (≥ 7 kênh dùng, đa số không vượt trội) — không dùng.

### Kiểu thumbnail (Sonnet xem 30 thumbnail vượt trội qua URL, không lưu ảnh)
1. **Chia đôi hai nhân vật / hai con đường** (thuê vs mua, tiết kiệm vs đầu tư) — Crux làm bằng hai người không mặt trong thế giới 3D, cùng xuất phát, hai kết cục.
2. **Một con số lớn + 1–2 từ**, tương phản cao (vàng/đỏ/xanh lá trên nền tối) — số phải là claim của tập.
3. **Biểu đồ / cột như một vật** (cột tiền cao thấp, mũi tên) + dấu hỏi — không mũi tên ngụ ý dự báo.
- Đa số thumbnail vượt trội có **mặt người lớn** biểu cảm (~2/3) — Crux **không dùng** (đặc tả thumbnail kênh: không mặt người); thay bằng hình người không mặt + tương phản. Chữ trên ảnh trung vị ~4–5 từ; Crux giữ ≤ 4 từ lớn (đọc được ở 168×94).

### Cho brief đóng gói (tiếng Anh; `toolkit/market/brief.py` đọc mục này)
- title: X vs Y: The N-Year Scorecard, Replayed Through Real History
- title: Same Start, Different Choice: X vs Y Over N Years
- title: [People like me]? What N Years of Real History Say
- thumbnail: split scene — two faceless figures from the same starting point on two paths in the 3D world, or one big claim number plus 1–2 words; high contrast (yellow/red/green on dark), no faces

## 4. Dải thời lượng
- Video vượt trội **dài hơn** video thường của chính kênh đó: trung vị ~15–16 phút (tứ phân vị ~12–19) so với ~12–13 phút (tự tính, kênh trực tiếp + lân cận). Cụm hạt giống Logical Money 15–18 phút (số chủ dự án ghi).
- Khuôn Crux: `101` 8–9 phút, `lab` 9–11 phút — **ngắn hơn dải vượt trội** ở các đề tài nhà ở (11–22 phút). Không đổi khuôn ở phiên này (quyền chủ dự án); WRITER theo `format`, G1 nêu khi hai dải không giao (`playbook/episode.md` §3.11). Đề tài có thể dài hơn tự nhiên: so sánh hai nhân vật × nhiều cửa sổ lịch sử (`lab` lên trần 11 phút).
- Giờ đăng của video vượt trội dồn vào **sáng giờ Mỹ (12–16 UTC)** và **thứ Hai**; thường đăng trải đều — tín hiệu yếu, chỉ tham khảo cho `HUONG-DAN-DANG.md`.

## 5. Câu hỏi khán giả xuyên đề tài (từ bình luận đã lọc, diễn đạt lại)
1. **"Có tính đủ chi phí ẩn của cả hai bên không?"** (thuế nhà, bảo hiểm, sửa chữa, phí giao dịch / tiền thuê tăng, chuyển nhà bị ép).
2. **"Kết quả đổi thế nào nếu đổi giả định — lãi vay, lợi suất, năm bắt đầu, ở bao lâu?"**
3. **"Người thuê có thật sự đầu tư phần chênh không?"** (hành vi, không phải toán).
4. **"Chuyện gì xảy ra khi đời có biến cố"** — mất việc, chủ nhà bán nhà, cần chăm sóc dài hạn.
5. **"Lựa chọn nào hợp giai đoạn đời tôi?"** — nghỉ hưu, góa, con nhỏ, cần linh hoạt.
Câu 2 là lợi thế riêng của Crux (nhiều cửa sổ lịch sử thật); câu 1 và 4 là điểm yếu đối thủ khán giả nêu nhiều nhất. Đề tài khán giả yêu cầu đã vào hàng đợi nhãn "từ khán giả" (#22–25).

## 6. Khuyến nghị đề tài Tập 7 + 8 (G1 lô 2 tập, D-011 Q1)
Máy không chọn đề tài (D-004); đây là ứng viên cho G1 lô Tập 7–8, chủ dự án quyết. PLAN kênh hiện đề xuất #2 cho Tập 7.

| Ứng viên | Ưu | Nhược | Tác động (dự kiến) | Rủi ro |
|---|---|---|---|---|
| **#13 15 năm hay 30 năm trả trong 15** — **khuyến nghị Tập 7** | cầu **cao** + khoảng trống **cao** (không video đầu bảng nào phát lại lịch sử); hồ sơ vòng 2 đã có `calc.py`; khung hai nhân vật xuất phát giống hệt hợp tự nhiên (cùng nhà, khác kỳ hạn); trả lời câu "prepay hay đầu tư" khán giả hỏi nhiều | thiếu `model.json` + `statements.json` (bổ sung ở Việc 0); có thể cần kind mới → phiên K | cao — chủ đề nhà, khán giả lớn, dải vượt trội 11–23 phút cho phép `lab` | không nói giá trị của linh hoạt; "history, not a forecast"; giáp đề tài #11 |
| **#20 Thuê vs mua — phát lại lịch sử thật** — **khuyến nghị Tập 8** | cầu **cao**, bình luận đã lọc dồi dào (nhiều nhất trong các đề tài), video hạt giống vượt trội rất cao dùng giả định cố định → điểm khác biệt rõ nhất của Crux; khuôn hai nhân vật đã được chứng minh | **chưa có hồ sơ máy đề tài** (cần chạy máy đề tài trước P1 Tập 8, ~1 phiên); dữ liệu giá thuê/giá nhà dài hạn cần kiểm quyền tái bản | rất cao nếu làm tốt; đối đầu trực diện video hạt giống | chỉ số giá nhà ≠ căn nhà; giá thuê CPI ≠ hợp đồng; bị so với video 17 phút — `lab` 11 phút phải đủ chất |
| #6 Bảo hiểm chăm sóc dài hạn 3 % vs 5 % | cầu cao, hồ sơ vòng 1 đầy đủ, bình luận đã lọc nhiều; khán giả lớn tuổi trung thành | khoảng trống vừa; chỉ số giá sản xuất ≠ giá gia đình trả | vừa–cao | không được nói gói 5 % "không đáng tiền" |
| #2 Tăng ca vs việc thứ hai (đề xuất PLAN kênh) | hồ sơ đủ (`model.json` + `statements.json`); khoảng trống cao | cầu **thấp**; chủ đề có cờ thời sự (luật "no tax on overtime") — cầu dễ tắt | thấp–vừa | thời sự: video cũ nhanh khi luật đổi |
| #3 Giới hạn $500,000 khi bán nhà (làm lại) | cầu cao + khoảng trống cao | Tập 4 cùng đề tài **không đăng** (hình nghèo, nhiều chữ) — làm lại cần hướng hình khác | cao | dữ liệu chỉ số vùng; cảm giác lặp với chủ dự án |

**Đề xuất gói G1 lô:** Tập 7 = #13, Tập 8 = #20 (máy đề tài làm hồ sơ #20 song song P1 Tập 7, không thêm lượt chạm). Phương án thay: Tập 8 = #6 nếu hồ sơ #20 không qua `topic-dossier.md` §4 (quyền dữ liệu).

## 7. Chi phí phiên
- YouTube Data API: **7.720 / 10.000 đơn vị**, **67 / 100 search** (11/10).
- AI (headless, 0 agent con): **≈ 0,34 USD** — Haiku phân loại kênh 0,028 · bình luận 0,135 · khoảng trống 0,034 · hồ sơ 0,041; Sonnet thumbnail (URL) 0,075; embeddings 0,026 (`~/market-cache/2026-10-11/ai-ledger.jsonl`).
