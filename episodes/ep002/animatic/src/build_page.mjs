// Bundle src/film_c5.js (scenes, film/lib, the signed engines and clips, timing, anchors, claims, tokens) into build/film.js
// for film.html (works from file://). The two signed engines read their tokens and data with a top-level await fetch / a
// window.DATA capture in C3/C4; here those lines are rewritten at build time (nothing else) so one page can hold both engines:
//   H2 engine: TOK <- window.TOK_E, DATA <- window.DATA_H2;  H3 engine: TOK <- window.TOK_E, DATA <- window.DATA_H3;
//   s11.js: method card <- window.CARD_E. Data files: python3 src/build_c5_data.py (work/c5/data-h2.js, data-h3.js; not committed).
//   cd episodes/ep002/animatic && npm ci && node src/build_page.mjs
import { build } from 'esbuild';
import { fileURLToPath } from 'url';
import fs from 'fs';
import path from 'path';
const AN = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const FIN = path.resolve(AN, '../design/c3/final/src');
const RW = [
  [path.join(FIN, 'engine.js'), [["await (await fetch('/tokens.json')).json()", 'window.TOK_E'], ['export const DATA = window.DATA;', 'export const DATA = window.DATA_H2;']]],
  [path.join(FIN, 'h3/engine.js'), [["await (await fetch('/episodes/ep002/design/c3/final/tokens.json')).json()", 'window.TOK_E'], ['export const DATA = window.DATA;', 'export const DATA = window.DATA_H3;']]],
  [path.join(AN, 'src/s11.js'), [["await (await fetch('/episodes/ep002/animatic/src/method_card.json')).json()", 'window.CARD_E']]],
];
const rewrite = { name: 'rewrite', setup(b) {
  for (const [file, reps] of RW) b.onLoad({ filter: new RegExp('^' + file.replace(/[.*+?^${}()|[\]\\/]/g, '\\$&') + '$') }, () => {
    let s = fs.readFileSync(file, 'utf8');
    for (const [a, c] of reps) { if (!s.includes(a)) throw new Error('rewrite: not found in ' + file + ': ' + a); s = s.replace(a, c); }
    return { contents: s, loader: 'js' };
  });
} };
await build({ entryPoints: [path.join(AN, 'src/film_c5.js')], bundle: true, format: 'iife', outfile: path.join(AN, 'build/film.js'), plugins: [rewrite],
  loader: { '.json': 'json' }, target: 'chrome120', minify: false, sourcemap: false, logLevel: 'info', legalComments: 'inline' });
