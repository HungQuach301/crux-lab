# topics-r1 — báo cáo vòng thử 1 (Mốc 3 v2)

Thẩm quyền: `decisions/D-004.md`. Thiết kế khoá trước khi sinh: `DESIGN.md`, `BRIEF.md`, `tools/cardcheck.py`. Đóng băng: `FREEZE.md` (`d16d1b4`) trước mọi kiểm. Key: SHA-256 `150b040e…` commit trước khi chấm, `key.json` commit sau khi nhận mã — SHA khớp. Bảng AI niêm phong `0150049` trước khi chấm.

## Kết luận vòng 1: **KHÔNG ĐẠT** (máy không hơn đối chứng)

| Cấp | Chỉ số | Ngưỡng | Kết quả | |
|---|---|---|---|---|
| CHÍNH-1 | Thẻ máy điểm ≥ 4 | ≥ 50 % (6/12) | **12/12 = 100 %** | đạt |
| CHÍNH-2 | ≥ 4 máy − ≥ 4 đối chứng | ≥ +20 điểm | 100 % − **6/6 = 100 %** → **0 điểm** | **không đạt** |
| CHẶN | Hồ sơ máy hợp lệ | ≥ 10/12 | **12/12** | đạt |

Không chỉ số nào nằm trong cửa sổ ±5 % quanh ngưỡng. Theo D-004 §5: vòng 1 tính là **"máy không hơn đối chứng"** (1/2 tới điều kiện dừng hẳn); chưa có vòng đạt nào.

**Đọc kết quả:** chủ dự án chấm 18/18 thẻ ở mức ≥ 4 (16 thẻ 4, hai thẻ 5 — một máy `debt-2`, một đối chứng), không chọn chip nào. Thang bị **chạm trần**: bộ đo không phân biệt được hai bên ở ngưỡng ≥ 4. Nghĩa tích cực: khuôn thẻ "quyết định của người xem" (D-003 §2) làm **mọi** thẻ — cả đối chứng — đều được muốn làm, khác M3 (máy thua 7–12). Tín hiệu phân biệt duy nhất (mức 5) là 1/12 máy so với 1/6 đối chứng — quá ít để kết luận.

## Phân bố điểm (chủ dự án)

| | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|
| Máy (12) | 1 | 11 | 0 | 0 | 0 |
| Đối chứng (6) | 1 | 5 | 0 | 0 | 0 |

- **Chip lý do:** không có.
- **Từng trụ:** vay nợ máy 4/4 (một 5) · đối chứng 2/2 (một 5); hưu trí 4/4 · 2/2; thuế 4/4 · 2/2.
- **Nửa đầu / nửa sau (theo thứ tự chấm):** điểm giống nhau (9 thẻ ≥ 4 mỗi nửa); thời gian 166 s so với 58 s — nhịp nhanh dần, thẻ 11 chỉ 3 s.
- **Thời gian chấm (THAM KHẢO):** tổng 224 s (3 phút 44 giây), trung vị 8 s/thẻ; lâu nhất thẻ 03 (43 s, đối chứng) và 01 (38 s, đối chứng).

## Bảng AI tham khảo (6 vai, niêm phong trước)

| Vai | Điểm TB | ≥ 4 máy | ≥ 4 đối chứng | Khớp nhị phân với chủ dự án | Spearman |
|---|---|---|---|---|---|
| đang có lời mời refinance | 2,67 | 1/12 | 1/6 | 2/18 | 0,00 |
| mua nhà lần đầu | 2,67 | 3/12 | 1/6 | 4/18 | +0,30 |
| sắp nghỉ hưu | 2,83 | 4/12 | 1/6 | 5/18 | −0,45 |
| làm tự do, lo thuế | 2,67 | 2/12 | 1/6 | 3/18 | −0,30 |
| vay xe / nợ thẻ | 2,44 | 3/12 | 2/6 | 5/18 | −0,04 |
| chỉ tò mò | 3,33 | 6/12 | 1/6 | 7/18 | −0,14 |

- Trung bình bảng: máy 2,83 (≥ 4: 26,4 %), đối chứng 2,64 (≥ 4: 19,4 %). Spearman trung bình bảng – chủ dự án: **−0,17** (vô nghĩa vì chủ dự án gần như không biến thiên).
- **Độ khớp AI – chủ dự án: thấp.** Bảng AI khắt khe hơn nhiều (TB ~2,7 so với 4,1). Chip AI khác nhau theo bên: thẻ đối chứng bị gắn *seen it* (3,0/thẻ) và *vague promise* (2,5/thẻ); thẻ máy chủ yếu *not me* (3,2/thẻ) và *too narrow* (1,2/thẻ). Gợi ý: máy cụ thể và mới hơn nhưng hẹp hơn; đối chứng rộng nhưng quen. Chỉ tham khảo.

## Hợp lệ hồ sơ máy: **12/12**

Mọi hồ sơ đạt V0 (đủ tệp, cardcheck, mới lạ hợp lệ), V1 (tải lại, SHA khớp), V2 (`calc.py` tái lập), V3 (12 agent mới tính lại độc lập, không thấy `calc.py`), V4 (trang nguồn + điều khoản), V5 (điều luật chính thức). Chi tiết: `verify/out/`. Ghi chú không đổi kết quả: tax-4 câu kết quả ghi 29,6 % nhưng giá trị 29,65 % (làm tròn 29,7 %); retire-3 đợt 2019 hoà 5/10; tax-3 dữ liệu chỉ số chứng khoán có điều khoản cấm tái bản (chỉ dùng số đã tính). Mới lạ: 12/12 `answered-without-data`, không có `not-found`.

## Sinh

- **Máy:** 3 agent (một/trụ), sinh 49 ứng viên, loại 37 (`machine/*-discards.md`; phần lớn vì `answered-with-data`). Đối chứng không được xem.
- **Đối chứng:** GPT-5.5 (`gpt-5.5-2026-04-23`, medium, không công cụ), 3 lệnh, 6/6 thẻ đạt khuôn ngay lệnh đầu, 45 s, 5 494 token.

## Bước 2

Cả 12 thẻ máy ≥ 4 → 12 hồ sơ ≤ 5 dòng, trang https://claude.ai/artifact/FAia52SXAVv4BQroQrToYE (`step2/`). Kết quả "Có/Không" → `topics/queue.md`. *(Chờ chủ dự án.)*

## Chi phí

OpenAI ~5,5 nghìn token (< 0,1 USD). Agent con: máy ~617 nghìn token (3 agent, 15–21 phút), V3 ~647 nghìn (12 agent, 3 phút), bảng AI ~304 nghìn (6 agent, 36 s). Thời gian vòng (đến lúc gửi trang bước 2): dưới 240 phút. Phút của chủ dự án: chấm 3 phút 44 giây.

## Đề xuất MỘT biến cho vòng 2 (ghi trước, chưa chạy)

**Cách chấm: ngân sách thay cho thang tuyệt đối** — chủ dự án chọn **đúng 9/18** thẻ "muốn làm" (giữ thẻ, trộn, câu hỏi, chip, tỉ lệ 12/6, bộ sinh và thước đo: "được chọn" thay cho "≥ 4"). Lý do: vòng 1 chạm trần (18/18 ≥ 4), nên thang tuyệt đối không phân biệt được; ngân sách bắt buộc so sánh mà không đổi bộ sinh. Với 9/18, CHÍNH-1 (≥ 6/12) và CHÍNH-2 (≥ +20 điểm) đều còn đạt được.
