// Tập 6 · C4 · ĐOẠN A = S01–S03 + ident. Ruth + séc + hàng 10 thùng (W10) → đồ thị: +2% a year, 10 thùng + "?" → dải lịch 20 năm → chồng dải
// lùi về 1947 → lia sang đồ thị V3 (đường của Ruth so với séc đầu) → về thế giới, đối trọng; ident: tối dần. Mốc giờ chỉ từ spine.json.
import * as THREE from 'three';
import { Ribbon } from '/toolkit/factory/world/lib3d.js';
import { setup, column, showColumn, setCheck, checkLabel, nameTag, rowBox, modeLook, followLight, chrome, brace, label, dip, kf, show, pulse,
  CHAR, C, ease, lin, mix, rgba } from '/episodes/ep006/world/c4kit.js';

const SEG = '/episodes/ep006/world/c4/a-s01-s03/';
const XL = 12, KX = 0.32, VY = (v) => (v - 0.85) * 12;           // đồ thị V3 trong thế giới: năm k → x, sức mua (phần) → y

export async function boot(res) {
  const poses = {
    wRuth0: { pos: [-4.2, 2.9, 9.8], tgt: [-0.1, 0.6, 0], fov: 35, chart: 0 },
    wRuth: { pos: [-3.0, 2.2, 7.8], tgt: [-0.7, 0.5, 0], fov: 35, chart: 0 },
    cRuth: { pos: [-0.8, 0.95, 24], tgt: [-0.8, 0.95, 0], fov: 14, chart: 1 },
    cLine: { pos: [XL + 3.0, 1.25, 19.5], tgt: [XL + 3.0, 1.25, 0], fov: 14, chart: 1 },
    wRuth2: { pos: [-2.6, 2.0, 8.6], tgt: [-0.6, 0.7, 0], fov: 35, chart: 0 },
  };
  const { S, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const ruth = column(scene, { x: 0, name: 'ruth' });
  const b = cue, P = S.ruth_path;
  // V3: vạch séc đầu (cố định, ink-muted) + đường của Ruth (ink; dưới vạch = warn)
  const base = new THREE.Mesh(new THREE.BoxGeometry(20 * KX + 0.4, 0.035, 0.04), new THREE.MeshStandardMaterial({ color: C.muted, emissive: new THREE.Color(C.muted), emissiveIntensity: 0.5, transparent: true }));
  base.position.set(XL + 10 * KX, VY(1), 0.4); scene.add(base);
  const line = Ribbon({ color: C.ink, z: 0.45, width: 0.07 }); scene.add(line);

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    const v = kf(S.rows.ruth, t);
    ruth.row.set({ value: v, pulse: pulse(t, b.a1.keep, 0.8) }); showColumn(ruth, 1); setCheck(ruth, S, t);
    const u = lin(t, S.line_draw[0], S.line_draw[1]) * 20, n = Math.floor(u);
    const pts = []; for (let k = 0; k <= n; k++) pts.push([XL + k * KX, VY(P[k]), P[k] < 1 ? C.warn : C.ink]);
    if (n < 20 && u > 0) pts.push([XL + u * KX, VY(mix(P[n], P[n + 1], u - n)), C.ink]);
    const lA = t >= MV.m_pan.t0 && t < MV.m_w.t1 ? 1 : 0;
    if (pts.length > 1) line.set(pts, 0.07); line.visible = lA > 0 && pts.length > 1; base.visible = lA > 0;
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    nameTag(O, ruth, 1 - cw);
    const R = rowBox(O, ruth, v), offS02 = MV.m_pan.t0 - 0.3;
    // S01.2: séc +2% a year; ngoặc 10 thùng + "?" (câu hỏi của bà)
    checkLabel(O, ruth, 'check: +2% a year', ok * show(t, b.a1.two, b.a2.twentieth - 0.4), { dx: 14 });
    const kA = ok * show(t, b.a1.keep, b.a2.twentieth - 0.4);
    brace(O, R.x0, R.x1, R.yb + 22, C.muted, kA, 5, -14);
    label(O, 'first check: 10 crates', (R.x0 + R.x1) / 2, R.yb + 86, { align: 'center', kind: 'number', px: 48, color: C.muted, alpha: kA });
    label(O, '?', R.x1 + 60, R.yt + 10, { kind: 'title', px: 96, alpha: kA, plate: null });
    log.roi['a1.two'] = [R.x0 - 200, R.yt - 200, R.x0, R.yb]; log.roi['a1.keep'] = [R.x0 - 10, R.yb, R.x1 + 10, R.yb + 110];
    // S02.1: dải lịch 20 ô dưới hàng (Aug 2006 → Aug 2026); S02.2: dải nhân lên, lùi về 1947
    const cA = ok * show(t, b.a2.twentieth, offS02), fill = lin(t, b.a2.twentieth, b.a2.august);
    if (cA > 0.01) {
      const c = O.ctx, w = (R.x1 - R.x0) / 20, y = R.yb + 40; c.save(); c.globalAlpha = cA;
      for (let k = 0; k < 20; k++) { c.fillStyle = k < fill * 20 ? CHAR.ruth : rgba(C.muted, 0.35); c.fillRect(R.x0 + k * w + 2, y, w - 4, 26); }
      c.restore();
      const sA = ok * show(t, b.a3.every, offS02), nS = Math.round(lin(t, b.a3.every, b.a3.nineteen + 0.4) * 14);
      if (sA > 0.01) {
        c.save();
        for (let j = 1; j <= nS; j++) { c.globalAlpha = sA * (0.55 - j * 0.03); c.fillStyle = C.muted; c.fillRect(R.x0 - j * 34, y - j * 34, R.x1 - R.x0, 18); }
        c.restore();
      }
      label(O, `${S.label_cues['a2.august']}`, (R.x0 + R.x1) / 2, y + 100, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.a2.august, offS02) });
      label(O, S.label_cues['a3.nineteen'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.a3.nineteen, offS02) });
      log.roi['a2.twentieth'] = [R.x0 - 10, y - 10, R.x1 + 10, y + 120]; log.roi['a3.every'] = [R.x0 - 500, y - 500, R.x1 + 10, y + 30];
    }
    // S03.1–S03.2: đồ thị V3 — vạch "first check" + định nghĩa; đường của Ruth tới năm 20, điểm cuối dưới vạch
    if (lA > 0) {
      const [bx0, by] = O.toScreen(XL - 0.2, VY(1), 0.4), [bx1] = O.toScreen(XL + 20 * KX + 0.2, VY(1), 0.4);
      label(O, 'first check', bx1, by - 26, { align: 'right', kind: 'name', px: 48, w: 600, color: C.muted, alpha: ok });
      label(O, S.label_cues['a4.keeping'], 960, 236, { align: 'center', kind: 'compare', px: 52, alpha: ok * show(t, b.a4.keeping, MV.m_w.t0 - 0.2) });
      const [ex, ey] = O.toScreen(XL + Math.min(u, 20) * KX, VY(P[Math.min(20, Math.ceil(u))]), 0.45);
      const eA = ok * show(t, b.a5.short, MV.m_w.t0 - 0.2);
      if (eA > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = eA; c.fillStyle = C.warn; c.beginPath(); c.arc(ex, ey, 12, 0, 7); c.fill(); c.restore(); }
      label(O, 'Ruth · ILLUSTRATIVE', ex, ey + 80, { align: 'right', kind: 'name', px: 48, w: 600, color: CHAR.ruth, alpha: ok * show(t, b.a5.ruth, MV.m_w.t0 - 0.2) });
      log.roi['a4.keeping'] = [400, 160, 1520, 260]; log.roi['a5.short'] = [ex - 30, ey - 30, ex + 30, ey + 30];
    }
    const cwA = show(t, b.a7.choose);
    chrome(O, 1, cwA > 0.01 ? S.label_cues['a7.choose'] : null, cwA);
    log.roi['a7.choose'] = [96, 860, 1500, 960];
    // ident: thế giới tối dần (nhạc hiệu A do music.post phát ở 3 s cuối đuôi S03)
    dip(O, ease(t, S.ident[0], S.ident[0] + 1.4));
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
