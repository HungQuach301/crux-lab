// Tập 9 · ĐOẠN F = S22–S25 (chương 6 "The tag on her door" + giới hạn + kết). Cận thẻ thuê, phố sau: thẻ lật 4% → 6% → 5%, đèn quét (nửa) → 5.1% điểm
// lật; Census 4.83% / 5.59% hai phía → cửa Nina, đèn trong cửa sổ, những thứ không đo → thẻ giới hạn → bảng điểm 4 dòng → khung 0:00 nửa sáng → lô
// trống của Nina → Nina cạnh cửa, thẻ đung đưa.
import { setup, Street, Home8, figure, RentTag, GrowthPairs, StockPile, nameTag, label, chrome, v7Card, chapterCard, legend, followLight, modeLook,
  show, pulse, ease, lin, sweep, END_X, APT, NINA, LIT, STK, C } from '/episodes/ep009/world/w9.js';

const SEG = `/${new URLSearchParams(location.search).get('seg')}/`;   // đoạn con (re-export) đọc spine.json của chính thư mục nó
export const STOCK_SRC = ['Stock returns: Kenneth R. French Data Library (Fama/French factors, total return);', 'cross-checked with Robert Shiller data.'];   // chủ dự án 15/10 (G1 câu 1 sửa)

export async function boot(res) {
  const poses = {
    cTag: { pos: [APT.x + 1.5, 0.8, APT.z + 2.6], tgt: [APT.x - 7, 0.4, -4], fov: 42, chart: 1 },
    wDoor: { pos: [APT.x + 0.9, 1.0, APT.z + 3.4], tgt: [APT.x + 0.5, 0.65, APT.z + 0.6], fov: 32, chart: 0 },
    cGrid: { pos: [11.9, 30, 3.0], tgt: [11.9, 0, -5.2], fov: 36, chart: 1 },
    w0: { pos: [12, 3.2, 3.5], tgt: [12, 2.6, -12], fov: 58, chart: 0 },   // = đoạn A, khung 0:00
    wLot: { pos: [END_X + 0.2, 1.7, 5.4], tgt: [NINA.x + 0.6, 0.5, -0.8], fov: 42, chart: 0 },
  };
  const { S, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const st10 = DATA.starts10, street = Street(scene, st10), H = Home8(scene);
  const nina = figure(scene, { x: NINA.x, z: NINA.z, lamp: true }), tag = RentTag(scene);
  const wall = GrowthPairs(scene, DATA.gS, DATA.gH, { x0: 0, w: 24, z: -12, unit: 0.9 });
  const pile = StockPile(scene, {});
  const Y = DATA.ahead10y, AS = DATA.ahead10.stocks;
  // lịch lật thẻ (giờ đoạn): [t, chữ thẻ, mảng đèn]
  const t0 = b.f0.tag, seq = [[t0 + 0.4, '4%', Y['4.0']], [t0 + 1.6, '6%', Y['6.0']], [b.f1.five, '5%', Y['5.0']], [b.f2.five, '5.1%', Y['5.06']],
    [b.f2.census, '4.83%', Y['4.83']], [b.f2.census + 1.6, '5.59%', Y['5.59']], [b.f3.tag, '5%', Y['5.0']]];

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    nina.lamp.set(1, t); nina.look(t > MV.m_door.t0 ? 0.4 : -0.5);
    let k = -1; for (let i = 0; i < seq.length; i++) if (t >= seq[i][0]) k = i;
    const prev = k > 0 ? seq[k - 1][2] : AS, cur = k >= 0 ? seq[k][2] : AS, kk = k >= 0 ? lin(t, seq[k][0], seq[k][0] + 1.0) : 1;
    // S25.2: phố sau bảng điểm đổi đèn theo từng dòng (tiền mặt → cổ phiếu → 15 năm); trước đó theo lịch lật thẻ
    const AC = DATA.ahead10.cash, m15 = new Set(DATA.starts15), s15 = st10.map((s) => { const j = DATA.starts15.indexOf(s); return j >= 0 ? DATA.ahead15s[j] : false; });
    let L = t < MV.m_w2.t0 ? sweep(prev, cur, kk, st10) : sweep(AS, AS, 1, st10);
    if (t > b.f8.cash - 0.2 && t < MV.m_w2.t0) L = t < b.f8.stocks ? sweep(AS, AC, lin(t, b.f8.cash - 0.2, b.f8.cash + 0.8), st10) : t < b.f8.fifteen ? sweep(AC, AS, lin(t, b.f8.stocks - 0.2, b.f8.stocks + 0.8), st10) : sweep(AS, s15, lin(t, b.f8.fifteen - 0.2, b.f8.fifteen + 0.8), st10);
    street.set({ ...L, cellA: cw * (t > MV.m_c.t1 - 0.3 && t < MV.m_w2.t0 ? 1 : 0) });
    H.tag.set({ a: 0 });
    tag.set({ text: k >= 0 && t < MV.m_w2.t0 ? seq[k][1] : '5%', flip: k >= 0 ? ease(t, seq[k][0] - 0.3, seq[k][0]) : 0, swing: 0.06 * Math.sin(t * 1.4) * (t > MV.m_door.t0 ? 1.5 : 1) });
    wall.set({ k: 1, a: show(t, MV.m_w2.t0, MV.m_lot.t1) });
    pile.set({ a: 0 });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    const tA = ok * (t < MV.m_w.t0 + 0.2 ? 1 : 0);
    label(O, "rent tag: the renter's yearly rent as a % of the price", 960, 900, { align: 'center', kind: 'name', px: 44, alpha: tA * show(t, b.f0.tag, b.f1.five) });
    label(O, '5%: about half lit', 960, 240, { align: 'center', kind: 'number', alpha: tA * show(t, b.f1.half, b.f2.five - 0.2), claims: ['yield5_tag', 'share_buyer_ahead_stocks_10y'] });
    label(O, 'flip point: about 5.1%', 960, 240, { align: 'center', kind: 'number', alpha: tA * show(t, b.f2.five, b.f2.census - 0.2), claims: ['flip_yield_stocks_10y'] });
    label(O, 'Census range: 4.83% to 5.59% a year · 47.2% to 58.3% lit', 960, 320, { align: 'center', kind: 'number', px: 46, alpha: tA * show(t, b.f2.both, MV.m_w.t0),
      claims: ['hvs_yield_2025Q4', 'hvs_yield_2026Q1', 'share_hvs_2025Q4_stocks_10y', 'share_hvs_2026Q1_stocks_10y'] });
    label(O, 'the tag is an assumption', 960, 900, { align: 'center', kind: 'name', px: 48, alpha: tA * show(t, b.f3.assumption) });
    log.roi['f1.half'] = [200, 180, 1720, 950]; log.roi['f2.both'] = [200, 180, 1720, 950];
    legend(O, tA * show(t, t0));
    if (cw < 0.05) nameTag(O, nina, show(t, MV.m_w.t1 - 0.3, MV.m_c.t0) + show(t, MV.m_lot.t1 - 0.3));
    label(O, 'not ranked: stocks vs a house', 960, 240, { align: 'center', kind: 'name', px: 52, alpha: (cw < 0.05 ? 1 : 0) * show(t, b.f4.none, b.f5.stability - 0.2) });
    label(O, 'not measured: stability, control', 960, 240, { align: 'center', kind: 'name', px: 52, alpha: (cw < 0.05 ? 1 : 0) * show(t, b.f5.stability, MV.m_c.t0) });
    const LIM = ['US only', 'history, not a forecast', 'no taxes on gains or on the home', 'renters who never skip a month'];   // đúng 4 giới hạn đã nói, hiện theo lời (M5: chỗ muốn tua S24)
    const lA = ok * show(t, b.f6.card, b.f7.back - 0.2);
    v7Card(O, 'Limits', LIM.slice(0, t < b.f6.taxes ? 2 : t < b.f6.renters ? 3 : 4), lA, { y: 200, w: 1100, x: 410 });
    STOCK_SRC.forEach((s, i) => label(O, s, 960, 760 + 48 * i, { align: 'center', kind: 'name', px: 36, alpha: lA, color: C.muted, plate: null }));
    // bảng điểm (B33): mỗi dòng một màu lựa chọn, không phán quyết
    const sb = ok * show(t, b.f7.back, MV.m_w2.t0);
    if (sb > 0.01) { O.card(170, 190, 1580, 470, { fill: '#141922', stroke: C.muted, lw: 3, alpha: 0.88 * sb });
      label(O, "Nina's question, replayed", 220, 270, { kind: 'title', px: 52, alpha: sb, plate: null, role: 'title' });
      const rows = [['cash: buyer ahead about 3 in 4 · 15 years: every one', C.warn, b.f8.cash, ['share_buyer_ahead_cash_10y', 'hold_15y', 'share_buyer_ahead_cash_15y']],
        ['stocks: about half (152 of 307) · 15 years: about 1 in 5', STK, b.f8.stocks, ['share_buyer_ahead_stocks_10y', 'share_buyer_ahead_stocks_10y_n', 'hold_15y', 'share_buyer_ahead_stocks_15y']],
        ['only the $92,000 invested: about 2 in 3', STK, b.f8.stocks + 0.8, ['savings_usd', 'share_buyer_ahead_lump_10y']],
        ['what tips it: the rent tag (flip about 5.1% vs 5 percent assumed)', '#D5DAE2', b.f8.fifteen, ['flip_yield_stocks_10y', 'yield_anchor_pct']]];
      rows.forEach(([s, c, tt, cl], i) => label(O, s, 230, 350 + 85 * i, { kind: 'number', px: 44, alpha: sb * show(t, tt), plate: null, color: c, claims: cl })); }
    log.roi['f8.cash'] = [170, 200, 1750, 760];
    label(O, 'same street as the start · pile in the market', 960, 240, { align: 'center', kind: 'name', px: 48, alpha: (cw < 0.05 ? 1 : 0) * show(t, b.f9.same, MV.m_lot.t0) });
    label(O, "Nina's own month: not on this street", 960, 240, { align: 'center', kind: 'name', px: 52, alpha: (cw < 0.05 ? 1 : 0) * show(t, b.f10.how, MV.m_door.t0) });
    legend(O, (cw < 0.05 ? 1 : 0) * show(t, b.f9.same, MV.m_lot.t0));
    chrome(O, { illus: 1 });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
