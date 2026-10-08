# Giao phiên K — Tập 5 (`episode.md` §7) · 2026-10-06

**Có hiệu lực khi G1 duyệt đề tài #17.** Một lần chạy cho Tập 5; gộp lô hàng chờ `checks-appeal.md` (thứ tự A10 → A11 → A12 → A5 → A7 → A9, tongket-t4 §5). Tên kind và params do K quyết. Tự merge chỉ khi đủ D-008 §2 (chỉ thêm kind/luật mới, selftest đạt, luật cũ không đổi hành vi, 0 lệch); lô A10–A12 sửa luật cũ → **hỏi chủ dự án**.

## Cần kind MỚI
Không dòng nào trong bảng "Loại mô hình" (`checks/CONTRACT.md`) phủ "số tháng tới khi dư nợ theo lịch / giá trị nhà tăng theo chỉ số chạm 80 %". Lý do từng kind: `topics-r2/machine/debt-2/model.json` → `noExistingKind`.
- **Đặc tả:** `topics-r2/machine/debt-2/model.json` → `newKindNeeds` (inputs, computation, outputs, invariants, dataNow).
- **Mở rộng của tập:** ba người mua ILLUSTRATIVE (`buyer_fast_*` 2004-01, `buyer_typical_*` 2014-06, `buyer_slow_*` 2005-10 — luật chọn và luật hoà ở `numbers.md`), đường chỉ số của người mua chậm (đỉnh/đáy), tháng chậm > 60 (`slowB_*`), ví dụ $400,000 (`ex_*`, ILLUSTRATIVE; giá từ MSPUS quý 2/2026), ngưỡng điểm giữa (`midpoint_*`).
- **Luật "tháng lãi mới nhất" = tháng lịch cuối cùng đủ tuần** (2026-09, 6,862 %), không phải `max(month)` (2026-10 chỉ 1 tuần, 7,28 %): bất biến K nên kiểm.
- **Bản tính bên dựng:** `episodes/ep005/model/model.py` → `out/model.json` (`params`, `raw`, `rounded`). Kiểm độc lập **55/55** (`model/independent/report.md`).
- **Dữ liệu:** `episodes/ep005/data/fetch.py --verify` (FRED HPIPONM226N, MORTGAGE30US, MSPUS; đối chiếu CSUSHPINSA — *Pre-Approval Required*, chỉ kiểm nội bộ, không lên hình — và OBMMIC30YF). `data.crosscheck`: lãi PMMS vs Optimal Blue trung bình 7 ngày 508/508 trong 0,5 điểm; % đổi theo tháng FHFA vs Case-Shiller 374/426 (52 tháng ở `mismatches`).

## Danh sách claim
`episodes/ep005/numbers.md`; claim dùng trong lời: comment `<!-- claims -->` của `story/script.md`. Luật pháp lý (12 U.S.C. 4901/4902, CFPB, điều lệ Fannie/Freddie): `data/sources.json` → `provisions`. **Mốc 75 % / 2 năm (gỡ theo giá trị) chưa có trích nguyên văn** (fanniemae.com, freddiemac.com bị proxy chặn) — xem G1.

## Luật tập đề xuất (K xét)
1. Mọi khung có số "on paper" (tháng tới 80 % theo chỉ số) mang nhãn điều kiện kiểu "on paper (national index), not removal" (`claims.conditions`, như S17 Tập 3–4).
2. Ba người mua + ví dụ $400,000 mang ILLUSTRATIVE trên mọi khung.
3. Không khung nào nêu số tiền phí PMI (không có nguồn).
