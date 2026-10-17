// Tập 9 · ĐOẠN D = S14–S18 (chương 4 "The pile that sank"). Hàng 307 đống nhỏ (đáy thấp nhất mỗi cửa sổ) + vạch $92,000: 183 tụt dưới → kệ N6 ngang
// tầm mắt: đống November 2007 tụt tới $54,310, người thuê vẫn đặt bó (đỉnh) → phố nhìn thẳng từ trên: nửa sáng (lõi) → 80 nhà sáng → tối → April 2012 nhấc
// lên, vẫn sáng → khối 2009–2016 sáng phần lớn → ba cột 5 / 10 / 15 năm → phố 15 năm: tiền mặt sáng hết → cổ phiếu tắt gần hết.
import { setup, Street, Home8, figure, MoneyStack, StockPile, nameTag, label, chrome, chapterCard, legend, followLight, modeLook,
  show, pulse, ease, lin, mix, xOf, zOf, colOf, SHELF, END_X, NINA, LIT, STK, C, THREE } from '/episodes/ep009/world/w9.js';

const SEG = `/${new URLSearchParams(location.search).get('seg')}/`;   // đoạn con (re-export) đọc spine.json của chính thư mục nó
const BX = -40, BW = 14, BZ = -2, BU = 1 / 1e5;   // hàng đống nhỏ: x = tháng, cao = $ × BU
const PS = 0.35, UNIT = 0.07 * 1e5 / PS;

export async function boot(res) {
  const X12 = xOf('2012-04');
  const poses = {
    cBars: { pos: [BX + BW / 2, 1.2, BZ + 17], tgt: [BX + BW / 2, 0.9, BZ], fov: 34, chart: 1 },   // M6 C07: khung rộng hơn, cả hàng trong khung
    cShelf: { pos: [SHELF.x + 0.4, 1.0, SHELF.z + 5.2], tgt: [SHELF.x, 0.85, SHELF.z], fov: 30, chart: 1 },
    cGrid: { pos: [11.9, 30, 3.0], tgt: [11.9, 0, -5.2], fov: 36, chart: 1 },
    c2012: { pos: [X12, 2.6, 9], tgt: [X12, 1.5, -1], fov: 32, chart: 1 },
  };
  const { S, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const st10 = DATA.starts10, n = st10.length, street = Street(scene, st10), H = Home8(scene);
  const nina = figure(scene, { x: NINA.x, z: NINA.z, lamp: true });
  const twin = figure(scene, { x: SHELF.x - 1.25, z: SHELF.z + 0.3, char: 'twin' });
  // hàng đống nhỏ (InstancedMesh): mỗi cửa sổ một cột, cao = $92,000 → tụt xuống đáy thấp nhất (low10) ở "dipped"
  const g = new THREE.BoxGeometry(BW / n * 0.7, 1, 0.3), bars = new THREE.InstancedMesh(g, new THREE.MeshStandardMaterial({ color: STK, roughness: 0.7, transparent: true }), n);
  bars.frustumCulled = false; scene.add(bars); bars.userData.checks = { role: 'bar', orient: 'v', series: 'lowest-pile', key: 'low-piles' };
  const line = new THREE.Mesh(new THREE.BoxGeometry(BW + 0.6, 0.02, 0.35), new THREE.MeshStandardMaterial({ color: C.ink, transparent: true })); line.position.set(BX + BW / 2, 92000 * BU, BZ + 0.05); scene.add(line);
  const M4 = new THREE.Matrix4(), col = new THREE.Color(), BX_ = (i) => BX + BW * i / (n - 1);
  const pile = StockPile(scene, {}), TL = DATA.traj[DATA.lowStart], li = TL.lowIdx;
  pile.children[3].material.color.set('#9AA4B2');   // vạch $92,000: xám trung (1080 + cine: ink #F2F4F7 đảo độ sáng với đai bó #E9E3D3 — bước cine CHẶN 16/10)
  const i12 = st10.indexOf('2012-04'), T12 = DATA.traj['2012-04'], N = T12.stocks.length - 1;
  const eq12 = MoneyStack(scene, { x: X12 - 0.75, z: 1.7, color: LIT, unit: UNIT, name: 'equity-2012', max: 60 });
  const pile12 = StockPile(scene, { x: X12 + 0.55, z: 1.7, s: PS, name: 'stocks-2012' });
  const A = DATA.ahead10.stocks, AC = DATA.ahead10.cash, flip = A.map((a, i) => AC[i] && !a);
  const m15 = new Set(DATA.starts15), i15 = st10.map((s) => DATA.starts15.indexOf(s));
  const c15 = st10.map((s, i) => (i15[i] >= 0 ? DATA.ahead15c[i15[i]] : false)), s15 = st10.map((s, i) => (i15[i] >= 0 ? DATA.ahead15s[i15[i]] : false));
  const late = (i) => st10[i] >= '2009-01';

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    nina.lamp.set(1, t); nina.look(-0.6);
    // hàng đống nhỏ
    const kd = ease(t, b.d1.dipped - 0.2, b.d1.dipped + 1.4), bA = show(t, 0, MV.m_sh.t1);
    for (let i = 0; i < n; i++) { const v = mix(92000, DATA.low10[i], kd); M4.makeScale(1, Math.max(1e-3, v * BU), 1).setPosition(BX_(i), v * BU / 2, BZ); bars.setMatrixAt(i, M4);
      col.set(STK).lerp(new THREE.Color(C.warn), DATA.below10[i] ? 0.7 * kd : 0); bars.setColorAt(i, col); }
    bars.instanceMatrix.needsUpdate = true; if (bars.instanceColor) bars.instanceColor.needsUpdate = true;
    bars.material.opacity = bA; bars.visible = bA > 0.01; line.material.opacity = bA; line.visible = bA > 0.01;
    // kệ N6: đống November 2007 chạy theo tháng tới đáy ở "sank"; sau đáy bó vẫn rơi (S14.3 "kept" → S14.5)
    const sA = show(t, MV.m_sh.t0, MV.m_g.t1);
    const k = t < b.d2.sank ? lin(t, MV.m_sh.t1, b.d2.sank) * li : li + lin(t, b.d2.kept, b.d4.sells + 2) * Math.min(18, TL.stocks.length - 1 - li);
    const kk = Math.floor(k), fr = k - kk, usd = TL.stocks[kk] + (TL.stocks[Math.min(TL.stocks.length - 1, kk + 1)] - TL.stocks[kk]) * fr;
    pile.set({ usd, a: sA, line: 1, dropK: t > b.d2.kept - 0.3 && t < b.d4.sells + 2 ? fr : -1 });
    twin.p.visible = sA > 0.05; twin.look(0.7);
    // phố: chưa sáng tới "Lit" (S15.2) → bản cổ phiếu cả phố; 80 nhà loé ở "eighty"; 2012 nhấc lên; khối cuối viền; 15 năm (S18)
    const up = show(t, MV.m_12.t0, MV.m_g2.t1);
    const r = ease(t, b.d6.lit - 0.1, b.d6.lit + 1.6), fl = (i) => (flip[i] ? show(t, b.d7.eighty - 0.1, b.d7.not + 0.4) : 0);
    const f15 = ease(t, b.d18.longer, b.d18.longer + 1.0), c15k = ease(t, b.d19.cash, b.d19.every + 0.4) * (1 - ease(t, b.d20.stocks - 0.1, b.d20.stocks + 0.6)), s15k = ease(t, b.d20.stocks - 0.1, b.d20.stocks + 0.6);
    street.set({
      vis: (i) => (m15.has(st10[i]) ? 1 : 1 - f15) * (r > 0.001 || t < b.d6.lit ? 1 : 1),
      lit: (i) => { if (f15 > 0.01) return mix(r * (A[i] ? 1 : 0), 0, f15) + c15k * (c15[i] ? 1 : 0) + s15k * (s15[i] ? 1 : 0); return r * (A[i] ? 1 : 0) + 0.9 * fl(i) * (1 - ease(t, b.d7.eighty + 0.6, b.d7.not)); },
      dark: (i) => { if (f15 > 0.01) return mix(r * (A[i] ? 0 : 1), 0, f15) + s15k * (s15[i] ? 0 : 1); return r * (A[i] ? 0 : 1) * (flip[i] ? ease(t, b.d7.eighty + 0.6, b.d7.not) + (t < b.d7.eighty ? 1 : 0) : 1); },
      hi: (i) => fl(i) * 0.7 + (late(i) ? 0.5 * show(t, b.d12.four, b.d14.lower) + 0.8 * pulse(t, b.d14.held, 1.4) : 0) + (i === i12 ? 0.5 * pulse(t, b.d9.glows, 1.4) : 0),
      lift: (i) => (i === i12 ? 1.3 * up : 0), big: (i) => (i === i12 ? 1 + (0.8 + 0.5 * ease(t, b.d11.whole, b.d11.whole + 1)) * up : 1),
      cellA: cw * (t > MV.m_g.t1 - 0.3 && (t < MV.m_12.t0 || t > MV.m_g2.t1) ? 1 : 0),
    });
    H.tag.set({ value: 5 });
    const g12 = show(t, MV.m_12.t0, MV.m_g2.t0 + 0.4);
    eq12.set({ usd: T12.eq[N] * ease(t, b.d10.ahead - 0.6, b.d10.ahead + 0.4), a: g12 });
    pile12.set({ usd: T12.stocks[N] * ease(t, b.d10.ahead - 0.4, b.d10.ahead + 0.6), a: g12, line: 0 });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    const aB = ok * bA * (t < MV.m_sh.t0 + 0.2 ? 1 : 0), [lx, ly] = O.toScreen(BX + BW + 0.4, 92000 * BU, BZ), [x0, y0] = O.toScreen(BX, 0, BZ), [x1] = O.toScreen(BX + BW, 0, BZ);
    label(O, '$92,000 start', lx + 10, ly, { align: 'left', kind: 'number', px: 40, alpha: aB, claims: ['savings_usd'] });
    label(O, 'lowest point of each pile, one per start month', 960, 880, { align: 'center', kind: 'name', px: 44, alpha: aB, color: C.muted });
    label(O, '183 of 307 dipped below $92,000', 960, 240, { align: 'center', kind: 'number', alpha: aB * show(t, b.d1.dipped), color: C.warn, claims: ['n_pot_below_start_stocks_10y', 'savings_usd'] });
    log.roi['d1.dipped'] = [x0 - 20, 180, x1 + 20, y0 + 20];
    const aS = ok * (t > MV.m_sh.t1 - 0.2 && t < MV.m_g.t0 + 0.2 ? 1 : 0), [px, py] = O.toScreen(SHELF.x + 0.9, pile.lineY(), SHELF.z + 0.55);
    label(O, '$92,000', px + 10, py, { align: 'left', kind: 'number', px: 44, alpha: aS, claims: ['savings_usd'] });
    label(O, 'lowest pile: $54,310', 960, 240, { align: 'center', kind: 'number', px: 60, alpha: aS * show(t, b.d2.sank), color: C.warn, claims: ['min_pot_stocks_10y'] });
    label(O, 'November 2007 start', 960, 320, { align: 'center', kind: 'number', px: 44, alpha: aS * show(t, b.d2.sank, b.d3.every - 0.3), color: C.muted, claims: ['low_start'] });
    label(O, 'assumption: invests every month, through every drop', 960, 320, { align: 'center', kind: 'name', px: 44, alpha: aS * show(t, b.d3.every) });
    label(O, 'she keeps adding a bundle every month', 960, 400, { align: 'center', kind: 'name', px: 44, alpha: aS * show(t, b.d2.kept, b.d3.every) });
    label(O, 'selling in a crash: not on this street', 960, 400, { align: 'center', kind: 'name', px: 48, alpha: aS * show(t, b.d4.sells) });
    if (sA > 0.05 && cw > 0.9) nameTag(O, twin, aS, { dy: -20 });
    log.roi['d2.sank'] = [500, 190, 1420, 360];
    const aG = ok * (t > MV.m_g.t1 - 0.2 && (t < MV.m_12.t0 + 0.2 || t > MV.m_g2.t1 - 0.2) ? 1 : 0);
    label(O, 'after the whole walk: how many lit?', 960, 230, { align: 'center', kind: 'name', alpha: aG * show(t, b.d5.how, b.d6.lit - 0.2) });
    label(O, '152 of 307 lit', 960, 230, { align: 'center', kind: 'number', px: 64, alpha: aG * show(t, b.d6.lit, b.d7.eighty - 0.2), color: LIT, claims: ['share_buyer_ahead_stocks_10y_n'] });
    label(O, 'about half', 960, 320, { align: 'center', kind: 'number', px: 56, alpha: aG * show(t, b.d6.half, b.d7.eighty - 0.2), claims: ['share_buyer_ahead_stocks_10y'] });
    label(O, '80 start months switched to the renter · none to the buyer', 960, 230, { align: 'center', kind: 'number', alpha: aG * show(t, b.d7.not, b.d8.count - 0.2), claims: ['n_flip_to_renter_10y', 'n_flip_to_buyer_10y'] });
    label(O, 'a count of what happened, not a promise', 960, 230, { align: 'center', kind: 'name', alpha: aG * show(t, b.d8.count, MV.m_12.t0) });
    log.roi['d6.lit'] = [300, 180, 1620, 950]; log.roi['d7.not'] = [300, 180, 1620, 950];
    const a12 = ok * (t > MV.m_12.t1 - 0.2 && t < MV.m_g2.t0 + 0.2 ? 1 : 0);
    label(O, 'April 2012 · with stocks: $237,632 ahead', 960, 240, { align: 'center', kind: 'number', px: 52, alpha: a12 * show(t, b.d10.ahead), color: LIT, claims: ['start_2012_04', 'adv_2012-04_stocks_10y'] });
    label(O, 'brightest house last time: still lit', 960, 320, { align: 'center', kind: 'name', px: 48, alpha: a12 * show(t, b.d9.glows - 0.3) });
    label(O, 'the whole house grew, not just $92,000 of it', 960, 880, { align: 'center', kind: 'name', px: 44, alpha: a12 * show(t, b.d11.whole), claims: ['savings_usd'] });
    log.roi['d10.ahead'] = [400, 190, 1520, 280];
    label(O, '2009 to mid-2016: nearly 4 in 5 lit', 960, 230, { align: 'center', kind: 'number', alpha: aG * show(t, b.d12.four, b.d15.half - 0.3), color: LIT, claims: ['era_2009-2016_span', 'era_2009-2016_share_stocks'] });
    label(O, 'after the crash: lit again', 960, 400, { align: 'center', kind: 'name', px: 48, alpha: aG * show(t, b.d12.nine, b.d15.shorter - 0.3) });
    label(O, 'lit in stretches · one long dark stretch', 960, 320, { align: 'center', kind: 'name', px: 48, alpha: aG * show(t, b.d13.stretches, b.d15.shorter - 0.3) });
    // B24b: ba cột tỉ lệ sáng theo thời gian ở (5 / 10 / 15 năm) trên tấm nền
    const cA = ok * show(t, b.d15.shorter - 0.2, b.d18.longer - 0.2);
    if (cA > 0.01) { O.card(560, 260, 800, 600, { fill: '#141922', stroke: C.muted, lw: 3, alpha: 0.95 * cA });
      const vals = [[53.4, '5 years', b.d15.half, 'share_buyer_ahead_stocks_5y', 'hold_5y'], [49.5, '10 years', b.d16.longer, 'share_buyer_ahead_stocks_10y_pct', 'hold_10y'], [21.9, '15 years', b.d16.longer + 0.5, 'share_buyer_ahead_stocks_15y_pct', 'hold_15y']], c = O.ctx;
      vals.forEach(([v, nm, tt, cid, hid], j) => { const k2 = ease(t, tt - 0.1, tt + 0.6), x = 660 + j * 230, h = 380 * v / 60 * k2; c.save(); c.globalAlpha = cA; c.fillStyle = STK; c.fillRect(x, 780 - h, 150, h); c.restore();
        label(O, nm, x + 75, 830, { align: 'center', kind: 'number', px: 40, alpha: cA, plate: null, claims: [hid] }); label(O, `${v.toFixed(1)}%`, x + 75, 760 - h, { align: 'center', kind: 'number', px: 44, alpha: cA * k2, plate: null, claims: [cid] }); });
      label(O, 'buyer ahead, by length of stay', 960, 330, { align: 'center', kind: 'name', px: 40, alpha: cA, plate: null }); }
    log.roi['d15.half'] = [560, 260, 1360, 860];
    label(O, '247 fifteen-year starts · cash: every one', 960, 230, { align: 'center', kind: 'number', alpha: aG * show(t, b.d19.every, b.d20.stocks - 0.2), color: C.warn, claims: ['n_15y', 'share_buyer_ahead_cash_15y'] });
    label(O, '15 years · stocks: about 1 in 5', 960, 230, { align: 'center', kind: 'number', alpha: aG * show(t, b.d20.one), color: STK, claims: ['hold_15y', 'share_buyer_ahead_stocks_15y'] });
    label(O, 'longer stay: most lights go out', 960, 320, { align: 'center', kind: 'name', px: 48, alpha: aG * show(t, b.d20.stocks, b.d22.tag) });
    label(O, 'next: the rent tag', 960, 880, { align: 'center', kind: 'name', px: 44, alpha: aG * show(t, b.d22.tag) });
    log.roi['d19.every'] = [300, 180, 1620, 950]; log.roi['d20.one'] = [300, 180, 1620, 950];
    legend(O, aG * show(t, b.d6.lit - 0.3) * (cA < 0.5 ? 1 : 0));
    chrome(O, { illus: 1 });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
