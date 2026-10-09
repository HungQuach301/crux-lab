// Tập 6 · C4 · ĐOẠN D = S13–S23 (Hồi 2). "Bức tường" 715 thanh (V1/V2, c4kit.Strip): mỗi quãng 20 năm một thanh theo tháng bắt đầu, cao = sức mua
// của séc tăng 2 % sau 20 năm; vạch "first check" cố định; phán màu ở S14; cụm 1947–1949; trung vị 80,7 % / 54,3 %; 1990–2006; 25 năm; ba chỉ số;
// về thế giới ở S23 (ba thanh loé: 1949, 1966, 2006 — sang hồi 3). Mốc giờ chỉ từ spine.json; dữ liệu world/grid.json (derive.py).
import * as THREE from 'three';
import { Person, Crates } from '/toolkit/factory/world/lib3d.js';
import { CK } from '/toolkit/factory/world/core.js';
import { setup, Strip, modeLook, followLight, chrome, label, seg2, dip, show, pulse, CHAR, C, ease, lin, mix, rgba } from '/episodes/ep006/world/c4kit.js';

const SEG = '/episodes/ep006/world/c4/d-s13-s23/';
const UNIT = 8, W = 40;

export async function boot(res) {
  const poses = {
    wWall0: { pos: [47, 3.2, 12], tgt: [36, 3.4, 0], fov: 42, chart: 0 },
    cWall: { pos: [20.8, 4.8, 98], tgt: [20.8, 4.8, 0], fov: 14, chart: 1 },
    cLeft: { pos: [10.5, 4.3, 52], tgt: [10.5, 4.3, 0], fov: 14, chart: 1 },
    cRight: { pos: [30.2, 4.3, 52], tgt: [30.2, 4.3, 0], fov: 14, chart: 1 },
    wWall1: { pos: [-7, 4.2, 15], tgt: [9, 4.0, 0], fov: 42, chart: 0 },
  };
  const { S, X, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses, ['/episodes/ep006/world/grid.json']);
  const G = X[0], b = cue, L = S.label_cues;
  const starts = G.cpiu20.map((r) => r[0]), v20 = G.cpiu20.map((r) => r[1]);
  const m25 = new Map(G.cpiu25), v25 = starts.map((s) => (m25.has(s) ? m25.get(s) : null));
  const strip = Strip(scene, v20, { x0: 0, width: W, unit: UNIT, depth: 0.3 });
  const iOf = (ym) => starts.indexOf(ym), iE = iOf('1949-01'), iC = iOf('1966-01'), iR = starts.length - 1, i90 = iOf('1990-01');
  const ruth = Person({ h: 1.45, color: CHAR.ruth }); ruth.position.set(W + 0.9, 0, 0.3); scene.add(ruth);
  ruth.userData.checks = { role: 'mark', char: 'ruth', shape: 'person', fill: CHAR.ruth, key: 'person-ruth' };
  const hline = (c, e) => { const m = new THREE.Mesh(new THREE.BoxGeometry(W + 0.6, 0.06, 0.05), new THREE.MeshStandardMaterial({ color: c, emissive: new THREE.Color(c), emissiveIntensity: e, transparent: true })); m.position.set(W / 2, 0, 0.3); scene.add(m); return m; };
  const medR = hline(C.ink, 0.6), medL = hline(C.muted, 0.4);
  medR.position.y = UNIT * S.med.rising / 100; medL.position.y = UNIT * S.med.level / 100;   // trung vị (out/model.json raw, qua spine)
  const crates = Crates({ size: 0.62, gap: 0.12, name: 'typical' }); crates.position.set(33.5, 10.6, 0); scene.add(crates);
  const mini = [G.cpiu20.map((r) => r[1]), G.cpiw20.map((r) => r[1]), G.pce20.map((r) => r[1])];
  const pceOff = starts.indexOf(G.pce20[0][0]);                 // PCE bắt đầu 1959-01: lệch phải cùng trục tháng

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    const grow = lin(t, S.grow[0], S.grow[1]);
    const verdict = ease(t, b.e4.kept - 0.05, b.e4.kept + 0.6);
    const mx = ease(t, b.f5.twenty - 0.1, b.f5.twenty + 1.0) * (1 - ease(t, b.f6.social - 0.6, b.f6.social + 0.2));
    const f19 = show(t, b.f4.gentler, MV.m_pull21.t0 - 0.3);
    const dimMini = show(t, b.f6.social - 0.3, MV.m_w23.t0 - 0.2);
    const hiP = Math.max(pulse(t, b.f7.start, 1.6), 0.6 * show(t, b.f7.start));
    strip.set({
      grow, verdict, morph: mx > 0 ? { to: v25, x: mx } : null, dim: 1 - 0.85 * dimMini,
      focus: (i) => (f19 > 0 ? mix(1, i >= i90 ? 1 : 0.15, f19) : 1),
      hi: (i) => (i === iR ? Math.max(pulse(t, b.e1.ruths, 1.4), hiP) : i === iE || i === iC ? hiP : (i === 300 ? pulse(t, b.e3.tile, 1.2) : 0)),
    });
    strip.line.visible = t >= b.e2.least - 0.05; strip.line.material.opacity = ease(t, b.e2.least - 0.05, b.e2.least + 0.4);
    medR.visible = t >= b.e9.eighty - 0.05 && t < b.f5.twenty; medR.material.opacity = ease(t, b.e9.eighty - 0.05, b.e9.eighty + 0.4);
    medL.visible = t >= b.f1.fifty - 0.05 && t < b.f5.twenty; medL.material.opacity = ease(t, b.f1.fifty - 0.05, b.f1.fifty + 0.4);
    const cA = show(t, b.f0.crates, b.f1.level);
    crates.set({ value: mix(1, S.med.rising / 100, ease(t, b.f0.most - 0.1, b.f0.most + 0.9)), appear: cA, pulse: pulse(t, b.f0.ten, 0.8) });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    const top = (i, v) => O.toScreen(strip.xOf(i), UNIT * v / 100, 0.3);
    const [fx0, fy] = O.toScreen(0, 0, 0.3), [fx1] = O.toScreen(W, 0, 0.3), [, ly] = O.toScreen(0, UNIT, 0.3);
    const wide = (t < MV.m_push15.t0 || t > MV.m_pull15.t1) && (t < MV.m_push19.t0 || t > MV.m_pull21.t1) ? 1 : 0;   // nhãn trục chỉ ở khung cả tường
    // trang kiểm: mỗi thanh một hình có case = tháng bắt đầu (coverage hồi 2)
    if (CK.on && grow >= 1 && mx < 0.5) for (let i = 0; i < starts.length; i++) {
      const x = strip.xOf(i), h = UNIT * v20[i] / 100; O.shape({ role: 'bar', world: [[x - strip.pitch / 2, 0, 0.3], [x + strip.pitch / 2, h, 0.3]], case: starts[i], value: v20[i], series: 'cpiu20' });
    }
    { const [x, y] = O.toScreen(ruth.position.x, 1.6, 0.3); label(O, 'Ruth', x, y - 24, { align: 'center', kind: 'name', px: 48, w: 600, color: CHAR.ruth, alpha: 1 - cw }); }
    const s13 = MV.m_push15.t0;
    label(O, L['e1.seven'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.e1.seven, b.e2.question - 0.2) });
    { const [x, y] = top(iR, v20[iR]); label(O, L['e1.ruths'], x, y - 40, { align: 'right', kind: 'name', px: 48, w: 600, color: CHAR.ruth, alpha: ok * show(t, b.e1.ruths, s13) * (1 - f19) });
      log.roi['e1.ruths'] = [x - 40, y - 100, x + 40, fy]; }
    label(O, 'first check', fx0, ly - 26, { align: 'left', kind: 'name', px: 48, w: 600, color: C.muted, alpha: ok * wide * show(t, b.e2.least) * (1 - dimMini) });
    label(O, L['e3.tile'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.e3.tile, b.e4.kept - 0.3) });
    label(O, L.axis0, fx0, fy + 64, { align: 'left', kind: 'number', px: 48, alpha: ok * wide * show(t, b.e3.month) * (1 - dimMini) });
    label(O, L.axis1, fx1, fy + 64, { align: 'right', kind: 'number', px: 48, alpha: ok * wide * show(t, b.e3.month) * (1 - dimMini) });
    log.roi['e3.tile'] = (() => { const [x, y] = top(300, v20[300]); return [x - 30, y - 30, x + 30, fy]; })(); log.roi['e2.least'] = [fx0, ly - 20, fx1, ly + 20];
    // S14: phán + 17 of 715 + 1 in 42 (trên cụm trái)
    label(O, L['e4.seventeen'], 960, 236, { align: 'center', kind: 'number', px: 56, color: C.cushion, alpha: ok * show(t, b.e4.seventeen, MV.m_push15.t1 + 0.3) });
    label(O, L['e5.one'], 960, 312, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.e5.one, MV.m_push15.t1 + 0.3) });
    log.roi['e4.kept'] = [fx0, ly - 40, fx1, fy]; log.roi['e4.seventeen'] = [600, 170, 1320, 270];
    // S15: cụm 1947–1949 (cLeft) + "none since"
    { const [x0, y0] = top(iOf('1947-09'), 104), [x1] = top(iE, 104);
      const a = ok * show(t, b.e6.september, MV.m_pull15.t0);
      if (a > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = a; c.strokeStyle = C.cushion; c.lineWidth = 5; c.strokeRect(x0 - 14, y0 - 16, x1 - x0 + 28, fy - y0 + 26); c.restore(); }
      label(O, L['e6.september'], x1 + 40, y0 + 70, { align: 'left', kind: 'number', px: 52, color: C.cushion, alpha: a });
      label(O, L['e7.since'], x1 + 60, y0 + 190, { align: 'left', kind: 'compare', px: 52, color: C.warn, alpha: ok * show(t, b.e7.since, MV.m_pull15.t0) });
      seg2(O, x1 + 60, y0 + 220, 1820, y0 + 220, C.warn, ok * show(t, b.e7.since, MV.m_pull15.t0), 4);
      log.roi['e6.september'] = [x0 - 20, y0 - 20, x1 + 700, fy]; log.roi['e7.since'] = [x1 + 40, y0 + 130, 1820, y0 + 230]; }
    // S16–S17: trung vị + hàng thùng điển hình + séc đều + ô năm 8
    label(O, L['e8.three'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.e8.three, b.f1.level - 0.3) });
    { const [, y] = O.toScreen(0, UNIT * S.med.rising / 100, 0.3); label(O, L.m80, fx1 + 10, y + 16, { align: 'left', kind: 'number', px: 48, alpha: ok * show(t, b.e9.eighty, MV.m_push19.t0) }); }
    label(O, L['e9.eighty'], 960, 312, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.e9.eighty, b.f0.crates) });
    { const [x0, y0] = O.toScreen(crates.edgeX(0), 10.6, 0), [x1] = O.toScreen(crates.edgeX(10), 10.6, 0);
      label(O, L['f0.ten'], (x0 + x1) / 2, y0 + 70, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.f0.ten, b.f1.level) }); log.roi['f0.most'] = [x0 - 10, y0 - 60, x1 + 10, y0 + 90]; }
    { const [, y] = O.toScreen(0, UNIT * S.med.level / 100, 0.3); label(O, L.m54, fx1 + 10, y + 16, { align: 'left', kind: 'number', px: 48, color: C.muted, alpha: ok * show(t, b.f1.fifty, MV.m_push19.t0) }); }
    label(O, L['f1.fifty'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.f1.fifty, MV.m_push19.t0) });
    const yA = ok * show(t, b.f2.eight, MV.m_push19.t0);
    if (yA > 0.01) {   // ô nhỏ: 20 năm, 8 ô đầu tô (séc đều chạm mức cuối của séc tăng khoảng năm 8)
      const c = O.ctx, x0 = 300, w = 60, y = 360; c.save(); c.globalAlpha = yA;
      for (let k = 0; k < 20; k++) { c.fillStyle = k < 8 * lin(t, b.f2.eight, b.f2.eight + 0.6) ? C.muted : rgba(C.grid, 0.9); c.fillRect(x0 + k * w + 3, y, w - 6, 34); }
      c.restore(); label(O, L['f2.eight'], 960, 312, { align: 'center', kind: 'number', px: 52, alpha: yA });
      log.roi['f2.eight'] = [x0, 280, x0 + 20 * w, 400];
    }
    log.roi['e9.eighty'] = [fx0, 0, fx1, fy]; log.roi['f1.fifty'] = log.roi['e9.eighty'];
    // S19: 1990–2006 (cRight)
    { const [xa, ya] = top(i90, 100), [xr, yr] = top(iR, v20[iR]);
      label(O, L['f4.n90'], xa, 236, { align: 'left', kind: 'number', px: 52, alpha: ok * f19 });
      label(O, L['f4.m90'], xa, 312, { align: 'left', kind: 'number', px: 52, alpha: ok * f19 });
      label(O, L['f4.n00'], 1820, 388, { align: 'right', kind: 'number', px: 52, alpha: ok * f19 });
      label(O, L['f4.ruth'], xr, fy + 64, { align: 'right', kind: 'number', px: 48, color: CHAR.ruth, alpha: ok * f19 * show(t, b.f4.ruths) });
      log.roi['f4.gentler'] = [xa - 10, ya - 20, xr + 20, fy]; log.roi['f4.ruths'] = [xr - 300, yr - 20, xr + 20, fy + 80]; }
    // S21: 25 năm
    label(O, L['f5.one'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.f5.one, b.f6.social - 0.4) });
    log.roi['f5.twenty'] = [fx0, ly - 60, fx1, fy];
    // S22: ba dải nhỏ cùng trục tháng (CPI-U, CPI-W, PCE từ 1959); thanh: cushion ≥ 100 %, warn < 100 %
    if (dimMini > 0.01) {
      const c = O.ctx, x0 = 160, x1 = 1760, pw = (x1 - x0) / starts.length, rowsY = [440, 660, 880], hS = 1.55;
      const tags = [['f6.cpiu', 0], ['f6.cpiw', b.f6.social], ['f6.pce', b.f6.gentler]];
      for (let r = 0; r < 3; r++) {
        const a = ok * dimMini * (r === 0 ? 1 : show(t, tags[r][1])); if (a < 0.01) continue;
        c.save(); c.globalAlpha = a; const off = r === 2 ? pceOff : 0;
        mini[r].forEach((v, i) => { c.fillStyle = v >= 100 ? C.cushion : rgba(C.warn, 0.85); const h = v * hS; c.fillRect(x0 + (i + off) * pw, rowsY[r] - h, Math.max(1, pw - 0.6), h); });
        c.restore(); seg2(O, x0, rowsY[r] - 100 * hS, x1, rowsY[r] - 100 * hS, C.muted, a * 0.9, 2);
        label(O, L[tags[r][0]], x0, rowsY[r] - 100 * hS - 22, { align: 'left', kind: 'number', px: 48, alpha: a });
      }
      log.roi['f6.social'] = [x0, 480, x1, 665]; log.roi['f6.gentler'] = [x0, 700, x1, 885];
    }
    { const [x, y] = top(iC, v20[iC]); log.roi['f7.start'] = [x - 400, y - 200, x + 400, fy]; }
    const cwA = show(t, b.f3.own, b.f4.gentler);
    chrome(O, 1, cwA > 0.01 ? L['f3.own'] : null, cwA);
    dip(O, 1 - ease(t, 0, 0.4));
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
