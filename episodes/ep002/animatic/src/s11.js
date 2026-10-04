// S11 · How we know this: the METHOD CARD (G-014). Lines from src/method_card.json (the model limits listed at the head of
// story/script.md + the S11 picture note); numbers only through their claims. Caption tier (64 px @1080) for every line, title
// in head tier; one line at a time (0.3 s apart), then held. The scene is padded (make_timing.py) so the full card stays
// >= 1 s per 3 words.
import { H2, C, CLS, ease } from './film.js';
const CARD = await (await fetch('/episodes/ep002/animatic/src/method_card.json')).json();
export function build({ T }) {
  const t0 = T.a('card') + 0.3;
  function line(ctx, parts, x, y, tier, a, color) {
    for (const [s, id] of parts) { const str = id ? CLS(id, s) : s; H2.text(ctx, str, x, y, tier, { alpha: a, color }); x += H2.measure(ctx, str, tier); }
  }
  return {
    reveal: { t0, step: 0.3, lines: CARD.lines.length },
    draw(ctx, t) {
      line(ctx, CARD.title, 96, 150, 'head', ease(t, t0, t0 + 0.3), C.muted);
      CARD.lines.forEach((l, i) => line(ctx, l.parts, 96, 285 + i * 92, 'caption', ease(t, t0 + 0.3 * (i + 1), t0 + 0.3 * (i + 1) + 0.3), C.ink));
      H2.badge(ctx, ease(t, t0, t0 + 0.3));
    },
  };
}
