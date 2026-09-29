# RIGHTS — Sổ quyền tài sản

Mọi tài sản đi vào một tập (dữ liệu, giọng, nhạc, SFX, font, hình, tham chiếu) có một dòng ở đây: nguồn, giấy phép (trích nguyên câu + link), phạm vi dùng, ghi công. Tài sản chưa có giấy phép trích nguyên văn thì **chưa được dùng trong bản phát hành** (lỗi L1 Chặn).

Phạm vi: **YT** = kênh YouTube có quảng cáo; **DL** = tải lại trong repo public.

| Mã | Tài sản | Loại | Nguồn/URL | Giấy phép (trích nguyên câu + link) | Phạm vi | Ghi công | Ngày |
|---|---|---|---|---|---|---|---|
| D-FRED-1 | MORTGAGE30US (Freddie Mac PMMS, 30 năm cố định, tuần) | Dữ liệu | https://fred.stlouisfed.org/series/MORTGAGE30US | FRED: "Copyrighted: Citation required … you may use these data series with proper attribution of the source and acknowledgment that you obtained the data from FRED" — https://fred.stlouisfed.org/legal/ ; cấm: "Redistribute any third party's proprietary content … for commercial use without first obtaining express written permission" | YT: hiển thị số và biểu đồ kèm ghi nguồn. DL: **không** (tải lại bằng `fetch.py`, E1-A2) | "Source: Freddie Mac via FRED" | 2026-09-28 |
| D-FRED-2 | OBMMIC30YF (Optimal Blue, đối chiếu) | Dữ liệu | https://fred.stlouisfed.org/series/OBMMIC30YF | Như D-FRED-1 | Chỉ đối chiếu nội bộ; không hiển thị | — | 2026-09-28 |
| D-HMDA | HMDA 2018–2025 (chi phí vay lại) | Dữ liệu | https://ffiec.cfpb.gov/ | "Information created by the CFPB is in the public domain and you may reproduce, publish, or otherwise use it without the Bureau's permission. Please consider appropriate citation to the Bureau as the source." — consumerfinance.gov (`episodes/ep001/data/hmda-sources.json`) | YT, DL | "Source: CFPB HMDA" | 2026-09-28 |
| D-FHFA | Hạn mức khoản vay chuẩn 2026 ($832,750) | Dữ liệu | fhfa.gov (bị proxy chặn; chủ dự án xác minh) | Chưa trích nguyên văn (fhfa.gov bị chặn) | YT (một con số, có ghi nguồn) | "Source: FHFA" | 2026-09-29 |
| V-ERIC | Giọng "Eric" (ElevenLabs premade, voice_id `cjVigY5qzO86Huf0OWal`) — **giọng tạm** Tập 1 bản cũ | Giọng TTS | ElevenLabs | "All paid plans include a commercial license, provided you're not using Beta Services." — https://help.elevenlabs.io/hc/en-us/articles/13313564601361 (trích qua Cine Lab RIGHTS.md, 2026-09-27). `eleven_v3` GA từ 02/02/2026. | YT dự kiến được, với gói trả phí; chờ chọn giọng cuối ở C3 | Chưa xác định | 2026-09-29 |
| F-INTER | Inter (400/600/700, latin) | Font | `toolkit/render/fonts/` (gói @fontsource/inter) | SIL Open Font License 1.1 — **chưa trích nguyên văn**; trích trước C5 | YT, DL | — | 2026-09-28 |
| A-MUSIC | Nhạc và tiếng dữ liệu (bảng âm S2) sinh bằng mã | Âm | `toolkit/audio/d_m2_audio.py`, `sonify_palettes.py` | Do dự án tự sinh; không mẫu bên thứ ba | YT, DL | — | 2026-09-28 |

## Tham chiếu (chỉ để xem; KHÔNG dùng trong tập)

| Mã | Tài sản | Nguồn | Được làm | Không được làm |
|---|---|---|---|---|
| REF-VOX | *How the US made affordable homes illegal* (Vox, 2021) | https://www.youtube.com/watch?v=0Flsg_mzG-M | Xem công khai; mô tả bằng lời kèm mốc thời gian | Tải, trích khung/âm/đoạn, sao chép thiết kế hay câu chữ |
| REF-3B1B | *Bayes theorem, the geometry of changing beliefs* (3Blue1Brown, 2019) | https://www.youtube.com/watch?v=HZGCoVF3YvM | Như trên | Như trên |
| REF-WSJ | *Mortgage Rates Hit 7%: What's Next for the Housing Market?* (WSJ News, 2026) | https://www.youtube.com/watch?v=lsOD1CHkWrY | Như trên | Như trên |
