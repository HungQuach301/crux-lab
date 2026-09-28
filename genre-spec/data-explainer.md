# Spec thể loại: data-explainer (v0, 2026-09-28)

Spec này tổng hợp các yêu cầu tay nghề cho thể loại data-explainer của kênh `us-personal-finance`. Nó đứng dưới `CHARTER.md` và `decisions/`, trên sổ gu (CHARTER §10). Khi hai nguồn mâu thuẫn, hiến chương thắng.

Theo CHARTER §2.6, spec lớn lên theo từng tập. Bản v0 này chỉ gom những gì bài D đã làm thật và được chấm, không thêm yêu cầu mới.

## Nguồn và cách ghi

Mỗi yêu cầu ghi nguồn trong ngoặc vuông.

| Mã | Tài liệu | Vị trí |
|---|---|---|
| `CH` | `CHARTER.md` (repo này) | mục 5 |
| `B` | [BRIEF-D.md](https://github.com/HungQuach301/crux-spike-opus55/blob/76613cfa756e2604770043435f79eb00e269e2b6/BRIEF-D.md) | nhánh `claude/opus55-cine-phase-d-jw6me1` @ `76613cf` |
| `Am` | [BRIEF-D-amendments.md](https://github.com/HungQuach301/crux-spike-opus55/blob/76613cfa756e2604770043435f79eb00e269e2b6/BRIEF-D-amendments.md) | cùng commit; mục 1–20, do chủ dự án quyết định |
| `R` | [REPORT-D.md](https://github.com/HungQuach301/crux-spike-opus55/blob/76613cfa756e2604770043435f79eb00e269e2b6/REPORT-D.md) | cùng commit; báo cáo M0 → M3 vòng 3 |
| `Au` | [audit/REPORT.md](https://github.com/HungQuach301/crux-spike-opus55/blob/afad8999e54adf6bd52fadb4a840465f9e5e7e74/audit/REPORT.md) | nhánh `audit/d-final` @ `afad899`; chấm độc lập của Phiên K |
| `RB` | [checks/RUBRIC.md](https://github.com/HungQuach301/crux-spike-opus55/blob/76613cfa756e2604770043435f79eb00e269e2b6/checks/RUBRIC.md) | phiếu chấm tay H1–H7 của bài D |

Cách đánh dấu:
- `[MÁY]` là yêu cầu kiểm được bằng máy.
- `[NGƯỜI]` là yêu cầu cần chủ dự án chấm tay.
- Ngưỡng số giữ nguyên như bài D, trừ chỗ có amendment sửa.
- Repo này **chưa có luật mã nào**; `checks/` để trống cho Phiên K1 (CHARTER §8).

## 0. Loại bỏ so với bài D

Thể loại này **không dùng thế giới 3D** [CH §5; Am 11–12]. Chuẩn điện ảnh ở đây là tay nghề: kịch bản, nhịp, âm thanh, dựng, và máy quay có lý do. Hướng hình là "biểu đồ là nhân vật chính, tay nghề điện ảnh bao quanh" [Am 12].

Các yêu cầu sau của BRIEF-D **bị bỏ**, không chuyển sang thành trượt đã biết:

| Yêu cầu bài D | Nguồn | Lý do bỏ |
|---|---|---|
| Không gian 3D phối cảnh, ≥ 3 lớp chiều sâu | B §4.3 | Am 11, CH §5 |
| Rack focus ≥ 3 lần, độ sâu trường ảnh | B §4.3 | như trên; Am 13 chỉ là cách làm tạm ở 2.5D |
| Làm mờ chuyển động, siêu lấy mẫu 8× | B §4.3 | như trên; luật V07 là trượt đã biết ở 2.5D (Am 15) |
| Ánh sáng key/fill/rim có nguồn gốc, bóng đổ mềm | B §4.4 | như trên |
| Render thử cảnh 3D ở bước 0 (DOF + blur 8×) | B §8b | như trên |
| Âm thanh vật lý của thế giới lookdev (gió, mưa, nước, sấm) | Am 11; R M2b | tài sản của hướng 3D đã dừng |

Parallax nhiều lớp, làm mờ lớp nền để dẫn mắt, và máy quay đi trên mặt phẳng biểu đồ vẫn **được phép**. Chúng là lựa chọn dựng, không phải yêu cầu [Am 13].

## 1. Luật cứng (không nhân nhượng)

- **DX-H1.** Lỗi số liệu = 0. Mọi số trên màn hình và trong lời là một claim có công thức và nguồn [CH §5; B §1.5]. `[MÁY]`
- **DX-H2.** Số không có nguồn gắn ILLUSTRATIVE, và huy hiệu hiện **cùng lúc** với số [CH §5; B §1.5]. `[MÁY]`
- **DX-H3.** Số lịch sử gắn năm dữ liệu. Mọi con số tiền ghi rõ danh nghĩa hay thực (đã trừ lạm phát) [B §1.5]. `[MÁY]`
- **DX-H4.** Dữ liệu gốc được commit kèm SHA-256, ngày tải, URL, và điều khoản sử dụng trích nguyên câu kèm đường dẫn. Nếu điều khoản không cho kênh có quảng cáo: DỪNG, báo lại [B §1.3]. `[MÁY]`
- **DX-H5.** Có nguồn đối chiếu độc lập, dung sai ghi rõ. Lệch thì báo, không tự chọn nguồn. Cần domain mới thì báo tên, không tự đổi nguồn [B §1.3; Am 5, 9]. `[MÁY]`
- **DX-H6.** Chống chọn mẫu có lợi: khi phép phân tích có nhiều điểm bắt đầu hay nhiều trường hợp, phải cho thấy **mọi** trường hợp, gồm cả những trường hợp đi ngược luận điểm [B §1.7]. `[MÁY]`
- **DX-H7.** Claim phải đúng cả về nghĩa, không chỉ về công thức. Bài D đếm "8 năm lãi > 10% mà số dư vẫn giảm" có gồm năm đã cạn tiền. Câu đó đúng theo công thức nhưng dễ gây hiểu lầm; chủ dự án cho sửa thành 7 [Au §5; Am 20]. `[NGƯỜI + MÁY]`
- **DX-H8.** Chính sách nền tảng [CH §5].

## 2. Nhân dạng (gen được bảo vệ)

Phần này chỉ chủ dự án được sửa (CHARTER §7.5).

- **DX-I1.** "We" chỉ người phân tích. Không có câu khuyên. Không dự báo thị trường [CH §5; B §1.6]. `[MÁY]`
- **DX-I2.** Nói "US only" và "history, not a forecast" khi dùng dữ liệu lịch sử, mỗi câu một lần ở hồi 1 [CH §5; Am 6]. `[MÁY]`
- **DX-I3.** Đầu vào mô tả (ví dụ "4%") không được trình bày như một khuyến nghị [B §1.6]. `[NGƯỜI]`
- **DX-I4.** Chữ trên màn hình không được đọc như câu mệnh lệnh. Bài D phải đổi "start", "Never ran out" sang cách nói khác [R M3, S10]. `[MÁY]`

## 3. Kịch bản

- **DX-S1. Cấu trúc hồi** [B §2.1; RB H3]:
  - cold open ≤ 15 s, ident ≤ 3 s;
  - hồi 1 dựng nhân vật và luật chơi;
  - hồi 2 cho các số phận tách nhau, cao trào ở điểm chênh lớn nhất;
  - hồi 3 cho mọi trường hợp, điều gì quyết định, và giới hạn của phép phân tích;
  - thẻ phương pháp;
  - outro ≥ 20 s, có vùng trống cho end screen.
  `[MÁY: thời lượng]`
- **DX-S2. Mỗi hồi có câu hỏi riêng, một bước ngoặt và một payoff** [B §2.2; RB H3]. Bài D chấm 3/5 ở vòng 2. `[NGƯỜI]`
- **DX-S3. Vòng mở.** Trong cold open, hình đi trước lời và đặt một câu hỏi mở cụ thể. Hồi 3 trả lời đúng câu hỏi đó, gọi lại bằng cùng hình hoặc cùng chữ. Ngay sau câu trả lời là câu nói rõ giới hạn của nó [B §2.1; RB H1; R M1]. Bài D chấm 4/5. `[NGƯỜI]`
- **DX-S4. Câu móc lại ở 0:30–0:45.** Một câu cụ thể, đo được, hứa điều người xem sẽ biết, và video giữ lời hứa đó [B §2.1; RB H2]. Bài D chấm 2/5 ở vòng 2. Nguyên nhân là hình minh hoạ không khớp lời hứa, nên vòng 3 vẽ lại thành một vật duy nhất [Am 17]. Xem sổ gu (d). `[NGƯỜI]`
- **DX-S5. Cái giá cụ thể.** Nói bằng năm và số dư (ghi thực hay danh nghĩa), không bằng khái niệm trừu tượng. Mọi điểm quyết định gọi tên năm và số dư [B §2.3; RB H4]. Bài D chấm 3/5. `[NGƯỜI]`
- **DX-S6. Callback.** Con số cốt lõi quay lại ≥ 3 lần, mỗi lần mang nghĩa mới [B §2.4]. `[MÁY]`
- **DX-S7. Mật độ số.** Trung bình ≤ 1 số mới mỗi 8 s; không cảnh nào > 2 số mới [B §2.5]. Bài D còn trượt ở 4 cảnh (S12). Sửa loại lỗi này cần viết lại kịch bản và thu lại giọng, nên phải kiểm **trước khi thu giọng** [R M3]. `[MÁY]`
- **DX-S8.** Câu ngắn và câu dài xen kẽ: độ lệch chuẩn chia trung bình độ dài câu ≥ 0,35 [B §2.6]. `[MÁY]`
- **DX-S9. Table read.** Đọc toàn kịch bản bằng TTS trước khi dựng, nộp audio và danh sách chỗ sửa. Chủ dự án nghe bằng tai; ASR và đo nhịp không thay được việc nghe [B §2.7; R M1]. `[NGƯỜI]`
- **DX-S10. Điểm chèn quảng cáo.** 2–3 điểm tại ranh giới hồi, mỗi điểm có khoảng lặng tự nhiên ≥ 1 s, ghi mốc thời gian [B §2.8]. `[MÁY]`
- **DX-S11. Tránh từ làm ASR hỏng** mà không đổi nghĩa: không dùng sở hữu cách ("retiree's"); đọc "Standard & Poor's 500 index" thay cho "S&P" [Am 4; Au §4]. Nguyên nhân gốc là lỗi của máy kiểm bài D (Au §4.1–4.2). K1 quyết định có giữ cách né này không. `[MÁY]`

## 4. Nhịp căng–chùng

- **DX-R1. Bản đồ căng–chùng** (tốc độ cắt, mật độ âm thanh, mức nhạc theo thời gian). Mỗi hồi có một đỉnh ở cao trào, sau đó là thung lũng nghỉ [B §3.1]. Đo từ stem, nên stem phải được giao (DX-F7) [Au §2]. `[MÁY]`
- **DX-R2.** Không đoạn nào > 60 s mà không đổi họ layout, cỡ cảnh hoặc lớp âm thanh [B §3.2]. `[MÁY]`
- **DX-R3. Khoảng thở.** Sau mỗi con số quyết định có ≥ 1,0 s không lời [B §3.3]. Luật R03 của bài D đo sai theo cả hai chiều (Au §6 K-4, K-5); K1 viết lại. `[MÁY]`
- **DX-R4.** ≥ 70% cú cắt rơi đúng phách hoặc đúng điểm hành động (±1 khung) [B §3.4]. `[MÁY]`
- **DX-R5. Độ dài cảnh** 1,2–12 s; độ lệch chuẩn chia trung bình ≥ 0,4; hồi 2 tăng tốc tới cao trào [B §3.5]. `[MÁY]`
- **DX-R6. Khoảng lặng có chủ ý**: ≥ 3 khoảng 0,8–1,5 s [B §5.3]. Vào mỗi khoảng lặng phải có chuyển tiếp khoảng 300 ms, không cắt cứng. Nhạc nhả như đuôi reverb, sfx tắt dần trong 150 ms, room tone lên thành sàn (không bao giờ im số tuyệt đối), mọi thứ trở lại trong 200 ms [Am 18]. Xem sổ gu (c). `[MÁY + NGƯỜI]`

## 5. Hình ảnh (2D, biểu đồ là nhân vật chính)

- **DX-V1. Bố cục.** Thứ bậc ba mức (một thứ nhìn đầu tiên); điểm nhìn chính ở giao điểm một phần ba hoặc giữa có chủ ý; đường dẫn mắt; khoảng trống phía trước theo hướng chuyển động; khoảng âm có chủ ý. Mọi khung đọc được trong 1 giây [B §4.2; RB H5]. `[NGƯỜI + MÁY: vị trí phần tử mức 1]`
- **DX-V2. Hình minh hoạ đúng lời đang hứa.** Ở các nhịp then chốt (vòng mở, câu móc lại, bước ngoặt, payoff), hình phải minh hoạ đúng điều lời đang nói và người xem hiểu trong 1 giây. Nguồn: sổ gu (d) [Am 17]. `[NGƯỜI]`
- **DX-V3.** Vùng an toàn chữ 90% [B §4.2]. `[MÁY]`
- **DX-V4.** Hai nhân vật giữ phía, màu và **hình dạng** riêng suốt phim (thời gian chạy trái → phải). Phân biệt được khi mô phỏng deuteranopia, protanopia và ở thang xám [B §4.3–4.4]. `[MÁY]`
- **DX-V5.** Mọi màu lấy từ token (`genre-spec/channel/visual-tokens.json`) qua một bảng grade. Grain và vignette nhẹ, cố định. Không banding trên gradient tối [B §4.4]. `[MÁY]`
- **DX-V6.** Tương phản chữ ≥ 4,5:1, và ≥ 7:1 cho chữ mức 1 [B §4.4; BUILDERS.md]. `[MÁY]`
- **DX-V7. Hoạt hình.** Có lấy đà, theo đà, chồng lớp chuyển động, cung chuyển động, dàn cảnh. Chữ động theo nhịp lời [B §4.5; RB H6]. Bài D chấm 4/5. `[NGƯỜI]`
- **DX-V8. Máy quay có lý do.** Mỗi chuyển động máy có lý do ghi trong shot list, có quán tính (lấy đà, vượt nhẹ), không tuyến tính [B §4.1, §4.3 phần 2D]. `[MÁY: mọi shot có đủ trường]`
- **DX-V9. Chữ sắc nét khi máy chuyển.** Không nhân đôi, không nhoè nhãn. Bài D để lọt lỗi này ở 15 s đầu vì máy kiểm miễn chấm đoạn máy chuyển [Au §3a, §6 D-2]. Lỗi phải được canh (CHARTER §7.3). `[MÁY]`
- **DX-V10. Chuyển cảnh.** ≥ 5 match cut (hình học hoặc ý nghĩa); ≥ 4 J-cut hoặc L-cut; không dùng dissolve mặc định [B §4.6]. Với biểu đồ nối tiếp, nhiều điểm cắt cố ý không thấy rõ. Luật "cắt thấy được" (R06) của bài D không hợp với thể loại này; K1 quyết định [Am 15]. `[MÁY]`
- **DX-V11. Giữ các luật bài C** [B §4.7]:
  - đồng bộ số–lời ±250 ms theo giá trị cuối;
  - đọc được ở cỡ 25%;
  - hiểu được ở thang xám;
  - không lặp một layout quá 2 lần trong 90 s;
  - tỷ lệ cột đúng;
  - biểu đồ đường có trục và nhãn neo. Luật C04 của bài D áp nhầm vào hình tô kín (Au §4.4).
  `[MÁY]`
- **DX-V12. Tiền kỳ.** Nộp storyboard, shot list, color script. Mỗi shot có cỡ cảnh, chuyển động máy và lý do [B §4.1, bỏ trường "tiêu cự giả lập" và "góc máy 3D"]. `[MÁY]`

## 6. Âm thanh theo dữ liệu, nhạc, lời, mix

- **DX-A1. Âm thanh theo dữ liệu (sonification).** Mỗi phần tử biểu đồ khi biến động có tiếng riêng, bắt đầu đúng khung phần tử đổi, và **nghe thấy được**. Cột mọc cho âm lên tới cao độ theo giá trị (thang cố định cho cả phim), đường vẽ cho âm liên tục theo độ dốc, điểm xuất hiện cho tiếng gảy theo trục y. Khi > 8 sự kiện/giây thì gộp thành cụm [Am 19a; R M3 vòng 3]. Mức duck của vòng 3 (−10 dB dưới lời, −16 dB quanh số) chưa được chấm là "nghe thấy được". Xem sổ gu (a). `[MÁY + NGƯỜI]`
- **DX-A2. Nhạc không lộ vòng lặp.** Mỗi hồi có phối khí riêng; vòng hợp âm xoay theo câu nhạc; leitmotif của mỗi nhân vật biến tấu theo số phận [B §5.2; Am 19b; RB H7]. Đo độ tự tương đồng giữa hai câu 4 ô liền nhau; bài D vòng 3 đạt 0% cặp ≥ 0,90 [R M3 vòng 3]. Xem sổ gu (b). `[MÁY + NGƯỜI]`
- **DX-A3. Nhạc sinh bằng code** (hoặc nguồn có giấy phép), có sổ giấy phép. Không sóng sin trơn: phải có envelope, filter, và một không gian reverb thống nhất. Đổi hoà âm ở bước ngoặt. Tempo map khớp dựng; điểm nhấn khớp cú cắt ±1 khung [B §5.2]. `[MÁY]`
- **DX-A4. Spotting và cue sheet.** Mỗi cue ghi thời điểm, chức năng kịch tính, key, tempo, và chỗ nào im kèm lý do [B §5.1]. `[MÁY]`
- **DX-A5. Sound design.** Whoosh theo chuyển động máy, cường độ theo tốc độ; riser vào mỗi lần hé lộ; impact tại con số quyết định; room tone; pan theo vị trí ngang [B §5.3]. `[MÁY]`
- **DX-A6. Số được nói có khoảng không riêng.** Nhạc và sfx hạ từ 0,5 s trước tới 1,6 s sau mỗi số được đọc; cắt đuôi câu quyết định +250 ms [Am 14; R M3]. `[MÁY]`
- **DX-A7. Lời đọc.**
  - Chỉ đạo diễn xuất từng câu.
  - Trung bình mỗi hồi 150–160 wpm; mọi câu 120–190 wpm [B §5.4; Am 8].
  - Mọi từ quan trọng có mặt trong ASR [B §5.4].
  - Xử lý giọng: khử sibilance, EQ, nén nhẹ.
  - Giọng ElevenLabs **không giãn thời gian**; lệch nhịp thì sinh lại take hoặc đổi `speed` [Am 1].
  - Đo wpm trên take sạch và trên bản trộn lệch nhau khoảng 7–9 wpm. Phải khai rõ đo trên cái nào [Am 16].
  `[MÁY]`
- **DX-A8. Giọng.** Hiện dùng tạm Eric `eleven_v3` (ElevenLabs), `eleven_multilingual_v2` làm dự phòng từng câu. Đây **không phải quyết định chọn giọng #158**; chọn giọng cuối là việc irreversible, chỉ chủ dự án quyết [Am 7; CH §7.5]. `[NGƯỜI]`
- **DX-A9. Mix.**
  - Lời là ưu tiên số một.
  - Nhạc khoét dải 1–4 kHz khi có lời (ducking đa dải).
  - Nhạc thấp hơn lời 18–22 dB (trung bình năng lượng).
  [B §5.5] `[MÁY]`
- **DX-A10. Master.**
  - −14 LUFS ±1; true peak ≤ −1 dBTP; LRA 6–10 LU.
  - Không clip; tương quan pha trung bình > 0,3; nghe được khi gộp mono.
  - Bài D đạt −14,0 LUFS, LRA 7,6, TP −1,8 dBTP.
  [B §5.6; R M3] `[MÁY]`

## 7. Kỹ thuật file

- **DX-F1.** 1920×1080, 30 fps CFR (quyết định #92) [B §0]. `[MÁY]`
- **DX-F2.** H.264 High, yuv420p, ≥ 16 Mbps. Metadata BT.709 (primaries, transfer, matrix), dải limited [B §6]. `[MÁY]`
- **DX-F3.** Không rơi hay lặp khung (theo PTS). Hình và tiếng cùng bắt đầu, lệch độ dài ≤ 25 ms [B §6; R M3 sync]. `[MÁY]`
- **DX-F4.** AAC 48 kHz 320 kbps stereo [B §6]. `[MÁY]`
- **DX-F5.** Phụ đề SRT khớp kịch bản 100%: ≤ 42 ký tự mỗi dòng, ≤ 2 dòng, mỗi cue 1–7 s, không có cue mồ côi [B §6; R M3 F09]. `[MÁY]`
- **DX-F6.** Chapters: ≥ 3 mốc, mỗi mốc ≥ 10 s, bắt đầu từ 0:00 [B §6]. `[MÁY]`
- **DX-F7.** Giao stem (voice, music, sfx, whoosh, room) kèm master, có SHA-256. Mỗi báo cáo kiểm ghi SHA của master nó chấm. Bài D thiếu stem M3 nên 6 luật không kiểm độc lập được [Au §2, §6 D-1; R M3 vòng 3]. `[MÁY]`

## 8. Đóng gói

- **DX-P1.** 3 phương án tiêu đề theo `genre-spec/channel/title-formulas.*` [B §7]. `[MÁY]`
- **DX-P2.** 3 thumbnail 1280×720 theo `genre-spec/channel/thumbnail-spec.md`, chỉ dùng token, đọc được ở cỡ 10% [B §7]. `[MÁY]`
- **DX-P3.** Thumbnail không gợi ý kết luận mà video không đưa ra [B §7]. `[NGƯỜI]`
- **DX-P4.** Mô tả có: nguồn (URL, năm dữ liệu), giả định, chapters, "not advice", và ghi rõ giọng tổng hợp [B §7]. `[MÁY]`

## 9. Khả năng tiếp cận

- **DX-X1.** Phụ đề đầy đủ (DX-F5).
- **DX-X2.** Tương phản chữ (DX-V6).
- **DX-X3.** Nhân vật và chuỗi dữ liệu không chỉ phân biệt bằng màu: dùng thêm hình dạng, nét liền hay đứt, và vị trí (DX-V4).
- **DX-X4.** Hiểu được ở thang xám và ở cỡ 25% (DX-V11).
- **DX-X5.** Nghe được khi gộp mono (DX-A10).

[B §4.4, §4.7, §5.6, §6; CH §5]

## 10. Đạt phát hành

- Máy kiểm không trượt luật cứng, không hồi quy.
- Điểm phiếu chấm của chủ dự án trung bình ≥ 4/5, không câu dưới 3.

[CH §5; RB]

Bài D dừng ở 3,29 (vòng 2: H1 4 · H2 2 · H3 3 · H4 3 · H5 4 · H6 4 · H7 3), chưa đạt [R M3 vòng 3].

Phiếu chấm tay cho Tập 1 do K1 soạn lại từ các mục `[NGƯỜI]` ở trên.
