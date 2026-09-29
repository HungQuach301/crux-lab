// C4 animatic engine = the signed C3 final engine (design/c3/final/src/engine.js) with four changes:
//  1. type tiers from animatic tokens.json (every size -20%, floor 40 px at 1080p);
//  2. scenes keep 1920x1080 LOGICAL coordinates but render at 1280x720 (ctx transform; WebGL at 1280x720);
//  3. timing: every scene gets T (its sentences from timing.json, local seconds) and T.a(id) resolves an anchor from
//     anchors.json (sentence n + keyword) -> no hard-coded seconds for any meaningful action;
//  4. text({sent:true}) marks a sentence-caption (a line that restates narration); hidden when NOCAP (blind strips).
// Every scene is a deterministic function of t (seconds, scene-local). Every number on screen goes through CL(claimId).
import * as THREE from 'three';
export { THREE };

export const TOK = await (await fetch('/src/tokens.json')).json();
export const DATA = window.DATA;
export const W = TOK.canvas.w, H = TOK.canvas.h, OW = TOK.canvas.out.w, OH = TOK.canvas.out.h;
const col = TOK.color;
export const C = {
  bg: col.bg, surface: col.surface, grid: col.grid, ink: col.ink, muted: col['ink-muted'], accent: col.accent,
  warn: col.warn, positive: col.positive, negative: col.negative, ...TOK.materials,
};
export const TIER = TOK.type.tiers;

// ---------- claims ----------
export const USED = new Set();
export function CL(id) {
  const c = DATA.claims[id];
  if (!c) throw new Error('unknown claim ' + id);
  USED.add(id); return c.display;
}

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

// ---------- text (flat, screen space, always sharp) ----------
export const TEXTLOG = new Map(); // string -> {tier, px, n, out}
let CUR_T = 0;
const SAFE = { x0: 40, x1: W - 40, y0: 36, y1: H - 18 };
export function rgba(hex, a) { const n = parseInt(hex.slice(1), 16); return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`; }
export function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
}
export function measure(ctx, s, tier, weight) {
  const T = TIER[tier]; ctx.save(); ctx.font = `${weight || T.weight} ${T.px}px Inter`; const w = ctx.measureText(s).width; ctx.restore(); return w;
}
// tier: hero | number | head | caption | label | note. o: color, align, alpha, weight, plate (bg colour), shadow
export function text(ctx, s, x, y, tier, o = {}) {
  const T = TIER[tier]; if (!T) throw new Error('tier ' + tier);
  const alpha = o.alpha === undefined ? 1 : o.alpha;
  if (alpha <= 0.001 || !s) return 0;
  if (o.sent && window.NOCAP) return measure(ctx, s, tier, o.weight);
  const px = T.px, weight = o.weight || T.weight;
  ctx.save(); ctx.globalAlpha = alpha;
  ctx.font = `${weight} ${px}px Inter`; ctx.textAlign = o.align || 'left'; ctx.textBaseline = 'alphabetic';
  ctx.fontVariantNumeric = 'tabular-nums';
  const w = ctx.measureText(s).width;
  const x0 = o.align === 'center' ? x - w / 2 : o.align === 'right' ? x - w : x;
  const top = y - px * 0.76, bot = y + px * 0.22;
  if (o.plate) { ctx.fillStyle = o.plate; roundRect(ctx, x0 - 18, top - 12, w + 36, bot - top + 24, 10); ctx.fill(); }
  else if (o.shadow) { ctx.shadowColor = 'rgba(0,0,0,0.9)'; ctx.shadowBlur = 14; ctx.shadowOffsetY = 3; }
  ctx.fillStyle = o.color || C.ink; ctx.fillText(s, x, y);
  ctx.restore();
  if (alpha >= 0.2) {
    const out = x0 < SAFE.x0 || x0 + w > SAFE.x1 || top < SAFE.y0 || bot > SAFE.y1;
    const e = TEXTLOG.get(s) || { tier, px, n: 0, out: 0, firstT: CUR_T, sent: !!o.sent };
    e.n++; if (out) e.out++; TEXTLOG.set(s, e);
  }
  return w;
}
export function badge(ctx, x, y, alpha = 1, align = 'right') { // ILLUSTRATIVE pill; (x,y) = text baseline anchor
  if (alpha <= 0.001) return 0;
  const s = 'ILLUSTRATIVE', px = TOK.type.badge.px;
  ctx.save(); ctx.font = `700 ${px}px Inter`; const w = ctx.measureText(s).width; ctx.restore();
  const x0 = align === 'right' ? x - w : x;
  ctx.save(); ctx.globalAlpha = alpha; ctx.fillStyle = C.warn; roundRect(ctx, x0 - 16, y - px * 0.76 - 12, w + 32, px * 0.98 + 24, 8); ctx.fill(); ctx.restore();
  text(ctx, s, x0, y, 'note', { weight: 700, color: C.bg, alpha });
  return w + 32;
}
// constant furniture: ILLUSTRATIVE badge (top right) and ONE source line (bottom left), both >= note tier
export function chrome(ctx, { illus = 0, source = '', srcAlpha = 1, plate = false } = {}) {
  if (illus > 0) badge(ctx, W - 96, 110, illus);
  if (source) text(ctx, source, 96, H - 44, 'note', { color: C.muted, alpha: srcAlpha, plate: plate ? 'rgba(14,17,22,0.78)' : null });
}
export function strike(ctx, x0, y, x1, color, alpha, lw = 7) {
  if (alpha <= 0) return; ctx.save(); ctx.globalAlpha = alpha; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineCap = 'round';
  ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke(); ctx.restore();
}
// 2D primitives (H3)
export function line(ctx, pts, color, lw, o = {}) {
  ctx.save(); ctx.globalAlpha = o.alpha === undefined ? 1 : o.alpha; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineJoin = 'round'; ctx.lineCap = o.cap || 'round';
  if (o.dash) ctx.setLineDash(o.dash); ctx.beginPath(); pts.forEach((p, i) => (i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]))); ctx.stroke(); ctx.restore();
}
export function rect(ctx, x, y, w, h, fill, a = 1) { if (a <= 0.001 || !h || !w) return; ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); ctx.restore(); }
export function srect(ctx, x, y, w, h, color, lw, a = 1, dash) { if (a <= 0.001) return; ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = color; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); ctx.restore(); }
export function hatch(ctx, x, y, w, h, color, a, step = 16, lw = 4) {
  if (a <= 0.001 || h <= 0 || w <= 0) return;
  ctx.save(); ctx.globalAlpha = a; ctx.beginPath(); ctx.rect(x, y, w, h); ctx.clip(); ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.beginPath();
  for (let k = -h; k < w + h; k += step) { ctx.moveTo(x + k, y + h); ctx.lineTo(x + k + h, y); }
  ctx.stroke(); ctx.restore();
}
export function dot(ctx, cx, cy, r, color, a = 1) { if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = color; ctx.beginPath(); ctx.arc(cx, cy, r, 0, 7); ctx.fill(); ctx.restore(); }
export function tri(ctx, cx, cy, r, color, a = 1) { if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = color; ctx.beginPath(); ctx.moveTo(cx, cy - r); ctx.lineTo(cx + r * 0.95, cy + r * 0.7); ctx.lineTo(cx - r * 0.95, cy + r * 0.7); ctx.closePath(); ctx.fill(); ctx.restore(); }
export function sq(ctx, cx, cy, r, color, a = 1) { rect(ctx, cx - r * 0.8, cy - r * 0.8, r * 1.6, r * 1.6, color, a); }
export const MARK = { nora: [dot, C.positive], walt: [tri, C.warn], anjali: [sq, C.negative] };
export function mark(ctx, who, cx, cy, r, a = 1) { const [f, c] = MARK[who]; f(ctx, cx, cy, r, c, a); }

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

// ---------- boot: 3D (optional) + 2D overlay, frame/strip/png API ----------
export function boot(mod, T) {
  const out = document.createElement('canvas'); out.width = OW; out.height = OH; document.body.appendChild(out);
  const ctx = out.getContext('2d', { willReadFrequently: true });
  let renderer = null, scene = null, camera = null;
  if (mod.uses3d) {
    const gl = document.createElement('canvas'); gl.width = OW; gl.height = OH;
    renderer = new THREE.WebGLRenderer({ canvas: gl, antialias: true, preserveDrawingBuffer: true, powerPreference: 'low-power' });
    renderer.setPixelRatio(1); renderer.setSize(OW, OH, false);
    renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFShadowMap;
    renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    scene = new THREE.Scene(); camera = new THREE.PerspectiveCamera(35, W / H, 0.1, 200);
  }
  const S = mod.build({ THREE, scene, camera, renderer, ctx, T });
  const proj = (v) => { const p = v.clone().project(camera); return { x: (p.x + 1) / 2 * W, y: (1 - p.y) / 2 * H }; };
  function draw(t) {
    CUR_T = t;
    const m = S.mode ? S.mode(t) : (mod.uses3d ? '3d' : '2d');
    ctx.setTransform(OW / W, 0, 0, OH / H, 0, 0);
    ctx.save(); ctx.fillStyle = C.bg; ctx.fillRect(0, 0, W, H); ctx.restore();
    if (m === '3d') {
      S.update(t); camera.updateMatrixWorld(); renderer.render(scene, camera);
      ctx.drawImage(renderer.domElement, 0, 0, W, H);
      const vg = ctx.createRadialGradient(W / 2, H / 2, H * 0.4, W / 2, H / 2, H * 0.98);
      vg.addColorStop(0, 'rgba(14,17,22,0)'); vg.addColorStop(1, 'rgba(14,17,22,0.5)'); ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
    }
    S.overlay(ctx, t, proj, m);
  }
  const b64 = (u8) => { let s = ''; const n = 0x8000; for (let i = 0; i < u8.length; i += n) s += String.fromCharCode.apply(null, u8.subarray(i, i + n)); return btoa(s); };
  const N = Math.round((T.start + T.dur) * TOK.canvas.fps) - Math.round(T.start * TOK.canvas.fps);
  const even = [0.08, 0.25, 0.42, 0.6, 0.78, 0.97].map((f) => f * T.dur);
  return {
    duration: T.dur, frames: N, stripTimes: (S.stripTimes || even).map((x) => Math.min(x, (N - 1) / TOK.canvas.fps)),
    hardTime: Math.min(S.hardTime ?? (N - 1) / TOK.canvas.fps, (N - 1) / TOK.canvas.fps), modeAt: (t) => (S.mode ? S.mode(t) : (mod.uses3d ? '3d' : '2d')),
    info: () => { if (!renderer) return '2d canvas'; const g = renderer.getContext(); const e = g.getExtension('WEBGL_debug_renderer_info'); return e ? g.getParameter(e.UNMASKED_RENDERER_WEBGL) : g.getParameter(g.RENDERER); },
    frame(t) { draw(t); return b64(new Uint8Array(ctx.getImageData(0, 0, OW, OH).data.buffer)); },
    png(t) { draw(t); return out.toDataURL('image/png'); },
    log: () => ({ used: [...USED].sort(), texts: [...TEXTLOG.entries()].map(([s, e]) => ({ s, ...e })),
      anchorsUsed: [...ANCH_USED].sort(), anchorsDeclared: T.anchorIds, anchorsKeywordMissing: T.missing }),
    strip(times) { // blind-test strip: 3 x 2 grid of 636x358 frames, numbered 1-6 (reading order), NO sentence captions
      const sc = document.createElement('canvas'); sc.width = 1920; sc.height = 728; const g = sc.getContext('2d');
      g.fillStyle = '#05070A'; g.fillRect(0, 0, 1920, 728);
      const was = window.NOCAP; window.NOCAP = true;
      times.forEach((t, i) => {
        const x = 2 + (i % 3) * 640 + 1, y = 2 + Math.floor(i / 3) * 363;
        draw(t); g.drawImage(out, x, y, 636, 358);
        g.fillStyle = C.warn; g.fillRect(x + 636 - 46, y + 358 - 46, 40, 40);
        ptxt(g, String(i + 1), x + 636 - 26, y + 358 - 14, { size: 30, weight: 700, color: C.bg, align: 'center' });
      });
      window.NOCAP = was;
      return sc.toDataURL('image/png');
    },
  };
}
