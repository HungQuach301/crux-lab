// Tập 9 · ĐOẠN B = S04–S06 (chương 2 "The first house"). Nhà January 1991 → đồ thị: cọc vốn người mua > hộp tiền mặt → đống cổ phiếu N6 vượt lên
// (số neo S04.3), cửa tối → đường $1 (1991) gần 5 lần → đống = $92,000 + bó mỗi tháng → nhà đầu phố sáng → tối → một mức tăng cố định vs bản ghi thật
// → thẻ V7 "Same costs as before" (giữ + MR1).
import { setup, Street, Home8, figure, MoneyStack, StockPile, Line, nameTag, label, chrome, v7Card, chapterCard, legend, followLight, modeLook,
  show, pulse, ease, lin, xOf, zOf, LIT, STK, C } from '/episodes/ep009/world/w9.js';

const SEG = `/${new URLSearchParams(location.search).get('seg')}/`;   // đoạn con (re-export) đọc spine.json của chính thư mục nó
const SZ = 1.3, XB = -2.7, XC = -1.95, XP = -1.0, PS = 0.35, UNIT = 0.07 * 1e5 / PS;   // cùng thang: $ → chiều cao như đống N6 (s = PS)
const LX = -36, LW = 12, LY = 0.3, LSY = 0.62;   // vùng đồ thị đường $1

export async function boot(res) {
  const poses = {
    wHouse: { pos: [-0.6, 0.75, 3.2], tgt: [0.2, 0.45, 0], fov: 40, chart: 0 },
    cHouse: { pos: [-1.3, 1.6, 10.5], tgt: [-1.3, 1.45, SZ], fov: 24, chart: 1 },
    cLines: { pos: [LX + LW / 2, LY + 1.7, 16], tgt: [LX + LW / 2, LY + 1.7, -2], fov: 26, chart: 1 },
  };
  const { S, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const st10 = DATA.starts10, street = Street(scene, st10), H = Home8(scene);
  const T = DATA.traj['1991-01'], N = T.stocks.length - 1;
  const buy = MoneyStack(scene, { x: XB, z: SZ, color: LIT, unit: UNIT, name: 'buyer-equity', max: 60 });
  const cash = MoneyStack(scene, { x: XC, z: SZ, color: C.warn, unit: UNIT, name: 'renter-cash', max: 60 });
  const pile = StockPile(scene, { x: XP, z: SZ, s: PS, name: 'renter-stocks-1991' });
  const real = Line(scene, DATA.g1991, { x0: LX, w: LW, y0: LY, sy: LSY, color: STK, width: 0.06 });
  const g1 = DATA.g1991[N], fix = DATA.g1991.map((_, k) => Math.pow(g1, k / N));
  const flat = Line(scene, fix, { x0: LX, w: LW, y0: LY, sy: LSY, color: C.muted, width: 0.05, z: -2.02 });
  const lit = DATA.ahead10.stocks.map((a, i) => (i === 0 ? 0 : a ? 1 : 0)), dark = DATA.ahead10.stocks.map((a, i) => (i === 0 ? 0 : a ? 0 : 1));

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    // nhà đầu phố: sáng (bản tiền mặt) tới "behind", tối sau đó; S05.4 lặp lại sáng → tối
    const d0 = t < b.b7.lit - 0.2 ? ease(t, b.b2.behind, b.b2.behind + 0.6) : ease(t, b.b7.dark - 0.1, b.b7.dark + 0.5);
    street.set({ lit: (i) => (i === 0 ? 1 - d0 : 0.35 * lit[i]), dark: (i) => (i === 0 ? d0 : 0.35 * dark[i]), hi: (i) => (i === 0 ? pulse(t, b.b0.january, 1.2) : 0), cellA: 0 });
    H.tag.set({ value: 5 });
    // cọc / hộp / đống (cuối 10 năm, 1991-01) — mọc ở cue; đống chạy lại theo tháng ở S05.2–S05.3
    const a1 = show(t, MV.m_c1.t0, MV.m_g.t0 + 0.3) + show(t, MV.m_p.t1 - 0.3, MV.m_w.t1);
    buy.set({ usd: T.eq[N] * ease(t, b.b1.cash - 0.2, b.b1.cash + 0.6), a: Math.min(1, a1) });
    cash.set({ usd: T.cash[N] * ease(t, b.b1.cash, b.b1.cash + 0.8), a: Math.min(1, a1) });
    let usd = 92000 + (T.stocks[N] - 92000) * ease(t, b.b2.stocks - 0.1, b.b2.stocks + 1.6), dk = -1;
    if (t > MV.m_p.t0) { const k = lin(t, b.b5.day, b.b6.grew + 0.6) * N, kk = Math.floor(k); usd = T.stocks[kk] + (T.stocks[Math.min(N, kk + 1)] - T.stocks[kk]) * (k - kk); dk = t > b.b5.deposit - 0.4 && t < b.b6.grew + 0.6 ? k - kk : -1; }
    pile.set({ usd, a: Math.min(1, a1), line: t > MV.m_p.t0 ? 1 : 0, dropK: dk });
    real.draw(t < MV.m_c2.t0 ? lin(t, b.b4.dollar - 0.2, b.b4.five + 0.3) : lin(t, b.b8.actually - 0.3, b.b8.actually + 1.6), show(t, MV.m_g.t0, MV.m_p.t1) + show(t, MV.m_c2.t0));
    flat.draw(lin(t, b.b8.one - 0.2, b.b8.one + 1.2), show(t, b.b8.one - 0.2));
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    const [hx, hy] = O.toScreen(0, 0.9, 0);
    label(O, 'the first house', hx, hy - 30, { align: 'center', kind: 'name', px: 48, alpha: (cw < 0.05 ? 1 : 0) * show(t, b.b0.first, MV.m_c1.t0) });
    const hA = ok * (t < MV.m_g.t0 + 0.2 || (t > MV.m_p.t1 - 0.2 && t < MV.m_w.t0 + 0.2) ? 1 : 0);
    label(O, 'January 1991', 960, 240, { align: 'center', kind: 'number', px: 52, alpha: hA * show(t, MV.m_c1.t1 - 0.3, b.b2.stocks - 0.3), claims: ['first_10y'] });
    const [bx, by] = O.toScreen(XB, 0, SZ), [cx] = O.toScreen(XC, 0, SZ), [px] = O.toScreen(XP, 0, SZ);
    const nm = hA * (t < MV.m_g.t0 ? 1 : 0);
    label(O, "buyer's equity", bx - 20, by + 50, { align: 'center', kind: 'name', px: 40, alpha: nm * show(t, b.b1.cash), color: LIT });
    label(O, 'cash', cx, by + 50, { align: 'center', kind: 'name', px: 40, alpha: nm * show(t, b.b1.cash), color: C.warn });
    label(O, 'stocks', px + 30, by + 50, { align: 'center', kind: 'name', px: 40, alpha: nm * show(t, b.b2.stocks), color: STK });
    label(O, 'with cash: $48,410 ahead', 960, 320, { align: 'center', kind: 'number', px: 52, alpha: hA * show(t, b.b1.ahead, b.b2.stocks - 0.3), color: C.warn, claims: ['adv_1991-01_cash_10y'] });
    label(O, 'with stocks: $485,063 behind', 960, 320, { align: 'center', kind: 'number', px: 56, alpha: hA * show(t, b.b2.behind, MV.m_g.t0), color: STK, claims: ['adv_1991-01_stocks_10y'] });
    label(O, 'same house, same mortgage, same rent', 960, 880, { align: 'center', kind: 'name', px: 44, alpha: hA * show(t, b.b3.only - 0.4, MV.m_g.t0) });
    log.roi['b1.ahead'] = [500, 270, 1420, 360]; log.roi['b2.behind'] = [460, 270, 1460, 360];
    const lA = ok * (t > MV.m_g.t1 - 0.2 && t < MV.m_p.t0 + 0.2 ? 1 : 0), [ex, ey] = O.toScreen(LX + LW, LY + g1 * LSY, -2), [sx, sy] = O.toScreen(LX, LY + LSY, -2);
    label(O, '$1', sx - 20, sy, { align: 'right', kind: 'number', px: 48, alpha: lA, claims: [] });
    label(O, '$1 in 1991 → almost 5 times', 960, 240, { align: 'center', kind: 'number', px: 52, alpha: lA * show(t, b.b4.five), color: STK, claims: ['stocks_growth_1991-01_10y'] });
    log.roi['b4.five'] = [480, 190, 1440, 280];
    label(O, '$92,000 on day one', 960, 240, { align: 'center', kind: 'number', px: 52, alpha: hA * show(t, b.b5.day, MV.m_w.t0), claims: ['savings_usd'] });
    label(O, '+ a deposit every month', 960, 320, { align: 'center', kind: 'name', px: 48, alpha: hA * show(t, b.b5.deposit, MV.m_w.t0) });
    // B09: un đường thẳng (mức cố định) vs bản ghi thật
    const fA = ok * (t > MV.m_c2.t1 - 0.2 ? 1 : 0), [fx, fy] = O.toScreen(LX + LW * 0.55, LY + fix[66] * LSY, -2), [rx2, ry2] = O.toScreen(LX + LW * 0.62, LY + DATA.g1991[74] * LSY, -2);
    label(O, 'one fixed growth rate', fx + 20, fy + 50, { align: 'left', kind: 'name', px: 44, alpha: fA * show(t, b.b8.one, S.card[0] - 0.2), color: '#C9CED6' });
    label(O, 'the real record, month by month', rx2 - 40, ry2 - 60, { align: 'right', kind: 'name', px: 44, alpha: fA * show(t, b.b8.actually, S.card[0] - 0.2), color: STK });
    log.roi['b8.one'] = [fx, fy, fx + 600, fy + 90]; log.roi['b8.actually'] = [rx2 - 760, ry2 - 110, rx2, ry2 - 10];
    v7Card(O, 'Same costs as before', ['$400,000 home · $92,000 = down payment + closing', 'mortgage, tax, insurance, repairs: 2.5% a year', 'cost of selling: 6%'],
      ok * show(t, S.card[0], S.total + 1));
    legend(O, (cw < 0.05 ? 1 : 0) * show(t, b.b7.lit - 0.3, MV.m_c2.t0));
    chrome(O, { illus: 1 });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
