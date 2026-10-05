# Sổ tay chạy một tập (playbook v3, Mốc B, 05/10/2026)

Áp từ Tập 4 (`decisions/D-006.md`). Khung: `playbook/quality-framework.md`. Biên kịch: `playbook/story.md`. Prompt mẫu: `playbook/prompts/`. Một tập chạy bằng một dòng: **"Chạy Tập N, phiên P1"** (hoặc "…, đề tài #k, phiên P1"), rồi "… P3" (và "… P2" chỉ khi G1 ghi "cần C3").

## 0. Mở phiên
`bash toolkit/verify.sh <nhánh-lệnh-ghi>`: kiểm công cụ, nhánh đúng lệnh (không tự đặt nhánh), `main` mới nhất. Trượt thì báo, không làm tiếp.

## 1. Ba cổng, hai hoặc ba phiên

| Phiên | Việc | Kết thúc ở | Chủ dự án |
|---|---|---|---|
| **P1** | Việc 0 (dữ liệu, mô hình, kiểm độc lập) → C1 máy (≤ 3 đề tài + logline, kiểm mù kể lại) → C2 (kịch bản, móc, kiểm máy + kiểm mù lời) → giao phiên K → **G1** | G1 trả lời | **G1** (1 lần) |
| **P2** *(chỉ khi G1 ghi "cần C3")* | C3 ký hiệu mới (≤ 2 ký hiệu/tập; cổng gốc) | C3 trả lời | C3 (ngoại lệ) |
| **P3** | C4 animatic (TỰ ĐỘNG) → C5 render + L1 (TỰ ĐỘNG) → **G2** → giao hàng → **G3** | Chủ dự án đăng; merge `main` | **G2**, **G3** |

- **G1 sau C2** (D-006 Q2), một gói ≤ 3 câu:
  1. đề tài + logline;
  2. kịch bản: cấu trúc, cold open và móc đã chọn **dạng chữ**, kèm 2 phương án móc còn lại, mỗi phương án một dòng;
  3. tiêu đề nháp + có cần C3 không.
- **Duyệt theo lô:** một G1 được duyệt 3–4 đề tài + logline cho cả mùa (`topics/season.md`). Tập sau lấy đề tài kế tiếp trong danh sách; G1 của tập đó chỉ còn câu 2–3.
- **Chưa có danh sách mùa:** P1 viết C2 cho đề tài được khuyến nghị; G1 hiện hai ứng viên kia, mỗi ứng viên một dòng. Đánh đổi: chủ dự án đổi đề tài → C2 viết lại (≈ 1 lượt WRITER + 6 người đọc). Máy không tự chọn đề tài (D-004).
- **Giọng, nhạc, hướng hình** dùng mặc định đã chốt (Eric `eleven_v3`, style C G-016, thư viện hình). Muốn đổi thì chủ dự án nêu ở G1.
- **Nguyên tắc tốc độ:** chỉ mở vòng sửa khi lỗi CHẶN, hoặc sai nghĩa / claim / pháp lý. Lỗi CHÍNH không đổi nghĩa → **hàng chờ** trong gói G2. **Ngoại lệ phải hỏi:**
  - vượt trần token > 25 % (§8);
  - đổi kịch bản đã duyệt;
  - số không xác minh được nguồn;
  - rủi ro pháp lý/bản quyền;
  - cần ký hiệu mới.
- Mỗi tập một nhánh `epNNN` từ `main`. Chỉ P3 merge (fetch trước; trong file dùng chung chỉ sửa phần của tập).
- **Bàn giao qua `episodes/epNNN/PLAN.md`**, đủ năm mục:
  1. bảng cổng;
  2. "Phiên sau đọc" (≤ ~8 file);
  3. việc treo;
  4. điểm dừng an toàn + lệnh chạy tiếp;
  5. KPI + token so trần.
  Phiên sau chỉ đọc hiến chương, `quality-framework.md`, file này, PLAN, ledger và các file được nêu tên.
- Trước mỗi gói cổng và mỗi issue TỰ ĐỘNG: **REVIEWER** soát (`quality-framework.md` §7).

## 2. Model, effort, số agent

| Việc | Model | Effort |
|---|---|---|
| Điều phối, WRITER, REVIEWER, tổng kết | Opus | Medium |
| Người đọc kiểm mù, người chấm, so cặp | Sonnet | mặc định |
| Render, checks, mã hoá, sinh giọng | lệnh trực tiếp (không agent) | — |

Mỗi agent con tốn **≈ 44 nghìn token cố định** (đo ở Mốc B). Ý đồ mỗi cổng ghi trước số agent dự kiến. Dùng lệnh trực tiếp thay agent khi không cần độc lập.

## 3. Đầu bài WRITER (C2)

WRITER **đọc `playbook/story.md` trước tiên**, rồi theo các luật sau:
1. **Từ khó ASR:**
   - không dải năm có gạch nối; không "minus", không số âm đọc lên; không ký hiệu ở chỗ phải đọc;
   - số tiền đọc rõ;
   - viết tắt có gạch nối ("T-bill") → dạng đầy đủ ở câu mang từ khoá (lessons E6, F7).
2. **Claim-risk áp cho câu NÊU số;** câu nhắc lại gọi bằng lời. Mỗi tỉ lệ một dạng cố định (E5). **Ràng buộc claim-risk đặt sau móc** (story §1.3).
3. Câu đối trọng sau mỗi kết luận; không mệnh lệnh (E4).
4. Mật độ số và khoảng thở theo story §3; khuôn tỉ lệ thời lượng theo `format` (story §4, Tham khảo).
5. Đoạn phương pháp = 1 câu + thẻ V7 + mô tả.
6. **Bảng nhịp** có cột loại nhịp (1 "hình tự mang ý" + câu "ý người xem phải đọc ra" / 2 "minh hoạ lời"). Hình lấy từ thư viện; ký hiệu mới phải ghi lý do.
7. Gen được bảo vệ và gu đã chốt (CHARTER §4, `taste-ledger.md`). Không chép kịch bản tập cũ.

**Móc do máy chọn (D-006 Q4):**
- WRITER viết **3 phương án 30 s đầu**, mỗi phương án một kiểu móc khác nhau (`packaging.md` §2). Cả ba đều theo story §1: 5 s đầu là được–mất hoặc câu hỏi trên sự thật hiện tại; lời hứa trước 0:30.
- **Tới khi có hiệu chuẩn chính thức:** chọn bằng WRITER + REVIEWER (REVIEWER chấm theo story §1, ghi lý do một dòng).
- **Ứng viên bộ đo: so cặp móc** (hiệu chuẩn Mốc B: chọn đúng bản gốc 6/6; điểm 1–5 và điểm bỏ xem KHÔNG ĐẠT, lessons F3). Chỉ dùng sau **hiệu chuẩn chính thức ở P1 Tập 4**:
  - ý đồ + ngưỡng ghi trước (ví dụ: so cặp chọn bản gốc ≥ 5/6 trên hai tập, bản làm kém = bỏ móc 5 s, cùng kịch bản);
  - đạt → so cặp vòng tròn 3 phương án, 3 người đọc mỗi cặp, chọn phương án thắng nhiều nhất;
  - trượt → giữ cách WRITER + REVIEWER.
- G1 hiện móc đã chọn dạng chữ trong kịch bản + 2 phương án còn lại, mỗi phương án một dòng. Chủ dự án chỉ đổi khi muốn. **Không sinh giọng cho phương án không chọn.**

## 4. Song song sau C2
- Phiên K (§7).
- Phối nhạc style C, đo độ lặp T2 (Tham khảo).
- Lời theo cảnh: tên take theo hash chữ; kiểm từ khoá ASR ngay khi sinh; chỉ sinh lại cảnh đổi chữ.

## 5. Gói phát hành và Shorts (G2)
- **Tiêu đề:** nháp ở G1 (so cặp một vòng, Tham khảo).
- **Thumbnail:** ở G2 chỉ đưa 3 thumbnail đã qua claim-risk, so cặp một vòng; chủ dự án chọn mặc định + bộ Test & Compare.
- **Shorts 2–3 cái 9:16 mỗi tập**, cắt từ nhịp then chốt đã qua checks:
  - ≤ 60 s;
  - chữ ≥ sàn dọc 56 px ở 1080×1920;
  - vùng an toàn dọc (trên 200 px, dưới 320 px);
  - ILLUSTRATIVE và "history, not a forecast" trên mọi khung có số.
  Dựng bằng thư viện mẫu khi phiên nhà máy xong (`moc-b/PLAN-FACTORY.md`). Trước đó cắt tay từ bản cuối.
- **Hướng dẫn đăng:** `episodes/epNNN/HUONG-DAN-DANG.md` theo mẫu `playbook/templates/HUONG-DAN-DANG.md`.

## 6. Giao hàng
- Lệnh: `python3 toolkit/deliver/deliver.py episodes/epNNN/out/video.mp4 --out episodes/epNNN/work/delivery --name epNNN --branch epNNN-delivery --push`
- Mã hoá: 1080p 8 Mb/s (24–30 fps), audio copy; phần 90 MB, `SHA256SUMS`, `JOIN.md`. Không gửi qua chat.
- Chủ dự án tải xong thì xoá nhánh (proxy chặn xoá → việc treo cho chủ dự án).
- **Git LFS trên nhánh `release-epNNN`: chưa thử** (chuyển sang phiên nhà máy). Phải kiểm hạn mức LFS của tài khoản trước; vượt thì giữ cách phần 90 MB.

## 7. Phiên K và hàng chờ luật
- K chạy **một lần mỗi tập**, ngay khi claim C2 chốt. Tên `model.kind`/params do K quyết.
- Mọi đề xuất đổi luật (của bên dựng, tổng kết, REVIEWER) ghi vào **`checks-appeal.md`**. K xử lý theo lô ở lần chạy của tập kế tiếp. Chỉ mở phiên K riêng khi cần **kind mới**.
- Checks khi dựng: chỉ luật liên quan cảnh vừa sửa. Đủ bộ hai lần: cuối C4 và ở C5, trên bản sao khoá có server riêng (`episodes/ep003/design/c5/checks.sh` là mẫu).

## 8. KPI và trần token

| KPI | Tập 2 | Tập 3 | Đích Tập 4 |
|---|---|---|---|
| Chủ dự án tham gia | 11 cổng + giao hàng | 3 cổng + xác nhận tải | **2 cổng (G1, G2) + G3 đăng**; +1 nếu cần C3 |
| Vòng mỗi cổng | C2 3 · C3 ~6 · C4 3 | C2 1 · C3 2 · C4 1 · C5 2 | TỰ ĐỘNG ≤ 2; sửa chỉ khi CHẶN/sai nghĩa |
| Số agent | ≈ 300 | 141 | **≤ 60** |
| Ký tự ElevenLabs | 9.436 | 5.551 | ≤ 6.000 (gồm Shorts: dùng lại lời tập) |
| Thời gian P1 → G2 | 3 ngày | ~1,5 ngày | ≤ 1 ngày làm máy |
| Token | không đọc được | ≈ 6 triệu (ước theo 141 × 44 nghìn) | **trần 3 triệu** |

**Trần token đề xuất (Tập 4)** = agent × 44 nghìn + ngữ cảnh điều phối:
- **P1 ≤ 1,4 triệu** (≈ 25 agent + 0,3 triệu điều phối);
- **P3 ≤ 1,4 triệu** (≈ 25 agent + 0,3 triệu);
- **P2 ≤ 0,5 triệu** khi có;
- dự trữ 0,2 triệu.

Mỗi phiên ghi token thực (số harness của agent con + ngữ cảnh phiên) vào PLAN mục 5. Vượt > 25 % → dừng hỏi.

## 9. Định dạng tập (`episode.yaml` → `format`)
| `format` | Thời lượng | Cấu trúc | Mid-roll |
|---|---|---|---|
| `lab` | 9–11 phút | móc → bối cảnh/nhân vật → hành trình (phép thử) → đáp án + ngưỡng → giới hạn | 2, ở ranh giới hồi |
| `101` | 8–9 phút | khái niệm → thí nghiệm nhỏ trên dữ liệu thật → khác nhau ở 2–3 người → giới hạn | 1, ở ranh giới hồi, trong khoảng lặng |

- **Luật chung:** mid-roll không đặt trong 2 phút đầu hay 2 phút cuối, luôn ở khoảng lặng ≥ 1 s.
- **`101` không độn nội dung:** thiếu chất thì ngắn hơn hoặc gộp khái niệm. Thời lượng tối thiểu là mềm; tối đa là cứng.
- Khuôn đã thiết kế, **chưa dựng tập 101**. Kiểm khuôn tự động nằm trong `build.sh` (phiên nhà máy).

## 10. Sau phát hành
Ở mốc 7 ngày: `episodes/epNNN/audience.md` theo mẫu `playbook/templates/audience.md`. Chủ dự án gửi **một** ảnh chụp YouTube Studio cho chat chiến lược. Điểm rời lớn nhất → nhịp kịch bản tương ứng → `lessons.md` / `story.md`.

## 11. Công cụ
| Việc | Lệnh |
|---|---|
| Mở phiên | `bash toolkit/verify.sh <nhánh>` |
| Dải kiểm mù | `python3 toolkit/blind/strips.py VIDEO SPANS.json OUTDIR` |
| Chia mẫu, gói chấm, gộp điểm, dừng sớm | `python3 toolkit/blind/packets.py deal / packet / tally / next` (như v2) |
| Giao hàng | `python3 toolkit/deliver/deliver.py …` (§6) |
| Test công cụ | `python3 -m unittest discover -s toolkit/tests` |
| Dựng một lệnh | `bash toolkit/build.sh episodes/epNNN/episode.yaml` — **chưa có**, phiên nhà máy (`moc-b/PLAN-FACTORY.md`) |
