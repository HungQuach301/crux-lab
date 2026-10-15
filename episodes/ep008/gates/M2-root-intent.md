# M2 Tập 8 — ý đồ cổng gốc tắt tiếng trên ANIMATIC XÁM (ghi TRƯỚC khi có animatic; không sửa sau khi thấy kết quả)

Ngày 2026-10-13 (chặng sau G1). Mô hình xưởng 6 mốc (tổng kết Tập 7 §2, chủ dự án duyệt 13/10): phép thử của vai Previz = **cổng gốc tắt tiếng trên animatic 540p xám**, thay cổng C3 riêng (G1 câu 3: "Không C3 riêng"). Nguồn hình: `out/video.mp4` của build animatic (`CRUX_GREY=1 bash toolkit/build.sh episodes/ep008/episode.yaml --no-shorts`; khung → độ sáng, chưa chất liệu). Công cụ `prod/root_gate.py` (chép rút gọn `episodes/ep007/c4/blind_c4.py` phần A). Người đọc headless khoá Console (`toolkit/blind/headless.sh --read`, mỗi lượt MỚI, chỉ mở tệp tên hex).

**Vai T** (= C2): người thuê Mỹ 2026, đủ 20 % trả trước, "tính đủ lãi, thuế, bảo hiểm, sửa chữa thì thuê có đắt hơn mua?". **Câu hỏi cố định** (như C3/C4 Tập 7): 1 What idea is this showing? 2 What changes over time? 3 What does it mean? 4 What advice, if any…? 5 Did the animation itself suggest this, or is it your own conclusion? ('none' nếu không có lời khuyên).

**Nhịp:** mọi nhịp loại 1 của `story/beats.md` (24 nhịp: B01 B02 B03 B05 B06 B07 B08 B09 B10 B11 B12 B13 B15 B17 B18 B20 B22 B23 B24 B25 B27 B29 B32 B33); ý cần đọc ra = cột "Muted read" nguyên văn (SHA của beats.md ghi trong tally). Dải 6 khung đều trong cảnh (đầu cảnh + 0,2 s → cuối cảnh − 0,2 s), tắt tiếng, giữ chữ/số trên hình (`toolkit/blind/strips.py`). Ghi chú: B26/B27 cùng cảnh S27 (chỉ B27 loại 1); B24 → S25, B25 → S26 sau khi số neo được dời ra đầu cảnh (chữ không đổi, ledger 13/10).

**Đọc + chấm:** 2 người đọc/nhịp; lệch → người thứ 3 (`--slots 3 --only …`); nhịp đạt khi ≥ 2/3 người đọc đúng (điểm 1 VÀ không `advice_stated`). **Gộp thận trọng** (lệnh chủ dự án): 2 người chấm headless độc lập trên cùng gói nhãn ngẫu nhiên; điểm của mỗi người đọc = **điểm thấp nhất** của hai người chấm; cờ khuyên bật nếu **bất kỳ** người chấm nào bật. Rubric khuyên mới (K4.2b): `advice_stated` tính; `advice_inferred` / `caution_only` chỉ báo kèm câu trích.

**Ngưỡng:** cổng ≥ 80 % nhịp đạt → **≥ 20/24 (83,3 %)**; 19/24 (79,2 %) và 20/24 nằm trong ±5 % quanh ngưỡng → nêu tên. Mọi nhịp có `advice_stated` → trượt nhịp đó, sửa trước M3.

**Biên nhiễu (A32, K4.4 trên nhánh `checks-k44`):** đọc lại cùng bản giao Tập 6 ba lượt cho 20 / 16 / 19 trên 23, 7 nhịp lật → một vòng sửa chỉ được **giữ** khi số nhịp đạt vượt bản tốt nhất ≥ 3 nhịp **hoặc** nhịp được sửa đạt 2/2 ở cả hai lượt đọc (≥ 2 lượt đồng ý — tổng kết Tập 7 §2d rủi ro 4: "chưa có A32 thì dùng tạm ≥ 2 lượt đọc lại đồng ý"). Không đạt điều kiện đó → giữ bản trước, nêu trước/sau ở G2.

**Sửa:** ≤ **2 vòng mỗi lỗi** (lệnh chủ dự án), sửa bằng HÌNH trước (đổi bố cục, máy quay, loại hình — vai Previz), nhãn là cách cuối; **không đổi lời**. Vòng 2 trượt cùng câu trả lời → hạ "ý cần đọc ra" về mức hình nói được (ghi `beats.md` trước khi chạy lại), hoặc trước/sau ở G2. Chỉ đọc lại các nhịp đã sửa (2 người đọc mới mỗi nhịp, cùng 2 người chấm mới).

**Lượt dự kiến:** vòng 1 = 48 lượt ảnh (+ người thứ 3 ≤ 24) + 2 người chấm ≈ $2,5–3,5 Console. Trần chặng $25 cứng (`logs/usage/spend_leg.py`); chạm → dừng hỏi.
