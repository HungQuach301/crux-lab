// R&D v4 · cảnh THẬT Tập 7 (đoạn g, t = 3 s: hai nhà Leo và Tessa) bọc lớp ánh sáng điện ảnh (opt-in). Cảnh gốc không sửa: import boot và bọc.
import { wrap } from '/rnd-hybrid/v4/light/cine.js';
import { boot as inner } from '/episodes/ep007/world/c4/g-s29-s33/scene.js';
export const boot = wrap(inner, { look: 'dusk', focus: 'center', aperture: 0.12 });
