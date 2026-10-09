# K-PLAN — phiên K (kind Tập 6 + K4.1), 08–09/10/2026 · ≤ 1 trang

**Nhánh:** `claude/phase-k-after-episode-5-frjcpw` (= `main` + commit đóng phiên này) · **main:** K4.1 @ `1678a38`, LOCK `4d688acd…` (đã tính lại trên main, khớp)

## 1. Trạng thái
- **K4.0.2 (kind Tập 6) đã lên main** @ `c54a489`, LOCK `1b83d940…`. Đã báo P3 Tập 6 ở #49.
  - Kind `fixed-raise-vs-index-windows`, viết từ đặc tả. Không đọc `model.py`/`calc.py` của bên dựng.
  - Dữ liệu thật Tập 6: FRED SHA khớp 4/4.
  - S01: 89 khoá, 0 lệch. Claim: 45/45, gồm `worst_window_years_2pct_fell_20y`. Bất biến: 8/8. Đối chứng nhiễu: 8/8.
  - Luật tập 3 qua S19 `forbiddenAmounts`: 83 câu script, 0 vi phạm; câu đối chứng trượt.
  - Selftest Python 334/334, trang 64/64. Fingerprint 99/99 trùng. REVIEWER: ĐẠT có sửa, đã sửa.
- **K4.1 (nhóm 1, chủ dự án duyệt 08/10) đã lên main.**
  - V11: glyph/plate.
  - F11: lấy danh sách phát hành từ nhà máy.
  - Rubric khuyên: chạy thử ở C4 Tập 6. `tally` luôn tính hai rubric, cổng mặc định theo rubric cũ.
  - A15.
  - Selftest Python 344/344, trang 67/67. Chỉ F11 đổi fingerprint. REVIEWER: ĐẠT có sửa; CHẶN/CHÍNH đã sửa trước merge.

## 2. Việc tiếp (≤ 3) và treo
1. **Tập 6:**
   - Bên dựng viết `contract.json`: `model.kind` + `index.name: "cpiu"` (mẫu `checks-runs/K402/contract-ep006-draft.json`), `claims.forbiddenAmounts`, `claims.conditions`.
   - **C4:** chạy thử rubric khuyên. Kiểm mù bản có lời, 2 người chấm, `tally --scores a.json b.json`, thêm đối chứng hình thật.
   - **C5:** đọc `V11.plateOverGraphics`. Lấy mẫu trang lâu hơn khoảng 39 %. F11 nhà máy phải ĐẠT trên cây C5 thật **trước G2**; trượt thì quay lại K2.
2. Lô K sau:
   - R07 cần hộp đối tượng theo từng cue.
   - V14 rule1 cần `chartW`.
   - Bên dựng ghi dải chrome thành đối tượng `card`, để V11 về 0.
   - Selftest kind thiếu ca chỉ số đối chiếu và ca hoà.
   - Hiệu chuẩn chỉ báo trên Tập 6: V15, V17, R08, T4, S22.
3. Treo:
   - Còn mở: A5, A7, A8, A23 (cờ `change` trên spine).
   - K3.6 còn ghi "chờ duyệt".

## 3. Quyết định đã có
08/10, gói K4.1 → `checks-runs/K41/GOI-answer.md`:
- câu 1: Có;
- câu 2: Có, với điều kiện F11 đạt ở C5 Tập 6;
- câu 3: Có, chạy thử ở C4 Tập 6; hỏi bảo hiểm hoặc hỏi báo giá = `caution_only`.

Lệnh: kind Tập 6 làm trước K4.1; K4.1 lên main trước C5 Tập 6.

## 5. Token (đọc từ transcript cục bộ; phiên một lượt, chưa có sự kiện `result`)
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần |
|---|---|---|---|---|---|
| K lô 08/10 (đã báo) | 08/10 17:58 | 170.090 | 757.341 | 80.464.818 | 927.431 |
| **K tiếp (kind T6 + K4.1)** | 09/10 00:38 | 66.160 | 787.773 | 34.298.973 | **853.933** |

Ghi chú:
- Có 3 agent REVIEWER, mỗi lượt cỡ ngữ cảnh 0,09–0,10 triệu token.
- Giờ máy:
  - selftest: 4 lượt, 14–21 phút mỗi lượt;
  - hiệu chuẩn kind: dưới 1 phút.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md`
2. `decisions/D-008.md`
3. `checks/README.md` (mục K4.0.2, K4.1)
4. `checks/CONTRACT.md`
5. `K-PLAN.md`
6. `checks-appeal.md`
7. `episodes/ep006/PLAN.md` (nhánh `ep006`)
8. K-brief của tập kế tiếp

## 7. Prompt phiên kế
```
Phiên K lô sau Tập 6. Nhánh <nhánh do lệnh ghi> từ main (K4.1 @ 1678a38, LOCK 4d688acd). Mở bằng `bash toolkit/verify.sh <nhánh>`; đọc mục 6 của K-PLAN.md.
Việc đầu tiên: chép câu trả lời dưới đây vào checks-runs/K42/answer.md, commit, push.
1. Kết quả C4/C5 Tập 6: rubric khuyên chạy thử (giữ/bỏ rubric cũ), F11 nhà máy trên cây C5 thật (ĐẠT → giữ; trượt → quay lại K2), V11.plateOverGraphics.
2. Hiệu chuẩn chỉ báo trên Tập 6 (V15, V17, R08, T4, S22) và kind mới cho tập kế (K-brief nếu có; chưa có thì ghi "chờ").
Chỉ thêm → tự merge theo D-008 §2; sửa luật cũ → gói ≤ 3 câu. Đóng phiên theo D-011: K-PLAN ≤ 1 trang, 4 số token, prompt phiên kế. DỪNG.
Câu trả lời / kết quả Tập 6:
<<DÁN CÂU TRẢ LỜI Ở ĐÂY>>
```
