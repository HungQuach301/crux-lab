// Tập 6 · C3 · phần chung của bốn đoạn N1 (hàng 10 thùng): dựng trang, cột "người + hàng thùng", khung khoá, lớp bắt buộc, nhãn, ngoặc.
// Mốc giờ chỉ từ spine.json của đoạn; hằng số ở đây = hình học + độ dài hiệu ứng chung.
import * as THREE from 'three';
import { Studio, Person, setOpacity } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, ease } from '/toolkit/factory/world/core.js';
import { Crates, Check, checkScale } from '/episodes/ep006/world/obj6.js';

export const POP = 0.2, PLATE = '#0B0E13', FIG = '#C9D3E2';
export const kf = (k, t) => { if (!k || !k.length) return 1; if (t <= k[0][0]) return k[0][1];
  for (let i = 1; i < k.length; i++) if (t <= k[i][0]) { const [a, x] = k[i - 1], [b, y] = k[i]; return b > a ? x + (y - x) * (t - a) / (b - a) : y; }
  return k[k.length - 1][1]; };
// hiện từ mốc a (dốc POP), tắt từ mốc z (dốc 0,3 s) nếu có
export const show = (t, a, z = Infinity) => ease(t, a - 0.05, a + POP) * (1 - ease(t, z, z + 0.3));

export async function setup(seg, res, poses) {
  const [S, CL] = await Promise.all([loadJSON(seg + 'spine.json'), loadJSON('/episodes/ep006/world/claims.json')]);
  await fonts();
  const cue = {}; for (const b of S.beats) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const st = Stage(res), scene = new THREE.Scene(), { floor } = Studio(scene, { shadowBox: 18 });
  return { S, CL, cue, st, O: st.O, renderer: st.renderer, scene, floor, CAM: Camera(poses, S.moves) };
}

// cột (FIX-R2): [người][tấm séc][hàng 10 thùng] — người không mặt (W4, ILLUSTRATIVE) đứng bên trái tấm séc của mình, séc đứng ngay đầu trái
// hàng thùng nó mua: cùng một khung thấy séc lớn lên (1,02^k) trong khi thùng tối dần.
export function column(scene, { x, z = 0, size = 0.5, gap = 0.1, name, h = 1.45, cw = 0.48, cbase = 0.75 }) {
  const row = Crates({ size, gap, name }); row.position.set(x, 0, z); scene.add(row);
  const card = Check({ w: cw, base: cbase, name }); card.position.set(row.edgeX(0) - 0.18 - cw / 2, 0, z); scene.add(card);
  const person = Person({ h, color: FIG }); person.position.set(card.position.x - cw / 2 - 0.3, 0, z - 0.25); scene.add(person);
  person.userData.checks = { role: 'mark', char: name, key: 'person-' + name };
  return { row, card, person, x, z, h, size, name, cw, cbase };
}
// nhãn sự thật của tấm séc (chỉ chế độ đồ thị, claim two_pct_growth_20y_pct): đặt trên đỉnh séc ở năm 20, căn trái theo mép trái séc
export function checkLabel(O, col, CL, alpha, o = {}) {
  const [x, y] = O.toScreen(col.card.position.x - col.cw / 2, col.cbase * checkScale(20) + 0.06, col.z);
  return label(O, `check: +${CL.two_pct_growth_20y_pct.display} a year`, x + (o.dx || 0), y - 22, { kind: 'number', px: o.px || 48, alpha, ...o });
}
export const checkBox = (O, col) => { const [x0, y0] = O.toScreen(col.card.position.x - col.cw / 2 - 0.1, col.cbase * checkScale(20), col.z), [x1, y1] = O.toScreen(col.card.position.x + col.cw / 2 + 0.1, 0, col.z); return [x0 - 6, y0 - 6, x1 + 6, y1 + 6]; };
export function showColumn(col, a) { setOpacity(col.person, a); col.person.scale.setScalar(Math.max(0.001, 0.85 + 0.15 * a)); }
// tấm séc theo khung khoá k (số kỷ niệm) của spine: S.cards[tên] = [[t, k], …]; không có khoá → k = k0
export function setCheck(col, S, t, appear = 1, k0 = 0) { const K = (S.cards || {})[col.name]; return col.card.set({ k: K ? kf(K, t) : k0, appear }); }

// chế độ đồ thị: sàn + sương lùi đi (như Tập 5)
export function modeLook(scene, floor, cw) { floor.material.opacity = 1 - 0.85 * cw; scene.fog.near = 30 + 120 * cw; scene.fog.far = 80 + 220 * cw; }

// lớp bắt buộc: ILLUSTRATIVE (mọi khung có nhân vật), nguồn + "US only · history, not a forecast" (mọi khung lịch sử)
export function chrome(O) { O.chrome({ illus: true, src: 'US consumer prices (CPI-U)', hist: true }); }

// ngoặc ngang trên hàng thùng (ink-muted = cố định: "những gì khoản đầu mua"; ink = phần còn sáng) — nét lớp phủ, toạ độ thiết kế
export function brace(O, x0, x1, y, color, a, lw = 5, tick = 14) {
  if (a <= 0.01) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.strokeStyle = color; c.lineWidth = lw;
  c.beginPath(); c.moveTo(x0, y + tick); c.lineTo(x0, y); c.lineTo(x1, y); c.lineTo(x1, y + tick); c.stroke(); c.restore();
}
export function label(O, s, x, y, o = {}) { return O.text(s, x, y, o.px || 52, { plate: PLATE, plateA: 0.72, ...o }); }
export { C };
