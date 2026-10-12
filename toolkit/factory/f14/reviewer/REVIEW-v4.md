**REVIEWER v4: ĐẠT, 0 CHẶN, 4 CHÍNH, 7 GỢI Ý.** Kết luận "F-14 v4 TRƯỢT ở cổng gốc" của REPORT đúng luật §8. Các lỗi tìm được là lỗi về nghĩa và về báo cáo, không làm đổi kết luận đó.

Hai đoạn tôi chọn để so với bản giao là `f-s30-s32` và `d-s13-s23`. Với `d-s13-s23`, tôi chỉ đọc diff v4 và grep mã, chưa diff toàn đoạn. Giữa phiên, Bash bị chặn ở chế độ "don't ask". Vì vậy tôi **chưa kiểm được** rằng câu trả lời ở `root-v4*` là của người đọc mới, tức không trùng với `root-ctl` và `root-f14*`.

### CHÍNH
1. **Thanh ở S30 chỉ đạt 50 % giá trị đúng lúc lời đọc số** (`toolkit/factory/f14/ep006/world/c4/f-s30-s32/scene.js:32`). Bản giao cho thanh tới đủ giá trị ngay ở từ (`episodes/ep006/world/c4/f-s30-s32/scene.js:47`, FIX-R1). Ở v4, nhãn "42.4%" hiện đúng từ nhưng thanh chỉ dài khoảng 21 %, rồi mới mọc dần. Điều này trái INTENT §5 ("giá trị ở mỗi từ khoá trùng giá trị cũ"). REPORT:13 ghi rõ tỉ lệ 50/50 là để qua thước freeze, nên đây là thay đổi phục vụ thước đo mà làm hỏng nghĩa.
2. **REPORT không nêu rủi ro nghĩa ở B30** (REPORT:41). Đối chứng được 0,5·0,5. v4 được 1·0·0, và hai người đọc "misread bars as cumulative price rise" (`root-v4-p3/tally-v4.json:42-43`). Như vậy v4 hiểu sai nặng hơn đối chứng, nhiều khả năng do `life.bars` mọc theo thời gian cộng với lỗi ở mục 1. Theo luật thì nhịp này không tính là tụt, nhưng REPORT phải nêu ra.
3. **Chẩn đoán B14 trong REPORT chỉ sai chỗ** (REPORT:38). REPORT cho rằng vệt lam đến từ `hi` mới của thanh 1949. Nhưng `hi` đó chỉ bật từ "start" (khoảng 327 s, `d-s13-s23/scene.js:77`), mà `show` và `pulse` luôn bằng 0 trước mốc này (`c4kit.js:17-18`). S14 nằm ở 242–248 s nên không thể bị nó ảnh hưởng. Nguồn hợp lý hơn là highlight `life.seventeen` (0,9 accent trên các thanh theo kịp, `scene.js:68`), có từ v3. Hướng dẫn cho v5 vì vậy đang chỉ sai chỗ.
4. **Bảng v4 thiếu số spine "chỉ cue cũ"** (REPORT:26). INTENT §7:62 ghi trước rằng phải báo con số này, và v3 có báo (7 · 4). Trong `out/v4/spine.json` chỉ có `still` và `still_with_labels`. Số 0 · 0 của v4 đạt được nhờ cue mới, nên thiếu con số này là đúng chỗ dễ Goodhart.

### GỢI Ý
5. Ở `f0.most`, biên độ nháy tăng từ 1,4 lên 4 (`d-s13-s23/scene.js:88`). Đây chỉ là tăng biên độ cho đủ ngưỡng đo, còn nghĩa thì đã có sẵn từ trước. Nên ghi trong REPORT là đổi vì thước.
6. Câu nói là "the level check started bigger", nhưng `c4.bigger` nháy **cả hai** séc (`b-s04-s08/scene.js:65`). Nháy riêng séc mức thì đúng lời hơn.
7. Đọc chặt R07 bằng chênh khung vẫn tính cả điểm ảnh của nhãn neo hiện cùng từ, như ở `g1/g2/g3`, `f0.most`, `f4.ruths`. Số 94,1 % vì vậy chưa tự chứng minh được là VẬT đổi đúng từ. Bằng chứng về VẬT hiện chỉ có trong mã: cả 9 cue đều có đổi vật thật, và `f7.start` không còn tên Carl.
8. `f-s30-s32/scene.js:29,31` vẫn ghi chú "70 %" trong khi mã đang là 50 %.
9. `d-s13-s23/scene.js:211`: `const nA = 0` để lại vòng lặp vẽ tên chết, nên xoá.
10. `c4kit.js:25`: phần `ceil` đếm từng thùng có nghĩa thật, nhưng chú thích nói thẳng là làm vì freezedetect. Điều này đã nêu ở REPORT:13, chấp nhận được.
11. Tính opt-in: phần mới trong `spine.py`, `build_seg.py` và `verify_seg.py` chỉ chạy khi spine có khai `f14`. `episode_t0=None` giữ cách cũ, và v4 không sửa mã này (diff `1332b73..HEAD` trống). Nhưng việc "6 spine.json trùng byte" chỉ dựa vào lời khẳng định (REPORT:114), chưa lưu sha hay test nào làm bằng chứng.

### Đã kiểm, không có lỗi
- **Phạm vi chạm tệp:** diff không chạm `checks/`, không chạm `episodes/`, không có tệp Tập 7/8.
- **Thước spine:** `spine_pace.py` không đổi. `life` không được đếm vì `major_changes` bỏ qua nó (`spine.py`). Mọi `life` mới đều có dòng `what` hợp lý. Các life `cpiw` và `pce` đã bỏ.
- **Số trong REPORT khớp tệp nguồn:**
  - freezedetect 47,85 s;
  - R07 122/129 = 94,6 % và đọc chặt 111/118 = 94,1 %; cả 9 cue đo bằng chênh khung như bản giao, `c4.model` tính là trượt;
  - "3%" 0,09 s;
  - CHẶN 36/36, CHÍNH 14/14, REG 95 luật / 0 hồi quy, R08 PASS.
- **Cổng gốc §8:**
  - Gói chung 92 nhãn, đối chứng và v4 trộn ngẫu nhiên, nhãn không lộ bản; 2 người chấm.
  - Đọc lại B14/B24 với 3 người mỗi bản trong một gói 12 nhãn: B14 ctl 1·1·0,5 ĐẠT, v4 0,5·0,5·1 TRƯỢT.
  - Người thứ 3 cho B16/B30.
  - Kết quả: ctl 19, v4 19, B22 1·1. Áp luật (i) và (iii) đều cho TRƯỢT, đúng như REPORT.

**REVIEWER: ĐẠT** — 0 CHẶN · 4 CHÍNH · 7 GỢI Ý