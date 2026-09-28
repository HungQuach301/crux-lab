# checks/ — máy kiểm của crux-lab (Phiên K1, khoá SHA)

Bộ luật này chấm mọi yêu cầu `[MÁY]` của [`genre-spec/data-explainer.md`](../genre-spec/data-explainer.md). Các yêu cầu `[NGƯỜI]` nằm trong [`RUBRIC.md`](RUBRIC.md) (H1–H8). Danh sách artefact bên dựng phải giao nằm trong [`CONTRACT.md`](CONTRACT.md).

Khoá: `checks/LOCK` là SHA-256 của toàn thư mục (cách tính ở cuối file).
- Bên dựng không sửa thư mục này (CHARTER §7.1, §8).
- Cho rằng một luật sai thì ghi khiếu nại. Luật chỉ đổi qua vai kiểm, và cần chủ dự án duyệt.

Gốc: `checks/` của bài D (`crux-spike-opus55`, nhánh `spike/opus55-cine`, LOCK `0478df73…`), đã sửa theo audit `audit/d-final` (`audit/REPORT.md` @ `afad899`). Các thay đổi ghi ở mục "Thay đổi so với bài D".

## Chạy

```
pip install numpy scipy soundfile av faster-whisper      # ffmpeg, ffprobe trên PATH; Node ≥ 18 và playwright (Chromium)
checks/run.sh [root] [--baseline <báo cáo kiểm của phiên bản trước>.json | --first]
checks/selftest/run.sh [thư-mục-kết-quả]                 # test tự chứng minh
```

`run.sh` chạy hai bước:
1. `node checks/page/sampler.js <root>`: bộ lấy mẫu trang dựng.
2. `python3 checks/py/run.py <root>`: mọi luật.

Kết quả ghi vào `<root>/out/checks/report.json` và `report.md`. Báo cáo ghi LOCK và SHA-256 của master được chấm.

Trạng thái của một luật:
- **PASS**: đạt.
- **FAIL**: trượt.
- **MISSING**: thiếu artefact, tính là không đạt.
- **ERROR**: luật lỗi, tính là không đạt.

`near` liệt kê mọi chỉ số nằm trong 5% quanh ngưỡng.

**REG (cổng hồi quy)** cần báo cáo kiểm của phiên bản trước (`--baseline`). Báo cáo này do phiên kiểm giữ, không lấy từ cây của bên dựng. Phiên bản đầu tiên chạy với `--first`. Không có cả hai thì REG là MISSING.

## Nguyên tắc đo

- Đo trên file đã giao: khung giải mã từ `out/video.mp4`, âm thanh giải mã, stem, ASR tự chạy.
- Không tin số khai báo khi đo được. File khai báo chỉ nói *đo ở đâu*, và luôn được đối chiếu với hình hoặc tiếng.
- **ASR** dùng faster-whisper `small.en` (int8, có mốc thời gian từng từ).
  - Audio được cắt **theo câu**: mỗi câu của `out/script.json` là một đoạn `[start − 0,6 s, end + 0,6 s]`.
  - Lý do: Whisper chạy cả file dài làm rơi từ (REPORT-D M3 vòng 3).
  - Hai đoạn kề nhau chồng lên nhau. Một từ thuộc về câu có phần thời gian chứa trung điểm của từ đó, nên mỗi từ chỉ được giữ một lần.
  - Nếu lượt giải mã đầu có ít hơn 85% số từ của câu, máy giải mã lại đoạn đó (có VAD) và giữ lượt có nhiều từ hơn. Trên bài D, lượt đầu bỏ mất "and the portfolio is rebalanced once a year" (671 s); lượt hai nghe đủ. Một từ không được đọc thì không lượt nào nghe thấy.
- **Luật khung hình** chạy qua trang dựng (hợp đồng `window.CHECKS`).
  - Đối tượng lấy mẫu mỗi 0,1 s.
  - Điểm ảnh lấy mẫu mỗi 0,2 s: mặt nạ lớp chữ và lớp đồ hoạ của trang, cộng khung video đã giải mã.

### Khung máy quay đang chuyển: không còn miễn trừ

Bài D bỏ qua mọi luật bố cục và luật chữ trong đoạn máy chuyển ở đầu cảnh. Nhờ vậy lỗi chữ nhân đôi ở 15 s đầu lọt qua (audit §3a, §6 D-2). Theo CHARTER §7.3, miễn trừ đó được thay bằng các tiêu chí sau.

| Nhóm luật | Trong khung máy chuyển, nay chấm thế nào |
|---|---|
| Chữ: **V12** (mới) | Mọi khung, mọi chữ. So chữ trên video với bản dựng sạch của trang ở cùng thời điểm, bằng tương quan chuẩn hoá (NCC) của luma, phải ≥ 0,97. Chữ nhân đôi, nhoè hoặc mờ chuyển động đều trượt. |
| Chữ: **V03** vùng an toàn | Mọi khung. Chỉ chữ **đang đi** (hộp dịch ≥ 4 px trong 0,1 s, tức đang vào hoặc ra khỏi khung) được chạm mép. |
| Chữ: **V08** tương phản, **C14** đọc được ở 25% | Mọi khung, với chữ **đứng yên trên màn hình** (dịch < 2 px trong 0,1 s). Chữ đang đi do V12 chấm, và được V08/C14 chấm lại khi đã dừng. |
| Chữ: **V11** va chạm | Mọi khung. Chữ đứng yên: một mẫu va chạm là trượt. Chữ đang đi: trượt khi cùng một va chạm có ở hai mẫu liên tiếp (0,2 s). Chữ lướt qua một đường trong chốc lát thì không tính. |
| Bố cục: C01, C03, C04, C07, V02, C12 | Chấm ở hai đầu đã dừng của cú máy. Phần giữa cú máy được giới hạn bởi **V13** (mới): mỗi cú ≤ 3,0 s, tổng thời gian trong cú máy ≤ 15% phim. |

"Trong cú máy" được **đo** từ `out/camera.json`: tốc độ máy ≥ 0,10 bề rộng khung/giây. Không có file đó thì dùng `scenes[].move` khai báo.

## Thay đổi so với bài D (LOCK `0478df73…`)

| Mã | Thay đổi | Lý do |
|---|---|---|
| A14 | `stem()` chuẩn hoá hai phía cùng một cách: bỏ sở hữu cách, rồi một biến tố, rồi `e` cuối. Nhờ vậy `retiree`, `retirees`, `retiree's` gặp nhau. `asr_join` nối token bắt đầu hoặc kết thúc bằng `&`, nên "S" "&P" thành "S&P". `words()` giữ "S&P" là một từ; khi so, token nối bằng `&` cũng được tính theo từng phần ("Standard&Poor's" có standard và poor). ASR cắt theo câu, giải mã lại khi thiếu từ. | audit §4.1, §4.2; REPORT-D (Whisper rơi từ khi chạy cả file) |
| C04 | Chỉ nét hở mới là chuỗi đường: `role:"series"`, hoặc path/polyline không tô, ≥ 10 đỉnh, nét màu chuỗi. Hình tô kín (biểu đồ tròn, "đống tiền") không còn bị đếm. | audit §4.4: 364 khung dương tính giả |
| R03 | Đo trên stem giọng (bắt buộc). Khoảng lặng bắt đầu ở đoạn ≥ 120 ms dưới −45 dBFS đầu tiên, bắt đầu trong [cuối số − 0,25 s, cuối số + 0,8 s], và kéo dài tới khi giọng trở lại ≥ 30 ms. Cụm số được nối thêm các từ đơn vị theo sau ("dollars", "percent", …). | audit K-4: đuôi của chính từ vừa đọc bị lấy làm hết khoảng lặng. audit K-5: "dollars" bị bỏ qua. |
| V03, V08, V11, C14, V12, V13 | Bỏ miễn trừ khung máy chuyển, thay bằng tiêu chí riêng (bảng trên). | audit §3a, §6 D-2; CHARTER §7.3 |
| V06, V07 | **Bỏ**: rack focus 3D; làm mờ chuyển động siêu lấy mẫu 8×. | CH §5, Am 11–13, DX §0 |
| V01 | Bỏ trường `focalMm` và `angle` (tiêu cự giả lập, góc máy 3D). Còn `size`, `move`, `moveReason`. | DX-V12 |
| V05, A10 | Đọc máy quay 2.5D `{t, x, y, zoom}`. Vẫn đọc được dạng cũ. Tiêu chí quán tính (lấy đà, vượt nhẹ, không tuyến tính) giữ nguyên. | DX-V8 |
| T1, T2, T3, REG | **Mới**: âm thanh theo dữ liệu nghe thấy được; nhạc không lặp; vào khoảng lặng có chuyển tiếp và sàn room tone; cổng hồi quy. | sổ gu G-001, G-002, G-003; CHARTER §5 |
| Mọi luật | Cột "mục" trỏ sang mã spec `DX-…`. Mỗi luật có `fingerprint` (SHA của định nghĩa đo và ngưỡng) để REG biết luật nào so được. | CHARTER §10 |

Quyết định của K1 về DX-S11: A14 đã sửa, nên cách né ở lời đọc (bỏ sở hữu cách, đọc "Standard & Poor's 500 index") không còn cần cho máy kiểm. Bên dựng được viết tự nhiên. Việc này chờ chủ dự án duyệt.

Giữ nguyên, K1 chưa quyết:
- R06 ("cắt thấy được trong hình"): DX-V10 ghi rằng luật này có thể không hợp với biểu đồ nối tiếp. Đổi luật cần chủ dự án duyệt.
- Các luật gắn với mô hình và nhân vật của bài D (S01, S05, S06, V04, V09: `1966`/`mirror`, 60/40, 4%): tập mới cần hợp đồng riêng cho mô hình của nó.

## Ngưỡng tạm (chủ dự án duyệt 2026-09-28)

Chủ dự án duyệt khoá `62b5206d…` ngày 2026-09-28, kèm điều kiện sau. Các ngưỡng dưới đây là **NGƯỠNG TẠM**. Chúng được hiệu chỉnh sau Tập 1 bằng điểm chấm tay của chủ dự án (phiếu `RUBRIC.md`, H5 cho V12/V13, H7 cho T2, H8 cho T1/T3).

| Luật | Ngưỡng tạm |
|---|---|
| T1 | độ nổi ≥ 3 dB; ≥ 1 dB trong cửa sổ số được đọc |
| T2 | câu nhạc lặp ≤ 5% |
| T3 | chuyển tiếp vào khoảng lặng 150–400 ms; sàn master ≥ −80 dBFS, room ≥ −75 dBFS |
| V12 | NCC ≥ 0,97 |
| V13 | mỗi cú máy ≤ 3 s; tổng thời gian máy chuyển ≤ 15% |

**Mọi thay đổi ngưỡng về sau cần chủ dự án duyệt, và phải khoá lại** (LOCK mới, CHARTER §7.1). Bên dựng không đổi ngưỡng. Phiên kiểm cũng không tự đổi ngưỡng khi chưa được duyệt.

## Luật mới: định nghĩa và cách đo

**T1 — âm thanh theo dữ liệu nghe thấy được** (DX-A1, sổ gu G-001)

1. **Sự kiện.** Hợp của hai nguồn:
   - sự kiện khai báo trong `out/sonify-events.json`: `f0` của mỗi cột, `f` của mỗi điểm, lúc bắt đầu mỗi lần vẽ đường;
   - sự kiện biểu đồ bộ lấy mẫu tự đo: camera giữ đứng, trang tiến 0,1 s, và một hình `bar`/`series`/`mark` (hoặc hình mang `char`) hiện ra hay đổi hộp ≥ 1 px.
   
   Các sự kiện cách nhau ≤ 0,15 s gộp thành một cụm. Mỗi cụm được đo ở lúc bắt đầu, và mỗi 0,5 s sau đó cho tới hết cụm.
2. **Độ nổi.** Đo trong cửa sổ `[t, t + 0,15 s]`, ở dải 1,5–8 kHz (Butterworth bậc 4):
   - độ nổi = 10·log10((P_son + P_rest) / P_rest);
   - P_son là công suất trong dải của stem `sonify`;
   - P_rest là công suất trong dải của tổng các stem còn lại (voice, music, whoosh, room, sfx).
   
   Độ nổi đo mức một tiếng làm dải đó to lên so với nền đang có.
3. **Ngưỡng.**
   - Độ nổi ≥ 3 dB, tức tiếng theo dữ liệu có công suất trong dải ít nhất bằng tất cả phần còn lại cộng lại.
   - Mức dải của chính tiếng đó ≥ −60 dBFS.
   - Trong cửa sổ số được đọc `[onset − 0,5 s, end + 1,6 s]` (ASR riêng), DX-A6 cho hạ sfx, nên ngưỡng là ≥ 1 dB. Đây là tiêu chí thay thế, không phải miễn trừ.
4. **Kiểm thật.** Tổng các stem phải khớp master trong dải (tương quan ≥ 0,90). Phải giao stem `sonify` riêng: nếu tiếng dữ liệu trộn vào `sfx` thì các hiệu ứng khác cũng bị tính là tiếng dữ liệu. Khi đó luật vẫn đo trên `sfx` và báo số, nhưng không thể đạt.

**T2 — nhạc không lặp** (DX-A2, sổ gu G-002)

- **Đặc trưng.** Mỗi ô nhịp (4 phách từ `out/tempo-map.json`) cho một vector chroma 12 bậc (55–2000 Hz) và một mẫu onset 16 bước. Mỗi câu nhạc gồm 4 ô.
- **Độ tự tương đồng** của một câu = cosine lớn nhất với các câu cách nó 1, 2, 3 và 4 câu. Vòng lặp dài 1–4 câu nhạc sẽ lộ ở một trong các độ trễ này.
- **Lặp** = độ tự tương đồng ≥ 0,90.
- **Ngưỡng.**
  - Lặp ≤ 5% số câu.
  - Không có 2 câu lặp liền nhau, vì như thế là cùng 4 ô nhạc nghe ba lần.
  - Đo được ≥ 8 câu. Câu nhỏ hơn −50 dBFS bị bỏ qua.

**T3 — vào khoảng lặng** (DX-R6, sổ gu G-003)

- **Khoảng lặng** giống A09: đoạn master ≤ −40 dBFS dài 0,8–1,5 s.
- **Nền (bed)** = music + sfx + whoosh (+ sonify).
- **Chuyển tiếp vào** được đo từ lúc nền còn cách mức trước khoảng lặng 3 dB tới lúc nền đã xuống 30 dB (hoặc < −70 dBFS). Mức trước khoảng lặng lấy phân vị 90 trong `[start − 0,8, start − 0,1]`.
- **Ngưỡng.**
  - Chuyển tiếp dài 150–400 ms. Cắt cứng thì trượt, và kéo lê quá dài cũng trượt.
  - Sàn room tone: trong khoảng lặng (bỏ 0,1 s ở mỗi đầu), master không xuống dưới −80 dBFS, và stem room có mức trung bình ≥ −75 dBFS. Không bao giờ im số tuyệt đối.

**REG — cổng hồi quy** (CHARTER §5)

- Luật **so được** khi có mặt trong cả hai báo cáo và định nghĩa không đổi:
  - cùng `fingerprint`;
  - hoặc, với báo cáo cũ chưa có fingerprint: cùng câu ngưỡng, và không nằm trong danh sách luật K1 đã đổi cách đo (`CHANGED_SINCE` trong `py/run.py`).
- Một luật so được, PASS ở phiên bản trước mà nay không PASS, là **hồi quy** và chặn phát hành.
- Báo cáo liệt kê các luật không so được và các luật đã cải thiện.

## Test tự chứng minh

`checks/selftest/run.sh` chạy hai phần. Mỗi luật có một fixture **phải trượt** và một fixture **phải đạt**.

- **`test_py.py`** cho luật Python.
  - Video và âm thanh là tổng hợp (ffmpeg, numpy).
  - Luật nghe lời được cấp bản chép cố định qua bộ đệm ASR, nên test kiểm logic luật chứ không kiểm bộ nhận dạng.
  - Phép cắt ASR theo câu có test riêng (`A14/asr-cut`).
  - REG có test riêng.
- **`test_page.js`** cho luật khung hình.
  - Một trang sạch mà mọi luật khung hình phải đạt, cộng một fixture trượt cho từng luật hay biến thể.
  - Video của mỗi fixture dựng từ chính trang đó. Riêng V12 dựng video khác trang: nhãn nhân đôi, nhãn nhoè.
  - Các ca mới:
    - C04 với biểu đồ tròn (phải đạt) và với nét hở không trục (phải trượt);
    - V03 trong cú máy khai báo (phải trượt: không còn miễn trừ);
    - chữ đang đi qua mép khung và qua đường (V03, V11 phải đạt);
    - V12 nhãn nhân đôi và nhãn nhoè (phải trượt);
    - T1: bộ lấy mẫu phải thấy điểm hiện ra và cột mọc, và không được sinh sự kiện từ phần tĩnh.

## Bảng luật

75 luật. **(mới)** = thêm ở khoá này; *(sửa)* = đổi cách đo so với bài D. Bỏ: V06, V07.

| Mã | Spec | Định nghĩa đo | Ngưỡng | Máy |
|---|---|---|---|---|
| F01 | DX-F1, DX-F2 | ffprobe of the video stream: codec, profile, pixel format, frame size, display aspect | h264 / High / yuv420p / 1920×1080 / 16:9 (square pixels) | Python |
| F02 | DX-F1 | r_frame_rate and avg_frame_rate from the stream header, and every packet duration (PTS step) in stream time base | both rates exactly 30/1 and every PTS step = 1/30 s (constant frame rate) | Python |
| F03 | DX-F3 | video packet PTS sorted: a repeated PTS is a duplicated frame, a step of k>1 frame periods is k-1 dropped frames; frame count compared with duration × 30 | dropped = 0, duplicated = 0, first PTS = 0, \|frames − duration×30\| ≤ 1 | Python |
| F04 | DX-F2 | video bitrate = sum of video packet sizes × 8 / stream duration (measured, not the header value) | ≥ 16 Mbps | Python |
| F05 | DX-F2 | stream colour tags (color_primaries, color_transfer, color_space, color_range) + decoded luma codes of 1 frame/10 s: share of Y samples outside 16–235 | all tags bt709, range tv (limited); Y outside 16–235 ≤ 0.1% of samples | Python |
| F06 | DX-F4 | ffprobe of the audio stream; bitrate = audio packet bytes × 8 / duration | AAC (LC), 48 kHz, 2 channels, measured ≥ 272 kbps (= 85% of the 320 kbps nominal: ffmpeg's native AAC at -b:a 320k measured 276 kbps on test C's master, so the measure allows its ABR undershoot but not a 256k or lower setting) | Python |
| F07 | DX-S1 (CH §1 length) | container duration (ffprobe format.duration) | ≥ 600 s (10:00) | Python |
| F08 | DX-V5 | decoded luma of 1 frame/2 s; banding score per frame (banding_score: 240 px tiles, mean Y ≤ 80, 16-px block means fitting a plane that spans 2–40 codes with residual ≤ 1 code; share of their pixels in flat runs ≥ 12 px ending in a 1–2 code step) | worst frame ≤ 5% (frames with < 1% dark-gradient area are skipped) | Python |
| F09 | DX-F5 | out/captions.srt parsed; joined subtitle text vs joined narration text of out/script.json (whitespace-normalised, exact characters otherwise); per cue: characters per line, lines, duration; cues must not overlap | text identical (100%); every line ≤ 42 chars; ≤ 2 lines; 1.0 ≤ duration ≤ 7.0 s; 0 overlaps | Python |
| F10 | DX-F6 | chapters from out/package/description.md (lines "m:ss Title") and, if present, the MP4 chapter atoms; chapter length = next start − start (last: to end of video) | ≥ 3 chapters; first at 0:00; each ≥ 10 s; MP4 chapters (if any) equal the description's | Python |
| A01 | DX-A10 | integrated loudness of the video's audio track, ITU-R BS.1770-4 (ffmpeg ebur128) | −14 LUFS ± 1 (−15 … −13) | Python |
| A02 | DX-A10 | true peak, 4× oversampled (ffmpeg ebur128 peak=true), max over both channels | ≤ −1.0 dBTP | Python |
| A03 | DX-A10 | loudness range (EBU Tech 3342, ffmpeg ebur128) | 6 … 10 LU | Python |
| A04 | DX-A10 | decoded audio samples (float) with \|x\| ≥ 0.999 (full scale), and runs of ≥ 2 consecutive such samples | 0 samples | Python |
| A05 | DX-A10 | stereo phase correlation r = ΣLR/√(ΣL²ΣR²) per 100 ms window, windows with RMS > −50 dBFS; mean over windows. Also share of windows with r < 0 (out-of-phase content) | mean r > 0.3; windows with r < 0 ≤ 5% | Python |
| A06 | DX-A10, DX-X5 | mono fold-down (L+R)/2 played as dual mono: integrated loudness vs the stereo mix (BS.1770), and voice-band (300–3400 Hz) energy of the fold-down vs the mean of L and R | mono loudness ≥ stereo − 3 LU; voice-band loss ≤ 3 dB | Python |
| A07 | DX-A9 | stems voice and music; 100 ms windows where voice is active (voice RMS > −45 dBFS); level gap = 10·log10(mean voice power) − 10·log10(mean music power) over those windows | 18 … 22 dB | Python |
| A08 | DX-A9 | music stem around each voice onset (≥ 0.6 s voice-free before, ≥ 0.6 s voice after): band levels (Welch PSD) in [t−0.6, t−0.1] vs [t+0.1, t+0.6]. presence drop = drop of 1–4 kHz; low drop = drop of 60–500 Hz. Medians over onsets | median presence drop ≥ 6 dB AND median (presence drop − low drop) ≥ 3 dB (the dip is band-limited, not broadband); ≥ 3 onsets measured | Python |
| A09 | DX-R6 | master: spans where RMS (50 ms window, 10 ms hop) stays ≤ −40 dBFS; intentional silence = such a span lasting 0.8–1.5 s (the first and last 2 s of the video excluded) | ≥ 3 spans of 0.8–1.5 s | Python |
| A10 *(sửa)* | DX-A5 | camera moves from out/camera.json (speed in frame widths/s, see camera_speed: 2.5D or legacy form, > 0.05, gaps < 0.2 s merged, ≥ 0.3 s); per move: peak speed vs peak whoosh-stem RMS (50 ms) in [start − 0.3 s, end + 0.3 s] | Spearman ρ(peak speed, whoosh dB) ≥ 0.6 over ≥ 5 moves; every move with peak ≥ 0.3 fw/s has a whoosh ≥ −45 dBFS | Python |
| A11 | DX-A5 | out/sfx-events.json (t, x in screen px of the sounding object); pan measured in the sfx stem over [t, t + 0.15 s]: (E_R − E_L)/(E_R + E_L); events with stem RMS > −50 dBFS | Pearson r(pan, (x − 960)/960) ≥ 0.7 over ≥ 8 events | Python |
| A12 | DX-A3 | out/tempo-map.json: accents[] and beats[]; cuts from out/transitions.json. Music onsets detected in the music stem (spectral flux). An accent "lands" when a cut is within ±1 frame (±33.3 ms); it is "real" when a music onset is within ±1 frame | ≥ 5 accents; 100% of accents land on a cut; ≥ 90% of accents are real; ≥ 70% of beats while music is audible have an onset within ±50 ms | Python |
| A13 | DX-A7 | out/voice/takes.json: for each take, the raw TTS file and the final (stretched) file; stretch = active speech span of final / of raw (span between first and last 20 ms window above −45 dBFS) | every \|stretch − 1\| ≤ 0.10 | Python |
| A14 *(sửa)* | DX-A7 | own ASR (faster-whisper small.en, int8, word timestamps) of the video's mixed audio, recognised sentence by sentence (asr_master). Key words per script sentence (out/script.json): every number, every proper name, every defined term (locked list DEFINED_TERMS + out/terms.json). A key word is heard if the ASR has it (numbers compared as values; names/terms by stem(), the same normal form on both sides: possessive, then one inflection, then a final e; "S&P" as S&P or "S and P", ASR tokens "S" "&P" joined; a joined token also counts by its parts, so "Standard&Poor’s" has standard and poor) among words starting within the sentence window [start − 1.5 s, end + 1.5 s] | 0 key words missing (no percentage threshold) | Python |
| A15 *(sửa)* | DX-A7 | own ASR words inside each sentence window; sentence rate = words of `spoken` / (last ASR word end − first ASR word start) × 60; act rate = Σ words / Σ sentence spans of the act (sentences of < 4 words are left out of the per-sentence cap) | every act 150 … 160 wpm; no sentence > 175 wpm | Python |
| S01 | DX-H1 | independent re-computation of every path in out/model.json from data/normalized/annual.csv with the brief's model (60/40 S&P 500 TR / 10-y Treasury, yearly rebalance, start-of-year withdrawal, year 1 = 4% of initial, then × (1 + previous year's inflation), 30 years, no tax, no fee); compared value by value (withdrawals, end-of-year nominal and real balances, depletion year) | model parameters exactly 0.60/0.40, 4%, 30 years; every value within max($0.50, 1e-6 relative); 0 mismatches | Python |
| S02 | DX-H1 | visible on-screen text (page sampler text track, every 0.1 s): phrases for "no taxes" and "no fees" (regex NO_TAX / NO_FEE), looked for in the methodology card scenes (act "method") and in the rest of the video | both phrases visible in the methodology card AND both visible outside it | trang + Python |
| S03 | DX-H4 | data/sources.json: per raw file path, url, sha256, downloaded (ISO date), terms {quote, url}; SHA-256 recomputed from the committed file; hosts of primary (Damodaran) and cross-check (FRED) sources | every file present with matching SHA-256, valid date, http(s) URL, terms quote ≥ 20 chars and terms URL; a primary file on pages.stern.nyu.edu; a cross-check file on fred.stlouisfed.org | Python |
| S04 | DX-H5 | data/normalized/annual.csv (primary) vs data/normalized/fred_inflation.csv (FRED CPI) and, if present, data/normalized/stocks2.csv; years used = 1928 … 2025 (every 30-year window 1928–1996); \|primary − cross-check\| per year in percentage points vs the tolerance declared in data/sources.json | declared tolerance ≤ 0.5 pp (inflation) and ≤ 0.5 pp (stocks); every year outside tolerance is listed in sources.json "mismatches" (reported, not silently resolved); every used year present in both | Python |
| S05 | DX-H1, DX-H2 | geometric mean of the 60/40 yearly return, recomputed for 1966–1995 and for the mirror sequence (1995 → 1966); the displayed claims (claims with character "1966"/"mirror" and kind "geomean") compared with the recomputation; mirror claims flagged illustrative | \|G(1966) − G(mirror)\| ≤ 0.01 pp; each displayed geomean claim within 0.005 pp of its recomputation; every mirror claim illustrative | Python |
| S06 | DX-H6 | page sampler: objects with a `year` attribute visible (opacity > 0.5, on frame) in act-3 frames; union over act 3 | every start year 1928 … 1996 shown (69 of 69), including years where order did no harm | trang + Python |
| S07 | DX-H1, DX-H2 | claims registry out/claims.json vs what is shown and said. On screen: every number in visible text (page sampler) must sit inside a claim span (data-claim). Narration: every number in out/script.json text must equal (value+unit) the display of a claim listed for that sentence's scene. Every claim: formula; source or illustrative; historical (source) claims carry dataYear | 0 orphan numbers on screen; 0 unregistered numbers in narration; 0 claims without formula; 0 unsourced non-illustrative claims; 0 sourced claims without dataYear | trang + Python |
| S08 | DX-H2 | page sampler, every 0.1 s and every frame in ±0.5 s around each first appearance: frames where an illustrative claim span is visible (opacity > 0.5, on frame) but no ILLUSTRATIVE badge is visible; and badge lag = first frame the claim is visible − first frame a badge is visible in that scene | 0 frames without badge; badge never later than the number (lag ≤ 0 frames) | trang + Python |
| S09 | DX-H3 | claims whose display contains "$" must declare basis nominal\|real. Screen (page sampler): whenever a $ claim is visible, a visible text in the same text block or within 300 px carries its basis word (BASIS regex). Narration: the sentence with the $ number, or the one before it in the same scene, carries the basis word | 0 money claims without basis; 0 frames missing the on-screen basis; 0 narration sentences missing it | trang + Python |
| S10 | DX-I1, DX-I2 | every narration sentence (out/script.json text) and every visible on-screen text, lower-cased, against locked regex lists: ADVICE, FORECAST, FOUR (4% as a recommendation), WE_BAD ("we/our/us" used for the viewer); required phrases "US only" and "history, not a forecast" (narration or screen) | 0 matches of ADVICE, FORECAST, FOUR, WE_BAD; both required phrases present | Python |
| S11 *(sửa)* | DX-S6 | claims with core=true. Appearances = distinct scenes where the claim is visible (page sampler) or spoken (heard by own ASR in that scene's narration window). Declared callbacks[] each need scene + distinct non-empty meaning, and must be real appearances | ≥ 1 core claim; each core claim appears in ≥ 3 distinct scenes spanning ≥ 2 acts; ≥ 3 declared callbacks with distinct meanings, all verified | trang + Python |
| S12 | DX-S7 | new number = first appearance (screen or narration) of a claim; axis-role claims (role "axis", only ever shown as axis labels/anchors per the page sampler) excluded. Scene of a new number = scene containing its first-appearance time | new numbers ≤ duration / 8 s; no scene with > 2 new numbers; 0 claims marked axis but shown outside axis labels | trang + Python |
| S13 | DX-S8 | sentence length = words in each out/script.json sentence text; coefficient of variation = population std / mean | CV ≥ 0.35 | Python |
| S14 | DX-S10 | out/adbreaks.json times; act boundaries from out/timeline.json acts; natural silence = span where the master RMS (50 ms/10 ms) stays ≤ −40 dBFS | 2 … 3 breaks; each within ±1.0 s of a boundary between two acts (not inside cold open/ident); each inside a silence ≥ 1.0 s | Python |
| S15 | DX-S1 | out/timeline.json acts[] (id, start, end) and scenes[].act; acts contiguous and in the brief's order | order cold-open, ident, act1, act2, act3, method, outro; cold open ≤ 15 s; ident ≤ 3 s; outro ≥ 20 s; timeline total ≥ 600 s; every scene inside its act | Python |
| R01 | DX-R1 | out/tension-map.json samples (t, cutRate, audioDensity, musicLevel, tension), peaks[], valleys[]; out/tension-map.png present. Declared curves vs measured: cut rate = cuts per 10 s window (out/transitions.json); music level = music-stem RMS dB (1 s); audio density = number of stems (voice, music, sfx, whoosh) above −45 dBFS per 1 s, 5 s moving mean. Peaks: local maximum of tension within ±10 s (5% of range slack); each act 1–3 has a peak within ±5 s of its climax (timeline acts[].climax); every peak is followed within 45 s by a declared valley that is ≥ 25% of the range lower | Pearson r ≥ 0.8 (cut rate), ≥ 0.7 (music level), ≥ 0.6 (audio density); 0 false peaks; 3 acts with a climax peak; 0 peaks without valley | Python |
| R02 | DX-R2 | change points = scene starts where the layout family (text before "/" in scenes[].layout) or the shot size (scenes[].shot / shot.size) changes, plus starts of audio-layer cues (out/cues.json cues[].t); gap between consecutive change points (0 and the end included) | longest gap ≤ 60 s | Python |
| R03 *(sửa)* | DX-R3 | decisive claims (decisive=true); each narration sentence saying one: own-ASR word run that says the value, extended over the unit words that follow it (dollars, percent, million, real, …; audit K-5). Pause measured on the voice stem (required): the first ≥ 120 ms run below −45 dBFS (20 ms RMS) that starts within [run end − 0.25 s, run end + 0.8 s], until the voice comes back for ≥ 30 ms; no such run = the voice runs on, pause 0 | ≥ 1 decisive claim; every pause ≥ 1.0 s; 0 decisive numbers not found in ASR | Python |
| R04 | DX-R4 | cuts from out/transitions.json; beats from out/tempo-map.json; a cut is on the beat if a beat is within ±1 frame; on action if the cut declares action=true and the picture moves into the cut (mean \|ΔY\| of the last 5 frames before the cut ≥ 1.5 × the outgoing shot's median) | ≥ 70% of cuts on a beat or on action | Python |
| R05 | DX-R5 | shot durations = scenes[].dur of out/timeline.json. Act 2 acceleration: act-2 scenes that start before the act-2 climax, split in three consecutive groups of equal count; group means | every shot 1.2 … 12 s (act "outro" exempt from the 12 s cap: it holds the end screen); CV = std/mean ≥ 0.4; act-2 means non-increasing and last ≤ 0.8 × first (≥ 6 scenes) | Python |
| R06 | DX-V10 (picture check of cuts) | every declared cut in out/transitions.json except dissolves: mean \|ΔY\| (luma, 1/4 scale) between the frame at the cut and the one before, vs the median of the ±10 surrounding frame pairs | ≥ 90% of cuts show a spike ≥ 3 × the surrounding median and ≥ 2 codes | Python |
| V01 *(sửa)* | DX-V12 | preprod/shotlist.json shots[]: fields size, move, moveReason (2.5D shot list: no simulated focal length, no 3D camera angle); coverage of out/timeline.json scenes (shots[].scene); storyboard (preprod/storyboard.*) and colour script (preprod/color-script.*) present | every shot has all 3 fields non-empty; moveReason ≥ 3 words; every timeline scene has ≥ 1 shot; storyboard and colour script present | Python |
| V02 *(sửa)* | DX-V1 | settled frames every 0.1 s: centre of each visible level-1 text vs the four thirds intersections (±96 px x, ±54 px y), or the vertical centre line (±48 px) when the scene declares composition "center" | ≥ 90% of level-1 samples placed | trang + Python |
| V03 *(sửa)* | DX-V3 | every frame (no camera-move exemption), every 0.2 s: ink bounding box of each visible text from the page's text layer (alpha > 64, badges included). A text travelling in or out of frame (its box moved ≥ 4 px since the object sample 0.1 s earlier) may cross the edge | all text ink of non-travelling texts inside x 96–1824, y 54–1026 (90% safe area); 0 violations | trang + Python |
| V04 | DX-V4, DX-X3 | objects with char "1966"/"mirror" every 0.1 s: horizontal order when both are visible (\|Δx\| ≥ 20 px), share of the main colour and main shape of each; year axis labels (role axis-label with year) ordered left → right | one side only for the whole video (≥ 1 sample); each character's main colour ≥ 95% and main shape ≥ 95% of its observations; colours differ; shapes differ; 0 time-order violations | trang + Python |
| V05 *(sửa)* | DX-V8 | camera path out/camera.json, per frame: 2.5D {t, x, y, zoom} (pan over the chart plane in page px, zoom = scale) or the legacy {t, pos, target, fovDeg, focusDist}. Speeds/accelerations normalised to frame widths (fw; 2.5D: pan / (1920/zoom) + \|d ln zoom\|). Moves as in A10, ≥ 0.5 s. Per move: ease = mean speed over the first and last 10% of the move ÷ peak; linear = speed stays within ±10% of its mean over ≥ 60% of the move; progress u from the rest position 0.6 s before to the rest position 0.6 s after; anticipation = u ≤ −0.3% before the peak-speed instant; overshoot = u peaks 0.3–8% past 1 after it and settles within 0.3%; peak \|acceleration\|. Truth check: Spearman ρ between camera speed and picture change (mean \|ΔY\| per 0.5 s window) | ≥ 5 moves; every move eased (≤ 0.4) and none linear; anticipation in ≥ 30% and overshoot in ≥ 30% of moves ≥ 1 s; no overshoot > 8%; peak \|a\| ≤ 8 fw/s²; ρ ≥ 0.3 | Python |
| V08 *(sửa)* | DX-V6 | every frame (no camera-move exemption), every 0.2 s, texts with opacity ≥ 0.95 standing still on screen (box moved < 2 px in 0.1 s; moving texts are judged by V12), on the delivered video frame: text colour = median of glyph-core pixels (glyph mask eroded 1 px), background = median of the ring 1–4 px around the ink (inside the badge for badge text); WCAG contrast | ≥ 4.5:1 for every text sample | trang + Python |
| V09 | DX-V4, DX-X3 | main colour of each character = most frequent fill/stroke of objects with char "1966" / "mirror" seen by the page sampler; simulated with Machado 2009 (severity 1) protanopia and deuteranopia, ΔE2000 between the two simulated colours; grey = WCAG relative-luminance contrast between them | ΔE2000 ≥ 20 under each simulation; grey contrast ≥ 1.5:1 | trang + Python |
| V10 *(sửa)* | DX-V10 | out/transitions.json cuts[] (t, from, to, type, match: geometric\|semantic, audio: j\|l, reason). Match cut, geometric: centroid of the bright salient region (Y > median + 2σ) of the last outgoing and first incoming frame within 10% of the frame; semantic: reason ≥ 5 words. J-cut: first own-ASR word of the incoming scene's first sentence starts ≥ 0.2 s before the cut; L-cut: last ASR word of the outgoing scene's last sentence ends ≥ 0.2 s after it. Dissolve detector on every cut ±15 frames (see dissolve_at) | ≥ 5 verified match cuts; ≥ 4 verified J/L-cuts; every declared dissolve has a reason ≥ 5 words and not "default"; 0 undeclared dissolves detected | Python |
| V11 *(sửa)* | DX-V11 (C rule text-line-collision, upgraded to pixels) | every frame (no camera-move exemption), every 0.2 s: text ink from the page's text layer (glyphs, badges with their pill, axis labels; alpha > 64) dilated by 2 px vs ink of the graphics layer (lines, axes, series, bars, marks, stroked outlines; neutral cards and backgrounds excluded); and text vs text (each text rendered alone). A text standing still collides when it overlaps in one sample; a text moving on screen (box moved ≥ 2 px in 0.1 s), or a pair of texts one of which moves, when the same overlap is there in two consecutive samples (0.2 s) | < 4 overlapping pixels for every text in every sample (moving text: not in two consecutive samples); 0 violations | trang + Python |
| V12 **(mới)** | DX-V9 (replaces the camera-move exemption) | every frame, every 0.2 s, every text with opacity ≥ 0.95 fully on frame: normalised cross-correlation of luma between the delivered video frame's coded Y plane and the clean page render's Y' (BT.709 weights) of the same instant (window.CHECKS.seek), inside the text box + 4 px. A doubled, smeared or motion-blurred label correlates poorly with its single sharp render (a ghost copy at 30% opacity: ≈ 0.96; at 50%: ≈ 0.91); grain, grade and vignette barely move it (affine inside a box). Texts with no ink contrast in the render (RMS < 8 codes) are skipped and counted | NCC ≥ 0.97 for every text sample; 0 violations | trang + Python |
| V13 **(mới)** | DX-V9, DX-V8 (replaces the camera-move exemption) | frames "in a move" = camera speed ≥ 0.10 fw/s from out/camera.json (same speed as V05; gaps < 0.2 s merged), or the declared scenes[].move when there is no camera file. The layout rules (C01, C03, C04, C07, V02, C12) judge a move by its settled ends; this rule bounds the frames they do not judge. The text rules have no exemption: V12 (text integrity) on every frame, V03/V08/V11/C14 with their moving-text criteria in the page sampler | every move ≤ 3.0 s; frames in a move ≤ 15% of the video | Python |
| C01 *(sửa)* | DX-V11 (C rule scene-leak) | every 0.1 s outside the camera move at scene start: shapes of a panel not listed in scenes[].panels, not background, opacity > 0.05, ≥ 16 px² on frame | 0 flagged frames | trang + Python |
| C02 | DX-V11 (C rule bg-over-data) | every 0.1 s: a background object (role bg) painted after (above) the first data shape and overlapping a data shape | 0 flagged frames | trang + Python |
| C03 *(sửa)* | DX-V11 (C rule unlabelled-curve) | settled frames, every 0.1 s: a visible curve (≥ 80 px diagonal, opacity > 0.1) without its bound label within 240 px, or any text within 60 px if unbound | 0 flagged frames | trang + Python |
| C04 *(sửa)* | DX-V11 (C rule axis-anchors) | settled frames, every 0.1 s: a line series (role series, or an open stroke: unfilled path/polyline of ≥ 10 vertices stroked in a series colour; ≥ 120 px) without an axis of its chart and ≥ 2 numeric anchors. Filled shapes (pie wedges, closed polygons, marks) are not line series | 0 flagged frames | trang + Python |
| C05 | DX-V11, DX-X4 (C rule grey-emphasis) | every 0.1 s: a level-1/emphasis text below 7:1 against the bg token in grey, or a 48 px+ non-emphasis text brighter in grey than it | 0 flagged frames | trang + Python |
| C06 | DX-V11 (C rule number-colour) | every 0.1 s: a number in a series colour whose colour differs from its series (data-series map) or from the nearest mark within 150 px | 0 flagged frames | trang + Python |
| C07 *(sửa)* | DX-V11 (C rule bar-proportion) | settled frames: a bar cropped along its value axis without an axis break, or bars of one chart (data-value, full) with scales differing > 3% | 0 flagged frames | trang + Python |
| C10 | DX-V1 (C rule level1) | chart scenes of ≥ 2 s: share of samples (0.1 s) with exactly one visible level-1 text; max simultaneous | ≥ 50% of samples with exactly one, never two | trang + Python |
| C11 | DX-V11 (C rule layout-repeat) | scenes[].layout of out/timeline.json; for each scene start, scenes with the same layout starting within the next 90 s | no layout used more than 2 times in any 90 s window | Python |
| C12 *(sửa)* | DX-V11 (C rule split-view) | camera frozen at t, page at t + 0.1 s; union box of changed objects (a growing object counts only its new strip); outside camera moves | no run ≥ 1.0 s where the changes span > 60% of frame width or height | trang + Python |
| C13 *(sửa)* | DX-V11 (number–voice sync ±250 ms) | for each narration sentence saying a number that is shown in the same scene: onset = start of the own-ASR word run saying the value; screen = first frame (frame-accurate) the claim span shows its final display text in that scene (page sampler claimFinal); when several claims of the scene carry the value, the one closest to the onset | \|screen − onset\| ≤ 250 ms for every pair; 0 spoken numbers missing from ASR | trang + Python |
| C14 *(sửa)* | DX-V11, DX-X4 (legible at 25%) | every frame (no camera-move exemption), every 0.2 s, texts with opacity ≥ 0.95 standing still on screen (moving texts: V12): smallest font run in px; on the delivered video frame downscaled 4× (box average), WCAG contrast between the 95th and 5th luminance percentile inside the text box | every text ≥ 28 px (cap height ≥ 5 px at 25%) and ≥ 3:1 at 25%; 0 violations | trang + Python |
| C15 | DX-V5 (C rule tokens only) | every 0.1 s: a colour on a visible object (text runs, text background, shape fill/stroke; gradients excepted) that is not in design/tokens.json colors | 0 flagged frames | trang + Python |
| P01 | DX-P2 | out/package/thumb-1..3.png with sidecars thumb-N.json texts[] (text, box [x,y,w,h], fontPx); design/tokens.json colours. Token share = pixels within 12 (RGB) of a token or of a blend of two tokens. Readability at 10%: area-downscale to 128×72; in each text box, WCAG contrast between the 95th and 5th luminance percentile | 3 thumbnails, each 1280×720; token share ≥ 97%; every text fontPx ≥ 90 (≥ 9 px at 10%) and contrast at 10% ≥ 3:1 | Python |
| T1 **(mới)** | DX-A1 (sổ gu G-001) | events = union of the declared out/sonify-events.json (bar f0, dot f, start of each line draw) and the chart events the page sampler measured with the camera frozen (a bar, series, mark or character shape appears or changes); events closer than 0.15 s form one cluster, measured at its onset and every 0.5 s to its end. Band 1.5–8 kHz (4th-order Butterworth), window [t, t + 0.15 s]: lift = 10·log10((P_son + P_rest) / P_rest), P_son = band power of the data-sound stem ("sonify", or "sfx" when the data sounds are mixed into it), P_rest = band power of the sum of the other stems (voice, music, whoosh, room [, sfx]). Inside a spoken-number window [onset − 0.5 s, end + 1.6 s] (own ASR), where DX-A6 lowers effects, the lift needed is 1 dB. Truth check: the stems add up to the master in the band (correlation of the band signals). Without a sonify stem the sfx stem is measured (reported) but the rule cannot pass: other effects would count as data sounds | every measured window: lift ≥ 3 dB (≥ 1 dB in a spoken-number window) and data-sound band level ≥ −60 dBFS; stems ~ master r ≥ 0.90; ≥ 1 cluster; sonify stem delivered | trang + Python |
| T2 **(mới)** | DX-A2 (sổ gu G-002) | music stem; bars of 4 beats from out/tempo-map.json beats (A12 checks those beats against the music's onsets); 4-bar phrases of chroma + onset pattern (phrase_features). For each phrase: the highest cosine similarity with the 1, 2, 3 and 4 phrases before it (a loop of 1–4 phrases repeats at one of these lags). A repeat = similarity ≥ 0.90. Quiet phrases (< −50 dBFS) are left out | ≥ 8 phrases measured; repeats ≤ 5% of phrases; never 2 repeated phrases in a row | Python |
| T3 **(mới)** | DX-R6 (sổ gu G-003) | intentional silences = master spans ≤ −40 dBFS (50 ms RMS, 10 ms hop) of 0.8–1.5 s (as A09). Bed = music + sfx + whoosh (+ sonify) stems summed, 20 ms RMS, 5 ms hop. Reference = 90th percentile of the bed in [start − 0.8, start − 0.1]. Entry = from the last instant the bed is within 3 dB of the reference (searched in [start − 1.0, start + 0.3]) to the first instant after it the bed is 30 dB below the reference (or below −70 dBFS). Reported, not judged: a bed already below −60 dBFS before the silence (nothing to release), and a bed whose median inside the silence stays within 20 dB of the reference (a quiet passage, no cut to judge; A09 still counts it). Floor: master 50 ms RMS minimum inside the silence (edges 0.1 s excluded) and the room stem mean level there | every entry 150–400 ms; master ≥ −80 dBFS and room stem ≥ −75 dBFS through every silence; ≥ 1 silence | Python |
| REG **(mới)** | CH §5, §4 khâu 3 (cổng hồi quy) | baseline = the checker's report of the previous version of the episode (--baseline). A rule is comparable when it is in both reports and its definition is unchanged: same fingerprint (sha256 of measure + threshold), or, for a baseline without fingerprints, the same threshold text and not in CHANGED_SINCE[baseline lock]. Regression = comparable rule PASS in the baseline and not PASS now (FAIL, MISSING or ERROR) | 0 regressions (a --first run has nothing to compare and passes; no baseline and no --first = MISSING) | Python |

## Khoá

`checks/LOCK` là SHA-256 của danh sách `sha256  đường-dẫn` của mọi file trong `checks/`, trừ `LOCK` và `__pycache__`. Danh sách sắp xếp theo `LC_ALL=C`, mỗi dòng kết thúc bằng `\n`.

```
cd checks && find . -type f ! -name LOCK ! -path '*/__pycache__/*' | LC_ALL=C sort | xargs sha256sum | sha256sum
```
