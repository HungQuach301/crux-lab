# Đầu bài DỰNG C3 — Tập 7 (headless khoá Console, `toolkit/api.sh build`)

Bạn là bên dựng của kênh `crux-lab` (data-explainer tài chính cá nhân Mỹ, thế giới 3D low-poly tối giản, D-010). Làm việc trong repo `/home/user/crux-lab`, chỉ trong `episodes/ep007/` (và đọc `toolkit/`, `episodes/ep006/`). **Không sửa `toolkit/`, `checks/`, `story/script.md`, `numbers.md`.** Không git commit (phiên điều phối commit). Trả lời cuối bằng tiếng Việt, ≤ 40 dòng: tệp đã tạo, số đo, vấn đề còn mở.

## Việc
Dựng **năm đoạn thế giới 3D có lời thật, nhạc và âm dữ liệu** cho C3 Tập 7 (ý đồ: `episodes/ep007/gates/C3-root-intent.md`), một **clip duyệt** cho chủ dự án xem trên điện thoại, và **dải 6 khung tắt tiếng** cho cổng gốc. Mẫu làm theo đúng Tập 6 C3: đọc `episodes/ep006/world/c3/README.md`, `episodes/ep006/world/{c3kit.py,c3kit.js,wlib.py,obj6.js}`, một đoạn mẫu `episodes/ep006/world/c3/s07-ruth/{spine.py,scene.js}`, `episodes/ep006/world/c3/spans.json`, `toolkit/visual-library/README.md` §1 và §5, `toolkit/factory/README.md` mục "Thế giới 3D", `toolkit/factory/world/{lib3d.js,core.js,spine.py,build_seg.py}`.

Nguồn nội dung (đọc trước): `episodes/ep007/story/beats.md` (cột "muted read" và "on-screen text" của B01, B06, B21, B23, B25; mục "Colour roles"; ghi chú cuối tệp), `episodes/ep007/story/script.md` (cảnh S01, S06, S21, S23, S25 — lời là bản hiện tại), `episodes/ep007/numbers.md` + `episodes/ep007/out/model.json` (mọi số trên hình qua claim, đúng cột "Hiển thị"), `episodes/ep007/episode.yaml` (giọng).

| Đoạn (`episodes/ep007/world/c3/<đoạn>/`) | Nhịp | Cảnh lời | Hình (muted read nguyên văn ở beats.md) |
|---|---|---|---|
| `s01-stack` | B01 · KEY-1 | S01 | Tessa không mặt cạnh nhà; chồng tiền mỏng hiện cạnh nhà, mỗi nhịp thêm một bó; giá mỗi tháng phía trên. Nhãn: "Tessa · ILLUSTRATIVE" · "$120 a month" · "$320,000 loan · week of Oct 8, 2026" |
| `s06-stack` | B06 · KEY-3 | S06 | Thanh khoản 30 năm nâng lên để xong trong 15 năm, cao hơn thanh 15 năm một chút; phần dôi thành bó tiền rơi lên chồng, tháng này qua tháng khác, tới đủ chiều cao. Nhãn: "30-year paid in 15: $2,948 a month" · "+$120 a month" · "the stack: $21,622 over 15 years" |
| `s21-track` | B21 · KEY-9 | S21 | **N1 Month track** chạy từ nhà Tessa: 180 ô, rồi thêm 15 ô sáng `warn` qua mốc 15 năm; sau đó một lớp mỏng trả thêm trên khoản bắt buộc làm đường kết thúc đúng ở ô 180. Nhãn ở beats.md B21 |
| `s23-track` | B23 | S23 | N1: tiền trả thêm đến thành một khối lớn mỗi ô thứ 12 thay vì lớp mỏng; đường kết thúc muộn 4 ô. Nhãn: "$8,792 once a year" · "ends in 184 months: 4 months later" |
| `s25-bar` | B25 · KEY-10 | S25 | **the bar**: thanh ngang (W3 `Beam`, `ink-muted`) dâng cạnh nhà tới độ cao lãi khoản vay; một đô la trả thêm đặt trên nó; đô la thứ hai nhãn "any other use" **được đặt áp vào thanh để so** (KHÔNG "trèo qua/vượt qua" — chủ dự án G1 câu 1 bỏ cụm "has to clear"). Nhãn: "the bar: 7.40% a year, before taxes" · "interest no longer charged, not an investment return" · "not tested: whether any investment clears it". Không hiện lợi suất đầu tư nào |

### N1 Month track — vật thể mới (`episodes/ep007/world/obj7.js`, theo kiểu `obj6.js`)
- Một ô low-poly = **một khoản trả tháng**; ô giống hệt nhau; trái → phải = thời gian (ngữ pháp chuyển động §1). Ô thường `ink`; ô quá 180 = `warn` (trễ); mốc 15 năm (ô 180) là vạch đứng yên `ink-muted`. Lớp/khối trả thêm: chọn màu trong vai E2 (không `accent` — chỉ lãi thị trường; không `costlier` làm chữ) và ghi lý do trong README.
- Bạn được chọn bố cục đọc nhanh nhất (một hàng dài 180 ô, hoặc 15 hàng × 12 ô = 15 năm) — ghi lý do; tham số hoá (`n`, `cols`, `.set({lit, late, extra, yearly})`), `userData.checks` như `obj6.js`. Số tháng chỉ ở chế độ đồ thị (chính diện), qua claim (`months_at_pay15_now`, `months_late_at_pay15_now`, `yearly_lump_months`, `monthly_extra_months`…).
- Mỗi lần trạng thái đổi = một nốt dữ liệu (như `c3kit.py`), mật độ sfx theo F-2.

### Luật chung (D-010, visual-library §1, §5)
- Bảng màu E2, phông Inter, sàn chữ 40 px @1080, nhãn ≤ ~8 từ và ≥ 1 s / 3 từ, "US only · history, not a forecast" + ILLUSTRATIVE theo lớp bắt buộc như c3kit.js Tập 6; ≥ 5 s đầu mỗi đoạn ở chế độ thế giới; số/nhãn so sánh chỉ ở chế độ đồ thị; mỗi động tác máy có lý do + âm; nhịp kết ở trạng thái kết luận, giữ yên ≥ 1 s; quy tắc spine 2/3/7 phải OK (`spine.check_rules`).
- Mọi số trên hình đúng claim (khớp `display`); không số ngoài claim; không chữ khuyên.
- Mốc ngày: không viết "this week" ở đâu; dùng "week of Oct 8, 2026".

### Giọng (ElevenLabs, có tốn ký tự)
- Dùng `toolkit/factory/voice.py` (cache SHA-256, take commit ở `episodes/ep007/voice-takes/`), cấu hình `voice:` của `episode.yaml`, mỗi cảnh một take: **S01, S06, S21, S23, S25** (S01 phải sinh lại: S01.2 đã đổi sau bản đọc thử). Trước khi sinh: in số ký tự sẽ dùng; **trần C3 = 3.000 ký tự**, vượt thì dừng và báo. Ghi `episodes/ep007/world/c3/voice-scenes.json` (cảnh → take, duration, ký tự) và kiểm chữ take == lời kịch bản.
- Chép/sửa `wlib.py` của Tập 6 sang `episodes/ep007/world/wlib.py` (đọc voice-scenes.json của Tập 7).

### Ra
1. `episodes/ep007/world/{obj7.js,c3kit.py,c3kit.js,wlib.py,claims.json (+ derive.py nếu cần)}`, mỗi đoạn `world/c3/<đoạn>/{spine.py,scene.js,spine.json,inputs.json}`; README `world/c3/README.md` (thiết kế, lý do màu/bố cục, lệnh tái lập). Chạy `python3 toolkit/tests/comment_guard.py episodes/ep007/world` nếu có.
2. Render 540p: `python3 toolkit/factory/world/build_seg.py episodes/ep007/world/c3/<đoạn> --res 540 --out episodes/ep007/world/c3/out/<đoạn>.mp4` (cần `NODE_PATH`/vendor như README nhà máy; vendor đã `npm ci`).
3. Clip duyệt `episodes/ep007/review-c3/c3-clip.mp4` (540p, H.264 + AAC, có lời + nhạc + âm dữ liệu): năm đoạn nối theo thứ tự trên, trước mỗi đoạn một thẻ tiêu đề 1,2 s (vd "S21 · Month track"), ffmpeg; đo loudness (−14 LUFS ± 1, true peak ≤ −1 dBTP) và độ dài.
4. `episodes/ep007/world/c3/spans.json` theo mẫu Tập 6 (clip, segment, beat, scene, type, span [0,total], times = tâm 6 lát, narration, `muted_read` chép **nguyên văn** cột muted read của beats.md); rồi `python3 toolkit/blind/strips.py <clip đoạn> <spans một đoạn> episodes/ep007/review-c3/strips-r1/` cho từng đoạn (dải TẮT TIẾNG, GIỮ chữ/số).
5. Đồng bộ: `toolkit/factory/world/sync_audit.py` (nếu chạy được) — ghi số cue ±0,2 s mỗi đoạn.
6. Tự xem lại ít nhất 2 khung PNG mỗi đoạn (Read ảnh) trước khi kết thúc: chữ đè nhau, chữ cắt mép, số sai claim, khung trống → sửa.

Không chạy kiểm mù (phiên điều phối chạy). Không sửa `story/`.
