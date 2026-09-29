// C5 film page: ONE page draws any frame of the whole episode (S01-S20) at 1920x1080. render.js renders the video
// from it (window.APP) and the checker samples it (window.CHECKS, checks/CONTRACT.md §Page), so both see the same frames.
//   seek(t)          draw the frame at t seconds (film time; frame f = t*30 of out/video.mp4)
//   freeze(t|null)   hold the 3D camera at its state of time t (H3 scenes have no camera: nothing to hold)
//   objects()        screen objects of the last seek, in paint order (engine.js REC)
//   layer(name, ids) redraw the current frame with only some objects: all | notext | text | glyph | graphics | only
// Scenes are built on demand (at most 3 kept; the rest disposed). Built with esbuild (build_page.mjs) -> build/film.js.
import './tok.js';
import timing from '../timing.json';
import anchors from '../anchors.json';
import * as E from './engine.js';
import * as s01 from './s01.js'; import * as s02 from './s02.js'; import * as s03 from './s03.js'; import * as s04 from './s04.js';
import * as s05 from './s05.js'; import * as s06 from './s06.js'; import * as s07 from './s07.js'; import * as s08 from './s08.js';
import * as s09 from './s09.js'; import * as s10 from './s10.js'; import * as s11 from './s11.js'; import * as s12 from './s12.js';
import * as s13 from './s13.js'; import * as s14 from './s14.js'; import * as s15 from './s15.js'; import * as s16 from './s16.js';
import * as s17 from './s17.js'; import * as s18 from './s18.js'; import * as s19 from './s19.js'; import * as s20 from './s20.js';

const MODS = { S01: s01, S02: s02, S03: s03, S04: s04, S05: s05, S06: s06, S07: s07, S08: s08, S09: s09, S10: s10,
  S11: s11, S12: s12, S13: s13, S14: s14, S15: s15, S16: s16, S17: s17, S18: s18, S19: s19, S20: s20 };
const FPS = E.TOK.canvas.fps, W = E.W, H = E.H, OW = E.OW, OH = E.OH;
const out = document.createElement('canvas'); out.width = OW; out.height = OH; out.id = 'film';
out.style.width = W + 'px'; out.style.height = H + 'px';
document.body.appendChild(out);
const raw = out.getContext('2d', { willReadFrequently: true });
const ctx = E.recorder(raw);
const SC = timing.scenes.map((s) => ({ id: s.id, f0: Math.round(s.start * FPS), f1: Math.round((s.start + s.dur) * FPS) }));
const FRAMES = SC[SC.length - 1].f1, TOTAL = FRAMES / FPS;

const built = new Map();
function get(id) {
  let s = built.get(id);
  if (s) { built.delete(id); built.set(id, s); return s; }
  s = E.makeScene(MODS[id], E.makeT(timing, anchors, id), ctx);
  built.set(id, s);
  while (built.size > 3) { const [k, v] = built.entries().next().value; v.dispose(); built.delete(k); }
  return s;
}
function locate(tg) {
  const gf = tg * FPS + 1e-6;
  const w = gf < SC[0].f0 ? SC[0] : SC.find((x) => gf < x.f1) || SC[SC.length - 1];
  return { w, t: Math.min(Math.max(0, tg - w.f0 / FPS), (w.f1 - w.f0 - 1) / FPS) };
}

let cur = 0, frozen = null, glKey = '', lastObjs = [];
function vignette() {
  const vg = ctx.createRadialGradient(W / 2, H / 2, H * 0.4, W / 2, H / 2, H * 0.98);
  vg.addColorStop(0, 'rgba(14,17,22,0)'); vg.addColorStop(1, 'rgba(14,17,22,0.5)'); ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
}
function draw(tg) {
  const { w, t } = locate(tg), s = get(w.id), R = E.REC;
  R.objs = []; R.seen = new Map(); R.stack = []; R.meta = []; R.scene = w.id; E.setCurT(t);
  raw.setTransform(1, 0, 0, 1, 0, 0); raw.globalAlpha = 1; raw.clearRect(0, 0, OW, OH);
  ctx.setTransform(OW / W, 0, 0, OH / H, 0, 0);
  const m = s.modeAt(t);
  E.obj({ role: 'bg', tag: 'rect', key: w.id + ':bg' }, () => { ctx.save(); ctx.fillStyle = E.C.bg; ctx.fillRect(0, 0, W, H); ctx.restore(); });
  if (m === '3d') {
    s.S.update(t);
    if (frozen !== null) { // freeze: the camera keeps its pose of time `frozen` (same scene, 3D), the objects move on
      const f = locate(frozen);
      if (f.w.id === w.id && s.modeAt(f.t) === '3d') { s.S.update(f.t); const p = s.pose(); s.S.update(t); s.setPose(p); }
    }
    s.camera.updateMatrixWorld();
    if (R.layer === 'all' || R.layer === 'notext') {
      const key = w.id + '|' + t + '|' + frozen;
      if (key !== glKey && !window.NO3D) { s.renderer.toneMappingExposure = s.exposure; s.renderer.render(s.scene, s.camera); glKey = key; }
      E.obj({ role: 'bg', tag: 'webgl', key: w.id + ':3d' }, () => ctx.drawImage(s.renderer.domElement, 0, 0, W, H));
      E.obj({ role: 'bg', tag: 'vignette', key: w.id + ':vignette' }, vignette);
    }
  }
  s.S.overlay(ctx, t, s.proj, m);
  if (R.layer === 'all') lastObjs = R.objs;
  return { w, t, s, m };
}
const OUTF = ['id', 'kind', 'tid', 'tag', 'role', 'text', 'box', 'opacity', 'level', 'emph', 'series', 'anchor', 'chart', 'year', 'char', 'case', 'runs', 'color',
  'fontPx', 'background', 'parent', 'claims', 'key', 'sig', 'panel', 'label', 'value', 'full', 'orient', 'shape', 'stroke', 'fill', 'curve', 'vertices', 'tier', 'sent'];
function clean(o) {
  const r = {};
  for (const k of OUTF) if (o[k] !== undefined) r[k] = o[k];
  if (r.kind === 'shape') { if (r.fill === undefined) r.fill = null; if (r.stroke === undefined) r.stroke = null; }
  r.sig = [r.kind, r.tag || '', r.role || '', r.text || '', (r.box || []).map((v) => Math.round(v)).join(','), r.fill || r.color || '', r.stroke || ''].join('|');
  return r;
}

const ready = (async () => {
  for (const wt of [400, 600, 700]) await document.fonts.load(`${wt} 48px Inter`);
  await document.fonts.ready;
  return true;
})();

window.CHECKS = {
  ready, fps: FPS, total: TOTAL, frames: FRAMES,
  seek(t) { cur = t; E.REC.layer = 'all'; E.REC.ids = null; draw(t); },
  freeze(t) { frozen = t === null || t === undefined ? null : t; },
  objects() { return lastObjs.filter((o) => o.box && o.box.every(Number.isFinite)).map(clean); },
  layer(name, ids) {
    E.REC.layer = name || 'all'; E.REC.ids = new Set(ids || []);
    draw(cur);
    if (E.REC.layer === 'all') E.REC.ids = null;
  },
};

// render.js / camera export
const b64 = (u8) => { let s = ''; const n = 0x8000; for (let i = 0; i < u8.length; i += n) s += String.fromCharCode.apply(null, u8.subarray(i, i + n)); return btoa(s); };
window.APP = {
  ready, fps: FPS, total: TOTAL, frames: FRAMES, scenes: SC,
  scene(id) { const s = get(id), w = SC.find((x) => x.id === id); return { f0: w.f0, f1: w.f1, N: w.f1 - w.f0, dur: s.T.dur, strip: s.S.stripTimes || null, hard: s.S.hardTime ?? null }; },
  frame(gf) { E.REC.layer = 'all'; cur = gf / FPS; const r = draw(cur); return [b64(new Uint8Array(raw.getImageData(0, 0, OW, OH).data.buffer)), r.m]; },
  frameRaw(gf) { E.REC.layer = 'all'; cur = gf / FPS; const r = draw(cur); return [raw.getImageData(0, 0, OW, OH).data, r.m]; },
  frameMode(gf) { E.REC.layer = 'all'; cur = gf / FPS; return draw(cur).m; },
  png(tg) { E.REC.layer = 'all'; cur = tg; draw(tg); return out.toDataURL('image/png'); },
  modeAt(tg) { const { w, t } = locate(tg); return get(w.id).modeAt(t); },
  // 3D camera of frame gf (null in H3 frames): position, look-at target, vertical fov (three.js units)
  camera(gf) {
    const { w, t } = locate(gf / FPS), s = get(w.id);
    if (s.modeAt(t) !== '3d') return null;
    s.S.update(t); const p = s.pose();
    return { scene: w.id, pos: p.pos, target: p.target, fovDeg: p.fov };
  },
  log(id) {
    const s = get(id);
    return { used: [...E.USED].sort(), texts: [...E.TEXTLOG.entries()].map(([k, e]) => ({ s: k, ...e })),
      anchorsUsed: [...E.ANCH_USED].sort(), anchorsDeclared: s.T.anchorIds, anchorsKeywordMissing: s.T.missing };
  },
  info() { const r = E.sharedRenderer(); const g = r.getContext(); const e = g.getExtension('WEBGL_debug_renderer_info'); return e ? g.getParameter(e.UNMASKED_RENDERER_WEBGL) : g.getParameter(g.RENDERER); },
};
