// Tập 2 · C5 film page: ONE page draws any frame of the whole episode (S01-S13) at 1920x1080. render_c5.js renders the video
// from it (window.APP) and the checker samples it (window.CHECKS, checks/CONTRACT.md §Page), so both see the same frames.
//   seek(t)          draw the frame at t seconds (film time; frame f = t*30 of out/video.mp4)
//   freeze(t|null)   2.5D camera: there is none (every frame is a still camera; out/camera.json is static), so nothing to hold
//   objects()        screen objects of the last seek, in paint order (rec.js ops -> objects)
//   layer(name, ids) redraw the current frame keeping only some ops: all | notext | text | glyph | graphics | only
// Same scene code as the C4 animatic (film.js/lib.js/sNN.js + the signed engines and clips), drawn at scale 1 instead of 2/3.
import './globals_c5.js';
import timing from '../timing.json';
import anchors from '../anchors.json';
import claimsFile from '../../out/claims.json';
import * as F from './film.js';
import * as s01 from './s01.js'; import * as s02 from './s02.js'; import * as s03 from './s03.js'; import * as s04 from './s04.js';
import * as s05 from './s05.js'; import * as s06 from './s06.js'; import * as s07 from './s07.js'; import * as s08 from './s08.js';
import * as s09 from './s09.js'; import * as s10 from './s10.js'; import * as s11 from './s11.js'; import * as s12 from './s12.js';
import * as s13 from './s13.js';
const { REC, H2, H3, C } = F;
const MODS = { S01: s01, S02: s02, S03: s03, S04: s04, S05: s05, S06: s06, S07: s07, S08: s08, S09: s09, S10: s10, S11: s11, S12: s12, S13: s13 };
const FPS = 30, W = 1920, H = 1080;
const cv = document.createElement('canvas'); cv.width = W; cv.height = H; cv.id = 'film'; document.body.appendChild(cv);
const raw = cv.getContext('2d', { willReadFrequently: true });
import { recorder } from './rec.js';
const rc = recorder(raw);
REC.on = true;
const jr = (x) => Math.floor(x + 0.5);
const SC = timing.scenes.map((s) => ({ id: s.id, f0: jr(s.start * FPS), f1: jr((s.start + s.dur) * FPS) }));
const FRAMES = SC[SC.length - 1].f1;

// ---- claims: spans of claim displays (or their number tokens) in each drawn string ----
const CLAIMS = Object.fromEntries(claimsFile.claims.map((c) => [c.claimId, c]));
const NUMRX = /\d+(?:,\d{3})*(?:\.\d+)?/g;
const TOKEN_OWNERS = {}; // number token -> claim ids whose display carries it (fallback attribution, as the C4 token check)
for (const c of claimsFile.claims) for (const k of String(c.display).match(NUMRX) || []) (TOKEN_OWNERS[k] ||= []).push(c.claimId);
let frameClaims = new Set(), buildClaims = new Map(), curScene = '';
const boundary = (s, i, len) => { const pre = s[i - 1] || ' ', post = s[i + len] || ' '; return !/[\d.,$]/.test(pre) && !/\d/.test(post) && !(post === '.' && /\d/.test(s[i + len + 1] || '')); };
function findAt(s, sub, used) { let i = -1, from = 0; while ((i = s.indexOf(sub, from)) >= 0) { if (boundary(s, i, sub.length) && !used.some(([a, b]) => i < b && i + sub.length > a)) return i; from = i + 1; } return -1; }
REC.claimsOf = (s) => {
  if (!/\d/.test(s)) return [];
  const ids = [...new Set([...H2.USED, ...H3.USED, ...frameClaims, ...(buildClaims.get(curScene) || [])])];
  const used = [], out = [];
  // whole displays first (longest first), then number tokens of the claims this frame took, then any claim carrying the token
  for (const id of ids.sort((a, b) => String(CLAIMS[b]?.display || '').length - String(CLAIMS[a]?.display || '').length)) {
    const d = String(CLAIMS[id]?.display ?? ''); if (!d || !/\d/.test(d)) continue;
    const i = findAt(s, d, used); if (i >= 0) { used.push([i, i + d.length]); out.push([id, i, d]); }
  }
  for (const m of s.matchAll(NUMRX)) {
    const k = m[0], i = m.index; if (used.some(([a, b]) => i < b && i + k.length > a) || !boundary(s, i, k.length)) continue;
    const own = (TOKEN_OWNERS[k] || []); const id = own.find((x) => ids.includes(x)) || own[0];
    if (id) { used.push([i, i + k.length]); out.push([id, i, k]); }
  }
  return out;
};

// ---- scenes ----
const built = {};
for (const s of timing.scenes) {
  H2.USED.clear(); H3.USED.clear(); curScene = s.id;
  built[s.id] = MODS[s.id].build({ T: F.makeT(timing, anchors, s.id) });
  buildClaims.set(s.id, new Set([...H2.USED, ...H3.USED]));
}
function locate(tg) {
  const gf = tg * FPS + 1e-6;
  const w = SC.find((x) => gf < x.f1) || SC[SC.length - 1];
  return { w, t: Math.min(Math.max(0, tg - w.f0 / FPS), (w.f1 - w.f0 - 1) / FPS) };
}
let cur = 0, lastOps = [], lastScene = '', layerName = 'all';
function drawAt(tg, keep, transparent) {
  const { w, t } = locate(tg);
  curScene = w.id; H2.USED.clear(); H3.USED.clear(); frameClaims = new Set();
  REC.ops = []; REC.n = 0; REC.keep = keep; REC.meta = [];
  H2.FRAME_TEXTS.length = 0; H3.resetFrame();
  raw.setTransform(1, 0, 0, 1, 0, 0); raw.globalAlpha = 1; raw.clearRect(0, 0, W, H);
  if (!transparent) { raw.fillStyle = C.bg; raw.fillRect(0, 0, W, H); }
  built[w.id].draw(rc, t);
  raw.setTransform(1, 0, 0, 1, 0, 0); raw.globalAlpha = 1;
  if (!keep) { lastOps = REC.ops; lastScene = w.id; }
  REC.keep = null;
}
// ---- objects from the ops of the last full frame ----
const BG = C.bg.toLowerCase();
const full = (b) => b[0] <= 0.5 && b[1] <= 0.5 && b[2] >= W - 0.5 && b[3] >= H - 0.5;
let lastObjs = [], kindOf = [];
function buildObjects() {
  const ops = lastOps, objs = [], seen = new Map();
  kindOf = new Array(ops.length).fill('shape');
  // dips: a full-frame bg fill painted with alpha a dims everything drawn before it by (1 - a)
  const dim = new Array(ops.length).fill(1);
  ops.forEach((o, j) => { if (o.op !== 'glyph' && full(o.box) && o.color === BG && o.alpha < 0.999) for (let k = 0; k < j; k++) dim[k] *= (1 - o.alpha); });
  const pillOf = new Map();
  ops.forEach((o, j) => { if (o.op === 'glyph' && o.text === 'ILLUSTRATIVE' && j > 0) { const p = ops[j - 1]; if (p.op === 'fill' && p.box[0] <= o.box[0] && p.box[2] >= o.box[2] && p.box[1] <= o.box[1] && p.box[3] >= o.box[3]) { pillOf.set(j - 1, j); kindOf[j - 1] = 'pill'; } } });
  const keyOf = (base) => { const k = seen.get(base) || 0; seen.set(base, k + 1); return k ? base + '#' + k : base; };
  ops.forEach((o, j) => {
    if (o.alpha <= 0.001) return;
    if (o.op === 'glyph') {
      kindOf[j] = 'glyph';
      const id = keyOf(lastScene + ':t:' + o.text), op = +(o.alpha * dim[j]).toFixed(3);
      const pj = [...pillOf.entries()].find(([, g]) => g === j);
      const pill = pj ? ops[pj[0]] : null;
      objs.push({ id, kind: 'text', tid: id, key: id, sig: id + '|' + o.box.map((v) => v.toFixed(1)).join(','), role: o.text === 'ILLUSTRATIVE' ? 'badge' : 'label',
        text: o.text, box: pill ? pill.box.map((v) => +v.toFixed(1)) : o.box.map((v) => +v.toFixed(1)), opacity: op, level: null, emph: false, series: null, anchor: null, chart: null, year: null, char: null,
        runs: [{ color: o.color, size: o.fontPx }], color: o.color, fontPx: o.fontPx, background: pill ? pill.color : null, parent: null, case: o.meta?.case ?? null,
        claims: o.spans.map((sp) => ({ id: sp.id, text: sp.text, box: sp.box.map((v) => +v.toFixed(1)), opacity: op, color: o.color, series: null, roll: false })) });
      return;
    }
    if (kindOf[j] === 'pill') return;
    const role = j === 0 && full(o.box) ? 'bg' : full(o.box) && o.color === BG ? 'bg' : o.color === BG ? 'card' : 'mark';
    const fillish = o.op === 'fill' || o.op === 'fillRect';
    const base = lastScene + ':' + role + ':' + o.op + ':' + o.color;
    const id = keyOf(base);
    objs.push({ id, kind: 'shape', key: id, sig: id + '|' + o.box.map((v) => v.toFixed(1)).join(','), tag: o.op === 'fillRect' || o.op === 'strokeRect' ? 'rect' : 'path', role,
      panel: null, chart: null, label: null, series: null, value: null, full: null, orient: null, char: null, shape: null, year: null, case: o.meta?.case ?? null,
      stroke: fillish ? null : o.color, fill: fillish ? o.color : null, opacity: +(o.alpha * dim[j]).toFixed(3), box: o.box.map((v) => +v.toFixed(1)), curve: false, vertices: o.verts });
    kindOf[j] = role === 'bg' ? 'bg' : role === 'card' ? 'card' : 'shape';
  });
  lastObjs = objs;
}
function seek(t) { cur = t; drawAt(t, null, false); buildObjects(); layerName = 'all'; }
function layer(name, ids) {
  layerName = name;
  if (name === 'all') { drawAt(cur, null, false); return; }
  const idset = new Set(ids || []);
  // op index -> object id (text: glyph op; badge pill belongs to its text)
  const objAt = []; let k = 0; const ops = lastOps;
  ops.forEach((o, j) => { if (o.alpha <= 0.001) { objAt[j] = null; return; } if (kindOf[j] === 'pill') { objAt[j] = 'pill'; return; } objAt[j] = lastObjs[k++]?.id; });
  ops.forEach((o, j) => { if (objAt[j] === 'pill') { const g = j + 1; objAt[j] = 'pill:' + g; } });
  const textIdOfPill = (j) => objAt[j + 1];
  const keep = (j) => {
    const kd = kindOf[j];
    switch (name) {
      case 'notext': return kd !== 'glyph' && kd !== 'pill';
      case 'text': return kd === 'glyph' || kd === 'pill';
      case 'glyph': return kd === 'glyph';
      case 'graphics': return kd === 'shape';
      case 'only': return kd === 'pill' ? idset.has(textIdOfPill(j)) : (kd === 'glyph' || kd === 'shape' || kd === 'card') && idset.has(objAt[j]);
      default: return true;
    }
  };
  drawAt(cur, keep, name !== 'notext');
}
window.CHECKS = {
  ready: document.fonts.ready.then(() => true),
  seek: (t) => { seek(t); return true; },
  freeze: () => true,
  objects: () => lastObjs,
  layer: (name, ids) => { layer(name, ids); return true; },
  total: FRAMES / FPS,
};
const b64 = (u8) => { let s = ''; const n = 0x8000; for (let i = 0; i < u8.length; i += n) s += String.fromCharCode.apply(null, u8.subarray(i, i + n)); return btoa(s); };
window.APP = {
  scenes: SC, frames: FRAMES,
  frame(f) { drawAt(f / FPS, null, false); return b64(new Uint8Array(raw.getImageData(0, 0, W, H).data.buffer)); },
  png(t) { seek(t); return cv.toDataURL('image/png'); },
  objects(t) { seek(t); return lastObjs; },
};
window.READY = true;
