# Giao phiên K — Tập 4 (`episode.md` §7) · 2026-10-05, P1

**Một lần chạy cho Tập 4, khi chủ dự án duyệt G1** (đề tài có thể đổi ở G1; nếu đổi, brief này huỷ). Tên kind và params do K quyết; bên dựng theo (lessons E8).

## Cần kind MỚI
Không dòng nào trong bảng "Loại mô hình" (`checks/CONTRACT.md`) phủ "giới hạn danh nghĩa cố định so với tăng trưởng chỉ số giá nhà theo vùng".
- **Đặc tả gốc:** `topics-r1/machine/tax-2/model.json` → `newKindNeeds` (inputs, params, computation, outputs, invariants — đủ 5 phần).
- **Mở rộng của tập** (định nghĩa ở `episodes/ep004/gates/V0-defs.md` mục 4): với giá mua minh hoạ P ∈ {200000, 300000}: `gain_at_<P>_<series>`, `cross_quarter_at_<P>_<series>` (quý đầu tiên ≥ 2001 Q1 có lãi > giới hạn, nghiêm ngặt), `stay_quarter_at_<P>_<series>` (quý đầu tiên mà từ đó tới quý bán lãi luôn > giới hạn), `metros_crossed_at_<P>`.
- **Bản tính của bên dựng:** `episodes/ep004/model/model.py` → `out/model.json` (`raw` chưa làm tròn, `rounded`). Kiểm độc lập 116/116 (`model/independent/`).
- **Dữ liệu:** `episodes/ep004/data/fetch.py` (14 chuỗi FRED, SHA khớp hồ sơ; dữ liệu không commit).

## Danh sách claim (chốt ở C2 vòng cuối)
`episodes/ep004/numbers.md` (claim ID = khoá `rounded`, cộng hằng số luật và `illustrative_price_*`, `metro_count`). Claim thật sự dùng trong lời: cột claim của `episodes/ep004/story/script.md`.

## Luật tập đề xuất (K xét)
1. Mọi khung có ngưỡng/lãi/quý vượt phải có nhãn "a home that rose like its metro area's average" hoặc dạng rút gọn đã khoá (claim-risk hồ sơ "Always say").
2. Giá $200,000/$300,000 mang nhãn ILLUSTRATIVE trên mọi khung (như claim nhân vật minh hoạ).
3. Không khung nào đổi ngưỡng thành số thuế phải nộp.
