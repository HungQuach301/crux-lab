// Tập 7 · C3 · phần chung của năm đoạn: dựng trang, "Tessa + nhà", the stack (W2, bó = một năm của khoản dự phòng), khung khoá, lớp bắt buộc, nhãn.
// Mốc giờ chỉ từ spine.json của đoạn; hằng số ở đây = hình học + độ dài hiệu ứng chung. Số trên hình chỉ qua claims.json (CL[id].display).
import * as THREE from 'three';
import { Studio, Person, House, Stack, setOpacity } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, ease } from '/toolkit/factory/world/core.js';

export const POP = 0.2, PLATE = '#0B0E13', FIG = '#C9D3E2';
export const kf = (k, t) => { if (!k || !k.length) return 0; if (t <= k[0][0]) return k[0][1];
  for (let i = 1; i < k.length; i++) if (t <= k[i][0]) { const [a, x] = k[i - 1], [b, y] = k[i]; return b > a ? x + (y - x) * (t - a) / (b - a) : y; }
  return k[k.length - 1][1]; };
// hiện từ mốc a (dốc POP), tắt từ mốc z (dốc 0,3 s) nếu có
export const show = (t, a, z = Infinity) => ease(t, a - 0.05, a + POP) * (1 - ease(t, z, z + 0.3));

export async function setup(seg, res, poses, { shadowBox = 14 } = {}) {
  const [S, CL] = await Promise.all([loadJSON(seg + 'spine.json'), loadJSON('/episodes/ep007/world/claims.json')]);
  await fonts();
  const cue = {}; for (const b of S.beats) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const st = Stage(res), scene = new THREE.Scene(), { floor } = Studio(scene, { shadowBox });
  const D = (k) => CL[k].display;
  return { S, CL, D, cue, st, O: st.O, renderer: st.renderer, scene, floor, CAM: Camera(poses, S.moves) };
}

// Tessa (W4, không mặt, ILLUSTRATIVE) đứng trước-trái căn nhà của cô (W1); nhà = ink-ish vật liệu kênh, không phải dữ liệu
export function home(scene, { x = 0, z = 0, w = 1.6, h = 1.15, side = -1 } = {}) {
  const house = House({ w }); house.position.set(x, 0, z); scene.add(house);
  const person = Person({ h, color: FIG }); person.position.set(x + side * (w / 2 + 0.6), 0, z + 0.45); scene.add(person);
  person.userData.checks = { role: 'mark', char: 'Tessa', key: 'person-tessa' };
  return { house, person, x, z, w, h };
}
// tên (vòng 3, REVIEW-C3 PHỤ): ngay dưới chân hình người, căn giữa theo người — không chồng lên mái nhà, luôn cạnh người; dx/dy chỉnh khi cần;
// kẹp tâm x ≥ 330 (cả dòng trong khung) và đường chân chữ ≤ 880 (trên dòng "US only …" khi máy di chuyển)
export function nameTag(O, hm, a = 1, o = {}) {
  const [fx, fy] = O.toScreen(hm.person.position.x, 0, hm.person.position.z);
  return label(O, 'Tessa · ILLUSTRATIVE', Math.max(330, fx + (o.dx || 0)), Math.min(880, fy + 50 + (o.dy || 0)), { align: o.align || 'center', kind: 'name', px: 48, w: 600, alpha: a, char: 'Tessa' });
}

// the stack (W2): bó mệnh giá CỐ ĐỊNH = một năm của khoản dự phòng (extra_vs15_total_now / 15 ≈ 12 × $120); 15 bó = $21,622.
// Bó = warn (beats.md Colour roles: "warn = the price of the fallback (the stack's bills)").
export const BUNDLE_TH = 0.17;
export function theStack(scene, G, { x, z = 0 }) {
  const s = Stack({ unitUsd: G.bundle_usd / BUNDLE_TH, bundleUsd: G.bundle_usd, w: 0.9, d: 0.6, maxUsd: G.stack_total * 1.05 });
  s.position.set(x, 0, z); scene.add(s); s.userData.checks = { role: 'bar', series: 'stack', key: 'the-stack' };
  return s;
}
export const stackSet = (s, usd) => { s.set({ usd, warnAboveUsd: -1 }); s.userData.checks.value = +usd.toFixed(2); return usd / s.userData.unitUsd; };

// N1 đường tháng chạy từ nhà Tessa (s21-track, s23-track dùng chung hình học + tư thế máy): nhà bên trái, cột-năm nối nhau sang phải,
// tháng 1 ở mép trước. Đồ thị = nhìn gần thẳng xuống mặt lưới (nghiêng 19°, tiêu cự dài) → lưới đọc như lịch 15 cột × 12 ô.
export const TRACK_POSES = {
  wT0: { pos: [-5.2, 3.4, 7.0], tgt: [1.7, 0, -1.8], fov: 40, chart: 0 },   // vòng 3: lệch trái 0,7 → Tessa (trái nhà) + tên trong khung
  wT: { pos: [-4.0, 4.2, 5.8], tgt: [1.9, 0, -2.0], fov: 40, chart: 0 },
  cT: { pos: [2.45, 13.2, 5.1], tgt: [2.45, 0, -2.0], fov: 31, chart: 1 },
};
export async function trackWorld(scene, MonthTrack) {
  const hm = home(scene, { x: -1.55, z: -1.4, side: 1 });
  hm.person.position.set(-2.7, 0, -0.5);   // vòng 3: trái-trước nhà (tên dưới chân không chạm lưới / nhãn số / nhà)
  const track = MonthTrack({ name: 'tessa' }); track.position.set(0, 0, 0); scene.add(track);
  return { hm, track };
}

// chế độ đồ thị: sàn + sương lùi đi (như Tập 5/6)
export function modeLook(scene, floor, cw) { floor.material.opacity = 1 - 0.85 * cw; scene.fog.near = 30 + 120 * cw; scene.fog.far = 80 + 220 * cw; }

// lớp bắt buộc (như c3kit.js Tập 6): ILLUSTRATIVE (mọi khung có Tessa), nguồn + "US only · history, not a forecast" (mọi khung)
export function chrome(O) { O.chrome({ illus: true, src: 'Freddie Mac weekly mortgage survey', hist: true }); }

// ngoặc ngang (nét lớp phủ, toạ độ thiết kế); tick > 0 = chân xuống, < 0 = chân lên
export function brace(O, x0, x1, y, color, a, lw = 5, tick = 14) {
  if (a <= 0.01) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.strokeStyle = color; c.lineWidth = lw;
  c.beginPath(); c.moveTo(x0, y + tick); c.lineTo(x0, y); c.lineTo(x1, y); c.lineTo(x1, y + tick); c.stroke(); c.restore();
}
export function label(O, s, x, y, o = {}) { return O.text(s, x, y, o.px || 52, { plate: PLATE, plateA: 0.72, ...o }); }
export { C, THREE, setOpacity, ease };
