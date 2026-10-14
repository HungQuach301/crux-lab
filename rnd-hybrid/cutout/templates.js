// Factory symbols (episode custom_symbols mechanism of toolkit/factory/page.html) for the paper-cutout R&D clip.
//   cutout    a paper stage: era background, camera keys, characters (rig.js) with pose/expression/walk keys, props, stickers, coins
//   archival  a public-domain photo laid on the table: Ken Burns inside the print, channel tone (duotone + grain), year + source on frame;
//             when the file is not on disk yet → an honest placeholder card naming the exact record to download (never a fake photo)
// Every time in p is shot-local seconds (the clip builder resolves word anchors). Deterministic: no Math.random, no clock, no network.
import { drawCharacter, drawProp, POSES, walkPose, blendPose, PALETTE as P, hash } from './rig.js';
import { ease, easeOut, lin, clamp, mix } from '/toolkit/factory/lib/engine.js';

// ---- preload archival files listed in the clip manifest (await at import: page.html imports symbols before READY)
const IMG = {};
try {
  const man = await (await fetch('/rnd-hybrid/work/external/manifest.json')).json();
  for (const [id, url] of Object.entries(man)) { const im = new Image(); im.src = url; await im.decode(); IMG[id] = im; }
} catch (e) { /* no manifest → placeholders */ }

const backOut = (t, a, dur = 0.35) => { if (t < a) return 0; const x = clamp((t - a) / dur), c = 1.9; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
function key(t, keys) { // [[t, v], …] → eased value; v number or array
  if (!keys || !keys.length) return undefined; if (!Array.isArray(keys[0])) return keys;
  if (t <= keys[0][0]) return keys[0][1]; const last = keys[keys.length - 1]; if (t >= last[0]) return last[1];
  for (let i = 1; i < keys.length; i++) if (t < keys[i][0]) { const [a, va] = keys[i - 1], [b, vb] = keys[i], k = ease(t, a, b);
    return Array.isArray(va) ? va.map((v, j) => mix(v, vb[j], k)) : typeof va === 'number' ? mix(va, vb, k) : (k < 0.5 ? va : vb); }
}
const step = (t, keys, d) => { let v = d; for (const [a, x] of keys || []) if (t >= a) v = x; return v; };

let GRAIN = null;
function grain(ctx, W, H, a = 0.07) { // static paper grain (seeded), multiplied over the frame
  if (!GRAIN) { GRAIN = new OffscreenCanvas(256, 256); const g = GRAIN.getContext('2d'), im = g.createImageData(256, 256);
    for (let i = 0; i < 256 * 256; i++) { const v = 200 + hash(i * 7 + 3) * 55; im.data.set([v, v, v, 255], i * 4); } g.putImageData(im, 0, 0); }
  ctx.save(); ctx.globalAlpha = a; ctx.globalCompositeOperation = 'multiply'; ctx.fillStyle = ctx.createPattern(GRAIN, 'repeat'); ctx.fillRect(0, 0, W, H); ctx.restore();
}
function vignette(ctx, W, H, a = 0.55) { const g = ctx.createRadialGradient(W / 2, H * 0.48, H * 0.35, W / 2, H / 2, H * 1.05);
  g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(1, `rgba(0,0,0,${a})`); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); }

const ERA = { 1930: { sky: '#211C17', glow: '#3A2F24', floor: '#2E261E', line: '#4A3C2E' }, now: { sky: '#0E1116', glow: '#1C2433', floor: '#171B22', line: '#2A303B' } };

function sticker(E, s, t) { // rotated paper sticker with white cut border; pops with overshoot at s.at
  const k = backOut(t, s.at ?? 0); if (k <= 0) return; const ctx = E.ctx, fs = s.size || 64;
  ctx.save(); ctx.font = `700 ${fs}px Inter`; const w = ctx.measureText(s.text).width + fs * 0.9, h = fs * 1.5;
  ctx.translate(s.x, s.y); ctx.rotate((s.rot || 0) * Math.PI / 180); ctx.scale(k, k);
  ctx.fillStyle = P.shadow; E.round(-w / 2 + 6, -h / 2 + 8, w, h, 14); ctx.fill();
  ctx.fillStyle = '#FFFFFF'; E.round(-w / 2 - 8, -h / 2 - 8, w + 16, h + 16, 20); ctx.fill();
  ctx.fillStyle = s.bg || P.warn; E.round(-w / 2, -h / 2, w, h, 14); ctx.fill();
  ctx.fillStyle = s.fg || P.bg; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(s.text, 0, fs * 0.04);
  ctx.restore(); E.stickers = (E.stickers || 0) + 1;
}

export const cutout = { draw(E, t, p, d) {
  const ctx = E.ctx, W = E.W, H = E.H, era = ERA[p.era] || ERA[1930], gy = p.ground ?? 860;
  // background (not under the camera: the page stays, the paper moves)
  ctx.fillStyle = era.sky; ctx.fillRect(0, 0, W, H);
  const g = ctx.createRadialGradient(W * 0.5, H * 0.45, 40, W * 0.5, H * 0.45, W * 0.55); g.addColorStop(0, era.glow); g.addColorStop(1, era.sky);
  ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  const cam = key(t, p.cam) || [W / 2, H / 2, 1];
  ctx.save(); ctx.translate(W / 2, H / 2); ctx.scale(cam[2], cam[2]); ctx.translate(-cam[0], -cam[1]);
  ctx.fillStyle = era.floor; ctx.fillRect(-2000, gy, W + 4000, 1200); ctx.fillStyle = era.line; ctx.fillRect(-2000, gy, W + 4000, 6);
  let people = false;
  for (const it of p.items || []) {
    const a0 = it.at ?? -1; if (t < a0) continue;
    const pos = key(t, it.move) || [it.x, it.y]; const pk = it.pop === false ? 1 : backOut(t, a0, it.popDur ?? 0.35);
    const alpha = it.out != null ? 1 - lin(t, it.out, it.out + 0.25) : 1; if (alpha <= 0) continue;
    if (it.kind === 'char') { people = true;
      let pose = POSES[step(t, it.poses, it.pose || 'stand')];
      const ch = (it.poses || []).filter(([a]) => a <= t).pop(); if (ch) { const prev = (it.poses || []).filter(([a]) => a < ch[0]).pop(); const from = POSES[prev ? prev[1] : it.pose || 'stand']; pose = blendPose(from, pose, ease(t, ch[0], ch[0] + 0.22)); }
      if (it.walk && t >= it.walk[0] && t < it.walk[1]) pose = blendPose(walkPose(t - it.walk[0]), pose, ease(t, it.walk[1] - 0.25, it.walk[1]));
      if (it.bob) pose = { ...pose, bob: Math.abs(Math.sin(t * it.bob * Math.PI)) * 10 };
      const seed = hash(it.id.length * 13 + Math.round(it.x)) * 3, blink = ((t + seed) % 3.4) < 0.11;
      drawCharacter(ctx, { id: it.id, x: pos[0], y: pos[1] + (1 - pk) * 30, s: (it.s || 1) * (0.92 + 0.08 * pk), flip: it.flip, pose, expr: step(t, it.exprs, it.expr || 'neutral'), blink, alpha: alpha * clamp(pk * 2) });
    } else if (it.kind === 'prop') {
      drawProp(ctx, it.id, { x: pos[0], y: pos[1], s: (it.s || 1) * pk, rot: key(t, it.rot) ?? 0, alpha, doors: key(t, it.doors) ?? 0, label: it.label });
      if (it.stamp && t >= it.stamp.at) sticker(E, { ...it.stamp, x: pos[0] + (it.stamp.dx || 0), y: pos[1] + (it.stamp.dy || -180) }, t);
    } else if (it.kind === 'queue') { people = true;
      for (let i = 0; i < it.n; i++) { const ai = a0 + i * (it.every ?? 0.08), k = backOut(t, ai); if (k <= 0) continue;
        const sway = Math.sin(t * 2.1 + i * 1.7) * 3; drawProp(ctx, 'person', { x: pos[0] + i * (it.gap || 74) + sway, y: pos[1] + (1 - k) * 40, s: (it.s || 1) * (0.85 + 0.15 * hash(i + 5)), alpha }); }
    } else if (it.kind === 'coins') {
      for (let i = 0; i < it.n; i++) { const ai = a0 + i * (it.every || 0.25); if (t < ai) continue; const f = easeOut(t, ai, ai + 0.35);
        drawProp(ctx, 'coin', { x: pos[0] + (i % (it.cols || 1)) * 64, y: mix(pos[1] - 260, pos[1] - Math.floor(i / (it.cols || 1)) * 14, f), s: it.s || 1, alpha }); }
    } else if (it.kind === 'build') { // house assembles piece by piece: equity paid in, one piece a month (illustrative)
      const k = lin(t, it.from, it.to); drawProp(ctx, 'house', { x: pos[0], y: pos[1], s: it.s || 1, alpha: 0.18 });
      ctx.save(); ctx.beginPath(); ctx.rect(pos[0] - 400, pos[1] - 470 * (it.s || 1) * k, 800, 470 * (it.s || 1) * k + 20); ctx.clip();
      drawProp(ctx, 'house', { x: pos[0], y: pos[1], s: it.s || 1 }); ctx.restore();
    } else if (it.kind === 'sticker') sticker(E, { ...it, x: pos[0], y: pos[1] }, t);
  }
  ctx.restore();
  for (const s of p.hud || []) sticker(E, s, t); // screen-fixed stickers
  grain(ctx, W, H); vignette(ctx, W, H, 0.45);
  if (p.year) E.text(p.year, E.SAFE.x0 + 10, E.SAFE.y0 + 70, 'head', { color: P.bg, plate: P.warn, alpha: fade(t, p.yearAt ?? 0), group: 'year' });
  if (p.caption) E.text(p.caption, W / 2, E.SAFE.y1 - 70, 'caption', { align: 'center', plate: P.surface, alpha: fade(t, p.captionAt ?? 0.2), group: 'cap' });
  if (people) E.illustrative();
} };
const fade = (t, a) => ease(t, a, a + 0.3);

export const archival = { draw(E, t, p, d) {
  const ctx = E.ctx, W = E.W, H = E.H;
  ctx.fillStyle = '#16130F'; ctx.fillRect(0, 0, W, H); // the table
  const camz = mix(1.0, 1.06, ease(t, 0, d)); // camera push over the whole print
  ctx.save(); ctx.translate(W / 2, H / 2); ctx.scale(camz, camz); ctx.rotate(-0.012); ctx.translate(-W / 2, -H / 2);
  const pw = 1380, ph = 860, px = (W - pw) / 2, py = (H - ph) / 2 - 30;
  ctx.fillStyle = 'rgba(0,0,0,0.5)'; ctx.fillRect(px + 14, py + 18, pw, ph);
  ctx.fillStyle = '#E9E4D8'; ctx.fillRect(px - 26, py - 26, pw + 52, ph + 52); // white print border
  ctx.save(); ctx.beginPath(); ctx.rect(px, py, pw, ph); ctx.clip();
  const im = IMG[p.slot];
  if (im) { // Ken Burns inside the print: focus point keys [cx, cy, zoom] in image fractions
    const kb = key(t / d, p.kb || [[0, [0.5, 0.5, 1.0]], [1, [0.5, 0.45, 1.12]]]);
    const sc = Math.max(pw / im.width, ph / im.height) * kb[2], iw = im.width * sc, ih = im.height * sc;
    const ix = clamp(px + pw / 2 - kb[0] * iw, px + pw - iw, px), iy = clamp(py + ph / 2 - kb[1] * ih, py + ph - ih, py);
    ctx.filter = 'grayscale(1) contrast(1.12) brightness(0.98)'; ctx.drawImage(im, ix, iy, iw, ih); ctx.filter = 'none';
    ctx.globalCompositeOperation = 'multiply'; ctx.fillStyle = '#C9B48F'; ctx.fillRect(px, py, pw, ph); // warm paper tone of the 1930 era
    ctx.globalCompositeOperation = 'screen'; ctx.fillStyle = 'rgba(14,17,22,0.35)'; ctx.fillRect(px, py, pw, ph);
    ctx.globalCompositeOperation = 'source-over';
  } else { // placeholder: never a fake photo — names the record the owner must download
    const g = ctx.createLinearGradient(px, py, px + pw, py + ph); g.addColorStop(0, '#3B342B'); g.addColorStop(1, '#241F19');
    ctx.fillStyle = g; ctx.fillRect(px, py, pw, ph); E.hatch(px, py, pw, ph, 0.18, '#6B5E4C', 28);
    ctx.fillStyle = '#E9E4D8'; ctx.textAlign = 'center'; ctx.font = '700 64px Inter'; ctx.fillText('ARCHIVAL PHOTO SLOT', W / 2, py + ph / 2 - 70);
    ctx.font = '600 46px Inter'; ctx.fillText(p.subject || '', W / 2, py + ph / 2 + 10);
    ctx.fillStyle = '#B9AE96'; ctx.font = '400 40px Inter'; ctx.fillText(`file pending: ${p.record || p.slot}`, W / 2, py + ph / 2 + 80);
  }
  grain(ctx, W, H, 0.1); ctx.restore(); ctx.restore(); vignette(ctx, W, H, 0.6);
  if (p.year) E.text(p.year, E.SAFE.x0 + 10, E.SAFE.y0 + 70, 'head', { color: P.bg, plate: P.warn, group: 'year' });
  if (p.source) E.text(p.source, E.SAFE.x1, E.SAFE.y1 - 6, 'note', { align: 'right', color: P.ink, plate: P.surface, group: 'src' });
  if (p.caption) E.text(p.caption, E.SAFE.x0 + 10, E.SAFE.y1 - 6, 'note', { color: P.ink, plate: P.surface, group: 'cap' });
} };

export default cutout;
