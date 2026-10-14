// Tập 8 · ĐOẠN D = S15–S22 (chương 4 "The darkest house"). Nhà April 2012 nhấc lên + chồng chênh lệch cao → lia ngược xuống June 2006, dừng (số neo 2:
// cửa tối, "$82,385 behind") → hai chồng: vốn người mua (lit) thấp hơn tiền mặt người thuê (warn) → chỉ số giá gần như phẳng 10 năm → lưới 5 / 10 / 15
// năm → Nina qua cuối phố, thẻ chưa xoay → MR2.
import { setup, Street, Home8, figure, MoneyStack, nameTag, label, chrome, chapterCard, legend, followLight, modeLook, show, pulse, ease, lin,
  xOf, zOf, colOf, byMonth, END_X, APT, NINA, LIT, C, THREE } from '/episodes/ep008/world/w8.js';
import { Ribbon } from '/toolkit/factory/world/lib3d.js';

const SEG = '/episodes/ep008/world/seg/d-s15-s22/';
const RX = -24, RW = 12, RY = 0.4, RH = 3.6, RZ = -2;
const BX = xOf('2012-04'), BZ = zOf('2012-04'), DX = xOf('2006-06'), DZ = zOf('2006-06'), FZ = 1.5;

export async function boot(res) {
  const poses = {
    cBright: { pos: [BX + 0.4, 1.4, 16], tgt: [BX + 0.4, 1.2, 0], fov: 14, chart: 1 },
    cDark: { pos: [DX + 0.3, 1.2, 16], tgt: [DX + 0.3, 1.0, 0], fov: 14, chart: 1 },
    cIdx: { pos: [RX + RW / 2, RY + RH / 2, RZ + 18], tgt: [RX + RW / 2, RY + RH / 2, RZ], fov: 25, chart: 1 },
    cGrid: { pos: [11.9, 31, 4.5], tgt: [11.9, 0, -5.2], fov: 34, chart: 1 },
    wNina: { pos: [END_X - 2.6, 2.1, 6.4], tgt: [APT.x + 0.4, 0.7, -0.9], fov: 42, chart: 0 },
  };
  const { S, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const st10 = DATA.starts10, n = st10.length, street = Street(scene, st10), H = Home8(scene);
  const nina = figure(scene, { x: NINA.x, z: NINA.z, lamp: true });
  const iB = st10.indexOf('2012-04'), iD = st10.indexOf('2006-06'), iM = st10.indexOf('2006-05');
  const a10 = DATA.ahead10['5'], a5 = byMonth(DATA.starts5, DATA.ahead5), a15 = byMonth(DATA.starts15, DATA.ahead15);
  const advB = MoneyStack(scene, { x: BX + 1.1, z: FZ, color: LIT, unit: 20000, name: 'best-advantage' });
  const eq = MoneyStack(scene, { x: DX - 0.45, z: FZ, color: LIT, unit: 12000, name: 'buyer-equity' });
  const cash = MoneyStack(scene, { x: DX + 0.45, z: FZ, color: C.warn, unit: 12000, name: 'renter-cash' });
  // chỉ số giá cả nước trong mười năm của June 2006 (chuẩn hoá = 1 ở tháng bắt đầu)
  const m0 = DATA.months.indexOf('2006-06'), m1 = DATA.months.indexOf('2016-06'), win = DATA.hpi.slice(m0, m1 + 1).map((v) => v / DATA.hpi[m0]);
  const X = (i) => RX + RW * i / (win.length - 1), Y = (v) => RY + (v - 0.6) / 0.7 * RH;
  const rib = Ribbon({ maxPts: win.length, width: 0.07, color: C.accent, z: RZ }), base = Ribbon({ maxPts: 2, width: 0.025, color: C.muted, z: RZ - 0.01 }); scene.add(rib, base);
  // lưới theo kỳ hạn: 5 / 10 / 15 năm (giờ đổi theo lời)
  const mode = (t) => (t < b.d10.five ? 10 : t < b.d13.every ? 5 : t < b.d15.five ? 15 : t < b.d15.ten ? 5 : t < S.at.fifteen ? 10 : 15);
  const stateOf = (i, H_) => { const s = st10[i]; if (H_ === 10) return a10[i] ? 1 : -1; const m = H_ === 5 ? a5 : a15; return m[s] === undefined ? 0 : m[s] ? 1 : -1; };

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    nina.lamp.set(1, t); nina.look(0.4);
    const inGrid = t > MV.m_grid.t0, Hn = mode(t), upB = show(t, 0.0, MV.m_dark.t0 + 0.6), upD = show(t, b.d3.darkest - 0.3, MV.m_idx.t0 + 0.4);
    const mayH = show(t, b.d11.may, b.d13.every - 0.3);
    street.set({
      lit: (i) => (inGrid ? (stateOf(i, Hn) === 1 ? 1 : 0) : a10[i] ? 1 : 0) + (i === iB ? 0.6 * upB : 0),
      dark: (i) => (inGrid ? (stateOf(i, Hn) === -1 ? 1 : 0) : a10[i] ? 0 : 1),
      vis: (i) => (inGrid && stateOf(i, Hn) === 0 ? 0.25 : 1),
      hi: (i) => (i === iM ? mayH : 0),
      lift: (i) => (i === iB ? 0.9 * upB : i === iD ? 0.9 * upD : 0), big: (i) => (i === iB ? 1 + 1.4 * upB : i === iD ? 1 + 1.4 * upD : 1),
      cellA: inGrid ? cw : 0,
    });
    advB.set({ usd: 483975 * ease(t, b.d0.about - 0.3, b.d0.about + 0.8), a: upB });
    // M5 nhịp: hai chồng mọc từ "a pair of stacks" (từ mở ý), đủ giá trị trước khi nhãn số hiện (F-14 (d))
    eq.set({ usd: 115374 * ease(t, b.d5.pair, Math.min(b.d5.pair + 1.4, b.d5.equity - 0.1)), a: show(t, b.d5.pair - 0.2, MV.m_idx.t0 + 0.4) });
    cash.set({ usd: 197760 * ease(t, b.d5.pair + 0.2, Math.min(b.d5.pair + 1.6, b.d5.equity - 0.1)), a: show(t, b.d5.pair - 0.2, MV.m_idx.t0 + 0.4) });
    const g = Math.max(2, Math.floor(win.length * ease(t, MV.m_idx.t1, b.d6.three + 1.2)));
    rib.set(win.slice(0, g).map((v, i) => [X(i), Y(v)])); rib.visible = t > MV.m_idx.t0 && t < MV.m_grid.t1;
    base.set([[X(0), Y(1)], [X(win.length - 1), Y(1)]]); base.visible = rib.visible;
    H.tag.set({ value: 5, swing: 0.05 * Math.sin(t * 1.3) });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    nameTag(O, nina, t > MV.m_w.t1 ? 1 : 0);
    const [bx, by] = O.toScreen(BX, 0.9 + 1.0, BZ), [sx, sy] = O.toScreen(BX + 1.1, advB.top(483975) + 0.1, FZ);
    label(O, 'April 2012', bx, by - 30, { align: 'center', kind: 'number', alpha: ok * show(t, b.d0.april, MV.m_dark.t0), color: LIT, claims: ['best_start_10y'] });
    label(O, 'about $484,000 ahead', sx + 40, sy - 20, { align: 'left', kind: 'number', alpha: ok * show(t, b.d0.about, MV.m_dark.t0), color: LIT, claims: ['best_adv_10y'] });
    label(O, '3.91% rate', 960, 900, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.d1.three, MV.m_dark.t0), claims: ['best_rate_10y'] });
    label(O, 'prices more than doubled', 960, 830, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.d1.doubled, MV.m_dark.t0), claims: ['best_price_change_10y'] });
    label(O, 'one month at the very top, not a typical one', 960, 230, { align: 'center', kind: 'name', px: 48, alpha: ok * show(t, b.d2.top, MV.m_dark.t0) });
    log.roi['d0.april'] = [bx - 200, by - 90, bx + 200, by + 200]; log.roi['d0.about'] = [sx - 60, sy - 70, sx + 560, sy + 300];
    const [dx, dy] = O.toScreen(DX, 0.9 + 1.0, DZ);
    label(O, 'June 2006', dx, dy + 280, { align: 'center', kind: 'number', alpha: ok * show(t, b.d3.june, MV.m_idx.t0), color: C.warn, claims: ['worst_start_10y'] });
    label(O, '$82,385 behind', 960, 230, { align: 'center', kind: 'number', px: 64, alpha: ok * show(t, b.d4.eighty, b.d5.equity - 0.4), color: C.warn, claims: ['worst_adv_10y'] });
    log.roi['d3.june'] = [dx - 220, dy - 90, dx + 220, dy + 220]; log.roi['d4.eighty'] = [dx - 400, 160, dx + 400, dy + 220];
    const [ex, ey] = O.toScreen(DX - 0.45, eq.top(115374) + 0.08, FZ), [cx, cy] = O.toScreen(DX + 0.45, cash.top(197760) + 0.08, FZ);
    label(O, "buyer's equity $115,374", ex - 30, ey - 20, { align: 'right', kind: 'number', px: 48, alpha: ok * show(t, S.at.equity2, MV.m_idx.t0), color: LIT, claims: ['worst_equity_10y'] });
    label(O, "renter's cash $197,760", cx + 30, cy - 20, { align: 'left', kind: 'number', px: 48, alpha: ok * show(t, S.at.cash2, MV.m_idx.t0), color: C.warn, claims: ['worst_pot_10y'] });
    label(O, 'cash, not stocks', cx + 30, cy + 44, { align: 'left', kind: 'name', px: 40, alpha: ok * show(t, S.at.cash2, MV.m_idx.t0), color: C.muted });
    log.roi['d5.equity'] = [ex - 500, ey - 70, ex + 60, ey + 300]; log.roi['d5.cash'] = [cx - 60, cy - 70, cx + 520, cy + 360];
    const iA = ok * (t > MV.m_idx.t1 && t < MV.m_grid.t0 ? 1 : 0), [zx, zy] = O.toScreen(X(win.length - 1), Y(win[win.length - 1]), RZ), [ox, oy] = O.toScreen(X(0), Y(1), RZ);
    label(O, 'prices up 3.2% in ten years', zx, zy - 50, { align: 'right', kind: 'number', alpha: iA * show(t, b.d6.three), claims: ['worst_price_change_10y'] });
    label(O, 'June 2006', ox, oy + 70, { align: 'left', kind: 'number', px: 44, alpha: iA, color: C.muted, claims: ['worst_start_10y'] });
    label(O, '6.68% rate', 960, 900, { align: 'center', kind: 'number', alpha: iA * show(t, b.d7.six), claims: ['worst_rate_10y'] });
    label(O, 'national index, not one house', 960, 230, { align: 'center', kind: 'name', alpha: iA * show(t, b.d8.national) });
    log.roi['d6.three'] = [ox, 200, zx + 40, oy + 40]; log.roi['d7.six'] = [700, 840, 1220, 920];
    const gA = ok * (t > MV.m_grid.t1 && t < MV.m_w.t0 ? 1 : 0);
    label(O, 'held five years: buyer ahead in 74.4%', 960, 230, { align: 'center', kind: 'number', alpha: gA * show(t, b.d10.seventy, b.d13.every - 0.3), claims: ['share_buyer_ahead_5y'] });
    const [mx, my] = O.toScreen(xOf('2006-05'), 0, zOf('2006-05'));
    label(O, 'May 2006 · $149,392 behind', mx, my + 80, { align: 'center', kind: 'number', px: 48, alpha: gA * mayH, color: C.warn, claims: ['worst_start_5y', 'worst_adv_5y'] });
    label(O, '15 years: every one (100%) · 247 start months', 960, 230, { align: 'center', kind: 'number', alpha: gA * show(t, b.d13.every, b.d15.five - 0.3), claims: ['share_buyer_ahead_15y', 'share_15y_pct', 'n_15y'] });
    label(O, 'weakest: $79,829 ahead', 960, 310, { align: 'center', kind: 'number', px: 48, alpha: gA * show(t, b.d14.weakest, b.d15.five - 0.3), color: LIT, claims: ['worst_adv_15y'] });
    const yrs = Hn === 5 ? 'five years' : Hn === 10 ? 'ten years' : 'fifteen years';
    label(O, `held ${yrs}`, 960, 230, { align: 'center', kind: 'name', px: 64, alpha: gA * show(t, b.d15.five, MV.m_w.t0) });
    const [ax, ay] = O.toScreen(0, 0, 0.9);
    label(O, 'January 1991', ax, ay + 60, { align: 'center', kind: 'number', px: 44, alpha: gA, color: C.muted, claims: ['first_10y'] });
    log.roi['d10.seventy'] = [400, 180, 1520, 900]; log.roi['d11.may'] = [mx - 300, my - 60, mx + 300, my + 120]; log.roi['d13.every'] = [300, 180, 1620, 900];
    log.roi['d15.five'] = [300, 180, 1620, 900];
    const [tx, ty] = O.toScreen(APT.x + 0.3, 0.95, APT.z + 0.66);
    label(O, 'the rent tag: unchanged', tx, ty - 40, { align: 'center', kind: 'name', px: 44, alpha: (cw < 0.05 ? 1 : 0) * show(t, b.d17.tag) });
    log.roi['d17.tag'] = [tx - 260, ty - 100, tx + 260, ty + 140];
    legend(O, gA + (t < MV.m_idx.t0 ? ok : 0));
    const [nx2, ny2] = O.toScreen(NINA.x, 1.3, NINA.z);
    label(O, "how long Nina stays: unknown", nx2, ny2 - 40, { align: 'center', kind: 'name', px: 44, alpha: (cw < 0.05 ? 1 : 0) * show(t, b.d16.nina - 0.3, b.d17.tag - 0.3) });
    chrome(O, {});
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
