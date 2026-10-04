// H1 shared objects: ONE set of things on ONE table, reused by K1-K7 and the thumbnail.
// History coordinates: month i of TB3MS from 1954-01 (i = 0) to 2026-08 (i = 871) -> x = X0 + i*DX; rate r -> y = KY*r.
import { THREE, C, DATA, mat, box, canvasTex, clamp, mix } from './engine.js';

export const RIDGE = DATA.ridge.map((d) => d[1]);
export const NM = RIDGE.length; // 872
export const X0 = -8, DX = 16 / (NM - 1), KY = 0.2;
export const xOf = (i) => X0 + i * DX;
export const STARTS = DATA.starts; // 753 'YYYY-MM'
export const startIdx = (ym) => DATA.ridge.findIndex((d) => d[0] === ym);
export const Z = { ridge0: -2.1, ridge1: -1.4, rail: -1.3, longRail: -0.62, tray0: 0.12 };

export function lights(scene, { key = [-2, 11, 7], target = [0, 0.6, -0.4], power = 260, hemi = 0.55, shadowSize = 1024 } = {}) {
  scene.background = new THREE.Color(C.bg);
  scene.add(new THREE.HemisphereLight('#8FA3C8', '#1A1410', hemi));
  const k = new THREE.SpotLight('#FFE6C4', power, 40, 0.75, 0.6, 1.25); k.position.set(...key); k.target.position.set(...target);
  k.castShadow = true; k.shadow.mapSize.set(shadowSize, shadowSize); k.shadow.bias = -0.0006; scene.add(k, k.target);
  const rim = new THREE.DirectionalLight('#A9B6CF', 0.45); rim.position.set(6, 5, -5); scene.add(rim);
  return k;
}
export function table(scene, w = 22, d = 10, z = 0) {
  const woodTex = canvasTex(1024, 1024, (g, ww, hh) => {
    g.fillStyle = C.wood; g.fillRect(0, 0, ww, hh);
    for (let i = 0; i < 8; i++) { g.fillStyle = i % 2 ? '#62442F' : '#5A3E2A'; g.fillRect(0, i * 128, ww, 126); g.fillStyle = '#3B281C'; g.fillRect(0, i * 128 + 126, ww, 2); }
    g.globalAlpha = 0.12; g.strokeStyle = '#2A1C12';
    for (let i = 0; i < 160; i++) { const y = (i * 37) % hh; g.beginPath(); g.moveTo(0, y); g.bezierCurveTo(ww * 0.3, y + 6, ww * 0.6, y - 6, ww, y + 3); g.stroke(); }
  });
  woodTex.wrapS = woodTex.wrapT = THREE.RepeatWrapping; woodTex.repeat.set(3, 1.5);
  const t = new THREE.Mesh(new THREE.BoxGeometry(w, 0.2, d), new THREE.MeshStandardMaterial({ map: woodTex, roughness: 0.7 }));
  t.position.set(0, -0.1, z); t.receiveShadow = true; scene.add(t);
  const wall = new THREE.Mesh(new THREE.PlaneGeometry(60, 24), mat(C.wall, { roughness: 1 })); wall.position.set(0, 6, z - d / 2 - 0.2); wall.receiveShadow = true; scene.add(wall);
  return t;
}

// ---- the ridge: TB3MS 1954-01..2026-08 as a landform (accent) ----
export function ridge(scene) {
  const sh = new THREE.Shape(); sh.moveTo(xOf(0), 0);
  RIDGE.forEach((r, i) => sh.lineTo(xOf(i), KY * r));
  sh.lineTo(xOf(NM - 1), 0); sh.closePath();
  const g = new THREE.ExtrudeGeometry(sh, { depth: Z.ridge1 - Z.ridge0, bevelEnabled: false, curveSegments: 1 });
  const m = new THREE.Mesh(g, mat(C.accent, { roughness: 0.92 })); m.position.z = Z.ridge0; m.castShadow = m.receiveShadow = true;
  scene.add(m); return m;
}
// a glowing wire along the ridge top for months [i0, i0+n) (in front of the ridge face), optional y shift
export function ridgeWire(scene, color = '#9CC2FF') {
  const m = new THREE.Mesh(new THREE.BufferGeometry(), new THREE.MeshBasicMaterial({ color, toneMapped: false }));
  scene.add(m);
  m.userData.set = (i0, n, dy = 0, z = Z.ridge1 + 0.03, upto = 1) => {
    const k = Math.max(2, Math.round(n * upto));
    const pts = []; for (let j = 0; j < k; j++) { const i = Math.min(NM - 1, i0 + j); pts.push(new THREE.Vector3(xOf(i), KY * RIDGE[i] + dy, z)); }
    m.geometry.dispose(); m.geometry = new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts, false, 'catmullrom', 0.1), Math.max(8, k * 2), 0.022, 6, false);
  };
  return m;
}

// ---- steel rail (fixed rate) with an amber sleeve made of n segments ----
export function rail(scene, n, { r = 0.035, posts = false } = {}) {
  const g = new THREE.Group(); scene.add(g);
  const steel = mat(C.steel, { roughness: 0.35, metalness: 0.75 });
  const bar = new THREE.Mesh(new THREE.CylinderGeometry(r, r, 1, 16), steel); bar.rotation.z = Math.PI / 2; bar.castShadow = true; g.add(bar);
  const glow = new THREE.InstancedMesh(new THREE.CylinderGeometry(r * 1.45, r * 1.45, 1, 12), new THREE.MeshBasicMaterial({ color: C.warn, toneMapped: false }), n);
  glow.instanceMatrix.setUsage(THREE.DynamicDrawUsage); g.add(glow);
  const p1 = box(0.05, 1, 0.05, steel), p2 = box(0.05, 1, 0.05, steel); if (posts) g.add(p1, p2);
  const M = new THREE.Matrix4(), Q = new THREE.Quaternion().setFromEuler(new THREE.Euler(0, 0, Math.PI / 2)), S = new THREE.Vector3(), P = new THREE.Vector3();
  // place: from x0 to x1 at height y, depth z; lit(j) -> 0..1 glow for segment j
  g.userData.place = (x0, x1, y, z, lit = () => 0, vis = 1) => {
    g.visible = vis > 0.01;
    bar.position.set((x0 + x1) / 2, y, z); bar.scale.set(1, Math.max(1e-3, x1 - x0), 1);
    if (posts) { p1.position.set(x0 + 0.06, y / 2, z); p1.scale.y = y; p2.position.set(x1 - 0.06, y / 2, z); p2.scale.y = y; }
    const seg = (x1 - x0) / n;
    for (let j = 0; j < n; j++) {
      const a = lit(j); P.set(x0 + seg * (j + 0.5), y, z); S.set(a > 0 ? 1 : 0, seg * 1.02, a > 0 ? 1 : 0);
      M.compose(P, Q, S); glow.setMatrixAt(j, M);
    }
    glow.instanceMatrix.needsUpdate = true;
  };
  return g;
}
// Leah's bead: an octahedron (her shape) in ink
export function bead(scene, s = 0.1) {
  const m = new THREE.Mesh(new THREE.OctahedronGeometry(s, 0), mat(C.ink, { roughness: 0.25, metalness: 0.1, emissive: new THREE.Color('#C9D2E0'), emissiveIntensity: 0.35, flatShading: true }));
  m.castShadow = true; scene.add(m); return m;
}
// head-start bracket: a vertical bar + two arms (positive). set(x, yBead, yRail, z): flips when bead is above the rail.
export function bracket(scene, { arm = 0.22, th = 0.035 } = {}) {
  const g = new THREE.Group(); scene.add(g);
  const solid = mat(C.positive, { roughness: 0.5, emissive: new THREE.Color(C.positive), emissiveIntensity: 0.35 });
  const hollow = mat(C.muted, { roughness: 0.6, transparent: true, opacity: 0.85 });
  const v = box(th, 1, th, solid), a1 = box(arm, th, th, solid), a2 = box(arm, th, th, solid); g.add(v, a1, a2);
  g.userData.set = (x, yb, yr, z, s = 1) => {
    g.visible = s > 0.01;
    const top = Math.max(yb, yr), bot = Math.min(yb, yr), h = Math.max(th, (top - bot)) * s;
    const flipped = yb > yr + 1e-4, m = flipped ? hollow : solid;
    v.material = a1.material = a2.material = m;
    const mid = (top + bot) / 2;
    v.position.set(x, mid, z); v.scale.set(1, h, 1);
    const dir = flipped ? 1 : 1; // arms point toward the rail/bead (+x)
    a1.position.set(x + dir * arm / 2, mid + h / 2, z); a2.position.set(x + dir * arm / 2, mid - h / 2, z);
    a1.scale.set(s, 1, 1); a2.scale.set(s, 1, 1);
  };
  return g;
}
// green glow sheet between bead and rail (the gap while the bead is under the rail)
export function gapGlow(scene, w = 0.05) {
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, 1, 0.02), new THREE.MeshBasicMaterial({ color: C.positive, transparent: true, opacity: 0.75, toneMapped: false }));
  scene.add(m);
  m.userData.set = (x, yb, yr, z, a = 1) => { const h = yr - yb; m.visible = h > 0.01 && a > 0.01; m.position.set(x, (yb + yr) / 2, z); m.scale.set(1, Math.max(1e-3, h - 0.12), 1); m.material.opacity = 0.75 * a; };
  return m;
}
// the 10-year glass frame (accent edges)
export function frame(scene, { w = 120 * DX, h = 3.9, z0 = Z.ridge0 - 0.08, z1 = Z.ridge1 + 0.1 } = {}) {
  const g = new THREE.Group(); scene.add(g);
  const em = new THREE.MeshBasicMaterial({ color: '#8DB6FF', toneMapped: false, transparent: true });
  const d = z1 - z0, t = 0.03;
  const add = (sx, sy, sz, x, y, z) => { const b = new THREE.Mesh(new THREE.BoxGeometry(sx, sy, sz), em); b.position.set(x, y, z); g.add(b); };
  for (const x of [0, w]) for (const z of [0, d]) add(t, h, t, x, h / 2, z);
  for (const y of [0, h]) { for (const z of [0, d]) add(w, t, t, w / 2, y, z); for (const x of [0, w]) add(t, t, d, x, y, d / 2); }
  const glass = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), new THREE.MeshBasicMaterial({ color: C.accent, transparent: true, opacity: 0.07, depthWrite: false }));
  glass.position.set(w / 2, h / 2, d / 2); g.add(glass);
  g.position.z = z0; g.userData = { em, glass, w, h };
  g.userData.alpha = (a) => { g.visible = a > 0.01; em.opacity = a; glass.material.opacity = 0.07 * a; };
  return g;
}
// faint outline copy of the frame (for overlap ghosts)
export function ghostFrame(scene, opacity = 0.35) {
  const f = frame(scene); f.userData.em.color = new THREE.Color(C.accent); f.userData.glass.visible = false; f.userData.alpha(opacity); return f;
}

// ---- two trays under the two halves; one tile per start month: column = year, row = month ----
export const TILE = { w: 0.19, d: 0.12, pitch: 0.14, low: 0.03, high: 0.16 };
export function tileXZ(k) { // k = start index 0..752
  const ym = STARTS[k], y = +ym.slice(0, 4), mo = +ym.slice(5, 7) - 1;
  const i0 = (y - 1954) * 12; // ridge index of Jan of that year
  return { x: xOf(i0 + 5.5), z: Z.tray0 + 0.06 + mo * TILE.pitch, early: ym < '1981-01' };
}
export function trays(scene) {
  const g = new THREE.Group(); scene.add(g);
  const tm = mat(C.tray, { roughness: 0.9 });
  const mk = (xa, xb) => {
    const w = xb - xa + 0.12, d = 12 * TILE.pitch + 0.12, cx = (xa + xb) / 2, cz = Z.tray0 + d / 2 - 0.0;
    const base = box(w, 0.04, d, tm); base.position.set(cx, 0.02, cz); g.add(base);
    for (const [sx, sz, x, z] of [[w, 0.04, cx, cz - d / 2], [w, 0.04, cx, cz + d / 2], [0.04, d, cx - w / 2, cz], [0.04, d, cx + w / 2, cz]]) {
      const r = box(sx, 0.09, sz, tm); r.position.set(x, 0.045, z); g.add(r);
    }
  };
  mk(xOf(0), xOf(27 * 12 - 1)); mk(xOf(27 * 12), xOf(STARTS.length - 1 + 0)); // 1954-01..1980-12 | 1981-01..2016-09
  const im = new THREE.InstancedMesh(new THREE.BoxGeometry(TILE.w, 1, TILE.d), mat('#FFFFFF', { roughness: 0.55 }), STARTS.length);
  im.castShadow = true; im.receiveShadow = true; im.instanceMatrix.setUsage(THREE.DynamicDrawUsage); g.add(im);
  const worst = new THREE.Group(); g.add(worst);
  const wm = box(TILE.w * 1.05, 1, TILE.d * 1.1, mat(C.negative, { roughness: 0.5 })); worst.add(wm);
  const ring = box(TILE.w * 1.12, 0.035, TILE.d * 1.2, mat('#1A1D24', { roughness: 0.6 })); worst.add(ring);
  const M = new THREE.Matrix4(), Q = new THREE.Quaternion(), S = new THREE.Vector3(), P = new THREE.Vector3(), col = new THREE.Color();
  const cGrey = new THREE.Color(C.muted), cRed = new THREE.Color(C.negative), cBlank = new THREE.Color(C.tileBlank);
  // state(k) -> { y: drop height above rest (0 = landed, null = not yet), kind: 'blank'|'grey'|'red', h: 0..1 extra height mix }
  g.userData.update = (state, worstK = DATA.worstIdx, worstPulse = 0) => {
    for (let k = 0; k < STARTS.length; k++) {
      const s = state(k); const { x, z } = tileXZ(k);
      if (!s || s.y === null || k === worstK && s.kind === 'red') { M.compose(P.set(x, -5, z), Q, S.set(1e-3, 1e-3, 1e-3)); im.setMatrixAt(k, M); im.setColorAt(k, cGrey); continue; }
      const hh = mix(TILE.low, TILE.high, s.h ?? (s.kind === 'red' ? 1 : 0));
      M.compose(P.set(x, 0.04 + hh / 2 + s.y, z), Q, S.set(1, hh, 1)); im.setMatrixAt(k, M);
      col.copy(s.kind === 'blank' ? cBlank : s.kind === 'red' ? cRed : cGrey);
      if (s.mixRed !== undefined) col.copy(cGrey).lerp(cRed, s.mixRed);
      im.setColorAt(k, col);
    }
    im.instanceMatrix.needsUpdate = true; if (im.instanceColor) im.instanceColor.needsUpdate = true;
    const s = state(worstK);
    worst.visible = !!(s && s.y !== null && s.kind === 'red');
    if (worst.visible) {
      const { x, z } = tileXZ(worstK), hh = TILE.high * 2 * (1 + 0.25 * worstPulse) * (s.h ?? 1);
      wm.scale.y = hh; wm.position.set(x, 0.04 + hh / 2 + s.y, z); ring.position.set(x, 0.04 + hh * 0.62 + s.y, z);
    }
  };
  return g;
}

// ---- jar of green liquid (the cushion) ----
export function jar(scene, { r = 0.3, h = 1.3 } = {}) {
  const g = new THREE.Group(); scene.add(g);
  const glass = new THREE.Mesh(new THREE.CylinderGeometry(r, r, h, 40, 1, true), new THREE.MeshStandardMaterial({ color: C.glass, transparent: true, opacity: 0.22, roughness: 0.08, metalness: 0.1, side: THREE.DoubleSide, depthWrite: false }));
  glass.position.y = h / 2; g.add(glass);
  const base = new THREE.Mesh(new THREE.CylinderGeometry(r * 1.02, r * 1.02, 0.04, 40), new THREE.MeshStandardMaterial({ color: C.glass, transparent: true, opacity: 0.4, roughness: 0.1 })); base.position.y = 0.02; g.add(base);
  const rim = new THREE.Mesh(new THREE.TorusGeometry(r, 0.018, 8, 40), mat('#DDE6EE', { roughness: 0.2, metalness: 0.3 })); rim.rotation.x = Math.PI / 2; rim.position.y = h; g.add(rim);
  const liq = new THREE.Mesh(new THREE.CylinderGeometry(r * 0.93, r * 0.93, 1, 40), new THREE.MeshStandardMaterial({ color: C.positive, roughness: 0.3, emissive: new THREE.Color(C.positive), emissiveIntensity: 0.45, transparent: true, opacity: 0.92 }));
  g.add(liq);
  const surf = new THREE.Mesh(new THREE.CircleGeometry(r * 0.93, 40), new THREE.MeshBasicMaterial({ color: '#7FE0AE', toneMapped: false })); surf.rotation.x = -Math.PI / 2; g.add(surf);
  // drain spout drops (when the cushion is being used up)
  const drip = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 1, 8), new THREE.MeshBasicMaterial({ color: C.positive, toneMapped: false })); g.add(drip);
  const pour = new THREE.Mesh(new THREE.CylinderGeometry(1, 1, 1, 10), new THREE.MeshBasicMaterial({ color: C.positive, toneMapped: false, transparent: true, opacity: 0.85 })); g.add(pour);
  g.userData = { r, h };
  // level 0..1 ; inflow (thickness 0..1) ; outflow 0..1
  g.userData.set = (level, inflow = 0, outflow = 0) => {
    const L = clamp(level) * (h - 0.08); liq.visible = L > 0.004; surf.visible = liq.visible;
    liq.scale.y = Math.max(1e-3, L); liq.position.y = 0.04 + L / 2; surf.position.y = 0.04 + L + 0.001;
    pour.visible = inflow > 0.02; const pr = 0.015 + 0.05 * clamp(inflow); const top = h + 0.9, bot = 0.04 + L;
    pour.scale.set(pr, top - bot, pr); pour.position.set(0, (top + bot) / 2, 0);
    drip.visible = false;
  };
  return g;
}

// ---- coin piles (interest paid): instanced silver coins; `extra` coins are red-rimmed (costlier part) ----
export function coinPile(scene, n, { r = 0.24, th = 0.04, color = C.coin } = {}) {
  const geo = new THREE.CylinderGeometry(r, r, th * 0.9, 28);
  const im = new THREE.InstancedMesh(geo, mat(color, { roughness: 0.35, metalness: 0.65 }), n); im.castShadow = im.receiveShadow = true; scene.add(im);
  const M = new THREE.Matrix4(), Q = new THREE.Quaternion(), S = new THREE.Vector3(1, 1, 1), P = new THREE.Vector3();
  im.userData.set = (x, z, count, y0 = 0, from = 0) => {
    for (let i = 0; i < n; i++) {
      const on = i < count; const jx = Math.sin(i * 12.99) * 0.005, jz = Math.cos(i * 7.31) * 0.005;
      M.compose(P.set(x + jx, y0 + th * (i + 0.5), z + jz), Q, on ? S.set(1, 1, 1) : S.set(1e-3, 1e-3, 1e-3)); im.setMatrixAt(i, M);
    }
    im.instanceMatrix.needsUpdate = true;
  };
  im.userData.th = th; return im;
}
// paper stack (balance still owed)
export function paperStack(scene, { w = 0.5, d = 0.36 } = {}) {
  const tex = canvasTex(128, 256, (g, ww, hh) => { g.fillStyle = C.paper; g.fillRect(0, 0, ww, hh); for (let y = 0; y < hh; y += 5) { g.fillStyle = C.paperLine; g.fillRect(0, y, ww, 1.5); } });
  tex.wrapS = tex.wrapT = THREE.RepeatWrapping; tex.repeat.set(1, 3);
  const top = mat(C.paper, { roughness: 0.95 });
  const side = new THREE.MeshStandardMaterial({ map: tex, roughness: 0.95 });
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, 1, d), [side, side, top, top, side, side]); m.castShadow = m.receiveShadow = true; scene.add(m);
  m.userData.set = (x, z, hgt) => { m.visible = hgt > 0.005; m.scale.y = Math.max(1e-3, hgt); m.position.set(x, hgt / 2, z); };
  return m;
}
// offer card (paper) with a printed icon: 'level' line or 'wavy' line — a picture, no words
export function offerCard(scene, kind, { w = 1.5, d = 1.0 } = {}) {
  const tex = canvasTex(600, 400, (g, ww, hh) => {
    g.fillStyle = C.paper; g.fillRect(0, 0, ww, hh);
    g.strokeStyle = '#D6CFBF'; g.lineWidth = 10; g.strokeRect(18, 18, ww - 36, hh - 36);
    g.fillStyle = '#CFC8B8'; for (let i = 0; i < 3; i++) g.fillRect(60, 300 + i * 26, 300 - i * 70, 10); // grey "fine print" bars (not text)
    g.lineWidth = 16; g.lineCap = 'round'; g.lineJoin = 'round';
    if (kind === 'level') { g.strokeStyle = '#5B6573'; g.beginPath(); g.moveTo(70, 170); g.lineTo(530, 170); g.stroke(); }
    else {
      g.strokeStyle = '#2F63C4'; g.beginPath();
      for (let x = 70; x <= 530; x += 4) { const y = 210 - 0.12 * (x - 70) * 0 + 60 * Math.sin((x - 70) / 46) * (0.5 + (x - 70) / 600) - 0.0; x === 70 ? g.moveTo(x, y) : g.lineTo(x, y); }
      g.stroke();
    }
  });
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, 0.02, d), [mat(C.paper), mat(C.paper), new THREE.MeshStandardMaterial({ map: tex, roughness: 0.9 }), mat(C.paper), mat(C.paper), mat(C.paper)]);
  m.castShadow = m.receiveShadow = true; scene.add(m); return m;
}
// Leah standee: a diamond on a small stand (her shape everywhere = octahedron)
export function leah(scene, s = 0.16) {
  const g = new THREE.Group(); scene.add(g);
  const st = new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.2, 0.06, 24), mat('#3A3F48', { roughness: 0.6 })); st.position.y = 0.03; st.castShadow = true; g.add(st);
  const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.015, 0.015, 0.4, 8), mat(C.steel, { metalness: 0.7, roughness: 0.3 })); pole.position.y = 0.26; g.add(pole);
  const d = new THREE.Mesh(new THREE.OctahedronGeometry(s, 0), mat(C.ink, { roughness: 0.25, emissive: new THREE.Color('#C9D2E0'), emissiveIntensity: 0.35, flatShading: true })); d.position.y = 0.46 + s; d.castShadow = true; g.add(d);
  g.userData.d = d; return g;
}
// a wire track (variable rate on the bench) through given points; set(pts, upto)
export function wire(scene, color = C.accent, r = 0.022, o = {}) {
  const m = new THREE.Mesh(new THREE.BufferGeometry(), new THREE.MeshStandardMaterial({ color, roughness: 0.35, emissive: new THREE.Color(color), emissiveIntensity: 0.55, transparent: !!o.opacity, opacity: o.opacity ?? 1 }));
  m.castShadow = !o.opacity; scene.add(m);
  m.userData.set = (pts) => { m.geometry.dispose(); if (pts.length < 2) { m.visible = false; return; } m.visible = true; m.geometry = new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts, false, 'catmullrom', 0.2), Math.max(8, pts.length * 3), r, 6, false); };
  return m;
}
