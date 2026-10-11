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

// ---------------------------------------------------------------- N1b Check — tấm séc của nhân vật (FIX-R2, D-009 E6: sửa bằng hình, không nhãn khuyên)
//  Thẻ đứng low-poly màu ink (vai "tấm séc tăng dần", beats.md Colour roles) + hai vạch grid trừu tượng (không ký hiệu/chữ số tiền).
//  Chiều cao = base·1,02^k (k = số kỷ niệm đã qua, 0 … 20 → ×1,486): séc LỚN LÊN mỗi năm, cạnh hàng thùng đang tối dần.
//  Vạch ngang ink-muted CỐ ĐỊNH ở chiều cao khoản đầu (rộng hơn thẻ) = "khoản đầu" để thấy phần séc đã vượt lên.
//  Gốc toạ độ = tâm đáy thẻ trên sàn, mặt trước hướng +z.
export const CHECK = { card: '#F2F4F7', line: '#2A303B', first: '#9AA4B2', rate: 1.02 };
export const checkScale = (k) => Math.pow(CHECK.rate, Math.max(0, k));
export function Check({ w = 0.42, base = 0.6, d = 0.05, name = 'check' } = {}) {
  const g = new THREE.Group(), inner = new THREE.Group();
  const m = mat(CHECK.card, { emissive: new THREE.Color(CHECK.card), emissiveIntensity: 0.3 });
  const body = new THREE.Mesh(new THREE.BoxGeometry(w, 1, d), m); body.position.y = 0.5; body.castShadow = body.receiveShadow = true;
  const ln = mat(CHECK.line), lines = [0.7, 0.52].map((f, j) => {
    const s = new THREE.Mesh(new THREE.BoxGeometry(w * (j ? 0.45 : 0.62), 0.035, 0.01), ln); s.position.set(-w * (j ? 0.18 : 0.1), f, d / 2 + 0.006); return s; });
  inner.add(body, ...lines); g.add(inner);
  const fm = mat(CHECK.first), first = new THREE.Mesh(new THREE.BoxGeometry(w + 0.2, 0.04, 0.02), fm); first.position.set(0, base, d / 2 + 0.02);
  g.add(first);
  g.userData = { w, base, d, inner, first, checks: { role: 'mark', series: name, key: `check-${name}` } };
  // k: số kỷ niệm (thực, có thể lẻ); appear ∈ [0,1]: thẻ mọc từ sàn + hiện dần
  g.set = ({ k = 0, appear = 1 } = {}) => {
    const s = checkScale(k), a = Math.min(1, Math.max(0, appear));
    inner.scale.set(1, Math.max(0.001, base * s * a), 1);
    for (const q of [m, ln, fm]) { q.opacity = Math.min(1, a * 1.5); q.depthWrite = a > 0.98; }
    g.visible = a > 0.002; first.visible = a > 0.5;
    g.userData.checks.level = +s.toFixed(4);
    return s;
  };
  g.set({ k: 0 });
  return g;
}
