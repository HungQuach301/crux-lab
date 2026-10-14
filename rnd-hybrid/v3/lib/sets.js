// R&D vòng 3 · bố cục chung của 3 cảnh mẫu (dùng cho cả H4 và H3 để so cùng khuôn hình):
//   S1 (t ∈ [0,1))   1930, đám đông trước ngân hàng đóng cửa — gốc toạ độ
//   S2 (t ∈ [1,2))   1934, người vay ký hợp đồng FHA — phòng ở x = 60
//   S3 (t ∈ [2,3))   lưới trả dần 20 → 30 năm — sàn ở x = 120
//   ORBIT (t ∈ [10,16)) máy lượn chậm 25° quanh Walt ở S1, Walt ≥ 25 % chiều cao khung
import * as THREE from 'three';

export const X2 = 60, X3 = 120;
export const WALT = [2.4, 0.16, -3.6];
export const CAMS = {
  S1: { pos: [8.6, 1.7, 3.8], tgt: [0.8, 2.0, -8.0], fov: 38 },
  S2: { pos: [X2 + 0.9, 1.75, 2.6], tgt: [X2 + 0.3, 0.95, -1.4], fov: 36 },
  S3: { pos: [X3 + 1.6, 3.4, 8.8], tgt: [X3 + 0.4, 0.8, -1.2], fov: 44 },
};
export function orbitCam(t) {   // t ∈ [10,16): góc −12° → +13°, ease
  const k = Math.min(1, Math.max(0, (t - 10) / 6)), e = k * k * (3 - 2 * k), a = THREE.MathUtils.degToRad(-12 + 25 * e), r = 4.6;
  const c = new THREE.Vector3(WALT[0], 1.05, WALT[2]);
  return { pos: [c.x + Math.sin(a + 0.55) * r, 1.45, c.z + Math.cos(a + 0.55) * r], tgt: [c.x - 0.3, 1.05, c.z - 0.6], fov: 34 };
}
export const which = (t) => (t >= 10 ? 'ORBIT' : t >= 2 ? 'S3' : t >= 1 ? 'S2' : 'S1');
// đám đông S1: [x, z, quay(độ), giới, trang phục, mũ, clip, cảm xúc]
export const CROWD = [
  [-3.6, -8.6, 10, 'male-b', 'brown', 1, 'idle', 'worried'], [-2.4, -9.2, 0, 'female-a', 'dress', 0, 'idle', 'sad'], [-1.2, -8.4, -8, 'male-c', 'grey', 1, 'emote-no', 'worried'],
  [0.2, -9.0, 5, 'male-d', 'navy', 1, 'idle', 'shocked'], [1.4, -8.2, -15, 'female-c', 'dress2', 0, 'idle', 'worried'], [2.8, -9.1, 0, 'male-e', 'charcoal', 1, 'holding-right', 'sad'],
  [4.0, -8.3, -20, 'male-f', 'brown', 1, 'idle', 'worried'], [-3.0, -6.8, 20, 'female-d', 'dress', 0, 'idle', 'worried'], [-0.6, -6.6, 10, 'male-b', 'navy', 1, 'emote-no', 'sad'],
  [1.0, -6.2, -10, 'female-e', 'dress2', 0, 'idle', 'shocked'], [4.6, -6.4, -30, 'male-c', 'grey', 1, 'idle', 'worried'], [-4.6, -5.6, 30, 'female-f', 'dress', 0, 'idle', 'sad'],
];
// lưới trả dần: mỗi cột = một năm, 12 ô = 12 kỳ trả; cao ô ∝ khoản trả tháng (minh hoạ, không ghi số)
export function payment(n, r = 0.05 / 12) { const N = n * 12; return r / (1 - Math.pow(1 + r, -N)); }   // trả dần đều (minh hoạ: lãi 5 %/năm)
