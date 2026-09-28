# A-M0: mẫu 10 giây chạy đầu cuối

Mẫu thử một câu lời trên dữ liệu thật: đường lãi suất 30 năm cố định hằng tuần (FRED `MORTGAGE30US`, 1971–2026) được vẽ ra, và đỉnh 18,63% (tuần 1981-10-09) hiện đúng lúc lời đọc con số đó. Mục đích là chạy hết chuỗi công cụ trong bố cục crux-lab rồi chạy bộ luật khoá lên kết quả. Đây không phải cảnh của tập.

Câu lời: *"Since 1971, the 30-year fixed rate peaked at 18.63% in 1981."*

## Chạy lại

```
export NODE_PATH=$(npm root -g) PYTHONDONTWRITEBYTECODE=1
S=episodes/ep001/m0-sample
EP_ROOT=$PWD/$S python3 toolkit/voice/d_el_voice.py        # lời: ElevenLabs Eric eleven_v3, dự phòng multilingual_v2 (take có sẵn thì dùng lại)
node $S/build.js                                            # file hợp đồng + dữ liệu trang dựng
node toolkit/render/render.js $S                            # dựng 2D → work/picture.mp4, out/camera.json
EP_ROOT=$PWD/$S node toolkit/finish/m3-glue.js pre          # tempo map, transitions, phụ đề, mô tả, cues, physical.json
node toolkit/audio/m3-sonify-events.js $S                   # sự kiện âm thanh theo dữ liệu, đọc từ trạng thái trang
SONIFY_GAIN_DB=10 bash toolkit/finish/m3-finish.sh $S       # sfx events, âm thanh + stem, mix, master, mux, bản xem trước
bash checks/run.sh $S --first                               # bộ luật khoá (không sửa gì trong checks/)
```

## Kết quả

| Bước | Kết quả |
|---|---|
| Lời | 8 lượt gọi, **504 ký tự** ElevenLabs. Take chọn: `eleven_v3` take 2, 7,52 s, không giãn thời gian. 4 lượt dự phòng `multilingual_v2` phát sinh vì hàm so khớp của bên dựng đọc sai cách ASR tách "18" ".63" "%". Đã sửa hàm (`toolkit/voice/keywords.py`) rồi chọn lại trên các take đã có, không tốn thêm ký tự. |
| Dựng 2D | 300 khung, 8 khung phụ mỗi khung, 4 worker: **115–120 s máy cho 10 s phim** (khoảng 12 s máy cho 1 s phim). Ước cho phim 10 phút: khoảng 2 giờ máy. |
| Âm thanh | 6 stem (voice, music, sfx, whoosh, room, **sonify**). Master −14,0 LUFS, true peak −1,7 dBTP. |
| Master | `out/video.mp4` (không commit, 25 MB), SHA-256 `82ba6767b35660de440150eecf3a12c9a37b3b5dade5ffc0126d7d318df8be70`. Bản xem trước: `work/preview.mp4` (3,3 MB). |
| Kiểm | LOCK `b97bfc6b…`: **41 PASS · 29 FAIL · 5 MISSING · 0 ERROR** (`out/checks/report.md`). |

### Luật áp dụng được cho mẫu

**Đạt (41):** F01–F06, F08, F09, A01, A02, A04–A07, A13, A14, S07–S09, R02, V01–V03, V08, V11–V13, C01–C07, C10–C15, REG.

**Trượt thật (3), mang sang M1:**

| Luật | Số đo | Nguyên nhân, cách xử lý ở tập |
|---|---|---|
| T1 | 3/4 cửa sổ nghe thấy; cửa sổ 1,4 s nổi **0,83 dB**, cần ≥ 1 dB (trong cửa sổ số được đọc) | Tiếng dữ liệu vào cùng lúc với chữ "Since 1971". Xem mục "Âm thanh theo dữ liệu" dưới đây. |
| R03 | khoảng lặng sau "18.63%" **0,54 s**, cần ≥ 1,0 s | Con số quyết định nằm giữa câu, "in 1981" theo ngay sau. Ở kịch bản: đặt số quyết định ở **cuối câu**. Không cắt take ra để chèn khoảng lặng (A13 cấm giãn). |
| A15 | **149,1 wpm**, cần 150–160 | Dấu "..." trong chữ gửi TTS làm chậm. Ở tập: bớt "...", đo wpm từng câu trước khi dựng. |

**Không áp được cho mẫu 10 giây** (cần phim ≥ 10 phút, nhiều cảnh, nhiều cú máy, đủ hồi hoặc mô hình của tập): F07, F10, A03, A08–A12, S02, S06, S10–S15, R01, R04–R06, V04, V05, V09, V10, T2, T3. MISSING: S01, S03–S05 (luật gắn mô hình và dữ liệu bài D), P01 (thumbnail).

Vòng 1 còn trượt C04 (55 khung): đường có trục nhưng mới có 1 mốc số (chỉ 1971). Vòng 2 cho cả hai mốc hiện ngay khi đường xuất hiện, và C04 đạt.

## Âm thanh theo dữ liệu: đo trước cho sổ gu G-001

Bên dựng tự đo độ nổi ở 1,5–8 kHz (cùng cửa sổ 0,15 s như T1) trên mẫu này, với ba mức tăng của stem `sonify`:

| Mức tăng | sonify so với lời (RMS toàn dải) | Độ nổi khi đang có lời | Độ nổi lúc lời nghỉ |
|---|---|---|---|
| 0 dB | −16 dB | 0,2–1,8 dB | 7,7–18 dB |
| +6 dB | −10 dB | 0,6–4,8 dB | 13–24 dB |
| +10 dB (đã dùng) | −6 dB | 1,4–7,9 dB | 17–28 dB |

Kết luận cho M1:
- Khi lời đang đọc, năng lượng 1,5–8 kHz của lời rất lớn (−16 đến −30 dBFS trong dải). Muốn tiếng dữ liệu nổi ≥ 3 dB giữa lúc lời đang đọc, nó phải to gần bằng lời. Điều đó dễ va với H8 "không át lời".
- Cách dựng khả thi là **biên đạo**: cho biểu đồ biến động chủ yếu ở chỗ lời nghỉ (hình đi trước lời, khoảng thở sau số). Nếu phải biến động khi đang có lời thì rơi vào cửa sổ số được đọc, nơi ngưỡng là 1 dB.
- **Chủ dự án nghe trên loa điện thoại (2026-09-28):** nghe thấy tiếng riêng của cột, đường, điểm, nhưng âm sắc chưa phù hợp; lời rõ nhưng vẫn bị tiếng dữ liệu lấn; không tăng +10 dB (sổ gu G-005, G-006). Thử mù ba bảng âm: `palettes.py` → `../review-m1/sonify-S1/S2/S3.mp4`.
- Bài D hạ lớp này −10 dB dưới lời và trộn vào `sfx`. Toolkit nay tách thành stem riêng và bỏ việc hạ đó (`toolkit/README.md`).
