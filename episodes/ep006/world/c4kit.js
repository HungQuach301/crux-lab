// Tập 6 · C4 · TIỆN ÍCH CHUNG cho sáu đoạn thế giới của tập (world/c4/<đoạn>/scene.js). Không đổi thư viện nhà máy (lib3d.js / core.js).
// Gốc: world/c3kit.js (cột người + séc + hàng thùng đã duyệt C3) + phần mới của C4: màu nhân vật (CHAR), dải 715 quãng (Strip, V1/V2),
// đường năm theo năm (Line, V3), thang mức tăng (Ladder, V10), lớp bắt buộc theo khung (chrome), nhãn ≥ 48 px trên nền mờ.
// Mốc giờ CHỈ từ spine.json của đoạn; hằng số ở đây = hình học + độ dài hiệu ứng chung.
import * as THREE from 'three';
import { Studio, Person, Crates, Check, checkScale, setOpacity, PALETTE } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, ease, lin, mix, rgba } from '/toolkit/factory/world/core.js';

export const POP = 0.2, PLATE = '#0B0E13';
// màu nhận diện (không mang nghĩa dữ liệu; bộ màu đã kiểm mù màu ở Tập 5 C5b, checks V09) — contract.json characters
export const CHAR = { ruth: '#BFAAFD', carl: '#DE638C', edna: '#9EFFE7' };
export const NAME = { ruth: 'Ruth', carl: 'Carl', edna: 'Edna' };
export const kf = (k, t) => { if (!k || !k.length) return 1; if (t <= k[0][0]) return k[0][1];
  for (let i = 1; i < k.length; i++) if (t <= k[i][0]) { const [a, x] = k[i - 1], [b, y] = k[i]; return b > a ? x + (y - x) * (t - a) / (b - a) : y; }
  return k[k.length - 1][1]; };
// hiện từ mốc a (dốc POP), tắt từ mốc z (dốc 0,3 s) nếu có
export const show = (t, a, z = Infinity) => (a == null ? 0 : ease(t, a - 0.05, a + POP) * (1 - ease(t, z, z + 0.3)));
export const pulse = (t, a, d = 0.6) => (a == null || t < a ? 0 : Math.max(0, 1 - (t - a) / d));

export async function setup(seg, res, poses, extra = []) {
  const [S, CL, ...X] = await Promise.all([loadJSON(seg + 'spine.json'), loadJSON('/episodes/ep006/world/claims.json'), ...extra.map((u) => loadJSON(u))]);
  await fonts();
  const cue = {}; for (const b of S.beats) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const MV = {}; for (const m of S.moves) MV[m.id] = m;
  const st = Stage(res), scene = new THREE.Scene(), { floor, key } = Studio(scene, { shadowBox: 24 });
  return { S, CL, X, cue, MV, st, O: st.O, renderer: st.renderer, scene, floor, key, CAM: Camera(poses, S.moves) };
}

// đèn chính theo điểm nhìn (bóng có ở mọi khu của đoạn dài)
export function followLight(key, tgt) {
  key.target.position.set(tgt[0], Math.max(0, tgt[1]), tgt[2]); key.position.set(tgt[0] - 6, Math.max(0, tgt[1]) + 11, tgt[2] + 10); key.target.updateMatrixWorld();
}
// chế độ đồ thị: sàn + sương lùi đi (như Tập 5)
export function modeLook(scene, floor, cw) { floor.material.opacity = 1 - 0.85 * cw; scene.fog.near = 30 + 120 * cw; scene.fog.far = 80 + 220 * cw; }

// cột (C3 FIX-R2): [người][tấm séc][hàng 10 thùng] — người không mặt (W4, ILLUSTRATIVE, màu nhận diện) bên trái séc, séc ở đầu trái hàng thùng.
// level: séc ĐỀU (không lớn lên, màu ink-muted) — khoản đều Ruth từ chối (S04, S08) và của Carl (S25).
export function column(scene, { x, z = 0, size = 0.5, gap = 0.1, name, who = name, h = 1.45, cw = 0.48, cbase = 0.75, person = true, level = false }) {
  const row = Crates({ size, gap, name }); row.position.set(x, 0, z); scene.add(row);
  const card = Check({ w: cw, base: cbase, name: name + (level ? '-level' : '') }); card.position.set(row.edgeX(0) - 0.18 - cw / 2, 0, z); scene.add(card);
  if (level) card.traverse((o) => { if (o.isMesh && o.material.color && o.material.color.getHexString() === 'f2f4f7') { o.material.color.set(C.muted); o.material.emissive.set(C.muted); o.material.emissiveIntensity = 0.12; } });
  let p = null;
  if (person) {
    p = Person({ h, color: CHAR[who] || PALETTE.person2 }); p.position.set(card.position.x - cw / 2 - 0.3, 0, z - 0.25); scene.add(p);
    p.userData.checks = { role: 'mark', char: who, shape: 'person', fill: CHAR[who], key: 'person-' + who };
  }
  return { row, card, person: p, x, z, h, size, name, who, cw, cbase, level };
}
export function showColumn(col, a) { if (col.person) { setOpacity(col.person, a); col.person.scale.setScalar(Math.max(0.001, 0.85 + 0.15 * a)); } }
export function hideColumn(col, a) { setOpacity(col.row, a); setOpacity(col.card, a); if (col.person) setOpacity(col.person, a); }
// tấm séc theo khung khoá k (số kỷ niệm) của spine: S.cards[tên] = [[t, k], …]; không có khoá → k = k0
export function setCheck(col, S, t, appear = 1, k0 = 0) { const K = (S.cards || {})[col.name]; return col.card.set({ k: col.level ? 0 : K ? kf(K, t) : k0, appear }); }
// nhãn sự thật của tấm séc (chế độ đồ thị): trên đỉnh séc ở năm 20
export function checkLabel(O, col, text, alpha, o = {}) {
  const [x, y] = O.toScreen(col.card.position.x - col.cw / 2, col.cbase * checkScale(col.level ? 0 : 20) + 0.06, col.z);
  return label(O, text, x + (o.dx || 0), y - 22 + (o.dy || 0), { kind: 'number', px: 48, alpha, ...o });
}
// tên trên đầu người (thế giới: tên; nhãn số chỉ ở đồ thị)
export function nameTag(O, col, a, o = {}) {
  if (!col.person || a <= 0.01) return null;
  const [x, y] = O.toScreen(col.person.position.x, col.h + 0.12, col.person.position.z);
  return label(O, o.text || NAME[col.who], x, y - 24, { align: 'center', kind: 'name', px: 48, w: 600, color: CHAR[col.who], alpha: a, ...o });
}
// toạ độ màn hình của hàng: x0/x1 mép, xl mép phần sáng, yt đỉnh, yb đáy
export function rowBox(O, col, v = 1) {
  const r = col.row, top = r.userData.height;
  const [x0, yt] = O.toScreen(r.edgeX(0), top, col.z + 0.4), [x1, yb] = O.toScreen(r.edgeX(10), 0, col.z + 0.4), [xl] = O.toScreen(r.edgeX(Math.min(10, 10 * v)), 0, col.z + 0.4);
  return { x0, x1, xl, yt, yb };
}

// lớp bắt buộc: nguồn "US consumer prices (CPI-U)" + "US only · history, not a forecast" trên MỌI khung (mọi khung của tập là lịch sử giá Mỹ);
// ILLUSTRATIVE khi có Ruth/Carl/Edna trên khung (illus ∈ [0,1]); đối trọng (cw) dòng trên history khi có
export function chrome(O, illus = 1, cw = null, cwA = 1) {
  O.chrome({ illus: illus > 0.01, illusA: illus, src: 'US consumer prices (CPI-U)', hist: true, ...(cw && cwA > 0.01 ? { cw, cwA } : {}) });
}
// ngoặc ngang (ink-muted = cố định; ink = phần còn sáng) — nét lớp phủ, toạ độ thiết kế
export function brace(O, x0, x1, y, color, a, lw = 5, tick = 14) {
  if (a <= 0.01) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.strokeStyle = color; c.lineWidth = lw;
  c.beginPath(); c.moveTo(x0, y + tick); c.lineTo(x0, y); c.lineTo(x1, y); c.lineTo(x1, y + tick); c.stroke(); c.restore();
}
export function label(O, s, x, y, o = {}) { return O.text(s, x, y, o.px || 52, { plate: PLATE, plateA: 0.72, ...o }); }
// đoạn thẳng lớp phủ (nét có ghi log.lines cho F-2)
export function seg2(O, x0, y0, x1, y1, color, a, lw = 4, dash = null) {
  if (a <= 0.01) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.strokeStyle = color; c.lineWidth = lw; if (dash) c.setLineDash(dash);
  c.beginPath(); c.moveTo(x0, y0); c.lineTo(x1, y1); c.stroke(); c.restore();
}
// mở/kết đoạn: phủ nền tối dần (ranh giới đoạn; ident ở đoạn a)
export function dip(O, a) { if (a <= 0.005) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.fillStyle = C.bg; c.fillRect(0, 0, 1920, 1080); c.restore(); }

// ================================================================ V1/V2 dải quãng: mỗi quãng H năm = một thanh đứng (InstancedMesh), x = tháng bắt đầu,
// cao = sức mua của khoản 2 % sau H năm (% khoản đầu; 100 % = vạch khoản đầu, cố định, ink-muted). Màu: chưa phán (ink-muted) → phán: cushion (≥ 100)
// / warn (< 100). set({grow, verdict, focus, dim, morph}) mỗi khung. Gốc: x0 = mép trái, đáy y = 0, mặt trước z.
export function Strip(scene, values, { x0 = 0, width = 40, unit = 3.0, depth = 0.25, z = 0, gapFrac = 0.18 } = {}) {
  const n = values.length, pitch = width / n, w = pitch * (1 - gapFrac);
  const geo = new THREE.BoxGeometry(w, 1, depth); geo.translate(0, 0.5, 0);
  const m = new THREE.MeshStandardMaterial({ roughness: 0.75, transparent: true, emissive: new THREE.Color('#000000') });
  const mesh = new THREE.InstancedMesh(geo, m, n); mesh.frustumCulled = false; mesh.castShadow = true; mesh.receiveShadow = true;
  const M4 = new THREE.Matrix4(), col = new THREE.Color(), cM = new THREE.Color(C.muted), cK = new THREE.Color(C.cushion), cW = new THREE.Color(C.warn), cA = new THREE.Color(C.accent), cBg = new THREE.Color(C.grid);
  for (let i = 0; i < n; i++) mesh.setColorAt(i, cM);
  scene.add(mesh);
  const line = new THREE.Mesh(new THREE.BoxGeometry(width + 0.6, 0.035, 0.05), new THREE.MeshStandardMaterial({ color: C.muted, emissive: new THREE.Color(C.muted), emissiveIntensity: 0.5, transparent: true }));
  line.position.set(x0 + width / 2, unit, z + depth / 2 + 0.03); scene.add(line);
  const xOf = (i) => x0 + (i + 0.5) * pitch;
  let vals = values.slice();
  const api = {
    mesh, line, n, pitch, unit, x0, width, xOf, values: () => vals,
    yOf: (pct) => unit * pct / 100,
    // grow ∈ [0,1]: thanh mọc trái → phải; verdict ∈ [0,1]: muted → cushion/warn; focus(i) → [0,1] sáng (1 = bình thường); dim: hệ số mờ chung
    // morph: {to: values2, x: 0…1} đổi chiều cao + số thanh (25 năm có ít thanh hơn: thanh thừa thu về 0); hi(i) → màu nhấn accent [0,1]
    set({ grow = 1, verdict = 0, focus = null, dim = 1, morph = null, hi = null, opacity = 1 } = {}) {
      const L = grow * (n + 30);
      for (let i = 0; i < n; i++) {
        let v = vals[i] ?? 0;
        if (morph) { const v2 = morph.to[i]; v = v2 == null ? v * (1 - morph.x) : mix(v, v2, morph.x); }
        const g = Math.min(1, Math.max(0, (L - i) / 30));
        const hgt = Math.max(0.001, unit * v / 100 * g);
        M4.makeScale(1, hgt, 1).setPosition(xOf(i), 0, z); mesh.setMatrixAt(i, M4);
        const kept = (morph && morph.x > 0.5 ? (morph.to[i] ?? 0) : vals[i]) >= 100;
        col.copy(cM).lerp(kept ? cK : cW, verdict);
        const f = focus ? focus(i) : 1, h = hi ? hi(i) : 0;
        if (h > 0) col.lerp(cA, h);
        col.lerp(cBg, (1 - f) * 0.78); col.multiplyScalar(0.35 + 0.65 * dim);
        mesh.setColorAt(i, col);
      }
      mesh.instanceMatrix.needsUpdate = true; mesh.instanceColor.needsUpdate = true;
      m.opacity = opacity; m.depthWrite = opacity > 0.98; mesh.visible = opacity > 0.005;
      line.material.opacity = opacity; line.visible = opacity > 0.005;
    },
    setValues(v) { vals = v.slice(); },
  };
  return api;
}
// thang năm cho dải (nhãn trục, chỉ đồ thị): năm y ở tháng 1 → x thế giới
export const stripYearX = (strip, starts, y) => { const i = starts.findIndex((s) => +s.slice(0, 4) >= y); return strip.xOf(Math.max(0, i)) - strip.pitch / 2; };

// ================================================================ V3 đường năm theo năm: điểm [k, %] trên khung đồ thị (x = năm 0…20, y = % so khoản đầu)
// vẽ ở lớp phủ (nét 2D theo khung đồ thị chính diện): frame = {x0, x1, y0, y1, v0, v1} toạ độ thiết kế.
export function lineXY(F, k, v) { return [F.x0 + (F.x1 - F.x0) * k / 20, F.y1 - (F.y1 - F.y0) * (v - F.v0) / (F.v1 - F.v0)]; }
export function drawPath(O, F, pts, upto, color, a, lw = 7, belowColor = null, ref = 100) {
  if (a <= 0.01 || upto <= 0) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.lineCap = 'round'; c.lineJoin = 'round'; c.lineWidth = lw;
  const n = Math.min(pts.length - 1, Math.floor(upto)), fr = upto - n;
  for (let j = 1; j <= n + (fr > 0 && n + 1 < pts.length ? 1 : 0); j++) {
    const v0 = pts[j - 1], v1 = j <= n ? pts[j] : mix(pts[j - 1], pts[j], fr), k1 = j <= n ? j : j - 1 + fr;
    c.strokeStyle = belowColor && Math.min(v0, v1) < ref - 1e-9 && (v1 < ref) ? belowColor : color;
    const [xa, ya] = lineXY(F, j - 1, v0), [xb, yb] = lineXY(F, k1, v1);
    c.beginPath(); c.moveTo(xa, ya); c.lineTo(xb, yb); c.stroke();
  }
  c.restore();
}
export function dot(O, x, y, r, color, a) { if (a <= 0.01) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.fillStyle = color; c.beginPath(); c.arc(x, y, r, 0, Math.PI * 2); c.fill(); c.restore(); }

// ================================================================ V10 thang mức tăng (chế độ thế giới: bậc thang; đồ thị: thanh ngang = phần quãng theo kịp)
export function Ladder(scene, rungs, { x0 = 0, y0 = 0.3, step = 0.9, len = 8, z = 0 } = {}) {
  const out = rungs.map((r, i) => {
    const g = new THREE.Group();
    const tread = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.12, 0.9), new THREE.MeshStandardMaterial({ color: '#5B6573', roughness: 0.8, transparent: true }));
    tread.position.set(x0 - 0.9, y0 + i * step, z); tread.castShadow = tread.receiveShadow = true;
    const bar = new THREE.Mesh(new THREE.BoxGeometry(1, 0.42, 0.3), new THREE.MeshStandardMaterial({ color: C.cushion, emissive: new THREE.Color(C.cushion), emissiveIntensity: 0.25, roughness: 0.6, transparent: true }));
    bar.geometry.translate(0.5, 0, 0); bar.position.set(x0, y0 + i * step, z); bar.castShadow = true;
    const back = new THREE.Mesh(new THREE.BoxGeometry(len, 0.42, 0.06), new THREE.MeshStandardMaterial({ color: C.grid, roughness: 0.9, transparent: true }));
    back.position.set(x0 + len / 2, y0 + i * step, z - 0.2);
    g.add(tread, bar, back); scene.add(g);
    bar.userData.checks = { role: 'bar', key: 'rung-' + r.id, case: r.id };
    return { ...r, g, bar, tread, back, y: y0 + i * step };
  });
  return { rungs: out, len, x0,
    set(i, frac, a = 1) { const r = out[i]; r.bar.scale.x = Math.max(0.001, len * frac); setOpacity(r.g, a); } };
}
export { C, ease, lin, mix, rgba, checkScale, setOpacity };
