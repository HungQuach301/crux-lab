// H3 · "Dòng thời gian lịch sử": the whole TB3MS history 1954-01..2026-08 is one landscape (the ridge); a 10-year frame
// slides along it; every stop drops one cell into a 753-cell strip directly under its start year (12 cells per year).
import { C, W, H, CL, DATA, text, badge, line, rect, srect, diamond, bracket, coins, roundRect,
  clamp, lin, ease, easeIn, easeOut, back, mix, inout, rgba, measureText } from './engine.js';

// ---------- data ----------
const SER = DATA.series.map((d) => d[1]); const NM = SER.length; // 872 months, 1954-01 .. 2026-08
const WIN = DATA.windows; const NW = WIN.length;                  // 753
const IDX = SER[NM - 1], VAR0 = 7.5, FIXED = 9, MARGIN = VAR0 - IDX;
const SPLIT = 324;                                                 // 1981-01
const rate = (i, k) => MARGIN + Math.max(0, IDX + SER[i + k] - SER[i]);      // Leah's variable rate, window i, month k
const above = (i, k) => rate(i, k) > FIXED + 1e-9;
const tv = (i, k) => SER[i] + (rate(i, k) - VAR0);                            // the same rate drawn in ridge (index) units
const railV = (i) => SER[i] + (FIXED - VAR0);
for (let i = 0; i < NW; i++) { let a = false; for (let k = 0; k < 120; k++) a = a || above(i, k); if (a !== WIN[i].above) throw new Error('above mismatch ' + i); }
const WORST = DATA.worstIdx, BESTI = DATA.ex.fall.i;
const SWEEP = DATA.sweep; // [{g, bits, worst}]
const sweepAt = (g) => SWEEP[clamp(Math.round((g + 1) / 0.05), 0, SWEEP.length - 1)];

// ---------- view: (month, value) -> screen ----------
const V = (o) => ({ m0: 0, m1: NM, v0: 0, v1: 17.5, X0: 96, X1: 1824, Yb: 610, Yt: 250, ...o });
const lerpV = (a, b, x) => { const o = {}; for (const k in a) o[k] = mix(a[k], b[k], x); return o; };
const X = (v, m) => v.X0 + (m - v.m0) / (v.m1 - v.m0) * (v.X1 - v.X0);
const Y = (v, val) => v.Yb - (val - v.v0) / (v.v1 - v.v0) * (v.Yb - v.Yt);
const FULL = V({});

function clipX(ctx, v, y0 = 0, y1 = H) { ctx.save(); ctx.beginPath(); ctx.rect(v.X0 - 2, y0, v.X1 - v.X0 + 4, y1 - y0); ctx.clip(); }
function ridge(ctx, v, o = {}) {
  const a = o.alpha ?? 1; if (a <= 0) return;
  const lo = Math.max(0, Math.floor(o.from ?? v.m0) - 1), hi = Math.min(NM - 1, Math.ceil(o.to ?? v.m1) + 1);
  if (hi <= lo) return;
  clipX(ctx, v, v.Yt - 30, H);
  const pts = []; for (let m = lo; m <= hi; m++) pts.push([X(v, m), Y(v, SER[m])]);
  ctx.globalAlpha = a * (o.fill ?? 0.16); ctx.fillStyle = C.accent; ctx.beginPath(); ctx.moveTo(pts[0][0], v.Yb);
  pts.forEach((p) => ctx.lineTo(p[0], p[1])); ctx.lineTo(pts[pts.length - 1][0], v.Yb); ctx.closePath(); ctx.fill();
  ctx.globalAlpha = 1; line(ctx, pts, C.accent, o.lw ?? 4, { alpha: a });
  ctx.restore();
}
// strip of 753 cells: column = start year (under that year on the ridge), row = start month (January on top)
const STRIP = { top: 664, row: 14 };
function cellRect(v, i, S = STRIP) {
  const col = Math.floor(i / 12), row = i % 12;
  const x0 = X(v, col * 12) + 1.5, x1 = X(v, col * 12 + 12) - 1.5;
  return [x0, S.top + row * S.row, Math.max(1, x1 - x0), S.row - 3];
}
function cells(ctx, v, fn, S = STRIP) {
  clipX(ctx, v);
  for (let i = 0; i < NW; i++) {
    const st = fn(i); if (!st || st.a <= 0) continue;
    const [x, y, w, h] = cellRect(v, i, S);
    rect(ctx, x, y - (st.dy || 0), w, h, st.c, st.a);
  }
  ctx.restore();
}
function ring(ctx, v, i, a, S = STRIP) { if (a <= 0) return; const [x, y, w, h] = cellRect(v, i, S); srect(ctx, x - 6, y - 6, w + 12, h + 12, C.ink, 4, a); }
function split(ctx, v, y0, y1, a = 1) { if (a <= 0) return; const x = X(v, SPLIT); line(ctx, [[x, y0], [x, y1]], C.muted, 2, { alpha: a, dash: [6, 8], cap: 'butt' }); }
function tally(ctx, v, upto, y = 628, h = 18, a = 1) {
  if (a <= 0) return; clipX(ctx, v);
  for (let i = 0; i <= Math.min(NW - 1, upto); i++) rect(ctx, X(v, i), y, Math.max(1, X(v, i + 1) - X(v, i) + 0.3), h, WIN[i].above ? C.warn : C.grid, a);
  ctx.restore();
}
function years(ctx, v, y = 900, o = {}) {
  const a = o.alpha ?? 1;
  text(ctx, CL('first_start').slice(-4), X(v, 0), y, 'note', { color: C.muted, alpha: a });
  text(ctx, CL('best_start_year'), X(v, SPLIT), y, 'note', { color: C.muted, align: 'center', alpha: a });
  if (o.today !== false) text(ctx, 'today', X(v, NM - 1), y, 'note', { color: C.muted, align: 'right', alpha: a });
}
// the 10-year frame on window i; ride = months ridden (0..120) or null (= whole window shown)
function frame(ctx, v, i, o = {}) {
  const a = o.alpha ?? 1; if (a <= 0) return;
  const x0 = X(v, i), x1 = X(v, i + 120), top = v.Yt - 26;
  rect(ctx, x0, top, x1 - x0, v.Yb - top, C.ink, 0.05 * a);
  srect(ctx, x0, top, x1 - x0, v.Yb - top, C.ink, 3, a);
  const K = o.ride == null ? 120 : clamp(o.ride, 0, 120);
  if (o.track !== false) {
    const pts = []; for (let k = 0; k <= Math.min(119, Math.floor(K)); k++) pts.push([X(v, i + k), Y(v, tv(i, k))]);
    line(ctx, pts, C.ink, o.tlw ?? 4, { alpha: a });
  }
  const yr = Y(v, railV(i));
  line(ctx, [[x0, yr], [x1, yr]], C.muted, o.rlw ?? 5, { alpha: a, cap: 'butt' });
  if (o.glow !== false) { // amber: the rail lights wherever the rate is above it
    let s = -1;
    for (let k = 0; k <= Math.min(120, Math.floor(K)); k++) {
      const on = k < 120 && k <= K && above(i, k);
      if (on && s < 0) s = k;
      if (!on && s >= 0) { line(ctx, [[X(v, i + s), yr], [X(v, i + k), yr]], C.warn, (o.rlw ?? 5) + 4, { alpha: a, cap: 'butt' }); s = -1; }
    }
    if (s >= 0) line(ctx, [[X(v, i + s), yr], [X(v, i + Math.min(120, K + 1)), yr]], C.warn, (o.rlw ?? 5) + 4, { alpha: a, cap: 'butt' });
  }
  if (o.bead !== false && o.ride != null) { const k = Math.min(119, Math.floor(K)); diamond(ctx, X(v, i + k), Y(v, tv(i, k)), o.br ?? 16, C.ink, a); }
}
function caption(ctx, s, a = 1, o = {}) { text(ctx, s, 96, 140, 'caption', { color: o.color || C.ink, alpha: a }); }

// ---------- K1 / K2: the desk view (rail, bead, head start). 100 px per point. ----------
const D = { x0: 520, x1: 1640, yr: 440, ppp: 100 };
function wob(x, t, seed) { // smooth illustrative wander (not data)
  return 34 * Math.sin(x / 140 + seed * 1.7 + t * 0.9) + 22 * Math.sin(x / 61 + seed * 3.1 - t * 1.3) + 12 * Math.sin(x / 27 + seed * 5.3 + t * 2.1);
}
function deskTrack(ctx, t, yStart, o = {}) {
  const known = o.known ?? 420, a = o.alpha ?? 1;
  const yAt = (x) => yStart + wob(x - D.x0, 0, 0) * Math.min(1, (x - D.x0) / 120) * 1.1;
  const xs = []; for (let x = D.x0; x <= D.x0 + known * (o.grow ?? 1); x += 4) xs.push([x, yAt(x)]);
  const xb = D.x0 + known * (o.grow ?? 1), yb = yAt(xb);
  if (o.fan) for (let s = 1; s <= 7; s++) { // the unknown road ahead: a fan of faint, changing paths
    const pts = []; for (let x = xb; x <= D.x1; x += 8) { const u = (x - xb) / (D.x1 - xb); pts.push([x, yb + u * (wob(x, t, s) * 2.2 + (s - 4) * 34 * u)]); }
    line(ctx, pts, C.ink, 3, { alpha: 0.22 * o.fan });
  }
  if (o.glow) { // gap between bead and rail: positive under, warn over
    ctx.save(); ctx.globalAlpha = o.glow; ctx.beginPath(); ctx.moveTo(D.x0, D.yr); xs.forEach((p) => ctx.lineTo(p[0], p[1])); ctx.lineTo(xs[xs.length - 1][0], D.yr); ctx.closePath();
    ctx.fillStyle = yStart >= D.yr ? C.cushion : C.warn; ctx.fill(); ctx.restore();
  }
  line(ctx, xs, C.ink, 5, { alpha: a });
  diamond(ctx, xb, yb, 20, C.ink, a);
  return [xb, yb];
}
function fixedLabel(ctx, a) { // "9% fixed", left of the rail's start: number in ink, word in ink-muted (D5)
  const xr = D.x0 - 60, y = D.yr + 19;
  text(ctx, CL('fixed_rate'), xr - measureText(ctx, ' fixed', 'label'), y, 'label', { align: 'right', alpha: a, group: 'fx' });
  text(ctx, ' fixed', xr, y, 'label', { align: 'right', color: C.muted, alpha: a, group: 'fx' });
}
function startLine(ctx, a = 1) { line(ctx, [[D.x0, 330], [D.x0, 800]], C.muted, 2, { alpha: 0.7 * a, dash: [6, 9], cap: 'butt' }); }
function rail(ctx, grow = 1, a = 1, lw = 6) { line(ctx, [[D.x0, D.yr], [mix(D.x0, D.x1, grow), D.yr]], C.muted, lw, { alpha: a, cap: 'butt' }); }

export const K1 = {
  duration: 8, stripTimes: [0.4, 1.4, 2.6, 3.8, 5.6, 7.6],
  draw(ctx, t) {
    startLine(ctx, ease(t, 0, 0.6));
    const gr = ease(t, 0.5, 1.5);
    rail(ctx, gr, 1, 6 + 4 * inout(t, 2.2, 2.6, 3.0, 3.4));   // look at the level one ...
    const tg = ease(t, 1.0, 2.4);
    const glow = 0.22 + 0.12 * Math.sin(t * 3.2) * ease(t, 4, 5);
    const yS = D.yr + 1.5 * D.ppp;
    if (t > 0.9) deskTrack(ctx, t, yS, { grow: tg, fan: ease(t, 2.2, 3.4), glow: glow * ease(t, 1.6, 2.6) });   // ... then at the lower, wandering one
    if (t > 3.4) { const p = inout(t, 3.4, 3.8, 4.2, 4.6); if (p > 0) { const pts = []; for (let x = D.x0; x <= D.x0 + 420; x += 4) pts.push([x, yS + wob(x - D.x0, 0, 0) * Math.min(1, (x - D.x0) / 120) * 1.1]); line(ctx, pts, C.ink, 5 + 5 * p, { alpha: p }); } }
    fixedLabel(ctx, ease(t, 1.2, 1.7));
    text(ctx, CL('var_start'), D.x0 - 60, yS + 20, 'label', { align: 'right', alpha: ease(t, 1.8, 2.3), group: 'vr' });
    text(ctx, 'variable', D.x0 - 60, yS + 90, 'label', { align: 'right', color: C.muted, alpha: ease(t, 1.8, 2.3), group: 'vr' });
    caption(ctx, "Leah's two offers", ease(t, 0.2, 0.7));
    badge(ctx, undefined, undefined, ease(t, 0.2, 0.7));
  },
};

export const K2 = {
  duration: 9, stripTimes: [0.3, 1.2, 3.4, 5.0, 6.6, 8.6],
  draw(ctx, t) {
    // gap in points over time: 1.5 -> 3 (wide) -> 0.5 (narrow) -> 0 (none) -> -1 (reversed) -> 1.5
    const keys = [[0, 1.5], [2.4, 1.5], [3.2, 3], [4.0, 3], [4.7, 0.5], [5.3, 0.5], [5.9, 0], [6.5, 0], [7.2, -1], [7.9, -1], [8.6, 1.5]];
    let g = 1.5; for (let j = 0; j < keys.length - 1; j++) if (t >= keys[j][0] && t <= keys[j + 1][0]) g = mix(keys[j][1], keys[j + 1][1], ease(t, keys[j][0], keys[j + 1][0]));
    const yS = D.yr + g * D.ppp;
    startLine(ctx);
    rail(ctx);
    deskTrack(ctx, t, yS, { fan: 0.5, glow: 0.18 });
    const snap = back(t, 0.3, 0.8);
    bracket(ctx, D.x0 - 8, D.yr, mix(D.yr, yS, clamp(snap, 0, 1.2)), ease(t, 0.3, 0.5), 26);
    // memory of the sizes tried: small brackets bottom-left, in order (big, small, none, reversed)
    const hist = [[4.0, 3], [5.3, 0.5], [6.5, 0], [7.9, -1]];
    hist.forEach(([tt, gg], j) => { const a = ease(t, tt - 0.1, tt + 0.3); if (a > 0) { const bx = 190 + j * 70, by = 880; line(ctx, [[bx - 34, by], [bx + 10, by]], C.muted, 3, { alpha: a, cap: 'butt' }); bracket(ctx, bx, by, by + gg * 40, a, 14); diamond(ctx, bx + 4, by + gg * 40, 9, C.ink, a); } });
    fixedLabel(ctx, 1);
    const la = Math.min(ease(t, 0.8, 1.2), 1 - ease(t, 2.4, 2.7)) + ease(t, 8.6, 8.9);
    text(ctx, CL('gap_start'), D.x0 - 60, D.yr + 0.75 * D.ppp + 20, 'label', { align: 'right', alpha: la });
    caption(ctx, 'The head start', ease(t, 0, 0.4));
    badge(ctx, undefined, undefined, 1);
  },
};

// ---------- K5: the replay ----------
const K5T = (() => { // start time of each of the 753 stops: slow first, then faster and faster, all done at 8.7 s
  const t0 = 1.7, tEnd = 8.7, d0 = 1.15, r = 0.58; let lo = 0, hi = 0.05;
  const total = (dm) => { let s = 0; for (let k = 0; k < NW; k++) s += Math.max(dm, d0 * Math.pow(r, k)); return s; };
  for (let it = 0; it < 60; it++) { const m = (lo + hi) / 2; if (total(m) > tEnd - t0) hi = m; else lo = m; }
  const T = [t0]; for (let k = 0; k < NW; k++) T.push(T[k] + Math.max(lo, d0 * Math.pow(r, k))); return T;
})();
const kAt = (t) => { let k = 0; while (k < NW && K5T[k + 1] <= t) k++; return k; };
export const K5 = {
  duration: 10, stripTimes: [0.2, 1.9, 2.9, 4.0, 6.4, 9.4],
  draw(ctx, t) {
    const VZ = V({ m0: -24, m1: 150, v1: 6.5 }), VA = V({ m0: -6, m1: 300, v1: 11 });
    const v = t < 1.7 ? lerpV(VZ, VA, ease(t, 0.2, 1.6)) : lerpV(VA, FULL, ease(t, 4.2, 6.8));
    ridge(ctx, v, {});
    const k = Math.min(NW - 1, kAt(t));
    const seg = K5T[k + 1] - K5T[k], u = clamp((t - K5T[k]) / seg);
    const slow = seg > 0.1, pos = slow ? k + ease(u, 0.78, 1) : k + u;
    // ghost frames: the previous stops, still outlined (neighbouring stretches overlap)
    for (let j = 1; j <= 3; j++) if (k - j >= 0 && t > 1.7) srect(ctx, X(v, Math.floor(pos) - j), v.Yt - 26, X(v, 120) - X(v, 0), v.Yb - v.Yt + 26, C.ink, 2, (0.45 - 0.12 * j) * (1 - ease(t, 6.5, 7.5)));
    const ride = t < 1.7 ? 0 : slow ? 120 * ease(u, 0, 0.72) : null;
    frame(ctx, v, Math.min(NW - 1, Math.floor(pos)), { ride: t < 1.7 ? 0 : ride, alpha: 1 - ease(t, 8.9, 9.4) });
    // cells: each stop drops a neutral cell straight down to its start year / month
    cells(ctx, v, (i) => { const td = K5T[i + 1] - 0.02; if (t < td) return null; const f = easeIn(t, td, td + 0.32); return { c: C.muted, a: Math.min(1, f * 3), dy: (1 - f) * (STRIP.top - v.Yb + 40) }; });
    split(ctx, v, v.Yt - 40, STRIP.top + 12 * STRIP.row, ease(t, 7.0, 8.0));
    years(ctx, v, 900, { alpha: ease(t, 6.8, 7.6) });
    caption(ctx, 'Every 10-year stretch since ' + CL('first_start'), ease(t, 0.3, 0.8));
    badge(ctx, undefined, undefined, 1);
  },
};

// ---------- K3: amber nearly everywhere, red only in a few cells, mostly on the left ----------
export const K3 = {
  duration: 10, stripTimes: [0.3, 1.8, 3.6, 5.6, 7.4, 9.4],
  draw(ctx, t) {
    const v = FULL;
    ridge(ctx, v);
    const f = 752 * ease(t, 0.2, 3.0);
    tally(ctx, v, f);
    frame(ctx, v, Math.round(f), { alpha: 1 - ease(t, 3.0, 3.5), tlw: 4 });
    const flip = (i) => 4.3 + 1.9 * i / (NW - 1);
    const hl = (i) => { const left = i < SPLIT; const e1 = inout(t, 6.5, 6.9, 8.2, 8.5), e2 = ease(t, 8.3, 8.7); return left ? 1 - 0.65 * e2 : 1 - 0.65 * e1; };
    cells(ctx, v, (i) => { const x = ease(t, flip(i), flip(i) + 0.25); const red = WIN[i].diff > 0; return { c: x < 0.5 ? C.muted : red ? C.costlier : C.grid, a: hl(i) }; });
    split(ctx, v, v.Yt - 40, STRIP.top + 12 * STRIP.row);
    years(ctx, v, 900);
    // one number per moment
    const a1 = inout(t, 2.6, 3.0, 4.1, 4.4), a2 = inout(t, 4.5, 4.9, 6.2, 6.5);
    if (a1 > 0) { const w = text(ctx, CL('share_rate_above_fixed'), 96, 150, 'number', { color: C.warn, alpha: a1, group: 'n1' }).x1; text(ctx, 'went above the fixed rate', w + 28, 150, 'caption', { color: C.muted, alpha: a1, group: 'n1' }); }
    if (a2 > 0) { const w = text(ctx, CL('share_all'), 96, 150, 'number', { color: C.ink, alpha: a2, group: 'n2' }).x1; text(ctx, 'cost more in total', w + 28, 150, 'caption', { color: C.muted, alpha: a2, group: 'n2' }); }
    text(ctx, CL('share_early'), (X(v, 0) + X(v, SPLIT)) / 2, 1010, 'number', { color: C.ink, align: 'center', alpha: inout(t, 6.6, 7.0, 8.2, 8.5) });
    text(ctx, CL('share_late'), (X(v, SPLIT) + X(v, NW)) / 2, 1010, 'number', { color: C.ink, align: 'center', alpha: ease(t, 8.5, 8.9) });
    badge(ctx, undefined, undefined, 1);
  },
};

// ---------- K4: the cushion (jar) ----------
const JAR_MAX = 16000;
function jar(ctx, x, y0, y1, w, val, a = 1) { // vessel + positive liquid (cushion > 0 only)
  if (a <= 0) return;
  const h = y1 - y0, lv = clamp(val / JAR_MAX) * (h - 12);
  ctx.save(); ctx.globalAlpha = a; roundRect(ctx, x, y0, w, h, 18); ctx.clip();
  rect(ctx, x, y1 - lv - 6, w, lv + 6, C.cushion, lv > 0.5 ? 1 : 0); ctx.restore();
  ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = C.muted; ctx.lineWidth = 4; roundRect(ctx, x, y0, w, h, 18); ctx.stroke(); ctx.restore();
}
function runPanel(ctx, ex, k, P, a = 1) { // one replay zoomed: rail at 9%, Leah's rate, debt wedge; k = months ridden
  if (a <= 0) return;
  const xs = (m) => mix(P.x0, P.x1, m / 120), ys = (r) => mix(P.yb, P.yt, (r - P.r0) / (P.r1 - P.r0));
  const K = clamp(k, 0, 120), n = Math.min(119, Math.floor(K));
  const path = ex.path;
  // debt still owed (taller at left): a flat wedge under the panel
  for (let m = 0; m <= n; m++) rect(ctx, xs(m), P.wb - ex.bals[m] / 50000 * P.wh, xs(m + 1) - xs(m) + 0.5, ex.bals[m] / 50000 * P.wh, C.grid, a);
  // saving each month: positive area between rail and rate where the rate is under 9%
  ctx.save(); ctx.globalAlpha = 0.35 * a; ctx.fillStyle = C.cushion;
  for (let m = 0; m <= n; m++) if (path[m] < FIXED) ctx.fillRect(xs(m), ys(FIXED), xs(m + 1) - xs(m) + 0.5, ys(path[m]) - ys(FIXED));
  ctx.restore();
  line(ctx, [[xs(0), ys(FIXED)], [xs(120), ys(FIXED)]], C.muted, 6, { alpha: a, cap: 'butt' });
  for (let m = 0; m <= n; m++) if (path[m] > FIXED) line(ctx, [[xs(m), ys(FIXED)], [xs(m + 1), ys(FIXED)]], C.warn, 10, { alpha: a, cap: 'butt' });
  const pts = []; for (let m = 0; m <= n; m++) pts.push([xs(m + 0.5), ys(path[m])]);
  line(ctx, pts, C.ink, 5, { alpha: a });
  diamond(ctx, xs(n + 0.5), ys(path[n]), 18, C.ink, a);
  return { xs, ys };
}
export const K4 = {
  duration: 10, stripTimes: [1.4, 2.95, 4.6, 5.9, 7.6, 9.3],
  draw(ctx, t) {
    const runs = [['blip', 0.2, 3.3], ['climb', 3.3, 6.5], ['fall', 6.5, 9.4]];
    const MV = V({ Yt: 196, Yb: 316, v1: 17.5 });
    ridge(ctx, MV, { lw: 3, fill: 0.14 });
    const P = { x0: 230, x1: 1400, yt: 380, yb: 860, r0: 3.4, r1: 19.6, wb: 1000, wh: 110 };
    const JX = 1560, JW = 170, J0 = 400, J1 = 860;
    let cur = null;
    runs.forEach(([key, a0, a1], j) => {
      const ex = DATA.ex[key], i = ex.i;
      const on = t >= a0 && (t < a1 || j === runs.length - 1);
      const res = ex.diff > 0 ? C.costlier : C.grid;
      const ca = ease(t, a0 + 2.75, a0 + 2.95); // result cell under the jar
      if (ca > 0) { const cy = mix(J1 - 30, 940 , easeIn(t, a0 + 2.75, a0 + 2.95)); rect(ctx, JX + 8 + j * 54, cy, 46, 30, res, 1); }
      if (!on) return;
      const fa = ease(t, a0, a0 + 0.25);
      // where in history: the frame on the small landscape
      srect(ctx, X(MV, i), MV.Yt - 14, X(MV, i + 120) - X(MV, i), MV.Yb - MV.Yt + 14, C.ink, 3, fa);
      rect(ctx, X(MV, i), MV.Yt - 14, X(MV, i + 120) - X(MV, i), MV.Yb - MV.Yt + 14, C.ink, 0.07 * fa);
      // connector from the small frame down to the panel
      ctx.save(); ctx.globalAlpha = 0.12 * fa; ctx.fillStyle = C.ink; ctx.beginPath(); ctx.moveTo(X(MV, i), MV.Yb); ctx.lineTo(X(MV, i + 120), MV.Yb); ctx.lineTo(P.x1, P.yt - 20); ctx.lineTo(P.x0, P.yt - 20); ctx.closePath(); ctx.fill(); ctx.restore();
      const k = 120 * lin(t, a0 + 0.3, a0 + 2.6);
      runPanel(ctx, ex, k, P, fa);
      cur = ex.cushion[Math.min(119, Math.floor(k))];
    });
    jar(ctx, JX, J0, J1, JW, Math.max(0, cur ?? 0));
    text(ctx, CL('fixed_rate'), 200, mix(860, 380, (9 - 3.4) / (19.6 - 3.4)) + 19, 'label', { align: 'right', color: C.muted });
    caption(ctx, 'What the lower start saves', ease(t, 0, 0.4));
    badge(ctx, undefined, undefined, 1);
  },
};

// ---------- K6: the worst replay ----------
export const K6 = {
  duration: 10, stripTimes: [0.4, 1.8, 3.4, 5.0, 7.2, 9.6],
  draw(ctx, t) {
    const i = WORST;
    const VZ = V({ m0: i - 22, m1: i + 126, Yt: 230, Yb: 860, X0: 96, X1: 1320 });
    const z = ease(t, 1.0, 2.4), v = lerpV(FULL, VZ, z);
    // landscape + strip (fade as we zoom)
    ridge(ctx, v, { alpha: 1 - 0.8 * z, to: z > 0.5 ? i : NM });
    ridge(ctx, v, { from: i, to: i + 120, alpha: 1 });
    const g15 = sweepAt(1.5).bits;
    cells(ctx, FULL, (j) => ({ c: g15[j] === '1' ? C.costlier : C.grid, a: 1 - ease(t, 0.9, 1.6) }));
    ring(ctx, FULL, i, (0.6 + 0.4 * Math.sin(t * 7)) * (1 - ease(t, 0.9, 1.4)));
    years(ctx, FULL, 900, { alpha: 1 - ease(t, 0.8, 1.3) });
    split(ctx, FULL, FULL.Yt - 40, STRIP.top + 12 * STRIP.row, 1 - ease(t, 0.8, 1.3));
    const ride = 120 * ease(t, 2.6, 6.0);
    frame(ctx, v, i, { ride: t < 2.6 ? 0 : ride, tlw: mix(4, 6, z), rlw: mix(5, 7, z), br: mix(14, 22, z), alpha: ease(t, 0.3, 0.8) });
    // right column: jar (fills a little, then empty), then the two coin piles
    const ex = DATA.ex.worst, kk = Math.min(119, Math.floor(ride));
    jar(ctx, 1560, 420, 860, 170, Math.max(0, t < 2.6 ? 0 : ex.cushion[kk]), ease(t, 2.2, 2.6) * (1 - ease(t, 6.2, 6.6)));
    const S = 330 / 26005.46, fixH = 330 * ease(t, 6.5, 7.3), extra = 11218.65 * S * ease(t, 7.9, 8.8);
    coins(ctx, 1500, 860, fixH, C.muted, ease(t, 6.5, 6.7));
    const top = coins(ctx, 1700, 860, fixH, C.muted, ease(t, 6.5, 6.7));
    coins(ctx, 1700, top, extra, C.costlier, 1);
    if (t > 6.5) { line(ctx, [[1446, 900], [1554, 900]], C.muted, 6, { cap: 'butt', alpha: ease(t, 6.5, 6.8) }); diamond(ctx, 1700, 902, 18, C.ink, ease(t, 6.5, 6.8)); }
    // numbers, one at a time
    const pk = DATA.ex.worst.path.indexOf(Math.max(...DATA.ex.worst.path));
    const pa = inout(t, 4.6, 5.0, 6.2, 6.5), py = Y(v, tv(i, pk));
    if (pa > 0) line(ctx, [[X(v, i + pk) + 24, py], [1380, py]], C.muted, 2, { alpha: pa, dash: [4, 8], cap: 'butt' });
    text(ctx, CL('worst_peak_rate'), 1404, py + 35, 'number', { alpha: pa });
    text(ctx, CL('fixed_int'), 1500, 860 - 330 - 28, 'label', { align: 'center', alpha: inout(t, 7.0, 7.3, 8.0, 8.2) });
    // final (owner C3 phase 2): the extra block is worst_share_of_fixed (43%) of the fixed pile; label it with that claim
    { const ya = 860 - 330 - 11218.65 * S - 34, aa = ease(t, 8.6, 8.9), wm = measureText(ctx, ' more', 'caption');
      text(ctx, CL('worst_share_of_fixed'), 1824 - wm, ya, 'number', { align: 'right', alpha: aa, group: 'ws' });
      text(ctx, ' more', 1824, ya, 'caption', { align: 'right', color: C.muted, alpha: aa, group: 'ws' }); }
    caption(ctx, 'Starting ' + CL('worst_start'), ease(t, 1.4, 1.9));
    badge(ctx, undefined, undefined, 1);
  },
};

// ---------- K7: moving the head start ----------
export const K7 = {
  duration: 10, stripTimes: [0.5, 2.9, 4.9, 6.6, 7.6, 9.5],
  draw(ctx, t) {
    const v = V({ Yt: 200, Yb: 520 }), S = { top: 548, row: 14 };
    const keys = [[0, 1.5], [1.0, 1.5], [2.4, 2], [3.4, 2], [4.4, 3], [5.4, 3], [8.6, -1]];
    let g = 1.5; for (let j = 0; j < keys.length - 1; j++) if (t >= keys[j][0] && t <= keys[j + 1][0]) g = mix(keys[j][1], keys[j + 1][1], ease(t, keys[j][0], keys[j + 1][0]));
    if (t > 8.6) g = -1;
    const sw = sweepAt(g);
    ridge(ctx, v);
    cells(ctx, v, (i) => ({ c: sw.bits[i] === '1' ? C.costlier : C.grid, a: 1 }), S);
    ring(ctx, v, WORST, 0.9, S);
    split(ctx, v, v.Yt - 30, S.top + 12 * S.row);
    years(ctx, v, 790, { today: false });
    // ruler + knob; Leah's mark at 1.5
    const R = { x0: 560, x1: 1460, y: 940 }, gx = (gg) => mix(R.x0, R.x1, (gg + 1) / 4);
    line(ctx, [[R.x0, R.y], [R.x1, R.y]], C.muted, 4, { cap: 'butt' });
    for (let gg = -1; gg <= 3.001; gg += 0.5) line(ctx, [[gx(gg), R.y - 12], [gx(gg), R.y + 12]], C.muted, 3, { cap: 'butt' });
    diamond(ctx, gx(1.5), R.y + 34, 12, C.muted, 1, 3);
    text(ctx, CL('gap_start'), gx(1.5), R.y + 108, 'label', { align: 'center', color: C.muted });
    line(ctx, [[gx(g), R.y - 34], [gx(g), R.y + 18]], C.ink, 8, { cap: 'round' });
    // the bracket itself, bottom left: rail level, bead below by g
    const bx = 340, by = 850, pp = 44;
    line(ctx, [[bx - 30, by], [bx + 110, by]], C.muted, 5, { cap: 'butt' });
    bracket(ctx, bx, by, by + g * pp, 1, 30); diamond(ctx, bx + 22, by + g * pp, 20, C.ink);
    // worst case: fixed coin pile + the extra block (red), right of the strip
    const Sc = 160 / 26005.46, top = coins(ctx, 1700, 1000, 160, C.muted, 1, 120, 14);
    coins(ctx, 1700, top, sw.worst * Sc, C.costlier, 1, 120, 14);
    const a2 = inout(t, 2.5, 2.8, 3.4, 3.6), a3 = inout(t, 4.5, 4.8, 5.5, 5.7);
    text(ctx, CL('spread2_share'), gx(2), 870, 'number', { align: 'center', color: C.costlier, alpha: a2 });
    text(ctx, CL('spread3_share'), gx(3), 870, 'number', { align: 'center', color: C.costlier, alpha: a3 });
    caption(ctx, 'Moving the head start', 1);
    badge(ctx, undefined, undefined, 1);
  },
};

// ---------- concept thumbnail (one still) ----------
export const THUMB = {
  duration: 1, stripTimes: [0],
  draw(ctx) {
    const v = V({ Yt: 150, Yb: 560 }), S = { top: 600, row: 15 };
    ridge(ctx, v, { lw: 6, fill: 0.2 });
    const g15 = sweepAt(1.5).bits;
    cells(ctx, v, (i) => ({ c: g15[i] === '1' ? C.costlier : C.grid, a: 1 }), S);
    split(ctx, v, v.Yt - 30, S.top + 12 * S.row);
    frame(ctx, v, WORST, { ride: 49, tlw: 7, rlw: 8, br: 24 });
    text(ctx, 'Fixed or variable?', 96, 990, 'hero');
    badge(ctx, undefined, undefined, 1);
  },
};
