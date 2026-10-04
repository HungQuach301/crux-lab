# PLAN — Tập 3 (playbook v2)

Nhánh: `ep003` (từ `main` `c0376d1`). Chỉ P3 merge `ep003` vào `main`. Khung: `playbook/quality-framework.md` v2; sổ tay: `playbook/episode.md`.

**Đề tài:** `topics/queue.md` #7 — "Savings Bonds That Double in 20 Years vs T-Bills" — hồ sơ `topics-r1/machine/retire-4/` (chủ dự án chỉ, 2026-10-04). Trụ: hưu trí (tập đầu của trụ). Mô hình: **kind mới** — đặc tả `retire-4/model.json → newKindNeeds` (nhãn làm việc `lock-vs-roll-replay`, tham số hoá để retire-3 dùng lại; **tên kind và params do phiên K quyết**).

## 1. Bảng cổng và quyết định

| Cổng | Trạng thái | Gói | Quyết định của chủ dự án |
|---|---|---|---|
| Hồ sơ đạt `topic-dossier.md` | XONG — `retire-4/dossier-check.md` 4/4; commit `43350f3` | — | — |
| Việc 0 | XONG — SHA trùng; kiểm độc lập 873/873 cửa sổ, 36/36 đại lượng; retire-3 11/11 qua cùng mô hình | `numbers.md` | — |
| C1 (GU) | XONG (vòng 1) | `gates/C1.md`, `gates/C1-blind.md`, issue #26 | A + A1; giả định (a) trong cold open + nhãn hình; ghim 8/2026; lãi EE 2.40% V1 "for bonds issued May–October 2026" |
| C2 (TỰ ĐỘNG) | ĐANG LÀM — WRITER | `gates/C2-intent.md` | — |
| Giao phiên K | chưa | — | — |

## 2. Phiên sau đọc
(P1 tiếp sau C1: `gates/C1.md`, `numbers.md`, `topics-r1/machine/retire-4/claim-risk.md`, `retire-4/model.json`; cập nhật cho P2 cuối P1)

## 3. Việc treo
- **Cho C3 (bắt buộc, lệnh chủ dự án 04/10):** cần **ít nhất một ký hiệu mới** cho ý "gấp đôi / sức mua" — không lặp hình Tập 2 (V1 lưới ô chạy lại, V3 đường lãi so vạch, dãy núi TB3MS đều đã dùng cho cùng chuỗi TB3MS ở Tập 2). Ứng viên chưa có trong thư viện: bội số tiền "×2" như một vạch đích; sức mua của gấp đôi (giỏ hàng co/giãn). C3 thiết kế mới, kiểm cổng gốc.
- **Giả định "nếu khi đó đã có bảo đảm"** cho mọi cửa sổ trước 5/2005: nói bằng lời và hiện trên hình **ngay từ đầu (cold open, trước mọi số lịch sử)** (claim `ctx_hypothetical`); WRITER và C3 nhận làm luật của tập.
- Khoá K của tập: kind mới → phiên K phải viết bản tính lại trước C4.
- **P3/C6:** trước phát hành cập nhật lãi EE công bố **1/11/2026** (một claim `ctx_ee_rate`; kết quả lịch sử không đổi). Lời/hình luôn ghi "for bonds issued May–October 2026".
- Ghim dữ liệu August 2026 (chủ dự án C1); TB3MS 9/2026 = 3.94% không dùng.

## 4. Điểm dừng an toàn
- 2026-10-04 (3): C1 xong. Đang: WRITER (`story/WRITER-brief.md`). Nếu mất: giao lại WRITER cùng đầu bài → `python3 episodes/ep003/story/check_script.py` → kiểm mù C2 theo `gates/C2-intent.md`.
- 2026-10-04 17:50 (2): **gói C1 gửi (sau REVIEWER), issue [#26](https://github.com/HungQuach301/crux-lab/issues/26). DỪNG chờ chủ dự án** (3 câu). Sau khi trả lời: ghi `taste-ledger.md`, `AUTHORSHIP.md` (trên `ep003`) + ledger; giao WRITER (đầu bài `episode.md` §3 + luật tập: giả định trước 5/2005 nói bằng lời thường **trong cold open, trước mọi số lịch sử** (theo quyết định câu 2) + nhãn hình; không đặt 3.72% cạnh 3.53% mà không chú giải; mốc 17 tháng luôn kèm "mẫu ngắn" + tỉ lệ toàn kỳ) → C2.
- 2026-10-04 17:10 (1): hồ sơ + Việc 0 xong. Đang: REVIEWER soát ý đồ C1 → kiểm mù C1 (`review-c1/`, manifest T/G/titles). Nếu mất container: `python3 episodes/ep003/data/fetch.py --verify --retire3 && python3 episodes/ep003/model/model.py && python3 episodes/ep003/model/model.py --retire3`.

## 5. KPI tạm
- Chủ dự án tham gia: 1 (C1, đang chờ). Vòng: C1 1. Lượt agent: 40 (kiểm độc lập 1, REVIEWER ý đồ 1, người đọc 36, người chấm 1, REVIEWER gói 1). Ký tự EL: 0.
