// C4 animatic engine = the signed C3 final engine (design/c3/final/src/engine.js) with four changes:
//  1. type tiers from animatic tokens.json (every size -20%, floor 40 px at 1080p);
//  2. scenes keep 1920x1080 LOGICAL coordinates but render at 1280x720 (ctx transform; WebGL at 1280x720);
//  3. timing: every scene gets T (its sentences from timing.json, local seconds) and T.a(id) resolves an anchor from
//     anchors.json (sentence n + keyword) -> no hard-coded seconds for any meaningful action;
//  4. text({sent:true}) marks a sentence-caption (a line that restates narration); hidden when NOCAP (blind strips).
//  5 (C5). Renders at 1920x1080 (the signed system's own size; tokens canvas.out) through ONE page for the whole film
//     (film.js / film.html: window.CHECKS for the checker, window.APP for render.js), so the video and the check page
//     draw the same frames. Every 2D drawing call goes through a recording proxy of the canvas context (REC below):
//     each paint op belongs to a screen object (text or shape) with its box, colours, opacity, role; layer masks
//     redraw the frame keeping only some objects (CHECKS.layer). In 'all' mode the proxy only passes calls through.
// Every scene is a deterministic function of t (seconds, scene-local). Every number on screen goes through CL(claimId).
import * as THREE from 'three';
export { THREE };

export const TOK = window.TOK;
export const DATA = window.DATA;
export const W = TOK.canvas.w, H = TOK.canvas.h, OW = TOK.canvas.out.w, OH = TOK.canvas.out.h;
const col = TOK.color;
export const C = {
  bg: col.bg, surface: col.surface, grid: col.grid, ink: col.ink, muted: col['ink-muted'], accent: col.accent,
  warn: col.warn, positive: col.positive, negative: col.negative, ...TOK.materials,
};
export const TIER = TOK.type.tiers;

// ---------- claims ----------
// CL() returns the claim's display text and queues the id: the next text() call looks for each queued display in its
// string (at number boundaries) and reports those spans as claim spans (CHECKS.objects() -> claims[]). A number in a
// text that did not come through CL() is reported without a claim span (the checker counts it as an orphan).
export const USED = new Set();
const PEND = [];
export const SCENE_CL = new Map(); // scene id -> claim ids that scene took through CL() (build time included)
export function CL(id) {
  const c = DATA.claims[id];
  if (!c) throw new Error('unknown claim ' + id);
  USED.add(id); PEND.push(id);
  const L = SCENE_CL.get(REC.scene) || []; if (!L.includes(id)) { L.push(id); SCENE_CL.set(REC.scene, L); }
  return c.display;
}


// a year written on screen without a claim yet (axis ticks, data years): the same text either way; once out/claims.json has a
// claim `id` whose display is exactly `lit`, it goes through CL() and the page reports it as a claim span
export function CLY(id, lit) { const c = DATA.claims[id]; return c && String(c.display) === lit ? CL(id) : lit; }
// CLT(id, tok): a number token taken from a claim's display (e.g. the year 2026 of the date anchor "September 24, 2026"); the
// next text() reports it as a span of that claim. Call it inside the text() argument so the id is still queued.
export function CLT(id, tok) { const d = String(CL(id)); if (!new RegExp('(^|[^\\d])' + tok + '($|[^\\d])').test(d)) throw new Error('CLT: ' + tok + ' not in ' + id); return tok; }

// ---------- timing (timing.json + anchors.json) ----------
export const ANCH_USED = new Set();
export function makeT(timing, anchors, sid) {
  const sc = timing.scenes.find((x) => x.id === sid); if (!sc) throw new Error('no scene ' + sid);
  const byN = new Map(sc.sentences.map((x) => [x.n, x]));
  const loc = (a) => a - sc.start;
  const mine = new Map(anchors.anchors.filter((x) => x.scene === sid).map((x) => [x.id, x]));
  const T = {
    id: sid, dur: sc.dur, start: sc.start, sentences: sc.sentences,
    s: (n) => { const x = byN.get(n); if (!x) throw new Error(sid + ' no sentence ' + n); return loc(x.start); },
    e: (n) => { const x = byN.get(n); if (!x) throw new Error(sid + ' no sentence ' + n); return loc(x.end); },
    a(id) {
      const A = mine.get(id); if (!A) throw new Error(sid + ' no anchor ' + id);
      ANCH_USED.add(id);
      const x = byN.get(A.n); if (!x) throw new Error(sid + ' anchor ' + id + ' sentence ' + A.n);
      let t;
      if (A.at === 'start') t = x.start; else if (A.at === 'end') t = x.end;
      else { const i = x.text.toLowerCase().indexOf(A.at.toLowerCase()); t = i < 0 ? x.start : x.start + (x.end - x.start) * (i / x.text.length); if (i < 0) T.missing.push(id); }
      return Math.max(0, Math.min(sc.dur, loc(t) + (A.dt || 0)));
    },
    missing: [], anchorIds: [...mine.keys()],
  };
  return T;
}

// ---------- easing ----------
export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lin = (t, a, b) => clamp((t - a) / (b - a));
export const smooth = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
export const ease = (t, a, b) => smooth(lin(t, a, b));
export const easeOut = (t, a, b) => { const x = lin(t, a, b); return 1 - Math.pow(1 - x, 3); };
export const back = (t, a, b) => { const x = lin(t, a, b), s = 1.2; return 1 + (s + 1) * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2); };
export const mix = (a, b, x) => a + (b - a) * x;
export const inout = (t, a, b, c, d) => Math.min(ease(t, a, b), 1 - ease(t, c, d));
export function rng(seed) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }

// ---------- recording proxy (C5): screen objects and layer masks for window.CHECKS ----------
// REC.layer: 'all' (normal frame: every call passes through; objects are recorded), 'notext', 'text', 'glyph', 'graphics',
// 'only' (REC.ids). Mask layers start from a transparent canvas and drop the background, the 3D view and text shadows.
export const REC = { on: true, layer: 'all', ids: null, scene: '', objs: [], stack: [], meta: [], seen: new Map(), n: 0 };
const MASK = () => REC.layer !== 'all' && REC.layer !== 'notext';
export function hex(c) {
  if (typeof c !== 'string') return { hex: 'url(gradient)', a: 1 };
  if (c[0] === '#') { const h = c.length === 4 ? '#' + [...c.slice(1)].map((x) => x + x).join('') : c.slice(0, 7); return { hex: h.toLowerCase(), a: 1 }; }
  const m = c.match(/rgba?\(([^)]+)\)/);
  if (!m) return { hex: c, a: 1 };
  const p = m[1].split(',').map((x) => parseFloat(x));
  return { hex: '#' + p.slice(0, 3).map((v) => Math.round(v).toString(16).padStart(2, '0')).join(''), a: p.length > 3 ? p[3] : 1 };
}
function callKey() { // stable key of a drawing call: the call path (bundle line:col of the last few frames)
  const e = {}; const lim = Error.stackTraceLimit; Error.stackTraceLimit = 7; Error.captureStackTrace(e); Error.stackTraceLimit = lim;
  const st = e.stack.split('\n').slice(3).map((l) => (l.match(/:(\d+:\d+)\)?$/) || [])[1] || '').join('/');
  let h = 0; for (let i = 0; i < st.length; i++) h = (h * 31 + st.charCodeAt(i)) | 0;
  return (h >>> 0).toString(36);
}
// meta for the objects drawn inside fn (role, chart, value, char, ...): withObj({role:'bar', chart:'x', value: 3}, () => rect(...))
export function withObj(meta, fn) { REC.meta.push(meta); try { return fn(); } finally { REC.meta.pop(); } }
const metaTop = () => Object.assign({}, ...REC.meta);
export function beginObj(o) {
  const m = metaTop();
  const ob = o.kind === 'text' ? { ...o, _first: true, opacity: 0 } : { kind: 'shape', ...o, ...m, _first: true, opacity: 0 };
  if (!ob.key) ob.key = REC.scene + ':' + (ob.kind === 'text' ? 't:' + ob.text : ob.role + ':' + callKey());
  const k = (REC.seen.get(ob.key) || 0); REC.seen.set(ob.key, k + 1);
  if (k) ob.key += '#' + k;
  ob.id = ob.key; if (ob.kind === 'text') ob.tid = ob.key;
  REC.stack.push(ob); return ob;
}
export function endObj() { REC.stack.pop(); }
function curObj(tag) { // the object a paint op belongs to: the open one, or a new anonymous shape (raw ctx calls in scenes)
  if (REC.stack.length) return [REC.stack[REC.stack.length - 1], false];
  const ob = beginObj({ tag, role: 'mark' }); REC.stack.pop(); return [ob, true];
}
function show(ob, op) {
  switch (REC.layer) {
    case 'all': return true;
    case 'notext': return ob.kind !== 'text';
    case 'text': return ob.kind === 'text' && (op === 'glyph' || op === 'pill');
    case 'glyph': return ob.kind === 'text' && op === 'glyph';
    case 'graphics': return ob.kind === 'shape' && ob.role !== 'bg' && ob.role !== 'card';
    case 'only': return REC.ids && REC.ids.has(ob.id) && (ob.kind !== 'text' || op === 'glyph' || op === 'pill');
    default: return true;
  }
}
function tbox(ctx, pts) { // device-space bbox of points under the current transform
  const m = ctx.getTransform(); let l = 1e9, t = 1e9, r = -1e9, b = -1e9;
  for (const [x, y] of pts) { const X = m.a * x + m.c * y + m.e, Y = m.b * x + m.d * y + m.f; if (X < l) l = X; if (X > r) r = X; if (Y < t) t = Y; if (Y > b) b = Y; }
  return [l, t, r, b];
}
const uni = (a, b) => (a ? [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])] : b.slice());
// every paint op: attribute to an object, update it, and draw it or not (layer)
function paint(ctx, op, box, colour, draw) {
  if (!REC.on) return draw();
  const tag = op === 'glyph' ? 'text' : op;
  const [ob, anon] = curObj(tag);
  const kind = ob.kind === 'text' ? (op === 'glyph' ? 'glyph' : (ob._fillOp || 'plate')) : op;
  if (REC.layer === 'all') {
    const c = hex(colour), a = ctx.globalAlpha * c.a;
    if (ob._first) { ob._first = false; REC.objs.push(ob); }
    if (ob.kind === 'text') {
      if (kind === 'glyph') ob.opacity = Math.max(ob.opacity, a);
      else if (kind === 'plate') ob.background = c.hex;
    } else {
      ob.box = uni(ob.box, box); ob.opacity = Math.max(ob.opacity, a);
      if (op === 'stroke' || op === 'strokeRect') { if (!ob.stroke) ob.stroke = c.hex; }
      else if (op !== 'image' && !ob.fill) ob.fill = c.hex;
      if (op === 'image' && !ob.tag) ob.tag = 'image';
      if (!ob.tag) ob.tag = op === 'fillRect' || op === 'strokeRect' ? 'rect' : 'path';
      if (ob._verts) ob.vertices = Math.max(ob.vertices || 0, ob._verts);
    }
  }
  if (!show(ob, kind)) return;
  if (MASK() && ob.kind === 'text') { ctx.save(); ctx.shadowColor = 'rgba(0,0,0,0)'; draw(); ctx.restore(); return; }
  draw();
}
// the proxy handed to scenes as ctx: tracks the current path's device bbox and routes every paint op through paint()
export function recorder(raw) {
  let P = null, nv = 0;
  const add = (pts) => { const b = tbox(raw, pts); P = uni(P, b); nv += pts.length; };
  const cache = new Map();
  const wrap = {
    beginPath() { P = null; nv = 0; raw.beginPath(); },
    moveTo(x, y) { add([[x, y]]); raw.moveTo(x, y); },
    lineTo(x, y) { add([[x, y]]); raw.lineTo(x, y); },
    arc(x, y, r, a0, a1, cc) { add([[x - r, y - r], [x + r, y + r], [x - r, y + r], [x + r, y - r]]); nv -= 3; raw.arc(x, y, r, a0, a1, cc); },
    arcTo(x1, y1, x2, y2, r) { add([[x1, y1], [x2, y2]]); nv -= 1; raw.arcTo(x1, y1, x2, y2, r); },
    rect(x, y, w, h) { add([[x, y], [x + w, y + h], [x, y + h], [x + w, y]]); raw.rect(x, y, w, h); },
    bezierCurveTo(a, b, c, d, e, f) { add([[a, b], [c, d], [e, f]]); raw.bezierCurveTo(a, b, c, d, e, f); },
    quadraticCurveTo(a, b, c, d) { add([[a, b], [c, d]]); raw.quadraticCurveTo(a, b, c, d); },
    closePath() { raw.closePath(); },
    fill(...a) { const b = P; const [ob] = REC.stack.length ? [REC.stack[REC.stack.length - 1]] : [null]; if (ob && ob.kind !== 'text') ob._verts = nv;
      paint(raw, 'fill', b || [0, 0, 0, 0], raw.fillStyle, () => raw.fill(...a)); },
    stroke(...a) { const lw = raw.lineWidth / 2 * Math.hypot(raw.getTransform().a, raw.getTransform().b); const b = P ? [P[0] - lw, P[1] - lw, P[2] + lw, P[3] + lw] : [0, 0, 0, 0];
      const top = REC.stack.length ? REC.stack[REC.stack.length - 1] : null; if (top && top.kind !== 'text') top._verts = nv;
      paint(raw, 'stroke', b, raw.strokeStyle, () => raw.stroke(...a)); },
    fillRect(x, y, w, h) { paint(raw, 'fillRect', tbox(raw, [[x, y], [x + w, y + h], [x, y + h], [x + w, y]]), raw.fillStyle, () => raw.fillRect(x, y, w, h)); },
    strokeRect(x, y, w, h) { const lw = raw.lineWidth / 2; paint(raw, 'strokeRect', tbox(raw, [[x - lw, y - lw], [x + w + lw, y + h + lw]]), raw.strokeStyle, () => raw.strokeRect(x, y, w, h)); },
    fillText(s, x, y, mw) { const m = raw.measureText(s); const b = tbox(raw, [[x - m.actualBoundingBoxLeft, y - m.actualBoundingBoxAscent], [x + m.actualBoundingBoxRight, y + m.actualBoundingBoxDescent]]);
      paint(raw, 'glyph', b, raw.fillStyle, () => (mw === undefined ? raw.fillText(s, x, y) : raw.fillText(s, x, y, mw))); },
    drawImage(img, ...a) { const [x, y, w, h] = a.length >= 8 ? a.slice(4) : a.length === 4 ? a : [a[0], a[1], img.width, img.height];
      paint(raw, 'image', tbox(raw, [[x, y], [x + w, y + h]]), '#000000', () => raw.drawImage(img, ...a)); },
  };
  return new Proxy(raw, {
    get(t, k) {
      if (k in wrap) return wrap[k];
      const v = Reflect.get(t, k);
      if (typeof v === 'function') { let f = cache.get(k); if (!f) { f = v.bind(t); cache.set(k, f); } return f; }
      return v;
    },
    set(t, k, v) { return Reflect.set(t, k, v); },
  });
}
// a shape object around a primitive
export function obj(meta, fn) { beginObj({ kind: 'shape', ...meta }); try { return fn(); } finally { endObj(); } }

// ---------- text (flat, screen space, always sharp) ----------
export const TEXTLOG = new Map(); // string -> {tier, px, n, out, outV03}
export let CUR_T = 0;
export function setCurT(t) { CUR_T = t; }
const SAFE = { x0: 40, x1: W - 40, y0: 36, y1: H - 18 };           // C4 engine check (signed system: safe x 96, top 64, bottom 40)
const SAFE3 = { x0: 96, x1: 1824, y0: 54, y1: 1026 };            // the checker's V03 rectangle (90% action/title safe)
export function rgba(hex, a) { const n = parseInt(hex.slice(1), 16); return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`; }
export function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
}
export function measure(ctx, s, tier, weight) {
  const T = TIER[tier]; ctx.save(); ctx.font = `${weight || T.weight} ${T.px}px Inter`; const w = ctx.measureText(s).width; ctx.restore(); return w;
}
const LEVEL = { hero: 1, number: 2, head: 2, caption: 2, label: 3, note: 3 };
function claimSpans(ctx, s, x0, top, bot, alpha, color) {
  // queued ids first (this text's own CL calls), then the claims the scene took earlier (values computed ahead, e.g. rows built at build time)
  const own = new Set(PEND); PEND.length = 0;
  const ids = [...new Set([...own, ...(SCENE_CL.get(REC.scene) || [])])];
  const used = [], out = [];
  for (const id of ids) {
    const d = String(DATA.claims[id].display);
    let i = -1, from = 0;
    while ((i = s.indexOf(d, from)) >= 0) {
      const pre = s[i - 1] || ' ', post = s[i + d.length] || ' ';
      const okB = !/[\d.,$]/.test(pre) && !/\d/.test(post) && !(post === '.' && /\d/.test(s[i + d.length + 1] || ''));
      if (okB && !used.some(([a, b]) => i < b && i + d.length > a)) break;
      from = i + 1; i = -1;
    }
    const hits = [];
    if (i >= 0) hits.push([i, d]);
    else if (own.has(id)) for (const tok of d.match(/\d+(?:,\d{3})*(?:\.\d+)?/g) || []) { // a number taken from the display (e.g. the year of "October 2023")
      let j = -1, f2 = 0;
      while ((j = s.indexOf(tok, f2)) >= 0) { const pr = s[j - 1] || ' ', po = s[j + tok.length] || ' '; if (!/[\d.,$]/.test(pr) && !/\d/.test(po) && !used.some(([a, b]) => j < b && j + tok.length > a)) break; f2 = j + 1; j = -1; }
      if (j >= 0) hits.push([j, tok]);
    }
    for (const [k, txt] of hits) {
      used.push([k, k + txt.length]);
      const a = x0 + ctx.measureText(s.slice(0, k)).width, b = x0 + ctx.measureText(s.slice(0, k + txt.length)).width;
      out.push({ id, text: txt, box: [a, top, b, bot], opacity: alpha, color, series: null, roll: false });
    }
  }
  return out.sort((p, q) => q.text.length - p.text.length); // longest first (a checker removing span texts one by one keeps "2023" whole)
}
// tier: hero | number | head | caption | label | note. o: color, align, alpha, weight, plate (bg colour), shadow, role, char, series
export function text(ctx, s, x, y, tier, o = {}) {
  const T = TIER[tier]; if (!T) throw new Error('tier ' + tier);
  const alpha = o.alpha === undefined ? 1 : o.alpha;
  if (alpha <= 0.001 || !s) { PEND.length = 0; return 0; }
  if (o.sent && window.NOCAP) { PEND.length = 0; return measure(ctx, s, tier, o.weight); }
  const px = T.px, weight = o.weight || T.weight;
  ctx.save(); ctx.globalAlpha = alpha;
  ctx.font = `${weight} ${px}px Inter`; ctx.textAlign = o.align || 'left'; ctx.textBaseline = 'alphabetic';
  ctx.fontVariantNumeric = 'tabular-nums';
  const w = ctx.measureText(s).width;
  const x0 = o.align === 'center' ? x - w / 2 : o.align === 'right' ? x - w : x;
  const top = y - px * 0.76, bot = y + px * 0.22;
  const colour = hex(o.color || C.ink).hex;
  const bx = tbox(ctx, [[x0, top], [x0 + w, bot]]);
  const spans = claimSpans(ctx, s, x0, top, bot, alpha, colour).map((sp) => ({ ...sp, box: tbox(ctx, [[sp.box[0], sp.box[1]], [sp.box[2], sp.box[3]]]) }));
  const m = metaTop();
  const ob = beginObj({ kind: 'text', role: o.role || (o.pill ? 'badge' : tier === 'head' && y < 260 ? 'title' : 'label'), text: s, tier, fontPx: px, level: o.pill ? null : LEVEL[tier],
    emph: false, color: colour, runs: [{ color: colour, size: px }], background: null, box: bx, claims: spans, parent: null, anchor: null, chart: o.chart || m.chart || null,
    year: null, char: o.char || m.char || null, series: o.series || m.series || null, sent: !!o.sent });
  if (o.pill) { ob._fillOp = 'pill'; ctx.fillStyle = o.pill; roundRect(ctx, x0 - 16, top - 12, w + 32, px * 0.98 + 24, 8); ctx.fill(); ob.background = hex(o.pill).hex; ob._fillOp = 'plate'; }
  if (o.plate) { ctx.fillStyle = o.plate; roundRect(ctx, x0 - 18, top - 12, w + 36, bot - top + 24, 10); ctx.fill(); }
  else if (o.shadow) { ctx.shadowColor = 'rgba(0,0,0,0.9)'; ctx.shadowBlur = 14; ctx.shadowOffsetY = 3; }
  ctx.fillStyle = o.color || C.ink; ctx.fillText(s, x, y);
  endObj();
  ctx.restore();
  if (alpha >= 0.2 && REC.layer === 'all') {
    const out = x0 < SAFE.x0 || x0 + w > SAFE.x1 || top < SAFE.y0 || bot > SAFE.y1;
    const pb = o.pill ? 12 : 0, ph = o.pill ? 16 : 0; // the checker's text mask: glyphs + badge pill (text plates are not in it)
    const out3 = x0 - ph < SAFE3.x0 || x0 + w + ph > SAFE3.x1 || top - pb < SAFE3.y0 || bot + pb > SAFE3.y1;
    const e = TEXTLOG.get(s) || { tier, px, n: 0, out: 0, outV03: 0, firstT: CUR_T, sent: !!o.sent };
    e.n++; if (out) e.out++; if (out3) e.outV03++; TEXTLOG.set(s, e);
  }
  return w;
}
// C5 (rule S09 on screen): the money basis next to $ numbers, in the owner's words ("dollars of the day" = not adjusted
// for inflation). One helper so every scene uses the same wording, tier and colour.
export const BASIS = 'dollars of the day';
// BASIS_MODE (owner, C5): 'near' = a note next to each $ group (K3.1 rule S09: basis within 300 px of every $ number);
// 'corner' = ONE fixed frame-level label under the ILLUSTRATIVE badge while any $ number is visible (film.js; checks K3.3),
// the near notes and near-only wording then vanish. Set by window.BASIS_MODE or film.html?basis=corner; default near.
export const BASIS_MODE = (() => { try { return window.BASIS_MODE || new URLSearchParams(location.search).get('basis') || 'near'; } catch (e) { return 'near'; } })();
export const NEAR = BASIS_MODE !== 'corner';
export const nb = (near, plain = '') => (NEAR ? near : plain);
export function basisNote(ctx, x, y, o = {}) {
  if (!NEAR) return 0;
  return text(ctx, o.s || BASIS, x, y, 'note', { color: o.color || C.muted, align: o.align || 'left', alpha: o.alpha === undefined ? 1 : o.alpha, plate: o.plate || null, shadow: o.shadow });
}
export function badge(ctx, x, y, alpha = 1, align = 'right') { // ILLUSTRATIVE pill; (x,y) = text baseline anchor
  if (alpha <= 0.001) return 0;
  const s = 'ILLUSTRATIVE', px = TOK.type.badge.px;
  ctx.save(); ctx.font = `700 ${px}px Inter`; const w = ctx.measureText(s).width; ctx.restore();
  const x0 = align === 'right' ? x - w : x;
  text(ctx, s, x0, y, 'note', { weight: 700, color: C.bg, alpha, pill: C.warn, role: 'badge' });
  return w + 32;
}
// constant furniture: ILLUSTRATIVE badge (top right) and ONE source line (bottom left), both >= note tier
export function chrome(ctx, { illus = 0, source = '', srcAlpha = 1, plate = false } = {}) {
  // C5: badge pill and source line moved inside the checker's 90% safe rectangle (V03: 96..1824 x 54..1026)
  // source first: its claim ids (CL/CLT inside the argument) are still queued for its own text() call
  if (source) text(ctx, source, 96, H - 64, 'note', { color: C.muted, alpha: srcAlpha, plate: plate ? 'rgba(14,17,22,0.78)' : null });
  if (illus > 0) badge(ctx, W - 112, 110, illus);
}
export function strike(ctx, x0, y, x1, color, alpha, lw = 7) {
  if (alpha <= 0) return; obj({ role: 'line', tag: 'line' }, () => { ctx.save(); ctx.globalAlpha = alpha; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineCap = 'round';
    ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke(); ctx.restore(); });
}
// 2D primitives (H3)
export function line(ctx, pts, color, lw, o = {}) {
  obj({ role: 'line', tag: pts.length > 2 ? 'polyline' : 'line', fill: null, vertices: pts.length }, () => {
    ctx.save(); ctx.globalAlpha = o.alpha === undefined ? 1 : o.alpha; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineJoin = 'round'; ctx.lineCap = o.cap || 'round';
    if (o.dash) ctx.setLineDash(o.dash); ctx.beginPath(); pts.forEach((p, i) => (i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]))); ctx.stroke(); ctx.restore();
  });
}
export function rect(ctx, x, y, w, h, fill, a = 1) { if (a <= 0.001 || !h || !w) return; obj({ role: 'mark', tag: 'rect' }, () => { ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); ctx.restore(); }); }
export function srect(ctx, x, y, w, h, color, lw, a = 1, dash) { if (a <= 0.001) return; obj({ role: 'mark', tag: 'rect', fill: null }, () => { ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = color; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); ctx.restore(); }); }
export function hatch(ctx, x, y, w, h, color, a, step = 16, lw = 4) {
  if (a <= 0.001 || h <= 0 || w <= 0) return;
  obj({ role: 'mark', tag: 'hatch', fill: null }, () => {
    ctx.save(); ctx.globalAlpha = a; ctx.beginPath(); ctx.rect(x, y, w, h); ctx.clip(); ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.beginPath();
    for (let k = -h; k < w + h; k += step) { ctx.moveTo(x + k, y + h); ctx.lineTo(x + k + h, y); }
    ctx.stroke(); ctx.restore();
    const ob = REC.stack[REC.stack.length - 1]; if (ob && ob.box) ob.box = [Math.max(ob.box[0], x), Math.max(ob.box[1], y), Math.min(ob.box[2], x + w), Math.min(ob.box[3], y + h)];
  });
}
export function dot(ctx, cx, cy, r, color, a = 1) { if (a <= 0) return; obj({ role: 'mark', tag: 'circle', shape: 'circle' }, () => { ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = color; ctx.beginPath(); ctx.arc(cx, cy, r, 0, 7); ctx.fill(); ctx.restore(); }); }
export function tri(ctx, cx, cy, r, color, a = 1) { if (a <= 0) return; obj({ role: 'mark', tag: 'polygon', shape: 'triangle' }, () => { ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = color; ctx.beginPath(); ctx.moveTo(cx, cy - r); ctx.lineTo(cx + r * 0.95, cy + r * 0.7); ctx.lineTo(cx - r * 0.95, cy + r * 0.7); ctx.closePath(); ctx.fill(); ctx.restore(); }); }
export function sq(ctx, cx, cy, r, color, a = 1) { if (a <= 0.001) return; obj({ role: 'mark', tag: 'rect', shape: 'square' }, () => { ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = color; ctx.fillRect(cx - r * 0.8, cy - r * 0.8, r * 1.6, r * 1.6); ctx.restore(); }); }
export const MARK = { nora: [dot, C.positive], walt: [tri, C.warn], anjali: [sq, C.negative] };
export const CHAR = { nora: 'median', walt: 'small', anjali: 'large' }; // contract.json characters keys
export function mark(ctx, who, cx, cy, r, a = 1) { const [f, c] = MARK[who]; withObj({ char: CHAR[who], case: CHAR[who] }, () => f(ctx, cx, cy, r, c, a)); }

// ---------- canvas textures (text printed on objects) ----------
export function canvasTex(w, h, draw) {
  const cv = document.createElement('canvas'); cv.width = w; cv.height = h;
  const g = cv.getContext('2d'); draw(g, w, h);
  const tex = new THREE.CanvasTexture(cv); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
  tex.userData.redraw = (fn) => { g.clearRect(0, 0, w, h); fn(g, w, h); tex.needsUpdate = true; };
  return tex;
}
export function ptxt(g, s, x, y, { size = 40, weight = 600, color = C.ink, align = 'left' } = {}) {
  g.font = `${weight} ${size}px Inter`; g.fillStyle = color; g.textAlign = align; g.textBaseline = 'alphabetic'; g.fillText(s, x, y);
}
export const mat = (color, o = {}) => new THREE.MeshStandardMaterial({ color, roughness: 0.8, metalness: 0, ...o });
export function box(w, h, d, m, { cast = true, recv = true } = {}) { const b = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m); b.castShadow = cast; b.receiveShadow = recv; return b; }
export const pm = (map, o = {}) => new THREE.MeshStandardMaterial({ map, roughness: 0.92, ...o });
export function paperEdgeTex() {
  const t = canvasTex(256, 256, (g, w, h) => { g.fillStyle = C.paper; g.fillRect(0, 0, w, h); for (let y = 0; y < h; y += 6) { g.fillStyle = C.paperLine; g.fillRect(0, y, w, 2); } });
  t.wrapS = t.wrapT = THREE.RepeatWrapping; return t;
}
// "owed" slab material: paper with negative diagonal stripes (pattern = not Anjali's solid square)
export function owedTex() {
  const t = canvasTex(256, 256, (g, w, h) => { g.fillStyle = '#F3E3E1'; g.fillRect(0, 0, w, h); g.strokeStyle = C.negative; g.lineWidth = 26; g.beginPath(); for (let k = -h; k < w + h; k += 64) { g.moveTo(k, h); g.lineTo(k + h, 0); } g.stroke(); });
  t.wrapS = t.wrapT = THREE.RepeatWrapping; return t;
}
export function woodTable(scene, w = 16, d = 8) {
  const woodTex = canvasTex(1024, 1024, (g, ww, hh) => {
    g.fillStyle = C.wood; g.fillRect(0, 0, ww, hh);
    for (let i = 0; i < 8; i++) { g.fillStyle = i % 2 ? '#62442F' : '#5A3E2A'; g.fillRect(0, i * 128, ww, 126); g.fillStyle = '#3B281C'; g.fillRect(0, i * 128 + 126, ww, 2); }
    g.globalAlpha = 0.12; g.strokeStyle = '#2A1C12';
    for (let i = 0; i < 160; i++) { const y = (i * 37) % hh; g.beginPath(); g.moveTo(0, y); g.bezierCurveTo(ww * 0.3, y + 6, ww * 0.6, y - 6, ww, y + 3); g.stroke(); }
  });
  woodTex.wrapS = woodTex.wrapT = THREE.RepeatWrapping; woodTex.repeat.set(2, 2);
  const table = new THREE.Mesh(new THREE.BoxGeometry(w, 0.2, d), new THREE.MeshStandardMaterial({ map: woodTex, roughness: 0.65 }));
  table.position.set(0, -0.1, 0); table.receiveShadow = true; scene.add(table);
  const wall = new THREE.Mesh(new THREE.PlaneGeometry(40, 16), mat(C.wall, { roughness: 1 })); wall.position.set(0, 5, -d / 2 - 0.3); wall.receiveShadow = true; scene.add(wall);
  return table;
}
// A house: box body + gable roof + windows + door. Origin at ground centre.
export function house({ w = 3, d = 2.4, h = 1.8, roof = 1.2, wall = C.houseWall, roofCol = C.roof, lit = 0, trim = '#EDE6D6' } = {}) {
  const g = new THREE.Group();
  const body = box(w, h, d, mat(wall, { roughness: 0.9 })); body.position.y = h / 2; g.add(body);
  const sh = new THREE.Shape(); sh.moveTo(-w / 2 - 0.08 * w / 3, 0); sh.lineTo(w / 2 + 0.08 * w / 3, 0); sh.lineTo(0, roof); sh.closePath();
  const r = new THREE.Mesh(new THREE.ExtrudeGeometry(sh, { depth: d * 1.08, bevelEnabled: false }), mat(roofCol, { roughness: 0.7 }));
  r.position.set(0, h, -d * 0.54); r.castShadow = r.receiveShadow = true; g.add(r);
  const winMat = new THREE.MeshStandardMaterial({ color: '#2B2F38', emissive: new THREE.Color('#FFC477'), emissiveIntensity: lit, roughness: 0.3 });
  const ww = w * 0.16, wh = h * 0.3;
  for (const x of [-w * 0.28, w * 0.28]) {
    const fr = box(ww * 1.12, wh * 1.12, 0.02 * w, mat(trim)); fr.position.set(x, h * 0.55, d / 2 + 0.005); g.add(fr);
    const wi = new THREE.Mesh(new THREE.PlaneGeometry(ww, wh), winMat); wi.position.set(x, h * 0.55, d / 2 + 0.02 * w); g.add(wi);
  }
  const door = box(w * 0.14, h * 0.5, 0.02 * w, mat('#5A3A2A')); door.position.set(0, h * 0.25, d / 2 + 0.01); g.add(door);
  g.userData = { winMat, w, d, h, roof };
  return g;
}
// wire-outline house (the viewer's own loan: no number)
export function outlineHouse({ w = 3, d = 2.4, h = 1.8, roof = 1.2, color = C.ink } = {}) {
  const g = new THREE.Group();
  const m = new THREE.LineBasicMaterial({ color, transparent: true });
  const b = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(w, h, d)), m); b.position.y = h / 2; g.add(b);
  const sh = new THREE.Shape(); sh.moveTo(-w / 2, 0); sh.lineTo(w / 2, 0); sh.lineTo(0, roof); sh.closePath();
  const r = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.ExtrudeGeometry(sh, { depth: d, bevelEnabled: false })), m); r.position.set(0, h, -d / 2); g.add(r);
  g.userData.mat = m; return g;
}


// ---------- scenes: 3D (optional, one shared WebGL renderer) + 2D overlay (C5: film.js drives them) ----------
let GL = null;
export function sharedRenderer() {
  if (GL) return GL;
  const gl = document.createElement('canvas'); gl.width = OW; gl.height = OH;
  const renderer = new THREE.WebGLRenderer({ canvas: gl, antialias: true, preserveDrawingBuffer: true, powerPreference: 'low-power' });
  renderer.setPixelRatio(1); renderer.setSize(OW, OH, false);
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  GL = renderer; return GL;
}
// build one scene (module + its timing); ctx = the recording proxy of the film canvas
export function makeScene(mod, T, ctx) {
  let renderer = null, scene = null, camera = null, target = new THREE.Vector3();
  if (mod.uses3d) {
    renderer = sharedRenderer(); renderer.toneMappingExposure = 1.0;
    scene = new THREE.Scene(); camera = new THREE.PerspectiveCamera(35, W / H, 0.1, 200);
    const la = camera.lookAt.bind(camera);
    camera.lookAt = (x, y, z) => { if (x && x.isVector3) target.copy(x); else target.set(x, y, z); la(x, y, z); };
  }
  PEND.length = 0; REC.scene = T.id;
  const S = mod.build({ THREE, scene, camera, renderer, ctx, T });
  PEND.length = 0;
  const exposure = renderer ? renderer.toneMappingExposure : 1;
  const N = Math.round((T.start + T.dur) * TOK.canvas.fps) - Math.round(T.start * TOK.canvas.fps);
  const modeAt = (t) => (S.mode ? S.mode(t) : (mod.uses3d ? '3d' : '2d'));
  const pose = () => ({ pos: camera.position.toArray(), quat: camera.quaternion.toArray(), fov: camera.fov, target: target.toArray() });
  const setPose = (p) => { camera.position.fromArray(p.pos); camera.quaternion.fromArray(p.quat); camera.fov = p.fov; camera.updateProjectionMatrix(); target.fromArray(p.target); };
  return {
    id: T.id, T, S, N, scene, camera, renderer, exposure, modeAt, pose, setPose,
    proj: (v) => { const p = v.clone().project(camera); return { x: (p.x + 1) / 2 * W, y: (1 - p.y) / 2 * H }; },
    dispose() {
      if (!scene) return;
      scene.traverse((o) => {
        if (o.geometry) o.geometry.dispose();
        const ms = Array.isArray(o.material) ? o.material : o.material ? [o.material] : [];
        for (const m of ms) { for (const k of Object.keys(m)) if (m[k] && m[k].isTexture) m[k].dispose(); m.dispose(); }
        if (o.isLight && o.shadow && o.shadow.map) o.shadow.map.dispose();
      });
    },
  };
}
