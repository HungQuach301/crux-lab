// Tập 6 · C4 vòng sửa 2 (cổng gốc tắt tiếng: B01 "refrigerator" / "shrink", B04 "two stacks of papers"). Dùng chung đoạn a, b, c; không đổi c4kit/lib3d.
// Tấm séc đọc ra là TẤM SÉC: thẻ NGANG (cột tạo với cw > cbase) + dòng người nhận, ô số tiền, dòng ký, dòng ghi chú (vạch trừu tượng, không ký hiệu/chữ số tiền).
// Lớn lên ĐỀU hai chiều ×1,02^k (đã duyệt C3), neo góc dưới phía hàng thùng; VIỀN séc đầu (ink-muted, cố định) giữ tại chỗ → séc nay lớn hơn séc đầu
// thấy được ở mọi tư thế máy. trend: nét trên mặt séc — 'rise' (séc tăng: nhích lên) · 'flat' (séc đều: phẳng) (B04 muted read).
// Gói card.set của lib3d: mọi lời gọi setCheck / card.set cũ giữ nguyên. Séc đều (col.level) không có viền (không lớn lên).
import * as THREE from 'three';
import { C, checkScale } from '/episodes/ep006/world/c4kit.js';

const INK = '#2A303B', R20 = checkScale(20);
const flat = (color) => new THREE.MeshStandardMaterial({ color, emissive: new THREE.Color(color), emissiveIntensity: 0.15, roughness: 0.8, transparent: true });

export function checkLook(col, { trend = col.level ? 'flat' : 'rise', anchor = 1 } = {}) {
  const g = col.card, { w, base, d, inner, first } = g.userData;
  inner.remove(...inner.children.slice(1)); g.remove(first);                       // hai vạch của thẻ đứng cũ + vạch séc đầu cũ (thay bằng viền)
  const mk = inner.children[0].material, mI = flat(INK), mG = flat(C.muted);
  const bar = (m, sx, sy) => { const b = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 0.01), m); b.scale.set(sx, sy, 1); return b; };
  // vạch séc trong toạ độ thẻ (x ∈ [−w/2, w/2], y ∈ [0, 1] theo chiều cao thẻ): dòng người nhận, dòng ghi chú, dòng ký, ô số tiền (khung)
  const T = 0.055, BX = 0.31, BW = 0.2, BH = 0.24, BY = 0.46;
  const marks = [[-0.12, 0.46, w * 0.56, T], [-0.27, 0.18, w * 0.3, T], [0.24, 0.18, w * 0.32, T],
    [BX, BY + BH / 2, w * BW, T], [BX, BY - BH / 2, w * BW, T], [BX - BW / 2, BY, w * 0.03, BH], [BX + BW / 2, BY, w * 0.03, BH]]
    .map(([x, y, sx, sy]) => { const b = bar(mI, sx, sy); b.position.set(w * x, y, d / 2 + 0.006); return b; });
  inner.add(...marks);
  // nét xu hướng (phần trên mặt séc): đặt lại mỗi khung theo cỡ thẻ để giữ đúng góc
  const tr = bar(mI, 1, 1); g.add(tr);
  // viền séc đầu: khung chữ nhật cỡ k = 0 tại chỗ (cùng góc dưới neo với thẻ)
  const ghost = new THREE.Group(), L = 0.022;
  if (!col.level) for (const [x, y, sx, sy] of [[0, base, w, L], [0, 0.011, w, L], [-w / 2, base / 2, L, base], [w / 2, base / 2, L, base]]) { const b = bar(mG, sx, sy); b.position.set(x, y, 0); ghost.add(b); }
  ghost.position.z = d / 2 + 0.02; g.add(ghost);
  const set0 = g.set;
  g.set = (o = {}) => {
    const s = set0(o), a = Math.min(1, Math.max(0, o.appear ?? 1));
    inner.scale.x = s; inner.position.x = anchor * (w / 2) * (1 - s);
    const cx = inner.position.x, ww = w * s, hh = base * s * a, x0 = cx - ww * 0.4, x1 = cx + ww * 0.4, y0 = hh * (trend === 'rise' ? 0.66 : 0.8), y1 = trend === 'rise' ? hh * 0.9 : y0;
    tr.position.set((x0 + x1) / 2, (y0 + y1) / 2, d / 2 + 0.008); tr.rotation.z = Math.atan2(y1 - y0, x1 - x0);
    tr.scale.set(Math.hypot(x1 - x0, y1 - y0), 0.045, 1); tr.visible = a > 0.3;
    const gA = Math.min(1, Math.max(0, (s - 1.005) / 0.03)) * Math.min(1, a * 1.5);  // viền chỉ hiện khi séc đã lớn hơn séc đầu
    mI.opacity = mk.opacity; mG.opacity = gA * mk.opacity; ghost.visible = gA > 0.01;
    return s;
  };
  if (col.person) col.person.position.x -= anchor * w * (R20 - 1);                 // chỗ cho séc năm 20 (lớn về phía người)
  g.set({ k: 0 });
  return g;
}
