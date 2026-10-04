// C5 recording proxy of the 2D canvas context (pattern: episodes/ep001/animatic/src/engine.js REC/recorder, adapted).
// The signed engines (H2, H3) and the scenes draw unchanged through this proxy; every paint op (fill, stroke, fillRect,
// strokeRect, fillText) gets a sequence number, its device-space box, colour and opacity. From the ops of one frame the
// film page builds the screen objects of the checks contract (checks/CONTRACT.md §Page: CHECKS.objects()) and redraws the
// same frame keeping only some ops for the layer masks (CHECKS.layer). Draws are pure functions of t, so op i of a redraw is
// op i of the recorded frame. REC.on = false (C4 animatic pages) -> the proxy is not used at all.
export const REC = { on: false, ops: [], n: 0, keep: null, meta: [], claimsOf: null };
// meta for every op drawn inside fn (e.g. {case: 'period-1954-1980'}): S06 coverage
export function withMeta(m, fn) { REC.meta.push(m); try { return fn(); } finally { REC.meta.pop(); } }

export function hex(c) {
  if (typeof c !== 'string') return { hex: 'url(gradient)', a: 1 };
  if (c[0] === '#') { const h = c.length === 4 ? '#' + [...c.slice(1)].map((x) => x + x).join('') : c.slice(0, 7); return { hex: h.toLowerCase(), a: 1 }; }
  const m = c.match(/rgba?\(([^)]+)\)/);
  if (!m) return { hex: c, a: 1 };
  const p = m[1].split(',').map((x) => parseFloat(x));
  return { hex: '#' + p.slice(0, 3).map((v) => Math.round(v).toString(16).padStart(2, '0')).join(''), a: p.length > 3 ? p[3] : 1 };
}
function tbox(ctx, pts) {
  const m = ctx.getTransform(); let l = 1e9, t = 1e9, r = -1e9, b = -1e9;
  for (const [x, y] of pts) { const X = m.a * x + m.c * y + m.e, Y = m.b * x + m.d * y + m.f; if (X < l) l = X; if (X > r) r = X; if (Y < t) t = Y; if (Y > b) b = Y; }
  return [l, t, r, b];
}
const uni = (a, b) => (a ? [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])] : b.slice());

export function recorder(raw) {
  let P = null, nv = 0;
  const add = (pts) => { P = uni(P, tbox(raw, pts)); nv += pts.length; };
  function paint(op, box, style, draw, extra) {
    const i = REC.n++;
    if (!REC.keep) {
      const c = hex(style);
      REC.ops.push({ i, op, box, color: c.hex, alpha: raw.globalAlpha * c.a, verts: nv, meta: REC.meta.length ? Object.assign({}, ...REC.meta) : null, ...(extra ? extra() : {}) });
      return draw();
    }
    if (REC.keep(i)) draw();
  }
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
    fill(...a) { paint('fill', P || [0, 0, 0, 0], raw.fillStyle, () => raw.fill(...a)); },
    stroke(...a) { const m = raw.getTransform(), lw = raw.lineWidth / 2 * Math.hypot(m.a, m.b); const b = P ? [P[0] - lw, P[1] - lw, P[2] + lw, P[3] + lw] : [0, 0, 0, 0];
      paint('stroke', b, raw.strokeStyle, () => raw.stroke(...a)); },
    fillRect(x, y, w, h) { paint('fillRect', tbox(raw, [[x, y], [x + w, y + h], [x, y + h], [x + w, y]]), raw.fillStyle, () => raw.fillRect(x, y, w, h)); },
    strokeRect(x, y, w, h) { const lw = raw.lineWidth / 2; paint('strokeRect', tbox(raw, [[x - lw, y - lw], [x + w + lw, y + h + lw]]), raw.strokeStyle, () => raw.strokeRect(x, y, w, h)); },
    fillText(s, x, y, mw) {
      const m = raw.measureText(s), w = m.width, al = raw.textAlign, x0 = al === 'center' ? x - w / 2 : (al === 'right' || al === 'end') ? x - w : x;
      const b = tbox(raw, [[x - m.actualBoundingBoxLeft, y - m.actualBoundingBoxAscent], [x + m.actualBoundingBoxRight, y + m.actualBoundingBoxDescent]]);
      const px = +((raw.font.match(/(\d+(?:\.\d+)?)px/) || [0, 0])[1]) * Math.hypot(raw.getTransform().a, raw.getTransform().b);
      paint('glyph', b, raw.fillStyle, () => (mw === undefined ? raw.fillText(s, x, y) : raw.fillText(s, x, y, mw)), () => {
        // claim spans: every claim display (or a number token of a display) found in the string, at number boundaries
        const spans = REC.claimsOf ? REC.claimsOf(s).map(([id, k, txt]) => {
          const a = x0 + raw.measureText(s.slice(0, k)).width, e = x0 + raw.measureText(s.slice(0, k + txt.length)).width;
          return { id, text: txt, box: tbox(raw, [[a, y - m.actualBoundingBoxAscent], [e, y + m.actualBoundingBoxDescent]]) };
        }) : [];
        return { text: s, fontPx: +px.toFixed(1), spans };
      });
    },
  };
  const cache = new Map();
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
