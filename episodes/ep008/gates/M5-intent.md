# M5 Tập 8 — ý đồ kiểm định trên NHÁP 540p màu (ghi TRƯỚC khi có nháp; REVIEWER soát trước khi chạy; không sửa sau khi thấy kết quả)

Ngày 2026-10-13 (sau merge `main` 44229bc1: D-013 + K4.4). Nháp = build `CRUX_GREY=0 bash episodes/ep008/prod/animatic.sh` (6 đoạn + ghép; màu theo hồi `world/grade8.js`), `work/factory/video.mp4` → `out/video.mp4` qua `prod/build_inputs.py --out`. Thứ tự: (1) checks đủ bộ → (2) cổng gốc trên nháp → (3) nhớ lại → (4) nhịp + liền mạch (máy + tay) → (5) lượt đạo diễn (chẩn đoán) → sửa (≤ 2 vòng mỗi lỗi) → (6) gói G2 + REVIEWER.

## 1. L1 — checks ĐỦ BỘ, gồm bộ lấy mẫu trang (LOCK `a35970a8…` K4.4 — lệnh chủ dự án "khi K44 đã merge thì theo LOCK mới")
`EP=episodes/ep008 bash toolkit/checks_split.sh /home/user/chk-ep008` (bản sao khoá; `RESUME=1` khi lệnh nền bị cắt ở trần 2 h). `contract.json lock` = `checks/LOCK`. Nháp 540p: A41 (a) sampler nháp ≠ 1080p đã có trong K4.4 — luật chỉ đo được ở 1080p (C14…) ghi "đo ở M6".
- **Đạt:** 0 CHẶN chưa giải thích. CHẶN do thiếu hợp đồng đã biết (kind mô hình mới `rent-buy-twin-replay` chưa có ở `checks/CONTRACT.md` — phiên K kind mới chưa chạy, `K-brief.md`) → liệt kê, không sửa luật, nêu G2. CHÍNH → sửa trước G2 nếu ở hình/chữ của tập (≤ 2 vòng), không thì nêu.
- Ghi số luật đạt/trượt theo cấp vào `gates/M5-checks.md`.

## 2. Cổng gốc tắt tiếng trên nháp (như `gates/M2-root-intent.md`)
24 nhịp loại 1, 2 người đọc mới/nhịp (+ người thứ 3 khi lệch), 2 người chấm mới, gộp thận trọng, rubric khuyên mới. **Mục đích:** bắt hồi quy do màu/chất liệu so với animatic r2 (19/24). Ngưỡng 20/24; `advice_stated` = 0. **Hồi quy** = nhịp đạt ở r1/r2 animatic mà trượt trên nháp → đọc lại nhịp đó một lần (2 người mới) trước khi coi là thật (biên nhiễu A32 ≈ 3 nhịp; "≥ 2 lượt đọc lại đồng ý"). Năm nhịp so sánh giữa cảnh (B09 B10 B20 B24 B25) đã hết 2 vòng ở M2 → chỉ đo, không sửa, trước/sau ở G2.

## 3. Nhớ lại (vai Đạo diễn sáng tạo; CHỈ BÁO — chưa hiệu chuẩn, `episode.md` §1a)
3 người đọc headless mới: 4 tấm × 12 khung theo hồi (cold open + hồi 1 · hồi 2 · hồi 3 · giới hạn + kết) + toàn văn lời có mốc giây. Hỏi: "What three moments do you remember most? What question was the video asking?" Người chấm: khớp K1/K2/K3 của `preprod/TAM-NHIN.md` §1 và câu hỏi của phim. Báo k/3 người kể ≥ 2/3 khoảnh khắc; không mở vòng sửa.

## 4. Nhịp (Editor) + liền mạch (Giám sát) — máy + tay, chỉ báo trừ khi lỗi khách quan
- `ffmpeg freezedetect` (n = 0,003, d = 3 s) trên nháp: tổng giây đứng hình có lời ≤ 30 s; quãng có lời không cú máy/không vật đổi > 8 s (spine `f14` cảnh báo) — liệt kê.
- Tay, trên nháp: 3 số neo có vật thể trong ±1 s quanh từ đọc; lặng trước số neo 0,7–1,0 s (timeline); màu hồi đúng `grade8.js` (lấy khung giữa mỗi hồi); footage bản đồ có nguồn trên hình và ≤ 6 s; chữ số chỉ ở đồ thị (verify quy tắc 1). Ghi `gates/M5-continuity.md`.
- J/L-cut: chỉ L-cut S30 → S31 trong đoạn f; qua biên đoạn nhà máy chưa hỗ trợ → nêu G2 (không sửa nhà máy giữa tập — `episode.md` §1: giữa tập chỉ sửa CHẶN + CHÍNH).

## 5. Lượt đạo diễn (chẩn đoán, D-010 §6)
1 lượt headless trên 12 khung trải đều mỗi hồi (4 tấm) + lời: 4 trục + lời phê theo mốc giây. Lời phê chỉ thành việc sửa khi phép thử của vai sở hữu cũng trượt ở đúng chỗ đó (§1a).

## 6. Sửa + gói
Lỗi trượt thật (CHẶN/CHÍNH, nhịp hồi quy đã xác nhận, câu khuyên) → sửa bằng hình trước, ≤ 2 vòng mỗi lỗi, vòng chỉ giữ khi vượt bản tốt nhất ngoài biên nhiễu. Hết vòng → trước/sau ở G2. **G2** (`templates/G2.md` nếu có, ≤ 3 câu): nháp 540p (đường dẫn), 3 khung tĩnh 1080p cảnh đinh (B01, B17–B18, B24/B32 — render `--res 1080` chỉ khung đơn, ≈ 5 phút máy), phiếu L3 (`templates/L3.md`), trước/sau, Short (mô tả + mốc giây, dựng ở M6), câu hỏi mở (S13 "3 in 4", câu chuyền tập kế). REVIEWER headless soát gói trước khi gửi.

**Chi dự kiến (Console):** cổng gốc ≈ $1,6 · nhớ lại ≈ $0,3 · đạo diễn ≈ $1 · REVIEWER ý đồ + gói ≈ $2,5 → ≈ $5,5; chặng hiện $5,75 → ≈ $11–12 / trần $25 cứng.
