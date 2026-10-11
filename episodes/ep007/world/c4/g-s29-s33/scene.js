// Tập 7 · C4 · ĐOẠN G = S29–S33. Leo (ILLUSTRATIVE, màu riêng, BÊN TRÁI Tessa) mọc cùng nhà; chồng của Leo thấp, hộp cushion rộng, thanh thấp — cạnh cụm
// của Tessa (chồng cao, thanh cao) → ô thứ ba trống (thanh trống, chồng trống: "your bar", "your stack") → thẻ phương pháp V7 → khung cold open: hai thẻ
// khoản vay trượt vào nhau thành "30-year paid in 15 = 15-year + a fallback", "week of Oct 8, 2026: $120 a month". Mốc giờ chỉ từ spine.json.
import { setup, figure, gesture, figTag, OfferCard, theStack, stackSet, BUNDLE_TH, modeLook, followLight, chrome, label, seg2, dip, CHAR,
  kf, show, pulse, C, ease, lin, mix, THREE, setOpacity } from '/episodes/ep007/world/c4kit.js';
import { Beam } from '/toolkit/factory/world/lib3d.js';

const SEG = '/episodes/ep007/world/c4/g-s29-s33/';
const PER_PCT = 0.3, GAP_U = 1 / 500;   // thanh: 0,3/điểm % (như S25); hộp cushion: 1/500 đơn vị mỗi $/tháng của khoảng chênh khoản trả

export async function boot(res) {
  const poses = {
    wPair0: { pos: [-3.0, 3.2, 11.5], tgt: [-1.4, 1.1, 0], fov: 44, chart: 0 },
    cPair: { pos: [-2.0, 1.7, 19.14], tgt: [-2.0, 1.7, 0], fov: 20, chart: 1 },
    cThree: { pos: [-0.4, 1.9, 24.24], tgt: [-0.4, 1.9, 0], fov: 20, chart: 1 },
    wHome: { pos: [-2.2, 2.7, 8.6], tgt: [1.7, 0.9, 0], fov: 40, chart: 0 },
    cHome: { pos: [1.2, 2.2, 16.93], tgt: [1.2, 2.2, 0], fov: 22, chart: 1 },
  };
  const { S, D, G, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue, X = S.x;
  const hm = figure(scene, { x: X.house }), leo = figure(scene, { x: X.leo_house, color: CHAR.leo, char: 'Leo' });
  const tStack = theStack(scene, G, { x: X.stack }), lStack = theStack(scene, G, { x: X.leo_stack });
  stackSet(tStack, G.stack_total); lStack.userData.checks.key = 'leo-stack'; lStack.userData.checks.char = 'Leo';
  const mkBeam = (x, key) => { const m = Beam({ length: 1.0 }); m.scale.set(1, 2.2, 1.4); m.position.x = x; scene.add(m); m.userData.checks = { role: 'mark', series: 'bar', key }; return m; };
  const tBar = mkBeam(X.bar, 'the-bar'), lBar = mkBeam(X.leo_bar, 'leo-bar'), blankBar = mkBeam(X.blank_bar, 'your-bar');
  tBar.position.y = G.bar * PER_PCT;
  const room = (x, gap) => { const m = new THREE.Mesh(new THREE.BoxGeometry(0.5, 1, 0.14), new THREE.MeshStandardMaterial({ color: C.cushion, emissive: new THREE.Color(C.cushion), emissiveIntensity: 0.45, transparent: true, depthWrite: false }));
    m.geometry.translate(0, 0.5, 0); m.position.set(x, 0, 1.0); m.userData.h = gap * GAP_U; m.userData.checks = { role: 'mark', key: `fallback-room-${x}`, value: gap }; scene.add(m); return m; };
  const lRoom = room(X.leo_house, S.gap.leo), tRoom = room(X.house, S.gap.tessa);
  const blankStack = new THREE.Mesh(new THREE.BoxGeometry(0.9, 2.0, 0.6), new THREE.MeshStandardMaterial({ color: C.muted, transparent: true, opacity: 0.12, depthWrite: false }));
  blankStack.position.set(X.blank_stack, 1.0, 0); scene.add(blankStack); blankStack.userData.checks = { role: 'mark', key: 'your-stack' };
  const card15 = OfferCard(scene, { x: X.cards[0], y: 4.0, w: 3.6, h: 0.8 }), card30 = OfferCard(scene, { x: X.cards[1], y: 4.0, w: 3.6, h: 0.8 }), cardM = OfferCard(scene, { x: X.merge, y: 4.0, w: 7.4, h: 0.9 });
  const leoH = leo.house, leoP = leo.person;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw); gesture(hm, t, S.gestures); gesture(leo, t, S.leo_gestures);
    // S29: nhà + Leo mọc ở "illustrative"
    const lv = ease(t, b.g0.illustrative - 0.1, b.g0.illustrative + 0.8);
    leoH.scale.set(1, Math.max(0.001, lv), 1); leoH.visible = lv > 0.01; leoP.scale.setScalar(Math.max(0.001, lv)); leoP.visible = lv > 0.01;
    stackSet(lStack, kf(S.leo_stack, t));
    // thanh: của Tessa đứng sẵn ở 7.40 % (từ đoạn f); của Leo trồi ở "bar" tới 2.65 %; thanh trống ở ô thứ ba
    const lu = ease(t, b.g3.bar - 0.02, b.g3.bar + 0.6); lBar.position.y = -0.12 + (0.12 + S.leo_bar * PER_PCT) * lu; lBar.visible = lu > 0.01;
    const glow = (m, ...ts) => m.glow(0.7 * Math.max(...ts.map(([a, d]) => pulse(t, a, d))), C.ink);
    glow(tBar, [b.g5.high, 1.0], [b.j0.high, 1.2], [b.h1.bar, 0.9]); glow(lBar, [b.g5.low, 1.0], [b.g3.earned, 1.0]);
    const bA = show(t, b.h0.pair) * (1 - ease(t, MV.m_w33.t0, MV.m_w33.t0 + 0.4));
    setOpacity(blankBar, 0.35 * bA); blankBar.position.y = 1.5; blankBar.glow(0.6 * pulse(t, b.h1.bar, 1.0), C.ink);
    blankStack.material.opacity = (0.12 + 0.2 * pulse(t, b.h1.stack, 1.0)) * bA; blankStack.visible = bA > 0.01;
    // hộp cushion (đường lui): Leo ở "room", Tessa ngay sau (nhỏ hơn); tắt khi về khung cold open
    const rEnd = 1 - ease(t, MV.m_w33.t0, MV.m_w33.t0 + 0.4);
    for (const [m, a] of [[lRoom, b.g2.room], [tRoom, b.g2.room + 0.3]]) { const u = ease(t, a - 0.05, a + 0.6) * rEnd; m.scale.y = Math.max(0.001, m.userData.h * u); m.visible = u > 0.01;
      m.material.opacity = 0.42 + 0.3 * (m === tRoom ? pulse(t, b.h2.fallback, 1.0) : 0); }
    // S33: hai thẻ → trượt vào nhau ở "plus" → một thẻ có dải cushion
    const mg = ease(t, b.j2.plus - 0.05, b.j2.plus + 0.8);
    card15.position.x = mix(X.cards[0], X.merge, mg); card30.position.x = mix(X.cards[1], X.merge, mg);
    card15.set({ a: show(t, b.j1.fifteen) * (1 - mg) }); card30.set({ a: show(t, b.j1.thirty) * (1 - mg) });
    cardM.set({ a: mg, band: ease(t, b.j2.fallback - 0.05, b.j2.fallback + 0.8) });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 1 - ease(t, 0, 0.4));
    const cardA = ok * show(t, b.i0.method, MV.m_w33.t0 - 0.05);
    dip(O, 0.72 * cardA);                     // thẻ V7: thế giới lùi sau, vẽ TRƯỚC mọi chữ
    figTag(O, hm); figTag(O, leo, lv * (1 - ease(t, MV.m_w33.t0, MV.m_w33.t0 + 0.3)));   // khung cold open (S33): chỉ Tessa
    const sc = (x, y, z = 0) => O.toScreen(x, y, z), p31 = MV.m_pan31.t0 - 0.05;
    { const [x, y] = sc(X.leo_house, 1.0); log.roi['g0.illustrative'] = [x - 200, y - 150, x + 200, y + 120]; }
    // S29–S30: nhãn của Leo (ba hàng trái), của Tessa (hàng phải)
    label(O, `Leo · ILLUSTRATIVE · ${D('r30_min_week_short')} · ${D('term_long')} at ${D('leo_r30')}`, 130, 205, { kind: 'number', alpha: ok * show(t, b.g0.lowest, p31), char: 'Leo',
      claims: ['r30_min_week_short', 'term_long', 'leo_r30'] });
    log.roi['g0.lowest'] = [120, 150, 1500, 230];
    { const [x, y] = sc(X.leo_stack, S.leo_total / G.bundle_usd * BUNDLE_TH), [, y0] = sc(X.leo_stack, 0); log.roi['g0.paid'] = [x - 70, y - 20, x + 70, y0];
      const [tx, ty] = sc(X.stack - 0.45, G.stack_total / G.bundle_usd * BUNDLE_TH), a = ok * show(t, b.g1.cheaper, p31);
      seg2(O, x + 60, y, mix(x + 60, tx, lin(t, b.g1.cheaper, b.g1.cheaper + 0.6)), y, C.ink, 0.8 * a, 4, [14, 10]);
      log.roi['g1.cheaper'] = [x - 70, y - 30, tx, y + 30]; }
    label(O, `Leo's stack: ${D('leo_extra_vs15_total')} (${D('leo_extra_vs15_month')})`, 130, 268, { kind: 'number', alpha: ok * show(t, b.g1.thirteen, p31), char: 'Leo',
      claims: ['leo_extra_vs15_total', 'leo_extra_vs15_month'] });
    log.roi['g1.thirteen'] = [120, 215, 1150, 290];
    label(O, `Leo: fallback ${D('leo_fallback_gap')}`, 130, 331, { kind: 'number', alpha: ok * show(t, b.g2.seven, p31), char: 'Leo', claims: ['leo_fallback_gap'] });
    log.roi['g2.seven'] = [120, 280, 1060, 350];
    { const [x, y] = sc(X.leo_house, 0, 1.0), [, y1] = sc(X.leo_house, S.gap.leo * GAP_U, 1.0); log.roi['g2.room'] = [x - 60, y1 - 20, x + 60, y]; }
    { const [x, y] = sc(X.leo_bar, S.leo_bar * PER_PCT), [, y0] = sc(X.leo_bar, 0);
      label(O, `bar ${D('leo_r30')}`, Math.max(250, x), y - 44, { align: 'center', kind: 'number', alpha: ok * show(t, b.g3.two, p31), char: 'Leo', claims: ['leo_r30'] });
      log.roi['g3.bar'] = [x - 90, y - 20, x + 90, y0]; log.roi['g3.two'] = [x - 160, y - 90, x + 160, y - 30]; log.roi['g3.earned'] = log.roi['g3.bar'];
      log.roi['g5.low'] = log.roi['g3.bar']; }
    // S30.3: thẻ tuần trên mái hai nhà
    { const wA = ok * show(t, b.g4.different, p31), [lx, ly] = sc(X.leo_house, 1.75), [tx, ty] = sc(X.house, 1.75);
      label(O, D('r30_min_week_short'), lx, ly - 30, { align: 'center', kind: 'number', px: 48, alpha: wA, char: 'Leo', claims: ['r30_min_week_short'] });
      label(O, D('last_week_short'), tx, ty - 30, { align: 'center', kind: 'number', px: 48, alpha: wA, char: 'Tessa', claims: ['last_week_short'] });
      log.roi['g4.different'] = [lx - 140, ly - 80, lx + 140, ly - 15]; log.roi['g4.same'] = [sc(X.leo_bar - 0.6, 0)[0], sc(0, 2.8)[1], sc(X.stack + 0.5, 0)[0], sc(0, 0)[1]]; }
    { const [x, y] = sc(X.leo_stack, S.leo_total / G.bundle_usd * BUNDLE_TH), [, y0] = sc(X.leo_stack, 0); log.roi['g5.short'] = [x - 70, y - 20, x + 70, y0]; }
    { const [x, y] = sc(X.stack, G.stack_total / G.bundle_usd * BUNDLE_TH), [, y0] = sc(X.stack, 0); log.roi['g5.tall'] = [x - 70, y - 20, x + 70, y0]; log.roi['j0.tall'] = log.roi['g5.tall']; }
    { const [x, y] = sc(X.bar, G.bar * PER_PCT); log.roi['g5.high'] = [x - 90, y - 30, x + 90, y + 30]; log.roi['j0.high'] = log.roi['g5.high']; }
    label(O, `Tessa · ILLUSTRATIVE: stack ${D('extra_vs15_total_now')} · bar ${D('r30_now')}`, 1800, 394, { align: 'right', kind: 'number', alpha: ok * show(t, b.g5.tessa, p31), char: 'Tessa',
      claims: ['extra_vs15_total_now', 'r30_now'] });
    log.roi['g5.tessa'] = [440, 345, 1800, 415];
    // S31: ô thứ ba trống — viền nét đứt quanh thanh trống và chồng trống; ba nhãn (cột phải)
    if (bA > 0.01) {
      const box = (x0, y0, x1, y1) => { const P = [[x0, y0], [x1, y0], [x1, y1], [x0, y1]].map(([x, y]) => sc(x, y, 0.3)), c = O.ctx; c.save(); c.globalAlpha = 0.85 * bA; c.strokeStyle = C.muted; c.lineWidth = 3; c.setLineDash([10, 8]);
        c.beginPath(); P.forEach(([x, y], i) => (i ? c.lineTo(x, y) : c.moveTo(x, y))); c.closePath(); c.stroke(); c.restore(); };
      box(X.blank_bar - 0.55, 1.38, X.blank_bar + 0.55, 1.62); box(X.blank_stack - 0.48, 0, X.blank_stack + 0.48, 2.0);
    }
    { const [x0, y0] = sc(X.blank_bar - 0.6, 2.1), [x1, y1] = sc(X.blank_stack + 0.5, 0); log.roi['h0.pair'] = [x0, y0, x1, y1]; }
    const fin = b.i0.method - 0.45;   // ba nhãn S31 tắt hẳn trước khi thẻ V7 hiện
    label(O, "your bar = your loan's own rate", 1810, 205, { align: 'right', kind: 'name', alpha: ok * show(t, b.h1.bar, fin) });
    label(O, 'your stack = how far apart', 1810, 268, { align: 'right', kind: 'name', alpha: ok * show(t, b.h1.stack, fin) });
    label(O, `the ${D('term_short')} and ${D('term_long')} offers sit`, 1810, 331, { align: 'right', kind: 'number', alpha: ok * show(t, b.h1.stack, fin), claims: ['term_short', 'term_long'] });
    log.roi['h1.bar'] = [900, 150, 1810, 230]; log.roi['h1.stack'] = [800, 215, 1810, 350];
    label(O, 'a dollar in the house is hard to get back', 1810, 394, { align: 'right', kind: 'compare', alpha: ok * show(t, b.h2.hard, fin) });
    log.roi['h2.hard'] = [600, 345, 1810, 415];
    { const [x, y] = sc(X.house, 1.0); log.roi['h2.house'] = [x - 200, y - 150, x + 200, y + 120]; const [rx, ry] = sc(X.house, 0, 1.0); log.roi['h2.fallback'] = [rx - 60, ry - 160, rx + 60, ry]; }
    // S32: thẻ phương pháp V7 (tiêu đề + 9 dòng, giữ qua cả hai câu)
    if (cardA > 0.01) {
      O.card(120, 140, 1680, 680, { fill: '#11161E', stroke: '#3A4250', lw: 3, alpha: 0.96 * cardA });
      label(O, 'How we know this', 150, 215, { kind: 'title', px: 60, alpha: cardA, plate: null });
      const L = [[`weekly US survey averages: ${D('n_weeks')} from ${D('first_week_short')}`, ['n_weeks', 'first_week_short']],
        ['strong-credit borrowers; points and fees differ'], ['principal and interest only: no property taxes,'], ['insurance, PMI or tax deductions'],
        ['the bar is before taxes; no investment or market return tested'], ['value of the fallback in a job loss or emergency: not measured'],
        [`Tessa · ILLUSTRATIVE: rates of the week of ${D('last_week_short')},`, ['last_week_short']], [`on ${D('principal')} only`, ['principal']],
        ['US only · History, not a forecast · Not advice on which loan']];
      L.forEach(([s, cl], k) => label(O, s, 150, 290 + 60 * k, { kind: cl ? 'number' : 'compare', px: 48, alpha: cardA, plate: null, claims: cl,
        color: k === L.length - 1 ? (t > b.i1.say ? C.ink : '#C9D1DC') : '#C9D1DC' }));
      log.roi['i0.method'] = [120, 140, 1800, 820]; log.roi['i1.say'] = [140, 730, 1800, 790];
    }
    { const c = O.ctx; c.save(); c.font = '600 54px Inter'; const w1 = c.measureText('US only').width, w0 = c.measureText('US only · ').width, wAll = c.measureText('US only · history, not a forecast').width; c.restore();
      seg2(O, 96, 1024, 96 + w1, 1024, C.ink, 0.9 * show(t, b.i1.only, MV.m_w33.t1), 4); seg2(O, 96 + w0, 1024, 96 + wAll, 1024, C.ink, 0.9 * show(t, b.i1.history, MV.m_w33.t1), 4);
      log.roi['i1.only'] = [90, 960, 96 + w1 + 6, 1030]; log.roi['i1.history'] = [96 + w0 - 6, 960, 96 + wAll + 6, 1030]; }
    // S33: chữ trên hai thẻ → một thẻ; giá tuần
    for (const [card, s, cl, at, id] of [[card15, `${D('term_short')} mortgage`, ['term_short'], b.j1.fifteen, 'j1.fifteen'], [card30, `${D('term_long')} paid ${D('paid_in_short')}`, ['term_long', 'paid_in_short'], b.j1.thirty, 'j1.thirty']]) {
      const [x, y] = sc(card.position.x, card.position.y, 0.05);
      label(O, s, x, y + 16, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, at) * (1 - ease(t, b.j2.plus - 0.3, b.j2.plus)), claims: cl });
      log.roi[id] = [x - 300, y - 60, x + 300, y + 60];
    }
    { const [x, y] = sc(X.merge, 4.0, 0.05);
      label(O, `${D('term_long')} paid ${D('paid_in_short')} = ${D('term_short')} + a fallback`, x, y + 14, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.j2.plus), claims: ['term_long', 'paid_in_short', 'term_short'] });
      log.roi['j2.plus'] = [x - 620, y - 70, x + 620, y + 70]; log.roi['j2.fallback'] = [x - 620, y + 10, x + 620, y + 80]; }
    label(O, `week of ${D('last_week_short')}: ${D('extra_vs15_month_now')}`, 960, 392, { align: 'center', kind: 'number', alpha: ok * show(t, b.j2.one), claims: ['last_week_short', 'extra_vs15_month_now'] });
    log.roi['j2.one'] = [500, 340, 1420, 410];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
