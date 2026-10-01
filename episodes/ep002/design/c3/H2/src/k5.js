// KEY-5 (S04.1-S04.2, S11.4-S11.6): the same loan replayed from every start month; the bead's track copies the ridge
// inside a 10-year frame; the frame steps right, faster and faster; each stop drops a (neutral) cell straight down.
import { C, W, DATA, CL, text, numWord, badge, line, poly, rect, srect, diamond, plane, replay, pathPts, ridgeGeom, drawRidge,
  replayPath, startRidgeIdx, STARTS, SPLIT_J, binGeom, RIDGE, ease, easeOut, back, mix, clamp, lin, FIXED } from './engine.js';
export const duration = 10.0;
export const stripTimes = [1.0, 2.3, 3.5, 5.2, 7.6, 9.8];
const P = plane(560, 1500, 150, 560, 3.0, 21.0, 120);
const G = ridgeGeom(200, 1720, 640, 900, 16.5);
const B = binGeom(G);
const BY0 = 930, BY1 = 990;
const NJ = STARTS.length;
// frame start index j as a function of t: slow first stops, then accelerating
function jAt(t) { if (t < 2.6) return 0; const u = clamp((t - 2.6) / 6.8); return Math.min(NJ - 1, Math.floor((NJ - 1) * Math.pow(u, 2.4))); }
function jStartTime(j) { return j === 0 ? 2.6 : 2.6 + 6.8 * Math.pow(j / (NJ - 1), 1 / 2.4); }
export function draw(ctx, t) {
  const j = jAt(t), s = startRidgeIdx(j);
  // ridge grows left -> right (the short track stretches into the long history)
  drawRidge(ctx, G, 1, ease(t, 0.0, 1.4));
  // bins under the two halves
  const ba = ease(t, 1.2, 1.7);
  srect(ctx, B.L[0] - 4, BY0 - 4, B.L[1] - B.L[0] + 8, BY1 - BY0 + 8, C.grid, 4, ba);
  srect(ctx, B.R[0] - 4, BY0 - 4, B.R[1] - B.R[0] + 8, BY1 - BY0 + 8, C.grid, 4, ba);
  // neutral cells dropped so far
  if (t >= 2.6) {
    for (let i = 0; i <= j; i++) {
      const st = jStartTime(i), f = easeOut(t, st, st + 0.3);
      const y = mix(G.y1, BY0, f);
      rect(ctx, B.xs[i], y, Math.max(B.cw, 2.2), BY1 - BY0, C.muted, 0.75 * Math.min(1, f * 2));
    }
  }
  // the replay plane: rail at 9% always; bead starts at 7.5%
  const fa = ease(t, 1.4, 1.8);
  if (t < 1.8) { line(ctx, [[P.x0, P.Y(FIXED)], [P.x1, P.Y(FIXED)]], C.ink, 10, { alpha: 1, cap: 'butt' }); diamond(ctx, P.X(0), P.Y(7.5), 30); }
  // previous frames on the ridge: faint outlines (neighbours overlap)
  const fx = (jj) => G.X(startRidgeIdx(jj)), fw = G.X(120) - G.X(0);
  if (t >= 1.8) {
    for (let k = 1; k <= 4; k++) if (j - k >= 0) srect(ctx, fx(j - k), G.y0 - 24, fw, G.y1 - G.y0 + 24, C.muted, 3, 0.35 / k);
    // overlap with the previous frame shaded
    if (j > 0) rect(ctx, fx(j), G.y0 - 24, fx(j - 1) + fw - fx(j), G.y1 - G.y0 + 24, C.muted, 0.12);
    srect(ctx, fx(j), G.y0 - 24, fw, G.y1 - G.y0 + 24, C.ink, 5, fa);
    // projection funnel: this frame is what the plane above replays
    line(ctx, [[fx(j), G.y0 - 24], [P.x0, P.y1 + 30]], C.grid, 3, { alpha: ease(t, 3.9, 4.3) }); line(ctx, [[fx(j) + fw, G.y0 - 24], [P.x1, P.y1 + 30]], C.grid, 3, { alpha: ease(t, 3.9, 4.3) });
  }
  if (t >= 1.8) {
    const path = replayPath(s);
    // first stop: the ridge segment lifts out of the frame and is copied into the plane (same shape, shifted to 7.5%)
    const lift = ease(t, 1.9, 2.6);
    if (lift < 1) {
      const src = []; for (let k = 0; k < 120; k++) src.push([G.X(s + k), G.Y(RIDGE[s + k].r)]);
      const dst = pathPts(P, path, 119);
      line(ctx, [[P.x0, P.Y(FIXED)], [P.x1, P.Y(FIXED)]], C.ink, 10, { cap: 'butt' });
      line(ctx, src.map((p, i) => [mix(p[0], dst[i][0], lift), mix(p[1], dst[i][1], lift)]), C.accent, 6);
      diamond(ctx, P.X(0), P.Y(7.5), 30);
    } else {
      // early stops redraw slowly (path draws through the 10 years); later ones appear whole
      const st = jStartTime(j), nxt = jStartTime(j + 1), dur = nxt - st;
      const n = dur > 0.3 ? 119 * ease(t, st, st + dur * 0.85) : 119;
      if (j > 0) replay(ctx, P, replayPath(startRidgeIdx(j - 1)), 119, { alpha: 0.25, bead: false, fill: false, railPath: false });
      replay(ctx, P, path, j === 0 ? 119 : n, { beadR: 30, aPos: 0.4, aWarn: 0.6 });
    }
  }
  text(ctx, CL('first_start'), G.x0, G.y0 - 60, 'label', { color: C.muted, alpha: inout(t, 0.6, 1.0, 1.6, 1.9) });
  text(ctx, '10 years', fx(Math.min(j, 300)) + fw / 2, G.y0 - 62, 'label', { align: 'center', color: C.ink, alpha: inout(t, 2.65, 2.95, 3.6, 3.9) });
  badge(ctx, 1);
}
function inout(t, a, b, c, d) { return Math.min(ease(t, a, b), 1 - ease(t, c, d)); }
