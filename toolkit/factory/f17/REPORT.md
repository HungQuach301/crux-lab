# F-17 · Báo cáo (14–15/10/2026) — lớp ánh sáng điện ảnh opt-in

Ý đồ + ngưỡng ghi trước: `INTENT.md` (commit `cdd69fe6`, trước mọi lần đo). Nhánh làm việc `factory-f17` từ `origin/main` @ `acdd14d6`, đẩy lên
`ccr-8f24a126-10ueok` (nhánh phiên do harness ghi). Nguyên mẫu: `rnd-hybrid/v4/light/` @ `ba5d27f8`. Không chạm `ep008`, `episodes/ep007`, `checks/`
(Tập 7 dựng qua thư mục thử `f17/trial/` re-export cảnh gốc; bước audio/verify chạy trong worktree ngoài repo `/var/tmp/f17/wt`, `bed.wav` sinh lại
trùng SHA bản giao `57c57cae…`).

<!--KQ-->

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

<!--CHITIET-->
