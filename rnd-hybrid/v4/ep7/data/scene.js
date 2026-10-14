// R&D v4 · cảnh THẬT Tập 7 (đoạn c, t = 85 s: lưới tuần, cột cao nhất) bọc lớp ánh sáng điện ảnh (opt-in). Cảnh gốc không sửa: import boot và bọc.
import { wrap } from '/rnd-hybrid/v4/light/cine.js';
import { boot as inner } from '/episodes/ep007/world/c4/c-s10-s15/scene.js';
export const boot = wrap(inner, { look: 'afternoon', focus: 'center', aperture: 0.08, sky: 0 });
