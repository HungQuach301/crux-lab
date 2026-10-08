// Tập 6 · VẬT THỂ MỚI (C3, D-010 quy tắc 4) — chưa vào lib3d.js (không sửa toolkit trong phiên này). Gen kênh: low-poly, màu kênh (E2 tokens.json).
//  N1 Crates — hàng 10 thùng = những gì khoản trả ĐẦU TIÊN của nhân vật mua được. value = sức mua hiện tại so với khoản đầu (0 … ≥ 1).
//  Thùng i (0-based) sáng theo PHẦN: b_i = clamp(n·value − i, 0, 1) — mờ liên tục, không làm tròn nguyên (REVIEW-C2v3 PHỤ-4):
//  0,904 → 9 thùng sáng đủ + thùng thứ 10 sáng 4 %. value ≥ 1 → 10 sáng đủ, KHÔNG BAO GIỜ quá n (PHỤ-5: Edna 105,7 % vẫn là 10).
//  Thùng tối = ink-muted sẫm (không biến mất). Không chữ, không nhãn, không dáng thực phẩm/tiền: khối hộp + nắp + một nẹp ngang.
import * as THREE from 'three';

export const CRATE = { lit: '#F2F4F7', dark: '#3E444D', slat: '#2A303B', glow: '#F2F4F7' };   // ink · ink-muted sẫm · grid (E2)
export const litOf = (value, n = 10) => Math.min(n, Math.max(0, n * value));                   // số thùng sáng (thực, có phần lẻ)

const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.8, transparent: true, ...o });

// ---------------------------------------------------------------- N1 hàng thùng (gốc toạ độ = tâm hàng, đáy trên sàn y = 0, mặt trước hướng +z)
export function Crates({ n = 10, size = 0.5, gap = 0.1, name = 'row' } = {}) {
  const g = new THREE.Group(), pitch = size + gap, W = n * pitch - gap, h = size * 0.78, d = size * 0.8;
  const body = new THREE.BoxGeometry(size, h, d), lid = new THREE.BoxGeometry(size * 1.04, size * 0.07, d * 1.04), slat = new THREE.BoxGeometry(size * 1.005, size * 0.05, 0.01);
  const lit = new THREE.Color(CRATE.lit), dark = new THREE.Color(CRATE.dark), crates = [];
  for (let i = 0; i < n; i++) {
    const c = new THREE.Group(), m = mat(CRATE.dark, { emissive: new THREE.Color(CRATE.glow), emissiveIntensity: 0 });
    const b = new THREE.Mesh(body, m); b.position.y = h / 2; b.castShadow = b.receiveShadow = true;
    const l = new THREE.Mesh(lid, m); l.position.y = h + size * 0.035; l.castShadow = true;
    const s = new THREE.Mesh(slat, mat(CRATE.slat)); s.position.set(0, h * 0.5, d / 2 + 0.006);
    c.add(b, l, s); c.position.x = -W / 2 + size / 2 + i * pitch;
    c.userData.checks = { role: 'mark', series: name, key: `crate-${name}-${i}` };
    g.add(c); crates.push({ c, m, s });
  }
  g.userData = { n, size, pitch, width: W, height: h + size * 0.07, crates };
  // value: sức mua so khoản đầu (0 … ≥ 1); appear ∈ [0,1]: thùng mọc lên từ sàn lần lượt trái → phải; pulse ∈ [0,1]: loé nhẹ các thùng đang sáng
  g.set = ({ value = 1, appear = 1, pulse = 0 } = {}) => {
    const L = litOf(value, n);
    for (let i = 0; i < n; i++) {
      const { c, m, s } = crates[i], bi = Math.min(1, Math.max(0, L - i));
      m.color.copy(dark).lerp(lit, bi); m.emissiveIntensity = bi * (0.32 + 0.35 * pulse);
      const a = Math.min(1, Math.max(0, appear * (1 + 0.3 * (n - 1)) - i * 0.3));   // mọc lần lượt, hàng đầy khi appear = 1
      c.scale.set(1, Math.max(0.001, a), 1); c.visible = a > 0.002;
      for (const q of [m, s.material]) { q.opacity = Math.min(1, a * 1.5); q.depthWrite = a > 0.98; }
      c.userData.checks.level = +bi.toFixed(3);
    }
    return L;
  };
  // toạ độ thế giới (cục bộ → thế giới) của mép trái/phải và tâm thùng i — cho nhãn và ngoặc ở lớp phủ
  g.crateX = (i) => g.position.x - W / 2 + size / 2 + i * pitch;
  g.edgeX = (f) => g.position.x - W / 2 + f * pitch - (f >= n ? gap : 0);   // f = số thùng (thực) tính từ trái
  g.set({ value: 1, appear: 1 });
  return g;
}
