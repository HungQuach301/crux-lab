// Tập 8 · ĐOẠN A = S01–S03 + ident (chương 1 "Nina's door"). Phố-lưới chạng vạng chưa sáng → cửa căn hộ của Nina qua cuối phố → đồ thị: tiền thuê
// (renter, warn) thấp hơn tháng đầu của người mua (buyer, lit) → hai chồng tiền để dành + nhà $400,000 → lưới nhìn từ trên: khối 2002–2007 tối, 6 ô
// sáng; lưới 15 năm sáng hết; câu hỏi của Nina → mọi ô hiện, April 2012 sáng / June 2006 tối ("opposite answers") → lưới mọc thành phố (thế giới),
// dòng góc + đối trọng → dọc phố tới Nina + người song sinh ở cửa; ident tối dần.
import { setup, Street, Home8, figure, MoneyStack, nameTag, label, chrome, seg2, dip, chapterCard, legend, followLight, modeLook, show, pulse, ease, lin,
  xOf, zOf, colOf, END_X, APT, NINA, BUY, LIT, C, THREE } from '/episodes/ep008/world/w8.js';

const SEG = '/episodes/ep008/world/seg/a-s01-s03/';
const SX = NINA.x + 1.15, SZ = 0.9;   // hai chồng cạnh Nina (bên phải cô, trước căn hộ)

export async function boot(res) {
  const poses = {
    w0: { pos: [-3.5, 4.2, 8.5], tgt: [14, 0.2, -4.5], fov: 44, chart: 0 },
    wDoor: { pos: [END_X - 1.2, 1.9, 6.4], tgt: [APT.x + 1.2, 0.75, -0.6], fov: 40, chart: 0 },
    cStacks: { pos: [SX - 0.15, 0.95, 16], tgt: [SX - 0.15, 0.95, 0.9], fov: 11, chart: 1 },
    cGrid: { pos: [11.9, 31, 4.5], tgt: [11.9, 0, -5.2], fov: 34, chart: 1 },
    wStreet: { pos: [3.5, 3.6, 7.5], tgt: [12, 0.3, -3.5], fov: 46, chart: 0 },
    wNina: { pos: [END_X - 2.2, 2.0, 6.2], tgt: [NINA.x - 0.2, 0.7, -0.3], fov: 40, chart: 0 },
  };
  const { S, D, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const st10 = DATA.starts10, street = Street(scene, st10), H = Home8(scene);
  const nina = figure(scene, { x: NINA.x, z: NINA.z, lamp: true }), twin = figure(scene, { x: NINA.x + 0.55, z: NINA.z + 0.1, char: 'twin' });
  // chồng: thang riêng của cảnh S01.2 ($150/bó) và S01.3 ($4,000/bó)
  const rent = MoneyStack(scene, { x: SX - 0.45, z: SZ, color: C.warn, unit: 150, name: 'rent-month1' });
  const buy1 = MoneyStack(scene, { x: SX + 0.35, z: SZ, color: LIT, unit: 150, name: 'buyer-month1' });
  const down = MoneyStack(scene, { x: SX - 0.45, z: SZ, color: '#9AA4B2', unit: 8000, name: 'down-payment' });
  const close = MoneyStack(scene, { x: SX + 0.35, z: SZ, color: '#9AA4B2', unit: 8000, name: 'closing-costs' });
  const era = (s) => s >= '2002-01' && s <= '2007-12', ahead = DATA.ahead10['5'];
  const m15 = new Set(DATA.starts15), i12 = st10.indexOf('2012-04'), i06 = st10.indexOf('2006-06');
  const at = S.at;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    nina.lamp.set(1, t); nina.look(t > b.a9.twins ? 0.6 : 0);
    twin.p.visible = t > b.a9.twins - 0.3; twin.p.scale.setScalar(Math.max(0.001, ease(t, b.a9.twins - 0.3, b.a9.twins + 0.2)));
    // S01.2 chồng tiền thuê / tháng đầu người mua; S01.3 hai chồng tiền để dành (thay chỗ)
    const s1 = show(t, MV.m_c1.t0 + 0.3, b.a2.down - 0.6), s2 = show(t, b.a2.down - 0.1, MV.m_grid.t0 + 0.2);
    rent.set({ usd: 1667 * ease(t, MV.m_c1.t0 + 0.4, MV.m_c1.t1 + 0.4), a: s1 });
    buy1.set({ usd: 2933 * ease(t, MV.m_c1.t0 + 0.3, MV.m_c1.t1 + 0.3), a: s1 });
    down.set({ usd: 80000 * ease(t, b.a2.down - 0.1, b.a2.down + 0.5), a: s2 });
    close.set({ usd: 12000 * ease(t, b.a2.down + 0.3, b.a2.down + 0.7), a: s2 });
    // lưới (S02–S03.1): khối 2002–2007 tối ở "seventy-two", 6 ô sáng ở "six"; lưới 15 năm ở "fifteen"; mọi ô ở "every" (S03.1); hai ô ở "same"
    const g72 = ease(t, b.a3.seventy - 0.1, b.a3.seventy + 1.6) * (1 - ease(t, b.a4.fifteen - 0.2, b.a4.fifteen + 0.2)), g6 = ease(t, b.a3.six - 0.1, b.a3.six + 0.4);
    const g15 = ease(t, b.a4.fifteen, b.a4.fifteen + 1.2) * (1 - ease(t, b.a5.wasted - 0.6, b.a5.wasted - 0.2));
    const gAll = ease(t, b.a6.every - 0.1, b.a6.every + 1.4), gPair = ease(t, b.a6.ten - 0.1, b.a6.ten + 0.4);
    const rise = ease(t, MV.m_w.t0, MV.m_w.t1);
    const inGrid = t < MV.m_w.t1;
    street.set({
      vis: (i) => { const s = st10[i]; if (!inGrid) return 1; if (g15 > 0.01) return m15.has(s) ? 1 : 1 - g15; if (t < b.a6.every - 0.1 && t > b.a5.wasted - 0.2) return 0.25; return 1; },
      lit: (i) => { const s = st10[i]; if (g15 > 0.01 && m15.has(s)) return g15; if (era(s) && ahead[i]) return g72 * g6; if (i === i12) return gPair * (1 - rise * 0.6); return 0; },
      dark: (i) => { const s = st10[i]; if (era(s) && !ahead[i]) return g72 * (1 - g15); if (i === i06) return gPair * (1 - rise * 0.6); return 0; },
      hi: (i) => (inGrid ? (era(st10[i]) ? 0.25 * g72 * (1 - g15) : 0) + 0.15 * gAll * (1 - gPair) : (i === 0 ? pulse(t, b.a8.house, 1.2) : 0)),
      cellA: cw * (t > MV.m_grid.t0 ? 1 : 0), rise: () => (inGrid ? (cw > 0.5 ? 0.15 : 1) : 0.15 + 0.85 * rise),
    });
    H.tag.set({ value: 5, swing: 0.05 * Math.sin(t * 1.3) });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 0.66 * ease(t, S.ident[0], S.ident[0] + 1.4));
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    if (t < MV.m_grid.t1 || t > MV.m_w.t0) nameTag(O, nina, t < MV.m_grid.t0 + 0.3 || t > MV.m_w.t1 ? 1 : 0);
    // S01.2: nhãn hai chồng (tên không số) + tỉ lệ ở "smaller", mốc thấp nhất ở "replayed"
    const [rx, ry] = O.toScreen(SX - 0.45, rent.top(1667) + 0.1, SZ), [bx, by] = O.toScreen(SX + 0.35, buy1.top(2933) + 0.1, SZ);
    const la = ok * s1;
    const [, gy] = O.toScreen(SX, 0, SZ);
    label(O, 'rent', rx, gy + 56, { align: 'center', kind: 'name', px: 48, alpha: la, color: C.warn });
    label(O, "buyer's first month", bx + 60, gy + 56, { align: 'center', kind: 'name', px: 48, alpha: la, color: LIT });
    label(O, "rent ÷ buyer's first month: 56.8%", 960, 250, { align: 'center', kind: 'number', alpha: la * show(t, b.a1.smaller), claims: ['today_rent_to_outlay'] });
    label(O, 'lowest replayed: 57.9%', 960, 330, { align: 'center', kind: 'number', px: 48, alpha: la * show(t, b.a1.replayed), claims: ['rent_to_outlay_min_10y'] });
    log.roi['a1.smaller'] = [rx - 120, by - 80, bx + 200, ry + 300]; log.roi['a1.replayed'] = [600, 280, 1320, 350];
    // S01.3: "$80,000 down · $12,000 closing" ở "down", "$400,000 home" ở "four"
    const [dx, dy] = O.toScreen(SX - 0.05, down.top(80000) + 0.15, SZ), lb = ok * s2;
    label(O, '$80,000 down · $12,000 closing', 960, 330, { align: 'center', kind: 'number', alpha: lb * show(t, b.a2.down), claims: ['down_usd', 'closing_usd'] });
    const [hx, hy] = [960, 250];
    label(O, '$400,000 home', 960, 250, { align: 'center', kind: 'number', alpha: lb * show(t, b.a2.four), claims: ['price'] });
    log.roi['a2.down'] = [500, 270, 1420, 350]; log.roi['a2.four'] = [600, 190, 1320, 270];
    // lưới: nhãn
    const gl = ok * (t > MV.m_grid.t1 ? 1 : 0);
    label(O, '6 of 72 start months in a row', 960, 230, { align: 'center', kind: 'number', alpha: gl * show(t, b.a3.six, b.a4.fifteen - 0.3), claims: ['era_2002-2007_share'] });
    label(O, '15 years: every one (100%)', 960, 230, { align: 'center', kind: 'number', alpha: gl * show(t, b.a4.every, b.a5.wasted - 0.5), claims: ['hold_15y', 'share_buyer_ahead_15y', 'share_15y_pct'] });
    label(O, 'Is her rent money wasted?', 960, 560, { align: 'center', kind: 'name', px: 72, alpha: gl * show(t, b.a5.wasted - 0.1, b.a6.every - 0.4) });
    label(O, 'every start month since January 1991 · ten years each', 960, 230, { align: 'center', kind: 'number', px: 48, alpha: gl * show(t, b.a6.every, b.a6.same - 0.3), claims: ['first_10y'] });
    const [p1x, p1y] = O.toScreen(xOf('2012-04'), 0, zOf('2012-04')), [p2x, p2y] = O.toScreen(xOf('2006-06'), 0, zOf('2006-06'));
    label(O, 'same rules · opposite answers', 960, 230, { align: 'center', kind: 'name', alpha: gl * show(t, b.a6.same, MV.m_w.t0) });
    label(O, 'April 2012', p1x, p1y + 70, { align: 'center', kind: 'number', px: 48, alpha: gl * show(t, b.a6.ten + 0.2, MV.m_w.t0), color: LIT, claims: ['best_start_10y'] });
    label(O, 'June 2006', p2x, p2y + 70, { align: 'center', kind: 'number', px: 48, alpha: gl * show(t, b.a6.ten + 0.2, MV.m_w.t0), color: C.warn, claims: ['worst_start_10y'] });
    // dải năm dưới lưới (đầu/cuối) + "data ends July 2026"
    const [ax, ay] = O.toScreen(0, 0, 0.9), [zx] = O.toScreen(25 * 0.95, 0, 0.9), ya = gl * show(t, b.a3.seventy, MV.m_w.t0);
    label(O, 'January 1991', ax, ay + 60, { align: 'center', kind: 'number', px: 48, alpha: ya, color: C.muted, claims: ['first_10y'] });
    label(O, 'July 2016', zx, ay + 60, { align: 'center', kind: 'number', px: 48, alpha: ya, color: C.muted, claims: ['last_10y'] });
    log.roi['a3.seventy'] = [500, 300, 1500, 900]; log.roi['a3.six'] = [500, 180, 1420, 900]; log.roi['a4.every'] = [400, 180, 1520, 900]; log.roi['a6.same'] = [p2x - 120, 280, p1x + 120, p1y + 100];
    legend(O, gl * show(t, b.a3.seventy - 0.3, MV.m_w.t0));
    label(O, 'the street ends where the data ends', zx, ay - 60, { align: 'right', kind: 'name', px: 40, alpha: gl * show(t, b.a4.every, b.a5.wasted - 0.4), color: C.muted });
    // S03.2: dòng góc gạch chân ở "history" + đối trọng (không lời khuyên) lên hình từ đó
    { const c = O.ctx; c.save(); c.font = '600 54px Inter'; const w0 = c.measureText('US only · ').width, wAll = c.measureText('US only · history, not a forecast').width; c.restore();
      seg2(O, 96 + w0, 1024, 96 + wAll, 1024, C.ink, 0.9 * show(t, b.a7.history, b.a8.street), 4); log.roi['a7.history'] = [96 + w0 - 6, 960, 96 + wAll + 6, 1030]; }
    const cwA = show(t, b.a7.history) * (1 - ease(t, S.ident[0], S.ident[0] + 0.6));
    chrome(O, { cw: cwA > 0.01 ? 'Not advice on whether to buy or rent' : null, cwA });
    if (t > b.a9.twins) label(O, 'Nina and her twin: ILLUSTRATIVE', 960, 300, { align: 'center', kind: 'name', px: 48, alpha: show(t, b.a9.twins, S.ident[0]) });
    log.roi['a8.street'] = [200, 300, 1700, 900]; log.roi['a9.twins'] = [700, 300, 1400, 900];
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
