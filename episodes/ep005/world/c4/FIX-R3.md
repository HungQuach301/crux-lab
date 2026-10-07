# C4 · vòng 3 (người dựng, vòng CUỐI cho B08/B17) + nhận xét đạo diễn lặp + lỗi khách quan · 2026-10-07

Nguồn: `gates/C4-root.md` (vòng 2: 10/12, B08 0/2, B17 1/3), `world/c4/FIX-R2.md`, câu trả lời `c4/root-r2/*.json` và `c4/root-r2x/*.json`, `review-c4/director-A.md` và `director-B.md`, D-010, `playbook/episode.md` §1.
Luật áp dụng: sửa bằng hình trước, nhãn sau cùng (≤ 8 từ, ≥ 48 px); khoá nghĩa (không thêm câu khuyên). Lời và take giữ nguyên: 20/20 cảnh lấy từ cache, `el_chars_spent 0`.
Phạm vi sửa: `world/c4/*`, `world/c4kit.js`. Có một lỗi thật trong toolkit, sửa tối thiểu và có test (mục C1). Không đụng `checks/`, không chạy `review_pack.py`, không commit.

## A. Vòng 3 cổng gốc

### B08 / S08
Vòng 2: hai người đọc suy ra hành động từ hai mốc trên hình ("đừng chờ 78 %, theo dõi và xin huỷ ở 80 %", "send a written request"). Hai nguyên nhân: nhãn điều kiện `conditions: written request · current on payments` còn nằm trong khung 1 của B08, và mốc 99 nổi hơn mốc 114.

| Trước (r2) | Sau (r3) |
|---|---|
| Cận cảnh rất sát (fov 8,4), không thấy cả đường | S07.1 thấy trọn đường 0–360 kỳ (`cLaw`). Ở "payment 99" máy đẩy nhẹ ×1,5 (`cNear`, động tác `m_near` có whoosh_soft), đường cong vẫn gần trọn khung. |
| Không có tên khung | Tên khung `the law's two dates on this schedule` (6 từ, 52 px). Hai mốc được trình bày là SỰ KIỆN của luật trên lịch, không phải danh sách việc. |
| Mốc 99 và mốc 114 không cân nhau | Hai mốc cùng một kiểu: cùng chấm, cùng gạch dọc xuống trục kỳ. Mỗi mốc có khối nhãn 4 dòng giống nhau, 48 px: `80% of original value` / `= $320,000` / `payment 99` / `may request` và `78% of original value` / `= $312,000` / `payment 114 (9.5 years)` / `ends automatically`. Khối 80 % nằm trái gạch 99, khối 78 % nằm phải gạch 114. Không đường nào cắt chữ. Hai vạch 80 % / 78 % dài tới đúng mốc của nó. Không mũi tên, không gì làm mốc sớm trông "tốt hơn". |
| `conditions: written request · current on payments` còn trong span B08 | Đổi thành `conditions: e.g. payments current` (muted), tắt ở cuối S07.3, trước span B08. |
| — | Con trỏ chạy dọc đường lịch 0 → 99 (S07.1 → "ninety-nine") và 99 → 114 (S08.1 → "nine"), cùng một nhịp cho cả hai mốc. Đoạn 32 s không còn đứng yên. |

Nghĩa của hai mốc giữ nguyên ("may request" / "ends automatically"). S08.3 (khung rộng `based on the schedule only` + chồng `home value` ngoài khung) giữ như r2.

### B17 / S17
Vòng 2: một người đọc lẫn "112 months on paper" với lịch, một người đưa lời khuyên. Nguyên nhân: mốc lịch 90 chỉ là một chớp sáng ở "ninety" (61,6 s), sau khung 5 của dải. Vì vậy trong dải chỉ thấy "on paper: 112 months".

| Trước | Sau |
|---|---|
| Lịch chạm 80 % ở kỳ 90: chớp (Burst) ở "ninety" | Lịch: Ô VUÔNG RỖNG (muted, mảnh) trên vạch 80 % ở tháng 90, nhãn `schedule: 90 payments` ngay DƯỚI vạch. Hiện ở "schedule" (S17.3), nên có trong khung 4 và 5 của dải. Bỏ chớp, để không có "phần thưởng" ở cuối. |
| `on paper: 112 months` ở dòng tiêu đề | Trên giấy: CHẤM ĐẶC (ink) ở tháng 112, nhãn `on paper: 112 months` TRÊN đường, có gạch dẫn. Hiện ở "eighty". Lịch nằm dưới vạch, trên giấy nằm trên vạch. Khác màu, khác hình, khác phía. |
| Không thấy khoảng cách 90 → 112 | Dải sáng nối ô vuông và chấm dọc vạch 80 % (không chữ). |
| Đường trên giấy vẽ tới tháng 118 | Dừng ở tháng 112. Chỉ số dừng ở tháng 112, dưới mức mua (đường gạch accent, giữ như r2). |

Khung 6 giữ như r2: nhà, khiên, `?`. Không có người.

## B. Nhận xét đạo diễn lặp ở cả A và B

| # | Trước | Sau |
|---|---|---|
| 1 · 0:42–0:55 | Khung gần trống khi bay sang. Ba tháp nhà giống hệt nhau, đứng im 11 s | Ba người mua có màu riêng (c4kit `BCOL`: Grace hồng, Owen tím nhạt, Victor xanh bạc hà; người + mái nhà, cùng màu ở đoạn C/D). Tên hiện ở "buyers" (52 px). Nhà đã đứng sẵn khi máy bay tới, nên khung không trống. Ở "three", mỗi người có một chồng VAY mọc lên rồi chạy theo đường trên giấy THẬT của họ (10 tháng / giây, cạnh vạch 80 %): Owen chạm sau ≈ 1,3 s, Grace ≈ 2,3 s, Victor lên trên 90 % rồi mới xuống, chạm ≈ 11 s. Không có số (chế độ thế giới). |
| 2 · S07 1:58–2:30 | Quá sát, đứng yên 32 s | Xem B08: thấy trọn đường cong, đẩy nhẹ tới 99/114, nhãn nằm trong khung, có con trỏ chạy. |
| 3 · S12 4:07–4:38 | Vạch 75 % dính vào vạch 80 % (34 px); 58,6 % nổi; đứng yên 31 s | Trục cột mở từ 60 % (HT 5 → 8, `cTally` fov 13 → 11,5): hai vạch cách nhau ≈ 61 px. Vạch 75 % và nhãn `75%` màu accent, có nền. Ở "Two years after purchase" lát ≤ 75 % sáng lần lượt trái → phải và bộ đếm `at or under 75%: x%` chạy lên, tới 15,6 % đúng "fifteen". 58,6 % (lời không đọc) chuyển muted, 48 px, không nền, xếp dưới. |
| 4 · 5:53–6:01 | Đồ thị Victor trống ≈ 7 s | Đường của Victor vẽ từ "Victor": 14 tháng đầu tới "Prices" ("rose a little"), rồi tới tháng 112 ở "eighty". |
| 5 · V7 | Nền thẻ trong suốt, toà nhà 3D lộ qua chữ | Nền thẻ đục (alpha 1). |
| 6 · nhãn bị cắt | `80%` ở 0:22 bị cắt; "slowest case ≈ 9 years" bị bó đường cắt; 4:46 nhãn chồng lên vạch 60; 6:38 khung tổng kết rối | 0:22: `80%`/`90%` có nền, trái đầu vạch. "slowest case" ở vùng trống trên-phải, gạch dẫn xuống đường chậm. Các nhãn tắt TRƯỚC cú lia, không bị cắt mép. Làn S15–S17: `80%` ở đầu PHẢI vạch, có nền. 4:46: một nhóm nhãn duy nhất, cao hẳn trên vạch 60, gạch dẫn xuống vạch; bỏ nhãn `60 months` riêng. 6:38: bó nền mờ còn 55 % (≈ 11 % độ sáng chữ); ba đường trên giấy và tên mang màu người mua, có nền (Owen trái, Grace phải vạch "a plan", Victor trên-trái đầu đường); légende "on paper" ba màu; chú thích "≈ 2 years matched…" ra vùng trống dưới các đường, gạch ngắn nối vạch "a plan"; `80%`/`75%` ở đầu phải. |
| 7 · kết 7:42 | Dừng cụt trên khung sáng | `wHouse` lùi để trọn bộ ba (nhà + khiên, người, căn hộ) vào khung. Giữ khung ≈ 2 s sau "forecast", rồi tối dần về đen trong 1,5 s cuối, cùng lúc nhạc nền tắt dần 1,5 s (`bed.py`). |

## C. Lỗi khách quan

1. **Chữ cũ treo qua cú bay (`yr 4 mo)` ~5:05; vòng 3 dựng lần 1 còn để cả nhãn S13 trên ba người mua). Đây là lỗi toolkit, đã sửa.**
   - Nguyên nhân: khi một khung chỉ XOÁ lớp phủ mà không vẽ gì (không chữ, không lớp bắt buộc, như giữa cú bay C → ba người mua), Chromium trả lại ảnh lớp phủ của khung trước. Nhật ký trang ghi `texts: []` nhưng video vẫn có chữ.
   - Tái hiện bằng `render_shots.js --only s7,s9 --workers 1`: core cũ cho khung có chữ (max 255), lặp 2/2. Một ca tổng hợp 300 khung không tái hiện được.
   - Sửa (`toolkit/factory/world/core.js`, `Overlay.begin`, +4 dòng): sau `clearRect` vẽ 1 px alpha 1/255.
   - Test `toolkit/tests/test_world_overlay_clear.py`: (a) kiểm tĩnh rằng begin() có lệnh vẽ sau khi xoá; (b) `CRUX_SLOW=1` dựng lại đúng ca thật, khung 0,4 s của s9 phải tối. Cả (a) và (b) đều OK; ở core cũ, (b) có chữ. Bộ `test_world*.py` 9/9 OK.
   - core.js nằm trong khoá cache, nên cả 4 đoạn render lại.
2. **Vật bật ra ở mép khung.**
   - 2:38: đường lịch, vạch 80/78 và lịch S06 không còn tắt bụp ở cuối cú bay về thế giới; chúng mờ trong 0,45 s đầu cú bay.
   - 2:45: hai chồng S09.2 MỌC lên khi máy đã quay về phía chúng, không còn bật ra ở mép.
   - 3:24–3:34: đường chỉ số của phố rời cùng cú đẩy `m_push`.
   - 4:40–4:44: cột tập A và hai vạch hiện và mờ dần trong cú bay, không còn bật/tắt.
3. **Khối tối trên lịch (1:21, 3:30):** `c4kit.litCalendar` cho trang đang lật hai mặt, tự sáng như giấy, không đổ bóng. Áp cho lịch S04, S06 và S10.4.
4. **Người cho vay ra khỏi khung khi "It protects the lender" (1:07):** `wCal` lùi và đặt giữa, nên người cho vay, nhà, người vay và lịch cùng ở trong khung. Tên `lender` ở lại. Nhãn `cost: not shown in this video` nâng lên trên lịch (lần dựng đầu, nhãn này đè `borrower` → F-2 BLOCK).

## D. Kiểm (540p, `work/factory/world/<đoạn>-540.*`, dựng cuối)

| Đoạn | Quy tắc 1/2/3 · cắt cứng | 5 s đầu W | W / C | F-2 | Sync lời (median, p90) · ASR | Sync hình ≤ 0,2 s |
|---|---|---|---|---|---|---|
| A S01–S03 | 0/0/0 · 0 | có | 52,9 / 47,1 % | WARN 6, **BLOCK 0** | +0,007 / 0,123 s · 131/141 | 16/17 (r2 17/17) |
| B S04–S09 | 0/0/0 · 0 | có | 32,3 / 67,7 % | WARN 5, **BLOCK 0** | 0,000 / 0,140 s · 299/334 | 20/21 |
| C S10–S14 | 0/0/0 · 0 | có | 31,5 / 68,5 % | WARN 5, **BLOCK 0** | 0,000 / 0,161 s · 296/327 | **26/26** |
| D S15–S20 | 0/0/0 · 0 | có | 20,7 / 79,3 % | WARN 1, **BLOCK 0** | 0,000 / 0,161 s · 319/360 | 22/24 |

Ghi chú về các cue chưa đạt và các mục không đổi:
- **A `c7.three` không đo được.** Cửa sổ nền của sync_audit (t − 0,7 … t − 0,15) rơi đúng vào cú bay `m_c7` (41,95–42,85), nên chuyển động chồng vay ở "three" không vượt nền. Chồng vay mọc ở three − 0,05 theo mã; đã thêm vùng ROI.
- **B `p1.lender`, D `o0.climbing` và `v1.fell`:** không đo được, như r2.
- **D `v2.schedule`** (thay `v2.ninety`): +0,056 s. **`a3.two`:** ROI mở rộng tới chú thích mới.
- F-2 WARN: phần lớn là sfx trên từ khoá như r2. Còn `đường × 360 payments` ở S08.3 (WARN, như r2).
- Master `bash toolkit/build.sh episodes/ep005/episode.yaml` exit 0, rồi `c4/build_inputs.py --out` → `out/video.mp4`. qc master: sàn chữ, tương phản, vùng an toàn, va chạm nhãn, F-2 giao nhau, ILLUSTRATIVE/history đều ĐẠT. Các dòng TRƯỢT cấu trúc (đối trọng đếm theo shot 2D, freezedetect) giống hệt r2.
- **Mới: qc loudness TRƯỢT sát ngưỡng.** True-peak −1,45 dBTP so với ngưỡng ≤ −1,5 (r2: −1,5). Đỉnh rải ở các đỉnh lời (24 s, 53 s, 249 s …), không phải âm mới. Đây là sai số của bước mix + AAC, ngoài phạm vi vòng này. Đề nghị bước mix của C5 chừa thêm 0,1 dB.
- C14 đo ở bản 1080p (C5).

## E. Dải mới (giữ PNG trước ở `review-c4/strips/<id>.r2.png`; giờ/sha cũ ở `strips.json` → `r3.prev`)
Vẽ lại 10 dải vì hình trong span đã đổi: **B02, B03, N1-S06, B07, B08, B12, B13-N2, B16, B17, B18**. B11 và B14 không đổi hình trong span, nên giữ nguyên.
`review-c4/animatic-540p.mp4` = master mới (464,47 s). `highlights.mp4` cắt lại theo đúng cách cắt của review_pack (168,4 s). `spans.json` không đổi (không chạy review_pack).

## F. Giờ render (thật, 540p, 4 lõi)
| Lượt | A | B | C | D | build.sh |
|---|---|---|---|---|---|
| dựng 1 (r3) | 295 s | trượt F-2 BLOCK ở verify (borrower × cost) | — | — | dừng sau 800 s |
| dựng 2 | 304 s | 507 s | 749 s | 514 s | ≈ 3300 s; phát hiện lỗi chữ treo trên master |
| dựng 3 (cuối, core.js sửa → render lại cả 4 đoạn) | 279 s (render 229 s / 58,0 s phim) | 472 s (383 / 129,8) | 750 s (657 / 132,6) | 515 s (411 / 144,0) | **3299 s** (world 2016, splice 85, mix 188, parts 114, shorts 808, qc 34) |

Thêm: stills dò bố cục (≈ 10 s mỗi lần, khoảng 20 lần), 3 lần render tái hiện lỗi lớp phủ (mỗi lần ≈ 100 s), sync_audit 4 đoạn × ≈ 2 phút.

## G. Việc tiếp
Cổng gốc C4 vòng 3 cho B08 và B17, với người đọc MỚI, dải `strips/B08-S08.png` và `strips/B17-S17.png`, cùng ý đồ (`gates/C4-root-intent.md`). Đây là vòng cuối theo luật tối đa 3 vòng. Nếu còn trượt, gói nêu bản trước/sau để chủ dự án chọn.
- Lưu ý cho người chấm B08: đáp án muted read không đổi (hai mốc trên đường lịch, giá trị nhà không có trên đồ thị). Nhãn mới là `the law's two dates on this schedule`.
- Lưu ý cho người chấm B17: hình phân biệt lịch (ô vuông, dưới vạch, tháng 90) với trên giấy (chấm, trên vạch, tháng 112).
- Các dải B02, B03, B07, B12, B13, B16, B18 đổi hình nhưng không đổi nghĩa. Nếu cần chắc chắn không lùi (khoá nghĩa), có thể chạy lại một vòng người đọc cho các dải này.
