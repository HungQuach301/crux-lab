# Tập 2 · C5 · tiếng (luồng A)

Bản mix cuối trên `animatic/timing.json` (tổng 585.6000 s, SHA-256 `abd2eda78e8f…`). File wav không commit (`.gitignore`); SHA-256 và kích thước trong `manifest.json`. Dựng lại: `python3 episodes/ep002/audio_src/takes.py && python3 episodes/ep002/audio_src/events.py && python3 episodes/ep002/audio_src/mix.py` (seed cố định).

## Đo trên master (`master.wav`, trước AAC)

- Âm lượng tích hợp **-14.1 LUFS** (đích −14, A01 ±1) · true peak **-1.5 dBTP** (trần −1,5; A02 ≤ −1,0) · LRA 3.1 LU.
- Limiter true peak (4× oversample, look-ahead 5 ms): gain nhỏ nhất -2.42 dB, dưới −1 dB ở 0.26% mẫu.
- Stem (dBFS RMS cả tập): voice -17.74, music -36.46, sonify -46.31, room -66.32; sfx/whoosh im (bảng S2 không có lớp sfx). Tổng stem = master (sai lệch lớn nhất 0.0e+00).

## Lời ưu tiên (G-006): duck dưới lời

- Nhạc (kiểu C của Tập 1, G-016 · chọn) đặt **19.95 dB dưới lời** trên các cửa sổ 100 ms có lời (cách đo A07; đích 20 dB như Tập 1); dải 1–4 kHz của nhạc duck thêm 13 dB khi có lời (nhìn trước 80 ms, thả 350 ms).
- Tiếng dữ liệu (S2 "minimal", G-005 · chọn): −16 dB dưới RMS lời trước side-chain; khi có lời thêm −8 dB và bỏ 95% dải 1–4 kHz; nốt rơi vào lời được dời vào khe âm tiết (−60…+120 ms): 335/453 nốt, trung vị 56.8 ms. Không bao giờ nâng mức. Năng lượng stem sonify trong dải khai báo (60–270 Hz + 4,5–7 kHz) = 97.4%. Nhạc nhường −10 dB trong hai dải đó khi tiếng dữ liệu kêu.
- Khoảng lặng (G-003): 7 khe lời ở các bước ngoặt (+ điểm quảng cáo): nền nhả τ 90 ms, room +8 dB, trở lại 200 ms — 26.15 s (0.85 s); 176.00 s (0.95 s); 222.82 s (1.71 s, quảng cáo); 321.04 s (1.17 s); 381.94 s (1.44 s, quảng cáo); 505.21 s (0.96 s); 565.91 s (1.01 s). Các cú cắt cảnh khác: nhạc phồng +3 dB.

## Tiếng dữ liệu: chọn sự kiện (cách S2 của Tập 1)

63 hành động dữ liệu (`out/sonify-events.json`, `work/audio/son-plan.json`, lý do trong `audio_src/events.py`), neo vào hình (`animatic/src/anchors`) và giải lại trên timing.json hiện tại: lãi suất vượt 9% (đường thả nổi cắt đường 9% = `line` dao động; các lần leo trên 9% ở S06, S07, S08 tới 19,3% = `line` đi lên); khởi đầu thấp hơn (mỗi lần lật điểm xuất phát = `dot`, cao độ theo độ cao); đệm tiết kiệm (hũ đầy = `bar` mọc, hũ cạn = `line` đi xuống ở S06.3, S07.5, S08.4); ô kết quả đỏ (khung chạy thả ô = `roll` tăng tốc theo dáng lãi T-bill; ô đỏ cao và to hơn; tỉ lệ đỏ 28,4/3,5/20,4/10,5/31,3/57,9/72,9% = `bar` cao độ theo tỉ lệ); chồng lãi và khối "đắt hơn" (S04, S08) = `bar`. Nhãn, số dạng chữ, thẻ, cú nhúng và thẻ phương pháp không có tiếng (S2 không có lớp sfx).

## Lời và ký tự ElevenLabs

- Eric `cjVigY5qzO86Huf0OWal`, `eleven_v3`, mặc định (không voice_settings, không speed, không thẻ ngắt), mỗi cảnh một lần gọi, thẻ cảm xúc thưa như kịch bản.
- 9 cảnh dùng lại take C2 (chữ trùng kịch bản, cùng giọng/mô hình/thiết lập). Sinh lại ở C5 vì kịch bản đổi (S08.6 "in dollars of the day"; v5.2: S04.4, S09.5, S09.6, S10.3 "from 1954 to 1980"), mỗi cảnh seed 1, seed 2 chỉ khi ASR thiếu từ khoá:
  - S04: seed 1 316 ký tự; dùng S04.9519444f.seed1.mp3 (49.32 s), ASR thiếu 0.
  - S08: seed 1 402 ký tự; dùng S08.d97e2064.seed1.mp3 (59.95 s), ASR thiếu 0.
  - S09: seed 1 365 ký tự, seed 2 365 ký tự; dùng S09.f5608718.seed2.mp3 (54.60 s), ASR thiếu 0.
  - S10: seed 1 379 ký tự; dùng S10.f5caf058.seed1.mp3 (64.52 s), ASR thiếu 0.
- **Ký tự ElevenLabs dùng ở C5: 1827.**
- Hạ nền cục bộ dưới một từ (A14 trên master nghe "Lea" thay "Leah" ở S02.2, stem lời một mình nghe đúng): S02.2 "leah" 39.80–40.56 s nhạc + tiếng dữ liệu -8 dB (dốc 80 ms; không nâng lời).

## Luật âm thanh (bản sao checks origin/main, LOCK `2fcc9fcc…`)

| Luật | Kết quả | Số đo |
|---|---|---|
| A01 (BLOCK) | PASS | integrated LUFS -14.1 |
| A02 (BLOCK) | PASS | true peak dBTP -1.4 |
| A03 (REFERENCE) | FAIL | LRA LU 3.1 |
| A04 (BLOCK) | PASS | samples at full scale 0 |
| A05 (BLOCK) | PASS | mean phase correlation 0.980468; windows r<0 (%) 0.0 |
| A06 (BLOCK) | PASS | mono − stereo LU 0.0; voice-band loss dB 0.002041 |
| A07 (REFERENCE) | PASS | voice − music dB 19.954178 |
| A08 (REFERENCE) | PASS | onsets measured 76; median 1-4 kHz drop dB 6.18919; median band-limited excess dB 6.173895 |
| A09 (REFERENCE) | PASS | silences 0.8-1.5 s 7 |
| A10 (REFERENCE) | FAIL | camera moves 0 |
| A11 (REFERENCE) | FAIL | events measured 0; Pearson pan~x None |
| A12 (REFERENCE) | PASS | accents 6; accents on a cut (%) 100.0; accents confirmed by onset (%) 100.0; beats confirmed by onset (%) 97.217235 |
| A13 (REFERENCE) | PASS | takes 13; max /stretch-1/ 0.0 |
| A14 (BLOCK) | PASS | key words 151; key words missing 0 |
| A15 (REFERENCE) | FAIL | wpm act cold-open 158.878885; wpm act act1 162.492431; wpm act act2 165.93391; wpm act act3 160.32252; wpm act method 190.709046; wpm act outro 182.286303; sentences > 175 wpm 26 |
| A16 (REFERENCE) | FAIL | sentences 67; fake break marks 15; sentences with a fake break 15 |
| A17 (REFERENCE) | FAIL | voiced sentences 67; abnormal sentences share 0.089552; abnormal gaps share 0.111111 |
| A18 (MAJOR) | PASS | takes 13; distinct voices (provider, voiceId, model) 1 |
| S14 (REFERENCE) | PASS | ad breaks 2; breaks off an act boundary 0; breaks without ≥1 s silence 0 |
| R01 (REFERENCE) | PASS | r cut rate 1.0; r music level 0.97296; r audio density 0.965784; false peaks 0; acts with climax peak 3; peaks without valley 0 |
| R02 (REFERENCE) | FAIL | longest stretch without a break s 67.333 |
| R03 (REFERENCE) | FAIL | decisive claims 3; shortest pause s 0.24; pauses < 1.0 s 3; decisive numbers not heard 0 |
| R04 (REFERENCE) | PASS | cuts on beat/action (%) 100.0 |
| T1 (REFERENCE) | PASS | slots measured 208; share of slots heard in a pause 0.817308; declared bands share of data-stem energy 0.984698; stems ~ master in band r 0.999992; data sounds delivered as their o |
| T2 (REFERENCE) | FAIL | phrases measured 71; repeated phrases (%) 64.788732; longest run of repeated phrases 14 |
| T3 (REFERENCE) | FAIL | silences measured 7; entries outside 150–400 ms 3; silences without a room-tone floor 0 |
| L1 (MAJOR) | PASS | voice-active windows 4420; voice/data 1–4 kHz ratio, 10th percentile (dB) 27.690484; key words lost to the data sounds 0 |

Bảng trên: chạy trên `out/video.mp4` thật của P (1080p, tiếng = master mặc định, −14,1 LUFS đo lại từ video). A10/A11 (tham khảo): không có chuyển động máy quay và không có sự kiện sfx (bảng S2). A15/A16: tốc độ đọc và dấu ngắt trong chữ TTS (kịch bản). Mọi luật CHẶN về tiếng đều đạt (A14: 0/151 từ khoá thiếu trên master). T2 (tham khảo): ostinato kiểu C dùng chung một âm giai nên chroma của các câu 4 ô giống nhau ≥ 0,90, dù chuỗi hợp âm không lặp; Tập 1 kiểu C đo 29%. Gu C đã khoá nên không đổi. T3 (tham khảo): lối vào khoảng lặng chậm vì pad tự tắt dần (1,3 s trước khoảng lặng không có nốt mới), giống Tập 1. A03 LRA (tham khảo): thấp vì lời được ưu tiên, giống Tập 1. A17/R02/R03 đo lời và nhịp kịch bản, không phụ thuộc mix.

## Bản nhạc thay thế (`--music alt`, chủ dự án C6: cùng kiểu C, ít lặp hơn)

Cùng nhạc cụ, cùng nhịp, cùng âm giai; mỗi ô tự chọn nhịp thump, bass, ostinato từ tập rộng hơn (không trùng ô trước), thỉnh thoảng có ô "thở" ở cuối câu nhạc (không thump/bass), hợp âm chọn theo độ tương phản. Lời, tiếng dữ liệu, duck, hạ nền "Leah", khoảng lặng và chuỗi master giữ nguyên. Master-alt: -14.1 LUFS, true peak -1.5 dBTP; nhạc 19.96 dB dưới lời. File: `stems-alt/{voice,music-alt,sonify,room}.wav` (tổng = `master-alt.wav`), SHA-256 ở `manifest.json` → `alt`. Mặc định vẫn là bản hiện tại.
- **T2 (câu nhạc 4 ô lặp lại): mặc định 64,8%, thay thế 19,7%** (Tập 1 kiểu C: 29%). Luật của bản thay thế: trên video thật của P (hình P + master-alt): A01 A02 A14 L1 S14 đạt; trên video tạm thêm A04-A07 A09 A12 T1 đạt, T3 2 lối vào chậm, A08 (tham khảo) 4,4 dB < 6.
- So sánh cho chủ dự án: `review-c6/music-ab.m4a` (57 s): hai đoạn, mỗi đoạn A = mặc định rồi B = thay thế; một tiếng bíp trước A, hai tiếng trước B. Đoạn 1 = S02.2 (có chữ "Leah" và chỗ hạ nền), đoạn 2 = S07.5 (hai lần chạy, tiếng dữ liệu, nhịp đầy). Chỉ mục: `review-c6/music-ab.json`.
