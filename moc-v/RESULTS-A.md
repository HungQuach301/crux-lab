# Mốc V · Phần A — kết quả làm thử (06/10/2026)

Đoạn thử: Tập 4 **S04.5 → S07.3**, 69,6 s ("Is it? Has their gain passed the cap?" → "…almost 3.8 times their 2000 level"): một nhịp then chốt (vượt trần, "That's past the cap") + một đoạn số liệu (chỉ số Phoenix, phép trừ $200,000, lãi theo quý).
**Trục xương sống:** `moc-v/proto/spine.py` → `spine.json` — 12 nhịp, mỗi nhịp: ý · câu lời · hành động hình · sự kiện âm · mức căng nhạc · cảm xúc · chuyển sang nhịp sau; mốc của từ khoá lấy từ alignment của take giọng (không gõ tay); **nhưng** trong mã từng hướng vẫn còn nhiều mốc gõ tay (khung máy quay, độ dài chuyển động, khoảng giữ, ví dụ 62,9/63,2/63,8 s ở b11) — Phần B phải đưa hết vào đặc tả nhịp. Hình, âm dữ liệu, sfx, nhạc đọc CÙNG lịch `draw`/`ride`/`events` nên đồng bộ do cấu trúc.
**Lời:** sinh lại theo cảnh bằng đúng cấu hình đã phát hành (Eric, `eleven_v3`, seed 1004) — 1.017 ký tự EL; take commit ở `moc-v/proto/voice-takes/`.

## Ba hướng

| | **R** bản đã phát hành | **A** vật thể thật 2D | **B** vật thể thật 3D | **C** hình học liên tục |
|---|---|---|---|---|
| Gen được bảo vệ | — | không đụng | **ĐỤNG "không thế giới 3D" (CHARTER §4)**: sân, khu phố, máy quay 3D. G-012a chỉ cho vật thể thật 3D là *phương án để chủ dự án chọn*; chọn B = chủ dự án sửa gen (CHARTER §6) | không đụng |
| Ý tưởng | nhà máy Mốc B: mẫu `person`/`line`/`bignum`, 4 cắt cứng (3 về màn hình trống) | nhà của Rosa & Frank đứng trên **chồng tiền** (cao ∝ $), trần = **xà thép**, thời gian = **lịch xé**, khu phố "SOLD" = nhiều giao dịch | cùng truyện A bằng three.js (CPU, SwiftShader): nhà, chồng tiền, xà kính, lịch, máy quay chuyển động | một khung đồ thị, máy quay đẩy/lùi, nhà nhỏ cưỡi đầu đường; phép trừ = cả đường trượt xuống $200,000; số bay từ đầu đường lên |
| Mã | — | `proto/A/a.js` | `proto/B/b.js` (agent riêng) | `proto/C/c.js` |
| Nhạc | style C một mạch (nhà máy) | mã, theo bản đồ căng (114 BPM, D dorian → F trưởng lúc thả, lặng ngắn sau "cap") | **Eleven Music (AI)** theo kế hoạch 5 đoạn cùng bản đồ căng + lặng sau "cap" | mã (như A) · bản phụ `C-aimusic` = cùng hình + nhạc AI để so riêng nguồn nhạc |

## Số đo (mục 2 áp vào từng bản; số thô `moc-v/measure/raw/m-proto-*.json`, `moc-v/eval/`)

| | R | A v2 | B | C v2 |
|---|---|---|---|---|
| % thời lượng chỉ có chữ | **28,6 %** | **0 %** | **0 %** | **0 %** |
| Từ mới trên màn hình / phút | 80 | 65 | 74 | 69 |
| % có đồ hoạ/vật thể chuyển động | 4,3 % | 54 % | **73 %** | 41 % |
| Nhân vật khi lời nói về họ (4 câu): hình người · vật của họ | 1/4 · 0/4 | 2/4 · 4/4 | 2/4 · 4/4 | 2/4 · 4/4 |
| Cắt cứng giữa mẫu không liên quan | 4 (đạo diễn: 3 cắt về màn hình trống, ≈ 9 s trống) | 0 (1 chỗ tua về 2000 bị gọi "gãy") | 0 (tua về 2000) | 0 (tua về 2000) |
| Âm dữ liệu (bảng S2; `eval/audio/audio-report-*.json`) | không | có: 90 nốt; đỉnh trong khe lời −3,5 dB so với RMS lời; nốt dời vào khe ≤ 120 ms | có (cùng lớp) | có |
| Hiệu ứng âm theo biến động (G-001) | không | 24 sự kiện (riser, thud khoá trần, chime lúc cắt trần, swish số bay, impact sau "cap", rise ×3,8) | có | có |
| Room tone + vào khoảng lặng (G-003) | không | sàn −62 dBFS, +6 dB khi lặng; nhạc nhả τ 90 ms sau "cap" | có | có |
| Nhạc: độ lặp (cặp câu ≥ 0,90; `eval/audio/music-selfsim.jsonl`) | 25 % (cả tập) | 0 % (7 cặp) | 0 % (7 cặp) | 0 % |
| Nhạc theo căng–chùng (DX-R1) | không | có, nhưng đạo diễn: "biên độ hẹp, nghe phẳng" | có (AI) | có, như A |
| Lời trên nhạc (A07) | — | 24,0 dB | 24,0 dB | 24,0 dB |
| Mức cuối | — | −14,0 LUFS · −1,5 dBTP | như A | như A |
| Đồng bộ lời (ASR vs alignment) | — | lệch trung vị 0,02 s, P90 0,135 s | như A | như A |
| **Đồng bộ hình–từ khoá ±0,2 s** (đo khởi động chuyển động trên video cuối, `sync_audit.py`) | đạo diễn: lệch 0,7–3 s ở 8 chỗ | **11/12** (1 nhãn nhỏ không đo được) | 8/12 (lệch: vạch trần +0,37, nhà mờ +0,24, bắt đầu vẽ −0,21; máy quay 3D làm nhiễu phép đo) | **9/12 đạt, 3 không đo được; mọi sự kiện đo được ≤ 0,1 s** |
| Thời gian render CPU (4 vCPU; chi tiết `eval/render/RENDER.md`) | — | 0,93–1,08 s máy / 1 s phim (2–3 luồng) → tập 8 phút ≈ 8–9 phút | **8,7–12,8 s / s** (nhà mã), 10,5 s / s (nhà CC-BY), 4 luồng, CPU dùng chung → tập 8 phút ≈ 70–100 phút | 0,78–1,04 s / s |

## Cổng gốc + kiểm mù tắt tiếng (ý đồ ghi trước `eval/ROOT-intent.md`; người đọc headless mù, người chấm độc lập)

| | K1 "lãi vượt trần Q2 2022, tụt, ở trên từ Q2 2023" | K2 "≈ $558,100 qua trần; giá ×3,8" | Khuyên |
|---|---|---|---|
| R | **ĐẠT** 2/2 (điểm 1, 1) | **ĐẠT** 2/2 | 0 |
| A v1 → v1b | 0,5 · 0,5 → 0,5 · 0,5 **TRƯỢT** | **ĐẠT** 2/2 | 0 |
| B v1 → v2 | 0,5 · 0,5 → 0,5 · 0,5 **TRƯỢT** (v2: đã hiểu đúng là LÃI, chỉ thiếu nhịp tụt) | 0,5 · 0,5 → **ĐẠT** 2/2 | 0 |
| C v1 → v1b | 0,5 · 0,5 → 0,5 · 0,5 **TRƯỢT** | **ĐẠT** 2/2 | 0 |
| *Tham khảo sau lượt đạo diễn (A v2, C v2)* | *0,5 · 0,5* | *2/2* | *0* |

**Vì sao K1 trượt ở A/B/C mà R đạt:** (1) dải 6 khung của K1 gồm cả đoạn đặt trần cạnh đường GIÁ TRỊ nhà trước phép trừ — khung tĩnh cho thấy "giá nhà đã vượt trần từ 2005"; v2 làm mờ đường giá trị nhưng chưa đủ; (2) nhịp "tụt lại dưới trần" 2022Q3–2023Q1 quá nhỏ ở thang cả 26 năm; R ghi hai nhãn sát nhau nên người đọc suy ra. **Hướng sửa ở Phần B (bằng HÌNH):** đặt trần chỉ sau khi đường LÃI xuất hiện (trước đó đường giá trị ở khung riêng, không có vạch); phóng đoạn 2021–2026 khi nói "slips back under" (inset hoặc máy quay đẩy); nhãn chỉ dùng khi hình đã thử mà vẫn trượt, có ghi lý do.

## Lượt đạo diễn (agent độc lập "xem có tiếng": khung 0,5 s + mức từng lớp + phổ + ASR + ý đồ nhịp) — `eval/director-*.md`

| Điểm 1–5 (hình mang nghĩa · liền mạch hình–lời–âm · nhịp · âm) | v1 | v2 (sau sửa) |
|---|---|---|
| R | 3 · 2 · 2 · 2 | — |
| A | 3 · 2 · 3 · 3 | **3 · 3 · 3 · 3** |
| B | 3 · 2 · 2 · 3 | **3,5 · 3 · 2,5 · 3** |
| C | 3 · 3 · 2 · 3 | 3 · 3 · 2,5 · 3 |

Đã sửa sau v1 (cả A, C; B qua agent): năm khoá theo lời; mỗi nhà SOLD bật = một tick; "let its value rise" có mũi tên; lấp đoạn 25–35 s ("their gain on paper = ?", khối $200,000 lúc nói "$200,000", "grown with the index" lúc nói "grown", chỉ ghi "paid" lúc "less"); ngoặc "well under"; nhà lướt về 2000 thay vì nhảy; tia sáng ở điểm cắt; Rosa & Frank trở lại ở b9–b10; nhà nảy qua trần lúc "past"; cảnh ×3,8 che hẳn biểu đồ; impact dời sau "cap" và hạ (sfx giờ chuẩn theo đỉnh: impact −23 dB, thud −16 dB dưới đỉnh lời).
**Kết luận cổng gốc: KHÔNG hướng nào đạt cổng gốc (K1 trượt ở cả A, B, C); bản phát hành R đạt nhờ nhãn chữ.** Vòng chính thức: A, C = vòng 1 + vòng 2 (sửa giữ nhãn kết luận); B = vòng 1 + vòng 2 (B v2 là lần sửa đầu tiên của B). A v2, C v2 đã dùng hết 2 vòng nên lần chấm sau lượt đạo diễn chỉ là THAM KHẢO.

**Còn lại (đạo diễn v2, việc Phần B):** B: khoá năm theo lời làm 2 s đầu đứng yên rồi vẽ 26 năm trong 2 s (cần vẽ đều 15,9→21,2 và để nhãn năm chạy theo); phối cảnh 56–62,5 s cắt đáy tháp làm phần vượt trông lớn (cần góc nhìn trực giao khi đọc số);  đặt trần lên đường lãi (như trên); chỗ tua về 2000 cần báo hiệu (lời/âm) hoặc bỏ; nhạc cần biên độ căng–chùng rộng hơn (cao trào ở 61 s chưa nghe ra); lớp bắt buộc (ILLUSTRATIVE, history/US only, nguồn, đối trọng) ở 40 px bị **cả bốn đạo diễn ghi là KHÔNG đọc được ở 25 %** (họ xem khung ~17 %, nên phép thử còn khắt hơn G-014, nhưng vẫn là lỗi); con số "0 % chỉ có chữ" có được một phần NHỜ đẩy lớp bắt buộc xuống chữ góc nhỏ → Phần B phải chứng minh lớp bắt buộc đọc được (≥ 48 px, chữ sáng, đo bằng luật C14 trên bản cuối) mà vẫn không quay lại thẻ chữ; cắt mép khi máy quay đẩy 58–63 s; "$558,100" nên bay VÀO biển trên nhà (ý đồ) chứ không lên tít.

## So nguồn tài sản (`assets/SOURCES.md`, đọc 06/10/2026; KHÔNG mua, không đăng ký)

| Lớp | Bản sinh bằng mã | Bản nguồn có giấy phép | Giá · điều khoản (nguyên văn trong SOURCES.md) | Rủi ro |
|---|---|---|---|---|
| Nhạc | `audio.py` (theo bản đồ căng, 0 % lặp, đổi điệu lúc thả, lặng đúng 'cap') | **Eleven Music** (`/v1/music`, kế hoạch 5 đoạn cùng bản đồ căng) — 69,6 s, **ước** ≈ 1.050 credit (900 credit/phút × 1,16 phút; không đọc được số dư) của gói EL hiện có — lệnh gọi do phiên điều phối thực hiện sau khi agent nghiên cứu xong | Starter $6 · Creator $22 · Pro $99/tháng; "All online and offline commercial use permitted, except film, TV, radio, & Studio Games" (mọi gói tự phục vụ; Free không cho tải và phải ghi công) | output "may not be unique" → có thể bị Content ID của người khác; EL không bảo đảm không vi phạm; **gói EL hiện tại của kênh chưa xác minh** (khoá API không có quyền đọc gói) — cần chủ dự án xác nhận ≥ Starter |
| Mô hình 3D | nhà low-poly dựng bằng mã (màu kênh, không cần ghi công) | `mmmm-models` "Mini Mike's Metro Minis" (CC-BY-4.0, npm) — `obj_house1` | miễn phí; "provided you give appropriate credit" → dòng ghi công trong mô tả | trông như cửa hàng/khối voxel hơn là nhà ở; texture bảng màu riêng lệch hệ màu kênh; Kenney/Poly Haven (CC0) **bị chặn mạng** nên chưa thử |
| Không thử | Meshy/Tripo/Luma (3D AI), Epidemic/Artlist | — | trang bị chặn; giá chỉ từ tìm kiếm, **chưa xác minh** | quyền tác giả output AI ở Mỹ chưa rõ |

**Đề xuất:** nhạc — giữ mã làm mặc định (đã đo theo bản đồ căng, không rủi ro Content ID); Eleven Music chỉ nếu chủ dự án nghe bản `C-aimusic` thấy hơn rõ **và** xác nhận gói EL ≥ Starter. 3D — nếu chọn B: nhà dựng bằng mã (khớp màu, không ghi công); không đề xuất mua dịch vụ nào.

## Phiếu L3 của chủ dự án cho từng hướng
Chưa có — chỉ chủ dự án chấm (lệnh: "điểm L3 … mỗi tập" và ngưỡng D-009 (d)). Gói A xin chủ dự án chấm 6 dòng §8 cho R, A, B, C sau khi xem `review/compare.mp4`.
