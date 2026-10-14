// R&D hình lai vòng 2 · mẫu cắm "GIẤY TRONG 3D" (style A). Không sửa toolkit/factory: chỉ import three + lib của nhà máy.
//   paperFigure()  nhân vật / đạo cụ cắt giấy (rig.js) → tấm phẳng CÓ ĐỘ DÀY: mặt in (texture canvas, vân giấy), 3 lớp mép giấy, lưng kraft,
//                  viền sáng (rim) = bóng dày lệch về phía đèn ngược, đổ bóng thật (customDepthMaterial theo alpha).
//   ACT            ánh sáng theo hồi (calm 1929 · crisis 1931 · relief 1934 · today) — cùng một cảnh, đổi hồi = đổi bộ đèn + sương + trời.
//   lowpoly        phố + ngân hàng low-poly (khối, trụ 8 mặt, trán tường) theo màu vật liệu lib3d.
// Tất định: không Math.random, không đồng hồ, không ảnh ngoài (mọi texture vẽ bằng mã).
import * as THREE from 'three';
import { drawCharacter, drawProp, PALETTE as P, hash } from '/rnd-hybrid/cutout/rig.js';

// ---------------------------------------------------------------- ánh sáng theo hồi
export const ACT = {
  calm1929: { sky: ['#2B2A33', '#8C6E52'], fog: ['#4A3F38', 14, 70], hemi: ['#F3DDBB', '#2A2018', 0.75], key: ['#FFD9A0', 2.6, [-12, 9, 6]], rim: ['#FFE2B0', 1.4, [8, 6, -14]], rimPaper: '#FFE8C2', lamp: 0 },
  crisis1931: { sky: ['#121823', '#4B5363'], fog: ['#262C37', 18, 70], hemi: ['#8EA0BC', '#191612', 0.55], key: ['#C9D6EA', 1.5, [-10, 12, 4]], rim: ['#A9C4FF', 2.2, [9, 7, -16]], rimPaper: '#CFE0FF', lamp: 1 },
  relief1934: { sky: ['#1A2433', '#9FB3C8'], fog: ['#56687D', 16, 80], hemi: ['#E9F0FA', '#2A2620', 0.85], key: ['#FFF1DC', 2.4, [-8, 14, 8]], rim: ['#FFF4E0', 1.2, [8, 8, -14]], rimPaper: '#FFF6E8', lamp: 0 },
};

export function lightAct(scene, act, { shadowBox = 16, target = [0, 0, -6] } = {}) {
  const A = ACT[act];
  const sky = document.createElement('canvas'); sky.width = 4; sky.height = 512; const g = sky.getContext('2d'), gr = g.createLinearGradient(0, 0, 0, 512);
  gr.addColorStop(0, A.sky[0]); gr.addColorStop(0.62, A.sky[1]); gr.addColorStop(1, A.fog[0]); g.fillStyle = gr; g.fillRect(0, 0, 4, 512);
  const st = new THREE.CanvasTexture(sky); st.colorSpace = THREE.SRGBColorSpace; scene.background = st;
  scene.fog = new THREE.Fog(A.fog[0], A.fog[1], A.fog[2]);
  scene.add(new THREE.HemisphereLight(A.hemi[0], A.hemi[1], A.hemi[2]));
  const key = new THREE.DirectionalLight(A.key[0], A.key[1]); key.position.set(...A.key[2]).add(new THREE.Vector3(...target)); key.castShadow = true;
  key.shadow.mapSize.set(4096, 4096); Object.assign(key.shadow.camera, { left: -shadowBox, right: shadowBox, top: shadowBox, bottom: -shadowBox, near: 0.5, far: 60 });
  key.shadow.bias = -0.0004; key.shadow.normalBias = 0.02; key.target.position.set(...target); scene.add(key, key.target);
  const rim = new THREE.DirectionalLight(A.rim[0], A.rim[1]); rim.position.set(...A.rim[2]).add(new THREE.Vector3(...target)); rim.target.position.set(...target); scene.add(rim, rim.target);
  return { A, key, rim };
}

// ---------------------------------------------------------------- vân giấy (tất định)
let GRAIN = null;
function grainTile() {
  if (GRAIN) return GRAIN; GRAIN = document.createElement('canvas'); GRAIN.width = GRAIN.height = 256; const g = GRAIN.getContext('2d'), im = g.createImageData(256, 256);
  for (let y = 0; y < 256; y++) for (let x = 0; x < 256; x++) { const i = y * 256 + x;
    const fib = 0.5 + 0.5 * Math.sin(x * 0.21 + hash(y * 3 + 1) * 6.28) * hash(y * 17 + 5);   // sợi giấy ngang
    const v = 214 + hash(i * 7 + 3) * 28 + fib * 13; im.data.set([v, v, v - 4, 255], i * 4); }
  g.putImageData(im, 0, 0); return GRAIN;
}
export function paperGrain(ctx, w, h, a = 0.35) { ctx.save(); ctx.globalCompositeOperation = 'multiply'; ctx.globalAlpha = a; ctx.fillStyle = ctx.createPattern(grainTile(), 'repeat'); ctx.fillRect(0, 0, w, h); ctx.restore(); }

// ---------------------------------------------------------------- tấm giấy có độ dày
// draw(ctx) vẽ hình ở toạ độ canvas (gốc = chân, giữa đáy); wPx × hPx canvas; pxPerM = px canvas / mét thế giới.
export function paperFigure({ draw, wPx = 768, hPx = 1152, pad = 24, pxPerM = 600, thick = 0.014, rimPaper = '#CFE0FF', rimShift = [-7, -9], rimWidth = 5,
  edge = '#E9E1CC', back = P.kraft, name = 'paper', grain = 0.3 }) {
  const mk = () => { const c = document.createElement('canvas'); c.width = wPx; c.height = hPx; return c; };
  const art = mk(), ac = art.getContext('2d'); ac.translate(wPx / 2, hPx - pad); draw(ac); ac.setTransform(1, 0, 0, 1, 0, 0);
  const sil = maskOf(art, 0, 0, 0), rim = maskOf(art, rimShift[0], rimShift[1], rimWidth), orig = mk(); orig.getContext('2d').drawImage(art, 0, 0);
  // vân giấy nhân lên phần mực rồi cắt lại theo alpha gốc
  ac.save(); ac.globalCompositeOperation = 'multiply'; ac.globalAlpha = grain; ac.fillStyle = ac.createPattern(grainTile(), 'repeat'); ac.fillRect(0, 0, wPx, hPx); ac.restore();
  ac.save(); ac.globalCompositeOperation = 'destination-in'; ac.drawImage(orig, 0, 0); ac.restore();
  const tex = (c, color = true) => { const t = new THREE.CanvasTexture(c); if (color) t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return t; };
  const tArt = tex(art), tSil = tex(sil, false), tRim = tex(rim, false);
  const w = wPx / pxPerM, h = hPx / pxPerM, y0 = pad / pxPerM;
  const geo = new THREE.PlaneGeometry(w, h); geo.translate(0, h / 2 - y0, 0);
  const g = new THREE.Group(); g.name = name;
  const depth = new THREE.MeshDepthMaterial({ depthPacking: THREE.RGBADepthPacking, alphaMap: tSil, alphaTest: 0.5 });
  const front = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ map: tArt, alphaTest: 0.5, roughness: 0.92, metalness: 0 }));
  front.castShadow = true; front.receiveShadow = true; front.customDepthMaterial = depth; g.add(front);
  for (let i = 1; i <= 3; i++) { // mép giấy: 3 lớp lùi dần, sáng như lõi giấy
    const m = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ color: edge, alphaMap: tSil, alphaTest: 0.5, roughness: 1, side: i === 3 ? THREE.DoubleSide : THREE.FrontSide }));
    m.position.z = -thick * i / 3; m.receiveShadow = true; if (i === 3) { m.material.color.set(back); } g.add(m);
  }
  // viền sáng: bóng dày lệch về phía đèn ngược, không chịu sương mờ hoàn toàn, không đổ bóng
  const r = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ color: rimPaper, alphaMap: tRim, alphaTest: 0.5, fog: false }));
  r.position.z = -thick - 0.003; g.add(r);
  g.userData = { w, h, art };
  return g;
}
// mặt nạ: trắng nơi có mực (dịch dx,dy; nở rộng grow px) trên nền đen
function maskOf(src, dx, dy, grow) {
  const c = document.createElement('canvas'); c.width = src.width; c.height = src.height; const x = c.getContext('2d');
  x.fillStyle = '#000'; x.fillRect(0, 0, c.width, c.height);
  const t = document.createElement('canvas'); t.width = src.width; t.height = src.height; const tx = t.getContext('2d');
  tx.drawImage(src, 0, 0); tx.globalCompositeOperation = 'source-in'; tx.fillStyle = '#fff'; tx.fillRect(0, 0, t.width, t.height);
  const N = grow ? 12 : 1; for (let i = 0; i < N; i++) { const a = (i / N) * Math.PI * 2; x.drawImage(t, dx + (grow ? Math.cos(a) * grow : 0), dy + (grow ? Math.sin(a) * grow : 0)); }
  return c;
}

export const charFigure = (c, o = {}) => paperFigure({ ...o, draw: (ctx) => drawCharacter(ctx, { x: 0, y: 0, s: o.s ?? 1.5, pose: c.pose, id: c.id, expr: c.expr, flip: c.flip, noShadow: true, blink: false }) });
export const propFigure = (id, po = {}, o = {}) => paperFigure({ ...o, draw: (ctx) => drawProp(ctx, id, { x: 0, y: 0, s: po.s ?? 1, doors: po.doors, label: po.label, noShadow: true }) });

// ---------------------------------------------------------------- phố + ngân hàng low-poly
const M = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.88, flatShading: true, ...o });
const box = (g, [w, h, d], [x, y, z], mat) => { const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat); m.position.set(x, y, z); m.castShadow = m.receiveShadow = true; g.add(m); return m; };

export function textPlate(text, { w = 6, h = 0.7, px = 120, fg = '#2A303B', bg = '#D9D4C7', weight = 700, spacing = 18 } = {}) {
  const c = document.createElement('canvas'); c.width = Math.round(w * 200); c.height = Math.round(h * 200); const x = c.getContext('2d');
  x.fillStyle = bg; x.fillRect(0, 0, c.width, c.height); paperGrain(x, c.width, c.height, 0.25);
  x.fillStyle = fg; x.font = `${weight} ${px}px Inter`; x.textAlign = 'center'; x.textBaseline = 'middle'; x.letterSpacing = `${spacing}px`; x.fillText(text, c.width / 2, c.height / 2 + px * 0.04);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  const m = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshStandardMaterial({ map: t, roughness: 0.9 })); m.receiveShadow = true; return m;
}

// Ngân hàng tân cổ điển: bậc thềm, 6 trụ 8 mặt, dầm, trán tường tam giác, cửa gỗ đóng, cửa sổ tối; gốc = giữa chân bậc thấp nhất
export function Bank({ w = 12, h = 8.5, d = 6, wall = '#CFC8B8', stone = '#B9B2A3', door = '#5A4330', closed = true } = {}) {
  const g = new THREE.Group(), mw = M(wall), ms = M(stone), md = M('#232833', { roughness: 0.4 }), mdoor = M(door);
  for (let i = 0; i < 4; i++) box(g, [w + 1.6 - i * 0.5, 0.22, 2.2 - i * 0.45], [0, 0.11 + i * 0.22, -i * 0.42], ms);         // bậc thềm
  const by = 0.88; box(g, [w, h - 1.6, d], [0, by + (h - 1.6) / 2, -1.8 - d / 2], mw);                                            // khối nhà
  for (let i = 0; i < 6; i++) { const x = -w / 2 + 0.9 + i * (w - 1.8) / 5;                                                       // trụ
    const c = new THREE.Mesh(new THREE.CylinderGeometry(0.34, 0.4, h - 2.6, 8), M('#E2DCCD')); c.position.set(x, by + 0.25 + (h - 2.6) / 2, -1.2); c.castShadow = c.receiveShadow = true; g.add(c);
    box(g, [0.95, 0.25, 0.95], [x, by + 0.12, -1.2], ms); box(g, [0.95, 0.22, 0.95], [x, by + h - 2.2, -1.2], ms); }
  box(g, [w + 0.6, 0.9, 1.6], [0, by + h - 1.65, -1.4], ms);                                                                     // dầm
  const s = new THREE.Shape(); s.moveTo(-w / 2 - 0.3, 0); s.lineTo(w / 2 + 0.3, 0); s.lineTo(0, 1.7); s.closePath();
  const ped = new THREE.Mesh(new THREE.ExtrudeGeometry(s, { depth: 1.5, bevelEnabled: false }), M('#C6BFAF')); ped.position.set(0, by + h - 1.2, -2.2); ped.castShadow = ped.receiveShadow = true; g.add(ped);
  const sign = textPlate('BANK', { w: 5.2, h: 0.62, px: 92, spacing: 30, bg: '#B9B2A3', fg: '#2A303B' }); sign.position.set(0, by + h - 1.65, -0.59); g.add(sign);
  box(g, [2.6, 3.6, 0.2], [0, by + 1.8, -1.85], md);                                                                             // khung cửa
  if (closed) { box(g, [1.25, 3.4, 0.12], [-0.64, by + 1.7, -1.72], mdoor); box(g, [1.25, 3.4, 0.12], [0.64, by + 1.7, -1.72], mdoor); }
  for (const x of [-4.2, -2.4, 2.4, 4.2]) box(g, [1.1, 2.4, 0.12], [x, by + 2.4, -1.75], md);
  return g;
}

// Dãy nhà phố: khối có cửa sổ (sáng/tối tất định), mái phẳng, gờ; seed cố định
export function Row({ n = 6, x0 = -20, step = 4.2, z = -16, seed = 3, hRange = [7, 14], colors = ['#6E6258', '#7D7066', '#5E5650', '#8A7C6C'], litP = 0.25, winColor = '#F6D58E' } = {}) {
  const g = new THREE.Group(), md = M('#1E222A', { roughness: 0.35 });
  for (let i = 0; i < n; i++) {
    const r = (k) => hash(seed * 101 + i * 13 + k), w = step * (0.86 + 0.12 * r(1)), h = hRange[0] + (hRange[1] - hRange[0]) * r(2), d = 6, x = x0 + i * step;
    box(g, [w, h, d], [x, h / 2, z - d / 2], M(colors[Math.floor(r(3) * colors.length)]));
    box(g, [w + 0.2, 0.3, 0.4], [x, h - 0.15, z + 0.1], M('#4A433D'));
    const cols = Math.max(2, Math.floor(w / 1.1)), rows = Math.floor((h - 1.5) / 1.6);
    for (let a = 0; a < rows; a++) for (let b = 0; b < cols; b++) {
      const lit = hash(seed * 7 + i * 31 + a * 5 + b) < litP;
      const wm = lit ? M('#2B2F38', { emissive: new THREE.Color(winColor), emissiveIntensity: 0.85, roughness: 0.3 }) : md;
      box(g, [0.55, 0.85, 0.08], [x - w / 2 + (b + 0.5) * w / cols, 1.6 + a * 1.6, z + 0.03], wm);
    }
  }
  return g;
}

export function Street(scene, { asphalt = '#23262C', walk = '#5C5852', curb = '#77716A' } = {}) {
  const g = new THREE.Group();
  const road = new THREE.Mesh(new THREE.PlaneGeometry(200, 200), M(asphalt, { roughness: 0.65 })); road.rotation.x = -Math.PI / 2; road.receiveShadow = true; g.add(road);
  box(g, [120, 0.16, 11], [0, 0.08, -11], M(walk));                                    // vỉa hè trước ngân hàng
  box(g, [120, 0.2, 0.3], [0, 0.1, -5.55], M(curb));
  for (let i = -40; i < 40; i++) box(g, [0.04, 0.165, 11], [i * 1.5, 0.083, -11], M('#4E4A45'));   // khe gạch lát
  scene.add(g); return g;
}

export function Lamp({ h = 4.6, color = '#F2B441', on = true } = {}) {
  const g = new THREE.Group(), mi = M('#1C2027', { roughness: 0.5 });
  const post = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.11, h, 6), mi); post.position.y = h / 2; post.castShadow = true; g.add(post);
  box(g, [0.36, 0.16, 0.36], [0, h, 0], mi);
  const glass = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.14, 0.5, 6), M('#3A3020', { emissive: new THREE.Color(color), emissiveIntensity: on ? 1.6 : 0 })); glass.position.y = h + 0.33; g.add(glass);
  box(g, [0.5, 0.08, 0.5], [0, h + 0.62, 0], mi);
  if (on) { const L = new THREE.PointLight(color, 22, 12, 1.4); L.position.y = h + 0.3; g.add(L); }
  return g;
}

// Lớp phủ 2D (chữ ở thiết kế 1920×1080): pill + chú thích, đúng sàn chữ 48 px của kênh
export function caption(ctx, W, H, { title, sub, tag = 'ILLUSTRATIVE', source } = {}) {
  const s = W / 1920; ctx.save(); ctx.scale(s, s);
  const pill = (txt, x, y, px, fg, bg, align = 'left') => { ctx.font = `600 ${px}px Inter`; const tw = ctx.measureText(txt).width, pw = tw + px * 0.9, ph = px * 1.45;
    const x0 = align === 'right' ? x - pw : x; ctx.fillStyle = bg; ctx.beginPath(); ctx.roundRect(x0, y, pw, ph, ph / 2); ctx.fill();
    ctx.fillStyle = fg; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText(txt, x0 + px * 0.45, y + ph / 2 + px * 0.04); return pw; };
  if (tag) pill(tag, 1824, 54, 40, '#0E1116', 'rgba(242,244,247,0.88)', 'right');
  if (title) { ctx.font = '700 72px Inter'; ctx.textBaseline = 'alphabetic'; ctx.fillStyle = 'rgba(14,17,22,0.55)'; ctx.fillText(title, 100, 958);
    ctx.fillStyle = '#F2F4F7'; ctx.fillText(title, 96, 952); }
  if (sub) { ctx.font = '400 48px Inter'; ctx.fillStyle = '#F2B441'; ctx.fillText(sub, 96, 1016); }
  if (source) { ctx.font = '400 40px Inter'; ctx.textAlign = 'right'; ctx.fillStyle = 'rgba(242,244,247,0.82)'; ctx.fillText(source, 1824, 1016); }
  ctx.restore();
}
export function vignette(ctx, W, H, a = 0.5) { const g = ctx.createRadialGradient(W / 2, H * 0.48, H * 0.3, W / 2, H / 2, H * 1.05);
  g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(1, `rgba(0,0,0,${a})`); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); }
