// Crux factory engine (Mốc B). Canvas 2D, a design space that is 1920x1080 (landscape) or 1080x1920 (Shorts), drawn at 1080p or 720p.
// Viết mới cho nhà máy; ý tưởng lấy từ engine Tập 2–3 (bậc chữ token, CL(), easing), không chép nguyên.
// The engine owns the channel standards so a template cannot break them (each fix is logged for qc.py):
//   floor     every text is drawn at an effective size ≥ the floor (40 px landscape, 56 px Shorts, design px after camera zoom); smaller → raised
//   contrast  text colour vs what is behind it (plate or background) ≥ 4.5:1; lower → ink, then a surface plate
//   safe      every text box is moved inside the safe area
//   overlap   a text box that hits an earlier box of another group is nudged (down, then up); still hitting → logged as a collision
//   tags      ILLUSTRATIVE badge on every frame that shows an illustrative claim or element; "US only · history, not a forecast" on every
//             frame that shows a historical number (claims.json flags)
//   breath    the whole frame pushes in slowly over each shot (1.000 → 1.015) so no frame is frozen while the narration runs
export const TIERS = { hero: 150, number: 96, head: 72, caption: 64, label: 54, note: 48, badge: 48 };
export const W8 = { hero: 700, number: 700, head: 700, caption: 600, label: 600, note: 400, badge: 700 };
export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lin = (t, a, b) => (b <= a ? (t >= a ? 1 : 0) : clamp((t - a) / (b - a)));
export const ease = (t, a, b) => { const x = lin(t, a, b); return x * x * (3 - 2 * x); };
export const easeOut = (t, a, b) => 1 - Math.pow(1 - lin(t, a, b), 3);
export const mix = (a, b, x) => a + (b - a) * x;

function lum(hex) {
  const n = parseInt(hex.slice(1, 7), 16), c = [n >> 16, (n >> 8) & 255, n & 255].map((v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
  return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
}
export const contrast = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
export function rgba(hex, a) { const n = parseInt(hex.slice(1, 7), 16); return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`; }
const hit = (a, b) => a.x0 < b.x1 && b.x0 < a.x1 && a.y0 < b.y1 && b.y0 < a.y1;

export function makeEngine(canvas, cfg) {
  // cfg: {orient:'h'|'v', res:1080|720, tokens, claims:{id:{display,historical,illustrative}}, data, floor:{h,v}}
  const V = cfg.orient === 'v';
  const W = V ? 1080 : 1920, H = V ? 1920 : 1080;
  const SC = cfg.res === 720 ? 2 / 3 : 1;
  canvas.width = Math.round(W * SC); canvas.height = Math.round(H * SC);
  const ctx = canvas.getContext('2d', { willReadFrequently: false });
  const col = cfg.tokens.color;
  const C = { bg: col.bg, surface: col.surface, grid: col.grid, ink: col.ink, muted: col['ink-muted'], accent: col.accent, warn: col.warn,
    ...(cfg.tokens.roles || {}) };
  const SAFE = V ? { x0: 72, y0: 200, x1: W - 72, y1: H - 320 } : { x0: 96, y0: 64, x1: W - 96, y1: H - 56 }; // Shorts: YouTube UI covers top/bottom
  const FLOOR = V ? (cfg.floor?.v ?? 56) : (cfg.floor?.h ?? 40);
  let boxes = [], frameFlags = null, zoom = 1, log = null;
  const E = { ctx, C, W, H, SAFE, V, FLOOR, claims: cfg.claims, data: cfg.data };

  E.CL = (id) => {
    const c = cfg.claims[id]; if (!c) throw new Error('unknown claim ' + id);
    frameFlags.claims.add(id); if (c.historical) frameFlags.hist = true; if (c.illustrative) frameFlags.illus = true;
    return c.display;
  };
  E.illustrative = () => { frameFlags.illus = true; };
  E.historical = () => { frameFlags.hist = true; };
  // text: s may hold {claimId} placeholders, resolved through CL()
  E.text = (s, x, y, tier, o = {}) => {
    const a = o.alpha ?? 1; if (a <= 0.01 || s == null || s === '') return null;
    s = String(s).replace(/\{([a-z0-9_]+)\}/gi, (_, id) => E.CL(id));
    let px = TIERS[tier] || tier; const w8 = o.weight || W8[tier] || 600;
    if (px * zoom < FLOOR) { log.raised.push({ s, from: px, to: FLOOR / zoom }); px = FLOOR / zoom; }
    const mw = (z) => { ctx.save(); ctx.font = `${w8} ${z}px Inter`; ctx.fontVariantNumeric = 'tabular-nums'; const v = ctx.measureText(s).width; ctx.restore(); return v; };
    let w = mw(px); const pad = o.plate ? 14 : 0, room = (SAFE.x1 - SAFE.x0) / zoom - 2 * pad;
    if (w > room) { const fit = Math.max(FLOOR / zoom, px * room / w); log.fitted.push({ s, from: px, to: +fit.toFixed(1) }); px = fit; w = mw(px); } // too wide: shrink, never below the floor
    let x0 = o.align === 'center' ? x - w / 2 : o.align === 'right' ? x - w : x;
    let y0 = y - px * 0.8; const h = px * 1.05;
    // safe area (after camera zoom the box must still sit inside: zoom is about the centre)
    const sx = (v, c) => c + (v - c) * zoom;
    const outOf = (bx0, by0, bx1, by1) => { bx0 = sx(bx0, W / 2); bx1 = sx(bx1, W / 2); by0 = sx(by0, H / 2); by1 = sx(by1, H / 2);
      let dx = 0, dy = 0; if (bx0 < SAFE.x0) dx = (SAFE.x0 - bx0) / zoom; else if (bx1 > SAFE.x1) dx = (SAFE.x1 - bx1) / zoom;
      if (by0 < SAFE.y0) dy = (SAFE.y0 - by0) / zoom; else if (by1 > SAFE.y1) dy = (SAFE.y1 - by1) / zoom; return [dx, dy]; };
    let [dx, dy] = outOf(x0 - pad, y0 - pad, x0 + w + pad, y0 + h + pad); if (dx || dy) { log.shifted.push({ s, dx: Math.round(dx), dy: Math.round(dy) }); x0 += dx; y0 += dy; }
    let box = { x0: x0 - pad, y0: y0 - pad, x1: x0 + w + pad, y1: y0 + h + pad, g: o.group || s };
    // overlap: nudge below, else above, the box it hits; a nudge that leaves the safe area is not taken
    for (let k = 0; k < 4; k++) {
      const other = boxes.find((b) => b.g !== box.g && hit(b, box)); if (!other) break;
      const opts = [other.y1 - box.y0 + 8, other.y0 - box.y1 - 8].map((st) => ({ ...box, y0: box.y0 + st, y1: box.y1 + st, st }))
        .filter((b) => { const [ex, ey] = outOf(b.x0, b.y0, b.x1, b.y1); return !ex && !ey; });
      const pick = opts.find((b) => !boxes.some((o2) => o2.g !== box.g && hit(o2, b))) || opts[0];
      if (!pick || k === 3) { log.collisions.push({ s, with: other.s }); break; }
      y0 += pick.st; box = { x0: pick.x0, y0: pick.y0, x1: pick.x1, y1: pick.y1, g: box.g };
    }
    box.s = s; boxes.push(box);
    // contrast against what is behind: plate colour, else the frame background
    const behind = o.plate || C.bg; let color = o.color || C.ink, plate = o.plate;
    if (contrast(color, behind) < 4.5) { log.recoloured.push({ s, color }); color = C.ink; if (contrast(color, behind) < 4.5) plate = C.surface; }
    log.texts.push({ s, px: +(px * zoom).toFixed(2), z: +zoom.toFixed(4), contrast: +contrast(color, plate || C.bg).toFixed(2), box: [box.x0, box.y0, box.x1, box.y1].map(Math.round) });
    ctx.save(); ctx.globalAlpha = a;
    if (plate) { ctx.fillStyle = plate; E.round(box.x0, box.y0, box.x1 - box.x0, box.y1 - box.y0, 10); ctx.fill(); }
    ctx.font = `${w8} ${px}px Inter`; ctx.fontVariantNumeric = 'tabular-nums'; ctx.textBaseline = 'alphabetic'; ctx.textAlign = 'left';
    ctx.fillStyle = color; ctx.fillText(s, x0, y0 + px * 0.8); ctx.restore();
    return box;
  };
  E.measure = (s, tier, weight) => { ctx.save(); ctx.font = `${weight || W8[tier] || 600} ${TIERS[tier] || tier}px Inter`; const w = ctx.measureText(String(s).replace(/\{([a-z0-9_]+)\}/gi, (_, id) => cfg.claims[id]?.display ?? id)).width; ctx.restore(); return w; };
  E.round = (x, y, w, h, r) => { r = Math.max(0, Math.min(r, w / 2, h / 2)); ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath(); };
  E.rect = (x, y, w, h, fill, a = 1) => { if (a <= 0 || w <= 0 || h <= 0) return; ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); ctx.restore(); };
  E.line = (pts, color, lw, a = 1, dash) => { if (a <= 0 || pts.length < 2) return; ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineCap = 'round'; ctx.lineJoin = 'round'; if (dash) ctx.setLineDash(dash); ctx.beginPath(); pts.forEach(([x, y], i) => (i ? ctx.lineTo(x, y) : ctx.moveTo(x, y))); ctx.stroke(); ctx.restore(); };
  E.dot = (x, y, r, fill, a = 1, ring) => { if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = fill; ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.fill(); if (ring) { ctx.strokeStyle = ring; ctx.lineWidth = 3; ctx.beginPath(); ctx.arc(x, y, r + 4, 0, 7); ctx.stroke(); } ctx.restore(); };
  E.hatch = (x, y, w, h, a = 1, color = C.muted, gap = 16) => { if (a <= 0 || w <= 0 || h <= 0) return; ctx.save(); ctx.beginPath(); ctx.rect(x, y, w, h); ctx.clip(); ctx.globalAlpha = a; ctx.strokeStyle = color; ctx.lineWidth = 3; ctx.beginPath(); for (let k = -h; k < w + h; k += gap) { ctx.moveTo(x + k, y + h); ctx.lineTo(x + k + h, y); } ctx.stroke(); ctx.restore(); };
  E.person = (cx, base, s, a = 1, color = C.ink) => { // faceless figure; always illustrative
    if (a <= 0) return; E.illustrative(); ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = color;
    ctx.beginPath(); ctx.moveTo(cx - 110 * s, base); ctx.lineTo(cx - 110 * s, base - 130 * s); ctx.bezierCurveTo(cx - 110 * s, base - 215 * s, cx - 64 * s, base - 245 * s, cx, base - 245 * s);
    ctx.bezierCurveTo(cx + 64 * s, base - 245 * s, cx + 110 * s, base - 215 * s, cx + 110 * s, base - 130 * s); ctx.lineTo(cx + 110 * s, base); ctx.closePath(); ctx.fill();
    ctx.beginPath(); ctx.arc(cx, base - 320 * s, 60 * s, 0, 7); ctx.fill(); ctx.restore();
  };

  // one frame: shots = [{template, t0, t1, p, lead?, dur?}] already resolved; T = time; extra = {hook} for Shorts
  E.frame = (templates, shots, T, extra = {}) => {
    boxes = []; frameFlags = { claims: new Set(), hist: false, illus: false };
    log = { t: +T.toFixed(3), raised: [], fitted: [], shifted: [], collisions: [], recoloured: [], texts: [], tags: [], shots: [] };
    ctx.setTransform(SC, 0, 0, SC, 0, 0); ctx.fillStyle = C.bg; ctx.fillRect(0, 0, W, H);
    const live = shots.filter((s) => T >= s.t0 - 1e-6 && T < s.t1 - 1e-6);
    for (const s of live) { // lead/dur: a Short that enters a shot mid-way keeps the shot's clock and length
      const tl = T - s.t0 + (s.lead || 0), d = s.dur ?? s.t1 - s.t0; zoom = 1 + 0.015 * clamp(tl / Math.max(d, 1));
      ctx.save(); ctx.translate(W / 2, H / 2); ctx.scale(zoom, zoom); ctx.translate(-W / 2, -H / 2);
      const tpl = templates[s.template]; if (!tpl) throw new Error('unknown template ' + s.template);
      tpl.draw(E, tl, s.p, d, s); ctx.restore(); log.shots.push(s.id);
      if (s.p.illustrative) frameFlags.illus = true; if (s.p.historical) frameFlags.hist = true;
    }
    zoom = 1;
    // Shorts (playbook §5): every frame that shows a number carries both ILLUSTRATIVE and the history tag
    if (V && (frameFlags.claims.size || frameFlags.hist)) { frameFlags.illus = true; frameFlags.hist = true; }
    if (extra.hook) E.text(extra.hook, W / 2, SAFE.y0 + 70, 'head', { align: 'center', group: 'hook' });
    if (frameFlags.illus) { E.text('ILLUSTRATIVE', SAFE.x1, SAFE.y0 + (V ? 170 : 44), 'badge', { align: 'right', color: C.bg, plate: C.warn, group: 'tag-ill' }); log.tags.push('ILLUSTRATIVE'); }
    // counterweights (episode.yaml, required by spec.py): a line shown on every frame whose claims trigger it; attach:'history' joins the history tag
    let hist = 'US only · history, not a forecast', k = 0;
    for (const cw of cfg.counterweights || []) {
      const on = (cw.claims || []).some((id) => frameFlags.claims.has(id)) || (cw.when === 'historical' && frameFlags.hist)
        || (cw.when === 'numbers' && (frameFlags.claims.size > 0 || frameFlags.hist));
      if (!on) continue; log.tags.push('CW:' + cw.id);
      if (cw.attach === 'history' && frameFlags.hist) { // joins the history tag; Shorts: too narrow to join, so its own muted line just above it
        if (!V) hist += ' · ' + cw.text; else E.text(cw.text, W / 2, SAFE.y1 - 76, 'note', { align: 'center', color: C.muted, group: 'tag-hist-' + cw.id });
        continue; }
      let lines = [cw.text];
      if (V && E.measure(cw.text, 'note', 700) * FLOOR / TIERS.note > SAFE.x1 - SAFE.x0 - 28) { // Shorts: split at the sentence break nearest the middle
        const cut = [...cw.text.matchAll(/[.,;] /g)].map((m) => m.index + 1).sort((a, b) => Math.abs(a - cw.text.length / 2) - Math.abs(b - cw.text.length / 2))[0] ?? cw.text.lastIndexOf(' ', cw.text.length / 2);
        lines = [cw.text.slice(0, cut).trim(), cw.text.slice(cut).trim()]; }
      for (const ln of lines) { E.text(ln, V ? W / 2 : SAFE.x1, V ? SAFE.y0 + 400 + 76 * k : SAFE.y0 + 112 + 62 * k, 'note', { align: V ? 'center' : 'right', weight: 700, color: C.ink, plate: C.surface, group: 'cw-' + cw.id }); k++; }
    }
    if (frameFlags.hist) { E.text(hist, V ? W / 2 : SAFE.x1, SAFE.y1 - 6, 'note', { align: V ? 'center' : 'right', color: C.muted, group: 'tag-hist' }); log.tags.push('HISTORY'); }
    log.claims = [...frameFlags.claims]; log.hist = frameFlags.hist; log.illus = frameFlags.illus;
    return log;
  };
  return E;
}
