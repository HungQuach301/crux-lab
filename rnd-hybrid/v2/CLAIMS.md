# Claim lịch sử của clip vòng 2 — đối chiếu nguồn gốc (14/10/2026)

Mỗi câu có số hoặc mốc đều được kiểm lại (kể cả nguyên văn luật 1934, N7) bằng nguồn gốc mà phiên tải về và đọc được. Tệp gốc lưu ngoài git; trong repo chỉ giữ SHA-256 và câu trích nguyên văn.

## Nguồn đã tải
| Mã | Nguồn | URL | SHA-256 của tệp tải về |
|---|---|---|---|
| N1 | HUD, *Federal Housing Administration History* (trang cơ quan) | https://www.hud.gov/aboutus/fhahistory | trang HTML động, không băm |
| N2 | FHA, *First Annual Report of the Federal Housing Administration* (1935, House Doc. 88, 74th Congress), bản PDF ở HUD User | https://www.huduser.gov/portal/sites/default/files/pdf/First-Annual-Report-of-the-Federal-Housing-Administration.pdf | `04d6e5cf2a3ceaa42517f067eb6a3c1e8ddd7fd6bd65dc4a8b60fbd2036051fe` |
| N3 | Federal Reserve History, G. Richardson, *Banking Panics of 1930–31* | https://www.federalreservehistory.org/essays/banking-panics-1930-31 | trang HTML động |
| N4 | Federal Reserve History, *Redlining* | https://www.federalreservehistory.org/essays/redlining | trang HTML động |
| N5 | Federal Reserve Bank of St. Louis, *Review*, 11/1955, "Federally underwritten mortgages…" (FRASER) | https://fraser.stlouisfed.org/files/docs/publications/frbslreview/rev_stls_195511.pdf | `16fa…`: xem dưới* |
| N7 | **National Housing Act**, 27/6/1934, Public No. 479, 73rd Congress, 48 Stat. 1246 (govinfo) | https://www.govinfo.gov/content/pkg/STATUTE-48/pdf/STATUTE-48-Pg1246.pdf | `c0b2e8c1feac974da539bfbee3547a4af1d5823e77d5b99af342a23343233f3d` |
| N6 | LoC, hồ sơ cph.3c17261 | https://www.loc.gov/item/96521489/?fo=json | `19a43d19…` (RIGHTS §F6 X-RND-1) |

\* SHA-256 của N5: `16c4a55b8bae79021d47e9aed8f8333eba34c0155c748fabffc4ee7fb0960722`.

## Claim → nguồn (trích nguyên văn)
| Câu trong lời | Nguồn | Trích nguyên văn | Kết luận |
|---|---|---|---|
| s02 "A bank lent about half the price." · thẻ "≈ HALF THE PRICE" | N1 | "Mortgage loan terms were limited to 50 percent of the property's market value." | Khớp. Nguồn nói "giới hạn 50 % giá thị trường"; lời nói "about half" là cách diễn đạt gần đúng |
| s03 "You had three to five years." · thẻ "3–5 YEARS" | N1 | "This included a repayment schedule spread over three to five years and ending with a balloon payment." | Khớp. Vòng 1 ghi "five years" là thiếu, nay đã sửa thành 3–5 |
| s04 "Then the whole loan came due, all at once." | N1 | "…ending with a balloon payment." | Khớp |
| s06 "In December 1930, New York's Bank of United States closed." | N3 | "But on December 11, the fourth-largest bank in New York City, Bank of United States, ceased operations." (đoạn về đợt hoảng loạn "In November 1930…") | Khớp. Ngày đóng cửa là **11/12/1930** |
| s07 "In 1931, its depositors still crowded outside." · ảnh LoC | N6 | Tiêu đề: "[Crowd of depositors gather in the rain outside Bank of United States after its failure]"; `date`: "1931." | Năm **1931 là năm LoC ghi cho tấm ảnh**, không phải năm đóng cửa. Tiêu đề LoC có chữ "after its failure", nên không mâu thuẫn với N3. Phiên chưa tìm được nguồn độc lập xác nhận ngày chụp, nên lời chỉ nói "In 1931" đúng như LoC ghi |
| s08 "In 1934, Congress created the FHA." | N1 | "Congress created the FHA in 1934." | Khớp |
| s09 "…up to eighty percent of the value," · thẻ "UP TO 80% OF VALUE" | N2 tr. 16 | "To be eligible for insurance, a mortgage must be for a principal amount not exceeding $16,000, nor 80 percent of the appraised value of the property…" | Khớp. Chính xác là 80 % **giá thẩm định** |
| s10 "paid down every month," | N2 tr. 16–17 | "A payment is to be made each month by the borrower… (d) Amortization payment on the principal of the mortgage." · "…the borrower may obtain the security of a fully amortized long-term loan." | Khớp |
| s10 "…for up to twenty years." · thẻ "UP TO 20 YEARS" | **N7 §203(b)(3)** (nguồn gốc), N4 | N7: "(3) Have a maturity satisfactory to the Administrator, but not to exceed twenty years. (4) Contain complete amortization provisions…" · N4: "…the 15- to 20-year loans they were attempting to standardize." | **Khớp nguyên văn luật 1934**: tối đa 20 năm, trả dần toàn phần. Mục §203(b)(2) cùng tệp cũng xác nhận 80 %: "not to exceed 80 per centum of the appraised value" |
| s12 "In 1954, the limit stretched to thirty years." · thẻ "1954: UP TO 30 YEARS" | N5 tr. 3 | "…the maximum maturity permitted by law on existing homes was 20 years, and on new homes 25 years." · "[Housing Act of 1954, effective October 1, 1954] The maximum maturity was increased on new construction from 25 to 30 years and on existing properties from 20 to 30 years." | Khớp. Có ghi chú: kỳ hạn 30 năm cho nhà cũ không được vượt 3/4 tuổi thọ còn lại của căn nhà theo ước tính FHA |
| s13 "The long, monthly mortgage starts here." | — | câu kết, không có số | Không phải claim số. Lời **không** nói "chuẩn hiện nay" như bản vòng 1 |

## Đã bỏ so với vòng 1
- "At its worst, in 1933, around a thousand homes were foreclosed every day": PDF Wheelock (2008) ở St. Louis Fed tải không được (FRASER chuyển hướng hỏng), nên chưa có nguồn gốc. Claim này đã **bỏ**.
- "Most people simply signed a new one" (gia hạn khoản vay): N1 không nói điều này, nên câu này cũng **bỏ**. Lời mới chỉ nêu điều kiện: "No new loan? You could lose the house."
- "Later, those terms stretched to thirty years": thay bằng mốc có nguồn là 1954 (N5).

## Còn mở
- Có nguồn thứ cấp nói kỳ hạn 25 năm (1938) và 30 năm cho nhà xây mới (1948) có trước 1954. N5 chỉ nói tình trạng luật vào mùa xuân 1954 (sau đợt kiểm soát tín dụng năm 1953). Lời "In 1954, the limit stretched to thirty years" đúng với N5 khi hiểu là "giới hạn chung cho cả nhà mới và nhà cũ". Nếu tập cần nói "lần đầu có 30 năm" thì phải tra Housing Act 1948.
