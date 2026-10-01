# Tập 2 · C5 · tiếng (luồng A)

Bản mix cuối trên `animatic/timing.json` (tổng 589.6333 s, SHA-256 `41a909724196…`). File wav không commit (`.gitignore`); SHA-256 và kích thước trong `manifest.json`. Dựng lại: `python3 episodes/ep002/audio_src/takes.py && python3 episodes/ep002/audio_src/events.py && python3 episodes/ep002/audio_src/mix.py` (seed cố định).

## Đo trên master (`master.wav`, trước AAC)

- Âm lượng tích hợp **-14.1 LUFS** (đích −14, A01 ±1) · true peak **-1.5 dBTP** (trần −1,5; A02 ≤ −1,0) · LRA 3.2 LU.
- Limiter true peak (4× oversample, look-ahead 5 ms): gain nhỏ nhất -2.22 dB, dưới −1 dB ở 0.25% mẫu.
- Stem (dBFS RMS cả tập): voice -17.78, music -36.45, sonify -46.31, room -66.31; sfx/whoosh im (bảng S2 không có lớp sfx). Tổng stem = master (sai lệch lớn nhất 0.0e+00).

## Lời ưu tiên (G-006): duck dưới lời

- Nhạc (kiểu C của Tập 1, G-016 · chọn) đặt **19.97 dB dưới lời** trên các cửa sổ 100 ms có lời (cách đo A07; đích 20 dB như Tập 1); dải 1–4 kHz của nhạc duck thêm 13 dB khi có lời (nhìn trước 80 ms, thả 350 ms).
- Tiếng dữ liệu (S2 "minimal", G-005 · chọn): −16 dB dưới RMS lời trước side-chain; khi có lời thêm −8 dB và bỏ 95% dải 1–4 kHz; nốt rơi vào lời được dời vào khe âm tiết (−60…+120 ms): 342/455 nốt, trung vị 57.75 ms. Không bao giờ nâng mức. Năng lượng stem sonify trong dải khai báo (60–270 Hz + 4,5–7 kHz) = 97.3%. Nhạc nhường −10 dB trong hai dải đó khi tiếng dữ liệu kêu.
- Khoảng lặng (G-003): 7 khe lời ở các bước ngoặt (+ điểm quảng cáo): nền nhả τ 90 ms, room +8 dB, trở lại 200 ms — 26.15 s (0.85 s); 174.31 s (1.04 s); 221.22 s (1.71 s, quảng cáo); 319.44 s (1.17 s); 380.33 s (1.42 s, quảng cáo); 509.06 s (1.14 s); 569.94 s (1.01 s). Các cú cắt cảnh khác: nhạc phồng +3 dB.

## Tiếng dữ liệu: chọn sự kiện (cách S2 của Tập 1)

63 hành động dữ liệu (`out/sonify-events.json`, `work/audio/son-plan.json`, lý do trong `audio_src/events.py`), neo vào hình (`animatic/src/anchors`) và giải lại trên timing.json hiện tại: lãi suất vượt 9% (đường thả nổi cắt đường 9% = `line` dao động; các lần leo trên 9% ở S06, S07, S08 tới 19,3% = `line` đi lên); khởi đầu thấp hơn (mỗi lần lật điểm xuất phát = `dot`, cao độ theo độ cao); đệm tiết kiệm (hũ đầy = `bar` mọc, hũ cạn = `line` đi xuống ở S06.3, S07.5, S08.4); ô kết quả đỏ (khung chạy thả ô = `roll` tăng tốc theo dáng lãi T-bill; ô đỏ cao và to hơn; tỉ lệ đỏ 28,4/3,5/20,4/10,5/31,3/57,9/72,9% = `bar` cao độ theo tỉ lệ); chồng lãi và khối "đắt hơn" (S04, S08) = `bar`. Nhãn, số dạng chữ, thẻ, cú nhúng và thẻ phương pháp không có tiếng (S2 không có lớp sfx).

## Lời và ký tự ElevenLabs

- Eric `cjVigY5qzO86Huf0OWal`, `eleven_v3`, mặc định (không voice_settings, không speed, không thẻ ngắt), mỗi cảnh một lần gọi, thẻ cảm xúc thưa như kịch bản.
- 12 cảnh dùng lại take C2 (chữ trùng kịch bản, cùng giọng/mô hình/thiết lập). **S08 sinh lại ở C5** vì S08.6 đổi chữ ("in dollars of the day"): seed 1, **402 ký tự EL** (C5 tổng), ASR 0 từ khoá thiếu. Take mới S08.d97e2064.seed1.mp3 dài 59.951 s (cũ 55,171 s): cảnh S08 dài hơn ~4,8 s; P đặt pad S08 = 1,25 s để khe S08.8→S09.1 (điểm quảng cáo 2) ≥ 1 s im.
- S09: ASR nghe "1954 -1980"; bộ đọc số của luật đọc dấu gạch thành dấu trừ, nên "1980" bị tính thiếu (giọng đọc đúng; seed 2 ở C2 cho cùng kết quả). Không sinh lại: nguyên nhân là dạng chữ "1954-to-1980" (việc A14 của P-ep002).

## Luật âm thanh (bản sao checks origin/main, LOCK `2fcc9fcc…`)

| Luật | Kết quả | Số đo |
|---|---|---|
| A01 (BLOCK) | PASS | integrated LUFS -14.1 |
| A02 (BLOCK) | PASS | true peak dBTP -1.4 |
| A03 (REFERENCE) | FAIL | LRA LU 3.2 |
| A04 (BLOCK) | PASS | samples at full scale 0 |
| A05 (BLOCK) | PASS | mean phase correlation 0.980571; windows r<0 (%) 0.0 |
| A06 (BLOCK) | PASS | mono − stereo LU 0.0; voice-band loss dB 0.002099 |
| A07 (REFERENCE) | PASS | voice − music dB 19.97398 |
| A08 (REFERENCE) | PASS | onsets measured 78; median 1-4 kHz drop dB 6.1045; median band-limited excess dB 5.424217 |
| A09 (REFERENCE) | PASS | silences 0.8-1.5 s 7 |
| A12 (REFERENCE) | PASS | accents 6; accents on a cut (%) 100.0; accents confirmed by onset (%) 100.0; beats confirmed by onset (%) 97.939068 |
| A13 (REFERENCE) | PASS | takes 13; max /stretch-1/ 0.0 |
| A14 (BLOCK) | FAIL | key words 151; key words missing 6 |
| A17 (REFERENCE) | FAIL | voiced sentences 67; abnormal sentences share 0.119403; abnormal gaps share 0.111111 |
| A18 (MAJOR) | PASS | takes 13; distinct voices (provider, voiceId, model) 1 |
| S14 (REFERENCE) | PASS | ad breaks 2; breaks off an act boundary 0; breaks without ≥1 s silence 0 |
| R02 (REFERENCE) | FAIL | longest stretch without a break s 67.1 |
| R03 (REFERENCE) | FAIL | decisive claims 3; shortest pause s 0.0; pauses < 1.0 s 3; decisive numbers not heard 0 |
| R04 (REFERENCE) | PASS | cuts on beat/action (%) 100.0 |
| T1 (REFERENCE) | PASS | slots measured 208; share of slots heard in a pause 0.841346; declared bands share of data-stem energy 0.984318; stems ~ master in band r 0.999992; data sounds delivered as their o |
| T2 (REFERENCE) | FAIL | phrases measured 68; repeated phrases (%) 45.588235; longest run of repeated phrases 12 |
| T3 (REFERENCE) | FAIL | silences measured 7; entries outside 150–400 ms 4; silences without a room-tone floor 0 |
| L1 (MAJOR) | PASS | voice-active windows 4401; voice/data 1–4 kHz ratio, 10th percentile (dB) 28.006475; key words lost to the data sounds 0 |

Bản ghi: video tạm = nền màu + master (AAC 320k) chỉ để luật đọc tiếng chạy; P mux bản thật rồi chạy lại. A14: "1980" ×3 (S09.5, S09.6, S10.3: ASR viết "1954 -1980", bộ đọc số hiểu là −1980), "1" ở S04.4 ("minus 1 point" → −1), "$9,472" ở S09.5 (cả stem lời một mình cũng nghe 9,407: lỗi take/ASR, không phải mix), "Leah" ở S02.2 (chỉ trên master; stem lời đạt; L1: 0 từ mất vì tiếng dữ liệu). T2 (tham khảo): nhạc kiểu C có ostinato cùng âm giai nên chroma 4 ô giống nhau ≥ 0,90 dù chuỗi hợp âm không lặp (Tập 1 kiểu C: 29%). T3 (tham khảo): 4 lối vào ngoài 150–400 ms (pad tự tắt dần trước khoảng lặng vì không có nốt mới 1,3 s trước, như Tập 1). A03 LRA 3,2 (tham khảo; lời ưu tiên, như Tập 1). A17/R02/R03 đo lời và nhịp kịch bản, không do mix.
