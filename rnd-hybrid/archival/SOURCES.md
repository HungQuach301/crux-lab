# Tư liệu phạm vi công cộng — rnd-hybrid (14/10/2026)

## Kết quả truy cập: **bị chặn, chưa tải tệp nào**
Thử từ container (curl qua proxy) và WebFetch, 06:16–06:45 UTC 14/10/2026:

| Host | curl (proxy) | WebFetch |
|---|---|---|
| www.loc.gov, tile.loc.gov | 403 CONNECT (chính sách mạng) | `getaddrinfo ENOTFOUND` |
| catalog.archives.gov, www.archives.gov, images.archives.gov | 403 / 000 | — |
| www.hud.gov, www.huduser.gov | 403 / 000 | — |
| commons.wikimedia.org, upload.wikimedia.org, dp.la, digitalcollections.nypl.org, fraser.stlouisfed.org, docsteach.org | 000 | ENOTFOUND |
| fred.stlouisfed.org, s3.amazonaws.com, elevenlabs.io | 200 / 307 | — |

→ Không có dòng RIGHTS §F6 nào được ghi (F5: ghi trước khi dựng, chỉ khi có tệp + nhãn quyền trích nguyên văn).
Để mở: chủ dự án thêm `www.loc.gov`, `tile.loc.gov`, `catalog.archives.gov`, `s3.amazonaws.com` (đã mở) vào *Allowed domains* của môi trường
(menu môi trường → Edit → Network access; https://code.claude.com/docs/en/cloud-environments#network-access), **hoặc** tự tải theo bảng dưới.

## URL cụ thể cho chủ dự án tải (ứng viên; quyền CHƯA đọc được — phải kiểm khi tải)
Thủ tục mỗi tệp (RIGHTS §F1 bậc 5, §F5): mở URL JSON, chép nguyên văn `rights_advisory` (LoC) / "Use restrictions" (NARA), lưu bản chụp
JSON + `sha256sum`, tải bản TIFF/JPEG lớn nhất, đặt ở `rnd-hybrid/work/external/<slot>.jpg` (ngoài git), rồi ghi dòng `X-RND-n` ở RIGHTS §F6.
Clip đọc tệp qua `rnd-hybrid/work/external/manifest.json` (`{"bank1931": "/rnd-hybrid/work/external/bank1931.jpg", …}`), không đổi mã.

| Ô trong clip | Ứng viên | URL nhãn quyền (JSON) | Dự kiến bậc | Ghi chú |
|---|---|---|---|---|
| `bank1931` (cảnh G, 1931) | Crowd at Bank of United States after its failure, NY, 1931 — NYWT&S Collection, LoC `cph.3c17261` | https://www.loc.gov/pictures/resource/cph.3c17261/?fo=json (id item `/item/…` lấy từ trang resource) | 5 (nhãn LoC thường "No copyright restriction known…" cho NYWT&S — **chưa xác minh**) | Bản sao Wikimedia ghi "No copyright restriction known" (qua kết quả tìm kiếm) |
| `bank1931` (thay thế, 1932) | *Depositors in Front of the Closed American Union Bank in New York City*, 26/4/1932, NARA NAID **12573155** (RG 306, USIA) | https://catalog.archives.gov/id/12573155 · API: https://catalog.archives.gov/api/v2/records/search?naId=12573155 | 1 nếu NARA ghi "Unrestricted"/public domain và người chụp là nhân viên liên bang; ảnh báo chí trong RG 306 → bậc 5 | DocsTeach ghi "public domain" (qua kết quả tìm kiếm) |
| `fsa_auction` (cảnh I, 1936) | Arthur Rothstein, *Auction* / *Hurrying to the auction*, Kearney, Nebraska, 05/1936 (FSA/OWI) — bản LoC cần tìm theo tiêu đề | https://www.loc.gov/collections/fsa-owi-black-and-white-negatives/?q=Rothstein+auction+Kearney&fo=json | 5 ("No known restrictions on images made by the Farm Security Administration…" là nhãn chung của bộ — **đọc theo từng tệp**) | NYPL có bản sao cùng tiêu đề (qua kết quả tìm kiếm) |
| dự phòng (nhà mới 1930s) | Rothstein, Irwinville Farms, GA, 1935 — LoC **2017765777**; Mydans, 1936 — LoC **2017767302** | https://www.loc.gov/item/2017765777/?fo=json · https://www.loc.gov/item/2017767302/?fo=json | 5 | Nhà tái định cư FSA/RA, **không phải** FHA → chỉ dùng với chú thích đúng, không đặt dưới lời "FHA" |
| dự phòng (HOLC/FHLBB) | Records of the Federal Home Loan Bank Board, RG 195 (bản đồ/khảo sát 1935–40) | https://catalog.archives.gov/search?q=%22Home%20Owners%27%20Loan%20Corporation%22&typeOfMaterials=photographs | 1 (tài liệu cơ quan liên bang) — FRASER ghi "No Copyright - United States (NoC-US)" cho bộ (qua kết quả tìm kiếm) | Bản đồ "redlining" nhạy cảm; chỉ khi tập bàn về nó |
| HUD | FHA 1934 (ảnh/ấn phẩm cơ quan) | https://www.huduser.gov/portal/ (tìm "FHA history photographs") | 1 nếu là tác phẩm nhân viên HUD/FHA | Chưa có URL tệp cụ thể |

## Số trong lời nháp và nguồn
| Claim | Hiển thị | Nguồn | Trạng thái |
|---|---|---|---|
| Khoản vay nhà trước 1934 thường ≤ 5 năm, ít/không trả gốc | lời s03–s05 (không số trên hình ngoài "5 YEARS") | St. Louis Fed, thông cáo 02/05/2008 về Wheelock (2008), *The Federal Response to Home Mortgage Distress*, FRB St. Louis Review 90(3): "many of the home loans … lasted no more than five years" (qua kết quả tìm kiếm) | cần đọc bản PDF gốc |
| Đỉnh 1933 ≈ 1.000 khoản vay nhà bị tịch biên mỗi ngày | J: "≈1,000" | cùng thông cáo, trích Wheelock: "At its worst, in 1933, around 1,000 home loans were foreclosed every day." | cần đọc bản PDF gốc |
| FHA (Đạo luật Nhà ở Quốc gia 1934) bảo hiểm khoản vay dài, trả dần hằng tháng; kỳ hạn sau kéo tới 30 năm | lời s10–s13 | kiến thức chuẩn (Green & Wachter 2005, *JEP* 19(4)) — **chưa trích trong phiên** | cần nguồn trích |
| $5,000 / $0 (cảnh N) | thanh | dựng bằng mã: khoản vay chỉ trả lãi 5 năm vs trả dần hết | ILLUSTRATIVE |
