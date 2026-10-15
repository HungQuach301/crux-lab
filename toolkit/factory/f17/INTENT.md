# F-17 · Ý đồ + ngưỡng ghi trước (viết 14/10/2026, TRƯỚC mọi lần đo)

Phiên nhà máy F-17, nhánh làm việc `factory-f17` từ `origin/main` @ `acdd14d6` (đẩy lên `ccr-8f24a126-10ueok`, nhánh phiên do harness ghi).
Nguyên mẫu: `rnd-hybrid/v4/light/` (nhánh `rnd-hybrid` @ `ba5d27f8`, `v4/REPORT.md`). Việc không phải tập (CHARTER §2.3): đưa lớp ánh sáng
điện ảnh vào nhà máy **opt-in** (khoá `cine` trong `spine.json`, như `f14`), mặc định tắt. **Không chạm `ep008`, `episodes/ep007`, `checks/`.**

## 1. Giả thuyết
1. Lớp `cine` gắn được vào mọi đoạn thế giới chỉ bằng một khoá spine, không sửa scene.js của tập; không khai → khung trùng byte bản cũ;
   nháp 540p (F-15) không bật lớp.
2. Màu dữ liệu (vật `userData.checks.role` ∈ series/bar/grid) giữ nghĩa sau lớp: không vân, phản xạ ≤ 0,15, và một pass khoá màu
   (vật dữ liệu vẽ dưới ánh sáng gốc rồi ghép, không qua grade/viền tối) → ΔE2000 ≤ 5 và không đảo thứ tự sáng. Luật mới bắt được lỗi v4
   (lưới K2 kem → hồng).
3. Chỉ bật AO (nửa độ phân giải) và DOF ở cảnh khai cận → giờ máy cả lớp giảm mạnh so v4 (5–7 s/khung, 40–55 s máy/s phim với 4 worker).

## 2. Đích (không hạ sau khi đo)
| # | Thước | Đích | Vai trò |
|---|---|---|---|
| T1 | Đoạn KHÔNG khai `cine`, render bằng mã F-17 vs `main` acdd14d6 (Tập 7 đoạn a, 2 cảnh, 540p **và** 1080p) | mp4 + nhật ký **trùng byte** | **chính** |
| T2 | Đoạn khai `cine`, `--res 540` | trùng byte với cùng đoạn không khai `cine` | **chính** |
| T3 | Tất định: một cảnh có `cine` (cận, đủ lớp) dựng hai lần ở hai lượt tiến trình | trùng MD5 | **chính** |
| T4 | Luật màu (ΔE2000 trung bình theo màu dữ liệu, trước/sau lớp, mẫu mỗi cảnh): **đối chứng** lưới K2 với cấu hình v4 (không khoá màu) | **CHẶN** (ΔE > 5 hoặc đảo thứ tự sáng) | **chính** (luật phải bắt được) |
| T5 | Luật màu trên K2 đã sửa và trên 3 cảnh Tập 7 (cận, phố, dữ liệu) + đoạn 30 s | **ĐẠT** mọi mẫu | **chính** |
| T6 | Viền nhân vật (cảnh cận): độ sáng thêm do viền (L\*, viền bật − viền tắt, cùng khung) ở nửa khối **xa đèn** / nửa **gần đèn** | xa ≤ 0,5 L\* trung bình **và** ≤ 10 % của phía gần | **chính** |
| T7 | Nhân vật không khai `silhouette`: ΔE2000 màu thân trung bình trước/sau lớp | ≤ 15 (giữ màu nhận diện; v4 bóng tối × 0,05–0,07 ≈ 40+) | chỉ báo |
| T8 | Vệt DOF trên đầu (cảnh cận, dải 1–6 px trên mép đầu theo mặt nạ nhân vật): max theo cột của L\*(DOF bật) − L\*(DOF tắt) | giảm ≥ 50 % so fragment bokeh v4 trên cùng khung | **chính** |
| T9 | Mái nhỏ: mái < ngưỡng px (đường kính chiếu) không mang vân ngói | 0 mái dưới ngưỡng có vân trên các khung thử | **chính** |
| T10 | Chữ serif qua `O.text({font:'serif'})` | có trong `log.texts` + đối tượng trang kiểm (`CK.on`) với `font: 'serif'` | **chính** |
| T11 | Giờ máy/s phim, đoạn 1080p 4 worker, `cine` / không `cine` cùng đoạn | ≤ **3,0×** | **chính** |
| T12 | `verify_seg` (quy tắc 1/2/3, cắt cứng, C14, F-2) trên đoạn `cine` 1080p | không CHẶN mới so bản không `cine` | **chính** |
| T13 | Cổng gốc tắt tiếng 3 nhịp (3 cảnh), trước/sau | **chẩn đoán** (A32: thước nhiễu ±2/21) — báo, không làm trượt | chỉ báo |

**Đạt = mọi số chính đạt.** Trượt → báo số, không hạ đích; điều phối/chủ dự án quyết merge.

## 3. Điều kiện đo
- Tập 7 dựng qua thư mục thử `toolkit/factory/f17/trial/<cảnh>/` (scene.js chỉ re-export cảnh gốc + spine.json chép + khoá `cine`);
  `episodes/ep007` không sửa. Sản phẩm nặng ở `/var/tmp/f17/` và `toolkit/factory/f17/work/` (không commit).
- Đo giờ: máy rỗi (kiểm `ps`), không chạy song song; 4 worker (`CRUX_ALL_CORES=1`, máy 4 nhân), SwiftShader.
- Dừng tiến trình chỉ theo PID đã xem trong `ps` (không `pkill -f`, không `pgrep -f`).

## 4. Chống Goodhart
- Luật màu đo **trước/sau trên điểm ảnh render thật** (trang không lớp vs trang có lớp, cùng t), mặt nạ theo vật dữ liệu co 2 px; không đo trên
  tham số vật liệu. Không nới ngưỡng ΔE 5 / thứ tự sáng sau khi đo.
- Đối chứng K2 dùng đúng cấu hình v4 (hồi `dusk`, không khoá màu); không chỉnh K2 để luật bắt được.
- Không đổi đặc tả cảnh Tập 7 để qua thước.

## 5. Ngân sách
Console trần cứng **$4** cả phiên (cổng gốc 3 nhịp × 2 bản ≈ $1, REVIEWER ≈ $2). Headless khoá Console, **0 agent con** (kể cả trong headless).
Không thumbnail, không nhà cung cấp ảnh/video AI, không mô hình người tải về. Tài sản CC0 ≤ 2 MB/tệp mới commit; còn lại tải lúc dựng + SHA-256.
