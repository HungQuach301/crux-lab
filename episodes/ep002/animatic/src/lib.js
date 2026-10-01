// Shared drawing for the C4 animatic scenes that are NOT one of the seven signed key clips. No new style: every function
// here is copied from the signed code (design/c3/final/src: k1.js/k2.js offer card + person, k4.js jar run; h3/scenes.js
// ridge, 10-year frame, cell strip, split line, year labels, ring, jar) and draws with the signed engines' primitives.
import { H2, H3, C, W, H, CL, mix, clamp, ease, lin } from './film.js';

// ---------- KEY-1/KEY-2 motif (k1.js / k2.js): offer card with folded corner, person with the diamond cut-out ----------
export const CARD = { CW: 680, CH: 470, CY: 196, LX: 130, RX: 1920 - 130 - 680 };
export function card(ctx, x, y, sx = 1, a = 1, CW = CARD.CW, CH = CARD.CH) {
  if (a <= 0.001) return;
  ctx.save(); ctx.globalAlpha = a; const cx = x + CW / 2; ctx.translate(cx, 0); ctx.scale(sx, 1); ctx.translate(-cx, 0); const f = 54;
  ctx.beginPath(); ctx.moveTo(x + 22, y); ctx.lineTo(x + CW - f, y); ctx.lineTo(x + CW, y + f); ctx.lineTo(x + CW, y + CH - 22);
  ctx.arcTo(x + CW, y + CH, x + CW - 22, y + CH, 22); ctx.lineTo(x + 22, y + CH); ctx.arcTo(x, y + CH, x, y + CH - 22, 22);
  ctx.lineTo(x, y + 22); ctx.arcTo(x, y, x + 22, y, 22); ctx.closePath();
  ctx.fillStyle = C.bg; ctx.fill(); ctx.lineWidth = 5; ctx.strokeStyle = C.muted; ctx.lineJoin = 'round'; ctx.stroke();
  ctx.beginPath(); ctx.moveTo(x + CW - f, y); ctx.lineTo(x + CW - f, y + f); ctx.lineTo(x + CW, y + f); ctx.stroke();
  ctx.restore();
}

// ---------- H3 view helpers (copied from design/c3/final/src/h3/scenes.js) ----------
const DATA3 = H3.DATA;
export const SER = DATA3.series.map((d) => d[1]); export const NM = SER.length;
export const WIN = DATA3.windows; export const NW = WIN.length;
const IDX = SER[NM - 1], VAR0 = 7.5, FIXED = 9, MARGIN = VAR0 - IDX;
export const SPLIT = 324, WORST = DATA3.worstIdx, BEST = DATA3.ex.fall.i;
export const rate = (i, k) => MARGIN + Math.max(0, IDX + SER[i + k] - SER[i]);
const above = (i, k) => rate(i, k) > FIXED + 1e-9;
export const tv = (i, k) => SER[i] + (rate(i, k) - VAR0);
const railV = (i) => SER[i] + (FIXED - VAR0);
export const sweepAt = (g) => DATA3.sweep[clamp(Math.round((g + 1) / 0.05), 0, DATA3.sweep.length - 1)];
export const V = (o) => ({ m0: 0, m1: NM, v0: 0, v1: 17.5, X0: 96, X1: 1824, Yb: 610, Yt: 250, ...o });
export const lerpV = (a, b, x) => { const o = {}; for (const k in a) o[k] = mix(a[k], b[k], x); return o; };
export const X = (v, m) => v.X0 + (m - v.m0) / (v.m1 - v.m0) * (v.X1 - v.X0);
export const Y = (v, val) => v.Yb - (val - v.v0) / (v.v1 - v.v0) * (v.Yb - v.Yt);
export const FULL = V({});
function clipX(ctx, v, y0 = 0, y1 = H) { ctx.save(); ctx.beginPath(); ctx.rect(v.X0 - 2, y0, v.X1 - v.X0 + 4, y1 - y0); ctx.clip(); }
export function ridge(ctx, v, o = {}) {
  const a = o.alpha ?? 1; if (a <= 0) return;
  const lo = Math.max(0, Math.floor(o.from ?? v.m0) - 1), hi = Math.min(NM - 1, Math.ceil(o.to ?? v.m1) + 1);
  if (hi <= lo) return;
  clipX(ctx, v, v.Yt - 30, H);
  const pts = []; for (let m = lo; m <= hi; m++) pts.push([X(v, m), Y(v, SER[m])]);
  ctx.globalAlpha = a * (o.fill ?? 0.16); ctx.fillStyle = C.accent; ctx.beginPath(); ctx.moveTo(pts[0][0], v.Yb);
  pts.forEach((p) => ctx.lineTo(p[0], p[1])); ctx.lineTo(pts[pts.length - 1][0], v.Yb); ctx.closePath(); ctx.fill();
  ctx.globalAlpha = 1; H3.line(ctx, pts, C.accent, o.lw ?? 4, { alpha: a });
  ctx.restore();
}
export const STRIP = { top: 664, row: 14 };
export function cellRect(v, i, S = STRIP) {
  const col = Math.floor(i / 12), row = i % 12;
  const x0 = X(v, col * 12) + 1.5, x1 = X(v, col * 12 + 12) - 1.5;
  return [x0, S.top + row * S.row, Math.max(1, x1 - x0), S.row - 3];
}
export function cells(ctx, v, fn, S = STRIP) {
  clipX(ctx, v);
  for (let i = 0; i < NW; i++) { const st = fn(i); if (!st || st.a <= 0) continue; const [x, y, w, h] = cellRect(v, i, S); H3.rect(ctx, x, y - (st.dy || 0), w, h, st.c, st.a); }
  ctx.restore();
}
export function ring(ctx, v, i, a, S = STRIP) { if (a <= 0) return; const [x, y, w, h] = cellRect(v, i, S); H3.srect(ctx, x - 6, y - 6, w + 12, h + 12, C.ink, 4, a); }
export function split(ctx, v, y0, y1, a = 1) { if (a <= 0) return; const x = X(v, SPLIT); H3.line(ctx, [[x, y0], [x, y1]], C.muted, 2, { alpha: a, dash: [6, 8], cap: 'butt' }); }
export function years(ctx, v, y = 900, o = {}) {
  const a = o.alpha ?? 1;
  H3.text(ctx, CL('first_start').slice(-4), X(v, 0), y, 'note', { color: C.muted, alpha: a });
  H3.text(ctx, CL('best_start_year'), X(v, SPLIT), y, 'note', { color: C.muted, align: 'center', alpha: a });
  if (o.today !== false) H3.text(ctx, 'today', X(v, NM - 1), y, 'note', { color: C.muted, align: o.todayAlign || 'right', alpha: a });
}
export function frame(ctx, v, i, o = {}) {
  const a = o.alpha ?? 1; if (a <= 0) return;
  const x0 = X(v, i), x1 = X(v, i + 120), top = v.Yt - 26;
  H3.rect(ctx, x0, top, x1 - x0, v.Yb - top, C.ink, 0.05 * a);
  H3.srect(ctx, x0, top, x1 - x0, v.Yb - top, C.ink, 3, a);
  const K = o.ride == null ? 120 : clamp(o.ride, 0, 120);
  if (o.track !== false) { const pts = []; for (let k = 0; k <= Math.min(119, Math.floor(K)); k++) pts.push([X(v, i + k), Y(v, tv(i, k))]); H3.line(ctx, pts, C.ink, o.tlw ?? 4, { alpha: a }); }
  const yr = Y(v, railV(i));
  H3.line(ctx, [[x0, yr], [x1, yr]], C.muted, o.rlw ?? 5, { alpha: a, cap: 'butt' });
  if (o.glow !== false) {
    let s = -1;
    for (let k = 0; k <= Math.min(120, Math.floor(K)); k++) {
      const on = k < 120 && k <= K && above(i, k);
      if (on && s < 0) s = k;
      if (!on && s >= 0) { H3.line(ctx, [[X(v, i + s), yr], [X(v, i + k), yr]], C.warn, (o.rlw ?? 5) + 4, { alpha: a, cap: 'butt' }); s = -1; }
    }
    if (s >= 0) H3.line(ctx, [[X(v, i + s), yr], [X(v, i + Math.min(120, K + 1)), yr]], C.warn, (o.rlw ?? 5) + 4, { alpha: a, cap: 'butt' });
  }
  if (o.bead !== false && o.ride != null) { const k = Math.min(119, Math.floor(K)); H3.diamond(ctx, X(v, i + k), Y(v, tv(i, k)), o.br ?? 16, C.ink, a); }
  return { yr, x0, x1, top };
}
export const JAR_MAX = 16000;
export function jar(ctx, x, y0, y1, w, val, a = 1, max = JAR_MAX) {
  if (a <= 0) return;
  const h = y1 - y0, lv = clamp(val / max) * (h - 12);
  ctx.save(); ctx.globalAlpha = a; H3.roundRect(ctx, x, y0, w, h, 18); ctx.clip();
  H3.rect(ctx, x, y1 - lv - 6, w, lv + 6, C.cushion, lv > 0.5 ? 1 : 0); ctx.restore();
  ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = C.muted; ctx.lineWidth = 4; H3.roundRect(ctx, x, y0, w, h, 18); ctx.stroke(); ctx.restore();
}
export const coins = H3.coins;

// ---------- the KEY-4 jar run (k4.js draw, parameterised by replay and jar scale) ----------
const D2 = H2.DATA.detail;
export function jarRun(ctx, start, n, o = {}) {
  const D = D2[start], FX = H2.FIXED, k = Math.min(119, Math.floor(n)), v = n <= 0 ? 0 : D.cushion[k];
  const P = o.P || H2.plane(400, 1340, 300, 920, o.r0 ?? 5.0, 19.5, 120);
  const J = { x: 1500, w: 210, top: 330, bot: 760 }, KJ = 380 / (o.jarMax ?? 1046);
  const above = n > 0 && D.path[k] > FX, below = n > 0 && n < 119 && D.path[k] <= FX;
  H2.replay(ctx, P, D.path, n, { beadR: 26, lw: 7, railW: 12 });
  H2.numWord(ctx, CL('fixed_rate'), 'fixed', P.x0 - 30, P.Y(FX) + 20, 'label', { align: 'right' });
  const lv = Math.min(380, Math.max(0, v) * KJ);
  ctx.save(); H2.roundRect(ctx, J.x, J.top, J.w, J.bot - J.top, 22); ctx.clip(); H2.rect(ctx, J.x, J.bot - lv, J.w, lv, C.cushion, 1); ctx.restore();
  if (below && o.flow !== false) {
    const bx = P.X(n), gy = (P.Y(D.path[k]) + P.Y(FX)) / 2, mx = J.x + J.w / 2, pts = [];
    for (let u = 0; u <= 1.0001; u += 0.04) { const cx = (bx + mx) / 2, cy = 170; pts.push([(1 - u) * (1 - u) * bx + 2 * u * (1 - u) * cx + u * u * mx, (1 - u) * (1 - u) * gy + 2 * u * (1 - u) * cy + u * u * (J.top - 10)]); }
    H2.line(ctx, pts, C.cushion, 10, { alpha: 0.9 });
    H2.line(ctx, [[mx, J.top - 10], [mx, J.bot - lv]], C.cushion, 10, { cap: 'butt', alpha: 0.9 });
  }
  H2.line(ctx, [[J.x + J.w - 4, J.bot - 30], [J.x + J.w + 46, J.bot - 30], [J.x + J.w + 46, J.bot - 6]], C.muted, 10, { cap: 'butt' });
  if (above && v > 0 && o.flow !== false) {
    H2.line(ctx, [[J.x + J.w + 46, J.bot - 6], [J.x + J.w + 46, J.bot + 80]], C.warn, 12, { cap: 'butt' });
    H2.line(ctx, [[J.x + 4, J.bot - lv], [J.x + J.w - 4, J.bot - lv]], C.warn, 10, { cap: 'butt' });
  }
  ctx.save(); ctx.strokeStyle = C.muted; ctx.lineWidth = 6; H2.roundRect(ctx, J.x, J.top, J.w, J.bot - J.top, 22); ctx.stroke(); ctx.restore();
  if (v < 0) H2.negArea(ctx, J.x, J.bot + 110, J.w, -v * 150 / 7577, 1, 22);
  H2.badge(ctx, 1);
}

// ---------- the "history, not a forecast" view: the ridge ends at today, empty space to its right ----------
export function ridgeToday(ctx, a = 1, o = {}) {
  const v = V({ m1: NM + 330, Yt: 300, Yb: 700 });
  ridge(ctx, v, { alpha: a });
  const xT = X(v, NM - 1);
  H3.line(ctx, [[xT, Y(v, SER[NM - 1]) - 40], [xT, v.Yb]], C.muted, 3, { alpha: a, dash: [6, 8], cap: 'butt' });
  if (o.labels !== false) {
    H3.text(ctx, 'today', xT, v.Yb + 80, 'note', { color: C.muted, align: 'center', alpha: a });
  }
  return v;
}

// month-by-month cushion (cumulative interest saved vs the 9% fixed loan) for window i: same arithmetic as model/model.py
// (payment re-amortised whenever the rate changes), copied from design/c3/final/src/build_data.py run2()/detail()
function run2(path) { let bal = 50000, cur = null, pay = 0; const ints = []; for (let k = 0; k < 120; k++) { const r = path[k]; if (r !== cur) { const x = r / 1200; pay = bal * x / (1 - Math.pow(1 + x, -(120 - k))); cur = r; } const i = bal * r / 1200; ints.push(i); bal -= pay - i; } return ints; }
const FIXI = run2(Array(120).fill(9));
const CUSH = new Map();
export function cushionOf(i) {
  if (CUSH.has(i)) return CUSH.get(i);
  const p = []; for (let k = 0; k < 120; k++) p.push(+rate(i, k).toFixed(6));
  const vi = run2(p); let c = 0; const out = vi.map((x, k) => (c += FIXI[k] - x));
  if (Math.abs(-out[119] - WIN[i].diff) > 0.5) throw new Error('cushion mismatch ' + i + ' ' + out[119] + ' ' + WIN[i].diff);
  CUSH.set(i, out); return out;
}
