# Hàng đợi đề tài

Đề tài chủ dự án đã "Có" ở bước 2. Vào hàng đợi **chưa** phải là chọn làm tập: chọn đề tài nào cho tập nào vẫn là quyền chủ dự án (D-004 §1). Hồ sơ đầy đủ (dữ liệu, `calc.py`, nguồn, mới lạ, rủi ro claim) ở thư mục ghi trong cột "Hồ sơ". **Luôn dùng đường dẫn đầy đủ có tiền tố vòng** (`topics-r1/…`, `topics-r2/…`): tên hồ sơ vòng 2 trùng vòng 1 (debt-2, tax-2, retire-4…). Số thứ tự dòng không đổi; dòng mới thêm vào cuối.

| # | Vòng | Đề tài (tiêu đề nháp) | Trụ | Bước 1 | Hồ sơ | Rủi ro cần xử lý trước khi làm |
|---|---|---|---|---|---|---|
| 1 | 1 | 7.5% Variable or 9% Fixed? Grad Loans Through History | vay nợ | 5 | `topics-r1/machine/debt-2/` | khoản vay thật dùng chỉ số kiểu SOFR, có trần lãi và biên theo tín dụng — tập không được nói 'khoản vay của bạn sẽ…'. |
| 2 | 1 | Overtime or a Second Job at $48 an Hour: Which Pays More? | thuế | 4 | `topics-r1/machine/tax-4/` | báo chí đã nói 'chỉ phần trả thêm được trừ'; cái mới là so với việc thứ hai. Câu kết quả đã sửa thành 29,65 % (errata 2026-10-04); có `model.json` + `statements.json`. |
| 3 | 1 | Bought Your Home in 2000? The $500,000 Tax-Free Limit Test | thuế | 4 | `topics-r1/machine/tax-2/` | chỉ số vùng ≠ căn nhà cụ thể; chưa tính chi phí cải tạo; số liệu chỉ số được sửa hằng quý. Có `model.json` + `statements.json` (2026-10-04). |
| 4 | 1 | Your $3,000 Tax Refund: What Is It Really Costing You? | thuế | 4 | `topics-r1/machine/tax-1/` | tiêu đề nói 'Your' — tập chỉ chứng minh cho hộ minh hoạ; không khuyên đổi khấu trừ lương. |
| 5 | 1 | 60 vs 72 Months on a $35,000 Car Loan: The Real Cost | vay nợ | 4 | `topics-r1/machine/debt-3/` | chỉ là lãi ngân hàng (không phải đại lý/công ty tài chính); không đo mất giá xe hay nợ âm. |
| 6 | 1 | Long-Term Care Insurance: 3% or 5% Inflation Protection? | hưu trí | 4 | `topics-r1/machine/retire-2/` | chỉ số giá sản xuất ≠ giá gia đình trả; không nói được gói 5 % 'không đáng tiền'. |
| 7 | 1 | Savings Bonds That Double in 20 Years vs T-Bills | hưu trí | 4 | `topics-r1/machine/retire-4/` | bảo đảm gấp đôi chỉ có từ 2005 — trước đó là giả định; nói rõ 'history, not a forecast'. |
| 8 | 1 | Sell at 11 Months or Wait for the Lower Tax Rate? | thuế | 4 | `topics-r1/machine/tax-3/` | dữ liệu chỉ số có điều khoản cấm tái bản — chỉ được dùng số đã tính, cần xác nhận quyền trước khi làm tập. |
| 9 | 1 | Paying a Point to Get 6.75%? What History Says | vay nợ | 4 | `topics-r1/machine/debt-4/` | gần với chủ đề Tập 1 (tái cấp vốn); 'history, not a forecast'. |
| 10 | 1 | 1-Year CD Pays More Than a 5-Year: Roll or Lock? | hưu trí | 4 | `topics-r1/machine/retire-3/` | lãi CD thật khác lợi suất trái phiếu; đợt 2022–24 chưa chấm hết được. |
| 11 | 1 | 3% Mortgage vs T-Bills: Where Should the $500 Have Gone? | vay nợ | 4 | `topics-r1/machine/debt-1/` | số chênh nhỏ, nhạy với làm tròn và giả định thuế. |
| 12 | 1 | Does a 2% Annuity Raise Really Keep Up With Prices? | hưu trí | 4 | `topics-r1/machine/retire-1/` | không so giá niên kim thật của hai lựa chọn; 'history, not a forecast'. |
| 13 | 2 | 15-Year Mortgage or a 30-Year Paid in 15? The Real Price | vay nợ | chọn (9/18) | `topics-r2/machine/debt-1/` | không nói giá trị của sự linh hoạt; 'history, not a forecast'. Chưa có `model.json` + `statements.json` (bổ sung khi được chọn làm tập, `playbook/topic-dossier.md`). |
| 14 | 2 | Stretching to 35% of Your Pay: How Long Until It's 28%? | vay nợ | chọn (9/18) | `topics-r2/machine/debt-3/` | lương bình quân ≠ lương của từng người; không tính thuế, bảo hiểm, chi phí nhà tăng. Chưa có `model.json` + `statements.json` (bổ sung khi được chọn làm tập, `playbook/topic-dossier.md`). |
| 15 | 2 | $1,000 Emergency: Tap the 401(k) or Use the Card? | thuế | chọn (9/18) | `topics-r2/machine/tax-2/` | quy định rút khẩn cấp mới, cần kiểm lại điều kiện; không khuyên rút tiền hưu. Chưa có `model.json` + `statements.json` (bổ sung khi được chọn làm tập, `playbook/topic-dossier.md`). |
| 16 | 2 | Rental Losses on $130,000 of Wages: Still Deductible? | thuế | chọn (9/18) | `topics-r2/machine/tax-3/` | không bàn các ngoại lệ (chuyên gia bất động sản, cho thuê ngắn ngày). Chưa có `model.json` + `statements.json` (bổ sung khi được chọn làm tập, `playbook/topic-dossier.md`). |
| 17 | 2 | 10% Down and Mortgage Insurance: How Long Did It Last? | vay nợ | chọn (9/18) | `topics-r2/machine/debt-2/` | bỏ bảo hiểm theo giá trị hiện tại do ngân hàng quyết và thường chặt hơn; chỉ số toàn quốc ≠ căn nhà. Chưa có `model.json` + `statements.json` (bổ sung khi được chọn làm tập, `playbook/topic-dossier.md`). |
| 18 | 2 | Travel Early in Retirement or Wait? The Price Test | hưu trí | chọn (9/18) | `topics-r2/machine/retire-4/` | chuỗi khách sạn chỉ từ 1997 (~3 giai đoạn 10 năm độc lập); dữ liệu không đo sức khoẻ. Chưa có `model.json` + `statements.json` (bổ sung khi được chọn làm tập, `playbook/topic-dossier.md`). |
| 19 | 2 | Waiting a Year for a Lower Car Loan Rate: Does It Pay Off? | vay nợ | chọn (9/18) | `topics-r2/machine/debt-4/` | lãi ngân hàng, không phải đại lý; không tính khuyến mãi của hãng. Chưa có `model.json` + `statements.json` (bổ sung khi được chọn làm tập, `playbook/topic-dossier.md`). |

Nguồn dòng 1–12: `topics-r1` vòng 1, bước 2 ngày 2026-10-01 (mã `topics-r1/step2/step2-code.txt`). Hợp lệ 12/12 (`topics-r1/REPORT.md`). Số liệu đóng băng ở `d16d1b4`; khi làm tập phải tải lại dữ liệu và kiểm lại (nguồn có thể đã sửa số).

Nguồn dòng 13–19: `topics-r2` vòng 2, bước 2 ngày 2026-10-04 (mã `topics-r2/step2/step2-code.txt`). Hợp lệ 12/12 theo giá trị (D-004 sửa đổi 1; `topics-r2/REPORT.md`). Số liệu đóng băng ở `b0b1e1f`; khi làm tập phải tải lại dữ liệu và kiểm lại.
