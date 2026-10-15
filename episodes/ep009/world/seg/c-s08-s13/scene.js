// Tập 9 · ĐOẠN C = S08–S13 (chương 3 "The lights go out"). Thẻ thuê N2 lật ra 5% + "assumption" → phố (câu hỏi hồi 2) → hai nhà mẫu: cọc vốn > đống
// → sáng; đống > cọc → cửa tối → phố nhìn cao 307 nhà → lô trống của Nina → 1990s sáng phần lớn, nhà đầu tối nhất → 16 tháng quanh 1999 ($1 < $1) vẫn sáng
// → 2000–2007 tối hết, 6 bóng tiền mặt tắt → June 2006 nhấc lên: bóng chồng tiền mặt, đống cổ phiếu cao hơn.
import { setup, Street, Home8, figure, MoneyStack, StockPile, DemoHouse, nameTag, label, chrome, chapterCard, legend, followLight, modeLook,
  show, pulse, ease, lin, xOf, zOf, colOf, mIdx, END_X, APT, NINA, LIT, STK, C } from '/episodes/ep009/world/w9.js';

const SEG = `/${new URLSearchParams(location.search).get('seg')}/`;   // đoạn con (re-export) đọc spine.json của chính thư mục nó
const PS = 0.35, UNIT = 0.07 * 1e5 / PS;

export async function boot(res) {
  const X06 = xOf('2006-06');
  const poses = {
    cTag: { pos: [APT.x + 0.3, 0.8, APT.z + 3.4], tgt: [APT.x + 0.3, 0.62, APT.z + 0.66], fov: 22, chart: 1 },
    wSide: { pos: [12, 2.6, 9.5], tgt: [12, 0.3, -4], fov: 50, chart: 0 },
    wDemo: { pos: [-5.2, 2.1, 8.2], tgt: [-5.2, 0.9, 1.5], fov: 42, chart: 0 },
    cStreet: { pos: [12, 17, 11.5], tgt: [12, 0, -5], fov: 48, chart: 1 },
    cLot: { pos: [END_X + 0.8, 3.0, 7.5], tgt: [NINA.x - 0.6, 0.5, -0.5], fov: 36, chart: 1 },
    c2006: { pos: [X06, 2.6, 9], tgt: [X06, 1.5, -1], fov: 32, chart: 1 },
  };
  const { S, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const st10 = DATA.starts10, n = st10.length, street = Street(scene, st10), H = Home8(scene);
  const nina = figure(scene, { x: NINA.x, z: NINA.z, lamp: true });
  const hA = DemoHouse(scene, { x: -7.6, z: 1.2 }), hB = DemoHouse(scene, { x: -3.6, z: 1.2 });
  const eqA = MoneyStack(scene, { x: -6.5, z: 1.6, color: LIT, unit: UNIT, name: 'demo-equity-a', max: 30 }), pA = StockPile(scene, { x: -5.8, z: 1.6, s: PS, name: 'demo-a' });
  const eqB = MoneyStack(scene, { x: -2.5, z: 1.6, color: LIT, unit: UNIT, name: 'demo-equity-b', max: 30 }), pB = StockPile(scene, { x: -1.8, z: 1.6, s: PS, name: 'demo-b' });
  const T6 = DATA.traj['2006-06'], N = T6.stocks.length - 1, i06 = st10.indexOf('2006-06');
  const cash6 = MoneyStack(scene, { x: X06 - 0.75, z: 1.7, color: C.warn, unit: UNIT, name: 'cash-2006', max: 60 });
  const pile6 = StockPile(scene, { x: X06 + 0.55, z: 1.7, s: PS, name: 'stocks-2006' });
  const A = DATA.ahead10.stocks, AC = DATA.ahead10.cash, lost = DATA.gS.map((g) => g < 1);
  const yr = (i) => +st10[i].slice(0, 4);
  // giờ hiện đèn theo khối (giờ lời): 1990s ở "Most", 2000–2007 ở "dark" (S12.1); sau 2007 chưa hiện (đoạn D)
  const rev = (i, t) => { const y = yr(i), f = (mIdx(st10[i]) - mIdx('1991-01')) / 108;
    if (y <= 1999) return ease(t, b.c6.most + 2.4 * f - 0.15, b.c6.most + 2.4 * f + 0.15);
    if (y <= 2007) { const g = (mIdx(st10[i]) - mIdx('2000-01')) / 96; return ease(t, b.c12.dark + 2.2 * g - 0.15, b.c12.dark + 2.2 * g + 0.15); }
    return 0; };

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    nina.lamp.set(1, t); nina.look(-0.5);
    const ghost = (i) => (yr(i) >= 2002 && yr(i) <= 2007 && AC[i] ? show(t, b.c14.cash, b.c14.out) * 0.8 : 0);
    const up = ease(t, MV.m_06.t0, MV.m_06.t1);
    street.set({
      lit: (i) => rev(i, t) * (A[i] ? 1 : 0) + ghost(i),
      dark: (i) => rev(i, t) * (A[i] ? 0 : 1) * (1 - ghost(i)),
      hi: (i) => (i === 0 ? pulse(t, b.c7.first, 1.6) : 0) + (lost[i] ? 0.8 * show(t, b.c10.less, b.c12.dark) : 0) + (i === i06 ? 0.5 * pulse(t, b.c18.darker, 1.2) : 0),
      lift: (i) => (i === i06 ? 1.3 * up : 0), big: (i) => (i === i06 ? 1 + 0.8 * up : 1), cellA: 0,
    });
    // thẻ N2: lật ra ở "tag" (swing), giữ 5%
    H.tag.set({ value: 5, swing: 0.5 * (1 - ease(t, b.c0.tag, b.c0.tag + 0.8)) * Math.sin(t * 7) });
    // hai nhà mẫu (S09.1–S09.2)
    const dA = show(t, MV.m_demo.t0, MV.m_c1.t1);
    hA.set({ lit: ease(t, b.c2.lit - 0.1, b.c2.lit + 0.4), a: dA }); hB.set({ dark: ease(t, b.c3.dark - 0.1, b.c3.dark + 0.4), a: dA });
    eqA.set({ usd: 400000 * ease(t, b.c2.equity - 0.3, b.c2.equity + 0.5), a: dA }); pA.set({ usd: 260000 * ease(t, b.c2.equity, b.c2.equity + 0.8), a: dA, line: 0 });
    eqB.set({ usd: 260000 * ease(t, b.c2.equity + 0.6, b.c3.dark), a: dA }); pB.set({ usd: 430000 * ease(t, b.c2.equity + 0.8, b.c3.dark + 0.2), a: dA, line: 0 });
    // June 2006: bóng tiền mặt ở "cash", đống cổ phiếu ở "stocks"
    const g6 = show(t, MV.m_06.t0, S.total + 1);
    cash6.set({ usd: T6.cash[N] * ease(t, b.c16.cash - 0.1, b.c16.cash + 0.6), a: 0.55 * g6 });
    pile6.set({ usd: 92000 + (T6.stocks[N] - 92000) * ease(t, b.c17.stocks - 0.1, b.c17.quarter + 0.4), a: g6 * ease(t, b.c17.stocks - 0.3, b.c17.stocks), line: 1 });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    const tA = ok * (t < MV.m_w1.t0 + 0.2 ? 1 : 0);
    label(O, 'rent tag: 5% of the price a year · July 2026 · assumption', 960, 240, { align: 'center', kind: 'number', px: 52, alpha: tA * show(t, b.c0.five), claims: ['yield_anchor_pct', 'hpi_last'] });
    log.roi['c0.five'] = [200, 190, 1720, 290];
    if (cw < 0.05) nameTag(O, nina, show(t, 0, MV.m_demo.t0) * 0);
    label(O, 'with the pile in stocks: how much of the street stays lit?', 960, 300, { align: 'center', kind: 'name', px: 52, alpha: (cw < 0.05 ? 1 : 0) * show(t, b.c1.street - 0.3, MV.m_demo.t1) });
    // nhà mẫu (thế giới, không số)
    const [ax, ay] = O.toScreen(-6.6, 0, 1.6), [bx] = O.toScreen(-2.6, 0, 1.6), wd = (cw < 0.05 ? 1 : 0) * dA;
    label(O, "buyer's equity bigger → lit", ax, ay + 60, { align: 'center', kind: 'name', px: 40, alpha: wd * show(t, b.c2.lit), color: LIT });
    label(O, "renter's pile bigger → dark", bx, ay + 60, { align: 'center', kind: 'name', px: 40, alpha: wd * show(t, b.c3.dark), color: STK });
    log.roi['c2.lit'] = [ax - 300, ay - 300, ax + 300, ay + 100]; log.roi['c3.dark'] = [bx - 300, ay - 300, bx + 300, ay + 100];
    // phố nhìn cao
    const sA = ok * (t > MV.m_c1.t1 - 0.2 && (t < MV.m_n.t0 || t > MV.m_s.t1 - 0.2) && t < MV.m_06.t0 + 0.2 ? 1 : 0);
    const [fx, fy] = O.toScreen(0, 0, 1.2), [lx] = O.toScreen(25 * 0.95, 0, 1.2);
    label(O, '307 start months', 960, 230, { align: 'center', kind: 'number', alpha: sA * show(t, b.c4.three, b.c6.most - 0.3), claims: ['n_10y'] });
    label(O, 'January 1991', fx, fy + 50, { align: 'center', kind: 'number', px: 44, alpha: sA * show(t, b.c4.july, MV.m_06.t0), color: C.muted, claims: ['first_10y'] });
    label(O, 'July 2016', lx, fy + 50, { align: 'center', kind: 'number', px: 44, alpha: sA * show(t, b.c4.july, MV.m_06.t0), color: C.muted, claims: ['last_10y'] });
    log.roi['c4.three'] = [600, 180, 1320, 270]; log.roi['c4.july'] = [fx - 200, fy, lx + 200, fy + 90];
    label(O, "Nina's month: not on the street yet", 960, 260, { align: 'center', kind: 'name', px: 52, alpha: ok * show(t, b.c5.nina, MV.m_s.t0 + 0.3) });
    label(O, '1990s: about 2 in 3 lit', 960, 230, { align: 'center', kind: 'number', alpha: sA * show(t, b.c6.two, b.c7.darkest - 0.2), claims: ['era_1990s_span', 'era_1990s_share_stocks'] });
    const [hx, hy] = O.toScreen(0, 0.8, 0);
    label(O, 'darkest: January 1991', hx + 40, hy - 50, { align: 'left', kind: 'number', px: 48, alpha: sA * show(t, b.c7.first, b.c9.stalled - 0.2), color: STK, claims: ['worst_start_stocks_10y'] });
    label(O, '16 start months: $1 ended below $1 · all 16 stay lit', 960, 230, { align: 'center', kind: 'number', px: 50, alpha: sA * show(t, b.c10.less, b.c12.dark - 0.2), claims: ['n_stocks_lost_10y', 'n_stocks_lost_buyer_ahead_10y'] });
    label(O, '2002 to 2007: none of 72', 960, 230, { align: 'center', kind: 'number', alpha: sA * show(t, b.c13.none, b.c14.cash - 0.2), color: STK, claims: ['era_2002-2007_span', 'era_2002-2007_share_stocks'] });
    label(O, 'with cash: 6 of 72', 960, 230, { align: 'center', kind: 'number', alpha: sA * show(t, b.c14.cash, MV.m_06.t0), color: C.warn, claims: ['era_2002-2007_share_cash'] });
    log.roi['c6.two'] = [500, 180, 1420, 900]; log.roi['c10.less'] = [300, 180, 1620, 900]; log.roi['c13.none'] = [500, 180, 1420, 900];
    legend(O, sA * show(t, b.c6.most - 0.3));
    // June 2006
    const jA = ok * (t > MV.m_06.t1 - 0.2 ? 1 : 0);
    label(O, 'June 2006 · with cash: $82,385 behind', 960, 240, { align: 'center', kind: 'number', px: 52, alpha: jA * show(t, b.c16.cash), color: C.warn, claims: ['adv_2006-06_cash_10y'] });
    label(O, 'with stocks: $261,689 behind', 960, 320, { align: 'center', kind: 'number', px: 56, alpha: jA * show(t, b.c17.quarter), color: STK, claims: ['adv_2006-06_stocks_10y'] });
    log.roi['c16.cash'] = [400, 190, 1520, 280]; log.roi['c17.quarter'] = [460, 270, 1460, 360];
    chrome(O, { illus: 1 });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
