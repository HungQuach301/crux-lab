# PLAN Tập 9 — Rent and invest the difference (tiếp Tập 8, gần #21) (≤ 1 trang)

**Nhánh:** `ccr-4d8bc942-73gdnl` (lệnh phiên; main 5c8093ac đã merge) · **Format:** `lab` · **Mô hình:** xưởng 6 mốc (D-013) · **Chặng vừa đóng:** sau G1 → G2 (**G2 trả lời 17/10**) (`session_01KBz3## 1. Mốc hiện tại
**G2 ĐÃ TRẢ LỜI (17/10, `gates/G2-answer.md`)** → chặng kế **M6 → G3**, phiên mới. **Trần M6 $8 cứng.**

## 2. Việc tiếp (≤ 3) và việc treo
1. Lời: sửa `story/script.md` theo G2 câu 2, 3, 6 (S02.2, S04.2, S14.2, S14.4–5 gộp, bỏ S18.4, rút S24.1) + nhãn "3 out of 4" (đoạn a, f bảng điểm) → **kiểm EL trước** → `prod/voice.py` (S02 S04 S14 S18 S24) → `prod/anchor_gap.py` → `build_inputs.py --timeline` → mid-roll (S18 đổi) + nhạc `--bed` + SH1 from/to.
2. Hình (một lượt 1080p, `CRUX_GREY=0 RES=1080 bash prod/animatic.sh`, chạy tiếp được): S07 gắn claim/tham số cho 14 số trên hình (`gates/checks-1080/report.json` S07) · C07 thang tường cột (a, f) + khung hàng đống (d) · V03/V11 nhãn · `splice.py --transitions out/factory/splice.json out/transitions.json` → `build_inputs.py --out` → checks đủ bộ 1080p (`RESUME=1 KEEP=1`, cache A29) — `cine` đo bằng bước `cine`, SSIM chỉ cảnh không lớp (ý đồ M5 CH6).
3. Short SH1 (`build.sh` không `--no-shorts`) · gói chữ (mô tả: ghi công "Origami" đúng mẫu `G1-answer.md` + "Stock returns: Kenneth R. French Data Library (Fama/French factors, total return); cross-checked with Robert Shiller data.") · `package_check.py` · giao `deliver.py` nhánh tạm `ep009-delivery` (+ 720p) → gói G3 (phiếu L3 chủ dự án chấm ở G3; ngoại lệ F07 ghi sẵn).
- Treo: lô K A47–A49 (A48: S01/S04/S05 MISSING) + đề xuất V12 theo đoạn (lessons T9-2); A32 nhiễu người chấm; lessons T9-3 (câu "chỗ muốn tua" vào kiểm mù C2) → Tổng kết.

## 3. Quyết định đã có
- 15/10 G1 (`gates/G1-answer.md`) + sửa câu 1 15/10 (không thư; kết quả suy ra; câu nguồn trên hình S24 + mô tả).
- 15/10 lệnh chặng sau G1 (animatic trước M3, vòng 2 số dày, EL, Origami, J/L 7, cine, data_db 34, aac_true_peak, sfx_real, trần $15).
- **17/10 G2 (`gates/G2-answer.md`):** Content ID 0 claim · đổi/cắt lời 2, 3, 6 (không xem lại) · giữ 8:44 = ngoại lệ F07 chủ dự án · giữ "Last time" · `cine` d1 tắt · SH1 duyệt (mốc theo 6c) · L3 chấm ở G3 · M6 một lượt 1080p, trần $8.

 sfx_real; trần $15.

## 4. Đã sửa gì, vì sao
| Vòng | Chỗ | Lỗi (đo) | Sửa | Sau |
|---|---|---|---|---|
| C2 v5 | S10–S17 | số dày 5/6 | bớt mốc năm/số nói, giữ hình | số dày 1/6, khuyên 0/6 |
| M2 cổng gốc r1→r2 | 17 nhịp | 10/27, B35 khuyên | hình (tường cột, nhà đầu phố, bó rơi) + nhãn không số | **17/27** (r1 10/27; sửa đếm 16/10), 0 khuyên; 10 nhịp hết vòng → G2 |
| M3 lời | S02 | ASR "three and four" (2 seed) | giữ take G1 | → G2 câu hỏi |
| M3 neo | S04.3 S14.3 S15.2 | neo giữa cảnh, không khe | take dẫn xuất chèn lặng (0 ký tự) | lặng 0,8 s |
| M5 nhịp | cả tập | freezedetect 260,5 s | hold_push (Tập 8) vào w9 | **25,3 s**; quãng > 8 s: 2 → 0 |
| M5 tua r1 | S03 S24 S25 | 3/3 muốn tua (lý do ở lời) | S24 thẻ 4 dòng đã nói, S25 phố đổi đèn theo bảng điểm | đo lại trên 1080p |
| M5 1080 | a1, b1 | C14 chú giải, F-2 | nền chữ, so le | dựng lại |

## 5. Sổ chi theo mốc (`lab`: 15 triệu · Console $45; **chặng trần CỨNG $15**)
| Mốc | Console | Chi tiết | EL | Giờ máy |
|---|---|---|---|---|
| M1–G1 (chặng trước) | $7,93 | | 3.058 | |
| M2 animatic | ≈ $3,3 | cổng gốc r1 + r2 + người 3 (headless) | 0 (take khô) | animatic ≈ 3 × 70 phút |
| C2 v5 + lời | $1,05 | WRITER $0,75 · kiểm mù r5 ≈ $0,3 | **5.772** (5.537 + 235 thử seed) | |
| M5 + G2 | ≈ $4.18 | REVIEWER ý đồ $0,37 · cổng gốc nháp ≈ $2,3 · nhớ lại/tua ×2 · đạo diễn $0,26 · REVIEWER G2 $0.88 | 0 | nháp 540p × 2 ≈ 2,3 h; 1080p ≈ 12 h (5 lượt); checks ≈ 8 h (4 lượt) |
Cộng chặng ≈ **$8.51 / $15** (gồm REVIEWER G2). EL còn 22.183 (làm mới 01/11). Agent con 0. Lượt phiên > 150 (vượt mức cảnh báo — ghi ở G2). Container khởi động lại 3 lần (16/10). Sửa nhà máy giữa tập (CHẶN): build.py argv; episode_page ?seg=. Lượt chạm chủ dự án chặng này: 2 (lệnh mở, sửa G1 câu 1).

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `episodes/ep009/PLAN.md` 4. `episodes/ep009/gates/G2-answer.md` 5. `episodes/ep009/gates/G2.md` 6. `episodes/ep009/gates/M5-checks.md` 7. `episodes/ep009/story/script.md` 8. `episodes/ep009/gates/G1-answer.md`

## 7. Mở chặng kế
`playbook/prompts/CHAY-TAP-N.md`: "Chạy Tập 9 — sau G2." (G2 đã chép). Bàn giao: `out/video.mp4` 1080p hiện tại + cache render chỉ ở container này (`work/`, không commit) — container mới thì dựng lại theo `episode.yaml` (≈ 12 h 1080p có lớp); take dẫn xuất `voice-takes/gap-*` + take thật đã commit. Token phiên này: `list_events(session_id="session_01KBz3MgLiozdsrE1ZXPmEMX", kinds=["result"])` → `toolkit/usage/from_events.py`.
