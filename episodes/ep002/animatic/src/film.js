// Tập 2 · C4 animatic layer over the SIGNED C3 final system (episodes/ep002/design/c3/final): no new drawing style here.
// - H2 = design/c3/final/src/engine.js (+ k1/k2/k4/k7 clips), H3 = design/c3/final/src/h3/engine.js (+ scenes.js K3/K5/K6).
//   Both engines are imported as they are (page.html gives each its own window.DATA before import); the signed clips are
//   imported unchanged and played through a TIME WARP: clip keyframes are pinned to anchors (sentence + keyword), so the
//   signed motion runs exactly as signed, only slower/faster and held, in step with the narration.
// - Timing pattern from episodes/ep001/animatic/src/engine.js (makeT: T.a(id) -> anchors.json -> timing.json).
// - One text log/mask/self-check over BOTH engines (their own per-frame text lists), so every string on screen is checked.
import * as H2 from '../../design/c3/final/src/engine.js';
import * as H3 from '../../design/c3/final/src/h3/engine.js';
export { H2, H3 };
export const C = H2.C, W = 1920, H = 1080, OW = 1280, OH = 720, S = OW / W;
export const { clamp, lin, smooth, ease, easeOut, mix, inout } = H2;
export const TOK = H2.TOK;
const SAFE = TOK.canvas.safe; // px at 1080: x 96, top 64, bottom 40

// ---------- claims ----------
export const CL = (id) => H2.CL(id);
// a part of a claim's display (e.g. "10 years" of term = "10 years (120 monthly payments)")
export function CLS(id, sub) { const d = H2.CL(id); if (!d.includes(sub)) throw new Error(`CLS: "${sub}" not in ${id} "${d}"`); return sub; }
export const usedClaims = () => [...new Set([...H2.USED, ...H3.USED])].sort();

// ---------- timing ----------
const norm = (s) => s.toLowerCase().replace(/’/g, "'").replace(/[^a-z0-9']+/g, ' ').trim().split(/\s+/).filter(Boolean);
export const ANCH_USED = new Set();
export function makeT(timing, anchors, sid) {
  const sc = timing.scenes.find((x) => x.id === sid); if (!sc) throw new Error('no scene ' + sid);
  const byId = new Map(sc.sentences.map((x) => [x.id, x]));
  const mine = new Map(anchors.anchors.filter((x) => x.scene === sid).map((x) => [x.id, x]));
  const sent = (id) => { const x = byId.get(id.includes('.') ? id : sid + '.' + id); if (!x) throw new Error(sid + ' no sentence ' + id); return x; };
  const T = {
    id: sid, dur: sc.dur, start: sc.start, sentences: sc.sentences, missing: [], anchorIds: [...mine.keys()],
    s: (id) => sent(id).start - sc.start,
    e: (id) => sent(id).end - sc.start,
    a(id) {
      const A = mine.get(id); if (!A) throw new Error(sid + ' no anchor ' + id);
      ANCH_USED.add(id);
      const x = sent(A.sentence); let t;
      if (A.at === 'start') t = x.start; else if (A.at === 'end') t = x.end;
      else {
        const k = norm(A.at), w = x.words.map((y) => y.t); let hit = -1;
        for (let i = 0; i + k.length <= w.length && hit < 0; i++) if (k.every((q, j) => w[i + j] === q)) hit = i;
        if (hit >= 0) t = x.words[hit].start;
        else { const i = x.text.toLowerCase().indexOf(A.at.toLowerCase()); t = i < 0 ? x.start : x.start + (x.end - x.start) * i / x.text.length; if (i < 0 && !T.missing.includes(id)) T.missing.push(id); }
      }
      return Math.max(0, Math.min(sc.dur, t - sc.start + (A.dt || 0)));
    },
  };
  return T;
}
// time warp: keys = [[clipTime, sceneTime], ...] (sceneTime from T.a / T.s / T.e). Piecewise linear, monotone, held at both ends.
export function warp(keys) {
  const k = keys.map(([c, s]) => [c, s]).sort((a, b) => a[1] - b[1]);
  for (let i = 1; i < k.length; i++) if (k[i][0] < k[i - 1][0]) throw new Error('warp: clip time goes back at key ' + i + ' ' + JSON.stringify(k));
  return (t) => {
    if (t <= k[0][1]) return k[0][0];
    for (let i = 0; i < k.length - 1; i++) if (t <= k[i + 1][1]) { const d = k[i + 1][1] - k[i][1]; return d <= 1e-6 ? k[i + 1][0] : mix(k[i][0], k[i + 1][0], (t - k[i][1]) / d); }
    return k[k.length - 1][0];
  };
}
// a dip to background between two shots (cut at tc): returns the overlay alpha
export const dipA = (t, tc, h = 0.22) => Math.max(0, 1 - Math.abs(t - tc) / h);
export function dip(ctx, t, tc, h = 0.22) { const a = dipA(t, tc, h); if (a > 0.001) { ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = C.bg; ctx.fillRect(-10, -10, W + 20, H + 20); ctx.restore(); } }
// shots: [[t0, drawFn(ctx, t)], ...] ; draws the shot whose [t0, next t0) holds t, with a dip at each cut
export function shots(ctx, t, list) {
  let j = 0; for (let i = 0; i < list.length; i++) if (t >= list[i][0]) j = i;
  // during the first half of a dip keep the previous shot so the cut is hidden under the dip
  if (j > 0 && t < list[j][0] + 0.001) j -= 1;
  list[j][1](ctx, t);
  for (let i = 1; i < list.length; i++) dip(ctx, t, list[i][0]);
}

// ---------- unified per-frame text list (both engines) ----------
export function frameTexts() {
  const out = [];
  for (const x of H2.FRAME_TEXTS) out.push({ s: x.s, px: x.px, color: x.color, alpha: x.alpha, box: x.box, plate: x.bgFill || null, plateBox: x.pill, group: null, eng: 'H2' });
  for (const b of H3.BOXES) out.push({ s: b.s, px: b.px, color: b.color, alpha: b.alpha, box: [b.gx0 * S, b.gy0 * S, (b.gx1 - b.gx0) * S, (b.gy1 - b.gy0) * S], plate: b.plate,
    plateBox: b.plate ? [b.x0 * S, b.y0 * S, (b.x1 - b.x0) * S, (b.y1 - b.y0) * S] : null, group: b.group, eng: 'H3' });
  return out;
}
const outOfSafe = (b) => b[0] < SAFE.x * S - 0.5 || b[0] + b[2] > OW - SAFE.x * S + 0.5 || b[1] < SAFE.top * S - 0.5 || b[1] + b[3] > OH - SAFE.bottom * S + 0.5;

// ---------- boot ----------
export function boot(scene, T, claimsMeta) {
  const out = document.createElement('canvas'); out.width = OW; out.height = OH; document.body.appendChild(out);
  const ctx = out.getContext('2d', { willReadFrequently: true });
  const TEXTLOG = new Map();
  let cur = 0;
  function draw(t, flags = {}) {
    cur = t;
    H2.FLAGS.mask = !!flags.mask; H2.FLAGS.notext = !!flags.notext; H3.FLAGS.MASK = !!flags.mask; H3.FLAGS.NOTEXT = !!flags.notext;
    H2.FRAME_TEXTS.length = 0; H3.resetFrame();
    ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.globalAlpha = 1; ctx.fillStyle = C.bg; ctx.fillRect(0, 0, OW, OH);
    ctx.setTransform(S, 0, 0, S, 0, 0);
    scene.draw(ctx, t);
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    H2.FLAGS.mask = H2.FLAGS.notext = H3.FLAGS.MASK = H3.FLAGS.NOTEXT = false;
    if (!flags.mask && !flags.notext) for (const x of frameTexts()) if (x.alpha >= 0.2) {
      const e = TEXTLOG.get(x.s) || { s: x.s, px: x.px, n: 0, out: 0, firstT: +t.toFixed(2), color: x.color };
      e.n++; if (outOfSafe(x.box)) e.out++; TEXTLOG.set(x.s, e);
    }
  }
  const b64 = (u8) => { let s = ''; const n = 0x8000; for (let i = 0; i < u8.length; i += n) s += String.fromCharCode.apply(null, u8.subarray(i, i + n)); return btoa(s); };
  const lum = (r, g, b) => { const f = (c) => { c /= 255; return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const hexl = (h) => { const n = parseInt(h.slice(1), 16); return lum(n >> 16, (n >> 8) & 255, n & 255); };
  // self-check of one frame (px at 720p): text -> nearest graphic pixel (R = 14), text -> text, contrast of the text colour
  // against its plate or the median of the graphics under its glyph box; plus the ILLUSTRATIVE rule
  function check(t) {
    draw(t); const all = frameTexts(); const texts = all.filter((x) => x.alpha >= 0.98);
    draw(t, { notext: true });
    const img = ctx.getImageData(0, 0, OW, OH).data, bg = [14, 17, 22], res = [];
    for (const tx of texts) {
      const [bx, by, bw, bh] = tx.plateBox || tx.box, R = 14; let dmin = 99; const under = [];
      for (let y = Math.max(0, Math.floor(by - R)); y < Math.min(OH, Math.ceil(by + bh + R)); y++) for (let x = Math.max(0, Math.floor(bx - R)); x < Math.min(OW, Math.ceil(bx + bw + R)); x++) {
        const i = (y * OW + x) * 4, d = Math.abs(img[i] - bg[0]) + Math.abs(img[i + 1] - bg[1]) + Math.abs(img[i + 2] - bg[2]);
        const inG = x >= tx.box[0] && x < tx.box[0] + tx.box[2] && y >= tx.box[1] && y < tx.box[1] + tx.box[3];
        if (inG) under.push(lum(img[i], img[i + 1], img[i + 2]));
        if (d <= 30) continue;
        const dx = Math.max(bx - x - 1, 0, x - (bx + bw)), dy = Math.max(by - y - 1, 0, y - (by + bh)); const dd = Math.hypot(dx, dy); if (dd < dmin) dmin = dd;
      }
      under.sort((a, b) => a - b);
      const Lb = tx.plate ? hexl(tx.plate) : (under.length ? under[Math.floor(under.length / 2)] : hexl(C.bg)), Lt = hexl(tx.color);
      let dtext = 99;
      for (const o of texts) { if (o === tx || (tx.group && o.group === tx.group)) continue; const [ox, oy, ow, oh] = o.box, [qx, qy, qw, qh] = tx.box;
        dtext = Math.min(dtext, Math.hypot(Math.max(ox - (qx + qw), 0, qx - (ox + ow)), Math.max(oy - (qy + qh), 0, qy - (oy + oh)))); }
      res.push({ s: tx.s, px: tx.px, dGraphic: +dmin.toFixed(1), dText: +dtext.toFixed(1), contrast: +((Math.max(Lt, Lb) + 0.05) / (Math.min(Lt, Lb) + 0.05)).toFixed(2) });
    }
    // ILLUSTRATIVE rule: a number token that belongs only to illustrative claims needs the badge in the same frame
    const vis = all.filter((x) => x.alpha >= 0.5).map((x) => x.s), hasBadge = vis.includes('ILLUSTRATIVE');
    const need = vis.filter((s) => (s.match(/\d+(?:,\d{3})*(?:\.\d+)?/g) || []).some((k) => claimsMeta.illusOnly.includes(k)));
    return { t, res, badgeMissing: !hasBadge && need.length ? need : null };
  }
  function texts(t) { draw(t); return frameTexts().filter((x) => x.alpha >= 0.2).map((x) => ({ s: x.s, px: x.px, box: x.box.map((v) => +v.toFixed(1)) })); }
  return {
    dur: T.dur, frames: Math.round(T.dur * 30), stripTimes: scene.stripTimes,
    frame(t) { draw(t); return b64(new Uint8Array(ctx.getImageData(0, 0, OW, OH).data.buffer)); },
    png(t, mask) { draw(t, { mask }); return out.toDataURL('image/png'); },
    texts, check,
    log: () => ({ claimsUsed: usedClaims(), texts: [...TEXTLOG.values()], anchorsUsed: [...ANCH_USED], anchorsDeclared: T.anchorIds, anchorsKeywordMissing: T.missing }),
  };
}
// keys that keep a signed clip's quick move (a card flip, a jump) at its signed speed around an anchored moment
export const around = (c, s, h = 0.2) => [[c - h, s - h], [c, s], [c + h, s + h]];
