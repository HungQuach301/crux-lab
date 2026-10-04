// S13 · End-screen tail (16 s: take + silence). The ridge as a quiet band at the bottom; one empty slot (grid outline, 16:9)
// where YouTube's end-screen video element goes. No text (the narration says it; README).
import { H3, C, ease } from './film.js';
import { V, ridge } from './lib.js';
export function build({ T }) {
  const t0 = T.a('end');
  return { draw(ctx, t) { const a = ease(t, t0, t0 + 0.8); ridge(ctx, V({ Yt: 780, Yb: 990 }), { alpha: 0.35 * a }); H3.srect(ctx, 640, 170, 640, 360, C.grid, 4, a); } };
}
