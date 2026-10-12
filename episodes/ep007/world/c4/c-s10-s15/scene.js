// Tập 7 · C4 · ĐOẠN C = S10–S15. Một trục thời gian chung (Aug 1991 → Oct 2026, trái → phải) cho mọi vật: thanh đứt nét "one assumed rate" →
// hai đường lãi khảo sát thật (V3) + hai thẻ khoản vay → lưới V1 1.833 ô (ô cuối = tuần của Tessa) → khoảng giữa hai đường rời xuống trục, phóng
// thành 1.833 cột khoảng chênh (V6 ngoặc nhỏ nhất / lớn nhất, vạch trung bình, chấm Tessa) → mỗi cột hạ về sàn rồi MỌC TỪ SÀN 0 thành một chồng (W2
// hàng + W5 đỉnh), cùng thang bó của the stack cạnh nhà → nhỏ nhất, cao nhất, trung vị, tuần cao bằng/hơn của Tessa (ít hơn 1/5). Mốc giờ chỉ từ spine.json.
// C5 r1: 1.833 cột rộng < 1 px → một tuần lẻ (nhỏ nhất / lớn nhất / của Tessa) không thấy được; mỗi tuần được gọi tên có CỘT ĐÁNH DẤU riêng (rộng
// ≈ 8 px, ink, đúng chiều cao của tuần đó, đứng trước hàng) → chồng "smallest" thấp nhất thấy được, mọi chồng đứng trên vạch sàn 0.
import { setup, figure, gesture, figTag, OfferCard, WeekGrid, WeekRow, theStack, stackSet, BUNDLE_TH, modeLook, followLight, chrome, label, seg2, vbrace, dip,
  kf, show, pulse, C, CK, ease, lin, mix, THREE } from '/episodes/ep007/world/c4kit.js';
import { Ribbon } from '/toolkit/factory/world/lib3d.js';

const SEG = '/episodes/ep007/world/c4/c-s10-s15/';
const RY = 0.35;                  // điểm % lãi → đơn vị (trục từ 0)
const MW = 0.075;                 // bề rộng cột đánh dấu (≈ 8 px ở máy đồ thị)

export async function boot(res) {
  const poses = {
    wC0: { pos: [1.2, 2.3, 14.5], tgt: [1.2, 1.7, 0], fov: 42, chart: 0 },     // C5 r1: chính diện → thanh giả định nằm ngang
    cC: { pos: [2.2, 3.0, 26], tgt: [2.2, 3.0, 0], fov: 20.6, chart: 1 },
    wRow: { pos: [-7.4, 2.9, 10.4], tgt: [1.8, 1.2, -0.8], fov: 46, chart: 0 },
    wEnd: { pos: [0.4, 2.6, 21], tgt: [0.4, 2.1, 0], fov: 21, chart: 0 },       // C5 r1: giữ khung phẳng (chính diện), chỉ đẩy nhẹ về Tessa
  };
  const { S, D, G, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue, X = S.x, N = S.weeks.length, W = X.x1 - X.x0, U = BUNDLE_TH / G.bundle_usd, GS = G.stack_total * U / (S.r30[N - 1] - S.r15[N - 1]);
  const xw = (i) => X.x0 + (i + 0.5) * W / N;
  const hm = figure(scene, { x: X.house }), stack = theStack(scene, G, { x: X.stack });
  stackSet(stack, G.stack_total);
  const glowS = new THREE.Mesh(new THREE.BoxGeometry(1.06, 15 * BUNDLE_TH + 0.1, 0.76), new THREE.MeshBasicMaterial({ color: C.warn, transparent: true, opacity: 0, depthWrite: false }));
  glowS.position.set(X.stack, (15 * BUNDLE_TH + 0.1) / 2, 0); scene.add(glowS);
  // S10.1: một mức lãi giả định = thanh ĐỨT NÉT phẳng (ink-muted, vật cố định) dọc trục thời gian, sau nhà
  const yA = S.assumed_rate * RY, rail = new THREE.Group(), ND = 26;
  for (let k = 0; k < ND; k++) { const m = new THREE.Mesh(new THREE.BoxGeometry(W / ND * 0.55, 0.06, 0.06), new THREE.MeshStandardMaterial({ color: C.muted, emissive: new THREE.Color(C.muted), emissiveIntensity: 0.45, transparent: true }));
    m.position.set(X.x0 + (k + 0.5) * W / ND, yA, 0.35); rail.add(m); }
  scene.add(rail); rail.userData.checks = { role: 'mark', key: 'assumed-rate' };
  // S10.2: hai thẻ khoản vay thật (V4 adapted), trên vùng đường lãi; rộng 4,5 (≈ 510 px) cho chữ 48 px nằm trong thẻ
  const card15 = OfferCard(scene, { x: X.cards[0], y: 4.55, w: 4.5, h: 0.72 }), card30 = OfferCard(scene, { x: X.cards[1], y: 4.55, w: 4.5, h: 0.72 });
  // hai đường lãi khảo sát, mỗi đường một màu (30 năm accent, 15 năm ink); vạch cùng màu dưới thẻ của nó
  const L30C = C.accent, L15C = C.ink;
  const l30 = Ribbon({ color: L30C, z: 0.3, width: 0.06, maxPts: N + 2 }), l15 = Ribbon({ color: L15C, z: 0.3, width: 0.05, maxPts: N + 2 });
  scene.add(l30, l15); l30.userData.checks = { role: 'series', series: 'r30', key: 'rate-30' }; l15.userData.checks = { role: 'series', series: 'r15', key: 'rate-15' };
  // lưới V1: tường sau trục, TRÊN vùng hai đường (đỉnh đường 30 năm ≈ 3,24) → lưới không phủ đường; cột khoảng chênh → chồng (cùng 1.833 vật)
  const grid = WeekGrid(scene, S.weeks, { x0: X.x0, width: W, y0: 3.45, height: 1.55, z: -0.6 });
  const cols = WeekRow(scene, S.extra, { x0: X.x0, width: W, z: 0.05, depth: 0.22, unit: U, name: 'gap-then-stacks' });
  const sp = S.r30.map((r, i) => r - S.r15[i]);
  // cột đánh dấu: một tuần được gọi tên, đúng chiều cao, đứng trước hàng (z 0,12 → mặt trước 0,27 > mặt trước hàng 0,16)
  const marker = (key, color = C.ink) => {
    const g = new THREE.BoxGeometry(MW, 1, 0.3); g.translate(0, 0.5, 0);
    const m = new THREE.Mesh(g, new THREE.MeshStandardMaterial({ color, emissive: new THREE.Color(color), emissiveIntensity: 0.35, roughness: 0.6, transparent: true }));
    m.visible = false; scene.add(m); m.userData.checks = { role: 'mark', key };
    m.set = (i, h, a, glow = 0) => { m.visible = a > 0.01; m.position.set(xw(i), 0, 0.12); m.scale.y = Math.max(0.001, h); m.material.opacity = a; m.material.emissiveIntensity = 0.35 + 0.65 * glow; };
    return m;
  };
  const mGapMin = marker('gap-min'), mGapMax = marker('gap-max'), mMin = marker('week-smallest'), mMax = marker('week-tallest'), mNow = marker('week-tessa');
  // S13.1 "rise": dải sáng chạy dọc đỉnh các chồng (trái → phải), mỗi 3 tuần một điểm
  const topLine = Ribbon({ color: C.ink, z: 0.2, width: 0.05, maxPts: Math.ceil(N / 3) + 2 }); scene.add(topLine); topLine.visible = false;
  const topPts = []; for (let i = 0; i < N; i += 3) topPts.push([xw(i), S.extra[i] * U]);
  // S15.1: vạch trung vị (ink, dày) dọc hàng
  const med = new THREE.Mesh(new THREE.BoxGeometry(1, 0.05, 0.04), new THREE.MeshBasicMaterial({ color: C.ink, transparent: true })); med.geometry.translate(0.5, 0, 0);
  med.position.set(X.x0, S.median * U, 0.3); scene.add(med); med.userData.checks = { role: 'mark', key: 'median-line', value: S.median };
  const cA = new THREE.Color(C.accent), cAd = new THREE.Color('#22355A'), cW = new THREE.Color(C.warn), cWd = new THREE.Color('#4A3F2A'), cI = new THREE.Color(C.ink);
  const T15 = G.stack_total;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw); gesture(hm, t, S.gestures);
    // thanh giả định: mọc trái → phải ở "one"; mờ khi đường thật vẽ; tắt khi lưới đầy
    const rg = lin(t, b.c0.one - 0.05, b.c0.one + 0.6), rA = (1 - 0.6 * ease(t, b.c1.rates, b.c1.rates + 1.0)) * (1 - ease(t, b.c2.priced, b.c2.priced + 0.5));
    rail.children.forEach((m, k) => { const v = Math.min(1, Math.max(0, rg * ND - k)); m.visible = v > 0.01 && rA > 0.01; m.scale.x = Math.max(0.001, v); m.material.opacity = rA; });
    const cardA = 1 - ease(t, b.c2.priced, b.c2.priced + 0.5);
    card15.set({ a: show(t, b.c1.real) * cardA }); card30.set({ a: show(t, b.c1.thirty) * cardA, band: 0 });
    // đường lãi: vẽ ở "real rates" (1,5 s); dịu 0,5 khi lưới hiện (lưới ở trên, không phủ); sáng lại ở "far"; tắt khi khoảng rời xuống trục ("gap")
    const dr = lin(t, b.c1.rates, b.c1.rates + 1.5) * (N - 1);
    const lA = (t < b.c4.far ? 1 - 0.5 * ease(t, b.c2.priced, b.c2.priced + 0.6) : mix(0.5, 1, ease(t, b.c4.far, b.c4.far + 0.6))) * (1 - ease(t, b.c5.gap, b.c5.gap + 0.8));
    for (const [L, R] of [[l30, S.r30], [l15, S.r15]]) {
      const m = Math.floor(dr), pts = []; for (let i = 0; i <= m; i += 2) pts.push([xw(i), R[i] * RY]);
      if (m < N - 1 && dr > m) pts.push([xw(dr), mix(R[m], R[m + 1], dr - m) * RY]); else if (m === N - 1) pts.push([xw(N - 1), R[N - 1] * RY]);
      if (pts.length > 1) L.set(pts); L.visible = pts.length > 1 && lA > 0.01; L.material.opacity = lA;
    }
    // lưới V1: tắt ngay đầu S11 (không còn sót ở "far")
    const gA = 1 - ease(t, b.c4.t0 - 0.3, b.c4.t0 + 0.2);
    grid.set({ fill: kf(S.fill, t), lastA: ease(t, b.c3.last - 0.05, b.c3.last + 0.3), wave: t > b.c3.earlier && t < b.c3.earlier + 1.9 ? (N - 1) * (1 - (t - b.c3.earlier) / 1.6) : null, a: gA });
    // cột khoảng chênh → chồng: dải khoảng giữa hai đường hiện từ "far" (sáng ở "above"); "gap" hạ xuống trục + phóng ×GS/RY; "least" ≥ nửa điểm sáng;
    // "every" (S13.1) mỗi cột HẠ VỀ SÀN rồi MỌC TỪ SÀN 0 tới extra_total × U (sóng trái → phải, accent → warn); S15.2 tuần cao bằng/hơn Tessa sáng
    const bandA = ease(t, b.c4.far + 0.2, b.c4.far + 0.8), ab = ease(t, b.c4.above - 0.05, b.c4.above + 0.5), mg = ease(t, b.c5.gap, b.c5.gap + 1.0), le = ease(t, b.c6.least - 0.05, b.c6.least + 0.4);
    const stk = (i) => Math.min(1, Math.max(0, (t - b.c8.every - 1.6 * i / N) / 0.8)), fw = ease(t, b.d2.fewer - 0.05, b.d2.fewer + 0.6);
    const dim = 0.55 * show(t, S.smallest, b.d1.median);   // các chồng khác tối bớt khi gọi tên nhỏ nhất / lớn nhất
    cols.set({ grow: bandA > 0.001 ? 1 : 0, a: Math.max(0.45 * bandA + 0.4 * ab, mg, stk(N - 1)),
      span: (i) => { const k = stk(i), g0 = [mix(S.r15[i] * RY, 0, mg), mix(S.r30[i] * RY, sp[i] * GS, mg)];
        if (k < 0.35) { const kd = k / 0.35; return [g0[0] * (1 - kd), g0[1] * (1 - kd)]; }
        const kg = (k - 0.35) / 0.65; return [0, S.extra[i] * U * (1 - (1 - kg) * (1 - kg))]; },
      color: (i, c) => { const k = stk(i); c.copy(cA).lerp(cAd, le * (sp[i] >= 0.5 - 1e-9 ? 0 : 0.85));
        if (k >= 0.35) { c.copy(cW).lerp(cWd, dim); c.lerp(cWd, 0.8 * fw * (S.extra[i] >= T15 ? 0 : 1)); } } });
    // cột đánh dấu: S11 nhỏ nhất ("zero") / lớn nhất ("one"); S13 chồng nhỏ nhất ("smallest"); S14 cao nhất ("tallest"); S15 tuần của Tessa ("high")
    mGapMin.set(S.i.spmin, sp[S.i.spmin] * GS, show(t, b.c5.zero, b.c6.least));
    mGapMax.set(S.i.spmax, sp[S.i.spmax] * GS, show(t, b.c5.one, b.c6.least));
    mMin.set(S.i.min, S.extra[S.i.min] * U, show(t, S.smallest, b.d1.median), pulse(t, b.c9.six, 0.8));
    mMax.set(S.i.max, S.extra[S.i.max] * U, show(t, b.d0.tallest, b.d1.median), pulse(t, b.d0.twenty, 0.8));
    mNow.set(N - 1, S.extra[N - 1] * U, show(t, b.d2.high), Math.max(pulse(t, b.d3.t0, 1.0), pulse(t, b.d3.expensive, 0.9)));
    { const p = lin(t, b.c8.rise - 0.05, b.c8.rise + 1.2), n = Math.floor(p * topPts.length), a = show(t, b.c8.rise, S.smallest - 0.35);
      topLine.visible = n > 1 && a > 0.01; if (n > 1) topLine.set(topPts.slice(0, n)); topLine.material.opacity = a; }
    const mL = ease(t, b.d1.median - 0.05, b.d1.median + 0.7) * (1 - ease(t, MV.m_w15.t0, MV.m_w15.t0 + 0.4)); med.scale.x = Math.max(0.001, W * mL); med.visible = mL > 0.01;
    med.material.opacity = 0.7 + 0.3 * pulse(t, b.d1.median + 0.7, 0.8);
    glowS.material.opacity = 0.35 * pulse(t, b.d3.expensive, 0.9); glowS.visible = glowS.material.opacity > 0.01;
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 1 - ease(t, 0, 0.4));   // mở đoạn từ khoảng giữ MR1 (vẽ TRƯỚC mọi chữ)
    figTag(O, hm);
    const sc = (x, y, z = 0) => O.toScreen(x, y, z), [, yFloor] = sc(X.x0, 0, 0.05), [xL] = sc(X.x0, 0, 0.05), [xR] = sc(X.x1, 0, 0.05);
    // vạch sàn 0 của cột khoảng chênh / hàng chồng (đồ thị): mọi cột đứng trên vạch này
    seg2(O, xL - 6, yFloor, xR + 6, yFloor, C.muted, 0.8 * ok * ease(t, b.c5.gap, b.c5.gap + 0.6), 3);
    // trang kiểm (coverage hồi 2): mỗi ô lưới / mỗi chồng tuần là một hình mang case = tuần
    if (CK.on) {
      if (gA > 0.5 && kf(S.fill, t) >= N) for (let i = 0; i < N; i++) O.shape({ role: 'mark', world: grid.box(i), case: S.weeks[i], series: 'weeks' });
      if (stk(N - 1) >= 1 && t < MV.m_w15.t1) for (let i = 0; i < N; i++) O.shape({ role: 'bar', world: [[xw(i) - W / N / 2, 0, 0.05], [xw(i) + W / N / 2, S.extra[i] * U, 0.05]], case: S.weeks[i], value: S.extra[i], series: 'extra_total' });
    }
    // S10.1: tên thanh giả định (thế giới hay đồ thị: không số)
    { const [x, y] = sc(X.x1, yA, 0.35), [x0] = sc(X.x0, yA, 0.35), xa = Math.min(1790, x);
      label(O, 'one assumed rate', xa, y - 34, { align: 'right', kind: 'name', px: 48, color: C.muted, alpha: show(t, b.c0.assumed, b.c2.priced - 0.1) });
      log.roi['c0.one'] = [x0 - 10, y - 20, x + 10, y + 20]; log.roi['c0.assumed'] = [xa - 480, y - 90, xa + 10, y - 20]; }
    // S10.2: thẻ + vạch màu của đường tương ứng dưới thẻ (hiện cùng đường); nhãn đường lãi
    for (const [card, s, cl, at, id, lc] of [[card15, `${D('term_short')} loan`, ['term_short'], b.c1.real, 'c1.real', L15C], [card30, `${D('term_long')} paid ${D('paid_in_short')}`, ['term_long', 'paid_in_short'], b.c1.thirty, 'c1.thirty', L30C]]) {
      const [x, y] = sc(card.position.x, card.position.y, 0.05), a = ok * show(t, at, b.c2.priced - 0.3);
      label(O, s, x, y + 16, { align: 'center', kind: 'number', px: 48, alpha: a, claims: cl });
      seg2(O, x - 90, y + 62, x + 90, y + 62, lc, a * show(t, b.c1.rates), 8);
      log.roi[id] = [x - 300, y - 50, x + 300, y + 50];
    }
    log.roi['c1.rates'] = [xL, sc(0, 3.4)[1], xR, yFloor];
    label(O, `every real week: ${D('term_short')} and ${D('term_long')}`, 960, 215, { align: 'center', kind: 'number', alpha: ok * show(t, b.c1.every, b.c2.priced - 0.3), claims: ['term_short', 'term_long'] });
    log.roi['c1.every'] = [xL, sc(0, 3.4)[1], xR, yFloor];
    // S10.3–S10.4: nhãn lưới; dải phương pháp ("how it was built"); ô của Tessa (vàng) + đường dẫn
    const g2 = b.c3.last - 0.45;   // nhãn lưới tắt hẳn trước nhãn ô của Tessa (cùng hàng 268)
    label(O, `${D('principal')} priced both ways each week`, 960, 205, { align: 'center', kind: 'number', alpha: ok * show(t, b.c2.both, b.c2.built - 0.4), claims: ['principal'] });
    label(O, `${D('n_weeks')} · ${D('first_week_short')} to ${D('last_week_month')}`, 960, 268, { align: 'center', kind: 'number', alpha: ok * show(t, b.c2.thirty, g2), claims: ['n_weeks', 'first_week_short', 'last_week_month'] });
    label(O, `method: ${D('principal')} · ${D('term_short')} vs ${D('term_long')} paid ${D('paid_in_short')}`, 960, 205,
      { align: 'center', kind: 'number', color: C.muted, alpha: ok * show(t, b.c2.built, g2), claims: ['principal', 'term_short', 'term_long', 'paid_in_short'] });
    { const [gx0, gy0] = sc(X.x0, grid.top, -0.6), [gx1, gy1] = sc(X.x1, 3.45, -0.6); log.roi['c2.priced'] = [gx0, gy0, gx1, gy1]; log.roi['c2.both'] = [560, 150, 1360, 230]; log.roi['c2.thirty'] = [560, 215, 1360, 290];
      log.roi['c2.built'] = [400, 150, 1520, 230]; log.roi['c3.earlier'] = [gx0, gy0, gx1, gy1]; log.roi['c4.far'] = [xL, sc(0, 3.4)[1], xR, yFloor]; }
    { const [cx, cy] = sc(...grid.at(N - 1)), lA = ok * show(t, b.c3.last, b.c4.t0 - 0.3), c = O.ctx;
      if (lA > 0.01) { const r = 15 + 8 * pulse(t, b.c3.last, 0.9); c.save(); c.globalAlpha = lA; c.fillStyle = C.warn; c.fillRect(cx - 9, cy - 9, 18, 18);
        c.strokeStyle = C.warn; c.lineWidth = 4; c.strokeRect(cx - r, cy - r, 2 * r, 2 * r); c.restore(); }
      seg2(O, cx, cy - 26, 1700, 290, C.warn, 0.8 * lA, 3);
      label(O, "Tessa's week = the last", 1800, 268, { align: 'right', kind: 'name', px: 48, alpha: lA });
      log.roi['c3.last'] = [cx - 30, cy - 30, cx + 30, cy + 30]; }
    // S11: khoảng giữa hai đường; rời xuống trục; ngoặc + cột đánh dấu nhỏ nhất / lớn nhất
    log.roi['c4.above'] = [xL, sc(0, 3.4)[1], xR, yFloor]; log.roi['c5.gap'] = log.roi['c4.above'];
    label(O, `${D('term_long')} minus ${D('term_short')} rate`, 960, 215, { align: 'center', kind: 'number', alpha: ok * show(t, b.c5.gap, b.c6.averaged - 0.35), claims: ['term_long', 'term_short'] });
    const brk = (i, at, z) => { const [x, y0] = sc(xw(i), 0, 0.05), [, y1] = sc(xw(i), sp[i] * GS, 0.05), a = ok * show(t, at, z); vbrace(O, x - 12, y1, y0, C.ink, a, 5, 14); return [x, y1]; };
    { const [x0, y0] = brk(S.i.spmin, b.c5.zero, b.c6.least), [x1, y1] = brk(S.i.spmax, b.c5.one, b.c6.least);
      log.roi['c5.zero'] = [x0 - 40, y0 - 20, x0 + 20, yFloor]; log.roi['c5.one'] = [x1 - 40, y1 - 20, x1 + 20, yFloor]; }
    label(O, `gap: ${D('spread_min')} to ${D('spread_max')}`, 960, 275, { align: 'center', kind: 'number', alpha: ok * show(t, b.c5.one, b.c6.averaged), claims: ['spread_min', 'spread_max'] });
    // S12: vạch trung bình (ink đứt nét) + vạch nửa điểm riêng (ink-muted liền, "least"); nhãn; chấm vàng Tessa, nhãn trên mọi cột; "little" ngoặc chấm ↔ trung bình
    const [, ya] = sc(X.x0, S.spread_mean * GS, 0.3);
    { const avA = ok * show(t, b.c6.averaged, MV.m_w13.t0), pr = lin(t, b.c6.averaged - 0.05, b.c6.averaged + 0.6);
      seg2(O, xL, ya, mix(xL, xR, pr), ya, C.ink, 0.9 * avA, 4, [12, 9]); log.roi['c6.averaged'] = [xL, ya - 20, xR, ya + 20];
      const [, yh] = sc(X.x0, 0.5 * GS, 0.3), hA = ok * show(t, b.c6.least, MV.m_w13.t0), ph = lin(t, b.c6.least - 0.05, b.c6.least + 0.5);
      seg2(O, xL, yh, mix(xL, xR, ph), yh, C.muted, 0.95 * hA, 3); }
    label(O, `average gap: ${D('spread_mean')}`, 960, 215, { align: 'center', kind: 'number', alpha: ok * show(t, b.c6.zero, MV.m_w13.t0), claims: ['spread_mean'] });
    log.roi['c6.zero'] = [660, 160, 1260, 230]; log.roi['c6.least'] = [xL, sc(0, 3.9)[1], xR, yFloor];
    label(O, `at least half a point: ${D('share_spread_ge_050')}`, 960, 275, { align: 'center', kind: 'number', alpha: ok * show(t, b.c6.two, MV.m_w13.t0), claims: ['share_spread_ge_050'] });
    log.roi['c6.two'] = [500, 225, 1420, 295];
    { const [x, y] = sc(xw(N - 1), sp[N - 1] * GS, 0.3), [, yTop] = sc(xw(S.i.spmax), sp[S.i.spmax] * GS, 0.3), a = ok * show(t, b.c7.eighth, MV.m_w13.t0), c = O.ctx;
      if (a > 0.01) { c.save(); c.globalAlpha = a; c.fillStyle = C.warn; c.strokeStyle = C.bg; c.lineWidth = 3; c.beginPath(); c.arc(x, y, 16 + 5 * pulse(t, b.c7.above, 0.8), 0, 7); c.fill(); c.stroke(); c.restore(); }
      const ly = yTop - 70;
      seg2(O, x, ly + 24, x, y - 20, C.warn, 0.85 * a, 3);
      label(O, `Tessa: ${D('spread_now')} · ILLUSTRATIVE`, 1790, ly, { align: 'right', kind: 'number', px: 48, alpha: a, claims: ['spread_now'], char: 'Tessa' });
      vbrace(O, x + 30, y, ya, C.warn, ok * show(t, b.c7.little, MV.m_w13.t0), 4, 12);
      log.roi['c7.eighth'] = [x - 30, y - 30, x + 30, y + 30]; log.roi['c7.above'] = log.roi['c7.eighth']; log.roi['c7.little'] = [x - 10, Math.min(y, ya) - 10, x + 40, Math.max(y, ya) + 10]; }
    // S13–S15: chồng
    { const [x0] = sc(X.x0, 0, 0.05); log.roi['c8.every'] = [x0, sc(0, 3.6, 0.05)[1], xR, yFloor]; log.roi['c8.rise'] = log.roi['c8.every']; }
    const mark = (i, at, z, s, cl, lx, ly, align) => {
      const [x, y] = sc(xw(i), S.extra[i] * U, 0.05), a = ok * show(t, at, z);
      seg2(O, x, ly + 14, x, y - 8, C.ink, 0.85 * a, 3);
      label(O, s, lx, ly, { align, kind: 'number', alpha: a, claims: cl }); return [x, y];
    };
    { const [x, y] = sc(xw(S.i.min), S.extra[S.i.min] * U, 0.05); log.roi['smallest'] = [x - 30, y - 20, x + 30, yFloor]; }
    { const [x, y] = mark(S.i.min, b.c9.six, b.d0.tallest, `smallest: ${D('extra_total_min')} · ${D('extra_total_min_week_short')}`, ['extra_total_min', 'extra_total_min_week_short'],
        sc(xw(S.i.min), 0)[0], 470, 'center');
      log.roi['c9.six'] = [x - 30, y - 20, x + 30, yFloor]; }
    { const [x, y] = sc(xw(S.i.max), S.extra[S.i.max] * U, 0.05); log.roi['d0.tallest'] = [x - 30, y - 20, x + 30, yFloor]; }
    { const [x, y] = mark(S.i.max, b.d0.twenty, b.d1.median - 0.3, `tallest: ${D('extra_total_max')} · ${D('extra_total_max_week_short')}`, ['extra_total_max', 'extra_total_max_week_short'], 1810, 380, 'right');
      log.roi['d0.twenty'] = [x - 30, y - 20, x + 30, yFloor]; }
    const [, ym] = sc(X.x0, S.median * U, 0.25); log.roi['d1.median'] = [xL, ym - 20, xR, ym + 20];
    const s15 = MV.m_w15.t0 - 0.05, mA = ok * show(t, b.d1.sixteen, b.d2.fewer - 0.1);
    label(O, `median week: ${D('extra_total_median')}`, 960, 215, { align: 'center', kind: 'number', alpha: mA, claims: ['extra_total_median'] });
    seg2(O, 960, 244, 960, ym - 6, C.ink, 0.6 * mA, 2);
    log.roi['d1.sixteen'] = [660, 160, 1260, 230];
    // S15.2: vạch nét đứt từ đỉnh the stack qua cả hàng; nhãn; chồng tuần của Tessa (đầu phải) sáng + số ngay trên chồng
    { const [sx, sy] = sc(X.stack + 0.45, G.stack_total * U, 0), fA = ok * show(t, b.d2.fewer, s15);
      seg2(O, sx, sy, mix(sx, xR, lin(t, b.d2.fewer, b.d2.fewer + 0.6)), sy, C.ink, 0.85 * fA, 4, [14, 10]);
      log.roi['d2.fewer'] = [sx, sy - 30, xR, yFloor]; log.roi['d3.expensive'] = [sc(X.stack - 0.5, 0)[0], sy - 20, sx + 10, yFloor];
      label(O, `as tall or taller: ${D('share_extra_ge_now')}`, 960, 275, { align: 'center', kind: 'number', alpha: ok * show(t, b.d2.one, s15), claims: ['share_extra_ge_now'] });
      log.roi['d2.one'] = [460, 225, 1460, 295];
      const hA = ok * show(t, b.d2.high, s15), [nx, ny] = sc(xw(N - 1), S.extra[N - 1] * U, 0.12), [, yMax] = sc(xw(S.i.max), S.extra[S.i.max] * U, 0.05), ly = yMax - 60;
      seg2(O, nx, ly + 24, nx, ny - 8, C.ink, 0.85 * hA, 3);
      label(O, `Tessa's stack: ${D('extra_vs15_total_now')} · ILLUSTRATIVE`, 1810, ly, { align: 'right', kind: 'number', alpha: hA, claims: ['extra_vs15_total_now'], char: 'Tessa' });
      log.roi['d2.high'] = [nx - 40, ny - 20, nx + 20, yFloor]; }
    { const [hx, hy] = sc(hm.person.position.x, hm.h, hm.person.position.z); log.roi['d4.worth'] = [hx - 90, hy - 90, hx + 90, hy + 60]; log.roi['d4.measure'] = log.roi['d4.worth']; }
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
