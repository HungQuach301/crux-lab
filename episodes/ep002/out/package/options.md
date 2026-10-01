# Tập 2 · Gói phát hành C6: phương án cho chủ dự án chọn

PACKAGING C6, 01/10/2026, nhánh `ep002`. Tệp này chỉ đưa **phương án và bằng chứng**; phần gu do chủ dự án chọn (`playbook/packaging.md` §1.8). Mọi số lấy từ `out/claims.json` (`display`). Không câu nào khuyên hay dự báo: quét bằng ADVICE/FORECAST/FOUR/WE_BAD của S10 (`checks/py/r_content.py`, chỉ import), 0 khớp trên tiêu đề và chữ thumbnail. Ký tự đếm bằng `len()` của Python. Tự kiểm: `selfcheck.json`, `legibility-25.png`. Dựng lại: `preprod/thumbs_c6/` (`render.js` → `selfcheck.py` → `pack_test.js` → `run_readers.sh` → `tally.py`).

Đầu vào đã chốt: C1 hướng **A** ("người như tôi" + lời hứa đáp án), tiêu đề nháp **A1**, không D; nghịch lý (vượt 9% ở 76.2% nhưng đắt hơn ở 14.2%) để **trong phim**, không lên tiêu đề. `description.md` giữ nguyên, không đổi số.

## 1. Tiêu đề (2 phương án, cùng hướng A, ≤ 60 ký tự)

| # | Tiêu đề | Ký tự | Claim | S10 |
|---|---|---|---|---|
| **A1** | Need Private Grad Loans? Variable vs Fixed Through History | 58 | không số. "Private Grad Loans": `ctx_plus_end` (ngữ cảnh, nói ở mô tả); "Through History": phát lại 753 cửa sổ từ `first_start` | 0 |
| **A2** | No Grad PLUS? How Much Lower a Variable Rate Had to Start | 57 | `ctx_plus_end` (từ July 1, 2026 sinh viên sau đại học mới không vay Grad PLUS); "how much lower … had to start" = câu hỏi của phim, đáp án ở lưới khoảng chênh `spread*_share`, `gap*_early/late` | 0 |

Ghi chú chữ:
- A2 viết dạng câu hỏi "No Grad PLUS?", không viết "Grad PLUS Ended": có ngoại lệ cho người đã ghi danh (`ctx_plus_exception`), và C1 dặn không nói "ai cũng phải vay tư nhân".
- A2 dùng "Had to Start" (quá khứ, lịch sử), không dùng "Must/Should Start" (giọng khuyên).
- Kiểm mù ghi lại ba cách đọc A2 (nguyên văn, `review-c6/pack-test/results.md`): một phụ huynh đọc thành "how much lower a variable rate must start to beat the federal Grad PLUS loan" (phim so với lãi cố định tư nhân 9%, không so với Grad PLUS); người refinance nói "doesn't apply to me"; người tò mò gọi "Grad PLUS" là "jargon". A1 không có ghi nhận đọc sai.

## 2. Thumbnail (1280×720; thumb-2/thumb-3 gốc không đạt claim-risk, xem 2b)

Mỗi hình là **still của một cảnh đã ký** (`design/c3/final/src`, engine D2 + E2), vẽ bằng chính engine với cờ NOTEXT (bỏ chữ phim), rồi đặt chữ phẳng Inter 700 bậc `hero` (150 px @1080 = **100 px** @720), màu `ink`/`ink-muted` (D5), cùng huy hiệu ILLUSTRATIVE của engine (bậc `badge`, 32 px). Bố cục (cảnh nào, khung nào, dời bao nhiêu) là **phương án**, không phải quyết định. Concept C3 (H2/H3 "Fixed or variable?") dùng màu trước E2 và lặp chữ của tiêu đề A1, nên không dùng lại chữ đó.

| File | Cảnh nguồn | Vật "anh hùng" (đọc được ở 10%) | Chữ (từ) | Claim | Cỡ chữ | Tương phản 10% (min) |
|---|---|---|---|---|---|---|
| `thumb-1.png` | KEY-1 `k1.js` t = 7,85 s | một người giơ hai thẻ lời mời, vạch 9% chạy qua cả hai, đường lãi của Leah trên thẻ phải | "9%" · "7.5%" (2) | `fixed_rate`, `var_start` | 100 px | 14,83 |
| `thumb-2.png` **(không đạt claim-risk: chỉ là bằng chứng kiểm mù)** | KEY-3 `h3/scenes.js` K3 t = 6,48 s | dải lịch sử T-bill (`accent`) + dải hổ phách + lưới 753 ô, ô đỏ dồn nửa trái | "14.2%" · "cost more" (3) | `share_all` | 100 px | 7,45 |
| `thumb-3.png` **(không đạt claim-risk: chỉ là bằng chứng kiểm mù)** | KEY-6 K6 t = 9,6 s | khung phóng 10 năm từ 4/1977 + hai chồng xu, khối đỏ chồng lên | "April 1977" · "43%" · "more" (4) | `worst_start`, `worst_share_of_fixed` | 100 px | 7,40 |

Cả ba: số của Leah → **có huy hiệu ILLUSTRATIVE** (32 px, tương phản 10% 3,49–6,16 trên viên). Tỉ lệ màu token toàn ảnh 100,0% (hình 2D, chỉ token và pha trộn hai token). Ở 25% (320×180) đọc được mọi chữ kể cả huy hiệu (8 px); ở 10% (128×72) đọc được chữ chính (10 px), huy hiệu thành vệt vàng.

### 2b. Biến thể đạt claim-risk (yêu cầu điều phối, sau kiểm mù)

`story/WRITER-brief.md` "Gen được bảo vệ": câu/chữ **nêu một tỉ lệ hay kết quả** phải kèm cả hai thời kỳ (1954–1980, từ 1981) và trường hợp xấu nhất; không ngụ ý "thả nổi xấu/an toàn". thumb-2 nêu 14.2% đứng riêng; thumb-3 chỉ cho thấy giai đoạn tệ nhất (lý do nguyên văn: "alarmist"). Hai ảnh gốc **giữ lại làm bằng chứng**, không đưa vào Test & Compare. **2b, 3b, 3c CHƯA được so cặp mù.**

| File | Cảnh nguồn | Chữ (từ) | Claim | Cỡ | Tương phản 10% (min) |
|---|---|---|---|---|---|
| `thumb-2b.png` | KEY-3 K3 t = 6,48 s (cùng hình thumb-2: nửa trái nhiều ô đỏ, nửa phải gần sạch) | "1954–1980" · "vs" · "1981 on" (4), đặt dưới lưới, nhãn trước dưới nửa trái | `period_early_label`, `period_late` | 100 px | 7,21 |
| `thumb-3b.png` | KEY-6 K6 t = 9,6 s (thu 0,88) | "Worst case:" · "April 1977" (4); bỏ "43% more" | `worst_start` | 100 px | 7,49 |
| `thumb-3c.png` (**đề xuất thay 3b**) | KEY-7 `k7.js` t = 9,8 s (khe khởi đầu rộng nhất; cột "trước 1981" còn đỏ, cột "từ 1981" sạch) | "How much" · "lower?" (3), không số | — | 100 px | 16,46 |

Cả ba: huy hiệu ILLUSTRATIVE 32 px, đúng 1280×720, token 100%, mọi số khớp claim, S10 0 khớp (`selfcheck.json`, `legibility-25.png` có đủ 6 ảnh).

Nhận định của người làm gói về 3b: **vẫn nghiêng về vi phạm.** "Worst case:" nói rõ đây là trường hợp xấu nhất, nhưng thumbnail vẫn chỉ cho thấy **một** kết quả (xấu nhất) mà không có hai thời kỳ. Hình khối đỏ chồng lên vẫn có thể đọc thành "thả nổi tệ". Vì vậy tôi đề xuất **3c** (KEY-7: khởi đầu thấp hơn so với hai nửa lịch sử). 3c cho thấy cả hai nửa bằng hình, không in số. Câu hỏi "How much lower?" hứa đúng đáp án của phim. Lưu ý: 3c lặp ý của tiêu đề A2 ("How Much Lower"), nên hợp với A1 hơn. 2b và 3c không mang số kết quả. Trường hợp xấu nhất vẫn nằm trong phim và trong mô tả.

Khi chủ dự án chọn, các biến thể được chọn sẽ được chép đè lên `thumb-2.png`/`thumb-3.png` (tên mà hợp đồng M3, F11 và P01 đọc). Bản gốc chuyển sang `evidence/`. Việc này chưa làm.

**Luật máy (đo bằng chính hàm trong `checks/py`, chỉ đọc):**
- **F11 PASS** (40 artefact M3 đã khai, 0 thiếu; gồm `out/package/thumb-1..3.png/.json`).
- **P01 FAIL (cấp THAM KHẢO)** chỉ ở một metric: "thumb texts below 90 px" = 3, đều là huy hiệu ILLUSTRATIVE 32 px. Kích thước 3/3 đúng, token share 99,997–99,999%, tương phản 10% (gồm huy hiệu) 3,67 / 3,77 / 3,77 ≥ 3. Đây là ngoại lệ chủ dự án đã chốt ở Tập 1 (minh bạch trước, huy hiệu nhỏ vẫn phải có; đề xuất sửa P01 ở `packaging.md` §5).
- **P02** chưa có trong `checks/` (mới là đề xuất §5). `selfcheck.json` đo thay: tiêu đề ≤ 60 ký tự (58, 57), mọi số khớp `display` của claim, S10 0 khớp.

## 3. Căng thẳng cần chủ dự án biết (báo, không tự quyết)
1. **Mọi thumbnail đều là hình khoản vay của Leah** (kể cả thumbnail trung tính dùng để thử), nên không có phương án "sạch P01" mà vẫn giữ huy hiệu. Bỏ huy hiệu thì sai S08; giữ thì P01 báo (tham khảo).
2. **thumb-2 "14.2% cost more"** có thể bị đọc thành "đắt hơn 14.2%" (thực ra: 14.2% số cửa sổ có tổng lãi cao hơn). Trong 24 lượt kiểm mù không lý do nào viết như vậy; các lý do khi thumb-2 thua dùng những chữ như "vague", "abstract", "hard to read" (nguyên văn ở `results.md`).
3. **thumb-3 chỉ cho thấy trường hợp xấu nhất** (1 trong 753 cửa sổ; `worst_start`, `worst_share_of_fixed`). Chữ "alarming"/"alarmist" xuất hiện trong 3 lý do nguyên văn: 2 lần là lý do **không** chọn thumb-3 (vai G, R), 1 lần là lý do chọn nó (vai P). Phim đặt nó cạnh 14.2% và 3.5%; thumbnail thì không. Đây là chỗ gu: hút hơn hay cân bằng hơn.
4. **thumb-1 bỏ chữ "fixed"/"variable"** trên thẻ (tiêu đề A1 đã nói, §1.1 không lặp). Nếu chọn A2 (không có chữ "fixed"), hai số "9%"/"7.5%" thiếu nhãn; tổ hợp A2 + thumb-1 chưa được thử.
5. Không thumbnail nào in nghịch lý 76.2% / 14.2% (giữ trong phim theo C1).

## 4. So cặp mù (THAM KHẢO): `review-c6/pack-test/results.md`
72 agent sonnet mới, mỗi agent một ảnh, 4 vai chia đều (sinh viên sau đại học, phụ huynh đồng ký, người refinance, người tò mò). Ý đồ ghi trước: `intent.md`.
- **Vòng tiêu đề** (thumbnail trung tính cố định): A1 **14/16** · A2 8/16 · đối chứng yếu 2/16. A1–A2 trực tiếp: A1 7/8. A2 mạnh nhất ở vai sinh viên (3/4), yếu nhất ở vai tò mò (1/4).
- **Vòng thumbnail** (tiêu đề A1 cố định): thumb-3 **19/24** · thumb-1 **18/24** · thumb-2 9/24 · đối chứng yếu 2/24. thumb-1 với thumb-3 hoà 4–4: người refinance chọn thumb-1 (6/6 cả vòng), người tò mò chọn thumb-3 (6/6).
- Bộ đo phân biệt được (đối chứng yếu ≤ 12,5%). Lệch vị trí: vòng tiêu đề chọn ô 1 15/24, vòng thumbnail 20/48.

Thẻ kết quả tìm kiếm cho chủ dự án xem (không đưa cho người đọc mù): `cards/card-title-*.png`, `cards/card-*.png`.

## 5. Câu hỏi cho chủ dự án (C6, ≤ 3)
1. **Tiêu đề:** A1 (tiêu đề nháp C1) hay A2?
2. **Thumbnail:** Test & Compare chỉ gồm ảnh đạt claim-risk. Đề xuất **thumb-1, thumb-2b, thumb-3c**, hoặc thay 3c bằng 3b nếu chủ dự án cho rằng 3b đạt. Ảnh nào làm mặc định? (2b, 3b, 3c chưa so cặp mù; thumb-2/thumb-3 gốc chỉ là bằng chứng.)
3. **Huy hiệu 32 px và P01:** giữ ngoại lệ như Tập 1 (đề xuất) hay bỏ số khỏi thumbnail?
