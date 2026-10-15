# Khung xét nhạc người sáng tác CC BY — cho G1 Tập 9 (F-18 mục 3)

> **Chưa đưa vào tập nào.** Nhạc của kênh vẫn bằng mã (RIGHTS `A-MUSIC`, D-013 mục 3) tới khi chủ dự án chọn ở G1 Tập 9.
> **Không nhạc AI** (cả nguồn "AI-assisted"); không nhà cung cấp nhạc AI. Tài liệu này là khung để chọn, không phải danh sách đã duyệt:
> mọi giấy phép bên dưới phải **kiểm lại trên trang của TỪNG BÀI lúc tải** (RIGHTS §G: trang tệp, không trang bộ sưu tập).

## 1. Nguồn (danh sách trắng đề xuất — thứ tự ưu tiên)

| # | Nguồn | Giấy phép thường gặp | Lọc / kiểm từng bài | Rủi ro đã biết |
|---|---|---|---|---|
| 1 | Nghệ sĩ độc lập phát hành CC BY 4.0 trên trang riêng (ví dụ cần kiểm: Kevin MacLeod — incompetech.com; Scott Buckley — scottbuckley.com.au; Josh Woodward — joshwoodward.com) | CC BY 4.0 (cả danh mục, theo trang nghệ sĩ) | Trích câu giấy phép trên trang bài/trang giấy phép của nghệ sĩ; lưu bản chụp + SHA-256 như X-F15-3 | Bài rất phổ biến → kênh khác dùng nhiều (kém nhận diện); bên thứ ba có thể đăng ký Content ID trái phép → claim |
| 2 | Free Music Archive (freemusicarchive.org) | trộn: CC BY, CC BY-SA, CC BY-NC…, mỗi bài một nhãn | Chỉ nhận nhãn **CC BY 3.0/4.0** của trang bài; loại BY-NC, BY-SA, BY-ND, "Sampling+" | Nhãn có thể đổi theo thời gian → bản chụp ngày tải là bằng chứng |
| 3 | ccMixter (dig.ccmixter.org) | CC BY hoặc CC BY-NC theo bài | Lọc "free for commercial use" và kiểm nhãn bài = CC BY | Remix chứa mẫu của người khác: phải xem chuỗi nguồn ("uses samples from") đều CC BY |
| 4 | Internet Archive — netlabels | theo mục | `licenseurl` của mục = CC BY; tác giả trong mục là người sáng tác | Nhiều mục tải lên bởi người không phải chủ quyền → chỉ nhận mục do chính netlabel/nghệ sĩ đăng |
| 5 | Musopen (bản thu nhạc cổ điển) | Public domain / CC0 theo bản thu | Kiểm nhãn bản thu (không chỉ nhạc phẩm) | Âm sắc cổ điển khó hợp G-016 (sáng, năng động) |

**Loại:** YouTube Audio Library (RIGHTS §G cấm), Pixabay Music và kho "royalty-free" có giấy phép riêng không phải CC (và có nội dung sinh bằng AI),
Jamendo bản CC BY-NC (thương mại phải mua giấy phép), mọi bài BY-NC/BY-SA/BY-ND, mọi bài gắn thẻ/ghi chú AI, bài có lời hát.

## 2. Tiêu chí giai điệu kênh (đo được trước, nghe sau)

| Tiêu chí | Nguồn luật/gu | Cách đo trước khi đưa chủ dự án nghe | Ngưỡng đề xuất |
|---|---|---|---|
| Sáng/tò mò hoặc năng động; không chậm, không buồn | G-016, G-016·chọn (C: 109–117 BPM) | nhịp (beat tracking) + giọng trưởng/dorian (chroma) | 100–125 BPM, hoặc trưởng/dorian rõ; loại thứ tự nhiên chậm |
| Không lộ vòng lặp | G-002, checks **T2** | `checks/py/r_sound.py` T2 trên bài đã cắt theo tập (cần `out/tempo-map.json` beats của bài) | ≤ 5 % câu 4 ô lặp, không 2 câu lặp liền |
| Chừa chỗ cho lời | G-006, A07 (nhạc dưới lời 20 dB), dải 1–4 kHz | phần năng lượng 1–4 kHz của bài; thử trộn bằng `toolkit/factory/music.py` (né 13 dB) | sau né: A07 ≥ 19,5 dB; không nhạc cụ chính đơn ca ở 1–4 kHz |
| Theo bản đồ căng (DX-R1), vào khoảng lặng mềm | DX-R1, G-003, checks **T3**, A09 | bài có stems hoặc nhiều đoạn (intro / xây / thả) để dựng theo hồi; thử cắt ở MR1/MR2 | T3: vào lặng 150–400 ms; ≥ 3 đoạn nhạc khác nhau cho 3 hồi |
| Hợp nhạc hiệu A (ident-A, close-A) | F-12, C3 Tập 6 | khoá/nhịp so với `toolkit/factory/theme/theme.json` | cùng khoá hoặc khoá kề; nhịp chênh ≤ 10 % |
| Không lời hát, không mẫu giọng | G-006 | nghe + ASR (faster-whisper) không ra chữ | 0 từ nhận dạng |
| Không phổ biến quá mức | nhận diện kênh | tìm tên bài trên YouTube (thủ công) | ưu tiên bài ít dùng |
| An toàn Content ID | YT | trang nghệ sĩ nói không đăng ký Content ID / có quy trình gỡ claim | có câu trích nguyên văn; không có → hạng thấp |

## 3. Ghi công (bắt buộc với CC BY)

Mô tả tập (do máy viết ở M6, D-013 mục 2), mỗi bài một dòng — đủ bốn phần TASL (tiêu đề, tác giả, nguồn, giấy phép) + ghi chú sửa đổi:

```
Music: "<Tên bài>" by <Nghệ sĩ> — <URL trang bài> — licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Edited and mixed under narration.
```

RIGHTS: mỗi bài một dòng mã `M-<nghệ sĩ>-<bài>` (cột như §G1: URL trang · tệp, tác giả, giấy phép, **trích nguyên văn**, ngày tải, SHA-256 bản gốc +
bản đã cắt, ghi công). Tệp nhạc > 2 MB không commit (như footage F5: `work/external/` + SHA-256).

## 4. Thủ tục chọn ở G1 Tập 9 (đề xuất)

1. **M1–M2 Tập 9:** bên dựng lập danh sách ngắn 6–9 bài (≥ 2 nguồn), mỗi bài có bản chụp giấy phép + bảng đo §2 (T2, BPM, khoá, 1–4 kHz).
2. Dựng **3 bản thử 60 s** cùng một đoạn của Tập 9 (cùng lời, cùng hình): nhạc bằng mã hiện tại (đối chứng) + 2 bài đứng đầu; trộn bằng nhà máy
   (A07 20 dB, né 1–4 kHz), loudnorm −14 LUFS. Đặt tên mù (X/Y/Z), khoá giải mã giữ riêng như thử giọng C3 Tập 1.
3. **G1:** chủ dự án nghe trên loa điện thoại (như G-005·chọn), chọn hoặc giữ nhạc bằng mã. Ghi vào sổ gu (G-016) + D-mới nếu đổi nguồn nhạc.
4. Nếu chọn bài CC BY: dòng RIGHTS + ghi công mô tả là điều kiện của G2; checks T2/T3/A07 chạy trên stem music như nhạc bằng mã.

## 5. Việc nhà máy cần nếu chọn nhạc ngoài (chưa làm — ngoài phạm vi F-18)

- `audio.music` đã nhận tệp WAV ngoài (`music.py`), nhưng **checks T2 cần `out/tempo-map.json` beats**: với nhạc ngoài phải dò phách (beat tracking) thay vì
  đọc lưới 114 BPM của nhạc bằng mã.
- Dựng theo hồi (DX-R1): cắt/ghép bài theo bản đồ căng và MR1/MR2 cần công cụ cắt ở biên câu nhạc (chưa có).
- `close_lift_db`, ident A: kiểm khoá/nhịp hợp với bài chọn.
