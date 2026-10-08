// Tập 6 · C3 · s29-three (B29) · ba người, ba hàng: cùng khoản tăng 2 %, năm 20: 10 · about 9 · about 4; khác nhau = tháng bắt đầu.
// FIX-R2: ba tấm séc cùng lớn lên ở "Same raise" tới cùng cỡ năm 20 (×1,486) cạnh ba hàng 10 · ≈ 9 · ≈ 4.
// FIX-R3: ba cột xếp theo thời gian (Edna 1949 · Carl 1966 · Ruth 2006); ở đồ thị một trục tháng bắt đầu tỉ lệ năm, mỗi cột nối xuống mốc
// của mình; một ngoặc chung nối đỉnh ba séc (cùng cỡ) + "same check: +2% a year". Ba cột cùng màu, cùng cỡ (không nhấn riêng Carl).
import * as THREE from 'three';
import { setup, column, showColumn, setCheck, modeLook, chrome, label, kf, show, C } from '/episodes/ep006/world/c3kit.js';
import { checkScale } from '/episodes/ep006/world/obj6.js';
import { mix, rgba } from '/toolkit/factory/world/core.js';

const SEG = '/episodes/ep006/world/c3/s29-three/';
const SZ = { size: 0.4, gap: 0.05, cw: 0.62, cbase: 1.0, h: 1.6 };   // FIX-R3: séc to hơn (năm 20 ≈ 140 px ở đồ thị), hàng hẹp hơn
const AX = { y0: 1945, y1: 2030, x0: 200, x1: 1720, y: 806, lab: 872 };   // trục tháng bắt đầu (thiết kế 1920×1080), chỉ ở đồ thị
const BR = { y: 402, lab: 372 };                                             // ngoặc chung trên đỉnh ba séc

export async function boot(res) {
  const poses = {
    wThree0: { pos: [-1.4, 3.8, 15.6], tgt: [-0.2, 0.9, 0], fov: 50, chart: 0 },
    wThree: { pos: [-0.9, 2.6, 12.8], tgt: [-0.2, 0.8, 0], fov: 52, chart: 0 },
    cThree: { pos: [-0.25, 1.15, 46.8], tgt: [-0.25, 1.15, 0], fov: 14, chart: 1 },
  };
  const { S, CL, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  // thứ tự trái → phải = thứ tự tháng bắt đầu (FIX-R3)
  const cols = [['edna', 'Edna', -5.7, CL.kept_up_last_start_20y.display, '10', 'full'],
    ['carl', 'Carl', 0.6, CL.worst_window_start_year_20y.display, 'about 4', 'four'],
    ['ruth', 'Ruth', 6.9, CL.guide_start.display, 'about 9', 'nine']]
    .map(([id, nm, x, start, val, ck]) => ({ ...column(scene, { x, name: id, ...SZ }), id, nm, start, val, ck }));
  const b = cue, mode = S.moves.find((m) => m.verb === 'mode');
  const ym = (s) => { const [y, m] = s.split('-').map(Number); return y + (m - 1) / 12; };
  const ax = (y) => AX.x0 + (AX.x1 - AX.x0) * (y - AX.y0) / (AX.y1 - AX.y0);

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    for (const c of cols) {
      const pulse = c.id === 'edna' ? show(t, b.d0.edna) * (1 - show(t, b.d0.edna + 0.6)) : 0;
      c.row.set({ value: kf(S.rows[c.id], t), pulse }); showColumn(c, 1); setCheck(c, S, t);
    }
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    const mA = ok * show(t, mode.t1), hA = show(t, b.d2.month), ctx = O.ctx;
    label(O, 'crates at year 20', 960, 236, { align: 'center', kind: 'compare', px: 52, alpha: ok * show(t, b.d1.crates) });
    // ngoặc chung: một vạch ngang trên ba séc, chân thả xuống đúng đỉnh mỗi séc (cùng cỡ năm 20) + nhãn sự thật
    const tops = cols.map((c) => O.toScreen(c.card.position.x, c.cbase * checkScale(20), c.z));
    if (mA > 0.01) {
      ctx.save(); ctx.globalAlpha = mA; ctx.strokeStyle = C.ink; ctx.lineWidth = 4; ctx.beginPath();
      ctx.moveTo(tops[0][0], BR.y); ctx.lineTo(tops[2][0], BR.y);
      for (const [x, y] of tops) { ctx.moveTo(x, BR.y); ctx.lineTo(x, y - 8); }
      ctx.stroke(); ctx.restore();
      O.shape({ role: 'line', box: [tops[0][0], BR.y, tops[2][0], tops[0][1] - 8], opacity: mA, key: 'same-check' });
    }
    label(O, `same check: +${CL.two_pct_growth_20y_pct.display} a year`, (tops[0][0] + tops[2][0]) / 2, BR.lab, { align: 'center', kind: 'number', px: 48, alpha: mA });
    log.roi['same.check'] = [tops[0][0] - 40, BR.lab - 50, tops[2][0] + 40, tops[0][1] + 150];
    // trục tháng bắt đầu: tỉ lệ năm; sáng lên ở "month" (S29.3)
    const axC = hA > 0.5 ? C.ink : C.muted;
    if (mA > 0.01) {
      ctx.save(); ctx.globalAlpha = mA; ctx.strokeStyle = axC; ctx.lineWidth = mix(3, 5, hA); ctx.beginPath(); ctx.moveTo(AX.x0, AX.y); ctx.lineTo(AX.x1, AX.y); ctx.stroke(); ctx.restore();
      O.shape({ role: 'line', box: [AX.x0, AX.y - 2, AX.x1, AX.y + 2], opacity: mA, key: 'start-axis' });
    }
    label(O, 'start month', AX.x1 + 80, AX.lab, { align: 'right', kind: 'name', px: 48, w: 600, color: axC, alpha: mA, emph: hA > 0.5 });
    for (const c of cols) {
      const [hx, hy] = O.toScreen(c.person.position.x, c.h + 0.12, c.person.position.z), [xl] = O.toScreen(c.row.edgeX(0), 0, 0.4);
      const [xr, yb] = O.toScreen(c.row.edgeX(10), 0, 0.4), cx = (O.toScreen(c.person.position.x, 0, 0)[0] + xr) / 2, tx = ax(ym(CL.paths.start[c.id]));
      label(O, c.nm, hx, hy - 24, { align: 'center', kind: 'name', px: 48, w: 600, alpha: 1 - cw });   // thế giới: tên ngắn (huy hiệu ILLUSTRATIVE cố định)
      label(O, `${c.nm} · ILLUSTRATIVE`, cx, 728, { align: 'center', kind: 'name', px: 48, w: 600, alpha: mA });
      label(O, c.val, xl, tops[0][1] - 4, { kind: 'number', px: 72, alpha: ok * show(t, b.d1[c.ck]) });
      // nối cột → mốc trên trục; mốc + tháng bắt đầu
      if (mA > 0.01) {
        ctx.save(); ctx.globalAlpha = mA; ctx.strokeStyle = rgba(axC, mix(0.55, 1, hA)); ctx.fillStyle = axC; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(cx, 748); ctx.lineTo(tx, AX.y - 12); ctx.stroke();
        ctx.beginPath(); ctx.arc(tx, AX.y, mix(8, 11, hA), 0, Math.PI * 2); ctx.fill(); ctx.restore();
        O.shape({ role: 'mark', box: [tx - 11, AX.y - 11, tx + 11, AX.y + 11], char: c.id, opacity: mA, key: 'start-' + c.id });
      }
      label(O, c.start, tx, AX.lab, { align: 'center', kind: 'number', px: 48, w: 600, color: axC, alpha: mA, emph: hA > 0.5 });
      log.roi[`d1.${c.ck}`] = [xl - 10, tops[0][1] - 70, xr + 10, yb + 10];
    }
    log.roi['d2.month'] = [AX.x0 - 40, AX.y - 30, 1824, AX.lab + 20];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
