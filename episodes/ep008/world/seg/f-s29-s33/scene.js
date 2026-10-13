// Tập 8 · ĐOẠN F = S29–S33 (chương 6 "The end of the street"). Nina ở bãi trống qua cuối phố → hai chồng tháng đầu (đồ thị) → chấm tiền thuê ÷ chi
// tháng đầu của 307 tháng + chấm của Nina thấp hơn mọi chấm → thẻ V7 → bảng điểm trên phố nhìn từ trên → khung 0:00: cùng phố, nay sáng/tối → câu của Nina →
// hộp tiền mặt + hộp thứ hai đóng (câu hỏi còn mở) → tắt dần.
import { setup, Street, Home8, figure, MoneyStack, GlassBox, nameTag, label, chrome, chapterCard, v7Card, dip, followLight, modeLook, show, pulse, ease, lin,
  xOf, zOf, colOf, END_X, APT, NINA, BOX, LIT, DARKW, C, THREE } from '/episodes/ep008/world/w8.js';

const SEG = '/episodes/ep008/world/seg/f-s29-s33/';
const SX = NINA.x + 1.15, SZ = 0.9, RX = -24, RW = 12, RY = 0.4, RH = 3.6, RZ = -2;

export async function boot(res) {
  const poses = {
    wEnd: { pos: [END_X - 3.2, 2.2, 6.4], tgt: [NINA.x - 0.8, 0.5, -1.2], fov: 44, chart: 0 },
    cStacks: { pos: [SX - 0.15, 0.95, 16], tgt: [SX - 0.15, 0.95, 0.9], fov: 11, chart: 1 },
    cDots: { pos: [RX + RW / 2 + 0.6, RY + RH / 2, RZ + 18], tgt: [RX + RW / 2 + 0.6, RY + RH / 2, RZ], fov: 25, chart: 1 },
    cGrid: { pos: [11.9, 31, 4.5], tgt: [11.9, 0, -5.2], fov: 34, chart: 1 },
    w0: { pos: [-3.5, 4.2, 8.5], tgt: [14, 0.2, -4.5], fov: 44, chart: 0 },
    wDoor: { pos: [END_X - 1.2, 1.9, 6.4], tgt: [APT.x + 1.2, 0.75, -0.6], fov: 40, chart: 0 },
    wBox: { pos: [BOX.x - 2.0, 1.4, 4.0], tgt: [BOX.x - 0.5, 0.5, -0.2], fov: 40, chart: 0 },
  };
  const { S, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const st10 = DATA.starts10, n = st10.length, street = Street(scene, st10), H = Home8(scene);
  const nina = figure(scene, { x: NINA.x, z: NINA.z, lamp: true });
  const rent = MoneyStack(scene, { x: SX - 0.45, z: SZ, color: C.warn, unit: 150, name: 'rent-month1' });
  const buy1 = MoneyStack(scene, { x: SX + 0.35, z: SZ, color: LIT, unit: 150, name: 'buyer-month1' });
  const box = GlassBox(scene, { x: BOX.x, z: BOX.z }), box2 = GlassBox(scene, { x: BOX.x - 1.3, z: BOX.z, max: 0 });
  const A = DATA.ahead10['5'], r1 = DATA.ratio1;
  // chấm tiền thuê ÷ chi tháng đầu (đồ thị): x = tháng bắt đầu (+ một cột trống rồi chấm của Nina), y = tỉ lệ 0,5 → 1,1
  const X = (i) => RX + RW * i / (n + 12), Y = (v) => RY + (v - 0.5) / 0.6 * RH, NX = RX + RW * (n + 10) / (n + 12);
  const dots = new THREE.InstancedMesh(new THREE.SphereGeometry(0.035, 6, 4), new THREE.MeshBasicMaterial({ color: C.muted, transparent: true }), n); dots.frustumCulled = false; scene.add(dots);
  const M4 = new THREE.Matrix4(); r1.forEach((v, i) => { M4.makeTranslation(X(i), Y(v), RZ); dots.setMatrixAt(i, M4); }); dots.instanceMatrix.needsUpdate = true;
  const nd = new THREE.Mesh(new THREE.SphereGeometry(0.08, 12, 8), new THREE.MeshBasicMaterial({ color: '#FFB86B', transparent: true })); nd.position.set(NX, Y(0.568), RZ); scene.add(nd);
  const iMin = r1.indexOf(Math.min(...r1));

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    nina.lamp.set(1, t); nina.look(t < b.f9.same ? -0.5 : 0.2);
    // phố: sáng/tối theo lịch sử (khung 0:00 nay đọc theo nghĩa mới); bảng điểm: các dòng tô lại ô tương ứng
    const rS = show(t, b.f8.stretch, MV.m_w.t0), rT = show(t, b.f8.lit, b.f8.stretch);
    street.set({ lit: (i) => (A[i] ? 1 : 0), dark: (i) => (A[i] ? 0 : 1), hi: (i) => (A[i] ? 0.35 * rT : 0.5 * rS) + (i === iMin ? 0 : 0), cellA: t > MV.m_grid.t0 && t < MV.m_w.t1 ? cw : 0 });
    const s1 = show(t, b.f1.first - 0.1, MV.m_dots.t0 + 0.4);
    buy1.set({ usd: 2933 * ease(t, b.f1.first - 0.1, b.f1.first + 0.6), a: s1 });
    rent.set({ usd: 1667 * ease(t, b.f1.first + 0.2, b.f1.first + 0.8), a: s1 });
    const dA = t > MV.m_dots.t0 && t < MV.m_grid.t1 ? 1 : 0; dots.visible = nd.visible = dA > 0;
    nd.scale.setScalar(1 + 0.5 * pulse(t, b.f4.lowest, 1.0));
    box.set({ n: 9, a: 1, glow: 0 }); box2.set({ n: 0, a: 0.7 * show(t, b.f11.open) });
    H.tag.set({ value: 5, swing: 0.05 * Math.sin(t * 1.3) });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, ease(t, S.total - 1.4, S.total - 0.1));
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    const wA = cw < 0.05 ? 1 : 0;
    nameTag(O, nina, wA * (t < MV.m_box.t0 ? 1 : 0));
    const [nx, ny] = O.toScreen(NINA.x - 1.6, 0.05, NINA.z - 1.2);
    label(O, "Nina's month: no house yet", nx, ny - 40, { align: 'center', kind: 'name', px: 48, alpha: wA * show(t, b.f0.past, MV.m_c.t0) });
    const [, gy] = O.toScreen(SX, 0, SZ), [rx] = O.toScreen(SX - 0.45, 0, SZ), [bx] = O.toScreen(SX + 0.35, 0, SZ), sA = ok * s1;
    label(O, 'rent', rx, gy + 56, { align: 'center', kind: 'name', px: 48, alpha: sA, color: C.warn });
    label(O, "buyer's first month", bx + 60, gy + 56, { align: 'center', kind: 'name', px: 48, alpha: sA, color: LIT });
    label(O, 'September 2026 average: 6.86%', 960, 230, { align: 'center', kind: 'number', alpha: sA * show(t, b.f2.six), claims: ['rate_month_latest', 'rate_latest'] });
    label(O, "buyer's first month: $2,933", 960, 310, { align: 'center', kind: 'number', alpha: sA * show(t, b.f2.two), color: LIT, claims: ['today_buyer_month1'] });
    label(O, '$1,667 = 56.8% of $2,933', 960, 390, { align: 'center', kind: 'number', alpha: sA * show(t, b.f3.fifty), color: C.warn, claims: ['today_rent_month1', 'today_rent_to_outlay', 'today_buyer_month1'] });
    log.roi['f2.six'] = [500, 170, 1420, 250]; log.roi['f2.two'] = [500, 250, 1420, 330]; log.roi['f3.fifty'] = [500, 330, 1420, 410];
    const pA = ok * dA, [mx, my] = O.toScreen(X(iMin), Y(r1[iMin]), RZ), [qx, qy] = O.toScreen(NX, Y(0.568), RZ), [ox, oy] = O.toScreen(RX, Y(0.5), RZ);
    label(O, 'lowest replayed: 57.9%, July 2006', mx, my + 70, { align: 'center', kind: 'number', px: 44, alpha: pA * show(t, b.f4.lowest), claims: ['rent_to_outlay_min_10y', 'rent_to_outlay_min_start_10y'] });
    label(O, "Nina's first month", qx - 20, qy - 40, { align: 'right', kind: 'name', px: 44, alpha: pA * (1 - show(t, b.f6.card - 0.3)), color: '#FFB86B' });
    label(O, 'first months only, not a forecast', 960, 230, { align: 'center', kind: 'name', alpha: pA * show(t, b.f5.compares) });
    label(O, 'rent ÷ buyer\'s first month, each start month', ox, 900, { align: 'left', kind: 'name', px: 40, alpha: pA, color: C.muted });
    log.roi['f4.lowest'] = [mx - 300, my - 60, qx + 60, my + 120]; log.roi['f5.compares'] = [400, 170, 1520, 250];
    v7Card(O, 'What this leaves out', ['national price index, not one home', 'starting rent is an assumption', 'rent history: consumer price index for rent (CPI)',
      'no income taxes · no interest deduction · no refinancing', 'no moving costs · no renter\'s insurance', 'full method in the description'], show(t, b.f6.card - 0.3, MV.m_grid.t0 + 0.3));
    log.roi['f6.card'] = [300, 200, 1620, 800];
    // bảng điểm (đồ thị, trên phố nhìn từ trên): mỗi dòng đúng màu của lựa chọn
    const gA = ok * (t > MV.m_grid.t1 && t < MV.m_w.t0 ? 1 : 0), rows = [['lit', 'most start months: buyer ahead (about 3 in 4)', LIT, ['share_buyer_ahead_10y']],
      ['stretch', 'dark stretch: April 2001 to December 2007', C.warn, ['renter_first_10y', 'renter_last_10y']], ['stays', 'longer stays: fewer dark doors', C.ink, null],
      ['tag', 'the answer moves with the rent tag', '#C9D0DA', null]];
    if (gA > 0.01) O.card(330, 170, 1260, 330, { fill: '#0F141B', stroke: C.muted, lw: 3, alpha: 0.92 * gA * show(t, b.f8.lit - 0.3) });
    rows.forEach(([k, s, col, cl], j) => label(O, s, 380, 240 + 72 * j, { align: 'left', kind: cl ? 'number' : 'name', px: 50, alpha: gA * show(t, b.f8[k]), color: col, plate: null, ...(cl ? { claims: cl } : {}) }));
    log.roi['f8.lit'] = [330, 170, 1590, 500];
    label(O, 'Is her rent money wasted?', 960, 250, { align: 'center', kind: 'name', px: 64, alpha: wA * show(t, b.f10.answer, MV.m_box.t0) });
    log.roi['f10.answer'] = [400, 180, 1520, 280]; log.roi['f9.same'] = [100, 200, 1820, 900];
    const [b2x, b2y] = O.toScreen(BOX.x - 1.3, 1.1, BOX.z), [b1x, b1y] = O.toScreen(...box.top());
    label(O, 'cash, not stocks', b1x + 20, b1y - 30, { align: 'center', kind: 'name', px: 44, alpha: wA * show(t, b.f11.open), color: C.warn });
    label(O, 'invested? not measured here', b2x - 30, b2y - 30, { align: 'center', kind: 'name', px: 44, alpha: wA * show(t, b.f11.invested) });
    log.roi['f11.invested'] = [b2x - 320, b2y - 90, b2x + 220, b2y + 200];
    chrome(O, { cw: t > MV.m_w.t1 ? 'Not advice on whether to buy or rent' : null, cwA: show(t, MV.m_w.t1) });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
