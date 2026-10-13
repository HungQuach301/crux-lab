# F-15 · Ý đồ + ngưỡng ghi trước (viết 13/10/2026, TRƯỚC mọi lần đo)

Phiên nhà máy F-15, nhánh `factory-f15` từ `origin/main` @ `c7358285` (push lên `claude/clever-hopper-qkzobc`, nhánh phiên do harness ghi).
Việc không phải tập (CHARTER §2.3) — giúp Tập 8: cắt vòng dựng lặp (Tập 7: ≈ 30 h máy ở P3 + 5,8 h ở P4, TONGKET-INPUT h, i, p) và mở đường cho
footage ngoài, **không đổi chất lượng** (D-009). Mọi thay đổi **opt-in, hoặc trùng byte khi không bật**.

## 1. Giả thuyết
1. Vòng sửa (kiểm mù, cổng gốc, checks đủ bộ kể cả bộ lấy mẫu trang) chạy được trên **bản nháp 540p cả tập** dựng từ cùng `episode.yaml`
   (cờ `--res 540`, tuỳ chọn `--spp`), rẻ hơn nhiều bản 1080p; bản 1080p chỉ dựng **một lần** sau khi nháp đạt. Phán quyết của checks và cổng gốc
   trên nháp khớp bản 1080p trong mức nhiễu đã biết, trừ các luật đọc điểm ảnh video đã liệt kê trước (§3).
2. Mất giờ máy ở Tập 7 phần lớn do môi trường (trần 2 h của lệnh nền, container mới thiếu đồ ngoài git, PyAV hỏng ASR), không do render: build
   nguyên tử + resume theo khung + `setsid nohup` + `verify.sh --install` loại các lượt trượt môi trường.
3. Footage ngoài (ảnh/video tư liệu, bản đồ) đi vào thế giới như một `plate` của cảnh, có nguồn/giấy phép tự ghi, mà không đổi byte đoạn cũ.

## 2. Đối chứng
| Thứ | Giá trị |
|---|---|
| Tập 7 bản G2 (720p) | `episodes/ep007/review-g2/full-720p.mp4` trên nhánh `ep007` (19.306.228 byte) |
| spine/timeline đã giao | 7 `world/c4/*/spine.json`, `out/factory/timeline.json`, `out/factory/captions.srt` của `main` @ `c7358285` |
| Giờ máy Tập 7 | P3 ≈ 30 h (1080p 7 lượt); P4 ≈ 5,8 h (dựng lại 1080p ≈ 2,9 h gồm 2 lượt trượt môi trường + 1 lượt cắt 2 h; lấy mẫu trang ≈ 2,9 h) |
| Nhiễu cổng gốc (A32) | cùng một bản 1080p cuối: 5 / 6 / 7 trên 21 tuỳ lượt chấm (`c5/root-final`, `regrade/`) → dải nhiễu ±2 nhịp |

## 3. Đích (không hạ sau khi đo)
| # | Thước | Đích | Vai trò |
|---|---|---|---|
| T1 | 7 `spine.json` + `timeline.json` + `captions.srt` khi dựng 1080p KHÔNG bật cờ mới, từ container mới | **trùng byte** với `main` | **chính** |
| T2 | SSIM (ffmpeg `ssim`, trung bình All) bản 1080p mới thu về 1280×720 so `review-g2/full-720p.mp4` | **≥ 0,97** (báo thêm min theo cảnh) | **chính** |
| T3 | Giờ máy nháp 540p cả tập (cache trống) / giờ máy 1080p một lần (cache trống), cùng máy 4 nhân | **≤ 0,40** | **chính** |
| T4 | Checks đủ bộ (bộ lấy mẫu trang + luật Python, LOCK `dc4981b3`) chạy HẾT trên nháp (video nháp phóng 1080 trong bản sao checks) | thoát 0, 0 ERROR mới so bản 1080p | **chính** |
| T5 | Mọi luật CHẶN/CHÍNH FAIL trên bản 1080p mới cũng FAIL trên nháp, NGOÀI tập R_pix dưới | **0 bỏ sót** | **chính** |
| T6 | Đồng phán quyết nháp ↔ 1080p trên mọi luật (PASS/FAIL/MISSING) | ≥ 90 % | chỉ báo |
| T7 | Cổng gốc tắt tiếng (`c4/blind_c4.py` root, 21 nhịp, 2 người chấm, gộp thận trọng) nháp ↔ 1080p mới | \|Δ điểm\| ≤ 2 nhịp và ≥ 80 % nhịp cùng PASS/FAIL | **chính** (khoá nghĩa) |
| T8 | Dải kiểm mù (`toolkit/blind/strips.py`) chạy trên nháp | ra đủ dải, không lỗi | chính |
| T9 | Resume theo khung: ngắt render một cảnh bằng PID giữa chừng, chạy lại `--resume` | tệp cảnh **trùng byte** với lượt không ngắt | **chính** |
| T10 | Build nguyên tử: lượt trượt giữa chừng | sản phẩm cũ trùng byte (SHA trước = sau) | **chính** |
| T11 | `verify.sh --install` trên container mới | dựng được tập mà không bước tay nào ngoài lệnh; một lần nhận dạng thử (ASR) ra đúng từ | **chính** (FRED: chỉ ĐẠT khi mạng cho) |
| T12 | `toolkit/api.sh`: agent con bị chặn; trần chi theo lệnh dừng lượt | Task/Agent bị từ chối; `--max-budget-usd` hiệu lực | **chính** |
| T13 | Footage: clip 540p 8 s (1 ảnh LoC "No known restrictions" + 1 bản đồ bang/vùng Mỹ); RIGHTS + SHA tự ghi; chữ/nguồn không đè hộp `focus` | 0 hộp chữ giao hộp chủ thể; 2 dòng RIGHTS đủ URL + giấy phép nguyên văn + ngày | **chính** |
| T14 | Mã thế giới không bật `plate`: đoạn Tập 7 render lại | khung trùng MD5 với `core.js`/`lib3d.js` cũ (một cảnh mẫu) | **chính** |

**R_pix** (luật đọc tệp/điểm ảnh video hoặc Shorts — ghi trước bằng quét mã `checks/py/r_*.py`, được phép khác giữa nháp và 1080p, vẫn báo từng
luật): A04 A13 F01 F05 F06 F07 F08 F10 S20 R07 V14 V08 V11 V12 R03 R04 R06 SH01 SH02 T1 V05 V09 V10 V13 P01 + mọi luật trang dùng mẫu điểm ảnh
video của bộ lấy mẫu (`videoReader`). Bỏ sót CHẶN/CHÍNH trong R_pix = **ghi tên**, kèm bản chất (độ phân giải hay nội dung).
**Đạt = mọi số chính đạt.** Trượt → báo số, không hạ đích, không merge (chủ dự án/điều phối quyết).

## 4. Điều kiện đo
- Tập 7 dựng từ bản sao làm việc ngoài repo (`git worktree` của `origin/ep007` + `toolkit/` của `factory-f15` chép đè), cùng kịch bản, giọng
  (`voice-takes/`, 0 ký tự EL), nhạc (`bed.wav` sinh lại bằng `build_inputs.py --timeline`), claim. **Không sửa `episodes/ep007`, `ep008`, `checks/`.**
- Cache trống cho cả hai lượt (nháp, 1080p); cùng `--workers` (≤ số nhân − 1); không chạy checks song song với render.
- Tiến trình dài chạy bằng `setsid nohup` (`toolkit/bg.sh`), dừng theo PID, kiểm `ps` (guard) trước khi dựng.

## 5. Chống Goodhart
- Không đổi đặc tả tập để nháp "giống" 1080p; nháp chỉ khác `res` (và `spp` khi khai). Không sửa `checks/`; luật mà nháp không đo được → ghi, không vá.
- Cổng gốc nháp và 1080p chấm cùng rubric, cùng số người, cùng gộp; không chọn lượt chấm đẹp.
- SSIM so với bản G2 thật, không với bản dựng trong phiên.

## 6. Ngân sách
Console trần **$15** cả phiên (cổng gốc 2 × ≈ $1, REVIEWER ≈ $1–2, thử `api.sh` < $1). Headless khoá Console, **0 agent con**. Push sau mỗi bước lớn.
