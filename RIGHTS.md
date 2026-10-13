# RIGHTS — Sổ quyền tài sản

Mọi tài sản đi vào một tập (dữ liệu, giọng, nhạc, SFX, font, hình, tham chiếu) có một dòng ở đây: nguồn, giấy phép (trích nguyên câu + link), phạm vi dùng, ghi công. Tài sản chưa có giấy phép trích nguyên văn thì **chưa được dùng trong bản phát hành** (lỗi L1 Chặn).

Phạm vi: **YT** = kênh YouTube có quảng cáo; **DL** = tải lại trong repo public.

| Mã | Tài sản | Loại | Nguồn/URL | Giấy phép (trích nguyên câu + link) | Phạm vi | Ghi công | Ngày |
|---|---|---|---|---|---|---|---|
| D-FRED-1 | MORTGAGE30US (Freddie Mac PMMS, 30 năm cố định, tuần) | Dữ liệu | https://fred.stlouisfed.org/series/MORTGAGE30US | FRED: "Copyrighted: Citation required … you may use these data series with proper attribution of the source and acknowledgment that you obtained the data from FRED" — https://fred.stlouisfed.org/legal/ ; cấm: "Redistribute any third party's proprietary content … for commercial use without first obtaining express written permission" | YT: hiển thị số và biểu đồ kèm ghi nguồn. DL: **không** (tải lại bằng `fetch.py`, E1-A2) | "Source: Freddie Mac via FRED" | 2026-09-28 |
| D-FRED-2 | OBMMIC30YF (Optimal Blue, đối chiếu) | Dữ liệu | https://fred.stlouisfed.org/series/OBMMIC30YF | Như D-FRED-1 | Chỉ đối chiếu nội bộ; không hiển thị | — | 2026-09-28 |
| D-HMDA | HMDA 2018–2025 (chi phí vay lại) | Dữ liệu | https://ffiec.cfpb.gov/ | "Information created by the CFPB is in the public domain and you may reproduce, publish, or otherwise use it without the Bureau's permission. Please consider appropriate citation to the Bureau as the source." — consumerfinance.gov (`episodes/ep001/data/hmda-sources.json`) | YT, DL | "Source: CFPB HMDA" | 2026-09-28 |
| D-FHFA | Hạn mức khoản vay chuẩn 2026 ($832,750) | Dữ liệu | fhfa.gov (bị proxy chặn; chủ dự án xác minh) | Chưa trích nguyên văn (fhfa.gov bị chặn) | YT (một con số, có ghi nguồn) | "Source: FHFA" | 2026-09-29 |
| V-ERIC | Giọng "Eric" (ElevenLabs premade, voice_id `cjVigY5qzO86Huf0OWal`), model `eleven_v3` mặc định — **giọng của Tập 1** (chủ dự án chọn mù ở C3; kiểu sinh theo cảnh + thẻ cảm xúc thưa ở C4) | Giọng TTS | ElevenLabs | ElevenLabs Terms of Service ("Last Updated: 31 March 2026"; áp dụng cho người cư trú ngoài EEA, Thuỵ Sĩ, UK), https://elevenlabs.io/terms-of-use: "(c) Use Restrictions. Your access to and use of the Services and your use of any Output (defined below) must comply with these Terms. Without limiting the forgoing: (i) if you access or use our Services free of charge (such a user, a “ Free User ”), you may only use the Services for non-commercial purposes; (ii) if you access or use our Services through a paid subscription plan (such a user, a “ Paid User ”), you may use the Services for commercial purposes, but in either case, your access and use of the Services and any Output must still comply with the Prohibited Use Policy." · "Except as expressly set forth herein, as between you and ElevenLabs, you retain all rights in and to your Output." — Billing, https://elevenlabs.io/docs/overview/administration/billing: "When generating content on our paid plans, you get commercial rights to use that content. If you are on the free plan, you can use the content non-commercially with attribution." (P2 trích 29/09/2026; SHA-256 trang lưu ở `episodes/ep001/work/c5/elevenlabs-terms.json`) | YT — tài khoản ở **gói trả phí Creator** (chủ dự án xác nhận 30/09/2026), dùng thương mại theo §(c)(ii) | Không bắt buộc với gói trả phí | 2026-09-29 |
| F-INTER | Inter (400/600/700, latin woff2) | Font | `toolkit/render/fonts/` = gói npm `@fontsource/inter` 5.3.0 (3 file woff2 trùng từng byte, SHA-256 đã so 29/09/2026); https://www.npmjs.com/package/@fontsource/inter/v/5.3.0 · gốc https://github.com/rsms/inter | SIL Open Font License 1.1. Trích nguyên văn từ `LICENSE` của gói (https://unpkg.com/@fontsource/inter@5.3.0/LICENSE, bản sao `toolkit/render/fonts/LICENSE-Inter-OFL-1.1.txt`): "Copyright 2016 The Inter Project Authors (https://github.com/rsms/inter)" · "This Font Software is licensed under the SIL Open Font License, Version 1.1." · "Permission is hereby granted, free of charge, to any person obtaining a copy of the Font Software, to use, study, copy, merge, embed, modify, redistribute, and sell modified and unmodified copies of the Font Software, subject to the following conditions:" · "1) Neither the Font Software nor any of its individual components, in Original or Modified Versions, may be sold by itself." · "2) Original or Modified Versions of the Font Software may be bundled, redistributed and/or sold with any software, provided that each copy contains the above copyright notice and this license." | YT (chữ trong video), DL (file font kèm LICENSE trong repo) | Không bắt buộc ghi công trong video; LICENSE đi kèm file font | 2026-09-29 |
| A-MUSIC | Nhạc và tiếng dữ liệu (bảng âm S2) sinh bằng mã | Âm | `toolkit/audio/d_m2_audio.py`, `sonify_palettes.py` | Do dự án tự sinh; không mẫu bên thứ ba | YT, DL | — | 2026-09-28 |
| S-OPENAI-M3 | Khoá API OpenAI "OpenAI TTS spike" (tiêm qua proxy, không lộ trong repo) dùng **MỘT LẦN** để sinh 20 luận điểm đối chứng Cổng Mốc 3 bằng `gpt-5.5` (Responses API, effort medium, không công cụ, không dữ liệu) | Dịch vụ LLM (secret) | https://api.openai.com/v1/responses | Chủ dự án cho phép 2026-09-30: *"Cho phép dùng khoá 'OpenAI TTS spike' MỘT LẦN cho M3; ghi RIGHTS và AUTHORSHIP; báo tôi ngay khi sinh xong đối chứng để tôi thu hồi khoá."* | Chỉ Cổng Mốc 3 (thẻ đối chứng, lưu nguyên văn ở `m3/control/`); không dùng trong tập | — | 2026-09-30 |
| S-OPENAI-DT1 | Khoá API OpenAI "OpenAI TTS spike" (tiêm qua proxy, không lộ trong repo) dùng cho **6 thẻ đề tài đối chứng** vòng 1 Mốc 3 v2 bằng `gpt-5.5` (Responses API, effort medium, không công cụ, không dữ liệu; một lệnh/trụ, gọi lại tối đa 2 lần) | Dịch vụ LLM (secret) | https://api.openai.com/v1/responses | Chủ dự án giao trong lệnh Phiên DT1 2026-10-01: *"BÊN ĐỐI CHỨNG: GPT-5.5 (gpt-5.5, effort medium, không công cụ, không dữ liệu)… Xong thì báo chủ dự án thu hồi khoá."* | Chỉ `topics-r1/control/` (lưu nguyên văn); không dùng trong tập | — | 2026-10-01 |

## F. Footage ngoài (D-013, chủ dự án duyệt 13/10; CHARTER §4)
Trần từng tập: **Tập 8 ≤ 15 %**, từ Tập 9 ≤ 20 % thời lượng. Checks: A39 (lô K Tập 8).

### F1. Danh sách trắng (theo thứ tự ưu tiên; dùng bậc có **số nhỏ nhất** có hình phù hợp)
| Bậc | Nguồn | Giấy phép | Phải kiểm từng tệp | Ghi trên hình / mô tả |
|---|---|---|---|---|
| 1 | **Tác phẩm của nhân viên chính phủ liên bang Mỹ** khi làm nhiệm vụ (17 U.S.C. §105: NASA, NOAA, USGS, các bộ ngành) | phạm vi công cộng | ảnh do nhà thầu/bên thứ ba chụp **không** thuộc §105 → chỉ dùng tệp cơ quan ghi rõ "public domain". **Tư liệu NARA/LoC phần lớn không phải tác phẩm §105**: tệp ghi "No known restrictions" chỉ là **đánh giá của tổ chức, không bảo đảm** → xếp **bậc 5** (dưới); **không** dùng phù hiệu, logo cơ quan (vd NASA insignia bị hạn chế); không dùng ảnh của chính quyền bang (luật khác nhau) | "Source: <cơ quan>, <năm>" |
| 2 | **Natural Earth** (bản đồ) · **Census TIGER/Line** · **OpenStreetMap dữ liệu** | Natural Earth: phạm vi công cộng · TIGER: phạm vi công cộng · OSM: **ODbL** (dữ liệu) | OSM: chỉ dùng **dữ liệu**, tự vẽ bằng màu kênh (thành sản phẩm từ dữ liệu, ghi công); **không** dùng ô bản đồ (tile) của OSM, vì phần đồ hoạ tile là BY-SA | OSM: "© OpenStreetMap contributors" trên hình + mô tả |
| 3 | **CC0 / Public Domain Mark** (Smithsonian Open Access, Met Open Access, Wikimedia Commons tệp ghi CC0/PD) | CC0 / PDM | đọc trang tệp, không đọc trang bộ sưu tập; PDM chỉ hợp lệ khi tổ chức gắn nhãn có thẩm quyền | "Source: <tổ chức>, <năm>" |
| 4 | **Pexels / Pixabay** | giấy phép riêng của nền tảng (không phải CC0): cho dùng thương mại, không bắt ghi công | **đọc giấy phép lúc tải** và lưu bản chụp (URL + ngày + băm SHA-256 của văn bản giấy phép); loại ảnh có người nhận ra được mặt, logo/nhãn hiệu, tác phẩm nghệ thuật, ảnh gắn nhãn tạo bằng AI | "Photo: <tác giả>/<nền tảng>" (tự nguyện) + năm nếu biết; không biết năm → không dùng làm tư liệu có năm |
| 5 | **NARA / LoC "No known restrictions"** (tư liệu không phải §105) | đánh giá quyền của tổ chức, **không bảo đảm** | lưu bản chụp nhãn quyền (URL + ngày + băm SHA-256); ghi "đánh giá của tổ chức, không bảo đảm" trong RIGHTS; LoC đọc `rights_advisory` qua `?fo=json` (cine #61) | "Source: <tổ chức>, <năm>" |
| 6 | **CC BY** (4.0 ưu tiên) | CC BY | ghi công đủ TASL (tiêu đề, tác giả, nguồn, giấy phép); không cắt xén làm đổi nghĩa | ghi công trên hình hoặc trong mô tả + RIGHTS |

### F2. Danh sách cấm
CC **NC** (phi thương mại: kênh có quảng cáo) · CC **ND** (không cho chỉnh sửa: kênh luôn phủ tông, cắt, thêm chuyển động) · **CC BY-SA cho hình/video** (điều khoản chia sẻ tương tự lan sang tác phẩm ghép) · quyền **không rõ** hoặc không trích được văn bản giấy phép · **logo, nhãn hiệu, giao diện sản phẩm** · **người thật trong vai nhân vật** (nhân vật kênh là ILLUSTRATIVE, không mặt) · đoạn của kênh YouTube khác, đài tin tức, "nhúng miễn phí" của kho ảnh thương mại · ảnh/video tạo bằng AI trình bày như tư liệu.

### F3. Trần và cách ghép (giữ ngôn ngữ hình kênh — cine-lab #49, #50, #93)
- **Trần:** ≤ 20 % thời lượng tập (Tập 8 ≤ 15 %); mỗi lần ≤ 6 s liền; không mở tập (5 s đầu ở thế giới — quy tắc 7) và không trùng số neo.
- **Chuyển động:** luôn có chuyển động máy (đẩy/lia chậm); điểm chính của ảnh (`focus`) nằm **trên** dải chú thích, rà một khung mỗi ảnh trước khi dựng (cine #49).
- **Tông:** phủ bảng màu kênh (grade về token + hạt nhẹ), không để màu ảnh gốc đứng riêng.
- **Hoà từ 3D:** mở đoạn bằng cảnh 3D nối tiếp rồi hoà ≥ 0,8 s (cine #93: cắt thẳng 3D ↔ ảnh thì 2/3 người xem nói "đổi chất liệu", kể cả khi có hoà 1,4 s). **Ưu tiên đặt ảnh trong thế giới** (tờ ảnh trên bàn, màn hình, bảng) hơn là toàn khung.
- **Dòng nguồn:** nguồn ảnh bên phải, nguồn số bên trái, cùng trên dải chú thích; không để một dòng che dòng kia (cine #50, #68).

### F4. Trung thực
- Ảnh minh hoạ **không làm bằng chứng**: không đi cùng claim số; mang nhãn minh hoạ khi không phải tư liệu đúng sự kiện.
- Tư liệu (`archival`) ghi **năm + nguồn trên hình**; năm không xác minh được → không dùng.
- Bản đồ tự vẽ từ dữ liệu ghi nguồn dữ liệu và năm của dữ liệu.

### F5. Thủ tục
1. Ghi dòng RIGHTS **trước khi** dựng (mã `X-<tập>-<n>`, URL tệp, giấy phép trích nguyên văn + link, ngày tải, bậc 1–6, phạm vi YT).
2. Lưu tệp gốc ngoài git (`work/external/`); trong repo chỉ có RIGHTS + băm SHA-256.
3. Checks A39 chặn khi thiếu hồ sơ, giấy phép cấm hoặc vượt trần. Ngoài danh sách trắng → **hỏi chủ dự án** (ngoại lệ pháp lý, CHARTER §5).

## G. SFX ghi âm thật (D-013)
Chỉ **CC0** hoặc **CC BY 4.0** (Freesound lọc theo giấy phép; trang tệp, không trang bộ sưu tập). Cấm: CC BY-NC, Sampling+, BBC RemArc (phi thương mại), kho trả phí, YouTube Audio Library. Mỗi tệp một dòng ở bảng trên (mã `S-<tên>`, URL tệp, tác giả, giấy phép trích nguyên văn + link, ngày tải); CC BY → ghi công trong mô tả tập dùng nó. Nhạc vẫn bằng mã (A-MUSIC); nhạc người sáng tác CC BY xét lại ở G1 Tập 9; không nhạc AI.

## Tham chiếu (chỉ để xem; KHÔNG dùng trong tập)

| Mã | Tài sản | Nguồn | Được làm | Không được làm |
|---|---|---|---|---|
| REF-VOX | *How the US made affordable homes illegal* (Vox, 2021) | https://www.youtube.com/watch?v=0Flsg_mzG-M | Xem công khai; mô tả bằng lời kèm mốc thời gian | Tải, trích khung/âm/đoạn, sao chép thiết kế hay câu chữ |
| REF-3B1B | *Bayes theorem, the geometry of changing beliefs* (3Blue1Brown, 2019) | https://www.youtube.com/watch?v=HZGCoVF3YvM | Như trên | Như trên |
| REF-WSJ | *Mortgage Rates Hit 7%: What's Next for the Housing Market?* (WSJ News, 2026) | https://www.youtube.com/watch?v=lsOD1CHkWrY | Như trên | Như trên |
