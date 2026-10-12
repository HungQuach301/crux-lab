// Tập 7 · C4 · ĐOẠN G = S29–S33. Leo (ILLUSTRATIVE, màu riêng, BÊN TRÁI Tessa) trượt vào cùng nhà + cọc lịch; chồng của Leo thấp, ngoặc cushion rộng,
// thanh thấp — cạnh cụm của Tessa (chồng cao, ngoặc hẹp hơn, thanh cao) → ô thứ ba trống giữa khung (người nét đứt, thanh trống được tờ giấy nâng lên,
// chồng trống co/giãn) + tờ đô la vào nhà gặp khoá → thẻ phương pháp V7 → khung cold open: hai thẻ khoản vay trượt vào nhau thành
// "30-year paid in 15 = 15-year + a fallback", một tờ đô la rơi khỏi chồng: "week of Oct 8, 2026: $120 a month". Mốc giờ chỉ từ spine.json.
import { setup, figure, gesture, figTag, OfferCard, theStack, stackSet, BUNDLE_TH, modeLook, followLight, chrome, label, brace, seg2, dip, CHAR,
  kf, show, pulse, C, ease, lin, mix, THREE, setOpacity } from '/episodes/ep007/world/c4kit.js';
import { Beam } from '/toolkit/factory/world/lib3d.js';
import { Bill } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c4/g-s29-s33/';
const PER_PCT = 0.3, GAP_U = 1 / 400, BY = 2.0;   // thanh: 0,3/điểm % (như S25); ngoặc cushion (V6): 1/400 đơn vị mỗi $/tháng, nằm ngang ở độ cao BY (trên mái)

export async function boot(res) {
  const poses = {
    wPair0: { pos: [-3.0, 3.2, 11.5], tgt: [-1.4, 1.1, 0], fov: 44, chart: 0 },
    cPair: { pos: [-2.0, 1.7, 19.14], tgt: [-2.0, 1.7, 0], fov: 20, chart: 1 },
    // cThree (C5): lia + dolly — ô thứ ba vào giữa khung, Tessa + nhà vẫn ở bên trái ("beside hers"); lề phải cho dây dẫn của hai nhãn S31
    cThree: { pos: [3.0, 1.9, 16.5], tgt: [3.0, 1.9, 0], fov: 20, chart: 1 },
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
  const lit = (s, a) => { const m = s.children[0].material; m.emissive.set(C.ink); m.emissiveIntensity = 0.5 * a; };   // chồng loé (S30.4, S31.3, S33.1)
  // ô thứ ba (C4 r4): thanh trống / chồng trống chỉ còn lớp mờ rất nhẹ — hình chính là viền nét đứt vẽ ở lớp phủ (không đặc)
  const blankStack = new THREE.Mesh(new THREE.BoxGeometry(0.9, 1.0, 0.6), new THREE.MeshStandardMaterial({ color: C.muted, transparent: true, opacity: 0.06, depthWrite: false }));
  blankStack.geometry.translate(0, 0.5, 0); blankStack.position.set(X.blank_stack, 0, 0); scene.add(blankStack); blankStack.userData.checks = { role: 'mark', key: 'your-stack' };
  // S31.2 "printed on the paperwork": tờ giấy (mặt sáng, dòng chữ giả, không số) trượt vào dưới thanh trống
  const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.8, transparent: true, ...o });
  const paper = new THREE.Group(); paper.add(new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.66, 0.02), mat('#E6E9EE', { emissive: new THREE.Color('#E6E9EE'), emissiveIntensity: 0.15 })));
  for (const [dy, w] of [[0.18, 0.34], [0.08, 0.34], [-0.02, 0.34], [-0.12, 0.2]]) { const l = new THREE.Mesh(new THREE.BoxGeometry(w, 0.025, 0.01), mat('#5B6573')); l.position.set(-(0.34 - w) / 2, dy, 0.015); paper.add(l); }
  paper.position.set(X.blank_bar, 0.33, 0.35); scene.add(paper); paper.userData.checks = { role: 'mark', key: 'paperwork' };
  // S29 "January": cọc lịch cắm cạnh nhà Leo (thế giới, không chữ — ngày ở nhãn đồ thị)
  const pin = new THREE.Group();
  for (const [w, h, y, c] of [[0.04, 0.7, 0.35, '#8C93A0'], [0.42, 0.34, 0.85, '#E6E9EE'], [0.42, 0.08, 1.04, C.muted]]) { const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.03), mat(c)); m.position.y = y; m.castShadow = true; pin.add(m); }
  pin.position.set(X.leo_pin, 0, 0.9); scene.add(pin); pin.userData.checks = { role: 'mark', key: 'leo-date-pin', char: 'Leo' };
  // S31.3 tờ đô la vào nhà (khó lấy lại); S33.3 tờ $120 rơi khỏi chồng
  const dIn = Bill({ name: 'paid-in' }), d120 = Bill({ name: 'month-120' }); scene.add(dIn, d120);
  const card15 = OfferCard(scene, { x: X.cards[0], y: 4.0, w: 3.6, h: 0.8 }), card30 = OfferCard(scene, { x: X.cards[1], y: 4.0, w: 3.6, h: 0.8 }), cardM = OfferCard(scene, { x: X.merge, y: 4.0, w: 7.4, h: 0.9 });
  const leoH = leo.house, leoP = leo.person;
  const tCore = tBar.userData.core, hand = [hm.person.position.x + 0.35, 0.62, hm.person.position.z + 0.15], door = [X.house, 0.25, 0.62];

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    // cụm Leo: trượt vào từ trái ở "illustrative"; tắt hẳn khi về khung cold open (S33 chỉ cụm Tessa)
    const sl = ease(t, b.g0.illustrative - 0.4, b.g0.illustrative + 0.8), lo = 1 - ease(t, MV.m_w33.t0 + 0.2, MV.m_w33.t0 + 0.7), dx = -3.2 * (1 - sl);
    leoH.position.x = X.leo_house + dx; leoP.position.x = X.leo_person + dx;
    leoH.scale.setScalar(Math.max(0.001, 0.6 + 0.4 * sl)); leoP.scale.setScalar(Math.max(0.001, 0.6 + 0.4 * sl)); leoH.visible = leoP.visible = sl > 0.01 && lo > 0.01;
    gesture(hm, t, S.gestures); gesture(leo, t, S.leo_gestures);
    const pu = ease(t, b.g0.january - 0.05, b.g0.january + 0.35); pin.position.y = 1.4 * (1 - pu) ** 2; setOpacity(pin, pu); pin.visible = pu > 0.01 && lo > 0.01;
    pin.scale.setScalar(1 + 0.15 * pulse(t, b.g4.different, 0.8));
    stackSet(lStack, kf(S.leo_stack, t)); lStack.visible = lo > 0.01;
    lit(lStack, Math.max(pulse(t, b.g5.short, 1.2), pulse(t, b.g1.cheaper, 0.8)));
    lit(tStack, Math.max(pulse(t, b.g5.tall, 1.2), pulse(t, b.j0.tall, 1.2), pulse(t, b.h2.fallback, 1.2)));
    // thanh: của Leo trồi ở "bar" tới 2.65 % (xa đầu Leo); của Tessa trồi ngay sau (không trôi nổi từ đầu đoạn); S33: thanh dày, ở "fallback" trượt vào cạnh chồng
    const lu = ease(t, b.g3.bar - 0.02, b.g3.bar + 0.6); lBar.position.y = -0.12 + (0.12 + S.leo_bar * PER_PCT) * lu; lBar.visible = lu > 0.01 && lo > 0.01;
    const tu = ease(t, b.g3.bar + 0.25, b.g3.bar + 0.9), th = ease(t, MV.m_w33.t0, MV.m_w33.t1), tm = ease(t, b.j2.fallback - 0.05, b.j2.fallback + 0.8);
    tBar.position.y = -0.12 + (0.12 + G.bar * PER_PCT) * tu; tBar.visible = tu > 0.01; tCore.scale.set(1, 1 + 1.6 * th, 1 + 1.6 * th);
    tBar.position.x = mix(X.bar, X.stack + 1.2, tm);
    const glow = (m, ...ts) => m.glow(0.7 * Math.max(...ts.map(([a, d]) => pulse(t, a, d))), C.ink);
    glow(tBar, [b.g5.high, 1.2], [b.j0.high, 1.2], [b.h1.bar, 0.9]); glow(lBar, [b.g5.low, 1.2], [b.g3.earned, 1.0]);
    // S31.1: ô thứ ba hiện ở "Any" (đế trước, thanh + chồng trống ngay sau), loé ở "pair"; thanh nằm sát sàn tới khi tờ giấy trượt vào ("printed") và nâng nó lên
    const bA = ease(t, b.h0.any - 0.05, b.h0.any + 0.6) * (1 - ease(t, MV.m_w33.t0, MV.m_w33.t0 + 0.4)), oA = bA * ease(t, b.h0.any + 0.2, b.h0.any + 0.8);
    const pp = ease(t, b.h1.paper - 0.05, b.h1.paper + 0.5), lift = ease(t, b.h1.paper + 0.35, b.h1.paper + 1.1), yB = mix(0.12, 1.5, lift);
    setOpacity(blankBar, 0.12 * oA); blankBar.position.y = yB; blankBar.visible = oA > 0.01; blankBar.glow(0.6 * pulse(t, b.h1.bar, 1.0), C.ink);
    paper.position.x = X.blank_bar + 2.6 * (1 - pp); setOpacity(paper, pp * oA); paper.visible = pp * oA > 0.01;
    // S31.2 "how far apart … sit": chồng trống co/giãn (khoảng cách hai đề nghị đổi → chồng đổi)
    const env = ease(t, b.h1.apart - 0.05, b.h1.apart + 0.3) * (1 - ease(t, b.h1.sit, b.h1.sit + 0.5)), hS = 2.0 * (1 + 0.32 * env * Math.sin((2 * Math.PI * (t - b.h1.apart)) / 1.5));
    blankStack.scale.y = hS; blankStack.material.opacity = (0.06 + 0.12 * pulse(t, b.h1.stack, 1.0)) * oA; blankStack.visible = oA > 0.01;
    // S31.3: tờ đô la từ tay Tessa bay vòng vào cửa nhà ("dollar" → "house"), ở "back" nhô ra rồi bị khoá chặn, lùi vào
    { const u = ease(t, b.h2.dollar + 0.15, b.h2.house), a = show(t, b.h2.dollar) * (1 - ease(t, b.h2.house - 0.15, b.h2.house + 0.05)), k = ease(t, b.h2.back - 0.05, b.h2.back + 0.25) * (1 - ease(t, b.h2.back + 0.8, b.h2.back + 1.2));
      const sh = 0.03 * Math.sin(40 * (t - b.h2.back)) * pulse(t, b.h2.back + 0.25, 0.5);
      dIn.rotation.x = Math.PI / 2; dIn.position.set(mix(hand[0], door[0], u) + sh, mix(hand[1], door[1] + 0.12, u) + 0.6 * Math.sin(Math.PI * u), mix(hand[2], door[2], u) + 0.3 * k);
      const s = Math.max(a, 0.55 * k); dIn.scale.setScalar(Math.max(0.001, s)); dIn.visible = s > 0.01; }
    // S33: hai thẻ (xa nhau) nảy khi lời gọi tên, TRƯỢT vào nhau từ "fifteen-year" tới ngay sau "plus" → một thẻ có dải cushion
    const mg = ease(t, b.j2.fifteen - 0.1, b.j2.plus + 0.2);
    card15.position.set(mix(X.cards[0], X.merge, mg), 4.0 + 0.15 * pulse(t, b.j2.fifteen, 0.6), 0); card30.position.set(mix(X.cards[1], X.merge, mg), 4.0 + 0.15 * pulse(t, b.j2.thirty, 0.6), 0);
    card15.set({ a: show(t, b.j1.fifteen) * (1 - ease(mg, 0.75, 1.0)) }); card30.set({ a: show(t, b.j1.thirty) * (1 - ease(mg, 0.75, 1.0)) });
    cardM.set({ a: ease(mg, 0.65, 1.0), band: ease(t, b.j2.fallback - 0.05, b.j2.fallback + 0.8) });
    // S33.3 "one": một tờ đô la rơi khỏi đỉnh chồng xuống sàn trước chồng
    { const u = ease(t, b.j2.one - 0.05, b.j2.one + 0.55), a = show(t, b.j2.one);
      d120.rotation.x = (Math.PI / 2) * (0.35 + 0.65 * u); d120.position.set(X.stack + 0.15 * u, mix(G.stack_total / G.bundle_usd * BUNDLE_TH + 0.15, 0.16, u * u), mix(0.0, 0.85, u));
      d120.scale.setScalar(Math.max(0.001, a)); d120.visible = a > 0.01; }
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 1 - ease(t, 0, 0.4));
    const cardA = ok * show(t, b.i0.method, MV.m_w33.t0 - 0.05);
    dip(O, 0.72 * cardA);                     // thẻ V7: thế giới lùi sau, vẽ TRƯỚC mọi chữ
    figTag(O, hm); figTag(O, leo, sl * (1 - ease(t, MV.m_w33.t0, MV.m_w33.t0 + 0.3)));   // khung cold open (S33): chỉ Tessa
    const sc = (x, y, z = 0) => O.toScreen(x, y, z), p31 = MV.m_pan31.t0 - 0.05;
    { const [x, y] = sc(X.leo_house, 1.0); log.roi['g0.illustrative'] = [x - 200, y - 150, x + 200, y + 120]; }
    { const [x, y] = sc(X.leo_pin, 1.0, 0.9); log.roi['g0.january'] = [x - 60, y - 60, x + 60, y + 80]; }
    // S29: hai nhãn của Leo (hàng trái), tắt ở S30.3 — S30.4 không khối chữ
    const pL = b.g4.same - 0.1;
    label(O, `Leo · ${D('r30_min_week_short')} · ${D('term_long')} at ${D('leo_r30')}`, 130, 205, { kind: 'number', alpha: ok * show(t, b.g0.lowest, pL), char: 'Leo',
      claims: ['r30_min_week_short', 'term_long', 'leo_r30'] });
    log.roi['g0.lowest'] = [120, 150, 1100, 230];
    { const [x, y] = sc(X.leo_stack, S.leo_total / G.bundle_usd * BUNDLE_TH), [, y0] = sc(X.leo_stack, 0); log.roi['g0.paid'] = [x - 70, y - 20, x + 70, y0];
      const [tx] = sc(X.stack - 0.45, G.stack_total / G.bundle_usd * BUNDLE_TH), a = ok * show(t, b.g1.cheaper, b.g2.room);
      seg2(O, x + 60, y, mix(x + 60, tx, lin(t, b.g1.cheaper, b.g1.cheaper + 0.6)), y, C.ink, 0.8 * a, 4, [14, 10]);
      log.roi['g1.cheaper'] = [x - 70, y - 30, tx, y + 30]; }
    label(O, `Leo's stack: ${D('leo_extra_vs15_total')} (${D('leo_extra_vs15_month')})`, 130, 268, { kind: 'number', alpha: ok * show(t, b.g1.thirteen, pL), char: 'Leo',
      claims: ['leo_extra_vs15_total', 'leo_extra_vs15_month'] });
    log.roi['g1.thirteen'] = [120, 215, 1150, 290];
    // S30.1 (C5 đúng-số): NGOẶC V6 cushion ngang trên mái mỗi nhà, độ rộng = khoảng khoản bắt buộc dưới khoản 15 năm (cùng thang: Leo ~$793 rộng hơn
    // Tessa ~$613); mọc từ giữa ra ở "room"; nhãn trên ngoặc ở "seven" (tắt khi thanh trồi); ngoặc của Tessa loé ở S31.3 "fallback"; tắt khi về cold open
    const rEnd = 1 - ease(t, MV.m_w33.t0, MV.m_w33.t0 + 0.4), bEnd = b.g3.bar - 0.1, lb = {};
    for (const [id, xc, gap, a0, kk] of [['leo', X.leo_house, S.gap.leo, b.g2.room, lo], ['tessa', X.house, S.gap.tessa, b.g2.room + 0.3, 1]]) {
      const u = ease(t, a0 - 0.05, a0 + 0.6), hw = gap * GAP_U / 2 * Math.max(0.02, u), [x0, y] = sc(xc - hw, BY), [x1] = sc(xc + hw, BY), fb = id === 'tessa' ? pulse(t, b.h2.fallback, 1.4) : 0;
      brace(O, x0, x1, y, C.cushion, ok * u * rEnd * kk * (0.85 + 0.15 * fb), 7 + 5 * fb, 18);
      lb[id] = [(x0 + x1) / 2, y - 22]; log.roi[id === 'leo' ? 'g2.room' : 'g2.room.tessa'] = [x0 - 10, y - 20, x1 + 10, y + 30];
      if (id === 'tessa') log.roi['h2.fallback'] = [x0 - 10, y - 30, x1 + 10, y + 40];
    }
    label(O, `${D('leo_fallback_gap')} below the ${D('term_short')}`, lb.leo[0], lb.leo[1], { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.g2.seven, bEnd), char: 'Leo',
      claims: ['leo_fallback_gap', 'term_short'] });
    label(O, D('fallback_gap_now'), lb.tessa[0], lb.tessa[1], { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.g2.seven, bEnd), char: 'Tessa', claims: ['fallback_gap_now'] });
    log.roi['g2.seven'] = [lb.leo[0] - 500, lb.leo[1] - 50, lb.leo[0] + 500, lb.leo[1] + 15];
    // thanh của Leo: nhãn canh trái từ đầu trái thanh (không đè đầu Leo)
    { const [x, y] = sc(X.leo_bar, S.leo_bar * PER_PCT), [, y0] = sc(X.leo_bar, 0), [xl] = sc(X.leo_bar - 0.5, 0);
      label(O, `bar ${D('leo_r30')}`, Math.max(110, xl), y - 44, { kind: 'number', alpha: ok * show(t, b.g3.two, p31), char: 'Leo', claims: ['leo_r30'] });
      log.roi['g3.bar'] = [x - 90, y - 20, x + 90, y0]; log.roi['g3.two'] = [xl - 20, y - 90, xl + 300, y - 30]; log.roi['g3.earned'] = log.roi['g3.bar'];
      log.roi['g5.low'] = log.roi['g3.bar']; }
    // S30.3: thẻ tuần ngay trên hai ngoặc (chỗ nhãn ngoặc vừa tắt)
    { const wA = ok * show(t, b.g4.different, p31);
      label(O, D('r30_min_week_short'), lb.leo[0], lb.leo[1], { align: 'center', kind: 'number', px: 48, alpha: wA, char: 'Leo', claims: ['r30_min_week_short'] });
      label(O, D('last_week_short'), lb.tessa[0], lb.tessa[1], { align: 'center', kind: 'number', px: 48, alpha: wA, char: 'Tessa', claims: ['last_week_short'] });
      log.roi['g4.different'] = [lb.leo[0] - 140, lb.leo[1] - 50, lb.leo[0] + 140, lb.leo[1] + 15]; log.roi['g4.same'] = [sc(X.leo_bar - 0.6, 0)[0], sc(0, 2.8)[1], sc(X.stack + 0.5, 0)[0], sc(0, 0)[1]]; }
    // S30.4 (C5): không khối chữ — loé lần lượt chồng / thanh của Leo rồi của Tessa; "high" = nhãn trên thanh của Tessa (đối xứng "bar 2.65%")
    { const [x, y] = sc(X.leo_stack, S.leo_total / G.bundle_usd * BUNDLE_TH), [, y0] = sc(X.leo_stack, 0); log.roi['g5.short'] = [x - 70, y - 20, x + 70, y0]; }
    { const [x, y] = sc(X.stack, G.stack_total / G.bundle_usd * BUNDLE_TH), [, y0] = sc(X.stack, 0); log.roi['g5.tall'] = [x - 70, y - 20, x + 70, y0]; log.roi['j0.tall'] = log.roi['g5.tall']; }
    { const [x, y] = sc(X.bar, G.bar * PER_PCT); log.roi['g5.high'] = [x - 130, y - 90, x + 130, y + 30]; log.roi['j0.high'] = [x - 90, y - 30, x + 90, y + 30];
      label(O, `bar ${D('r30_now')}`, x, y - 44, { align: 'center', kind: 'number', alpha: ok * show(t, b.g5.high, p31), char: 'Tessa', claims: ['r30_now'] }); }
    log.roi['g5.tessa'] = [sc(X.bar - 0.6, 0)[0], sc(0, 2.8)[1], sc(X.stack + 0.5, 0)[0], sc(0, 0)[1]];
    // S31 (C4 r4 + C5): ô thứ ba trống THẤY BẰNG HÌNH — đế cùng cỡ lô nhà (nền sáng nhẹ + viền nét đứt trên sàn), người viền nét đứt, chồng trống và
    // thanh trống là khối viền nét đứt (12 cạnh, không đặc); nét dày hơn khi lời gọi tên từng vật
    const [lc, lw, ld] = X.lot, poly = (P, a, lw0, fill) => { const c = O.ctx; c.save(); c.globalAlpha = a; c.beginPath(); P.forEach(([x, y], i) => (i ? c.lineTo(x, y) : c.moveTo(x, y))); c.closePath();
      if (fill) { c.fillStyle = C.ink; c.globalAlpha = a * fill; c.fill(); c.globalAlpha = a; } c.strokeStyle = C.ink; c.lineWidth = lw0; c.setLineDash([16, 10]); c.stroke(); c.restore(); };
    const wire = (x0, x1, y0, y1, z0, z1, a, lw0) => { const c = O.ctx, V = (i) => sc(i & 1 ? x1 : x0, i & 2 ? y1 : y0, i & 4 ? z1 : z0); c.save(); c.globalAlpha = a; c.strokeStyle = C.ink; c.lineWidth = lw0; c.setLineDash([10, 7]);
      c.beginPath(); for (const [i, j] of [[0, 1], [2, 3], [4, 5], [6, 7], [0, 2], [1, 3], [4, 6], [5, 7], [0, 4], [1, 5], [2, 6], [3, 7]]) { const [ax, ay] = V(i), [bx, by] = V(j); c.moveTo(ax, ay); c.lineTo(bx, by); } c.stroke(); c.restore(); };
    // người viền nét đứt (cùng cỡ Tessa: thân viên nang + đầu cầu) — "any fixed-rate borrower"
    const ghost = (x, a, lw0) => { if (a <= 0.01) return; const c = O.ctx, h = hm.h, z = hm.person.position.z, [hx, hy] = sc(x, h * 0.86, z), [, hy2] = sc(x, h * 0.86 + h * 0.13, z), r = hy - hy2;
      const [bx, bt] = sc(x, h * 0.39 + h * 0.21, z), [, bb] = sc(x, h * 0.39 - h * 0.21, z), [bx2] = sc(x + h * 0.16, 0, z), br = bx2 - bx;
      c.save(); c.globalAlpha = a; c.strokeStyle = C.ink; c.lineWidth = lw0; c.setLineDash([10, 7]); c.beginPath(); c.arc(hx, hy, r, 0, 2 * Math.PI); c.stroke();
      c.beginPath(); c.arc(bx, bt, br, Math.PI, 0); c.lineTo(bx + br, bb); c.arc(bx, bb, br, 0, Math.PI); c.closePath(); c.stroke(); c.restore(); };
    const fin = b.i0.method - 0.45;   // ba nhãn S31 (và dây dẫn) tắt hẳn trước khi thẻ V7 hiện
    const kA = 1 - cardA;   // C4 r4b: đế + khối viền ô thứ ba tắt khi thẻ V7 hiện (verify F-2: đường dưới chữ thẻ)
    if (bA * kA > 0.01) {
      const lotP = [[lc - lw / 2, -ld / 2], [lc + lw / 2, -ld / 2], [lc + lw / 2, ld / 2], [lc - lw / 2, ld / 2]].map(([x, z]) => sc(x, 0.01, z));
      poly(lotP, 0.95 * bA * kA, 4 + 3 * pulse(t, b.h0.pair, 1.0), 0.1);
      ghost(X.ghost, 0.85 * oA * kA, 3 + 2 * pulse(t, b.h0.pair, 1.0));
      wire(X.blank_stack - 0.45, X.blank_stack + 0.45, 0, hS, -0.3, 0.3, 0.95 * oA * kA, 3 + 3 * pulse(t, b.h1.stack, 1.0));
      wire(X.blank_bar - 0.5, X.blank_bar + 0.5, yB - 0.12, yB + 0.12, -0.25, 0.25, 0.95 * oA * kA, 3 + 3 * Math.max(pulse(t, b.h1.bar, 1.0), pulse(t, b.h1.paper + 1.1, 0.8)));
    }
    { const xs = [-1, 1].flatMap((u) => [-1, 1].map((v) => sc(lc + u * lw / 2, 0, v * ld / 2)[0])), [, yT] = sc(X.blank_stack, 2.1), [, yB0] = sc(lc, 0, ld / 2);
      log.roi['h0.any'] = [Math.min(...xs), yT, Math.max(...xs), yB0]; log.roi['h0.pair'] = log.roi['h0.any']; }
    // hai nhãn (cột phải) + dây dẫn đi ở lề phải ngoài chữ: thanh (lề ngoài, x 1878) vào cạnh phải thanh trống; chồng (lề trong, x 1850) qua TRÊN đỉnh thanh
    // vào đỉnh chồng trống — hai dây không cắt nhau, không cắt chữ
    const aB = ok * show(t, b.h1.bar, fin), aS = ok * show(t, b.h1.stack, fin);
    label(O, "your bar = your loan's own rate", 1810, 205, { align: 'right', kind: 'name', alpha: aB });
    label(O, 'your stack = how far apart', 1810, 268, { align: 'right', kind: 'name', alpha: aS });
    { const lead = (P, a) => { if (a <= 0.01) return; const c = O.ctx; c.save(); c.globalAlpha = 0.9 * a; c.strokeStyle = C.ink; c.lineWidth = 3; c.beginPath();
        P.forEach(([x, y], i) => (i ? c.lineTo(x, y) : c.moveTo(x, y))); c.stroke(); const [ex, ey] = P[P.length - 1]; c.fillStyle = C.ink; c.beginPath(); c.arc(ex, ey, 7, 0, 2 * Math.PI); c.fill(); c.restore(); };
      const [bx, by] = sc(X.blank_bar + 0.5, yB), [sx, sy] = sc(X.blank_stack, hS), yS = Math.min(sy - 22, sc(X.blank_bar, yB + 0.12)[1] - 30);
      lead([[1818, 191], [1878, 191], [1878, by], [bx + 6, by]], aB);
      lead([[1818, 254], [1850, 254], [1850, yS], [sx, yS], [sx, sy - 4]], aS);
      log.roi['h1.paper'] = [bx - 230, by - 30, bx + 30, sc(X.blank_bar, 0)[1]]; log.roi['h1.apart'] = [sx - 90, sc(X.blank_stack, 2.7)[1], sx + 90, sc(X.blank_stack, 0)[1]]; }
    label(O, `the ${D('term_short')} and ${D('term_long')} offers sit`, 1810, 331, { align: 'right', kind: 'number', alpha: ok * show(t, b.h1.stack, fin), claims: ['term_short', 'term_long'] });
    log.roi['h1.bar'] = [900, 150, 1810, 230]; log.roi['h1.stack'] = [800, 215, 1810, 350];
    label(O, 'a dollar in the house is hard to get back', 1810, 394, { align: 'right', kind: 'compare', alpha: ok * show(t, b.h2.hard, fin) });
    log.roi['h2.hard'] = [600, 345, 1810, 415];
    // S31.3: khoá ở cửa nhà ("hard"), lắc khi tờ đô la bị chặn ("back")
    { const [x, y] = sc(door[0], 0.42, door[2] + 0.05), a = ok * show(t, b.h2.hard, fin) * kA, j = 4 * Math.sin(40 * (t - b.h2.back)) * pulse(t, b.h2.back + 0.25, 0.5), c = O.ctx;
      if (a > 0.01) { c.save(); c.globalAlpha = a; c.strokeStyle = C.ink; c.fillStyle = C.ink; c.lineWidth = 5; c.beginPath(); c.arc(x + j, y - 14, 11, Math.PI, 0); c.stroke();
        c.fillRect(x + j - 17, y - 14, 34, 26); c.restore(); }
      log.roi['h2.back'] = [x - 60, y - 60, x + 60, y + 40]; const [hx, hy] = sc(...hand); log.roi['h2.dollar'] = [Math.min(hx, x) - 60, hy - 140, Math.max(hx, x) + 60, y + 60]; }
    { const [x, y] = sc(X.house, 1.0); log.roi['h2.house'] = [x - 200, y - 150, x + 200, y + 120]; }
    // S32 (C5): thẻ phương pháp V7 ĐỤC, tiêu đề theo lời ("What this leaves out") + 6 dòng (beats B32), giữ qua cả hai câu
    if (cardA > 0.01) {
      O.card(120, 140, 1680, 590, { fill: '#11161E', stroke: '#3A4250', lw: 3, alpha: cardA });
      label(O, 'What this leaves out', 150, 215, { kind: 'title', px: 60, alpha: cardA, plate: null });
      const L = [[`survey: ${D('n_weeks')} from ${D('first_week_short')}; strong credit, fees vary`, ['n_weeks', 'first_week_short']],
        ['principal and interest only: no taxes, insurance, PMI'], ['the bar is before taxes; no investment return tested'],
        ["the fallback's value in a job loss: not measured"],
        [`Tessa · ILLUSTRATIVE: rates of ${D('last_week_short')}, on ${D('principal')} only`, ['last_week_short', 'principal']],
        ['US only · History, not a forecast · Not advice on which loan']];
      L.forEach(([s, cl], k) => label(O, s, 150, 300 + 70 * k, { kind: cl ? 'number' : 'compare', px: 48, alpha: cardA, plate: null, claims: cl,
        color: k === L.length - 1 ? (t > b.i1.say ? C.ink : '#C9D1DC') : '#C9D1DC' }));
      log.roi['i0.method'] = [120, 140, 1800, 730]; log.roi['i1.say'] = [140, 600, 1800, 670];
    }
    { const c = O.ctx; c.save(); c.font = '600 54px Inter'; const w1 = c.measureText('US only').width, w0 = c.measureText('US only · ').width, wAll = c.measureText('US only · history, not a forecast').width; c.restore();
      seg2(O, 96, 1024, 96 + w1, 1024, C.ink, 0.9 * show(t, b.i1.only, MV.m_w33.t1), 4); seg2(O, 96 + w0, 1024, 96 + wAll, 1024, C.ink, 0.9 * show(t, b.i1.history, MV.m_w33.t1), 4);
      log.roi['i1.only'] = [90, 960, 96 + w1 + 6, 1030]; log.roi['i1.history'] = [96 + w0 - 6, 960, 96 + wAll + 6, 1030]; }
    // S33: chữ trên hai thẻ (đi theo thẻ, tắt trước khi hai chữ gặp nhau) → một thẻ; tờ $120 + giá tuần dưới chân
    for (const [card, s, cl, at, id] of [[card15, `${D('term_short')} mortgage`, ['term_short'], b.j1.fifteen, 'j1.fifteen'], [card30, `${D('term_long')} paid ${D('paid_in_short')}`, ['term_long', 'paid_in_short'], b.j1.thirty, 'j1.thirty']]) {
      const [x, y] = sc(card.position.x, card.position.y, 0.05);
      label(O, s, x, y + 16, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, at) * (1 - ease(mg, 0.2, 0.42)), claims: cl });
      log.roi[id] = [x - 300, y - 60, x + 300, y + 60];
    }
    { const [x15, y] = sc(X.cards[0], 4.0, 0.05), [x30] = sc(X.cards[1], 4.0, 0.05); log.roi['j2.knows'] = [x15 - 300, y - 60, x15 + 300, y + 60]; log.roi['j2.thirty'] = [x30 - 300, y - 60, x30 + 300, y + 60];
      log.roi['j2.fifteen'] = [x15 - 300, y - 60, x30 + 300, y + 60]; }
    { const [x, y] = sc(X.merge, 4.0, 0.05);
      label(O, `${D('term_long')} paid ${D('paid_in_short')} = ${D('term_short')} + a fallback`, x, y + 14, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.j2.plus), claims: ['term_long', 'paid_in_short', 'term_short'] });
      log.roi['j2.plus'] = [x - 620, y - 70, x + 620, y + 70]; log.roi['j2.fallback'] = [x - 620, y + 10, x + 620, sc(X.stack, 0)[1]]; }
    label(O, `week of ${D('last_week_short')}: ${D('extra_vs15_month_now')}`, 1800, 944, { align: 'right', kind: 'number', px: 48, alpha: ok * show(t, b.j2.one), claims: ['last_week_short', 'extra_vs15_month_now'] });
    { const [x, y] = sc(X.stack, G.stack_total / G.bundle_usd * BUNDLE_TH); log.roi['j2.one'] = [Math.min(x - 120, 920), y - 20, 1800, 960]; }
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
