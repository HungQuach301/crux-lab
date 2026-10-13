# REPORT — hồ sơ đề tài #20 rent-buy-1 "Rent vs Buy a Home — Replayed Through Real History" (Tập 8)

Máy đề tài, 11/10/2026. Kiểm theo `playbook/topic-dossier.md` §4. Dữ liệu ở `data/` (không commit, `.gitignore`); tải lại bằng URL ghim `&coed=` trong `sources.json`, so `sha256`.

## Bảng §4

| # | Mục | Kết quả | Bằng chứng |
|---|---|---|---|
| 1 | `model.json` có `kind` khớp checks hoặc `newKindNeeds` đủ năm phần | **ĐẠT** | Không kind nào trong bảng "Loại mô hình" của `checks/CONTRACT.md` tính người thuê + người mua (gần nhất `ltv-first-passage`: dư nợ vs chỉ số giá, không có tiền thuê). `kind: null`, `kindStatus: "new"`, `newKindNeeds` có đủ `inputs`, `computation`, `outputs`, `invariants`, `dataNow`. Không đặt tên kind. |
| 2 | Mọi đại lượng nêu trong card và câu diễn giải có trong `quantities` | **ĐẠT** | 76 đại lượng trong `model.json → quantities`, mỗi cái trỏ `result.json → numbers[id=…]`. Kiểm máy: mọi `uses` của 11 câu nằm trong `quantities` → `uses not in quantities: []`. Card chỉ dùng `price` ($400,000), `first_10y` (1991) và tên đại lượng (`guideWindows`). `limits` không chứa số (trỏ câu 6). |
| 3 | Mọi câu trong `statements.json` ra `True` | **ĐẠT** | Chạy thật (dưới). Mỗi câu: văn bản dựng lại từ dữ liệu phải trùng nguyên văn + điều kiện logic của câu (vd. câu 9: tỉ lệ hôm nay < mức thấp nhất lịch sử) + mọi `uses` có trong số tính. |
| 4 | Ngày "hiện tại" của dữ liệu trong `sources.json` | **ĐẠT** | `sources.json → dataNow`: giá nhà đến 2026-07, CPI tiền thuê đến 2026-08 (2025-10 trống ở nguồn), PMMS tuần đến 2026-10-08 (tháng đủ cuối 2026-09), TB3MS đến 2026-09; cửa sổ cuối kết thúc 2026-07. Mỗi chuỗi có `lastObservation` + `updatedQuote`. |

### Kết quả chạy mục 3 (dán nguyên)
```
$ python3 calc.py --statement 1
True
$ python3 calc.py --statement 2
True
$ python3 calc.py --statement 3
True
$ python3 calc.py --statement 4
True
$ python3 calc.py --statement 5
True
$ python3 calc.py --statement 6
True
$ python3 calc.py --statement 7
True
$ python3 calc.py --statement 8
True
$ python3 calc.py --statement 9
True
$ python3 calc.py --statement 10
True
$ python3 calc.py --statement 11
True
uses not in quantities: []
```

## Quyền dữ liệu (mỗi chuỗi một dòng; trích nguyên văn trang chuỗi FRED + https://fred.stlouisfed.org/legal/, đọc 11/10/2026)

| Chuỗi | Trang chuỗi (nguyên văn) | Trang pháp lý (nguyên văn) | Hiển thị trên video có quảng cáo? |
|---|---|---|---|
| HPIPONM226N (FHFA) | "Public Domain: Citation Requested" | "Public Domain: Citation requested These series may be under copyright or in the public domain and may be used without permission, provided you do not engage in any prohibited use. When using, please cite the data source and acknowledge that you obtained the data from FRED (example, “ Source: BLS via FRED ”) when displaying or publishing it." | **Có**, ghi "Source: FHFA via FRED" |
| CUUR0000SEHA (BLS) | "Public Domain: Citation Requested" | như dòng trên | **Có**, ghi "Source: BLS via FRED" |
| MORTGAGE30US (Freddie Mac) | "Copyrighted: Citation Required" | "Copyrighted: Citation required These series are under copyright; but, provided you have not engaged in any prohibited uses, you may use these data series with proper attribution of the source and acknowledgment that you obtained the data from FRED (example, “ Source: BLS via FRED ”) when displaying or publishing it." | **Có**, ghi "Source: Freddie Mac via FRED" (như RIGHTS.md D-FRED-1; không phát lại tệp dữ liệu) |
| TB3MS (Fed Board) | "Public Domain: Citation Requested" | như dòng HPIPONM226N | **Có**, ghi "Source: Federal Reserve via FRED" (chỉ dùng cho biến thể kiểm độ bền) |

Điều khoản thương mại chung (legal §IV, nguyên văn): "Series with the following copyright labels—Public Domain: Citation requested and Copyrighted: Citation required—may be used for internal commercial uses and may be displayed in textbooks, newsletters, or reports to clients provided that appropriate attribution is given to FRED as well as the original source of the data." Không dùng chuỗi "Pre-Approval Required" (Case-Shiller bị loại). Chưa có dòng RIGHTS.md cho HPIPONM226N / CUUR0000SEHA / TB3MS — phiên P2 thêm khi chọn làm tập.

## Mô hình (tóm tắt)
Hai người ILLUSTRATIVE cùng tháng bắt đầu s, cùng tiền. Người mua: nhà $400,000 theo chỉ số FHFA quốc gia (chỉ số ≠ một căn nhà), 20 % cọc + 3 % phí mua, vay 30 năm lãi PMMS trung bình tháng s, chi phí sở hữu 2,5 %/năm giá trị hiện tại (thuế 1,0 + bảo hiểm 0,5 + sửa chữa 1,0), phí bán 6 %. Người thuê: tiền thuê đầu = y(s) × giá, y = 5 % ở 2026-07 (giả định) kéo lùi theo CPI tiền thuê / chỉ số giá, tăng theo CPI "Rent of primary residence". Chi tiêu bằng nhau; bên trả ít hơn giữ phần chênh trong quỹ tiền mặt (0 %; biến thể T-bill). Lợi thế người mua = vốn ròng nhà − quỹ người thuê. Phát lại mọi tháng 1991-01 → 2016-07 (10 năm, 307 cửa sổ); thêm 5 năm (367) và 15 năm (247).

## Kết quả chính (từ `statements.json`)
- 10 năm: người mua hơn ở 75,6 % cửa sổ; tệ nhất 6/2006 (thua $82,385), tốt nhất 4/2012 (hơn $483,975).
- Ba thời kỳ: 1990s 100 % · 2002–2007 8,3 % · 2009–2016 100 %. 5 năm 74,4 %; 15 năm 100 %.
- Độ nhạy: 64,2 % (thuê 4 %) · 92,2 % (6 %) · 66,4 % (quỹ hưởng lãi T-bill).
- Hôm nay (9/2026, 6,86 %): tiền thuê = 56,8 % chi phí tháng đầu của người mua, thấp hơn mọi tháng bắt đầu đã phát lại (thấp nhất 57,9 %, 7/2006).

## Câu hỏi khán giả (hồ sơ cầu)
- 1 (thuê có đắt hơn mua khi tính lãi, thuế, bảo hiểm, sửa chữa): **trả lời** — theo tỉ lệ cố định ghi rõ.
- 2 (số đổi theo lãi vay, giá nhà, tiền thuê): **trả lời** — lịch sử thật + 3 kỳ hạn + độ nhạy tiền thuê.
- 3 (chi phí ẩn): **trả lời một phần** — phí mua, phí bán, chi phí sở hữu; không có chi phí chuyển nhà, bảo hiểm người thuê.
- 4 (đầu tư phần chênh): **không** — chỉ tiền mặt / T-bill, không cổ phiếu.
- 5 (yếu tố phi tài chính): **không**.

## Giới hạn / việc còn mở
- `novelty.json`: WebSearch bị từ chối trong phiên này → chưa tìm web; kết luận khoảng trống dựa trên hồ sơ cầu + mổ xẻ Logical Money. Cần chạy lại trước C1.
- Mức tiền thuê ban đầu là giả định (không có chuỗi FRED mức tiền thuê được dùng); kết quả nhạy với nó (câu 6).
