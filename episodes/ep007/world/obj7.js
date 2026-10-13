// Tập 7 · VẬT THỂ MỚI (C3, D-010 quy tắc 4) — chưa vào lib3d.js (không sửa toolkit trong phiên này). Gen kênh: low-poly, màu kênh (E2).
//  N1 MonthTrack — "đường tháng": một ô = MỘT khoản trả tháng; ô giống hệt nhau; trái → phải = thời gian.
//   Bố cục lịch: cột = một năm (cols = 12 ô), cột nối nhau trái → phải; trong cột, tháng 1 ở mép trước (+z), tháng 12 ở mép sau.
//   180 ô = 15 cột đủ. Ô quá n (trễ) = warn, sáng theo PHẦN như W10 (14,6 → 14 ô đủ + ô thứ 15 sáng 60 %). Vạch 15 năm (sau ô n) = ink-muted, đứng yên.
//   Màu theo vai E2 (beats.md Colour roles, vòng 3): ô khoản bắt buộc = ink-muted ("the required-payment level"), lớp trả thêm của Tessa = ink
//   ("the payments", sáng, nổi trên ô). Trả thêm: lớp mỏng trên mỗi ô (extra); gom (S23): 12 lớp của một cột-năm TRƯỢT về ô thứ 12 và chồng
//   lên nhau thành một khối 12 lớp (cùng tổng).
//  PayBar — thanh khoản trả tháng (ink), phần trên mức warnAbove = warn (giá của khoản dự phòng). Chiều cao = USD × scale.
//  Bill — một tờ đô la low-poly (màu vật liệu tiền của lib3d, không chữ) cho S25.
import * as THREE from 'three';

export const TRACK = { ink: '#F2F4F7', warn: '#F2B441', extra: '#F2F4F7', mark: '#9AA4B2', empty: '#2A303B' };   // ink · warn · ink (trả thêm) · ink-muted · grid (E2)
const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.8, transparent: true, ...o });
const cl01 = (x) => Math.min(1, Math.max(0, x));

// ---------------------------------------------------------------- N1 đường tháng (gốc toạ độ = góc trước-trái của ô 1 trên sàn)
export function MonthTrack({ n = 180, cols = 12, spare = 2, tile = 0.34, gap = 0.08, th = 0.07, slab = 0.035, name = 'track' } = {}) {
  const g = new THREE.Group(), pitch = tile + gap, years = Math.ceil(n / cols), nmax = n + spare * cols;
  const box = (h, f = 1) => new THREE.BoxGeometry(tile * f, h, tile * f);
  // lớp trả thêm phủ 72 % mặt ô (vành ink-muted của khoản bắt buộc vẫn thấy); khi gom, lớp chồng lên nhau cách SG → khối = 12 lớp đếm được
  const SF = 0.72, SG = 0.006;
  const tiles = new THREE.InstancedMesh(box(th), mat('#FFFFFF', { emissive: new THREE.Color('#FFFFFF'), emissiveIntensity: 0 }), nmax);
  const slabs = new THREE.InstancedMesh(box(slab, SF), mat(TRACK.extra, { emissive: new THREE.Color(TRACK.extra), emissiveIntensity: 0.8 }), n);
  for (const m of [tiles, slabs]) { m.castShadow = m.receiveShadow = true; m.frustumCulled = false; g.add(m); }
  // vạch 15 năm: thanh mảnh đứng yên dọc theo cột, ngay sau ô n (giữa cột years-1 và years)
  const markX = years * pitch - gap / 2, depth = cols * pitch - gap;
  const mark = new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.32, depth + 0.5), mat(TRACK.mark, { emissive: new THREE.Color(TRACK.mark), emissiveIntensity: 0.4 }));
  mark.position.set(markX, 0.16, -depth / 2 + tile / 2); mark.castShadow = true; g.add(mark);
  const pos = (i) => [Math.floor(i / cols) * pitch + tile / 2, -(i % cols) * pitch];   // x, z của tâm ô i (0-based)
  const M = new THREE.Matrix4(), col = new THREE.Color(), C = { req: new THREE.Color(TRACK.mark), warn: new THREE.Color(TRACK.warn), empty: new THREE.Color(TRACK.empty) };
  const hide = new THREE.Matrix4().makeScale(0, 0, 0);
  tiles.userData.checks = { role: 'mark', series: name, key: `track-${name}-tiles` };
  slabs.userData.checks = { role: 'mark', series: name, key: `track-${name}-extra` };
  mark.userData.checks = { role: 'mark', series: name, key: `track-${name}-mark` };
  g.userData = { n, cols, pitch, tile, th, years, nmax, markX, depth, slab, SG };
  const sm = (u) => u * u * (3 - 2 * u);
  // lit: số ô thường đã đặt (0 … n, thực: ô cuối mọc dần); late: số ô trễ (warn, thực); extra: số cột-năm (0 … years, thực) đã có lớp mỏng,
  // trái → phải; gathered: số cột-năm (từ trái, thực) mà 12 lớp đã trượt về ô thứ 12 thành một khối (phần lẻ = đang trượt; lớp xa ô 12
  // khởi hành muộn hơn, đến sau, nằm trên cùng) — hoặc mảng tiến độ [0,1] từng cột (nhiều cột trượt cùng lúc); markA ∈ [0,1]: vạch 15 năm; pulse ∈ [0,1]: loé nhẹ ô trễ
  g.set = ({ lit = n, late = 0, extra = 0, gathered = 0, markA = 1, pulse = 0 } = {}) => {
    for (let i = 0; i < nmax; i++) {
      const [x, z] = pos(i), isLate = i >= n, a = isLate ? cl01(late - (i - n)) : cl01(lit - i);
      if (a <= 0.002) { tiles.setMatrixAt(i, hide); continue; }
      const s = isLate ? 1 : a;   // ô thường mọc từ sàn; ô trễ hiện đủ cỡ, sáng theo phần (như W10)
      M.makeScale(1, s, 1).setPosition(x, th * s / 2, z); tiles.setMatrixAt(i, M);
      col.copy(C.empty).lerp(isLate ? C.warn : C.req, isLate ? a * (0.85 + 0.15 * pulse) : 1); tiles.setColorAt(i, col);
    }
    const zEnd = pos(cols - 1)[1];
    for (let i = 0; i < n; i++) {
      const c = Math.floor(i / cols), r = i % cols, a = cl01(extra - c) * cl01(lit - i), [x, z] = pos(i);
      if (a <= 0.002) { slabs.setMatrixAt(i, hide); continue; }
      const gp = Array.isArray(gathered) ? (gathered[c] || 0) : cl01(gathered - c);
      const k = cols - 1 - r, dl = 0.35 * k / (cols - 1), e = sm(cl01((gp - dl) / (1 - dl)));
      const y0 = th + slab * a / 2 + 0.002, y1 = th + 0.002 + k * (slab + SG) + slab / 2;
      M.makeScale(1, a, 1).setPosition(x, y0 + (y1 - y0) * e + 0.05 * Math.sin(Math.PI * e), z + (zEnd - z) * e); slabs.setMatrixAt(i, M);
    }
    for (const m of [tiles, slabs]) m.instanceMatrix.needsUpdate = true;
    if (tiles.instanceColor) tiles.instanceColor.needsUpdate = true;
    mark.material.opacity = markA; mark.visible = markA > 0.01;
    tiles.userData.checks.level = +Math.min(n, lit).toFixed(2); tiles.userData.checks.late = +late.toFixed(2);
    slabs.userData.checks.level = +extra.toFixed(3); slabs.userData.checks.gathered = Array.isArray(gathered) ? +gathered.reduce((s, v) => s + v, 0).toFixed(3) : +gathered.toFixed(3);
  };
  // đỉnh khối năm của cột c (toạ độ thế giới) — cho nhãn S23
  g.blockTop = (c) => { const [x, z] = pos(c * cols + cols - 1); return [g.position.x + x, g.position.y + th + cols * (slab + SG), g.position.z + z]; };
  // toạ độ thế giới (đã cộng vị trí nhóm) — cho nhãn/ngoặc ở lớp phủ: tâm ô i, mép trái/phải của cột c, mép trước/sau
  g.tileAt = (i) => { const [x, z] = pos(i); return [g.position.x + x, g.position.y + th, g.position.z + z]; };
  g.colX = (c, side = 0) => g.position.x + c * pitch + (side < 0 ? 0 : side > 0 ? tile : tile / 2);
  g.frontZ = () => g.position.z + tile / 2;
  g.backZ = () => g.position.z - (cols - 1) * pitch - tile / 2;
  g.markWorldX = () => g.position.x + markX;
  g.set({});
  return g;
}

// ---------------------------------------------------------------- thanh khoản trả tháng: ink tới warnAbove, phần trên = warn (gốc = tâm đáy)
export function PayBar({ w = 0.8, d = 0.5, scale = 1 / 1200, name = 'bar' } = {}) {
  const g = new THREE.Group();
  const base = new THREE.Mesh(new THREE.BoxGeometry(w, 1, d), mat(TRACK.ink, { emissive: new THREE.Color(TRACK.ink), emissiveIntensity: 0.12 }));
  const top = new THREE.Mesh(new THREE.BoxGeometry(w, 1, d), mat(TRACK.warn, { emissive: new THREE.Color(TRACK.warn), emissiveIntensity: 0.3 }));
  for (const m of [base, top]) { m.castShadow = m.receiveShadow = true; g.add(m); }
  base.userData.checks = { role: 'bar', series: name, key: `pay-${name}` }; top.userData.checks = { role: 'bar', series: name, key: `pay-${name}-above` };
  g.userData = { w, d, scale };
  // usd: chiều cao (USD/tháng); warnAbove: mức trên đó tô warn; topA ∈ [0,1]: độ hiện phần warn; appear ∈ [0,1]
  g.set = ({ usd = 0, warnAbove = Infinity, topA = 1, appear = 1 } = {}) => {
    const h = usd * scale * appear, hb = Math.min(h, warnAbove * scale), ht = Math.max(0, h - hb);
    base.scale.y = Math.max(0.001, hb); base.position.y = hb / 2; base.visible = hb > 0.002;
    top.scale.y = Math.max(0.001, ht); top.position.y = hb + ht / 2; top.visible = ht > 0.002 && topA > 0.01;
    top.material.color.set(TRACK.ink).lerp(new THREE.Color(TRACK.warn), topA);
    base.userData.checks.value = +Math.min(usd, warnAbove).toFixed(2); top.userData.checks.value = +Math.max(0, usd - warnAbove).toFixed(2);
    return h;
  };
  g.topY = (usd) => usd * scale;
  g.set({});
  return g;
}

// ---------------------------------------------------------------- tờ đô la (thẻ phẳng màu tiền + huy hiệu tròn sáng ở giữa; không chữ)
export function Bill({ w = 0.62, h = 0.28, d = 0.02, name = 'bill' } = {}) {
  const g = new THREE.Group();
  const body = new THREE.Mesh(new THREE.BoxGeometry(w, d, h), mat('#5E8C6A', { roughness: 0.7 })); body.castShadow = body.receiveShadow = true;
  const seal = new THREE.Mesh(new THREE.CylinderGeometry(h * 0.3, h * 0.3, d * 1.3, 12), mat('#C9D8C4', { roughness: 0.6 }));
  const edge = new THREE.Mesh(new THREE.BoxGeometry(w * 0.9, d * 1.2, h * 0.08), mat('#4E7A5A')); edge.position.z = h * 0.36;
  const edge2 = edge.clone(); edge2.position.z = -h * 0.36;
  g.add(body, seal, edge, edge2);
  g.userData.checks = { role: 'mark', series: name, key: `bill-${name}` };
  return g;
}
