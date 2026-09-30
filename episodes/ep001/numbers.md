# Tập 1 — Bảng số (DATA, 2026-09-28)

Mọi con số tập 1 được phép dùng. Bảng sinh từ `out/claims.json` (chạy `python3 build.py`), không gõ tay. Số viết kiểu Mỹ. Nhân vật dùng ID trung tính `median` / `small` / `large`; WRITER đặt tên. Cả ba nhân vật đều **ILLUSTRATIVE**: người giả định, còn khoản vay và phí là trung vị HMDA thật.

## 1. Mốc ngày (thay mọi cách nói "this week" / "today")

- **Mốc: September 24, 2026.** Đây là điểm mới nhất của FRED `MORTGAGE30US` (Freddie Mac PMMS, vay 30 năm lãi cố định). Tải lại ngày 2026-09-28; file không đổi (SHA-256 `b2b254ff…`, `fetch.py --verify`: 0 lệch).
- **Nghĩa của ngày này.** FRED ghi *"Frequency: Weekly, Ending Thursday"* và *"Updated: Sep 24, 2026 11:02 AM CDT"*. Tức là con số 7.03% là trung bình tuần PMMS, công bố vào thứ Năm 24/9/2026, và FRED gắn nhãn tuần kết thúc ngày đó. Kỳ công bố sau là *"Oct 1, 2026"*. Các câu trích nằm ở `data/sources.json → latestObservation`.
- **Cách nói đúng:** "the week ending September 24, 2026" hoặc "Freddie Mac's weekly average published September 24, 2026". Đừng viết "rates this week".
- Ghi chú FRED (trích nguyên văn): *"On November 17, 2022, Freddie Mac changed the methodology… The weekly mortgage rate is now based on applications submitted to Freddie Mac from lenders across the country."* Chưa kiểm được trực tiếp tuần lấy hồ sơ gồm những ngày nào, vì freddiemac.com bị chặn (xem mục 6, ý 5).
- **Dữ liệu FRED không nằm trong repo** (repo public; FRED/Freddie Mac và Optimal Blue có bản quyền, không phải public domain; `amendments.md` E1-A2). Từ bản clone mới: `python3 episodes/ep001/data/fetch.py --verify` tải lại file thiếu từ URL ghim (`pinnedUrl`, cắt ở quan sát cuối đã ghi), kiểm SHA-256, dựng lại `data/normalized/mortgage30_weekly.csv` và `crosscheck_weekly.csv` rồi kiểm SHA-256 của chúng (`data/sources.json → derived`).
- Mọi claim "hôm nay" đều ghi ngày trong công thức, và có trường `asOf: 2026-09-24`. Khi FRED ra điểm mới (1/10/2026), chạy `fetch.py` rồi `build.py`. Các claim có `asOf` sẽ đổi. `build.py` tự kiểm để ngày mốc trùng `sources.json`.

## 2. Nhân vật khoản vay lớn: quyết định về hạn mức conforming

**Vấn đề.** Khoản $1,005,000 cũ (trung vị nhóm $750k+) vượt hạn mức conforming cơ sở. PMMS lại là lãi của khoản vay conforming. Cách tính cũ vì thế áp lãi PMMS lên một khoản jumbo. Dữ liệu cũng cho thấy trong nhóm $750k+ (2025, mục đích 31) có 30,962 khoản NC và 32,452 khoản C: một nửa nhóm là jumbo.

**Hạn mức (FHFA, cơ sở, nhà 1 căn, "most of the United States").** Câu trích nằm ở `data/cll.json`.

| Năm | Giá trị | Trích | URL |
|---|---|---|---|
| 2026 (hiện hành) | **$832,750** | "In most of the United States, the 2026 conforming loan limit (CLL) value for one-unit properties will be $832,750, an increase of $26,250 from 2025." | https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2026 |
| 2025 | $806,500 | "In most of the United States, the 2025 CLL value for one-unit properties will be $806,500, an increase of $39,950 (or 5.2 percent) from 2024." | https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2025 |
| 2023 | $726,200 | "In most of the United States, the 2023 conforming loan limit (CLL) value for one-unit properties is $726,200, an increase of $79,000 from $647,200 in 2022." | https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2023 |

**Cách lấy.**
- **2026: chủ dự án đã xác minh (owner-verified, 2026-09-29).** Chủ dự án đọc giá trị **$832,750** trong thông cáo báo chí chính thức của FHFA, "FHFA Announces Conforming Loan Limit Values for 2026", ngày **November 25, 2025**: https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2026. Ghi ở `data/cll.json → 2026` (`verifiedBy`, `verified`, `released`) và claim `cll2026` (`ownerVerified: true`, `released: 2025-11-25`).
- 2023 và 2025: `www.fhfa.gov` vẫn bị proxy chặn với curl lẫn WebFetch (EGRESS_BLOCKED). Câu trích của hai năm này là nội dung trang fhfa.gov do WebSearch trả về, chưa được chủ dự án xác minh. Kiểm chéo nội tại: 832,750 − 26,250 = 806,500, khớp giá trị 2025. Tập chỉ cần 2023 để giải thích mép $720k; nếu dùng hai số này trên màn hình, cần chủ dự án xác minh như 2026.

**Quyết định: giữ nhân vật lớn là một nhóm HMDA thật và đưa khoản vay xuống dưới hạn mức.**
- Nhóm mới: HMDA 2025, mục đích 31, lien 1, 360 tháng, total_loan_costs > 0. Thêm cờ `conforming_loan_limit = C` và loan_amount từ $600,000 tới **dưới $720,000**. loan_amount công bố theo bin 10k, nên nhóm chỉ gồm các bin 600–610k … 710–720k.
- Vì sao mép trên là $720k chứ không phải $832,750: nhân vật **vay từ tháng 10/2023**, nên khoản vay gốc phải dưới hạn mức **2023** ($726,200). Khoản tái cấp vốn (dư nợ $636,466) thì dưới cả hạn mức 2025 lẫn 2026. Như vậy lãi PMMS áp đúng cho cả khoản cũ lẫn khoản mới.
- Cờ C được định nghĩa ở trang trường dữ liệu HMDA (trích nguyên văn, curl trực tiếp): *"conforming_loan_limit Description: Indicates whether the reported loan amount exceeds the GSE (government sponsored enterprise) conforming loan limit Values: C (Conforming) NC (Nonconforming) U (Undetermined) NA (Not Applicable)"* (https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields).
- Kết quả: 36,385 khoản; trung vị khoản vay **$655,000**; phí trung vị **$5,514**; tỉ lệ phí 0.85%. Tải lại theo luồng từ ffiec.cfpb.gov (SHA-256 `f7b407df…`, 401 MB, không lưu file gốc; `data/hmda-sources.json → extFiles`). Kiểm tra: tổng dòng sau lọc bằng đúng n31 = 488,241 của lần tải trước.
- Phương án dự phòng (giữ jumbo và cộng một chênh lãi jumbo ILLUSTRATIVE) **không dùng**.
- **Giới hạn còn lại** (nên nói trong thẻ phương pháp): PMMS mô tả khoản vay **thông thường** (conventional). Trong 3 nhóm HMDA có cả FHA/VA/USDA: 55% số khoản mục đích 31 năm 2025 là conventional, nhóm lớn là 68%. Lãi của khoản vay cũ lấy theo lãi trung bình tháng, không theo từng người.

## 3. Thay đổi so với claims cũ (M1b)

| Cũ | Mới | Ghi chú |
|---|---|---|
| ID `*_maya`, `*_dan`, `*_priya` | `*_median`, `*_small`, `*_large` | median và small giữ nguyên giá trị |
| `loan_priya` $1,005,000 | `loan_large` **$655,000** | nhóm conforming mới |
| `cost_priya` $5,034 | `cost_large` **$5,514** | |
| `sav_priya` $593 | `sav_large` **$387** | |
| `be_simple_priya` 9 | `be_simple_large` **15** | |
| `be_bal_priya` 11 | `be_bal_large` **18** | |
| `net36_priya` $11,482 | `net36_large` **$5,250** | |
| `net84_priya` $30,387 | `net84_large` **$17,571** | |
| `cut36_priya` 0.2 | `cut36_large` **0.32** | |
| `share_big` 0.5% ($750k+) | `share_large` **0.8%** (0.85%) | |
| `behp_max` 6 | `behl_max` **11** | tỉ lệ phí nhóm lớn 2025 áp cho mọi năm → ILLUSTRATIVE |
| `r_today` "latest week (2026-09-24)" | cùng 7.03%, công thức ghi "PMMS week ending Thursday September 24, 2026" | mọi claim "hôm nay" có `asOf` |
| — | mới: `anchor_date`, `band600`, `band720`, `cll2023/2025/2026`, `share_median`, `n_large`, `n_small`, `be_simple_05`, `be_bal_05`, `be_bal_025` ("never"), và các claim bối cảnh (mục F) | |

Giá trị của median, small và phần lịch sử **không đổi**: FRED không có điểm mới sau 24/9/2026, HMDA không đổi.

**Kịch bản cũ:** `script/script.tpl.md` còn dùng ID cũ và câu "this week". `build.py` báo danh sách ID thiếu, và **không ghi đè** `script/script.md` / `out/script-draft.json`. WRITER viết lại theo ID mới.

## 4. Bảng mọi con số

### A. Thế giới lãi suất

| Claim ID | Hiển thị | Nghĩa | Nguồn | Ngày/năm dữ liệu | ILLUSTRATIVE? | Danh nghĩa/thực |
|---|---|---|---|---|---|---|
| `anchor_date` | September 24, 2026 | Mốc ngày của mọi số "hôm nay": giá trị PMMS mới nhất, FRED ghi ngày thứ Năm kết thúc tuần, công bố cùng ngày | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026 |  | n/a |
| `r_today` | 7.03% | Lãi 30 năm PMMS tuần kết thúc thứ Năm 24/9/2026 — lãi tái cấp vốn | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026; as of 2026-09-24 |  | n/a |
| `seven` | 7 | Chữ số đầu của lãi ngày mốc (7.03%) | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026; as of 2026-09-24 |  | n/a |
| `oct2023` | October 2023 | Tháng các nhân vật vay (đỉnh tháng của đợt giảm gần nhất) | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2023 |  | n/a |
| `r_old` | 7.62% | Lãi 30 năm trung bình tháng 10/2023 (trung bình 4 tuần) — lãi khoản vay cũ của nhân vật | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2023 |  | n/a |
| `cut_today` | 0.59 | Mức giảm lãi (điểm %) từ 10/2023 tới ngày mốc | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [2023, 2026]; as of 2026-09-24 |  | n/a |
| `k35` | 35 | Số kỳ trả đã qua khi tái cấp vốn (10/2023 → 9/2026) | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [2023, 2026]; as of 2026-09-24 | ILLUSTRATIVE | n/a |
| `term30` | 30 | Kỳ hạn 30 năm | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026 |  | n/a |
| `peak` | 18.63% | Lãi tuần cao nhất từ 1971 | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 1981-10-09 |  | n/a |
| `y1981` | 1981 | Năm lãi cao nhất lịch sử chuỗi | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 1981 |  | n/a |
| `low` | 2.65% | Lãi tuần thấp nhất từ 1971 | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2021-01-07 |  | n/a |
| `low_date` | January 7, 2021 | Tuần đạt đáy lịch sử | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2021 |  | n/a |
| `rise_since_low` | 4.38 | Lãi ngày mốc cao hơn đáy 2021 bao nhiêu điểm | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [2021, 2026]; as of 2026-09-24 |  | n/a |
| `peak2023` | 7.79% | Lãi tuần cao nhất năm 2023 | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2023-10-26 |  | n/a |
| `peak2023_since` | 2000 | Đỉnh 2023 cao nhất kể từ năm này | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2000-11-10 |  | n/a |
| `peak_since2000` | 2000 | Câu cold open A: *"In October 2023, the average 30-year fixed mortgage rate in the US hit its highest level since 2000."* Tuần cao nhất của 10/2023 là tuần kết thúc October 26, 2023 (7.79%). Tìm trên cả chuỗi từ 2000-01-01: tuần cuối trước đó có giá trị ≥ 7.79% là **November 10, 2000** (7.79%, bằng); tuần cuối cao hơn hẳn là October 20, 2000 (7.83%). Không tuần nào từ November 17, 2000 tới October 19, 2023 đạt 7.79%. Nghĩa của "since 2000": cao nhất kể từ tuần November 10, 2000 (bằng tuần đó). Trung bình tháng cũng khớp: 10/2023 (7.62%) cao nhất kể từ 11/2000. Test: `model/test_refi.py::test_peak_since2000_recomputed_from_csv` | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2000–2023 |  | n/a |
| `today_since` | January 16, 2025 | Lần gần nhất trước ngày mốc lãi tuần ≥ 7.03% | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2025-01-16 |  | n/a |
| `r_year_ago` | 6.30% | Lãi tuần cách mốc 52 tuần | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2025-09-25 |  | n/a |
| `y1971` | 1971 | Năm bắt đầu chuỗi PMMS | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 1971 |  | n/a |
| `y2017` | 2017 | Năm đầu chuỗi đối chiếu Optimal Blue | fred-OBMMIC30YF (https://fred.stlouisfed.org/series/OBMMIC30YF) | 2017 |  | n/a |

### B. Chi phí đóng hồ sơ (HMDA)

| Claim ID | Hiển thị | Nghĩa | Nguồn | Ngày/năm dữ liệu | ILLUSTRATIVE? | Danh nghĩa/thực |
|---|---|---|---|---|---|---|
| `y2025` | 2025 | Năm HMDA mới nhất dùng | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | n/a |
| `y2018` | 2018 | Năm đầu HMDA có total_loan_costs | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2018 |  | n/a |
| `n31` | 488,241 | Số khoản tái cấp vốn đổi lãi/kỳ hạn năm 2025 (lọc: lien 1, 360 tháng, có chi phí) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | n/a |
| `cost_median` | $5,124 | Phí đóng hồ sơ (total loan costs) của nhân vật trung vị | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | danh nghĩa (USD năm dữ liệu) |
| `cost_p25` | $3,443 | Phí: 1/4 số khoản trả ít hơn mức này | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | danh nghĩa (USD năm dữ liệu) |
| `cost_p75` | $8,270 | Phí: 1/4 số khoản trả nhiều hơn mức này | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | danh nghĩa (USD năm dữ liệu) |
| `share_median` | 1.5% | Như trên, mọi quy mô | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | n/a |
| `share_small` | 3.4% | Phí trung vị tính theo % khoản vay, khoản < $150k | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | n/a |
| `share_large` | 0.8% | Như trên, nhóm nhân vật lớn (conforming $600k–<$720k) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | n/a |
| `n_small` | 25,038 | Số khoản trong nhóm nhân vật nhỏ | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | n/a |
| `n_large` | 36,385 | Số khoản trong nhóm nhân vật lớn | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | n/a |
| `band150` | $150,000 | Mép nhóm khoản nhỏ | — (giả định/tham số) | — |  | danh nghĩa (USD năm dữ liệu) |
| `band600` | $600,000 | Mép dưới nhóm nhân vật lớn | — (giả định/tham số) | — |  | danh nghĩa (USD năm dữ liệu) |
| `band720` | $720,000 | Mép trên (không gồm) nhóm nhân vật lớn — dưới hạn mức 2023 | — (giả định/tham số) | — |  | danh nghĩa (USD năm dữ liệu) |
| `band750` | $750,000 | Mép nhóm $750k+ (chỉ còn là bối cảnh) | — (giả định/tham số) | — |  | danh nghĩa (USD năm dữ liệu) |
| `cll2023` | $726,200 | Hạn mức vay conforming cơ sở 2023 (nhà 1 căn, phần lớn nước Mỹ) | fhfa-cll (https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2023) | 2023 |  | danh nghĩa (USD năm dữ liệu) |
| `cll2025` | $806,500 | Hạn mức conforming cơ sở 2025 | fhfa-cll (https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2025) | 2025 |  | danh nghĩa (USD năm dữ liệu) |
| `cll2026` | $832,750 | Hạn mức conforming cơ sở 2026 (hiện hành); **chủ dự án đã xác minh** trên thông cáo FHFA ngày November 25, 2025 | fhfa-cll (https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2026) | 2026 |  | danh nghĩa (USD năm dữ liệu) |

### C1. Nhân vật median (mọi quy mô)

| Claim ID | Hiển thị | Nghĩa | Nguồn | Ngày/năm dữ liệu | ILLUSTRATIVE? | Danh nghĩa/thực |
|---|---|---|---|---|---|---|
| `loan_median` | $375,000 | Khoản vay ban đầu của nhân vật trung vị | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `cost_median` | $5,124 | Phí đóng hồ sơ (total loan costs) của nhân vật trung vị | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | danh nghĩa (USD năm dữ liệu) |
| `sav_median` | $221 | Khoản trả hằng tháng giảm được (trung vị) | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [2023, 2026]; as of 2026-09-24 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `be_simple_median` | 24 | Hoà vốn cách chia đơn giản, tháng (trung vị) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | n/a |
| `be_bal_median` | 30 | Hoà vốn tính cả dư nợ, tháng (trung vị) — đáp án chính | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | n/a |
| `net36_median` | $1,039 | Lời/lỗ ròng nếu bán sau 3 năm (trung vị; dấu: xem giá trị) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `net84_median` | $8,093 | Lời/lỗ ròng nếu bán sau 7 năm (trung vị) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `cut36_median` | 0.5 | Mức giảm lãi tối thiểu để hoà vốn trong 36 tháng (trung vị), điểm % | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025] | ILLUSTRATIVE | n/a |
| `gap24` | $1,133 | Dư nợ khoản mới cao hơn khoản cũ bao nhiêu ở tháng 24 (trung vị) — phần cách chia đơn giản bỏ sót | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |

### C2. Nhân vật small (< $150k)

| Claim ID | Hiển thị | Nghĩa | Nguồn | Ngày/năm dữ liệu | ILLUSTRATIVE? | Danh nghĩa/thực |
|---|---|---|---|---|---|---|
| `loan_small` | $115,000 | Khoản vay ban đầu của nhân vật nhỏ | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `cost_small` | $3,667 | Phí đóng hồ sơ (total loan costs) của nhân vật nhỏ | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | danh nghĩa (USD năm dữ liệu) |
| `sav_small` | $68 | Khoản trả hằng tháng giảm được (nhỏ) | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [2023, 2026]; as of 2026-09-24 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `be_simple_small` | 55 | Hoà vốn cách chia đơn giản, tháng (nhỏ) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | n/a |
| `be_bal_small` | 75 | Hoà vốn tính cả dư nợ, tháng (nhỏ) — đáp án chính | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | n/a |
| `net36_small` | −$1,777 (lỗ) | Lời/lỗ ròng nếu bán sau 3 năm (nhỏ; dấu: xem giá trị) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `net84_small` | $386 | Lời/lỗ ròng nếu bán sau 7 năm (nhỏ) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `cut36_small` | 1.12 | Mức giảm lãi tối thiểu để hoà vốn trong 36 tháng (nhỏ), điểm % | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025] | ILLUSTRATIVE | n/a |

### C3. Nhân vật large (conforming $600k–<$720k)

| Claim ID | Hiển thị | Nghĩa | Nguồn | Ngày/năm dữ liệu | ILLUSTRATIVE? | Danh nghĩa/thực |
|---|---|---|---|---|---|---|
| `loan_large` | $655,000 | Khoản vay ban đầu của nhân vật lớn | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `cost_large` | $5,514 | Phí đóng hồ sơ (total loan costs) của nhân vật lớn | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | danh nghĩa (USD năm dữ liệu) |
| `sav_large` | $387 | Khoản trả hằng tháng giảm được (lớn) | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [2023, 2026]; as of 2026-09-24 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `be_simple_large` | 15 | Hoà vốn cách chia đơn giản, tháng (lớn) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | n/a |
| `be_bal_large` | 18 | Hoà vốn tính cả dư nợ, tháng (lớn) — đáp án chính | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | n/a |
| `net36_large` | $5,250 | Lời/lỗ ròng nếu bán sau 3 năm (lớn; dấu: xem giá trị) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `net84_large` | $17,571 | Lời/lỗ ròng nếu bán sau 7 năm (lớn) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025]; as of 2026-09-24 | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `cut36_large` | 0.32 | Mức giảm lãi tối thiểu để hoà vốn trong 36 tháng (lớn), điểm % | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025] | ILLUSTRATIVE | n/a |

### D. So sánh hai cách tính (nhân vật median theo mức giảm)

| Claim ID | Hiển thị | Nghĩa | Nguồn | Ngày/năm dữ liệu | ILLUSTRATIVE? | Danh nghĩa/thực |
|---|---|---|---|---|---|---|
| `hold36` | 36 | Mục tiêu hoàn vốn 3 năm (giả định của câu hỏi) | — (giả định/tham số) | — | ILLUSTRATIVE | n/a |
| `y3` | 3 | Kịch bản bán nhà sau 3 năm | — (giả định/tham số) | — | ILLUSTRATIVE | n/a |
| `y7` | 7 | Kịch bản bán nhà sau 7 năm | — (giả định/tham số) | — | ILLUSTRATIVE | n/a |
| `s025` | 0.25 | Mức giảm lãi 0,25 điểm (lưới phân tích) | — (giả định/tham số) | — |  | n/a |
| `s05` | 0.5 | Mức giảm 0,5 điểm | — (giả định/tham số) | — |  | n/a |
| `s10` | 1 | Mức giảm 1 điểm | — (giả định/tham số) | — |  | n/a |
| `be_simple_025` | 38 | Nhân vật trung vị, giảm 0,25 điểm: hoà vốn cách chia đơn giản (tháng) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025] | ILLUSTRATIVE | n/a |
| `be_bal_025` | never | Như trên, cách tính dư nợ: không bao giờ hoà vốn | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025] | ILLUSTRATIVE | n/a |
| `be_simple_05` | 26 | Trung vị, giảm 0,5 điểm: cách chia đơn giản (tháng) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025] | ILLUSTRATIVE | n/a |
| `be_bal_05` | 36 | Trung vị, giảm 0,5 điểm: cách tính dư nợ (tháng) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025] | ILLUSTRATIVE | n/a |
| `be_simple_10` | 16 | Trung vị, giảm 1 điểm: cách chia đơn giản (tháng) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025] | ILLUSTRATIVE | n/a |
| `be_bal_10` | 18 | Trung vị, giảm 1 điểm: cách tính dư nợ (tháng) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025] | ILLUSTRATIVE | n/a |

### E. Lịch sử (1971–2026, khoản $300,000 ILLUSTRATIVE)

| Claim ID | Hiển thị | Nghĩa | Nguồn | Ngày/năm dữ liệu | ILLUSTRATIVE? | Danh nghĩa/thực |
|---|---|---|---|---|---|---|
| `n_eps` | 13 | Số đợt lãi giảm ≥ 1 điểm từ 1971 | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [1971, 2026] |  | n/a |
| `beh_min` | 10 | Hoà vốn ngắn nhất qua các đợt (giảm 1 điểm, cách dư nợ) | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [1971, 2026] |  | n/a |
| `beh_max` | 20 | Hoà vốn dài nhất qua các đợt | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [1971, 2026] |  | n/a |
| `behs_min` | 10 | Như trên, cách đơn giản: ngắn nhất | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [1971, 2026] |  | n/a |
| `behs_max` | 21 | Cách đơn giản: dài nhất | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [1971, 2026] |  | n/a |
| `n_further` | 3 | Số đợt lãi còn giảm thêm 1 điểm trước khi kịp hoà vốn | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [1971, 2026] |  | n/a |
| `n_nofurther` | 10 | Số đợt còn lại | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [1971, 2026] |  | n/a |
| `ex_peak` | July 1984 | Ví dụ: tháng đỉnh | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 1984 |  | n/a |
| `ex_refi` | November 1984 | Ví dụ: tháng tái cấp vốn | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 1984 |  | n/a |
| `ex_be` | 19 | Ví dụ: số tháng hoà vốn | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 1984 | ILLUSTRATIVE | n/a |
| `ex_gap` | 7 | Ví dụ: số tháng tới khi lãi giảm thêm 1 điểm | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 1984 |  | n/a |
| `r23` | August 2024 | Tháng đầu lãi thấp hơn đỉnh 10/2023 một điểm | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2024 |  | n/a |
| `be23` | 19 | Hoà vốn nếu tái cấp vốn tháng đó | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2024 |  | n/a |
| `behd_min` | 18 | Qua các đợt, với tỉ lệ phí khoản nhỏ: ngắn nhất | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [1971, 2026] | ILLUSTRATIVE | n/a |
| `behd_max` | 39 | Như trên: dài nhất | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [1971, 2026] | ILLUSTRATIVE | n/a |
| `behl_max` | 11 | Qua các đợt, với tỉ lệ phí nhóm lớn 2025: dài nhất | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [1971, 2026] | ILLUSTRATIVE | n/a |
| `m81` | 2 | Số tháng từ đỉnh 10/1981 tới khi thấp hơn 1 điểm | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 1981 |  | n/a |
| `be81` | 13 | Hoà vốn của lần tái cấp vốn đó | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 1981 | ILLUSTRATIVE | n/a |

### F. Bối cảnh từ dữ liệu HMDA trong repo

| Claim ID | Hiển thị | Nghĩa | Nguồn | Ngày/năm dữ liệu | ILLUSTRATIVE? | Danh nghĩa/thực |
|---|---|---|---|---|---|---|
| `n31_conforming` | 457,217 | Trong n31, số khoản conforming (cờ C) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | n/a |
| `conv_share31` | 55% | Trong n31, tỉ lệ khoản thông thường (không FHA/VA/USDA) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | n/a |
| `rate31_p50` | 6.00% | Lãi trung vị của các khoản tái cấp vốn mới năm 2025 | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 |  | n/a |
| `purch23_ge7` | 30% | Tỉ lệ khoản vay mua nhà 2023 (lien 1, 30 năm) có lãi ≥ 7% | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2023 |  | n/a |
| `purch23_n_ge7` | 881,835 | Số khoản đó | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2023 |  | n/a |
| `purch23_n` | 2,906,771 | Tổng số khoản vay mua nhà 2023 cùng bộ lọc | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2023 |  | n/a |

Ghi chú cột:
- Tiền là USD danh nghĩa của năm dữ liệu, không trừ lạm phát.
- Lãi suất là lãi danh nghĩa theo năm.
- Với net36/net84, số hiển thị là trị tuyệt đối; lời hay lỗ phải nói bằng chữ. Riêng `net36_small` là **lỗ $1,777**.
- `cost_*` là **total loan costs** (Closing Disclosure mục D), *không* gồm "Other Costs" (thuế, phí đăng ký, trả trước). Xem mục 6, ý 6.

### G. Dạng đọc bằng lời (gắn với claim gốc; `parent` trong claims.json)

| Claim ID | Hiển thị | Gốc | Nghĩa / điều kiện | Nguồn | Ngày/năm dữ liệu | ILLUSTRATIVE? |
|---|---|---|---|---|---|---|
| `share_walt` | about 3.2% | `cost_small` ÷ `loan_small` | $3,667 ÷ $115,000 = 3.19%: hoá đơn của chính nhân vật small so với khoản vay. **Khác** `share_small` 3.4% (trung vị các tỉ lệ từng khoản); đừng dùng hai số trong cùng một cảnh. | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2025 | ILLUSTRATIVE |
| `n31_approx` | nearly half a million | `n31` 488,241 | kiểm: 450,000 ≤ n31 < 500,000 | hmda-lar | 2025 | |
| `cut_today_words` | just over half a point | `cut_today` 0.59 | kiểm: 0.50 < x < 0.625 | fred-MORTGAGE30US | as of 2026-09-24 | |
| `cut36_large_words` | about a third of a point | `cut36_large` 0.32 | kiểm: \|x − 1/3\| ≤ 0.04 | hmda-lar + FRED (mô hình) | [2023, 2025] | ILLUSTRATIVE |
| `purch23_words` | three in ten | `purch23_ge7` 30.3% | 881,835 trên 2,906,771 khoản vay **mua nhà giải ngân năm 2023** (HMDA 2023, lien 1, 360 tháng, có lãi) có lãi ≥ 7.00%. **Không phải** tỉ lệ trong số khoản còn dư nợ hôm nay. Tải trực tiếp từ ffiec.cfpb.gov, SHA `aeacd608…` | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | 2023 | |
| `ge7_threshold` | seven percent | ngưỡng của `purch23_ge7` | **Tham số phân tích do ta chọn** (số tròn, ngay dưới lãi ngày mốc 7.03%), **không có nguồn**. Khi đọc, nói đây là ngưỡng ta chọn, không gán cho một cơ quan nào. | — | — | |

Các ID cơ bản đều đã có trong bảng: `y1971` (1971), `term30` (30 năm), `s025` / `s05` / `s10` (¼, ½, 1 điểm), `y3` / `y7` (3 và 7 năm).

**Quy tắc "1%":** chưa tìm được câu trích nào từ nguồn truy cập được. Các host có thể có câu này đều bị chặn: cbsnews.com, freddiemac.com, fanniemae.com, nar.realtor. consumerfinance.gov truy cập được nhưng không có câu nào như vậy. Câu "a common rule of thumb … wait for a full percentage-point drop" hiện **không có nguồn**. Chỉ dùng được nếu nói rõ đó là cách nói phổ biến, không gán nguồn, hoặc sau khi chủ dự án mở một host.

<!-- build.py: section H BEGIN (generated, do not edit) -->
### H. Cửa sổ tái cấp vốn 2026: từng mở, đang khép (sinh bởi `build.py`)

Tuần = tuần PMMS kết thúc thứ Năm. Test tính lại độc lập từ CSV: `model/test_refi.py::test_window2026_recomputed_from_csv`.

| Claim ID | Hiển thị | Nghĩa | Nguồn | Ngày/năm dữ liệu | ILLUSTRATIVE? | Danh nghĩa/thực |
|---|---|---|---|---|---|---|
| `low2026` | 5.98% | Lãi tuần thấp nhất năm 2026 (tới ngày mốc) | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026-02-26; as of 2026-09-24 |  | n/a |
| `low2026_date` | February 26, 2026 | Tuần của mức thấp nhất 2026 | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026-02-26; as of 2026-09-24 |  | n/a |
| `low2026_since` | September 2022 | Đáy 2026 thấp nhất kể từ tuần này (lần gần nhất trước đó lãi ≤ mức đáy); cũng là lần đầu dưới 6% kể từ tuần này. "Lowest since September 2022" và "lowest in more than three years" đều đúng | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2022-09-08 |  | n/a |
| `jan2026` | 6.06% | Lãi tuần kết thúc 15/1/2026: lúc đó thấp nhất kể từ tuần 15/9/2022. **Không phải** đáy 2026 (đáy là `low2026`). Không có tuần PMMS nào ghi ngày 12/1/2026 | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026-01-15 |  | n/a |
| `jan2026_since` | September 2022 | Mức 6.06% tuần 15/1/2026 thấp nhất kể từ tuần này | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2022-09-15 |  | n/a |
| `cut_low2026` | 1.64 | Chênh giữa lãi cũ của nhân vật (`r_old`) và đáy 2026, điểm % | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [2023, 2026] |  | n/a |
| `k_low2026` | 28 | Số kỳ trả đã qua nếu vay lại ở tháng đáy 2026 (10/2023 → 2/2026, cùng quy ước với `k35`) | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [2023, 2026] | ILLUSTRATIVE | n/a |
| `sav_low2026_median` | $459 | Nhân vật median vay lại ở tuần đáy 2026: tiết kiệm mỗi tháng | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | [2023, 2026] | ILLUSTRATIVE | danh nghĩa (USD năm dữ liệu) |
| `be_simple_low2026_median` | 12 | Như trên: hoà vốn cách chia đơn giản (tháng) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025] | ILLUSTRATIVE | n/a |
| `be_bal_low2026_median` | 11 | Như trên: hoà vốn tính cả dư nợ (tháng) | hmda-lar (https://ffiec.cfpb.gov/data-browser/) | [2023, 2025] | ILLUSTRATIVE | n/a |
| `first7_since` | January 2025 | Ngày mốc là lần đầu lãi ≥ 7.00% kể từ tuần này (cùng tuần với `today_since`, nhưng ngưỡng 7.00% thay vì 7.03%) | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2025-01-16; as of 2026-09-24 |  | n/a |
| `rise_since_low2026` | 1.05 | Lãi ngày mốc cao hơn đáy 2026 bao nhiêu điểm | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026; as of 2026-09-24 |  | n/a |
| `weeks_rise_since_low2026` | 30 | Số tuần từ đáy 2026 tới ngày mốc | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026; as of 2026-09-24 |  | n/a |
| `weeks_below_r_old_minus_1` | 29 | Số tuần năm 2026 lãi thấp hơn `r_old` ít nhất 1 điểm (≤ 6.62%): "cửa sổ" mở bao lâu trong năm; chuỗi liền bắt đầu từ tuần 14/8/2025 | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026; as of 2026-09-24 |  | n/a |
| `cut1_last_2026` | July 23, 2026 | Tuần cuối cùng của cửa sổ đó (sau tuần này lãi luôn > 6.62%) | fred-MORTGAGE30US (https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026-07-23; as of 2026-09-24 |  | n/a |
<!-- build.py: section H END -->

## 5. Màu nhân vật (design/tokens.json)

`genre-spec/channel/visual-tokens.json` chỉ có 6 màu ngoài nền: ink, ink-muted, accent, warn, positive, negative. Chữ dùng ink và ink-muted, đường lãi dùng accent. Vì thế ba nhân vật buộc phải lấy warn, positive, negative. Không thêm màu mới.

| Vai | Token | Hex | Hình dạng | Tương phản trên bg #0E1116 |
|---|---|---|---|---|
| Đường lãi | accent | #4C8DFF | đường liền, không marker | 5.91:1 |
| small | warn (giữ nguyên) | #F2B441 | tam giác | 10.25:1 |
| median | positive (trước là ink #F2F4F7, trùng chữ) | #3FBF7F | tròn | 8.08:1 |
| large | negative (trước là accent, trùng đường lãi) | #E5484D | vuông | 4.83:1 |
| Chữ | ink / ink-muted | #F2F4F7 / #9AA4B2 | — | 17.16:1 / 7.50:1 (≥ 4.5 ✓; mức 1 ≥ 7 ✓) |

**Mô phỏng CVD.** Dùng ma trận Machado 2009 (mức nặng 1.0) và thang xám luminance Rec.709. ΔE76 trong CIELAB (bình thường / deutan / protan / xám):
- small–median: 75.1 / 47.1 / 36.9 / **7.9**
- small–large: 62.8 / 33.2 / 55.1 / 23.4
- median–large: 111.8 / **21.7** / 28.5 / 15.5
- đường lãi–large: 105.1 / 105.2 / 79.2 / **5.9**
- đường lãi–median: 108.1 / 86.2 / 87.9 / 9.6
- đường lãi–small: 128.4 / 132.8 / 124.7 / 17.5

**Đọc kết quả:**
- Khi mù màu, mọi cặp vẫn cách nhau ≥ 21.
- Ở thang xám, small–median và đường lãi–large rất gần nhau. Vì thế **hình dạng là bắt buộc** (tròn / tam giác / vuông), đường lãi không có marker, và mỗi nhân vật giữ một phía màn hình (DX-V4).
- negative chỉ 4.83:1: đủ cho nét và marker, **không** đủ cho chữ mức 1. Nhãn tên nhân vật viết bằng ink, đặt cạnh marker màu.
- positive/negative còn là màu bill/saved. Trong khung đang có marker nhân vật thì đừng tô bill/saved bằng hai màu này; dùng hoa văn hoặc ink-muted.
- Script kiểm: tôi chạy ngoài repo, công thức ghi ở đây.

## 6. Dữ kiện bối cảnh

### 6a. Dữ kiện bối cảnh có sẵn (tính từ dữ liệu trong repo; claim ở bảng mục 4)

- Đáy lịch sử 2.65% vào tuần kết thúc January 7, 2021. Tới ngày mốc, lãi cao hơn đáy **4.38 điểm** (`low`, `low_date`, `rise_since_low`).
- Đỉnh 2023 là 7.79% (tuần October 26, 2023), cao nhất kể từ năm **2000** (tuần November 10, 2000, cũng 7.79%) (`peak2023`, `peak2023_since`; câu cold open A dùng `peak_since2000`, cùng giá trị, ghi đủ nghĩa "since 2000").
- 7.03% ngày mốc là mức cao nhất kể từ tuần **January 16, 2025** (7.04%). 52 tuần trước (September 25, 2025) lãi là 6.30% (`today_since`, `r_year_ago`).
- HMDA 2025 có **488,241** khoản tái cấp vốn đổi lãi/kỳ hạn (lien 1, 30 năm, có chi phí). Trong đó 457,217 là conforming, 55% là conventional, lãi trung vị của khoản mới là **6.00%** (`n31`, `n31_conforming`, `conv_share31`, `rate31_p50`).
- Vay mua nhà năm 2023 (HMDA, lien 1, 30 năm): **30%** (881,835 trên 2,906,771 khoản) có lãi ≥ 7.00% (`purch23_ge7`, `purch23_n_ge7`, `purch23_n`). Đây là tỉ lệ trong số khoản *được giải ngân năm 2023*, không phải tỉ lệ trong số khoản *còn dư nợ hôm nay*.
- 13 đợt lãi giảm ≥ 1 điểm kể từ 1971: xem nhóm E. Luôn nói kèm "history, not a forecast" và "US only".

### 6b. Dữ kiện bối cảnh (nguồn bổ sung, theo yêu cầu của WRITER)

| # | Claim ID | Dữ kiện | Nguồn và trích | Ngày dữ liệu | Trạng thái |
|---|---|---|---|---|---|
| 1 | `ctx_rule1pct` | Quy tắc "giảm 1%" | Chưa có trích từ nguồn sơ cấp. Host bị chặn: www.cbsnews.com (bài "Does the mortgage refinancing 1% rule still apply this fall?", 2025), freddiemac.com, fanniemae.com. Bản tóm tắt của WebSearch (không phải trích nguyên văn) mô tả quy tắc là "only refinance… if you're able to lower your interest rate by at least one full percentage point". | 2025 | **CHƯA DÙNG ĐƯỢC** như câu trích. Có thể nói "a common rule of thumb" mà không gán nguồn. |
| 2 | `ctx_formula` | Công thức "phí ÷ tiết kiệm hằng tháng" | Không có trang CFPB nào trong tầm với nêu công thức này. Gần nhất là CFPB, Ask CFPB #136 (last reviewed OCT 19, 2023), https://www.consumerfinance.gov/ask-cfpb/how-should-i-use-lender-credits-and-points-also-called-discount-points-en-136/: "You might agree to pay $675 more in closing costs, in exchange for a lower rate of 4.875%. Now : You pay $675 Over the life of the loan : Pay $14 less each month". Trang này cũng khuyên "calculate the total costs over a few different possible timeframes". Phép chia là của ta. Host bị chặn: freddiemac.com, fanniemae.com (máy tính refinance), www.chase.com. | 2023 | Có trích CFPB (ví dụ, không có công thức) |
| 3 | `ctx_nmdb_ge6` | Tỉ lệ khoản vay đang có lãi ≥ 6% | FHFA NMDB, www.fhfa.gov/data/nmdb, **bị chặn**. Bản tóm tắt của WebSearch (nguồn thứ cấp calculatedrisk, không phải trích nguyên văn): 21.9% ở Q4 2025. Thay bằng số có sẵn `purch23_ge7` (30% khoản vay mua nhà 2023 có lãi ≥ 7%). | Q4 2025 | **CHƯA DÙNG ĐƯỢC** cho tới khi mở fhfa.gov |
| 4 | `ctx_tenure` | Số năm sở hữu nhà trước khi bán | NAR 2025 Profile, www.nar.realtor, **bị chặn**; census.gov (AHS) **bị chặn**. Bản tóm tắt của WebSearch: trung vị 11 năm, "an all-time high". | 2025 | **CHƯA DÙNG ĐƯỢC** |
| 5 | `ctx_pmms_profile` | PMMS mô tả người vay nào | Trích FRED (trực tiếp): "The weekly mortgage rate is now based on applications submitted to Freddie Mac from lenders across the country." Trang phương pháp của Freddie Mac **bị chặn** (freddiemac.com, freddiemac.gcs-web.com). Bản tóm tắt của WebSearch: "conventional, conforming, fully amortizing home purchase loans for borrowers who put 20% down and have excellent credit". | từ 2022-11-17 | Nửa trên có trích; phần "20% down, excellent credit" **chờ xác minh** |
| 6 | `ctx_tlc` | total_loan_costs gồm những gì | Reg C 12 CFR 1003.4(a)(17)(i) (https://www.consumerfinance.gov/rules-policy/regulations/1003/4/): "the amount of total loan costs, as disclosed pursuant to Regulation Z, 12 CFR 1026.38(f)(4)". Reg Z 1026.38(f) (https://www.consumerfinance.gov/rules-policy/regulations/1026/38/): "(4) Total loan costs. Under the subheading "Total Loan Costs (Borrower-Paid)," the sum of the amounts disclosed as borrower-paid pursuant to paragraph (f)(5)…" và "(5) Subtotal of loan costs. The sum of loan costs, calculated by totaling the amounts described in paragraphs (f)(1) through (3)…" [(f)(1) origination charges; (f)(2)–(3) các dịch vụ người vay tự chọn và không tự chọn]. Tức là **không gồm** mục "Other Costs" (1026.38(g): thuế, phí đăng ký, khoản trả trước, ký quỹ). Mọi curl đều trực tiếp, 2026-09-28. | quy định hiện hành | **CÓ NGUỒN**. Lời nên nói "loan costs", không nói "all closing costs"; hoặc nói rõ là thiếu Other Costs. |

Hoá đơn của CFPB (tham khảo): bản tin 27/9/2023 viết "These costs rose 22% from 2021 to $5,954". Con số này là cho *mọi* khoản vay năm 2022, không phải riêng tái cấp vốn (https://www.consumerfinance.gov/archive/newsroom/cfpb-mortgage-report-finds-jumps-in-closing-costs-and-denials-for-insufficient-income-growing-proportion-of-cash-out-refinances/).
