// Tập 5 · VẬT THỂ MỚI ĐỀ XUẤT (C3, D-010 quy tắc 4) — chưa vào lib3d.js (không sửa toolkit trong phiên này). Cùng gen kênh: low-poly, màu kênh.
//  N1 Calendar  — lịch trả nợ: mỗi trang = một kỳ trả; lật trang = một tháng trôi qua; ngừng lật = "dừng đồng hồ". Ở thế giới không có số.
//  N2 Bars      — cột phát lại: mỗi tháng mua một cột mảnh đứng trên sàn; chiều cao = số tháng tới 80 % trên giấy (không phải tiền).
//  N3 foldPaths — chuyển cảnh: đường phát lại của mỗi tháng mua gập thành cột của chính nó (thời gian nằm ngang → chiều cao).
import * as THREE from 'three';
import { PALETTE } from '/toolkit/factory/world/lib3d.js';

const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.85, transparent: true, ...o });

// ---------------------------------------------------------------- N1 lịch (bảng đứng, xấp trang, gáy vòng; một trang lật quanh mép trên)
export function Calendar({ w = 1.0, h = 1.25, tab = null } = {}) {
  const g = new THREE.Group(), d = 0.12;
  const add = (m, x, y, z) => { m.position.set(x, y, z); m.castShadow = m.receiveShadow = true; g.add(m); return m; };
  add(new THREE.Mesh(new THREE.BoxGeometry(w * 1.08, h * 1.06, 0.05), mat('#3A4250')), 0, h / 2, -0.04);           // bảng
  const block = add(new THREE.Mesh(new THREE.BoxGeometry(w, h * 0.92, d), mat('#EDE8DC')), 0, h * 0.46, d / 2);   // xấp trang còn lại
  const head = add(new THREE.Mesh(new THREE.BoxGeometry(w, h * 0.16, d + 0.01), mat('#5B6573')), 0, h * 0.86, d / 2);   // dải đầu trang (không chữ)
  for (const x of [-w * 0.3, 0, w * 0.3]) add(new THREE.Mesh(new THREE.TorusGeometry(0.05, 0.015, 6, 12), mat('#C9D1DC')), x, h * 0.95, d + 0.01);
  // trang đang lật: bản lề ở mép trên
  const hinge = new THREE.Group(); hinge.position.set(0, h * 0.92, d + 0.02); g.add(hinge);
  const page = new THREE.Mesh(new THREE.BoxGeometry(w, h * 0.92, 0.012), mat('#F6F2E8')); page.position.set(0, -h * 0.46, 0); page.castShadow = true; hinge.add(page);
  let tabM = null;
  if (tab) { tabM = new THREE.Mesh(new THREE.BoxGeometry(w * 0.34, h * 0.14, 0.016), mat(tab, { emissive: new THREE.Color(tab), emissiveIntensity: 0.25 })); tabM.position.set(w * 0.24, -h * 0.2, 0.012); hinge.add(tabM); }
  g.userData = { w, h, block, head, page, hinge, tab: tabM, faceY: h * 0.5, faceZ: d + 0.03 };
  // flip ∈ [0,1): tiến độ lật của trang hiện tại; pages: số trang còn lại (0–1, độ dày xấp)
  g.set = ({ flip = 0, pages = 1, glow = 0 } = {}) => {
    const f = Math.max(0, Math.min(1, flip));
    hinge.rotation.x = -Math.PI * 0.92 * (f * f * (3 - 2 * f));
    page.material.opacity = f < 0.75 ? 1 : 1 - (f - 0.75) / 0.25; if (tabM) tabM.material.opacity = page.material.opacity;
    block.scale.z = 0.35 + 0.65 * pages; block.position.z = d / 2 * block.scale.z;
    head.material.emissive = new THREE.Color(glow > 0 ? PALETTE.warn : '#000000'); head.material.emissiveIntensity = 0.9 * glow;
  };
  return g;
}

// ---------------------------------------------------------------- N2 cột phát lại (InstancedMesh; đứng trên sàn y = 0, mặt phẳng z cố định)
export function Bars({ n = 320, w = 0.028, d = 0.12 } = {}) {
  const geo = new THREE.BoxGeometry(1, 1, 1); geo.translate(0, 0.5, 0);
  const m = new THREE.MeshStandardMaterial({ roughness: 0.6, transparent: true, emissive: new THREE.Color('#000000') });
  const mesh = new THREE.InstancedMesh(geo, m, n); mesh.frustumCulled = false; mesh.castShadow = mesh.receiveShadow = true;
  const M = new THREE.Matrix4(), col = new THREE.Color(), hide = new THREE.Matrix4().makeScale(0, 0, 0);
  // items: [{x, h, color}] — chiều cao thế giới; phần tử thiếu thì ẩn
  mesh.set = (items, ww = w) => {
    for (let i = 0; i < n; i++) {
      const it = items[i];
      if (!it || it.h <= 0.001) { mesh.setMatrixAt(i, hide); continue; }
      M.makeScale(ww * (it.wMul || 1), it.h, d).setPosition(it.x, it.y || 0, it.z || 0); mesh.setMatrixAt(i, M);
      col.set(it.color || PALETTE.ink); mesh.setColorAt(i, col);
    }
    mesh.instanceMatrix.needsUpdate = true; if (mesh.instanceColor) mesh.instanceColor.needsUpdate = true;
  };
  return mesh;
}

// ---------------------------------------------------------------- N3 gập đường → cột
// path: [[x,y]…] đường phát lại của một tháng mua (từ lúc mua tới khi chạm 80 %); bar: {x, y0, h} cột đích.
// u = 0: đúng đường; u = 1: đoạn thẳng đứng trùng cột. Điểm thứ k đi tới vị trí k/(n−1) dọc cột (thời gian nằm ngang → chiều cao).
export function foldPath(path, bar, u) {
  const n = path.length, e = 1 - Math.pow(1 - u, 3);   // bắt đầu nhanh: chuyển động thấy ngay ở từ khoá
  return path.map(([x, y], k) => { const f = n > 1 ? k / (n - 1) : 1; return [x + (bar.x - x) * e, y + (bar.y0 + bar.h * f - y) * e]; });
}
