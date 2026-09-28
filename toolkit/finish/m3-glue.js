'use strict';
// Contract files that depend on the timeline and the render (from test D's src/d/m3-glue.js).
// crux-lab: EP_ROOT = episode root. The episode's own edit decisions come from <root>/edit/glue.json:
//   {bpm:{act:bpm}, match:{sceneId:[type, reason]}, silences:[[sentenceId, why]], accents:[sceneId], adBreaksAfter:[sentenceId],
//    impacts:[textId]}, the cue sheet from <root>/edit/cues.json and the description from <root>/edit/description.md,
//   where {act:<id>} and {scene:<id>} become m:ss.
//   node toolkit/finish/m3-glue.js pre    -> tempo-map.json (beats + accents on cuts), transitions.json, silences.json, captions.srt,
//                                   package/description.md, cues.json, tension-map (M2 range), adbreaks.json, render-log.json
//   node toolkit/finish/m3-glue.js post  -> sfx-events.json from the render's first-visible texts
const fs = require('fs');
const path = require('path');

const R = path.resolve(process.env.EP_ROOT || '.');
const GLUE = JSON.parse(fs.readFileSync(path.join(R, 'edit', 'glue.json'), 'utf8'));
const J = (p) => JSON.parse(fs.readFileSync(p, 'utf8'));
const W = (rel, o) => { const p = path.join(R, rel); fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, typeof o === 'string' ? o : JSON.stringify(o, null, 1)); };
const tl = J(path.join(R, 'out', 'timeline.json'));
const script = J(path.join(R, 'out', 'script.json'));
const FR = 1 / 30;

// match cuts (semantic: the idea carries across the cut; reasons >= 5 words)
const MATCH = GLUE.match || {};

function pre() {
  // intentional silences (music, sfx and whoosh out; room tone stays under -40 dBFS): after decisive / reveal lines
  const SIL = GLUE.silences || [];
  const silences = SIL.map(([sid, why]) => {
    const i = script.sentences.findIndex((l) => l.id === sid);
    const l = script.sentences[i], nx = script.sentences[i + 1];
    const t0 = l.end + 0.08, room = (nx ? nx.start : tl.total) - 0.08 - t0;
    const cap = /ad break/.test(why) ? 3.2 : 1.3; // the ad-break silences run up to the next act's first line
    return room >= 0.8 ? { t: +t0.toFixed(3), dur: +Math.min(cap, room).toFixed(3), why, after: sid } : null;
  }).filter(Boolean);
  W('out/silences.json', { silences });
  const full = { bpm: GLUE.bpm };
  const cuts = tl.scenes.slice(1).map((s) => s.start);
  // the tempo map follows the edit: every cut is a beat; each shot is divided into a whole number of beats at the
  // act's nominal tempo (so the local tempo moves a little shot to shot, like a conductor following picture)
  const nominal = (t) => { const a = tl.acts.find((x) => t >= x.start && t < x.end) || tl.acts[tl.acts.length - 1]; const b = full.bpm[a.id]; return Array.isArray(b) ? b[0] : b; };
  const edges = [0, ...cuts, tl.total];
  const beats = [];
  for (let i = 0; i + 1 < edges.length; i++) {
    const a = edges[i], b = edges[i + 1], per = 60 / nominal(a);
    const n = Math.max(1, Math.round((b - a) / per));
    for (let k = 0; k < n; k++) beats.push(+(a + (b - a) * k / n).toFixed(4));
  }
  const onBeat = (c) => beats.some((b) => Math.abs(b - c) <= FR + 1e-6);
  // accents: cuts that sit on a beat at the start of a new idea (act boundary, reveal scenes)
  const ACC = GLUE.accents || [];
  const silPre = J(path.join(R, 'out', 'silences.json')).silences;
  const accents = tl.scenes.filter((s) => ACC.includes(s.id) && onBeat(s.start) && !silPre.some((x) => s.start >= x.t - 0.1 && s.start <= x.t + x.dur + 0.1)).map((s) => s.start);
  W('out/tempo-map.json', { bpm: full.bpm, beats, accents, note: 'tempo map follows the edit: every cut is a beat, each shot holds a whole number of beats near the act tempo; accents are cuts' });
  const transitions = { cuts: tl.scenes.slice(1).map((s, i) => {
    const from = tl.scenes[i].id, base = s.id.replace(/-[bc]$/, '');
    const m = MATCH[base] && !s.id.endsWith('-b') ? MATCH[base] : null;
    return { t: s.start, from, to: s.id, type: 'cut', match: m ? m[0] : null, audio: s.cutIn || null, action: false,
      reason: m ? m[1] : s.id.endsWith('-b') ? 'a second angle inside one long line of narration' : `hard cut on the beat into ${base.replace(/-/g, ' ')} to start the next idea` };
  }) };
  W('out/transitions.json', transitions);

  // captions: one cue per sentence, split into <= 42-char lines (max 2) and 1-7 s cues by the word timing
  const cues = [];
  const cueMap = {};
  const wrap = (txt) => { const ws = txt.split(' '); const lines = ['']; for (const w of ws) { const c = lines[lines.length - 1]; if ((c + ' ' + w).trim().length > 42) lines.push(w); else lines[lines.length - 1] = (c + ' ' + w).trim(); } return lines; };
  for (const l of script.sentences) {
    const words = l.text.split(' ');
    // chunks of <= 2 lines of 42 chars
    const chunks = [];
    let cur = [];
    for (const w of words) { const cand = [...cur, w].join(' '); if (wrap(cand).length > 2) { chunks.push(cur); cur = [w]; } else cur.push(w); }
    if (cur.length) chunks.push(cur);
    // no orphan: move words forward until the last chunk is long enough to read for >= 1 s
    while (chunks.length > 1 && chunks[chunks.length - 1].join(' ').length < 24 && chunks[chunks.length - 2].length > 4) chunks[chunks.length - 1].unshift(chunks[chunks.length - 2].pop());
    const n = l.text.length;
    let acc = 0;
    chunks.forEach((c, k) => {
      const txt = c.join(' ');
      const a = l.start + (l.end - l.start) * acc / n;
      acc += txt.length + 1;
      const b = k === chunks.length - 1 ? l.end : l.start + (l.end - l.start) * acc / n;
      cues.push({ a, b, lines: wrap(txt) });
    });
  }
  for (let i = 0; i < cues.length; i++) {
    if (cues[i].b - cues[i].a < 1.0) {
      const j = i + 1 < cues.length && wrap(cues[i].lines.join(' ') + ' ' + cues[i + 1].lines.join(' ')).length <= 2 && cues[i + 1].b - cues[i].a <= 7 ? i + 1
        : i > 0 && wrap(cues[i - 1].lines.join(' ') + ' ' + cues[i].lines.join(' ')).length <= 2 && cues[i].b - cues[i - 1].a <= 7 ? i - 1 : -1;
      if (j === i + 1) { cues[i + 1] = { a: cues[i].a, b: cues[i + 1].b, lines: wrap(cues[i].lines.join(' ') + ' ' + cues[i + 1].lines.join(' ')) }; cues.splice(i, 1); i--; continue; }
      if (j === i - 1) { cues[i - 1] = { a: cues[i - 1].a, b: cues[i].b, lines: wrap(cues[i - 1].lines.join(' ') + ' ' + cues[i].lines.join(' ')) }; cues.splice(i, 1); i -= 2; continue; }
    }
  }
  for (let i = 0; i < cues.length; i++) {
    const nx = cues[i + 1] ? cues[i + 1].a : tl.total;
    if (cues[i].b - cues[i].a < 1.0) cues[i].b = Math.min(cues[i].a + 1.0, nx - 0.02);
    if (cues[i].b - cues[i].a < 1.0 && i > 0) cues[i].a = Math.max(cues[i - 1].b + 0.02, cues[i].b - 1.0);
    cues[i].b = Math.min(cues[i].b, nx - 0.02, cues[i].a + 7.0);
  }
  const ts = (x) => { const ms = Math.round(x * 1000); const h = Math.floor(ms / 3600000), m = Math.floor(ms / 60000) % 60, s = Math.floor(ms / 1000) % 60; return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')},${String(ms % 1000).padStart(3, '0')}`; };
  W('out/captions.srt', cues.map((c, i) => `${i + 1}\n${ts(c.a)} --> ${ts(c.b)}\n${c.lines.join('\n')}\n`).join('\n'));
  void cueMap;
  // description with chapters (M2 segment)
  const sc = (id) => tl.scenes.find((s) => s.id === id).start;
  const mmss = (t) => `${Math.floor(t / 60)}:${String(Math.floor(t % 60)).padStart(2, '0')}`;
  const act = (id) => tl.acts.find((a) => a.id === id).start;
  W('out/package/description.md', fs.readFileSync(path.join(R, 'edit', 'description.md'), 'utf8').replace(/\{(act|scene):([\w-]+)\}/g, (_, k, id) => mmss(k === 'act' ? act(id) : sc(id))));
  // adbreaks: none inside the M2 segment (its only act-to-act boundary with speech on both sides is act1|act2, after the end)
  // ad breaks: inside the silences at the act1|act2 and act2|act3 boundaries
  const brk = (GLUE.adBreaksAfter || []).map((sid) => silences.find((x) => x.after === sid)).filter(Boolean).map((x) => { const bnd = tl.acts.find((a) => a.start > x.t).start; return { t: +Math.min(x.t + x.dur - 0.5, Math.max(x.t + 0.5, bnd)).toFixed(3), boundary: bnd, why: 'act boundary, inside a ' + x.dur.toFixed(2) + ' s silence' }; });
  W('out/adbreaks.json', { breaks: brk });
  // cue sheet and tension map, cut to the M2 range
  const cs = J(path.join(R, 'edit', 'cues.json'));
  W('out/cues.json', { ...cs, silences });
  // numbers[]: video time of every spoken number (the mix dips music, whoosh and sfx around each one); no physical beds
  const cm = eval(fs.readFileSync(path.join(R, 'render', 'data.js'), 'utf8').replace('window.DATA = ', '(').replace(/;\s*$/, ')')).cues;
  const numbers = [...new Set(Object.entries(cm).filter(([k]) => /\|[−$]?\d/.test(k)).map(([, v]) => v))].sort((a, b) => a - b);
  W('out/physical.json', { beds: [], events: [], numbers });
  console.log('beats', beats.length, 'accents', accents.length, '| cuts', cuts.length, 'on beat', cuts.filter(onBeat).length, '| silences', silences.length, '| captions', cues.length);
}

function post() {
  const seen = J(path.join(R, 'work', 'text-first.json'));
  const events = [];
  for (const [tid, v] of Object.entries(seen)) {
    if (!(v.level === 1 || v.claims > 0 || v.role === 'badge')) continue;
    if (v.t < 0.3) continue;
    const impact = (GLUE.impacts || []).includes(tid) || /-l1$/.test(tid) && v.claims > 0;
    events.push({ t: v.t, x: v.x, id: tid, kind: impact ? 'impact' : 'reveal', ...(impact ? { riser: 0.9 } : {}) });
  }
  events.sort((a, b) => a.t - b.t);
  // keep events at least 0.25 s apart (each is measured over its own 150 ms window)
  const kept = [];
  for (const e of events) if (!kept.length || e.t - kept[kept.length - 1].t >= 0.25) kept.push(e);
  W('out/sfx-events.json', { events: kept.map((e) => ({ t: e.t, x: e.x, id: e.id, kind: e.kind, ...(e.riser ? { riser: e.riser } : {}) })) });
  const run = J(path.join(R, 'work', 'render-run.json'));
  W('out/render-log.json', { subframes: 8, shutter: 0.5, render: run });
  console.log('sfx events', kept.length);
}

if (process.argv[2] === 'post') post(); else pre();
