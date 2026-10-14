// Tập 8 · ĐOẠN B = S04–S07 (chương 2 "Two twins, one rent tag"). Căn hộ (thuê) — Nina giữa — nhà (mua); chi phí người mua; hộp kính CASH của người thuê;
// bản ghi thật của Mỹ thay một đường giả định; thẻ RENT trên cửa; bản đồ "US only"; tiền thuê quyết phần vào hộp; thẻ lay → MR1.
import { setup, Street, Home8, figure, MoneyStack, GlassBox, USMap, mapCredit, nameTag, label, chrome, dip, chapterCard, v7Card, followLight, modeLook,
  show, pulse, ease, lin, kf, END_X, APT, NINA, BUY, BOX, LIT, C, THREE, PALETTE } from '/episodes/ep008/world/w8.js';
import { Ribbon } from '/toolkit/factory/world/lib3d.js';

const SEG = '/episodes/ep008/world/seg/b-s04-s07/';
const RX = -24, RW = 12, RY = 0.4, RH = 3.6, RZ = -2;           // tường đồ thị bản ghi thật (xa phố, chỉ thấy ở cRecord)
const TAGX = APT.x + 0.3, TAGZ = APT.z + 0.66, DOOR = [APT.x, 0.3, APT.z + 0.7];

export async function boot(res) {
  const mid = (APT.x + BUY.x) / 2;
  const poses = {
    wWide: { pos: [END_X - 2.5, 3.2, 8.5], tgt: [mid, 0.6, -1.2], fov: 44, chart: 0 },
    wTwins: { pos: [mid - 1.2, 2.4, 7.4], tgt: [mid, 0.6, -1.2], fov: 42, chart: 0 },
    cTwins: { pos: [mid, 1.0, 22], tgt: [mid, 1.0, -1.2], fov: 17, chart: 1 },
    wBox: { pos: [BOX.x - 1.6, 1.6, 4.4], tgt: [BOX.x + 0.6, 0.5, -0.4], fov: 40, chart: 0 },
    cRecord: { pos: [RX + RW / 2 + 0.6, RY + RH / 2, RZ + 18], tgt: [RX + RW / 2 + 0.6, RY + RH / 2, RZ], fov: 25, chart: 1 },
    wDoor: { pos: [APT.x - 2.4, 2.0, 5.6], tgt: [APT.x + 0.2, 0.6, -2.6], fov: 42, chart: 0 },
    cTag: { pos: [TAGX + 0.6, 0.75, 9], tgt: [TAGX + 0.6, 0.72, TAGZ], fov: 12, chart: 1 },
    wFlow: { pos: [BOX.x - 0.6, 3.2, 5.2], tgt: [(BOX.x + APT.x) / 2, 0.45, -0.6], fov: 22, chart: 0 },   // M5 "chỗ muốn tua" vòng 1: thẻ 5 % trên cửa đọc được cạnh hộp (S07.3; fov 42 → 22, máy cao hơn để đầu người song sinh không che thẻ)
  };
  const { S, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const street = Street(scene, DATA.starts10), H = Home8(scene), map = await USMap(scene, { x: APT.x - 1, z: -7.5, s: 0.7 });
  const nina = figure(scene, { x: NINA.x, z: NINA.z, lamp: true });
  const tB = figure(scene, { x: BUY.x - 1.1, z: 0.3, char: 'twin' }), tR = figure(scene, { x: APT.x - 0.9, z: 0.3, char: 'twin' });
  const box = GlassBox(scene, { x: BOX.x, z: BOX.z }), box2 = GlassBox(scene, { x: BOX.x - 1.3, z: BOX.z, max: 0 });
  const sav = MoneyStack(scene, { x: BUY.x - 1.7, z: 0.4, color: '#9AA4B2', unit: 4000, name: 'buyer-savings' });
  const savR = MoneyStack(scene, { x: APT.x - 1.5, z: 0.6, color: '#9AA4B2', unit: 4000, name: 'renter-savings' });
  // chi phí hằng tháng của người mua: viên nhỏ rơi vào khe mái nhà
  const coin = (c) => { const m = new THREE.Mesh(new THREE.BoxGeometry(0.16, 0.05, 0.12), new THREE.MeshStandardMaterial({ color: c, transparent: true })); scene.add(m); return m; };
  const coins = [0, 1, 2, 3, 4].map(() => coin(LIT));
  const flyB = [0, 1, 2, 3, 4, 5].map(() => coin(C.warn));
  // đồ thị bản ghi thật: một đường giả định (thẳng) + ba dải (giá nhà, tiền thuê, lãi), x = tháng 1991-01 → 2026-07
  const n = DATA.months.length, X = (i) => RX + RW * i / (n - 1), Yi = (v) => RY + (v - 1) / 3.6 * RH, Yr = (v) => RY + v / 12 * RH;
  const assumed = Ribbon({ maxPts: 2, width: 0.06, color: '#9AA4B2', z: RZ }), rP = Ribbon({ maxPts: n, width: 0.07, color: C.accent, z: RZ }),
    rR = Ribbon({ maxPts: n, width: 0.07, color: '#8FB4FF', z: RZ }), rM = Ribbon({ maxPts: n, width: 0.05, color: '#C9D3E2', z: RZ });
  scene.add(assumed, rP, rR, rM);
  const axis = new THREE.Mesh(new THREE.BoxGeometry(RW, 0.02, 0.02), new THREE.MeshStandardMaterial({ color: C.muted })); axis.position.set(RX + RW / 2, RY, RZ); scene.add(axis);
  const rate = DATA.rate.map((v, i) => v ?? DATA.rate[Math.max(0, i - 1)] ?? 8);
  const AT = S.at;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    street.set({ lit: () => 0, dark: () => 0 });
    nina.lamp.set(1, t); nina.look(t < b.b4.rents ? 0.7 * Math.sin(Math.min(1, (t - b.b1.down) / 6) * Math.PI) : -0.5);
    // S04.2: hai chồng tiền để dành của người mua bay vào nhà (đặt cọc ở "down", chi phí đóng ở "closing")
    sav.set({ usd: 92000 * (1 - 0.87 * ease(t, b.b1.down, b.b1.down + 0.6) - 0.13 * ease(t, b.b1.closing, b.b1.closing + 0.5)), a: show(t, 0.3, b.b1.closing + 0.6) });
    H.house.setLit(0.6 * ease(t, b.b1.mortgage, b.b1.mortgage + 0.4));
    // S04.3: mỗi khoản chi một viên rơi vào khe mái nhà
    ['interest', 'property', 'insurance', 'repairs', 'selling'].forEach((k, i) => { const c = coins[i], p = (t - b.b2[k] + 0.2) / 0.6; c.visible = p > 0 && p < 1;
      if (c.visible) c.position.set(BUY.x - 0.2 + 0.1 * i, 1.6 - 1.0 * p * p, BUY.z + 0.2); });
    // S04.5: người thuê bước tới cửa căn hộ ở "rents"; chồng tiền để dành cạnh cửa
    tR.p.position.x = APT.x - 0.9 + 0.5 * ease(t, b.b4.rents, b.b4.rents + 1.0);
    savR.set({ usd: 92000 * ease(t, b.b4.savings - 0.1, b.b4.savings + 0.4) * (1 - ease(t, b.b6.down, b.b6.down + 0.7)), a: show(t, b.b4.savings - 0.1, b.b6.down + 0.8) });
    // S05: hộp kính — đóng ở "cash"; đặt cọc + chi phí đóng vào ở "down"; một bó mỗi tháng từ cửa căn hộ (S05.3, S07.3)
    const nIn = 4 * ease(t, b.b6.down, b.b6.down + 0.7) + Math.min(5, Math.max(0, (t - b.b7.month + 0.3) / 0.7)) * (t < b.b8.treasury + 2 ? 1 : 1) + Math.min(3, Math.max(0, (t - b.b17.aside) / 0.8));
    box.set({ n: nIn, a: show(t, b.b5.cash - 0.6), glow: show(t, b.b8.treasury, b.b9.investing) });
    box2.set({ n: 0, a: 0.6 * show(t, b.b9.investing, b.b10.card) });
    const flows = [[b.b7.month - 0.3, 5, 0.7], [b.b17.aside, 3, 0.8]];
    flyB.forEach((f, i) => { f.visible = false; });
    let fi = 0;
    for (const [t0, cnt, dt] of flows) for (let k = 0; k < cnt && fi < flyB.length; k++, fi++) {
      const p = (t - t0 - k * dt) / 0.6, f = flyB[fi]; if (p <= 0 || p >= 1) continue; f.visible = true;
      f.position.set(DOOR[0] + (BOX.x - DOOR[0]) * p, DOOR[1] + 0.6 * Math.sin(Math.PI * p) + (0.5 - DOOR[1]) * p, DOOR[2] + (BOX.z - DOOR[2]) * p); }
    // S06: đường giả định (thẳng) → nghiêng ở "moves"; bản ghi thật tích từng tháng từ "prices"/"rents"/"rates"
    const asA = show(t, b.b11.growth - 0.2, MV.m_w2.t0), tilt = 0.6 * Math.sin(Math.max(0, t - b.b12.moves) * 2.2) * (t > b.b12.moves && t < b.b12.replay ? 1 : 0);
    assumed.set([[X(0), Yi(1)], [X(n - 1), Yi(1) + (2.2 + tilt) * ease(t, b.b11.growth - 0.2, b.b11.growth + 1.0)]]); assumed.visible = asA > 0.01; assumed.material.opacity = asA;
    const grow = (c) => Math.max(2, Math.floor(n * ease(t, c, c + 2.6)));
    rP.set(DATA.hpi.slice(0, grow(b.b13.prices)).map((v, i) => [X(i), Yi(v)])); rR.set(DATA.rent.slice(0, grow(b.b13.rents)).map((v, i) => [X(i), Yi(v)])); rM.set(rate.slice(0, grow(b.b13.rates)).map((v, i) => [X(i), Yr(v)]));
    for (const [r, c] of [[rP, b.b13.prices], [rR, b.b13.rents], [rM, b.b13.rates]]) { r.visible = t > c - 0.1 && t < MV.m_w2.t1; }
    axis.visible = asA > 0.01;
    // S07: thẻ trên cửa ("tag"), lật tới 5 % ("five"); lay ở "turns"; bản đồ "US only" dưới mặt đất S07.1 → nhãn S07.2
    const tg = show(t, b.b15.tag - 0.3);
    H.tag.set({ value: 5, a: Math.max(0.2, tg), swing: 0.25 * Math.sin((t - b.b18.turns) * 6) * pulse(t, b.b18.turns, 1.6) + 0.05 * Math.sin(t * 1.3) });
    map.set(show(t, b.b15.tag - 0.8, MV.m_c3.t0 + 0.3) + 0.0 * show(t, b.b16.history, MV.m_w3.t0));
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 0.0);
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    nameTag(O, nina, t < MV.m_c2.t0 || t > MV.m_w2.t1 ? (t > MV.m_c3.t0 && t < MV.m_w3.t1 ? 0 : 1) : 0);
    const [hx, hy] = O.toScreen(BUY.x, 1.6, BUY.z), [ax2, ay2] = O.toScreen(APT.x, 1.9, APT.z);
    const wl = cw < 0.05 ? 1 : 0;
    label(O, 'buys', hx, hy - 30, { align: 'center', kind: 'name', px: 48, alpha: wl * show(t, Math.max(b.b0.pay, S.chapter[0] + 2.7), b.b2.selling + 1), color: LIT });
    label(O, 'rents', ax2, ay2 - 30, { align: 'center', kind: 'name', px: 48, alpha: wl * show(t, Math.max(b.b0.pay, S.chapter[0] + 2.7), MV.m_w1.t0 - 0.3), color: C.warn });
    label(O, 'mortgage', hx + 160, hy + 90, { align: 'left', kind: 'name', px: 44, alpha: wl * show(t, b.b1.mortgage, b.b2.interest - 0.1) });
    [['interest', 'interest'], ['property', 'property tax'], ['insurance', 'insurance'], ['repairs', 'repairs'], ['selling', 'cost of selling']].forEach(([k, s], i) =>
      label(O, s, hx + 170, hy - 40 + 52 * i, { align: 'left', kind: 'name', px: 44, alpha: wl * show(t, b.b2[k], MV.m_c1.t0 + 0.2) }));
    log.roi['b2.interest'] = [hx - 120, hy - 100, hx + 520, hy + 220];
    label(O, "upkeep: 2.5 percent a year · selling: 6 percent", 960, 250, { align: 'center', kind: 'number', alpha: ok * show(t, b.b3.two, MV.m_w1.t0), claims: ['owner_cost_pct', 'sell_pct'] });
    log.roi['b3.two'] = [400, 190, 1520, 270];
    const [bx, by] = O.toScreen(...box.top());
    label(O, 'cash, not stocks', bx, by - 30, { align: 'center', kind: 'name', alpha: wl * show(t, b.b5.stocks, b.b9.investing - 0.3), color: C.warn });
    label(O, 'Treasury bill interest only', bx, by + 40, { align: 'center', kind: 'name', px: 44, alpha: wl * show(t, b.b8.treasury, b.b9.investing) });
    const [b2x, b2y] = O.toScreen(BOX.x - 1.3, 1.1, BOX.z);
    label(O, 'invested? not measured here', b2x - 40, b2y + 260, { align: 'center', kind: 'name', px: 44, alpha: wl * show(t, b.b9.investing, b.b10.card) });
    log.roi['b5.cash'] = [bx - 200, by - 80, bx + 200, by + 200]; log.roi['b9.investing'] = [b2x - 300, b2y - 80, b2x + 200, b2y + 200];
    v7Card(O, 'Not counted on either side', ["moving costs · renter's insurance", 'income taxes · mortgage interest deduction', 'refinancing'], show(t, b.b10.card, MV.m_c2.t0 + 0.2));
    // S06: nhãn đồ thị
    const rA = ok * (t < MV.m_w2.t0 ? 1 : 0);
    const [ex, ey] = O.toScreen(X(n - 1), Yi(3.2), RZ), [px2, py2] = O.toScreen(X(n - 1), Yi(DATA.hpi[n - 1]), RZ), [qx, qy] = O.toScreen(X(n - 1), Yi(DATA.rent[n - 1]), RZ), [mx, my] = O.toScreen(X(n - 1), Yr(rate[n - 1]), RZ);
    label(O, 'one assumed growth rate', ex - 40, ey - 40, { align: 'right', kind: 'name', px: 48, alpha: rA * show(t, b.b11.growth, b.b13.prices), color: '#C9D0DA' });
    label(O, 'the real monthly US record', 960, 230, { align: 'center', kind: 'name', alpha: rA * show(t, b.b13.prices) });
    label(O, 'home prices', px2 + 20, py2, { align: 'left', kind: 'name', px: 44, alpha: rA * show(t, b.b13.prices + 2.4), color: C.accent });
    label(O, 'rents', qx + 20, qy - 40, { align: 'left', kind: 'name', px: 44, alpha: rA * show(t, b.b13.rents + 2.4), color: '#8FB4FF' });
    label(O, 'mortgage rates', mx + 20, my + 60, { align: 'left', kind: 'name', px: 44, alpha: rA * show(t, b.b13.rates + 2.4), color: '#C9D3E2' });
    const [ox, oy] = O.toScreen(RX, RY, RZ), [zx] = O.toScreen(RX + RW, RY, RZ);
    label(O, 'January 1991', ox, oy + 60, { align: 'left', kind: 'number', px: 44, alpha: rA * show(t, b.b13.prices), color: C.muted, claims: ['first_10y'] });
    label(O, 'starting rent: ?', 960, 900, { align: 'center', kind: 'name', alpha: rA * show(t, b.b14.rent), color: C.warn });
    log.roi['b11.growth'] = [ox, ey - 100, zx, oy]; log.roi['b13.prices'] = [ox, 200, zx + 300, oy]; log.roi['b14.rent'] = [700, 840, 1220, 920];
    // S07: nhãn thẻ (đồ thị) + bản đồ (nguồn trên hình)
    const [tx, ty] = O.toScreen(TAGX, 0.95, TAGZ);
    label(O, 'starting rent: 5% a year (assumption)', 960, 250, { align: 'center', kind: 'number', alpha: ok * show(t, b.b16.one - 0.6, MV.m_w3.t0), claims: ['yield_anchor_pct'] });
    label(O, '$1,667 a month', 960, 330, { align: 'center', kind: 'number', alpha: ok * show(t, b.b16.one, MV.m_w3.t0), claims: ['today_rent_month1'] });
    log.roi['b15.tag'] = [tx - 160, ty - 60, tx + 160, ty + 140]; log.roi['b16.one'] = [500, 190, 1420, 350];
    mapCredit(O, show(t, b.b15.tag - 0.8, MV.m_c3.t0 + 0.3) * (cw < 0.5 ? 1 : 0));
    label(O, 'US only', 960, 860, { align: 'center', kind: 'name', alpha: show(t, b.b15.tag - 0.4, MV.m_c3.t0) * (cw < 0.5 ? 1 : 0) });
    chrome(O, {});
    log.roi['b18.turns'] = [tx - 160, ty - 60, tx + 160, ty + 140]; log.roi['b17.aside'] = [300, 300, 1600, 900];
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
