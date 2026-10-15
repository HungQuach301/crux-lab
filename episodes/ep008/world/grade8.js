// Tập 8 · M4 MÀU THEO HỒI (tổng kết Tập 7 §4d; bảng màu hồi khai ở preprod/TAM-NHIN.md §2 và beats.md "Act palettes" — gu đã có trong beats C2,
// không thêm màu ngoài token kênh): tông ánh sáng + nền của thế giới theo GIỜ TẬP. Chỉ chạm ánh sáng/nền (không đổi màu vật dữ liệu: buyer = lit,
// renter = warn giữ nguyên). Animatic xám (M2) không dùng.
//   cold open + hồi 1: xanh lạnh · hồi 2: ấm dần, rơi về xám ở June 2006 (S17–S19), ấm lại (S20–S22) · hồi 3: trung tính sáng · giới hạn + kết: trung
//   tính chạng vạng, đèn Nina là nguồn ấm duy nhất.
import * as THREE from 'three';

export const TONES = {
  cold: { hemi: '#BCD0EE', hemiI: 0.9, key: '#DDE8FF', bg: '#0B1018' },
  warm: { hemi: '#EBD9BE', hemiI: 0.95, key: '#FFE3BC', bg: '#13100C' },
  grey: { hemi: '#B4B7BC', hemiI: 0.8, key: '#D6D8DB', bg: '#0F1012' },
  neutral: { hemi: '#D2D7DE', hemiI: 0.95, key: '#FFF2E2', bg: '#0E1116' },
  dusk: { hemi: '#8B97AD', hemiI: 0.7, key: '#C4BFD4', bg: '#090C11' },
};
// [giờ tập (s), tông] — mốc = đầu cảnh trên out/factory/timeline.json (13/10): S08 184,8 · S09 ≈ 224 · S16 ≈ 333 · S17 349,5 · S20 ≈ 394 · S23 450,9 · S31 579,9
export const KEYS = [[0, 'cold'], [184.0, 'cold'], [186.0, 'warm'], [340.0, 'warm'], [348.5, 'grey'], [393.0, 'grey'], [397.0, 'warm'], [450.0, 'warm'],
  [452.0, 'neutral'], [578.0, 'neutral'], [581.0, 'dusk'], [700, 'dusk']];
const c1 = new THREE.Color(), c2 = new THREE.Color();
const mixHex = (a, b, x) => c1.set(a).lerp(c2.set(b), x).clone();
export function toneAt(T) {
  let k = 0; for (let i = 0; i < KEYS.length - 1; i++) if (T >= KEYS[i][0]) k = i;
  const [ta, a] = KEYS[k], [tb, b] = KEYS[k + 1], x = Math.min(1, Math.max(0, (T - ta) / Math.max(1e-6, tb - ta))), A = TONES[a], B = TONES[b];
  return { hemi: mixHex(A.hemi, B.hemi, x), hemiI: A.hemiI + (B.hemiI - A.hemiI) * x, key: mixHex(A.key, B.key, x), bg: mixHex(A.bg, B.bg, x), name: x < 0.5 ? a : b };
}
// áp vào cảnh: HemisphereLight đầu tiên + đèn chính (key) + nền + sương
export function grade(scene, key, T) {
  const g = toneAt(T); let hemi = null; scene.traverse((o) => { if (!hemi && o.isHemisphereLight) hemi = o; });
  if (hemi) { hemi.color.copy(g.hemi); hemi.intensity = g.hemiI; }
  if (key) key.color.copy(g.key);
  scene.background = g.bg; if (scene.fog) scene.fog.color.copy(g.bg);
  return g.name;
}
