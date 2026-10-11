# Danh sách kênh cùng chủ đề — Phiên Thị trường (`market-r1`, 2026-10-11)

Sinh bằng `python3 toolkit/market/report.py channels` từ `~/market-cache/<ngày>/` (ngoài git). **Không có số liệu thô** (lượt xem, người đăng ký, like): chỉ định danh kênh, vòng tròn, nhãn và lý do. "Video nổ" = video có hệ số vượt trội ≥ 5× (lượt xem / trung vị kênh ±90 ngày, ≥ 10.000 lượt; **tự tính, không phải chỉ số YouTube**). Cỡ kênh: lớn ≥ 100 nghìn, vừa ≥ 10 nghìn, nhỏ dưới — nhãn, không phải số.

**Cách chọn** (`toolkit/market/discover.py`): tìm theo VIDEO trước — 21 đề tài (19 dòng hàng đợi + 2 "từ hạt giống") × 3 lượt search (30 ngày theo lượt xem, 90 ngày theo lượt xem, top 20 theo độ liên quan; regionCode US, tiếng Anh, 4–20 phút) + 3 search vòng "hình thức". Ứng viên = kênh có video dài xuất hiện ở **≥ 3 đề tài**, + kênh nổi bật (channelSections) của chúng, + kênh **mới nổi** (kênh < 2 năm có video ≥ 3× số người đăng ký hoặc lượt xem/ngày thuộc 10 % cao nhất), + hạt giống chủ dự án. Phân loại vòng tròn và lý do loại: Haiku headless trên tên + mô tả + 15 tiêu đề gần nhất (máy đoán, có thể sai — sửa ở đây).

**Không dừng hỏi duyệt, không phải câu hỏi G1.** Nếu muốn sửa, chủ dự án ghi tự do trong câu trả lời G1 Tập 7 ("bỏ kênh X / thêm kênh Y"); không ghi gì = giữ. Hiệu chỉnh hằng tháng theo nguồn "video đề xuất" khi có Analytics kênh mình (`playbook/episode.md` §10).

## Từ chủ dự án (bỏ thử việc)

| Kênh | Vòng | Kiểu | Video nổ | Ghi chú |
|---|---|---|---|---|
| [Logical Money](https://www.youtube.com/channel/UCKhpM-cu2Cod-GyG6KngNYg) | trực tiếp (hạt giống) | narrated money-psychology lessons with stories | 3 | mổ xẻ: `market/teardowns/` |
| [Jack Explains Money](https://www.youtube.com/channel/UCZJnbHQTYBy1I8GpHlsAUMg) | trực tiếp (hạt giống) | general money tips and lifestyle comparisons | 5 | mổ xẻ: `market/teardowns/` |

## Vòng trực tiếp — giải thích / dữ liệu tài chính cá nhân Mỹ, video dài

| Kênh | Cỡ | Kiểu (máy tả) | Video nổ | Vì sao vào |
|---|---|---|---|---|
| [Hannah Invests](https://www.youtube.com/channel/UCNF5Np30COaoOZSYu9hKa7A) | nhỏ | animated story-driven explainers with compounding examples | 6 | mới nổi: lượt xem ≥ 3× người đăng ký, lượt xem/ngày cao · kênh < 2 năm, ≥ 2 video nổ → lên thẳng |
| [James Retires](https://www.youtube.com/channel/UCHpnFtErfky9Td9JIwypF8g) | nhỏ | step-by-step US retirement tax breakdowns with dollar examples | 2 | mới nổi: lượt xem ≥ 3× người đăng ký · kênh < 2 năm, ≥ 2 video nổ → lên thẳng |
| [Tom – Lazy Real Estate](https://www.youtube.com/channel/UCDOCO-HOYrwDpIu_a-9f4KQ) | nhỏ | year-by-year net-worth scorecards | 1 | ≥ 3 đề tài |
| [Finance Flow](https://www.youtube.com/channel/UCjN2vUJcsQezdjFxSfJFxmw) | nhỏ | animated what-if investing simulations | 1 | ≥ 3 đề tài |
| [Rich by Routine](https://www.youtube.com/channel/UCtsSIzNJVBR1Az9d5b5XTbw) | nhỏ | "The Real Math" comparison breakdowns | 0 | ≥ 3 đề tài |

## Vòng lân cận — giáo dục tài chính có mặt người (nói trước máy, cố vấn, podcast)

| Kênh | Cỡ | Kiểu (máy tả) | Video nổ | Vì sao vào |
|---|---|---|---|---|
| [Erin Talks Money · Erin Moriarity](https://www.youtube.com/channel/UCpXipTyhIY9kprpvVd-lu0A) | lớn | host commentary on retirement and money | 39 | ≥ 3 đề tài |
| [Holy Schmidt!](https://www.youtube.com/channel/UCl9IwlpNczNQllEfeIrzscQ) | lớn | retirement advice talk | 19 | ≥ 3 đề tài |
| [Bob Sharpe](https://www.youtube.com/channel/UCWAbnw-xB8x47xrfhtlDC9Q) | lớn | talking-head investing advice | 16 | ≥ 3 đề tài |
| [MoneywithSwAbi](https://www.youtube.com/channel/UCuo7iQC6soA3ExG4IMMZC8g) | vừa | FIRE creator story and tax-aware planning | 12 | ≥ 3 đề tài |
| [Home Loan Education](https://www.youtube.com/channel/UCugwwKRUS5juG0qYif2HABA) | vừa | loan officer math walkthroughs | 10 | ≥ 3 đề tài |
| [Retirement 4 the Rest of Us](https://www.youtube.com/channel/UC7HWHEt9zMnuRonSglOe3oQ) | vừa | advisor-style retirement talk | 9 | mới nổi: lượt xem/ngày cao · kênh < 2 năm, ≥ 2 video nổ → lên thẳng |
| [Dividend Hustle Mark](https://www.youtube.com/channel/UCtDoMEqEFNoSq2J2A7fuFpQ) | nhỏ | retirement income and yield rankings | 9 | mới nổi: lượt xem ≥ 3× người đăng ký, lượt xem/ngày cao · kênh < 2 năm, ≥ 2 video nổ → lên thẳng |
| [Fund It.](https://www.youtube.com/channel/UCDyw-rKFdNBMhpak-DmbohQ) | nhỏ | edited clips from talking-head finance speakers | 7 | mới nổi: lượt xem/ngày cao · kênh < 2 năm, ≥ 2 video nổ → lên thẳng |
| [Sparky](https://www.youtube.com/channel/UC2pwSPZTSpRUcuVIf8FLoLw) | nhỏ | first-person money-story listicles | 2 | mới nổi: lượt xem ≥ 3× người đăng ký · kênh < 2 năm, ≥ 2 video nổ → lên thẳng |
| [Affordable Retirement Abroad](https://www.youtube.com/channel/UC_wTStQtEKl8fk4vxAfK0hA) | nhỏ | on-the-ground retirement cost audits | 2 | mới nổi: lượt xem ≥ 3× người đăng ký, lượt xem/ngày cao · kênh < 2 năm, ≥ 2 video nổ → lên thẳng |

## Vòng hình thức — giải thích bằng dữ liệu ngoài tài chính — **chỉ học đóng gói**

| Kênh | Cỡ | Kiểu (máy tả) | Video nổ | Vì sao vào |
|---|---|---|---|---|
| [Data Penguin](https://www.youtube.com/channel/UCv09moG9-_c1DafpwBHLV3Q) | nhỏ | data-driven world-comparison visuals | 13 | mới nổi: lượt xem ≥ 3× người đăng ký, lượt xem/ngày cao · kênh < 2 năm, ≥ 2 video nổ → lên thẳng |
| [TierLine](https://www.youtube.com/channel/UC_QmXnQUVEthT2i3Y-lF1oA) | nhỏ | animated ranking countdown race | 2 | mới nổi: lượt xem ≥ 3× người đăng ký, lượt xem/ngày cao · kênh < 2 năm, ≥ 2 video nổ → lên thẳng |
| [Healthy Wealthy Life Hack Picks](https://www.youtube.com/channel/UCtEZdShBmMsq858MVXRfsfg) | nhỏ | faceless science and tech explainers | 0 | ≥ 3 đề tài |

## Mới nổi — thử việc 90 ngày (đến 2027-01-09)

Kênh < 2 năm. **≥ 2 video nổ trong 90 ngày → lên vòng tương ứng**; không thì bỏ ở lần làm mới sau hạn. Phần lớn là kênh không mặt người, mới mở — cùng khuôn với Crux nên là đối thủ trực tiếp nếu sống sót.

| Kênh | Vòng (máy đoán) | Kiểu | Video nổ | Vì sao vào |
|---|---|---|---|---|
| [WealthCraft](https://www.youtube.com/channel/UCoIB14v81iJHcjFdV7iIB_A) | lân cận | POV lifestyle narrative | 1 | ≥ 3 đề tài |
| [Yudi J - NRI Personal Finance](https://www.youtube.com/channel/UCVqlWPMM32FOnQ9-DABnBlQ) | lân cận | personal talking-head guidance for Indian immigrants in the US | 0 | mới nổi: lượt xem ≥ 3× người đăng ký, lượt xem/ngày cao |
| [Retirement Without Kids with Ari Taublieb, CFP®](https://www.youtube.com/channel/UCtd_UQcUq7368v7ENPQTpJg) | lân cận | CFP advisor talking head | 0 | mới nổi: lượt xem ≥ 3× người đăng ký, lượt xem/ngày cao |
| [Calm Dollar](https://www.youtube.com/channel/UCyN8MSuZ27wOJZAzIBJFY0g) | lân cận | calm plain-English US money explainers | 0 | ≥ 3 đề tài |
| [DOAC Money Moments](https://www.youtube.com/channel/UCzwWL05SqOntZAruBD4fKMQ) | lân cận | podcast money-moment clips with expert interviews | 0 | mới nổi: lượt xem ≥ 3× người đăng ký, lượt xem/ngày cao |
| [Devil in the Decimal](https://www.youtube.com/channel/UC2TaG60rXcbrws_Wf7T601w) | trực tiếp | real-math comparison explainers with illustrative scenarios | 0 | ≥ 3 đề tài |
| [The Hidden Money Equation](https://www.youtube.com/channel/UCDbMUAvYE7fPubKesEHrtmA) | trực tiếp | animated scenario stories with real numbers | 0 | ≥ 3 đề tài |
| [Davidson Money Stories](https://www.youtube.com/channel/UCWodeFwozcefCEW2l-MP_6w) | trực tiếp | animated two-character scenario math | 0 | mới nổi: lượt xem/ngày cao |
| [Mr Finance Wise](https://www.youtube.com/channel/UCcg7VnTDboJDOIz3CMsve6g) | trực tiếp | 2D animated math comparisons | 0 | mới nổi: lượt xem ≥ 3× người đăng ký, lượt xem/ngày cao |
| [Worthspring](https://www.youtube.com/channel/UChllrfC2MDdVnilJdVX4-sw) | trực tiếp | simple investing explainers with real numbers | 0 | ≥ 3 đề tài |
| [Grayson Invests](https://www.youtube.com/channel/UCjKDjHbyiChzOhV-WC8S0vg) | trực tiếp | animated money-math explainers | 0 | ≥ 3 đề tài |
| [Money Rerouted](https://www.youtube.com/channel/UCtpaYePfaqqBsD0SFwlEQwg) | trực tiếp | worked-example loan and rate math | 0 | ≥ 3 đề tài |
| [MoneyMechanics](https://www.youtube.com/channel/UCuGKWV2U0dyfk89LtRxm5AQ) | trực tiếp | plain-English topic explainers with worked math | 0 | ≥ 3 đề tài |
| [In Depth Analysis](https://www.youtube.com/channel/UCWjOxV02a6UpzILHx98BkCg) | hình thức | data-driven narrated explainer | 0 | mới nổi: lượt xem ≥ 3× người đăng ký, lượt xem/ngày cao |

## Đã loại

Luật loại: bán khoá học/chọn cổ phiếu, tin tức, không phải tiếng Anh/khán giả Mỹ, không có video dài trong 90 ngày (và ngoài đề tài, bán sản phẩm).

| Kênh | Lý do |
|---|---|
| [AJ Retires Tips](https://www.youtube.com/channel/UC0aIEMpdTCjfZbS17TNF7ZQ) | bán sản phẩm, không phải khán giả Mỹ / tiếng Anh |
| [Aussie Wealth With Finn](https://www.youtube.com/channel/UC-GBKaUc2pW3mDYnLQg8MfA) | không phải khán giả Mỹ / tiếng Anh |
| [Autotrends](https://www.youtube.com/channel/UCdDNg5k8iJojFaJWoS121Uw) | tin tức, ngoài đề tài |
| [British Mortgages with Jack](https://www.youtube.com/channel/UCnpki_Vxaw98NNnSjaS7FWw) | không phải khán giả Mỹ / tiếng Anh |
| [Filipino Way](https://www.youtube.com/channel/UCsBB7JYXEV_W8uVh4yrSSag) | ngoài đề tài |
| [Graham Stephan](https://www.youtube.com/channel/UCV6KDgJskWaEckne5aPA0aQ) | tin tức |
| [HinExp](https://www.youtube.com/channel/UCytiKJcsuKFARvAeUABvRBA) | không phải khán giả Mỹ / tiếng Anh |
| [Jeff & Sarah Reed - Gold IRA Blueprint](https://www.youtube.com/channel/UClR2DV-thtqsaY5p1jNBc0Q) | bán sản phẩm |
| [Josh K. Fay](https://www.youtube.com/channel/UCWr4GiYhA8ssmBZJl6dkUKQ) | không phải khán giả Mỹ / tiếng Anh |
| [Learning to Retire](https://www.youtube.com/channel/UC0T5vJJEl1337CoNqxQI45w) | không phải khán giả Mỹ / tiếng Anh |
| [Marissa Van](https://www.youtube.com/channel/UCc8mgmxzl_Yhf9PlvElZ68w) | ngoài đề tài |
| [Money Mindset With Luke](https://www.youtube.com/channel/UCl18g6vdg0a2YoWG6gvem1A) | không phải khán giả Mỹ / tiếng Anh |
| [Nathan Udomsri](https://www.youtube.com/channel/UCqRwPJ5UDRa6wPmi9fPJZrw) | bán sản phẩm |
| [Nishant Gawande, Retirement Planner](https://www.youtube.com/channel/UCS4M7TXiS-xV2kqgaf0G3jw) | không phải khán giả Mỹ / tiếng Anh |
| [Own in Paradise - Maxim Baginskiy](https://www.youtube.com/channel/UCWwumZsLJxyhyjAWDm4VgBQ) | bán sản phẩm |
| [Retire or Rehire](https://www.youtube.com/channel/UCOg_wd3rtA6HVeR1IaeJGWw) | không phải khán giả Mỹ / tiếng Anh |
| [Scrimp and Spend](https://www.youtube.com/channel/UCpxabBXB2UAt2grCl0pIJ9g) | không phải khán giả Mỹ / tiếng Anh |
| [The Graham Stephan Show](https://www.youtube.com/channel/UCa-ckhlKL98F8YXKQ-BALiw) | tin tức, ngoài đề tài |
| [The Iced Coffee Happy Hour](https://www.youtube.com/channel/UC4sf1VBOWrlBh_bCnCOdvwQ) | ngoài đề tài, không có video dài trong 90 ngày |
| [The Iced Coffee Hour](https://www.youtube.com/channel/UCMSYZVlQmyG8_2MkIKzg0kw) | ngoài đề tài |
| [The Iced Coffee Hour Clips](https://www.youtube.com/channel/UCeBQ24VfikOriqSdKtomh0w) | ngoài đề tài |
| [The Real Car Dealer](https://www.youtube.com/channel/UC0rI_kRLLvxyZ6AjjzX81yA) | ngoài đề tài |
| [UK Finance Simplified](https://www.youtube.com/channel/UCtxnhpliXK2GhCPvJHie_Ww) | không phải khán giả Mỹ / tiếng Anh |
| [Wall Street Truthbombs](https://www.youtube.com/channel/UCTK_cv-y88CScoudcXnS1Ew) | tin tức |
