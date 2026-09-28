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
| A14 | `stem()` chuẩn hoá hai phía cùng một cách: bỏ sở hữu cách, rồi một biến tố, rồi `e` cuối. Nhờ vậy `retiree`, `retirees`, `retiree's` gặp nhau. `asr_join` nối token bắt đầu hoặc kết thúc bằng `&`, nên "S" "&P" thành "S&P". `words()` giữ "S&P" là một từ. ASR cắt theo câu. | audit §4.1, §4.2; REPORT-D (Whisper rơi từ khi chạy cả file) |
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

<!-- RULE TABLE -->

## Khoá

`checks/LOCK` là SHA-256 của danh sách `sha256  đường-dẫn` của mọi file trong `checks/`, trừ `LOCK` và `__pycache__`. Danh sách sắp xếp theo `LC_ALL=C`, mỗi dòng kết thúc bằng `\n`.

```
cd checks && find . -type f ! -name LOCK ! -path '*/__pycache__/*' | LC_ALL=C sort | xargs sha256sum | sha256sum
```
