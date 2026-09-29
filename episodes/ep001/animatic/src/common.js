// C4 animatic: shared pieces lifted from the signed C3 style frames (SF1-SF6) so every scene uses the same objects,
// the same scale rules and the same motion grammar (design/c3/final/system.md §3-§4).
import { THREE, C, W, H, DATA, CL, text, measure, line, rect, dot, hatch, strike, mark, ease, easeOut, back, mix, clamp,
  canvasTex, ptxt, mat, box, pm, woodTable, paperEdgeTex, house } from './engine.js';

export const PL = 'rgba(14,17,22,0.85)';

// ---------- H1: rooms ----------
export function kitchen(scene, renderer, { w = 18, d = 9, key = 90 } = {}) {
  scene.background = new THREE.Color(C.bg);
  renderer.toneMappingExposure = 1.05;
  scene.add(new THREE.HemisphereLight('#8FA3C8', '#1A1410', 0.6));
  const k = new THREE.SpotLight('#FFE2BC', key, 26, 0.75, 0.55, 1.3); k.position.set(-1.5, 9, 4); k.target.position.set(0.6, 0, -0.4);
  k.castShadow = true; k.shadow.mapSize.set(1024, 1024); k.shadow.bias = -0.0005; scene.add(k, k.target);
  const rim = new THREE.DirectionalLight('#A9B6CF', 0.35); rim.position.set(5, 4, -4); scene.add(rim);
  woodTable(scene, w, d);
  return k;
}
export function outdoors(scene, renderer, { sky = '#1B2536', trees = 12 } = {}) {
  scene.background = new THREE.Color(sky);
  scene.fog = new THREE.Fog(sky, 20, 44);
  renderer.toneMappingExposure = 1.05;
  scene.add(new THREE.HemisphereLight('#B9C8EE', '#3A3A2E', 1.4));
  const sun = new THREE.DirectionalLight('#FFD9A8', 2.8); sun.position.set(-7, 9, 7); sun.castShadow = true;
  sun.shadow.mapSize.set(1024, 1024); Object.assign(sun.shadow.camera, { left: -12, right: 12, top: 10, bottom: -7, near: 1, far: 36 }); sun.shadow.bias = -0.0006; scene.add(sun);
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(90, 50), mat('#34472F', { roughness: 1 })); ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  const walk = new THREE.Mesh(new THREE.PlaneGeometry(90, 2.6), mat('#6B6E73', { roughness: 0.95 })); walk.rotation.x = -Math.PI / 2; walk.position.set(0, 0.004, 0.2); walk.receiveShadow = true; scene.add(walk);
  let s = 3 >>> 0; const r = () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296);
  for (let i = 0; i < trees; i++) { const k = 0.7 + r() * 0.7, tr = new THREE.Mesh(new THREE.ConeGeometry(0.8 * k, 2.8 * k, 7), mat('#22352A')); tr.position.set(-18 + i * 3.2 + r(), 1.4 * k, -9.5 - r() * 3); tr.castShadow = true; scene.add(tr); }
  return sun;
}
export function shadowAll(g) { g.traverse((o) => { if (o.isMesh) o.castShadow = o.receiveShadow = true; }); return g; }

// ---------- H1: the refinance letter (SF2), with optional rows; row k highlighted ----------
export function letter(scene, { rows = [], width = 2.2 } = {}) {
  const LW = width, LH = LW * 11 / 8.5;
  let lastKey = '';
  const draw = (hl) => (g, w, h) => {
    g.fillStyle = '#F7F4EC'; g.fillRect(0, 0, w, h);
    g.fillStyle = '#2E3440'; g.fillRect(0, 0, w, 190);
    ptxt(g, 'REFINANCE OFFER', 70, 128, { size: 92, weight: 700, color: '#FFFFFF' });
    ptxt(g, 'A new loan at a lower rate', 70, 290, { size: 62, weight: 600, color: '#20242C' });
    ptxt(g, 'pays off your current loan.', 70, 370, { size: 62, weight: 600, color: '#20242C' });
    g.fillStyle = '#CFC9BB'; for (let i = 0; i < 3; i++) g.fillRect(70, 440 + i * 56, 900 - (i % 3) * 170, 20);
    // rows: [{label, value}] from y=640; the last row is the bill (boxed)
    rows.forEach((r, i) => {
      const y = 660 + i * 190, k = hl[i] || 0, bill = i === rows.length - 1;
      if (k > 0) { g.fillStyle = `rgba(242,180,65,${0.55 * k})`; g.fillRect(40, y - 40, w - 80, 170); }
      if (bill) { g.strokeStyle = '#20242C'; g.lineWidth = 6; g.strokeRect(40, y - 40, w - 80, 170); }
      ptxt(g, r.label, 80, y + 70, { size: 66, weight: 700, color: '#20242C' });
      ptxt(g, r.value, w - 80, y + 78, { size: 104, weight: 700, color: '#20242C', align: 'right' });
    });
  };
  const tex = canvasTex(1100, 1424, draw([]));
  const edge = mat('#EDE8DC');
  const m = box(LW, 0.012, LH, [edge, edge, pm(tex), edge, edge, edge]); scene.add(m);
  return { mesh: m, LW, LH, set(hl) { const key = hl.map((x) => x.toFixed(2)).join(','); if (key !== lastKey) { tex.userData.redraw(draw(hl)); lastKey = key; } } };
}

// ---------- H1: cash (SF1/SF3) ----------
export function cashMats() {
  const bandTex = canvasTex(512, 64, (g, w, h) => { g.fillStyle = C.cash; g.fillRect(0, 0, w, h); for (let y = 0; y < h; y += 5) { g.fillStyle = '#B9CFBF'; g.fillRect(0, y, w, 1); } g.fillStyle = C.cashBand; g.fillRect(w / 2 - 70, 0, 140, h); });
  const topTex = canvasTex(512, 384, (g, w, h) => { g.fillStyle = '#D5E6D8'; g.fillRect(0, 0, w, h); g.strokeStyle = '#6FA383'; g.lineWidth = 10; g.strokeRect(14, 14, w - 28, h - 28); g.fillStyle = C.cashBand; g.fillRect(w / 2 - 60, 0, 120, h); });
  const cs = mat(C.cashSide, { roughness: 0.95 });
  return [cs, cs, pm(topTex), cs, pm(bandTex), cs];
}
// a column of monthly bundles: bundle i lands at time landT(i); returns update(t)
export function bundleColumn(scene, { n, dollars, K, FW = 1.25, FD = 0.95, x = 0, z = 0 }) {
  const mats = cashMats(), bt = dollars * K, arr = [];
  const g = new THREE.BoxGeometry(FW * 0.96, bt * 0.92, FD * 0.8);
  for (let i = 0; i < n; i++) {
    const b = new THREE.Mesh(g, mats); b.castShadow = b.receiveShadow = true;
    b.userData.jx = Math.sin(i * 12.9898 + dollars) * 0.025; b.userData.jr = Math.sin(i * 78.233 + dollars) * 0.03; b.visible = false; scene.add(b); arr.push(b);
  }
  return {
    bt, arr,
    update(t, landT, dx = 0) {
      arr.forEach((b, i) => {
        const td = landT(i), land = easeOut(t, td - 0.16, td);
        b.visible = t >= td - 0.16;
        b.position.set(x + dx + b.userData.jx, bt * (i + 0.5) + (1 - land) * 0.7, z + b.userData.jx * 0.5);
        b.rotation.y = b.userData.jr + (1 - land) * 0.35;
      });
    },
  };
}
// payment stack with a liftable top slab (SF1): the slab = a monthly saving
export function paymentStack(scene, { total, slab, height = 1.7, SW = 1.5, SD = 1.0, x = 1.1, z = 0.2 }) {
  const K = height / total;
  const stackTex = canvasTex(512, 512, (g, w, h) => { g.fillStyle = C.cash; g.fillRect(0, 0, w, h); for (let y = 0; y < h; y += 5) { g.fillStyle = '#B9CFBF'; g.fillRect(0, y, w, 1); } g.fillStyle = C.cashBand; g.fillRect(w / 2 - 60, 0, 120, h); for (let y = 0; y < h; y += 64) { g.fillStyle = '#6E8A76'; g.fillRect(0, y, w, 4); } });
  stackTex.repeat.set(1, 2); stackTex.wrapT = THREE.RepeatWrapping;
  const topTex = canvasTex(512, 340, (g, w, h) => { g.fillStyle = '#D5E6D8'; g.fillRect(0, 0, w, h); g.strokeStyle = '#6FA383'; g.lineWidth = 10; g.strokeRect(14, 14, w - 28, h - 28); g.fillStyle = C.cashBand; g.fillRect(w / 2 - 60, 0, 120, h); });
  const side = pm(stackTex), topM = pm(topTex);
  const hBase = (total - slab) * K, hSlab = slab * K;
  const base = box(SW, hBase, SD, [side, side, topM, side, side, side]); base.position.set(x, hBase / 2, z); scene.add(base);
  const slabMats = [0, 1, 2, 3, 4, 5].map((i) => new THREE.MeshStandardMaterial({ map: i === 2 ? topTex : stackTex, roughness: 0.9, emissive: new THREE.Color(C.positive), emissiveIntensity: 0 }));
  const sl = box(SW, hSlab, SD, slabMats); scene.add(sl);
  const glow = new THREE.PointLight(C.positive, 0, 4, 2); scene.add(glow);
  const grey = new THREE.Color('#7E838C'), white = new THREE.Color('#ffffff');
  const st = { K, hBase, hSlab, SW, SD, x, z, base, slab: sl,
    // lift 0..1 (up), glowK 0..1, greyK 0..1
    set(lift, glowK = 0, greyK = 0, dy = 0.7) {
      sl.position.set(x, hBase + hSlab / 2 + dy * lift, z); sl.rotation.y = 0.08 * lift;
      slabMats.forEach((m) => { m.emissiveIntensity = 0.35 * glowK; m.color.copy(white).lerp(grey, greyK); });
      glow.position.set(x, hBase + hSlab + dy * lift + 0.3, z + 1.0); glow.intensity = 6 * glowK;
    },
    slabY(lift, dy = 0.7) { return hBase + hSlab / 2 + dy * lift; },
  };
  st.set(0);
  return st;
}
// paper ream = loan costs (SF3/SF5)
export function ream(scene, { dollars, K, FW = 1.25, FD = 0.95, label = null, big = 136 }) {
  const edge = paperEdgeTex(); edge.repeat.set(1, 3);
  const h = dollars * K;
  const front = canvasTex(640, Math.max(96, Math.round(640 * h / FW)), (g, w, hh) => {
    g.fillStyle = C.paper; g.fillRect(0, 0, w, hh); for (let y = 0; y < hh; y += 7) { g.fillStyle = C.paperLine; g.fillRect(0, y, w, 2); }
    if (label) { g.fillStyle = '#2E3440'; g.fillRect(0, hh * 0.14, w, hh * 0.72); ptxt(g, label, w / 2, hh * 0.5 + big * 0.35, { size: big, weight: 700, color: '#FFFFFF', align: 'center' }); }
  });
  const m = box(FW, h, FD, [pm(edge), pm(edge), pm(edge), pm(edge), pm(front), pm(edge)]); m.userData.h = h; scene.add(m);
  return m;
}

// ---------- H3 pieces ----------
// rate-cut ruler (horizontal): 0 .. max points; the 1-point line as a dashed tick (test value)
export function cutRuler(ctx, { x0 = 260, x1 = 1660, y = 560, max = 1.25, alpha = 1, onePt = 1, label = true, oneLabel = true }) {
  const xOf = (c) => x0 + (c / max) * (x1 - x0);
  line(ctx, [[x0, y], [x1, y]], C.grid, 6, { alpha });
  line(ctx, [[x0, y - 20], [x0, y + 20]], C.grid, 4, { alpha });
  if (label) text(ctx, 'rate cut (points) →', x1, y + 70, 'note', { align: 'right', color: C.muted, alpha });
  text(ctx, 'no cut', x0, y + 70, 'note', { align: 'center', color: C.muted, alpha });
  if (onePt > 0) {
    line(ctx, [[xOf(1), y - 150], [xOf(1), y + 30]], C.ink, 4, { dash: [14, 10], alpha: alpha * onePt });
    if (oneLabel) text(ctx, CL('s10') + '-point line', xOf(1), y - 172, 'note', { align: 'center', color: C.ink, alpha: alpha * onePt });
  }
  return xOf;
}
// month ruler (flat, SF3): ticks per month, only listed months numbered
export function monthRuler(ctx, { x0 = 330, x1 = 1590, y = 912, max = 36, m = 0, numbered = [], alpha = 1, late = 1e9, word = 'months', color }) {
  const rx = (k) => x0 + (k / max) * (x1 - x0);
  ctx.save(); ctx.globalAlpha = alpha; ctx.fillStyle = C.grid; ctx.fillRect(x0, y, x1 - x0, 4); ctx.restore();
  const step = max > 60 ? 1 : 1, wbar = max > 60 ? 4 : 8;
  for (let k = 1; k <= max; k += step) {
    const lit = k <= m + 1e-6; ctx.save(); ctx.globalAlpha = alpha; ctx.fillStyle = lit ? (k > late ? C.negative : (color || C.ink)) : C.grid;
    ctx.fillRect(rx(k) - wbar / 2, y - (lit ? 30 : 16), wbar, lit ? 30 : 16); ctx.restore();
  }
  text(ctx, word, x1 + 24, y + 4, 'note', { color: C.muted, alpha });
  for (const [k, s, a, col] of numbered) text(ctx, s, rx(k), y + 62, 'label', { align: 'center', color: col || C.ink, alpha: alpha * a });
  return rx;
}
export function houseIcon(ctx, cx, yb, s, fill, a, outline, lw = 4) { // 2D house (SF6): (cx, yb) = bottom centre
  if (a <= 0) return;
  const w = 70 * s, h = 46 * s, rf = 34 * s;
  ctx.save(); ctx.globalAlpha = a; ctx.beginPath();
  ctx.moveTo(cx - w / 2, yb); ctx.lineTo(cx + w / 2, yb); ctx.lineTo(cx + w / 2, yb - h); ctx.lineTo(cx + w / 2 + 6 * s, yb - h);
  ctx.lineTo(cx, yb - h - rf); ctx.lineTo(cx - w / 2 - 6 * s, yb - h); ctx.lineTo(cx - w / 2, yb - h); ctx.closePath();
  if (outline) { ctx.setLineDash([10, 8]); ctx.strokeStyle = C.ink; ctx.lineWidth = lw; ctx.stroke(); }
  else { ctx.fillStyle = fill; ctx.fill(); }
  ctx.restore();
}
// weekly rate chart (SF1 grammar): weeks [{d, r}], draws to fractional index `head`
export function rateLine(ctx, weeks, xOf, yOf, head, color = C.accent, lw = 7, from = 0) {
  if (head <= from) return null;
  const pts = []; const full = Math.floor(head);
  for (let i = from; i <= Math.min(full, weeks.length - 1); i++) pts.push([xOf(i), yOf(weeks[i].r)]);
  if (head > full && full + 1 < weeks.length) { const f = head - full; pts.push([mix(xOf(full), xOf(full + 1), f), mix(yOf(weeks[full].r), yOf(weeks[full + 1].r), f)]); }
  if (pts.length === 1) pts.push(pts[0]);
  line(ctx, pts, color, lw);
  return pts[pts.length - 1];
}
// a plain paper card (flat, H1 overlay): the loan file
export function card(ctx, x, y, w, h, a = 1) {
  if (a <= 0) return;
  ctx.save(); ctx.globalAlpha = a; ctx.shadowColor = 'rgba(0,0,0,0.6)'; ctx.shadowBlur = 30; ctx.shadowOffsetY = 10;
  ctx.fillStyle = '#EFEBE2'; ctx.fillRect(x, y, w, h); ctx.shadowColor = 'transparent';
  ctx.fillStyle = '#2E3440'; ctx.fillRect(x, y, w, 96); ctx.restore();
}
export { house };
