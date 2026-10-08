// Tập 6 · C3 · phần chung của bốn đoạn N1 (hàng 10 thùng): dựng trang, cột "người + hàng thùng", khung khoá, lớp bắt buộc, nhãn, ngoặc.
// Mốc giờ chỉ từ spine.json của đoạn; hằng số ở đây = hình học + độ dài hiệu ứng chung.
import * as THREE from 'three';
import { Studio, Person, setOpacity } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, ease } from '/toolkit/factory/world/core.js';
import { Crates } from '/episodes/ep006/world/obj6.js';

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

// cột: hàng 10 thùng tâm x, người không mặt (W4, ILLUSTRATIVE) đứng sau thùng đầu tiên (đầu trái của hàng: hàng "của" người đó)
export function column(scene, { x, z = 0, size = 0.5, gap = 0.1, name, h = 1.45 }) {
  const row = Crates({ size, gap, name }); row.position.set(x, 0, z); scene.add(row);
  const person = Person({ h, color: FIG }); person.position.set(row.crateX(0), 0, z - size * 1.3); scene.add(person);
  person.userData.checks = { role: 'mark', char: name, key: 'person-' + name };
  return { row, person, x, z, h, size, name };
}
export function showColumn(col, a) { setOpacity(col.person, a); col.person.scale.setScalar(Math.max(0.001, 0.85 + 0.15 * a)); }

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
