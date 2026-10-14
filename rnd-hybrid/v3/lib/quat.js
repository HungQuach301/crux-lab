// R&D vòng 3 · H4′: người lớn 3D có xương — Quaternius Universal Base Characters [Standard] (CC0) + Universal Animation Library [Standard] (CC0, 43 clip).
// Bản Standard miễn phí CHỈ có thân "Superhero" (nam/nữ); không mua bản trả phí. Giảm vẻ "siêu anh hùng" bằng:
//   - trang phục theo vùng xương (áo khoác, sơ mi, cà vạt, quần, giày, váy dài) — màu đỉnh, không texture;
//   - pháp tuyến vùng áo làm mượt theo trục xương (toon + nét mực không vẽ cơ ngực/bụng), thân áo phồng nhẹ;
//   - váy dài 1930 (khối tròn xoay gắn xương chậu), mũ phớt gắn xương đầu, tóc Quaternius gắn xương đầu.
// Mặt: drawFace (rig.js) CHIẾU lên bề mặt đầu cong trong shader (toạ độ chiếu tính ở tư thế gốc, đi theo xương) — không dán tấm phẳng.
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import * as SkeletonUtils from 'three/addons/utils/SkeletonUtils.js';
import { drawFace } from '/rnd-hybrid/cutout/rig.js';
import { TOON, toonMat, fedora } from '/rnd-hybrid/v3/lib/kenney.js';

const BASE = '/rnd-hybrid/v3/assets/quaternius/';
const loader = new GLTFLoader(), cache = new Map();
const load = (p) => { if (!cache.has(p)) cache.set(p, loader.loadAsync(BASE + p)); return cache.get(p); };
let CLIPS = null;
export async function clips() { if (!CLIPS) CLIPS = Object.fromEntries((await load('ual/UAL1_Standard.glb')).animations.map((c) => [c.name, c])); return CLIPS; }

export const SKIN = { light: '#E9C3A0', medium: '#C98E66', tan: '#A9714C', dark: '#6E4630', deep: '#4A2E22' };
export const HAIR = { black: '#1E1A17', brown: '#4A3222', auburn: '#6E3A22', grey: '#8A8A88', blond: '#B89B62' };
export const OUT = {   // trang phục 1930 (kênh: không màu chói)
  charcoal: { coat: '#3E434D', shirt: '#E6DEC8', tie: '#7A3B33', trousers: '#2C3038', shoes: '#1C1A18' },
  brown: { coat: '#6B5644', shirt: '#E9E1CC', tie: '#2F3B52', trousers: '#4C3D31', shoes: '#2A1E16' },
  navy: { coat: '#2F3B52', shirt: '#E6DEC8', tie: '#8A6F5A', trousers: '#232C3D', shoes: '#1C1A18' },
  grey: { coat: '#6E7380', shirt: '#EDE4CF', tie: '#5A4330', trousers: '#4F535C', shoes: '#22201E' },
  tweed: { coat: '#7C6A52', shirt: '#E9E1CC', tie: '#3E4A3A', trousers: '#5C4E3E', shoes: '#2A1E16' },
  dressPlum: { coat: '#6F5A78', shirt: '#E9E1CC', dress: '#5E4E6A', shoes: '#2A1E16' },
  dressGreen: { coat: '#4E6B5E', shirt: '#E9E1CC', dress: '#3A5146', shoes: '#2A1E16' },
  dressNavy: { coat: '#3D4A66', shirt: '#E9E1CC', dress: '#2F3B52', shoes: '#1C1A18' },
};
const REG = (b) => /^(Head|neck_01)$/.test(b) ? 'head' : /^(hand|index|middle|pinky|ring|thumb)/.test(b) ? 'hand' : /^(foot|ball)/.test(b) ? 'foot'
  : /^(thigh|calf)/.test(b) ? 'leg' : /^(upperarm|lowerarm)/.test(b) ? 'arm' : 'torso';

// texture mặt (trong suốt): nét rig.js + má hồng; một texture cho mỗi cảm xúc
const FT = new Map();
function faceTex(expr) {
  if (FT.has(expr)) return FT.get(expr);
  const c = document.createElement('canvas'); c.width = c.height = 512; const g = c.getContext('2d');
  g.translate(256, 256 + 150); g.scale(3.1, 3.1);
  // quầng sáng mảnh quanh nét (đọc được trên da sẫm), rồi nét mực
  const halo = document.createElement('canvas'); halo.width = halo.height = 512; const hg = halo.getContext('2d'); hg.translate(256, 256 + 150); hg.scale(3.1, 3.1); drawFace(hg, expr, false);
  hg.setTransform(1, 0, 0, 1, 0, 0); hg.globalCompositeOperation = 'source-in'; hg.fillStyle = 'rgba(245,236,220,0.55)'; hg.fillRect(0, 0, 512, 512);
  g.setTransform(1, 0, 0, 1, 0, 0); for (let k = 0; k < 8; k++) { const a = k / 8 * Math.PI * 2; g.drawImage(halo, Math.cos(a) * 5, Math.sin(a) * 5); }
  g.translate(256, 256 + 150); g.scale(3.1, 3.1); drawFace(g, expr, false);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; FT.set(expr, t); return t;
}
// vật liệu toon + chiếu mặt (attribute faceUv/faceW, uniform faceMap)
function bodyMat(chest) {
  const m = toonMat({ vertexColors: true }), u = { faceMap: { value: faceTex('neutral') }, chestMap: { value: chest } };
  m.onBeforeCompile = (sh) => { sh.uniforms.faceMap = u.faceMap; sh.uniforms.chestMap = u.chestMap;
    sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\nattribute vec2 faceUv; attribute float faceW; attribute vec2 chestUv; varying vec2 vFaceUv; varying float vFaceW; varying vec2 vChestUv;')
      .replace('#include <begin_vertex>', '#include <begin_vertex>\nvFaceUv = faceUv; vFaceW = faceW; vChestUv = chestUv;');
    sh.fragmentShader = sh.fragmentShader.replace('#include <common>', '#include <common>\nuniform sampler2D faceMap, chestMap; varying vec2 vFaceUv; varying float vFaceW; varying vec2 vChestUv;\nfloat inside(vec2 q){ return step(0., q.x) * step(q.x, 1.) * step(0., q.y) * step(q.y, 1.); }')
      .replace('#include <color_fragment>', '#include <color_fragment>\n{ vec4 c = texture2D(chestMap, vChestUv); diffuseColor.rgb = mix(diffuseColor.rgb, c.rgb, c.a * inside(vChestUv));\n  vec4 f = texture2D(faceMap, vFaceUv); diffuseColor.rgb = mix(diffuseColor.rgb, f.rgb, f.a * inside(vFaceUv) * clamp(vFaceW, 0., 1.)); }'); };
  m.customProgramCacheKey = () => 'crux-face2'; m.userData.u = u; return m;
}
// ngực: sơ mi chữ V + cà vạt + ve áo + cúc (nét mực), trong suốt ngoài các hình đó
const CT = new Map();
function chestTex(O) {
  const key = JSON.stringify(O); if (CT.has(key)) return CT.get(key);
  const c = document.createElement('canvas'); c.width = 512; c.height = 512; const g = c.getContext('2d');
  if (O.dress) { g.fillStyle = O.shirt; g.beginPath(); g.moveTo(196, 0); g.lineTo(316, 0); g.lineTo(256, 70); g.closePath(); g.fill();   // cổ váy
    g.strokeStyle = '#15171C'; g.lineWidth = 6; g.beginPath(); g.moveTo(196, 0); g.lineTo(256, 70); g.lineTo(316, 0); g.stroke();
    g.fillStyle = '#15171C'; for (const y of [120, 200, 280]) { g.beginPath(); g.arc(256, y, 9, 0, 7); g.fill(); } }
  else { g.fillStyle = O.shirt; g.beginPath(); g.moveTo(170, 0); g.lineTo(342, 0); g.lineTo(256, 250); g.closePath(); g.fill();
    if (O.tie) { g.fillStyle = O.tie; g.beginPath(); g.moveTo(240, 0); g.lineTo(272, 0); g.lineTo(266, 40); g.lineTo(280, 215); g.lineTo(256, 245); g.lineTo(232, 215); g.lineTo(246, 40); g.closePath(); g.fill(); }
    g.strokeStyle = '#15171C'; g.lineWidth = 7; g.beginPath(); g.moveTo(150, 0); g.lineTo(256, 270); g.lineTo(362, 0); g.stroke();   // ve áo
    g.lineWidth = 4; g.beginPath(); g.moveTo(170, 0); g.lineTo(206, 120); g.moveTo(342, 0); g.lineTo(306, 120); g.stroke();
    g.fillStyle = '#15171C'; for (const y of [330, 420]) { g.beginPath(); g.arc(256, y, 10, 0, 7); g.fill(); } }
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; CT.set(key, t); return t;
}

// một người: { root, face(expr), pose(clip, t, {arm}) }
export async function adult({ sex = 'm', skin = 'light', hair = 'SimpleParted', hairColor = 'brown', outfit = 'charcoal', hat = true, hatColor = null, beard = false, height = null } = {}) {
  const src = await load(`ubc/Superhero_${sex === 'm' ? 'Male' : 'Female'}_FullBody.gltf`), CL = await clips(), O = OUT[outfit];
  const root = SkeletonUtils.clone(src.scene); root.updateMatrixWorld(true);
  let body = null; const hide = [];
  root.traverse((n) => { if (n.isSkinnedMesh) { if (n.material.name && /Superhero/.test(n.material.name)) body = n; else hide.push(n); } });
  hide.forEach((n) => (n.visible = false));   // mắt + lông mày gốc: thay bằng mặt vẽ
  const geo = body.geometry = body.geometry.clone(), pos = geo.attributes.position, nrm = geo.attributes.normal, si = geo.attributes.skinIndex, sw = geo.attributes.skinWeight;
  const bones = body.skeleton.bones, bb = new THREE.Box3().setFromBufferAttribute(pos), H = bb.max.y - bb.min.y, cx = (bb.max.x + bb.min.x) / 2;
  // khung đầu (tư thế gốc, toạ độ lưới) để chiếu mặt
  const region = new Array(pos.count), dom = new Array(pos.count), hb = new THREE.Box3();
  for (let i = 0; i < pos.count; i++) { let bi = 0, bw = -1; for (let k = 0; k < 4; k++) { const w = sw.getComponent(i, k); if (w > bw) { bw = w; bi = si.getComponent(i, k); } }
    dom[i] = bones[bi].name; region[i] = REG(dom[i]); if (dom[i] === 'Head') hb.expandByPoint(new THREE.Vector3().fromBufferAttribute(pos, i)); }
  const hs = hb.getSize(new THREE.Vector3()), hc = hb.getCenter(new THREE.Vector3());
  const col = new Float32Array(pos.count * 3), fuv = new Float32Array(pos.count * 2), fw = new Float32Array(pos.count), cuv = new Float32Array(pos.count * 2).fill(-1);
  const C = new THREE.Color(), v = new THREE.Vector3(), n = new THREE.Vector3(), set = (i, hex) => { C.set(hex); col.set([C.r, C.g, C.b], i * 3); };
  // lát thân theo chiều cao (2 % H): tâm z và bán kính x/z lớn nhất của các đỉnh thân → khối áo trơn
  const SL = 50, sl = Array.from({ length: SL }, () => ({ z: 0, n: 0, rx: 0, rz: 0 })), TOR = /^(pelvis|spine_0[123])$/;
  const sIdx = (y) => Math.min(SL - 1, Math.max(0, Math.floor((y - bb.min.y) / H * SL)));
  for (let i = 0; i < pos.count; i++) if (TOR.test(dom[i])) { v.fromBufferAttribute(pos, i); const q = sl[sIdx(v.y)]; q.z += v.z; q.n++; }
  for (const q of sl) q.z = q.n ? q.z / q.n : 0;
  for (let i = 0; i < pos.count; i++) if (TOR.test(dom[i])) { v.fromBufferAttribute(pos, i); const q = sl[sIdx(v.y)]; q.rx = Math.max(q.rx, Math.abs(v.x - cx)); q.rz = Math.max(q.rz, Math.abs(v.z - q.z)); }
  const hr = hs.clone().multiplyScalar(0.5), hcE = hc.clone().add(new THREE.Vector3(0, -hs.y * 0.04, -hs.z * 0.06)), top = hc.y + hs.y * 0.12, Hw = hs.y * 0.6;
  const chestTop = bb.min.y + H * 0.845, chestH = H * 0.3;
  for (let i = 0; i < pos.count; i++) {
    v.fromBufferAttribute(pos, i); n.fromBufferAttribute(nrm, i); const y = (v.y - bb.min.y) / H, r = region[i];
    let c = SKIN[skin];
    if (r === 'foot') c = O.shoes; else if (r === 'leg') c = O.dress ? (y > 0.1 ? O.dress : SKIN[skin]) : O.trousers;
    else if (r === 'arm') c = O.coat; else if (r === 'torso') c = O.dress && y < 0.55 ? O.dress : O.coat;
    else if (dom[i] === 'neck_01' && y < 0.845) c = O.shirt;
    set(i, c);
    // thân: kéo về elip của lát (giấu cơ ngực/bụng), pháp tuyến theo elip
    if (TOR.test(dom[i])) { const q = sl[sIdx(v.y)], dx = (v.x - cx) / (q.rx || 1), dz = (v.z - q.z) / (q.rz || 1), d = Math.hypot(dx, dz) || 1;
      const tx = cx + dx / d * q.rx * 1.02, tz = q.z + dz / d * q.rz * 1.04, k = 0.85; v.x += (tx - v.x) * k; v.z += (tz - v.z) * k;
      n.set(dx / d / (q.rx || 1), n.y * 0.3, dz / d / (q.rz || 1)).normalize(); pos.setXYZ(i, v.x, v.y, v.z); nrm.setXYZ(i, n.x, n.y, n.z);
    }
    if ((r === 'torso' || dom[i] === 'neck_01') && n.z > 0.05 && v.y < chestTop && v.y > chestTop - chestH) { const q = sl[sIdx(Math.min(v.y, chestTop - H * 0.04))];
      cuv[i * 2] = (v.x - cx) / ((q.rx || H * 0.1) * 1.6) + 0.5; cuv[i * 2 + 1] = 1 - (chestTop - v.y) / chestH; }
    // mặt: phía trước đầu kéo về mặt elip trơn (bỏ mũi/môi/hốc mắt điêu khắc) rồi chiếu nét rig.js
    fuv[i * 2] = -1; fuv[i * 2 + 1] = -1; fw[i] = 0;
    if (dom[i] === 'Head') { const e = v.clone().sub(hcE).divide(hr), d = e.length() || 1, p = e.clone().divideScalar(d).multiply(hr).add(hcE);
      const wF = THREE.MathUtils.smoothstep(n.z, -0.1, 0.35) * THREE.MathUtils.smoothstep(v.y, hc.y - hs.y * 0.55, hc.y - hs.y * 0.3);
      if (wF > 0) { v.lerp(p, wF * 0.92); const ne = p.clone().sub(hcE).divide(hr).divide(hr).normalize(); n.lerp(ne, wF).normalize(); pos.setXYZ(i, v.x, v.y, v.z); nrm.setXYZ(i, n.x, n.y, n.z); }
      fuv[i * 2] = (v.x - hc.x) / (hs.x * 0.78) + 0.5; fuv[i * 2 + 1] = 1 - (top - v.y) / Hw; fw[i] = THREE.MathUtils.smoothstep(n.z, 0.1, 0.4); }
  }
  geo.setAttribute('color', new THREE.BufferAttribute(col, 3)); geo.setAttribute('faceUv', new THREE.BufferAttribute(fuv, 2)); geo.setAttribute('faceW', new THREE.BufferAttribute(fw, 1)); geo.setAttribute('chestUv', new THREE.BufferAttribute(cuv, 2));
  const mat = bodyMat(chestTex(O)); body.material = mat; body.castShadow = body.receiveShadow = true; body.frustumCulled = false;
  // tóc / râu: bản "Origin at 0" cùng gốc toạ độ với thân → gắn vào xương đầu bằng nghịch đảo ma trận xương ở tư thế gốc
  const head = bones.find((b) => b.name === 'Head'), headInv = new THREE.Matrix4().copy(head.matrixWorld).invert();
  const attach = async (file, color) => { const g = await load('ubc/hair/' + file + '.gltf'); const h = g.scene.clone(true); h.updateMatrixWorld(true);
    h.traverse((m) => { if (m.isMesh) { m.material = toonMat({ color }); m.castShadow = true; } });
    const holder = new THREE.Group(); holder.matrixAutoUpdate = false; holder.matrix.copy(headInv).multiply(root.matrixWorld); holder.add(h); head.add(holder); return holder; };
  if (hair) await attach('Hair_' + (hat && hair !== 'Buns' && hair !== 'Long' ? 'Buzzed' : hair), HAIR[hairColor]);   // đội mũ: tóc ngắn (không lòi qua mũ)
  if (beard) await attach('Hair_Beard', HAIR[hairColor]);
  if (hat) { const f = fedora(hatColor || O.trousers || '#2C3038'); const top = hb.max.clone(); top.x = hc.x; top.z = hc.z;
    const holder = new THREE.Group(); holder.matrixAutoUpdate = false; holder.matrix.copy(headInv).multiply(root.matrixWorld); const s = hs.x * 1.05;
    f.scale.setScalar(s * 1.08); f.position.set(hc.x, hb.max.y - hs.y * 0.3, hc.z - hs.z * 0.06); holder.add(f); head.add(holder); }
  // váy dài 1930: khối tròn xoay gắn xương chậu
  if (O.dress) { const pel = bones.find((b) => b.name === 'pelvis'), pts = []; for (let k = 0; k <= 8; k++) { const t = k / 8; pts.push(new THREE.Vector2(H * (0.095 + 0.06 * t * t), -H * 0.5 * t)); }
    const skirt = new THREE.Mesh(new THREE.LatheGeometry(pts, 20), toonMat({ color: O.dress })); skirt.castShadow = true;
    const holder = new THREE.Group(); holder.matrixAutoUpdate = false; holder.matrix.copy(new THREE.Matrix4().copy(pel.matrixWorld).invert()).multiply(root.matrixWorld);
    skirt.position.set(cx, bb.min.y + H * 0.56, (bb.max.z + bb.min.z) / 2); holder.add(skirt); pel.add(holder); }
  const wrap = new THREE.Group(); wrap.add(root); const target = height || (sex === 'm' ? 1.78 : 1.66); root.scale.multiplyScalar(target / H);
  const mixer = new THREE.AnimationMixer(root); let cur = null;
  return { root: wrap, H: target,
    face(expr) { mat.userData.u.faceMap.value = faceTex(expr); },
    pose(name, t = 0, { arm = null } = {}) { const key = name + '|' + arm;
      if (cur !== key) { mixer.stopAllAction(); const base = CL[name].clone(); if (arm) base.tracks = base.tracks.filter((tr) => !/(clavicle_r|upperarm_r|lowerarm_r|hand_r|_r\.)/.test(tr.name));
        mixer.clipAction(base).play(); if (arm) { const a = CL[arm].clone(); a.tracks = a.tracks.filter((tr) => /(clavicle_r|upperarm_r|lowerarm_r|hand_r|_r\.)/.test(tr.name)); mixer.clipAction(a).play(); } cur = key; }
      mixer.setTime(t); },
  };
}
