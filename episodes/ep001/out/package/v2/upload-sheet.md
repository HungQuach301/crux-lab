# Tập 1 · Phiếu tải lên YouTube (PACKAGING v2, 30/09/2026)

Phiếu điền cho YouTube Studio. **Chủ dự án chốt lần cuối 30/09/2026 (theo gu, khác kết quả so cặp mù):** tiêu đề a1, thumbnail H (mặc định) + W + L cho Test & Compare, mô tả DA sửa hai dòng đầu theo a1, end screen E1. (Lần chốt trước — c2 / W, thumb-3, L — đã thay.) Chỗ còn ghi **ĐỀ XUẤT** là việc chủ dự án chọn khi tải lên. Chữ công khai viết tiếng Anh, ghi chú viết tiếng Việt. Tệp phim: `out/video.mp4` (591,3 s = **9:51**; PACKAGING không động vào).

## 1. Chi tiết

| Trường | Giá trị |
|---|---|
| Title | **Why a Smaller Loan Needs a Bigger Rate Cut to Be Worth It** (a1, 57 ký tự; claim `cut36_small` 1.12 > `cut36_large` 0.32, phép thử 3 năm). Test & Compare chỉ thử thumbnail, tiêu đề giữ cố định. |
| Description | `description.md` — hai dòng đầu **DA sửa theo a1** (144 ký tự): "A refinance on a smaller loan needs a bigger rate cut to earn back its fees within 3 years. Here is how big, for small, typical and large loans." Chapters đã có sẵn (0:00 …), phải bắt đầu bằng 0:00. |
| Thumbnail | Test & Compare, 3 ảnh (chốt 30/09): **`thumb-H.png` (mặc định, tải lên đầu tiên)**, `thumb-W.png`, `thumb-L.png`. H và L giữ huy hiệu ILLUSTRATIVE cỡ theo token (32 px = 48 px × 2/3), vì 1.12 / 0.32 / $1,133 là số của nhân vật minh hoạ; H giữ "pts" (điểm phần trăm, không đổi sang %). W không cần huy hiệu (5.98% là số thật, `low2026`). Cả ba 1280×720, PNG < 2 MB. Test & Compare cho dữ liệu thật phân xử giữa gu (a1 + H) và so cặp mù (c2 + W). |
| Playlist | **ĐỀ XUẤT**: tạo "Refinance & Mortgage Math" (Tập 1 là video đầu). Tên kênh dự phòng: "Crux: Money Math, Checked". |
| Audience | **Made for kids: No** ("No, it's not made for kids"). |
| Age restriction | Không. |
| Paid promotion | Không. |
| **Altered or synthetic content** | **YES**. Lời dẫn là giọng tổng hợp (ElevenLabs, `RIGHTS.md`). Người xem có thể tưởng là người thật nói, nên phải khai. Nhạc và âm dữ liệu sinh bằng code. |
| Tags | refinance, mortgage refinance, is refinancing worth it, refinance break even, refinance closing costs, closing costs, when to refinance, 1% rule refinance, one point rule, rate and term refinance, mortgage rates 2026, 30 year mortgage rate, 2023 mortgage, refinance math, break-even point, Freddie Mac mortgage rates, HMDA, personal finance (323 ký tự, giới hạn 500) |
| Hashtags (3, dòng cuối mô tả) | #refinance #mortgagerates #personalfinance |
| Category | **Education** |
| Video language / Title & description language | **English** |
| Caption | Tải `out/captions.srt` (English), không dùng phụ đề tự động. |
| Recording date / location | Để trống (phim dữ liệu, không quay). |
| License | Standard YouTube License. |
| Comments | On, "Hold potentially inappropriate comments for review". |
| Shorts remixing | Chủ dự án chọn. |

"1% rule refinance" chỉ nằm trong tags, vì người Mỹ tìm bằng cụm này. Tiêu đề và phim dùng "one-point rule" (một điểm phần trăm), xem `titles.md`.

## 2. Nguồn trong mô tả: link FHFA

- Hạn mức vay chuẩn (conforming loan limit) 2026, thông cáo FHFA ngày 25/11/2025: https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2026
- Trang tổng hợp hạn mức (dự phòng): https://www.fhfa.gov/data/conforming-loan-limit
- **Chưa kiểm được từ phiên này.** `fhfa.gov` bị proxy chặn (`RIGHTS.md`, `numbers.md §2`). Link thông cáo 2026 là link chủ dự án đã tự đọc (`cll2026` owner-verified). Link trang tổng hợp là URL tôi biết từ trước, chưa mở được, nên chủ dự án cần bấm thử trước khi đăng.

## 3. Giờ đăng (ĐỀ XUẤT, khán giả Mỹ)

- **Thứ Năm 01/10/2026, 10:00 ET** (7:00 PT), hoặc nếu lỡ thì **thứ Ba 06/10 hoặc thứ Tư 07/10, 11:00 ET**.
- Lý do:
  1. Người xem là người đang trả góp nhà ở Mỹ, xem sau giờ làm (chiều tối ET/PT). Đăng buổi sáng ET cho video vài giờ để được lập chỉ mục trước khung đó ở cả bốn múi giờ.
  2. Ngày giữa tuần (thứ Ba–thứ Năm) tránh sáng thứ Hai và cuối tuần, khi lượng tìm "refinance" gắn với tin lãi suất thấp hơn. Đây là kinh nghiệm chung, không phải dữ liệu của kênh: kênh chưa có số liệu Analytics.
  3. **Mốc dữ liệu:** Freddie Mac công bố PMMS thứ Năm, khoảng 12:00 ET (theo FRED, kỳ sau là 01/10/2026). Đăng 10:00 ET thứ Năm thì "7.03%, week ending September 24, 2026" vẫn là số mới nhất khi video lên. Sau đó phim vẫn đúng, vì mọi số "hôm nay" đều ghi ngày, nhưng không còn là tuần mới nhất. Nếu số 01/10 lệch nhiều, cân nhắc thêm dòng ghi chú ngày trong bình luận ghim (không sửa phim).
- Chưa có dữ liệu kênh. Sau 3–5 video, thay đề xuất này bằng "When your viewers are on YouTube" trong Analytics.

## 4. Câu mời bình luận (dòng cuối mô tả, trước hashtag)

> What does the fee line on your refinance offer say? Round it if you like. Real bills vary a lot, and we'd like to see the range.

Câu này hỏi con số trên lá thư chứ không hỏi thông tin cá nhân (khoản vay, địa chỉ). Nó không khuyên và mở đúng vào điểm "phí thật khác nhau" của S19 (một nửa hoá đơn 2025 nằm trong khoảng $3,443–$8,270).

## 5. Bình luận ghim (đăng ngay sau khi công khai, bằng tài khoản kênh)

> The answer in one line: for a new 30-year loan to pay back its fees within 3 years, our three illustrative borrowers needed rate cuts of 1.12 points ($115,000 loan), half a point ($375,000) and about a third of a point ($655,000). That's 8:07 in the video.
>
> Two things we count that the quick answers skip: the fees ($5,124 was the 2025 median bill) and what you still owe, since a fresh 30-year loan pays down the balance more slowly.
>
> Nora, Walt and Anjali are illustrative, built from 2025 medians. Rates are Freddie Mac's weekly average for the week ending September 24, 2026. History, not a forecast; US only; not advice.

Kiểm claim: `cut36_small` 1.12, `cut36_median` 0.5 ("half a point", S18.5), `cut36_large_words` "about a third of a point", `loan_small` / `loan_median` / `loan_large`, `cost_median` $5,124, `anchor_date`. Chương 8:07 "A line for each loan size". Quét S10: 0 khớp.

## 6. End screen — **E1** (chốt 30/09, không render lại)

**Vấn đề.** Lời cuối (S20.5 "How long do you picture yourself in your home?") bắt đầu ở 588,3 s, phim hết ở 591,3 s. 20 s cuối (571–591 s) là cảnh S20 đầy chữ: tiêu đề trên cùng, "+$8,093 ahead / if she stays 7 years" giữa phải, câu hỏi cuối và thước năm ở dưới (khung đã xem ở 572 s, 582 s, 589 s). Không có vùng trống dành cho phần tử end screen, nên đặt phần tử nào cũng che số hoặc câu hỏi.

- **E1 (không đụng phim, dùng được ngay):** end screen **5 s** (586,3–591,3 s), **2 phần tử**: "Subscribe" (tròn) ở góc trên trái, dưới dòng tiêu đề, trên mái nhà (vùng trời tối); "Best for viewer" (video) ở dưới trái, vùng trên thước năm, trái câu hỏi. Vẫn chạm một phần câu hỏi cuối. Phải xem trước trong Studio.
- **E2 (đề xuất cho bản dựng sau / Tập 2):** thêm **đuôi 15–20 s** sau lời cuối. Cảnh S20 mờ về nền `bg`, còn lại câu hỏi cuối ở giữa trên, và chừa hai ô (Subscribe + 1 video) ở nửa dưới theo lưới end screen 16:9 của YouTube. Việc này cần dựng lại hình, mux lại và kiểm lại K3 (F-rule độ dài). **Chưa làm.** Chủ dự án quyết ở bước tổng kết Tập 1.
- Khi kênh có video thứ hai: phần tử video đặt "Most recent upload" hoặc Tập 2.

## 7. Trước khi bấm Public

- [ ] Tiêu đề a1; bật Test & Compare với H (mặc định), W, L.
- [ ] Mô tả DA sửa theo a1 (`description.md`); bấm thử link FHFA.
- [ ] Altered or synthetic = Yes; Made for kids = No; Education; English.
- [ ] Phụ đề `captions.srt`.
- [ ] Playlist.
- [ ] End screen E1 (5 s, 2 phần tử), xem trước trong Studio.
- [ ] Đăng bình luận ghim.
