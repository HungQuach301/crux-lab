// H1 "real objects": shared renderer, flat screen-space text, paper textures, simple house builder.
// Everything is deterministic in t (seconds); no Math.random without a seed.
import * as THREE from 'three';
export { THREE };

export const W = 1280, H = 720;
// Channel tokens (genre-spec/channel/visual-tokens.json) + a few object-material colours (paper, wood) that are
// not UI colours.
export const C = {
  bg: '#0E1116', surface: '#171B22', ink: '#F2F4F7', muted: '#9AA4B2', accent: '#4C8DFF',
  warn: '#F2B441', positive: '#3FBF7F', negative: '#E5484D', grid: '#2A303B',
  paper: '#F4F1EA', paperEdge: '#D9D3C4', wood: '#6B4A33',
};

export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lin = (t, a, b) => clamp((t - a) / (b - a));
export const smooth = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
export const ease = (t, a, b) => smooth(lin(t, a, b));
export const easeOut = (t, a, b) => { const x = lin(t, a, b); return 1 - Math.pow(1 - x, 3); };
export const back = (t, a, b) => { const x = lin(t, a, b), s = 1.4; return 1 + (s + 1) * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2); };
export const mix = (a, b, x) => a + (b - a) * x;
export function rng(seed) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }

// ---------- canvas textures (text printed on objects) ----------
export function canvasTex(w, h, draw) {
  const cv = document.createElement('canvas'); cv.width = w; cv.height = h;
  const g = cv.getContext('2d');
  draw(g, w, h);
  const tex = new THREE.CanvasTexture(cv);
  tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
  tex.userData.redraw = (fn) => { g.clearRect(0, 0, w, h); fn(g, w, h); tex.needsUpdate = true; };
  return tex;
}
export function font(g, size, weight = 600) { g.font = `${weight} ${size}px Inter`; }
export function txt(g, s, x, y, { size = 40, weight = 600, color = C.ink, align = 'left', base = 'alphabetic' } = {}) {
  font(g, size, weight); g.fillStyle = color; g.textAlign = align; g.textBaseline = base; g.fillText(s, x, y);
}

// ---------- flat screen-space labels (always sharp) ----------
export function label(ctx, s, x, y, o = {}) {
  const { size = 26, weight = 600, color = C.ink, align = 'left', alpha = 1, bg = null, pad = 8, shadow = true, base = 'alphabetic' } = o;
  if (alpha <= 0.001) return { w: 0 };
  ctx.save(); ctx.globalAlpha = alpha;
  ctx.font = `${weight} ${size}px Inter`; ctx.textAlign = align; ctx.textBaseline = base;
  ctx.fontVariantNumeric = 'tabular-nums';
  const w = ctx.measureText(s).width;
  if (bg) {
    const x0 = align === 'center' ? x - w / 2 : align === 'right' ? x - w : x;
    ctx.fillStyle = bg; roundRect(ctx, x0 - pad, y - size * 0.92 - pad * 0.6, w + pad * 2, size * 1.2 + pad * 1.2, 6); ctx.fill();
  } else if (shadow) { ctx.shadowColor = 'rgba(0,0,0,0.85)'; ctx.shadowBlur = 10; ctx.shadowOffsetY = 2; }
  ctx.fillStyle = color; ctx.fillText(s, x, y);
  ctx.restore();
  return { w };
}
export function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
}
export function badge(ctx, s, x, y, alpha = 1, color = C.warn) {
  label(ctx, s, x, y, { size: 16, weight: 700, color: C.bg, bg: color, pad: 6, alpha });
}
export function chrome(ctx, t, { illus = true, source = '' } = {}) {
  // small constant furniture: nominal $, ILLUSTRATIVE, source line
  label(ctx, 'nominal $', 1216, 44, { size: 16, weight: 600, color: C.muted, align: 'right', shadow: false });
  if (illus) badge(ctx, 'ILLUSTRATIVE', 1000, 44);
  if (source) label(ctx, source, 32, 700, { size: 15, weight: 400, color: C.muted, shadow: true });
}
export function strike(ctx, x0, y, x1, color, alpha) {
  ctx.save(); ctx.globalAlpha = alpha; ctx.strokeStyle = color; ctx.lineWidth = 4; ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke(); ctx.restore();
}

// ---------- materials & geometry ----------
export const mat = (color, o = {}) => new THREE.MeshStandardMaterial({ color, roughness: 0.8, metalness: 0, ...o });
export function box(w, h, d, m, { cast = true, recv = true } = {}) {
  const b = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m); b.castShadow = cast; b.receiveShadow = recv; return b;
}
// A house: box body + gable roof prism + windows (emissive when lit) + door + chimney. Origin at ground centre.
export function house({ w = 3, d = 2.4, h = 1.8, roof = 1.2, wall = '#C9BBA4', roofCol = '#3B3F48', lit = 0, trim = '#EDE6D6' } = {}) {
  const g = new THREE.Group();
  const body = box(w, h, d, mat(wall, { roughness: 0.9 })); body.position.y = h / 2; g.add(body);
  const sh = new THREE.Shape(); sh.moveTo(-w / 2 - 0.12, 0); sh.lineTo(w / 2 + 0.12, 0); sh.lineTo(0, roof); sh.closePath();
  const rg = new THREE.ExtrudeGeometry(sh, { depth: d + 0.3, bevelEnabled: false });
  const r = new THREE.Mesh(rg, mat(roofCol, { roughness: 0.7 })); r.position.set(0, h, -d / 2 - 0.15); r.castShadow = r.receiveShadow = true; g.add(r);
  const ch = box(w * 0.1, roof * 0.7, w * 0.1, mat('#6E4F3E')); ch.position.set(w * 0.25, h + roof * 0.55, -d * 0.1); g.add(ch);
  const winMat = new THREE.MeshStandardMaterial({ color: '#2B2F38', emissive: new THREE.Color('#FFC477'), emissiveIntensity: lit, roughness: 0.3 });
  const wins = [];
  const ww = w * 0.16, wh = h * 0.3;
  for (const [x, y] of [[-w * 0.28, h * 0.55], [w * 0.28, h * 0.55]]) {
    const fr = box(ww + 0.08, wh + 0.08, 0.04, mat(trim)); fr.position.set(x, y, d / 2 + 0.01); g.add(fr);
    const wi = new THREE.Mesh(new THREE.PlaneGeometry(ww, wh), winMat); wi.position.set(x, y, d / 2 + 0.035); g.add(wi); wins.push(wi);
    const bar = box(0.025, wh, 0.02, mat(trim)); bar.position.set(x, y, d / 2 + 0.045); g.add(bar);
  }
  // side windows
  for (const z of [-d * 0.2, d * 0.22]) {
    const wi = new THREE.Mesh(new THREE.PlaneGeometry(ww * 0.9, wh), winMat); wi.rotation.y = Math.PI / 2; wi.position.set(w / 2 + 0.012, h * 0.55, z); g.add(wi);
  }
  const door = box(w * 0.14, h * 0.5, 0.05, mat('#5A3A2A')); door.position.set(0, h * 0.25, d / 2 + 0.02); g.add(door);
  const step = box(w * 0.26, 0.08, 0.3, mat('#8C8C88')); step.position.set(0, 0.04, d / 2 + 0.15); g.add(step);
  g.userData = { winMat, w, d, h, roof };
  return g;
}

// A stack of paper sheets (one merged column of thin boxes with small deterministic jitter).
export function paperSheet(w, d, th, color, edgeColor) {
  const m = [mat(edgeColor, { roughness: 0.95 }), mat(edgeColor, { roughness: 0.95 }), mat(color, { roughness: 0.9 }),
    mat(edgeColor), mat(edgeColor, { roughness: 0.95 }), mat(edgeColor, { roughness: 0.95 })];
  const b = new THREE.Mesh(new THREE.BoxGeometry(w, th, d), m); b.castShadow = true; b.receiveShadow = true; return b;
}

// ---------- boot ----------
export function boot(mod) {
  const gl = document.createElement('canvas'); gl.width = W; gl.height = H;
  const renderer = new THREE.WebGLRenderer({ canvas: gl, antialias: true, preserveDrawingBuffer: true, powerPreference: 'low-power' });
  renderer.setPixelRatio(1); renderer.setSize(W, H, false);
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  const out = document.createElement('canvas'); out.width = W; out.height = H; document.body.appendChild(out);
  const ctx = out.getContext('2d', { willReadFrequently: true });
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(35, W / H, 0.1, 200);
  const S = mod.build({ THREE, scene, camera, renderer });
  const proj = (v) => { const p = v.clone().project(camera); return { x: (p.x + 1) / 2 * W, y: (1 - p.y) / 2 * H }; };
  function draw(t) {
    S.update(t);
    camera.updateMatrixWorld();
    renderer.render(scene, camera);
    ctx.clearRect(0, 0, W, H);
    ctx.drawImage(gl, 0, 0);
    // soft vignette
    const vg = ctx.createRadialGradient(W / 2, H / 2, H * 0.35, W / 2, H / 2, H * 0.95);
    vg.addColorStop(0, 'rgba(14,17,22,0)'); vg.addColorStop(1, 'rgba(14,17,22,0.55)');
    ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
    S.overlay(ctx, t, proj);
  }
  const b64 = (u8) => { let s = ''; const n = 0x8000; for (let i = 0; i < u8.length; i += n) s += String.fromCharCode.apply(null, u8.subarray(i, i + n)); return btoa(s); };
  return {
    duration: S.duration, stripTimes: S.stripTimes, posterTime: S.posterTime,
    info: () => { const g = renderer.getContext(); const e = g.getExtension('WEBGL_debug_renderer_info'); return e ? g.getParameter(e.UNMASKED_RENDERER_WEBGL) : g.getParameter(g.RENDERER); },
    frame(t) { draw(t); return b64(new Uint8Array(ctx.getImageData(0, 0, W, H).data.buffer)); },
    png(t) { draw(t); return out.toDataURL('image/png'); },
    strip(times) {
      // 1920x220: six 320x180 thumbnails, numbered 1-6, time under each
      const sc = document.createElement('canvas'); sc.width = 1920; sc.height = 220; const g = sc.getContext('2d');
      g.fillStyle = C.bg; g.fillRect(0, 0, 1920, 220);
      times.forEach((t, i) => {
        draw(t); g.drawImage(out, i * 320 + 2, 2, 316, 178);
        g.fillStyle = C.warn; g.fillRect(i * 320 + 100, 186, 30, 30);
        txt(g, String(i + 1), i * 320 + 115, 209, { size: 22, weight: 700, color: C.bg, align: 'center' });
        txt(g, `t = ${t.toFixed(1)} s`, i * 320 + 140, 209, { size: 20, weight: 600, color: C.ink });
      });
      return sc.toDataURL('image/png');
    },
  };
}
