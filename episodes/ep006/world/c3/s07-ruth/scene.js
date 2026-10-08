// Tập 6 · C3 · s07-ruth (B07) · hàng 10 thùng của Ruth: 10 sáng → "less" mờ tới 0,904 → đồ thị: ngoặc 10 chỗ + "about 9 in 10 (90.4%)".
import * as THREE from 'three';
import { setup, column, showColumn, modeLook, chrome, brace, label, kf, show, C } from '/episodes/ep006/world/c3kit.js';

const SEG = '/episodes/ep006/world/c3/s07-ruth/';

export async function boot(res) {
  const poses = {
    wRuth0: { pos: [-3.6, 2.9, 9.8], tgt: [0.5, 0.6, 0], fov: 35, chart: 0 },
    wRuth: { pos: [-2.4, 2.2, 7.8], tgt: [-0.1, 0.5, 0], fov: 35, chart: 0 },
    cRuth: { pos: [0, 0.5, 21.99], tgt: [0, 0.5, 0], fov: 14, chart: 1 },
  };
  const { S, CL, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  const ruth = column(scene, { x: 0, name: 'ruth' });
  const mv = S.moves.find((m) => m.verb === 'mode'), b = cue;
  const pct = CL.guide_real_2pct_end_pct.display;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    const v = kf(S.rows.ruth, t);
    ruth.row.set({ value: v, appear: 1, pulse: show(t, b.a1.nine) * (1 - show(t, b.a1.nine + 0.6)) });
    showColumn(ruth, 1);
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    const [hx, hy] = O.toScreen(ruth.person.position.x, ruth.h + 0.12, ruth.person.position.z);
    label(O, 'Ruth · ILLUSTRATIVE', hx, hy - 24, { align: 'center', kind: 'name', px: 48, w: 600 });
    const r = ruth.row, top = r.userData.height;
    // ngoặc + nhãn DƯỚI hàng (đồ thị): ink-muted = cả 10 chỗ khoản đầu mua; ink = phần còn sáng hôm nay
    const [x0, yt] = O.toScreen(r.edgeX(0), top, 0.4), [x1, yb] = O.toScreen(r.edgeX(10), 0, 0.4), [xl] = O.toScreen(r.edgeX(10 * v), 0, 0.4);
    log.roi['a0.less'] = [x0 - 10, yt - 10, x1 + 10, yb + 10];
    const tA = ok * show(t, b.a1.ten), nA = ok * show(t, b.a1.nine);
    brace(O, x0, x1, yb + 22, C.muted, tA, 5, -14);
    label(O, 'first check: 10 crates', (x0 + x1) / 2, yb + 86, { align: 'center', kind: 'number', alpha: tA, color: C.muted });
    brace(O, x0, xl, yb + 132, C.ink, nA, 5, -14);
    label(O, `today: about 9 in 10 crates (${pct})`, (x0 + xl) / 2, yb + 196, { align: 'center', kind: 'number', alpha: nA });
    log.roi['a1.ten'] = [x0 - 10, yb, x1 + 10, yb + 110]; log.roi['a1.nine'] = [x0 - 10, yb + 110, x1 + 10, yb + 220];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
