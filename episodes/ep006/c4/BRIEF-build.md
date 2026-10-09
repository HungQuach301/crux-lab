# Đầu bài agent dựng C4 Tập 6 (P3b, 09/10) — chuẩn bị animatic cả tập, KHÔNG render

Nhánh `ep006` (đã có F-12, K4.0.2, K4.1; LOCK 4d688acd). Làm trong `/home/user/crux-lab`, commit lên `ep006` (không push — phiên chính push).

## Đã sửa gì, vì sao (PLAN §4)
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| G1 b | S16, S24, S27, S29 | 7:50 < 8:00 (mid-roll) | +93 từ, 1 số mới | **8:56,6 thật** | sát trần cứng 9:00 |
| C3 r1→r2 | N1 ×4 | khuyên 8/8 (khoản đều) | séc lớn lên ×1,02^k | khuyên 1/8, nghĩa 8/8 | S29 chốt ở C4 (bản có lời) |
| P3 | F-12 | khúc đóng mất dưới −20 dB | `music.post()` +12 dB/0,5 s sau chữ cuối; ident A 3 s | −14,0 LUFS · −1,0 dBTP | đã vào `main` |

## Đọc
`toolkit/factory/README.md` (phần world, F-12) · mẫu Tập 5: `episodes/ep005/episode.yaml`, `episodes/ep005/c4/build_inputs.py`, `episodes/ep005/world/c4kit.{py,js}`, `episodes/ep005/world/c4/*/` · Tập 6: `story/script.md`, `story/beats.md` (bảng nhịp = hình phải làm), `numbers.md`, `contract.json`, `world/{c3kit.*,obj6.js,derive.py,claims.json,wlib.py}`, `world/c3/` (4 đoạn đã duyệt C3: S07, S24, S27, S29 v2 — **giữ ý hình đã duyệt**), `gates/C3-answer.md`, `gates/C3-director.md`, `gates/REVIEW-C2v3.md` PHỤ 4–6, `out/timeline-len.json`, `story/timeline_len.py`.

## Làm
1. **Cả tập là thế giới 3D** (như Tập 5): đoạn `world:` liên tiếp phủ S01–S32 (ranh giới tự chọn ở chỗ đổi hồi/ident/MR1), `world/c4kit.{py,js}` chung, `world/c4/<đoạn>/{spine.py,scene.js}`. Vật từ `lib3d.js` (W10 `Crates` + `Check` đã vào thư viện), V1/V3/V10 ở chế độ đồ thị. 8 quy tắc hình–âm (`quality-framework.md` §6b/D-010). Gen: ILLUSTRATIVE trên mọi khung có Ruth/Carl/Edna; "US only · history, not a forecast" và "CPI-U"/"US consumer prices" trên khung số lịch sử; không số tiền; không so tổng tiền nhận ("more money", "pays more", "in total" bị cấm — S19).
2. **Bài học Tập 4 (KHÔNG đăng: "hình nghèo, nhiều chữ")**: hình phải mang nghĩa và có chuyển động; chữ trên khung tối thiểu; nhãn ≤ ~8 từ, ≥ 48 px ở 1080, hiện ≥ 1 s/3 từ (luật Tập 6 từ G2 Tập 5).
3. **Hàng chờ C4**: lượt đạo diễn C3 (S24 10–19 s đứng → vật chuyển động gắn "fastest price rise"; S27 mốc năm 1949/1966/1969/1986 + màu nhấn vùng chồng; S29 nhấn ba ngày đúng "month"; các ý khác trong `C3-director.md` nếu rẻ); PHỤ-4 (thùng mờ liên tục), PHỤ-5 (trần 10 thùng).
4. **Âm (episode.md §5b)**: `audio: {lufs: -14, true_peak: -2.0, close_lift_db: 12, ident: {after: S03}}` + nhạc nền theo bản đồ căng, mỗi hồi một cue, không lặp vòng (mẫu `episodes/ep005/world/music/`); lặng 0,7–0,9 s trước ≤ 3 số neo (`anchor: true`), bỏ sfx "land" đè từ khoá neo; không tăng mật độ sfx.
5. `episode.yaml` đủ: `scope: full`, `res: 720` (C4 animatic; C5 đổi 1080), `fps: 30`, acts, scenes với tail (S03 4,0 gồm ident 3 s; S10 1,2; S12 1,5; S31 5; S32 2; còn lại 1,0), **mid-roll MR1 sau S12** (lặng ≥ 1 s, ≥ 2 phút đầu/cuối), counterweights, `world:`, `shorts:` nháp (ứng viên beats.md: B01+B07, B14–B15, B29). `c4/build_inputs.py` theo mẫu Tập 5 (gen/script, claims chưa làm tròn từ `out/model.json raw` + khoá suy ra, tokens, data).
6. `contract.json`: giữ nguyên phần `model` (đã PASS S01/S05); điền `characters` (màu/side/shape theo mã thật), `claims.core/decisive/conditions` (điều kiện "history, not a forecast", "US consumer prices"/"CPI-U"), `coverage` nếu lưới 715 ô gắn `case`.

## Ràng buộc cứng
- **Không đổi chữ kịch bản, không sinh giọng mới**: EL đã dùng 7.699/7.700 ký tự duyệt. Mọi take có sẵn ở `voice-takes/`; build phải trúng cache 30/30 cảnh, 0 ký tự EL. Lệch băm → dừng, báo.
- **Độ dài ≤ 9:00 (540,0 s) cứng**; hiện 536,6 s (dư 3,4 s). Mọi phần cộng (lặng trước số neo, hold, đuôi, sửa đồng bộ) tính vào. Vượt → rút hold/đuôi cảnh và lặng không mang nghĩa trước; KHÔNG cắt lời; vẫn vượt → dừng, báo hai phương án. **≥ 8:00** để có mid-roll.
- **Không render**: không chạy `build.sh`, `build_seg.py` render, hay Playwright dài. Chỉ: `python3 toolkit/tests/comment_guard.py episodes/ep006/world`, `spec.py`/kiểm khai, mỗi `spine.py` + `check_rules`, `numbers_said.py`, `build_inputs.py`, đo tổng timeline. Phiên chính chạy build nền.
- Không sửa `checks/`, `toolkit/` (sửa nhà máy giữa tập chỉ khi CHẶN/CHÍNH của tập — khi đó dừng và báo thay vì tự sửa).

## Trả về (≤ 25 dòng)
File đã viết; ranh giới đoạn; tổng timeline (s) và mid-roll (giây, khoảng lặng); số neo chọn; kết quả lint/spine/spec; rủi ro; **lệnh build chính xác** (gồm bước trước/sau như Tập 5); SHA commit.
