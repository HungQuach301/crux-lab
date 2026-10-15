# PLAN Tập 8 — Rent vs Buy, replayed (#20) (≤ 1 trang)

**Nhánh:** `ep008` · **Đề tài:** #20 · **Format:** `lab` · **Mô hình:** xưởng 6 mốc (D-013) · **Chặng vừa đóng:** sau G1 → **dừng ở G2** (`session_01D3z2xMwUwt9NXv8xLDkV6d`)

## 1. Trạng thái
**G2 chờ chủ dự án** (`gates/G2.md`, REVIEWER lượt 2 ĐẠT có sửa — đã áp; nháp r2 `review-g2/draft-540p.mp4` 10:26). M2: cold open v3 + kiểm mù lời 6/6, 0 khuyên; animatic xám, cổng gốc 19/24 (5 nhịp so sánh giữa cảnh → G2). M3–M4: nháp màu theo hồi (`grade8.js`), giọng một lần (S13 seed 1009). M5: nhịp ĐẠT sau 2 vòng (freezedetect 0 s, spine 0); nhớ lại 3/3; **chỗ muốn tua TRƯỢT** (vòng hình r3 S07 không vượt r2 → hoàn; cắt lời → G2 câu 5); cổng gốc chẩn đoán 17/24, 0 khuyên; liền mạch ĐẠT trừ J/L-cut; đạo diễn chẩn đoán; checks đủ bộ khoá `a35970a8` TRƯỢT (ngoài S01 S04 S05 ghi trước: S03 S06 S07 S09 A14 + mục M6; `gates/M5-checks.md`, báo cáo `review-m5/checks-r2/`).

## 2. Việc tiếp (≤ 3) và việc treo
1. Chép G2 → `gates/G2-answer.md`; áp lựa chọn (câu 1 "out of", câu 5 cắt lời, câu 6 "dollars of the day", câu 7 S23 allowTerms, màu câu 3/8); sinh lại giọng các câu đổi.
2. M6: S06 coverage, nhãn claim trên hình (S07), chrome basis (S09), hạ tiếng dữ liệu (L1), −2,0 dBTP → dựng 1080p + Short SH1 + mô tả → checks đủ bộ 1080p (`--baseline review-m5/checks-r2/report.json`; luật độ phân giải F05 F08 R03 R04 V05 V10 V08 V12 C14) → G3.
3. Khi K4.4b vào `main`: merge vào `ep008` trước checks đủ bộ (lệnh 14/10).
- Treo: J/L-cut qua biên đoạn (nhà máy `splice.py`, BACKLOG); tiếng ghi thật (cần tài khoản Freesound); kind `rent-buy-twin-replay` chưa có ở `checks/CONTRACT.md` (phiên K).

## 3. Quyết định đã có (chủ dự án)
- 13/10 G1 (`gates/G1-answer.md`): HVS xác minh; kịch bản v2 + cold open mới; T1; N1/N2 vào thư viện, N4 v2 + "cash, not stocks", bỏ N5; footage chỉ bản đồ NE; không C3; 1 Short; không thumbnail.
- 14/10 (`gates/update-14-10.md`): cổng gốc khi so hai bản = chẩn đoán, không vòng thêm; G2 nêu nhịp lật + khung trước/sau; L3 là thước cuối.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| M2 r1→r2 | lưới/phố | không biết sáng/tối nghĩa gì; B32 khuyên | chú giải lit/dark, nhãn có chủ ngữ, dòng bảng điểm | 13 → 19/24, 0 khuyên | 5 nhịp → G2 |
| M5 nhịp r1 | cả tập | freezedetect 282 s, 9 quãng > 8 s | máy tiến chậm khi đứng; 9 thay đổi major ở từ mở ý | 67,9 s; 0 quãng | đồ thị |
| M5 nhịp r2 | đồ thị | quãng đồ thị dài đứng | "thở" 0 ↔ 2,5 % (cStacks 1,2 %: verify F-2) | 0 s | "đổi vì thước" → G2 |

## 5. Mức cảnh báo, token, chi (`lab`: 15 triệu · Console $45; **chặng trần CỨNG $25**)
| Chặng | Console | Theo mốc | EL | Giờ máy |
|---|---|---|---|---|
| sau G1 → G2 | **$11,10** / $25 (`logs/usage/spend_leg.py`) | M2 ≈ $5,74 (WRITER cold open $3,37, kiểm mù, cổng gốc ×2) · M3–M4 $0 · M5 ≈ $5,36 (REVIEWER ý đồ $0,69, cổng gốc, nhớ lại/tua ×2, đạo diễn $0,26, REVIEWER G2 ×2 $1,74) | đã dùng 98.214 / 144.034 (còn 45.820, làm mới 01/11) | nháp 4 lần ≈ 6 h; checks ≈ 6,5 h; 2 lần container khởi động lại |
| sau G2 → G3 (14–15/10) | **≈ $2,03** (spend_leg 13,13 − 11,10) · **cả tập ≈ $19,4** / $25 | M6: cổng gốc 1080p ≈ $1,6 · nhớ lại/tua ≈ $0,45 · dựng/checks $0 (máy) · REVIEWER G3 chưa chạy | 1.943 ký tự (6 cảnh sinh lại); còn ≈ 42.700 | dựng 1080p ≈ 6,5 h; checks 1080p ≈ 8 h+ |
Token phiên: đọc ở chặng sau bằng `list_events(session_id="session_01D3z2xMwUwt9NXv8xLDkV6d", kinds=["result"])` → `toolkit/usage/from_events.py`. Agent con 0 (api.sh `--disallowedTools "Task,Agent"`).

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/quality-framework.md` 4. `episodes/ep008/PLAN.md` 5. `episodes/ep008/gates/G2.md` 6. `episodes/ep008/gates/G2-answer.md` 7. `episodes/ep008/gates/M5-pace.md` 8. `episodes/ep008/gates/M5-checks.md`

## 7. Prompt phiên kế (D-011)
```
Chạy Tập 8 — sau G2 (mô hình xưởng 6 mốc). Nhánh ep008 (@ <HEAD> hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep008`; đọc mục 6 của episodes/ep008/PLAN.md.
Việc đầu tiên: chép câu trả lời G2 dưới đây vào episodes/ep008/gates/G2-answer.md; ghi taste-ledger.md, AUTHORSHIP.md, ledger; đọc token chặng trước (PLAN §5); commit, push. Khi K4.4b đã vào main: merge vào ep008 trước checks đủ bộ.
Chặng này: áp G2 → M6 (1080p, Short SH1, checks đủ bộ 1080p) → G3. Trần chi theo lệnh chủ dự án; headless khoá Console, 0 agent con; dừng tiến trình bằng PID.
Câu trả lời G2:
<<DÁN CÂU TRẢ LỜI G2 Ở ĐÂY>>
```
