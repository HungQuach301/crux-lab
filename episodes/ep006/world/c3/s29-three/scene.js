// Tập 6 · C3 · s29-three (B29) · ba người, ba hàng: cùng khoản tăng 2 %, năm 20: 10 · about 9 · about 4; khác nhau = tháng bắt đầu.
import * as THREE from 'three';
import { setup, column, showColumn, modeLook, chrome, label, kf, show, C } from '/episodes/ep006/world/c3kit.js';
import { mix } from '/toolkit/factory/world/core.js';

const SEG = '/episodes/ep006/world/c3/s29-three/';
const SZ = { size: 0.48, gap: 0.07 };

export async function boot(res) {
  const poses = {
    wThree0: { pos: [-1.6, 3.6, 15.0], tgt: [0, 0.9, 0], fov: 48, chart: 0 },
    wThree: { pos: [-1.0, 2.4, 12.2], tgt: [0, 0.8, 0], fov: 50, chart: 0 },
    cThree: { pos: [0, 2.74, 46.3], tgt: [0, 2.74, 0], fov: 14, chart: 1 },
  };
  const { S, CL, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  const cols = [['edna', 'Edna', -6.0, CL.kept_up_last_start_20y.display, '10', 'full'],
    ['ruth', 'Ruth', 0, CL.guide_start.display, 'about 9', 'nine'],
    ['carl', 'Carl', 6.0, CL.worst_window_start_year_20y.display, 'about 4', 'four']]
    .map(([id, nm, x, start, val, ck]) => ({ ...column(scene, { x, name: id, ...SZ }), id, nm, start, val, ck }));
  const b = cue, mode = S.moves.find((m) => m.verb === 'mode');

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    for (const c of cols) {
      const pulse = c.id === 'edna' ? show(t, b.d0.edna) * (1 - show(t, b.d0.edna + 0.6)) : 0;
      c.row.set({ value: kf(S.rows[c.id], t), pulse }); showColumn(c, 1);
    }
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    const mA = ok * show(t, mode.t1), hA = show(t, b.d2.month);
    label(O, `crates at year 20 · same ${CL.two_pct_growth_20y_pct.display} raise`, 960, 236, { align: 'center', kind: 'compare', px: 52, alpha: ok * show(t, b.d1.crates) });
    for (const c of cols) {
      const [hx, hy] = O.toScreen(c.person.position.x, c.h + 0.12, c.person.position.z), [xl] = O.toScreen(c.row.edgeX(0), 0, 0.4);
      // đồ thị: tên + tháng bắt đầu ở mép trái hàng
      label(O, c.nm, hx, hy - 24, { align: 'center', kind: 'name', px: 48, w: 600, alpha: 1 - cw });   // thế giới: tên ngắn (huy hiệu ILLUSTRATIVE cố định)
      label(O, `${c.nm} · ILLUSTRATIVE`, xl, 550, { kind: 'name', px: 48, w: 600, alpha: mA });
      label(O, `${c.start}`, xl, 610, { kind: 'number', px: 48, w: 600, color: hA > 0.5 ? C.ink : C.muted, alpha: mA, emph: hA > 0.5 });
      label(O, c.val, xl, 462, { kind: 'number', px: 72, alpha: ok * show(t, b.d1[c.ck]) });
      const [x0, yt] = O.toScreen(c.row.edgeX(0), c.row.userData.height, 0.4), [x1, yb] = O.toScreen(c.row.edgeX(10), 0, 0.4);
      log.roi[`d1.${c.ck}`] = [x0 - 10, 390, x1 + 10, yb + 10];
    }
    log.roi['d2.month'] = [96, 560, 1824, 630];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
