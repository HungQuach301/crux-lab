# R3 — Kênh mới bùng nổ (chủ dự án 29/10/2026)

**Câu hỏi:** video dài nào (≥ 3 phút, không phải Short) đạt ≥ 1.000.000 lượt xem trong 7 ngày đầu, trên kênh được tạo ≤ 31 ngày trước ngày đăng video? Chúng có mẫu chung nào, và mẫu nào áp được cho Money Rerouted?

**Dữ liệu:** chỉ YouTube Data API v3, số công khai, lấy ngày 29/10/2026. Không dùng trình duyệt tự động, không cào HTML, không dùng agent con. Số thô ở `market/r3/*.json`. Chủ dự án 29/10 cho commit số thô; **hạn làm mới hoặc xoá: 28/11/2026** (YouTube API Developer Policies III.E.4). Mã ở `toolkit/market/r3/`. Mọi tỉ số tự tính ghi **"tự tính, không phải chỉ số YouTube"**.

## Kết luận ngắn

1. **19 video đạt** (mục tiêu ~20): 3 lớp A (chắc chắn) · 11 lớp B1 (đạt cả khi giả định bi quan) · 5 lớp B2 (chỉ đạt ở giả định giữa). **8 video tiếng Anh**; 11 video Hindi, Bengal, Tây Ban Nha, Telugu, Odia.
2. **Tài chính cá nhân: 0 video đạt.** Video gần nhất là "economics of sleeper buses" (Business by baniya). Nó bị loại vì kênh đổi chủ đề đột ngột sau video hit. Video "tiền" duy nhất trong ảnh chụp 0–3 ngày là truyện kể AI kiểu "billionaire pretended…", tức kể chuyện, không phải tài chính.
3. **Không lộ mặt: 15/19.** Lộ mặt gồm 2 kênh Spencer (cùng một người) và 2 kênh doanh nghiệp (hãng phim, hãng nhạc).
4. Mẫu trội của video tiếng Anh: **giải thích một thứ cụ thể, nhìn thấy được**, dài **9–12 phút**, ảnh bìa là **một vật thể hoặc sơ đồ mặt cắt kèm ≤ 4 chữ**, tiêu đề **56–68 ký tự**. Video hit thường là **video thứ 1–4 của kênh**. Shorts gần như không kéo khán giả sang (mục 5e).
5. Lớp A chỉ có 3 (< 10), nên theo bước 4 **cần chủ dự án duyệt trước khi lên lịch chụp hằng ngày** (mục 6). Ảnh chụp ngày đầu đã lưu: `market/r3/snap-20261029.json`.

## 1. Phương pháp

| Bước | Làm gì | Số |
|---|---|---|
| Thu | `search.list` type=video, order=viewCount, relevanceLanguage=en, regionCode=US, 9 cửa sổ 7 ngày phủ 01/09–29/10 (63 ngày). Mỗi cửa sổ 9 truy vấn: 7 truy vấn gộp 25 cụm đề tài bằng toán tử OR (finance·money·personal finance·investing·stock market / economy·business·billionaire·company / true crime·mystery·unsolved·case / history·documentary·war·ancient / AI·tech·technology·explained·science / survival·challenge·story·experiment / gaming·minecraft·podcast·interview·reaction), videoDuration=medium; thêm 1 truy vấn không từ khoá medium và 1 không từ khoá long. Cộng `videos.list chart=mostPopular` US, 15 category (2 category báo 404) | 81 search, 3.829 + 1.836 ID → **5.637 video** |
| Lọc | `videos.list` → ≥ 1M lượt xem: **2.484**; `channels.list` (1.933 kênh) → tuổi kênh lúc đăng ≤ 31 ngày: **42**, trong đó ≥ 180 s: **30** | |
| Kiểm kênh | `playlistItems` (toàn bộ lịch sử đăng của 28 kênh, kênh nào cũng < 150 video) → video đầu tiên, thứ tự của video hit, nhịp đăng, Shorts | |
| Quota | **8.369 / 9.000 đơn vị** (search 8.100; videos 221; channels 41; playlistItems 7) — `market/r3/quota.json` | |

**Nguồn của 19 video đạt:** cụm survival·challenge·story·experiment 9 · history 3 · tech 3 · truy vấn không từ khoá 2 · economy 1 · mostPopular 1. Cụm finance, crime, gaming: 0.

**Gộp đề tài bằng OR, vì sao:** 25 cụm × 9 cửa sổ = 225 search, tức 22.500 đơn vị, quá ngân sách. Gộp bằng OR phủ đủ 25 cụm với 81 search. Đánh đổi: mỗi truy vấn chỉ trả 50 kết quả nhiều lượt xem nhất, nên cụm hẹp dễ bị cụm rộng lấn.

**Giới hạn cần biết:**
- `order=viewCount` trả về kênh lớn trước, nên kênh mới chỉ chiếm 30/2.484 video ≥ 1M. Mẫu này là **đáy lọc qua lưới tìm kiếm**, không phải điều tra toàn bộ.
- `relevanceLanguage` và `regionCode` chỉ ưu tiên, không lọc cứng, nên vẫn lọt nhiều video Nam Á.
- `videoDuration=medium` là 4–20 phút, nên video 3–4 phút chỉ đến qua mostPopular hoặc truy vấn long.
- Video đăng trước 01/09 trên kênh tạo cuối tháng 8 không được quét.

**Phân lớp:**
- **A** = đăng ≤ 8,5 ngày trước và đã ≥ 1M. Lượt xem chỉ tăng, nên 1M đã đạt trong cửa sổ 7–8 ngày.
- **B** = cũ hơn, quy ngược về ngày 7 bằng đường cong chuẩn **V₇ = V_hôm nay × (7/tuổi)^α**:
  - α = 0,3 là giả định giữa: video viral thường có ~60–65 % lượt xem 30 ngày trong tuần đầu.
  - α = 0,5 là giả định bi quan: ~48 %.
  - **B1** đạt cả khi bi quan; **B2** chỉ đạt ở giả định giữa.
- Giả định này **chưa hiệu chuẩn**: ảnh chụp hằng ngày (mục 6) sẽ đo α thật.

**Loại kênh tái dụng hoặc mua lại:** không kênh nào có video đầu tiên cũ hơn ngày tạo kênh. Có 5 kênh bị loại vì đổi chủ đề, tên kênh lệch nội dung, hoặc nghi đăng lại (mục 3).

## 2. Bảng 19 video đạt

Sắp xếp: tiếng Anh trước, rồi theo lớp, rồi theo lượt xem. Lượt xem tính đến 29/10. "Ước ngày 7" = bi quan–giữa (tự tính, không phải chỉ số YouTube). Tuổi kênh tính bằng ngày. **Cờ "nghi QC trả tiền"** = video hit có lượt xem > 100 lần trung vị các video dài khác của kênh, và < 1,5 người đăng ký trên 1.000 lượt xem (tự tính; quảng cáo in-stream có tính lượt xem).

| # | Tiêu đề | Kênh | Tạo kênh | Đăng | Tuổi kênh | Lượt xem | Lớp | Ước ngày 7 | Dài | Ngách · ngôn ngữ | Cờ | Liên kết |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | No Celebrity Told WAR Stories Like Lee Marvin | Drollery | 2026-10-07 | 2026-10-22 | 15.3 | 1.25M | A | đã ≥ 1M | 11:01 | kể chuyện người nổi tiếng Mỹ cổ điển · en | — | [C6-FIlJaPNk](https://www.youtube.com/watch?v=C6-FIlJaPNk) |
| 2 | Shiva Dragon Bike vs Rudra Phoenix Bike / Epic Bike Racing Challenge / 3D Animation | Shiva Rudra World | 2026-09-16 | 2026-09-24 | 8.2 | 7.89M | B1 | 3.52M–4.86M | 5:01 | hoạt hình 3D thiếu nhi (đua xe) · en/hi | nghi QC trả tiền | [hFxcsAyonKw](https://www.youtube.com/watch?v=hFxcsAyonKw) |
| 3 | iPhone Users: Turn This OFF Immediately! (your phone is listening) | Call Spencer! | 2026-10-08 | 2026-10-10 | 2.1 | 5.15M | B1 | 3.15M–3.83M | 15:24 | mẹo công nghệ / quyền riêng tư · en | lộ mặt; cùng người với Spencer Knows! | [rExDQd6hsMU](https://www.youtube.com/watch?v=rExDQd6hsMU) |
| 4 | Nepal Floods 2026 Explained: What Caused the Deadly Flash Flood? | UnderTheHeadline | 2026-08-28 | 2026-08-28 | 0.1 | 4.11M | B1 | 1.38M–2.13M | 12:31 | tin tức giải thích / địa lý · en | — | [u5F175REX_U](https://www.youtube.com/watch?v=u5F175REX_U) |
| 5 | Nobita, Shinchan & Masao Digging Challenge to Get Rich 😱 | KrishoPlays | 2026-09-18 | 2026-10-10 | 22.2 | 2.71M | B1 | 1.64M–2.01M | 10:18 | hoạt hình thiếu nhi (nhân vật có IP) · en | dùng nhân vật Doraemon/Shin-chan | [-70ITYN4RY0](https://www.youtube.com/watch?v=-70ITYN4RY0) |
| 6 | Watch NEW YORK Grow for 400 Years - 3D Timelapse (No AI imagery) | CityEons | 2026-10-03 | 2026-10-17 | 13.8 | 1.63M | B1 | 1.24M–1.38M | 8:58 | lịch sử đô thị timelapse 3D · en | — | [Xn1s4JvDKYY](https://www.youtube.com/watch?v=Xn1s4JvDKYY) |
| 7 | How Did ANCIENT INUIT Igloos Stay Warm at -50°C With NO Electricity? | ZENO | 2026-08-18 | 2026-09-12 | 25.4 | 2.46M | B2 | 0.95M–1.39M | 6:14 | lịch sử cổ đại / "how did" · en | — | [0tSwA12rEtk](https://www.youtube.com/watch?v=0tSwA12rEtk) |
| 8 | Gmail Users: Turn This OFF Immediately! (Google AI scans your email) | Spencer Knows! | 2026-09-10 | 2026-09-20 | 9.6 | 1.85M | B2 | 0.78M–1.10M | 9:15 | mẹo công nghệ / quyền riêng tư · en | lộ mặt; cùng người với Call Spencer! | [7ShrUmwrR1U](https://www.youtube.com/watch?v=7ShrUmwrR1U) |
| 9 | Los Gemelos Yeti 2026 😅 ¡El Yeti ya no puede con ellos! 🐾 Dibujos animados 🎬 | Ye-Ye Yeti en Español | 2026-10-07 | 2026-10-24 | 17.1 | 2.21M | A | đã ≥ 1M | 13:16 | hoạt hình thiếu nhi · es | — | [ejuIUDRjq8M](https://www.youtube.com/watch?v=ejuIUDRjq8M) |
| 10 | Jagdalpur (Episode 1) A Musical Series / Mashaal / Shaan R Grover / Aditi Budhathoki / Coov Records | Coov Records Official | 2026-10-18 | 2026-10-23 | 5 | 2.06M | A | đã ≥ 1M | 12:27 | series nhạc kịch Ấn · hi | lộ mặt; kênh hãng nhạc, có ca sĩ/diễn viên sẵn | [Owv2qnEdqfA](https://www.youtube.com/watch?v=Owv2qnEdqfA) |
| 11 | भिंडी के एक बीज ने बदली गरीब किसान की किस्मत / Moral Story | Shini Ki Dunia  | 2026-08-21 | 2026-09-21 | 30.9 | 3.78M | B1 | 1.62M–2.28M | 11:56 | truyện đạo đức nông thôn · hi | — | [4L4ErMYyMJU](https://www.youtube.com/watch?v=4L4ErMYyMJU) |
| 12 | কোটিপতি স্বামী বউয়ের সামনে কাজের মেয়েকে বিয়ে করলেন কেন? Moral Bangla Story | DipRaj Story | 2026-08-27 | 2026-09-13 | 16.7 | 3.45M | B1 | 1.35M–1.96M | 17:41 | truyện đạo đức / drama gia đình · bn | — | [YLrdEkZncAo](https://www.youtube.com/watch?v=YLrdEkZncAo) |
| 13 | 😱 / Teacher Day से शुरू हुआ एक यादगार सफर / Hindi Cartoon Story | Sabzi ki Story ai | 2026-09-03 | 2026-09-23 | 19.7 | 3.24M | B1 | 1.42M–1.98M | 8:57 | hoạt hình thiếu nhi rau củ · hi | — | [alzq9TYSMX8](https://www.youtube.com/watch?v=alzq9TYSMX8) |
| 14 | गाँव का सफर / Hindi Story / Sabzi Ki Story | Sabzi ki Story ai | 2026-09-03 | 2026-10-02 | 28.7 | 3.05M | B1 | 1.54M–2.03M | 10:25 | hoạt hình thiếu nhi rau củ · hi | — | [ZQSOransWxk](https://www.youtube.com/watch?v=ZQSOransWxk) |
| 15 | Thulabharam - The Title Documentary / Ravi Teja / Vivek Athreya / Vivek Sagar / Bridge Productions | Bridge Productions | 2026-10-08 | 2026-10-11 | 2.8 | 2.99M | B1 | 1.85M–2.24M | 4:31 | quảng bá phim Telugu · te | lộ mặt; kênh hãng phim, video quảng bá phim có ngôi sao | [-v8e95Cx9Zc](https://www.youtube.com/watch?v=-v8e95Cx9Zc) |
| 16 | নানির বাড়ির মজার ভ্রমণ 🚂🎡 / Amazing Village Adventure / Bangla Cartoon Story | মজার বাংলা | 2026-09-08 | 2026-09-19 | 11.2 | 2.91M | B1 | 1.22M–1.72M | 9:14 | hoạt hình thiếu nhi rau củ · bn | — | [_dc9OmLUzuU](https://www.youtube.com/watch?v=_dc9OmLUzuU) |
| 17 | बर्थडे के बाद गांव पहुंचे  😱 / Hindi Cartoon Story | Sabzi ki Story ai | 2026-09-03 | 2026-09-21 | 17.7 | 2.11M | B2 | 0.90M–1.27M | 9:44 | hoạt hình thiếu nhi rau củ · hi | — | [2ZJhVKnIKmk](https://www.youtube.com/watch?v=2ZJhVKnIKmk) |
| 18 | Aalu Ko Kabadiwale Se Mila Purana Truck… Croreon Ki Company Ka Pehla Kadam! 🚛🥔 / आलू की नई शुरुआत! | Sabzi Nagar World | 2026-08-22 | 2026-09-16 | 24.5 | 2.02M | B2 | 0.81M–1.17M | 17:16 | truyện hoạt hình rau củ (nghèo → giàu) · hi | — | [lgz9pbKbOTQ](https://www.youtube.com/watch?v=lgz9pbKbOTQ) |
| 19 | Kalijai - ଜାଇର କରୁଣ କାହାଣୀ / Maa Kalijai Story / Maa Kalijai Temple Chilika | KALINGA VAIBHAVAM | 2026-10-08 | 2026-10-09 | 0.8 | 1.41M | B2 | 0.83M–1.02M | 14:23 | thần thoại / đền chùa Odisha · or | — | [cIjNzXlWZzg](https://www.youtube.com/watch?v=cIjNzXlWZzg) |

**Theo lớp:** A 3 (#1, #9, #10) · B1 11 · B2 5. **Tiếng Anh:** #1–#8. **Tài chính cá nhân:** không có. **Không lộ mặt:** tất cả trừ #3, #8, #10, #15.

Kênh nhiều video đạt: Sabzi ki Story ai có 3 video (#13, #14, #17). Nếu tính một video cho mỗi kênh thì còn **17 kênh**.

## 3. Bị loại (≥ 1M, kênh ≤ 31 ngày, dài ≥ 3 phút)

| Kênh | Video | Lượt xem | Tuổi kênh | Lý do |
|---|---|---|---|---|
| Rural Travel TV | [59S5LE28cLo](https://www.youtube.com/watch?v=59S5LE28cLo) | 1.22M | 16.2 | ước ngày 7: 0.81M–0.95M |
| きれいなゴミ箱 | [5J90D5NTDhA](https://www.youtube.com/watch?v=5J90D5NTDhA) | 1.49M | 21 | ước ngày 7: 0.73M–0.97M |
| Kishan Chavda History | [9-wrTgva9xk](https://www.youtube.com/watch?v=9-wrTgva9xk) | 1.50M | 0.2 | ước ngày 7: 0.56M–0.83M |
| Sabji By Yash | [DKB8oMQHbH8](https://www.youtube.com/watch?v=DKB8oMQHbH8) | 1.16M | 10.6 | tiêu đề trùng gần nguyên văn video của Sabzi Nagar World đăng 4 ngày trước → nghi đăng lại |
| cartoonkudo | [Dbyu2Eizw5U](https://www.youtube.com/watch?v=Dbyu2Eizw5U) | 1.14M | 21.1 | 4 video đầu là Shorts mèo/dê tiếng Anh, rồi đổi sang truyện Hindi → đổi chủ đề |
| México Innovador | [S4Sbl7K9Up4](https://www.youtube.com/watch?v=S4Sbl7K9Up4) | 2.29M | 23.1 | tên + mô tả kênh tiếng Tây Ban Nha về Mexico, nội dung tiếng Anh về Elon Musk; video đầu tiên 23 ngày sau ngày tạo → dấu hiệu kênh tái dụng |
| SSundeePlus | [VMPYMYuGxms](https://www.youtube.com/watch?v=VMPYMYuGxms) | 1.45M | 6.2 | ước ngày 7: 0.65M–0.90M |
| Business by baniya | [b2ClWB7bPLY](https://www.youtube.com/watch?v=b2ClWB7bPLY) | 1.17M | 30 | sau video hit chuyển hẳn sang livestream pegboard/bảng từ → đổi chủ đề đột ngột, nghi bán/tái dụng |
| History Tab Open | [ihGK1iyUN1E](https://www.youtube.com/watch?v=ihGK1iyUN1E) | 1.14M | 8.2 | ước ngày 7: 0.53M–0.72M |
| Munna Toon World | [tHIbsYo_Uyw](https://www.youtube.com/watch?v=tHIbsYo_Uyw) | 5.38M | 29 | 4 video đầu là Shorts "#montagem #mhacommunity", rồi đổi sang truyện rau củ Hindi → đổi chủ đề |
| Dr. Ants | [wStCAWCJKv8](https://www.youtube.com/watch?v=wStCAWCJKv8) | 1.34M | 14 | ước ngày 7: 0.82M–1.00M |

## 4. Danh sách phụ: Short (< 3 phút) ≥ 1M trên kênh ≤ 31 ngày

Phần này chỉ để tham khảo; Shorts không tính vào mục tiêu. Đặc điểm: thú cưng, em bé AI, meme, "how X works" 60–75 giây. Hai kênh "Things Opened" và "You Built It" là **giải thích vật thể bằng hình 3D**, cùng họ với #6 CityEons.

| Tiêu đề (cắt 60 ký tự) | Kênh | Đăng | Tuổi kênh | Lượt xem | Dài | Liên kết |
|---|---|---|---|---|---|---|
| JACK CLOGGED THE TOILET at Daycare! 🚽💩😱 Iggy FREAKS OUT! / E | Kelli’s Korner Adventures | 2026-10-23 | 28.6 | 40.47M | 31 s | [ajjH9jQGDJU](https://www.youtube.com/watch?v=ajjH9jQGDJU) |
| Hero Dog Saves Baby from Falling Ceiling Fan! 😱🐶 | Max & Leo | 2026-10-26 | 9.2 | 35.74M | 17 s | [KdZBPQEKucg](https://www.youtube.com/watch?v=KdZBPQEKucg) |
| Bro said "eat faster"💀 #funnyshorts #memes | zard | 2026-10-21 | 9.1 | 29.67M | 24 s | [N_SLOJ5PI6U](https://www.youtube.com/watch?v=N_SLOJ5PI6U) |
| Get yours with the link in the bio 🔗🐶If your pup always want | Snugosaur | 2026-10-20 | 4.9 | 19.46M | 14 s | [T5optJIqEro](https://www.youtube.com/watch?v=T5optJIqEro) |
| Korean Self-Serve Ramen store 🤤🤤 | Sorm Koemse03 | 2026-10-24 | 28.4 | 17.40M | 157 s | [pU48Zknxi_0](https://www.youtube.com/watch?v=pU48Zknxi_0) |
| What Should I Name This Ferret? | Paws & Talons Trail | 2026-10-15 | 0.4 | 15.53M | 60 s | [TGeInjWcUM8](https://www.youtube.com/watch?v=TGeInjWcUM8) |
| Piano-Black Luxury Suitcase Transforms Into Cyber Super-Spor | ASA Hacks | 2026-10-27 | 16.8 | 14.33M | 31 s | [U0efP8smHbU](https://www.youtube.com/watch?v=U0efP8smHbU) |
| Comment “Horse” if you need this😍🐴#equestrian #gallop #horse | LumaRein | 2026-10-22 | 5.7 | 13.22M | 15 s | [4DREt0WWLkQ](https://www.youtube.com/watch?v=4DREt0WWLkQ) |
| HEY DADDY, GIVE ME THE PHONE!” 😂📱👶 This Baby Has DEMANDS! #S | Tiny BabyLogic Al | 2026-10-22 | 23.2 | 13.00M | 16 s | [C6PizTSttRg](https://www.youtube.com/watch?v=C6PizTSttRg) |
| How a USB-C Cable Really Works 🔌 #shorts | Things Opened | 2026-10-21 | 5.7 | 6.79M | 73 s | [1Ug_sjO1zrA](https://www.youtube.com/watch?v=1Ug_sjO1zrA) |
| How a Strip of Dirt Becomes a Road | You Built It | 2026-10-15 | 3.6 | 5.23M | 67 s | [KYo7Vj6dT-8](https://www.youtube.com/watch?v=KYo7Vj6dT-8) |
| He Paid $20 to Fix His Corvette… It Got EVEN WORSE 💀😭 / Cuh  | Cuh vs Bro | 2026-10-25 | 0.8 | 1.42M | 74 s | [mE14sET4ONM](https://www.youtube.com/watch?v=mE14sET4ONM) |

## 5. Mẫu chung (phân tích, không sao chép)

### 5a. Ngách
- **Tiếng Anh (8):**
  - giải thích một sự vật hoặc sự kiện cụ thể: lũ Nepal, lều tuyết Inuit, New York 400 năm (3 video);
  - mẹo công nghệ "Turn This OFF" về quyền riêng tư (2, cùng một người);
  - kể chuyện hoài cổ về người nổi tiếng Mỹ (1, khán giả lớn tuổi);
  - hoạt hình thiếu nhi (2, một dùng nhân vật có IP, một nghi quảng cáo trả tiền).
- **Ngoài tiếng Anh (11):** áp đảo bởi **hoạt hình AI rau củ hoặc truyện đạo đức** Hindi và Bengal (7). Mô-típ lặp: nghèo → giàu, về quê thăm ông bà, lũ hoặc bão trên tàu. Có ≥ 5 kênh làm cùng một khuôn, thậm chí trùng tiêu đề, nên đây là **ngách bão hoà, chép nhau**.
- **Không có tài chính cá nhân và không có true crime** dù đã có truy vấn riêng. Tài chính trên YouTube do kênh lâu năm chiếm hết top lượt xem. Điều này khớp với `market/CHANNELS.md` R1: kênh mới tài chính tăng chậm, không bùng nổ.

### 5b. Độ dài
- Trung vị **10:25** (cả 19), **9:47** (tiếng Anh). Dải 4:31–17:16.
- Không video nào > 18 phút. 9 truy vấn `long` không đóng góp video nào đạt; 18/19 đến từ truy vấn medium, 1 từ mostPopular (category 28). Với kênh mới, **8–13 phút** là vùng an toàn.

### 5c. Định dạng
- **Không lộ mặt:** 15/19.
- **Hình AI:** ít nhất 11 video dùng hình hoặc hoạt hình AI tạo sinh (rau củ, truyện đạo đức, Drollery, ZENO, KrishoPlays).
- **3D hoặc sơ đồ có chủ đích:** UnderTheHeadline (bản đồ địa hình 3D), CityEons (dựng 3D, ghi rõ **"No AI imagery"** trong tiêu đề và dùng nó làm điểm bán), ZENO (mặt cắt nhiệt độ).
- **Phim tài liệu hoặc kể chuyện:** Drollery (clip lưu trữ + kể).
- **Lộ mặt:** chỉ Spencer (người thật chỉ tay vào màn hình).

### 5d. Tiêu đề (8 video tiếng Anh)
- Số ký tự: trung vị **65** (45–83).
- Có số: 4/8 ("2026", "-50°C", "400 Years").
- Câu hỏi: 2/8 ("What Caused…?", "How Did…?").
- Viết HOA nhấn từ khoá: 5/8 (NEW YORK, ANCIENT INUIT, NO Electricity, OFF, WAR).
- Ngoặc đơn nói rõ lợi ích hoặc nỗi sợ: 3/8 ("(your phone is listening)", "(No AI imagery)", "(Google AI scans your email)").
- Khuôn lặp lại được:
  - "**[Đối tượng] Users: Turn This OFF Immediately! ([lý do])**";
  - "**How Did [nhóm người] [làm việc khó] With NO [công nghệ]?**";
  - "**Watch [nơi] Grow for [N] Years**";
  - "**[Sự kiện] Explained: What Caused …?**".
- Mỗi kênh tự lặp khuôn của mình: video sau gần như cùng cú pháp.

### 5e. Ảnh bìa (mô tả bằng lời; xem ở scratchpad, không tải vào repo)
- **#4 Nepal:** khối địa hình 3D, vòng đỏ + mũi tên đỏ chỉ điểm vỡ, chữ trắng to "HOW DID THIS HAPPEN?" bên trái nền đen.
- **#7 ZENO:** mặt cắt lều tuyết, mũi tên luồng khí cam/xanh, hai nhãn số "-50°C" / "+16°C". Không có người.
- **#6 CityEons:** ảnh vệ tinh Manhattan sơ khai, "1600 → 2026" trên cùng, "NEW YORK" chữ giãn cách + cờ Mỹ.
- **#3, #8 Spencer:** mặt người + giao diện thật (Gmail, iPhone), chữ đỏ "TURN OFF!" + mũi tên.
- **Hoạt hình AI:** cảnh đông nhân vật, màu bão hoà, ít chữ (chữ chỉ có ở bản Bengal).
- **Mẫu chung:** **một ý nhìn được trong 1 giây**, ≤ 4 chữ hoặc chỉ một cặp số, mũi tên hoặc vòng đỏ dẫn mắt. Khớp với quy tắc chữ ảnh của `packaging/R1.md` (≤ 4 chữ + 1 số).

### 5f. Tần suất và vị trí video hit
- Video hit là **video thứ 1–4 của kênh** ở 13/19 (trung vị thứ 3). Tuổi kênh lúc đăng trung vị **15 ngày**.
- Nhịp đăng trung vị ~3 video/tuần. Riêng UnderTheHeadline đăng dồn 17 video/tuần quanh một sự kiện.
- **Sau hit thường hụt:** video kế tiếp của nhiều kênh chỉ còn 1–5 % lượt xem của hit (ZENO, History Tab Open, Spencer Knows!, Shiva Rudra; tỉ số hit/trung vị video dài khác: 82–1.115 lần). Chỉ CityEons (×2), KrishoPlays (×4), DipRaj (×6), KALINGA (×2) giữ được mức. Đây là các kênh có **khuôn series ổn định**.

### 5g. Shorts kéo sang?
- 13/19 video (11/17 kênh) thuộc kênh **không có Short nào**. Ở 6 kênh còn lại, tổng lượt xem Shorts < 5 % video hit, trừ Coov Records: trailer 100–120 s đạt 0,83M, đăng 2 ngày trước tập 1. Đó là kéo bằng trailer, không phải Shorts thuần.
- **Không thấy dấu hiệu Shorts nuôi video dài** ở kênh mới. Nguồn lớn nhiều khả năng là đề xuất (Browse/Suggested); API không cho xem nguồn traffic, nên đây là suy luận.

## 6. Bước 4: ảnh chụp hằng ngày (CHỜ CHỦ DỰ ÁN)

Lớp A = 3 < 10. Ảnh chụp ngày đầu `snap-20261029.json`: 5 video 0–3 ngày ≥ 100k trên kênh ≤ 31 ngày. Hai video dài:
- [Ab0chKJs5wg](https://www.youtube.com/watch?v=Ab0chKJs5wg): truyện AI "billionaire…" 18:28, 0,16M;
- [eS_1-ZF--b8](https://www.youtube.com/watch?v=eS_1-ZF--b8): 18:13, 0,17M.

Cả hai thuộc ngách **truyện tỉ phú cải trang**, kề chủ đề tiền.

**Đề xuất lịch:** mỗi ngày 1 lần trong ≤ 14 ngày (dừng sớm khi đủ 20 video lớp A).
- Mỗi lượt: 1 cửa sổ 3 ngày × 9 truy vấn = 900 đơn vị + mostPopular và tra cứu ~80 đơn vị, tức **≈ 1.000 đơn vị/ngày**. Còn đủ chỗ cho việc khác trong ngân sách 9.000.
- Lợi ích phụ: đo α thật cho đường cong ở mục 1.
- Cách chạy: `toolkit/market/r3/collect.py`, `filter.py`, `uploads.py`, mỗi ngày ghi `market/r3/snap-YYYYMMDD.json`.
- **Chưa lên lịch.** Chủ dự án duyệt thì đặt scheduled task.

## 7. Áp dụng cho Money Rerouted (khán giả lõi CHARTER §1: người Mỹ 25–40, thuê/sắp mua nhà, mới đầu tư)

| Mẫu | Áp được? | Ưu | Nhược | Tác động (5 tiêu chí CHARTER §2.4) | Rủi ro |
|---|---|---|---|---|---|
| **Một vật thể hoặc sơ đồ mặt cắt nhìn được trong 1 giây** trên ảnh bìa và mở đầu (ZENO, UnderTheHeadline, CityEons) | **Có**, khớp thế giới 3D low-poly và "hình mang nghĩa" | dùng lại vật thể sẵn có của tập; R1 đã có quy tắc ≤ 4 chữ + 1 số | cần vật thể đủ mạnh cho mỗi đề tài | chất lượng ↑ (đường mắt), công ≈ 0 thêm (đã ở cổng D-015) | ẩn dụ vật thể sai nghĩa với số liệu → kiểm claim-risk như R1 |
| **Khuôn tiêu đề "How/What … ?" kèm một con số cụ thể**, 55–68 ký tự | **Có**, tiêu đề tập vốn trả lời một quyết định | tăng tò mò mà không giật gân | dễ trượt sang "clickbait" | tốc độ =, chất lượng = nếu số đúng | số trên tiêu đề phải có nguồn; gen "không dự báo" |
| **Ngoặc đơn nêu lợi ích hoặc nỗi sợ** "(…)" | **Có điều kiện** | rõ lợi ích cho người 25–40 | khuôn "Turn This OFF Immediately!" là giọng cảnh báo, trái gen "không khuyên" | — | mệnh lệnh = khuyên → **không dùng dạng mệnh lệnh**, chỉ dùng dạng mô tả |
| **Độ dài 8–13 phút** | **Có**, đã đúng (`lab` 9–11, `101` 8–9) | xác nhận định dạng hiện tại | `deep` 14–17 nằm ngoài vùng hit của kênh mới | không đổi | — |
| **Khuôn series cố định, tiêu đề cùng cú pháp** (CityEons, KrishoPlays giữ mức; kênh không khuôn thì hụt sau hit) | **Có** | người xem nhận ra series; thuật toán có chuỗi đề xuất | đơn điệu nếu lặp quá | tốc độ ↑ (ít quyết định đóng gói), mở rộng ↑ | khuôn phải phục vụ câu hỏi, không ép đề tài |
| **Giải thích bám sự kiện nóng, đăng dồn** (UnderTheHeadline: 17 video/tuần quanh lũ Nepal) | **Một phần**: tin chính sách hoặc thuế (ví dụ luật thuế mới) | đỉnh tìm kiếm ngắn mà lớn | phá nhịp tập và cổng chất lượng | tốc độ ↓↓, chất lượng có thể ↓ | mâu thuẫn CHARTER §2.4 chất lượng là ràng buộc → chỉ dùng khi một tập đã sẵn dữ liệu |
| **Hoạt hình AI tạo sinh đông nhân vật** (ngách rau củ, truyện đạo đức) | **Không** | rẻ, nhanh | trái gen 3D tối giản, nhân vật không mặt; ngách bão hoà, chép nhau | chất lượng ↓ | chính sách "nội dung lặp lại / tạo hàng loạt" của YPP |
| **Truyện kể "billionaire cải trang"** (snap 0–3 ngày) | **Không** | kề chủ đề tiền | hư cấu, trái định vị "dữ liệu thật" | — | nhãn ILLUSTRATIVE không cứu được thể loại hư cấu |
| **Lộ mặt chỉ tay vào giao diện** (Spencer) | **Không**, CHARTER §1 không lộ mặt | — | — | — | — |
| **"No AI imagery" làm điểm bán** (CityEons) | **Nên cân nhắc**: Crux dựng 3D bằng mã, không AI tạo sinh | phân biệt với làn sóng AI slop | phải đúng tuyệt đối | chất lượng = | tuyên bố sai → mất tin; cần kiểm khi có footage ngoài |
| **Trailer hoặc Short đăng trước tập 1–2 ngày** (Coov) | **Có thể thử** với Short hiện có (D-013 đã có 1 Short/tập) | không tốn thêm công: chỉ đổi thứ tự đăng | Shorts ở kênh mới gần như không kéo sang video dài (mục 5g) | tốc độ = | đo bằng Studio trước khi coi là luật |

**Điều không áp được, và vì sao:**
- Không có bằng chứng kênh **tài chính cá nhân** mới nào đạt 1M trong 7 ngày suốt 63 ngày quét, nên kỳ vọng "bùng nổ" cho Money Rerouted không có cơ sở từ mẫu này.
- Mẫu bùng nổ thật nằm ở **giải thích vật thể hoặc lịch sử hoặc sự kiện** và **hoạt hình thiếu nhi**.
- Con đường áp được là mượn **cách đóng gói** (vật thể 1 giây, câu hỏi kèm số, khuôn series). Không mượn ngách.

**Đề xuất (chờ chủ dự án):**
1. Duyệt hay không lịch chụp hằng ngày ≤ 14 ngày (mục 6).
2. Thử một tập mà tiêu đề và ảnh bìa dùng khuôn "How/What … ?" kèm số + vật thể mặt cắt, so với tập đối chứng. Việc này đã nằm trong cổng đóng gói D-015, không thêm cổng.
3. Hạn 28/11/2026: chạy lại để làm mới, hoặc xoá `market/r3/*.json` và các bảng số trong file này.
