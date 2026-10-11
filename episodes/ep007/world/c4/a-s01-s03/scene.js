// Tập 7 · C4 · ĐOẠN A = S01–S03 + ident. Tessa cạnh nhà; 4 bó lần lượt ra cửa nhà bay vào the stack sát tường nhà (mọc theo nhịp S01.1, dừng
// trước S01.2), tấm giấy vay (vật riêng, trước mặt tiền) → đồ thị: "price of the fallback: $120 a month" (5,94 s), "$320,000 loan · week of Oct 8, 2026" trên tấm giấy vay → hai thẻ khoản vay (V4 adapted) → lùi
// máy: dải 1.833 tuần (V1 xem trước) mọc thành cột giá → hai thẻ có lãi tuần 8/10/2026 → thế giới, dòng góc gạch chân, đối trọng; ident tối dần.
import { setup, figure, gesture, figTag, LoanTag, OfferCard, WeekStrip, nameTag, theStack, stackSet, BUNDLE_TH, modeLook, followLight, chrome, label, seg2, dip,
  kf, show, pulse, C, ease, lin, THREE } from '/episodes/ep007/world/c4kit.js';
import { Bill, TRACK } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c4/a-s01-s03/';
const FLY_W = 0.9 * 0.85, FLY_D = 0.6;   // bó bay = cỡ bó trong chồng

export async function boot(res) {
  const poses = {
    wS0: { pos: [-3.6, 2.7, 8.6], tgt: [0.3, 0.7, 0], fov: 35, chart: 0 },
    wS: { pos: [-2.5, 2.0, 6.6], tgt: [0.3, 0.75, 0], fov: 35, chart: 0 },
    cS: { pos: [0.3, 1.45, 21], tgt: [0.3, 1.45, 0], fov: 15, chart: 1 },
    cStrip: { pos: [-1.5, 1.7, 29], tgt: [-1.5, 1.2, -3.2], fov: 18, chart: 1 },
    cCards: { pos: [0, 1.9, 16], tgt: [0, 1.9, 0], fov: 18, chart: 1 },
    wEnd: { pos: [-3.4, 2.5, 9.2], tgt: [0.2, 1.3, 0], fov: 38, chart: 0 },
  };
  const { S, D, G, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue;
  const hm = figure(scene, { x: -0.3 }), stack = theStack(scene, G, { x: S.stack_x, z: S.stack_z }), tag = LoanTag(scene, hm);
  // C4 r3: chồng sát tường phải → tấm giấy vay dời sang trước mặt tiền (phải cửa), không đứng trước chồng; vẫn là vật của nhà
  tag.position.x = hm.house.position.x + hm.w * 0.34;
  const cardA = OfferCard(scene, { x: S.cards[0], y: 2.6, w: 3.0, h: 0.8 }), cardB = OfferCard(scene, { x: S.cards[1], y: 2.6, w: 3.0, h: 0.8 });
  const strip = WeekStrip(scene, S.weeks_extra, { x0: -9, width: 15, z: -3.2 });
  // tờ đô la trả thêm (S02.2 "each extra dollar"): ở đầu cánh tay của Tessa, mặt hướng máy
  const bill = Bill({ name: 'extra-dollar' }); bill.rotation.x = Math.PI / 2; bill.scale.setScalar(0.6); bill.position.y = -hm.h * 0.24; hm.pivot.children[0].add(bill);
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
  // thẻ: hiện ở từ khoá, mờ khi lùi máy ra dải tuần (dải nằm sau thẻ), về lại khi đẩy máy về thẻ; về thế giới (S03.2) thẻ THU ĐI cùng lúc chữ
  // tắt (tên thẻ có chữ số → chỉ ở đồ thị) — vòng bố cục 1: không còn hai hộp tối rỗng 45–53 s
  const wOut = (t) => 1 - ease(t, MV.m_w.t0, MV.m_w.t0 + 0.3);
  const cardsA = (t) => (1 - ease(t, MV.m_pull.t0, MV.m_pull.t0 + 0.5) + ease(t, MV.m_push.t0 + 0.3, MV.m_push.t1)) * wOut(t);

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
    const cA = cardsA(t);
    cardA.set({ a: show(t, b.a2.fifteen) * Math.min(1, cA) }); cardB.set({ a: show(t, b.a2.thirty) * Math.min(1, cA), band: ease(t, b.a2.kept - 0.05, b.a2.kept + 0.6) });
    const sA = 1 - ease(t, MV.m_push.t0, MV.m_push.t0 + 0.6);
    strip.set({ grow: lin(t, b.a3.every, b.a3.every + 1.2), rise: ease(t, b.a3.price - 0.35, b.a3.price + 1.05), lastA: ease(t, b.a3.price + 1.0, b.a3.price + 1.6), a: sA });
    bill.visible = t > b.a3.extra - 0.1 && t < b.a3.extra + 2.9;
    bill.scale.setScalar(0.6 * Math.min(ease(t, b.a3.extra - 0.1, b.a3.extra + 0.2), 1 - ease(t, b.a3.extra + 2.5, b.a3.extra + 2.9)) + 0.001);
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 0.62 * ease(t, S.ident[0], S.ident[0] + 1.4));   // ident: thế giới tối dần (vẽ TRƯỚC mọi chữ)
    const nb = figTag(O, hm);
    if (nb) { const ip = pulse(t, b.a4.illustrative, 1.4); seg2(O, nb[0], nb[3] + 14, nb[2], nb[3] + 14, C.warn, ip, 5); log.roi['a4.illustrative'] = [nb[0] - 10, nb[1] - 20, nb[2] + 10, nb[3] + 24]; }
    const [dx, dy] = O.toScreen(...door); log.roi['a0.costs'] = [dx - 90, dy - 70, dx + 90, dy + 50];
    const [tx, ty] = O.toScreen(...tag.top()); log.roi['a1.borrowing'] = [tx - 70, ty - 20, tx + 70, ty + 130];
    // S01: nhãn giá (hai dòng) hiện cùng lúc bó đầu chạm (5,94 s); nhãn khoản vay ("dollars"). Nhãn S01 tắt khi thẻ khoản vay đầu hiện (S02.1).
    // Vòng bố cục 1 (đạo diễn: giá đọc thành giá của khoản vay vì nằm ngay dưới nhãn khoản vay, cùng cột với tấm giấy vay): mỗi nhãn neo VẬT của
    // nó bằng dây dẫn và đứng ở hai phía khác nhau — giá: khối trên-phải CHỒNG, dây xuống đỉnh chồng; khoản vay: dòng trên-trái, dây xuống tấm giấy
    // vay; hai khối cách nhau ≥ 80 px theo chiều đứng
    const cS1 = b.a2.fifteen - 0.35, [sx, sy] = O.toScreen(stack.position.x, Math.max(h, 0.17) + 0.12, 0);
    const pa = ok * show(t, S.land, cS1), px = Math.min(sx + 200, 1500);   // r3: lệch phải thêm — dây của nhãn khoản vay (x tấm giấy) không cắt khối giá
    label(O, 'price of the fallback:', px, sy - 200, { align: 'center', kind: 'number', alpha: pa });
    label(O, D('extra_vs15_month_now'), px, sy - 135, { align: 'center', kind: 'number', px: 60, alpha: pa, claims: ['extra_vs15_month_now'] });
    seg2(O, sx, sy - 110, sx, sy + 14, C.warn, 0.85 * pa, 3);
    log.roi['a1.land'] = [px - 320, sy - 250, px + 320, sy + 20];
    // C4 r3: tấm giấy vay giờ ở trước mặt tiền, gần chồng hơn → nhãn khoản vay lên cao hơn (trên mái), cách khối giá ≥ 80 px theo chiều đứng
    const la = ok * show(t, b.a1.dollars, cS1), lx = Math.max(560, tx - 260), ly = ty - 330;
    label(O, `${D('principal')} loan · week of ${D('last_week_short')}`, lx, ly, { align: 'center', kind: 'number', alpha: la, claims: ['principal', 'last_week_short'] });
    seg2(O, tx, ly + 20, tx, ty - 8, C.muted, 0.85 * la, 3);
    log.roi['a1.dollars'] = [lx - 480, ly - 50, lx + 480, ty];
    // S02.1 / S03.1: chữ trên hai thẻ (tên khoản vay; lãi của tuần ở dòng hai)
    for (const [card, title, cl, rate, rc, at, rt] of [[cardA, `${D('term_short')} mortgage`, ['term_short'], D('r15_now'), 'r15_now', b.a2.fifteen, b.a4.six],
      [cardB, `${D('term_long')} paid ${D('paid_in_short')}`, ['term_long', 'paid_in_short'], D('r30_now'), 'r30_now', b.a2.thirty, b.a4.seven]]) {
      const [cx, cy] = O.toScreen(card.position.x, card.position.y, 0.05), vis = ok * show(t, at) * Math.min(1, cA);
      const two = show(t, rt);
      label(O, title, cx, cy - 4 - 22 * two, { align: 'center', kind: 'number', px: 48, alpha: vis, claims: cl });
      label(O, rate, cx, cy + 46, { align: 'center', kind: 'number', px: 56, alpha: vis * two, claims: [rc] });
      log.roi[at === b.a2.fifteen ? 'a2.fifteen' : 'a2.thirty'] = [cx - 300, cy - 80, cx + 300, cy + 80];
      log.roi[at === b.a2.fifteen ? 'a4.six' : 'a4.seven'] = [cx - 200, cy + 10, cx + 200, cy + 70];
    }
    { const [bx, by] = O.toScreen(cardB.position.x, cardB.position.y - 0.33, 0.05); log.roi['a2.kept'] = [bx - 300, by - 20, bx + 300, by + 20]; }
    { const [wx, wy] = O.toScreen(0, 3.3, 0.05);
      label(O, `week of ${D('last_week_short')}`, wx, wy, { align: 'center', kind: 'number', alpha: ok * show(t, b.a4.october, MV.m_w.t0) * (t > MV.m_push.t1 ? 1 : 0), claims: ['last_week_short'] });
      log.roi['a4.october'] = [wx - 300, wy - 50, wx + 300, wy + 15]; }
    // S02.2: dải tuần
    { const [ax, ay] = O.toScreen(strip.xOf(0), 0, strip.z), [zx, zy] = O.toScreen(strip.xOf(strip.n - 1), 0, strip.z), [, ty2] = O.toScreen(-1.5, 3.25, strip.z);
      label(O, `every week since ${D('first_week_short')}`, (ax + zx) / 2, ty2, { align: 'center', kind: 'number', alpha: ok * show(t, b.a3.surveys, MV.m_push.t0 - 0.1) * (t > MV.m_pull.t1 ? 1 : 0), claims: ['first_week_short'] });
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
