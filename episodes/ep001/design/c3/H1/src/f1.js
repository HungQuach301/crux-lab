// F1 · Cold open: the missed window. Nora's house at night; a bank-style rate sign in the yard; a $459/month cheque
// rises out of her mailbox while the rate sits at the 2026 low, then falls back when the rate climbs above 7%.
// Claims: low2026 5.98%, low2026_date Feb 26 2026, low2026_since Sept 2022, oct2023, r_old 7.62%,
// sav_low2026_median $459, r_today 7.03% (anchor_date Sep 24 2026), seven, first7_since Jan 2025.
import { THREE, C, W, H, canvasTex, txt, label, chrome, badge, mat, box, house, ease, easeOut, lin, mix, clamp, rng } from './common.js';

export function build({ scene, camera, renderer }) {
  const duration = 9.0;
  scene.background = new THREE.Color('#0A0F1C');
  scene.fog = new THREE.Fog('#0A0F1C', 14, 34);
  renderer.toneMappingExposure = 1.15;

  // lights: moon + sky + warm windows + porch
  scene.add(new THREE.HemisphereLight('#5A74B8', '#10131A', 0.55));
  const moon = new THREE.DirectionalLight('#AFC4FF', 0.9); moon.position.set(-6, 9, 5); moon.castShadow = true;
  moon.shadow.mapSize.set(1024, 1024); Object.assign(moon.shadow.camera, { left: -8, right: 8, top: 8, bottom: -8, near: 1, far: 30 }); moon.shadow.bias = -0.0008;
  scene.add(moon);
  const warm = new THREE.PointLight('#FFB660', 6, 9, 1.6); warm.position.set(1.4, 1.4, 1.2); scene.add(warm);

  // ground, path, curb
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(60, 40), mat('#1B2A22', { roughness: 1 })); ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  const path_ = box(0.9, 0.02, 4, mat('#5B5E63')); path_.position.set(1.5, 0.01, 1.9); scene.add(path_);
  const street = new THREE.Mesh(new THREE.PlaneGeometry(60, 4), mat('#15171B', { roughness: 0.95 })); street.rotation.x = -Math.PI / 2; street.position.set(0, 0.005, 6.2); street.receiveShadow = true; scene.add(street);
  const curb = box(60, 0.12, 0.25, mat('#6C6F75')); curb.position.set(0, 0.06, 4.1); scene.add(curb);

  // Nora's house
  const hs = house({ w: 3.4, d: 2.6, h: 1.9, roof: 1.3, wall: '#B8AE9C', roofCol: '#2E323A', lit: 2.2 });
  hs.position.set(1.5, 0, -1.2); scene.add(hs);
  const porch = new THREE.PointLight('#FFC98A', 2.5, 4, 2); porch.position.set(1.5, 1.35, 0.4); scene.add(porch);
  // neighbours and trees (silhouettes for depth)
  const r = rng(7);
  for (const [x, z, s] of [[-7, -5, 0.9], [8, -4.5, 1.0], [-11, -8, 1.1], [12, -9, 1.2]]) {
    const n = house({ w: 3 * s, d: 2.4 * s, h: 1.7 * s, roof: 1.1 * s, wall: '#3A3F4A', roofCol: '#1C1F26', lit: x > 0 ? 0.35 : 0.0 }); n.position.set(x, 0, z); scene.add(n);
  }
  for (let i = 0; i < 9; i++) {
    const x = -12 + i * 3 + r() * 1.2, z = -6.5 - r() * 3, s = 0.8 + r() * 0.8;
    const tr = new THREE.Mesh(new THREE.ConeGeometry(0.9 * s, 3 * s, 7), mat('#0F1A16')); tr.position.set(x, 1.5 * s, z); tr.castShadow = true; scene.add(tr);
  }
  // stars
  const sp = []; for (let i = 0; i < 260; i++) sp.push((r() - 0.5) * 80, 6 + r() * 20, -25 - r() * 10);
  const sg = new THREE.BufferGeometry(); sg.setAttribute('position', new THREE.Float32BufferAttribute(sp, 3));
  scene.add(new THREE.Points(sg, new THREE.PointsMaterial({ color: '#C9D6FF', size: 0.06, fog: false })));

  // ---- the rate sign (bank-board style) ----
  const sign = new THREE.Group(); sign.position.set(-2.35, 0, 1.3); sign.rotation.y = 0.2; scene.add(sign);
  for (const x of [-0.8, 0.8]) { const p = box(0.08, 1.0, 0.08, mat('#3A3D44', { metalness: 0.5, roughness: 0.5 })); p.position.set(x, 0.5, -0.02); sign.add(p); }
  const PW = 2.0, PH = 2.1, PY = 1.0; // panel bottom y
  const frame = box(PW + 0.1, PH + 0.1, 0.12, mat('#23262D', { metalness: 0.6, roughness: 0.4 })); frame.position.set(0, PY + PH / 2, -0.07); sign.add(frame);
  // rate scale (5% .. 8%) occupies panel-local y in [y5, y8] on the left 40%
  const TW = 1000, TH = 1050, sy = (v) => TH - (80 + (v - 5) / 3 * (TH - 200)); // texture px
  const RMIN = 5, RMAX = 8;
  const state = { big: '7.62%', date: 'OCT 2023', col: C.warn, dim: 0 };
  const faceTex = canvasTex(TW, TH, drawFace);
  function drawFace(g) {
    g.fillStyle = '#10141B'; g.fillRect(0, 0, TW, TH);
    // scale
    g.fillStyle = '#1A1F28'; g.fillRect(40, 40, 330, TH - 80);
    for (let v = 5; v <= 8.001; v += 0.5) {
      const y = sy(v), major = Math.abs(v - Math.round(v)) < 0.01;
      g.fillStyle = '#9AA4B2'; g.fillRect(70, y - 2, major ? 70 : 40, 4);
      if (major) txt(g, `${v}%`, 160, y + 16, { size: 46, weight: 600, color: C.muted });
    }
    // 7% threshold (red)
    g.fillStyle = C.negative; g.fillRect(56, sy(7) - 4, 300, 8);
    // Nora's loan 7.62% (brass tick)
    g.fillStyle = C.warn; g.fillRect(56, sy(7.62) - 4, 300, 8);
    txt(g, "NORA 7.62%", 360, sy(7.62) - 16, { size: 34, weight: 700, color: C.warn, align: 'right' });
    if (state.ghost) { g.fillStyle = 'rgba(63,191,127,0.55)'; g.fillRect(56, sy(5.98) - 3, 300, 6); txt(g, 'FEB 2026 LOW', 360, sy(5.98) + 40, { size: 28, weight: 700, color: 'rgba(63,191,127,0.8)', align: 'right' }); }
    // right: title, digits, date
    txt(g, '30-YEAR FIXED', 420, 110, { size: 48, weight: 700, color: C.ink });
    txt(g, 'US weekly average', 420, 160, { size: 36, weight: 400, color: C.muted });
    g.fillStyle = '#07090D'; g.fillRect(410, 300, 560, 300);
    txt(g, state.big, 690, 510, { size: 170, weight: 700, color: state.col, align: 'center' });
    txt(g, state.date, 700, 680, { size: 38, weight: 700, color: C.ink, align: 'center' });
    if (state.sub) txt(g, state.sub, 700, 736, { size: 34, weight: 400, color: C.muted, align: 'center' });
  }
  const faceMat = new THREE.MeshStandardMaterial({ map: faceTex, emissiveMap: faceTex, emissive: new THREE.Color('#ffffff'), emissiveIntensity: 0.9, roughness: 0.6 });
  const face = new THREE.Mesh(new THREE.PlaneGeometry(PW, PH), faceMat); face.position.set(0, PY + PH / 2, 0.0); sign.add(face);
  const texToLocal = (px, py) => new THREE.Vector3(-PW / 2 + px / TW * PW, PY + PH - py / TH * PH, 0.02);
  // pointer (3D brass wedge) and green band
  const ptr = new THREE.Mesh(new THREE.ConeGeometry(0.07, 0.2, 3), new THREE.MeshStandardMaterial({ color: '#FFFFFF', emissive: '#FFFFFF', emissiveIntensity: 0.6 }));
  ptr.rotation.z = Math.PI / 2; sign.add(ptr);
  const band = new THREE.Mesh(new THREE.BoxGeometry(0.08, 1, 0.03), new THREE.MeshStandardMaterial({ color: C.positive, emissive: C.positive, emissiveIntensity: 1.4, transparent: true, opacity: 0.9 }));
  sign.add(band);
  const glow = new THREE.PointLight(C.positive, 0, 3, 2); sign.add(glow); glow.position.set(-0.3, 1.6, 0.5);

  // ---- mailbox + cheque ----
  const MB = new THREE.Vector3(-0.35, 0, 3.1);
  const mb = new THREE.Group(); mb.position.copy(MB); mb.rotation.y = -0.5; scene.add(mb);
  const mpost = box(0.09, 1.0, 0.09, mat('#4A3A2E')); mpost.position.y = 0.5; mb.add(mpost);
  const mbm = mat('#3C5A86', { metalness: 0.55, roughness: 0.4 });
  const mbody = box(0.34, 0.16, 0.6, mbm); mbody.position.y = 1.08; mb.add(mbody);
  const mtop = new THREE.Mesh(new THREE.CylinderGeometry(0.17, 0.17, 0.6, 20), mbm); mtop.castShadow = true;
  mtop.rotation.x = Math.PI / 2; mtop.position.y = 1.16; mb.add(mtop);
  const flag = box(0.03, 0.26, 0.1, mat(C.negative)); mb.add(flag);
  const chqTex = canvasTex(1024, 470, (g, w, h) => {
    g.fillStyle = '#E9F5EC'; g.fillRect(0, 0, w, h);
    g.strokeStyle = '#3FBF7F'; g.lineWidth = 10; g.strokeRect(14, 14, w - 28, h - 28);
    txt(g, 'PAY TO', 50, 90, { size: 30, weight: 600, color: '#51625A' });
    txt(g, 'Nora', 170, 92, { size: 48, weight: 700, color: '#1D2A24' });
    txt(g, 'ILLUSTRATIVE', w - 50, 88, { size: 28, weight: 700, color: '#9A6A00', align: 'right' });
    txt(g, '$459', 50, 285, { size: 190, weight: 700, color: '#1F7A4D' });
    txt(g, '/ month', 520, 280, { size: 70, weight: 600, color: '#1F7A4D' });
    txt(g, 'lower payment at 5.98%', 50, 400, { size: 46, weight: 600, color: '#2E3C35' });
  });
  const chqMat = new THREE.MeshStandardMaterial({ map: chqTex, emissiveMap: chqTex, emissive: new THREE.Color('#ffffff'), emissiveIntensity: 0.55, roughness: 0.7, side: THREE.DoubleSide });
  const chq = new THREE.Mesh(new THREE.PlaneGeometry(1.25, 0.574), chqMat); chq.castShadow = true; scene.add(chq);
  const chqLight = new THREE.PointLight(C.positive, 0, 3.5, 2); scene.add(chqLight);

  // rate path: schematic between claimed points (no intermediate values are shown)
  const HOVER = new THREE.Vector3(0.1, 2.75, 2.7);
  const T_DOWN = [1.1, 3.3], T_UP = [5.5, 7.4];
  const rateAt = (t) => t < T_DOWN[1] ? mix(7.62, 5.98, ease(t, ...T_DOWN)) : mix(5.98, 7.03, ease(t, ...T_UP));
  let lastKey = '';
  const grey = new THREE.Color('#8A8F98'), white = new THREE.Color('#ffffff');

  function update(t) {
    // camera: slow push-in and drift
    const k = ease(t, 0, duration);
    camera.position.set(mix(-1.3, -0.6, k), mix(2.2, 2.0, k), mix(10.2, 9.0, k));
    camera.lookAt(mix(-0.5, -0.35, k), 1.55, 0);
    const rate = rateAt(t);
    // sign face state (redraw only when text changes)
    let st;
    if (t < T_DOWN[0] + 0.05) st = { big: '7.62%', date: 'OCT 2023', sub: 'when Nora borrowed', col: C.warn };
    else if (t < T_DOWN[1]) st = { big: '···', date: '', sub: '', col: C.muted };
    else if (t < T_UP[0]) st = { big: '5.98%', date: 'WEEK ENDING FEB 26, 2026', sub: 'lowest since Sept 2022', col: C.positive };
    else if (t < T_UP[1]) st = { big: '···', date: '', sub: '', col: C.muted };
    else st = { big: '7.03%', date: 'WEEK ENDING SEP 24, 2026', sub: 'above 7% · first since Jan 2025', col: C.negative };
    st.ghost = t >= T_DOWN[1];
    const key = st.big + st.date + st.ghost;
    if (key !== lastKey) { Object.assign(state, st); faceTex.userData.redraw(drawFace); lastKey = key; }
    // pointer and band on the scale
    const py = sy(rate), p = texToLocal(380, py); ptr.position.set(p.x + 0.02, p.y, 0.06);
    const top = texToLocal(0, sy(7.62)).y, yb = p.y;
    const bh = Math.max(0.001, top - yb); band.scale.y = bh; band.position.set(texToLocal(330, 0).x, yb + bh / 2, 0.04);
    const open = clamp((7.62 - rate) / (7.62 - 5.98)); // 1 at the 2026 low
    band.material.opacity = 0.9 * clamp(open * 1.5) * (1 - 0.8 * ease(t, 5.7, 6.4)); band.material.emissiveIntensity = 1.4 * (1 - 0.8 * ease(t, 5.7, 6.4)); glow.intensity = 3 * open;

    // cheque: rises out of the mailbox while the rate is low, greys and drops back as the rate climbs past 7%
    const up = easeOut(t, 2.2, 3.6), fall = ease(t, 6.3, 7.4), greyK = ease(t, 5.7, 6.4);
    const mbw = new THREE.Vector3(MB.x, 1.25, MB.z);
    const hover = HOVER;
    const pos = mbw.clone().lerp(hover, up * (1 - fall));
    pos.y += Math.sin(t * 2.4) * 0.04 * up * (1 - fall);
    chq.position.copy(pos);
    const sc = clamp(0.15 + 0.85 * up) * (1 - 0.85 * fall);
    chq.scale.setScalar(Math.max(0.01, sc));
    chq.visible = up > 0.01 && fall < 0.98;
    chq.rotation.set(-0.12 + fall * -1.0, 0.1 + Math.sin(t * 1.3) * 0.05, Math.sin(t * 1.7) * 0.03 * (1 - fall));
    chqMat.color.copy(white).lerp(grey, greyK); chqMat.emissiveIntensity = 0.55 * (1 - greyK) + 0.08;
    chqLight.position.copy(pos).add(new THREE.Vector3(0, 0, 0.5)); chqLight.intensity = 5 * up * (1 - greyK);
    // mailbox flag: up while the offer is "out", down after it drops back
    const fl = 1 - fall; flag.position.set(0.19, 1.16 + 0.14 * fl, 0.12); flag.rotation.x = (1 - fl) * -1.4;
  }

  function overlay(ctx, t, P) {
    chrome(ctx, t, { illus: true, source: 'Rates: Freddie Mac PMMS via FRED (weekly). Nora: illustrative borrower built from CFPB HMDA 2025 medians.' });
    // captions (bottom, flat)
    const cap = (s, a, b, col = C.ink) => { const al = Math.min(ease(t, a, a + 0.35), 1 - ease(t, b - 0.3, b)); label(ctx, s, W / 2, 640, { size: 30, weight: 600, color: col, align: 'center', alpha: al }); };
    cap('October 2023: Nora borrows at 7.62%', 0.2, 2.2);
    cap('In February 2026 the average rate fell to 5.98%', 2.3, 4.0);
    cap('At that rate Nora could have paid $459 less a month', 4.0, 5.7, C.positive);
    cap("She didn't take it.", 5.7, 7.3);
    cap('By late September 2026 the rate was back above 7%', 7.4, 9.2, C.negative);
    const m = P(new THREE.Vector3(-0.35, 1.5, 3.1));
    label(ctx, 'offer not taken', m.x + 70, m.y + 10, { size: 24, weight: 600, color: C.muted, alpha: ease(t, 7.2, 7.7) });
  }

  return { duration, update, overlay, stripTimes: [0.8, 2.6, 4.4, 6.0, 7.0, 8.6], posterTime: 4.6 };
}
