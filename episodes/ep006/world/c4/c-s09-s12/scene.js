// Tập 6 · C4 · ĐOẠN C = S09–S12 (+ MR1). Đồ thị V3 trong thế giới: đường sức mua của Ruth theo kỷ niệm (Ribbon), vạch "first check" cố định,
// chấm mỗi năm (cushion / warn), hàng 10 thùng nhỏ theo đầu đường; ĐỈNH S10.2 = đoạn 15 → 16 rơi qua vạch; S12: lùi máy + giãn trục, đường séc đều.
// Mốc giờ chỉ từ spine.json.
import * as THREE from 'three';
import { Ribbon, Crates } from '/toolkit/factory/world/lib3d.js';
import { setup, modeLook, followLight, chrome, label, seg2, dot, kf, show, pulse, CHAR, C, ease, mix } from '/episodes/ep006/world/c4kit.js';

const SEG = '/episodes/ep006/world/c4/c-s09-s12/';
const KX = 0.42, Y0 = 2.4, SZ = [12, 4.6];                         // năm k → x = k·KX; vạch séc đầu ở y = Y0; thang y: gần (S09–S11) → rộng (S12)

export async function boot(res) {
  const poses = {
    cNear0: { pos: [3.4, 2.15, 19], tgt: [3.4, 2.15, 0], fov: 14, chart: 1 },
    cNear: { pos: [5.4, 2.0, 18], tgt: [5.4, 2.0, 0], fov: 14, chart: 1 },
    cWide: { pos: [5.0, 1.75, 27], tgt: [5.0, 1.75, 0], fov: 14, chart: 1 },
  };
  const { S, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue, P = S.ruth_path, PL = S.level_path;
  const base = new THREE.Mesh(new THREE.BoxGeometry(20 * KX + 0.5, 0.03, 0.04), new THREE.MeshStandardMaterial({ color: C.muted, emissive: new THREE.Color(C.muted), emissiveIntensity: 0.5, transparent: true }));
  base.position.set(10 * KX, Y0, 0.4); scene.add(base);
  const line = Ribbon({ color: C.ink, z: 0.46, width: 0.06 }), lvl = Ribbon({ color: C.muted, z: 0.44, width: 0.05 }); scene.add(line, lvl);
  const row = Crates({ size: 0.26, gap: 0.05, name: 'ruth' }); row.position.set(4.2, 0.2, 0); scene.add(row);
  const vAt = (A, u) => { const n = Math.min(19, Math.floor(u)); return u >= 20 ? A[20] : mix(A[n], A[n + 1], u - n); };

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    const s = mix(SZ[0], SZ[1], ease(t, MV.m_pull.t0, MV.m_pull.t1)), VY = (v) => Y0 + (v - 1) * s;
    const u = kf(S.draw, t), u2 = kf(S.level_draw, t);
    const pts = []; for (let k = 0; k <= Math.floor(u); k++) pts.push([k * KX, VY(P[k]), P[k] < 1 ? C.warn : C.ink]);
    if (u % 1 > 0) pts.push([u * KX, VY(vAt(P, u)), vAt(P, u) < 1 ? C.warn : C.ink]);
    line.visible = pts.length > 1; if (line.visible) line.set(pts, 0.06);
    const lp = []; for (let k = 0; k <= Math.floor(u2); k++) lp.push([k * KX, VY(PL[k])]);
    if (u2 % 1 > 0) lp.push([u2 * KX, VY(vAt(PL, u2))]);
    lvl.visible = lp.length > 1; if (lvl.visible) lvl.set(lp, 0.05, C.muted);
    row.set({ value: vAt(P, Math.max(0, u)), pulse: pulse(t, b.d3.fell, 0.9) });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0, L = S.label_cues; log.roi = {};
    const sc = (k, v) => O.toScreen(k * KX, VY(v), 0.46);
    const [bx1, by] = O.toScreen(20 * KX + 0.25, Y0, 0.4);
    label(O, 'first check', bx1, by - 26, { align: 'right', kind: 'name', px: 48, w: 600, color: C.muted, alpha: 1 });
    { const [x0, y0] = O.toScreen(0, Y0, 0.4); label(O, L.axis0, x0, y0 + 70, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.d0.ruths) }); }
    { const [x2, y2] = O.toScreen(20 * KX, Y0, 0.4); label(O, L.axis20, x2, y2 + 70, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.d3.since) }); }
    // chấm mỗi kỷ niệm 1 … 15 (cushion ≥ 100 %, warn < 100 %); S09.2 loé
    for (let k = 1; k <= Math.min(20, Math.floor(u)); k++) {
      const [x, y] = sc(k, P[k]), under = P[k] < 1, f = under ? pulse(t, b.d1.slipped, 1.2) : (k === 3 || k === 7 ? pulse(t, b.d1.climbed, 1.2) : 0);
      dot(O, x, y, 9 + 9 * f, under ? C.warn : C.cushion, 1);
    }
    label(O, L['d0.twelve'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.d0.twelve, b.d2.august - 0.4) });
    log.roi['d0.twelve'] = [400, 170, 1520, 260]; log.roi['d1.slipped'] = (() => { const [x, y] = sc(2, P[2]); const [x2] = sc(6, P[6]); return [x - 30, y - 60, x2 + 30, y + 60]; })();
    // S10.1 mốc năm 15; S10.2 cú rơi; S11.1 mốc năm 16
    { const [x, y] = sc(15, P[15]); const a = ok * show(t, b.d2.august); dot(O, x, y, 13 + 8 * pulse(t, b.d2.more, 1.0), C.cushion, a);
      label(O, L['d2.august'], x - 30, y - 50, { align: 'right', kind: 'number', px: 48, alpha: a * (1 - show(t, MV.m_pull.t0)) }); log.roi['d2.august'] = [x - 700, y - 110, x + 30, y + 30]; }
    { const [x, y] = sc(16, P[16]); const a = ok * show(t, b.d4.august); dot(O, x, y, 13, C.warn, a);
      label(O, L['d4.august'], x + 30, y + 80, { align: 'left', kind: 'number', px: 48, alpha: a * (1 - show(t, MV.m_pull.t0)) }); log.roi['d4.august'] = [x - 30, y + 10, x + 700, y + 100]; }
    log.roi['d3.fell'] = (() => { const [x, y] = sc(15, P[15]); const [x2, y2] = sc(16, P[16]); return [x - 40, y - 40, x2 + 40, y2 + 40]; })();
    // S12: séc đều tới mức cuối của séc tăng ở năm 5; vạch nét đứt 90,4 %; điểm cuối séc tăng
    const fA = ok * show(t, b.d6.five);
    if (fA > 0.01) {
      const [x5, y5] = sc(5, PL[5]), [x20, y20] = sc(20, P[20]);
      seg2(O, x5, y20, x20, y20, C.ink, fA * 0.8, 3, [12, 10]);
      dot(O, x5, y5, 13, C.muted, fA); label(O, L['d6.five'], x5 - 20, y5 + 80, { align: 'left', kind: 'number', px: 48, color: C.ink, alpha: fA });
      log.roi['d6.five'] = [x5 - 30, y5 - 30, x5 + 900, y5 + 100];
    }
    { const [x20, y20] = sc(20, P[20]); const a = ok * show(t, b.d7.twenty); dot(O, x20, y20, 13 + 6 * pulse(t, b.d7.twenty, 1), C.warn, a);
      label(O, L['d7.twenty'], x20, y20 - 50, { align: 'right', kind: 'number', px: 48, alpha: a }); log.roi['d7.twenty'] = [x20 - 800, y20 - 110, x20 + 30, y20 + 30]; }
    label(O, 'level check', ...(() => { const [x, y] = sc(Math.min(20, u2), vAt(PL, Math.min(20, u2))); return [x + 20, y + 20]; })(), { align: 'left', kind: 'name', px: 48, w: 600, color: C.muted, alpha: ok * show(t, b.d5.level) * (u2 >= 4 ? 1 : 0) });
    label(O, 'Ruth · ILLUSTRATIVE', ...(() => { const [x, y] = sc(0, 1); return [x, y - 64]; })(), { align: 'left', kind: 'name', px: 48, w: 600, color: CHAR.ruth, alpha: show(t, b.d0.ruths, b.d2.august - 0.3) });
    label(O, '?', 1700, 330, { align: 'center', kind: 'title', px: 120, alpha: ok * show(t, b.d8.ruths), plate: null });
    log.roi['d8.ruths'] = [1600, 200, 1800, 360];
    chrome(O, 1);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
