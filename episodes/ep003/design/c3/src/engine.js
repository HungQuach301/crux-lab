// Tập 3 C3: engine chép từ toolkit/visual-library/code/h3/engine.js (thư viện hình v1); chỉ đổi đường dẫn tokens.
// ../../tokens.json incl. E2 aliases (costlier #C72323, cushion #269783). Original note: H3 engine (Tập 2, C3). 2D canvas only. Code adapted from episodes/ep001/design/c3/final/src/engine.js (same token
// file, same 6 type tiers, same CL()); scenes are new. Design space is 1920x1080 (token sizes are px at 1080p); the
// output canvas is 1280x720 (scale 2/3). Flags: MASK (every text box becomes a flat `surface` block), NOTEXT
// (graphics only, used by the clearance/contrast self-check).
export const TOK = await (await fetch('/episodes/ep003/design/c3/tokens.json')).json();
export const DATA = window.DATA;
const RES1080 = new URLSearchParams(location.search).get('res') === '1080'; // C5: bản cuối 1080p + window.CHECKS (§6.1: chỉ độ phân giải)
export const W = 1920, H = 1080, OW = RES1080 ? 1920 : 1280, OH = RES1080 ? 1080 : 720, SC = OW / W;
const col = TOK.color;
export const C = { bg: col.bg, surface: col.surface, grid: col.grid, ink: col.ink, muted: col['ink-muted'], accent: col.accent,
  warn: col.warn, cushion: TOK.episodeAliases.cushion.hex, costlier: TOK.episodeAliases.costlier.hex };
export const TIER = TOK.type.tiers;
export const FLAGS = { MASK: false, NOTEXT: false, LAYER: 'all', ONLY: null };
// C5 (hợp đồng trang, checks/CONTRACT.md §Page): CL() đánh dấu đoạn claim trong chuỗi bằng ký tự riêng (U+E000 id U+E001 chữ U+E002);
// text() bỏ dấu trước khi đo/vẽ (hình không đổi) và ghi đoạn claim của từng chữ cho window.CHECKS.objects().
const MK0 = '\uE000', MK1 = '\uE001', MK2 = '\uE002', MKRE = /\uE000([^\uE001]*)\uE001([^\uE002]*)\uE002/g;
export const mark = (id, s) => MK0 + id + MK1 + s + MK2;
export const plain = (s) => String(s).replace(MKRE, '$2');
function spans(s) { const out = []; let txt = '', last = 0; s = String(s); for (const m of s.matchAll(MKRE)) { txt += s.slice(last, m.index); out.push({ id: m[1], a: txt.length, text: m[2] }); txt += m[2]; last = m.index + m[0].length; } return { txt: txt + s.slice(last), spans: out }; }
export let SHAPES = [];           // per frame: shapes drawn (design px), paint order shared with BOXES via SEQ
let SEQ = 0;
export function shape(o) { if ((o.opacity ?? 1) <= 0.001) return; SHAPES.push({ seq: SEQ++, ...o }); }

export const USED = new Set();
export function CL(id) { const c = DATA.claims[id]; if (!c) throw new Error('unknown claim ' + id); USED.add(id); return mark(id, c.display); }

export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lin = (t, a, b) => clamp((t - a) / (b - a));
export const smooth = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
export const ease = (t, a, b) => smooth(lin(t, a, b));
export const easeIn = (t, a, b) => { const x = lin(t, a, b); return x * x; };
export const easeOut = (t, a, b) => { const x = lin(t, a, b); return 1 - Math.pow(1 - x, 3); };
export const back = (t, a, b) => { const x = lin(t, a, b), s = 1.4; return 1 + (s + 1) * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2); };
export const mix = (a, b, x) => a + (b - a) * x;
export const inout = (t, a, b, c, d) => Math.min(ease(t, a, b), 1 - ease(t, c, d));
export function rgba(hex, a) { const n = parseInt(hex.slice(1), 16); return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`; }
export function roundRect(ctx, x, y, w, h, r) {
  r = Math.max(0, Math.min(r, w / 2, h / 2));
  ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
}

// ---------- text: only the 6 token tiers (smallest 48 px at 1080p = 32 px at 720p) ----------
export let BOXES = [];            // per frame: every drawn text element (design px)
export const TEXTLOG = new Map(); // string -> {tier, px, n}
let TEXTCTX = null; // layer 'text' / 'glyph' / 'only': graphics go to a scratch canvas, text to the visible one
export function resetFrame() { BOXES = []; SHAPES = []; SEQ = 0; }
export function measureText(ctx, s, tier, weight) { const T = TIER[tier]; ctx.save(); ctx.font = `${weight || T.weight} ${T.px}px Inter`; const w = ctx.measureText(plain(s)).width; ctx.restore(); return w; }
// o: color, align, alpha, weight, plate (colour; padded rounded block behind the text)
export function text(ctx, s, x, y, tier, o = {}) {
  const T = TIER[tier]; if (!T) throw new Error('tier ' + tier);
  const alpha = o.alpha === undefined ? 1 : o.alpha;
  if (alpha <= 0.001 || !s) return { w: 0 };
  const sp = spans(s); s = sp.txt;
  const tctx = TEXTCTX || ctx; ctx = tctx;
  const px = T.px, weight = o.weight || T.weight;
  ctx.save(); ctx.font = `${weight} ${px}px Inter`; ctx.fontVariantNumeric = 'tabular-nums';
  const w = ctx.measureText(s).width; ctx.restore();
  const x0 = o.align === 'center' ? x - w / 2 : o.align === 'right' ? x - w : x;
  const top = y - px * 0.76, bot = y + px * 0.22;
  const pad = o.plate ? [16, 10] : [0, 0];
  const box = { s, group: o.group || null, tier, px, color: o.color || C.ink, alpha, plate: o.plate || null, weight, role: o.role || null, seq: SEQ++,
    x0: x0 - pad[0], y0: top - pad[1], x1: x0 + w + pad[0], y1: bot + pad[1], gx0: x0, gy0: top, gx1: x0 + w, gy1: bot, claims: [] };
  if (sp.spans.length) { ctx.save(); ctx.font = `${weight} ${px}px Inter`; ctx.fontVariantNumeric = 'tabular-nums';
    for (const c of sp.spans) { const a = x0 + ctx.measureText(s.slice(0, c.a)).width, b = a + ctx.measureText(c.text).width; box.claims.push({ id: c.id, text: c.text, box: [a, top, b, bot] }); }
    ctx.restore(); }
  BOXES.push(box);
  box.idx = BOXES.length - 1;
  if (FLAGS.LAYER === 'only' && !(FLAGS.ONLY && FLAGS.ONLY.has('t' + box.idx))) return box;
  if (alpha >= 0.2) { const e = TEXTLOG.get(s) || { tier, px, n: 0 }; e.n++; TEXTLOG.set(s, e); }
  if (FLAGS.NOTEXT) return box;
  ctx.save(); ctx.globalAlpha = alpha;
  if (o.plate && FLAGS.LAYER !== 'glyph') { ctx.fillStyle = o.plate; roundRect(ctx, box.x0, box.y0, box.x1 - box.x0, box.y1 - box.y0, 10); ctx.fill(); }
  if (FLAGS.MASK) { ctx.fillStyle = C.surface; ctx.fillRect(x0, top, w, bot - top); }
  else {
    ctx.font = `${weight} ${px}px Inter`; ctx.textAlign = o.align || 'left'; ctx.textBaseline = 'alphabetic'; ctx.fontVariantNumeric = 'tabular-nums';
    ctx.fillStyle = box.color; ctx.fillText(s, x, y);
  }
  ctx.restore();
  return box;
}
// C5 V03: default x moved 16 px left so the plate (text + 16) ends at the safe edge 1824 (was 1840)
// ILLUSTRATIVE badge: warn pill, bg text, token type.badge (48 px at 1080p = 32 px at 720p). (x,y) = right edge, baseline
export function badge(ctx, x = W - 96 - 16, y = 118, alpha = 1) {
  if (alpha <= 0.001) return;
  const w = measureText(ctx, 'ILLUSTRATIVE', 'note', 700);
  text(ctx, 'ILLUSTRATIVE', x - w, y, 'note', { weight: 700, color: C.bg, alpha, plate: C.warn, role: 'badge' });
}

// ---------- 2D primitives ----------
export function line(ctx, pts, color, lw, o = {}) {
  if (pts.length < 2) return;
  { const xs = pts.map((p) => p[0]), ys = pts.map((p) => p[1]), h = lw / 2;
    shape({ tag: pts.length > 2 ? 'polyline' : 'line', role: o.role || 'line', stroke: color, fill: null, opacity: o.alpha === undefined ? 1 : o.alpha, vertices: pts.length,
      box: [Math.min(...xs) - h, Math.min(...ys) - h, Math.max(...xs) + h, Math.max(...ys) + h], ...(o.meta || {}) }); }
  ctx.save(); ctx.globalAlpha = o.alpha === undefined ? 1 : o.alpha; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineJoin = 'round'; ctx.lineCap = o.cap || 'round';
  if (o.dash) ctx.setLineDash(o.dash); ctx.beginPath(); pts.forEach((p, i) => (i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]))); ctx.stroke(); ctx.restore();
}
export function rect(ctx, x, y, w, h, fill, a = 1, meta) { if (a <= 0.001 || !h || !w) return; shape({ tag: 'rect', role: 'mark', fill, stroke: null, opacity: a, box: [Math.min(x, x + w), Math.min(y, y + h), Math.max(x, x + w), Math.max(y, y + h)], ...(meta || {}) }); ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); ctx.restore(); }
export function srect(ctx, x, y, w, h, color, lw, a = 1, dash) { if (a <= 0.001) return; shape({ tag: 'rect', role: 'line', fill: null, stroke: color, opacity: a, box: [x - lw / 2, y - lw / 2, x + w + lw / 2, y + h + lw / 2] }); ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = color; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); ctx.restore(); }
export function diamond(ctx, cx, cy, r, color, a = 1, stroke = null) {
  if (a <= 0) return; shape({ tag: 'path', role: 'mark', shape: 'diamond', fill: stroke ? null : color, stroke: stroke ? color : null, opacity: a, box: [cx - r, cy - r, cx + r, cy + r] });
  ctx.save(); ctx.globalAlpha = a; ctx.beginPath(); ctx.moveTo(cx, cy - r); ctx.lineTo(cx + r * 0.78, cy); ctx.lineTo(cx, cy + r); ctx.lineTo(cx - r * 0.78, cy); ctx.closePath();
  if (stroke) { ctx.strokeStyle = color; ctx.lineWidth = stroke; ctx.stroke(); } else { ctx.fillStyle = color; ctx.fill(); ctx.strokeStyle = C.bg; ctx.lineWidth = 3; ctx.stroke(); }
  ctx.restore();
}
// head-start bracket between y1 (rail) and y2 (bead) at x; fill positive when the bead is under the rail, warn when over
export function bracket(ctx, x, yRail, yBead, a = 1, arm = 22) {
  if (a <= 0) return;
  const top = Math.min(yRail, yBead), bot = Math.max(yRail, yBead), h = bot - top;
  const fill = yBead >= yRail ? C.cushion : C.warn;
  if (h > 1) rect(ctx, x - arm - 6, top, arm, h, fill, 0.55 * a);
  ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = C.ink; ctx.lineWidth = 5; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  ctx.beginPath(); ctx.moveTo(x - 6, top); ctx.lineTo(x - arm - 12, top); ctx.lineTo(x - arm - 12, bot); ctx.lineTo(x - 6, bot); ctx.stroke(); ctx.restore();
}
// coin pile: flat discs (side view) from base y upward; returns top y
export function coins(ctx, cx, baseY, hPx, color, a = 1, w = 128, disc = 16) {
  if (a <= 0 || hPx <= 0) return baseY;
  shape({ tag: 'rect', role: 'mark', shape: 'coins', fill: color, stroke: null, opacity: a, box: [cx - w / 2 - 3, baseY - hPx, cx + w / 2 + 3, baseY] });
  const n = Math.floor(hPx / disc), rem = hPx - n * disc;
  ctx.save(); ctx.globalAlpha = a;
  for (let i = 0; i < n + (rem > 1 ? 1 : 0); i++) {
    const hh = i < n ? disc : rem, y = baseY - i * disc - hh, dx = ((i * 37) % 7) - 3;
    ctx.fillStyle = color; roundRect(ctx, cx - w / 2 + dx, y + 1, w, hh - 2, Math.min(6, (hh - 2) / 2)); ctx.fill();
  }
  ctx.restore(); return baseY - hPx;
}

const hexrgb0 = (h) => { const n = parseInt(h.slice(1), 16); return [n >> 16, (n >> 8) & 255, n & 255]; };
const r1 = (v) => Math.round(v * 100) / 100;
// window.CHECKS objects of the last drawn frame (design px = screen px at 1080p), in paint order
function objectsOf() {
  const lc = (c) => (c ? String(c).toLowerCase() : null);
  const seen = new Map();
  const T = BOXES.map((b, i) => {
    const k = (b.group ? b.group + ':' : '') + b.s; const n = seen.get(k) || 0; seen.set(k, n + 1);
    const plated = !!b.plate, box = plated ? [b.x0, b.y0, b.x1, b.y1] : [b.gx0, b.gy0, b.gx1, b.gy1];
    // a reversed-out pill (text in bg colour on an ink/warn plate) is a badge for the contract (its contrast is read inside the pill)
    const role = b.role || (b.plate && b.plate !== C.surface && b.plate !== C.bg ? 'badge' : b.tier === 'head' ? 'title' : 'label');
    return { seq: b.seq, o: { id: 't' + i, kind: 'text', tid: k + '#' + n, role, text: b.s, box: box.map(r1), opacity: r1(b.alpha), level: b.tier === 'hero' ? 1 : null, emph: b.tier === 'hero',
      color: lc(b.color), fontPx: b.px, runs: [{ color: lc(b.color), size: b.px }], background: lc(b.plate), parent: null, key: k + '#' + n,
      claims: b.claims.map((c) => ({ id: c.id, text: c.text, box: c.box.map(r1), opacity: r1(b.alpha), color: lc(b.color) })), sig: k + '|' + box.map(Math.round).join(',') } };
  });
  const Sh = SHAPES.map((o, i) => ({ seq: o.seq, o: { id: 's' + i, kind: 'shape', tag: o.tag, role: o.role, panel: o.panel || null, chart: o.chart || null, char: o.char || null, shape: o.shape || null, ...(o.case != null ? { case: o.case } : {}), ...(o.year != null ? { year: o.year } : {}),
    fill: lc(o.fill), stroke: lc(o.stroke), opacity: r1(o.opacity ?? 1), box: o.box.map(r1), vertices: o.vertices || null, key: (o.char || o.role) + ':' + o.tag + ':' + i, sig: o.tag + '|' + o.box.map(Math.round).join(',') } }));
  return [...Sh, ...T].sort((a, b) => a.seq - b.seq).map((x) => x.o);
}

// ---------- boot ----------
export function boot(S) {
  const out = document.createElement('canvas'); out.width = OW; out.height = OH; document.body.appendChild(out);
  const ctx = out.getContext('2d', { willReadFrequently: true });
  const scratch = document.createElement('canvas'); scratch.width = OW; scratch.height = OH; const sctx = scratch.getContext('2d');
  const SURF = hexrgb0(C.surface);
  function draw(t) {
    resetFrame();
    const L = FLAGS.LAYER, textOnly = L === 'text' || L === 'glyph' || L === 'only';
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    if (L === 'all' || L === 'notext') { ctx.fillStyle = C.bg; ctx.fillRect(0, 0, OW, OH); } else ctx.clearRect(0, 0, OW, OH);
    FLAGS.NOTEXT = L === 'graphics' || L === 'notext';
    ctx.setTransform(SC, 0, 0, SC, 0, 0);
    if (textOnly) { sctx.setTransform(1, 0, 0, 1, 0, 0); sctx.clearRect(0, 0, OW, OH); sctx.setTransform(SC, 0, 0, SC, 0, 0); TEXTCTX = ctx; S.draw(sctx, t); TEXTCTX = null; }
    else S.draw(ctx, t);
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    FLAGS.NOTEXT = false;
    if (L === 'graphics') { // contract: no bg, no card fill (the neutral surface panels and plates)
      const im = ctx.getImageData(0, 0, OW, OH), d = im.data;
      for (let i = 0; i < d.length; i += 4) if (d[i + 3] && Math.abs(d[i] - SURF[0]) <= 3 && Math.abs(d[i + 1] - SURF[1]) <= 3 && Math.abs(d[i + 2] - SURF[2]) <= 3) d[i + 3] = 0;
      ctx.putImageData(im, 0, 0);
    }
  }
  const b64 = (u8) => { let s = ''; const n = 0x8000; for (let i = 0; i < u8.length; i += n) s += String.fromCharCode.apply(null, u8.subarray(i, i + n)); return btoa(s); };
  const lum = (r, g, b) => { const f = (c) => { c /= 255; return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const hexrgb = (h) => { const n = parseInt(h.slice(1), 16); return [n >> 16, (n >> 8) & 255, n & 255]; };
  const BG = hexrgb(C.bg);
  // self-check of one frame: clearance (design px) from each text element to graphics and to other text; local contrast
  function check(t) {
    FLAGS.NOTEXT = false; draw(t); const boxes = BOXES.filter((b) => b.alpha >= 0.99);
    FLAGS.NOTEXT = true; draw(t); FLAGS.NOTEXT = false;
    const img = ctx.getImageData(0, 0, OW, OH).data;
    const res = [];
    for (const b of boxes) {
      const R = 16; // search radius, design px
      const px0 = Math.max(0, Math.floor((b.x0 - R) * SC)), px1 = Math.min(OW - 1, Math.ceil((b.x1 + R) * SC));
      const py0 = Math.max(0, Math.floor((b.y0 - R) * SC)), py1 = Math.min(OH - 1, Math.ceil((b.y1 + R) * SC));
      let clear = R, under = [];
      for (let y = py0; y <= py1; y++) for (let x = px0; x <= px1; x++) {
        const i = (y * OW + x) * 4, r = img[i], g = img[i + 1], bl = img[i + 2];
        const X = (x + 0.5) / SC, Y = (y + 0.5) / SC;
        const inside = X >= b.x0 && X <= b.x1 && Y >= b.y0 && Y <= b.y1;
        if (inside && X >= b.gx0 && X <= b.gx1 && Y >= b.gy0 && Y <= b.gy1) under.push(lum(r, g, bl));
        const nonbg = Math.max(Math.abs(r - BG[0]), Math.abs(g - BG[1]), Math.abs(bl - BG[2])) > 10;
        if (!nonbg) continue;
        const dx = Math.max(b.x0 - X, 0, X - b.x1), dy = Math.max(b.y0 - Y, 0, Y - b.y1);
        const d = inside ? 0 : Math.hypot(dx, dy) - 0.75 / SC; // half-pixel tolerance
        if (d < clear) clear = Math.max(0, d);
      }
      under.sort((a, c) => a - c);
      const Lbg = b.plate ? lum(...hexrgb(b.plate)) : (under.length ? under[Math.floor(under.length / 2)] : lum(...BG));
      const Lt = lum(...hexrgb(b.color));
      const contrast = (Math.max(Lt, Lbg) + 0.05) / (Math.min(Lt, Lbg) + 0.05);
      let tclear = 999;
      for (const o of boxes) if (o !== b && !(b.group && o.group === b.group)) { const dx = Math.max(o.x0 - b.x1, b.x0 - o.x1, 0), dy = Math.max(o.y0 - b.y1, b.y0 - o.y1, 0); tclear = Math.min(tclear, Math.hypot(dx, dy)); }
      res.push({ s: b.s, px: b.px, clear: +clear.toFixed(1), tclear: +tclear.toFixed(1), contrast: +contrast.toFixed(2), color: b.color, plate: b.plate });
    }
    return res;
  }
  let CUR = 0;
  window.CHECKS = {
    seek(t) { CUR = t; FLAGS.LAYER = 'all'; FLAGS.ONLY = null; document.documentElement.style.background = document.body.style.background = ''; draw(t); return true; },
    freeze() { return true; }, // no camera: the 2D page has no camera state to hold
    objects() { return objectsOf(); },
    layer(name, ids) {
      FLAGS.LAYER = name || 'all'; FLAGS.ONLY = name === 'only' ? new Set(ids || []) : null;
      const transparent = !['all', 'notext'].includes(FLAGS.LAYER);
      document.documentElement.style.background = document.body.style.background = transparent ? 'transparent' : '';
      draw(CUR); return true;
    },
  };
  return {
    duration: S.duration, frames: Math.round(S.duration * 30), stripTimes: S.stripTimes,
    frame(t) { draw(t); return b64(new Uint8Array(ctx.getImageData(0, 0, OW, OH).data.buffer)); },
    png(t) { draw(t); return out.toDataURL('image/png'); },
    boxes(t) { draw(t); return BOXES.map((b) => ({ s: b.s, px: b.px, box: [b.x0, b.y0, b.x1 - b.x0, b.y1 - b.y0], glyph: [b.gx0, b.gy0, b.gx1 - b.gx0, b.gy1 - b.gy0] })); },
    check,
    setMask(m) { FLAGS.MASK = !!m; },
    log: () => ({ used: [...USED].sort(), texts: [...TEXTLOG.entries()].map(([s, e]) => ({ s, ...e })) }),
    strip(times, masked) { // 3x2 grid of 640x360 frames, numbered 1-6 above each frame, no captions
      FLAGS.MASK = !!masked;
      const G = 16, TW = 640, TH = 360, LH = 64;
      const sc = document.createElement('canvas'); sc.width = 3 * TW + 4 * G; sc.height = 2 * (TH + LH) + 3 * G; const g = sc.getContext('2d');
      g.fillStyle = '#05070A'; g.fillRect(0, 0, sc.width, sc.height);
      times.forEach((t, i) => {
        const cx = G + (i % 3) * (TW + G), cy = G + Math.floor(i / 3) * (TH + LH + G);
        draw(t); g.drawImage(out, cx, cy + LH, TW, TH);
        g.fillStyle = C.warn; g.fillRect(cx, cy + 6, 52, 52);
        g.font = '700 40px Inter'; g.fillStyle = C.bg; g.textAlign = 'center'; g.fillText(String(i + 1), cx + 26, cy + 47);
      });
      FLAGS.MASK = false;
      return sc.toDataURL('image/png');
    },
  };
}
