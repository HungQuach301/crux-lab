// Writes the paper-cutout library to standalone SVG files (svg/), from the same path data the canvas templates draw.
//   node rnd-hybrid/cutout/export_svg.mjs
import fs from 'fs'; import path from 'path'; import { fileURLToPath } from 'url';
const HERE = path.dirname(fileURLToPath(import.meta.url));
const R = await import(path.join(HERE, 'rig.js'));
const { CHARACTERS, EXPRESSIONS, EYES, BROWS, MOUTHS, POSES, PROPS, PALETTE: P } = R;
const OUT = path.join(HERE, 'svg'); fs.mkdirSync(OUT, { recursive: true });
const EDGE = 'stroke="rgba(0,0,0,0.18)" stroke-width="3"';
const HAND = 'M-15,0 a15,15 0 1,0 30,0 a15,15 0 1,0 -30,0 Z', SHOE = 'M-16,-4 L18,-4 Q40,-2 42,10 L42,16 L-18,16 Q-22,6 -16,-4 Z';
// extras are not exported by rig.js: re-read them through a tiny accessor on the module text (single source stays rig.js)
const src = fs.readFileSync(path.join(HERE, 'rig.js'), 'utf8');
const EXTRA = new Function('P', 'return ' + src.match(/const EXTRA = (\{[\s\S]*?\n\});/)[1])(P);
function face(expr) {
  const e = EXPRESSIONS[expr], ey = EYES[e.eyes], m = MOUTHS[e.mouth]; let s = `<g id="face-${expr}" stroke-linecap="round" fill="none">`;
  for (const d of ey.white || []) s += `<path d="${d}" fill="#FFFFFF"/>`;
  for (const d of ey.fill || []) s += `<path d="${d}" fill="${P.faceInk}"/>`;
  for (const d of ey.stroke || []) s += `<path d="${d}" stroke="${P.faceInk}" stroke-width="6"/>`;
  for (const d of BROWS[e.brows]) s += `<path d="${d}" stroke="${P.faceInk}" stroke-width="5"/>`;
  if (m.fill) s += `<path d="${m.fill}" fill="${P.faceInk}"/>`; if (m.white) s += `<path d="${m.white}" fill="#FFFFFF"/>`;
  if (m.stroke) s += `<path d="${m.stroke}" stroke="${P.faceInk}" stroke-width="6"/>`;
  return s + '</g>';
}
function character(id, pose, expr) { // nested groups = the rig (each joint a <g id> with its pivot transform; swap rotate() to animate)
  const ch = CHARACTERS[id], rig = ch.rig, po = POSES[pose];
  const ex = (k, front) => ch.extras.filter((x) => EXTRA[x].on === k && (k !== 'head' || EXTRA[x].front === front)).map((x) => `<path d="${EXTRA[x].d}" fill="${EXTRA[x].fill}" ${EDGE}/>`).join('');
  const part = (k, inner = '') => { const j = rig[k]; return `<g id="${k}" transform="translate(${j.at[0]},${j.at[1]}) rotate(${po[k] || 0}) scale(${j.scale || 1})">` +
    (k === 'head' ? ex('head', false) : '') + `<path d="${j.shape}" fill="${j.fill}" ${EDGE}/>` +
    (j.hand ? `<path transform="translate(0,${j.len + 8})" d="${HAND}" fill="${j.hand}" ${EDGE}/>` : '') +
    (j.foot ? `<path transform="translate(0,${j.len + 4})" d="${SHOE}" fill="${j.foot}" ${EDGE}/>` : '') +
    (k === 'head' ? ex('head', true) + face(expr) : ex(k, true)) + inner + '</g>'; };
  const torsoInner = part('uaL', part('faL')) + part('thL', part('shL')) + part('thR', part('shR'));
  // draw order: back limbs, torso, front limbs (SVG order = paint order)
  const j = rig.torso;
  return `<g id="${id}"><g transform="translate(0,${j.at[1]})">` +
    `<g id="back">${part('uaL', part('faL'))}${part('thL', part('shL'))}</g>${part('thR', part('shR'))}` +
    `<g id="torso"><path d="${j.shape}" fill="${j.fill}" ${EDGE}/>${ex('torso', true)}</g>${part('head')}${part('uaR', part('faR'))}</g></g>`;
}
const wrap = (w, h, vb, body, title) => `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="${vb}"><title>${title}</title>${body}</svg>\n`;
let n = 0;
for (const id of Object.keys(CHARACTERS)) {
  fs.writeFileSync(path.join(OUT, `char-${id}.svg`), wrap(360, 680, '-180,-660 360,680', character(id, 'stand', 'neutral'), CHARACTERS[id].name + ' — ILLUSTRATIVE')); n++;
  let sheet = ''; Object.keys(EXPRESSIONS).forEach((e, i) => { sheet += `<g transform="translate(${i * 300 + 150},700)">${character(id, 'stand', e)}<text x="0" y="60" font-family="Inter" font-size="34" text-anchor="middle" fill="#9AA4B2">${e}</text></g>`; });
  fs.writeFileSync(path.join(OUT, `expr-${id}.svg`), wrap(1800, 800, '0,0 1800,800', `<rect width="1800" height="800" fill="${P.bg}"/>` + sheet, CHARACTERS[id].name + ' — 6 expressions')); n++;
}
for (const [id, pr] of Object.entries(PROPS)) {
  const body = pr.parts.map((p) => `<path d="${p.d}" fill="${p.fill}" ${EDGE}/>`).join('') + (pr.label ? `<text x="0" y="${pr.label.y}" font-family="Inter" font-weight="700" font-size="${id === 'bank' ? 64 : 44}" text-anchor="middle" fill="${P.navy}">${pr.label.text}</text>` : '');
  const w = pr.w + 40, h = pr.h + 60;
  fs.writeFileSync(path.join(OUT, `prop-${id}.svg`), wrap(w, h, `${-w / 2},${-h + 20} ${w},${h}`, body, id)); n++;
}
fs.writeFileSync(path.join(OUT, 'palette.json'), JSON.stringify(P, null, 1) + '\n');
console.log('wrote', n, 'svg + palette.json to', path.relative(process.cwd(), OUT));
