# retire-4 — kiểm hợp lệ hồ sơ (`playbook/topic-dossier.md` §4)

Chạy 2026-10-04, phiên P1 Tập 3 (nhánh `ep003`). Ghi ở đây thay vì `topics-r1/REPORT.md` để không đụng file dùng chung (phiên DT1 đang làm các hồ sơ khác).

| # | Mục | Kết quả |
|---|---|---|
| 1 | `model.json`: kind có sẵn **hoặc** `newKindNeeds` đủ 5 phần | ĐẠT — `kindStatus: new`, `kind: null` (tên do phiên K; nhãn làm việc của chủ dự án `lock-vs-roll-replay`); đủ tóm tắt + inputs, calculation, outputs, invariants; tham số hoá cho retire-3 (`retire3Instance`) |
| 2 | Mọi đại lượng trong card và câu diễn giải có trong `quantities` | ĐẠT — 49 đại lượng; 41 được câu dùng |
| 3 | Mọi câu trong `statements.json` ra True | ĐẠT — 30/30 (`calc.py --statement N`); thử âm: đổi 1.378→1.388 (số của nhóm khác), 'none'→'1', 1990→1950 đều ra False |
| 4 | Ngày "hiện tại" của dữ liệu trong `sources.json` | ĐẠT — `dataAsOf.date` 2026-08-01; SHA tải lại 2026-10-04 trùng bản đóng băng |

## Thay đổi so với bản đóng băng `d16d1b4`
- Số trong `result.json → numbers` **không đổi**; `calc.py` chạy mặc định in đúng 14 số cũ.
- Câu chữ `answer`, `guess`, `changesDecision`, `limits`, `assumptions[0]` viết lại thành các câu có mục trong `statements.json` (mỗi số một đối tượng). Câu cũ "because rates fell over the following decades" (không kiểm được) thay bằng `chg-2` (87.6%). "1950s–1980s" → "from 1950 to 1989" (93.1%).
- Thêm: 17 tháng bắt đầu có bảo đảm thật (5/2005–9/2006) — cả 17 lần lăn T-bill chỉ đạt 1.378–1.388 lần; 856 tháng (98.1%) là giả định.
- `claim-risk.md`: mục bắt buộc "giả định trước 5/2005 phải nói bằng lời và trên hình từ kết quả đầu tiên"; 6 cửa sổ trong ±0.5% quanh gấp đôi.
- `sources.json`: `dataAsOf`, quyền dữ liệu (FRED "Public Domain: Citation Requested" cho cả TB3MS và CPIAUCNS), trích dẫn, xác minh nguyên văn 31 CFR 351.34(a)/351.35(f)(2).
