// Tập 6 · C3 · s24-carl (B24) · Ruth → Carl; đồ thị: bộ đếm kỷ niệm 1 → 20, hàng của Carl mờ dần mỗi năm tới ≈ 4,3; ô nhỏ đường của Ruth.
// FIX-R2: tấm séc của Carl lớn lên ×1,02 mỗi kỷ niệm (cùng nhịp hàng mờ), séc Ruth ở cỡ năm 20; "check" = "check: +2% a year" trên séc.
import * as THREE from 'three';
import { setup, column, showColumn, setCheck, checkLabel, checkBox, modeLook, chrome, brace, label, kf, show, C } from '/episodes/ep006/world/c3kit.js';
import { ease, lin } from '/toolkit/factory/world/core.js';

const SEG = '/episodes/ep006/world/c3/s24-carl/';
const INSET = { x0: 1420, x1: 1800, y0: 220, y1: 400, v0: 0.88, v1: 1.06 };   // ô nhỏ (thiết kế 1920×1080) góc trên phải (FIX-R2: nhường chỗ séc): năm 0 → 20, sức mua 88 % → 106 %

export async function boot(res) {
  const poses = {
    wRuth: { pos: [-15.4, 2.2, 7.8], tgt: [-13.1, 0.5, 0], fov: 35, chart: 0 },
    wCarl: { pos: [-3.4, 2.2, 7.8], tgt: [-1.1, 0.5, 0], fov: 35, chart: 0 },
    cCarl: { pos: [0.85, 1.06, 25.86], tgt: [0.85, 1.06, 0], fov: 14, chart: 1 },
  };
  const { S, CL, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  const ruth = column(scene, { x: -12, name: 'ruth' }), carl = column(scene, { x: 0, name: 'carl' });
  const b = cue, Y = S.years.carl;
  const yearAt = (t) => Y.filter((y) => t >= y).length;
  const ix = (k) => INSET.x0 + (INSET.x1 - INSET.x0) * k / 20, iy = (v) => INSET.y1 - (INSET.y1 - INSET.y0) * (v - INSET.v0) / (INSET.v1 - INSET.v0);

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    ruth.row.set({ value: kf(S.rows.ruth, t), pulse: show(t, b.b0.ruth) * (1 - show(t, b.b0.ruth + 0.5)) });
    const cA = ease(t, b.b1.carl - 0.05, b.b1.carl + 0.8), vC = kf(S.rows.carl, t);
    carl.row.set({ value: vC, appear: cA, pulse: show(t, b.b5.never) * (1 - show(t, b.b5.never + 0.6)) }); showColumn(carl, cA);
    setCheck(ruth, S, t); setCheck(carl, S, t, cA);
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    { const [x, y] = O.toScreen(ruth.person.position.x, ruth.h + 0.12, ruth.person.position.z); label(O, 'Ruth · ILLUSTRATIVE', x, y - 24, { align: 'center', kind: 'name', px: 48, w: 600, alpha: 1 - cw }); }
    { const [x, y] = O.toScreen(carl.person.position.x, carl.h + 0.12, carl.person.position.z); label(O, 'Carl · ILLUSTRATIVE', x, y - 24, { align: 'center', kind: 'name', px: 48, w: 600, alpha: cA * (1 - cw) }); }
    const r = carl.row, top = r.userData.height, k = yearAt(t);
    const [x0, yt] = O.toScreen(r.edgeX(0), top, 0.4), [x1, yb] = O.toScreen(r.edgeX(10), 0, 0.4), [xl] = O.toScreen(r.edgeX(10 * vC), 0, 0.4);
    // nhãn đồ thị (số chỉ khi chartW ≥ 0,95): ngày, giá, 20 of 20 — cột trái; ngoặc + nhãn dưới hàng
    const mA = ok * show(t, S.moves[1].t1);
    label(O, `Carl · ILLUSTRATIVE · ${CL.worst_window_start_year_20y.display}`, 120, 385, { kind: 'number', px: 48, w: 600, alpha: mA });
    label(O, `prices: ${CL.raise_needed_all_20y_pct.display}, the fastest stretch`, 120, 228, { kind: 'number', px: 48, alpha: ok * show(t, b.b2.fastest) });
    label(O, `less buying power on ${CL.worst_window_years_2pct_fell_20y.display} anniversaries`, 120, 306, { kind: 'compare', px: 48, alpha: ok * show(t, b.b4.before) });
    checkLabel(O, carl, CL, ok * show(t, b.b3.check), { dx: 14 }); log.roi['b3.check'] = checkBox(O, carl);
    const tA = ok * show(t, b.b3.first);
    brace(O, x0, x1, yb + 22, C.muted, tA, 5, -14);
    label(O, 'first check: 10 crates', x0, yb + 86, { kind: 'number', px: 48, alpha: tA, color: C.muted });
    if (k >= 1) label(O, `year ${k}`, x1, yt - 30, { align: 'right', kind: 'number', px: 52, alpha: ok });
    const eA = ok * show(t, Y[19] + 0.25);
    brace(O, x0, xl, yb + 132, C.ink, eA, 5, -14);
    label(O, `year 20: about 4 of 10 crates (${CL.worst_real_value_2pct_payment_after_20y_pct.display})`, x0, yb + 196, { kind: 'number', px: 48, alpha: eA });
    log.roi['b4.every'] = [x0 - 10, yt - 80, x1 + 10, yb + 10]; log.roi['b3.first'] = [x0 - 10, yb, x1 + 10, yb + 110];
    // ô nhỏ: vạch khoản đầu (ink-muted, cố định) + đường của Ruth (ink) vẽ trái → phải từ "Ruth's"
    const iA = ok * show(t, b.b5.ruths), d = lin(t, b.b5.ruths, b.b5.ruths + 1.2);
    if (iA > 0.01) {
      const c = O.ctx; c.save(); c.globalAlpha = iA; c.lineCap = 'round';
      c.strokeStyle = C.muted; c.lineWidth = 4; c.beginPath(); c.moveTo(ix(0), iy(1)); c.lineTo(ix(20), iy(1)); c.stroke();
      c.strokeStyle = C.ink; c.lineWidth = 6; c.beginPath(); const P = S.ruth_path, n = Math.max(1, Math.round(d * 20));
      c.moveTo(ix(0), iy(P[0])); for (let j = 1; j <= n; j++) c.lineTo(ix(j), iy(P[j])); c.stroke(); c.restore();
      label(O, 'first check', INSET.x0, iy(1) + 80, { align: 'left', kind: 'name', px: 48, w: 600, color: C.muted, alpha: iA });
      label(O, 'Ruth · ILLUSTRATIVE:', INSET.x1, 470, { align: 'right', kind: 'name', px: 48, w: 600, alpha: iA });
      label(O, 'back above in early years', INSET.x1, 530, { align: 'right', kind: 'compare', px: 48, alpha: iA });
      log.roi['b5.ruths'] = [INSET.x0 - 300, INSET.y0 - 20, INSET.x1 + 10, 545];
    }
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
