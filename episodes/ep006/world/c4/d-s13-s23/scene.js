// Tập 6 · C4 · ĐOẠN D = S13–S23 (Hồi 2). "Bức tường" 715 thanh (V1/V2, c4kit.Strip): mỗi quãng 20 năm một thanh theo tháng bắt đầu, cao = sức mua
// của séc tăng 2 % sau 20 năm; vạch "first check" cố định; phán màu ở S14; cụm 1947–1949; trung vị 80,7 % / 54,3 %; 1990–2006; 25 năm; ba chỉ số;
// về thế giới ở S23 (ba thanh loé: 1949, 1966, 2006 — sang hồi 3). Mốc giờ chỉ từ spine.json; dữ liệu world/grid.json (derive.py).
import * as THREE from 'three';
import { Person, Crates } from '/toolkit/factory/world/lib3d.js';
import { CK } from '/toolkit/factory/world/core.js';
import { setup, Strip, stripYearX, modeLook, followLight, chrome, label, seg2, dip, show, pulse, setOpacity, CHAR, C, ease, lin, mix, rgba } from '/episodes/ep006/world/c4kit.js';

const SEG = '/episodes/ep006/world/c4/d-s13-s23/';
const UNIT = 8, W = 40;

export async function boot(res) {
  const poses = {
    wWall0: { pos: [47, 3.2, 12], tgt: [36, 3.4, 0], fov: 42, chart: 0 },
    // R1: khung đồ thị nới để mọi thanh + nhãn trung vị nằm trong [96, 1824] và trên dải chân trang (cWall: tường x 100–1590 px, đáy 780 px;
    // cLeft: đẩy nhẹ vào 1947–1980, đáy 850 px, đỉnh thanh dưới hàng nhãn; cRight: 1990–2006, đỉnh thanh ≤ 420 px dưới ba hàng nhãn, đáy 800 px)
    cWall: { pos: [23.08, 6.44, 118], tgt: [23.08, 6.44, 0], fov: 14, chart: 1 },
    cLeft: { pos: [14.3, 5.17, 73.3], tgt: [14.3, 5.17, 0], fov: 14, chart: 1 },
    cRight: { pos: [28, 5.45, 92], tgt: [28, 5.45, 0], fov: 14, chart: 1 },
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
  // trung vị (out/model.json raw, qua spine): vị trí đặt mỗi khung (R1: hạ dần từ 100 % theo lời)
  const crates = Crates({ size: 0.62, gap: 0.12, name: 'typical' }); crates.position.set(33.5, 11.5, 0); scene.add(crates);
  const mini = [G.cpiu20.map((r) => r[1]), G.cpiw20.map((r) => r[1]), G.pce20.map((r) => r[1])];
  const pceOff = starts.indexOf(G.pce20[0][0]);                 // PCE bắt đầu 1959-01: lệch phải cùng trục tháng
  // R1: séc ĐỀU của cùng quãng = séc tăng / 1,02^20 (cùng giá; trung vị 80,7 / 1,486 = 54,3) — S17 tường đổi sang séc đều
  const lv20 = v20.map((v) => v / Math.pow(1.02, 20)), n = starts.length;
  const wAt = (sid, re) => { const w = S.words.find((q) => q.sid.startsWith(sid) && re.test(q.w)); return w ? w.s : null; };
  const tRuth15 = wAt('S15.2', /^Ruth/), tRising16 = wAt('S16.2', /^rising/);
  // quét sáng trái → phải (đếm / hỏi từng quãng / xếp theo tháng): thanh i loé khi đầu quét đi qua
  const tw = (s, px = 48) => { const c = O.ctx; c.save(); c.font = `700 ${px}px Inter`; const w = c.measureText(s).width; c.restore(); return w; };
  const sweep = (t, a, d) => { if (t < a || t > a + d + 0.3) return null; const p = (t - a) / d * (n + 80) - 40; return (i) => Math.max(0, 1 - Math.abs(i - p) / 40); };

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    const grow = lin(t, S.grow[0], S.grow[1]);
    const verdict = ease(t, b.e4.kept - 0.05, b.e4.kept + 0.6);
    const mx = ease(t, b.f5.twenty - 0.1, b.f5.twenty + 1.0) * (1 - ease(t, b.f6.social - 0.6, b.f6.social + 0.2));
    const f19 = show(t, b.f4.gentler, MV.m_pull21.t0 - 0.3);
    const dimMini = show(t, b.f6.social - 0.3, MV.m_w23.t0 - 0.2);
    const hiP = Math.max(pulse(t, b.f7.start, 1.6), 0.6 * show(t, b.f7.start));
    // R1 động tác theo lời: S13 "seven hundred fifteen" quét đếm, "question … least" quét hỏi từng quãng, "month" quét theo tháng;
    // S16 "typical" sáng các quãng quanh trung vị; S17 "level" tường đổi sang séc ĐỀU (cùng quãng), về séc tăng khi đẩy máy S19
    const sw = sweep(t, b.e1.seven, 1.5) || sweep(t, b.e2.question, b.e2.least - b.e2.question) || sweep(t, b.e3.month, 1.0);
    const fT = show(t, b.e8.typical, b.e9.eighty + 1.2), medV = S.med.rising;
    const ml = ease(t, b.f1.level, b.f1.level + 1.6) * (1 - ease(t, MV.m_push19.t0, MV.m_push19.t1));
    const hR = Math.max(pulse(t, b.e1.ruths, 1.4), pulse(t, tRuth15, 1.6), hiP);
    strip.set({
      grow, verdict, morph: ml > 0.001 ? { to: lv20, x: ml } : mx > 0 ? { to: v25, x: mx } : null, dim: 1 - 0.85 * dimMini, opacity: 1 - 0.97 * dimMini,
      focus: (i) => (f19 > 0 ? mix(1, i >= i90 ? 1 : 0.15, f19) : fT > 0 ? mix(1, Math.abs(v20[i] - medV) <= 2.5 ? 1 : 0.3, fT) : 1),
      hi: (i) => Math.max(sw ? sw(i) : 0, i === iR ? hR : i === iE || i === iC ? hiP : (i === 300 ? pulse(t, b.e3.tile, 1.2) : 0)),
    });
    setOpacity(ruth, 1 - dimMini);
    strip.line.visible = t >= b.e2.least - 0.05 && dimMini < 0.99; strip.line.material.opacity = ease(t, b.e2.least - 0.05, b.e2.least + 0.4) * (1 - dimMini);
    // R1: vạch trung vị HẠ từ vạch séc đầu (100 %) xuống mức trung vị từ đầu cụm lời tới đúng từ số ("rising" → "eighty"; "level" → "fifty-four")
    const yR = mix(100, S.med.rising, ease(t, tRising16, b.e9.eighty)), yL = mix(100, S.med.level, ease(t, b.f1.level, b.f1.fifty));
    medR.visible = t >= tRising16 - 0.05 && t < b.f5.twenty; medR.material.opacity = ease(t, tRising16 - 0.05, tRising16 + 0.3); medR.position.y = UNIT * yR / 100;
    medL.visible = t >= b.f1.level - 0.05 && t < b.f5.twenty; medL.material.opacity = ease(t, b.f1.level - 0.05, b.f1.level + 0.3); medL.position.y = UNIT * yL / 100;
    const cA = show(t, b.f0.crates, b.f1.level + 0.7);
    crates.set({ value: mix(1, S.med.rising / 100, ease(t, b.f0.most - 0.1, b.f0.most + 0.9)), appear: cA, pulse: pulse(t, b.f0.ten, 0.8) });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    const top = (i, v) => O.toScreen(strip.xOf(i), UNIT * v / 100, 0.3);
    const [fx0, fy] = O.toScreen(0, 0, 0.3), [fx1] = O.toScreen(W, 0, 0.3), [, ly] = O.toScreen(0, UNIT, 0.3);
    const wide = (t < MV.m_push15.t0 || t > MV.m_pull15.t1) && (t < MV.m_push19.t0 || t > MV.m_pull21.t1) ? 1 : 0;   // nhãn trục chỉ ở khung cả tường
    // trang kiểm: mỗi thanh một hình có case = tháng bắt đầu (coverage hồi 2)
    if (CK.on && grow >= 1 && mx < 0.5 && ml < 0.5 && dimMini < 0.5) for (let i = 0; i < starts.length; i++) {
      const x = strip.xOf(i), h = UNIT * v20[i] / 100; O.shape({ role: 'bar', world: [[x - strip.pitch / 2, 0, 0.3], [x + strip.pitch / 2, h, 0.3]], case: starts[i], value: v20[i], series: 'cpiu20' });
    }
    { const [x, y] = O.toScreen(ruth.position.x, 1.6, 0.3); label(O, 'Ruth', x, y - 24, { align: 'center', kind: 'name', px: 48, w: 600, color: CHAR.ruth, alpha: (1 - cw) * (t > MV.m_w23.t0 ? ease(t, MV.m_w23.t1 - 0.1, MV.m_w23.t1 + 0.2) : 1) }); }   // vòng sửa 3: không hiện khi máy còn chạy về thế giới (phát lại: ra mép 114,7)
    const s13 = MV.m_push15.t0;
    label(O, L['e1.seven'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.e1.seven, b.e2.question - 0.2) });
    { const [x, y0] = top(iR, v20[iR]), y = Math.min(y0, ly); label(O, L['e1.ruths'], x, y - 40, { align: 'right', kind: 'name', px: 48, w: 600, color: CHAR.ruth, alpha: ok * show(t, b.e1.ruths, s13) * (1 - f19) });
      log.roi['e1.ruths'] = [x - 40, y - 100, x + 40, fy]; }
    const s15 = t > MV.m_push15.t0 ? 1 - ease(t, b.e8.typical, b.e8.typical + 0.3) : 0;
    label(O, 'first check', fx0, ly - 26, { align: 'left', kind: 'name', px: 48, w: 600, color: C.muted, alpha: ok * wide * (1 - s15) * show(t, b.e2.least) * (1 - show(t, b.f6.social - 0.3)) });
    label(O, L['e3.tile'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.e3.tile, b.e4.kept - 0.3) });
    // vòng sửa 3 (B15: trục ngang đọc ra "thời gian của một séc"): từ S15 nhãn trục cả ở cLeft (tắt khi lùi máy), mốc năm bắt đầu 1966 · 1986 giữa
    // "1947" và "Aug 2006" + chú thích trục "start month" — mỗi thanh = một quãng 20 năm theo tháng bắt đầu; mốc ngoài khung thì ẩn
    const ax = ok * show(t, b.e3.month) * (1 - show(t, b.f6.social - 0.3)), wS = t > MV.m_push15.t1 && t < MV.m_pull15.t1 + 1 ? 1 - show(t, MV.m_pull15.t0 - 0.1, MV.m_pull15.t1 - 0.3) : wide;
    const tk = ok * show(t, MV.m_push15.t1) * (1 - show(t, b.f6.social - 0.3)) * wS, inF = (x, s) => { const h = tw(s) / 2; return x - h >= 100 && x + h <= 1820 ? 1 : 0; };
    label(O, L.axis0, fx0, fy + 64, { align: 'left', kind: 'number', px: 48, alpha: ax * wS * (fx0 >= 96 ? 1 : 0) });
    label(O, L.axis1, fx1, fy + 64, { align: 'right', kind: 'number', px: 48, alpha: ax * wS * (fx1 <= 1824 ? 1 : 0) });
    { const xs = [1966, 1986].map((y) => O.toScreen(stripYearX(strip, starts, y), 0, 0.3)[0]);
      xs.forEach((x, j) => { const s = String([1966, 1986][j]), a = tk * inF(x, s); seg2(O, x, fy + 6, x, fy + 18, C.muted, a, 3); label(O, s, x, fy + 64, { align: 'center', kind: 'number', px: 48, alpha: a }); });
      const xm = (xs[0] + xs[1]) / 2; label(O, 'start month', xm, fy + 64, { align: 'center', kind: 'name', px: 48, w: 600, color: C.muted, alpha: tk * inF(xm, 'start month') }); }
    log.roi['e3.tile'] = (() => { const [x, y] = top(300, v20[300]); return [x - 30, y - 30, x + 30, fy]; })(); log.roi['e2.least'] = [fx0, ly - 20, fx1, ly + 20];
    // S14: phán + 17 of 715 + 1 in 42 (trên cụm trái)
    label(O, L['e4.seventeen'], 960, 236, { align: 'center', kind: 'number', px: 56, color: C.cushion, alpha: ok * show(t, b.e4.seventeen, MV.m_push15.t1 + 0.3) });
    label(O, L['e5.one'], 960, 312, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.e5.one, MV.m_push15.t1 + 0.3) });
    log.roi['e4.kept'] = [fx0, ly - 40, fx1, fy]; log.roi['e4.seventeen'] = [600, 170, 1320, 270];
    // S15: cụm 1947–1949 (cLeft) + "none since"
    // R1 (nghĩa B15): cụm xanh 1947–1949 = đỉnh thanh VƯỢT vạch "first check" (giữ được sức mua); "Since" = vạch warn chạy dọc vạch séc đầu từ 1949
    // tới thanh của Ruth (tới đúng "Ruth's"), mọi thanh sau đó nằm dưới; lùi máy thấy vạch tới thanh Ruth, thanh Ruth loé
    // R2 (B15 vòng 2: "không rõ trục đo gì", không ai thấy thanh của Ruth): máy lùi ngay sau "Since" (spine), vạch "none since" chạy từ cụm xanh tới
    // ĐÚNG thanh cuối ở "Ruth's"; thanh cuối tô màu Ruth (như các cảnh khác) + tên; khoảng hụt từ đỉnh mỗi thanh sau 1949 tới vạch "first check"
    // tô warn nhạt theo vạch chạy → cao thanh đọc ra là sức mua SO VỚI SÉC ĐẦU (thiếu bao nhiêu), không phải giá
    { const [x0, y0] = top(iOf('1947-09'), 104), [x1] = top(iE, 104);
      const a = ok * show(t, b.e6.september, b.e8.typical);
      if (a > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = a; c.strokeStyle = C.cushion; c.lineWidth = 5; c.strokeRect(x0 - 14, y0 - 16, x1 - x0 + 28, fy - y0 + 26); c.restore(); }
      label(O, L['e6.september'], x1 + 40, 250, { align: 'left', kind: 'number', px: 52, color: C.cushion, alpha: ok * show(t, b.e6.september, MV.m_pull15.t0) });
      const pS = lin(t, b.e7.since, tRuth15), [xs, yb] = O.toScreen(strip.xOf(iE + 1), UNIT * 1.005, 0.36), [xe] = O.toScreen(mix(strip.xOf(iE + 1), strip.xOf(iR), pS), UNIT, 0.36);
      const gA = ok * show(t, b.e7.since, b.e8.typical), iCut = mix(iE + 1, iR, pS);
      if (gA > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = gA; c.fillStyle = rgba(C.warn, 0.3);
        for (let i = iE + 1; i <= iCut; i++) { const [xa] = O.toScreen(strip.xOf(i) - strip.pitch / 2, 0, 0.3), [xb, yt] = O.toScreen(strip.xOf(i) + strip.pitch / 2, UNIT * v20[i] / 100, 0.3); c.fillRect(xa, ly, xb - xa, yt - ly); }
        c.restore(); }
      seg2(O, xs, yb, xe, yb, C.warn, ok * show(t, b.e7.since, b.e8.typical), 6);
      label(O, L['e7.since'], xs + 10, yb - 30, { align: 'left', kind: 'compare', px: 52, color: C.warn, alpha: ok * show(t, b.e7.since, b.e8.typical - 0.3) });
      // vòng sửa 3 (B15): thanh của Ruth tô màu Ruth + tên từ cuối cú lùi máy (nửa sau S15), không chờ "Ruth's"
      const rA = ok * show(t, MV.m_pull15.t1 - 0.4, b.e8.typical + 0.6), [xr0] = O.toScreen(strip.xOf(iR) - 0.14, 0, 0.3), [xr1, yr] = O.toScreen(strip.xOf(iR) + 0.14, UNIT * v20[iR] / 100, 0.3);
      if (rA > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = rA; c.fillStyle = CHAR.ruth; c.fillRect(xr0, yr, xr1 - xr0, fy - yr); c.restore(); }
      label(O, 'Ruth', Math.min(xr1 + 14, 1820 - tw('Ruth')), ly + 48, { align: 'left', kind: 'name', px: 48, w: 600, color: CHAR.ruth, alpha: rA });
      const inL = t > MV.m_push15.t1 ? 1 : 0;   // R2: suốt S15 nhãn vạch ở đầu PHẢI (trái là "none since"), về trái ở "typical"
      label(O, 'first check', Math.min(1800, fx1), ly - 26, { align: 'right', kind: 'name', px: 48, w: 600, color: C.muted, alpha: ok * inL * show(t, b.e6.every, b.e8.typical - 0.3) });
      log.roi['e6.september'] = [x0 - 20, 190, x1 + 700, fy]; log.roi['e7.since'] = [xs, yb - 90, 1820, fy]; }
    // S16–S17: trung vị + hàng thùng điển hình + séc đều + ô năm 8
    label(O, L['e8.three'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.e8.three, b.f1.level - 0.3) });
    { const [, y] = O.toScreen(0, UNIT * yR / 100, 0.3); label(O, L.m80, fx1 + 10, y + 16, { align: 'left', kind: 'number', px: 48, alpha: ok * show(t, b.e9.eighty, MV.m_push19.t0) }); }
    label(O, L['e9.eighty'], 960, 312, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.e9.eighty, b.f0.crates) });
    { const [x0, y0] = O.toScreen(crates.edgeX(0), 11.5, 0), [x1] = O.toScreen(crates.edgeX(10), 11.5, 0);
      label(O, L['f0.ten'], (x0 + x1) / 2, y0 + 70, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.f0.ten, b.f1.level + 0.7) }); log.roi['f0.most'] = [x0 - 10, y0 - 60, x1 + 10, y0 + 90]; }
    { const [, y] = O.toScreen(0, UNIT * yL / 100, 0.3); label(O, L.m54, fx1 + 10, y + 16, { align: 'left', kind: 'number', px: 48, color: C.muted, alpha: ok * show(t, b.f1.fifty, MV.m_push19.t0) }); }
    label(O, L['f1.fifty'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.f1.fifty, MV.m_push19.t0) });
    const yA = ok * show(t, b.f2.sunk, MV.m_push19.t0);   // R1: hàng 20 ô năm hiện từ "sunk", tô dần từng năm tới đúng "eight" (số hiện ở "eight")
    if (yA > 0.01) {   // ô nhỏ: 20 năm, 8 ô đầu tô (séc đều chạm mức cuối của séc tăng khoảng năm 8)
      const c = O.ctx, x0 = 300, w = 60, y = 360; c.save(); c.globalAlpha = yA;
      for (let k = 0; k < 20; k++) { c.fillStyle = k < 8 * lin(t, b.f2.sunk + 0.3, b.f2.eight) ? C.muted : rgba(C.grid, 0.9); c.fillRect(x0 + k * w + 3, y, w - 6, 34); }
      c.restore(); label(O, L['f2.eight'], 960, 312, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.f2.eight, MV.m_push19.t0) });
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
    label(O, L['f5.one'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.f5.one, b.f6.social - 0.9) });   // R1: tắt hẳn trước nhãn CPI-U
    log.roi['f5.twenty'] = [fx0, ly - 60, fx1, fy];
    // S22: ba dải nhỏ cùng trục tháng (CPI-U, CPI-W, PCE từ 1959); thanh: cushion ≥ 100 %, warn < 100 %
    if (dimMini > 0.01) {
      // R1: mỗi dải một hàng riêng — nhãn TRÊN dải (không đè thanh), tường 3D tắt hẳn (không chồng lớp)
      const c = O.ctx, x0 = 160, x1 = 1760, pw = (x1 - x0) / starts.length, rowsY = [424, 664, 904], hS = 1.6;
      const tags = [['f6.cpiu', 0], ['f6.cpiw', b.f6.social], ['f6.pce', b.f6.gentler]];
      for (let r = 0; r < 3; r++) {
        const a = ok * dimMini * (r === 0 ? 1 : show(t, tags[r][1])); if (a < 0.01) continue;
        c.save(); c.globalAlpha = a; const off = r === 2 ? pceOff : 0;
        mini[r].forEach((v, i) => { c.fillStyle = v >= 100 ? C.cushion : rgba(C.warn, 0.85); const h = v * hS; c.fillRect(x0 + (i + off) * pw, rowsY[r] - h, Math.max(1, pw - 0.6), h); });
        c.restore(); seg2(O, x0, rowsY[r] - 100 * hS, x1, rowsY[r] - 100 * hS, C.muted, a * 0.9, 2);
        label(O, L[tags[r][0]], x0, rowsY[r] - 194, { align: 'left', kind: 'number', px: 48, alpha: a });
      }
      log.roi['f6.social'] = [x0, 440, x1, 670]; log.roi['f6.gentler'] = [x0, 680, x1, 910];
    }
    { const [x, y] = top(iC, v20[iC]); log.roi['f7.start'] = [x - 400, y - 200, x + 400, fy]; }
    const cwA = show(t, b.f3.own, b.f4.gentler);
    chrome(O, 1, cwA > 0.01 ? L['f3.own'] : null, cwA);
    dip(O, 1 - ease(t, 0, 0.4));
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
