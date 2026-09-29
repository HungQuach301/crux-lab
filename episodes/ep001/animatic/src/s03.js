// S03 · Near the top. Kết hợp: H3 2023 weekly line (Nora's dot at October 2023, near the 7.79% peak) -> cut ->
// H1 a street of ten houses bought in 2023; three light up, one of them Nora's (three in ten at 7% or more).
import { THREE, C, W, H, DATA, CL, text, chrome, line, dot, mark, ease, easeOut, back, mix, house , CLY } from './engine.js';
import { outdoors, rateLine, shadowAll, PL } from './common.js';
export const uses3d = true;

export function build({ scene, camera, renderer, T }) {
  const tD = T.a('draw'), tN = T.a('nora'), tP = T.a('peak'), tS = T.a('since'), tSt = T.a('street'), t3 = T.a('three'), tLb = T.a('label');
  const wk = DATA.w23.weeks, N = wk.length, iPk = wk.findIndex((w) => w.d === DATA.w23.peak);
  const iOct = wk.findIndex((w) => w.d.startsWith('2023-10'));
  const X0 = 220, X1 = 1500, YB = 800, R0 = 5.8, R1 = 8.1, YT = 280;
  const xOf = (i) => X0 + (i / (N - 1)) * (X1 - X0), yOf = (r) => YB - ((r - R0) / (R1 - R0)) * (YB - YT);
  const head = (t) => t < tN ? ease(t, tD, tN) * iOct : iOct + ease(t, tN, tP + 0.8) * (N - 1 - iOct);
  function chart(ctx, t) {
    const a0 = easeOut(t, 0, 0.4);
    text(ctx, 'US ' + CL('term30') + '-year mortgage rate, weekly, ' + CL('oct2023').slice(-4), 96, 128, 'head', { alpha: a0 });
    line(ctx, [[X0, YB], [X1, YB]], C.grid, 3);
    for (const [m, s] of [['2023-01', 'Jan'], ['2023-04', 'Apr'], ['2023-07', 'Jul'], ['2023-10', 'Oct']]) {
      const i = wk.findIndex((w) => w.d.slice(0, 7) === m); const x = xOf(i); line(ctx, [[x, YB], [x, YB + 14]], C.grid, 3); text(ctx, s, x, YB + 60, 'note', { color: C.muted, align: 'center' });
    }
    line(ctx, [[X0, yOf(7)], [X1, yOf(7)]], C.grid, 3);
    text(ctx, CL('seven') + '%', X0 - 20, yOf(7) + 15, 'note', { color: C.muted, align: 'right' });
    const h = rateLine(ctx, wk, xOf, yOf, head(t)); if (h) dot(ctx, h[0], h[1], 11, C.accent);
    const aN = easeOut(t, tN - 0.1, tN + 0.5), xN = mix(xOf(iOct), xOf(iOct + 2), 0.5), yN = mix(200, yOf(DATA.f1.rOld), easeOut(t, tN - 0.1, tN + 0.6));
    dot(ctx, xN, yN, 17, C.positive, aN);
    text(ctx, 'Nora borrowed here', xN - 30, yOf(DATA.f1.rOld) - 76, 'label', { align: 'right', alpha: easeOut(t, tN + 0.4, tN + 0.8), plate: PL });
    text(ctx, CL('r_old') + ' · ' + CL('oct2023'), xN - 30, yOf(DATA.f1.rOld) - 22, 'note', { align: 'right', color: C.positive, alpha: easeOut(t, tN + 0.4, tN + 0.8), plate: PL });
    const aP = easeOut(t, tP - 0.1, tP + 0.3), xp = xOf(iPk), yp = yOf(wk[iPk].r);
    dot(ctx, xp, yp, 13, C.ink, aP);
    text(ctx, 'peak ' + CL('peak2023'), xp + 30, yp - 40, 'label', { alpha: aP, plate: PL });
    text(ctx, 'highest since ' + CL('peak2023_since'), xp + 30, yp + 16, 'note', { color: C.ink, alpha: easeOut(t, tS, tS + 0.4), plate: PL });
    chrome(ctx, { illus: aN, source: 'Freddie Mac weekly survey, via FRED (St. Louis Fed data). Nora: illustrative.' });
  }
  outdoors(scene, renderer, { sky: '#161E2C' });
  const cols = ['#CDBF9F', '#B9C3CC', '#C9BBA4', '#BFB3A0', '#D2C6B0', '#C9BBA4', '#B7BEC6', '#CDBF9F', '#C4B8A2', '#BAC2C9'];
  const lit = [2, 5, 8], NORA = 5;
  const Hs = cols.map((c, i) => {
    const k = 0.85 + 0.25 * Math.abs(Math.sin(i * 2.3));
    const g = shadowAll(house({ w: 2.0 * k, d: 1.7 * k, h: 1.2 * k, roof: 0.85 * k, wall: c, roofCol: i % 2 ? '#3B3F48' : '#4A4036', lit: 0 }));
    g.position.set(-11.7 + i * 2.6, 0, -2.6); scene.add(g);
    g.userData.mats = []; g.traverse((o) => { if (o.isMesh && o.material.color && o.material !== g.userData.winMat) g.userData.mats.push([o.material, o.material.color.clone()]); });
    return g;
  });
  const dark = new THREE.Color('#2A2F38');
  const lampT = (j) => t3 + j * 0.45;
  function update(t) {
    const k = ease(t, tSt, T.dur);
    camera.position.set(mix(-1.5, 0.3, k), 3.4, 21.5); camera.lookAt(mix(-1.5, 0.3, k), 2.3, -2.0);
    lit.forEach((i, j) => { Hs[i].userData.winMat.emissiveIntensity = 4.0 * ease(t, lampT(j), lampT(j) + 0.4); });
    const dk = 0.65 * ease(t, t3, t3 + 0.8);
    Hs.forEach((g, i) => { if (!lit.includes(i)) g.userData.mats.forEach(([m, c0]) => m.color.copy(c0).lerp(dark, dk)); });
  }
  function street(ctx, t, P) {
    text(ctx, 'Homes bought with a loan in ' + CL('oct2023').slice(-4), 96, 128, 'head', { alpha: easeOut(t, tSt, tSt + 0.4), shadow: true });
    const pn = P(new THREE.Vector3(Hs[NORA].position.x, 0, -1.3));
    const aN = easeOut(t, lampT(1), lampT(1) + 0.4);
    mark(ctx, 'nora', pn.x - 60, pn.y + 70, 16, aN); text(ctx, 'Nora', pn.x - 36, pn.y + 86, 'label', { alpha: aN, shadow: true });
    lit.forEach((i, j) => { const p = P(new THREE.Vector3(Hs[i].position.x, 0, -1.5)); const a = easeOut(t, lampT(j), lampT(j) + 0.3); ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = C.warn; ctx.fillRect(p.x - 60, p.y + 8, 120, 10); ctx.restore(); });
    const aL = easeOut(t, tLb, tLb + 0.4);
    const s0 = CL('purch23_words'); const s1 = s0[0].toUpperCase() + s0.slice(1);
    text(ctx, s1 + ' had a rate of ' + CL('seven') + '% or more', W / 2, 900, 'caption', { align: 'center', alpha: aL, plate: PL });
    text(ctx, CL('term30') + '-year home-purchase loans made in ' + CL('oct2023').slice(-4), W / 2, 966, 'note', { align: 'center', color: C.ink, alpha: aL, plate: PL });
    chrome(ctx, { illus: aN, source: 'HMDA ' + CLY('y2023', '2023') + ' (US home-loan records). Nora is illustrative.', plate: true });
  }
  return {
    mode: (t) => (t >= tSt ? '3d' : '2d'), update,
    overlay: (ctx, t, P, m) => (m === '3d' ? street(ctx, t, P) : chart(ctx, t)),
    stripTimes: [tN - 1.5, tN + 1.2, tS + 1.0, tSt + 1.0, lampT(2) + 0.6, T.dur - 0.2],
  };
}
