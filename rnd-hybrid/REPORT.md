# R&D "hình lai không dùng AI sinh hình" — gói cho chủ dự án (nhánh `rnd-hybrid`, 14/10/2026)

## Gói (3 câu)
1. Nhà máy canvas hiện có dựng được clip lịch sử 46,9 s bằng nhân vật cắt giấy SVG do Claude vẽ (3 nhân vật × 6 biểu cảm), sticker, một cảnh dữ liệu có sẵn (`bignum`, `bars`) và ô ảnh tư liệu Ken Burns + tông kênh. Clip có 17 cảnh, trung vị 2,79 s, 30 fps, hai lần dựng lại trùng byte; máy chạy 100 s ở 1080p; giọng ElevenLabs 666 ký tự; nhà cung cấp hình 0 $.
2. Phiên chưa tải được ảnh tư liệu nào: LoC, NARA, HUD và Wikimedia đều bị chính sách mạng chặn, nên clip đang mang 2 **ô chờ ảnh** ghi rõ hồ sơ cần tải (`archival/SOURCES.md`). Đọc mù tắt tiếng 2 người cũng chưa đo, vì phiên không có agent con và headless khoá Console (`blind/PHIEU.md`).
3. **Khuyến nghị:** duyệt thử "hình lai" (chế độ b của `CHARTER-PROPOSAL.md` §A) trên **một chương lịch sử của Tập 9**, với hai điều kiện: anh mở host `www.loc.gov`, `tile.loc.gov`, `catalog.archives.gov` (hoặc tự tải 2 ảnh trong bảng), và 2 người đọc mù clip này đạt ngưỡng ghi trước.

**Clip:** `rnd-hybrid/clip/out/clip-1080.mp4` (1920×1080, 30 fps, 46,94 s, 6,9 MB, SHA-256 `736f1e06…af1bb9`).

## Số đo
| Mục | Số | Ghi chú |
|---|---|---|
| Chi API | ElevenLabs: **666 ký tự** gửi (lời đã chuẩn hoá ≤ 800). Đồng hồ `/v1/user/subscription`: 98.214 → 98.507 (+293 credit, eleven_v3). Quy đổi theo gói Creator ≈ 0,06–0,15 $. Console: 0 $ (headless khoá). OpenAI: 0 | Trần 12 $: dùng < 2 % |
| Giờ máy | 1080p: 100–103 s mỗi lần cho 46,9 s phim (≈ 2,2 s máy / 1 s phim, 4 worker, 4 lõi); 540p: 46 s. Cả phiên: 3 lần dựng 1080p + 2 lần 540p + ASR ≈ **7 phút máy** | Tập 4–5 thế giới 3D: ≈ 2 s máy/s ở **540p**, nên ở cùng độ phân giải thì cắt giấy nhanh hơn ≈ 2× |
| Cảnh | 17 cảnh, **trung vị 2,79 s**, ngắn nhất 1,65 s, dài nhất 3,74 s | Tham chiếu GoDocs Suez: 1,9 s |
| Tất định | Xoá cache rồi dựng lại: 17/17 đoạn trùng byte, picture SHA trùng | Không có Math.random, không ảnh ngoài, không phụ thuộc đồng hồ |
| Tư liệu | 2 ô (cảnh G 2,20 s + cảnh I 2,79 s) = **10,6 %** thời lượng | Dưới trần §F (15/20 %); hiện là ô chờ ảnh. Nhánh ảnh thật (xám, tông giấy, Ken Burns, viền in) đã chạy thử bằng thẻ test, **không đưa vào clip** |
| ASR lời (small.en) | Khớp toàn văn, lệch duy nhất "insured" → "ensured" (đồng âm) | |
| Âm lượng | −14,6 LUFS, −1,5 dBTP | loudnorm 1 lượt; nhà máy dùng 2 lượt |
| Đọc mù tắt tiếng 2 người | **chưa đo** | phiếu + ngưỡng ghi trước: `blind/PHIEU.md` |
| Thời gian phiên | ≈ 30 phút (06:15–06:45 UTC), 0 agent con | |

## Đã làm theo 5 việc
1. **Tư liệu** (`archival/SOURCES.md`): toàn bộ host lưu trữ bị chặn (proxy 403, WebFetch ENOTFOUND), nên RIGHTS §F6 **không ghi dòng nào**. File có 6 ứng viên kèm URL JSON để kiểm quyền: LoC `cph.3c17261` (1931), NARA NAID 12573155 (1932), FSA Rothstein Kearney (1936), LoC 2017765777/2017767302, NARA RG 195. Clip đọc ảnh qua `work/external/manifest.json`, không phải sửa mã.
2. **Thư viện cắt giấy** (`cutout/`):
   - `rig.js` là nguồn duy nhất cho cả canvas lẫn SVG. Mỗi nhân vật có 10 khớp: thân, đầu, cánh tay/cẳng tay trái-phải, đùi/cẳng chân trái-phải.
   - Biểu cảm: 5 kiểu mắt, 5 kiểu mày, 6 kiểu miệng, ghép thành 6 biểu cảm (neutral, happy, worried, shocked, sad, relieved), có chớp mắt tất định.
   - 8 tư thế và chu kỳ đi bộ.
   - Đạo cụ: nhà 1930, nhà nay, ngân hàng (cửa đóng/mở), giấy vay, xu, người xếp hàng.
   - Bảng màu theo token kênh.
   - `export_svg.mjs` xuất 12 SVG gồm nhân vật, tờ biểu cảm, đạo cụ, kèm `palette.json`. Nhân vật: Walt và Ruth (1930), Sam (hôm nay), tất cả mang nhãn ILLUSTRATIVE.
3. **Clip** (`clip/make_clip.py`): giọng tạo qua `toolkit/factory/voice.py` (Eric, eleven_v3, có cache và commit take). Hình dựng qua `toolkit/factory/render.js` + `page.html`, nạp mẫu `cutout`/`archival` bằng cơ chế custom_symbols, không sửa nhà máy. Tiếng gồm lời, tiếng "pop" giấy khi sticker hiện, tiếng "swish" mỗi cắt cảnh và một lớp đệm hai hợp âm, tất cả sinh bằng mã.
4. **Chính sách YouTube** (`POLICY.md`):
   - Nhãn nội dung tổng hợp: hoạt hình và giọng premade không thuộc diện phải khai. Vì kênh là chủ đề tài chính, nên ghi rõ "synthetic voice".
   - "Inauthentic content" (từ 15/07/2025) đặt rủi ro lên chính khuôn mẫu. Cách giảm rủi ro: mỗi tập một mô phỏng riêng.
   - Lồng tiếng: auto dubbing của YouTube 0 $ (27 thứ tiếng, theo báo chí 02/2026); ElevenLabs tính 3.000 credit/phút (≈ 30 k cho một tập 10 phút, mỗi thứ tiếng); dịch rồi TTS lại bằng nhà máy ≈ 10 k, và dịch được cả chữ trên hình.
   - Các trang support.google.com bị chặn, nên câu trích YouTube lấy qua kết quả tìm kiếm.
5. **Đề xuất CHARTER** (`CHARTER-PROPOSAL.md`): chỉ đề xuất mở rộng gen hình §4 thành hai chế độ (thumbnail đã bỏ theo quyết định chủ dự án 14/10: giữ không thumbnail). Phiên **không** áp dụng và không sửa CHARTER, RIGHTS hay checks.

## Chưa đạt / cần biết
- Lời nháp có 3 claim mới cần đọc nguồn gốc trước khi vào tập: 5 năm/ít trả gốc, ≈ 1.000/ngày năm 1933, FHA 1934 → 30 năm. Hiện chỉ có thông cáo St. Louis Fed 2008 qua kết quả tìm kiếm (`archival/SOURCES.md`). Clip là bản nháp R&D, **không phát hành**.
- Cảnh I đặt ảnh FSA năm 1936 dưới lời "in 1933". Năm trên hình đúng với ảnh (§F4), nhưng người xem có thể thấy lệch; đọc mù câu Q7 sẽ trả lời.
- Sticker xoay vẽ thẳng lên canvas nên không vào log chữ của engine (sàn chữ, tương phản). `qc.py` và `checks/` chưa chạy trên clip; việc này để phiên K quyết.
- Engine chỉ hỗ trợ 1080/720, nên bản "540p" thực ra dựng ở 720p.
- Chưa tải được ảnh thật nào; trong clip là ô chờ ảnh, ghi rõ hồ sơ cần tải.

## Tệp
`archival/SOURCES.md` · `cutout/{rig.js,templates.js,export_svg.mjs,sheet.html,svg/}` · `clip/{narration.json,voice_clip.py,make_clip.py,voice-takes/,out/}` ·
`blind/PHIEU.md` · `POLICY.md` · `CHARTER-PROPOSAL.md`. Tái lập: `python3 rnd-hybrid/clip/voice_clip.py`
(dùng cache, 0 ký tự) → `python3 rnd-hybrid/clip/make_clip.py --res 1080 --workers 4`.
