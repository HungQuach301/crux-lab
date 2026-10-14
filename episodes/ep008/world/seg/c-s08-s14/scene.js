// Tập 8 · ĐOẠN C = S08–S14 (chương 3 "The street lights up"). Lưới mọc trái → phải (1991 → 2016) → Nina qua cuối phố → luật đèn trên hai nhà ví dụ →
// đi dọc phố: 1990s sáng, từ April 2001 cửa tối tới December 2007 → đồ thị: 6 trên 72 → sáng lại 2009 → 2016 → đếm tại chỗ (số neo 1: about 3 out of 4)
// → dải chênh lệch theo tháng, trung vị khoảng $157,000, độ trải.
import { setup, Street, Home8, figure, nameTag, label, chrome, chapterCard, legend, followLight, modeLook, show, pulse, ease, lin,
  xOf, zOf, colOf, END_X, APT, NINA, LIT, C, THREE } from '/episodes/ep008/world/w8.js';
import { Ribbon } from '/toolkit/factory/world/lib3d.js';

const SEG = '/episodes/ep008/world/seg/c-s08-s14/';
const RX = -24, RW = 12, RY = 0.4, RH = 3.6, RZ = -2;

export async function boot(res) {
  const poses = {
    wSide: { pos: [12, 4.2, 12.5], tgt: [12, 0, -5], fov: 50, chart: 0 },
    cGrid: { pos: [11.9, 31, 4.5], tgt: [11.9, 0, -5.2], fov: 34, chart: 1 },
    wEnd: { pos: [END_X - 3.5, 2.4, 6.5], tgt: [NINA.x - 1.2, 0.5, -1.5], fov: 44, chart: 0 },
    wPair: { pos: [9.5, 5.5, 7.5], tgt: [9.5, 0.3, -4.5], fov: 44, chart: 0 },
    wWalk0: { pos: [-3.2, 2.8, 4.8], tgt: [3.2, 0.3, -4.2], fov: 46, chart: 0 },
    wWalk1: { pos: [7.2, 2.8, 4.8], tgt: [13.2, 0.3, -4.2], fov: 46, chart: 0 },
    cAdv: { pos: [RX + RW / 2, RY + RH / 2, RZ + 18], tgt: [RX + RW / 2, RY + RH / 2, RZ], fov: 25, chart: 1 },
  };
  const { S, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const st10 = DATA.starts10, n = st10.length, street = Street(scene, st10), H = Home8(scene);
  const nina = figure(scene, { x: NINA.x, z: NINA.z, lamp: true });
  const ahead = DATA.ahead10['5'], ex1 = st10.indexOf('1995-06'), ex2 = st10.indexOf('2006-06');
  // khoảng hiện đèn theo thời kỳ (giờ lời)
  const span = (s) => s < '2000-01' ? [b.c7.every, b.c7.every + 3.0, '1991-01', '1999-12'] : s < '2001-04' ? [b.c8.start, b.c8.start + 1.2, '2000-01', '2001-03']
    : s <= '2007-12' ? [b.c9.april, b.c10.december + 0.4, '2001-04', '2007-12'] : [b.c13.again, b.c13.every + 2.5, '2008-01', '2016-07'];
  const mIdx = (s) => (+s.slice(0, 4)) * 12 + (+s.slice(5, 7));
  const rev = (i, t) => { const s = st10[i], [a, z, s0, s1] = span(s), f = (mIdx(s) - mIdx(s0)) / Math.max(1, mIdx(s1) - mIdx(s0)); return ease(t, a + (z - a) * f - 0.15, a + (z - a) * f + 0.15); };
  const era = (s) => s >= '2002-01' && s <= '2007-12';
  // dải chênh lệch (đồ thị): x = tháng bắt đầu, y = chênh lệch người mua − người thuê sau 10 năm
  const adv = DATA.adv10, X = (i) => RX + RW * i / (n - 1), Y = (v) => RY + (v + 150000) / 650000 * RH;
  const rib = Ribbon({ maxPts: n, width: 0.06, color: C.ink, z: RZ }), zero = Ribbon({ maxPts: 2, width: 0.025, color: C.muted, z: RZ - 0.01 }), med = Ribbon({ maxPts: 2, width: 0.035, color: LIT, z: RZ + 0.01 });
  scene.add(rib, zero, med);
  const sorted = [...adv].sort((x, y) => x - y), median = sorted[Math.floor(n / 2)];

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    nina.lamp.set(1, t); nina.look(-0.6);
    const pb = lin(t, b.c1.each - 0.2, b.c1.right + 0.3);
    const exL = show(t, b.c4.lights - 0.1, MV.m_walk.t0), exD = show(t, b.c5.dark - 0.1, MV.m_walk.t0);
    const cnt1 = pulse(t, b.c16.three, 1.6), cnt2 = pulse(t, b.c17.seventy, 1.4);
    street.set({
      vis: (i) => ease(pb * 1.08, colOf(st10[i]) / 26 - 0.02, colOf(st10[i]) / 26 + 0.02) + (t < b.c1.each ? 1 : 0),
      rise: (i) => (i === ex1 ? 1 + 0.6 * exL : i === ex2 ? 1 + 0.6 * exD : 1),
      lit: (i) => (i === ex1 ? exL : 0) + (t > b.c6.walking ? rev(i, t) * (ahead[i] ? 1 : 0) : 0),
      dark: (i) => (i === ex2 ? exD : 0) + (t > b.c6.walking ? rev(i, t) * (ahead[i] ? 0 : 1) : 0),
      hi: (i) => (era(st10[i]) ? 0.3 * show(t, b.c11.seventy, b.c13.again) : 0) + (ahead[i] ? cnt1 : cnt2) * 0.8,
      cellA: cw * (t < MV.m_adv.t0 ? 1 : 0),
    });
    H.tag.set({ value: 5, swing: 0.05 * Math.sin(t * 1.3) });
    // dải chênh lệch: vẽ trái → phải sau cú lia, vạch 0, trung vị ở "one"
    const g = Math.max(2, Math.floor(n * ease(t, MV.m_adv.t1, b.c20.one - 0.2)));
    rib.set(adv.slice(0, g).map((v, i) => [X(i), Y(v), v > 0 ? LIT : C.warn])); rib.visible = t > MV.m_adv.t0;
    zero.set([[X(0), Y(0)], [X(n - 1), Y(0)]]); zero.visible = rib.visible;
    med.set([[X(0), Y(median)], [X(n - 1), Y(median)]]); med.visible = t > b.c20.one - 0.1; med.material.opacity = show(t, b.c20.one - 0.1);
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    nameTag(O, nina, t > MV.m_w1.t1 && t < MV.m_pair.t1 ? 1 : 0);
    const gA = ok * (t < MV.m_adv.t0 ? 1 : 0);
    const [ax, ay] = O.toScreen(0, 0, 0.9), [zx] = O.toScreen(25 * 0.95, 0, 0.9);
    label(O, 'January 1991', ax, ay + 60, { align: 'center', kind: 'number', px: 48, alpha: gA * show(t, b.c1.january, b.c18.interest - 0.3), color: C.muted, claims: ['first_10y'] });
    label(O, 'July 2016', zx, ay + 60, { align: 'center', kind: 'number', px: 48, alpha: gA * show(t, b.c1.right, b.c18.interest - 0.3), color: C.muted, claims: ['last_10y'] });
    label(O, '307 start months · ten years each', 960, 230, { align: 'center', kind: 'number', alpha: gA * show(t, b.c2.three, MV.m_w1.t0), claims: ['n_10y'] });
    log.roi['c1.each'] = [ax - 60, 300, zx + 60, ay + 80]; log.roi['c2.three'] = [500, 180, 1420, 260];
    const [nx, ny] = O.toScreen(NINA.x - 1.6, 0.05, NINA.z - 1.2), wA = cw < 0.05 ? 1 : 0;
    label(O, "Nina's month: no house yet", nx, ny - 40, { align: 'center', kind: 'name', px: 48, alpha: wA * show(t, b.c3.past, MV.m_pair.t0) });
    log.roi['c3.past'] = [nx - 300, ny - 100, nx + 300, ny + 100];
    const [e1x, e1y] = O.toScreen(xOf('1995-06'), 1.2, zOf('1995-06')), [e2x, e2y] = O.toScreen(xOf('2006-06'), 1.2, zOf('2006-06'));
    label(O, "buyer's equity > renter's cash", e1x, e1y - 40, { align: 'center', kind: 'name', px: 44, alpha: wA * show(t, b.c4.lights, MV.m_walk.t0), color: LIT });
    label(O, "renter's cash bigger", e2x, e2y - 40, { align: 'center', kind: 'name', px: 44, alpha: wA * show(t, b.c5.dark, MV.m_walk.t0), color: C.warn });
    log.roi['c4.lights'] = [e1x - 200, e1y - 100, e1x + 200, e1y + 160]; log.roi['c5.dark'] = [e2x - 200, e2y - 100, e2x + 200, e2y + 160];
    label(O, '2002 to 2007: 6 of 72 (8.3%)', 960, 230, { align: 'center', kind: 'number', alpha: gA * show(t, b.c11.six, b.c13.again), claims: ['era_2002-2007_span', 'era_2002-2007_share', 'era_2002-2007_pct'] });
    label(O, 'lit again: every start 2009 to mid-2016', 960, 230, { align: 'center', kind: 'number', alpha: gA * show(t, b.c13.every, b.c15.counted), claims: ['era_2009-2016_share'] });
    label(O, 'buyer ahead: about 3 out of 4 (75.6%)', 960, 230, { align: 'center', kind: 'number', px: 64, alpha: gA * show(t, b.c16.three, b.c19.lit - 0.3), color: LIT, claims: ['share_buyer_ahead_10y', 'share_buyer_ahead_10y_pct'] });
    label(O, 'renter ahead: 75 of 307', 960, 320, { align: 'center', kind: 'number', alpha: gA * show(t, b.c17.seventy, b.c19.lit - 0.3), color: C.warn, claims: ['n_renter_ahead_10y'] });
    label(O, 'counted: interest · tax · insurance · repairs · buying and selling', 960, 900, { align: 'center', kind: 'name', px: 44, alpha: gA * show(t, b.c18.interest, MV.m_adv.t0) });
    log.roi['c11.six'] = [500, 180, 1420, 900]; log.roi['c16.three'] = [300, 170, 1620, 900]; log.roi['c17.seventy'] = [700, 270, 1220, 350];
    // S14: đồ thị chênh lệch
    const aA = ok * (t > MV.m_adv.t1 ? 1 : 0);
    label(O, 'a count of history, not a promise', 960, 230, { align: 'center', kind: 'name', alpha: ok * show(t, b.c19.lit) });
    const [ox, oy] = O.toScreen(RX, Y(0), RZ), [mx, my] = O.toScreen(RX + RW, Y(median), RZ);
    label(O, 'middle start month: about $157,000 ahead', mx, my - 30, { align: 'right', kind: 'number', px: 48, alpha: aA * show(t, b.c20.one), color: LIT, claims: ['median_adv_10y'] });
    label(O, 'buyer ahead', ox - 20, Y(200000) > 0 ? O.toScreen(RX, Y(200000), RZ)[1] : oy - 100, { align: 'right', kind: 'name', px: 40, alpha: aA, color: LIT });
    label(O, 'renter ahead', ox - 20, O.toScreen(RX, Y(-80000), RZ)[1], { align: 'right', kind: 'name', px: 40, alpha: aA, color: C.warn });
    const [s0x, s0y] = O.toScreen(RX + RW + 0.3, Y(sorted[0]), RZ), [, s1y] = O.toScreen(RX + RW + 0.3, Y(sorted[n - 1]), RZ), sp = aA * show(t, b.c21.spread);
    if (sp > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = sp; c.strokeStyle = C.ink; c.lineWidth = 5; c.beginPath(); c.moveTo(s0x - 14, s0y); c.lineTo(s0x, s0y); c.lineTo(s0x, s1y); c.lineTo(s0x - 14, s1y); c.stroke(); c.restore(); }
    label(O, 'wide spread', s0x + 20, (s0y + s1y) / 2, { align: 'left', kind: 'name', px: 44, alpha: sp });
    log.roi['c20.one'] = [ox, my - 80, mx + 20, my + 40]; log.roi['c21.spread'] = [s0x - 30, s1y, s0x + 300, s0y];
    legend(O, show(t, b.c4.lights - 0.2, MV.m_adv.t0));
    chrome(O, {});
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
