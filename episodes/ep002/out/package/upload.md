# Tập 2 · Phiếu tải lên YouTube (C6, 01/10/2026)

Phiếu điền cho YouTube Studio. Chỗ ghi **CHỦ DỰ ÁN CHỌN** là câu hỏi C6 (`options.md` §5); chưa chốt gì. Chữ công khai tiếng Anh, ghi chú tiếng Việt. Tệp phim: `out/video.mp4` (585,6 s = **9:45**; PACKAGING không động vào).

## 1. Chi tiết

| Trường | Giá trị |
|---|---|
| Title | **CHỦ DỰ ÁN CHỌN**: **A1** "Need Private Grad Loans? Variable vs Fixed Through History" (58 ký tự) hoặc **A2** "No Grad PLUS? How Much Lower a Variable Rate Had to Start" (57). Test & Compare chỉ thử thumbnail; tiêu đề giữ cố định. |
| Description | `out/package/description.md`, dán nguyên văn (bỏ dòng chú thích `<!-- … -->` đầu tệp). Số → claim: `description-claims.json`. Không sửa. |
| Chapters | Đã có trong `description.md`, khớp `out/timeline.json` (`scenes[].start`, làm tròn xuống giây). Bảng đối chiếu ở §2. |
| Thumbnail | **Test & Compare, 3 ảnh**: `thumb-1.png`, `thumb-2.png`, `thumb-3.png` (1280×720 PNG, mỗi ảnh < 2 MB). Ảnh mặc định (tải lên đầu tiên): **CHỦ DỰ ÁN CHỌN**. Cả ba mang huy hiệu ILLUSTRATIVE (số của Leah). |
| Playlist | ĐỀ XUẤT: playlist riêng cho chuỗi "replay" (Tập 1 refinance, Tập 2 vay sau đại học), ví dụ "Money Decisions, Replayed Through History". Chủ dự án đặt tên. |
| Audience | Made for kids: **No**. |
| Age restriction / Paid promotion | Không / Không. |
| **Altered or synthetic content** | **YES**: lời dẫn là giọng tổng hợp (ElevenLabs "Eric", `RIGHTS-ep002.md` V-ERIC); mô tả đã ghi "Narration: synthetic voice". |
| Tags (15, 391 ký tự / 500) | private student loans, grad school loans, graduate student loans, Grad PLUS, Grad PLUS loans 2026, fixed vs variable student loan, variable rate student loan, fixed rate student loan, private student loan interest rates, student loan interest rates history, co-signer student loan, student loan refinance fixed or variable, Treasury bill rate history, interest rate history, personal finance |
| Hashtags (dòng cuối mô tả, nếu chủ dự án muốn) | #studentloans #gradschool #personalfinance |
| Category | Education |
| Video language / title & description language | English |
| Captions | Tải `out/captions.srt` (English), không dùng phụ đề tự động. |
| License / Comments | Standard YouTube License / On, "Hold potentially inappropriate comments for review". |

Tags không có tên bên cho vay (kênh không nêu thương hiệu, C1 câu 3). Tags và hashtag đã quét S10: 0 khớp.

## 2. Chapters (đối chiếu `out/timeline.json` ↔ `description.md`)

| Cảnh | `start` (s) | Chapter | Thời lượng |
|---|---|---|---|
| S01 | 0.0 | 0:00 Two offers | 27 s |
| S02 | 26.967 | 0:26 Why private loans | 40 s |
| S03 | 67.3 | 1:07 Leah's loan and the head start | 60 s |
| S04 | 126.8 | 2:06 Every stretch since January 1954 | 50 s |
| S05 | 176.933 | 2:56 The contradiction | 48 s |
| S06 | 224.433 | 3:44 The cushion | 39 s |
| S07 | 263.767 | 4:23 Two kinds of history | 58 s |
| S08 | 322.067 | 5:22 The worst stretch: April 1977 | 61 s |
| S09 | 383.3 | 6:23 Moving the head start | 55 s |
| S10 | 438.7 | 7:18 Other offers, and the answer | 67 s |
| S11 | 506.033 | 8:26 How we know this | 24 s |
| S12 | 530.033 | 8:50 Where an offer falls | 40 s (đến 569,6) |
| S13 | 569.6 | (không thành chapter: đuôi end screen, 16 s) | — |

YouTube cần chapter đầu là 0:00, ≥ 3 chapter, mỗi chapter ≥ 10 s: đạt (ngắn nhất S11, 24 s).

## 3. End screen (đuôi S13 có sẵn trong phim, 569,6–585,6 s)

Phim đã chừa chỗ (kế hoạch C3 `packaging.md` §5; `animatic/src/s13.js`): dải lịch sử mờ ở đáy (y 780–990 @1080), **một khung viền `grid` 16:9** ở giữa trên: x 640–1280, y 170–530 @1920×1080 (= 33,3–66,7% ngang, 15,7–49,1% dọc). Không có chữ trên hình.

| Phần tử | Vị trí | Thời gian |
|---|---|---|
| **Video** ("Best for viewer" hoặc video gần nhất; khi có, Tập 1) | khớp đúng khung viền giữa trên (kéo phần tử cho bằng khung, YouTube giữ tỉ lệ 16:9) | **9:30 → 9:45** (570–585,6 s). Lời S13.2 "Another replay from this channel is on screen now." bắt đầu 9:34,26, nên phần tử phải hiện trước 9:34. |
| **Subscribe** (tròn) | giữa, dưới khung, trên dải lịch sử (tâm ≈ x 960, y 650 @1080) | 9:30 → 9:45 |

Tổng 15,6 s (YouTube cho 5–20 s). Xem trước trong Studio: phần tử không được che dải lịch sử ở đáy (không có số, chỉ nền).

## 4. Test & Compare

- Ảnh: **thumb-1** (hai lời mời, "9%" · "7.5%"), **thumb-2** (lịch sử, "14.2% cost more"), **thumb-3** (giai đoạn tệ nhất, "April 1977" · "43% more").
- Kiểm mù (THAM KHẢO, tiêu đề A1 cố định): thumb-3 19/24 · thumb-1 18/24 · thumb-2 9/24 (`review-c6/pack-test/results.md`). Nếu chủ dự án chọn A2, thứ hạng thumbnail dưới A2 chưa đo.
- **Việc sau khi đăng** (ghi vào `playbook/packaging.md` §6 khi tổng kết Tập 2): tỉ lệ thời gian xem của từng thumbnail theo Test & Compare; CTR của tiêu đề; so với kiểm mù và với gu.

## 5. Trước khi bấm Public
- [ ] Tiêu đề (A1 hoặc A2, theo C6).
- [ ] Dán `description.md` (bỏ dòng chú thích đầu); chapters hiện đúng.
- [ ] Test & Compare: thumb-1, thumb-2, thumb-3; ảnh mặc định theo C6.
- [ ] Altered or synthetic = Yes; Made for kids = No; Education; English.
- [ ] Phụ đề `captions.srt`.
- [ ] End screen: video khớp khung + Subscribe, 9:30–9:45; xem trước.
