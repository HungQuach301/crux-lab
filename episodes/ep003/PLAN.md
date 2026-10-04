# PLAN — Tập 3 (playbook v2)

Nhánh: `ep003` (từ `main` `c0376d1`). Chỉ P3 merge `ep003` vào `main`. Khung: `playbook/quality-framework.md` v2; sổ tay: `playbook/episode.md`.

**Đề tài:** `topics/queue.md` #7 — "Savings Bonds That Double in 20 Years vs T-Bills" — hồ sơ `topics-r1/machine/retire-4/` (chủ dự án chỉ, 2026-10-04). Trụ: hưu trí (tập đầu của trụ). Mô hình: **kind mới** — đặc tả `retire-4/model.json → newKindNeeds` (nhãn làm việc `lock-vs-roll-replay`, tham số hoá để retire-3 dùng lại; **tên kind và params do phiên K quyết**).

## 1. Bảng cổng và quyết định

| Cổng | Trạng thái | Gói | Quyết định của chủ dự án |
|---|---|---|---|
| Hồ sơ đạt `topic-dossier.md` | XONG — `retire-4/dossier-check.md` 4/4; commit `43350f3` | — | — |
| Việc 0 | XONG — SHA trùng; kiểm độc lập 873/873 cửa sổ, 36/36 đại lượng; retire-3 11/11 qua cùng mô hình | `numbers.md` | — |
| C1 (GU) | XONG (vòng 1) | `gates/C1.md`, `gates/C1-blind.md`, issue #26 | A + A1; giả định (a) trong cold open + nhãn hình; ghim 8/2026; lãi EE 2.40% V1 "for bonds issued May–October 2026" |
| C2 (TỰ ĐỘNG) | **XONG — QUA vòng 1** (máy ĐẠT; 6/6, khuyên 0); issue #28; phân loại nhịp #27 | `gates/C2.md`, `gates/C2-blind.md` | cấu trúc + cold open bản tạm → C3 |
| Giao phiên K | **XONG — đã giao** (issue #29); khoá K chưa có | `checks-notes.md` | tên kind/params do K |

## 2. Phiên sau đọc (P2: C3, C4)
1. `episodes/ep003/story/script.md` (C2 v1 + ghi chú hình S05.5–S05.7 sửa §6.6)
2. `episodes/ep003/story/beats.md` + `story/beats-class.json` (SHA `2299ddf5…`, issue #27)
3. `episodes/ep003/story/treatment-alt.md` (phương án cấu trúc thứ hai cho câu (1) gói C3)
4. `episodes/ep003/numbers.md`
5. `episodes/ep003/gates/C1.md` (quyết định C1, luật giả định, việc treo ký hiệu mới)
6. `episodes/ep003/gates/C2.md` (tín hiệu cho C3: 3.53/3.47, giả định 1/6, mất chú ý S04/S05)
7. `toolkit/visual-library/README.md`
8. `episodes/ep003/review-c2/table-read.json` + `table-read.m4a` (lời đọc theo cảnh, take theo hash chữ)

## 3. Việc treo
- **Cho C3 (bắt buộc, lệnh chủ dự án 04/10):** cần **ít nhất một ký hiệu mới** cho ý "gấp đôi / sức mua" — không lặp hình Tập 2 (V1 lưới ô chạy lại, V3 đường lãi so vạch, dãy núi TB3MS đều đã dùng cho cùng chuỗi TB3MS ở Tập 2). Ứng viên chưa có trong thư viện: bội số tiền "×2" như một vạch đích; sức mua của gấp đôi (giỏ hàng co/giãn). C3 thiết kế mới, kiểm cổng gốc.
- **Giả định "nếu khi đó đã có bảo đảm"** cho mọi cửa sổ trước 5/2005: nói bằng lời và hiện trên hình **ngay từ đầu (cold open, trước mọi số lịch sử)** (claim `ctx_hypothetical`); WRITER và C3 nhận làm luật của tập.
- **Khoá K của tập** (issue #29): kind mới → phiên K viết bản tính lại, merge `main` **trước C4**. C3 không cần khoá K.
- **Phối nhạc (P2, cho câu (3) gói C3):** chưa làm ở P1 — engine Tập 2 `episodes/ep002/audio_src/mix.py` (style C, G-016 · chọn) cần mốc thời gian animatic/tempo map; P2 dựng clip phối ≤ 60 s trên table read + đo T2 (`toolkit/audio/d_music_selfsim.py`, tham khảo; Tập 2 19,7%).
- **Gói C3 phải liệt kê:** sửa ghi chú hình S05.5–S05.7 (§6.6: "52.3% overall" + "small sample · one era" cùng hiện với "0 of 17"); tên nhân vật Dana (ILLUSTRATIVE) là gu; đề xuất lời chỉ giữ 3.47, 3.53 lên hình (6/6 người đọc vấp).
- **P3/C6:** trước phát hành cập nhật lãi EE công bố **1/11/2026** (một claim `ctx_ee_rate`; kết quả lịch sử không đổi). Lời/hình luôn ghi "for bonds issued May–October 2026".
- Ghim dữ liệu August 2026 (chủ dự án C1); TB3MS 9/2026 = 3.94% không dùng.

## 4. Điểm dừng an toàn
- 2026-10-04 (4): **P1 XONG.** C2 qua vòng 1 (issue #28), phân loại nhịp #27, giao phiên K #29, table read 3 911 ký tự. **Dừng.** P2 bắt đầu khi PLAN ghi "P1 xong" (đã ghi): C3 không cần khoá K; C4 cần khoá K đã merge `main`. Tái lập: `python3 episodes/ep003/data/fetch.py --verify && python3 episodes/ep003/model/model.py && python3 episodes/ep003/story/check_script.py`.
- 2026-10-04 (3): C1 xong. Đang: WRITER (`story/WRITER-brief.md`). Nếu mất: giao lại WRITER cùng đầu bài → `python3 episodes/ep003/story/check_script.py` → kiểm mù C2 theo `gates/C2-intent.md`.
- 2026-10-04 17:50 (2): **gói C1 gửi (sau REVIEWER), issue [#26](https://github.com/HungQuach301/crux-lab/issues/26). DỪNG chờ chủ dự án** (3 câu). Sau khi trả lời: ghi `taste-ledger.md`, `AUTHORSHIP.md` (trên `ep003`) + ledger; giao WRITER (đầu bài `episode.md` §3 + luật tập: giả định trước 5/2005 nói bằng lời thường **trong cold open, trước mọi số lịch sử** (theo quyết định câu 2) + nhãn hình; không đặt 3.72% cạnh 3.53% mà không chú giải; mốc 17 tháng luôn kèm "mẫu ngắn" + tỉ lệ toàn kỳ) → C2.
- 2026-10-04 17:10 (1): hồ sơ + Việc 0 xong. Đang: REVIEWER soát ý đồ C1 → kiểm mù C1 (`review-c1/`, manifest T/G/titles). Nếu mất container: `python3 episodes/ep003/data/fetch.py --verify --retire3 && python3 episodes/ep003/model/model.py && python3 episodes/ep003/model/model.py --retire3`.

## 5. KPI tạm (cuối P1)
- Chủ dự án tham gia: **1** (C1) — mục tiêu Tập 3: 3 + xác nhận tải.
- Vòng: C1 **1** · C2 **1** (qua, không dự phòng).
- Lượt agent: **55** — kiểm độc lập 2 (lần đầu + mở rộng NC-1/NC-2); REVIEWER 4 (ý đồ C1, gói C1, ý đồ C2, issue C2); WRITER 2 (viết + áp claim); người đọc mù 45 (C1 36, C2 9); người chấm độc lập 2.
- Ký tự ElevenLabs: **3 911** (table read C2).
- Thời gian: P1 bắt đầu 2026-10-04 16:40 UTC; C1 gửi 17:50; C2 qua + giao K 2026-10-04.
- Token: không đọc được.
