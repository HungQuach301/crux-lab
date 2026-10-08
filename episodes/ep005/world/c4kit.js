// Tập 5 · C4 · TIỆN ÍCH CHUNG cho các đoạn thế giới của tập (dùng bởi seg-*/scene.js). Không đổi thư viện nhà máy (lib3d.js / core.js).
//  - flyGuard: F-1 "nắp ống kính" — trong cú bay (pose.fly) fov ≤ FOV_CAP và máy CÂN (giảm góc cúi theo tỉ lệ) để cạnh đứng không nghiêng.
//  - measure: đo mỗi khung log (0,1 s) — che khung (hộp bao 3D chiếu, như F-1 thử) + độ nghiêng LỚN NHẤT của cạnh đứng vật thế giới trên màn hình.
//  - followLight: đèn chính (bóng) đi theo điểm nhìn (hướng sáng không đổi) — vật ở mọi khu đều có bóng.
//  - Street / Buyers: hai cụm thế giới dùng ở RANH GIỚI ĐOẠN (B→C phố; C→D ba người mua) — dựng bằng cùng một hàm, cùng toạ độ → khung đầu đoạn sau
//    trùng khung cuối đoạn trước.
import * as THREE from 'three';
import { House, Stack, Person, Beam, Neighborhood, PALETTE, setOpacity } from '/toolkit/factory/world/lib3d.js';

export const FOV_CAP = 38;                 // độ (dọc): tiêu cự ngắn nhất cho phép khi máy bay sát vật
export const LEVEL = 0.85;                 // giữa cú bay: giảm góc cúi/ngửa còn 25 % (cân máy) — hết ở hai đầu cú bay (tư thế khai báo)
export const POP = 0.15, PLATE = '#0B0E13';
export const SX = 48, BX = 30, BX2 = 120;            // khu phố (S09 → S10), khu ba người mua (S03.4, S14 → S15)

export function cues(S) { const c = {}; for (const b of S.beats) c[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 }; return c; }
export function moves(S) { const m = {}; for (const x of S.moves) m[x.id] = x; return m; }
export const interp = (kf, t) => { if (t <= kf[0][0]) return kf[0][1]; for (let i = 1; i < kf.length; i++) if (t <= kf[i][0]) { const [a, x] = kf[i - 1], [b, y] = kf[i]; return x + (y - x) * (t - a) / (b - a); } return kf[kf.length - 1][1]; };

// ------------------------------------------------------------------ F-1 nắp ống kính + cân máy (chỉ trong cú bay; ngoài cú bay không đổi gì)
export function flyGuard(CAM, MV, t) {
  const p = CAM.poseAt(t);
  if (!p.fly) return p;
  const m = CAM.cam;
  const pos = p.pos, tgt = p.tgt.slice(), d = Math.hypot(tgt[0] - pos[0], tgt[2] - pos[2]);
  const mv = MV.find((q) => q.style === 'fly' && t > q.t0 && t < q.t1), x = mv ? Math.min(1, Math.max(0, (t - mv.t0) / (mv.t1 - mv.t0))) : 0, k = LEVEL * Math.sqrt(Math.sin(Math.PI * x));   // 0 ở hai đầu → liền tư thế
  tgt[1] = pos[1] + (tgt[1] - pos[1]) * (1 - k);
  // giữ chiều cao khung ở điểm nhìn (dolly-zoom của core.js) nhưng không rộng hơn FOV_CAP
  const fov = Math.min(FOV_CAP, p.fov);
  m.fov = fov; m.position.set(...pos); m.lookAt(...tgt); m.updateProjectionMatrix(); m.updateMatrixWorld();
  return { ...p, tgt, fov, capped: p.fov > FOV_CAP, d };
}

// ------------------------------------------------------------------ đo che khung + nghiêng cạnh đứng
const bx = new THREE.Box3(), b1 = new THREE.Box3(), cv = new THREE.Vector4(), vA = new THREE.Vector3(), vB = new THREE.Vector3();
function boxOf(o) {
  bx.makeEmpty(); o.updateMatrixWorld(true);
  o.traverse((m) => {
    if (!m.isMesh || !m.visible) return;
    const op = [].concat(m.material).reduce((a, q) => Math.max(a, q.opacity ?? 1), 0); if (op < 0.05) return;
    if (m.isInstancedMesh) m.computeBoundingBox(); else if (!m.geometry.boundingBox) m.geometry.computeBoundingBox();
    bx.union(b1.copy(m.isInstancedMesh ? m.boundingBox : m.geometry.boundingBox).applyMatrix4(m.matrixWorld));
  });
  return bx.isEmpty() ? null : bx.clone();
}
function clipSeg(x0, y0, x1, y1) {   // Liang–Barsky trong khung 1920×1080
  let u0 = 0, u1 = 1; const dx = x1 - x0, dy = y1 - y0;
  for (const [p, q] of [[-dx, x0], [dx, 1920 - x0], [-dy, y0], [dy, 1080 - y0]]) {
    if (p === 0) { if (q < 0) return null; continue; }
    const r = q / p; if (p < 0) { if (r > u1) return null; if (r > u0) u0 = r; } else { if (r < u0) return null; if (r < u1) u1 = r; }
  }
  return [x0 + u0 * dx, y0 + u0 * dy, x0 + u1 * dx, y0 + u1 * dy];
}
export function measure(cam, objs) {
  let cover = { f: 0, obj: null }, tilt = { deg: 0, obj: null };
  const near = cam.near * 1.01;
  for (const [name, o] of Object.entries(objs)) {
    const B = boxOf(o); if (!B) continue;
    // che khung (chặn trên): hình chữ nhật bao của 8 góc chiếu
    // hộp bao cắt ở mặt phẳng gần (góc sau máy không còn tính là "che cả khung"): đỉnh trước máy + giao điểm 12 cạnh với mặt phẳng gần
    let x0 = 1, x1 = -1, y0 = 1, y1 = -1, any = false;
    const P = []; for (let i = 0; i < 8; i++) P.push(new THREE.Vector3(i & 1 ? B.max.x : B.min.x, i & 2 ? B.max.y : B.min.y, i & 4 ? B.max.z : B.min.z).applyMatrix4(cam.matrixWorldInverse));
    const pts = P.filter((p) => p.z <= -near);
    for (let i = 0; i < 8; i++) for (const bit of [1, 2, 4]) { const j = i | bit; if (j === i) continue; const a = P[i], c = P[j];
      if ((a.z + near) * (c.z + near) < 0) pts.push(a.clone().lerp(c, (a.z + near) / (a.z - c.z))); }
    for (const p of pts) { cv.set(p.x, p.y, p.z, 1).applyMatrix4(cam.projectionMatrix); const x = cv.x / cv.w, y = cv.y / cv.w; any = true;
      x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y); }
    const f = !any ? 0 : Math.max(0, Math.min(1, x1) - Math.max(-1, x0)) * Math.max(0, Math.min(1, y1) - Math.max(-1, y0)) / 4;
    if (f > cover.f) cover = { f: +f.toFixed(4), obj: name };
    // cạnh đứng: 4 cạnh của hộp bao (đường thẳng đứng thật của thế giới), cắt ở mặt phẳng gần, chiếu, cắt theo khung, ≥ 40 px
    for (const [ex, ez] of [[B.min.x, B.min.z], [B.max.x, B.min.z], [B.min.x, B.max.z], [B.max.x, B.max.z]]) {
      vA.set(ex, B.min.y, ez).applyMatrix4(cam.matrixWorldInverse); vB.set(ex, B.max.y, ez).applyMatrix4(cam.matrixWorldInverse);
      if (vA.z > -near && vB.z > -near) continue;
      if (vA.z > -near) vA.lerp(vB, (vA.z + near) / (vA.z - vB.z)); else if (vB.z > -near) vB.lerp(vA, (vB.z + near) / (vB.z - vA.z));
      const pa = vA.clone().applyMatrix4(cam.projectionMatrix), pb = vB.clone().applyMatrix4(cam.projectionMatrix);
      const s = clipSeg((pa.x + 1) * 960, (1 - pa.y) * 540, (pb.x + 1) * 960, (1 - pb.y) * 540); if (!s) continue;
      const L = Math.hypot(s[2] - s[0], s[3] - s[1]); if (L < 40) continue;
      const deg = Math.atan2(Math.abs(s[2] - s[0]), Math.abs(s[3] - s[1])) * 180 / Math.PI;
      if (deg > tilt.deg) tilt = { deg: +deg.toFixed(2), obj: name };
    }
  }
  return { cover, tilt };
}

export function followLight(key, tgt) {
  const off = [-6, 11, 10];
  key.target.position.set(tgt[0], Math.max(0, tgt[1]), tgt[2]); key.position.set(tgt[0] + off[0], Math.max(0, tgt[1]) + off[1], tgt[2] + off[2]);
  key.target.updateMatrixWorld();
}

// ------------------------------------------------------------------ khu phố (S09 cuối → S10): mỗi nhà = một tháng mua
export function Street(scene) {
  const g = Neighborhood({ n: 14, seed: 11, spanX: [SX - 8, SX + 8], z: -1.2, size: 0.62 });
  scene.add(g);
  const poses = {
    wStreet: { pos: [SX - 3.0, 1.45, 5.6], tgt: [SX - 1.6, 0.75, -1.2], fov: 35, chart: 0 },
    wStreetR: { pos: [SX + 3.6, 1.45, 5.6], tgt: [SX + 5.0, 0.75, -1.2], fov: 35, chart: 0 },
  };
  return { g, poses };
}

// ------------------------------------------------------------------ ba người mua minh hoạ (không mặt), mỗi người cạnh căn nhà trên chồng giá trị
// C4 r3 (đạo diễn A+B: "ba tháp giống hệt nhau"): mỗi người mua một MÀU riêng (người + mái nhà + tên + đường của họ ở S18), cùng thứ tự Grace · Owen · Victor
// ở mọi đoạn. Màu nhận diện (không mang nghĩa dữ liệu): tránh accent (chỉ số), warn, cushion (tiền để dành), costlier.
// C5b (checks V09): cùng họ màu (hồng · tím nhạt · xanh bạc hà) nhưng tách độ sáng — mọi cặp ΔE2000 ≥ 22 khi mô phỏng mù đỏ/lục (Machado 2009),
// xám ≥ 1,66:1; tên trên nền nhãn ≥ 5,7:1 (V08). Trước: #EE9CC4 · #B9A2FF · #79D7C9 (xám 1,05–1,28; ΔE 2,1–19).
export const BNAME = ['Grace', 'Owen', 'Victor'], BKEY = ['grace', 'owen', 'victor'], BCOL = ['#DE638C', '#BFAAFD', '#9EFFE7'];
// loans: true → mỗi người thêm chồng VAY (xám đậm) cạnh tháp giá trị + vạch 80 % (muted) — S03.4: tỉ lệ vay trên giấy của từng người chạy theo dữ liệu thật
export function Buyers(scene, X = BX, { loans = false } = {}) {
  const U = 2e5, out = [];
  for (let i = 0; i < 3; i++) {
    const x = X + (i - 1) * 3.0;
    const stack = Stack({ unitUsd: U, w: 0.9, d: 0.6 }); stack.position.set(x, 0, 0); const h = stack.set({ usd: 400000, tintBelowUsd: 40001, tint: PALETTE.cushion, tintA: 1 }); scene.add(stack);
    const house = House({ w: 1.25, roof: BCOL[i] }); house.position.set(x, h, 0); scene.add(house);
    const p = Person({ h: 1.15, color: BCOL[i] }); p.position.set(x + 1.05, 0, 0.55); p.rotation.y = -0.35; scene.add(p);
    p.userData.checks = { role: 'mark', char: BKEY[i], shape: 'person', case: BKEY[i], fill: BCOL[i], key: 'person-' + BKEY[i] };   // C5 trang kiểm (V04/V09/S06 hồi 3); khung render không đổi
    const it = { x, stack, house, person: p, top: h + house.userData.height, valueH: h };
    if (loans) {
      it.loan = Stack({ unitUsd: U, w: 0.5, d: 0.45 }); it.loan.position.set(x - 0.82, 0, 0.1); scene.add(it.loan);
      it.tick = Beam({ length: 0.8, color: PALETTE.muted }); it.tick.position.set(x - 0.82, 0.8 * 400000 / U, 0.1); scene.add(it.tick);
    }
    out.push(it);
  }
  const poses = { wBuyers: { pos: [X + 0.4, 2.2, 11.4], tgt: [X, 1.6, 0], fov: 35, chart: 0 } };
  return { items: out, poses,
    set(a) { for (const it of out) for (const o of [it.stack, it.house, it.person]) setOpacity(o, a); },
    // share: tỉ lệ vay ÷ giá trị (trên giấy) của người i; a: độ hiện; g: hệ số mọc (0 → 1)
    loan(i, share, a, g = 1) { const it = out[i]; if (!it.loan) return; it.loan.set({ usd: 400000 * share * g, tintBelowUsd: 1e9, tint: '#5B6573', tintA: 0.9 }); setOpacity(it.loan, a > 0.01 && g > 0.01 ? a : 0); setOpacity(it.tick, a * Math.min(1, g * 1.5)); } };
}

// C4 r3 (đạo diễn: "khối tối trên cuốn lịch" 1:21, 3:30): trang đang lật (mặt sau quay về máy khi lật qua đỉnh) tự sáng như giấy, hai mặt, không đổ bóng
export function litCalendar(cal) {
  const pg = cal.userData.page;
  pg.material.side = THREE.DoubleSide; pg.material.emissive = new THREE.Color('#E9E4D8'); pg.material.emissiveIntensity = 0.75; pg.castShadow = false;
  return cal;
}
