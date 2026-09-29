'use strict';
// H2 "Hồ sơ và bằng chứng" — shared helpers. A scene builds DOM once (build) and sets state for time t (update).
// Camera: a 2.5D desk (CSS perspective, tilt, pan, zoom); papers can lift (translateZ) and defocus with distance.
(function () {
  const desk = document.getElementById('desk');
  const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const lerp = (a, b, p) => a + (b - a) * p;
  const ease = (p) => { p = clamp(p); return p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2; };
  const easeOut = (p) => 1 - Math.pow(1 - clamp(p), 3);
  const back = (p) => { p = clamp(p); const c = 1.4; return 1 + (c + 1) * Math.pow(p - 1, 3) + c * Math.pow(p - 1, 2); };
  const seg = (t, a, b) => clamp((t - a) / (b - a));

  function el(tag, parent, cls, style, html) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (style) Object.assign(e.style, style);
    if (html != null) e.innerHTML = html;
    (parent || desk).appendChild(e);
    return e;
  }
  const px = (v) => v + 'px';
  function box(parent, cls, x, y, w, h, style) { return el('div', parent, cls, Object.assign({ left: px(x), top: px(y), width: px(w), height: px(h) }, style || {})); }
  function text(parent, s, x, y, size, o) {
    o = o || {};
    const e = el('div', parent, 't ' + (o.cls || ''), Object.assign({ left: px(x), top: px(y), fontSize: px(size), fontWeight: o.w || 400, color: o.color || '' }, o.style || {}), s);
    if (o.align === 'right') { e.style.transform = 'translateX(-100%)'; }
    if (o.align === 'center') { e.style.transform = 'translateX(-50%)'; }
    return e;
  }
  const SVGNS = 'http://www.w3.org/2000/svg';
  function svg(parent, x, y, w, h) {
    const s = document.createElementNS(SVGNS, 'svg');
    s.setAttribute('width', w); s.setAttribute('height', h); s.setAttribute('viewBox', `0 0 ${w} ${h}`);
    Object.assign(s.style, { left: px(x), top: px(y) });
    (parent || desk).appendChild(s); return s;
  }
  function sv(parent, tag, attrs) { const e = document.createElementNS(SVGNS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); parent.appendChild(e); return e; }
  // stroke reveal (pen): set path length based dash
  function penPrep(p) { const L = p.getTotalLength(); p.style.strokeDasharray = L + ' ' + L; p.style.strokeDashoffset = L; p._L = L; return p; }
  function pen(p, prog) { p.style.strokeDashoffset = p._L * (1 - clamp(prog)); p.style.opacity = prog > 0 ? 1 : 0; }
  // hand-drawn ellipse around (cx,cy) with rx,ry — slightly overshooting loop
  function loopPath(cx, cy, rx, ry, seed) {
    const n = 48, pts = []; const s = seed || 1;
    for (let i = 0; i <= n * 1.12; i++) {
      const a = -2.2 + (i / n) * Math.PI * 2;
      const wob = 1 + 0.04 * Math.sin(i * 0.9 + s) + 0.03 * Math.sin(i * 0.37 + 2 * s);
      pts.push([cx + Math.cos(a) * rx * wob, cy + Math.sin(a) * ry * wob * (1 + 0.06 * i / n)]);
    }
    return 'M' + pts.map((p) => p[0].toFixed(1) + ',' + p[1].toFixed(1)).join(' L');
  }
  // highlighter: a div with multiply blend that grows from left
  function highlighter(parent, x, y, w, h, color) {
    const e = box(parent, 'hl', x, y, w, h, { background: color, opacity: .55 });
    e.style.transform = 'scaleX(0)'; return e;
  }
  function hl(e, prog) { e.style.transform = `scaleX(${easeOut(prog)}) skewX(-6deg)`; }
  function stamp(parent, x, y, size, rot) {
    const e = el('div', parent, 'stamp', { left: px(x), top: px(y), fontSize: px(size), transform: `rotate(${rot || -4}deg)` }, 'ILLUSTRATIVE');
    return e;
  }

  // camera: keys [t, {x, y, z(oom), tilt, roll}] — eased between keys
  let cam = { x: 640, y: 360, z: 1, tilt: 0, roll: 0 };
  function camAt(keys, t) {
    if (t <= keys[0][0]) return keys[0][1];
    for (let i = 1; i < keys.length; i++) {
      const [t1, c1] = keys[i], [t0, c0] = keys[i - 1];
      if (t <= t1) { const p = ease((t - t0) / (t1 - t0)); const o = {}; for (const k in c1) o[k] = lerp(c0[k] != null ? c0[k] : c1[k], c1[k], p); return o; }
    }
    return keys[keys.length - 1][1];
  }
  function setCam(c) {
    cam = c;
    desk.style.transform = `translate(640px, 372px) rotateX(${c.tilt}deg) rotateZ(${c.roll}deg) scale(${c.z}) translate(${-c.x}px, ${-c.y}px)`;
  }
  // depth-of-field: blur papers by distance from the camera focus (world units / zoom)
  function dof(items, maxBlur) {
    for (const it of items) {
      const cx = it.x + it.w / 2, cy = it.y + it.h / 2;
      const dx = Math.max(0, Math.abs(cx - cam.x) - it.w / 2), dy = Math.max(0, Math.abs(cy - cam.y) - it.h / 2);
      const d = Math.hypot(dx, dy) * cam.z;
      const b = clamp((d - 420) / 700) * (maxBlur || 5);
      it.e.style.filter = b > 0.15 ? `blur(${b.toFixed(2)}px)` : 'none';
    }
  }
  function lift(e, z, rot, dx, dy) {
    e.style.transform = `translate3d(${dx || 0}px, ${dy || 0}px, ${z || 0}px) rotate(${rot || 0}deg)`;
    const s = 18 + (z || 0) * 0.35;
    e.style.boxShadow = `${(z || 0) * 0.15}px ${s}px ${s * 2}px rgba(0,0,0,${0.5 + clamp((z || 0) / 200) * 0.15}), 0 2px 4px rgba(0,0,0,.4)`;
  }
  const money = (v) => '$' + Math.round(v).toLocaleString('en-US');

  window.K = { desk, clamp, lerp, ease, easeOut, back, seg, el, box, text, svg, sv, penPrep, pen, loopPath, highlighter, hl, stamp, camAt, setCam, dof, lift, money, px,
    C: { bg: '#0e1116', surface: '#171b22', ink: '#f2f4f7', muted: '#9aa4b2', grid: '#2a303b', accent: '#4c8dff', warn: '#f2b441', positive: '#3fbf7f', negative: '#e5484d' } };
  window.SCENE = null; // set by f?.js: { dur, build(data), update(t) }
  window.setT = (t) => { window.SCENE.update(t); };
})();
