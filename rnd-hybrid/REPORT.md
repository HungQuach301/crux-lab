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

---

# Vòng 2 (14/10/2026): phong cách A + chất in B + tư liệu C đứng riêng

## Gói (3 câu)
1. Clip mới `v2/clip/out/clip-1080.mp4` (46,9 s, 19 cảnh, trung vị **2,17 s**) theo phong cách chủ dự án chọn: giấy trong thế giới 3D (khung A, đã sửa đèn bù, cột đèn, tờ CLOSED), mặt giấy in nét mực/bán sắc/vân giấy (B), ảnh LoC 1931 đứng riêng toàn khung 4,27 s rồi hoà về cảnh A. Mọi claim số đã đối chiếu nguồn gốc (`v2/CLAIMS.md`), kể cả nguyên văn luật 1934 §203: "not to exceed twenty years", 80 % giá thẩm định.
2. Chi **≈ 0,19 $** (ElevenLabs +870 credit cho 3 take, OpenAI 0, Console 0) trên trần 10 $. Nhưng giờ máy tăng vọt: **42,5 phút** cho 46,9 s phim (≈ 54 s máy mỗi giây phim, 4 lõi, swiftshader + bóng 4096 px), so với 1,7 phút ở vòng 1. Đọc mù 2 người **vẫn chưa đo** vì không có người đọc độc lập (0 agent con, Console khoá).
3. **Khuyến nghị:** chủ dự án xem clip và tờ trước/sau `v2/BEFORE-AFTER.jpg`. Nếu giữ hướng này, việc kế tiếp là (a) chọn 2 người đọc mù theo `blind/PHIEU-v2.md`, (b) một phiên tối ưu render (bóng 2048, PCF thường, bỏ đèn thừa) trước khi dùng cho một chương Tập 9. Đề xuất CHARTER §4 "gen lai A+C": `CHARTER-PROPOSAL.md` mục B (chỉ đề xuất).

## Số đo
| Mục | Số | Ghi chú |
|---|---|---|
| Thời lượng | 46,87 s (lời 45,36 s sau atempo 1,06 + 0,3 s đầu + 1,2 s đuôi) | take speed 0,9 dài 48,08 s; take speed 1,0 lại dài hơn (51,4 s), nên giữ 0,9 và tăng nhịp bằng atempo (giữ cao độ) |
| Cảnh | 19 cảnh · **trung vị 2,17 s** · ngắn nhất 1,07 s (J, cảnh hoà ra) · dài nhất 4,70 s (P) | vòng 1: 2,79 s · GoDocs: 1,9 s |
| Tư liệu | 1 lần, **4,27 s** liền (hoà vào 0,7 s + đầy khung + hoà ra 0,8 s về cảnh A) = **9,1 %** | ≤ 6 s liền, ≤ 20 % (RIGHTS §F3); không có nhân vật trên ảnh |
| Chi API | ElevenLabs: đồng hồ `/v1/user/subscription` 98.507 → 99.377 (**+870 credit**, eleven_v3) cho 3 take (679 + 679 + 619 ký tự gửi). Theo giá gói Creator ≈ **0,19 $** · OpenAI 0 · Console 0 | 2 take bỏ đi (dài quá 45 s) đã xoá khỏi repo |
| Giờ máy | 1080p: **2.548 s tường** (4 worker, 4 lõi) = 54 s máy mỗi giây phim; tổng worker-giây 9.141. Cảnh J dựng 1 worker: 89 s/s. Xem trước 540p (19 khung tĩnh): 70 s | Vòng 1: 100 s cho 46,9 s. Nghi chính: WebGL phần mềm (swiftshader) + bóng PCFSoft 4096 px + nhiều tấm alpha. **Chưa tối ưu** |
| Tất định | Dựng lại cảnh J vào cache khác: SHA-256 `00dbab8b…` trùng byte | không Math.random, không đồng hồ |
| Lời (ASR faster-whisper small.en) | khớp toàn văn; chỉ khác cách viết số ("80" so với "eighty") | |
| Âm lượng | −14,6 LUFS, đỉnh −1,5 dBFS | loudnorm 1 lượt |
| Tệp | `v2/clip/out/clip-1080.mp4`: 22 MB (mã lại crf 21 cho repo), SHA-256 `940c36d9…f94b7c6`; bản gốc crf 16 48 MB ở `work/v2/` (ngoài git) `bce020a6…09f795dc9` | |
| Đọc mù tắt tiếng 2 người | **chưa đo** | phiếu + đáp án mới: `blind/PHIEU-v2.md`; dải 6 khung: `v2/blind-strips/` |

## Claim đã sửa (chi tiết ở `v2/CLAIMS.md`)
- **"five years"** sửa thành **"three to five years"**, kèm "about half the price" (HUD: "limited to 50 percent… three to five years… balloon payment").
- **FHA 1934:** "up to eighty percent of the value… paid down every month, for up to twenty years". Nguồn: 48 Stat. 1246 §203(b)(2)–(4), FHA *First Annual Report* (1935) và Fed History.
- **Mốc 30 năm:** "In 1954, the limit stretched to thirty years". Nguồn: St. Louis Fed *Review* 11/1955 (Housing Act 1954: nhà mới 25 → 30 năm, nhà cũ 20 → 30 năm).
- **Ngày đóng cửa Bank of United States:** **11/12/1930** (Fed History). LoC ghi năm **1931** cho tấm ảnh, và tiêu đề có chữ "after its failure", nên hai nguồn không mâu thuẫn. Lời chia thành hai câu: "In December 1930… closed." rồi "In 1931, its depositors still crowded outside."
- **Đã bỏ:**
  - "≈ 1,000 foreclosures a day": PDF Wheelock 2008 tải không được, chưa có nguồn gốc;
  - "most people simply signed a new one": không có nguồn;
  - "still the standard today": không có nguồn.

## Đã làm theo yêu cầu sửa A
- **Hàng người trung cảnh:** thêm đèn bù ấm phía máy quay, cộng một đèn bù đi theo máy quay trong mọi cảnh.
- **Cột đèn:** dời khỏi bậc thềm, sang (13,5; −6,2).
- **Tờ CLOSED:** thẻ giấy 2,0 m, chữ 150 px trên texture, máy đẩy vào ở cảnh H. Đọc được ở 1080p (tờ trước/sau, hàng 2).

## Chưa đạt / cần biết
- **Giờ máy là vấn đề lớn nhất của hướng này.** Ở mức hiện tại, một tập 10 phút cần ≈ 9 giờ máy (4 lõi). Phải tối ưu trước khi dùng thật.
- **Chữ trên thẻ giấy 3D** nằm trong texture, nên không vào log chữ của trang kiểm. `checks/` chưa chạy trên clip (phiên không chạm `checks/`).
- **Cảnh J chỉ 1,07 s** (phần đuôi sau lần hoà ra từ ảnh), có thể thấy hơi vội.
- **Cảnh "Today"** vẫn có dãy nhà phố tối phía sau, vì hồi `today` chưa phủ hết thế giới.
- **Lời và năm trên hình:** lời nói "In December 1930", năm trên hình là "December 1930". Đây là năm của sự kiện; ảnh mang năm LoC (1931) ở dòng nguồn.

## Tệp vòng 2
`v2/clip/{narration.json, voice_v2.py, build.py, seg/{world.js, scene.js, spine.json, timeline.json, inputs.json}, voice-takes/, out/}` · `v2/{paper3d.js, illus2d.js}` ·
`v2/CLAIMS.md` · `v2/BEFORE-AFTER.jpg` · `v2/blind-strips/` · `blind/PHIEU-v2.md` · `CHARTER-PROPOSAL.md` mục B · RIGHTS §F6 `X-RND-1`.
Tái lập: `python3 rnd-hybrid/v2/clip/voice_v2.py` (dùng cache, 0 ký tự) → `python3 rnd-hybrid/v2/clip/build.py --res 1080 --workers 4`.
