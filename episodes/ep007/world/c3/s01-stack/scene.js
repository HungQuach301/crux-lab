// Tập 7 · C3 · s01-stack (B01, KEY-1) · Tessa cạnh nhà; the stack hiện cạnh nhà và thêm một bó mỗi nhịp → đồ thị: "$120 a month" trên chồng,
// "$320,000 loan · week of Oct 8, 2026" trên nhà.
import { setup, home, nameTag, theStack, stackSet, modeLook, chrome, label, kf, show } from '/episodes/ep007/world/c3kit.js';

const SEG = '/episodes/ep007/world/c3/s01-stack/';

export async function boot(res) {
  const poses = {
    wS0: { pos: [-3.6, 2.7, 8.6], tgt: [0.3, 0.7, 0], fov: 35, chart: 0 },
    wS: { pos: [-2.5, 2.0, 6.6], tgt: [0.3, 0.75, 0], fov: 35, chart: 0 },
    cS: { pos: [0.1, 1.2, 18], tgt: [0.1, 1.2, 0], fov: 15, chart: 1 },
  };
  const { S, CL, D, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  const hm = home(scene, { x: -0.3 }), stack = theStack(scene, CL._geom, { x: 1.45 });
  const b = cue;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    const h = stackSet(stack, kf(S.stack, t));
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    nameTag(O, hm);
    const [sx, sy] = O.toScreen(stack.position.x, Math.max(h, 0.2) + 0.12, 0), [sx0, sy0] = O.toScreen(stack.position.x - 0.5, 0, 0), [sx1] = O.toScreen(stack.position.x + 0.5, 0, 0);
    log.roi['a0.costs'] = log.roi['a0.month'] = [sx0 - 10, sy - 200, sx1 + 10, sy0 + 10];
    label(O, D('extra_vs15_month_now'), sx, sy - 20, { align: 'center', kind: 'number', px: 64, alpha: ok * show(t, b.a1.three), claims: ['extra_vs15_month_now'] });
    log.roi['a1.three'] = [sx - 220, sy - 90, sx + 220, sy + 10];
    const [hx, hy] = O.toScreen(hm.house.position.x, 2.35, 0);
    label(O, `${D('principal')} loan · week of ${D('last_week_short')}`, hx + 60, hy, { align: 'center', kind: 'number', alpha: ok * show(t, b.a1.payment) });
    log.roi['a1.payment'] = [hx - 500, hy - 60, hx + 620, hy + 20];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
