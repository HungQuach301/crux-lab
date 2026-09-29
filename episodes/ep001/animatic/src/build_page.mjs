// Bundle src/film.js (scenes, engine, timing, anchors, tokens, three.js) into build/film.js for film.html (works from file://).
//   cd episodes/ep001/animatic && npm ci && node src/build_page.mjs
import { build } from 'esbuild';
import { fileURLToPath } from 'url';
import path from 'path';
const AN = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
await build({ entryPoints: [path.join(AN, 'src/film.js')], bundle: true, format: 'iife', outfile: path.join(AN, 'build/film.js'),
  loader: { '.json': 'json' }, target: 'chrome120', minify: false, sourcemap: false, logLevel: 'info', legalComments: 'inline' });
