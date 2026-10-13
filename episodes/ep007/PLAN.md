# PLAN Tập 7 — 30-Year Mortgage Paid Off in 15 Years: What It Really Costs (≤ 1 trang)

**Nhánh:** `ep007` · **Đề tài:** #13 · **Format:** `lab` · **Phiên vừa đóng:** P3 (`session_01PyBa4wV9BaBLVGdCDRJC6K`) — **dừng ở G2** · Lịch sử: `archive/PLAN-history.md`

## 1. Trạng thái
**G2 chờ chủ dự án** (`gates/G2.md`, REVIEWER `gates/REVIEW-G2.md` áp đủ). Bản 1080p 606,7 s (10:06,7), MR1 191,3 / MR2 443,4 s, −14,0 LUFS; Shorts SH1 (B06–B07), SH2 (B30); SH3 bỏ. Cổng gốc bản cuối **5–7/21** (C4 tốt nhất 16/21; hồi quy 10 nhịp sau sửa C5 theo đạo diễn). Chưa đạt: S21 lớp trả thêm (C3 câu 1, quá 3 vòng), S25 "phải vượt" 2/2 (C3 câu 5; lời S25.4/tên "the bar"). Checks Python: CHẶN A14 (S15.3, S25.2 "Tessa's" — A34), F11 (gói P4); bộ lấy mẫu trang chưa chạy. Master 1080p `out/video.mp4` **chỉ ở container** (không commit).

## 2. Việc tiếp (≤ 3) và việc treo
1. Chép câu trả lời G2 → `gates/G2-answer.md`; áp (hoàn 10 cảnh? sửa "her" ×2 cho A14? S25 giữ/sửa S25.4?).
2. P4: gói ChatGPT (`packaging.md` §7), **checks đủ bộ có bộ lấy mẫu trang** (≈ 6–8 h ở 1080p, `RESUME=1` khi bị cắt), giao hàng, G3, merge `main` **squash** (lịch sử `ep007` có ≈ 300 MB tệp nặng).
3. Lô K Tập 8: A34 (A14 tên riêng sở hữu cách), A29 (`checks-k43` @3a00e91: chưa đạt tiêu chí so byte, Tập 6 chưa thử).
- Treo: `api.sh` không chặn agent con trong headless (hai lượt C5 dùng) — việc nhà máy; F-14 (Tập 8).

## 3. Quyết định đã có (chủ dự án)
G1 → `gates/G1-answer.md` · C3 → `gates/C3-answer.md` · 12–13/10 giữa chặng (lời S25.5/S31.3, phạm vi C5, A29 chỉ Tập 7, A34, SH3 bỏ, S25 không sửa thêm, G2 ngay, push sau mỗi bước, dừng tiến trình theo PID) → `gates/C4-answer.md`.

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C4 v1–v3 | S21 | lớp trả thêm không thấy (CHÍNH) | tấm sáng · tờ đô la · cận cảnh | extra 0/2 mọi vòng | G2 trước/sau |
| C4 r1–r4 | a–g | bố cục, F-2, S01/S06/S09/S23/S25/S31 | `briefs/builder-c4-*` | cổng gốc 16/21 | — |
| C5 r1 | cả tập | đạo diễn lặp CHÍNH, đúng-số S13/S30 | `briefs/builder-c5-r1{A,B}` | **5–7/21 (hồi quy 10 nhịp)** | G2 |
| C5 | S25/S31 lời | "clears" | S25.5/S31.3 | must_beat 2/2 vẫn | G2 |
| C5 | A14 | ASR "Tessa's" | seed khác 5 cảnh | còn S15.3, S25.2 | "her" hoặc A34 |
| C5 | d, f, g 1080p | C14, F-2, cache hỏng (đĩa đầy) | chú giải, nhãn, xoá cache | verify 7/7 | — |

## 5. Mức cảnh báo, token, chi (`lab`: 15 triệu · Console $45)
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless | Console |
|---|---|---|---|---|---|---|---|
| P1 | 11/10 13:49 | 0,10 | 0,32 | 27,51 | 0,41 triệu | 0,81 triệu | ≈ $8,9 |
| P2 | 11/10 15:32 | ≥ 0,08 | ≥ 0,28 | ≥ 34,79 | ≥ 0,36 triệu | ≈ 0,5 triệu | ≈ $22,3 |
| P3 | 13/10 | **chưa đọc được** | **chưa đọc được** | **chưa đọc được** | **chưa đọc được** | 189 lượt (kiểm mù, đạo diễn) | **≈ $83,5** |
P3: một lượt kéo dài ≈ 2 ngày → log chưa có sự kiện `result` (`episode.md` §8: chỉ ghi được đến lượt trước) — P4 đọc bằng `list_events(kinds=["result"])` + `from_events.py --session session_01PyBa4wV9BaBLVGdCDRJC6K`. **Cả tập Console ≈ $115** (chủ dự án biết 12/10). EL: dư 66.164 / 144.034 (làm mới 01/11). Giờ máy P3 ≈ 30 h.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/prompts/P3.md` (chặng P4) 4. `episodes/ep007/PLAN.md` 5. `episodes/ep007/gates/G2.md` 6. `episodes/ep007/gates/G2-answer.md` 7. `episodes/ep007/gates/C4-answer.md` 8. `playbook/packaging.md` §7

## 7. Prompt phiên kế (D-011)
```
Chạy Tập 7, phiên P4 (áp G2 → gói ChatGPT → checks đủ bộ → giao hàng → G3). Nhánh ep007. Mở bằng `bash toolkit/verify.sh ep007`; đọc mục 6 của episodes/ep007/PLAN.md.
Gói đã gửi: episodes/ep007/gates/G2.md. Việc đầu tiên: chép câu trả lời dưới đây vào episodes/ep007/gates/G2-answer.md, ghi taste-ledger.md, AUTHORSHIP.md, ledger; commit, push.
Master 1080p chỉ ở container P3 (out/video.mp4, không commit): còn tệp thì chạy tiếp ở đó (D-011); mất thì dựng lại `bash toolkit/build.sh episodes/ep007/episode.yaml` (res 1080; ≈ 4–5 h, chạy tiếp được) rồi `c5/shorts_only.py`.
Đọc 4 số token của P3 (session_01PyBa4wV9BaBLVGdCDRJC6K) ghi vào PLAN §5. Checks đủ bộ có bộ lấy mẫu trang trước giao hàng (RESUME=1 khi bị cắt). Merge main sau G3: squash.
Việc nặng: headless khoá Console (toolkit/api.sh), 0 agent con; dừng tiến trình bằng PID đã lưu; push sau mỗi bước lớn.
Câu trả lời G2:
<<DÁN CÂU TRẢ LỜI G2 Ở ĐÂY>>
```
