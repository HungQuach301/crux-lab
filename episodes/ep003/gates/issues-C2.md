# Bản nháp issue (P1 — REVIEWER soát trước khi mở)

## A. `[Phân loại nhịp] Tập 3 — bảng nhịp loại 1 / loại 2` (trước mọi kiểm mù hình)
Bảng `story/beats-class.json` SHA-256 `2299ddf57793ae1285ba8eeec1b1e0bff8d65b500d7aeee248e6e461c05b25a0` (từ `story/beats.md` SHA-256 `dfdca530…`). Nhịp then chốt 7; loại 1 (hình tự mang ý) **6/7 = 86%** (sàn 60%).

| Nhịp | Loại | Ý người xem phải đọc ra khi tắt tiếng (nguyên văn `beats.md`) |
|---|---|---|
| KEY-1 | 1 | "A person is choosing between two ways to park money for 20 years: a chain of short bills, or a bond that is guaranteed to reach ×2 at year 20." |
| KEY-2 | 1 | "Almost the whole history shown is a what-if (hatched, 'IF today's guarantee had existed'); only a short stretch from May 2005 is real." |
| KEY-3 | 2 | (loại 2: chú giải 3.72 vs 3.53, minh hoạ lời) |
| KEY-4 | 1 | "Overall about half of the rolls beat double, but the middle era (1950–1989) nearly always beat it and the starts from 1990 almost never did; the earliest era never did." |
| KEY-5 | 1 | "The only starts where the guarantee was real are a small cluster at the very end, all short of ×2 — tagged 'small sample · one era'; overall about half still beat ×2." |
| KEY-6 | 1 | "Doubling the dollars did not always keep up with prices: often the doubled stack is smaller than the 'price shadow' of what the original money bought; worst case barely over half." |
| KEY-7 | 1 | "There is a threshold on the bill-rate scale just above the long-run average; to beat ×2 the 20-year average rate must land above it, and the marker can land on either side." |

Bảng không đổi sau issue này; hạ loại chỉ qua dự phòng C3, nêu trong gói C3. Chủ dự án có quyền phủ quyết.

## B. `[Cổng C2 · tự động] Tập 3 — qua`
- Kết quả: máy ĐẠT (claim 46/46, S10 0, US only + history-not-a-forecast, luật giả định ở cold open); kiểm mù lời đúng **6/6**, khuyên **0/6** (đúng sát ngưỡng: 4/6 người đọc viết "Don't judge… by today's rate", người chấm độc lập xếp không phải lời khuyên hành động; không chấm lại), không cảnh nào ≥ 4/6 mất chú ý (tối đa 3/6).
- Ngưỡng: ≥ 5/6, khuyên 0, < 4/6 mỗi cảnh. Vòng 1/2; không dùng dự phòng.
- Tín hiệu cho C3: 6/6 vấp cặp 3.53/3.47; giả định chỉ nêu rõ 1/6 (nhãn hình gánh); đối chứng M1b cho thấy câu 3–4 không phân biệt được.
- File: `gates/C2.md`, `gates/C2-blind.md`, `story/script.md`, `story/beats.md`. Cấu trúc + cold open là bản tạm → chủ dự án duyệt ở C3.

## C. `[Phiên K] Tập 3 — kind mới (đặc tả retire-4 newKindNeeds; nhãn làm việc của chủ dự án) — đầu vào`
- Đầu vào: `episodes/ep003/numbers.md`, `episodes/ep003/checks-notes.md` (danh sách claim = `checks-notes.md` §2, 46 ID), đặc tả `topics-r1/machine/retire-4/model.json → newKindNeeds` (tham số hoá; retire-3 dùng lại được).
- Tên kind và params do phiên K quyết; bản dựng theo sau. Khoá K cần merge `main` **trước C4**.
- Việc treo: "khoá K của tập" (PLAN §3).
