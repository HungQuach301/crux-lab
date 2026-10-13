// Tập 7 · C4 · ĐOẠN E = S21–S24. N1 Month track BẢN C4 (c4kit.TrackC4): vách 15 năm làm đích → 180 ô đặt tới vách → (3/4) 14,6 ô trễ quá vách →
// mỗi tháng MỘT TỜ ĐÔ LA (nhỏ hơn ô) từ tay Tessa đặt lên mặt ô, ô bắt buộc giữ ink-muted quanh tờ, ô trễ rút hết → đường xong đúng ô 180 → bóng lịch
// 30 năm rút về vách, thanh mức bắt buộc đứng yên, một khoản bắt buộc tách lãi/gốc (lãi co lại) → một tờ nhấc lên (tháng khó, đường lui còn) → tờ nằm
// yên; mỗi năm 12 tờ nhấc theo thứ tự, gom thành MỘT XẤP hạ xuống ô 12N, 11 ô giữa tối hẳn → đẩy vào vách: 4 ô trễ → chồng lãi nhỏ + khay tài khoản 12
// tờ (đối trọng S24.2) → tờ đô la từ tay Tessa.
// C5 (bố cục/nhịp, không đổi loại hình): đường tháng mọc từ cửa nhà (S21); thanh mức ngang trên khối dư nợ hạ bậc, giữ tới "fallback" (S22); thanh hai
// phần sang phải vách, lãi TRK.dark / gốc ink, khe màu nền ở chỗ nối (S22.2); cột đầu gom chậm (S23); lãi nhỏ giọt khi xấp đầu chờ, hũ kính cạnh Tessa, tờ đô la rời tay vào nhà (S24).
// Mốc giờ chỉ từ spine.json.
import { setup, figure, gesture, nameTag, TrackC4, SplitBar, TRK, BUNDLE_TH, modeLook, followLight, chrome, SRC_SIM, label, seg2, dip,
  kf, show, pulse, C, ease, lin, mix, THREE, setOpacity } from '/episodes/ep007/world/c4kit.js';
import { TRACK_POSES } from '/episodes/ep007/world/c3kit.js';
import { Stack } from '/toolkit/factory/world/lib3d.js';
import { Bill } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c4/e-s21-s24/';

export async function boot(res) {
  // cQ: góc 3/4 (~40°) trước lưới — KHÔNG nhìn thẳng xuống lúc tấm trả thêm phủ (thấy cạnh tấm); vách thấp + trong mờ không che ô trễ;
  // Tessa, khoản bắt buộc tách hai phần (S22.2) và chồng lãi nhỏ (S24) đều trong khung
  // cW: đẩy vào vách + ô trễ của S23.3 (chồng lãi S24.1 cũng trong khung)
  const poses = { ...TRACK_POSES, cQ: { pos: [2.2, 5.4, 5.9], tgt: [2.5, 0.3, -1.9], fov: 52, chart: 1 },
    cW: { pos: [6.1, 3.0, 3.2], tgt: [6.4, 0.1, -1.3], fov: 40, chart: 1 } };
  const { S, D, G, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue, X = S.x;
  const hm = figure(scene, { x: X.house[0], z: X.house[1], side: 1 }); hm.person.position.set(X.tessa[0], 0, X.tessa[1]);
  const track = TrackC4({ name: 'tessa' }); scene.add(track); const T = track.userData;
  // S22.1: thanh mức khoản bắt buộc (ink-muted, vật cố định) dọc mép trước 15 cột
  const rail = new THREE.Mesh(new THREE.BoxGeometry(1, 0.05, 0.06), new THREE.MeshStandardMaterial({ color: TRK.req, emissive: new THREE.Color(TRK.req), emissiveIntensity: 0.5, transparent: true }));
  // C5 CHÍNH: thanh nằm NGANG ở cao RY, TRÊN khối dư nợ hạ bậc (15 khối, cao BALH × dư nợ đầu năm / gốc, màu tường nhà = khoản vay) trước mép trước
  const RY = 0.62, BALH = 0.5, RZ = track.frontZ() + 0.33;
  rail.geometry.translate(0.5, 0, 0); rail.position.set(0, RY, RZ); scene.add(rail); rail.userData.checks = { role: 'mark', key: 'required-level' };
  const balk = new THREE.InstancedMesh(new THREE.BoxGeometry(T.tile, 1, 0.14).translate(0, 0.5, 0), new THREE.MeshStandardMaterial({ color: '#D9D4C7', roughness: 0.8, emissive: new THREE.Color('#D9D4C7'), emissiveIntensity: 0.12, transparent: true }), 15);
  balk.castShadow = true; balk.frustumCulled = false; scene.add(balk); balk.userData.checks = { role: 'bar', series: 'balance', key: 'balance-steps' };
  // C5 CHÍNH (S21 2,5 s): đường tháng mọc từ cửa nhà ("shortcut") dọc hàng ô 3 tới vách — nằm dưới ô khi ô đặt, tắt khi sang đồ thị
  const lane = new THREE.Mesh(new THREE.BoxGeometry(1, 0.012, 0.16), new THREE.MeshStandardMaterial({ color: TRK.req, emissive: new THREE.Color(TRK.req), emissiveIntensity: 0.6, transparent: true }));
  lane.geometry.translate(0.5, 0, 0); lane.position.set(X.house[0], 0.006, -2 * T.pitch); scene.add(lane); lane.userData.checks = { role: 'mark', key: 'track-lane' };
  const bar = SplitBar({ x: X.bar[0], z: X.bar[1], h: 2.0 }); scene.add(bar);
  // C5 CHÍNH: lãi (co lại) giữ TRK.dark của kit (không màu vai trò; xanh tiền gần cushion → bỏ), gốc (giãn ra) ink; KHE màu nền rộng hơn thanh ở chỗ nối → hai phần tách bạch
  const seam = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.035, 0.45), new THREE.MeshStandardMaterial({ color: C.bg, roughness: 0.9, transparent: true })); bar.add(seam);
  // S24.1: chồng lãi nhỏ (bó màu tiền — không phải warn: warn = giá của đường lui)
  const ist = Stack({ unitUsd: G.bundle_usd / BUNDLE_TH, bundleUsd: G.bundle_usd, w: 0.9, d: 0.6, maxUsd: 9000 }); ist.position.set(X.istack[0], 0, X.istack[1]); scene.add(ist);
  ist.userData.checks = { role: 'bar', series: 'yearly-extra-interest', key: 'yearly-extra-interest' };
  const IUSD = 8166;   // yearly_vs_monthly_interest (độ cao vật; nhãn qua claim)
  // C5 CHÍNH (S24.1 "sits longer"): một tờ lãi (Bill) nhỏ giọt rơi vào chồng ở mỗi giọt S.drip_t, chồng dâng theo bậc S.drip
  const drop1 = Bill({ name: 'interest-drip' }); drop1.scale.setScalar(0.8); scene.add(drop1);
  // S21.3 (C4 r2 — khoá nghĩa ở r4: cận cảnh tờ to của r3 hạ B21 → bỏ): phần trả thêm của mỗi tháng = MỘT TỜ ĐÔ LA (Bill của obj7, vật tiền của
  // S24.3/S25, sáng hơn chút) NHỎ HƠN Ô (62 % × 41 % cạnh ô) nằm TRÊN mặt ô; ô bắt buộc giữ ink-muted và thấy quanh tờ ở mọi khung (tấm của kit tắt:
  // drop = 0). Tờ rời tay Tessa, qua mép trước cột đầu rồi rải vào từng cột-năm (chạm ở land[c], một nốt mỗi cột).
  // S23 (C4 r3): 12 tờ của năm nhấc theo thứ tự (sau → trước), gom thành xấp có khe (BLP) lơ lửng ngay trên ô 12 rồi HẠ xuống ô 12; 11 ô giữa tối hẳn
  const BS = new THREE.Vector3(0.34, 1.8, 0.5), BH = 0.02 * BS.y, BLP = BH + 0.04, HOV = 0.3;
  const glowBill = (g) => { g.traverse((m) => { if (m.isMesh) { m.material = m.material.clone(); m.material.emissive = m.material.color.clone().lerp(new THREE.Color('#FFFFFF'), 0.3); m.material.emissiveIntensity = 0.7; } }); return g; };
  const proto = glowBill(Bill({ name: 'extra-month' })), bills = proto.children.map((p) => {
    const im = new THREE.InstancedMesh(p.geometry.clone().translate(p.position.x, p.position.y, p.position.z), p.material, T.n);
    im.castShadow = im.receiveShadow = true; im.frustumCulled = false; scene.add(im); return im; });
  bills[0].userData.checks = { role: 'mark', series: 'tessa', key: 'track-tessa-extra-bills' };
  // S24.2: "tài khoản" của Tessa — C5 CHÍNH: khay → HŨ KÍNH (vách trong mờ cao JH) cạnh cô, thu JS (không đè người, trên tên); 12 tờ chờ tới kỳ trả năm
  const JS = 0.7, JH = 1.3;
  const tray = new THREE.Group(), trayBox = new THREE.Mesh(new THREE.BoxGeometry(0.9, JH, 0.62), new THREE.MeshStandardMaterial({ color: TRK.req, transparent: true, opacity: 0.2, depthWrite: false }));
  trayBox.position.y = JH / 2; tray.add(trayBox);
  for (let k = 0; k < 12; k++) { const s = glowBill(Bill({ name: 'account' })); s.scale.set(1, 2, 1); s.position.set(0, 0.06 + k * 0.085, 0); tray.add(s); }
  tray.scale.setScalar(JS); tray.position.set(X.tray[0], 0, X.tray[1]); scene.add(tray); tray.userData.checks = { role: 'mark', key: 'account-tray' };
  const bill = Bill({ name: 'extra-dollar' }); scene.add(bill);
  // dest (C5 CHÍNH): cửa nhà (mặt trước, House w 1,6 → sâu 1,15); HV: đầu bàn tay Tessa (cánh tay viên nang dài 0,39 h dưới khớp vai)
  const hand = [X.tessa[0] + 0.35, 0.7, X.tessa[1] + 0.2], dest = [X.house[0], 0.28, X.house[1] + 0.6], HV = new THREE.Vector3(), H0 = new THREE.Vector3();
  const lay = S.lay, land = S.land, NC = 15;
  const cl = (x) => Math.min(1, Math.max(0, x)), sm = (u) => u * u * (3 - 2 * u);
  const dep = (c) => land[0] - S.drop + 0.07 * c, via = [track.colX(0, -1) - 0.25, 0.95], zEnd = track.tileAt(T.cols - 1)[2];
  const blockTop = (c) => { const [x, y, z] = track.tileAt(c * T.cols + T.cols - 1); return [x, y + T.cols * BLP, z]; };
  const BM = new THREE.Matrix4(), BQ = new THREE.Quaternion(), BE = new THREE.Euler(), BP = new THREE.Vector3(), HIDE = new THREE.Matrix4().makeScale(0, 0, 0);
  // tờ tháng i: bay (Bezier tay → mép trước cột đầu → ô) rồi nằm trên ô; gathered(c), bob(i), lift = {i, a}
  function setBills(t, gathered, bob, lift) {
    for (let i = 0; i < T.n; i++) {
      const c = Math.floor(i / T.cols), r = i % T.cols, t0 = dep(c);
      if (t < t0) { for (const m of bills) m.setMatrixAt(i, HIDE); continue; }
      const [x, yt, z] = track.tileAt(i), yR = yt + BH / 2 + 0.004, u = sm(lin(t, t0, land[c]));
      if (u < 1) {
        const v = 1 - u, zm = mix(hand[2], z, 0.5);
        BP.set(v * v * hand[0] + 2 * v * u * via[0] + u * u * x, v * v * hand[1] + 2 * v * u * via[1] + u * u * yR, v * v * hand[2] + 2 * v * u * zm + u * u * z);
        BE.set(0.95 * v, 0.25 * Math.sin(Math.PI * u), 0);
      } else {
        // gom: tờ k (k = 0 ở ô 12, đáy xấp) nhấc ở dl(k), bay tới chỗ của nó trong xấp lơ lửng HOV trên ô 12; cả xấp hạ ở 0,8–1
        const g = gathered(c), k = T.cols - 1 - r, e = sm(cl((g - 0.5 * k / (T.cols - 1)) / 0.3)), dn = sm(cl((g - 0.8) / 0.2)), y1 = yt + 0.004 + k * BLP + BH / 2;
        BP.set(x, yR + (y1 + HOV * (1 - dn) - yR) * e + 0.12 * Math.sin(Math.PI * e) + bob(i) + (lift.i === i ? 1.1 * lift.a : 0), z + (zEnd - z) * e); BE.set(0, 0, 0);
      }
      BM.compose(BP, BQ.setFromEuler(BE), BS); for (const m of bills) m.setMatrixAt(i, BM);
    }
    for (const m of bills) m.instanceMatrix.needsUpdate = true;
  }

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw); gesture(hm, t, S.gestures);
    const late = t < S.clear_t ? kf(S.late21, t) : kf(S.late23, t);
    const curM = Math.min(179, Math.max(0, Math.floor(179 * lin(t, S.cursor[0], S.cursor[1])))), curOn = t > S.cursor[0] - 0.05 && t < S.cursor[1] + 0.4 ? 1 : 0;
    const gc = 15 * ease(t, b.b0.requires - 0.05, b.b0.requires + 1.2) * (1 - ease(t, b.b0.sooner - 0.05, b.b0.sooner + 0.6));
    const gathered = (c) => ease(t, S.gather[c][0], S.gather[c][1]),
      // S24.1 (C5 CHÍNH): xấp năm đầu (tờ 0–11) CHỜ — nhấc 0,16 từ "about", nảy nhẹ mỗi giọt lãi, hạ xuống ô ở "arrives"
      wait = ease(t, b.b6.about, b.b6.about + 0.5) * (1 - ease(t, S.arrives, S.arrives + 0.35)), dripP = S.drip_t.reduce((s, d) => s + pulse(t, d, 0.45), 0),
      // sóng S23 "mỗi tháng một tờ": gợn rất thấp (0,03) — tờ vẫn đọc là nằm trên ô, không lơ lửng (đạo diễn lượt 3)
      bob = (i) => { const u = (t - (S.wave[0] + (S.wave[1] - S.wave[0] - 0.3) * i / 179)) / 0.3; return (u > 0 && u < 1 ? 0.03 * Math.sin(Math.PI * u) : 0) + (i < 12 ? wait * (0.16 + 0.04 * dripP) : 0); },
      lift = { i: S.lift.i, a: ease(t, S.lift.t[0] - 0.05, S.lift.t[0] + 0.45) * (1 - ease(t, S.lift.t[1], S.lift.t[1] + 0.5)) };
    setBills(t, gathered, bob, lift);
    // ô bắt buộc: ink-muted suốt S21–S22 (C4 r2), tối hẳn khi năm đã gom (S23, C4 r3: 11 ô không trả thêm); không tấm kit (drop = 0); loé "required" nhẹ (0,3)
    const cover = (c) => 0.95 * cl((gathered(c) - 0.8) / 0.2);
    track.set({ lit: kf(S.lit, t), late, cover, drop: 0,
      // C5: cột đầu loé khi 12 tờ trượt vào xấp (S23 "once"); cột đầu loé theo mỗi giọt lãi + "arrives" (S24.1, ô dưới xấp đang chờ)
      flash: (c) => Math.min(1, pulse(t, lay[c] + 0.2, 0.6) + 0.3 * pulse(t, b.a2.required, 0.9) + curOn * (Math.floor(curM / 12) === c ? 0.7 : 0) + (c === 9 ? pulse(t, b.b2.later, 1.2) : 0)
        + (c === 0 ? 0.6 * Math.sin(Math.PI * gathered(0)) + 0.35 * wait * dripP + pulse(t, S.arrives, 0.8) : 0)),
      ghost: gc, ghostA: gc > 0.01 ? 1 : 0,
      // vách hiện mờ (0,45) khi đường tháng từ cửa nhà chạm tới (C5), rõ ở "pay" như cũ
      markA: Math.max(0.45 * ease(t, S.lane[1] - 0.2, S.lane[1] + 0.3), ease(t, S.mark_t - 0.05, S.mark_t + 0.5)) * (0.75 + 0.6 * pulse(t, b.a0.same, 1.0)) * (1 + 0.5 * pulse(t, b.b0.sooner, 1.0)),
      pulse: show(t, b.a1.late) * (1 - show(t, b.a1.late + 0.6)) + show(t, b.b5.four) * (1 - show(t, b.b5.four + 0.6)) });
    // S22.1 (C5 CHÍNH): thanh mức + khối dư nợ mọc theo cột từ "requires"; GIỮ qua lúc về thế giới (S22.3), sáng ở "fallback", tắt khi sang S23
    const rG = lin(t, b.b0.requires, b.b0.requires + 0.8), rA = ease(t, b.b0.requires - 0.05, b.b0.requires + 0.6) * (1 - ease(t, MV.m_c23.t0, MV.m_c23.t0 + 0.4));
    rail.scale.x = Math.max(0.001, T.markX * rG); rail.visible = rA > 0.01; rail.material.opacity = rA;
    rail.material.emissiveIntensity = 0.5 + 1.0 * pulse(t, b.b0.stays, 1.0) + 1.6 * pulse(t, S.fallback, 1.4);
    for (let c = 0; c < 15; c++) { const g = sm(cl((rG * 15 - c) / 1.0)); BM.makeScale(1, Math.max(0.001, BALH * S.bal[c] * g), 1).setPosition(track.colX(c), 0, RZ); balk.setMatrixAt(c, g > 0.002 ? BM : HIDE); }
    balk.instanceMatrix.needsUpdate = true; balk.material.opacity = 0.9 * rA; balk.visible = rA > 0.01;
    const lA = ease(t, S.lane[0] - 0.05, S.lane[0] + 0.3) * (1 - ease(t, MV.m_c21.t0, MV.m_c21.t0 + 0.6));
    lane.scale.x = Math.max(0.001, (T.markX - X.house[0]) * sm(lin(t, S.lane[0], S.lane[1]))); lane.material.opacity = 0.85 * lA; lane.visible = lA > 0.01;
    const bA = show(t, b.b1.cut) * (1 - ease(t, MV.m_w22.t0, MV.m_w22.t0 + 0.4));
    bar.set({ share: S.share[curM], a: bA }); bar.visible = bA > 0.01; seam.position.y = bar.h * S.share[curM];
    bar.children[1].material.emissiveIntensity = 0.35 + 0.8 * pulse(t, b.b1.principal, 1.0) + 0.4 * pulse(t, b.b1.fixed, 0.8);
    // S24.1 (C5 CHÍNH): chồng lãi dâng 40 % ở "charges" rồi nhỏ giọt 10 bậc tới "arrives"; tờ lãi rơi 0,35 s vào đỉnh chồng trước mỗi giọt
    const iA = 1 - ease(t, MV.m_w24.t0, MV.m_w24.t0 + 0.5), iLev = kf(S.drip, t);
    ist.set({ usd: IUSD * iLev * iA });
    { const k = S.drip_t.findIndex((d) => t >= d - 0.35 && t < d), top = IUSD * iLev / G.bundle_usd * BUNDLE_TH;
      drop1.visible = k >= 0 && iA > 0.5;
      if (drop1.visible) { const v = sm(cl((t - S.drip_t[k] + 0.35) / 0.35)); drop1.position.set(X.istack[0], top + 0.03 + 0.9 * (1 - v), X.istack[1]); drop1.rotation.set(0, 0.4 * k, 0.25 * (1 - v)); } }
    const tA = show(t, b.b7.account) * (1 - ease(t, MV.m_w24.t0, MV.m_w24.t0 + 0.5));
    setOpacity(tray, tA); trayBox.material.opacity = 0.2 * tA; trayBox.material.depthWrite = false; tray.visible = tA > 0.01;
    // S24.3 (C5 CHÍNH): tờ đô la hiện TRONG TAY Tessa ("Tessa", theo đầu bàn tay), rời tay ở "puts", bay vòng (Bezier qua đỉnh) vào cửa nhà tới "mortgage"
    hm.person.updateMatrixWorld(true); hm.pivot.localToWorld(HV.set(0, -0.39 * hm.h, 0));
    const [f0, f1, f2] = S.fly, a1 = show(t, f0) * (1 - ease(t, f2 - 0.25, f2)), u = sm(cl((t - f1) / (f2 - f1)));
    bill.visible = a1 > 0.01; bill.scale.setScalar(Math.max(0.001, a1 * (1 - 0.6 * u)));
    bill.rotation.set(Math.PI / 2 * (0.35 * (1 - u)), 0.3 * Math.sin(1.7 * t) * (1 - u), 0.6 * Math.sin(Math.PI * u));
    // tay giữ giơ tới sau "mortgage" (gesture hold 2,2) → đầu bàn tay đứng yên suốt chuyến bay: điểm rời tay = HV (không trạng thái giữa các khung)
    H0.copy(HV);
    { const v = 1 - u, cx = mix(H0.x, dest[0], 0.5), cy = Math.max(H0.y, dest[1]) + 1.0, cz = mix(H0.z, dest[2], 0.5);
      bill.position.set(v * v * H0.x + 2 * v * u * cx + u * u * dest[0], v * v * H0.y + 2 * v * u * cy + u * u * dest[1], v * v * H0.z + 2 * v * u * cz + u * u * dest[2]); }
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 1 - ease(t, 0, 0.4));
    // tên Tessa hạ thấp ở chế độ đồ thị: không chạm mép trước-trái của lưới (đạo diễn lượt 3); ẩn như figTag khi người ra khỏi khung
    { const [px] = O.toScreen(hm.person.position.x, 0.5, hm.person.position.z); nameTag(O, hm, Math.min(1, Math.max(0, Math.min(px - 40, 1880 - px) / 80)), { dx: -32 * cw, dy: 70 * cw }); }
    const sc = (x, y, z = 0) => O.toScreen(x, y, z);
    const [gx0, gy0] = sc(track.colX(0, -1), T.th, track.backZ()), [gx1, gy1] = sc(track.colX(T.years + 1, 1), T.th, track.frontZ());
    const [fx0, fy0] = sc(track.colX(0, -1), T.th, track.frontZ()), [mx, my] = sc(track.markWorldX(), 0, track.frontZ()), [mbx, mby] = sc(track.markWorldX(), 0.18, track.backZ());
    const grid = [Math.min(gx0, fx0), Math.min(gy0, mby) - 20, Math.max(gx1, mx), Math.max(fy0, gy1)];
    log.roi['a0.pay'] = grid; log.roi['a0.same'] = [Math.min(mx, mbx) - 30, mby - 30, Math.max(mx, mbx) + 30, my + 10];
    const [lx, ly] = sc(...track.tileAt(T.n)), [lx2] = sc(...track.tileAt(T.n + 12));
    log.roi['a1.doesnt'] = [lx - 60, ly - 60, lx2 + 60, ly + 260];
    // S21.2: hai nhãn của trạng thái "trễ" (tắt khi tấm trả thêm bắt đầu rơi)
    const old = b.a2.finish - 0.05;
    label(O, `pay ${D('pay15_now')} on the ${D('term_long')}: ${D('months_at_pay15_now')}`, 960, 205, { align: 'center', kind: 'number', alpha: ok * show(t, b.a1.ends, old),
      claims: ['pay15_now', 'term_long', 'months_at_pay15_now'] });
    log.roi['a1.ends'] = [300, 150, 1620, 230];
    // "about 15 months late" (mới ở C4): trên NỀN TỐI đặc, phía trên đầu sau của vách (không đè ô amber); tắt khi ô trễ bắt đầu rút
    { const lx3 = Math.min(1530, Math.max(400, mbx)), ly3 = mby - 70;
      label(O, D('months_late_at_pay15_now'), lx3, ly3, { align: 'center', kind: 'number', color: C.warn, plateA: 0.95, alpha: ok * show(t, b.a1.late, land[0] - 0.1), claims: ['months_late_at_pay15_now'] });
      log.roi['a1.late'] = [lx3 - 300, ly3 - 50, lx3 + 300, ly3 + 20]; }
    // S21.3: tờ tiền từ tay Tessa tới cột đầu; nhãn hai dòng chỉ hiện khi không còn ô trễ nào
    { const [hx, hy] = sc(...hand); log.roi['a2.finish'] = [Math.min(hx, fx0) - 40, Math.min(hy, gy0) - 60, sc(track.colX(1, 1), 0, track.frontZ())[0] + 10, Math.max(hy, fy0) + 10]; }
    log.roi['a2.required'] = grid;
    const s7 = ok * show(t, b.a2.seven, b.b0.requires - 0.1) * (late <= 0 ? 1 : 0);
    label(O, `to finish in ${D('monthly_extra_months')}:`, 960, 205, { align: 'center', kind: 'number', alpha: s7, claims: ['monthly_extra_months'] });
    label(O, `${D('extra_month_about')} extra on top of the ${D('pay30_amt')} required`, 960, 268, { align: 'center', kind: 'number', alpha: s7, claims: ['extra_month_about', 'pay30_amt'] });
    log.roi['a2.seven'] = [300, 150, 1620, 290];
    // S22.1
    const w22 = MV.m_w22.t0 - 0.05;
    label(O, `required payment: stays ${D('pay30_amt')}`, 1120, 872, { align: 'center', kind: 'number', alpha: ok * show(t, b.b0.stays, w22), claims: ['pay30_amt'] });
    { const [r0x, r0y] = sc(0, RY, RZ), [r1x, r1y] = sc(T.markX, RY, RZ), [, b0y] = sc(0, 0, RZ);
      log.roi['b0.requires'] = [r0x, Math.min(r0y, r1y) - 30, sc(track.colX(29, 1), 0, 0)[0], b0y + 10]; log.roi['b0.stays'] = [r0x, Math.min(r0y, r1y) - 30, r1x, b0y + 10]; }
    label(O, 'loan ends sooner', Math.min(1700, mbx), mby - 60, { align: 'center', kind: 'compare', alpha: ok * show(t, b.b0.sooner, w22) });
    log.roi['b0.sooner'] = [mbx - 40, mby - 30, Math.min(1920, sc(track.colX(29, 1), 0, 0)[0]), my + 10];
    // S22.2: khoản bắt buộc tách hai phần + tên hai phần (không số)
    { const [bx, by0] = sc(X.bar[0], 0, X.bar[1]), [bxS, byS] = sc(X.bar[0], bar.h * S.share[curM], X.bar[1]), [bxT, byT] = sc(X.bar[0], bar.h, X.bar[1]);
      const pa = ok * bA * show(t, b.b1.cut);
      // C5: thanh ở phải vách (x ≈ 1560–1740) → tên gốc NGAY TRÊN đỉnh thanh, tên lãi NGAY DƯỚI chân thanh (căn giữa; không đè "loan ends sooner" y ≤ 350)
      label(O, 'principal', bxT, byT - 24, { align: 'center', kind: 'name', px: 48, alpha: pa * ease(t, b.b1.cut + 0.6, b.b1.cut + 1.2) });
      label(O, 'interest', bx, by0 + 50, { align: 'center', kind: 'name', px: 48, color: C.muted, alpha: pa });
      log.roi['b1.cut'] = [bx - 70, byT - 20, bxT + 70, by0 + 10]; log.roi['b1.fixed'] = log.roi['b1.cut']; log.roi['b1.principal'] = [Math.min(bx, bxS) - 70, byT - 20, bxT + 70, byS + 10]; }
    label(O, "next month's interest ↓, payment fixed", 960, 205, { align: 'center', kind: 'compare', alpha: ok * show(t, b.b1.interest, w22) });
    log.roi['b1.interest'] = [400, 150, 1520, 230];
    // S22.3 (thế giới): cột năm 10 loé, một tấm nhấc lên
    { const [x, y] = sc(...track.tileAt(S.lift.i)); log.roi['b2.later'] = [x - 60, y - 160, x + 60, y + 60]; log.roi['b2.wrong'] = log.roi['b2.later']; }
    // S23
    log.roi['b3.send'] = grid; { const [x, y] = sc(...blockTop(0)); log.roi['b3.once'] = [Math.min(gx0, fx0) - 10, y - 30, x + 60, fy0 + 10]; }
    log.roi['b4.extra'] = [Math.min(gx0, fx0), sc(...blockTop(7))[1] - 30, mx, my];
    const s24 = b.b7.verdict - 0.35;   // hai nhãn S23 giữ qua S24.1 (≥ 3 s đọc), nhường chỗ cho hai nhãn đối trọng S24.2
    label(O, `${D('yearly_lump')} (${D('yearly_lump_formula')})`, 960, 205, { align: 'center', kind: 'number', alpha: ok * show(t, b.b4.one, s24), claims: ['yearly_lump', 'yearly_lump_formula'] });
    log.roi['b4.one'] = [400, 150, 1520, 230];
    log.roi['b5.ends'] = [lx - 60, ly - 60, lx2 + 60, ly + 120];
    label(O, `ends in ${D('yearly_lump_months')}: ${D('yearly_lump_late')} than monthly`, 960, 268, { align: 'center', kind: 'number', alpha: ok * show(t, b.b5.four, s24),
      claims: ['yearly_lump_months', 'yearly_lump_late'] });
    log.roi['b5.four'] = [300, 215, 1620, 290];
    // S24.1–S24.2: chồng lãi nhỏ + nhãn; đối trọng (hai nhãn, khay viền nét đứt)
    const w24 = MV.m_w24.t0 - 0.05;
    { const [x, y] = sc(X.istack[0], IUSD / G.bundle_usd * BUNDLE_TH, X.istack[1]), [, y0] = sc(X.istack[0], 0, X.istack[1]);
      label(O, `${D('yearly_vs_monthly_interest')} more interest`, 1810, y - 40, { align: 'right', kind: 'number', alpha: ok * show(t, b.b6.about, w24), claims: ['yearly_vs_monthly_interest'] });
      log.roi['b6.charges'] = [x - 70, y - 20, x + 70, y0 + 10]; log.roi['b6.about'] = [1100, y - 90, 1810, y - 30]; }
    // C5: "sits" = xấp năm đầu đang chờ (cột 0) + chồng lãi đang nhỏ giọt
    { const [, y] = sc(...blockTop(0)), [, y0] = sc(X.istack[0], 0, X.istack[1]); log.roi['b6.sits'] = [Math.min(gx0, fx0), y - 60, Math.max(mx, sc(X.istack[0] + 0.5, 0, X.istack[1])[0]), Math.max(fy0, y0 + 10)]; }
    label(O, 'not a verdict on paying yearly', 960, 205, { align: 'center', kind: 'compare', alpha: ok * show(t, b.b7.verdict, w24) });
    label(O, 'what it earns there: not counted', 960, 268, { align: 'center', kind: 'compare', alpha: ok * show(t, b.b7.counted, w24) });
    log.roi['b7.verdict'] = [460, 150, 1460, 230]; log.roi['b7.counted'] = [460, 215, 1460, 290];
    { const q = [[-0.48, 0], [0.48, 0], [0.48, JH + 0.04], [-0.48, JH + 0.04]].map(([u, v]) => sc(X.tray[0] + JS * u, JS * v, X.tray[1] + JS * 0.32)), c = O.ctx, a = ok * show(t, b.b7.counted, w24);
      if (a > 0.01) { c.save(); c.globalAlpha = 0.9 * a; c.strokeStyle = C.ink; c.lineWidth = 3; c.setLineDash([10, 8]); c.beginPath(); q.forEach(([x, y], i) => (i ? c.lineTo(x, y) : c.moveTo(x, y))); c.closePath(); c.stroke(); c.restore(); }
      const xs = q.map((p) => p[0]), ys = q.map((p) => p[1]); log.roi['b7.account'] = [Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)]; }
    { const [hx, hy] = sc(HV.x, HV.y, HV.z), [dx, dy] = sc(...dest); log.roi['b8.dollar'] = [Math.min(hx, dx) - 80, Math.min(hy, dy) - 150, Math.max(hx, dx) + 80, Math.max(hy, dy) + 60]; log.roi['b8.earn'] = [dx - 80, dy - 80, dx + 80, dy + 80]; }
    chrome(O, { src: SRC_SIM(D) });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
