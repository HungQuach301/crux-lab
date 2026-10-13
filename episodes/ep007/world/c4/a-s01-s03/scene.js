// Tập 7 · C4 · ĐOẠN A = S01–S03 + ident. Tessa cạnh nhà; 4 bó lần lượt ra cửa nhà bay vào the stack sát tường nhà (mọc theo nhịp S01.1, dừng
// trước S01.2), tấm giấy vay (vật riêng, trước mặt tiền) → đẩy vào đồ thị: "price of the fallback: $120 a month" (5,94 s), "$320,000 loan · week of
// Oct 8, 2026" ngay trên tấm giấy vay; xấp khoản trả nhà mọc cao hơn hai xấp hoá đơn nhỏ ("biggest bill") → hai thẻ khoản vay (V4 adapted) có chồng
// khoản trả + đống dự phòng → giữ thẻ tới "replayed", lùi máy: dải 1.833 tuần (V1 xem trước) mọc trên mặt phẳng riêng sau/trên nhà, thành cột giá →
// đẩy vào tay Tessa: tờ đô la bay vào nhà → hai thẻ có lãi tuần 8/10/2026 → thế giới (thẻ ở lại, mờ), dòng góc gạch chân, đối trọng, máy đẩy vào; ident.
import { setup, figure, gesture, figTag, LoanTag, OfferCard, WeekStrip, nameTag, theStack, stackSet, BUNDLE_TH, modeLook, followLight, chrome, label, seg2, dip,
  kf, show, pulse, C, ease, lin, mix, setOpacity, PALETTE, THREE } from '/episodes/ep007/world/c4kit.js';
import { Bill, TRACK } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c4/a-s01-s03/';
const FLY_W = 0.9 * 0.85, FLY_D = 0.6;   // bó bay = cỡ bó trong chồng
const CARD_Y = 2.35, CARD_W = 2.6, CARD_H = 1.1;   // thẻ cao hơn bản C4: chỗ cho chồng khoản trả (S02) dưới tên, dòng lãi (S03) trên dải cushion
const STRIP_Y = 2.15, STRIP_UNIT = 1.9 / 30000;    // C5 r1: dải tuần trên mặt phẳng riêng, đáy cao hơn đỉnh mái → không đè nhà

export async function boot(res) {
  const poses = {
    wS0: { pos: [-3.6, 2.7, 8.6], tgt: [0.3, 0.7, 0], fov: 35, chart: 0 },
    wS: { pos: [-2.5, 2.0, 6.6], tgt: [0.3, 0.75, 0], fov: 35, chart: 0 },
    cS: { pos: [0.2, 1.45, 21], tgt: [0.2, 1.45, 0], fov: 11, chart: 1 },        // C5 r1: chặt hơn wS → cú chuyển ở "$320,000" là đẩy vào
    cStrip: { pos: [-1.5, 1.9, 29], tgt: [-1.5, 1.6, -3.2], fov: 18, chart: 1 },
    cHand: { pos: [-0.9, 1.25, 8.5], tgt: [-0.9, 0.95, 0], fov: 22, chart: 1 },  // tay Tessa + cửa nhà (tờ đô la trả thêm)
    cCards: { pos: [0, 1.9, 16], tgt: [0, 1.9, 0], fov: 18, chart: 1 },
    wEnd: { pos: [-3.4, 2.5, 9.2], tgt: [0.2, 1.3, 0], fov: 38, chart: 0 },
    wIn: { pos: [-2.4, 2.1, 7.4], tgt: [0.0, 1.5, 0], fov: 36, chart: 0 },
  };
  const { S, D, G, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue, AT = S.at;
  const hm = figure(scene, { x: -0.3 }), stack = theStack(scene, G, { x: S.stack_x, z: S.stack_z }), tag = LoanTag(scene, hm);
  // C4 r3: chồng sát tường phải → tấm giấy vay dời sang trước mặt tiền (phải cửa), không đứng trước chồng; vẫn là vật của nhà
  tag.position.x = hm.house.position.x + hm.w * 0.34;
  const cardA = OfferCard(scene, { x: S.cards[0], y: CARD_Y, w: CARD_W, h: CARD_H }), cardB = OfferCard(scene, { x: S.cards[1], y: CARD_Y, w: CARD_W, h: CARD_H });
  // S02.1: trong thẻ, chồng khoản trả tháng (màu tiền) — 15 năm cao, 30 năm thấp; đống dự phòng (cushion) cạnh chồng 30 năm = phần trả thêm bỏ được
  // trong tháng khó (pay30on15 − pay30). Thang riêng của thẻ (chồng cao nhất 0,5); con của nhóm thẻ → mờ / to cùng thẻ
  const PS = 0.5 / G.pay30on15, money = (c, e = 0) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.75, transparent: true, emissive: new THREE.Color(c), emissiveIntensity: e });
  const inCard = (card, x, usd, c, name) => { const g = new THREE.BoxGeometry(0.5, 1, 0.12); g.translate(0, 0.5, 0); const m = new THREE.Mesh(g, money(c, 0.1));
    m.position.set(x, -CARD_H / 2 + 0.13, 0.09); m.userData.h = usd * PS; m.userData.checks = { role: 'mark', key: `card-${name}` }; card.add(m); return m; };
  const p15 = inCard(cardA, 0, G.pay15, PALETTE.bill, 'pay15'), p30 = inCard(cardB, -0.42, G.pay30, PALETTE.bill, 'pay30'), cush = inCard(cardB, 0.38, G.pay30on15 - G.pay30, C.cushion, 'cushion');
  const strip = WeekStrip(scene, S.weeks_extra, { x0: -9, width: 15, z: -3.2, unit: STRIP_UNIT });
  strip.mesh.position.y = STRIP_Y;
  // mặt phẳng riêng của dải + trục thời gian (ink-muted) ở mép trước
  const shelf = new THREE.Mesh(new THREE.BoxGeometry(15.3, 0.06, 0.75), new THREE.MeshStandardMaterial({ color: '#232A35', roughness: 0.7, transparent: true }));
  shelf.position.set(-1.5, STRIP_Y - 0.03, -3.2); shelf.receiveShadow = true; scene.add(shelf);
  const axis = new THREE.Mesh(new THREE.BoxGeometry(15.3, 0.035, 0.03), new THREE.MeshStandardMaterial({ color: C.muted, emissive: new THREE.Color(C.muted), emissiveIntensity: 0.5, transparent: true }));
  axis.position.set(-1.5, STRIP_Y - 0.03, -3.2 + 0.39); scene.add(axis); axis.userData.checks = { role: 'mark', key: 'strip-axis' };
  const yc = new THREE.Color();
  // tờ đô la trả thêm (S02.2 "each extra dollar"): ở đầu cánh tay của Tessa, mặt hướng máy; "principal" một tờ bay vào cửa nhà
  const bill = Bill({ name: 'extra-dollar' }); bill.rotation.x = Math.PI / 2; bill.scale.setScalar(0.6); bill.position.y = -hm.h * 0.24; hm.pivot.children[0].add(bill);
  const flyBill = Bill({ name: 'extra-dollar-fly' }); flyBill.visible = false; scene.add(flyBill);
  const P0 = new THREE.Vector3(); gesture(hm, AT['S02.2:principal'] - 0.02, S.gestures); hm.person.updateMatrixWorld(true); bill.getWorldPosition(P0);
  const P1 = new THREE.Vector3(hm.house.position.x, 0.3, hm.house.position.z + hm.w * 0.36 + 0.05);
  // S01.2 "biggest bill": hai xấp hoá đơn nhỏ + xấp khoản trả nhà mọc cao (tờ đô la xếp có khe, bên trái Tessa)
  const pile = (x, n) => { const g = new THREE.Group(); g.position.set(x, 0, 0.2); scene.add(g);
    for (let k = 0; k < n; k++) { const s = Bill({ name: 'bill-pile' }); s.scale.setScalar(0.6); s.position.y = 0.012 + k * 0.045; g.add(s); }
    g.userData.checks = { role: 'mark', key: `bills-${x}` }; return g; };
  const pays = pile(S.bills_x[0], 24), small = [pile(S.bills_x[1], 4), pile(S.bills_x[2], 3)];
  // bó bay: hộp warn + đai (như bó trong chồng) — một bó cho mỗi lần chạm (S.lands)
  const flies = S.lands.map(() => {
    const f = new THREE.Group();
    f.add(new THREE.Mesh(new THREE.BoxGeometry(FLY_W, BUNDLE_TH * 0.92, FLY_D), new THREE.MeshStandardMaterial({ color: TRACK.warn, roughness: 0.8 })),
      new THREE.Mesh(new THREE.BoxGeometry(FLY_W * 0.16, BUNDLE_TH * 0.94, FLY_D * 1.02), new THREE.MeshStandardMaterial({ color: '#E9E2CF', roughness: 0.8 })));
    f.children[0].castShadow = true; scene.add(f); return f; });
  const door = [hm.house.position.x, BUNDLE_TH / 2 + 0.02, 0.58 + FLY_D / 2 + 0.05];   // bậc cửa (lib3d House: cửa giữa mặt trước)
  const path = (p, k) => {   // bậc cửa → chỗ của bó k trong chồng, vòng ra trước rồi hạ xuống
    const e = p * p * (3 - 2 * p), y1 = k * BUNDLE_TH + BUNDLE_TH / 2;
    return [door[0] + (stack.position.x - door[0]) * e, door[1] + (y1 - door[1]) * e + 0.55 * Math.sin(Math.PI * p), door[2] + (stack.position.z - door[2]) * e + 0.35 * Math.sin(Math.PI * p)];
  };
  // thẻ: hiện ở từ khoá; GIỮ tới "replayed" (C5 r1: không còn khung trống trước dải), về lại khi đẩy máy về thẻ; về thế giới (S03.2) thẻ ở lại MỜ,
  // không chữ (tên thẻ có chữ số → chỉ ở đồ thị), tắt cùng ident
  const cardsA = (t) => Math.min(1, 1 - ease(t, MV.m_pull.t0 + 1.1, MV.m_pull.t0 + 1.5) + ease(t, MV.m_push.t0 + 0.3, MV.m_push.t1))
    * (1 - 0.6 * ease(t, MV.m_w.t0, MV.m_w.t0 + 0.4)) * (1 - ease(t, S.ident[0], S.ident[0] + 0.8));
  const g0 = MV.m_pull.t0 + 1.0;   // dải mọc theo cú lùi máy (thẻ đang tắt)

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw); gesture(hm, t, S.gestures);
    const h = stackSet(stack, kf(S.stack, t));
    // bó k: trồi ra ở bậc cửa POP_OUT s, bay FLY s, chạm chồng đúng S.lands[k] (chồng nhận bó cùng lúc); sau chạm không còn vật nào ở cửa
    S.lands.forEach((tl, k) => {
      const f = flies[k], t0f = tl - S.fly, born = ease(t, t0f - S.pop_out, t0f);
      f.visible = born > 0.01 && t < tl;
      if (f.visible) { const [x, y, z] = path(Math.min(1, Math.max(0, (t - t0f) / S.fly)), k); f.position.set(x, y, z - (1 - born) * 0.3); f.scale.setScalar(0.25 + 0.75 * born); }
    });
    tag.set(show(t, b.a1.borrowing));
    // S01.2: hoá đơn nhỏ ở "city"; xấp khoản trả mọc từng tờ "payment" → "biggest"; tắt khi thẻ khoản vay hiện
    const cS1 = b.a2.fifteen - 0.35, pa0 = show(t, AT['S01.2:city'], cS1), np = 24 * lin(t, AT['S01.2:payment'], AT['S01.2:biggest'] + 0.2);
    for (const g of small) setOpacity(g, pa0);
    setOpacity(pays, show(t, AT['S01.2:payment'] - 0.1, cS1)); pays.children.forEach((s, k) => { s.visible = s.visible && k < np; });
    const cA = cardsA(t);
    cardA.set({ a: show(t, b.a2.fifteen) * cA }); cardB.set({ a: show(t, b.a2.thirty) * cA, band: ease(t, b.a2.kept - 0.05, b.a2.kept + 0.6) });
    // chồng trong thẻ: chỉ ở S02 (S03 thẻ mang lãi)
    const sOn = t < MV.m_push.t0;
    for (const [m, at] of [[p15, b.a2.fifteen], [p30, b.a2.thirty], [cush, b.a2.kept]]) {
      const g = ease(t, at - 0.05, at + 0.6); m.scale.y = Math.max(0.001, m.userData.h * g); m.visible = m.visible && sOn && g > 0.01; }
    cush.material.emissiveIntensity = 0.1 + 0.9 * pulse(t, AT['S02.1:bad'], 1.0);
    const sA = (1 - 0.65 * ease(t, MV.m_hand.t0, MV.m_hand.t1)) * (1 - ease(t, MV.m_push.t0, MV.m_push.t0 + 0.6));
    strip.set({ grow: lin(t, g0, b.a3.every + 1.0), rise: ease(t, b.a3.price - 0.35, b.a3.price + 1.05), lastA: ease(t, b.a3.price + 1.0, b.a3.price + 1.6), a: sA });
    // năm lẻ đậm hơn → từng năm (từng nhóm ô tuần) tách ra, không đọc thành sóng liền
    for (let i = 0; i < strip.n; i++) if (S.weeks_year[i] % 2) { strip.mesh.getColorAt(i, yc); strip.mesh.setColorAt(i, yc.multiplyScalar(0.7)); }
    strip.mesh.instanceColor.needsUpdate = true;
    const shA = ease(t, g0 - 0.3, g0 + 0.3) * sA; setOpacity(shelf, shA); setOpacity(axis, shA);
    // tờ đô la: trong tay từ "extra" tới "principal", rồi bay vào cửa nhà (0,6 s)
    const tp = AT['S02.2:principal'];
    bill.visible = t > b.a3.extra - 0.1 && t < tp;
    bill.scale.setScalar(0.6 * ease(t, b.a3.extra - 0.1, b.a3.extra + 0.2) + 0.001);
    { const p = (t - tp) / 0.6; flyBill.visible = p > 0 && p < 1;
      if (flyBill.visible) { const e = p * p * (3 - 2 * p); flyBill.position.lerpVectors(P0, P1, e); flyBill.position.y += 0.35 * Math.sin(Math.PI * p);
        flyBill.rotation.set(Math.PI / 2 * (1 - p), 2.4 * p, 0); flyBill.scale.setScalar(0.6 * (1 - 0.6 * p)); } }
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 0.62 * ease(t, S.ident[0], S.ident[0] + 1.4));   // ident: thế giới tối dần (vẽ TRƯỚC mọi chữ)
    const nb = figTag(O, hm);
    if (nb) { const ip = pulse(t, b.a4.illustrative, 1.4); seg2(O, nb[0], nb[3] + 14, nb[2], nb[3] + 14, C.warn, ip, 5); log.roi['a4.illustrative'] = [nb[0] - 10, nb[1] - 20, nb[2] + 10, nb[3] + 24]; }
    const [dx, dy] = O.toScreen(...door); log.roi['a0.costs'] = [dx - 90, dy - 70, dx + 90, dy + 50];
    const [tx, ty] = O.toScreen(...tag.top()); log.roi['a1.borrowing'] = [tx - 70, ty - 20, tx + 70, ty + 130];
    // S01: nhãn giá (hai dòng) hiện cùng lúc bó đầu chạm (5,94 s); nhãn khoản vay ("dollars") NGAY TRÊN tấm giấy vay (C5 r1). Hai khối cách nhau
    // ≥ 80 px theo chiều đứng: giá ở trên-phải chồng (dây xuống đỉnh chồng), khoản vay sát tấm giấy. Nhãn S01 tắt khi thẻ khoản vay đầu hiện (S02.1).
    const [sx, sy] = O.toScreen(stack.position.x, Math.max(h, 0.17) + 0.12, 0);
    const pa = ok * show(t, S.land, cS1), px = Math.min(sx + 200, 1500);
    label(O, 'price of the fallback:', px, sy - 300, { align: 'center', kind: 'number', alpha: pa });
    label(O, D('extra_vs15_month_now'), px, sy - 235, { align: 'center', kind: 'number', px: 60, alpha: pa, claims: ['extra_vs15_month_now'] });
    seg2(O, sx, sy - 205, sx, sy + 14, C.warn, 0.85 * pa, 3);
    log.roi['a1.land'] = [px - 320, sy - 350, px + 320, sy + 20];
    const la = ok * show(t, b.a1.dollars, cS1), lx = Math.max(560, tx), ly = ty - 52;
    label(O, `${D('principal')} loan · week of ${D('last_week_short')}`, lx, ly, { align: 'center', kind: 'number', alpha: la, claims: ['principal', 'last_week_short'] });
    log.roi['a1.dollars'] = [lx - 480, ly - 50, lx + 480, ty];
    // S02.1 / S03.1: chữ trên hai thẻ — tên ở dải trên; lãi của tuần (S03) ở giữa, TRÊN dải cushion. S03: thẻ 30 năm mang lãi 30 năm thường → "30-year mortgage"
    const s03 = t >= MV.m_push.t0;
    for (const [card, title, cl, rate, rc, at, rt] of [[cardA, `${D('term_short')} mortgage`, ['term_short'], D('r15_now'), 'r15_now', b.a2.fifteen, b.a4.six],
      [cardB, s03 ? `${D('term_long')} mortgage` : `${D('term_long')} paid ${D('paid_in_short')}`, s03 ? ['term_long'] : ['term_long', 'paid_in_short'], D('r30_now'), 'r30_now', b.a2.thirty, b.a4.seven]]) {
      const [cx, cy] = O.toScreen(card.position.x, card.position.y, 0.05), [, ny] = O.toScreen(card.position.x, card.position.y + 0.3, 0.05), [, ry] = O.toScreen(card.position.x, card.position.y - 0.06, 0.05);
      const vis = ok * show(t, at) * Math.min(1, cA) * (s03 ? 1 : 1 - ease(t, MV.m_pull.t0 + 0.2, MV.m_pull.t0 + 0.5));   // chữ tắt trước khi thẻ nhỏ lại (không chồng)
      label(O, title, cx, ny, { align: 'center', kind: 'number', px: 48, alpha: vis, claims: cl });
      label(O, rate, cx, ry, { align: 'center', kind: 'number', px: 56, alpha: vis * show(t, rt), claims: [rc] });
      log.roi[at === b.a2.fifteen ? 'a2.fifteen' : 'a2.thirty'] = [cx - 300, cy - 80, cx + 300, cy + 80];
      log.roi[at === b.a2.fifteen ? 'a4.six' : 'a4.seven'] = [cx - 200, ry - 35, cx + 200, ry + 35];
    }
    { const [bx, by] = O.toScreen(cardB.position.x, cardB.position.y - CARD_H / 2 + 0.07, 0.05); log.roi['a2.kept'] = [bx - 300, by - 120, bx + 300, by + 20]; }
    { const [wx, wy] = O.toScreen(0, 3.3, 0.05);
      label(O, `week of ${D('last_week_short')}`, wx, wy, { align: 'center', kind: 'number', alpha: ok * show(t, b.a4.october, MV.m_w.t0) * (t > MV.m_push.t1 ? 1 : 0), claims: ['last_week_short'] });
      log.roi['a4.october'] = [wx - 300, wy - 50, wx + 300, wy + 15]; }
    // S02.2: dải tuần — nhãn trên dải, hai đầu trục dưới mặt phẳng
    { const [ax, ay] = O.toScreen(strip.xOf(0), STRIP_Y, strip.z), [zx, zy] = O.toScreen(strip.xOf(strip.n - 1), STRIP_Y, strip.z), [, ty2] = O.toScreen(-1.5, STRIP_Y + 2.45, strip.z);
      const after = t > MV.m_pull.t1 ? 1 : 0, sEnd = MV.m_hand.t0 - 0.1;
      label(O, `every week since ${D('first_week_short')}`, (ax + zx) / 2, ty2, { align: 'center', kind: 'number', alpha: ok * show(t, b.a3.surveys, sEnd) * after, claims: ['first_week_short'] });
      const [, yb] = O.toScreen(0, STRIP_Y - 0.05, strip.z + 0.4), aA = ok * show(t, b.a3.every, sEnd) * after;
      label(O, D('first_week_short'), ax, yb + 40, { align: 'left', kind: 'number', px: 48, color: C.muted, alpha: aA, claims: ['first_week_short'] });
      label(O, D('last_week_short'), zx, yb + 40, { align: 'right', kind: 'number', px: 48, color: C.muted, alpha: aA, claims: ['last_week_short'] });
      log.roi['a3.every'] = [ax, ty2 + 20, zx, ay]; log.roi['a3.surveys'] = [(ax + zx) / 2 - 420, ty2 - 50, (ax + zx) / 2 + 420, ty2 + 15]; log.roi['a3.price'] = [ax, ty2 + 20, zx, zy]; }
    { const [hx, hy] = O.toScreen(hm.person.position.x + 0.4, hm.h, hm.person.position.z); log.roi['a3.extra'] = [hx - 80, hy - 80, hx + 80, hy + 40]; }
    // S03.2: dòng góc gạch chân ở "only", "history" (nét dưới hộp chữ, không cắt chữ)
    { const c = O.ctx; c.save(); c.font = '600 54px Inter'; const w1 = c.measureText('US only').width, w0 = c.measureText('US only · ').width, wAll = c.measureText('US only · history, not a forecast').width; c.restore();
      seg2(O, 96, 1024, 96 + w1, 1024, C.ink, 0.9 * show(t, b.a5.only, b.a6.say), 4); seg2(O, 96 + w0, 1024, 96 + wAll, 1024, C.ink, 0.9 * show(t, b.a5.history, b.a6.say), 4);
      log.roi['a5.only'] = [90, 960, 96 + w1 + 6, 1030]; log.roi['a5.history'] = [96 + w0 - 6, 960, 96 + wAll + 6, 1030]; }
    const cwA = show(t, b.a6.say);
    chrome(O, { cw: cwA > 0.01 ? S.label_cues['a6.say'] : null, cwA });
    log.roi['a6.say'] = [96, 880, 1500, 960];
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
