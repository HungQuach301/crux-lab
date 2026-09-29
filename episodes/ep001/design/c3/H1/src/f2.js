// F2 · Break-even moves from month 24 to month 30. A ream of paper = the $5,124 loan costs; one $221 cash bundle per
// month stacks beside it on the same scale (height ∝ dollars). At month 24 the column is level with the ream, but a red
// sheet "+$1,133 more owed" lands on the ream; six more bundles (month 30) are needed.
// Claims: cost_median $5,124, sav_median $221, be_simple_median 24, gap24 $1,133, be_bal_median 30.
// The red layer's thickness month by month comes from model/refi.py (balance_after, same inputs as the median
// character: $375,000 at 7.62%, 35 payments made, new 30-year loan at 7.03%); only the month-24 value is printed.
import { THREE, C, W, H, canvasTex, txt, label, chrome, badge, mat, box, ease, easeOut, back, lin, mix, clamp, strike } from './common.js';

const GAP = [0, 42, 85, 128, 171, 215, 259, 304, 349, 394, 440, 487, 534, 581, 629, 677, 726, 775, 825, 875, 926, 977, 1028, 1080, 1133, 1186, 1240, 1294, 1348, 1403, 1459];
const COST = 5123.53, SAV = 221.30;

export function build({ scene, camera, renderer }) {
  const duration = 10.0;
  scene.background = new THREE.Color('#0E1116');
  renderer.toneMappingExposure = 1.05;
  const K = 0.1 / SAV; // scene units per dollar (one $221 bundle = 0.1)

  scene.add(new THREE.HemisphereLight('#8FA3C8', '#1A1410', 0.5));
  const key = new THREE.SpotLight('#FFE2BC', 60, 20, 0.62, 0.55, 1.4); key.position.set(-1.0, 7.5, 3.2); key.target.position.set(0, 1, 0);
  key.castShadow = true; key.shadow.mapSize.set(1024, 1024); key.shadow.bias = -0.0005; scene.add(key, key.target);
  const rim = new THREE.DirectionalLight('#A9B6CF', 0.25); rim.position.set(5, 3, -4); scene.add(rim);

  // table (wood planks via canvas texture) and back wall
  const woodTex = canvasTex(1024, 1024, (g, w, h) => {
    g.fillStyle = '#5E412D'; g.fillRect(0, 0, w, h);
    for (let i = 0; i < 8; i++) { g.fillStyle = i % 2 ? '#62442F' : '#5A3E2A'; g.fillRect(0, i * 128, w, 126); g.fillStyle = '#3B281C'; g.fillRect(0, i * 128 + 126, w, 2); }
    g.globalAlpha = 0.12; g.strokeStyle = '#2A1C12';
    for (let i = 0; i < 160; i++) { const y = (i * 37) % h; g.beginPath(); g.moveTo(0, y); g.bezierCurveTo(w * 0.3, y + 6, w * 0.6, y - 6, w, y + 3); g.stroke(); }
  });
  woodTex.wrapS = woodTex.wrapT = THREE.RepeatWrapping; woodTex.repeat.set(2, 2);
  const table = new THREE.Mesh(new THREE.BoxGeometry(14, 0.2, 7), new THREE.MeshStandardMaterial({ map: woodTex, roughness: 0.65 }));
  table.position.set(0, -0.1, 0); table.receiveShadow = true; scene.add(table);
  const wall = new THREE.Mesh(new THREE.PlaneGeometry(30, 12), mat('#1A1E26', { roughness: 1 })); wall.position.set(0, 4, -3.2); wall.receiveShadow = true; scene.add(wall);

  // ---- the bill: a ream whose height is $5,124 ----
  const BX = -1.05, SX = 1.05, FW = 1.5, FD = 1.1;
  const edgeTex = canvasTex(512, 512, (g, w, h) => { g.fillStyle = '#EFEBE2'; g.fillRect(0, 0, w, h); for (let y = 0; y < h; y += 6) { g.fillStyle = y % 12 ? '#DCD6C8' : '#E6E1D5'; g.fillRect(0, y, w, 2); } });
  edgeTex.wrapT = THREE.RepeatWrapping;
  const billH = COST * K;
  const billFront = canvasTex(768, 1186, (g, w, h) => {
    g.fillStyle = '#EFEBE2'; g.fillRect(0, 0, w, h); for (let y = 0; y < h; y += 7) { g.fillStyle = '#DCD6C8'; g.fillRect(0, y, w, 2); }
    g.fillStyle = C.negative; g.fillRect(0, h * 0.36, w, h * 0.28);
    txt(g, 'LOAN COSTS', w / 2, h * 0.36 + 110, { size: 70, weight: 700, color: '#FFFFFF', align: 'center' });
    txt(g, '$5,124', w / 2, h * 0.36 + 270, { size: 150, weight: 700, color: '#FFFFFF', align: 'center' });
  });
  const invoiceTop = canvasTex(1024, 750, (g, w, h) => {
    g.fillStyle = '#F7F4EC'; g.fillRect(0, 0, w, h);
    txt(g, 'REFINANCE OFFER — CLOSING', 60, 100, { size: 44, weight: 700, color: '#20242C' });
    g.fillStyle = '#C9C3B5'; for (let i = 0; i < 6; i++) g.fillRect(60, 160 + i * 60, 560 - (i % 3) * 90, 14);
    txt(g, 'Loan costs', 60, 620, { size: 52, weight: 600, color: '#20242C' });
    txt(g, '$5,124', w - 60, 640, { size: 110, weight: 700, color: C.negative, align: 'right' });
  });
  const pm = (map, o = {}) => new THREE.MeshStandardMaterial({ map, roughness: 0.92, ...o });
  const bill = new THREE.Mesh(new THREE.BoxGeometry(FW, billH, FD), [pm(edgeTex), pm(edgeTex), pm(invoiceTop), pm(edgeTex), pm(billFront), pm(edgeTex)]);
  bill.position.set(BX, billH / 2, 0); bill.castShadow = bill.receiveShadow = true; scene.add(bill);

  // ---- the hidden part: red sheets on top of the ream (what is still owed beyond the old loan) ----
  const redFront = canvasTex(768, 256, (g, w, h) => {
    g.fillStyle = '#C8383D'; g.fillRect(0, 0, w, h);
    for (let y = 0; y < h; y += 8) { g.fillStyle = '#B53035'; g.fillRect(0, y, w, 2); }
    txt(g, '+$1,133 more owed', w / 2, h / 2 + 30, { size: 78, weight: 700, color: '#FFFFFF', align: 'center' });
  });
  const redPlain = mat('#C8383D', { roughness: 0.9 });
  const red = new THREE.Mesh(new THREE.BoxGeometry(FW + 0.02, 1, FD + 0.02), [redPlain, redPlain, redPlain, redPlain, pm(redFront), redPlain]);
  red.castShadow = true; scene.add(red);
  const red2 = new THREE.Mesh(new THREE.BoxGeometry(FW + 0.02, 1, FD + 0.02), mat('#B8343A', { roughness: 0.9 })); red2.castShadow = true; scene.add(red2);

  // ---- $221 bundles (one per month) ----
  const bandTex = canvasTex(512, 64, (g, w, h) => {
    g.fillStyle = '#DCE9DF'; g.fillRect(0, 0, w, h); for (let y = 0; y < h; y += 5) { g.fillStyle = '#B9CFBF'; g.fillRect(0, y, w, 1); }
    g.fillStyle = C.warn; g.fillRect(w / 2 - 90, 0, 180, h); txt(g, '$221', w / 2, 50, { size: 44, weight: 700, color: '#1B1F26', align: 'center' });
  });
  const noteTop = canvasTex(512, 256, (g, w, h) => {
    g.fillStyle = '#D5E6D8'; g.fillRect(0, 0, w, h); g.strokeStyle = '#6FA383'; g.lineWidth = 8; g.strokeRect(12, 12, w - 24, h - 24);
    g.fillStyle = C.warn; g.fillRect(w / 2 - 70, 0, 140, h);
    txt(g, 'SAVED', w / 2, 118, { size: 40, weight: 700, color: '#1B1F26', align: 'center' }); txt(g, '$221', w / 2, 180, { size: 54, weight: 700, color: '#1B1F26', align: 'center' });
  });
  const sideM = mat('#BFD5C4', { roughness: 0.95 });
  const bmats = [sideM, sideM, pm(noteTop), sideM, pm(bandTex), sideM];
  const bundles = [];
  for (let i = 0; i < 30; i++) {
    const b = new THREE.Mesh(new THREE.BoxGeometry(FW * 0.96, 0.098, FD * 0.8), bmats); b.castShadow = b.receiveShadow = true;
    b.userData.jx = Math.sin(i * 12.9898) * 0.035; b.userData.jr = Math.sin(i * 78.233) * 0.03; scene.add(b); bundles.push(b);
  }

  // ---- desk calendar (tent) ----
  const cal = new THREE.Group(); cal.position.set(3.0, 0, -0.9); cal.rotation.y = -0.35; scene.add(cal);
  let calMonth = -1;
  const calTex = canvasTex(512, 512, drawCal(0));
  function drawCal(m) {
    return (g, w, h) => {
      g.fillStyle = '#F7F4EC'; g.fillRect(0, 0, w, h); g.fillStyle = '#2E3440'; g.fillRect(0, 0, w, 110);
      txt(g, 'MONTH', w / 2, 80, { size: 60, weight: 700, color: '#FFFFFF', align: 'center' });
      txt(g, String(m), w / 2, 390, { size: 250, weight: 700, color: m >= 30 ? '#1F7A4D' : '#20242C', align: 'center' });
      txt(g, 'after refinancing', w / 2, 470, { size: 38, weight: 600, color: '#6B7280', align: 'center' });
    };
  }
  const page = new THREE.Mesh(new THREE.PlaneGeometry(1.3, 1.3), new THREE.MeshStandardMaterial({ map: calTex, roughness: 0.9 }));
  page.position.set(0, 0.65, 0.2); page.rotation.x = -0.28; page.castShadow = true; cal.add(page);
  const backP = box(1.3, 1.3, 0.02, mat('#2E3440')); backP.position.set(0, 0.65, -0.18); backP.rotation.x = 0.28; cal.add(backP);
  const ring = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 1.2, 8), mat('#9AA4B2', { metalness: 0.8, roughness: 0.3 })); ring.rotation.z = Math.PI / 2; ring.position.set(0, 1.27, 0.01); cal.add(ring);

  // ---- level line (a laser line across both stacks) ----
  const laser = new THREE.Mesh(new THREE.BoxGeometry(4.3, 0.018, 0.018), new THREE.MeshBasicMaterial({ color: '#FFFFFF', transparent: true }));
  scene.add(laser);

  // month clock: 1..24 in [0.8, 4.8], hold, 25..30 in [7.3, 9.0]
  const monthAt = (t) => t < 0.8 ? 0 : t < 4.8 ? (t - 0.8) / 4.0 * 24 : t < 7.3 ? 24 : Math.min(30, 24 + (t - 7.3) / 1.7 * 6);
  const dropTime = (i) => i < 24 ? 0.8 + (i + 1) / 24 * 4.0 - 4.0 / 24 : 7.3 + (i - 23) / 6 * 1.7 - 1.7 / 6; // bundle i (0-based) lands at month i+1
  const REVEAL = [5.9, 6.7];

  function gapAt(mf) { const a = Math.floor(mf), b = Math.min(30, a + 1); return mix(GAP[a], GAP[b], mf - a); }

  function update(t) {
    const k = ease(t, 0, duration);
    camera.position.set(mix(0.9, 0.3, k), mix(3.4, 3.1, k), mix(8.6, 7.8, k));
    camera.lookAt(0.35, 1.6, 0);
    const mf = monthAt(t), m = Math.floor(mf + 1e-6);
    if (m !== calMonth) { calTex.userData.redraw(drawCal(m)); calMonth = m; }
    bundles.forEach((b, i) => {
      const td = dropTime(i), land = easeOut(t, td - 0.16, td);
      b.visible = t >= td - 0.16;
      const y = 0.049 + i * 0.1;
      b.position.set(SX + b.userData.jx, y + (1 - land) * 0.9, 0.05 + b.userData.jx * 0.5);
      b.rotation.y = b.userData.jr + (1 - land) * 0.4;
    });
    // red layer: revealed at month 24, then follows the model's gap
    const rv = back(t, ...REVEAL);
    const gap = gapAt(Math.max(24, mf));
    const rh = Math.max(0.001, gap * K);
    red.visible = t >= REVEAL[0];
    const r1 = 1133 * K, r2 = Math.max(0.001, rh - r1);
    red.scale.y = r1; red.position.set(BX + (1 - clamp(rv)) * 2.2, billH + r1 / 2 + (1 - clamp(rv)) * 1.2, 0);
    red.rotation.z = (1 - clamp(rv)) * -0.25;
    red2.visible = gap > 1134; red2.scale.y = r2; red2.position.set(BX, billH + r1 + r2 / 2, 0);
    // laser: at the ream top during 24-check, then at ream+red, green at month 30
    const lvl = t < REVEAL[0] ? billH : billH + rh * clamp(rv);
    laser.position.set(0, lvl + 0.01, FD / 2 + 0.02);
    laser.material.opacity = ease(t, 4.3, 4.8) * (t < REVEAL[0] ? 1 : 0.85);
    laser.material.color.set(t > 8.95 ? C.positive : t > REVEAL[0] ? C.negative : '#FFFFFF');
  }

  function overlay(ctx, t, P) {
    chrome(ctx, t, { illus: true, source: 'Loan costs: CFPB HMDA 2025 median. Savings and balance: Crux model (model/refi.py). Nora is illustrative.' });
    label(ctx, "Nora's refinance", 48, 56, { size: 30, weight: 700, color: C.ink, alpha: 1 });
    const bt = P(new THREE.Vector3(BX, billH, FD / 2)), st = P(new THREE.Vector3(SX, 0, FD / 2));
    const a0 = ease(t, 0.1, 0.6);
    label(ctx, 'one-time loan costs', bt.x, bt.y - 34, { size: 24, weight: 600, color: C.ink, align: 'center', alpha: a0 * (1 - ease(t, 5.8, 6.1)) });
    const mf = Math.min(30, Math.floor(0.0001 + (t < 0.8 ? 0 : t < 4.8 ? (t - 0.8) / 4.0 * 24 : t < 7.3 ? 24 : 24 + (t - 7.3) / 1.7 * 6)));
    const colTop = P(new THREE.Vector3(SX, Math.max(0.1, mf * 0.1), FD / 2));
    label(ctx, '+$221 saved each month', colTop.x, colTop.y - 30, { size: 24, weight: 700, color: C.positive, align: 'center', alpha: ease(t, 0.8, 1.2) * (1 - ease(t, 4.6, 4.9)) });
    // the simple division, then struck
    const d = ease(t, 4.8, 5.2);
    const lv = P(new THREE.Vector3(0, billH, 0));
    label(ctx, '$5,124 ÷ $221 a month → 24 months', W / 2, 108, { size: 40, weight: 700, color: C.ink, align: 'center', alpha: d });
    if (t > 6.2) { const w = 620; strike(ctx, W / 2 - w / 2, 94, W / 2 + w / 2, C.negative, ease(t, 6.2, 6.6)); }
    label(ctx, 'At month 24 she still owes $1,133 more than on the old loan', W / 2, 640, { size: 30, weight: 600, color: '#FF8A8E', align: 'center', alpha: ease(t, 6.3, 6.7) * (1 - ease(t, 7.9, 8.2)) });
    // result
    label(ctx, 'Break-even: month 30', W / 2, 640, { size: 46, weight: 700, color: C.positive, align: 'center', alpha: ease(t, 9.0, 9.4) });
    label(ctx, 'Month 24 — level?', W / 2, 640, { size: 34, weight: 600, color: C.ink, align: 'center', alpha: ease(t, 4.8, 5.1) * (1 - ease(t, 5.9, 6.2)) });
    label(ctx, 'So the savings must keep stacking…', W / 2, 640, { size: 30, weight: 600, color: C.ink, align: 'center', alpha: ease(t, 8.2, 8.4) * (1 - ease(t, 8.8, 9.0)) });
  }

  return { duration, update, overlay, stripTimes: [0.6, 3.0, 5.4, 6.9, 8.3, 9.7], posterTime: 6.95 };
}
