// Crux paper-cutout library (R&D rnd-hybrid, 14/10/2026). Drawn by Claude as SVG path data; no generated images.
// One source of truth for both outputs:
//   - export_svg.mjs writes each character / expression / prop to a standalone .svg (svg/);
//   - templates.js draws the same paths on the factory canvas (Path2D(d)), so frames are deterministic (no images, no randomness).
// Character = parts with a pivot, a parent and a rest offset; pose = angles (deg) per joint; face = eyes + brows + mouth (swappable).
// Coordinates: design px at scale 1, character origin = between the feet on the ground, y up is negative. Height ≈ 560 px.

export const PALETTE = { // channel tokens (ep007 design/tokens.json) + paper tones for cut-out material
  bg: '#0E1116', surface: '#171B22', grid: '#2A303B', ink: '#F2F4F7', muted: '#9AA4B2', accent: '#4C8DFF', warn: '#F2B441',
  positive: '#3FBF7F', negative: '#E5484D',
  paper: '#EDE4CF', kraft: '#C49A6C', kraftDark: '#8E6B47', navy: '#1F2A3A', slate: '#3A4352', shadow: 'rgba(0,0,0,0.38)',
  skinA: '#E8C39E', skinB: '#A9754F', skinC: '#F1D2B6', hairA: '#3B2A20', hairB: '#1E1A17', faceInk: '#1A1D24',
};
const P = PALETTE;

// ---- part shapes (local coords, pivot at 0,0, part hangs along +y unless noted)
const capsule = (w, len) => `M${-w / 2},0 L${w / 2},0 L${w / 2 - 2},${len} Q0,${len + w / 2} ${-w / 2 + 2},${len} Z`;
const HAND = 'M-15,0 a15,15 0 1,0 30,0 a15,15 0 1,0 -30,0 Z';
const SHOE = 'M-16,-4 L18,-4 Q40,-2 42,10 L42,16 L-18,16 Q-22,6 -16,-4 Z';
const HEAD = 'M0,-150 C46,-150 72,-118 72,-78 C72,-34 44,-6 0,-6 C-44,-6 -72,-34 -72,-78 C-72,-118 -46,-150 0,-150 Z';

const torso = {
  suit: 'M-58,-232 Q0,-246 58,-232 L64,-120 L52,0 L-52,0 L-64,-120 Z',
  dress: 'M-52,-232 Q0,-244 52,-232 L56,-150 L92,40 L-92,40 L-56,-150 Z',
  hoodie: 'M-62,-234 Q0,-250 62,-234 L70,-110 L60,4 L-60,4 L-70,-110 Z',
};

// joints: name → {parent, at:[x,y] in parent's coords, shape, fill, w, len}
function body(o) {
  const L = o.limb; // {arm, fore, thigh, shin, armW, legW}
  return {
    torso: { parent: null, at: [0, -L.hip], shape: torso[o.torso], fill: o.top },
    head: { parent: 'torso', at: [0, -222], shape: HEAD, fill: o.skin, scale: 1.32 },
    uaL: { parent: 'torso', at: [-50, -214], shape: capsule(L.armW, L.arm), fill: o.sleeve },
    faL: { parent: 'uaL', at: [0, L.arm], shape: capsule(L.armW - 6, L.fore), fill: o.cuff || o.sleeve, hand: o.skin, len: L.fore },
    uaR: { parent: 'torso', at: [50, -214], shape: capsule(L.armW, L.arm), fill: o.sleeve },
    faR: { parent: 'uaR', at: [0, L.arm], shape: capsule(L.armW - 6, L.fore), fill: o.cuff || o.sleeve, hand: o.skin, len: L.fore },
    thL: { parent: 'torso', at: [-26, -6], shape: capsule(L.legW, L.thigh), fill: o.legs },
    shL: { parent: 'thL', at: [0, L.thigh], shape: capsule(L.legW - 4, L.shin), fill: o.shin || o.legs, foot: o.shoe, len: L.shin },
    thR: { parent: 'torso', at: [26, -6], shape: capsule(L.legW, L.thigh), fill: o.legs },
    shR: { parent: 'thR', at: [0, L.thigh], shape: capsule(L.legW - 4, L.shin), fill: o.shin || o.legs, foot: o.shoe, len: L.shin },
  };
}
const LIMB = { arm: 100, fore: 94, thigh: 112, shin: 108, hip: 230, armW: 34, legW: 38 };

// hats / hair / extras: drawn on the head (head coords) or torso (torso coords)
const EXTRA = {
  fedora: { on: 'head', front: true, d: 'M-96,-118 Q0,-136 96,-118 L88,-108 Q0,-120 -88,-108 Z M-60,-120 L-54,-182 Q0,-200 54,-182 L60,-120 Z', fill: '#3A3F4A', band: 'M-60,-136 L60,-136 L60,-122 L-60,-122 Z' },
  bun: { on: 'head', front: false, d: 'M-74,-80 C-80,-140 -40,-162 0,-162 C40,-162 80,-140 74,-80 C60,-120 30,-128 0,-128 C-30,-128 -60,-120 -74,-80 Z M40,-150 a30,30 0 1,0 60,0 a30,30 0 1,0 -60,0 Z', fill: P.hairA },
  cap: { on: 'head', front: true, d: 'M-74,-92 C-72,-150 -36,-164 0,-164 C40,-164 74,-148 74,-96 C50,-118 -40,-126 -74,-92 Z', fill: P.hairB },
  tie: { on: 'torso', front: true, d: 'M-10,-230 L10,-230 L14,-208 L8,-120 L0,-108 L-8,-120 L-14,-208 Z', fill: '#8E3B3B' },
  vest: { on: 'torso', front: true, d: 'M-40,-226 L-6,-150 L-6,-4 L-50,-4 L-58,-120 Z M40,-226 L6,-150 L6,-4 L50,-4 L58,-120 Z', fill: '#4B5262' },
  collar: { on: 'torso', front: true, d: 'M-34,-234 Q0,-216 34,-234 L28,-214 Q0,-200 -28,-214 Z', fill: P.paper },
  pocket: { on: 'torso', front: true, d: 'M-40,-70 L40,-70 L36,-30 L-36,-30 Z', fill: '#3C74D9' },
  phone: { on: 'faR', front: true, d: 'M-14,96 L14,96 L14,146 L-14,146 Z', fill: P.navy },
};

export const CHARACTERS = {
  walt: { name: 'Walt (1930 homeowner)', era: 1930, rig: body({ torso: 'suit', top: '#5B6472', sleeve: '#5B6472', legs: '#2E3440', shoe: '#17191E', skin: P.skinA, limb: LIMB }),
    extras: ['collar', 'vest', 'tie', 'fedora'], hairFront: null },
  ruth: { name: 'Ruth (1930 homeowner)', era: 1930, rig: body({ torso: 'dress', top: '#7F9CC9', sleeve: '#7F9CC9', legs: P.skinB, shin: P.skinB, shoe: '#5A2E2E', skin: P.skinB, limb: { ...LIMB, armW: 30, legW: 26 } }),
    extras: ['bun', 'collar'] },
  sam: { name: 'Sam (homeowner today)', era: 2026, rig: body({ torso: 'hoodie', top: P.accent, sleeve: P.accent, legs: '#34507A', shoe: '#E9ECEF', skin: P.skinC, limb: LIMB }),
    extras: ['cap', 'pocket', 'phone'] },
};

// ---- faces (head coords; eyes at y ≈ -86, mouth at y ≈ -44)
const ell = (cx, cy, rx, ry) => `M${cx - rx},${cy} a${rx},${ry} 0 1,0 ${2 * rx},0 a${rx},${ry} 0 1,0 ${-2 * rx},0 Z`;
export const EYES = {
  open: { fill: [ell(-26, -86, 7, 8), ell(26, -86, 7, 8)] },
  wide: { white: [ell(-26, -88, 15, 16), ell(26, -88, 15, 16)], fill: [ell(-26, -86, 6, 6), ell(26, -86, 6, 6)] },
  happy: { stroke: ['M-38,-82 Q-26,-98 -14,-82', 'M14,-82 Q26,-98 38,-82'] },
  sad: { fill: [ell(-26, -84, 6, 7), ell(26, -84, 6, 7)], stroke: ['M-40,-91 L-14,-97', 'M14,-97 L40,-91'] },
  closed: { stroke: ['M-38,-86 Q-26,-78 -14,-86', 'M14,-86 Q26,-78 38,-86'] },
};
export const BROWS = {
  none: [], up: ['M-42,-110 Q-26,-122 -10,-112', 'M10,-112 Q26,-122 42,-110'],
  worried: ['M-42,-104 L-12,-116', 'M12,-116 L42,-104'], angry: ['M-42,-114 L-12,-104', 'M12,-104 L42,-114'], flat: ['M-40,-108 L-12,-108', 'M12,-108 L40,-108'],
};
export const MOUTHS = {
  smile: { stroke: 'M-24,-48 Q0,-26 24,-48' },
  flat: { stroke: 'M-18,-42 L18,-42' },
  o: { fill: ell(0, -40, 12, 15) },
  frown: { stroke: 'M-22,-34 Q0,-52 22,-34' },
  grin: { fill: 'M-30,-50 Q0,-50 30,-50 Q26,-20 0,-18 Q-26,-20 -30,-50 Z', white: 'M-26,-48 L26,-48 L22,-40 L-22,-40 Z' },
  wobble: { stroke: 'M-24,-38 q8,-8 16,0 q8,8 16,0 q8,-8 16,0' },
};
export const EXPRESSIONS = { // ≥ 4 required; 6 here
  neutral: { eyes: 'open', brows: 'flat', mouth: 'flat' },
  happy: { eyes: 'happy', brows: 'up', mouth: 'smile' },
  worried: { eyes: 'open', brows: 'worried', mouth: 'wobble' },
  shocked: { eyes: 'wide', brows: 'up', mouth: 'o' },
  sad: { eyes: 'sad', brows: 'worried', mouth: 'frown' },
  relieved: { eyes: 'closed', brows: 'up', mouth: 'grin' },
};

// ---- poses (deg; + = clockwise on screen). Limbs hang down at 0.
export const POSES = {
  stand: { torso: 0, head: 0, uaL: 8, faL: -4, uaR: -8, faR: 4, thL: 3, shL: -2, thR: -3, shR: 2 },
  wave: { torso: -2, head: -4, uaL: 8, faL: -4, uaR: -150, faR: -30, thL: 3, shL: -2, thR: -3, shR: 2 },
  hold: { torso: 0, head: 6, uaL: -38, faL: -70, uaR: 38, faR: 70, thL: 3, shL: -2, thR: -3, shR: 2 },
  phone: { torso: 0, head: 10, uaL: 8, faL: -4, uaR: -20, faR: -120, thL: 3, shL: -2, thR: -3, shR: 2 },
  shock: { torso: -6, head: -8, uaL: 120, faL: 40, uaR: -120, faR: -40, thL: 8, shL: -4, thR: -8, shR: 4 },
  slump: { torso: 8, head: 18, uaL: 4, faL: 0, uaR: -2, faR: 0, thL: 2, shL: 0, thR: -2, shR: 0 },
  cheer: { torso: -3, head: -6, uaL: 150, faL: 20, uaR: -150, faR: -20, thL: 3, shL: -2, thR: -3, shR: 2 },
  point: { torso: 0, head: 0, uaL: 8, faL: -4, uaR: -95, faR: -5, thL: 3, shL: -2, thR: -3, shR: 2 },
};
export function walkPose(t, speed = 1.6) { const s = Math.sin(t * Math.PI * 2 * speed), c = Math.cos(t * Math.PI * 2 * speed);
  return { torso: 2, head: 0, uaL: -22 * s, faL: -12 - 8 * c, uaR: 22 * s, faR: -12 + 8 * c, thL: 24 * s, shL: Math.max(0, 30 * c), thR: -24 * s, shR: Math.max(0, -30 * c), bob: Math.abs(s) * 8 }; }
export function blendPose(a, b, k) { const o = {}; for (const key of new Set([...Object.keys(a), ...Object.keys(b)])) o[key] = (a[key] ?? 0) + ((b[key] ?? 0) - (a[key] ?? 0)) * k; return o; }

// ---- props (origin = ground centre)
export const PROPS = {
  house: { w: 520, h: 470, parts: [
    { d: 'M-210,0 L210,0 L210,-260 L-210,-260 Z', fill: P.paper },
    { d: 'M-250,-250 L0,-440 L250,-250 Z', fill: '#B5543C' },
    { d: 'M120,-330 L170,-330 L170,-400 L120,-400 Z', fill: '#8B3F2E' },
    { d: 'M-40,0 L40,0 L40,-150 L-40,-150 Z', fill: P.kraftDark },
    { d: 'M-170,-200 L-90,-200 L-90,-120 L-170,-120 Z', fill: '#8FB3E8' },
    { d: 'M90,-200 L170,-200 L170,-120 L90,-120 Z', fill: '#8FB3E8' },
    { d: 'M-132,-200 L-128,-200 L-128,-120 L-132,-120 Z M-170,-162 L-90,-162 L-90,-158 L-170,-158 Z M128,-200 L132,-200 L132,-120 L128,-120 Z M90,-162 L170,-162 L170,-158 L90,-158 Z', fill: P.slate },
  ] },
  houseModern: { w: 560, h: 420, parts: [
    { d: 'M-240,0 L240,0 L240,-250 L-240,-250 Z', fill: '#D9DEE6' },
    { d: 'M-262,-246 L262,-246 L180,-390 L-180,-390 Z', fill: '#3A4352' },
    { d: 'M-60,0 L20,0 L20,-170 L-60,-170 Z', fill: P.accent },
    { d: 'M60,-210 L210,-210 L210,-110 L60,-110 Z', fill: '#8FB3E8' },
    { d: 'M-210,-210 L-110,-210 L-110,-110 L-210,-110 Z', fill: '#8FB3E8' },
  ] },
  bank: { w: 640, h: 520, parts: [
    { d: 'M-300,0 L300,0 L300,-30 L-300,-30 Z M-280,-30 L280,-30 L280,-56 L-280,-56 Z', fill: '#BFC6D1' },
    { d: 'M-260,-56 L260,-56 L260,-360 L-260,-360 Z', fill: P.paper },
    { d: 'M-300,-360 L300,-360 L0,-500 Z', fill: '#BFC6D1' },
    { d: 'M-226,-56 L-186,-56 L-186,-360 L-226,-360 Z M-136,-56 L-96,-56 L-96,-360 L-136,-360 Z M96,-56 L136,-56 L136,-360 L96,-360 Z M186,-56 L226,-56 L226,-360 L186,-360 Z', fill: '#D9DEE6' },
    { d: 'M-70,-56 L70,-56 L70,-250 L-70,-250 Z', fill: '#2A303B' },
  ], doors: { x0: -70, x1: 70, y0: -250, y1: -56, fill: '#8E6B47' }, label: { text: 'BANK', y: -394 } },
  note: { w: 300, h: 380, parts: [
    { d: 'M-150,-380 L110,-380 L150,-340 L150,0 L-150,0 Z', fill: P.paper },
    { d: 'M110,-380 L110,-340 L150,-340 Z', fill: '#CFC4AA' },
    { d: 'M-110,-250 L110,-250 L110,-242 L-110,-242 Z M-110,-210 L110,-210 L110,-202 L-110,-202 Z M-110,-170 L70,-170 L70,-162 L-110,-162 Z M-110,-60 L10,-60 L10,-56 L-110,-56 Z', fill: '#B9AE96' },
  ], label: { text: 'MORTGAGE', y: -300 } },
  coin: { w: 60, h: 60, parts: [{ d: ell(0, -30, 30, 30), fill: P.warn }, { d: ell(0, -30, 20, 20), fill: '#D99A2B' }] },
  person: { w: 90, h: 260, parts: [ // faceless queue figure (back view)
    { d: 'M-44,0 L-44,-120 C-44,-170 -24,-186 0,-186 C24,-186 44,-170 44,-120 L44,0 Z', fill: '#4B5262' },
    { d: ell(0, -222, 34, 36), fill: P.skinA },
    { d: 'M-42,-232 Q0,-290 42,-232 L50,-226 L-50,-226 Z', fill: '#2E3440' } ] },
};

// ---- drawing on any CanvasRenderingContext2D (the factory canvas or a test canvas)
const cache = new Map();
const path = (d) => { let p = cache.get(d); if (!p) { p = new Path2D(d); cache.set(d, p); } return p; };
const rad = (a) => (a * Math.PI) / 180;

function fillPath(ctx, d, fill, edge = true) {
  const p = path(d); ctx.fillStyle = fill; ctx.fill(p);
  if (edge) { ctx.lineWidth = 3; ctx.strokeStyle = 'rgba(0,0,0,0.18)'; ctx.stroke(p); } // cut edge
}

// pose → world matrices per part (DOMMatrix), then draw back-to-front
function partMatrices(rig, pose, base) {
  const M = {};
  const order = ['torso', 'head', 'uaL', 'faL', 'uaR', 'faR', 'thL', 'shL', 'thR', 'shR'];
  for (const k of order) { const j = rig[k], parent = j.parent ? M[j.parent] : base;
    M[k] = parent.translate(j.at[0], j.at[1]).rotate(pose[k] || 0).scale(j.scale || 1); }
  return M;
}

export function drawFace(ctx, expr, blink = false) {
  const e = EXPRESSIONS[expr] || EXPRESSIONS.neutral, eyes = EYES[blink && e.eyes !== 'happy' ? 'closed' : e.eyes];
  ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  for (const d of eyes.white || []) { ctx.fillStyle = '#FFFFFF'; ctx.fill(path(d)); }
  for (const d of eyes.fill || []) { ctx.fillStyle = P.faceInk; ctx.fill(path(d)); }
  ctx.strokeStyle = P.faceInk; ctx.lineWidth = 6;
  for (const d of eyes.stroke || []) ctx.stroke(path(d));
  ctx.lineWidth = 5; for (const d of BROWS[e.brows] || []) ctx.stroke(path(d));
  const m = MOUTHS[e.mouth];
  if (m.fill) { ctx.fillStyle = P.faceInk; ctx.fill(path(m.fill)); }
  if (m.white) { ctx.fillStyle = '#FFFFFF'; ctx.fill(path(m.white)); }
  if (m.stroke) { ctx.lineWidth = 6; ctx.stroke(path(m.stroke)); }
  ctx.fillStyle = 'rgba(229,72,77,0.22)'; ctx.fill(path(ell(-44, -58, 12, 8))); ctx.fill(path(ell(44, -58, 12, 8))); // cheeks
}

// character: {id, x, y, s, flip, pose, expr, blink, alpha}; shadow pass first (paper lifted off the page)
export function drawCharacter(ctx, c) {
  const ch = CHARACTERS[c.id], rig = ch.rig, pose = c.pose;
  const base = new DOMMatrix().translate(c.x, c.y - (pose.bob || 0)).scale((c.flip ? -1 : 1) * c.s, c.s);
  const M = partMatrices(rig, pose, base);
  const back = ['uaL', 'faL', 'thL', 'shL'], front = ['thR', 'shR', 'torso', 'head', 'uaR', 'faR'];
  ctx.save(); ctx.globalAlpha = c.alpha ?? 1;
  for (const pass of c.noShadow ? ['paper'] : ['shadow', 'paper']) { // noShadow: paper in a lit 3D scene casts a real shadow (v2/paper3d.js)
    ctx.save(); if (pass === 'shadow') ctx.translate(7 * c.s, 9 * c.s);
    for (const k of [...back, ...front]) {
      const j = rig[k]; ctx.save(); ctx.setTransform(ctx.getTransform().multiply(M[k]));
      const sh = pass === 'shadow';
      if (k === 'head') for (const x of ch.extras) if (EXTRA[x].on === 'head' && !EXTRA[x].front) fillPath(ctx, EXTRA[x].d, sh ? P.shadow : EXTRA[x].fill, !sh);
      fillPath(ctx, j.shape, sh ? P.shadow : j.fill, !sh);
      if (j.hand) { ctx.save(); ctx.translate(0, j.len + 8); fillPath(ctx, HAND, sh ? P.shadow : j.hand, !sh); ctx.restore(); }
      if (j.foot) { ctx.save(); ctx.translate(0, j.len + 4); fillPath(ctx, SHOE, sh ? P.shadow : j.foot, !sh); ctx.restore(); }
      for (const x of ch.extras) { const ex = EXTRA[x]; if (ex.on === k && (ex.front || k !== 'head')) { fillPath(ctx, ex.d, sh ? P.shadow : ex.fill, !sh); if (ex.band && !sh) fillPath(ctx, ex.band, P.navy, false); } }
      if (k === 'head' && !sh) drawFace(ctx, c.expr, c.blink);
      ctx.restore();
    }
    ctx.restore();
  }
  ctx.restore();
}

export function drawProp(ctx, id, o) { // o: {x, y, s, rot, alpha, doors (0 open → 1 closed), label}
  const pr = PROPS[id]; ctx.save(); ctx.globalAlpha = o.alpha ?? 1; ctx.translate(o.x, o.y); ctx.rotate(rad(o.rot || 0)); ctx.scale(o.s, o.s);
  for (const pass of o.noShadow ? ['paper'] : ['shadow', 'paper']) { ctx.save(); if (pass === 'shadow') ctx.translate(8, 10);
    for (const part of pr.parts) fillPath(ctx, part.d, pass === 'shadow' ? P.shadow : part.fill, pass !== 'shadow');
    ctx.restore(); if (pass === 'shadow') continue;
    if (pr.doors && o.doors) { const D = pr.doors, w = (D.x1 - D.x0) / 2 * o.doors;
      fillPath(ctx, `M${D.x0},${D.y1} L${D.x0 + w},${D.y1} L${D.x0 + w},${D.y0} L${D.x0},${D.y0} Z`, D.fill);
      fillPath(ctx, `M${D.x1 - w},${D.y1} L${D.x1},${D.y1} L${D.x1},${D.y0} L${D.x1 - w},${D.y0} Z`, D.fill); }
    const lab = o.label ?? pr.label?.text; if (lab) { ctx.fillStyle = P.navy; ctx.font = `700 ${id === 'bank' ? 64 : 44}px Inter`; ctx.textAlign = 'center'; ctx.fillText(lab, 0, pr.label?.y ?? -300); }
  }
  ctx.restore();
}

// deterministic hash noise (no Math.random): paper grain + sticker jitter
export function hash(n) { let x = Math.imul(n ^ 0x9e3779b9, 0x85ebca6b); x ^= x >>> 13; x = Math.imul(x, 0xc2b2ae35); x ^= x >>> 16; return (x >>> 0) / 4294967296; }
