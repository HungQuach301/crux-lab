// SF3 · Break-even moves from month 24 to month 30 (S09-S10). H1, one dollar scale for every object on the table:
//   ream   = loan costs $5,124 (paper)
//   column = one $221 cash bundle per month saved
//   two paper stacks = balance paid off since the refinance: old loan (if kept) vs new loan. The new loan pays down
//   more slowly (fresh 30-year clock), so its stack is shorter. At month 24 the difference ($1,133, hatched) is lifted
//   onto the ream: it is still owed on the new loan vs the old one, so it has to be earned back too. Six more bundles:
//   level at month 30.
// Claims: cost_median sav_median be_simple_median gap24 be_bal_median. Stack heights / the hatched slab after month
// 24 follow model/refi.py (data.js); only $1,133 is printed. Month track: 36 tiles, only 24 and 30 are numbered.
import { THREE, C, W, H, DATA, CL, text, measure, chrome, strike, ease, easeOut, back, mix, clamp, canvasTex, ptxt, mat, box, pm,
  woodTable, paperEdgeTex, owedTex, mark } from './engine.js';

export const uses3d = true;
const DUR = 12.0;

export function build({ scene, camera, renderer }) {
  const M = DATA.median;
  scene.background = new THREE.Color(C.bg);
  renderer.toneMappingExposure = 1.05;
  scene.add(new THREE.HemisphereLight('#8FA3C8', '#1A1410', 0.6));
  const key = new THREE.SpotLight('#FFE2BC', 110, 28, 0.7, 0.55, 1.3); key.position.set(-1.0, 9, 5); key.target.position.set(0, 1, 0);
  key.castShadow = true; key.shadow.mapSize.set(1024, 1024); key.shadow.bias = -0.0005; scene.add(key, key.target);
  const rim = new THREE.DirectionalLight('#A9B6CF', 0.35); rim.position.set(5, 4, -4); scene.add(rim);
  woodTable(scene, 18, 8);

  const K = 2.35 / 11000; // scene units per dollar, for EVERY object in this frame
  const FW = 1.25, FD = 0.95;
  const X = { bill: -1.25, sav: -3.3, old: 1.3, nw: 2.8 };
  // month clock: 1..24 in [0.8, 4.8]; hold; 25..30 in [7.2, 9.6]
  const monthAt = (t) => t < 0.8 ? 0 : t < 4.8 ? (t - 0.8) / 4.0 * 24 : t < 7.2 ? 24 : Math.min(30, 24 + (t - 7.2) / 2.4 * 6);
  const at = (arr, m) => { const a = Math.floor(m), b = Math.min(arr.length - 1, a + 1); return mix(arr[a], arr[b], m - a); };

  // ---- ream = loan costs ----
  const edge = paperEdgeTex(); edge.repeat.set(1, 3);
  const billH = M.cost * K;
  const front = canvasTex(640, Math.round(640 * billH / FW), (g, w, h) => {
    g.fillStyle = C.paper; g.fillRect(0, 0, w, h); for (let y = 0; y < h; y += 7) { g.fillStyle = C.paperLine; g.fillRect(0, y, w, 2); }
    g.fillStyle = '#2E3440'; g.fillRect(0, h * 0.18, w, h * 0.64);
    ptxt(g, 'LOAN COSTS', w / 2, h * 0.43, { size: 76, weight: 700, color: '#FFFFFF', align: 'center' });
    ptxt(g, CL('cost_median'), w / 2, h * 0.43 + 150, { size: 136, weight: 700, color: '#FFFFFF', align: 'center' });
  });
  const bill = box(FW, billH, FD, [pm(edge), pm(edge), pm(edge), pm(edge), pm(front), pm(edge)]); bill.position.set(X.bill, billH / 2, 0); scene.add(bill);

  // ---- $221 bundles ----
  const bandTex = canvasTex(512, 64, (g, w, h) => { g.fillStyle = C.cash; g.fillRect(0, 0, w, h); for (let y = 0; y < h; y += 5) { g.fillStyle = '#B9CFBF'; g.fillRect(0, y, w, 1); } g.fillStyle = C.cashBand; g.fillRect(w / 2 - 70, 0, 140, h); });
  const topTex = canvasTex(512, 384, (g, w, h) => { g.fillStyle = '#D5E6D8'; g.fillRect(0, 0, w, h); g.strokeStyle = '#6FA383'; g.lineWidth = 10; g.strokeRect(14, 14, w - 28, h - 28); g.fillStyle = C.cashBand; g.fillRect(w / 2 - 60, 0, 120, h); });
  const cs = mat(C.cashSide, { roughness: 0.95 });
  const bmats = [cs, cs, pm(topTex), cs, pm(bandTex), cs];
  const bt = M.sav * K;
  const bundles = [];
  for (let i = 0; i < 30; i++) {
    const b = new THREE.Mesh(new THREE.BoxGeometry(FW * 0.96, bt * 0.92, FD * 0.8), bmats); b.castShadow = b.receiveShadow = true;
    b.userData.jx = Math.sin(i * 12.9898) * 0.025; b.userData.jr = Math.sin(i * 78.233) * 0.03; scene.add(b); bundles.push(b);
  }
  const dropTime = (i) => i < 24 ? 0.8 + (i + 1) / 24 * 4.0 : 7.2 + (i - 23) / 6 * 2.4; // bundle i lands at month i+1

  // ---- balance paid off: two paper stacks ----
  const stackMat = (col) => { const t = paperEdgeTex(); t.repeat.set(1, 6); return new THREE.MeshStandardMaterial({ map: t, color: col, roughness: 0.9 }); };
  const oldS = box(FW * 0.9, 1, FD * 0.9, stackMat('#E4E6EA')); scene.add(oldS);
  const newS = box(FW * 0.9, 1, FD * 0.9, stackMat('#86A9F2')); scene.add(newS);
  // the difference (owed): hatched slab; and the empty outline it leaves on top of the new stack
  const ot = owedTex(); ot.repeat.set(2, 1);
  const owed = box(FW * 0.9 + 0.02, 1, FD * 0.9 + 0.02, new THREE.MeshStandardMaterial({ map: ot, roughness: 0.85 })); scene.add(owed);
  const ghost = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(FW * 0.9, 1, FD * 0.9)), new THREE.LineDashedMaterial({ color: C.negative, dashSize: 0.06, gapSize: 0.05 }));
  scene.add(ghost);

  // ---- month track: 36 tiles along the front edge ----
  const tiles = [];
  const tileOff = mat('#3A3F48'), tileOn = mat('#E9E2D2', { emissive: new THREE.Color('#8C7F5E'), emissiveIntensity: 0.25 }), tileLate = mat('#F3E3E1', { emissive: new THREE.Color(C.negative), emissiveIntensity: 0.25 });

  const laser = new THREE.Mesh(new THREE.BoxGeometry(2.3, 0.02, 0.02), new THREE.MeshBasicMaterial({ color: '#FFFFFF', transparent: true, opacity: 0 })); scene.add(laser);
  const REVEAL = [5.4, 6.1], MOVE = [6.5, 7.3];

  function owedState(t, m) {
    const g = at(M.gap, Math.max(0, m)) * K;
    const grow = easeOut(t, ...REVEAL), mv = ease(t, ...MOVE);
    const newTop = at(M.newPaid, m) * K;
    const from = new THREE.Vector3(X.nw, newTop + g / 2, 0), to = new THREE.Vector3(X.bill, billH + g / 2, 0);
    const p = from.clone().lerp(to, mv); p.y += Math.sin(mv * Math.PI) * 1.0;
    return { g, grow, mv, p, newTop };
  }
  function update(t) {
    const k = ease(t, 0, DUR);
    camera.position.set(mix(-0.2, -0.25, k), mix(2.4, 2.3, k), mix(8.7, 8.3, k)); camera.lookAt(-0.25, 1.12, 0);
    const m = monthAt(t);
    bundles.forEach((b, i) => {
      const td = dropTime(i), land = easeOut(t, td - 0.16, td);
      b.visible = t >= td - 0.16;
      b.position.set(X.sav + b.userData.jx, bt * (i + 0.5) + (1 - land) * 0.7, b.userData.jx * 0.5);
      b.rotation.y = b.userData.jr + (1 - land) * 0.35;
    });
    const ho = Math.max(0.001, at(M.oldPaid, m) * K), hn = Math.max(0.001, at(M.newPaid, m) * K);
    oldS.scale.y = ho; oldS.position.set(X.old, ho / 2, 0); newS.scale.y = hn; newS.position.set(X.nw, hn / 2, 0);
    const o = owedState(t, m);
    owed.visible = t >= REVEAL[0]; owed.scale.y = Math.max(0.001, o.g * (o.mv > 0 ? 1 : o.grow)); owed.position.copy(o.p);
    if (o.mv <= 0) owed.position.y = o.newTop + o.g * o.grow / 2;
    owed.rotation.z = Math.sin(o.mv * Math.PI) * 0.15;
    ghost.visible = o.mv > 0.05; ghost.scale.y = Math.max(0.001, o.g); ghost.position.set(X.nw, o.newTop + o.g / 2, 0); ghost.computeLineDistances();
    tiles.forEach((tl, i) => { tl.material = i + 1 <= m + 1e-6 ? (i + 1 > 24 ? tileLate : tileOn) : tileOff; });
    // level line from the ream (+ owed once it has landed) across to the savings column
    const lvl = billH + (o.mv >= 1 ? o.g : 0);
    laser.position.set((X.bill + X.sav) / 2, lvl + 0.012, FD / 2 + 0.03); laser.scale.x = 1.35;
    laser.material.opacity = ease(t, 4.5, 4.9) * (t > MOVE[0] && t < MOVE[1] ? 0 : 1);
    laser.material.color.set(t > 9.6 ? C.positive : t > MOVE[1] ? C.negative : '#FFFFFF');
  }

  function overlay(ctx, t, P) {
    const m = monthAt(t), o = owedState(t, m);
    // headline: the simple division, then struck; the answer
    const aD = easeOut(t, 4.8, 5.2);
    const wD = text(ctx, CL('cost_median') + ' ÷ ' + CL('sav_median') + ' a month = ' + CL('be_simple_median') + ' months', 96, 150, 'head', { alpha: aD * (1 - 0.5 * ease(t, 6.5, 6.9)) * (1 - ease(t, 9.4, 9.7)) });
    strike(ctx, 90, 125, 102 + wD, C.negative, ease(t, 6.5, 6.9) * (1 - ease(t, 9.4, 9.7)), 8);
    text(ctx, 'Break-even: month ' + CL('be_bal_median'), 96, 160, 'number', { color: C.positive, alpha: easeOut(t, 9.6, 10.0) });
    // labels above the objects
    const pb = P(new THREE.Vector3(X.bill, billH + (o.mv >= 1 ? o.g : 0), 0));
    const pb0 = P(new THREE.Vector3(X.bill, 0, FD / 2)), ps0 = P(new THREE.Vector3(X.sav, 0, FD / 2));
    text(ctx, 'loan costs', pb0.x, pb0.y + 58, 'label', { align: 'center', alpha: easeOut(t, 0.1, 0.5), shadow: true });
    const nB = Math.min(30, Math.floor(m + 1e-6));
    const ps = P(new THREE.Vector3(X.sav, Math.max(0.05, nB * bt), 0));
    text(ctx, '+' + CL('sav_median') + ' a month', ps0.x, ps0.y + 58, 'label', { align: 'center', color: '#8FE0B5', alpha: easeOut(t, 0.8, 1.2), shadow: true });
    const pst = P(new THREE.Vector3((X.old + X.nw) / 2, at(M.oldPaid, m) * K, 0));
    const aP = easeOut(t, 1.0, 1.4);
    text(ctx, 'balance paid off', pst.x, Math.min(pst.y - 96, 700), 'label', { align: 'center', alpha: aP, shadow: true });
    text(ctx, 'since refinancing', pst.x, Math.min(pst.y - 40, 756), 'note', { align: 'center', color: C.ink, alpha: aP, shadow: true });
    const po = P(new THREE.Vector3(X.old, 0, FD / 2)), pn = P(new THREE.Vector3(X.nw, 0, FD / 2));
    text(ctx, 'old loan', po.x, po.y + 58, 'label', { align: 'center', color: C.ink, alpha: aP, shadow: true });
    text(ctx, 'new loan', pn.x, pn.y + 58, 'label', { align: 'center', color: '#B9CFFA', alpha: aP, shadow: true });
    // the owed part: named when it appears (second headline row), then on the ream
    const aO = easeOut(t, 5.6, 6.0) * (1 - ease(t, 7.0, 7.3));
    const wO = text(ctx, CL('gap24') + ' still owed', 96, 268, 'number', { color: '#FF8A8E', alpha: aO, plate: 'rgba(14,17,22,0.85)' });
    text(ctx, 'on the new loan vs the old one', 96, 340, 'label', { alpha: aO, plate: 'rgba(14,17,22,0.85)' });
    const pr = P(new THREE.Vector3(X.bill, billH + o.g, 0));
    const aR = easeOut(t, 7.2, 7.6);
    text(ctx, '+ ' + CL('gap24') + ' still owed', pr.x, pr.y - 40, 'label', { align: 'center', color: '#FF8A8E', alpha: aR * (1 - ease(t, 9.3, 9.6)), shadow: true });
    text(ctx, 'loan costs', pr.x, pr.y - 96, 'label', { align: 'center', color: C.ink, alpha: easeOut(t, 9.6, 10.0), shadow: true });
    text(ctx, '+ still owed', pr.x, pr.y - 40, 'label', { align: 'center', color: '#FF8A8E', alpha: easeOut(t, 9.6, 10.0), shadow: true });
    // month ruler (flat): one tick per month, only claimed months numbered
    const RX0 = 330, RX1 = 1590, RY = 912, rx = (k) => RX0 + (k / 36) * (RX1 - RX0);
    const aRu = easeOut(t, 0.5, 0.9);
    ctx.save(); ctx.globalAlpha = aRu; ctx.fillStyle = C.grid; ctx.fillRect(RX0, RY, RX1 - RX0, 4); ctx.restore();
    for (let k = 1; k <= 36; k++) {
      const lit = k <= m + 1e-6; ctx.save(); ctx.globalAlpha = aRu; ctx.fillStyle = lit ? (k > 24 ? C.negative : C.ink) : C.grid;
      ctx.fillRect(rx(k) - 4, RY - (lit ? 30 : 16), 8, lit ? 30 : 16); ctx.restore();
    }
    text(ctx, 'months', RX1 + 24, RY + 4, 'note', { color: C.muted, alpha: aRu });
    text(ctx, CL('be_simple_median'), rx(24), RY + 62, 'label', { align: 'center', color: t > MOVE[0] ? C.muted : C.ink, alpha: easeOut(t, 4.6, 5.0) });
    if (t > MOVE[0]) strike(ctx, rx(24) - 38, RY + 42, rx(24) + 38, C.negative, ease(t, 6.5, 6.9), 6);
    text(ctx, CL('be_bal_median'), rx(30), RY + 62, 'label', { align: 'center', color: C.positive, alpha: easeOut(t, 9.6, 10.0) });
    chrome(ctx, { illus: 1, source: 'Nora (illustrative). Fees: 2025 median (HMDA). Dollars of the day.', plate: true });
  }

  return { duration: DUR, update, overlay, stripTimes: [0.4, 3.0, 5.0, 6.0, 7.4, 11.9], hardTime: 11.95 };
}
