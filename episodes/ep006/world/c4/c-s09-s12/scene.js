// Tập 6 · C4 · ĐOẠN C = S09–S12 (+ MR1). Mở ở THẾ GIỚI (quy tắc 7): cột Ruth [người][séc][hàng 10 thùng] như khung mở đầu, séc lớn lên từng
// kỷ niệm, hàng thùng theo sức mua năm đó (cùng bộ đếm năm S.draw với đường), "twelve" hàng loé → đồ thị (m_c9). Đồ thị V3 trong thế giới: đường sức mua của Ruth theo kỷ niệm (Ribbon), vạch "first check" cố định,
// chấm mỗi năm (cushion / warn), hàng 10 thùng nhỏ theo đầu đường; ĐỈNH S10.2 = đoạn 15 → 16 rơi qua vạch; S12: lùi máy + giãn trục, đường séc đều.
// Mốc giờ chỉ từ spine.json.
import * as THREE from 'three';
import { Ribbon, Crates } from '/toolkit/factory/world/lib3d.js';
import { setup, column, showColumn, nameTag, rowBox, modeLook, followLight, chrome, label, seg2, dot, kf, show, pulse, CHAR, C, ease, mix } from '/episodes/ep006/world/c4kit.js';

const SEG = '/episodes/ep006/world/c4/c-s09-s12/';
const KX = 0.42, Y0 = 2.4, SZ = [12, 4.6];                         // năm k → x = k·KX; vạch séc đầu ở y = Y0; thang y: gần (S09–S11) → rộng (S12)
const WX = -12;                                                    // cột thế giới của Ruth (ngoài khung mọi tư thế đồ thị: cNear0/cNear/cWide thấy x ≥ −1)

export async function boot(res) {
  const poses = {
    wRuth: { pos: [WX - 3.0, 2.2, 7.8], tgt: [WX - 0.7, 0.5, 0], fov: 35, chart: 0 },   // = wRuth của đoạn a/e/f, dời theo cột
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
  const ruth = column(scene, { x: WX, name: 'ruth-world', who: 'ruth' });
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
    row.position.y = mix(1.0, 0.2, ease(t, MV.m_pull.t0, MV.m_pull.t1));   // R1: hàng nhỏ nâng khỏi dải chân trang ở cNear0/cNear (y 0,2 → đáy 940–990 px); cWide hạ về 0,2 (dưới đường séc đều)
    row.set({ value: vAt(P, Math.max(0, u)), pulse: pulse(t, b.d3.fell, 0.9) });
    ruth.row.set({ value: vAt(P, Math.max(0, u)), pulse: pulse(t, b.d0.twelve, 0.9) }); ruth.card.set({ k: Math.min(20, u), appear: 1 }); showColumn(ruth, 1);
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0, L = S.label_cues; log.roi = {};
    const sc = (k, v) => O.toScreen(k * KX, VY(v), 0.46);
    const [bx1, by] = O.toScreen(20 * KX + 0.25, Y0, 0.4);
    nameTag(O, ruth, 1 - cw);
    if (cw < 0.5) { const R = rowBox(O, ruth, vAt(P, Math.max(0, u))); log.roi['d0.twelve'] = [R.x0 - 10, R.yt - 20, R.x1 + 10, R.yb + 20]; }
    // R1: "first check" — cNear0: kẹp vào mép phải (vạch dài quá khung); cWide: dời sang NGAY SAU đầu vạch (không chồng nhãn séc tăng ở năm 20)
    { const pw = ease(t, MV.m_pull.t0, MV.m_pull.t1), c = O.ctx; c.save(); c.font = '600 48px Inter'; const wF = c.measureText('first check').width; c.restore();
      const pu = ease(t, MV.m_push.t0, MV.m_push.t1);   // cNear0: dưới vạch (đường năm 13–15 ở trên vạch); cNear: trên vạch (năm 16–20 ở dưới)
      label(O, 'first check', mix(Math.min(bx1, 1800), bx1 + 24 + wF, pw), mix(mix(by + 56, by - 26, pu), by + 16, pw), { align: 'right', kind: 'name', px: 48, w: 600, color: C.muted, alpha: Math.max(0, (cw - 0.8) / 0.2) }); }
    // nhãn trục năm: gần (S09–S11) dưới vạch, thấp hơn chỗ đường hụt năm 2 (R1); khi lùi máy (S12) xuống hàng đáy dưới đầu đường séc đều — không đè chấm năm 20, nét đứt séc đều và nhãn séc tăng
    const axHide = show(t, MV.m_push.t0 - 0.35, MV.m_pull.t1 - 0.3);   // R1: nhãn trục tắt khi đẩy/lùi máy (không trượt ra mép trái)
    const yAx = (() => { const [, y2] = O.toScreen(20 * KX, Y0, 0.4), [, yl] = sc(20, PL[20]); return mix(y2 + 190, Math.max(y2 + 70, yl + 90), ease(t, MV.m_pull.t0, MV.m_pull.t1)); })();
    { const [x0] = O.toScreen(0, Y0, 0.4); label(O, L.axis0, x0 - 12, yAx, { align: 'left', kind: 'number', px: 48, alpha: ok * show(t, b.d0.ruths) * (1 - axHide) }); }
    { const [x2] = O.toScreen(20 * KX, Y0, 0.4); label(O, L.axis20, x2, yAx, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.d3.since) * (1 - show(t, MV.m_pull.t0 - 0.3, MV.m_pull.t1 - 0.3)) }); }
    // chấm mỗi kỷ niệm 1 … 15 (cushion ≥ 100 %, warn < 100 %); S09.2 loé
    for (let k = 1; k <= Math.min(20, Math.floor(u)); k++) {
      const [x, y] = sc(k, P[k]), under = P[k] < 1, f = under ? pulse(t, b.d1.slipped, 1.2) : (k === 3 || k === 7 ? pulse(t, b.d1.climbed, 1.2) : 0);
      dot(O, x, y, 9 + 9 * f, under ? C.warn : C.cushion, cw);
    }
    label(O, L['d0.anniv'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.d0.anniv, b.d2.august - 0.4) });
    log.roi['d0.anniv'] = [400, 170, 1520, 260]; log.roi['d1.slipped'] = (() => { const [x, y] = sc(2, P[2]); const [x2] = sc(6, P[6]); return [x - 30, y - 60, x2 + 30, y + 60]; })();
    // S10.1 mốc năm 15; S10.2 cú rơi; S11.1 mốc năm 16
    { const [x, y] = sc(15, P[15]); const a = ok * show(t, b.d2.august); dot(O, x, y, 13 + 8 * pulse(t, b.d2.more, 1.0), C.cushion, a);
      // R1: nhãn đặt TRÊN đỉnh cao nhất của đường năm 0–15 (không nằm lên đường)
      let yTop = y; for (let k = 0; k <= 15; k++) yTop = Math.min(yTop, sc(k, P[k])[1]);
      label(O, L['d2.august'], x - 30, yTop - 44, { align: 'right', kind: 'number', px: 48, alpha: a * (1 - show(t, MV.m_pull.t0)) }); log.roi['d2.august'] = [x - 700, yTop - 110, x + 30, y + 30]; }
    { const [x, y] = sc(16, P[16]); const a = ok * show(t, b.d4.august); dot(O, x, y, 13, C.warn, a);
      // R1: dưới-trái điểm năm 16 (đường trước đó ở trên vạch, sau đó ở bên phải) — không đè đường, không ra mép phải
      label(O, L['d4.august'], x - 30, y + 64, { align: 'right', kind: 'number', px: 48, alpha: a * (1 - show(t, MV.m_pull.t0)) }); log.roi['d4.august'] = [x - 700, y + 10, x + 30, y + 100]; }
    log.roi['d3.fell'] = (() => { const [x, y] = sc(15, P[15]); const [x2, y2] = sc(16, P[16]); return [x - 40, y - 40, x2 + 40, y2 + 40]; })();
    // S12: séc đều tới mức cuối của séc tăng ở năm 5; vạch nét đứt 90,4 %; điểm cuối séc tăng
    const fA = ok * show(t, b.d6.five);
    if (fA > 0.01) {
      const [x5, y5] = sc(5, PL[5]), [x20, y20] = sc(20, P[20]);
      seg2(O, x5, y20, x20, y20, C.ink, fA * 0.8, 3, [12, 10]);
      dot(O, x5, y5, 13, C.muted, fA); label(O, L['d6.five'], 960, 236, { align: 'center', kind: 'number', px: 52, color: C.ink, alpha: fA });   // R1: hàng tiêu đề (không đè đường séc đều)
      log.roi['d6.five'] = [x5 - 30, y5 - 30, x20 + 30, y20 + 30];
    }
    { const [x20, y20] = sc(20, P[20]); const a = ok * show(t, b.d7.twenty); dot(O, x20, y20, 13 + 6 * pulse(t, b.d7.twenty, 1), C.warn, a);
      label(O, L['d7.twenty'], 960, 312, { align: 'center', kind: 'number', px: 52, alpha: a }); log.roi['d7.twenty'] = [x20 - 60, y20 - 60, x20 + 30, y20 + 30]; }   // R1: hàng tiêu đề 2
    label(O, 'level check', ...(() => { const [x, y] = sc(Math.min(20, u2), vAt(PL, Math.min(20, u2))); return [x + 20, y + 20]; })(), { align: 'left', kind: 'name', px: 48, w: 600, color: C.muted, alpha: ok * show(t, b.d5.level) * (u2 >= 4 ? 1 : 0) });
    label(O, 'Ruth · ILLUSTRATIVE', ...(() => { const [x, y] = sc(0, 1); return [x, y - 64]; })(), { align: 'left', kind: 'name', px: 48, w: 600, color: CHAR.ruth, alpha: cw * show(t, b.d0.ruths, MV.m_push.t0 - 0.35) });   // R1: tắt trước khi đẩy máy (không trượt ra mép trái)
    label(O, '?', 1700, 330, { align: 'center', kind: 'title', px: 120, alpha: ok * show(t, b.d8.ruths), plate: null });
    log.roi['d8.ruths'] = [1600, 200, 1800, 360];
    chrome(O, 1);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
