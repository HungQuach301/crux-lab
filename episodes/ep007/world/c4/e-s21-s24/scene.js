// Tập 7 · C4 · ĐOẠN E = S21–S24. N1 Month track BẢN C4 (c4kit.TrackC4): vách 15 năm làm đích → 180 ô đặt tới vách → (3/4) 14,6 ô trễ quá vách →
// TẤM trả thêm dày, phát quang RƠI vào từng cột, ô bắt buộc tối hẳn, ô trễ rút hết → đường xong đúng ô 180 → bóng lịch 30 năm rút về vách, thanh mức
// bắt buộc đứng yên, một khoản bắt buộc tách lãi/gốc (lãi co lại) → một tấm nhấc lên (tháng khó, đường lui còn) → sóng mỗi tháng một lớp, gom thành
// khối năm 12 lớp có khe → 4 ô trễ → chồng lãi nhỏ + khay tài khoản (đối trọng S24.2) → tờ đô la từ tay Tessa. Mốc giờ chỉ từ spine.json.
import { setup, figure, gesture, figTag, TrackC4, SplitBar, TRK, BUNDLE_TH, modeLook, followLight, chrome, SRC_SIM, label, seg2, dip,
  kf, show, pulse, C, ease, lin, mix, THREE, setOpacity } from '/episodes/ep007/world/c4kit.js';
import { TRACK_POSES } from '/episodes/ep007/world/c3kit.js';
import { Stack } from '/toolkit/factory/world/lib3d.js';
import { Bill } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c4/e-s21-s24/';

export async function boot(res) {
  // cQ: góc 3/4 (~40°) trước lưới — KHÔNG nhìn thẳng xuống lúc tấm trả thêm phủ (thấy cạnh tấm); vách thấp + trong mờ không che ô trễ;
  // Tessa, khoản bắt buộc tách hai phần (S22.2) và chồng lãi nhỏ (S24) đều trong khung
  const poses = { ...TRACK_POSES, cQ: { pos: [2.2, 5.4, 5.9], tgt: [2.5, 0.3, -1.9], fov: 52, chart: 1 } };
  const { S, D, G, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue, X = S.x;
  const hm = figure(scene, { x: X.house[0], z: X.house[1], side: 1 }); hm.person.position.set(X.tessa[0], 0, X.tessa[1]);
  const track = TrackC4({ name: 'tessa' }); scene.add(track); const T = track.userData;
  // S22.1: thanh mức khoản bắt buộc (ink-muted, vật cố định) dọc mép trước 15 cột
  const rail = new THREE.Mesh(new THREE.BoxGeometry(1, 0.05, 0.06), new THREE.MeshStandardMaterial({ color: TRK.req, emissive: new THREE.Color(TRK.req), emissiveIntensity: 0.5, transparent: true }));
  rail.geometry.translate(0.5, 0, 0); rail.position.set(0, 0.03, track.frontZ() + 0.16); scene.add(rail); rail.userData.checks = { role: 'mark', key: 'required-level' };
  const bar = SplitBar({ x: X.bar[0], z: X.bar[1], h: 2.0 }); scene.add(bar);
  // S24.1: chồng lãi nhỏ (bó màu tiền — không phải warn: warn = giá của đường lui)
  const ist = Stack({ unitUsd: G.bundle_usd / BUNDLE_TH, bundleUsd: G.bundle_usd, w: 0.9, d: 0.6, maxUsd: 9000 }); ist.position.set(X.istack[0], 0, X.istack[1]); scene.add(ist);
  ist.userData.checks = { role: 'bar', series: 'yearly-extra-interest', key: 'yearly-extra-interest' };
  const IUSD = 8166;   // yearly_vs_monthly_interest (độ cao vật; nhãn qua claim)
  // S24.2: khay "tài khoản" cạnh Tessa — 12 tấm đang chờ tới kỳ trả năm
  const tray = new THREE.Group(), trayBox = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.12, 0.62), new THREE.MeshStandardMaterial({ color: TRK.req, transparent: true, opacity: 0.35, depthWrite: false }));
  trayBox.position.y = 0.06; tray.add(trayBox);
  for (let k = 0; k < 12; k++) { const s = new THREE.Mesh(new THREE.BoxGeometry(0.29, 0.06, 0.29), new THREE.MeshStandardMaterial({ color: TRK.ink, emissive: new THREE.Color(TRK.ink), emissiveIntensity: 0.7, transparent: true }));
    s.position.set(0, 0.14 + k * 0.085, 0); tray.add(s); }
  tray.position.set(X.tray[0], 0, X.tray[1]); scene.add(tray); tray.userData.checks = { role: 'mark', key: 'account-tray' };
  const bill = Bill({ name: 'extra-dollar' }); scene.add(bill);
  const hand = [X.tessa[0] + 0.35, 0.7, X.tessa[1] + 0.2], dest = [X.house[0] + 0.1, 2.1, X.house[1] + 0.9];
  const lay = S.lay, land = S.land, NC = 15;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw); gesture(hm, t, S.gestures);
    const late = t < S.clear_t ? kf(S.late21, t) : kf(S.late23, t);
    const curM = Math.min(179, Math.max(0, Math.floor(179 * lin(t, S.cursor[0], S.cursor[1])))), curOn = t > S.cursor[0] - 0.05 && t < S.cursor[1] + 0.4 ? 1 : 0;
    const gc = 15 * ease(t, b.b0.requires - 0.05, b.b0.requires + 1.2) * (1 - ease(t, b.b0.sooner - 0.05, b.b0.sooner + 0.6));
    track.set({ lit: kf(S.lit, t), late,
      flash: (c) => Math.min(1, pulse(t, lay[c] + 0.2, 0.6) + 0.5 * pulse(t, b.a2.required, 0.9) + curOn * (Math.floor(curM / 12) === c ? 0.7 : 0) + (c === 9 ? pulse(t, b.b2.later, 1.2) : 0)),
      cover: (c) => ease(t, land[c] - 0.12, land[c] + 0.15), drop: (c) => lin(t, land[c] - S.drop, land[c]),
      gathered: (c) => ease(t, S.gather[c][0], S.gather[c][1]),
      bob: (i) => { const u = (t - (S.wave[0] + (S.wave[1] - S.wave[0] - 0.3) * i / 179)) / 0.3; return (u > 0 && u < 1 ? 0.14 * Math.sin(Math.PI * u) : 0) + (i < 12 ? 0.12 * pulse(t, b.b3.once, 0.4) : 0); },
      lift: { i: S.lift.i, a: ease(t, S.lift.t[0] - 0.05, S.lift.t[0] + 0.45) * (1 - ease(t, S.lift.t[1], S.lift.t[1] + 0.5)) },
      ghost: gc, ghostA: gc > 0.01 ? 1 : 0,
      markA: ease(t, S.mark_t - 0.05, S.mark_t + 0.5) * (0.75 + 0.6 * pulse(t, b.a0.same, 1.0)) * (1 + 0.5 * pulse(t, b.b0.sooner, 1.0)),
      pulse: show(t, b.a1.late) * (1 - show(t, b.a1.late + 0.6)) + show(t, b.b5.four) * (1 - show(t, b.b5.four + 0.6)) });
    const rA = ease(t, b.b0.requires - 0.05, b.b0.requires + 0.6) * (1 - ease(t, MV.m_w22.t0, MV.m_w22.t0 + 0.4));
    rail.scale.x = Math.max(0.001, T.markX * lin(t, b.b0.requires, b.b0.requires + 0.8)); rail.visible = rA > 0.01; rail.material.opacity = rA;
    rail.material.emissiveIntensity = 0.5 + 1.0 * pulse(t, b.b0.stays, 1.0);
    const bA = show(t, b.b1.cut) * (1 - ease(t, MV.m_w22.t0, MV.m_w22.t0 + 0.4));
    bar.set({ share: S.share[curM], a: bA }); bar.visible = bA > 0.01;
    bar.children[1].material.emissiveIntensity = 0.35 + 0.8 * pulse(t, b.b1.principal, 1.0) + 0.4 * pulse(t, b.b1.fixed, 0.8);
    ist.set({ usd: IUSD * ease(t, b.b6.charges, b.b6.charges + 0.7) * (1 - ease(t, MV.m_w24.t0, MV.m_w24.t0 + 0.5)) });
    const tA = show(t, b.b7.account) * (1 - ease(t, MV.m_w24.t0, MV.m_w24.t0 + 0.5));
    setOpacity(tray, tA); trayBox.material.opacity = 0.35 * tA; tray.visible = tA > 0.01;
    // S24.3: tờ đô la hiện trong tay Tessa ("dollar"), bay lên về phía nhà rồi lơ lửng (câu hỏi mở)
    const a1 = show(t, b.b8.dollar), u = ease(t, b.b8.dollar + 0.2, b.b8.dollar + 1.8);
    bill.visible = a1 > 0.01; bill.scale.setScalar(Math.max(0.001, a1));
    bill.rotation.set(Math.PI / 2 * (0.35 + 0.65 * u), 0.3 * Math.sin(1.7 * t), 0);
    bill.position.set(mix(hand[0], dest[0], u), mix(hand[1], dest[1], u) + 0.6 * Math.sin(Math.PI * u) + 0.04 * Math.sin(2.2 * t), mix(hand[2], dest[2], u));
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 1 - ease(t, 0, 0.4));
    figTag(O, hm);
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
    // "about 15 months late" (mới ở C4) cạnh ô trễ; tắt khi ô trễ bắt đầu rút (cột đầu phủ xong)
    label(O, D('months_late_at_pay15_now'), 1810, ly - 80, { align: 'right', kind: 'number', color: C.warn, alpha: ok * show(t, b.a1.late, land[0] - 0.1), claims: ['months_late_at_pay15_now'] });
    log.roi['a1.late'] = [1200, ly - 130, 1810, ly - 60];
    // S21.3: tấm rơi; nhãn hai dòng chỉ hiện khi không còn ô trễ nào
    log.roi['a2.finish'] = [fx0 - 10, gy0 - 120, track.colX ? sc(track.colX(1, 1), 0, track.frontZ())[0] + 10 : fx0 + 100, fy0 + 10];
    log.roi['a2.required'] = grid;
    const s7 = ok * show(t, b.a2.seven, b.b0.requires - 0.1) * (late <= 0 ? 1 : 0);
    label(O, `to finish in ${D('monthly_extra_months')}:`, 960, 205, { align: 'center', kind: 'number', alpha: s7, claims: ['monthly_extra_months'] });
    label(O, `${D('extra_month_about')} extra on top of the ${D('pay30_amt')} required`, 960, 268, { align: 'center', kind: 'number', alpha: s7, claims: ['extra_month_about', 'pay30_amt'] });
    log.roi['a2.seven'] = [300, 150, 1620, 290];
    // S22.1
    const w22 = MV.m_w22.t0 - 0.05;
    label(O, `required payment: stays ${D('pay30_amt')}`, 1120, 872, { align: 'center', kind: 'number', alpha: ok * show(t, b.b0.stays, w22), claims: ['pay30_amt'] });
    { const [r0x, r0y] = sc(0, 0.03, track.frontZ() + 0.16), [r1x] = sc(T.markX, 0.03, track.frontZ() + 0.16);
      log.roi['b0.requires'] = [r0x, r0y - 30, sc(track.colX(29, 1), 0, 0)[0], r0y + 30]; log.roi['b0.stays'] = [r0x, r0y - 30, r1x, r0y + 30]; }
    label(O, 'loan ends sooner', Math.min(1700, mbx), mby - 60, { align: 'center', kind: 'compare', alpha: ok * show(t, b.b0.sooner, w22) });
    log.roi['b0.sooner'] = [mbx - 40, mby - 30, Math.min(1920, sc(track.colX(29, 1), 0, 0)[0]), my + 10];
    // S22.2: khoản bắt buộc tách hai phần + tên hai phần (không số)
    { const [bx, by0] = sc(X.bar[0] + 0.3, 0, X.bar[1]), [, byS] = sc(X.bar[0] + 0.3, bar.h * S.share[curM], X.bar[1]), [, byT] = sc(X.bar[0] + 0.3, bar.h, X.bar[1]);
      const pa = ok * bA * show(t, b.b1.cut);
      // tên hai phần bên phải thanh, TRÊN tên "Tessa · ILLUSTRATIVE" (dưới chân Tessa, x ≤ ~600): gốc ngang đỉnh thanh, lãi ngay dưới
      label(O, 'principal', bx + 22, byT + 40, { kind: 'name', px: 48, alpha: pa * ease(t, b.b1.cut + 0.6, b.b1.cut + 1.2) });
      label(O, 'interest', bx + 22, Math.min(by0 - 20, byT + 118), { kind: 'name', px: 48, color: C.muted, alpha: pa });
      log.roi['b1.cut'] = [bx - 90, byT - 20, bx + 20, by0 + 10]; log.roi['b1.fixed'] = log.roi['b1.cut']; log.roi['b1.principal'] = [bx - 90, byT - 20, bx + 20, byS + 10]; }
    label(O, "next month's interest ↓, payment fixed", 960, 205, { align: 'center', kind: 'compare', alpha: ok * show(t, b.b1.interest, w22) });
    log.roi['b1.interest'] = [400, 150, 1520, 230];
    // S22.3 (thế giới): cột năm 10 loé, một tấm nhấc lên
    { const [x, y] = sc(...track.tileAt(S.lift.i)); log.roi['b2.later'] = [x - 60, y - 160, x + 60, y + 60]; log.roi['b2.wrong'] = log.roi['b2.later']; }
    // S23
    log.roi['b3.send'] = grid; { const [x, y] = sc(...track.blockTop(0)); log.roi['b3.once'] = [Math.min(gx0, fx0) - 10, y - 30, x + 60, fy0 + 10]; }
    log.roi['b4.extra'] = [Math.min(gx0, fx0), sc(...track.blockTop(7))[1] - 30, mx, my];
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
    log.roi['b6.sits'] = [Math.min(gx0, fx0), sc(...track.blockTop(0))[1] - 30, mx, fy0];
    label(O, 'not a verdict on paying yearly', 960, 205, { align: 'center', kind: 'compare', alpha: ok * show(t, b.b7.verdict, w24) });
    label(O, 'what it earns there: not counted', 960, 268, { align: 'center', kind: 'compare', alpha: ok * show(t, b.b7.counted, w24) });
    log.roi['b7.verdict'] = [460, 150, 1460, 230]; log.roi['b7.counted'] = [460, 215, 1460, 290];
    { const q = [[-0.5, 0, -0.36], [0.5, 0, -0.36], [0.5, 1.2, -0.36], [-0.5, 1.2, -0.36]].map(([u, v, w]) => sc(X.tray[0] + u, v, X.tray[1] + w + 0.36)), c = O.ctx, a = ok * show(t, b.b7.counted, w24);
      if (a > 0.01) { c.save(); c.globalAlpha = 0.9 * a; c.strokeStyle = C.ink; c.lineWidth = 3; c.setLineDash([10, 8]); c.beginPath(); q.forEach(([x, y], i) => (i ? c.lineTo(x, y) : c.moveTo(x, y))); c.closePath(); c.stroke(); c.restore(); }
      const xs = q.map((p) => p[0]), ys = q.map((p) => p[1]); log.roi['b7.account'] = [Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)]; }
    { const [hx, hy] = sc(...hand), [dx, dy] = sc(...dest); log.roi['b8.dollar'] = [Math.min(hx, dx) - 80, Math.min(hy, dy) - 80, Math.max(hx, dx) + 80, Math.max(hy, dy) + 60]; log.roi['b8.earn'] = [dx - 80, dy - 80, dx + 80, dy + 80]; }
    chrome(O, { src: SRC_SIM(D) });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
