# K-PLAN — phiên K lô sau tổng kết Tập 5 (08/10/2026) · ≤ 1 trang

**Nhánh:** `claude/phase-k-after-episode-5-frjcpw` (lệnh ghi `checks-k40`; phiên chạy trên nhánh được giao) · **main:** `2c5eacf` (K4.0.1, LOCK `79aeec0d…`) · **nhánh:** đầu nhánh (+ nhóm 1 K4.1, chưa merge)

## 1. Trạng thái
- **Nhóm 2 XONG, đã merge main** (D-008 §2):
  - K4.0 `329eedd` → K4.0.1 `2c5eacf` sửa theo REVIEWER.
  - Luật mới, theo cấp:
    - S19 CHẶN;
    - S20, S21 CHÍNH;
    - V14, R07, R08, T4, V15, V17, S22 THAM KHẢO (chỉ báo, nêu tên ở `checks/README.md`).
  - Selftest Python 328/328, trang 64/64.
  - 89/89 luật cũ trùng fingerprint và cấp; trước/sau trên Tập 3–5 trùng.
  - Tập 5 C5c dựng lại: mọi số đếm luật trang trùng run-c5c.
  - Hồi tố chỉ báo, không sửa tập đã phát hành.
- **Nhóm 1 sẵn trên nhánh, CHƯA merge** (gói `checks-runs/K41/GOI-chu-du-an.md`, 3 câu):
  - A22: V11 Tập 5 từ 2612 xuống 359;
  - A10 + A16: F11 đọc danh sách từ nhà máy;
  - A9 + A21: rubric khuyên ba cờ.
  - Selftest Python 336/336 trên nhánh.
- **Nhóm 3:** A12 xong (K4.0). A15 nằm ở REVIEWER mục 9, trên nhánh.
- **REVIEWER:**
  - K4.0: ĐẠT có sửa, 2 CHÍNH đã sửa ở K4.0.1.
  - Nhóm 1, lần cuối: ĐẠT có sửa, 0 CHẶN, 0 CHÍNH.

## 2. Việc tiếp (≤ 3) và treo
1. Dán câu trả lời 3 câu vào `checks-runs/K41/GOI-answer.md`. Áp các câu "Có" → khoá **K4.1**: LOCK, README mục K4.1, merge main, kiểm SHA. Câu "Không" → revert phần đó trên nhánh trước khi khoá.
2. **Kind Tập 6:** `origin/ep006:episodes/ep006/K-brief.md` (có, @ `26278228`). Cần kind mới: khoản trả tăng tỉ lệ cố định mỗi năm so với chỉ số giá tháng, mọi cửa sổ H năm. Viết từ đặc tả `topics-r1/machine/retire-1/model.json → newKindNeeds`. Bất biến: ô CPI trống là THIẾU (715 = 716 − 1), hoà lấy tháng sớm nhất. Luật tập 3 của brief → `claims.forbiddenAmounts` (S19). Tự merge nếu chỉ thêm. **Trước C3 Tập 6** (D-011 Q3).
3. Treo:
   - selftest chứng minh `plateOverGraphics > 0` ở ca badge-on-series (REVIEWER THAM KHẢO 6), làm trước khi merge K4.1;
   - F11 nhà máy chạy trên cây C5 đủ media (G2 Tập 6);
   - R07 cần hộp đối tượng theo cue;
   - V14 rule1 cần `chartW`;
   - dải chrome ghi thành `card`, việc của bên dựng (để V11 về 0).
   - Còn mở: A5, A7, A8, A23 (cờ `change` trên spine).

## 3. Quyết định đã có
- 08/10 D-011 Q3: phiên K lô song song Tập 6 P1, merge trước C3.
- D-008 §2: nhóm 2 tự merge. Nhóm 1 sửa luật cũ nên hỏi chủ dự án.

## 5. Token (log phiên, đọc từ transcript cục bộ đến 17:58 UTC; chưa có sự kiện `result` vì phiên một lượt)
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần |
|---|---|---|---|---|---|
| K lô 08/10 (gồm 3 agent con) | 17:58 | 170.090 | 757.341 | 80.464.818 | **927.431** |

Agent con: chấm khuyên 0,06 tr, REVIEWER 0,15 tr và 0,10 tr (cỡ ngữ cảnh do công cụ báo). Giờ máy: selftest 2 × 21–24 phút; lấy mẫu trang Tập 5 42,6 và 59,4 phút; ASR R07 Tập 5 ≈ 6 phút.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md`
2. `decisions/D-008.md`
3. `checks/README.md` (mục K4.0, K4.0.1)
4. `checks-runs/K41/GOI-chu-du-an.md`
5. `K-PLAN.md` (tệp này)
6. `checks-appeal.md` (khối K4.0)
7. `origin/ep006:episodes/ep006/K-brief.md`
8. `topics-r1/machine/retire-1/model.json`

## 7. Prompt phiên kế
```
Phiên K tiếp (K4.1 + kind Tập 6). Nhánh claude/phase-k-after-episode-5-frjcpw (đầu nhánh = commit đóng phiên K 08/10; main @ 2c5eacf, LOCK 79aeec0d). Mở bằng `bash toolkit/verify.sh`; đọc mục 6 của K-PLAN.md.
Việc đầu tiên: chép câu trả lời dưới đây vào checks-runs/K41/GOI-answer.md, commit, push.
1. Nhóm 1 (K4.1): áp câu "Có"; câu "Không" → revert phần đó trên nhánh. Làm việc treo REVIEWER 6 (selftest plateOverGraphics). Chạy selftest đủ bộ, cập nhật checks/README.md mục K4.1 + LOCK, REVIEWER, merge main, kiểm SHA LOCK trên main.
2. Kind Tập 6 từ episodes/ep006/K-brief.md trên origin/ep006 (nếu chưa có thì ghi rõ "chờ" và dừng phần này): viết kind từ đặc tả, selftest tính tay, S01/S05 trên dữ liệu thật Tập 6 0 lệch, luật tập 3 qua claims.forbiddenAmounts; chỉ thêm → tự merge main theo D-008 §2 trước C3 Tập 6.
Đóng phiên theo D-011: K-PLAN ≤ 1 trang, 4 số token, prompt phiên kế. DỪNG.
Câu trả lời gói K4.1 (checks-runs/K41/GOI-chu-du-an.md):
<<DÁN CÂU TRẢ LỜI GÓI K4.1 Ở ĐÂY>>
```
