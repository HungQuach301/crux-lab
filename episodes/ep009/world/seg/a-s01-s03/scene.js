// Tập 9 · ĐOẠN A = S01–S03 + ident (chương 1 "Two piles, one street"). Phố chưa sáng + tường 307 cặp cột (nhà / cổ phiếu) → đồ thị tường: about 9 in 10
// → Nina + hộp CASH "$92,000 saved" → phố nhìn cao: bản tiền mặt sáng 3/4 → hộp đổi thành đống N6, bản cổ phiếu sáng nửa → 15 năm: sáng hết → tắt gần
// hết → thế giới: Nina ở cửa, câu hỏi → lùi thấy phố nửa sáng + tường cột → phố hiện lại từng nhà, chú giải → kệ N6: $92,000 + bó mỗi tháng, tụt mà
// bó vẫn rơi; ident tối dần.
import { setup, Street, Home8, figure, GlassBox, StockPile, GrowthPairs, nameTag, label, chrome, seg2, dip, chapterCard, legend, followLight, modeLook,
  show, pulse, ease, lin, sweep, xOf, zOf, colOf, END_X, APT, NINA, BOX, SHELF, LIT, STK, C } from '/episodes/ep009/world/w9.js';

const SEG = `/${new URLSearchParams(location.search).get('seg')}/`;   // đoạn con (re-export) đọc spine.json của chính thư mục nó
const WZ = -12;   // tường cột sau phố

export async function boot(res) {
  const poses = {
    w0: { pos: [12, 3.2, 3.5], tgt: [12, 2.6, -12], fov: 58, chart: 0 },
    cWall: { pos: [12, 3.4, WZ + 22], tgt: [12, 2.6, WZ], fov: 34, chart: 1 },
    cNina: { pos: [(BOX.x + NINA.x) / 2, 1.2, 8.5], tgt: [(BOX.x + NINA.x) / 2, 0.6, 0.4], fov: 26, chart: 1 },
    cStreet: { pos: [17, 17, 14], tgt: [16, 0, -4.5], fov: 44, chart: 1 },
    wNina: { pos: [END_X + 4.2, 1.7, 3.6], tgt: [9, 0.4, -4.5], fov: 46, chart: 0 },
    wWide: { pos: [12, 7.5, 17], tgt: [12, 1.0, -6.5], fov: 46, chart: 0 },
    cPile: { pos: [SHELF.x, 2.0, SHELF.z + 10], tgt: [SHELF.x, 1.7, SHELF.z], fov: 30, chart: 1 },
  };
  const { S, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const st10 = DATA.starts10, n = st10.length, street = Street(scene, st10), H = Home8(scene);
  const nina = figure(scene, { x: NINA.x, z: NINA.z, lamp: true });
  const box = GlassBox(scene, { x: BOX.x, z: BOX.z }), pile = StockPile(scene, {});
  const wall = GrowthPairs(scene, DATA.gS, DATA.gH, { x0: 0, w: 24, z: WZ, unit: 0.9 });
  const cashA = DATA.ahead10.cash, stkA = DATA.ahead10.stocks, none = st10.map(() => false);
  const m15 = new Set(DATA.starts15), i15 = st10.map((s) => DATA.starts15.indexOf(s));
  const c15 = st10.map((s, i) => (i15[i] >= 0 ? DATA.ahead15c[i15[i]] : false)), s15 = st10.map((s, i) => (i15[i] >= 0 ? DATA.ahead15s[i15[i]] : false));
  const T = DATA.traj[DATA.lowStart].stocks;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    nina.lamp.set(1, t); nina.look(t > b.a5.invests - 1 && t < MV.m_wall.t1 ? -0.8 : 0);
    // tường cột: mọc ở "stocks" (S01.1), tô cột cổ phiếu cao hơn ở "nine"; hiện lại ở nghịch lý S03.3; tắt khi xuống phố
    const wA = t < MV.m_st.t1 ? 1 - ease(t, MV.m_st.t0, MV.m_st.t1) : show(t, MV.m_wall.t0, MV.m_c2.t0);
    wall.set({ k: t < MV.m_st.t0 ? ease(t, b.a0.stocks - 0.3, b.a0.stocks + 2.0) : 1, a: wA, hiS: ease(t, b.a0.nine, b.a0.nine + 0.6) });
    // đèn phố: chưa sáng → tiền mặt (ahead) → cổ phiếu (half) → 15 năm: tiền mặt (every) → cổ phiếu (stocks) → cổ phiếu 10 năm (nghịch lý) → hiện lại (S03.5)
    let L;
    if (t < b.a2.ahead - 0.1) L = sweep(none, none, 0, st10);
    else if (t < b.a3.half - 0.1) L = sweep(none, cashA, lin(t, b.a2.ahead - 0.1, b.a2.ahead + 1.4), st10);
    else if (t < b.a4.fifteen) L = sweep(cashA, stkA, lin(t, b.a3.half - 0.1, b.a3.half + 1.4), st10);
    else if (t < b.a4.stocks - 0.1) L = sweep(stkA, c15, lin(t, b.a4.every - 0.2, b.a4.every + 1.0), st10);
    else if (t < MV.m_wall.t0) L = sweep(c15, s15, lin(t, b.a4.stocks - 0.1, b.a4.stocks + 1.2), st10);
    else if (t < b.a8.replayed - 0.1) L = sweep(s15, stkA, lin(t, MV.m_wall.t0, MV.m_wall.t1), st10);
    else L = sweep(none, stkA, lin(t, b.a8.replayed, b.a8.lit), st10);
    const f15 = ease(t, b.a4.fifteen - 0.1, b.a4.fifteen + 0.8) * (1 - ease(t, MV.m_wall.t0, MV.m_wall.t1));
    const reveal = t > b.a8.replayed - 0.2 ? lin(t, b.a8.replayed - 0.2, b.a8.lit) : 1;
    street.set({ ...L, vis: (i) => (m15.has(st10[i]) ? 1 : 1 - f15) * (t > b.a8.replayed - 0.2 ? ease(reveal * 1.1 - colOf(st10[i]) / 26 * 0.1, 0, 1) : 1), cellA: 0 });
    H.tag.set({ value: 5, swing: 0.05 * Math.sin(t * 1.3) });
    // hộp CASH (S02.1 → S02.2) đổi thành đống N6 ở "stocks" (S02.3); đống ở kệ cả phần còn lại
    const sw = ease(t, b.a3.stocks - 0.1, b.a3.stocks + 0.6);
    box.set({ n: 9.2 * ease(t, b.a1.saved - 0.6, b.a1.saved + 0.3), a: (t > MV.m_nina.t0 ? 1 : 0) * (1 - sw), glow: pulse(t, b.a2.cash, 1.0) });
    // đống: $92,000 tới S03.6 "plus", rồi chạy theo tháng (tháng bắt đầu có quỹ thấp nhất) tới hết S03.7
    const k = lin(t, b.a9.plus, b.a10.drop + 0.8) * (T.length - 1), kk = Math.floor(k), fr = k - kk;
    const usd = t < b.a9.plus ? 92000 : T[kk] + (T[Math.min(T.length - 1, kk + 1)] - T[kk]) * fr;
    pile.set({ usd, a: sw * (t < MV.m_w.t0 + 0.4 || t > MV.m_c2.t0 ? 1 : 0.0), line: show(t, b.a9.pile), dropK: t > b.a9.plus && t < b.a10.drop + 0.8 ? fr : -1 });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 0.66 * ease(t, S.ident[0], S.ident[0] + 1.4));
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    // tường (đồ thị): tên cột ở đáy, nhãn tỉ lệ ở "renting"
    const gA = ok * (t < MV.m_nina.t0 + 0.2 ? 1 : 0), [lx, ly] = O.toScreen(0, 0, WZ), [rx] = O.toScreen(24, 0, WZ);
    label(O, 'each pair: one ten-year stretch', 960, 860, { align: 'center', kind: 'name', px: 44, alpha: gA, color: C.muted });
    label(O, 'home prices', lx + 40, ly + 70, { align: 'left', kind: 'name', px: 44, alpha: gA, color: '#C9CED6' });
    label(O, 'stocks', rx - 40, ly + 70, { align: 'right', kind: 'name', px: 44, alpha: gA, color: STK });
    label(O, 'stocks grew more than home prices: about 9 in 10', 960, 230, { align: 'center', kind: 'number', alpha: gA * show(t, b.a1.so), claims: ['share_stocks_beat_house_10y'] });
    log.roi['a1.so'] = [300, 180, 1620, 900];
    // Nina + hộp CASH
    const nA = ok * show(t, MV.m_nina.t1 - 0.2, MV.m_st.t0 + 0.3);
    label(O, '$92,000 saved', 960, 250, { align: 'center', kind: 'number', alpha: nA * show(t, b.a1.saved), claims: ['savings_usd'] });
    const [bx, by] = O.toScreen(BOX.x, 1.0, BOX.z);
    label(O, 'cash', bx, by - 30, { align: 'center', kind: 'name', px: 44, alpha: nA, color: C.warn });
    log.roi['a1.saved'] = [600, 190, 1320, 280];
    // phố nhìn cao: nhãn theo bản
    const sA = ok * (t > MV.m_st.t1 - 0.2 && t < MV.m_w.t0 + 0.2 ? 1 : 0);
    label(O, 'with cash: buyer ahead about 3 out of 4', 960, 230, { align: 'center', kind: 'number', alpha: sA * show(t, b.a2.ahead, b.a3.stocks - 0.1), color: C.warn, claims: ['share_buyer_ahead_cash_10y'] });
    label(O, 'with stocks: about half', 960, 230, { align: 'center', kind: 'number', alpha: sA * show(t, b.a3.stocks, b.a4.fifteen - 0.2), color: STK, claims: ['share_buyer_ahead_stocks_10y'] });
    label(O, '15 years · cash: every one', 960, 230, { align: 'center', kind: 'number', alpha: sA * show(t, b.a4.every, b.a4.stocks - 0.2), color: C.warn, claims: ['hold_15y', 'share_buyer_ahead_cash_15y'] });
    label(O, 'longer stay: the answer flips', 960, 320, { align: 'center', kind: 'name', px: 48, alpha: sA * show(t, b.a4.stocks + 0.6) });
    label(O, '15 years · stocks: about 1 in 5', 960, 230, { align: 'center', kind: 'number', alpha: sA * show(t, b.a4.stocks), color: STK, claims: ['hold_15y', 'share_buyer_ahead_stocks_15y'] });
    const [cx, cy] = O.toScreen(BOX.x, 1.2, BOX.z);
    label(O, sw < 0.5 ? "renter's money: cash" : "renter's money: stocks", cx, cy - 40, { align: 'right', kind: 'name', px: 40, alpha: sA * show(t, b.a2.cash - 0.1), color: sw < 0.5 ? C.warn : STK });
    log.roi['a2.ahead'] = [200, 180, 1720, 900]; log.roi['a3.half'] = [200, 180, 1720, 900]; log.roi['a4.every'] = [200, 180, 1720, 900]; log.roi['a4.stocks'] = [200, 180, 1720, 900];
    legend(O, sA * show(t, b.a2.ahead - 0.2) + (cw < 0.05 ? show(t, b.a8.lit - 0.1, MV.m_c2.t0) : 0));
    // thế giới: câu hỏi (không số)
    if (cw < 0.05) nameTag(O, nina, show(t, MV.m_w.t1 - 0.2, MV.m_wall.t1));
    label(O, 'Rent and invest the difference?', 960, 300, { align: 'center', kind: 'name', px: 64, alpha: (cw < 0.05 ? 1 : 0) * show(t, b.a5.invests, MV.m_wall.t1 + 0.4) });
    log.roi['a5.invests'] = [400, 240, 1520, 340];
    { const c = O.ctx; c.save(); c.font = '600 54px Inter'; const w0 = c.measureText('US only · ').width, wAll = c.measureText('US only · history, not a forecast').width; c.restore();
      seg2(O, 96 + w0, 1024, 96 + wAll, 1024, C.ink, 0.9 * show(t, b.a7.history, b.a8.replayed), 4); log.roi['a7.history'] = [96 + w0 - 6, 960, 96 + wAll + 6, 1030]; }
    // kệ N6
    const pA = ok * (t > MV.m_c2.t1 - 0.2 ? 1 : 0), [px, py] = O.toScreen(SHELF.x + 1.0, pile.lineY(), SHELF.z + 0.55);
    label(O, '$92,000', px + 10, py, { align: 'left', kind: 'number', px: 48, alpha: pA * show(t, b.a9.pile), claims: ['savings_usd'] });
    label(O, '+ the monthly gap', 960, 250, { align: 'center', kind: 'name', px: 52, alpha: pA * show(t, b.a9.plus) });
    label(O, 'every month, even in drops (assumption)', 960, 330, { align: 'center', kind: 'name', px: 48, alpha: pA * show(t, b.a10.market - 0.6) });
    label(O, usd < 92000 ? 'below $92,000 — still adding' : '', 960, 880, { align: 'center', kind: 'number', px: 44, alpha: pA * (t > b.a10.market - 0.6 ? 1 : 0), color: C.warn, claims: ['savings_usd'] });
    label(O, "renting twin's pile: whole US stock market", 960, 880, { align: 'center', kind: 'name', px: 44, alpha: pA * show(t, b.a10.market, S.ident[0]), color: STK });
    log.roi['a9.pile'] = [px, py - 50, px + 300, py + 30]; log.roi['a9.plus'] = [500, 200, 1420, 290];
    const cwA = show(t, b.a2.cash) * (1 - ease(t, S.ident[0], S.ident[0] + 0.6));
    chrome(O, { cw: cwA > 0.01 ? 'Not advice to buy, rent or invest' : null, cwA, illus: t > MV.m_nina.t0 ? 1 : 0 });
    if (t > b.a1.saved - 0.5 && t < MV.m_st.t1) label(O, 'Nina and her twins: ILLUSTRATIVE', 960, 900, { align: 'center', kind: 'name', px: 44, alpha: ok * show(t, b.a1.saved - 0.4, MV.m_st.t0) });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
