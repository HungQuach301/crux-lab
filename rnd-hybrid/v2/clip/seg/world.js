// R&D hình lai vòng 2 · THẾ GIỚI của clip 45 s: phong cách A (giấy trong 3D) + chất in B trên mặt giấy (nét mực, bán sắc, vân giấy).
// Ba khu trên cùng một mặt đất: phố ngân hàng (gốc toạ độ, như khung A), khu nhà 1930 (x = −40), khu hôm nay (x = +40).
// Đèn theo hồi nội suy được (setAct): calm1929 → crisis1931 → relief1934 → today. Tất định: không Math.random, không đồng hồ.
import * as THREE from 'three';
import { CHARACTERS, POSES, blendPose, drawProp, PALETTE as P, hash } from '/rnd-hybrid/cutout/rig.js';
import { ACT, paperFigure, Bank, Row, Street, Lamp, paperGrain } from '/rnd-hybrid/v2/paper3d.js';
import { inkChar, inked, INK, halftone } from '/rnd-hybrid/v2/illus2d.js';

export const ACTS = { ...ACT, today: { sky: ['#5E86B8', '#CFE0F0'], fog: ['#B8C8D8', 30, 120], hemi: ['#F4F8FF', '#3A3630', 1.0], key: ['#FFF6E6', 2.7, [-8, 14, 8]], rim: ['#FFFFFF', 1.0, [8, 8, -14]], rimPaper: '#FFFFFF' } };

// ---------------------------------------------------------------- đèn + trời nội suy
export function Lights(scene) {
  const sky = document.createElement('canvas'); sky.width = 4; sky.height = 256; const sg = sky.getContext('2d'), st = new THREE.CanvasTexture(sky); st.colorSpace = THREE.SRGBColorSpace;
  const dome = new THREE.Mesh(new THREE.SphereGeometry(190, 24, 12), new THREE.MeshBasicMaterial({ map: st, side: THREE.BackSide, fog: false, depthWrite: false })); scene.add(dome);
  scene.fog = new THREE.Fog('#000', 10, 100);
  const hemi = new THREE.HemisphereLight('#fff', '#000', 1); scene.add(hemi);
  const key = new THREE.DirectionalLight('#fff', 1); key.castShadow = true; key.shadow.mapSize.set(4096, 4096);
  Object.assign(key.shadow.camera, { left: -16, right: 16, top: 16, bottom: -16, near: 0.5, far: 70 }); key.shadow.bias = -0.0004; key.shadow.normalBias = 0.02;
  const rim = new THREE.DirectionalLight('#fff', 1); scene.add(key, key.target, rim, rim.target);
  const C = (a, b, k) => new THREE.Color(a).lerp(new THREE.Color(b), k);
  let lastSky = '';
  return {
    set(a, b = a, k = 0, target = [0, 0, -8]) {
      const A = ACTS[a], Bq = ACTS[b], m = (x, y) => x + (y - x) * k, tv = new THREE.Vector3(...target);
      const s0 = C(A.sky[0], Bq.sky[0], k).getStyle(), s1 = C(A.sky[1], Bq.sky[1], k).getStyle(), f0 = C(A.fog[0], Bq.fog[0], k);
      const sig = s0 + s1 + f0.getHexString(); if (sig !== lastSky) { lastSky = sig;
        const g = sg.createLinearGradient(0, 0, 0, 256); g.addColorStop(0, s0); g.addColorStop(0.47, s1); g.addColorStop(0.53, '#' + f0.getHexString()); g.addColorStop(1, '#' + f0.getHexString());
        sg.fillStyle = g; sg.fillRect(0, 0, 4, 256); st.needsUpdate = true; }
      dome.position.copy(tv);
      scene.fog.color.copy(f0); scene.fog.near = m(A.fog[1], Bq.fog[1]); scene.fog.far = m(A.fog[2], Bq.fog[2]);
      hemi.color.copy(C(A.hemi[0], Bq.hemi[0], k)); hemi.groundColor.copy(C(A.hemi[1], Bq.hemi[1], k)); hemi.intensity = m(A.hemi[2], Bq.hemi[2]);
      key.color.copy(C(A.key[0], Bq.key[0], k)); key.intensity = m(A.key[1], Bq.key[1]); key.position.set(...A.key[2].map((v, i) => m(v, Bq.key[2][i]))).add(tv); key.target.position.copy(tv);
      rim.color.copy(C(A.rim[0], Bq.rim[0], k)); rim.intensity = m(A.rim[1], Bq.rim[1]); rim.position.set(...A.rim[2].map((v, i) => m(v, Bq.rim[2][i]))).add(tv); rim.target.position.copy(tv);
      key.target.updateMatrixWorld(); rim.target.updateMatrixWorld();
    },
  };
}

// ---------------------------------------------------------------- giấy in (chất B trên mặt tấm giấy A)
const PRINT = { outline: 5, light: [-0.7, -0.85], shade: 0.34, dots: 0.3, grain: 0.3 };
export function printChar(c, o = {}) {
  const wPx = o.wPx ?? 820, hPx = o.hPx ?? 1152, pad = o.pad ?? 28;
  return paperFigure({ rimPaper: '#CFE0FF', rimWidth: 4, ...o, wPx, hPx, pad, grain: 0,
    draw: (ctx) => inkChar(ctx, { s: o.s ?? 1.5, ...c }, { x: 0, y: 0, w: wPx, h: hPx, pad, ...PRINT, ...(o.print || {}) }) });
}
export function printDraw(draw, o = {}) {
  const wPx = o.wPx ?? 600, hPx = o.hPx ?? 600, pad = o.pad ?? 20;
  return paperFigure({ rimPaper: '#CFE0FF', rimWidth: 3, ...o, wPx, hPx, pad, grain: 0, draw: (ctx) => inked(ctx, draw, { x: 0, y: 0, w: wPx, h: hPx, pad, ...PRINT, ...(o.print || {}) }) });
}
export const printProp = (id, po = {}, o = {}) => printDraw((g) => drawProp(g, id, { x: 0, y: 0, s: po.s ?? 1, label: po.label, doors: po.doors, noShadow: true }), o);

// thẻ giấy chữ lớn (số / nhãn) — đọc được ở 1080p: chữ ≥ 90 px trên texture, thẻ đứng trong thế giới
export function card(lines, { w = 900, h = 420, bg = P.paper, fg = INK, accent = null, px = 120, sub = null, subPx = 64, rot = 0, pxPerM = 500, ...o } = {}) {
  return printDraw((g) => {
    g.save(); g.rotate(rot * Math.PI / 180); g.fillStyle = bg; g.beginPath(); g.roundRect(-w / 2, -h, w, h, 26); g.fill();
    if (accent) { g.fillStyle = accent; g.fillRect(-w / 2, -h, w, 26); }
    g.fillStyle = fg; g.textAlign = 'center'; g.textBaseline = 'middle'; g.font = `800 ${px}px Inter`;
    const L = [].concat(lines), y0 = -h / 2 - (L.length - 1) * px * 0.55 - (sub ? subPx * 0.6 : 0);
    L.forEach((s, i) => g.fillText(s, 0, y0 + i * px * 1.1));
    if (sub) { g.font = `600 ${subPx}px Inter`; g.fillStyle = '#4A5160'; g.fillText(sub, 0, y0 + L.length * px * 1.1 - px * 0.2 + subPx * 0.5); }
    g.restore();
  }, { wPx: w + 120, hPx: h + 120, pad: 40, pxPerM, print: { dots: 0.12, shade: 0.2 }, ...o });
}
export function tree(o = {}) {
  return printDraw((g) => {
    g.fillStyle = '#5A4330'; g.beginPath(); g.moveTo(-22, 0); g.lineTo(22, 0); g.lineTo(14, -240); g.lineTo(-14, -240); g.closePath(); g.fill();
    for (const [x, y, r, c] of [[0, -360, 150, '#3F6B4E'], [-90, -300, 100, '#4C7A58'], [95, -295, 105, '#365E44'], [10, -470, 95, '#4C7A58']]) { g.fillStyle = c; g.beginPath(); g.arc(x, y, r, 0, Math.PI * 2); g.fill(); }
  }, { wPx: 480, hPx: 640, pxPerM: 160, ...o });
}

// biến thể người xếp hàng (cùng rig, đổi màu áo)
export function variants() {
  const v = (id, base, top, extras) => { const b = CHARACTERS[base], rig = JSON.parse(JSON.stringify(b.rig));
    for (const k of ['torso', 'uaL', 'uaR', 'faL', 'faR']) rig[k].fill = top; CHARACTERS[id] = { ...b, rig, extras: extras || b.extras }; };
  v('q1', 'walt', '#4B5262', ['collar', 'tie', 'fedora']); v('q2', 'ruth', '#8A6F5A'); v('q3', 'walt', '#6B5E52', ['collar', 'vest', 'fedora']);
  v('q4', 'walt', '#3E4A5C', ['collar', 'fedora']); v('q5', 'ruth', '#5E6E86');
}

// một nhân vật nhiều nét mặt/tư thế: các tấm giấy chồng cùng chỗ, chọn một (đổi biểu cảm = đổi tấm, như hoạt hình cắt giấy)
export function Actor(scene, id, states, o = {}) {
  const g = new THREE.Group(), m = {};
  for (const [name, st] of Object.entries(states)) { const f = printChar({ id, pose: st.pose, expr: st.expr, flip: st.flip }, o); f.visible = false; g.add(f); m[name] = f; }
  scene.add(g);
  return { g, show(name) { g.visible = name != null; for (const [k, f] of Object.entries(m)) f.visible = k === name; } };
}

export function buildWorld(scene) {
  variants();
  Street(scene);
  // ---- khu ngân hàng (gốc): như khung A, sửa: cột đèn rời khỏi bậc thềm, đèn bù cho hàng người
  scene.add(Row({ n: 14, x0: -48, step: 7.5, z: -46, seed: 11, hRange: [18, 40], colors: ['#3A3F4A', '#454B57', '#343944'], litP: 0.16 }));
  scene.add(Row({ n: 3, x0: -16, step: 4.6, z: -16.5, seed: 3, hRange: [8, 13], litP: 0.22 }));
  scene.add(Row({ n: 4, x0: 15, step: 4.6, z: -16.5, seed: 5, hRange: [9, 15], litP: 0.2 }));
  const bank = Bank({ closed: false }); bank.position.set(0, 0.16, -12.6); scene.add(bank);
  // cửa gỗ có bản lề (mở → đóng), mặt cửa ở z = −14.37
  const dm = new THREE.MeshStandardMaterial({ color: '#5A4330', roughness: 0.8, flatShading: true });
  const doors = [-1, 1].map((sgn) => { const piv = new THREE.Group(); piv.position.set(sgn * 1.27, 0.16 + 0.88 + 1.7, -14.37);
    const d = new THREE.Mesh(new THREE.BoxGeometry(1.25, 3.4, 0.12), dm); d.position.x = -sgn * 0.63; d.castShadow = d.receiveShadow = true; piv.add(d); scene.add(piv); return { piv, sgn }; });
  const closedSign = card('CLOSED', { w: 760, h: 300, px: 150, bg: '#F3EBD6', fg: '#8E2B2B', accent: '#8E2B2B', pxPerM: 520, thick: 0.008 });
  closedSign.position.set(0, 0.16 + 0.88 + 1.55, -14.22); scene.add(closedSign);
  const lampL = Lamp({ on: true }); lampL.position.set(-7.5, 0.16, -6.2); scene.add(lampL);
  const lampR = Lamp({ on: true }); lampR.position.set(13.5, 0.16, -6.2); scene.add(lampR);
  const fillQ = new THREE.PointLight('#FFE0B8', 26, 14, 1.3); fillQ.position.set(6.5, 3.2, -6.4); scene.add(fillQ);      // đèn bù hàng người (phía máy quay)
  const fillW = new THREE.PointLight('#FFE3BF', 6, 14, 1.5); fillW.position.set(12.5, 2.6, -2.2); scene.add(fillW);
  const queue = [];
  const Q = [['q4', 'stand', 'neutral', true], ['person'], ['q2', 'stand', 'worried'], ['q1', 'phone', 'sad', true], ['person'], ['q3', 'stand', 'worried'], ['q5', 'slump', 'sad', true]];
  Q.forEach(([id, pose, expr, flip], i) => {
    const f = id === 'person' ? printProp('person', { s: 2.6 }, { wPx: 360, hPx: 760, pxPerM: 400 })
      : printChar({ id, pose: POSES[pose], expr, flip }, { s: 1.0, wPx: 540, hPx: 800, pxPerM: 400, print: { outline: 4, dots: 0.2 } });
    f.position.set(-0.2 + 1.25 * i, i < 1 ? 0.16 + 0.66 : 0.16, i < 1 ? -11.7 : -10.4 + 0.12 * i); scene.add(f); queue.push(f);
  });
  // ---- khu nhà 1930 (x = −40): nhà giấy của Walt + hàng xóm + cây
  const H0 = new THREE.Vector3(-40, 0.16, -11);
  const house = printProp('house', { s: 1 }, { wPx: 640, hPx: 600, pxPerM: 110, thick: 0.05 }); house.position.copy(H0); scene.add(house);
  const housePivot = new THREE.Group(); housePivot.position.copy(H0); scene.add(housePivot); scene.remove(house); house.position.set(0, 0, 0); housePivot.add(house);   // gập ra sau quanh chân
  for (const [dx, dz, s] of [[-9, -4, 0.8], [8.5, -3.5, 0.85], [-17, -6, 0.75], [16, -6, 0.7]]) { const h = printProp('house', { s }, { wPx: 640, hPx: 600, pxPerM: 110 * 1, thick: 0.04 }); h.position.set(H0.x + dx, 0.16, H0.z + dz); scene.add(h); }
  for (const [dx, dz] of [[-5.2, -1.5], [5.4, -1.2], [-12.5, -3.5], [12.5, -2.8]]) { const t = tree(); t.position.set(H0.x + dx, 0.16, H0.z + dz); scene.add(t); }
  // ---- khu hôm nay (x = +40)
  const T0 = new THREE.Vector3(40, 0.16, -11);
  const modern = printProp('houseModern', { s: 1 }, { wPx: 680, hPx: 560, pxPerM: 110, thick: 0.05 }); modern.position.copy(T0); scene.add(modern);
  for (const [dx, dz, s] of [[-9, -4, 0.85], [9, -3.6, 0.8]]) { const h = printProp('houseModern', { s }, { wPx: 680, hPx: 560, pxPerM: 110, thick: 0.04 }); h.position.set(T0.x + dx, 0.16, T0.z + dz); scene.add(h); }
  for (const [dx, dz] of [[-5.4, -1.4], [5.6, -1.2]]) { const t = tree(); t.position.set(T0.x + dx, 0.16, T0.z + dz); scene.add(t); }
  return { bank, doors, closedSign, queue, H0, T0, house, housePivot, modern };
}
