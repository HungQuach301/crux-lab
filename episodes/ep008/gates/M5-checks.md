# M5 Tập 8 — checks ĐỦ BỘ trên nháp r2 (540p), khoá `a35970a8…` (K4.4; K4.4b chưa vào `main` 14/10)

Lệnh: `EP=episodes/ep008 bash toolkit/checks_split.sh /home/user/chk-ep008` (bản sao khoá; bộ lấy mẫu trang 33 cảnh ≈ 6 h, chạy lại 3 lần với `RESUME=1` vì trần 2 h/lệnh nền) → sửa hồ sơ/hợp đồng (không đổi hình) → `KEEP=1 PYONLY=1` chấm lại trên `page.json` cũ. Báo cáo `/home/user/chk-ep008/episodes/ep008/out/checks/report.{json,md}` (ngoài git).

**Lần 1 (đủ bộ):** ĐẠT 45 · TRƯỢT 38 · MISSING 13 · ERROR 9. **Lần 2 (Python, sau sửa hồ sơ):** ĐẠT 46 · TRƯỢT 37 · MISSING 13 · ERROR 9.

## CHẶN (BLOCK) — theo REVIEWER C2: chỉ S01, S04, S05 được ghi trước; **mọi CHẶN khác là trượt thật** (dưới đây ghi nguyên nhân + nơi sửa, không coi là đạt)
| Luật | Kết quả | Loại | Xử lý |
|---|---|---|---|
| S01, S05 | MISSING | **đã ghi trước** (C2): kind `rent-buy-twin-replay` chưa có ở `r_model.py KINDS` | phiên K kind mới (`K-brief.md`); G2 nêu |
| S04 | MISSING | **đã ghi trước** (C2): không có chuỗi đối chiếu thứ hai (hồ sơ #20) | như trên |
| S03 | TRƯỢT → còn "cross-check on a declared host" | lần 1: `data/sources.json` thiếu `files[]` (hồ sơ dùng `series`) → **đã thêm** 4 tệp FRED ghim (đạt files/host chính); còn đối chiếu = cùng gốc S04 | đã sửa phần sửa được |
| S06 | MISSING | contract chưa khai `coverage[]` | khai ở M6 (hồi 2: năm 1991–2016; hồi 3: thẻ 4/5/6 %) |
| S07 | TRƯỢT: số nói chưa đăng ký 7 → **0**; số trên hình không claim **6** | lần 1 thiếu claim tham số → **đã thêm** `term_30y`, `era_2002-2007_span`, `hold_15y` + đăng ký `yield4_tag`, `yield6_tag`, `rate_month_latest`; 6 số hình ("6 of 72", "15 years", "2002 to 2007", "$2,933" ở S29/S30) cần gắn claim trên nhãn → **trang lấy mẫu lại ở M6** | M6 |
| S09 | TRƯỢT: 14 claim $ thiếu `basis`; 664 khung thiếu nhãn gốc tiền | claim chưa khai nominal/real; chrome chưa bật `basis`; lời chỉ nói "today" (máy đọc là real) | **câu hỏi G2**: các số $ là "dollars of the day" (danh nghĩa) → cần nói một lần ("in dollars of the day") + nhãn chrome "All $ in dollars of the day" — đổi lời là của chủ dự án |
| A14 | ERROR | công cụ: PyAV 19 bỏ tham số `metadata_errors` mà faster-whisper 1.2.1 dùng → đã cài PyAV 16.0.1 (giải mã chạy) | chạy lại A14/L1 (bên dưới) |
| F01 | TRƯỢT `size 960x540` | nháp 540p (đo ở M6, 1080p) | M6 |
| F10, F11, S21 | MISSING/TRƯỢT `description.md` | gói phát hành làm ở M6/P4 | M6 |
| SH01–SH05 | MISSING `out/shorts/SH1.mp4` | Short dựng ở M6 (lệnh G1) | M6 |
| REG | MISSING | lần chạy đầu của tập (chưa có báo cáo nền) | M6 dùng báo cáo này làm `--baseline` |

## CHÍNH (MAJOR)
| Luật | Kết quả | Xử lý |
|---|---|---|
| S23 | "wasted" ×3 (S02.3 lời + màn S02, S32: "Is her rent money wasted?") | **đã ghi trước** (C4): câu lời đã duyệt — giữ CHÍNH, nêu G2; không thêm `allowTerms` sau khi thấy kết quả |
| V09 | nhân vật khai thấy 0/3 | trang ghi khoá `Nina/Marcus/Priya`, hợp đồng `nina/marcus/priya` → **đã sửa** khoá chữ thường (`w8.js figure`); đo lại ở M6. Lưu ý: ba hình người cùng màu thân (FIG) ≠ màu khai → ΔE có thể trượt khi đã thấy — G2 |
| V03 | 402 mẫu chữ ra vùng an toàn | phần lớn dòng chrome "US only…" mực x 95 < 96 (1 px) + nhãn đồ thị sát mép; nhà máy (chrome) → BACKLOG; nhãn tập sửa ở M6 |
| V11 | 1.135 va chạm chữ × hình (nhãn 1.127) | chrome/nhãn đè hình 3D (nhà, lưới) — loại cũ Tập 6–7; một phần do máy tiến/thở (nhãn trôi qua vật) — G2 |
| V12 | 4.776 mẫu NCC < 0,97 | **phụ thuộc độ phân giải (C3)** — 540p chỉ báo, đo ở M6 |
| L1 | ERROR | như A14 |

## THAM KHẢO (chỉ báo) — đáng nêu
R07 ERROR (chạy lại ở M6), R09 TRƯỢT (J/L-cut lệch G1 — `M5-continuity.md`), V14 (3 nhịp 5 s đầu "không ở thế giới" — cold open bắt đầu bằng thế giới rồi vào đồ thị ở 5 s, như thiết kế quy tắc 7), V17 (14 nhãn hiện quá ngắn), C11 (bố cục lặp > 2 trong 90 s: 32 — lưới từ trên dùng nhiều), T2–T4 (sfx dày/lặp — sfx tổng hợp, chưa có tiếng ghi thật), T1 MISSING (`sonification.bandsHz` chưa khai).

## Kết luận
**TRƯỢT** (luật C2): ngoài S01 S04 S05 ghi trước, còn CHẶN trượt thật — S03 (đối chiếu), S06, S07 (hình), S09, A14 (công cụ), và các mục thuộc mốc phát hành M6 (F01 540p, F10/F11 mô tả, SH01–05, REG). CHẶN sửa được bằng hồ sơ đã sửa và đo lại (S02 ĐẠT; S07 lời 0; S03 phần tệp). Còn lại: hợp đồng chưa có (S01 S04 S05, phiên K), M6 (F01 F10 F11 SH S06, S07 hình, V09), **câu hỏi lời S09** (G2), công cụ A14/L1 (chạy lại).
