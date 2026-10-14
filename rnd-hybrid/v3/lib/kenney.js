// R&D vòng 3 · H4: người 3D có xương từ Kenney "Mini Characters" (CC0) + đạo cụ Kenney (CC0), nạp bằng GLTFLoader của three (vendor nhà máy).
//  - màu: đọc colormap → màu đỉnh (vertexColors) → đổi màu theo bảng trang phục 1930 (giữ da, tóc tối); vật liệu toon 3–4 bậc
//  - mũ phớt (khối tự dựng) gắn vào xương đầu; mặt = decal canvas vẽ bằng drawFace của rig.js, đổi theo cảm xúc
//  - chuyển động: clip có sẵn trong GLB (idle, walk, sit, interact-right, emote-yes/no, holding-right…), mixer.setTime(t) → tất định
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import * as SkeletonUtils from 'three/addons/utils/SkeletonUtils.js';
import { drawFace } from '/rnd-hybrid/cutout/rig.js';

const BASE = '/rnd-hybrid/v3/assets/kenney/';
const loader = new GLTFLoader();
const cache = new Map();
export async function glb(path) { if (!cache.has(path)) cache.set(path, loader.loadAsync(BASE + path)); return cache.get(path); }

// gradient toon 4 bậc (NearestFilter) — dùng chung cho người, vật, nhà
export const TOON = (() => { const d = new Uint8Array([70, 140, 205, 255]); const t = new THREE.DataTexture(d, 4, 1, THREE.RedFormat); t.minFilter = t.magFilter = THREE.NearestFilter; t.generateMipmaps = false; t.needsUpdate = true; return t; })();
export const toonMat = (o = {}) => new THREE.MeshToonMaterial({ gradientMap: TOON, ...o });

// đọc ảnh colormap một lần → hàm lấy màu theo uv
const pix = new Map();
async function sampler(url) {
  if (!pix.has(url)) pix.set(url, (async () => { const im = new Image(); im.src = url; await im.decode(); const c = document.createElement('canvas'); c.width = im.width; c.height = im.height;
    const g = c.getContext('2d'); g.drawImage(im, 0, 0); const d = g.getImageData(0, 0, c.width, c.height).data;
    return (u, v) => { const x = Math.min(c.width - 1, Math.max(0, Math.floor(u * c.width))), y = Math.min(c.height - 1, Math.max(0, Math.floor(v * c.height))), i = (y * c.width + x) * 4; return [d[i], d[i + 1], d[i + 2]]; }; })());
  return pix.get(url);
}
// bảng màu chính của Kenney (đo từ colormap) → nhóm
const SW = { dark: [56, 56, 61], orange: [255, 126, 68], slate: [79, 82, 96], brownSkin: [176, 96, 65], lavender: [160, 168, 201], blue: [103, 148, 217], purple: [168, 120, 232],
  grey: [134, 139, 161], skinL: [253, 228, 199], red: [207, 83, 79], pink: [243, 120, 240], white: [255, 255, 255], green: [97, 203, 139], ice: [208, 232, 255],
  skinM: [242, 191, 153], skinT: [241, 151, 108], yellow: [255, 192, 68] };
const near = (c) => { let best = null, bd = 1e9; for (const [k, s] of Object.entries(SW)) { const d = (c[0] - s[0]) ** 2 + (c[1] - s[1]) ** 2 + (c[2] - s[2]) ** 2; if (d < bd) { bd = d; best = k; } } return best; };
const hex = (h) => { const n = parseInt(h.slice(1), 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; };
// trang phục 1930: mọi màu quần áo → dạ xám/nâu/xanh than, áo sơ mi kem; da + tóc giữ
export const OUTFIT = {
  charcoal: { coat: '#3E434D', coat2: '#2C3038', shirt: '#E6DEC8', accent: '#7A3B33' },
  brown: { coat: '#6B5644', coat2: '#4C3D31', shirt: '#E9E1CC', accent: '#3E4A5C' },
  navy: { coat: '#2F3B52', coat2: '#232C3D', shirt: '#E6DEC8', accent: '#8A6F5A' },
  grey: { coat: '#6E7380', coat2: '#4F535C', shirt: '#EDE4CF', accent: '#5A4330' },
  dress: { coat: '#7F6A8E', coat2: '#5E4E6A', shirt: '#E9E1CC', accent: '#3A3F4A' },
  dress2: { coat: '#4E6B5E', coat2: '#3A5146', shirt: '#E9E1CC', accent: '#6B5644' },
  modern: null,   // giữ màu gốc (hôm nay)
};
function recolor(rgb, o) {
  const k = near(rgb); if (!o) return rgb;
  if (['skinL', 'skinM', 'skinT', 'brownSkin', 'dark'].includes(k)) return rgb;
  const base = SW[k], L = (rgb[0] + rgb[1] + rgb[2]) / (base[0] + base[1] + base[2] + 1);   // giữ phần bóng đổ nướng sẵn
  const tgt = hex(k === 'white' || k === 'ice' ? o.shirt : k === 'orange' ? '#5A4330' : ['red', 'pink', 'yellow'].includes(k) ? o.accent : ['grey', 'slate', 'lavender'].includes(k) ? o.coat2 : o.coat);
  return tgt.map((v) => Math.min(255, v * L));
}

// mặt: tấm decal (nền màu da + nét rig.js), một texture cho mỗi cảm xúc
const faceTex = new Map();
function faceTexture(expr, skin) {
  const key = expr + skin; if (faceTex.has(key)) return faceTex.get(key);
  const c = document.createElement('canvas'); c.width = c.height = 256; const g = c.getContext('2d');
  g.fillStyle = skin; g.fillRect(0, 0, 256, 256); g.translate(128, 128 + 70); g.scale(1.45, 1.45); drawFace(g, expr, false);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; faceTex.set(key, t); return t;
}

export function fedora(color = '#2C3038', band = '#15171C') {
  const g = new THREE.Group(), m = toonMat({ color }), mb = toonMat({ color: band });
  const brim = new THREE.Mesh(new THREE.CylinderGeometry(0.62, 0.64, 0.05, 20), m); g.add(brim);
  const crown = new THREE.Mesh(new THREE.CylinderGeometry(0.36, 0.42, 0.42, 16), m); crown.position.y = 0.23; g.add(crown);
  const dent = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.08, 0.66), m); dent.position.y = 0.44; g.add(dent);
  const b = new THREE.Mesh(new THREE.CylinderGeometry(0.425, 0.43, 0.09, 16), mb); b.position.y = 0.07; g.add(b);
  g.traverse((o) => { if (o.isMesh) o.castShadow = true; });
  return g;
}

// một người: { root, mixer, play(name, t, {arm}), face(expr) }
export async function person(file, { outfit = 'charcoal', hat = true, height = 1.5, hatColor } = {}) {
  const src = await glb('mini-characters/' + file + '.glb'), S = await sampler(BASE + 'mini-characters/Textures/colormap.png');
  const root = SkeletonUtils.clone(src.scene), o = OUTFIT[outfit];
  let head = null, skinVotes = {};
  root.traverse((n) => {
    if (n.isBone && n.name === 'head') head = n;
    if (!n.isMesh) return;
    const geo = n.geometry = n.geometry.clone(), uv = geo.attributes.uv, nrm = geo.attributes.normal, col = new Float32Array(uv.count * 3);
    const C = new THREE.Color();
    for (let i = 0; i < uv.count; i++) { const rgb = recolor(S(uv.getX(i), uv.getY(i)), o); C.setRGB(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255, THREE.SRGBColorSpace); col.set([C.r, C.g, C.b], i * 3);
      { const k = near(S(uv.getX(i), uv.getY(i))); if (k.startsWith('skin') || k === 'brownSkin') skinVotes[k] = (skinVotes[k] || 0) + 1; } }
    geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
    n.material = toonMat({ vertexColors: true }); n.castShadow = true; n.receiveShadow = true; n.frustumCulled = false;
  });
  const skinK = Object.entries(skinVotes).sort((a, b) => b[1] - a[1])[0]?.[0] || 'skinM', skin = `rgb(${SW[skinK].join(',')})`;
  // kích thước: chuẩn hoá chiều cao
  root.updateMatrixWorld(true); const bb = new THREE.Box3().setFromObject(root), h = bb.max.y - bb.min.y;
  const wrap = new THREE.Group(); wrap.add(root);
  // decal mặt + mũ gắn vào xương đầu (toạ độ xương: đo khối đầu ở tư thế gốc)
  const hb = new THREE.Box3(); root.traverse((n) => { if (n.isMesh && n.name.includes('head')) hb.expandByObject(n); });
  const hs = hb.getSize(new THREE.Vector3()), hc = hb.getCenter(new THREE.Vector3());
  const inv = new THREE.Matrix4().copy(head.matrixWorld).invert(), front = new THREE.Vector3(hc.x, hc.y - hs.y * 0.02, hb.max.z + 0.004).applyMatrix4(inv), top = new THREE.Vector3(hc.x, hb.max.y, hc.z).applyMatrix4(inv);
  const hsLocal = hs.clone().divideScalar(head.getWorldScale(new THREE.Vector3()).x);
  const faceMat = new THREE.MeshToonMaterial({ gradientMap: TOON, map: faceTexture('neutral', skin) });
  const plate = new THREE.Mesh(new THREE.PlaneGeometry(hsLocal.x * 0.62, hsLocal.x * 0.62), faceMat); plate.position.copy(front); head.add(plate);
  if (hat) { const f = fedora(hatColor || (o ? o.coat2 : '#2C3038')); f.scale.setScalar(hsLocal.x * 0.9); f.position.copy(top).add(new THREE.Vector3(0, -hsLocal.y * 0.12, 0)); head.add(f); }
  root.scale.setScalar(height / h);
  const mixer = new THREE.AnimationMixer(root), clips = Object.fromEntries(src.animations.map((c) => [c.name, c]));
  let cur = null;
  return {
    root: wrap, head, skin,
    face(expr) { faceMat.map = faceTexture(expr, skin); },
    // arm: tên clip chỉ áp cho tay phải (vd ngồi + ký); t = giây của clip (tất định)
    pose(name, t = 0, { arm = null, armT = t } = {}) {
      const key = name + '|' + arm; if (cur !== key) { mixer.stopAllAction(); mixer.clipAction(clips[name]).play();
        if (arm) { const c = clips[arm].clone(); c.tracks = c.tracks.filter((tr) => tr.name.startsWith('arm-right')); mixer.clipAction(c).play(); } cur = key; }
      mixer.setTime(t); if (arm) { /* hai action cùng mixer: thời gian chung */ }
    },
    clips: Object.keys(clips),
  };
}

export async function prop(path, { scale = 1, color = null } = {}) {
  const src = await glb(path), r = src.scene.clone(true);
  r.traverse((n) => { if (!n.isMesh) return; const m = [].concat(n.material).map((mm) => toonMat({ color: color || mm.color, map: mm.map || null }));
    n.material = m.length === 1 ? m[0] : m; n.castShadow = n.receiveShadow = true; });
  r.scale.setScalar(scale); return r;
}
