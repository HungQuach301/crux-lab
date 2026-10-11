// Tập 7 · C3 · s06-stack (B06, KEY-3) · thanh 30 năm nâng lên mức trả xong trong 15 năm, vượt thanh 15 năm; phần dôi (warn) thành bó tiền rơi
// lên the stack 15 lần tới đủ chiều cao → đồ thị: "$2,948 a month", "+$120 a month", "the stack: $21,622 over 15 years".
import { setup, home, nameTag, theStack, stackSet, BUNDLE_TH, modeLook, chrome, label, kf, show, C, THREE } from '/episodes/ep007/world/c3kit.js';
import { PayBar, TRACK } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c3/s06-stack/';
const SCALE = 1 / 1230;   // USD/tháng → chiều cao thế giới (thanh khoản trả); chồng dùng thang bó riêng (BUNDLE_TH mỗi năm)

export async function boot(res) {
  const poses = {
    wS: { pos: [-4.4, 2.7, 8.4], tgt: [-0.6, 1.1, 0], fov: 38, chart: 0 },
    cS: { pos: [-0.3, 1.5, 20], tgt: [-0.3, 1.5, 0], fov: 19, chart: 1 },
  };
  const { S, CL, D, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  const G = CL._geom, b = cue;
  const hm = home(scene, { x: -2.8 }), stack = theStack(scene, G, { x: -1.1 });
  const bar15 = PayBar({ scale: SCALE, name: '15-year' }), bar30 = PayBar({ scale: SCALE, name: '30-year' });
  bar15.position.set(0.55, 0, 0); bar30.position.set(2.0, 0, 0); scene.add(bar15, bar30);
  // bó đang bay (phần dôi rời khỏi thanh 30 năm, theo cung, chạm đỉnh chồng)
  const fly = new THREE.Mesh(new THREE.BoxGeometry(0.9, BUNDLE_TH * 0.92, 0.6), new THREE.MeshStandardMaterial({ color: TRACK.warn, roughness: 0.8, emissive: new THREE.Color(TRACK.warn), emissiveIntensity: 0.25 }));
  fly.castShadow = true; scene.add(fly);
  const sliver = (G.pay30on15 - G.pay15) * SCALE;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    bar15.set({ usd: G.pay15 });
    const u30 = kf(S.bar30, t); bar30.set({ usd: u30, warnAbove: G.pay15, topA: Math.min(1, Math.max(0, (u30 - G.pay15) / (G.pay30on15 - G.pay15))) });
    stackSet(stack, kf(S.stack, t));
    // bó bay: k = bó đang trên đường (rời thanh drop_dur s trước khi chạm)
    fly.visible = false;
    for (let k = 0; k < S.drops.length; k++) {
      const t1 = S.drops[k], t0 = t1 - S.drop_dur; if (t < t0 || t >= t1) continue;
      const x = (t - t0) / S.drop_dur, ys = bar30.topY(G.pay30on15) - sliver / 2, ye = k * BUNDLE_TH + BUNDLE_TH / 2;
      fly.position.set(bar30.position.x + (stack.position.x - bar30.position.x) * x, ys + (ye - ys) * x + 1.1 * Math.sin(Math.PI * x), 0);
      fly.scale.set(0.85, (sliver / BUNDLE_TH) * (1 - x) + x, 1); fly.visible = true;
    }
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    nameTag(O, hm);
    const top15 = bar15.topY(G.pay15), top30 = bar30.topY(u30);
    // tên thanh dưới chân (không đè nhãn số phía trên); nhãn số: trên cặp thanh (căn phải), "+$120" ngay phải phần warn, nhãn chồng cao hơn
    const [x15, f15] = O.toScreen(bar15.position.x, 0, 0.3), [x30, f30] = O.toScreen(bar30.position.x, 0, 0.3), [, y30] = O.toScreen(bar30.position.x, bar30.topY(G.pay30on15), 0);
    label(O, '15-year', x15, f15 + 52, { align: 'center', kind: 'name', px: 48, w: 600 });
    label(O, '30-year', x30, f30 + 52, { align: 'center', kind: 'name', px: 48, w: 600 });
    label(O, `30-year paid in 15: ${D('pay30on15_now')}`, 1800, y30 - 80, { align: 'right', kind: 'number', alpha: ok * show(t, b.a0.forty), claims: ['pay30on15_now'] });
    const [xs, ys] = O.toScreen(bar30.position.x + 0.42, top15 + sliver / 2, 0);
    label(O, `+${D('extra_vs15_month_now')}`, xs + 26, ys + 18, { kind: 'number', px: 56, alpha: ok * show(t, b.a1.one), claims: ['extra_vs15_month_now'] });
    const [kx, ky] = O.toScreen(stack.position.x, 15 * BUNDLE_TH, 0);
    label(O, `the stack: ${D('extra_vs15_total_now')} over 15 years`, kx, Math.min(ky, y30) - 150, { align: 'center', kind: 'number', alpha: ok * show(t, b.a2.twenty), claims: ['extra_vs15_total_now'] });
    const [bx0, by0] = O.toScreen(bar30.position.x - 0.5, top30 + 0.3, 0), [bx1, by1] = O.toScreen(bar30.position.x + 0.5, 0, 0);
    log.roi['a0.finishing'] = [bx0, by0, bx1, by1];
    log.roi['a0.forty'] = [900, y30 - 135, 1810, y30 - 55];
    log.roi['a1.one'] = [xs, ys - 50, xs + 420, ys + 40];
    const [sx0, sy0] = O.toScreen(stack.position.x - 0.5, 15 * BUNDLE_TH + 0.2, 0), [sx1, sy1] = O.toScreen(bar30.position.x + 0.5, 0, 0);
    log.roi['a1.same'] = [sx0, sy0, sx1, sy1];
    log.roi['a2.twenty'] = [kx - 460, Math.min(ky, y30) - 205, kx + 460, Math.min(ky, y30) - 135];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
