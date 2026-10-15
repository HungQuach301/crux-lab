# M6 Tập 8 — checks ĐỦ BỘ trên bản phát hành 1080p, khoá K4.4b `b45516422eb936f244f7e5f5c77504974a94a6b0fec19e05254a0126f0c7f9d6`

Lệnh: `EP=episodes/ep008 bash toolkit/checks_split.sh /home/user/chk-ep008 --baseline …/review-m5/checks-r2/report.json`, bộ lấy mẫu trang ở 1080p (≈ 31 cảnh, không cache — K4.4.1 đo xong nhưng chưa khoá), chạy tiếp 3 lần `RESUME=1` (trần 2 h/lệnh nền; lượt cuối tách nền, PID 11502), xong 15/10 ≈ 03:30 UTC. Báo cáo: `review-m6/checks-1080/report.{json,md}`; chạy lại 3 luật sau khi sửa dữ liệu khai (không đổi hình): `review-m6/checks-1080/report-partial-F15-S21-F13.{json,md}`.

**Kết quả đủ bộ:** ĐẠT 57 · TRƯỢT 43 · MISSING 4 · ERROR 1 (nháp r2 ở M5: 46 · 37 · 13 · 9). Sau chạy lại F15, S21: **ĐẠT 59 · TRƯỢT 41**. Theo cấp (sau chạy lại): CHẶN 32 ĐẠT · 2 TRƯỢT · 3 MISSING; CHÍNH 12 ĐẠT · 4 TRƯỢT · 1 ERROR; THAM KHẢO 15 ĐẠT · 35 TRƯỢT · 1 MISSING.

## So baseline (`review-m5/checks-r2`, nháp 540p, khoá K4.4)
- **Hết trượt (13):** F01 (1080p), F10, F11 (mô tả + gói giao), **S06** (coverage), **S07** (nhãn claim trên hình + số nói), **S09** (gốc tiền: `basis: nominal` + "in dollars of the day" + nhãn chrome), **S23** (`allowTerms` "wasted", G2 câu 7), SH01–SH05 (Short), REG (có baseline).
- **Mới trượt so baseline:** F15 (CHÍNH) — **đã sửa**: khoảng bản đồ khai ở `episode.yaml external` còn giờ trước khi cắt (151,70–157,68 s, nay rơi vào nhãn "5% … $1,667"); giờ thật 142,43–148,40 s → chạy lại F15 **ĐẠT** (F13 ĐẠT). A09 (THAM KHẢO) — lặng 0,8–1,5 s: 2 (cần 3) sau khi cắt lời.

## CHẶN còn lại (giải thích)
| Luật | Kết quả | Giải thích |
|---|---|---|
| S01, S05 | MISSING | kind mô hình `rent-buy-twin-replay` chưa có ở `checks/py/r_model.py KINDS` — ghi trước từ M5 (REVIEWER C2); phiên K kind mới |
| S04 | MISSING | không có chuỗi đối chiếu thứ hai (hồ sơ #20) — ghi trước |
| S03 | TRƯỢT: "cross-check on a declared host" | cùng gốc S04 (không có tệp vai crosscheck); phần tệp/host chính ĐẠT |
| A14 | TRƯỢT: 1/112 từ khoá — "2016" ở S12.1 "mid-2016" → ASR "mid -2016" | chủ dự án G2 câu 1: **giữ "mid-2016"** (ASR nghe đúng, chỉ tách chữ) → lô K như A34. "3 out of 4", "2 out of 3": ĐẠT |

## CHÍNH còn lại
| Luật | Kết quả | Giải thích / hướng |
|---|---|---|
| L1 | TRƯỢT 18,5 dB < 20 (M5: 15,1; trung vị 31,1; 16 cửa sổ có tiếng dữ liệu; 0 từ khoá mất) | tiếng dữ liệu đã hạ 6 dB, còn thiếu 1,5 dB ở phân vị 10. Sửa = hạ thêm `data_db` 31 → 34 + trộn lại (hình giữ nguyên, ≈ 40 phút máy) → master mới, giao lại + chạy lại L1/A* — **G3 câu hỏi**, không tự làm (master đã giao) |
| V03 | TRƯỢT 405 mẫu chữ sát mép vùng an toàn | chủ yếu dòng chrome "US only…" (mực x 95 < 96, 1 px — nhà máy) + nhãn đồ thị sát mép; như M5 |
| V11 | TRƯỢT 1.156 va chạm chữ × hình 3D | chữ/chrome đè vật 3D (nhà, lưới) — loại cũ Tập 6–7; một phần do máy tiến/thở |
| V12 | TRƯỢT 7 mẫu NCC < 0,97 (M5 540p: 4.776) | 7 mẫu chữ trôi khi máy chạy (S30 "Nina's first month", "rent"); tĩnh/trôi trung vị 1,0 |
| V09 | ERROR `ValueError … 'nu'` | lỗi công cụ checks: một nhân vật thấy trên trang nhưng `mainColour = None` → `hex_rgb(None)`. Khoá chữ thường đã đúng (Nina/Marcus/Priya được thấy) → khiếu nại lô K |

## THAM KHẢO đáng nêu
R07 58,7 % cue hình ±0,2 s (ngưỡng tham khảo 92 %) · R09 5 chuyển hồi cắt cứng (J/L-cut lệch G1 — đã nêu) · A09 (trên) · T2–T4 sfx tổng hợp lặp/dày · V14, V17, C11 như M5 · T1 MISSING (`sonification.bandsHz` chưa khai).

## Kết luận
0 CHẶN chưa giải thích: S01 S04 S05 (+ S03 cùng gốc) = hợp đồng chưa có, ghi trước; A14 = lựa chọn của chủ dự án ở G2. CHÍNH: L1 thiếu 1,5 dB (câu hỏi G3), V03/V11/V12 loại cũ, V09 lỗi công cụ.
