# Khán giả R1 — số công khai kênh Money Rerouted (17/10/2026)

**Nguồn:** YouTube Data API v3 (dữ liệu công khai) qua `toolkit/market/mcommon.py`, kéo 17/10/2026 ~giữa ngày UTC; 81 đơn vị hạn mức, 0 search, 0 lệnh AI. Số thô kênh mình: `audience/r1/channel.json` (kênh + 9 video), `audience/r1/comments.json` (20 bình luận mới nhất/video, chỉ văn bản). So sánh: `audience/r1/compare.json` — **chỉ số tổng hợp của nhóm** (trung vị, tứ phân vị, hạng của mình); số từng kênh khác ở `~/market-cache/2026-10-17/` ngoài git, đúng luật dữ liệu của `market/README.md` (III.E.4). Mọi tỉ lệ là **tự tính, không phải chỉ số YouTube**.

## 1. Kênh mình

Kênh tạo 02/10/2026 (14,6 ngày tuổi lúc kéo). **1 người đăng ký · 367 lượt xem tổng · 9 video** (7 video dài, 2 Short).

| Ngày đăng | Loại | Tiêu đề | Thời lượng | Tuổi (ngày) | Lượt xem | Like | Bình luận | Xem/ngày |
|---|---|---|---|---|---|---|---|---|
| 02/10 | dài | Why a Smaller Loan Needs a Bigger Rate Cut to Be Worth It (`OEVfD-ywzLc`) | 9:52 | 14,5 | 24 | 2 | 1* | 1,65 |
| 05/10 | dài | Need Private Grad Loans? Variable vs Fixed Through History (`-AwfRUE6UTI`) | 9:46 | 11,6 | 75 | 1 | 1* | 6,47 |
| 06/10 | dài | EE Bonds vs T-Bills: Can Rolling Beat Double in 20 Years? (`2ErffZBHggE`) | 9:33 | 10,6 | 51 | 2 | 1* | 4,82 |
| 08/10 | dài | 10% Down: When Does PMI Actually End? (`1o-2RJ-DdfE`) | 7:46 | 8,6 | **106** | 2 | 1* | **12,29** |
| 08/10 | Short | 10% Down: When Does PMI Actually End? #personalfinance … (`vCExC7CoImY`) | 0:38 | 8,6 | 70 | 1 | 0 | 8,12 |
| 11/10 | dài | Can a 2% Annuity Raise Keep Up With Inflation? (`dn6-0g2RvD0`) | 8:57 | 5,9 | 2 | 1 | 0 | 0,34 |
| 13/10 | dài | 15-Year Mortgage vs. 30-Year Paid in 15: The Real Cost (`p78Ca1OHTgM`) | 10:07 | 3,6 | 4 | 1 | 0 | 1,11 |
| 13/10 | Short | 30-Year Mortgage, 15-Year Payoff #personalfinance … (`Lj6PBFl5tDI`) | 0:36 | 3,6 | 40 | 0 | 0 | 11,15 |
| 15/10 | dài | Is Rent Really Wasted? Buying vs. Renting for 10 Years (`26SfSIDPpzk`) | 10:07 | 1,6 | 5 | 0 | 0 | 3,15 |

\* Cả 4 bình luận là **bình luận ghim của chính kênh** (đối chiếu `authorChannelId` với id kênh, không lưu). Bình luận của khán giả: **0**.

Cộng: video dài 267 lượt xem / 9 like; Short 110 lượt xem / 1 like.

## 2. So với kênh trực tiếp + nhỏ/mới nổi

Nhóm so sánh: 14 kênh trong `market/CHANNELS.md` — 2 hạt giống (Logical Money, Jack Explains Money), 5 vòng trực tiếp (Hannah Invests, James Retires, Tom – Lazy Real Estate, Finance Flow, Rich by Routine), 7 mới nổi vòng trực tiếp (Devil in the Decimal, The Hidden Money Equation, Davidson Money Stories, Mr Finance Wise, Worthspring, Grayson Invests, MoneyMechanics). Chỉ video dài (> 3 phút, `pull.py` bỏ Short/live), 24 tháng.

| Chỉ số (tự tính) | Mình | Nhóm: trung vị (P25–P75) | Mới nổi: trung vị | Hạng của mình (cao→thấp) |
|---|---|---|---|---|
| Lượt xem/video dài **30 ngày đầu** (proxy: video 30–60 ngày tuổi, < 3 video thì 30–90) | **chưa có** — video già nhất 14,5 ngày | 687 (180–2.902), n = 12 kênh | 168 (n = 5) | — |
| Lượt xem/video dài **cùng tuổi 1–15 ngày** (thay cho dòng trên) | **24** | 307 (58–3.160), n = 12 | 140 (n = 6) | **12/13** |
| Lượt xem 30 ngày / người đăng ký | chưa có (và 1 người đăng ký) | 1,43 (0,77–2,49) | 1,86 | — |
| Tổng lượt xem / người đăng ký | 367 (chia cho 1 — không có nghĩa) | 132 (93–443) | 364 | 4/15 |
| Nhịp đăng (video dài/tuần, 90 ngày hoặc từ khi lập kênh) | **3,4** | 2,1 (1,0–3,9) | 1,6 | 6/15 |
| Khoảng cách trung vị giữa hai video (ngày) | 2,2 | 2,0 (1,0–4,1) | 1,0 | — |
| Thời lượng trung vị video dài (phút) | **9,8** | 11,1 (9,7–17,8) | 10,7 | 11/15 (ngắn thứ 5) |
| Like / 1.000 lượt xem (mình: gộp 7 video) | 33,7 (9 like / 267) | 13,4 (5,0–16,7), n = 13 | 5,0 | 2/14 |
| Bình luận khán giả / 1.000 lượt xem | **0** | 1,7 (0,5–3,4), n = 13 | 0,5 | đồng cuối (cùng 3 kênh = 0) |
| Người đăng ký | **1** | 231 (40–1.883) | 50 | 15/15 |
| Tuổi kênh (ngày) | 14,6 | 131 (63–1.271) | 125 | trẻ nhất |

## 3. Năm phát hiện

1. **Chưa đo được "30 ngày đầu" — mọi kết luận về lượt xem là sớm.** Video già nhất 14,5 ngày; chỉ số chính đầu tiên là 01/11 (`OEVfD-ywzLc` đủ 30 ngày), mốc `market/CALIBRATION.md` 06/11 có 5 video ≥ 28 ngày. Ở cùng tuổi 1–15 ngày, trung vị video dài của mình **24 lượt xem**, hạng **12/13**, bằng ~1/13 trung vị nhóm (307) và ~1/6 trung vị nhóm mới nổi (140). Chỉ hơn được Davidson Money Stories (15); ngang Devil in the Decimal (25).
2. **Lượt xem đang giảm theo từng video, không tăng.** Bốn video đầu (02–08/10) đạt 1,7–12,3 lượt xem/ngày; ba video sau (11–15/10) chỉ 0,3–3,2/ngày (2, 4, 5 lượt xem sau 1,6–5,9 ngày). Kênh 1 người đăng ký nên mỗi video mới gần như không có khán giả sẵn để thông báo — lượt xem phụ thuộc hoàn toàn vào tìm kiếm/đề xuất, mà API công khai không cho biết nguồn nào.
3. **Short kéo lượt xem/ngày ngang hoặc hơn video dài nhưng không ra người đăng ký.** 2 Short: 70 và 40 lượt xem (8,1 và 11,2/ngày) — Short 13/10 nhận gấp 10 lần video dài cùng đề tài cùng ngày (40 vs 4). Short chiếm 110/377 lượt xem (29 %) với 1 like; tổng kênh vẫn 1 người đăng ký.
4. **Video PMI (`1o-2RJ-DdfE`) là video duy nhất vượt trội — và là video ngắn nhất.** 106 lượt xem, 12,3/ngày, gấp ~4,4× trung vị video dài của kênh (24), thời lượng 7:46 so với 9:33–10:07 của các video khác; có Short đi kèm cùng ngày. Một điểm dữ liệu, không đủ để kết luận về thời lượng; khớp với `market/REPORT.md` §1 rằng đề tài nhà ở có cầu cao hơn (PMI #17 bị gắn cầu thấp — đây là tín hiệu đầu tiên ngược nhãn, kiểm lại ở mốc 06/11).
5. **Nhịp đăng và thời lượng không phải điểm nghẽn; tương tác khán giả là 0.** 3,4 video dài/tuần — hạng 6/15, trên trung vị nhóm (2,1) và gấp đôi nhóm mới nổi (1,6). Thời lượng 9,8 phút nằm trong dải mới nổi (10,7) nhưng ngắn hơn 4/5 kênh vòng trực tiếp (17,6–21,4 phút) và dải video vượt trội ~15 phút của `REPORT.md` §4. Like/1.000 lượt xem cao (33,7, hạng 2/14) nhưng trên mẫu 9 like, mà 0 bình luận khán giả — bình luận ghim kết bằng câu hỏi chưa nhận được câu trả lời nào ở 4 video.

## 4. Giới hạn

- **API công khai không có:** tỉ lệ nhấp thumbnail (CTR), số lượt hiển thị, thời gian xem / giữ chân trung bình, đường cong giữ chân, nguồn lưu lượng (tìm kiếm, đề xuất, duyệt, bên ngoài), nhân khẩu học, người đăng ký thu về theo video, lượt xem 30 ngày đầu theo thời điểm. Những thứ này cần **YouTube Studio / YouTube Analytics API** (đăng nhập chủ kênh) — chỉ có chúng mới trả lời được phát hiện 2 (lỗi ở thumbnail/tiêu đề hay do không được hiển thị).
- "30 ngày đầu" của kênh khác là **proxy**: lượt xem hiện tại của video 30–60 ngày tuổi (30–90 nếu ít hơn 3 video), không phải lượt xem tại ngày 30. Dòng "cùng tuổi 1–15 ngày" là so sánh công bằng nhất hiện có, nhưng mẫu kênh mình chỉ 7 video.
- Số lượt xem công khai trễ và được YouTube lọc; tổng kênh (367) lệch nhẹ tổng từng video (377). Like có thể có của chính chủ kênh/người quen — API không phân biệt.
- 2 kênh (Davidson, Mr Finance Wise) không có video 30–90 ngày tuổi; 2 kênh (Rich by Routine, MoneyMechanics) không có video 1–15 ngày → n mỗi dòng ghi riêng. Nhóm so sánh do máy phân loại ở `market-r1` (11/10), chưa qua chủ dự án.
- Bình luận: 20 mới nhất mỗi video theo `order=time`; chỉ bình luận cấp đầu, không lấy trả lời.

**Làm lại** (không sửa toolkit): script trong phiên gọi `mcommon.channels/videos/yt` cho kênh mình + `commentThreads`, và `pull.pull()` cho 14 kênh; ~81 đơn vị. Mốc kế: **01/11** (video đầu đủ 30 ngày) và **06/11** (`CALIBRATION.md`).
