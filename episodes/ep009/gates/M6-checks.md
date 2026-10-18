# M6 — checks đủ bộ 1080p · Tập 9 · 18/10

Master `1a21c9e42d9fcc3fd5c4cbe78ee748b85963be91242cda5b1ac8afb3db12aa13` (511,3 s), khoá `eb6d0fce…` (K4.4.1), bộ lấy mẫu trang đủ 26 cảnh, baseline = `gates/checks-1080/report.json` (M5, video `62f157fb…`). Báo cáo: `gates/checks-m6/report.{json,md}`.

**ĐẠT 62 · TRƯỢT 38 · MISSING 4 · ERROR 1** (M5 1080p: ĐẠT 45 · TRƯỢT 45 · MISSING 14 · ERROR 1).

- **Hết trượt (18):** F10, F11 (`out/voice/takes.json` vào git như Tập 8), A13, A14, A18, **S07** (claim cho số trên hình + số nói), S09, S21, S23, SH01–SH05 (Short), **V03**, **C07**, T4, REG (có baseline).
- **Trượt mới (1):** L1 (M5 MISSING → đo được trên 1080p): 17,6 dB < 20.
- **CHẶN:** chỉ còn S01, S04, S05 MISSING (hợp đồng chưa có — như Tập 8, lô K A47–A49). **0 CHẶN thật.**
- **CHÍNH trượt, có giải thích (`out/explanations.json`):** F07 (8:31 < 9:00, ngoại lệ chủ dự án ở G2) · V11 1.617 va chạm chữ × hình 3D (dòng chrome và nhãn không nền trên thế giới 3D, loại cũ Tập 6–8) · V12 564 mẫu NCC < 0,97 (máy trôi/thẻ chương; tĩnh P05 0,982) · **L1 17,6 dB** → câu hỏi G3.
- **THAM KHẢO:** 34 trượt, chỉ báo số đo (A10–A17 nhịp lời, R01–R09 nhịp cắt, C04 trục, C15…); R09 "chuyển hồi cắt thẳng 3" — J/L-cut qua biên đoạn đã ghi `out/transitions.json` (7 mối), loại nhà máy BACKLOG như Tập 8.

## Sửa trong M6 và cách sửa
| Luật | Lỗi (M5) | Sửa | Đổi điểm ảnh? |
|---|---|---|---|
| S07 | 14 số trên hình không claim, 6 số nói | nhãn mang claim (tham số `hold_5y`, `start_2006_06`, `start_2012_04`; thẻ chi phí có claim; bỏ nhãn "$1"); claim lời S03.5 S04.1 S09.3 S10.1 S15.2 | có (chữ nhãn) |
| C07 | 434 khung "cột tràn trục giá trị" | tường cột: hộp bao cả khối InstancedMesh → 16 khúc "bóng" role `bar` ở layer 31 (không camera nào vẽ) + nhóm cha role `grid` (cine vẫn coi là dữ liệu); đống cổ phiếu chỉ khai các bó (không cọc); khung cBars rộng hơn | **không** — 7 khung 1080p (5 có cine) trùng 100 % bản trước |
| V03 | 206 mẫu chữ ngoài vùng an toàn | nhãn kẹp trong 96–1824 px; "$92,000 start" (bị cắt chữ "start" sau khi nới khung cBars — bắt được ở checks lượt 1) | có |
| R09 | `out/transitions.json` không có J/L | `splice.py --transitions` | không |

**1080p chạy lần 2 (luật Line producer — lý do ghi tại đây):** sửa đo C07 đổi `w9.js` → khoá cache render của cả 10 đoạn đổi → dựng lại toàn bộ (≈ 7 h) dù điểm ảnh không đổi; kèm sửa nhãn S14 (lỗi thật). So master trước (`e2ff7cf3…`): đoạn không cine trùng 100 %; đoạn cine lệch ≤ 60/255 rải toàn khung (hạt/dither của lớp cine giữa hai lượt), d đổi nhãn S14.

## Short SH1 (qc nhà máy)
29,8 s · sàn chữ 56 px ĐẠT · tương phản 7,5:1 · vùng an toàn 0 · ILLUSTRATIVE/history 0 khung thiếu · đối trọng 3/3 ≥ 30 khung · −13,9 LUFS / −2,2 dBTP.

## qc nhà máy, mục báo TRƯỢT không áp
"master đối trọng 0 khung log" ×3 — qc chỉ đếm khung 2D, tập toàn khung thế giới 3D (như Tập 8; checks S-rules đếm đủ) · "phần 720p > 90 MB" — phần của nhà máy không dùng; giao bằng phần cắt byte 90 MB + xem trước 720p 2,5 Mbps (≈ 55 MB/phần).
