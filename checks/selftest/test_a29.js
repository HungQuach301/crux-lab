'use strict';
// A29 (K4.4.1): per-segment key of a one-file world page (sampler.pageSegments). A change in one segment's module or spine directory changes that segment's
// key only; a module added to another segment (shifting module indices) changes nothing else; a shared module, shared JSON or the HTML outside the blob
// changes every key; a scene spanning two segments changes when either does (REVIEWER K4.4.1 C1); a spine matching no segment → null (whole-file check).
//   node checks/selftest/test_a29.js
const fs = require('fs'), os = require('os'), path = require('path');
const { pageSegments } = require('../page/sampler.js');
const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'a29-'));
function segments(o) {
  const B = { mods: [{ src: 'core' + (o.core || '') }, { src: "import '__CRUXMOD_0__'; seg A" + (o.a || '') }, ...(o.extra ? [{ src: 'helper' }] : []),
    { src: "import '__CRUXMOD_0__';" + (o.extra ? " import '__CRUXMOD_2__';" : '') + ' seg B' + (o.b || '') }],
  order: [], core: 0, fps: 30, claims: [{ id: 'x', display: '$1' }], view: null,
  segs: [{ id: 'a', mod: 1, t0: 0, t1: 10 }, { id: 'b', mod: o.extra ? 3 : 2, t0: 10, t1: 20 }],
  json: { '/w/a/spine.json': JSON.stringify({ episode_t0: 0, x: o.sa || 0 }), '/w/b/spine.json': JSON.stringify({ episode_t0: o.bt0 ?? 10 }),
    '/w/claims.json': '{"v":' + (o.cl || 0) + '}' } };
  const f = path.join(dir, Math.random().toString(36).slice(2) + '.html');
  fs.writeFileSync(f, `<!doctype html><html><head><script>window.__CRUX = ${JSON.stringify(B).replace(/<\//g, '<\\/')};</script></head><body><script type="module">${o.rt || 'rt'}</script></body></html>\n`);
  return pageSegments('file://' + f);
}
const keys = (o) => { const k = segments(o); return k && [k.at(1), k.at(15), k.over(5, 15)]; };
const cases = [   // [name, change, want changed: seg A key, seg B key, key of a scene spanning [5, 15]]
  ['change seg A module', { a: '!' }, [true, false, true]],
  ['change seg A spine', { sa: 1 }, [true, false, true]],
  ['change seg B module', { b: '!' }, [false, true, true]],
  ['add a module to seg B (indices shift)', { extra: true }, [false, true, true]],
  ['change shared module (core)', { core: '!' }, [true, true, true]],
  ['change shared JSON', { cl: 1 }, [true, true, true]],
  ['change the HTML outside the blob (runtime, fonts)', { rt: 'rt2' }, [true, true, true]],
];
const ref = keys({});
let bad = 0;
if (!ref) { console.log('FAIL: pageSegments returned null on a well-formed page'); process.exit(1); }
for (const [name, o, want] of cases) {
  const k = keys(o), got = k.map((x, i) => x !== ref[i]);
  const ok = got.every((g, i) => g === want[i]);
  if (!ok) bad++;
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}: changed A=${got[0]} B=${got[1]} A+B=${got[2]} (want ${want})`);
}
const one = segments({});
console.log(one.over(1, 9) === segments({ b: '!' }).over(1, 9) ? 'PASS a scene inside A ignores a change in B' : (bad++, 'FAIL scene inside A'));
console.log(segments({ bt0: 12 }) === null ? 'PASS spine t0 matching no segment → null (whole-file check)' : (bad++, 'FAIL spine t0 mismatch'));
console.log(pageSegments('file://' + path.join(dir, 'missing.html')) === null ? 'PASS no page → null (whole-file check)' : (bad++, 'FAIL no page'));
process.exit(bad ? 1 : 0);
