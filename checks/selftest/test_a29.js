'use strict';
// A29 (K4.3): per-segment key of a one-file world page (sampler.pageSegments). A change in one segment's module or spine directory changes that segment's
// key only; a module added to another segment (shifting module indices) changes nothing else; a shared module or shared JSON changes every key.
//   node checks/selftest/test_a29.js
const fs = require('fs'), os = require('os'), path = require('path');
const { pageSegments } = require('../page/sampler.js');
const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'a29-'));
function page(o) {
  const B = { mods: [{ src: 'core' + (o.core || '') }, { src: "import '__CRUXMOD_0__'; seg A" + (o.a || '') }, ...(o.extra ? [{ src: 'helper' }] : []),
    { src: "import '__CRUXMOD_0__';" + (o.extra ? " import '__CRUXMOD_2__';" : '') + ' seg B' + (o.b || '') }],
  order: [], core: 0, fps: 30, claims: [{ id: 'x', display: '$1' }], view: null,
  segs: [{ id: 'a', mod: 1, t0: 0, t1: 10 }, { id: 'b', mod: o.extra ? 3 : 2, t0: 10, t1: 20 }],
  json: { '/w/a/spine.json': JSON.stringify({ episode_t0: 0, x: o.sa || 0 }), '/w/b/spine.json': JSON.stringify({ episode_t0: 10 }), '/w/claims.json': '{"v":' + (o.cl || 0) + '}' } };
  const f = path.join(dir, Math.random().toString(36).slice(2) + '.html');
  fs.writeFileSync(f, `<!doctype html><html><head><script>window.__CRUX = ${JSON.stringify(B).replace(/<\//g, '<\\/')};</script></head><body><script type="module">rt</script></body></html>\n`);
  const k = pageSegments('file://' + f);
  return k && [k.at(1), k.at(15)];
}
const cases = [
  ['change seg A module', { a: '!' }, [true, false]],
  ['change seg A spine', { sa: 1 }, [true, false]],
  ['change seg B module', { b: '!' }, [false, true]],
  ['add a module to seg B (indices shift)', { extra: true }, [false, true]],
  ['change shared module (core)', { core: '!' }, [true, true]],
  ['change shared JSON', { cl: 1 }, [true, true]],
];
const ref = page({});
let bad = 0;
if (!ref) { console.log('FAIL: pageSegments returned null on a well-formed page'); process.exit(1); }
for (const [name, o, want] of cases) {
  const k = page(o), got = [k[0] !== ref[0], k[1] !== ref[1]];
  const ok = got[0] === want[0] && got[1] === want[1];
  if (!ok) bad++;
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}: changed A=${got[0]} B=${got[1]} (want ${want})`);
}
console.log(pageSegments('file://' + path.join(dir, 'missing.html')) === null ? 'PASS no page → null (whole-file check)' : (bad++, 'FAIL no page'));
process.exit(bad ? 1 : 0);
