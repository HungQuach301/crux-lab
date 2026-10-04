// H2 "Hình học của lãi" engine. Code pattern reused from episodes/ep001/design/c3/final/src/engine.js (text tiers,
// CL(), easing, boot/frame API); scenes, objects and layouts are new. Design space 1920x1080 (token sizes are px at
// 1080p), drawn into a 1280x720 canvas (scale 2/3). Every scene is a pure function of t.
// Flags: MASK  -> every text box is replaced by a flat `surface` block (masked strips, done in the build, not after);
//        NOTEXT -> text layer skipped entirely (graphics-only layer for the self-check).
export const TOK = await (await fetch('/tokens.json')).json();
export const DATA = window.DATA;
export const W = 1920, H = 1080, OW = 1280, OH = 720, S = OW / W;
const col = TOK.color;
export const C = { bg: col.bg, surface: col.surface, grid: col.grid, ink: col.ink, muted: col['ink-muted'], accent: col.accent,
  warn: col.warn, positive: col.positive, negative: col.negative };
export const TIER = TOK.type.tiers;
export const FLAGS = { mask: false, notext: false };

// ---------- claims ----------
export const USED = new Set();
export function CL(id) { const d = DATA.claims[id]; if (!d) throw new Error('unknown claim ' + id); USED.add(id); return d; }

// ---------- easing ----------
export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lin = (t, a, b) => clamp((t - a) / (b - a));
export const smooth = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
export const ease = (t, a, b) => smooth(lin(t, a, b));
export const easeOut = (t, a, b) => { const x = lin(t, a, b); return 1 - Math.pow(1 - x, 3); };
export const back = (t, a, b) => { const x = lin(t, a, b), s = 1.4; return 1 + (s + 1) * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2); };
export const mix = (a, b, x) => a + (b - a) * x;
export const inout = (t, a, b, c, d) => Math.min(ease(t, a, b), 1 - ease(t, c, d));
export function rgba(hex, a) { const n = parseInt(hex.slice(1), 16); return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`; }

// ---------- text ----------
export let FRAME_TEXTS = [];
export const TEXTLOG = new Map();
let CUR_T = 0;
export function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
}
export function measure(ctx, s, tier, weight) { const T = TIER[tier]; ctx.save(); ctx.font = `${weight || T.weight} ${T.px}px Inter`; ctx.fontVariantNumeric = 'tabular-nums'; const w = ctx.measureText(s).width; ctx.restore(); return w; }
// box in design px of the inked glyphs
function inkBox(ctx, s, x, y) {
  const m = ctx.measureText(s);
  return [x - m.actualBoundingBoxLeft, y - m.actualBoundingBoxAscent, m.actualBoundingBoxLeft + m.actualBoundingBoxRight, m.actualBoundingBoxAscent + m.actualBoundingBoxDescent];
}
function logText(s, tier, px, color, box, alpha, bgFill, pill) {
  const ob = box.map((v) => v * S);
  FRAME_TEXTS.push({ s, tier, px, color, box: ob, alpha, bgFill, pill: pill ? pill.map((v) => v * S) : null });
  if (alpha >= 0.2) {
    const out = ob[0] < 26 || ob[1] < 24 || ob[0] + ob[2] > OW - 26 || ob[1] + ob[3] > OH - 12;
    const e = TEXTLOG.get(s) || { tier, px, n: 0, out: 0, firstT: CUR_T, color }; e.n++; if (out) e.out++; TEXTLOG.set(s, e);
  }
}
function maskBlock(ctx, box, alpha) { ctx.save(); ctx.globalAlpha = Math.max(alpha, 0.999); ctx.fillStyle = C.surface; ctx.fillRect(box[0] - 3, box[1] - 3, box[2] + 6, box[3] + 6); ctx.restore(); }
// tier: hero | number | head | caption | label | note ; o: color, align, alpha, weight
export function text(ctx, s, x, y, tier, o = {}) {
  const T = TIER[tier]; if (!T) throw new Error('tier ' + tier);
  const alpha = o.alpha === undefined ? 1 : o.alpha;
  if (alpha <= 0.02 || !s) return 0;
  const px = T.px, weight = o.weight || T.weight;
  ctx.save(); ctx.font = `${weight} ${px}px Inter`; ctx.textAlign = o.align || 'left'; ctx.textBaseline = 'alphabetic'; ctx.fontVariantNumeric = 'tabular-nums';
  const w = ctx.measureText(s).width; const box = inkBox(ctx, s, x, y);
  ctx.restore();
  logText(s, tier, px, o.color || C.ink, box, alpha, null);
  if (FLAGS.notext) return w;
  if (FLAGS.mask) { if (alpha > 0.15) maskBlock(ctx, box, alpha); return w; }
  ctx.save(); ctx.globalAlpha = alpha; ctx.font = `${weight} ${px}px Inter`; ctx.textAlign = o.align || 'left'; ctx.textBaseline = 'alphabetic'; ctx.fontVariantNumeric = 'tabular-nums';
  ctx.fillStyle = o.color || C.ink; ctx.fillText(s, x, y); ctx.restore();
  return w;
}
// a number + a muted word after it (lesson D5: secondary words next to an emphasised number are ink-muted)
export function numWord(ctx, num, word, x, y, tier, o = {}) {
  const w1 = measure(ctx, num, tier), w2 = word ? measure(ctx, ' ' + word, tier, 600) : 0;
  let x0 = o.align === 'center' ? x - (w1 + w2) / 2 : o.align === 'right' ? x - w1 - w2 : x;
  text(ctx, num, x0, y, tier, { color: o.color || C.ink, alpha: o.alpha });
  if (word) text(ctx, word, x0 + w1 + measure(ctx, ' ', tier), y, tier, { color: C.muted, alpha: o.alpha, weight: 600 });
  return w1 + w2;
}
export function badge(ctx, alpha = 1) { // ILLUSTRATIVE pill, top right, type.badge (48 px at 1080)
  if (alpha <= 0.02) return;
  const s = 'ILLUSTRATIVE', px = TOK.type.badge.px, xr = W - 96, y = 112;
  ctx.save(); ctx.font = `700 ${px}px Inter`; const w = ctx.measureText(s).width; const box = inkBox(ctx, s, xr - w, y); ctx.restore();
  const pill = [xr - w - 18, y - px * 0.76 - 13, w + 36, px * 0.98 + 26];
  logText(s, 'badge', px, C.bg, box, alpha, C.warn, pill);
  if (FLAGS.notext) return;
  if (FLAGS.mask) { maskBlock(ctx, pill, alpha); return; }
  ctx.save(); ctx.globalAlpha = alpha; ctx.fillStyle = C.warn; roundRect(ctx, ...pill, 9); ctx.fill();
  ctx.font = `700 ${px}px Inter`; ctx.fillStyle = C.bg; ctx.fillText(s, xr - w, y); ctx.restore();
}

// ---------- primitives ----------
export function line(ctx, pts, color, lw, o = {}) {
  if (pts.length < 2) return; ctx.save(); ctx.globalAlpha = o.alpha === undefined ? 1 : o.alpha; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineJoin = 'round'; ctx.lineCap = o.cap || 'round';
  if (o.dash) ctx.setLineDash(o.dash); ctx.beginPath(); pts.forEach((p, i) => (i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]))); ctx.stroke(); ctx.restore();
}
export function poly(ctx, pts, fill, a = 1) { if (a <= 0.001 || pts.length < 3) return; ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = fill; ctx.beginPath(); pts.forEach((p, i) => (i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]))); ctx.closePath(); ctx.fill(); ctx.restore(); }
export function rect(ctx, x, y, w, h, fill, a = 1) { if (a <= 0.001 || !h || !w) return; ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); ctx.restore(); }
export function srect(ctx, x, y, w, h, color, lw, a = 1, dash) { if (a <= 0.001) return; ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = color; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); ctx.restore(); }
// costlier areas: solid negative with bg diagonal seams (texture = second channel vs positive/warn under CVD)
export function negArea(ctx, x, y, w, h, a = 1, step = 22) {
  if (h < 0) { y += h; h = -h; } if (a <= 0.001 || h <= 0.5 || w <= 0) return;
  rect(ctx, x, y, w, h, C.negative, a);
  ctx.save(); ctx.globalAlpha = a; ctx.beginPath(); ctx.rect(x, y, w, h); ctx.clip(); ctx.strokeStyle = C.bg; ctx.lineWidth = 5; ctx.beginPath();
  for (let k = -h - 40; k < w + h; k += step) { ctx.moveTo(x + k, y + h); ctx.lineTo(x + k + h, y); } ctx.stroke(); ctx.restore();
}
export function diamond(ctx, cx, cy, r, a = 1) { // Leah = ink + diamond, with a bg keyline so it reads on any fill
  if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; ctx.beginPath(); ctx.moveTo(cx, cy - r); ctx.lineTo(cx + r * 0.78, cy); ctx.lineTo(cx, cy + r); ctx.lineTo(cx - r * 0.78, cy); ctx.closePath();
  ctx.fillStyle = C.ink; ctx.fill(); ctx.lineWidth = 5; ctx.strokeStyle = C.bg; ctx.stroke(); ctx.restore();
}

// ---------- rate plane ----------
// P = {x0, x1, y0 (top), y1 (bottom), r0 (rate at bottom), r1 (rate at top), months}
export const FIXED = 9.0;
export function plane(x0, x1, y0, y1, r0, r1, months = 120) {
  return { x0, x1, y0, y1, r0, r1, months, X: (k) => x0 + (x1 - x0) * k / months, Y: (r) => y1 - (y1 - y0) * (r - r0) / (r1 - r0) };
}
// path: array of monthly rates; upto: months drawn (fractional). Fills between path and rail: positive below, warn above.
export function bandFill(ctx, P, path, upto, o = {}) {
  const n = Math.min(path.length - 1, upto); if (n <= 0) return;
  const pts = []; for (let k = 0; k <= Math.floor(n); k++) pts.push([k, path[k]]);
  if (n % 1) { const k = Math.floor(n); pts.push([n, mix(path[k], path[k + 1], n - k)]); }
  const yR = P.Y(FIXED), aG = o.aPos ?? 0.55, aW = o.aWarn ?? 0.72;
  // split at rail crossings, then fill each run of same-side months as ONE polygon (no seams between months)
  const sp = [pts[0]];
  for (let i = 0; i < pts.length - 1; i++) {
    const [ka, ra] = pts[i], [kb, rb] = pts[i + 1];
    if ((ra - FIXED) * (rb - FIXED) < 0) sp.push([ka + (kb - ka) * (FIXED - ra) / (rb - ra), FIXED]);
    sp.push(pts[i + 1]);
  }
  let run = [sp[0]], side = 0;
  const flush = () => { if (run.length > 1 && side) poly(ctx, [[P.X(run[0][0]), yR], ...run.map(([k, r]) => [P.X(k), P.Y(r)]), [P.X(run[run.length - 1][0]), yR]], side > 0 ? C.warn : C.positive, side > 0 ? aW : aG); };
  for (let i = 1; i < sp.length; i++) {
    const s2 = Math.sign((sp[i - 1][1] + sp[i][1]) / 2 - FIXED);
    if (s2 !== side && side !== 0) { flush(); run = [sp[i - 1]]; }
    side = s2 || side; run.push(sp[i]);
  }
  flush();
}
export function pathPts(P, path, upto, dy = 0) {
  const n = Math.min(path.length - 1, upto), pts = [];
  for (let k = 0; k <= Math.floor(n); k++) pts.push([P.X(k), P.Y(path[k]) + dy]);
  if (n % 1 && Math.floor(n) + 1 < path.length) { const k = Math.floor(n); pts.push([P.X(n), P.Y(mix(path[k], path[k + 1], n - k)) + dy]); }
  return pts;
}
export function rateAt(path, n) { const k = Math.min(path.length - 1, Math.floor(n)); return k + 1 < path.length ? mix(path[k], path[k + 1], n - k) : path[k]; }
// the rail: thick level ink line; segments under the path where rate > 9% glow warn
export function rail(ctx, P, path, upto, a = 1, x1 = null, lw = 10) {
  const yR = P.Y(FIXED);
  line(ctx, [[P.x0, yR], [x1 ?? P.x1, yR]], C.ink, lw, { alpha: a, cap: 'butt' });
  if (!path) return;
  const n = Math.min(path.length - 1, upto);
  for (let k = 0; k < n; k++) {
    const ra = path[k], rb = rateAt(path, Math.min(n, k + 1));
    if (ra <= FIXED && rb <= FIXED) continue;
    let ka = k, kb = Math.min(n, k + 1);
    if (ra <= FIXED) ka = k + (FIXED - ra) / (rb - ra) * (kb - k); else if (rb <= FIXED) kb = k + (FIXED - ra) / (rb - ra) * (kb - k);
    line(ctx, [[P.X(ka), yR], [P.X(kb), yR]], C.warn, lw + 6, { alpha: a, cap: 'butt' });
  }
}

// ---------- history ridge (T-bill, accent) ----------
export const RIDGE = DATA.ridge; // from 1953-01
export const IDX = RIDGE[RIDGE.length - 1].r;
export const ridgeIndex = (ym) => RIDGE.findIndex((d) => d.m === ym);
export function ridgeGeom(x0, x1, y0, y1, rmax = 17, from = '1954-01') {
  const i0 = ridgeIndex(from), n = RIDGE.length - 1 - i0;
  return { x0, x1, y0, y1, i0, n, X: (i) => x0 + (x1 - x0) * (i - i0) / n, Y: (r) => y1 - (y1 - y0) * r / rmax };
}
export function drawRidge(ctx, G, a = 1, upto = 1) {
  const pts = []; const last = G.i0 + Math.round(G.n * upto);
  for (let i = G.i0; i <= last; i++) pts.push([G.X(i), G.Y(RIDGE[i].r)]);
  poly(ctx, [[G.x0, G.y1], ...pts, [pts[pts.length - 1][0], G.y1]], C.accent, 0.16 * a);
  line(ctx, pts, C.accent, 4, { alpha: a });
  line(ctx, [[G.x0, G.y1], [G.x1, G.y1]], C.grid, 3, { alpha: a, cap: 'butt' });
}
// Leah's replayed path for the window starting at ridge index s (same formula as model.py)
export function replayPath(s, var0 = 7.5) { const m = var0 - IDX, p = []; for (let k = 0; k < 120; k++) p.push(+(m + Math.max(0, IDX + RIDGE[s + k].r - RIDGE[s].r)).toFixed(6)); return p; }
export const STARTS = DATA.starts; // 753 start months
export const startRidgeIdx = (j) => ridgeIndex(STARTS[0]) + j;
export const SPLIT_J = STARTS.indexOf('1981-01');

// ---------- cushion tank ----------
// T = {x, w, yZero, top, bottom, k (px per $)}; value in $ (+ = cushion, - = costlier)
export function tank(ctx, T, value, a = 1, o = {}) {
  srect(ctx, T.x, T.top, T.w, T.bottom - T.top, C.grid, 4, a);
  const hpx = value * T.k;
  if (hpx > 0) rect(ctx, T.x + 2, T.yZero - hpx, T.w - 4, hpx, C.positive, a);
  else negArea(ctx, T.x + 2, T.yZero, T.w - 4, -hpx, a);
  line(ctx, [[T.x - 14, T.yZero], [T.x + T.w + 14, T.yZero]], C.ink, 5, { alpha: a, cap: 'butt' });
}
// flying slabs: each month's saving (+) / extra (-) leaves the band at month k and lands on the tank surface
export function slabs(ctx, P, T, path, cum, n, a = 1, flight = 4) {
  for (let k = Math.max(0, Math.floor(n) - flight); k < Math.min(cum.length, Math.floor(n) + 1); k++) {
    const f = clamp((n - k) / flight); if (f >= 1) continue;
    const amt = cum[k] - (k ? cum[k - 1] : 0), h = Math.max(2, Math.abs(amt) * T.k);
    const sx = P.X(k + 0.5), sy = mix(P.Y(path[k]), P.Y(FIXED), 0.5);
    const tx = T.x + T.w / 2, ty = T.yZero - (k ? cum[k - 1] : 0) * T.k - (amt > 0 ? h / 2 : -h / 2);
    const e = smooth(f), x = mix(sx, tx, e), y = mix(sy, ty, e) - Math.sin(e * Math.PI) * 60, w = mix(14, T.w - 4, e);
    rect(ctx, x - w / 2, y - h / 2, w, h, amt > 0 ? C.positive : C.warn, a * (1 - 0.3 * e));
  }
}

// ---------- boot ----------
export function boot(mod) {
  const out = document.createElement('canvas'); out.width = OW; out.height = OH; document.body.appendChild(out);
  const ctx = out.getContext('2d', { willReadFrequently: true });
  const scene = mod.build ? mod.build() : mod;
  function draw(t, flags = {}) {
    CUR_T = t; FLAGS.mask = !!flags.mask; FLAGS.notext = !!flags.notext; FRAME_TEXTS = [];
    ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.fillStyle = C.bg; ctx.fillRect(0, 0, OW, OH);
    ctx.setTransform(S, 0, 0, S, 0, 0);
    scene.draw(ctx, t);
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    FLAGS.mask = FLAGS.notext = false;
  }
  const b64 = (u8) => { let s = ''; const n = 0x8000; for (let i = 0; i < u8.length; i += n) s += String.fromCharCode.apply(null, u8.subarray(i, i + n)); return btoa(s); };
  const N = Math.round(scene.duration * 30);
  // self-check for one frame: text vs graphics distance (D4), local contrast (D2), text-text distance
  function check(t) {
    draw(t, { notext: true });
    const texts = FRAME_TEXTS.filter((x) => x.alpha >= 0.98);
    const img = ctx.getImageData(0, 0, OW, OH).data;
    const bgc = [14, 17, 22];
    const lum = (r, g, b) => { const f = (c) => { c /= 255; return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
    const hexl = (h) => { const n = parseInt(h.slice(1), 16); return lum(n >> 16, (n >> 8) & 255, n & 255); };
    const res = [];
    for (const tx of texts) {
      const [bx, by, bw, bh] = tx.pill || tx.box; const R = 14; // badge: distance measured from its pill
      let dmin = 99, worstC = 99;
      const tl = hexl(tx.color);
      if (tx.bgFill) { const bl = hexl(tx.bgFill); worstC = (Math.max(tl, bl) + 0.05) / (Math.min(tl, bl) + 0.05); }
      for (let y = Math.max(0, Math.floor(by - R)); y < Math.min(OH, Math.ceil(by + bh + R)); y++) for (let x = Math.max(0, Math.floor(bx - R)); x < Math.min(OW, Math.ceil(bx + bw + R)); x++) {
        const i = (y * OW + x) * 4, d = Math.abs(img[i] - bgc[0]) + Math.abs(img[i + 1] - bgc[1]) + Math.abs(img[i + 2] - bgc[2]);
        const inside = x >= bx && x < bx + bw && y >= by && y < by + bh;
        if (!tx.bgFill && inside) { const l = lum(img[i], img[i + 1], img[i + 2]); const c = (Math.max(tl, l) + 0.05) / (Math.min(tl, l) + 0.05); if (c < worstC) worstC = c; }
        if (d <= 30) continue;
        const dx = Math.max(bx - x - 1, 0, x - (bx + bw)), dy = Math.max(by - y - 1, 0, y - (by + bh));
        const dd = Math.hypot(dx, dy); if (dd < dmin) dmin = dd;
      }
      let dtext = 99;
      for (const o of texts) { if (o === tx) continue; const [ox, oy, ow, oh] = o.box; const dx = Math.max(ox - (bx + bw), 0, bx - (ox + ow)), dy = Math.max(oy - (by + bh), 0, by - (oy + oh)); dtext = Math.min(dtext, Math.hypot(dx, dy)); }
      res.push({ s: tx.s, px: tx.px, dGraphic: +dmin.toFixed(1), dText: +dtext.toFixed(1), contrast: +worstC.toFixed(2) });
    }
    return res;
  }
  return {
    duration: scene.duration, frames: N, stripTimes: scene.stripTimes,
    frame(t) { draw(t); return b64(new Uint8Array(ctx.getImageData(0, 0, OW, OH).data.buffer)); },
    png(t, flags) { draw(t, flags); return out.toDataURL('image/png'); },
    texts(t) { draw(t); return FRAME_TEXTS.map((x) => ({ s: x.s, px: x.px, box: x.box.map((v) => +v.toFixed(1)) })); },
    check,
    log: () => ({ used: [...USED].sort(), texts: [...TEXTLOG.entries()].map(([s, e]) => ({ s, ...e })) }),
    strip(times, mask) { // 3x2 grid, 1920 x 1128: six 624x351 frames, numbered 1-6 under each, no captions
      const tw = 624, th = 351, g = 12, lab = 50;
      const sc = document.createElement('canvas'); sc.width = 3 * tw + 4 * g; sc.height = 2 * (th + lab) + 3 * g; const q = sc.getContext('2d');
      q.fillStyle = '#06080B'; q.fillRect(0, 0, sc.width, sc.height);
      times.forEach((t, i) => {
        const cx = g + (i % 3) * (tw + g), cy = g + Math.floor(i / 3) * (th + lab + g);
        draw(t, { mask }); q.drawImage(out, cx, cy, tw, th);
        q.fillStyle = C.ink; q.font = '700 34px Inter'; q.textAlign = 'center'; q.fillText(String(i + 1), cx + tw / 2, cy + th + 40);
      });
      return sc.toDataURL('image/png');
    },
  };
}

// one replay on a plane: fills, rail (with warn segments), variable line (accent), Leah's diamond at the head
export function replay(ctx, P, path, n, o = {}) {
  const a = o.alpha ?? 1;
  ctx.save(); ctx.beginPath(); ctx.rect(P.x0 - 30, P.y0 - 30, P.x1 - P.x0 + 60, P.y1 - P.y0 + 60); ctx.clip();
  if (o.fill !== false) bandFill(ctx, P, path, n, { aPos: (o.aPos ?? 0.55) * a, aWarn: (o.aWarn ?? 0.72) * a });
  rail(ctx, P, o.railPath === false ? null : path, n, o.railAlpha ?? a, null, o.railW ?? 10);
  line(ctx, pathPts(P, path, n), C.accent, o.lw ?? 6, { alpha: a });
  ctx.restore();
  if (o.bead !== false && n >= 0) diamond(ctx, P.X(Math.min(n, path.length - 1)), P.Y(rateAt(path, Math.min(n, path.length - 1))), o.beadR ?? 24, a);
}
// result bins under the ridge: cells (one per start month) placed under their start month, or sorted (costlier first)
export function binGeom(G) {
  const j0 = ridgeIndex(STARTS[0]);
  const xs = STARTS.map((_, j) => G.X(j0 + j));
  const cw = (G.x1 - G.x0) / G.n;
  return { xs, cw, L: [xs[0], xs[SPLIT_J - 1] + cw], R: [xs[SPLIT_J], xs[STARTS.length - 1] + cw] };
}
