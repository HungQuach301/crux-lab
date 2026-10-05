# checks/ — máy kiểm của crux-lab (Phiên K1, K2, K3, K3.1, K3.2, K3.3, K3.4, K3.5, K3.6, K3.7; khoá SHA)

Bộ luật này chấm mọi yêu cầu `[MÁY]` của [`genre-spec/data-explainer.md`](../genre-spec/data-explainer.md). Các yêu cầu `[NGƯỜI]` nằm trong [`RUBRIC.md`](RUBRIC.md) (H1–H8). Danh sách artefact bên dựng phải giao nằm trong [`CONTRACT.md`](CONTRACT.md).

Khoá: `checks/LOCK` là SHA-256 của toàn thư mục (cách tính ở cuối file).
- Bên dựng không sửa thư mục này (CHARTER §7.1, §8).
- Cho rằng một luật sai thì ghi khiếu nại. Luật chỉ đổi qua vai kiểm, và cần chủ dự án duyệt.

Gốc: `checks/` của bài D (`crux-spike-opus55`, nhánh `spike/opus55-cine`, LOCK `0478df73…`), đã sửa theo audit `audit/d-final` (`audit/REPORT.md` @ `afad899`). Các thay đổi ghi ở mục "Thay đổi so với bài D". Thay đổi của K2 (luật đọc từ hợp đồng tập; T1 định nghĩa lại; L1, S16, F11 mới) ghi ở mục "Thay đổi ở khoá K2". Thay đổi của K3 (mỗi luật một cấp CHẶN / CHÍNH / THAM KHẢO; F12, A16–A18 mới; S02, REG, F07 sửa) ghi ở mục "Thay đổi ở khoá K3"; cấp của từng luật ở mục "Cấp của luật". K3.1 (F12 phủ cả tài sản hình) ghi ở mục "Thay đổi ở khoá K3.1". K3.2 (S09: lời đọc nói mỗi gốc tính tiền ít nhất một lần cả tập) ghi ở mục "Thay đổi ở khoá K3.2". K3.3 (S09: nhãn gốc cấp khung cho khung một gốc) ghi ở mục "Thay đổi ở khoá K3.3". K3.4 (S10: bộ dò ADVICE không bắt nhầm từ chỉ thị đứng riêng) ghi ở mục "Thay đổi ở khoá K3.4". K3.5 (loại mô hình mới `float-vs-fixed-replay` cho Tập 2) ghi ở mục "Thay đổi ở khoá K3.5". K3.6 (khoá S05 mới cho `float-vs-fixed-replay`; S05 so claim tháng sau chuẩn hoá) ghi ở mục "Thay đổi ở khoá K3.6". K3.7 (loại mô hình mới `lock-vs-roll-replay` cho Tập 3, dùng lại cho retire-3) ghi ở mục "Thay đổi ở khoá K3.7".

## Chạy

```
pip install numpy scipy soundfile av faster-whisper      # ffmpeg, ffprobe trên PATH; Node ≥ 18 và playwright (Chromium)
checks/run.sh [root] [--contract <contract.json>] [--baseline <báo cáo kiểm của phiên bản trước>.json | --first]   # gốc tập: episodes/<tập>
checks/selftest/run.sh [thư-mục-kết-quả]                 # test tự chứng minh
```

`run.sh` chạy hai bước:
1. `node checks/page/sampler.js <root>`: bộ lấy mẫu trang dựng.
2. `python3 checks/py/run.py <root>`: mọi luật.

Kết quả ghi vào `<root>/out/checks/report.json` và `report.md`. Báo cáo ghi LOCK, SHA-256 của master được chấm và đường dẫn hợp đồng tập đã đọc.

**Hợp đồng tập.** Mặc định là `<root>/contract.json` (gốc tập `episodes/<tập>/`); `--contract` chỉ file khác. Luật đọc từ đó nhân vật, màu và hình dạng nhận diện, mô hình và claims, nguồn và đối chiếu dữ liệu, các trường hợp phải hiện đủ, dải tần tiếng dữ liệu, artefact phải giao (schema: `CONTRACT.md`, mục "Hợp đồng tập"). Thiếu trường thì luật báo MISSING và nêu tên trường.

Trạng thái của một luật:
- **PASS**: đạt.
- **FAIL**: trượt.
- **MISSING**: thiếu artefact, tính là không đạt.
- **ERROR**: luật lỗi, tính là không đạt.

**Cấp của luật (K3).** Mỗi luật có một cấp (`py/tiers.py`; bảng ở mục "Cấp của luật"):
- **CHẶN** (lớp L1 của Cine Lab): số liệu, claim, nguồn, điều khoản, quyền tài sản, kỹ thuật file, âm lượng, true peak, ASR không mất từ khoá. **Chỉ luật CHẶN làm trượt tập**: một luật CHẶN không PASS (FAIL, MISSING hay ERROR) thì tập **TRƯỢT**.
- **CHÍNH**: độ rõ lời (L1 "không lấn lời"), va chạm chữ, tương phản, đọc được (ở 25%, vùng an toàn, chữ không nhân đôi); theo quyết định của chủ dự án khi duyệt K3: độ dài (F07) và đổi model giọng giữa tập (A18). Luật CHÍNH không đạt thì bên dựng phải giải thích trong `out/explanations.json` (≥ 8 chữ mỗi luật); chưa giải thích thì tập ở trạng thái **CHỜ GIẢI THÍCH**. Chủ dự án đọc lời giải thích ở gói duyệt.
- **THAM KHẢO**: mọi chỉ tiêu tay nghề hay số lượng. Chỉ báo số đo; không làm trượt, không cần giải thích (nguyên tắc chống Goodhart của Cine Lab: số lần dùng kỹ thuật chỉ là cảnh báo).

Báo cáo ghi `episode` = TRƯỢT / CHỜ GIẢI THÍCH / ĐẠT và bảng đạt/không đạt theo cấp. Trạng thái PASS/FAIL của từng luật vẫn giữ (để hiệu chỉnh và để REG so).

`near` liệt kê **mọi chỉ số nằm trong ±5% quanh ngưỡng**, đạt hay không, kèm tên luật, tên chỉ số và cấp; `report.md` có mục riêng "Chỉ số trong ±5% quanh ngưỡng". Ngưỡng 0 (đếm lỗi) không có dải ±5%; ngưỡng `==` không có dải.

**REG (cổng hồi quy)** cần báo cáo kiểm của phiên bản trước (`--baseline`). Báo cáo này do phiên kiểm giữ, không lấy từ cây của bên dựng. Phiên bản đầu tiên chạy với `--first`. Không có cả hai thì REG là MISSING.

## Nguyên tắc đo

- Đo trên file đã giao: khung giải mã từ `out/video.mp4`, âm thanh giải mã, stem, ASR tự chạy.
- Không tin số khai báo khi đo được. File khai báo chỉ nói *đo ở đâu*, và luôn được đối chiếu với hình hoặc tiếng.
- **Claim** (K3.6): `out/claims.json` ghi `value` chưa làm tròn; dung sai S05 là 0,005 (lãi, tỉ lệ %, khoản trả), $0,50 (tiền), tháng chính xác sau chuẩn hoá (`YYYY-MM` ≡ `YYYY-MM-01`). Số làm tròn để hiện nằm ở `display`.
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
- ~~Các luật gắn với mô hình và nhân vật của bài D~~: K2 đã chuyển sang hợp đồng tập (mục "Thay đổi ở khoá K2").

## Thay đổi ở khoá K2 (2026-09-28, chờ chủ dự án duyệt)

| Mã | Thay đổi | Lý do |
|---|---|---|
| S01 | Tính lại mô hình theo `model.kind` của hợp đồng tập. Hai loại có bản tính lại độc lập (`py/r_model.py`): `retirement-6040` (bài D, giữ nguyên phép tính K1) và `refinance-breakeven` (Tập 1, mô hình M1b: hoà vốn tính cả dư nợ, ba nhân vật, **mô phỏng lịch sử** 13 đợt giảm lãi do phiên kiểm tự viết từ câu mô tả trong hợp đồng). Phần nào của file mô hình không được tính lại thì bị liệt kê, và luật trượt. Trên `out/model.json` của Tập 1 (`ep001` @ `bbc28fb`): 619 giá trị, 0 lệch, không còn phần nào chưa tính lại. | chỉ dẫn K2 §1, §3 (vòng 2); `episodes/ep001/checks-notes.md` §2 |
| S03 | Tên miền nguồn chính và nguồn đối chiếu đọc từ `data.hosts`, file nguồn từ `data.sources`. | như trên |
| S04 | Các cặp chuỗi đối chiếu (file, cột, khoá, hệ số, dung sai, khoảng dùng) đọc từ `data.crosscheck[]`. | như trên |
| S05 | Claim nào là đại lượng mô hình đọc từ `model.claims`; bất biến của luận điểm (bài D: hai đường cùng trung bình nhân) từ `model.params`; claim phải gắn ILLUSTRATIVE đọc từ `claims.illustrative` và từ nhân vật `illustrative:true`. | như trên |
| S06 | Trường hợp phải hiện đủ đọc từ `coverage[]` (`year` hoặc `case`, hồi, danh sách hay khoảng). Bộ lấy mẫu ghi thêm `casesTrack` (thuộc tính `case` của đối tượng trang). | như trên |
| V04 | Nhân vật, màu (token hoặc hex), hình dạng và bên đọc từ `characters`. Màu và hình chính trên màn hình phải **đúng cái hợp đồng khai**, không chỉ "khác nhau". Mọi cặp nhân vật giữ một bên suốt phim, đúng bên khai báo. Bộ lấy mẫu ghi mọi cặp `char`, không còn gắn `1966`/`mirror`. | như trên |
| V09 | Mô phỏng mù màu cho **mọi cặp** nhân vật của hợp đồng. | như trên |
| T1 | **Định nghĩa lại**: nghe thấy ở khe nghỉ của lời (giữa âm tiết, giữa từ, giữa câu) và ở chỗ không có lời; dải tần lấy từ `sonification.bandsHz` của tập (theo cue sheet); không đòi nổi lên trong lúc lời đang đọc. Mỗi mẫu của một lần vẽ đường là một sự kiện, nên lần vẽ được đo mỗi 0,5 s. Kiểm thật thêm: dải khai báo phải chứa ≥ 50% năng lượng của stem `sonify`. | sổ gu G-006; `episodes/ep001/checks-notes.md` §1 |
| L1 | **Mới**: tiếng dữ liệu không lấn lời (năng lượng lời so với tiếng dữ liệu ở 1–4 kHz khi có lời; ASR không mất từ khoá vì tiếng dữ liệu). | sổ gu G-006 |
| S16 | **Mới, tạm**: câu nói con số quyết định phải gắn với một nhân vật hoặc kịch bản của hợp đồng tập. Tên có thể nằm ở bất kỳ câu nào trước đó **trong cùng cảnh** (không bắt lặp tên ở mỗi câu). | sổ gu G-008; G-009 |
| S13 | **Định nghĩa lại** (G-009). Luật cũ (CV độ dài mọi câu ≥ 0,35) **thưởng câu vụn**: chèn câu 1–3 chữ làm CV tăng (chuỗi "Maya borrowed in 2023. Rates peaked. She paid 35 times. Rates fell. The bill: $5,124." có CV 1,14, đạt dễ). Nay: CV chỉ tính trên câu ≥ 4 chữ (xen kẽ dài ngắn thật), và **cấm chuỗi ≥ 3 câu liền nhau ≤ 6 chữ**. Một câu ngắn để nhấn vẫn được. Câu dẫn chuyện không có số không bao giờ bị phạt. | sổ gu G-009 |
| F11 | **Mới**: artefact mốc phát hành (`artefacts.M3`) đã khai đều được giao, và danh sách khai gồm mọi file phát hành của `CONTRACT.md`. | chỉ dẫn K2 §1 (artefact phải giao); CHARTER §7.3 |

Hợp đồng của bài D do phiên kiểm ghi lại từ các hằng số K1 đã gắn cứng: `checks-runs/D-r3-6531f6c8/contract.json` (nằm ngoài `checks/`).

**Rà luật về lời theo G-009** ("kịch bản phải là một câu chuyện … liền mạch, có chuyển ý, không cụt lủn"):

| Luật | Ép câu vụn / cấm câu dẫn chuyện không số? | Quyết định |
|---|---|---|
| S13 (DX-S8) | **Có**: CV trên mọi câu, câu vụn làm CV tăng | **Sửa** (trên) |
| S16 | Bắt câu có số quyết định (hoặc câu ngay trước) gọi tên nhân vật: ép lặp tên, cắt ngang mạch kể | **Sửa**: xét cả cảnh tới câu đó |
| S12 (DX-S7, ≤ 1 số mới / 8 s, ≤ 2 số mới / cảnh) | Không: chỉ giới hạn số, không đòi số; càng nhiều câu dẫn chuyện không số càng dễ đạt | Giữ |
| A15 (150–160 wpm mỗi hồi, không câu > 175 wpm) | Không: câu vụn đọc TTS thường vượt 175 wpm, nên luật này còn chống câu vụn | Giữ |
| R03 (≥ 1,0 s thở sau số quyết định) | Đẩy số quyết định về cuối câu, không ép tách câu; một khoảng thở ở ranh giới mệnh đề cũng đạt | Giữ |
| S09 (câu có số $ hoặc câu ngay trước nói thực/danh nghĩa) | Có thể ép lặp "nominal" trong mạch kể; nhưng đây là luật nội dung (DX-H3), nới cần chủ dự án quyết | Giữ, **ghi để chủ dự án cân nhắc** (K3.2: chủ dự án quyết, lời đọc nay chỉ cần nói mỗi gốc một lần cả tập) |
| S10, S11, S07, A14, C13, F09 | Không liên quan độ dài câu hay câu không số | Giữ |

Trên kịch bản M1b của Tập 1 (`out/script-draft.json` @ `bbc28fb`): S13 mới **trượt** (cold open "Maya locked in 7.62%. / This week's average: 7.03%. / Refinancing costs $5,124. / So when does that money come back?" là một chuỗi câu vụn), luật cũ cho đạt (CV 0,40). Bài D r3: S13 mới trượt ("Same money in. / Same money out. / Same average.").

Còn gắn với bài D, ngoài phạm vi K2 (ghi để khoá sau xử lý): A14 (danh sách thuật ngữ khoá `DEFINED_TERMS` là từ vựng hưu trí; tập mới chỉ **thêm** được qua `out/terms.json`), S02 (cụm "no taxes" / "no fees" là giả định của mô hình bài D).

## Thay đổi ở khoá K3 (chủ dự án duyệt 2026-09-29, kèm hai sửa: F07 hạ CHÍNH với ngưỡng 480–900 s; A18 nâng CHÍNH)

Nguồn: chỉ dẫn K3 của chủ dự án; Cine Lab `docs/cine-lab/CINE-LAB-KHUNG-CHAT-LUONG.md` §1 (mô hình 3 lớp, "Nguyên tắc chống Goodhart") và `docs/cine-lab/CINE-LAB-BAI-HOC-BRIEF-D.md` (W1–W9, N1–N7) @ `HungQuach301/cine-lab` main.

| Mã | Thay đổi | Lý do |
|---|---|---|
| mọi luật | Mỗi luật một cấp CHẶN / CHÍNH / THAM KHẢO (`py/tiers.py`, bảng "Cấp của luật"). Báo cáo có phán quyết tập: chỉ CHẶN làm trượt; CHÍNH không đạt cần giải thích (`out/explanations.json`); THAM KHẢO chỉ báo số đo. Đo và ngưỡng của các luật cũ **không đổi**, trừ S02, REG, F07 (fingerprint giữ nguyên, REG so được với báo cáo K2) | W2, W3, N2, N3; chỉ dẫn K3 §1–2 |
| REG | Chỉ hồi quy của luật CHẶN làm trượt; hồi quy khác liệt kê kèm cấp | chỉ dẫn K3 §2: chỉ CHẶN làm trượt tập |
| S02 | Giả định phải hiện đọc từ `claims.assumptions` của hợp đồng tập (trước: gắn cứng "no taxes"/"no fees" của bài D). Hợp đồng bài D ghi lại hai regex K1 | S02 nay là CHẶN (claim); K2 đã ghi nó còn gắn bài D, nên không được chặn Tập 1 bằng giả định của bài khác |
| F12 | **Mới, CHẶN**: sổ quyền `out/rights.json`: mọi stem có tiếng có mục; tài sản bên thứ ba có trích điều khoản, URL và `commercial:true`; tài sản tự làm có đường dẫn mã sinh | "quyền tài sản" thuộc CHẶN nhưng chưa có luật nào canh (CHARTER §7.3: không có điểm mù không được canh); DX-A3 (sổ giấy phép); Cine Lab R1 |
| A16 | **Mới, THAM KHẢO**: dấu ngắt giả trong văn bản gửi TTS (`spoken` so với `text`) | chỉ dẫn K3 §3 |
| A17 | **Mới, THAM KHẢO**: mật độ khoảng lặng trong câu và giữa câu bất thường (đo trên stem giọng) | chỉ dẫn K3 §3 |
| A18 | **Mới, CHÍNH** (chủ dự án nâng khi duyệt): đổi giọng hay model giọng giữa tập; xảy ra thì bên dựng phải giải thích | chỉ dẫn K3 §3; duyệt K3: lỗi gốc của Tập 1 v1, trái G-010 |
| F07 | **Sửa, CHÍNH** (chủ dự án hạ khi duyệt): độ dài 480–900 s (trước: ≥ 600 s) | duyệt K3: ngưỡng cũ lệch CHARTER §1 (8–15 phút); chặn độ dài dễ dẫn tới giãn thời gian |
| báo cáo | Mục "Chỉ số trong ±5% quanh ngưỡng" nêu tên luật, chỉ số, cấp; `--list` in cấp và lý do | chỉ dẫn K3 §4 |

**Hiệu chỉnh cảnh báo mới trên Tập 1** (nhánh `ep001`, `out/voice/` @ `bbc28fb`; số đo và kịch bản ở `checks-runs/K3-calibration/`):
- A16: 73/83 câu `spoken` có dấu ngắt giả (114 dấu "…", 1 dấu câu thừa, 0 thẻ pause); câu viết không có các chỗ ngắt đó.
- A18: `takes.json` khai 78 take `eleven_v3` và 5 take `eleven_multilingual_v2` cùng giọng Eric: **đổi model giữa tập**. Phổ dài hạn **từng take** không tách được hai model (5 take v2 nằm trong phân bố v3: v3 trung vị 2,01 dB, p95 3,30 dB; v2 1,89–4,24 dB), nên luật không đặt ngưỡng trên từng take. **Theo nhóm** thì tách được: 5 take v2 cách trung bình v3 2,44 dB; 5 take v3 ngẫu nhiên: p99 1,69 dB. A18 đọc giọng khai báo và ghi số đo nhóm để đối chiếu. Điểm mù còn lại: bên dựng khai một model mà thực tế dùng hai thì máy không thấy (ghi để khoá sau).
- A17: Tập 1 chưa có stem giọng đủ tập; mẫu m0 (1 câu) đạt. Ngưỡng tạm, hiệu chỉnh khi có stem Tập 1.

## Thay đổi ở khoá K3.1 (chờ chủ dự án duyệt)

Nguồn: chỉ dẫn K3.1 của chủ dự án (F12 chỉ canh stem âm thanh; tài sản hình bên thứ ba chưa có luật nào canh). Cấp giữ **CHẶN**.

| Mã | Thay đổi | Lý do |
|---|---|---|
| F12 | **Sửa, CHẶN**: ngoài stem có tiếng, sổ quyền `out/rights.json` phải phủ **mọi tài sản hình** của bản dựng. Danh sách tài sản hình = `rights.visual[]` của hợp đồng tập ∪ `out/visual-assets.json` (manifest bên dựng khai) `{assets:[{name, kind}]}`, `kind` ∈ `image`, `document`, `font`, `model3d`, `texture`, `quote-card`. **Không khai ở đâu cả = MISSING** (máy không tự đoán hình của bản dựng; danh sách rỗng khai rõ thì được). Mỗi tài sản hình phải có một mục sổ quyền liệt kê tên nó trong `visuals`. Luật cho từng mục: (a) bên thứ ba (ảnh, phông chữ, mô hình và texture 3D, …): trích điều khoản ≥ 20 ký tự, URL điều khoản, `commercial:true`; (b) **public domain** (`publicDomain:true`, ví dụ tài liệu liên bang Mỹ): `source.url` và `pdBasis` (căn cứ public domain, ≥ 20 ký tự, ví dụ "17 U.S.C. §105 …"), không cần điều khoản; (c) tự làm: `generator` là đường dẫn tồn tại (dưới gốc hoặc thư mục cha); (d) **thẻ trích dẫn dựng lại** (`quote-card`), ai vẽ cũng vậy: `quoteSource.who` và `quoteSource.url` (nguồn gốc câu trích). Kind lạ thì trượt | "quyền tài sản" là CHẶN (K3), nhưng F12 K3 chỉ nhìn stem: một ảnh, phông hay tài liệu bên thứ ba lọt vào hình không bị máy thấy (CHARTER §7.3: không có điểm mù không được canh); `RIGHTS.md` (mọi tài sản có một dòng, kể cả font, hình) |

- **Dò tài nguyên trang thực sự nạp** (bổ sung khi duyệt K3.1, đóng điểm mù "máy chỉ kiểm lời khai"). Bộ lấy mẫu (`page/sampler.js`) ghi vào `out/checks/page.json` → `resources`: mọi request Playwright hoàn tất (`url`, loại, mã HTTP, content-type), mục Resource Timing (`performance.getEntriesByType('resource')`, bộ đệm nâng lên 100 000), và mọi mặt phông của `document.fonts` (`family`, `status`) sau khi dựng hết phim. F12 so với danh sách hình đã khai:
  - **Tài nguyên hình** = file có đuôi ảnh (`png jpg jpeg gif webp avif svg bmp ico tif tiff apng jxl`), tài liệu (`pdf`), mô hình 3D (`glb gltf obj fbx stl ply usdz dae 3ds`), texture (`ktx ktx2 basis dds hdr exr tga`); không có đuôi thì theo content-type (`image/*`, `model/*`, `application/pdf`) hoặc loại request `image`. Mỗi file phải khớp một tài sản hình đã khai: `path` / `paths` (đường dẫn tương đối từ gốc tập, hoặc glob; URL http so theo đường dẫn), không có thì tên file = `name`.
  - **Phông** chấm theo **họ phông** (`document.fonts`, `status: loaded`), không theo file: họ phải trùng `family` (hoặc `name`) của một tài sản `kind: font` đã khai (không phân biệt hoa thường). Nhờ vậy phông nạp từ `data:` URL hay từ bộ đệm cũng bị bắt. File phông (`woff woff2 ttf otf eot`, loại `font`) không chấm riêng theo URL.
  - Tài nguyên nạp mà không khai → **trượt (CHẶN)**. Trang không có `resources` (bộ lấy mẫu cũ) hoặc không có `out/checks/page.json` → MISSING.
- **Quy tắc loại trừ** (không tính là tài sản hình):
  1. *Nội bộ trình duyệt*: URL `data:`, `blob:`, `about:`, `chrome:`, `chrome-extension:`, `chrome-error:`, `chrome-search:`, `devtools:`, `javascript:`; request thất bại hoặc HTTP ≥ 400 (không nạp được thì không lên hình); request tự động `/favicon.ico` của trình duyệt (loại `other`); phông hệ thống (không nằm trong `document.fonts`, vì `document.fonts` chỉ có mặt phông `@font-face` / `FontFace`). Lưu ý: ảnh `data:` bị loại theo URL; phông `data:` vẫn bị bắt theo họ phông.
  2. *Không phải hình*: tài liệu trang, script, stylesheet, JSON/CSV, wasm, âm thanh (âm thanh do phần stem của F12 canh).
  3. *File sinh bởi chính mã dự án*: khớp một quy tắc `{glob, generator}` trong `generated` của manifest (`out/visual-assets.json`) hoặc `rights.generated` của hợp đồng tập, **và** `generator` là đường dẫn tồn tại (dưới gốc hoặc thư mục cha). Quy tắc có generator không tồn tại thì F12 trượt và file đó bị tính là chưa khai.
- Điểm mù còn lại (ghi để khoá sau): hình vẽ trực tiếp bằng mã trên trang (SVG nội tuyến, canvas) không có request nên không bị dò (đó là hình tự làm, trừ khi mã chép lại hình bên thứ ba); ảnh nhúng `data:`; phông hệ thống dùng qua `font-family` không có `@font-face`; video nạp trên trang (không thuộc các loại hình của chỉ dẫn); hình ghép vào video sau khi dựng trang (hậu kỳ) không đi qua trang.
- Fingerprint của F12 đổi. F12 mới từ K3 nên REG chưa có báo cáo nào để so; các luật khác giữ fingerprint của khoá K3.
- **Ảnh hưởng tới Tập 1** (`ep001`): hợp đồng tập chưa có `rights.visual`, chưa có `out/visual-assets.json`, chưa có `out/rights.json`. F12 vẫn **MISSING** (trước K3.1 cũng MISSING vì thiếu `out/rights.json`), nay nêu thêm tên danh sách tài sản hình và cần chạy lại bộ lấy mẫu K3.1 (`resources`). Để đạt: khai danh sách hình, ít nhất phông Inter với `family: "Inter"` (`RIGHTS.md` F-INTER; trang dựng nạp Inter qua `@font-face` nên bộ lấy mẫu sẽ thấy họ này) và ghi mục cho Inter có **trích nguyên văn** OFL 1.1 + URL (`RIGHTS.md` ghi "chưa trích nguyên văn": hiện sẽ trượt); ảnh hay texture do mã dự án sinh mà trang nạp thì khai quy tắc `generated`; cùng các mục đã có cho giọng Eric (chờ trích điều khoản) và nhạc tự sinh.

## Thay đổi ở khoá K3.2 (quyết định của chủ dự án 2026-09-30)

Nguồn: quyết định của chủ dự án về S09 (mục K2 "Rà luật về lời theo G-009" đã ghi S09 để chủ dự án cân nhắc). Cấp giữ **CHẶN**.

| Mã | Thay đổi | Lý do |
|---|---|---|
| S09 | **Sửa phần lời đọc, CHẶN**: mỗi **gốc tính tiền được dùng trong tập** (gốc `basis` của mọi claim $ trong `out/claims.json`: `nominal` và/hoặc `real`) phải được nói **ít nhất một lần trong lời đọc cả tập** (`out/script.json`, ở câu nào cũng được). Từ nhận gốc là regex `BASIS`, không đổi (`nominal`, `before inflation`, `dollars of the day`, `then-year` / `real`, `inflation-adjusted`, `today's dollars`, `<năm> dollars`, `after inflation`). Tập dùng cả hai gốc thì phải nói cả hai. Số $ đọc lên mà không khớp claim nào thì không biết gốc, tính là thiếu. Không còn yêu cầu theo câu hay theo hồi, không đọc trường `act`. **Phần trên hình giữ nguyên CHẶN**: mọi khung có claim $ phải có nhãn gốc trong cùng khối chữ hoặc trong 300 px. Phần claim giữ nguyên: mọi claim $ khai `basis` | Luật cấp câu (câu có số $ hoặc câu ngay trước, cùng cảnh, phải nói gốc) ép lặp "nominal" 26 lần trong Tập 1, trái G-010 (lời đọc tự nhiên, không lặp máy móc). Bản nháp K3.2 đầu (mỗi hồi một lần, trước số $ đầu tiên) vẫn buộc sửa 6 hồi, kéo theo sinh lại giọng và render lại. Mục đích DX-H3 (người xem không nhầm thực với danh nghĩa) do **nhãn trên hình** mang ở từng khung có số $; lời đọc chỉ cần giới thiệu gốc một lần |

- Fingerprint của S09 đổi, nên REG không so S09 với báo cáo cũ (định nghĩa khác). Các luật khác giữ fingerprint của khoá K3.1.
- `CONTRACT.md` không đổi (không thêm trường).
- **Ảnh hưởng tới Tập 1** (`ep001-v2`, `out/script.json` + `out/claims.json`): phần lời đọc **đạt** (gốc dùng: `nominal`; lời đọc có nói `nominal`; 0 số $ không rõ gốc). Phần trên hình vẫn do bộ lấy mẫu trang chấm khi chạy đủ.

## Thay đổi ở khoá K3.3 (chủ dự án duyệt 2026-09-30)

Nguồn: quyết định của chủ dự án về phần trên hình của S09. Cấp giữ **CHẶN**. Phần lời đọc (K3.2) và phần claim không đổi.

| Mã | Thay đổi | Lý do |
|---|---|---|
| S09 | **Sửa phần trên hình, CHẶN**. Mỗi khung lấy mẫu được chấm theo các gốc của claim $ đang hiện (độ mờ > 0,5). (a) **Khung chỉ có một gốc**: đạt khi có một **nhãn gốc cấp khung**. Đó là bất kỳ chữ nào đang hiện trên khung mang từ của gốc đó (regex `BASIS`, ví dụ nhãn góc "All $ in dollars of the day"), không cần nằm gần số. Vì chấm từng khung nên nhãn phải hiện **suốt lúc** có số $; khung nào có số mà nhãn chưa hiện hoặc đã tắt thì trượt. (b) **Khung trộn nhiều gốc** (nominal và real): giữ luật cũ, mỗi số $ phải có từ gốc của chính nó trong cùng khối chữ hoặc trong 300 px; nhãn góc không thay được. (c) Claim $ không khai gốc thì luôn trượt | 70 nhãn cạnh từng số làm rối hình đã ký. Nhãn gốc cấp khung (chú thích góc, dòng đơn vị) là quy ước chuẩn của biểu đồ dữ liệu, đủ cho mục đích DX-H3 (người xem không nhầm thực với danh nghĩa). Khi một khung trộn hai gốc, nhãn chung không nói được số nào thuộc gốc nào, nên vẫn cần nhãn cạnh từng số |

- Fingerprint của S09 đổi (định nghĩa khác), nên REG không so S09 với báo cáo cũ.
- Điểm mù (ghi để khoá sau): nhãn cấp khung nhận ra bằng từ khoá, nên một chữ tình cờ mang từ gốc (ví dụ "real" trong "real estate") cũng được tính là nhãn trên khung một gốc.

## Thay đổi ở khoá K3.4 (chủ dự án duyệt 2026-09-30)

Nguồn: quyết định của chủ dự án về bộ dò ADVICE của S10. Cấp giữ **CHẶN**, mục đích DX-I1/DX-I2 (không khuyên, không dự báo) giữ nguyên.

| Mã | Thay đổi | Lý do |
|---|---|---|
| S10 | **Sửa bộ dò ADVICE, CHẶN**. Trước đây mẫu `^(… never\|always\|don't\|do not …)` bắt mọi dòng **bắt đầu** bằng từ chỉ thị. Nay `never`, `always`, `don't`, `do not` chỉ tính là lời khuyên khi ở **dạng mệnh lệnh**: đứng đầu dòng hoặc đầu mệnh đề (sau `. ! ? ; : — –`), theo sau (có thể qua `ever`) là một **động từ hành động hướng tới người xem** (danh sách `ACTION`: refinance, buy, sell, lock, wait, pay, borrow, invest, withdraw, take, sign, switch, keep, spend, save, retire, …). Từ chỉ thị đứng riêng hay làm nhãn kết quả ("Never", "Never / not before the old loan's last payment") và câu kể ("the fees never come back") không tính. Các mẫu ADVICE khác giữ nguyên: lời khuyên có chủ ngữ người xem (`you should/must/need to/…`, `should you …`), `we/I recommend`, câu mệnh lệnh bắt đầu bằng `consider/make sure/avoid/invest/buy/sell/choose/pick/keep/start/stop/talk to/plan`, "safe withdrawal rate". Áp cho cả lời đọc và chữ trên hình. **FORECAST, FOUR, WE_BAD và hai cụm bắt buộc ("US only", "history, not a forecast") không đổi** | Bắt nhầm, không nới mục đích: chữ trên hình "Never" ở S11 Tập 1 là **kết quả tính toán** (hoà vốn không bao giờ tới trước kỳ trả cuối của khoản vay cũ), không phải lời bảo người xem làm gì. Luật cũ khớp theo vị trí đầu dòng nên không phân biệt được nhãn kết quả với mệnh lệnh. Mọi lời khuyên dạng mệnh lệnh ("Never refinance before …", "Don't sell in a crash", "Always lock the rate") vẫn trượt |

- Fingerprint của S10 đổi (định nghĩa khác), nên REG không so S10 với báo cáo cũ.
- Điểm mù (ghi để khoá sau): lời khuyên mệnh lệnh dùng động từ ngoài danh sách `ACTION` sau never/always/don't/do not sẽ lọt; danh sách mở rộng qua khoá sau.

## Ngưỡng tạm (chủ dự án duyệt 2026-09-28; K2, K3 bổ sung, chờ duyệt)

Chủ dự án duyệt khoá `62b5206d…` ngày 2026-09-28, kèm điều kiện sau. Các ngưỡng dưới đây là **NGƯỠNG TẠM**. Chúng được hiệu chỉnh sau Tập 1 bằng điểm chấm tay của chủ dự án (phiếu `RUBRIC.md`, H5 cho V12/V13, H7 cho T2, H8 cho T1/T3).

| Luật | Ngưỡng tạm |
|---|---|
| T1 *(K2)* | ở khe nghỉ của lời: độ nổi ≥ 3 dB (khung 20 ms); ≥ 60% số lượt nghe được; dải khai báo ≥ 50% năng lượng stem `sonify` |
| L1 *(K2)* | lời/tiếng dữ liệu ở 1–4 kHz, phân vị 10 của các cửa sổ có tiếng dữ liệu, ≥ 20 dB; 0 từ khoá bị mất |
| S16 *(K2)* | ≥ 75% câu có số quyết định gắn nhân vật hoặc kịch bản (tên trong cùng cảnh, tới câu đó) |
| S13 *(K2)* | CV độ dài câu (câu ≥ 4 chữ) ≥ 0,35; 0 chuỗi ≥ 3 câu liền ≤ 6 chữ |
| T2 | câu nhạc lặp ≤ 5% |
| T3 | chuyển tiếp vào khoảng lặng 150–400 ms; sàn master ≥ −80 dBFS, room ≥ −75 dBFS |
| V12 | NCC ≥ 0,97 |
| V13 | mỗi cú máy ≤ 3 s; tổng thời gian máy chuyển ≤ 15% |
| A17 *(K3)* | câu có khoảng lặng trong câu > 20% hoặc ≥ 1 lần / 5 chữ: ≤ 10% số câu; khoảng giữa câu < 0,10 s hoặc > max(3·G, G + 1 s): ≤ 10% |
| A18 *(K3)* | 1 giọng (nhà cung cấp, voiceId, model) cho cả tập |
| F07 *(K3)* | 480–900 s (CHARTER §1) |

### Điểm hiệu chỉnh của T1 và L1 (K2)

Chuẩn là phán đoán của chủ dự án; ba điểm bắt buộc:

| Mẫu | Phán đoán của chủ dự án | Phải | T1 (lượt nghe được ≥ 0,60) | L1 (phân vị 10, 1–4 kHz, ≥ 20 dB) |
|---|---|---|---|---|
| **Bài D vòng 3** (master `6531f6c8…`, stem M3) | "chưa có tiếng dữ liệu" (H7 = 3,5) | T1 trượt | **TRƯỢT**: 39/355 = 0,11 (dải 1,5–8 kHz của hợp đồng D). Mở dải ra 40 Hz–16 kHz (lợi nhất cho D): 0,16, vẫn trượt. Không có stem `sonify` | MISSING (không có stem `sonify`) |
| **m0 gốc** (tiếng dữ liệu 0 dB, trước +10 dB) | "vẫn bị lấn" | L1 trượt | đạt, 10/13 = 0,77 | **TRƯỢT**: −7,9 dB |
| **S2** (chủ dự án chọn), dải theo cue sheet M1b: 60–270 Hz + 4,5–7 kHz | "nghe thấy", "không lấn lời" | T1, L1 đạt | **ĐẠT**: 10/13 = 0,77 | **ĐẠT**: 26,9 dB, 0 từ mất |
| S1 (tham khảo), 125–500 Hz | — | — | đạt, 0,77 | đạt, 22,6 dB |
| S3 (tham khảo), 125–1000 Hz | — | — | đạt, 0,85 | trượt, 16,1 dB |
| m0 +10 dB (tham khảo) | "vẫn bị lấn" | — | đạt, 0,92 | trượt, −17,9 dB |

- Ngưỡng T1 hạ từ 0,75 (lượt trước) xuống **0,60**: với dải đúng cue sheet, S2 chỉ còn 0,77, sát 0,75; D ở 0,11. 0,60 để S2 có biên 0,17 và D cách xa 0,49.
- Ngưỡng L1 giữ **20 dB**: m0 gốc −7,9 dB và m0 +10 dB −17,9 dB đều trượt xa; S2 đạt với biên 6,9 dB. Không cần nâng.
- m0 gốc = stem `sonify` của `m0-sample` hạ 10 dB (bản +10 dB là bản đã commit; README của mẫu ghi `SONIFY_GAIN_DB=10`), master = tổng stem.
- Cách tách lớp tiếng dữ liệu cho S1–S3 (bộ duyệt chỉ có mp4): mix / g − Σ(stem khác của m0), g bình phương nhỏ nhất (1,134). Kiểm trên m0 có stem thật: T1 giống hệt, L1 lệch 2,7 dB; nhiễu AAC làm L1 của S1–S3 là cận dưới.
- Số đo và kịch bản: `checks-runs/K2-calibration/`; bài D: `checks-runs/D-r3-6531f6c8/K2/`.

**Mọi thay đổi ngưỡng về sau cần chủ dự án duyệt, và phải khoá lại** (LOCK mới, CHARTER §7.1). Bên dựng không đổi ngưỡng. Phiên kiểm cũng không tự đổi ngưỡng khi chưa được duyệt.

## Luật mới: định nghĩa và cách đo

**T1 — âm thanh theo dữ liệu nghe thấy được** (DX-A1, sổ gu G-001, G-006; K2 định nghĩa lại)

1. **Sự kiện.** Hợp của hai nguồn:
   - sự kiện khai báo trong `out/sonify-events.json`: `f0` của mỗi cột, `f` của mỗi điểm, **mọi mẫu** của mỗi lần vẽ đường (nên một lần vẽ là một cụm);
   - sự kiện biểu đồ bộ lấy mẫu tự đo: camera giữ đứng, trang tiến 0,1 s, và một hình `bar`/`series`/`mark` (hoặc hình mang `char`) hiện ra hay đổi hộp ≥ 1 px.

   Các sự kiện cách nhau ≤ 0,15 s gộp thành một cụm. Mỗi cụm cho một **lượt** ở lúc bắt đầu và mỗi 0,5 s sau đó tới hết cụm.
2. **Dải tần** = `sonification.bandsHz` của hợp đồng tập, lấy từ cue sheet (tiếng dữ liệu đặt ở đâu thì đo ở đó). Không có thì MISSING.
3. **Khe nghỉ của lời.** Khung 20 ms (bước 5 ms) mà stem giọng < −45 dBFS, hoặc thấp hơn đỉnh của chính nó trong ±0,3 s ít nhất 15 dB: khe giữa âm tiết, giữa từ, giữa câu, và mọi chỗ không có lời.
4. **Nghe thấy.** Một lượt ở `t` nghe thấy khi, ở một khung khe nghỉ trong `[t − 0,10, t + 0,50 s]`:
   - độ nổi = 10·log10((P_son + P_rest) / P_rest) ≥ 3 dB (P_son: công suất trong dải của stem `sonify`; P_rest: của tổng các stem còn lại);
   - mức dải của tiếng dữ liệu ≥ −60 dBFS.

   Trong lúc lời đang đọc, T1 **không đòi gì** (L1 chấm chỗ đó).
5. **Ngưỡng (tạm).** ≥ 60% số lượt nghe thấy.
6. **Kiểm thật.** Dải khai báo chứa ≥ 50% năng lượng của stem `sonify` (không khai dải rỗng để né). Tổng các stem khớp master trong dải (tương quan ≥ 0,90). Phải có stem `sonify` riêng; tiếng dữ liệu trộn vào `sfx` thì luật đo trên `sfx`, báo số, nhưng không thể đạt.

**L1 — không lấn lời** (DX-A1, DX-A9, sổ gu G-006; K2, mới)

1. **Năng lượng.** Cửa sổ 100 ms có lời (stem giọng > −45 dBFS, như A07). Ở dải 1–4 kHz (phụ âm và formant trên, nơi bị che thì mất độ rõ): tỉ số = 10·log10(P_giọng / P_sonify), chỉ tính các cửa sổ có tiếng dữ liệu trong dải (≥ −80 dBFS). Lấy phân vị 10. Ngưỡng tạm: ≥ 20 dB. Không cửa sổ nào có tiếng dữ liệu khi có lời thì đạt.
2. **Từ khoá.** ASR riêng (như `asr_master`: cắt theo câu, small.en, hai lượt) trên hai bản trộn stem: mọi stem, và mọi stem trừ `sonify`. Từ khoá như A14 (số, tên riêng, thuật ngữ). Một từ nghe được khi không có tiếng dữ liệu mà mất khi có là **bị mất**. Ngưỡng: 0.
3. Cần stem `sonify` (thiếu thì MISSING: phải tách được mới chấm được).

**S16 — số quyết định gắn với hoàn cảnh người xem** (DX-S3, RUBRIC H4, sổ gu G-008; K2, mới, tạm)

- Số quyết định = `display` của claim `decisive=true` trong `out/claims.json` hoặc có tên trong `claims.decisive` của hợp đồng tập.
- Câu quyết định = câu của `out/script.json` nói một số đó (so theo giá trị).
- Câu đó **gắn** khi nó, hoặc câu ngay trước trong cùng cảnh, gọi tên một nhân vật hay kịch bản của hợp đồng tập (`characters.<k>.words`, `scenarios.<k>.words`; khớp nguyên từ, không phân biệt hoa thường, từ đơn khớp cả số nhiều).
- Ngưỡng tạm: ≥ 1 câu quyết định; ≥ 75% câu quyết định được gắn. Chưa có tập nào được chủ dự án chấm H4 theo tiêu chí mới để hiệu chỉnh.

**F11 — artefact phải giao** (K2, mới)

- `artefacts.M3` của hợp đồng tập (đường dẫn hoặc glob): mỗi mục khớp ≥ 1 file; danh sách phải gồm mọi file phát hành của `CONTRACT.md` (`RELEASE_FILES` trong `py/r_file.py`).

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
  - K2 đổi định nghĩa của S01, S03–S06, S13, V04, V09, T1 (câu đo đổi, nên fingerprint đổi): REG không so các luật này với báo cáo khoá trước. F11, S16, L1 mới, không có gì để so.
  - K3 đổi định nghĩa của S02, REG và F07 (fingerprint đổi); F12, A16, A17, A18 mới. Mọi luật khác giữ fingerprint của khoá K2 `f9e24c91…`, nên REG so được với báo cáo K2.
  - K3.1 đổi định nghĩa của F12 (fingerprint đổi). Mọi luật khác giữ fingerprint của khoá K3 `b57a88f9…`.
- Một luật so được, PASS ở phiên bản trước mà nay không PASS, là **hồi quy**. K3: chỉ hồi quy của luật **CHẶN** làm REG trượt; hồi quy của luật CHÍNH, THAM KHẢO được liệt kê kèm cấp (luật CHÍNH đó vẫn cần giải thích vì nó không PASS).
- Báo cáo liệt kê các luật không so được và các luật đã cải thiện.

## Thay đổi ở khoá K3.5 (chủ dự án duyệt 2026-10-01, a93637a)

Nguồn: việc giao cho phiên K3.5 (Tập 2: khoản vay lãi thả nổi so với lãi cố định, phát lại qua mọi cửa sổ của lịch sử chỉ số lãi ngắn hạn). **Không luật nào đổi cấp, ngưỡng hay định nghĩa.** Chỉ thêm một loại mô hình mà S01 và S05 đã đọc qua `model.kind`.

| Mã | Thay đổi | Lý do |
|---|---|---|
| S01, S05 (`r_model.py`) | **Loại mô hình mới `float-vs-fixed-replay`** (bảng "Loại mô hình" của `CONTRACT.md`). Viết **từ đặc tả**: các trường `numbers[].definition` và `assumptions` của `topics-r1/machine/debt-2/result.json` (không phải `topics-r2/machine/debt-2`, đề tài khác trùng tên). Không đọc `calc.py` hay mã nào dưới `episodes/ep002/`; nhánh `ep002` chưa có `checks-notes.md` lúc khoá. Tham số: file chỉ số và cột, gốc vay, số kỳ, lãi cố định, lãi thả nổi khởi điểm, tháng bắt đầu đầu tiên, sàn chỉ số, trần lãi (tuỳ chọn, mặc định không có), các mốc chia thời kỳ, các khoảng chênh khởi điểm cho đường độ nhạy (tuỳ chọn). Đại lượng: số cửa sổ; tổng lãi khoản cố định; tỉ lệ cửa sổ thả nổi đắt hơn (cả kỳ, theo thời kỳ); chênh trung vị, tốt nhất, xấu nhất và tháng bắt đầu tốt nhất, xấu nhất; lãi cao nhất; khoản trả hàng tháng cao nhất; tỉ lệ đắt hơn theo khoảng chênh khởi điểm. Ba bất biến cho S05: lãi tháng đầu của khoản thả nổi = lãi khởi điểm; chỉ số không âm; tổng lãi khoản cố định khớp công thức trả đều | Tập 2 cần bản tính lại độc lập; thiếu thì S01 và S05 là MISSING |
| Tháng | Mọi tháng (tham số, file chỉ số, file mô hình, khoá claim) được **chuẩn hoá trước khi so**: `YYYY-MM` ≡ `YYYY-MM-01`; ngày khác `01` không phải tháng và không khớp | Bài học topics-r2 V3: so chuỗi ngày làm `1977-04` ≠ `1977-04-01` |

- Đối chiếu (không phải test, vì dữ liệu không nằm trong `checks/`): chạy bản tính lại trên FRED TB3MS (1934-01 … 2026-08, tải 2026-10-01) với tham số của đặc tả cho ra đúng mọi số trong `result.json`: 753 cửa sổ (1954-01 … 2016-09), lãi cố định $26,005, đắt hơn 14,2%, chênh trung vị −$3,832, tốt nhất −$15,295, xấu nhất +$11,219 (bắt đầu 1977-04), lãi cao nhất 20,60%, 324 cửa sổ 1954–1980 đắt hơn 28,4%, 429 cửa sổ từ 1981 đắt hơn 3,5%. Thêm: khoản trả cao nhất $863,36; đường độ nhạy (chênh khởi điểm 0,5 / 1,0 / 1,5 / 2,0 điểm) 42,5% / 31,3% / 14,2% / 8,8%.
- Chữ mô tả của S01 và S05 (`r_content.py`) **không sửa** (vẫn chỉ nêu hai loại cũ làm ví dụ), để fingerprint của mọi luật giữ nguyên như khoá K3.4; REG so được mọi luật với báo cáo cũ. Danh sách loại đầy đủ ở `CONTRACT.md` và `KINDS` của `r_model.py`.
- S05 so `float(claim.value)`: claim tháng (ví dụ "1977-04") không đưa thẳng vào S05 được, nên loại này cho khoá số `worstStartYear` / `worstStartMonth`; tháng dạng chuỗi được so ở S01. (K3.6: S05 nay so được claim tháng, xem mục "Thay đổi ở khoá K3.6".)
- Điểm mù (ghi để khoá sau): bất biến 3 (lãi cố định tính từng tháng = công thức) canh chính bản tính lại của máy kiểm, không có đầu vào nào của bên dựng làm nó trượt; đường độ nhạy giữ mọi tham số khác, chỉ dời lãi khởi điểm (và vì thế biên lãi).

## Thay đổi ở khoá K3.6 (chờ chủ dự án duyệt)

Nguồn: việc giao cho phiên K3.6 (Tập 2 sau C2): mục "K3.6" của `episodes/ep002/checks-notes.md` (nhánh `ep002`, 26 claim kịch bản v3 chưa có khoá) và bốn đề xuất của K3.5 (issue #13). Viết **từ đặc tả** (mục đó và các trường `definition`/`assumptions` của `topics-r1/machine/debt-2/result.json`); không đọc `calc.py` hay mã dựng dưới `episodes/ep002/` (`model/`, `calc*`). **Không luật nào đổi cấp hay ngưỡng.**

| Mã | Thay đổi | Lý do |
|---|---|---|
| S05 (`r_model.py`, kind `float-vs-fixed-replay`) | **Khoá mới**, mỗi khoá tường minh (S05 không ghép hai khoá để "suy ra" một số): `shareCostlierAtSpread:<điểm>:<tháng đầu thời kỳ>` (tỉ lệ cửa sổ đắt hơn theo khoảng chênh **và** thời kỳ); `worstDifferenceAtSpread:<điểm>` (chênh xấu nhất, $); `worstStartAtSpread:<điểm>` (tháng bắt đầu của cửa sổ xấu nhất, hoà thì tháng sớm nhất; dạng số `worstStartAtSpreadYear:<điểm>` / `worstStartAtSpreadMonth:<điểm>` như `worstStartYear/Month`); `minShareCostlierOverSpreads:<tháng đầu thời kỳ>` (nhỏ nhất qua **mọi** khoảng chênh trong `params.spreads`; không có `spreads` = MISSING); `floatFirstPayment` (khoản trả tháng đầu của khoản thả nổi: trả đều gốc trên `termMonths` kỳ ở `floatStartRate`); `firstPaymentGap` (= `fixedPayment` − `floatFirstPayment`); `worstWindowMaxRate` (lãi tháng cao nhất trong cửa sổ xấu nhất); `shareRateAboveFixed` (% cửa sổ có ít nhất một tháng lãi > `fixedRate`, so **nghiêm ngặt**); `worstShareOfFixed` (= 100 × `worstDifference` / `fixedTotalInterest`, %). Khoảng chênh = `fixedRate` − lãi thả nổi khởi điểm, nhận cả **0 và số âm** (khoản thả nổi khởi điểm bằng hoặc cao hơn lãi cố định). Sai số như K3.5: $0,50 tiền; 0,005 lãi, tỉ lệ (%), khoản trả; tháng chính xác | 26 claim kịch bản v3 của Tập 2 không có khoá K3.5 |
| S05 (`r_content.py`) | **Claim tháng** (issue #13, đề xuất 1): khi khoá là một đại lượng tháng (`firstStart`, `lastStart`, `bestStart`, `worstStart`, `worstStartAtSpread:<điểm>`), S05 so giá trị claim viết `YYYY-MM` hoặc `YYYY-MM-01` **sau chuẩn hoá** (cùng hàm `ym` của S01); ngày khác `01`, hay một số, thì lệch. Khoá số không đổi hành vi. Chữ mô tả của S05 (đề xuất 4) nay nêu ví dụ khoá đúng của cả ba loại (`geomean:1966`, `maya.cut36`, `shareCostlierAtSpread:1.5:1954-01`; ví dụ cũ `breakEven:0.5`, `spreadFor:36` không phải khoá của loại nào) và cách so tháng | Claim ngày của kịch bản (`first_start`, `last_start`, `worst_start`, `best_start`, `gap_worst_start_all`) nay vào thẳng S05, không phải đổi sang `…Year/…Month` |

- **Fingerprint:** chỉ S05 đổi (định nghĩa khác: so được claim tháng), nên REG không so S05 với báo cáo cũ. Mọi luật khác (80 luật còn lại và REG) giữ fingerprint của `main` @ `a93637a` (LOCK `bd1948d9…`).
- **Không làm (và vì sao):** chữ mô tả của **S01** giữ nguyên (đề xuất 4): sửa chữ đổi fingerprint của S01 mà không đổi hành vi, REG mất khả năng so S01, và việc giao giữ fingerprint mọi luật cũ trừ S05/S06 của mục ngày. **S06** không đổi: S06 so `year`/`case` dạng chuỗi, không có ngày, nên không cùng gốc với đề xuất 1; đề xuất 2 (thuộc tính `month` có `range`) là tính năng mới, cần bộ lấy mẫu trang phát `monthsTrack`; để khoá sau. Đề xuất 3: chốt quy ước (dưới đây), không nới dung sai.
- **Quy ước giá trị claim (issue #13, đề xuất 3):** `out/claims.json` ghi `value` **chưa làm tròn** (ví dụ `14.2118`, không phải `14.2`); `display` mới là chữ làm tròn trên màn hình. S05 so `value` với số tính lại bằng dung sai **0,005** cho lãi, tỉ lệ (%) và khoản trả, **$0,50** cho tiền (nên tiền làm tròn tới đô la vẫn đạt), tháng chính xác. Một tỉ lệ làm tròn tới 0,1 thường lệch quá 0,005 và S05 trượt **dù `display` đúng**: đó là chủ ý (claim phải mang đúng số mô hình, chữ hiển thị do S07/S08 so).
- **Gói số của `gap_worst_start_all`** ("tháng xấu nhất trùng nhau ở mọi khoảng chênh"): một claim chỉ gắn được một khoá; gắn `worstStartAtSpread:<điểm>` thì S05 kiểm một khoảng chênh. Muốn kiểm câu "mọi khoảng chênh", hợp đồng tập gắn thêm claim `worstStartAtSpread:<điểm>` cho từng khoảng chênh của `spreads`. Điểm mù ghi để khoá sau.
- Đối chiếu (không phải test): trên FRED TB3MS (1934-01 … 2026-08, SHA-256 `ebf04b1a…` như `data/sources.json` của Tập 2) với `contract.json` của `ep002` @ `7d0fb44`, cả 26 claim của mục K3.6 gắn được khoá và tính lại được; 16 khớp, 10 lệch **chỉ vì `claims.json` ghi tỉ lệ đã làm tròn** (số tính lại làm tròn ra đúng `display`). Chi tiết ở gói duyệt của phiên K3.6.

## Thay đổi ở khoá K3.7 (chờ chủ dự án duyệt)

Nguồn: việc giao cho phiên K của Tập 3 (issue #29). Viết **từ đặc tả**: `topics-r1/machine/retire-4/model.json` (`newKindNeeds`, `quantities[].meaning`), `statements.json`, `episodes/ep003/numbers.md` và `checks-notes.md` (nhánh `ep003`). Không đọc `calc.py`, `episodes/ep003/model/` hay mã dựng nào. **Không luật nào đổi cấp, ngưỡng hay định nghĩa**; chỉ thêm một loại mô hình mà S01 và S05 đọc qua `model.kind`.

| Mã | Thay đổi | Lý do |
|---|---|---|
| S01, S05 (`r_model.py`) | **Loại mô hình mới `lock-vs-roll-replay`** (bảng "Loại mô hình" của `CONTRACT.md`): khoá một bội số đã biết (`lock.multiple`) hoặc một chuỗi lãi khoá (`lock.file…`, kép mỗi `q` tháng) trong `horizonMonths` tháng, so với lăn một lãi ngắn hạn mỗi `roll.periodMonths` tháng, phát lại từ mọi tháng bắt đầu. Tham số hoá để retire-3 dùng lại (`p = 12`, chuỗi khoá GS5 `q = 12`, `H = 60`, `startFilter:{type:"rollRateAboveLockRate"}` và các chuỗi liên tiếp). Tập con tháng bắt đầu (`subsets`, được chồng nhau), CPI (`deflator`), dải gần hoà (`nearBandPct`). Khoá S05 theo dạng `<đại lượng>` hoặc `<đại lượng>:<tập>`, phủ: tỉ lệ lăn hơn / khoá hơn / hoà (cả kỳ, theo thời kỳ, cửa sổ có bảo đảm thật), trung vị / nhỏ nhất / lớn nhất của bội số và tháng của chúng, cửa sổ mới nhất, lãi lăn mới nhất và tháng, lãi tương đương của bội số (3,53%), **ngưỡng lãi trung bình** `steadyBreakevenRate` (3,47%) và tỉ lệ quy tắc trung bình đúng `shareMeanRuleAgrees`, tỉ lệ trung bình dưới lãi tháng đầu, **sức mua theo CPI** (số cửa sổ thực, tỉ lệ giữ / mất sức mua, trung vị, thấp nhất và tháng, tháng cuối mất sức mua), biên tập và số cửa sổ trước một tập (`nWindowsBefore`, `shareWindowsBefore`: cửa sổ giả định trước 5/2005), số kỳ không chồng, đếm gần hoà, hằng của kỳ (`horizonYears`, `rollsPerHorizon`). Năm bất biến của đặc tả cho S05 | Tập 3 cần bản tính lại độc lập; thiếu thì S01 và S05 là MISSING |
| Tháng | Như K3.5/K3.6: mọi tháng (tham số, file, file mô hình, claim) so **sau chuẩn hoá** (`YYYY-MM` ≡ `YYYY-MM-01`; ngày khác `01` không phải tháng). Ô trống hoặc "." trong file chuỗi là **thiếu**, không phải 0 (CPIAUCNS 2025-10 trống) | Bài học topics-r2 V3; dữ liệu CPI có tháng trống |

- **Fingerprint:** `r_content.py`, `tiers.py`, `run.py` không đổi; fingerprint của cả 82 luật (gồm REG) trùng `main` @ `594c850` (LOCK `2fcc9fcc…`), nên REG so được mọi luật với báo cáo cũ. Không luật cũ nào đổi hành vi: S01/S05 chỉ chạy nhánh mới khi `model.kind` = `lock-vs-roll-replay`.
- Đối chiếu (không phải test, vì dữ liệu không nằm trong `checks/`): FRED TB3MS và CPIAUCNS (coed 2026-08-01, SHA-256 `ebf04b1a…`, `f79e3a78…` như `retire-4/sources.json`), tham số của `retire-4/model.json` (`roll.termMonths` 3). Cả **50** claim mô hình của `numbers.md` (46 claim kịch bản trừ 5 claim bối cảnh/người xem = 41, cộng 9 ID khác của `numbers.md`) gắn được khoá và tính lại được: **41 khớp**, **9 lệch chỉ vì `numbers.md` ghi tỉ lệ đã làm tròn 0,1** (số tính lại làm tròn ra đúng giá trị ghi; ví dụ 52,3482 → 52,3), **0 lệch thật**. Bảy bất biến đạt. S01 trên `out/model.json` hiện có của `ep003` (dựng trước khi có tên kind): 3.560 giá trị so, **mọi cửa sổ khớp**; 16 lệch và 4 phần không tính lại đều do tên trường / dạng (thiếu tham số nhắc lại, `…LockVsRollPct` đặt tên khác, `rollRateLatest` là object, `skippedStarts` là danh sách) — bên dựng đổi theo `CONTRACT.md`.
- Điểm mù (ghi để khoá sau): (1) năm bất biến canh chính bản tính lại của máy kiểm; không đầu vào nào của bên dựng làm chúng trượt (như K3.5). (2) Đề xuất của `checks-notes.md` §3 — "mọi khung hiện cửa sổ trước 2005-05 có nhãn giả định" — chưa phải luật: cần thuộc tính tháng trên đối tượng trang (như đề xuất `monthsTrack` của K3.6); đến khi có, S02 (`claims.assumptions`) chỉ canh nhãn có trên màn hình, không canh từng khung. (3) `startFilter` chỉ có một loại (`rollRateAboveLockRate`); retire-3 chưa chạy trên dữ liệu thật ở khoá này (chưa có GS1/GS5 ghim).

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
    - K2: V04 trượt khi màu trên màn hình khác màu hợp đồng tập khai (`V04-not-declared-colour`); mọi fixture có `contract.json`.
- **K2** (Python): S01 thêm ca `S01/refinance` (mô hình Tập 1, một tháng hoà vốn lệch 1 phải trượt); S03–S06, V04, V09 đọc hợp đồng của fixture; T1 mới (tiếng dữ liệu trong khe âm tiết: nổi thì đạt, thấp 30 dB thì trượt); L1 (tiếng 2 kHz ngang lời và làm mất con số thì trượt; nhịp 300 Hz thấp thì đạt); S16 (hai câu số quyết định gọi tên nhân vật hoặc kịch bản thì đạt, không gọi thì trượt); F11 (thiếu một file đã khai thì trượt).

- **K3** (Python): A16 (`spoken` có "…" và thẻ `[pause]` thì trượt; số đọc bằng chữ có dấu phẩy và gạch ngang có trong câu viết thì đạt); A17 (mỗi câu có hai khoảng lặng 0,6 s thì trượt; câu liền, cách nhau 0,4 s thì đạt); A18 (hai model khai trong `takes.json` thì trượt, số đo nhóm phải tách được); F12 (thiếu mục cho stem nhạc và giọng không được phép thương mại thì trượt; stem im lặng không cần mục); S02 đọc giả định từ hợp đồng fixture. Ca riêng: `F07/too-long` (905 s trượt, 480 s đạt); `TIERS` (mọi luật có cấp, F07 và A18 là CHÍNH theo quyết định của chủ dự án; một luật không cấp thì trượt), `VERDICT` (CHẶN không đạt → TRƯỢT; chỉ THAM KHẢO không đạt → ĐẠT; CHÍNH không đạt chưa giải thích → CHỜ GIẢI THÍCH, có giải thích → ĐẠT), `REG/tier` (hồi quy của luật THAM KHẢO không làm REG trượt, của luật CHẶN thì có), `NEAR` (chỉ số cách ngưỡng 4,5% ở hai phía được nêu, cách 6% thì không).
- **K3.1** (Python, F12 tài sản hình): fixture `F12` phải đạt với đủ sáu loại tài sản hình (ảnh, phông, tài liệu public domain, texture tự làm, thẻ trích dẫn) và phải trượt khi giọng không được phép thương mại. Ca riêng: `F12/photo` (ảnh bên thứ ba không có mục → trượt; có mục đủ điều khoản → đạt); `F12/font` (phông khai trong hợp đồng tập, mục thiếu điều khoản → trượt; có trích OFL + URL → đạt); `F12/public-domain` (tài liệu liên bang có `source.url` và `pdBasis` → đạt, không cần điều khoản; thiếu nguồn và căn cứ → trượt); `F12/quote-card` (thẻ trích dẫn tự vẽ thiếu `quoteSource` → trượt dù có generator); `F12/self-made` (generator không tồn tại → trượt); `F12/no-manifest` (không khai danh sách hình ở đâu → MISSING, tính là trượt; danh sách rỗng khai rõ trong hợp đồng → đạt); `F12/loaded` (trang nạp một ảnh không khai → trượt; khai bằng glob `path` → đạt); `F12/loaded-font` (`document.fonts` có họ phông không khai → trượt; mặt phông `unloaded` không tính); `F12/generated` (file do mã dự án sinh, khớp quy tắc `generated` có generator tồn tại → đạt; generator không tồn tại → trượt; ảnh 404 không tính). Trang (`test_page.js`, đầu-cuối qua bộ lấy mẫu thật): `F12-undeclared-font` (trang nạp một phông không khai → trượt) và `F12-declared-image` (trang nạp một ảnh đã khai → đạt); trang fixture có thêm `load:{images, fonts}`.
- **K3.2** (Python, S09 lời đọc cả tập): `S09/said-once` (tập có số $ mà lời đọc không nói gốc nào → trượt; nói một lần, ở cảnh cuối, sau các số $ → đạt); `S09/every-basis` (tập dùng cả nominal và real mà chỉ nói "nominal" → trượt; nói cả hai → đạt); `S09/screen` (lời đọc nói gốc nhưng khung hình thiếu nhãn gốc → **vẫn trượt**); `S09/unknown-basis` (số $ đọc lên không khớp claim nào → trượt). Trang: `S09-no-basis` của `test_page.js` (khung có số $ không nhãn gốc → trượt) giữ nguyên; lời đọc của trang fixture nay có một câu nói gốc "real" (trước là rỗng), để trang sạch vẫn đạt S09 và ca trượt chỉ trượt vì nhãn trên hình.
- **K3.3** (trang, S09 phần trên hình, `test_page.js` đầu-cuối qua bộ lấy mẫu thật): `S09-frame-label` (khung một gốc, số không có nhãn cạnh, có nhãn góc "All $ in real terms" xa số → đạt); `S09-no-basis` (khung một gốc, không nhãn nào → trượt); `S09-mixed-corner-only` (khung có $1,200 real và $900 nominal, chỉ có nhãn góc → trượt); `S09-mixed-labelled` (khung trộn, mỗi số có nhãn gốc cạnh nó → đạt). Fixture trang thêm claim `$900` nominal (chỉ hiện ở các ca S09 trộn); lời đọc của fixture nói cả hai gốc.
- **K3.4** (Python, S10 ADVICE; lời đọc và chữ trên hình qua `textTrack` của `page.json`): `S10/never-label` (chữ trên hình "Never" đứng riêng và "Never / not before the old loan's last payment" → đạt; "Never refinance before the old loan's last payment." → trượt); `S10/never-narration` ("the fees never come back" → đạt; "Never refinance before the fees come back." → trượt); `S10/should` ("You should refinance." → trượt; "Maya could refinance." → đạt); `S10/old-advice` (ba dạng cũ "Don't sell in a crash.", "Always lock the rate.", "Consider the fees." phải bị bắt **cả ba** → trượt; cùng sự việc kể như lịch sử → đạt). Fixture `S10` cũ ("You should keep your withdrawals at 4%.") vẫn trượt.
- **K3.5** (Python, loại mô hình `float-vs-fixed-replay`; chỉ số tổng hợp 5 tháng, khoản vay $1.200 trả 2 kỳ, mọi cửa sổ tính tay được và viết lại trong test, không gọi mã của luật): `S01/float-fixed` (mọi cửa sổ khớp, tháng viết lẫn `YYYY-MM` và `YYYY-MM-01` → đạt; chênh của một cửa sổ lệch $1 → trượt); `S01/float-fixed-dates` (`worstStart` "2000-01" → đạt; "2000-01-15" → trượt); `S05/float-fixed` (lãi cố định $13,5168, đắt hơn 25% cả kỳ, 50% / 0% theo hai thời kỳ, tháng xấu nhất 2000-01, lãi cao nhất 17%, độ nhạy 25% ở chênh 3 điểm và 50% ở chênh 0 → đạt; thời kỳ thứ hai khai 50% → trượt); `S05/float-fixed-first-rate` (trần 5% dưới lãi khởi điểm 6% → bất biến lãi tháng đầu trượt; trần 20% → đạt); `S05/float-fixed-index` (sàn chỉ số −5 để chỉ số âm → bất biến chỉ số không âm trượt; sàn 0 → đạt).
- **K3.6** (Python, khoá S05 mới của `float-vs-fixed-replay`; cùng chỉ số 5 tháng và khoản vay $1.200 trả 2 kỳ; bảng lãi theo khoảng chênh −1, 0, 1, 2, 3 tính tay trong test bằng hàm trả 2 kỳ của test, không gọi mã của luật): `S05/float-fixed-spread-period` (tỉ lệ đắt hơn theo khoảng chênh và thời kỳ: 100/100, 50/50, 50/50, 50/0, 50/0 → đạt; khoảng chênh 2 từ 2000-03 khai 50% → trượt); `S05/float-fixed-spread-worst` (chênh xấu nhất ở −1, 0, 3 và tháng xấu nhất "2000-01-01", 2000 / 1 → đạt; chênh ở 0 lệch $1 → trượt); `S05/float-fixed-spread-worst-start` (tháng xấu nhất ở chênh 2 "2000-01" → đạt; "2000-03" → trượt); `S05/float-fixed-min-spreads` (nhỏ nhất qua −1…3: 50% / 0% → đạt; 50% từ 2000-03, tức bỏ sót chênh 2 và 3 → trượt); `S05/float-fixed-payments` (khoản trả đầu $604,5037, chênh khoản trả $2,2547 → đạt; chênh đổi dấu → trượt); `S05/float-fixed-window` (lãi đỉnh cửa sổ xấu nhất 17%, 50% cửa sổ có tháng lãi > 9% dù chỉ 25% đắt hơn, tỉ số xấu nhất / lãi cố định → đạt; khai 25% → trượt); `S05/float-fixed-rate-above` (lãi khởi điểm 9% = lãi cố định: tháng đầu bằng đúng 9% không tính, 50% → đạt; 100% → trượt, tức so không nghiêm ngặt); `S05/float-fixed-months` (claim tháng "2000-01", "2000-04-01", "2000-01-01", "2000-02" → đạt; "2000-01-15" → trượt).
- **K3.7** (Python, loại mô hình `lock-vs-roll-replay`; mọi số tính tay trong test, không gọi mã của luật). Bội số hằng (kiểu retire-4): lãi lăn 12, 24, 0, 12, 6, 12 (2000-01 … 06), p = 1, H = 2, m = 1,02, CPI 100, 100, 101, 98, 100, 100, trống: `S01/lock-roll` (mọi cửa sổ và tổng hợp khớp, tháng viết lẫn hai dạng → đạt; bội số cửa sổ 2000-03 lệch 0,001 → trượt); `S05/lock-roll-shares` (lăn hơn 20%, hoà 20% vì 1,02 × 1,00 = m, khoá hơn 60%, theo tập 50% / 0% → đạt; hoà tính là lăn hơn, 40% → trượt); `S05/lock-roll-real` (4 cửa sổ thực, 2000-05 bỏ vì CPI 2000-07 trống, giữ sức mua 75%, thấp nhất 99,96% ở 2000-04 → đạt; đếm cả cửa sổ bị bỏ → trượt); `S05/lock-roll-mean-rule` (ngưỡng lãi đều 11,9406%, quy tắc trung bình đúng 80% vì cửa sổ hoà, trung bình dưới lãi đầu 40%, lãi tương đương 12,6162% → đạt; 100% → trượt); `S05/lock-roll-sets` (biên tập, số và tỉ lệ cửa sổ trước tập, gần hoà 3, cửa sổ mới nhất, hằng của kỳ → đạt; `subsetTo` lấy tháng cuối dữ liệu thay vì tháng bắt đầu cuối → trượt); `S05/lock-roll-months` (claim tháng hai dạng và dạng số → đạt; "2000-03-15" → trượt). Chuỗi lãi khoá có lọc (kiểu retire-3: p = 2, q = 4, H = 4): `S01/lock-roll-series` (hai chuỗi liên tiếp tách rời → đạt; gộp thành một → trượt); `S05/lock-roll-filter` (khoá hơn 66,667% cả kỳ, 50% trong tập lọc, 2 chuỗi, 1 chuỗi khoá chiếm đa số → đạt; 1 chuỗi → trượt).

## Cấp của luật (K3)

Sinh từ `py/tiers.py` (`python3 checks/py/run.py x --list` in `tier`, `tierReason`). Số luật: **29 CHẶN · 11 CHÍNH · 42 THAM KHẢO** (82 luật, gồm REG).

| Cấp | Luật |
|---|---|
| CHẶN | F01, F02, F03, F04, F05, F06, F08, F09, F10, F11, F12, A01, A02, A04, A05, A06, A14, S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, C07, REG |
| CHÍNH | F07, A18, V03, V08, V09, V11, V12, C02, C05, C14, L1 |
| THAM KHẢO | A03, A07, A08, A09, A10, A11, A12, A13, A15, A16, A17, S11, S12, S13, S14, S15, S16, R01, R02, R03, R04, R05, R06, V01, V02, V04, V05, V10, V13, C01, C03, C04, C06, C10, C11, C12, C13, C15, P01, T1, T2, T3 |

| Mã | Cấp | Vì sao |
|---|---|---|
| F01 | CHẶN | kỹ thuật file |
| F02 | CHẶN | kỹ thuật file |
| F03 | CHẶN | kỹ thuật file |
| F04 | CHẶN | kỹ thuật file |
| F05 | CHẶN | kỹ thuật file |
| F06 | CHẶN | kỹ thuật file |
| F07 | CHÍNH | độ dài theo CHARTER §1 (8–15 phút); chủ dự án hạ CHÍNH: chặn độ dài dễ dẫn tới giãn thời gian |
| F08 | CHẶN | kỹ thuật file: banding do mã hoá |
| F09 | CHẶN | kỹ thuật file: phụ đề đúng lời, đúng quy cách |
| F10 | CHẶN | kỹ thuật file: chapters hợp lệ với YouTube (≥ 3, từ 0:00, mỗi chương ≥ 10 s) |
| F11 | CHẶN | kỹ thuật file: artefact phát hành đã giao |
| F12 | CHẶN | quyền tài sản |
| A01 | CHẶN | âm lượng |
| A02 | CHẶN | true peak |
| A03 | THAM KHẢO | độ động (LRA) là lựa chọn nghề; nền tảng chỉ chuẩn hoá âm lượng tích hợp (A01) |
| A04 | CHẶN | kỹ thuật file: clip |
| A05 | CHẶN | kỹ thuật file: pha |
| A06 | CHẶN | kỹ thuật file: gộp mono |
| A07 | THAM KHẢO | tỉ lệ lời/nhạc là chỉ tiêu mix; độ rõ lời do L1 và A14 canh |
| A08 | THAM KHẢO | cách duck nhạc là tay nghề |
| A09 | THAM KHẢO | số lần dùng kỹ thuật (≥ 3 khoảng lặng) |
| A10 | THAM KHẢO | tay nghề: whoosh theo máy |
| A11 | THAM KHẢO | tay nghề: pan theo vật |
| A12 | THAM KHẢO | tay nghề: điểm nhấn nhạc |
| A13 | THAM KHẢO | tay nghề: giãn giọng |
| A14 | CHẶN | ASR không mất từ khoá |
| A15 | THAM KHẢO | chỉ tiêu tốc độ đọc |
| A16 | THAM KHẢO | cảnh báo: dấu ngắt giả trong văn bản gửi TTS |
| A17 | THAM KHẢO | cảnh báo: mật độ khoảng lặng giữa câu bất thường |
| A18 | CHÍNH | đổi model giọng giữa tập; chủ dự án nâng CHÍNH: lỗi gốc của Tập 1 v1, trái G-010 |
| S01 | CHẶN | số liệu: tính lại mô hình |
| S02 | CHẶN | claim: giả định của mô hình hiện trên màn hình |
| S03 | CHẶN | nguồn và điều khoản sử dụng dữ liệu |
| S04 | CHẶN | số liệu: đối chiếu nguồn |
| S05 | CHẶN | claim khớp mô hình; ILLUSTRATIVE |
| S06 | CHẶN | số liệu: hiện đủ mọi trường hợp đã hứa (không chọn lọc) |
| S07 | CHẶN | claim: mọi số có claim, công thức, nguồn |
| S08 | CHẶN | claim: huy hiệu ILLUSTRATIVE |
| S09 | CHẶN | claim: thực/danh nghĩa |
| S10 | CHẶN | claim: không khuyên, không dự báo (gen được bảo vệ, CHARTER §5) |
| S11 | THAM KHẢO | số lần dùng kỹ thuật (callback ≥ 3) |
| S12 | THAM KHẢO | chỉ tiêu mật độ số |
| S13 | THAM KHẢO | chỉ tiêu độ dài câu |
| S14 | THAM KHẢO | tay nghề: điểm chèn quảng cáo |
| S15 | THAM KHẢO | tay nghề: cấu trúc hồi, trần cold open |
| S16 | THAM KHẢO | chỉ tiêu gắn số với nhân vật |
| R01 | THAM KHẢO | luật nhịp |
| R02 | THAM KHẢO | luật nhịp |
| R03 | THAM KHẢO | luật nhịp |
| R04 | THAM KHẢO | luật nhịp |
| R05 | THAM KHẢO | luật nhịp |
| R06 | THAM KHẢO | luật nhịp |
| V01 | THAM KHẢO | tay nghề: hồ sơ tiền kỳ |
| V02 | THAM KHẢO | tay nghề: bố cục một phần ba |
| V03 | CHÍNH | đọc được: chữ ngoài vùng an toàn bị giao diện trình phát che |
| V04 | THAM KHẢO | tay nghề: nhận diện nhân vật |
| V05 | THAM KHẢO | tay nghề: chuyển động máy |
| V08 | CHÍNH | tương phản |
| V09 | CHÍNH | tương phản: mù màu |
| V10 | THAM KHẢO | số lần dùng kỹ thuật (match cut, J/L-cut) |
| V11 | CHÍNH | va chạm chữ |
| V12 | CHÍNH | đọc được: chữ nhân đôi, nhoè |
| V13 | THAM KHẢO | chỉ tiêu thời lượng cú máy |
| C01 | THAM KHẢO | tay nghề: lộ panel khác cảnh |
| C02 | CHÍNH | va chạm: nền đè lên dữ liệu |
| C03 | THAM KHẢO | tay nghề: nhãn đường |
| C04 | THAM KHẢO | tay nghề: trục và mốc |
| C05 | CHÍNH | tương phản: nhấn mạnh trong thang xám |
| C06 | THAM KHẢO | tay nghề: màu số theo chuỗi |
| C07 | CHẶN | số liệu: cột bị cắt trục hoặc lệch tỉ lệ làm sai số liệu |
| C10 | THAM KHẢO | tay nghề: một chữ cấp 1 |
| C11 | THAM KHẢO | tay nghề: lặp bố cục |
| C12 | THAM KHẢO | tay nghề: thay đổi chia đôi khung |
| C13 | THAM KHẢO | luật nhịp: số khớp lời ±250 ms |
| C14 | CHÍNH | đọc được ở 25% |
| C15 | THAM KHẢO | tay nghề: chỉ dùng token màu |
| P01 | THAM KHẢO | tay nghề: thumbnail |
| T1 | THAM KHẢO | chỉ tiêu tay nghề: tiếng dữ liệu nghe thấy |
| T2 | THAM KHẢO | chỉ tiêu tay nghề: nhạc không lặp |
| T3 | THAM KHẢO | chỉ tiêu tay nghề: vào khoảng lặng |
| L1 | CHÍNH | độ rõ lời: tiếng dữ liệu không lấn lời |
| REG | CHẶN | cổng hồi quy của luật CHẶN (CHARTER §5) |

**Luật không có trong danh sách của chủ dự án, K3 tự xếp** (cần chủ dự án duyệt):
- CHẶN: F08 (banding), F09 (phụ đề), F10 (chapters hợp lệ), F11 (artefact), A04–A06 (clip, pha, gộp mono) — kỹ thuật file; S06 (hiện đủ trường hợp), S10 (không khuyên, không dự báo), C07 (cột cắt trục) — số liệu và claim; S02 (giả định hiện trên màn hình) — claim.
- CHÍNH: V03 (vùng an toàn), V12 (chữ nhân đôi, nhoè), V09 và C05 (tương phản khi mù màu và trong thang xám), C02 (nền đè dữ liệu) — cùng họ với đọc được, tương phản, va chạm.
- THAM KHẢO (hạ từ "mọi luật ngang hàng" của K2): A03 (độ động LRA: lựa chọn nghề, nền tảng chỉ chuẩn hoá âm lượng tích hợp), A07–A13 (mix, duck, whoosh, pan, nhấn, giãn giọng), S11, S14, S15 (callback, điểm quảng cáo, cấu trúc hồi), V01, V02, V04, V05, V10, C01, C03, C04, C06, C10–C13, C15, P01 — tay nghề hoặc số lượng.

## Bảng luật

82 luật. **(mới)** = thêm ở khoá K1; *(sửa)* = K1 đổi cách đo so với bài D; **(K2 mới)**, *(K2 sửa)* = khoá K2; **(K3 mới)**, *(K3 sửa)* = khoá K3. Bỏ: V06, V07. Cấp của từng luật ở mục "Cấp của luật". Cột định nghĩa và ngưỡng sinh từ `python3 checks/py/run.py x --list`.

| Mã | Spec | Định nghĩa đo | Ngưỡng | Máy |
|---|---|---|---|---|
| F01 | DX-F1, DX-F2 | ffprobe of the video stream: codec, profile, pixel format, frame size, display aspect | h264 / High / yuv420p / 1920×1080 / 16:9 (square pixels) | Python |
| F02 | DX-F1 | r_frame_rate and avg_frame_rate from the stream header, and every packet duration (PTS step) in stream time base | both rates exactly 30/1 and every PTS step = 1/30 s (constant frame rate) | Python |
| F03 | DX-F3 | video packet PTS sorted: a repeated PTS is a duplicated frame, a step of k>1 frame periods is k-1 dropped frames; frame count compared with duration × 30 | dropped = 0, duplicated = 0, first PTS = 0, \|frames − duration×30\| ≤ 1 | Python |
| F04 | DX-F2 | video bitrate = sum of video packet sizes × 8 / stream duration (measured, not the header value) | ≥ 16 Mbps | Python |
| F05 | DX-F2 | stream colour tags (color_primaries, color_transfer, color_space, color_range) + decoded luma codes of 1 frame/10 s: share of Y samples outside 16–235 | all tags bt709, range tv (limited); Y outside 16–235 ≤ 0.1% of samples | Python |
| F06 | DX-F4 | ffprobe of the audio stream; bitrate = audio packet bytes × 8 / duration | AAC (LC), 48 kHz, 2 channels, measured ≥ 272 kbps (= 85% of the 320 kbps nominal: ffmpeg's native AAC at -b:a 320k measured 276 kbps on test C's master, so the measure allows its ABR undershoot but not a 256k or lower setting) | Python |
| F07 *(K3 sửa)* | DX-S1 (CH §1 length) | container duration (ffprobe format.duration); K3: the range of CHARTER §1 (8–15 minutes) | 480 … 900 s (8:00–15:00) | Python |
| F08 | DX-V5 | decoded luma of 1 frame/2 s; banding score per frame (banding_score: 240 px tiles, mean Y ≤ 80, 16-px block means fitting a plane that spans 2–40 codes with residual ≤ 1 code; share of their pixels in flat runs ≥ 12 px ending in a 1–2 code step) | worst frame ≤ 5% (frames with < 1% dark-gradient area are skipped) | Python |
| F09 | DX-F5 | out/captions.srt parsed; joined subtitle text vs joined narration text of out/script.json (whitespace-normalised, exact characters otherwise); per cue: characters per line, lines, duration; cues must not overlap | text identical (100%); every line ≤ 42 chars; ≤ 2 lines; 1.0 ≤ duration ≤ 7.0 s; 0 overlaps | Python |
| F10 | DX-F6 | chapters from out/package/description.md (lines "m:ss Title") and, if present, the MP4 chapter atoms; chapter length = next start − start (last: to end of video) | ≥ 3 chapters; first at 0:00; each ≥ 10 s; MP4 chapters (if any) equal the description's | Python |
| F11 **(K2 mới)** | CH §4 khâu 3 (hợp đồng tập, K2) | episode contract (contract.json) artefacts.M3: the release list of paths (globs allowed); each must match ≥ 1 file under the root. The list must include every release file of checks/CONTRACT.md (RELEASE_FILES; a stem may be .wav or .flac). Contract without artefacts.M3 = MISSING | every declared M3 artefact delivered; every checks/CONTRACT.md release file declared | Python |
| F12 **(K3 mới, K3.1 sửa)** | DX-A3 (sổ giấy phép), CH §5 (K3: quyền tài sản; K3.1: tài sản hình) | rights ledger out/rights.json {assets:[{name, stems:[…], visuals:[…], kind, origin, licence, thirdParty, terms:{quote, url}, commercial, generator, publicDomain, pdBasis, source:{url}, quoteSource:{who, url}}]}. (1) Sound: every delivered stem (out/audio/stems/<name>.wav\|flac of voice, music, sfx, whoosh, room, sonify) with sound (1 s RMS above −60 dBFS somewhere) must be covered by an asset listing it in stems. (2) Pictures (K3.1): the visual asset list = contract.json rights.visual[] ∪ out/visual-assets.json assets[] ({name, kind ∈ image, document, font, model3d, texture, quote-card, path\|paths (root-relative path or glob of the loaded file), family (font)}); neither declared = MISSING. Every listed visual must be covered by an asset listing its name in visuals. (3) Loaded (K3.1): the page sampler records what the render page really loads (Playwright requests + Resource Timing; document.fonts). Every loaded picture file (image, pdf, 3D model, texture by extension or content type) must match a declared visual (path/paths glob, else file name = name), and every loaded font family (status loaded) must be a declared font (family or name, case-insensitive). Not counted: browser-internal URLs (data:, blob:, about:, chrome*:, devtools:), failed loads, the browser's /favicon.ico probe, page code/styles/data; files made by the project's own code = matching a generated rule {glob, generator} (contract rights.generated or manifest generated) whose generator path exists. No sampler resources = MISSING. Every asset: origin and licence non-empty, thirdParty a boolean. Public-domain asset (publicDomain = true, e.g. a US federal document): source.url http(s) and pdBasis ≥ 20 chars (the ground for public domain), no terms needed. Other third-party asset (TTS voice, library music or sound, photo, font, 3D model, texture, …): terms quote ≥ 20 chars and http(s) terms URL, commercial = true (the terms allow an ad-supported channel). An asset made by this project: generator = a path that exists under the root or one of its parent folders. A reconstructed quote card (kind or listed kind quote-card), whoever drew it: quoteSource.who non-empty and quoteSource.url http(s) (where the quoted words come from) | 0 sounding stems without a rights entry; visual list declared; 0 listed visuals without a rights entry; 0 visuals of an unknown kind; 0 loaded picture files or font families not declared; 0 generated rules without an existing generator; 0 assets with a missing field; 0 third-party assets without terms (or public-domain source and basis) or not cleared for commercial use; ≥ 1 asset | Python + trang |
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
| A16 **(K3 mới)** | DX-A7 (K3, cảnh báo) | every sentence of out/script.json: `spoken` (the text sent to TTS) against `text` (the written sentence). Fake break = a mark that asks the TTS for a pause the written sentence does not have: ellipsis (... or …), a dash used as a pause (spaced hyphen, en or em dash, --) that the written sentence does not have, a pause tag (SSML <break>, [pause]/[beat]/[silence], (pause)), doubled punctuation (",,"), and every comma, semicolon, colon or sentence-internal full stop the spoken text carries beyond the written text (tokens with digits left out) | 0 fake break marks (REFERENCE: reported, never fails the episode) | Python |
| A17 **(K3 mới)** | DX-A7, DX-R6 (K3, cảnh báo) | voice stem, 20 ms RMS, 10 ms hop, active above −45 dBFS; each sentence of out/script.json: its voiced span (first to last active frame within [start − 0.3, end + 0.3]) and its inner pauses (inactive runs ≥ 0.25 s inside the span); gap = silence between the voiced spans of two consecutive sentences of the same scene; G = the episode's median gap. Abnormal sentence: inner pauses > 20% of its voiced span, or ≥ 1 inner pause per 5 words. Abnormal gap: < 0.10 s (sentences run together) or > max(3·G, G + 1.0 s) | PROVISIONAL: abnormal sentences ≤ 10%; abnormal gaps ≤ 10%; ≥ 1 sentence voiced (REFERENCE: reported, never fails the episode) | Python |
| A18 **(K3 mới)** | DX-A8 (K3, cảnh báo) | out/voice/takes.json: the voice of each take = (provider, voiceId, model), per take or else from the file's "voice" block (no model anywhere = MISSING); distinct voices across the takes. Truth check on the take files (final, else raw): long-term spectrum of the voiced frames (20 ms, above −45 dBFS) in 1/3-octave bands 100 Hz–8 kHz, level-normalised; for each declared voice other than the main one with ≥ 3 measured takes, the distance between its mean spectrum and the main voice's, against the 99th percentile of the same distance for random sets of main-voice takes (reported: one take alone does not separate two models, so the check reads the declared voice and measures a group) | PROVISIONAL: 1 voice (provider, voiceId, model) for the whole episode (REFERENCE: reported, never fails the episode) | Python |
| S01 *(K2 sửa)* | DX-H1 | independent re-computation of the episode model (K2: read from the episode contract, contract.json `model`): `kind` names the checker's own re-implementation (checks/py/r_model.py: "retirement-6040" = test D's 60/40 withdrawal model, "refinance-breakeven" = Episode 1: payment = P·r/(1 − (1 + r)^−n), r = annual %/1200, savings = payment(old) − payment(old − spread), break-even = ceil(cost / savings), spread for a target = smallest cut with savings ≥ cost / months); `params` its inputs; `output` the builder's model file, compared value by value. A part of the model output the kind does not re-compute is listed (not silently trusted). Contract without model.kind / output / params, or a kind without a re-implementation = MISSING | every re-computed value within max($0.50, 1e-6 relative) (money), 0.005 (rates, payments), exactly (months); 0 mismatches; 0 model parts not re-computed; ≥ 1 value compared | Python |
| S02 *(K3 sửa)* | DX-H1 | visible on-screen text (page sampler text track, every 0.1 s): the model assumptions the episode contract declares (K3: contract.json claims.assumptions [{id, pattern}], each pattern a case-insensitive regular expression; test D: "no taxes" and "no fees", the K1 regexes NO_TAX / NO_FEE), looked for in the methodology card scenes (act "method") and in the rest of the video. Contract without claims.assumptions = MISSING | every declared assumption visible in the methodology card AND visible outside it; ≥ 1 assumption declared | trang + Python |
| S03 *(K2 sửa)* | DX-H4 | sources file named by the episode contract (contract.json data.sources, e.g. data/sources.json): per raw file path, url, sha256, downloaded (ISO date), terms {quote, url}; SHA-256 recomputed from the committed file; host of each file by role vs the hosts the contract declares (data.hosts.primary / data.hosts.crosscheck; test D: pages.stern.nyu.edu / fred.stlouisfed.org). Contract without data.sources or data.hosts = MISSING | every file present with matching SHA-256, valid date, http(s) URL, terms quote ≥ 20 chars and terms URL; ≥ 1 primary file on a declared primary host; ≥ 1 cross-check file on a declared cross-check host | Python |
| S04 *(K2 sửa)* | DX-H5 | series pairs the episode contract declares (contract.json data.crosscheck[]: series, primary {file, key, column, scale}, crosscheck {file, key, column, scale}, tolerance, used); per used key \|primary − cross-check\| (after scale) vs the declared tolerance; mismatches listed in the sources file (data.sources) "mismatches" [{year\|key, series}]. Test D: annual.csv vs fred_inflation.csv (inflation) and stocks2.csv (stocks), 1928–2025. Contract without data.crosscheck = MISSING | ≥ 1 pair; every declared tolerance ≤ 0.5 (pp); every used key present in both series; every key outside tolerance listed in "mismatches" (reported, not silently resolved) | Python |
| S05 *(K2 sửa; K3.6 sửa)* | DX-H1, DX-H2 | claims the episode contract maps to model quantities (contract.json model.claims) compared with the checker's own re-computation of that quantity (r_model value(), one per model kind: e.g. "geomean:1966" retirement-6040, "maya.cut36" refinance-breakeven, "shareCostlierAtSpread:1.5:1954-01" float-vs-fixed-replay; K3.6: a month quantity, e.g. "worstStart", is compared with a claim value written "YYYY-MM" or "YYYY-MM-01" after normalisation, YYYY-MM ≡ YYYY-MM-01, any other day is not a month); the model kind's thesis invariants from model.params (test D: sameGeomean 1966/mirror within 0.01 pp); ILLUSTRATIVE flags: every claim listed in contract claims.illustrative, and every claim of a character the contract marks illustrative, carries illustrative=true in out/claims.json | ≥ 1 mapped claim; each mapped claim present and within its tolerance (0.005 pp for rates and means, exact for months after normalisation, $0.50 for money); every invariant holds; 0 claims missing their ILLUSTRATIVE flag | Python |
| S06 *(K2 sửa)* | DX-H6 | every case the episode promises to show (contract.json coverage[]: attribute "year" or "case", act, values [..] or range [a, b]): page sampler objects carrying that attribute, visible (opacity > 0.5, on frame) in frames of that act; union over the act. Test D: year, act 3, 1928–1996. Contract without coverage = MISSING | every declared value shown (e.g. 69 of 69 start years), including cases where the thesis did not hold | trang + Python |
| S07 | DX-H1, DX-H2 | claims registry out/claims.json vs what is shown and said. On screen: every number in visible text (page sampler) must sit inside a claim span (data-claim). Narration: every number in out/script.json text must equal (value+unit) the display of a claim listed for that sentence's scene. Every claim: formula; source or illustrative; historical (source) claims carry dataYear | 0 orphan numbers on screen; 0 unregistered numbers in narration; 0 claims without formula; 0 unsourced non-illustrative claims; 0 sourced claims without dataYear | trang + Python |
| S08 | DX-H2 | page sampler, every 0.1 s and every frame in ±0.5 s around each first appearance: frames where an illustrative claim span is visible (opacity > 0.5, on frame) but no ILLUSTRATIVE badge is visible; and badge lag = first frame the claim is visible − first frame a badge is visible in that scene | 0 frames without badge; badge never later than the number (lag ≤ 0 frames) | trang + Python |
| S09 *(K3.2, K3.3 sửa)* | DX-H3 | claims whose display contains "$" must declare basis nominal\|real. Screen (page sampler, K3.3): on a frame whose visible $ claims share one basis, a frame-level label (any visible on-frame text carrying that basis word, BASIS regex) covers them all; on a frame mixing bases, each $ claim needs its basis word in the same text block or within 300 px. Narration (whole episode): every basis used in the episode (the basis of each $ claim of out/claims.json) has its basis word said at least once anywhere in out/script.json; a $ number spoken in the narration that matches no claim has no known basis and counts as missing | 0 money claims without basis; 0 frames missing the on-screen basis; 0 bases used but never said in the narration | trang + Python |
| S10 *(K3.4 sửa)* | DX-I1, DX-I2 | every narration sentence (out/script.json text) and every visible on-screen text, lower-cased, against locked regex lists: ADVICE (K3.4: never/always/don't/do not count only in the imperative, at the start of a line or clause and followed by an action verb aimed at the viewer; a lone directive word or a result label does not), FORECAST, FOUR (4% as a recommendation), WE_BAD ("we/our/us" used for the viewer); required phrases "US only" and "history, not a forecast" (narration or screen) | 0 matches of ADVICE, FORECAST, FOUR, WE_BAD; both required phrases present | Python |
| S11 *(sửa)* | DX-S6 | claims with core=true. Appearances = distinct scenes where the claim is visible (page sampler) or spoken (heard by own ASR in that scene's narration window). Declared callbacks[] each need scene + distinct non-empty meaning, and must be real appearances | ≥ 1 core claim; each core claim appears in ≥ 3 distinct scenes spanning ≥ 2 acts; ≥ 3 declared callbacks with distinct meanings, all verified | trang + Python |
| S12 | DX-S7 | new number = first appearance (screen or narration) of a claim; axis-role claims (role "axis", only ever shown as axis labels/anchors per the page sampler) excluded. Scene of a new number = scene containing its first-appearance time | new numbers ≤ duration / 8 s; no scene with > 2 new numbers; 0 claims marked axis but shown outside axis labels | trang + Python |
| S13 *(K2 sửa)* | DX-S8 (sổ gu G-009) | K2 redefinition. Sentence length = words in each out/script.json sentence text (in script order). (a) Variation: coefficient of variation (population std / mean) over the sentences of ≥ 4 words: long and short sentences alternate, and fragments cannot buy the variation. (b) Flow: a staccato passage = ≥ 3 consecutive sentences of ≤ 6 words each (a single short sentence for emphasis is allowed; a string of them is choppy). Narration without numbers is never penalised | PROVISIONAL: CV (sentences ≥ 4 words) ≥ 0.35; 0 staccato passages | Python |
| S14 | DX-S10 | out/adbreaks.json times; act boundaries from out/timeline.json acts; natural silence = span where the master RMS (50 ms/10 ms) stays ≤ −40 dBFS | 2 … 3 breaks; each within ±1.0 s of a boundary between two acts (not inside cold open/ident); each inside a silence ≥ 1.0 s | Python |
| S15 | DX-S1 | out/timeline.json acts[] (id, start, end) and scenes[].act; acts contiguous and in the brief's order | order cold-open, ident, act1, act2, act3, method, outro; cold open ≤ 15 s; ident ≤ 3 s; outro ≥ 20 s; timeline total ≥ 600 s; every scene inside its act | Python |
| S16 **(K2 mới)** | DX-S3, RUBRIC H4 (sổ gu G-008) | decisive numbers = displays of the claims with decisive=true in out/claims.json or listed in contract.json claims.decisive; a decisive sentence = an out/script.json sentence whose text says one of them (numbers compared as values). It is tied to the viewer's situation when that sentence, or any sentence before it in the same scene (the story has already put the viewer with that person or scenario; sổ gu G-009: a story does not repeat the name in every sentence), names a character or a scenario the episode contract declares (characters.<k>.words, scenarios.<k>.words; whole-word match, case-insensitive). Contract without the words of its characters/scenarios = MISSING | PROVISIONAL: ≥ 1 decisive sentence; ≥ 75% of decisive sentences tied to a declared character or scenario | Python |
| R01 | DX-R1 | out/tension-map.json samples (t, cutRate, audioDensity, musicLevel, tension), peaks[], valleys[]; out/tension-map.png present. Declared curves vs measured: cut rate = cuts per 10 s window (out/transitions.json); music level = music-stem RMS dB (1 s); audio density = number of stems (voice, music, sfx, whoosh) above −45 dBFS per 1 s, 5 s moving mean. Peaks: local maximum of tension within ±10 s (5% of range slack); each act 1–3 has a peak within ±5 s of its climax (timeline acts[].climax); every peak is followed within 45 s by a declared valley that is ≥ 25% of the range lower | Pearson r ≥ 0.8 (cut rate), ≥ 0.7 (music level), ≥ 0.6 (audio density); 0 false peaks; 3 acts with a climax peak; 0 peaks without valley | Python |
| R02 | DX-R2 | change points = scene starts where the layout family (text before "/" in scenes[].layout) or the shot size (scenes[].shot / shot.size) changes, plus starts of audio-layer cues (out/cues.json cues[].t); gap between consecutive change points (0 and the end included) | longest gap ≤ 60 s | Python |
| R03 *(sửa)* | DX-R3 | decisive claims (decisive=true); each narration sentence saying one: own-ASR word run that says the value, extended over the unit words that follow it (dollars, percent, million, real, …; audit K-5). Pause measured on the voice stem (required): the first ≥ 120 ms run below −45 dBFS (20 ms RMS) that starts within [run end − 0.25 s, run end + 0.8 s], until the voice comes back for ≥ 30 ms; no such run = the voice runs on, pause 0 | ≥ 1 decisive claim; every pause ≥ 1.0 s; 0 decisive numbers not found in ASR | Python |
| R04 | DX-R4 | cuts from out/transitions.json; beats from out/tempo-map.json; a cut is on the beat if a beat is within ±1 frame; on action if the cut declares action=true and the picture moves into the cut (mean \|ΔY\| of the last 5 frames before the cut ≥ 1.5 × the outgoing shot's median) | ≥ 70% of cuts on a beat or on action | Python |
| R05 | DX-R5 | shot durations = scenes[].dur of out/timeline.json. Act 2 acceleration: act-2 scenes that start before the act-2 climax, split in three consecutive groups of equal count; group means | every shot 1.2 … 12 s (act "outro" exempt from the 12 s cap: it holds the end screen); CV = std/mean ≥ 0.4; act-2 means non-increasing and last ≤ 0.8 × first (≥ 6 scenes) | Python |
| R06 | DX-V10 (picture check of cuts) | every declared cut in out/transitions.json except dissolves: mean \|ΔY\| (luma, 1/4 scale) between the frame at the cut and the one before, vs the median of the ±10 surrounding frame pairs | ≥ 90% of cuts show a spike ≥ 3 × the surrounding median and ≥ 2 codes | Python |
| V01 *(sửa)* | DX-V12 | preprod/shotlist.json shots[]: fields size, move, moveReason (2.5D shot list: no simulated focal length, no 3D camera angle); coverage of out/timeline.json scenes (shots[].scene); storyboard (preprod/storyboard.*) and colour script (preprod/color-script.*) present | every shot has all 3 fields non-empty; moveReason ≥ 3 words; every timeline scene has ≥ 1 shot; storyboard and colour script present | Python |
| V02 *(sửa)* | DX-V1 | settled frames every 0.1 s: centre of each visible level-1 text vs the four thirds intersections (±96 px x, ±54 px y), or the vertical centre line (±48 px) when the scene declares composition "center" | ≥ 90% of level-1 samples placed | trang + Python |
| V03 *(sửa)* | DX-V3 | every frame (no camera-move exemption), every 0.2 s: ink bounding box of each visible text from the page's text layer (alpha > 64, badges included). A text travelling in or out of frame (its box moved ≥ 4 px since the object sample 0.1 s earlier) may cross the edge | all text ink of non-travelling texts inside x 96–1824, y 54–1026 (90% safe area); 0 violations | trang + Python |
| V04 *(K2 sửa)* | DX-V4, DX-X3 | characters read from the episode contract (contract.json characters: color token or hex, shape, side); page objects with that `char` every 0.1 s: main colour and main shape of each (most frequent fill/stroke, shape) and their shares; for every pair of characters seen together (\|Δx\| ≥ 20 px) the sign of their horizontal order; year axis labels (role axis-label with year) ordered left → right. Contract without characters (or a character without color/shape) = MISSING | every declared character seen; main colour = declared colour and ≥ 95% of its observations; main shape = declared shape and ≥ 95%; declared colours all differ; each pair keeps one side for the whole video, and the side the contract declares (left < centre < right) when both sides are declared; 0 time-order violations | trang + Python |
| V05 *(sửa)* | DX-V8 | camera path out/camera.json, per frame: 2.5D {t, x, y, zoom} (pan over the chart plane in page px, zoom = scale) or the legacy {t, pos, target, fovDeg, focusDist}. Speeds/accelerations normalised to frame widths (fw; 2.5D: pan / (1920/zoom) + \|d ln zoom\|). Moves as in A10, ≥ 0.5 s. Per move: ease = mean speed over the first and last 10% of the move ÷ peak; linear = speed stays within ±10% of its mean over ≥ 60% of the move; progress u from the rest position 0.6 s before to the rest position 0.6 s after; anticipation = u ≤ −0.3% before the peak-speed instant; overshoot = u peaks 0.3–8% past 1 after it and settles within 0.3%; peak \|acceleration\|. Truth check: Spearman ρ between camera speed and picture change (mean \|ΔY\| per 0.5 s window) | ≥ 5 moves; every move eased (≤ 0.4) and none linear; anticipation in ≥ 30% and overshoot in ≥ 30% of moves ≥ 1 s; no overshoot > 8%; peak \|a\| ≤ 8 fw/s²; ρ ≥ 0.3 | Python |
| V08 *(sửa)* | DX-V6 | every frame (no camera-move exemption), every 0.2 s, texts with opacity ≥ 0.95 standing still on screen (box moved < 2 px in 0.1 s; moving texts are judged by V12), on the delivered video frame: text colour = median of glyph-core pixels (glyph mask eroded 1 px), background = median of the ring 1–4 px around the ink (inside the badge for badge text); WCAG contrast | ≥ 4.5:1 for every text sample | trang + Python |
| V09 *(K2 sửa)* | DX-V4, DX-X3 | every pair of characters declared in the episode contract (contract.json characters; colours resolved from design/tokens.json): the main colour of each on screen (page sampler) simulated with Machado 2009 (severity 1) protanopia and deuteranopia, ΔE2000 between the two simulated colours; grey = WCAG relative-luminance contrast between them. Contract without characters = MISSING | every declared character seen; for every pair: ΔE2000 ≥ 20 under each simulation, grey contrast ≥ 1.5:1 | trang + Python |
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
| T1 *(K2 sửa)* | DX-A1 (sổ gu G-001, G-006) | K2 redefinition. Events = union of the declared out/sonify-events.json (bar f0, dot f, start of each line draw) and the chart events the page sampler measured with the camera frozen (every declared line sample is an event, so a line draw is one cluster); events closer than 0.15 s form one cluster; a slot = the onset of a cluster and every 0.5 s to its end. Band = the bands the episode puts its data sounds in (contract.json sonification.bandsHz, from the cue sheet; 4th-order Butterworth each, summed). Frames of 20 ms (5 ms hop). A pause of the voice = a frame where the voice stem is below −45 dBFS or ≥ 15 dB below its own maximum within ±0.3 s (gaps between syllables and words, between sentences, and where there is no voice). A slot is heard when, in some pause frame of [t − 0.10 s, t + 0.50 s], lift = 10·log10((P_son + P_rest) / P_rest) ≥ 3 dB and the data-sound band level ≥ −60 dBFS (P_son = band power of the data-sound stem "sonify", P_rest = band power of the sum of the other stems). Nothing is asked of the data sounds while the voice is sounding (L1 judges that). Truth checks: the declared bands hold ≥ 50% of the data stem's energy; the stems add up to the master in the band. Without a sonify stem the sfx stem is measured (reported) but the rule cannot pass. Contract without sonification.bandsHz = MISSING | PROVISIONAL: ≥ 60% of slots heard; ≥ 1 slot; declared bands ≥ 50% of the data stem energy; stems ~ master r ≥ 0.90; sonify stem delivered | trang + Python |
| T2 **(mới)** | DX-A2 (sổ gu G-002) | music stem; bars of 4 beats from out/tempo-map.json beats (A12 checks those beats against the music's onsets); 4-bar phrases of chroma + onset pattern (phrase_features). For each phrase: the highest cosine similarity with the 1, 2, 3 and 4 phrases before it (a loop of 1–4 phrases repeats at one of these lags). A repeat = similarity ≥ 0.90. Quiet phrases (< −50 dBFS) are left out | ≥ 8 phrases measured; repeats ≤ 5% of phrases; never 2 repeated phrases in a row | Python |
| T3 **(mới)** | DX-R6 (sổ gu G-003) | intentional silences = master spans ≤ −40 dBFS (50 ms RMS, 10 ms hop) of 0.8–1.5 s (as A09). Bed = music + sfx + whoosh (+ sonify) stems summed, 20 ms RMS, 5 ms hop. Reference = 90th percentile of the bed in [start − 0.8, start − 0.1]. Entry = from the last instant the bed is within 3 dB of the reference (searched in [start − 1.0, start + 0.3]) to the first instant after it the bed is 30 dB below the reference (or below −70 dBFS). Reported, not judged: a bed already below −60 dBFS before the silence (nothing to release), and a bed whose median inside the silence stays within 20 dB of the reference (a quiet passage, no cut to judge; A09 still counts it). Floor: master 50 ms RMS minimum inside the silence (edges 0.1 s excluded) and the room stem mean level there | every entry 150–400 ms; master ≥ −80 dBFS and room stem ≥ −75 dBFS through every silence; ≥ 1 silence | Python |
| L1 **(K2 mới)** | DX-A1, DX-A9 (sổ gu G-006) | the data sounds do not cover the voice. (a) Energy: 100 ms windows where the voice stem is active (RMS > −45 dBFS); 1–4 kHz band (4th-order Butterworth) of the voice stem and of the data-sound stem "sonify"; ratio = 10·log10(P_voice / P_son) per window, over the windows where the data sound is present in the band (≥ −80 dBFS); the 10th percentile of those ratios. (b) Words: own ASR (as asr_master: sentence clips, small.en, two-pass) of the sum of all stems and of the sum of all stems but sonify; key words of each sentence as A14 (numbers, names, defined terms + out/terms.json); a key word heard without the data sounds and missed with them is lost. Needs the sonify stem (MISSING without it: the data sounds must be separable to be judged) | PROVISIONAL: 10th-percentile voice/data ratio in 1–4 kHz ≥ 20 dB (no window with a data sound = pass); 0 key words lost to the data sounds | Python |
| REG *(K3 sửa)* | CH §5, §4 khâu 3 (cổng hồi quy) | baseline = the checker's report of the previous version of the episode (--baseline). A rule is comparable when it is in both reports and its definition is unchanged: same fingerprint (sha256 of measure + threshold), or, for a baseline without fingerprints, the same threshold text and not in CHANGED_SINCE[baseline lock]. Regression = comparable rule PASS in the baseline and not PASS now (FAIL, MISSING or ERROR). K3: only a regression of a BLOCK (CHẶN) rule counts; regressions of MAJOR and REFERENCE rules are listed with their tier | 0 regressions of BLOCK rules (a --first run has nothing to compare and passes; no baseline and no --first = MISSING) | Python |

## Khoá

`checks/LOCK` là SHA-256 của danh sách `sha256  đường-dẫn` của mọi file trong `checks/`, trừ `LOCK` và `__pycache__`. Danh sách sắp xếp theo `LC_ALL=C`, mỗi dòng kết thúc bằng `\n`.

```
cd checks && find . -type f ! -name LOCK ! -path '*/__pycache__/*' | LC_ALL=C sort | xargs sha256sum | sha256sum
```
