// F3 · Walt and Anjali. Two houses whose volumes are in proportion to the loans ($115,000 vs $655,000, 5.7×).
// In front of each: a ream = loan costs (same $→height scale for both) and a column of monthly-savings bundles that
// grows for 36 months. At year 3 Walt's column is still below his ream; Anjali's is far above hers. Yard signs give the
// rate cut each needs to break even within 3 years.
// Claims: loan_small $115,000, cost_small $3,667, sav_small $68, cut36_small 1.12, loan_large $655,000,
// cost_large $5,514, sav_large $387, cut36_large_words "about a third of a point", hold36 36 / y3 3.
// Columns are plain sums of monthly savings (no balance effect); no shortfall/surplus number is printed.
import { THREE, C, W, H, canvasTex, txt, label, chrome, mat, box, house, ease, easeOut, back, mix, clamp, rng } from './common.js';

export function build({ scene, camera, renderer }) {
  const duration = 9.5;
  scene.background = new THREE.Color('#1F2A3D');
  scene.fog = new THREE.Fog('#1F2A3D', 18, 40);
  renderer.toneMappingExposure = 1.05;
  scene.add(new THREE.HemisphereLight('#B9C8EE', '#3A3A2E', 1.5));
  const sun = new THREE.DirectionalLight('#FFD9A8', 3.0); sun.position.set(-7, 8, 6); sun.castShadow = true;
  sun.shadow.mapSize.set(1024, 1024); Object.assign(sun.shadow.camera, { left: -10, right: 10, top: 8, bottom: -6, near: 1, far: 30 }); sun.shadow.bias = -0.0006; scene.add(sun);

  const ground = new THREE.Mesh(new THREE.PlaneGeometry(60, 40), mat('#34472F', { roughness: 1 })); ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  const walk = new THREE.Mesh(new THREE.PlaneGeometry(60, 2.2), mat('#6B6E73', { roughness: 0.95 })); walk.rotation.x = -Math.PI / 2; walk.position.set(0, 0.004, 1.6); walk.receiveShadow = true; scene.add(walk);

  // houses: volume ∝ loan → linear scale = (655/115)^(1/3)
  const L = Math.cbrt(655000 / 115000);
  const base = { w: 2.3, d: 1.9, h: 1.35, roof: 0.95 };
  const walt = house({ ...base, wall: '#CDBF9F', roofCol: '#4A4036', lit: 0.25 }); walt.position.set(-3.3, 0, -1.9); scene.add(walt);
  const anj = house({ w: base.w * L, d: base.d * L, h: base.h * L, roof: base.roof * L, wall: '#B9C3CC', roofCol: '#3A404C', lit: 0.25 }); anj.position.set(2.5, 0, -3.1); scene.add(anj);
  const r = rng(3);
  for (let i = 0; i < 10; i++) { const s = 0.7 + r() * 0.7, tr = new THREE.Mesh(new THREE.ConeGeometry(0.8 * s, 2.8 * s, 7), mat('#22352A')); tr.position.set(-12 + i * 2.7 + r(), 1.4 * s, -8 - r() * 3); tr.castShadow = true; scene.add(tr); }

  // ---- reams (loan costs) and savings columns, one $ scale ----
  const K = 0.2 / 1000; // units per dollar
  const FW = 0.95, FD = 0.75;
  const edge = canvasTex(256, 256, (g, w, h) => { g.fillStyle = '#EFEBE2'; g.fillRect(0, 0, w, h); for (let y = 0; y < h; y += 5) { g.fillStyle = '#DAD4C6'; g.fillRect(0, y, w, 2); } });
  const pm = (map) => new THREE.MeshStandardMaterial({ map, roughness: 0.92 });
  function ream(cost, text) {
    const h = cost * K;
    const front = canvasTex(512, Math.round(512 * h / FW), (g, w, hh) => {
      g.fillStyle = '#EFEBE2'; g.fillRect(0, 0, w, hh); for (let y = 0; y < hh; y += 6) { g.fillStyle = '#DAD4C6'; g.fillRect(0, y, w, 2); }
      g.fillStyle = '#2E3440'; g.fillRect(0, hh * 0.2, w, hh * 0.6);
      txt(g, 'LOAN COSTS', w / 2, hh * 0.5 - 20, { size: 54, weight: 700, color: '#FFFFFF', align: 'center' });
      txt(g, text, w / 2, hh * 0.5 + 75, { size: 104, weight: 700, color: '#FFFFFF', align: 'center' });
    });
    const m = new THREE.Mesh(new THREE.BoxGeometry(FW, h, FD), [pm(edge), pm(edge), pm(edge), pm(edge), pm(front), pm(edge)]);
    m.castShadow = m.receiveShadow = true; m.userData.h = h; scene.add(m); return m;
  }
  const noteTex = canvasTex(256, 128, (g, w, h) => { g.fillStyle = '#D5E6D8'; g.fillRect(0, 0, w, h); g.strokeStyle = '#6FA383'; g.lineWidth = 6; g.strokeRect(8, 8, w - 16, h - 16); g.fillStyle = C.warn; g.fillRect(w / 2 - 36, 0, 72, h); });
  const noteSide = mat('#BFD5C4', { roughness: 0.95 }), bandSide = mat('#C9B27A', { roughness: 0.9 });
  function column(sav) {
    const th = sav * K, arr = [];
    const g = new THREE.BoxGeometry(FW * 0.92, th * 0.94, FD * 0.8);
    for (let i = 0; i < 36; i++) {
      const b = new THREE.Mesh(g, [noteSide, noteSide, pm(noteTex), noteSide, bandSide, noteSide]); b.castShadow = b.receiveShadow = true;
      b.userData = { jx: Math.sin(i * 12.99 + sav) * 0.02, jr: Math.sin(i * 78.2 + sav) * 0.03, th }; scene.add(b); arr.push(b);
    }
    return arr;
  }
  const P0 = { wf: -4.35, ws: -3.15, af: 1.45, as: 2.65, z: 1.25 };
  const wRe = ream(3667.05, '$3,667'), aRe = ream(5513.97, '$5,514');
  const wCol = column(67.87), aCol = column(386.54);
  const lasers = [0, 1].map(() => { const l = new THREE.Mesh(new THREE.BoxGeometry(2.3, 0.02, 0.02), new THREE.MeshBasicMaterial({ color: '#FFFFFF', transparent: true, opacity: 0 })); scene.add(l); return l; });

  // ---- yard signs with the answer ----
  function yardSign(lines, col) {
    const g = new THREE.Group();
    const tex = canvasTex(1024, 560, (c, w, h) => {
      c.fillStyle = '#F7F4EC'; c.fillRect(0, 0, w, h); c.fillStyle = col; c.fillRect(0, 0, w, 120);
      txt(c, 'RATE CUT NEEDED', w / 2, 84, { size: 64, weight: 700, color: '#FFFFFF', align: 'center' });
      txt(c, lines[0], w / 2, 330, { size: 170, weight: 700, color: '#1B1F26', align: 'center' });
      txt(c, lines[1], w / 2, 480, { size: 66, weight: 600, color: '#4B5563', align: 'center' });
    });
    const board = new THREE.Mesh(new THREE.BoxGeometry(1.9, 1.04, 0.04), [mat('#DDD'), mat('#DDD'), mat('#DDD'), mat('#DDD'), new THREE.MeshStandardMaterial({ map: tex, roughness: 0.8 }), mat('#DDD')]);
    board.position.y = 1.35; board.castShadow = true; g.add(board);
    for (const x of [-0.7, 0.7]) { const p = box(0.05, 1.0, 0.05, mat('#5B4636')); p.position.set(x, 0.5, -0.03); g.add(p); }
    scene.add(g); return g;
  }
  const wSign = yardSign(['1.12 points', 'in 3 years'], C.warn); wSign.position.set(-1.35, 0, 0.1); wSign.rotation.y = 0.12;
  const aSign = yardSign(['about 1/3', 'of a point · 3 years'], '#8A93A3'); aSign.position.set(4.55, 0, 0.3); aSign.rotation.y = -0.18;

  const monthAt = (t) => clamp((t - 2.5) / 4.0) * 36;

  function place(re, x) { re.position.set(x, re.userData.h / 2, P0.z); }
  function update(t) {
    const k = ease(t, 0, duration);
    camera.position.set(mix(-0.2, 0.2, k), mix(3.6, 3.3, k), mix(12.6, 11.6, k));
    camera.lookAt(0.1, 1.55, -0.6);
    // reams drop in
    for (const [re, x, t0] of [[wRe, P0.wf, 1.2], [aRe, P0.af, 1.45]]) { const d = easeOut(t, t0, t0 + 0.5); place(re, x); re.position.y += (1 - d) * 3; re.visible = t > t0; }
    const mf = monthAt(t);
    for (const [col, x] of [[wCol, P0.ws], [aCol, P0.as]]) {
      col.forEach((b, i) => {
        const land = easeOut(mf, i, i + 0.9); b.visible = mf > i;
        b.position.set(x + b.userData.jx, b.userData.th * (i + 0.5) + (1 - land) * 0.6, P0.z + b.userData.jx);
        b.rotation.y = b.userData.jr + (1 - land) * 0.3;
      });
    }
    // level lines at each ream top: green once the column passes it
    [[wRe, P0.wf, P0.ws, wCol], [aRe, P0.af, P0.as, aCol]].forEach(([re, xf, xs, col], j) => {
      const l = lasers[j]; l.position.set((xf + xs) / 2, re.userData.h + 0.01, P0.z + FD / 2 + 0.02);
      l.material.opacity = ease(t, 2.2, 2.6);
      const h = col[0].userData.th * mf; l.material.color.set(h >= re.userData.h ? C.positive : '#FFFFFF');
    });
    for (const [s, t0] of [[wSign, 6.9], [aSign, 7.2]]) { const u = back(t, t0, t0 + 0.55); s.scale.set(1, Math.max(0.001, u), 1); s.visible = t > t0; }
  }

  function overlay(ctx, t, P) {
    chrome(ctx, t, { illus: true, source: 'Loans and loan costs: CFPB HMDA 2025 medians. Savings and rate cuts: Crux model. Walt and Anjali are illustrative.' });
    const a = ease(t, 0.2, 0.8);
    const wN = P(new THREE.Vector3(-3.3, 1.35 + 0.95 + 0.35, -1.9)), aN = P(new THREE.Vector3(2.5, (1.35 + 0.95) * L + 0.35, -3.1));
    // character marks (shape + colour from design/tokens.json: small = triangle/warn, large = square/negative)
    const tri = (x, y, al) => { ctx.save(); ctx.globalAlpha = al; ctx.fillStyle = C.warn; ctx.beginPath(); ctx.moveTo(x, y - 18); ctx.lineTo(x + 11, y); ctx.lineTo(x - 11, y); ctx.fill(); ctx.restore(); };
    const sq = (x, y, al) => { ctx.save(); ctx.globalAlpha = al; ctx.fillStyle = C.negative; ctx.fillRect(x - 9, y - 18, 18, 18); ctx.restore(); };
    tri(wN.x - 70, wN.y - 34, a); label(ctx, 'Walt', wN.x - 50, wN.y - 34, { size: 30, weight: 700, alpha: a });
    label(ctx, '$115,000 loan', wN.x, wN.y, { size: 24, weight: 600, color: C.ink, align: 'center', alpha: a });
    sq(aN.x - 80, aN.y - 34, a); label(ctx, 'Anjali', aN.x - 60, aN.y - 34, { size: 30, weight: 700, alpha: a });
    label(ctx, '$655,000 loan', aN.x, aN.y, { size: 24, weight: 600, color: C.ink, align: 'center', alpha: a });
    label(ctx, 'house volume ∝ loan size', 32, 672, { size: 16, weight: 400, color: C.muted, alpha: a });
    // ream + savings labels
    const mf = monthAt(t);
    for (const [re, xf, xs, sav, s] of [[wRe, P0.wf, P0.ws, 67.87, '+$68 a month'], [aRe, P0.af, P0.as, 386.54, '+$387 a month']]) {
      const rt = P(new THREE.Vector3(xf, re.userData.h, P0.z + FD / 2));
      label(ctx, 'loan costs', rt.x, rt.y - 14, { size: 20, weight: 600, color: C.ink, align: 'center', alpha: ease(t, 1.7, 2.1) });
      const ct = P(new THREE.Vector3(xs, Math.max(0.02, sav * K * mf), P0.z + FD / 2));
      label(ctx, s, ct.x + 62, Math.min(ct.y - 4, 600), { size: 22, weight: 700, color: C.positive, alpha: ease(t, 2.4, 2.8) });
    }
    // month counter
    const m = Math.floor(mf + 1e-6);
    label(ctx, m >= 36 ? 'After 3 years' : `Month ${m} of 36`, 48, 60, { size: 34, weight: 700, color: m >= 36 ? C.warn : C.ink, alpha: ease(t, 2.3, 2.6) });
    // captions
    const cap = (s, a0, b0, col = C.ink) => label(ctx, s, W / 2, 640, { size: 28, weight: 600, color: col, align: 'center', alpha: Math.min(ease(t, a0, a0 + 0.3), 1 - ease(t, b0 - 0.3, b0)) });
    cap('Same kind of refinance offer, very different loans', 0.3, 2.4);
    cap('Fees are close. Monthly savings are not.', 2.5, 6.8);
    cap('The smaller loan needs a much bigger rate cut', 7.0, 9.8, C.warn);
  }

  return { duration, update, overlay, stripTimes: [0.9, 2.2, 4.0, 5.8, 7.2, 9.0], posterTime: 8.6 };
}
