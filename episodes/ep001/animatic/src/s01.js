// S01 · The week rates bottomed. Kết hợp H3 -> H1 -> H3 (signed SF1), every action anchored (anchors.json).
import { THREE, C, W, H, DATA, CL, text, chrome, line, rect, dot, hatch, strike, ease, easeOut, mix, canvasTex, ptxt, mat, box, pm , CLY } from './engine.js';
import { kitchen, paymentStack, rateLine, PL } from './common.js';

export const uses3d = true;

export function build({ scene, camera, renderer, T }) {
  const F = DATA.f1, wk = F.weeks, N = wk.length;
  const a = (id) => T.a(id);
  const tDraw = a('draw'), tLow = a('low'), tSince = a('since'), tK = a('kitchen'), tRate = a('rate'), tLift = a('lift'),
    tGrey = a('grey'), tDrop = a('drop'), tC = a('chart'), tAbove = a('above7'), tSince7 = a('since7');
  const X0 = 190, X1 = 1380, YB = 780, R0 = 5.8, R1 = 7.9, YT = 250;
  const xOf = (i) => X0 + (i / (N - 1)) * (X1 - X0);
  const yOf = (r) => YB - ((r - R0) / (R1 - R0)) * (YB - YT);
  const iLow = wk.findIndex((w) => w.d === F.low), iLast = wk.findIndex((w) => w.d === F.lastIn), iEnd = N - 1;
  const iFirst = wk.findIndex((w) => w.in);
  const i7 = wk.findIndex((w, i) => i > iLow && w.r > 7); // first week back above 7%
  // head: draw to the low by the keyword "5.98"; after the cut, climb so the line crosses 7% at "above 7"
  const climbEnd = Math.min(T.dur - 1.2, tAbove + 1.2 * (iEnd - i7) / Math.max(1, i7 - iLow) + 0.8);
  const head = (t) => t < tC ? ease(t, tDraw, tLow) * iLow
    : iLow + (t < tAbove ? ease(t, tC + 0.2, tAbove) * (i7 - iLow) : (i7 - iLow) + ease(t, tAbove, climbEnd) * (iEnd - i7));
  const closeAt = tC + 0.2 + (tAbove - tC - 0.2) * ((iLast + 1 - iLow) / Math.max(1, i7 - iLow));

  function chart(ctx, t) {
    const hd = head(t);
    const a0 = easeOut(t, 0, 0.4);
    text(ctx, 'US ' + CL('term30') + '-year mortgage rate, weekly', 96, 128, 'head', { alpha: a0 });
    text(ctx, 'latest: week ending ' + CL('anchor_date'), 96, 190, 'note', { color: C.muted, alpha: easeOut(t, climbEnd - 0.4, climbEnd) });
    line(ctx, [[X0, YB], [X1, YB]], C.grid, 3);
    const ticks = [['2025-08', 'Aug ' + CL('y2025')], ['2025-11', 'Nov'], ['2026-02', 'Feb ' + CLY('y2026', '2026')], ['2026-05', 'May'], ['2026-08', 'Aug']];
    for (const [m, s] of ticks) { const i = wk.findIndex((w) => w.d.slice(0, 7) === m); const x = xOf(i); line(ctx, [[x, YB], [x, YB + 14]], C.grid, 3); text(ctx, s, x, YB + 60, 'note', { color: C.muted, align: 'center' }); }
    const xa = xOf(iFirst - 0.5), xb = xOf(Math.min(iLast + 0.5, hd)), yT = yOf(F.thr);
    const closed = ease(t, closeAt, closeAt + 0.6);
    if (hd >= iFirst - 0.5) { rect(ctx, xa, yT, Math.max(0, xb - xa), YB - yT, C.accent, mix(0.2, 0.08, closed)); if (closed > 0) hatch(ctx, xa, yT, xb - xa, YB - yT, C.muted, 0.25 * closed, 22, 3); }
    line(ctx, [[X0, yOf(7)], [X1, yOf(7)]], C.grid, 3);
    text(ctx, CL('seven') + '%', X0 - 20, yOf(7) + 15, 'note', { color: C.muted, align: 'right' });
    const aN = easeOut(t, 0.4, 0.9);
    line(ctx, [[X0, yOf(F.rOld)], [X1, yOf(F.rOld)]], C.muted, 4, { dash: [14, 12], alpha: aN });
    dot(ctx, X1 + 34, yOf(F.rOld) - 15, 15, C.positive, aN);
    text(ctx, 'Nora ' + CL('r_old'), X1 + 60, yOf(F.rOld), 'label', { alpha: aN });
    line(ctx, [[X0, yT], [X1, yT]], C.accent, 4, { dash: [6, 10], alpha: aN });
    text(ctx, CL('s10') + ' percentage point', X1 + 24, yT + 12, 'note', { color: C.accent, alpha: aN });
    text(ctx, "below Nora's rate", X1 + 24, yT + 60, 'note', { color: C.accent, alpha: aN });
    const aW = easeOut(t, tDraw + 2.5, tDraw + 3.0);
    text(ctx, 'the window', xOf(iFirst) + 20, YB - 28, 'label', { color: C.accent, alpha: aW * (1 - closed) });
    line(ctx, [[xOf(iLast + 0.5), yT], [xOf(iLast + 0.5), YB]], C.ink, 3, { alpha: closed });
    text(ctx, 'window closed', xOf(iFirst) + 20, YB - 28, 'label', { color: C.ink, alpha: closed });
    text(ctx, 'Closed after the week ending ' + CL('cut1_last_2026'), W / 2, 900, 'label', { align: 'center', alpha: closed });
    const h = rateLine(ctx, wk, xOf, yOf, hd); if (h) dot(ctx, h[0], h[1], 11, C.accent);
    const aL = easeOut(t, tLow - 0.2, tLow + 0.3), aL2 = aL * (1 - ease(t, tC + 0.5, tC + 1.0)), xl = xOf(iLow), yl = yOf(wk[iLow].r), cx = 780;
    dot(ctx, xl, yl, 15, C.ink, aL);
    line(ctx, [[xl, yl - 22], [xl, 450]], C.ink, 3, { alpha: aL2 });
    text(ctx, CL('low2026'), cx, 410, 'number', { align: 'center', alpha: aL, plate: PL });
    text(ctx, 'week ending ' + CL('low2026_date'), cx, 480, 'note', { align: 'center', color: C.ink, alpha: aL2, plate: PL });
    text(ctx, 'lowest since ' + CL('low2026_since'), cx, 532, 'note', { align: 'center', color: C.muted, alpha: easeOut(t, tSince, tSince + 0.4) * aL2 / Math.max(aL, 1e-6), plate: PL });
    const aE = easeOut(t, tAbove, tAbove + 0.4), ye = yOf(wk[Math.min(iEnd, Math.floor(hd))].r);
    text(ctx, CL('r_today'), X1 + 24, yOf(wk[iEnd].r) + 42, 'number', { color: C.negative, alpha: easeOut(t, climbEnd - 0.3, climbEnd) });
    text(ctx, 'Back above ' + CL('seven') + '%', W / 2, 972, 'caption', { align: 'center', alpha: aE });
    text(ctx, 'first time since ' + CL('first7_since'), W / 2, 1016, 'note', { align: 'center', color: C.muted, alpha: easeOut(t, tSince7, tSince7 + 0.4) });
    chrome(ctx, { illus: 0 });
    text(ctx, 'Source: Freddie Mac weekly survey, via FRED (St. Louis Fed data)', 96, 1016, 'note', { color: C.muted, alpha: 1 - aE });
  }

  // ---- H1 kitchen (SF1) ----
  kitchen(scene, renderer, { w: 16, d: 8, key: 70 });
  const folderTex = canvasTex(1024, 720, (g, w, h) => {
    g.fillStyle = '#E9E2D2'; g.fillRect(0, 0, w, h); g.fillStyle = '#2E3440'; g.fillRect(0, 0, w, 150);
    ptxt(g, "NORA'S LOAN", 50, 105, { size: 76, weight: 700, color: '#FFFFFF' });
    ptxt(g, CL('r_old'), 50, 420, { size: 250, weight: 700, color: '#20242C' });
    ptxt(g, CL('oct2023'), 56, 560, { size: 76, weight: 600, color: '#4B5563' });
  });
  const fm = mat('#D8CFBC');
  const folder = box(2.4, 0.04, 1.69, [fm, fm, pm(folderTex), fm, fm, fm]); folder.position.set(-1.75, 0.02, 0.55); folder.rotation.y = 0.12; scene.add(folder);
  const st = paymentStack(scene, { total: F.oldPayment, slab: F.savLow });
  const lift = (t) => easeOut(t, tLift, tLift + 0.8) * (1 - ease(t, tDrop - 0.5, tDrop + 0.1));
  function update(t) {
    const k = ease(t, tK, tC);
    camera.position.set(mix(0.2, 0.05, k), mix(3.0, 2.85, k), mix(9.4, 8.6, k)); camera.lookAt(-0.1, 0.95, 0);
    const on = easeOut(t, tLift, tLift + 0.6) * (1 - ease(t, tGrey, tGrey + 0.4)), gk = ease(t, tGrey, tGrey + 0.4);
    st.set(lift(t), on, gk);
  }
  function kitchenOverlay(ctx, t, P) {
    const a1 = easeOut(t, tK, tK + 0.3);
    const bt = P(new THREE.Vector3(st.x, st.hBase + st.hSlab, st.z + st.SD / 2));
    const aP = a1 * (1 - ease(t, tLift, tLift + 0.3));
    text(ctx, "Nora's monthly payment", bt.x, 214, 'label', { align: 'center', alpha: aP, shadow: true });
    const f = P(new THREE.Vector3(-1.75, 0.05, 1.4));
    const aR = easeOut(t, tRate - 0.2, tRate + 0.3);
    text(ctx, "Nora's loan", f.x, f.y + 60, 'label', { align: 'center', alpha: a1, shadow: true });
    text(ctx, CL('r_old') + ' since ' + CL('oct2023'), f.x, f.y + 116, 'label', { align: 'center', color: C.warn, alpha: aR, plate: PL });
    const sl = P(new THREE.Vector3(st.x - st.SW / 2, st.slabY(lift(t)), st.z + st.SD / 2)), lx = sl.x - 40;
    const aS = easeOut(t, tLift + 0.3, tLift + 0.7), gk = ease(t, tGrey, tGrey + 0.4);
    const w459 = text(ctx, CL('sav_low2026_median') + ' a month less', lx, sl.y + 10, 'number', { align: 'right', color: gk > 0.5 ? C.muted : C.positive, alpha: aS, shadow: true });
    text(ctx, 'at the ' + CL('low2026') + ' rate', lx, sl.y + 70, 'label', { align: 'right', alpha: aS * (1 - gk), shadow: true });
    if (gk > 0) strike(ctx, lx - w459 - 10, sl.y - 20, lx + 10, C.negative, gk);
    text(ctx, "She didn't take it.", 1580, 620, 'caption', { align: 'center', alpha: easeOut(t, tGrey, tGrey + 0.3), plate: 'rgba(14,17,22,0.8)', sent: true });
    chrome(ctx, { illus: 1, source: 'Nora is illustrative. Dollars of the day = not adjusted for inflation.', plate: true });
  }
  return {
    mode: (t) => (t >= tK && t < tC ? '3d' : '2d'),
    update,
    overlay: (ctx, t, P, m) => (m === '3d' ? kitchenOverlay(ctx, t, P) : chart(ctx, t)),
    stripTimes: [tLow - 1.5, tSince + 1, tRate + 1, tLift + 1.4, tDrop + 0.3, T.dur - 0.2],
    hardTime: T.dur - 0.1,
  };
}
