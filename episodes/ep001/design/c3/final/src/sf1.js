// SF1 · Cold open: the missed window (S01). D = H3 chart -> cut -> H1 kitchen -> cut -> H3 chart.
// A (H3): the weekly rate line draws down into the window (shaded ONLY over weeks at least 1 point below Nora's 7.62%)
//         and stops at the February 2026 low.
// B (H1): Nora's kitchen table. Her monthly payment is a stack of cash (height = dollars); the top $459 lifts out
//         (the saving the low rate offered), hangs, then greys and drops back: she didn't take it.
// C (H3): the line climbs out of the window (after the week ending July 23, 2026) and back above 7%.
// Claims: low2026 low2026_date low2026_since r_old oct2023 sav_low2026_median seven first7_since r_today anchor_date
//         cut1_last_2026 s10 (window test) y2025.
import { THREE, C, W, H, DATA, CL, text, measure, badge, chrome, line, rect, dot, hatch, strike, ease, easeOut, inout, lin, mix, clamp,
  canvasTex, ptxt, mat, box, pm, woodTable } from './engine.js';

export const uses3d = true;
const A_END = 4.6, B_END = 8.4, DUR = 12.0;

export function build({ scene, camera, renderer }) {
  const F = DATA.f1, wk = F.weeks, N = wk.length;
  // ---------------- H3 chart geometry ----------------
  const X0 = 190, X1 = 1380, YB = 780, R0 = 5.8, R1 = 7.9, YT = 250;
  const xOf = (i) => X0 + (i / (N - 1)) * (X1 - X0);
  const yOf = (r) => YB - ((r - R0) / (R1 - R0)) * (YB - YT);
  const iLow = wk.findIndex((w) => w.d === F.low), iLast = wk.findIndex((w) => w.d === F.lastIn), iEnd = N - 1;
  const iFirst = wk.findIndex((w) => w.in);
  // head position (fractional week index): A draws to the low; C draws from the low to the end
  const head = (t) => t < 0.5 ? 0 : t < 3.4 ? ease(t, 0.5, 3.4) * iLow : t < B_END ? iLow : iLow + ease(t, B_END + 0.2, 11.0) * (iEnd - iLow);

  function chart(ctx, t) {
    const hd = head(t);
    const a0 = easeOut(t, 0, 0.4);
    text(ctx, 'US 30-year mortgage rate, weekly', 96, 128, 'head', { alpha: a0 });
    text(ctx, 'latest: week ending ' + CL('anchor_date'), 96, 196, 'note', { color: C.muted, alpha: easeOut(t, 10.6, 11.0) });
    // axis + month labels (years named once each)
    line(ctx, [[X0, YB], [X1, YB]], C.grid, 3);
    const ticks = [['2025-08', 'Aug ' + CL('y2025')], ['2025-11', 'Nov'], ['2026-02', 'Feb 2026'], ['2026-05', 'May'], ['2026-08', 'Aug']];
    for (const [m, s] of ticks) {
      const i = wk.findIndex((w) => w.d.slice(0, 7) === m); const x = xOf(i);
      line(ctx, [[x, YB], [x, YB + 14]], C.grid, 3);
      text(ctx, s, x, YB + 66, 'note', { color: C.muted, align: 'center' });
    }
    // the window: shaded only over the weeks in it, revealed as the line reaches them
    const xa = xOf(iFirst - 0.5), xb = xOf(Math.min(iLast + 0.5, hd)), yT = yOf(F.thr);
    const closed = ease(t, 9.6, 10.2);
    if (hd >= iFirst - 0.5) {
      rect(ctx, xa, yT, Math.max(0, xb - xa), YB - yT, C.accent, mix(0.2, 0.08, closed));
      if (closed > 0) hatch(ctx, xa, yT, xb - xa, YB - yT, C.muted, 0.25 * closed, 22, 3);
    }
    // reference lines: 7% grid, Nora's rate, 1 point below Nora's rate
    line(ctx, [[X0, yOf(7)], [X1, yOf(7)]], C.grid, 3);
    text(ctx, CL('seven') + '%', X0 - 20, yOf(7) + 18, 'note', { color: C.muted, align: 'right' });
    const aN = easeOut(t, 0.2, 0.7);
    line(ctx, [[X0, yOf(F.rOld)], [X1, yOf(F.rOld)]], C.muted, 4, { dash: [14, 12], alpha: aN });
    dot(ctx, X1 + 34, yOf(F.rOld) - 18, 16, C.positive, aN);
    text(ctx, 'Nora ' + CL('r_old'), X1 + 62, yOf(F.rOld), 'label', { alpha: aN });
    line(ctx, [[X0, yT], [X1, yT]], C.accent, 4, { dash: [6, 10], alpha: aN });
    text(ctx, CL('s10') + ' percentage point', X1 + 24, yT + 14, 'note', { color: C.accent, alpha: aN });
    text(ctx, "below Nora's rate", X1 + 24, yT + 70, 'note', { color: C.accent, alpha: aN });
    // window label (inside the shaded weeks, under the line)
    const aW = easeOut(t, 1.2, 1.7);
    text(ctx, 'the window', xOf(iFirst) + 20, YB - 28, 'label', { color: C.accent, alpha: aW * (1 - closed) });
    line(ctx, [[xOf(iLast + 0.5), yT], [xOf(iLast + 0.5), YB]], C.ink, 3, { alpha: closed });
    text(ctx, 'window closed', xOf(iFirst) + 20, YB - 28, 'label', { color: C.ink, alpha: closed });
    text(ctx, 'The window closed after the week ending ' + CL('cut1_last_2026'), W / 2, 912, 'label', { align: 'center', alpha: closed });
    // rate line draws itself
    if (t >= 0.5) {
      const pts = []; const full = Math.floor(hd);
      for (let i = 0; i <= full; i++) pts.push([xOf(i), yOf(wk[i].r)]);
      if (hd > full && full + 1 < N) { const f = hd - full; pts.push([mix(xOf(full), xOf(full + 1), f), mix(yOf(wk[full].r), yOf(wk[full + 1].r), f)]); }
      if (pts.length === 1) pts.push(pts[0]);
      line(ctx, pts, C.accent, 7);
      const h = pts[pts.length - 1]; dot(ctx, h[0], h[1], 11, C.accent);
    }
    // low callout (above the window line, clear of the later climb)
    const aL = easeOut(t, 3.3, 3.8), aL2 = aL * (1 - ease(t, 9.3, 9.6)), xl = xOf(iLow), yl = yOf(wk[iLow].r), cx = 780;
    dot(ctx, xl, yl, 15, C.ink, aL);
    line(ctx, [[xl, yl - 22], [xl, yOf(F.thr) - 8]], C.ink, 3, { alpha: aL2 });
    line(ctx, [[xl, yl - 22], [xl, 450]], C.ink, 3, { alpha: aL * (1 - aL2 / Math.max(aL, 1e-6)) });
    const PL = 'rgba(14,17,22,0.92)';
    text(ctx, CL('low2026'), cx, 410, 'number', { align: 'center', alpha: aL, plate: PL });
    text(ctx, 'week ending ' + CL('low2026_date'), cx, 488, 'note', { align: 'center', color: C.ink, alpha: aL2, plate: PL });
    text(ctx, 'lowest since ' + CL('low2026_since'), cx, 542, 'note', { align: 'center', color: C.muted, alpha: aL2, plate: PL });
    // end: back above 7%
    const aE = easeOut(t, 10.8, 11.2), ye = yOf(wk[iEnd].r);
    dot(ctx, xOf(iEnd), ye, 15, C.ink, aE);
    text(ctx, CL('r_today'), X1 + 24, ye + 40, 'number', { color: C.negative, alpha: aE });
    text(ctx, 'Back above ' + CL('seven') + '%, first time since ' + CL('first7_since'), W / 2, 980, 'caption', { align: 'center', alpha: aE });
    chrome(ctx, { illus: aN, source: 'Source: Freddie Mac weekly rate survey, via FRED' });
  }

  // ---------------- H1 kitchen ----------------
  scene.background = new THREE.Color(C.bg);
  renderer.toneMappingExposure = 1.05;
  scene.add(new THREE.HemisphereLight('#8FA3C8', '#1A1410', 0.55));
  const key = new THREE.SpotLight('#FFE2BC', 70, 20, 0.6, 0.55, 1.4); key.position.set(-1.2, 7.5, 3.4); key.target.position.set(0.3, 0.8, 0);
  key.castShadow = true; key.shadow.mapSize.set(1024, 1024); key.shadow.bias = -0.0005; scene.add(key, key.target);
  const rim = new THREE.DirectionalLight('#A9B6CF', 0.3); rim.position.set(5, 3, -4); scene.add(rim);
  woodTable(scene);
  // Nora's loan folder (flat on the table)
  const folderTex = canvasTex(1024, 720, (g, w, h) => {
    g.fillStyle = '#E9E2D2'; g.fillRect(0, 0, w, h); g.fillStyle = '#2E3440'; g.fillRect(0, 0, w, 150);
    ptxt(g, "NORA'S LOAN", 50, 105, { size: 76, weight: 700, color: '#FFFFFF' });
    ptxt(g, CL('r_old'), 50, 420, { size: 250, weight: 700, color: '#20242C' });
    ptxt(g, CL('oct2023'), 56, 560, { size: 76, weight: 600, color: '#4B5563' });
    ptxt(g, 'ILLUSTRATIVE', w - 50, 660, { size: 50, weight: 700, color: '#9A6A00', align: 'right' });
  });
  const folder = box(2.4, 0.04, 1.69, [mat('#D8CFBC'), mat('#D8CFBC'), pm(folderTex), mat('#D8CFBC'), mat('#D8CFBC'), mat('#D8CFBC')]);
  folder.position.set(-1.75, 0.02, 0.55); folder.rotation.y = 0.12; scene.add(folder);
  // payment stack: height = Nora's monthly payment at 7.62% (dollars); the top slab = $459
  const K = 1.7 / F.oldPayment, SW = 1.5, SD = 1.0;
  const stackTex = canvasTex(512, 512, (g, w, h) => { g.fillStyle = C.cash; g.fillRect(0, 0, w, h); for (let y = 0; y < h; y += 5) { g.fillStyle = '#B9CFBF'; g.fillRect(0, y, w, 1); } g.fillStyle = C.cashBand; g.fillRect(w / 2 - 60, 0, 120, h); for (let y = 0; y < h; y += 64) { g.fillStyle = '#6E8A76'; g.fillRect(0, y, w, 4); } });
  stackTex.repeat.set(1, 2);
  stackTex.wrapT = THREE.RepeatWrapping;
  const topTex = canvasTex(512, 340, (g, w, h) => { g.fillStyle = '#D5E6D8'; g.fillRect(0, 0, w, h); g.strokeStyle = '#6FA383'; g.lineWidth = 10; g.strokeRect(14, 14, w - 28, h - 28); g.fillStyle = C.cashBand; g.fillRect(w / 2 - 60, 0, 120, h); });
  const side = pm(stackTex), topM = pm(topTex);
  const hBase = (F.oldPayment - F.savLow) * K, hSlab = F.savLow * K;
  const base = box(SW, hBase, SD, [side, side, topM, side, side, side]); base.position.set(1.1, hBase / 2, 0.2); scene.add(base);
  const slabMats = [0, 1, 2, 3, 4, 5].map((i) => new THREE.MeshStandardMaterial({ map: i === 2 ? topTex : stackTex, roughness: 0.9, emissive: new THREE.Color(C.positive), emissiveIntensity: 0 }));
  const slab = box(SW, hSlab, SD, slabMats); scene.add(slab);
  const glow = new THREE.PointLight(C.positive, 0, 4, 2); scene.add(glow);
  const grey = new THREE.Color('#7E838C'), white = new THREE.Color('#ffffff');
  const slabY = (t) => { const up = easeOut(t, 5.3, 6.1), dn = ease(t, 7.4, 8.0); return hBase + hSlab / 2 + 0.7 * up * (1 - dn); };
  function update(t) {
    const k = ease(t, A_END, B_END);
    camera.position.set(mix(0.2, 0.1, k), mix(3.0, 2.9, k), mix(9.4, 8.8, k)); camera.lookAt(-0.1, 0.95, 0);
    slab.position.set(1.1, slabY(t), 0.2); slab.rotation.y = 0.08 * easeOut(t, 5.3, 6.1) * (1 - ease(t, 7.4, 8.0));
    const on = easeOut(t, 5.3, 5.9) * (1 - ease(t, 7.0, 7.4)), gk = ease(t, 7.0, 7.4);
    slabMats.forEach((m) => { m.emissiveIntensity = 0.35 * on; m.color.copy(white).lerp(grey, gk); });
    glow.position.set(1.1, slabY(t) + 0.3, 1.2); glow.intensity = 6 * on;
  }
  function kitchenOverlay(ctx, t, P) {
    const a = easeOut(t, A_END, A_END + 0.3);
    const bt = P(new THREE.Vector3(1.1, hBase + hSlab, 0.2 + SD / 2));
    text(ctx, "Nora's monthly payment", bt.x, 214, 'label', { align: 'center', alpha: a * (1 - ease(t, 5.6, 5.9)), shadow: true });
    text(ctx, 'at ' + CL('r_old'), bt.x, 280, 'label', { align: 'center', color: C.muted, alpha: a * (1 - ease(t, 5.6, 5.9)), shadow: true });
    const sy = P(new THREE.Vector3(1.1, slabY(t) + hSlab / 2, 0.2 + SD / 2));
    const aS = easeOut(t, 5.8, 6.2);
    const gk = ease(t, 7.0, 7.4);
    const sl = P(new THREE.Vector3(1.1 - SW / 2, slabY(t), 0.2 + SD / 2)), lx = sl.x - 40;
    const w459 = text(ctx, CL('sav_low2026_median') + ' a month less', lx, sl.y + 10, 'number', { align: 'right', color: gk > 0.5 ? C.muted : C.positive, alpha: aS, shadow: true });
    text(ctx, 'if she had refinanced at ' + CL('low2026'), lx, sl.y + 80, 'label', { align: 'right', alpha: aS * (1 - gk), shadow: true });
    if (gk > 0) strike(ctx, lx - w459 - 10, sl.y - 25, lx + 10, C.negative, gk);
    const f = P(new THREE.Vector3(-1.75, 0.05, 1.4));
    text(ctx, "Nora's loan, " + CL('oct2023'), f.x, f.y + 70, 'label', { align: 'center', alpha: a, shadow: true });
    text(ctx, "She didn't take it.", W / 2, 968, 'caption', { align: 'center', alpha: easeOut(t, 6.8, 7.1), plate: 'rgba(14,17,22,0.8)' });
    chrome(ctx, { illus: 1, source: 'Nora is an illustrative borrower. Dollars of the day.', plate: true });
  }

  return {
    duration: DUR,
    mode: (t) => (t >= A_END && t < B_END ? '3d' : '2d'),
    update,
    overlay: (ctx, t, P, m) => (m === '3d' ? kitchenOverlay(ctx, t, P) : chart(ctx, t)),
    stripTimes: [1.2, 3.9, 4.9, 6.6, 8.1, 11.9],
    hardTime: 11.95,
  };
}
