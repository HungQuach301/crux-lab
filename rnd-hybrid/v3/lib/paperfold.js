// R&D vòng 3 · H3 (đối chứng): ĐẠO CỤ GIẤY GẤP 3D tự dựng + NHÂN VẬT GIẤY NHIỀU LỚP (5 lớp tách z, mép cong, tự đổ bóng lên nhau).
//   foldBox     khối gấp: mặt lõm nhẹ (giấy căng trên nếp), nếp gấp tối, vân giấy in
//   roll        cột giấy cuộn (trụ hở, đường mép dán)
//   layered     nhân vật rig.js tách 5 lớp: tay sau · chân sau · thân+chân trước · đầu (+mũ, mặt) · tay trước; mỗi lớp một tấm giấy cong có mép dày
// Tất định: vân giấy bằng hash, không Math.random.
import * as THREE from 'three';
import { drawCharacter, hash } from '/rnd-hybrid/cutout/rig.js';
import { inked } from '/rnd-hybrid/v2/illus2d.js';

// texture giấy: màu nền + sợi + hạt + chữ/hoạ tiết tuỳ chọn (draw)
const texCache = new Map();
export function paperTex(color, { w = 256, h = 256, draw = null, key = null, rep = [1, 1] } = {}) {
  const k = key || color + w + h; if (!draw && texCache.has(k)) return texCache.get(k);
  const c = document.createElement('canvas'); c.width = w; c.height = h; const g = c.getContext('2d');
  g.fillStyle = color; g.fillRect(0, 0, w, h);
  const im = g.getImageData(0, 0, w, h), d = im.data;
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) { const i = (y * w + x) * 4, n = (hash(i * 3 + 7) - 0.5) * 18 + (hash(y * 31 + 3) - 0.5) * 10 * Math.sin(x * 0.2 + y);
    d[i] += n; d[i + 1] += n; d[i + 2] += n - 2; }
  g.putImageData(im, 0, 0);
  if (draw) draw(g, w, h);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(...rep);
  if (!draw) texCache.set(k, t); return t;
}
export const paperMat = (color, o = {}) => new THREE.MeshStandardMaterial({ map: paperTex(color, o), roughness: 0.95, metalness: 0, side: o.side ?? THREE.FrontSide });

// khối gấp: BoxGeometry chia ô, mỗi mặt lõm theo sin (giấy căng), nếp = khung tối trên texture
export function foldBox(w, h, d, color, { sag = 0.012, faces = null, open = false } = {}) {
  const geo = new THREE.BoxGeometry(w, h, d, 8, 8, 8), p = geo.attributes.position, n = geo.attributes.normal, v = new THREE.Vector3(), nn = new THREE.Vector3();
  for (let i = 0; i < p.count; i++) { v.fromBufferAttribute(p, i); nn.fromBufferAttribute(n, i);
    const u = nn.x !== 0 ? [v.y / h + 0.5, v.z / d + 0.5] : nn.y !== 0 ? [v.x / w + 0.5, v.z / d + 0.5] : [v.x / w + 0.5, v.y / h + 0.5];
    const s = Math.sin(Math.PI * u[0]) * Math.sin(Math.PI * u[1]) * sag * Math.min(w, h, d, 1.5); v.addScaledVector(nn, -s); p.setXYZ(i, v.x, v.y, v.z); }
  geo.computeVertexNormals();
  const crease = (g, W, H) => { g.strokeStyle = 'rgba(40,30,20,0.45)'; g.lineWidth = 5; g.strokeRect(2, 2, W - 4, H - 4); };
  const base = paperMat(color, { draw: crease, key: color + 'crease' });
  const mats = [0, 1, 2, 3, 4, 5].map((i) => (faces && faces[i]) ? faces[i] : base);
  const m = new THREE.Mesh(geo, mats); m.castShadow = m.receiveShadow = true; return m;
}
export function roll(r, h, color) {   // cột giấy cuộn: trụ hở + mép dán
  const g = new THREE.Group(), mat = paperMat(color, { draw: (c, W, H) => { c.fillStyle = 'rgba(40,30,20,0.35)'; c.fillRect(W * 0.48, 0, 6, H); }, key: color + 'seam', side: THREE.DoubleSide });
  const m = new THREE.Mesh(new THREE.CylinderGeometry(r, r * 1.04, h, 18, 1, true), mat); m.castShadow = m.receiveShadow = true; g.add(m); return g;
}
export function prism(w, h, d, color) {   // trán tường / mái: lăng trụ tam giác gấp
  const s = new THREE.Shape(); s.moveTo(-w / 2, 0); s.lineTo(w / 2, 0); s.lineTo(0, h); s.closePath();
  const m = new THREE.Mesh(new THREE.ExtrudeGeometry(s, { depth: d, bevelEnabled: false }), paperMat(color)); m.castShadow = m.receiveShadow = true; m.position.z = -d / 2; return m;
}
export function printedPlane(w, h, draw, { px = 300 } = {}) {
  const t = paperTex('#EDE4CF', { w: Math.round(w * px), h: Math.round(h * px), draw }); t.repeat.set(1, 1);
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.02), new THREE.MeshStandardMaterial({ map: t, roughness: 0.95 })); m.castShadow = m.receiveShadow = true; return m;
}

// ---------------------------------------------------------------- nhân vật giấy 5 lớp
const LAYERS = [['uaL', 'faL'], ['thL', 'shL'], ['thR', 'shR', 'torso'], ['head'], ['uaR', 'faR']];
const kraft = new THREE.MeshStandardMaterial({ color: '#B98E5E', roughness: 1, side: THREE.BackSide });
function bentPlane(w, h, bend) { const g = new THREE.PlaneGeometry(w, h, 16, 1), p = g.attributes.position;
  for (let i = 0; i < p.count; i++) { const x = p.getX(i) / (w / 2); p.setZ(i, -bend * x * x); } g.computeVertexNormals(); return g; }
export function layered(c, { s = 1.0, pxPerM = 420, wPx = 640, hPx = 900, pad = 24, gap = 0.035, bend = 0.03, print = true } = {}) {
  const g = new THREE.Group(), w = wPx / pxPerM, h = hPx / pxPerM;
  LAYERS.forEach((only, li) => {
    const cv = document.createElement('canvas'); cv.width = wPx; cv.height = hPx; const x = cv.getContext('2d'); x.translate(wPx / 2, hPx - pad);
    const draw = (gg) => drawCharacter(gg, { x: 0, y: 0, s, id: c.id, pose: c.pose, expr: c.expr, flip: c.flip, noShadow: true, only });
    if (print) inked(x, draw, { x: 0, y: 0, w: wPx, h: hPx, pad, outline: 4, light: [-0.7, -0.85], shade: 0.3, dots: 0.22, grain: 0.3 }); else draw(x);
    const t = new THREE.CanvasTexture(cv); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
    const geo = bentPlane(w, h, bend * (li === 3 ? 1.6 : 1)); geo.translate(0, h / 2 - pad / pxPerM, 0);
    const front = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ map: t, alphaTest: 0.5, roughness: 0.92 }));
    front.customDepthMaterial = new THREE.MeshDepthMaterial({ depthPacking: THREE.RGBADepthPacking, map: t, alphaTest: 0.5 });
    front.castShadow = front.receiveShadow = true;
    const back = new THREE.Mesh(geo, kraft.clone()); back.material.map = t; back.material.alphaTest = 0.5; back.material.color.set('#C9A27A'); back.position.z = -0.004;
    const lay = new THREE.Group(); lay.add(front, back); lay.position.z = (li - 2) * gap; g.add(lay);
  });
  return g;
}
