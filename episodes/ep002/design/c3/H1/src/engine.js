// C3 Tập 2 · H1 "Vật thể thật" — engine (adapted from episodes/ep001/design/c3/final/src/engine.js: same token file,
// same idea of ONE text function, every number through CL(claimId)). New here:
//   * 1280x720 native; type tiers = Tập 1 tiers x0.8 (G-009 C3: "giảm đều ~20%") x 2/3 (1080 -> 720), floor 27 px @720
//     = 40.5 px @1080 (G-014 floor 40 px).
//   * EVERY string sits on an opaque token-`bg` plate (D2): no text ever touches a 3D material.
//   * MASK mode: the glyph box of every string (incl. the ILLUSTRATIVE badge) is replaced by a flat `surface` block.
//   * AUDIT mode: glyphs are not drawn; boxes are logged so render.js can measure text-to-graphics distance (D4).
import * as THREE from 'three';
export { THREE };

export const TOK = await (await fetch('/tokens.json')).json();
export const DATA = window.DATA;
export const W = 1280, H = 720, FPS = 30;
const col = TOK.color;
export const C = {
  bg: col.bg, surface: col.surface, grid: col.grid, ink: col.ink, muted: col['ink-muted'], accent: col.accent,
  warn: col.warn, positive: col.positive, negative: col.negative, ...TOK.materials,
  // 3D-only object materials added for this direction (never used for text or flat marks):
  steel: '#8E98A6', coin: '#C3C8CF', coinEdge: '#A7AEB8', glass: '#CFE3F2', tray: '#232831', tileBlank: '#E6E1D6',
};
// px @720p; at1080 = px * 1.5
export const TIER = {
  hero: { px: 80, weight: 700 }, number: { px: 52, weight: 700 }, head: { px: 40, weight: 700 },
  caption: { px: 34, weight: 600 }, label: { px: 30, weight: 600 }, note: { px: 27, weight: 600 },
  badge: { px: 32, weight: 700 },
};
export const BADGE_PX = 32; // tokens type.badge 48 @1080 -> 32 @720

export const MODE = { mask: false, audit: false };
export const USED = new Set();
export function CL(id) { const c = DATA.claims[id]; if (!c) throw new Error('unknown claim ' + id); USED.add(id); return c.display; }

// ---------- easing ----------
export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lin = (t, a, b) => clamp((t - a) / (b - a));
export const smooth = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
export const ease = (t, a, b) => smooth(lin(t, a, b));
export const easeOut = (t, a, b) => { const x = lin(t, a, b); return 1 - Math.pow(1 - x, 3); };
export const back = (t, a, b) => { const x = lin(t, a, b), s = 1.7; return 1 + (s + 1) * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2); };
export const mix = (a, b, x) => a + (b - a) * x;
export const inout = (t, a, b, c, d) => Math.min(ease(t, a, b), 1 - ease(t, c, d));

// ---------- text ----------
export let FRAME_TEXTS = [];
export const TEXTLOG = new Map();
let CUR_T = 0;
const SAFE = { x0: 32, x1: W - 32, y0: 24, y1: H - 16 };
export function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
}
const PADX = 12, PADY = 8;
// Draw one string on an opaque plate. Returns the plate box {x,y,w,h}.
export function text(ctx, s, x, y, tier, o = {}) {
  const T = TIER[tier]; if (!T) throw new Error('tier ' + tier);
  const alpha = o.alpha === undefined ? 1 : o.alpha;
  if (alpha <= 0.02 || !s) return null;
  const px = T.px, weight = o.weight || T.weight;
  ctx.save(); ctx.globalAlpha = alpha;
  ctx.font = `${weight} ${px}px Inter`; ctx.textAlign = o.align || 'left'; ctx.textBaseline = 'alphabetic';
  ctx.fontVariantNumeric = 'tabular-nums';
  const m = ctx.measureText(s);
  const gx0 = Math.floor(x - m.actualBoundingBoxLeft), gx1 = Math.ceil(x + m.actualBoundingBoxRight);
  const gy0 = Math.floor(y - m.actualBoundingBoxAscent), gy1 = Math.ceil(y + m.actualBoundingBoxDescent);
  // plate height uses the font's cap/descender span so plates of one tier line up
  const py0 = Math.min(gy0, Math.round(y - px * 0.76)), py1 = Math.max(gy1, Math.round(y + px * 0.22));
  const plate = o.plateColor || C.bg;
  const pb = { x: gx0 - PADX, y: py0 - PADY, w: gx1 - gx0 + 2 * PADX, h: py1 - py0 + 2 * PADY };
  ctx.fillStyle = plate; roundRect(ctx, pb.x, pb.y, pb.w, pb.h, o.radius ?? 8); ctx.fill();
  if (MODE.mask) { ctx.fillStyle = C.surface; ctx.fillRect(gx0 - 1, gy0 - 1, gx1 - gx0 + 2, gy1 - gy0 + 2); }
  else if (!MODE.audit) { ctx.fillStyle = o.color || C.ink; ctx.fillText(s, x, y); }
  ctx.restore();
  if (alpha >= 0.99) {
    const box = { s, px, tier, color: o.color || C.ink, plate, gx0, gx1, gy0, gy1, pb };
    FRAME_TEXTS.push(box);
    const out = pb.x < SAFE.x0 || pb.x + pb.w > SAFE.x1 || pb.y < SAFE.y0 || pb.y + pb.h > SAFE.y1;
    const e = TEXTLOG.get(s) || { tier, px, px1080: px * 1.5, color: box.color, n: 0, out: 0, firstT: CUR_T };
    e.n++; if (out) e.out++; TEXTLOG.set(s, e);
  }
  return pb;
}
export function badge(ctx, alpha = 1) { // ILLUSTRATIVE pill, top right; warn plate, bg text
  if (alpha <= 0.02) return;
  ctx.save(); ctx.font = `700 ${BADGE_PX}px Inter`; const w = ctx.measureText('ILLUSTRATIVE').width; ctx.restore();
  text(ctx, 'ILLUSTRATIVE', W - 40 - 14 - w, 66, 'badge', { color: C.bg, plateColor: C.warn, alpha, radius: 6 });
}
// one source line (note tier, muted): the ridge is real data (TB3MS, FRED: "Public Domain: Citation Requested")
export const SRC = '3-month Treasury bill rate, via FRED';
export function source(ctx, where = 'br', alpha = 1) {
  if (where === 'br') text(ctx, SRC, W - 40 - 12, H - 36, 'note', { align: 'right', color: C.muted, alpha });
  else text(ctx, SRC, 40 + 12, 60, 'note', { color: C.muted, alpha });
}
// a number (ink, emphasised) followed by its secondary words (muted, D5) on one baseline, two plates 8 px apart
export function numWords(ctx, num, words, x, y, o = {}) {
  const nt = o.numTier || 'number', wt = o.wordTier || 'label';
  ctx.save(); ctx.font = `${TIER[nt].weight} ${TIER[nt].px}px Inter`; const wn = ctx.measureText(num).width;
  ctx.font = `${TIER[wt].weight} ${TIER[wt].px}px Inter`; const ww = words ? ctx.measureText(words).width : 0; ctx.restore();
  const gap = 2 * PADX + 10, total = wn + (words ? gap + ww : 0);
  const x0 = o.align === 'center' ? x - total / 2 : o.align === 'right' ? x - total : x;
  text(ctx, num, x0, y, nt, { color: o.numColor || C.ink, alpha: o.alpha });
  if (words) text(ctx, words, x0 + wn + gap, y, wt, { color: o.wordColor || C.muted, alpha: o.alpha });
}

// ---------- 3D helpers ----------
export const mat = (color, o = {}) => new THREE.MeshStandardMaterial({ color, roughness: 0.8, metalness: 0, ...o });
export function box(w, h, d, m, { cast = true, recv = true } = {}) { const b = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m); b.castShadow = cast; b.receiveShadow = recv; return b; }
export function canvasTex(w, h, draw) {
  const cv = document.createElement('canvas'); cv.width = w; cv.height = h;
  const g = cv.getContext('2d'); draw(g, w, h);
  const tex = new THREE.CanvasTexture(cv); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8; return tex;
}

// ---------- boot ----------
export function boot(mod) {
  const out = document.createElement('canvas'); out.width = W; out.height = H; document.body.appendChild(out);
  const ctx = out.getContext('2d', { willReadFrequently: true });
  const gl = document.createElement('canvas'); gl.width = W; gl.height = H;
  const renderer = new THREE.WebGLRenderer({ canvas: gl, antialias: true, preserveDrawingBuffer: true, powerPreference: 'low-power' });
  renderer.setPixelRatio(1); renderer.setSize(W, H, false);
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene(); const camera = new THREE.PerspectiveCamera(35, W / H, 0.1, 200);
  const S = mod.build({ THREE, scene, camera, renderer, ctx });
  const proj = (v) => { const p = v.clone().project(camera); return { x: (p.x + 1) / 2 * W, y: (1 - p.y) / 2 * H }; };
  function draw(t) {
    CUR_T = t; FRAME_TEXTS = [];
    ctx.save(); ctx.fillStyle = C.bg; ctx.fillRect(0, 0, W, H); ctx.restore();
    S.update(t); camera.updateMatrixWorld(); renderer.render(scene, camera);
    ctx.drawImage(renderer.domElement, 0, 0);
    const vg = ctx.createRadialGradient(W / 2, H / 2, H * 0.42, W / 2, H / 2, H * 0.98);
    vg.addColorStop(0, 'rgba(14,17,22,0)'); vg.addColorStop(1, 'rgba(14,17,22,0.45)'); ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
    S.overlay(ctx, t, proj);
  }
  const b64 = (u8) => { let s = ''; const n = 0x8000; for (let i = 0; i < u8.length; i += n) s += String.fromCharCode.apply(null, u8.subarray(i, i + n)); return btoa(s); };
  const N = Math.round(S.duration * FPS);
  const hex = (h) => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];
  // D4 audit at time t: render without glyphs; for each string, distance (px) from its glyph box to the nearest pixel
  // that is not its plate colour (= any graphic or other plate edge), searched up to 40 px; and min box-to-box distance.
  function audit(t) {
    MODE.audit = true; draw(t); MODE.audit = false;
    const img = ctx.getImageData(0, 0, W, H).data;
    const res = [];
    for (const b of FRAME_TEXTS) {
      const pc = hex(b.plate); let dist = 99;
      for (let d = 1; d <= 40 && dist === 99; d++) {
        const x0 = b.gx0 - d, x1 = b.gx1 + d, y0 = b.gy0 - d, y1 = b.gy1 + d;
        const test = (x, y) => { if (x < 0 || y < 0 || x >= W || y >= H) return false; const i = (y * W + x) * 4; return Math.abs(img[i] - pc[0]) + Math.abs(img[i + 1] - pc[1]) + Math.abs(img[i + 2] - pc[2]) > 30; };
        for (let x = x0; x <= x1 && dist === 99; x++) if (test(x, y0) || test(x, y1)) dist = d;
        for (let y = y0; y <= y1 && dist === 99; y++) if (test(x0, y) || test(x1, y)) dist = d;
      }
      let tt = 999;
      for (const o of FRAME_TEXTS) if (o !== b) {
        const dx = Math.max(o.gx0 - b.gx1, b.gx0 - o.gx1, 0), dy = Math.max(o.gy0 - b.gy1, b.gy0 - o.gy1, 0);
        tt = Math.min(tt, Math.hypot(dx, dy));
      }
      res.push({ s: b.s, px: b.px, color: b.color, plate: b.plate, toGraphics: dist, toText: tt === 999 ? null : +tt.toFixed(1) });
    }
    return res;
  }
  return {
    duration: S.duration, frames: N, stripTimes: S.stripTimes,
    info: () => { const g = renderer.getContext(); const e = g.getExtension('WEBGL_debug_renderer_info'); return e ? g.getParameter(e.UNMASKED_RENDERER_WEBGL) : g.getParameter(g.RENDERER); },
    frame(t) { draw(t); return b64(new Uint8Array(ctx.getImageData(0, 0, W, H).data.buffer)); },
    png(t, mask = false) { MODE.mask = mask; draw(t); MODE.mask = false; return out.toDataURL('image/png'); },
    audit,
    boxes(t) { draw(t); return FRAME_TEXTS.map((b) => ({ text: b.s, box: [b.gx0, b.gy0, b.gx1 - b.gx0, b.gy1 - b.gy0], plate: [b.pb.x, b.pb.y, b.pb.w, b.pb.h], fontPx: b.px, color: b.color })); },
    log: () => ({ used: [...USED].sort(), texts: [...TEXTLOG.entries()].map(([s, e]) => ({ s, ...e })) }),
    strip(times, mask) { // 3x2 grid of 640x360 frames, numbered 1-6 in a band above each frame, no captions
      const sc = document.createElement('canvas'); sc.width = 1920; sc.height = 2 * 404; const g = sc.getContext('2d');
      g.fillStyle = C.bg; g.fillRect(0, 0, sc.width, sc.height);
      MODE.mask = !!mask;
      times.forEach((t, i) => {
        const cx = (i % 3) * 640, cy = Math.floor(i / 3) * 404;
        draw(t); g.drawImage(out, cx + 2, cy + 42, 636, 358);
        g.fillStyle = C.warn; g.fillRect(cx + 8, cy + 4, 34, 34);
        g.font = '700 26px Inter'; g.fillStyle = C.bg; g.textAlign = 'center'; g.fillText(String(i + 1), cx + 25, cy + 31);
      });
      MODE.mask = false;
      return sc.toDataURL('image/png');
    },
  };
}
