// Tập 6 · C3 · s27-edna (B27) · Edna: hàng sáng đủ ở năm 20 (trần 10) → lùi máy: hai quãng Edna/Carl trên một trục thời gian, phần chồng tô;
// cùng mấy năm giá: hàng Edna vẫn 10 sáng, hàng Carl mờ đi.
import * as THREE from 'three';
import { setup, column, showColumn, modeLook, chrome, brace, label, kf, show, PLATE, C } from '/episodes/ep006/world/c3kit.js';
import { ease, lin, mix, rgba } from '/toolkit/factory/world/core.js';

const SEG = '/episodes/ep006/world/c3/s27-edna/';
const AX = { y0: 1949, y1: 1986, x0: 200, x1: 1720, eY: 318, cY: 400, h: 36 };   // trục thời gian (thiết kế 1920×1080), chỉ ở cBoth

export async function boot(res) {
  const poses = {
    wEdna0: { pos: [-7.4, 2.9, 9.8], tgt: [-3.1, 0.6, 0], fov: 35, chart: 0 },
    wEdna: { pos: [-6.0, 2.2, 7.8], tgt: [-3.7, 0.5, 0], fov: 35, chart: 0 },
    cEdna: { pos: [-1.665, 0.706, 25.86], tgt: [-1.665, 0.706, 0], fov: 14, chart: 1 },
    cBoth: { pos: [0, 2.27, 34.36], tgt: [0, 2.27, 0], fov: 14, chart: 1 },
  };
  const { S, CL, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  const edna = column(scene, { x: -3.6, name: 'edna' }), carl = column(scene, { x: 3.6, name: 'carl' });
  const b = cue, mode = S.moves.find((m) => m.verb === 'mode'), pull = S.moves.find((m) => m.verb === 'pull');
  const yr = (y) => AX.x0 + (AX.x1 - AX.x0) * (y - AX.y0) / (AX.y1 - AX.y0);
  const cnt = (Y, t) => Y.filter((y) => t >= y).length;
  const e0 = +CL.paths.start.edna.slice(0, 4), c0 = +CL.paths.start.carl.slice(0, 4);

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    const eA = ease(t, b.c0.edna - 0.05, b.c0.edna + 0.8), cA = ease(t, b.c3.carl - 0.05, b.c3.carl + 0.8);
    const vE = kf(S.rows.edna, t), vC = kf(S.rows.carl, t);
    edna.row.set({ value: vE, appear: eA, pulse: show(t, b.c4.end) * (1 - show(t, b.c4.end + 1.2)) }); showColumn(edna, eA);
    carl.row.set({ value: vC, appear: cA }); showColumn(carl, cA);
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0, u = ease(t, pull.t0, pull.t1); log.roi = {};
    for (const [col, nm, a] of [[edna, 'Edna', eA], [carl, 'Carl', cA]]) {
      const [x, y] = O.toScreen(col.person.position.x, col.h + 0.12, col.person.position.z);
      label(O, cw < 0.95 ? `${nm} · ILLUSTRATIVE` : nm, x, y - 24, { align: 'center', kind: 'name', px: 48, w: 600, alpha: a * (cw < 0.95 ? 1 - cw : u) });
    }
    // cEdna: nhãn ngày + kept up (cột trái); cBoth: nhãn ngày đi lên đầu thanh của Edna
    const mA = ok * show(t, mode.t1);
    label(O, `Edna · ILLUSTRATIVE · ${CL.kept_up_last_start_20y.display}`, mix(120, AX.x0, u), mix(385, AX.eY - 28, u), { kind: 'number', px: 48, w: 600, alpha: mA });
    label(O, 'kept up: the last start month that did', 120, 228, { kind: 'compare', px: 48, alpha: ok * show(t, b.c0.kept, pull.t0 - 0.3) });
    const r = edna.row, top = r.userData.height;
    const [x0, yt] = O.toScreen(r.edgeX(0), top, 0.4), [x1, yb] = O.toScreen(r.edgeX(10), 0, 0.4);
    const kE = Math.max(cnt(S.years.edna, t), t >= S.years.edna_rep[0] ? 17 + cnt(S.years.edna_rep, t) : 0);
    const kA = ok * (kE >= 1 ? 1 : 0) * (1 - show(t, pull.t0 - 0.3)) + ok * show(t, b.c4.end);
    if (kE >= 1) label(O, `year ${kE}`, x1, yt - 30, { align: 'right', kind: 'number', px: 52, alpha: kA });
    const fA = ok * show(t, S.years.edna[19] + 0.2, pull.t0 - 0.3), gA = ok * show(t, b.c4.end);
    brace(O, x0, x1, yb + 22, C.ink, Math.max(fA, gA), 5, -14);
    label(O, 'year 20: all 10 still lit', x0, yb + 86, { kind: 'number', px: 48, alpha: fA });
    label(O, 'all 10 crates still lit', x0, yb + 80, { kind: 'number', px: 48, alpha: gA });
    log.roi['c1.twenty'] = [x0 - 10, yt - 90, x1 + 10, yb + 110];
    // trục thời gian (cBoth): thanh Edna ("Her"), thanh Carl ("Carl's"), phần chồng ("same")
    const bA = ok * u, eW = lin(t, b.c3.her, b.c3.her + 0.8), cWd = lin(t, b.c3.carl, b.c3.carl + 0.8), sA = ok * show(t, b.c4.same);
    if (bA > 0.01) {
      const c = O.ctx; c.save();
      if (sA > 0.01) { c.globalAlpha = sA; c.fillStyle = rgba(C.muted, 0.5); c.fillRect(yr(c0), AX.eY - 12, yr(e0 + 20) - yr(c0), AX.cY + AX.h - AX.eY + 24); }
      c.globalAlpha = bA; c.fillStyle = C.ink;
      if (eW > 0) c.fillRect(yr(e0), AX.eY, (yr(e0 + 20) - yr(e0)) * eW, AX.h);
      if (cWd > 0) c.fillRect(yr(c0), AX.cY, (yr(c0 + 20) - yr(c0)) * cWd, AX.h);
      c.restore();
      O.shape({ role: 'bar', box: [yr(e0), AX.eY, yr(e0 + 20), AX.eY + AX.h], char: 'edna', opacity: bA * (eW > 0 ? 1 : 0) });
      O.shape({ role: 'bar', box: [yr(c0), AX.cY, yr(c0 + 20), AX.cY + AX.h], char: 'carl', opacity: bA * (cWd > 0 ? 1 : 0) });
    }
    label(O, `Carl · ILLUSTRATIVE · from ${CL.worst_window_start_year_20y.display}`, AX.x1, AX.cY + AX.h + 56, { align: 'right', kind: 'number', px: 48, w: 600, alpha: ok * show(t, b.c3.carl) });
    label(O, 'same years of prices: her last, his first', (yr(c0) + yr(e0 + 20)) / 2, 205, { align: 'center', kind: 'compare', px: 48, alpha: sA });
    log.roi['c3.her'] = [AX.x0 - 10, AX.eY - 70, AX.x1 + 10, AX.cY + AX.h + 70]; log.roi['c4.same'] = log.roi['c3.her'];
    // hàng của Carl: bộ đếm năm 1 → 3 ở "start"
    const kC = cnt(S.years.carl, t);
    if (kC >= 1) { const [xc, yc] = O.toScreen(carl.row.edgeX(10), top, 0.4); label(O, `year ${kC}`, xc, yc - 30, { align: 'right', kind: 'number', px: 52, alpha: ok }); }
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
