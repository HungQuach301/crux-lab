# C3 · vòng 2 (sửa người dựng) — N1 lịch, N2 cột · 2026-10-07

Nguồn trượt: `gates/C3-root.md` vòng 1 — nghĩa 2/2 cả hai hình, nhưng khuyên_tính (A9) 2/2 cả hai (`c3/root/*.json`, `key.json`).
Nguyên tắc sửa: **bằng hình trước** (D-009 E6). Không đổi lời, take, độ dài đoạn (N1 449 khung, N2 446 khung), `spans.json` (muted read giữ nguyên chữ — khoá nghĩa), quy tắc D-010 1/2/3/7.
Chỉ một nhãn mới (N2 `one stretch of purchase months`, 5 từ, 50 px) thay cho nhãn cũ `one stretch` — mở rộng nhãn có sẵn, không thêm dòng.

## 1. Chẩn đoán — phần tử nào mời câu khuyên

### N1 (B06) — "ở lâu cho tới khi trả gốc nhanh lên", "trả thêm sớm", "bán/tái cấp vốn sớm thì chỉ trả lãi"
| Phần tử (vòng 1) | Vì sao mời khuyên |
|---|---|
| Chồng vay đi hết 360 kỳ; khung 6 dừng ở **"payment 346", chồng gần hết**, nhãn "faster later" | Cuối đường thành **phần thưởng**: muốn tới đoạn trả nhanh thì phải **ở lâu** → "stay in the home long enough". Máy quay giữ trên cung 30 năm, không giữ trên các ngày của lịch mà tập cần (kỳ 99 = 80 %, kỳ 114 = 78 %). |
| Chip `$2,362/month · principal + interest` nằm suốt cạnh đường dư nợ đang đi xuống (khung 3–6) | Đặt "vốn" cạnh "lãi" ngay trên đường chậm-rồi-nhanh → người đọc tự suy "đầu kỳ chủ yếu trả lãi" → "trả thêm gốc sớm". |
| Người vay (và nhà) còn đứng ở mép trái trong mọi khung đồ thị | Đồ thị đọc thành "**bạn** ở trong căn nhà này bao lâu" (thời gian ở = biến chọn được), không phải lịch của khoản vay. |

### N2 (B13) — "lên kế hoạch ở lại nhiều năm để vượt qua đợt giảm"; cột chậm = lý do giữ nhà
| Phần tử (vòng 1) | Vì sao mời khuyên |
|---|---|
| Đường chỉ số giá quốc gia **nổi phía trên cụm cột warn**, đoạn đỉnh→đáy đậm ngay trên đầu cụm, rồi **hồi phục** tới 2016 | Bố cục "đợt giảm đè lên những người chờ lâu, sau đó giá hồi" = câu chuyện **giữ qua đợt giảm** ("ride it out"). Trục x (tháng mua) bị đọc như thời gian sở hữu. |
| Tiêu đề trục `… · one bar per purchase month` **tắt** khi đường chỉ số bắt đầu vẽ (khung 5–6) | Đúng lúc chỉ số xuất hiện, chữ nói cột là **tháng mua** biến mất → cột đọc thành "thời gian giữ nhà". |
| Ngoặc + nhãn `one stretch` chỉ ở **đỉnh** cụm | Nhấn chiều cao (bao lâu) thay vì vị trí trên trục (**khi nào mua**). |

## 2. Đã đổi gì

### N1 — `world/c3/n1-calendar/{spine.py,scene.js}` (spine v4)
1. **Máy quay/hình giữ trên ngày của lịch, không trên cung 30 năm:** chồng vay + lịch chỉ đi kỳ 0 → **kỳ 114** (`claims.sched78_months_latest`), tới nơi đúng "faster" rồi **đứng yên** tới hết (lịch ngừng lật, bộ đếm `payment 114`). Không còn khung "chồng gần hết ở kỳ 346".
2. **Cả lịch 360 kỳ được in sẵn** (W5 muted, mảnh) trong 0,6 s từ "Each" — một lịch cố định từ đầu; đoạn chồng đã đi tô đậm (ink). "slowly at first" = đoạn đậm gần như nằm ngang; "faster later" = đoạn cuối dốc của **đường in sẵn** sáng lên ở "faster" (chồng không đi tới đó). Hình dạng chậm-rồi-nhanh vẫn đủ trên màn → muted read giữ.
3. **Chip vốn + lãi chỉ trong S06.1:** hiện ở "figure" như trước (REVIEWER R1 B06), tắt quanh "Each" (±0,2 s) — không nằm cạnh đường dư nợ đang đi xuống.
4. **Người + nhà + khiên rời khung khi sang đồ thị** (opacity = 1 − chart). Thế giới 5 s đầu giữ nguyên (quy tắc 7).
5. Nốt dữ liệu: mỗi 24 kỳ tới kỳ 114 (trước: mỗi 5 năm tới 30 năm).

### N2 — `world/c3/n2-bars/{spine.py,scene.js}` (spine v4)
1. **Chỉ số giá quốc gia chuyển vào trục tháng mua:** dải mảnh 90 px ngay dưới chân cột, trên hàng năm (vẽ trên lớp phủ, cùng x với cột); đoạn đỉnh→đáy đậm ở "slump". Không còn đường nổi đè trên cụm cột; phần hồi phục chỉ là một đoạn mảnh trong trục.
2. **Trục tháng mua chiếm ưu thế:** tiêu đề `Months to 80% on paper · one bar per purchase month` **giữ suốt** chế độ đồ thị; năm 48 px (trước 44); khung đồ thị hạ (cBars tgt y 1,7 → 0,9) để chỗ cho dải.
3. **Dải warn mờ dọc cụm** từ đỉnh cụm xuống hết trục + dải chỉ số (ở "together") → nối cụm chậm ↔ **tháng mua 2005–2009** ↔ đoạn chỉ số cùng tháng.
4. Nhãn `one stretch` → `one stretch of purchase months` (5 từ, 50 px, giữa trên cụm). ROI sync `t2.national` = dải chỉ số + nhãn bên trái.

Không sửa `obj5.js` (không cần vật mới), `toolkit/`, `checks/`, N3, cold open, `spans.json`.

## 3. Trước / sau (dải mù, cùng thời điểm `spans.json`)
- N1: trước `review-c3/strips/N1-calendar.r1.png` → sau `review-c3/strips/N1-calendar.png`. Khung 4–6 sau: `payment 43 / 92 / 114`, chồng đứng ở kỳ 114, đường in sẵn tới 360, không chip vốn + lãi, không người/nhà. Khung 3 vẫn có chip.
- N2: trước `review-c3/strips/N2-bars.r1.png` → sau `review-c3/strips/N2-bars.png`. Khung 3–6 sau: tiêu đề trục giữ, dải warn xuống trục, chỉ số là dải trong trục (khung 5–6), không đường nào trên cụm.
- Lưu ý: khung 6 N2 rơi đúng "national" (13,45 s cục bộ) — nhãn chỉ số đang hiện, đoạn "slump" đậm chưa hiện (giống vòng 1; khoảng thời gian dải giữ nguyên).

## 4. Kiểm (bằng chứng `review-c3/evidence/`)
| Đoạn | spine 2/3/7 | verify quy tắc 1 / 2 (từ khoá) / 3 | cắt cứng | 5 s đầu W | W / C | sync lời (median, p90) | sync hình ≤ 0,2 s |
|---|---|---|---|---|---|---|---|
| N1 | OK | 0 / 0 (8) / 0 | 0 | có | 38,7 % / 61,3 % | −0,016 / 0,106 s | **4/4** (faster +0,006) |
| N2 | OK | 0 / 0 (9) / 0 | 0 | có | 37,3 % / 62,7 % | −0,008 / 0,099 s | **5/5** (national +0,013) |
Lần dựng N2 thứ nhất có sync 4/5 (t2.national +0,646 s: ROI chỉ phủ dải, đỉnh rơi vào "slump") → ROI mở rộng sang nhãn chỉ số bên trái, dựng lại: 5/5.
Lời: đoạn cắt take thật (`wlib.clip_voice`), 0 ký tự EL; ASR khớp 32/37 (N1), 38/38 (N2) như vòng 1.

## 5. Clip + giờ render
- `review-c3/c3-clip.mp4`: thay N1 (khung 1070–1518) và N2 (2029–2474) bằng bản mới; cold open, N3, thẻ tiêu đề lấy khung-đúng-khung từ clip r1 (PSNR so r1 41–47 dB = chỉ khác do mã hoá lại). 2476 khung, 82,53 s (r1 82,61 s: âm cuối ngắn hơn 0,07 s). Dải `strips.json` cập nhật N1/N2 + sha video mới; PNG N3 giữ của r1.
- Giờ render thật (540p, 4 lõi): N1 bản cuối render 32,3 s wall cho 14,97 s phim (3,61 s/s), build 39,6 s; N2 bản cuối 53,8 s cho 14,93 s (6,03 s/s — dải vẽ trên lớp phủ mỗi khung), build 61,3 s. Cả vòng: N1 2 lần dựng ≈ 79 s, N2 3 lần dựng thành công + 1 lỗi trang (1 s) ≈ 183 s; ASR sync 3 lượt; ghép clip + dải ≈ 30 s.

## 6. Việc tiếp
Chạy lại cổng gốc C3 cho N1, N2 (người đọc MỚI, dải mới, cùng ý đồ `gates/C3-root-intent.md`); ghi `gates/C3-root-r2.md`. Khoá nghĩa: nghĩa phải ≥ 2/2 như vòng 1. Nếu vẫn khuyên: vòng 3 mới tới nhãn (≤ 8 từ, ≥ 48 px).
Khi dựng tập (S06/S07): N1 đứng ở kỳ 114 nối thẳng vào `push cPay→cSched80` của S07 (phóng vào 0–10 năm); N2 dải chỉ số dưới chân cột cần thống nhất với S11/S14 (cùng cBars).
