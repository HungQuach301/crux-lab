# F-17 · Báo cáo (14–15/10/2026) — lớp ánh sáng điện ảnh opt-in

Ý đồ + ngưỡng ghi trước: `INTENT.md` (commit `cdd69fe6`, trước mọi lần đo). Nhánh làm việc `factory-f17` từ `origin/main` @ `acdd14d6`, đẩy lên
`ccr-8f24a126-10ueok` (nhánh phiên do harness ghi). Nguyên mẫu: `rnd-hybrid/v4/light/` @ `ba5d27f8`. Không chạm `ep008`, `episodes/ep007`, `checks/`
(Tập 7 dựng qua thư mục thử `f17/trial/` re-export cảnh gốc; bước audio/verify chạy trong worktree ngoài repo `/var/tmp/f17/wt`, `bed.wav` sinh lại
trùng SHA bản giao `57c57cae…`).

**Kết luận: TRƯỢT** (theo INTENT §2, không hạ đích): **T11 giờ máy 5,8× > 3,0×** (đích chính) và **T6 viền: tỉ lệ xa/gần đèn 12 % > 10 %** (đích chính;
phía xa đèn 0,15 L\* ≤ 0,5 thì đạt). Mọi đích chính khác ĐẠT, gồm cả luật màu mới (đối chứng K2 v4 CHẶN, bản sửa và 3 cảnh Tập 7 ĐẠT) và verify của
đoạn 1080p có lớp. Luật màu và verify đã **bắt thật** ba lỗi của chính F-17 trong lúc thử (§3) — đã sửa, đo lại. Điều phối/chủ dự án quyết merge.

| # | Thước | Đích | Đo | Kết quả |
|---|---|---|---|---|
| T1 | không khai `cine`, mã F-17 vs `main` acdd14d6 (Tập 7 đoạn a, cảnh s1 + s4, 540p **và** 1080p) | mp4 + nhật ký trùng byte | **8/8 tệp trùng MD5** (`out/T1-T3-md5.txt`; tên tệp cache khác vì khoá gồm `core.js`/`render_shots.js` đã đổi) | **ĐẠT** |
| T2 | khai `cine`, `--res 540` | trùng byte bản không khai | test `test_factory_f17.F17Render.test_c`: mp4 + nhật ký trùng; `render.json` không có `cine`; ở 1080p thì khác (lớp chạy), nhật ký chữ vẫn trùng. Chạy 3 lượt liên tiếp đạt | **ĐẠT** |
| T3 | tất định: cảnh cận s4 (đủ lớp: AO + DOF + khoá màu) dựng 2 tiến trình | trùng MD5 | `230c544b…` cả hai (`out/T1-T3-md5.txt`) | **ĐẠT** |
| T4 | luật màu trên **đối chứng K2 cấu hình v4** (`trial/k2-v4`, `v4: true`) | CHẶN | **CHẶN**: kem `#C9C2B0` ΔE2000 **13,74**, xanh `#4C8DFF` **9,05** (`out/cine/still-k2-v4.color.json`) | **ĐẠT** |
| T5 | luật màu: K2 đã sửa + 3 cảnh Tập 7 + đoạn 30 s | ĐẠT mọi mẫu | K2 sửa ΔE max **0,26**. Đoạn a (chứa đoạn 30 s): bước `cine` của build 1080p lần 3, **24 mẫu, 89 nhóm, ΔE max 1,8**; c: 15 mẫu (3/shot) ΔE max **2,93** + 10 mẫu (2/shot) 2,94; g: 15 mẫu **0,20** + 10 mẫu 1,81; 0 đảo thứ tự sáng. (Build lần 1 và 2 của đoạn a: CHẶN/TRƯỢT — §3) | **ĐẠT** (sau sửa) |
| T6 | viền người: ΔL\* (viền bật − tắt) phía xa đèn (n·đèn ≤ 0) | ≤ 0,5 **và** ≤ 10 % phía gần | xa max **0,15** (a), 0,11 (c), 0,04 (g); gần min 1,18; **xa/gần max 0,12** (a, t = 21,8 s: 0,15 / 1,19) · chẩn đoán "lõi xa đèn" (cả ô 3×3 xa đèn — bỏ điểm mép MSAA nơi tay đè thân): **≤ 0,01** | **TRƯỢT** (tỉ lệ) |
| T7 | màu thân người ΔE2000 trước/sau (không khai silhouette) | ≤ 15 (chỉ báo) | max **16,3** (a, cảnh rộng ngày), 11,0 (c), 16,1 (g hoàng hôn); khung cận 27 s: 5,7 | chỉ báo: vượt nhẹ ở cảnh rộng |
| T8 | vệt DOF trên đầu (dải 1–6 px trên mép đầu, max theo cột ΔL\* DOF bật − tắt) | giảm ≥ 50 % so fragment v4 | **1,4 vs 11,2 L\*** (−87 %); p95 0,82 vs 6,12 (`out/cine/a.cine.json`) | **ĐẠT** |
| T9 | mái < ngưỡng px không vân | 0 mái dưới ngưỡng có vân | 0 (cơ chế mỗi khung); đếm khung-mái trơn/vân: c 8/32, g 9/55, K2 2/0 | **ĐẠT** |
| T10 | `O.text({font:'serif'})` vào nhật ký + trang kiểm | có `font: 'serif'` | test `test_d`: `log.texts[].font` và đối tượng `CK.on` mang `serif`; chữ thường không có trường | **ĐẠT** |
| T11 | giờ máy/s phim, đoạn a 1080p (54,9 s), 4 worker, cache trống | ≤ 3,0× | render: không lớp **563 s** (10,3 s máy/s phim) · có lớp **3.263 s** (59,4 s/s) = **5,8×** (build lần 1: 3.391 s = 6,0×; lần 2: 3.423 s) | **TRƯỢT** |
| T12 | `verify_seg` đoạn a 1080p có lớp | không CHẶN mới | build lần 3: quy tắc 1/2/3 = 0, cắt cứng 0, chế độ như gốc, **C14 0/1.486**, **F-2 OK** (0 nhãn đè, 0 đường cắt chữ, SNR từ khoá 16,4 dB) = y hệt bản không lớp (`out/T12-*.verify.json`) | **ĐẠT** (sau sửa; build lần 2 TRƯỢT — §3) |
| T13 | cổng gốc tắt tiếng 3 nhịp (B01, B15, B29), 2 người đọc/bản, 2 người chấm, một gói chung | chẩn đoán | có lớp **3/3 ĐẠT**; gốc 2/3 + B01 chờ người thứ 3 (0,5 · 1); 0 nhịp nêu lời khuyên (`root/tally.json`) | chẩn đoán (A32: nhiễu ±2/21) |


## 1. Đã làm
1. **`toolkit/factory/world/cine/`** (từ v4, không sửa core/lib3d/scene của tập): `cine.js` (lớp), `looks.js` (hồi, vai trò vân, `DATA_ROLES`),
   `cine.html` (trang render khi có lớp), `cine_check.js` + `cine_color.py` (luật màu mới), `assets/` (18 tệp Poly Haven CC0 ≤ 2 MB, `manifest.json`
   SHA-256, `fetch.py [--verify]`; tệp > 2 MB → `dl/` gitignore). RIGHTS **§F9**.
2. **Khoá spine `cine`** (như `f14`): `render_shots.js` chỉ mở `cine.html` khi spine có `cine` **và** res ≥ 1080 **và** khung ngang **và** không `--spp`
   (`--cine 0` ép tắt). Không khai → danh sách tệp khoá cache như cũ (khoá cache cũ không đổi, trừ việc `core.js`/`render_shots.js` đổi — §5).
   `build_seg.py`: bước `cine` (sau mux, trước verify) chỉ khi spine có `cine` và res ≥ 1080 → CHẶN dừng build.
3. **Bộ lớp mặc định khi bật:** HDRI theo hồi (+ trời, sương), vân CC0 theo màu vật liệu, bóng mềm (PCF 2048, radius theo hồi), grade + hạt tất định.
   **DOF và AO chỉ ở shot khai `shot: 'close'`**; AO nửa độ phân giải (`setSize` /2). Nháp 540p, `--spp`, Short dọc, trang kiểm `CK.on`: không bật.
4. **Khoá màu dữ liệu:** vật `checks.role` ∈ series/bar/grid (và con) không nhận vân, `envMapIntensity` ≤ 0,15; ảnh lớp **không vẽ** chúng (vẫn đổ
   bóng); `LockPass` vẽ lại chúng dưới **đèn/sương/bóng gốc** của cảnh, tone-map + sRGB trong shader (pha trộn như ra canvas), ghép **sau** OutputPass;
   grade/viền tối bỏ qua điểm ảnh đó, DOF không làm mờ chúng. Trời theo shot (`sky: 0`) cho shot có dữ liệu bán trong suốt trên nền trời.
   Luật: `cine_check.js` (trang không lớp vs có lớp, cùng t, 3 mẫu/shot; mặt nạ theo màu gốc, co 2 px, ≥ 200 điểm) → `cine_color.py`: **ΔE2000 > 5 hoặc
   đảo thứ tự L\* (|ΔL\*| ≥ 1 trước, ≥ 0,5 sau, đổi dấu) = CHẶN**.
5. **Nhân vật:** chỉ Person của lib3d (thân viên nang + đầu cầu cùng vật liệu); giữ màu nhận diện, viền = Fresnel × max(0, n·đèn) (phía xa đèn = 0, v4 sàn
   0,15); thân sẫm chỉ khi shot khai `silhouette: true`.
6. **Giới hạn v4 đã sửa:** DOF nới độ sâu 3×3 trước khi gom mẫu (hết vệt mép MSAA trên đầu); mái < `roof.minPx` (260 px ở 1080, đường kính cầu bao chiếu)
   dùng vật liệu trơn; `O.text(…, {font: 'serif'})` (vào `log.texts[].font` và đối tượng trang kiểm).
7. `toolkit/blind/headless.sh`: thêm `--disallowedTools Task,Agent,Workflow` và trần chi mỗi lượt opt-in `CRUX_HEADLESS_CAP_USD`.
8. Test `toolkit/tests/test_factory_f17.py`.

## 2. Giờ máy (T11) — đâu là chỗ đắt
Một khung 1080p, một trang, máy rỗi (`measure_layers.js`, đoạn a t = 12 s, shot rộng không AO/DOF; `out/T11-layers-a-t12.jsonl`):

| cấu hình | không lớp | đủ lớp | − khoá màu | − HDRI | − grade | − bóng mềm | − vân | − viền |
|---|---|---|---|---|---|---|---|---|
| ms/khung | 319 | 1.854 | 1.292 | 1.470 | 1.500 | 1.668 | 1.727 | 1.750 |
| chi phí lớp (đủ − bỏ lớp) | | | **+562** | +384 | +355 | +187 | +127 | +105 |

- Pass khoá màu đắt nhất: vẽ lại cả cảnh (vật khác chỉ ghi độ sâu) **và tính lại bản đồ bóng 2048** với đèn gốc. Chỉ bật khi có vật dữ liệu hiện.
- Grade + hạt và OutputPass/ghép là các pass toàn khung riêng; với SwiftShader mỗi pass 1080p ≈ 0,1–0,3 s.
- Với 4 worker trên 4 nhân, mỗi khung đủ lớp ≈ 7,9 s/worker (khung một trang 1,85 s): SwiftShader đa luồng nên song song không cộng tuyến tính.
- Cảnh cận (AO nửa độ phân giải + DOF) đắt hơn nữa: s4 147 s/s phim với 1 worker.
- Hướng giảm (chưa làm, không đổi đích): gộp OutputPass + khoá + grade thành một pass; pass khoá dùng lại bản đồ bóng (đèn gốc chỉ khác vị trí); nửa
  độ phân giải cho HDRI PMREM; bỏ khoá màu ở shot không có dữ liệu bán trong suốt (vật dữ liệu đục có thể khoá bằng vật liệu). Ước: ≈ 3–3,5×.
- So v4 (REPORT v4: 40–55 s máy/s phim với 4 worker, ước tính từ khung một trang): F-17 đo **thật** trên cả đoạn 59,4 s/s — AO/DOF chỉ ở shot cận
  nhưng thêm pass khoá màu; ước v4 lấy khung một trang × 30 / 4 nên thấp hơn thực tế.
- **Một tập 10 phút có lớp ≈ 10 giờ máy render** (4 nhân) so với ≈ 1,7 giờ không lớp.

## 3. Luật màu và verify bắt lỗi của chính F-17 (đã sửa, đo lại)
1. **Vật dữ liệu bán trong suốt vẽ hai lần** (lượt đo 1, cảnh c t = 26,4 s: đường lãi mờ dần ΔE 15–18, đảo thứ tự sáng) → ảnh lớp không vẽ vật dữ liệu.
2. **Pha trộn ở không gian tuyến tính** trong composer vs không gian sRGB đã tone-map trên canvas (cùng chỗ, sau sửa 1 còn ΔE 15,6) → `LockPass`
   vẽ như ra canvas (cờ `isXRRenderTarget` trên RT riêng: three tone-map + mã sRGB trong shader), ghép sau OutputPass. Đo lại: ΔE max 2,94.
3. **Chồng tiền của Leo mang `checks.char`** nên bị gắn viền như người (lượt đo đầu cảnh g) → chỉ Person (viên nang + cầu cùng vật liệu).
4. **Build 1080p lần 1 (đoạn a): bước `cine` CHẶN** ở mẫu mới (3/shot): t = 24,1 s dải tuần tối 8 % (pass khoá dùng tham số bóng mềm — bias/normalBias/radius —
   thay vì bóng gốc) và t = 26,2 s (cận) dải tuần **bán trong suốt trên nền trời HDRI** đọc sáng hơn (ΔE 6,6–6,9). Sửa: khôi phục tham số bóng gốc trong
   pass khoá; tắt trời ở shot có dữ liệu trong suốt trên nền trời.
5. **Build lần 2: verify TRƯỢT — 2 cắt cứng (19,93 s, 28,53 s)**: tắt/bật trời theo shot làm nền đổi đột ngột. Sửa: đoạn a tắt trời **cả đoạn** (`sky: 0`,
   như đoạn dữ liệu c); README/`cine.js` ghi: khai trời ở mức đoạn, khoá theo shot chỉ khi shot mở/đóng bằng chuyển cảnh. Build lần 3: mọi bước ĐẠT.
Hệ quả thiết kế: **dữ liệu bán trong suốt + trời HDRI** không đi cùng nhau dưới luật màu; đoạn có dải tuần (a) và đoạn dữ liệu (c) chạy không trời.

## 4. Thử trên Tập 7
- **3 cảnh v4** (cận Tessa 27 s, dữ liệu 85 s, phố 3 s) dựng lại 1080p trước/sau: `out/SHEET-before-after.jpg` (dòng 1: cận — bản tờ dựng **trước** sửa
  trời, cận còn trời mờ DOF; bản cuối của đoạn a không trời). Số từng ảnh: `out/cine/still-*.color.json` (đều ĐẠT, ΔE ≤ 1,83).
- **Đoạn 30 s 1080p trước/sau**: cắt 15–45 s của đoạn a dựng đủ bước (`build_seg`, verify đạt) — `clip30-a-ctl.mp4` / `clip30-a.mp4` ở `/var/tmp/f17/out/`
  (không commit video; SHA-256 ở `out/clip30.sha256`, kèm hai bản đoạn đầy đủ).
- **V11**: luật trang của checks không chạy (cần dựng cả tập + bộ lấy mẫu trang ≈ 6 h). Trang kiểm `CK.on` **không bật lớp** nên lớp `glyph`/`graphics`
  mà V11 đo không đổi theo cấu tạo; phần "nhãn đè" của A19 = V11 trong F-2 của verify_seg: 0 nhãn đè, 0 đường cắt chữ ở cả hai bản. **Rủi ro chưa đo:**
  V12 so chữ trên khung video với trang sạch — nền sau chữ có tấm nền mờ khác giữa trang (không lớp) và video (có lớp) → cần một lượt checks đủ bộ
  trước khi dùng cho tập thật.
- **Cổng gốc 3 cảnh** (chẩn đoán): dải 6 khung 1080p **render thật** (không cắt từ video) ở đúng thời điểm của `strips.py`; B01 (S01, đoạn a — cảnh cận
  27 s thuộc S02, nhịp không có "muted read"), B15 (S15, đoạn c), B29 (S29, đoạn g). Có lớp 3/3; gốc 2/3 + 1 chờ. Một lượt, hai người đọc: không đủ để
  nói lớp giúp hiểu (A32).

## 5. Giới hạn, phát hiện
1. **Khoá cache render đổi một lần cho mọi đoạn** (`core.js` thêm serif, `render_shots.js` thêm khoá `cine`) — đoạn của tập đang làm dựng lại một lần;
   khung không đổi (T1). Ep008 không bị chạm trong phiên này nhưng sẽ dựng lại khi lấy main mới.
2. **Màu dữ liệu được khoá bằng cách vẽ chúng dưới ánh sáng studio gốc**: vật dữ liệu không nhận ánh sáng hồi (không ấm lên lúc hoàng hôn, không bóng mềm
   lên chính nó, DOF không làm mờ). Trên nền đã lên đèn, ô kem có thể **trông** xám (tương phản đồng thời, K2) dù ΔE = 0,26 — luật đo màu tuyệt đối,
   không đo cảm nhận.
3. **Luật màu chỉ đo vai trò series/bar/grid** như lệnh. Ở Tập 7 nhiều vật mang dữ liệu khai `role: 'mark'` có `series` (track, thẻ) — không được khoá,
   không được đo.
4. Luật tự chấm một phần: cơ chế khoá và thước cùng định nghĩa "trước" = cảnh dưới đèn gốc. Luật **không** đảm bảo màu cảm nhận, chỉ đảm bảo điểm ảnh
   dữ liệu (lõi, co 2 px) giữ màu trước lớp; mép, nhóm < 200 điểm ảnh và vật mờ dần < 0,5 không đo.
5. Viền người (T6): phần sáng phía xa đèn là điểm mép MSAA nơi viền của tay (phía gần đèn) pha vào thân; theo thước gốc vẫn là TRƯỢT.
6. Short dọc và trang kiểm không có lớp: Short từ đoạn có lớp sẽ khác hình bản ngang.
7. Chữ serif dùng phông hệ thống (DejaVu Serif của container); không đóng gói phông.
8. `isXRRenderTarget` là cờ nội bộ của three (0.186.1) để ép tone-map trong RT; nâng three phải kiểm lại.
9. Cảnh thử của test thiếu `await fonts()` → không tất định (2 kết quả luân phiên, cả khi không khai cine) — sửa trong test, ghi lại vì cùng họ lỗi
   "render phụ thuộc lịch sử trang" của F-15 §5.2.

## 6. Chi và token
Console (headless khoá Console, 0 agent con — `headless.sh --tools Read|"" --disallowedTools Task,Agent,Workflow`): cổng gốc 12 đọc + 2 chấm
**$0,41**; REVIEWER: §7. Sổ chi `spend.json`, trần cứng $4. Không gọi API nào khác (0 ký tự EL, không ảnh/video AI, không mô hình người tải về).

<!--REVIEWER-->

