// F-17 · đối chứng luật màu: K2 của rnd-hybrid/v4/hist/k2/scene.js @ ba5d27f8, chỉ bỏ install() (lớp gắn qua khoá `cine` của spine.json).
// R&D v4 · K2 chương lịch sử KHÔNG vẽ người (2b): lưới 20 → 30 năm, VẬT THỂ SỐ LIỆU 3D trong thế giới đã lên ánh sáng (lớp cine, hồi 'dusk').
// Mỗi ô = một tháng trả góp, mỗi cột = một năm (12 ô). 20 cột đầu = giới hạn 1934 (National Housing Act §203(b)(3): "not to exceed twenty
// years", v2/CLAIMS.md s10/N7); 10 cột thêm (accent) = 1954 lên 30 năm (N5, s12). Ngôi nhà ở cuối hàng = món vay trả xong.
// Cột năm là tấm sổ cái (vân giấy CC0), nền đường (vân nhựa đường CC0) — vai trò vật liệu nhận theo màu (looks.js ROLES).
import * as THREE from 'three';
import { Stage, Camera, fonts, C } from '/toolkit/factory/world/core.js';
import { Studio, House, PALETTE } from '/toolkit/factory/world/lib3d.js';

export async function boot(res) {
  await fonts();
  const st = Stage(res), O = st.O, renderer = st.renderer, scene = new THREE.Scene(), { floor, key } = Studio(scene, { shadowBox: 14 });
  const poses = { k: { pos: [-3.2, 7.4, 12.5], tgt: [0.9, 0.0, -0.4], fov: 40, chart: 1 } };
  const CAM = Camera(poses, []);
  // sổ cái: 30 cột × 12 ô; cột = 0,42 m, ô 0,32 × 0,32, cao 0,06
  const N = 30, R = 12, P = 0.42, T = 0.3, x0 = -6.3;
  const slab = new THREE.Mesh(new THREE.BoxGeometry(N * P + 0.4, 0.12, R * 0.36 + 0.4), new THREE.MeshStandardMaterial({ color: '#E9E3D3', roughness: 0.9 }));
  slab.position.set(x0 + N * P / 2 - P / 2, 0.06, 0); slab.receiveShadow = slab.castShadow = true; scene.add(slab); slab.userData.checks = { role: 'mark', key: 'ledger' };
  const tile = new THREE.BoxGeometry(T, 0.07, T);
  const m20 = new THREE.MeshStandardMaterial({ color: '#C9C2B0', roughness: 0.7 }), m30 = new THREE.MeshStandardMaterial({ color: C.accent, roughness: 0.6, emissive: new THREE.Color(C.accent), emissiveIntensity: 0.15 });
  const grid = new THREE.Group(); grid.userData.checks = { role: 'series', key: 'months' }; scene.add(grid);
  for (let c = 0; c < N; c++) for (let r = 0; r < R; r++) {
    const m = new THREE.Mesh(tile, c < 20 ? m20 : m30); m.position.set(x0 + c * P, 0.155, (r - (R - 1) / 2) * 0.36); m.castShadow = m.receiveShadow = true; grid.add(m);
  }
  const wall = new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.55, R * 0.36 + 0.3), new THREE.MeshStandardMaterial({ color: '#8C8C88', roughness: 0.6 }));   // vách 20 năm (gỗ)
  wall.position.set(x0 + 19.5 * P, 0.38, 0); wall.castShadow = true; scene.add(wall);
  const house = House({ w: 1.7 }); house.position.set(x0 + N * P + 1.4, 0, -0.2); house.rotation.y = -0.35; scene.add(house);
  function frame(t) {
    const pose = CAM.apply(t), cam = CAM.cam;
    key.target.position.set(0, 0, 0);
    renderer.render(scene, cam);
    const log = O.begin(t, pose.chart, cam);
    const [ax, ay] = O.toScreen(x0 - P / 2, 0.2, R * 0.18 + 0.25), [bx, by] = O.toScreen(x0 + 19.5 * P, 0.2, R * 0.18 + 0.25), [cx, cy] = O.toScreen(x0 + (N - 0.5) * P, 0.2, R * 0.18 + 0.25);
    const [tx1, ty1] = O.toScreen(x0 + 9.5 * P, 0.6, -R * 0.18 - 0.2), [tx2, ty2] = O.toScreen(x0 + 24.5 * P, 0.6, -R * 0.18 - 0.2);
    O.text('1934: up to 20 years', tx1, ty1 - 40, 56, { kind: 'number', align: 'center', plate: '#0B0E13', plateA: 0.72 });
    O.text('1954: up to 30 years', tx2 + 40, ty2 - 110, 56, { kind: 'number', align: 'center', color: '#9DC0FF', plate: '#0B0E13', plateA: 0.72 });
    O.text('one tile = one monthly payment', ax + 10, ay + 70, 44, { kind: 'title', plate: '#0B0E13', plateA: 0.6 });
    O.chrome({ src: 'National Housing Act, 1934 · FHA, 1954', hist: true });
    st.compose(); log.camMoving = false; return log;
  }
  return { canvas: st.out, frame };
}
