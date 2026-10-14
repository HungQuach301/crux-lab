# Chính sách YouTube hiện hành + chi phí lồng tiếng — rnd-hybrid (tra 14/10/2026)

**Giới hạn đọc nguồn:** `support.google.com` và `blog.youtube` bị chặn từ container (curl 000, WebFetch ENOTFOUND). Các câu của YouTube dưới đây
lấy **qua kết quả tìm kiếm web** (đoạn trích của chính trang trợ giúp khi có, nếu không thì báo chí), **chưa đọc trực tiếp trang**: chủ dự án mở
lại link trước khi dùng làm căn cứ. Trang ElevenLabs đọc trực tiếp (curl 200), có SHA-256.

## 1. Nhãn nội dung tổng hợp ("altered or synthetic content")
- **Nguồn:** YouTube Help *Disclosing use of altered or synthetic content* https://support.google.com/youtube/answer/14328491 ; YouTube Blog
  (03/2024) https://blog.youtube/news-and-events/disclosing-ai-generated-content
- **Phải khai** (trong YouTube Studio, mục "Altered content" lúc tải lên) khi nội dung **thực tế** mà người xem có thể nhầm là người, nơi, cảnh hay sự kiện
  có thật, làm bằng phương tiện biến đổi/tổng hợp kể cả AI sinh. Ví dụ phải khai: thay/tạo hình dạng hoặc **giọng tổng hợp của một người thật**, sửa
  cảnh quay địa điểm thật, dựng sự kiện lớn hư cấu trông như thật.
- **Không phải khai:** nội dung rõ ràng không thực tế, **hoạt hình**, hiệu ứng thấy rõ, AI chỉ dùng hỗ trợ sản xuất (kịch bản, ý tưởng, phụ đề…).
- Nhãn hiện trong mô tả mở rộng; với chủ đề nhạy cảm (bầu cử, xung đột, thảm hoạ, **tài chính**, y tế) có thể hiện **trên trình phát**. YouTube có thể tự
  gắn nhãn khi tiêu đề/mô tả nhắc tới nội dung tổng hợp.
- **Áp vào Crux (suy luận, không phải lời YouTube):** nhân vật cắt giấy = hoạt hình, rõ không thực tế → không thuộc diện khai. Giọng Eric
  (ElevenLabs premade) **không** giả một người thật có danh tính → theo đoạn trích, không thuộc ví dụ phải khai; nhưng vì kênh là tài chính (chủ đề
  nhạy cảm), khuyến nghị **tự nguyện bật "Altered content" = Không** và ghi trong mô tả "Narration: synthetic voice (ElevenLabs)". Ảnh tư liệu chỉ phủ
  tông + Ken Burns, không sửa nội dung → không phải khai, nhưng phải giữ năm + nguồn trên hình (RIGHTS §F4). Cấm tuyệt đối: dùng AI tô màu/"phục
  chế" ảnh tư liệu rồi trình như ảnh gốc (vừa là F2 "ảnh tạo bằng AI trình như tư liệu", vừa thuộc diện phải khai).

## 2. Kiếm tiền: nội dung "không xác thực" (sản xuất hàng loạt / lặp lại) và "tái sử dụng"
- **Nguồn:** YouTube channel monetization policies https://support.google.com/youtube/answer/1311392 (đoạn trích qua tìm kiếm); làm rõ của YouTube
  07/2025 qua PPC Land https://ppc.land/youtube-clarifies-inauthentic-content-policy-changes/ , Search Engine Journal
  https://www.searchenginejournal.com/youtube-clarifies-monetization-update-targeting-spam-not-reaction-channels/550755/
- **Từ 15/07/2025** mục "repetitious content" đổi tên thành **"inauthentic content"**: *nội dung sản xuất hàng loạt hoặc lặp lại* — trông như làm từ
  **khuôn mẫu, ít hoặc không biến đổi giữa các video**, hoặc **dễ nhân bản ở quy mô lớn**. YouTube nói đây là "minor update", loại này "has always been
  ineligible". Áp cho **cả kênh**: vi phạm có thể mất kiếm tiền toàn kênh. Ví dụ YouTube nêu khi làm rõ: kênh đăng nhiều truyện kể chỉ khác bề
  mặt; nhiều slideshow cùng một lời kể.
- **Reused content** (bình luận, clip, tổng hợp, phản ứng) là mục riêng, không đổi: được kiếm tiền khi thêm giá trị gốc đáng kể.
- **Rủi ro với hướng "hình lai" (đánh giá của phiên):** chính khuôn mẫu làm nhà máy rẻ (nhân vật cắt giấy + sticker + ảnh Ken Burns) là thứ chính
  sách soi. Giảm rủi ro bằng: mỗi tập một câu hỏi/mô phỏng riêng trên dữ liệu thật (định vị *phòng thí nghiệm*), lời viết riêng, cảnh dữ liệu dựng
  từ mô hình của tập, không tái dùng nguyên chuỗi cảnh; nhân vật lặp lại được (như kênh hoạt hình) nhưng hành động/biểu cảm theo truyện. Ảnh tư
  liệu không được chiếm vai trò "slideshow" (giữ trần ≤ 20 %, §F3).

## 3. Lồng tiếng nhiều thứ tiếng
### 3a. Tự lồng tiếng của YouTube (auto dubbing)
- **Nguồn:** YouTube Help *Use automatic dubbing* https://support.google.com/youtube/answer/15569972 (đoạn trích qua tìm kiếm); YouTube Blog
  https://blog.youtube/news-and-events/youtube-auto-dubbing-expressive-speech/ ; Thurrott https://www.thurrott.com/music-videos/332404/youtubes-auto-dubbing-now-supports-27-languages
- Bật mặc định cho kênh đủ điều kiện (không thì bật qua early access ở Advanced settings); tạo **track âm thanh dịch**, video ghi "auto-dubbed" trong
  mô tả, người xem chọn track. Không đủ điều kiện: > 120 phút, ít lời/chỉ nhạc, ngôn ngữ nguồn không hỗ trợ, nói quá nhanh, có khiếu nại bản quyền.
  Có thể để "Publish manually" để duyệt từng bản trước khi đăng; YouTube cảnh báo chất lượng không đều giữa các thứ tiếng.
- Theo báo chí 02/2026: mở cho **mọi nhà sáng tạo** (04/02/2026), **27 thứ tiếng**; *Expressive Speech* (giữ cảm xúc) ở 8 thứ tiếng (EN, FR, DE, HI, ID,
  IT, PT, ES); khớp môi là thử nghiệm giới hạn. **Chi phí: 0 $.** Không sửa được kịch bản dịch theo câu; **chữ trên hình vẫn là tiếng Anh**.
### 3b. ElevenLabs Dubbing (đọc trực tiếp 14/10/2026)
- https://elevenlabs.io/pricing (SHA-256 trang `1d802ae2…a59de6eb`): *"Dubbing 2,000 credits per minute (automatic with watermark), 3,000 (automatic
  without watermark), 5,000 (Dubbing Studio with watermark) or 10,000 (Dubbing Studio without watermark)"*; *"Text to Speech 1 credit per character"*.
- https://elevenlabs.io/docs/overview/capabilities/dubbing (SHA-256 `e33b0be2…0c98bae4`): Dubbing v2 alpha, 90+ thứ tiếng, "Dubbing Studio is in
  maintenance mode", "For Dubbing v2, transcript editing and audio regeneration via the API are available on Enterprise plans only", "Dubbing v2 (priced
  per minute in US dollars on Automatic Dubbing)".
- **Chi cho một tập `lab` 10 phút** (gói Creator hiện có: hạn mức 144.034 ký tự/tháng gồm cộng dồn, đã dùng 98.507 — `/v1/user/subscription` 14/10):
  | Cách | Credit / thứ tiếng | Ghi chú |
  |---|---|---|
  | Auto dubbing YouTube | 0 | không sửa được, chữ trên hình tiếng Anh |
  | ElevenLabs automatic, không watermark | 30.000 | ≈ 2/3 hạn mức còn lại của tháng cho **một** thứ tiếng |
  | **Dịch kịch bản + TTS lại bằng nhà máy** (đề xuất) | ≈ 9.000–10.000 (≈ 1 credit/ký tự, kịch bản 10 phút ≈ 9 k ký tự) | rẻ ≈ 3 lần; giữ mốc từ (with-timestamps) nên cảnh/sticker vẫn khớp lời; **chữ trên hình dịch được vì mọi chữ là mã** — lợi thế riêng của hình dựng bằng code + cắt giấy |
- **Khuyến nghị:** thử auto dubbing YouTube (0 $) cho tiếng Tây Ban Nha trên 1 tập cũ để đo nhu cầu; chỉ khi một thứ tiếng có khán giả mới làm bản
  bản địa đầy đủ bằng nhà máy (TTS + chữ trên hình dịch, ≈ 10 k credit/tập). Chưa đề xuất ElevenLabs Dubbing.
