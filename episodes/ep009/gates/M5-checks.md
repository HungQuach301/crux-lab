# M5 Tập 9 — checks ĐỦ BỘ trên bản (b) 1080p có `cine` (LOCK K4.4.1 `eb6d0fce…`) — 16/10

Bản: `out/video.mp4` (SHA-256 `62f157fb67156842…`, 523,9 s, 1920×1080). Lệnh: `EP=episodes/ep009 bash toolkit/checks_split.sh /home/user/chk-ep009` (4 lượt: trần 2 h ×3, container khởi động lại ×1; trang kiểm sửa giữa chừng — nhà máy `episode_page` đặt `?seg=` từng đoạn). Báo cáo đủ: `gates/checks-1080/report.{json,md}`.
**Kết quả: ĐẠT 45 · TRƯỢT 45 · MISSING 14 · ERROR 1 → TRƯỢT.**

## CHẶN
| Luật | Loại | Chi tiết | Xử lý |
|---|---|---|---|
| S01, S05, S04 | MISSING — **ghi trước (A48)** | kind `rent-buy-twin-replay` chưa có ở KINDS; không khai `data.crosscheck` | lô K (A48), không sửa luật |
| **A14** | thật | S02.2 "3 in 4" → ASR "three and four" (đã biết, 2 seed); S14.2 "stock piles" → "stockpiles" | G2 câu 2 (đổi lời) |
| **S07** | thật | 14 số trên hình chưa gắn claim ("$1", "$1 in 1991 → almost 5 times", "2.5%", "6%", "5%" thẻ, "June 2006", "April 2012", "80 switched…", "5 years"…) + 6 số nói chưa đăng ký | M6: gắn claim/tham số (mã nhãn, không đổi hình) |
| **S09** | thật | gốc tiền "danh nghĩa" (mọi $) chưa nói trong lời | G2 câu 3 (tiền lệ Tập 8: ", in dollars of the day") |
| **C07** | thật | 434 khung "cột tràn khung theo trục giá trị": tường cột 0:05–0:52 (S01–S03 + ident), hàng đống thấp S14 (239 khung) | M6: hạ thang tường cột / khung cBars (hình) |
| F10, F11, SH01–05, REG | thủ tục M6 | gói chữ, Short SH1, giao hàng, lần đầu | M6 |

## CHÍNH
| Luật | Chi tiết | Xử lý |
|---|---|---|
| **F07** | 523,9 s < 540 (`lab` 9–11 phút) | G2 câu 4 (không độn; G1 cho `--g1-short`) |
| **S23** | "has to" trong S18.4 "…the pile has to compound…" (mẫu "have to") | G2 câu 5 (đổi chữ; không thêm `allowTerms` sau khi thấy kết quả — ý đồ §1) |
| **V03** | 206 mẫu chữ ngoài vùng an toàn | M6 (nhãn) |
| **V11** | 1.667 va chạm chữ × hình (Tập 8: 1.135) | M6 (một phần do máy tiến chậm `hold_push`, như Tập 8) |
| **V12** (đo lần đầu với `cine`) | 543 mẫu NCC < 0,97 (tĩnh p05 0,989; đang chuyển động p05 0,934); thấp nhất S14 "lowest point of each pile…" NCC −0,01 (d1 **không** có lớp), S04 "first house: dark" 0,841 (b1 có lớp) | báo — 10 mẫu thấp nhất: 9 ở b1 (có lớp), 1 ở d1; chưa có số theo đoạn cho cả 543 mẫu → chưa tách phần do `cine` |
| A18, S21 | thủ tục (M6) | M6 |

**Bước `cine` (build_seg, ΔE2000 ≤ 5, không đảo độ sáng):** a1, b1, f2 ĐẠT; **d1 CHẶN 2 vòng → TẮT lớp ở S14–S15** (khung có lớp `gates/G2-assets/cine-d1-on-t12.jpg`). Tỉ lệ `cine` thật: S01–S02 + S04 + S25 = 22,7 + 32,4 + 32,4 ≈ **87,5 s = 16,7 %** (lệnh chặng 5 cảnh → còn 3 đoạn / 4 cảnh).
**Âm:** −14,1 LUFS · AAC −2,2 dBTP (≤ −2,0, một lượt) · L1 ĐẠT (checks; đo tay lời/dữ liệu 1–4 kHz p10 74,6 dB) · T3, T4 TRƯỢT (THAM KHẢO/không chặn).
