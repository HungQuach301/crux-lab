// Crux factory templates (Mốc B). Each template: draw(E, t, p, d) — t seconds since the shot started, p resolved params (every "@word"
// anchor already turned into seconds since the shot start by build.py, so an element never appears before its word), d shot length.
// Generalised from the symbols that passed blind checks in Tập 1–3 (toolkit/visual-library/README.md); new code, parameterised:
//   title    hook / question card (cold open, chapter question)            V-none (text)
//   bignum   one claim, large, with a caption                              number card
//   bars     same-scale bars from 0 (axis always starts at 0)              V2 family
//   line     series drawn left→right = time, optional fixed level (still)  V3 "đường lãi so vạch"
//   swarm    every replay window becomes one dot on a value axis with a fixed gate; dots above the gate change colour; tally "X of N"
//                                                                           V1 "lưới ô chạy lại" + Tập 3 "đàn chấm về đích"
//   paths    one saver, two paths side by side, nothing highlighted          V4 / Tập 3 KEY-1
//   timeline a span of years with a hatched what-if stretch and its label   Tập 3 KEY-2
//   method   "How we know this" card, ≤ 6 lines                             V7
//   person   faceless illustrative figure + caption (badge automatic)       V4 figure
//   endcard  next episode line + end-screen space
// Colour roles never change meaning: accent = market rate / roll, muted = fixed level (never moves), warn = above the fixed level,
// ink = the viewer-like person and plain text. A template never writes a number that is not a claim ({claimId} or claim: …).
import { ease, easeOut, lin, mix, clamp, TIERS } from './engine.js';

const at = (p, k, def = 0) => (typeof p[k] === 'number' ? p[k] : def);
const fade = (t, a0) => ease(t, a0, a0 + 0.4);
const role = (E, r) => ({ accent: E.C.accent, muted: E.C.muted, warn: E.C.warn, ink: E.C.ink })[r] || E.C.accent;
const num = (E, id) => { const c = E.claims[id]; const v = typeof c.value === 'number' ? c.value : parseFloat(String(c.value).replace(/[^\d.-]/g, '')); if (!isFinite(v)) throw new Error('claim ' + id + ' is not numeric'); return v; };
const series = (E, key) => { const v = typeof key === 'string' ? key.split('.').reduce((o, k) => o?.[k], E.data) : key; if (!Array.isArray(v)) throw new Error('no data ' + key); return v; };
// Shorts: the plot sits between the hook/badge/title block (top) and the counterweight + history lines (bottom, engine)
const box = (E) => ({ x0: E.SAFE.x0 + 24, x1: E.SAFE.x1 - 24, y0: E.SAFE.y0 + (E.V ? 440 : 150), y1: E.SAFE.y1 - (E.V ? 340 : 110) });

export const title = { draw(E, t, p) {
  const b = box(E), lines = p.lines || [], ats = p.ats || [];
  if (p.kicker) E.text(p.kicker, E.W / 2, b.y0 + 40, 'caption', { align: 'center', color: E.C.muted, alpha: fade(t, at(p, 'at')) });
  const y0 = E.V ? E.H * 0.42 : E.H * 0.46, step = E.V ? 110 : 96;
  lines.forEach((s, i) => E.text(s, E.W / 2, y0 + i * step, i === 0 ? 'head' : 'caption', { align: 'center', alpha: fade(t, ats[i] ?? at(p, 'at')), group: 'title' + i }));
} };

export const bignum = { draw(E, t, p) {
  const a0 = at(p, 'at'), y = E.V ? E.H * 0.45 : E.H * 0.5, k = easeOut(t, a0, a0 + 0.5);
  E.ctx.save(); E.ctx.translate(E.W / 2, y); E.ctx.scale(0.9 + 0.1 * k, 0.9 + 0.1 * k); E.ctx.translate(-E.W / 2, -y);
  E.text(`{${p.claim}}`, E.W / 2, y, 'hero', { align: 'center', alpha: k, color: role(E, p.role || 'ink'), group: 'big' });
  E.ctx.restore();
  if (p.caption) E.text(p.caption, E.W / 2, y + (E.V ? 150 : 120), 'caption', { align: 'center', alpha: fade(t, at(p, 'captionAt', a0 + 0.3)) });
  if (p.sub) E.text(p.sub, E.W / 2, y + (E.V ? 240 : 200), 'note', { align: 'center', color: E.C.muted, alpha: fade(t, at(p, 'subAt', a0 + 0.6)) });
} };

export const bars = { draw(E, t, p) { // same scale, axis from 0 (no parameter turns this off)
  const b = box(E), items = p.items || [], n = items.length; if (!n) return;
  const vals = items.map((it) => num(E, it.claim)); if (vals.some((v) => v < 0)) throw new Error('bars: negative values need a signed template');
  const vmax = Math.max(...vals) * 1.08, labW = E.V ? 0 : 420, x0 = b.x0 + labW, x1 = b.x1 - 220;
  if (E.V) return barsV(E, t, p, b, items, vals, vmax);
  const rowH = Math.min(170, (b.y1 - b.y0) / n), bh = Math.min(64, rowH * 0.45);
  if (p.title) E.text(p.title, b.x0, b.y0 - 30, 'caption', { alpha: fade(t, at(p, 'at')) });
  E.line([[x0, b.y0], [x0, b.y0 + rowH * n]], E.C.grid, 4, fade(t, at(p, 'at')));
  E.text('0', x0, b.y0 + rowH * n + 60, 'note', { align: 'center', color: E.C.muted, alpha: fade(t, at(p, 'at')), group: 'axis0' });
  items.forEach((it, i) => {
    const a0 = it.at ?? at(p, 'at') + 0.3 * i, g = easeOut(t, a0, a0 + 0.8), yc = b.y0 + rowH * (i + 0.5) + (E.V ? 40 : 0);
    const w = (x1 - x0) * vals[i] / vmax * g;
    if (E.V) E.text(it.label, x0, yc - bh / 2 - 22, 'label', { alpha: fade(t, a0), group: 'bl' + i });
    else E.text(it.label, x0 - 24, yc + 18, 'label', { align: 'right', alpha: fade(t, a0), group: 'bl' + i });
    E.rect(x0, yc - bh / 2, w, bh, role(E, it.role), fade(t, a0));
    E.text(`{${it.claim}}`, x0 + w + 20, yc + 18, 'label', { alpha: fade(t, a0 + 0.6), group: 'bv' + i });
  });
} };

// Shorts: one row per item = label (left) and value (right) on one line, the same-scale bar from 0 as a strip under it,
// so 12 rows fit between the title and the counterweight line without labels overlapping
function barsV(E, t, p, b, items, vals, vmax) {
  const top = E.SAFE.y0 + 410, bottom = E.SAFE.y1 - 195, n = items.length, rowH = Math.min(120, (bottom - top) / n);
  const bh = Math.max(5, Math.min(36, rowH - 61)), x0 = b.x0, x1 = b.x1;
  if (p.title) E.text(p.title, b.x0, top - 30, 'caption', { alpha: fade(t, at(p, 'at')), wrapUp: true });
  items.forEach((it, i) => {
    const a0 = it.at ?? at(p, 'at') + 0.3 * i, g = easeOut(t, a0, a0 + 0.8), yb = top + rowH * i + 45;
    E.text(it.label, x0, yb, 'label', { alpha: fade(t, a0), group: 'bl' + i });
    E.text(`{${it.claim}}`, x1, yb, 'label', { align: 'right', alpha: fade(t, a0 + 0.6), group: 'bv' + i });
    E.rect(x0, yb + 15, (x1 - x0) * vals[i] / vmax * g, bh, role(E, it.role), fade(t, a0));
  });
}

export const line = { draw(E, t, p) {
  const b = box(E), S = series(E, p.series), xk = p.x ?? 'x', yk = p.y ?? 'y', ys = S.map((r) => +r[yk]);
  const lvl = p.level ? num(E, p.level) : null, ymax = Math.max(...ys, lvl ?? 0) * 1.1, ymin = 0; // from 0
  const X = (i) => mix(b.x0 + 60, b.x1, i / (S.length - 1)), Y = (v) => mix(b.y1, b.y0, (v - ymin) / (ymax - ymin));
  const a0 = at(p, 'at0'), a1 = at(p, 'at1', a0 + 4), k = lin(t, a0, a1), nv = Math.max(2, Math.ceil(k * S.length));
  if (p.title) E.text(p.title, b.x0, b.y0 - 40, 'caption', { alpha: fade(t, a0), wrapUp: true });
  E.line([[b.x0 + 60, b.y1], [b.x1, b.y1]], E.C.grid, 4, fade(t, a0));
  E.text(String(S[0][xk]).slice(0, 4), b.x0 + 60, b.y1 + 64, 'note', { color: E.C.muted, alpha: fade(t, a0), group: 'x0' });
  E.text(String(S[S.length - 1][xk]).slice(0, 4), b.x1, b.y1 + 64, 'note', { align: 'right', color: E.C.muted, alpha: fade(t, a0), group: 'x1' });
  if (lvl != null) { const la = at(p, 'levelAt', a0); E.line([[b.x0 + 60, Y(lvl)], [b.x1, Y(lvl)]], E.C.muted, 6, fade(t, la));
    // Shorts: the plot is narrow, so the label goes where its plate covers the fewest points of the whole series (left/right/centre,
    // above/below the level); the plate never hides where the gain crosses
    let lx = b.x1, ly = Y(lvl) - 18, al = 'right';
    if (E.V) {
      const lw = E.measure(p.levelLabel || `{${p.level}}`, E.FLOOR, 600) + 28, pts = S.map((r, i) => [X(i), Y(ys[i])]);
      const cands = [['left', b.x0 + 60, -18], ['right', b.x1, -18], ['center', (b.x0 + 60 + b.x1) / 2, -18], ['left', b.x0 + 60, 78], ['right', b.x1, 78], ['center', (b.x0 + 60 + b.x1) / 2, 78]]
        .map(([a, x, dy]) => { const x0 = a === 'left' ? x : a === 'right' ? x - lw : x - lw / 2, y0 = Y(lvl) + dy - 0.8 * E.FLOOR - 20, y1 = y0 + 1.05 * E.FLOOR + 40;
          return { a, x, dy, n: pts.filter(([px, py]) => px >= x0 - 8 && px <= x0 + lw + 8 && py >= y0 && py <= y1).length }; });
      const best = cands.reduce((m, c) => (c.n < m.n ? c : m)); lx = best.x; ly = Y(lvl) + best.dy; al = best.a; }
    E.text(p.levelLabel || `{${p.level}}`, lx, ly, 'label', { align: al, color: E.C.ink, plate: E.C.surface, alpha: fade(t, la), group: 'lvl' }); }
  if (t < a0) return;
  for (let i = 1; i < nv; i++) { const hi = lvl != null && ys[i] > lvl;
    E.line([[X(i - 1), Y(ys[i - 1])], [X(i), Y(ys[i])]], hi ? E.C.warn : E.C.accent, 4, 1); }
} };

export const swarm = { draw(E, t, p) {
  const b = box(E), S = series(E, p.series), vk = p.value || 'v', vals = S.map((r) => +r[vk]);
  // gate: a claim id, or a definitional constant (the bond's ×2) that must name the claim defining it (gateDef)
  const gate = typeof p.gate === 'number' ? (p.gateDef ? (E.CL(p.gateDef), p.gate) : (() => { throw new Error('swarm: numeric gate needs gateDef'); })()) : num(E, p.gate), lo = p.min ?? 0, hi = p.max ?? Math.max(...vals) * 1.05;
  const X = (v) => mix(b.x0 + 40, b.x1 - 40, (v - lo) / (hi - lo)), base = b.y1 - (E.V ? 300 : 90);
  const a0 = at(p, 'at0'), a1 = at(p, 'at1', a0 + 6), r = E.V ? 7 : 6, bins = new Map();
  E.line([[b.x0 + 40, base + 24], [b.x1 - 40, base + 24]], E.C.grid, 4, fade(t, a0));
  const ga = at(p, 'gateAt', a0); E.line([[X(gate), b.y0 + 40], [X(gate), base + 40]], E.C.muted, 10, fade(t, ga));
  E.text(p.gateLabel || `{${p.gate}}`, X(gate) + 24, b.y0 + 60, 'number', { color: E.C.ink, alpha: fade(t, ga), group: 'gate' });
  if (p.axisLabel) E.text(p.axisLabel, E.V ? E.W / 2 : b.x1 - 40, E.V ? base + 68 : b.y0 + 40, 'note', { align: E.V ? 'center' : 'right', color: E.C.muted, alpha: fade(t, a0), group: 'axl' });
  // legend above the plot (what a dot is; the what-if mark of the hypothetical starts): hatch swatch + muted lines
  (p.legend || []).forEach((s, i) => { const la = at(p, 'legendAt', ga), y = E.SAFE.y0 + (E.V ? 250 + i * 72 : 50 + i * 58); // Shorts: below the hook line and the ILLUSTRATIVE badge
    if (i === 0 && p.legendHatch) E.hatch(b.x0, y - 34, 34, 34, fade(t, la), E.C.muted, 9);
    E.text(s, b.x0 + (i === 0 && p.legendHatch ? 48 : 0), y, 'note', { color: i ? E.C.muted : E.C.ink, alpha: fade(t, la), group: 'lg' + i }); });
  const order = vals.map((v, i) => i); // chronological: the data order
  const shown = Math.floor(lin(t, a0, a1) * order.length); let above = 0;
  // every dot stays visible: when the tallest stack would leave the plot, the rows tighten (dots overlap vertically) instead of dropping
  const binOf = (v) => Math.round((X(v) - b.x0) / (2 * r + 1)), full = new Map(); vals.forEach((v) => full.set(binOf(v), (full.get(binOf(v)) || 0) + 1));
  const dy = Math.min(2 * r + 1, (base - b.y0 - (E.V ? 200 : 120)) / Math.max(...full.values()));
  for (let j = 0; j < shown; j++) { const i = order[j], v = vals[i], bx = binOf(v), h = bins.get(bx) || 0; bins.set(bx, h + 1);
    const y = base - h * dy; if (v > gate) above++;
    E.dot(b.x0 + bx * (2 * r + 1) + r, y, r, v > gate ? E.C.warn : E.C.accent, Math.min(1, (shown - j) / 8 + 0.4)); }
  (p.marks || []).forEach((m, k) => { const i = S.findIndex((r2) => String(r2[p.key || 's']) === String(m.match)); if (i < 0) return; const ma = m.at ?? a1;
    E.dot(X(vals[i]), base + 24, r + 6, E.C.ink, fade(t, ma), E.C.ink); // on the axis, under the stack
    E.text(m.label, X(vals[i]), base + (E.V ? 150 + 92 * (k % 2) : 100), 'label', { align: 'center', plate: E.C.surface, alpha: fade(t, ma), group: 'm' + k }); });
  if (p.tally) { const ta = at(p, 'tallyAt', a1); E.text(p.tally, b.x1 - 40, b.y0 + (E.V ? 140 : 120), 'caption', { align: 'right', alpha: fade(t, ta), group: 'tally' }); }
  E.historical();
} };

export const paths = { draw(E, t, p) {
  const b = box(E), lanes = [p.a, p.b].filter(Boolean), gap = (b.y1 - b.y0) / (lanes.length + 1);
  lanes.forEach((L, i) => { const a0 = L.at ?? at(p, 'at') + 1.2 * i, y = b.y0 + gap * (i + 1), k = easeOut(t, a0, a0 + 2.5);
    E.text(L.label, b.x0, y - 56, 'label', { alpha: fade(t, a0), group: 'pl' + i });
    E.rect(b.x0, y - 26, (b.x1 - b.x0) * k, 52, role(E, L.role || (i ? 'accent' : 'muted')), fade(t, a0));
    if (L.end) E.text(L.end, b.x1, y + 90, 'note', { align: 'right', color: E.C.muted, alpha: fade(t, a0 + 1.5), group: 'pe' + i }); });
  if (p.question) E.text(p.question, E.W / 2, b.y1 - 10, 'head', { align: 'center', alpha: fade(t, at(p, 'questionAt', 4)), group: 'q' });
} };

export const timeline = { draw(E, t, p) {
  const b = box(E), y = E.V ? E.H * 0.5 : E.H * 0.55, h = 120, f = +p.from, to = +p.to, sp = +String(p.split).slice(0, 4) + ((+String(p.split).slice(5, 7) || 1) - 1) / 12;
  const X = (yr) => mix(b.x0, b.x1, (yr - f) / (to - f)), a0 = at(p, 'at0'), k = easeOut(t, a0, a0 + 1.5), sa = at(p, 'splitAt', a0 + 1.5);
  E.rect(b.x0, y - h / 2, (b.x1 - b.x0) * k, h, E.C.surface, 1);
  E.hatch(b.x0, y - h / 2, (X(sp) - b.x0), h, fade(t, sa));
  E.rect(X(sp), y - h / 2, (b.x1 - X(sp)) * lin(t, sa, sa + 0.6), h, E.C.ink, 0.85);
  E.text(String(f), b.x0, y + h / 2 + 64, 'note', { color: E.C.muted, alpha: fade(t, a0), group: 'tf' });
  E.text(String(to), b.x1, y + h / 2 + 64, 'note', { align: 'right', color: E.C.muted, alpha: fade(t, a0), group: 'tt' });
  if (p.splitLabel) E.text(p.splitLabel, X(sp), y - h / 2 - 30, 'label', { align: 'center', alpha: fade(t, sa), group: 'ts' });
  if (p.whatIf) E.text(p.whatIf, b.x0, y - h / 2 - 110, 'label', { plate: E.C.surface, alpha: fade(t, sa + 0.4), group: 'tw' });
} };

export const method = { draw(E, t, p) {
  const b = box(E), lines = (p.lines || []).slice(0, 6), a0 = at(p, 'at');
  E.ctx.save(); E.ctx.globalAlpha = fade(t, a0); E.ctx.fillStyle = E.C.surface; E.round(b.x0, b.y0 - 60, b.x1 - b.x0, b.y1 - b.y0 + 60, 18); E.ctx.fill(); E.ctx.restore();
  E.text(p.title || 'How we know this', b.x0 + 48, b.y0 + 40, 'head', { alpha: fade(t, a0), plate: undefined });
  const step = Math.min(E.V ? 150 : 110, (b.y1 - b.y0 - 140) / Math.max(1, lines.length));
  lines.forEach((s, i) => E.text(s, b.x0 + 48, b.y0 + 150 + i * step, 'note', { alpha: fade(t, a0 + 0.25 * (i + 1)), plate: E.C.surface, group: 'ml' + i }));
} };

export const person = { draw(E, t, p) {
  const a0 = at(p, 'at'), cx = E.V ? E.W / 2 : E.SAFE.x0 + 320, base = E.V ? E.H * 0.6 : E.SAFE.y1 - 40;
  E.person(cx, base, E.V ? 1.3 : 1.2, fade(t, a0));
  (p.caption || []).forEach((s, i) => E.text(s, E.V ? E.W / 2 : cx + 300, E.V ? base + 120 + i * 90 : E.H * 0.42 + i * 90, i ? 'label' : 'caption',
    { align: E.V ? 'center' : 'left', alpha: fade(t, (p.ats || [])[i] ?? a0 + 0.3 * i), group: 'pc' + i }));
} };

export const endcard = { draw(E, t, p) {
  const a0 = at(p, 'at');
  const y = E.V ? E.H * 0.45 : E.SAFE.y0 + 120;
  E.text(p.channel || 'Crux', E.W / 2, y, 'head', { align: 'center', alpha: fade(t, a0) });
  if (p.next) E.text(p.next, E.W / 2, y + 100, 'caption', { align: 'center', color: E.C.muted, alpha: fade(t, a0 + 0.3) });
} };

export const TEMPLATES = { title, bignum, bars, line, swarm, paths, timeline, method, person, endcard };
