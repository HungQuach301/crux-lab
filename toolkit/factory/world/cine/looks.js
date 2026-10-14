// F-17 · BẢNG "HỒI" của lớp ánh sáng điện ảnh (chép rnd-hybrid/v4/light/looks.js @ ba5d27f8, thêm tham số nhà máy).
// Mỗi hồi một HDRI (Poly Haven CC0), một phương đèn chính, một màu sương, một grade. Tập 7: a, b = ngày · c, d, e = chiều · f, g = hoàng hôn.
export const ACT = { a: 'day', b: 'day', c: 'afternoon', d: 'afternoon', e: 'afternoon', f: 'dusk', g: 'dusk' };

const G = (lift, gamma, gain, sat, contrast, vignette, grain) => ({ lift, gamma, gain, sat, contrast, vignette, grain });
// rimK: cường độ viền người khi GIỮ màu nhận diện (mặc định) · rimKSil: khi cảnh khai silhouette (thân sẫm × silhouette, như v4)
export const LOOKS = {
  day: { env: 0.6, envRot: 0.6, skyI: 0.75, fog: '#9AA3AE', hemiK: 0.35, hemiSky: '#D6E2F2', hemiGround: '#3A3530',
    key: '#FFF0DA', keyI: 2.4, keyEl: 42, keyAz: -40, rim: '#CFE0FF', rimI: 0.6, shadowRadius: 7, ao: 1.0,
    silhouette: 0.07, rimPerson: '#FFF4E2', rimK: 0.9, rimKSil: 2.4,
    grade: G([0.015, 0.02, 0.035], [1, 1, 1.02], [1.03, 1.0, 0.96], 0.9, 0.22, 0.32, 0.03) },
  afternoon: { env: 0.55, envRot: 1.4, skyI: 0.7, fog: '#B3A898', hemiK: 0.3, hemiSky: '#E8DCC8', hemiGround: '#3A3028',
    key: '#FFDDB0', keyI: 2.7, keyEl: 28, keyAz: -55, rim: '#BFD4FF', rimI: 0.7, shadowRadius: 6, ao: 1.0,
    silhouette: 0.06, rimPerson: '#FFE6C0', rimK: 1.0, rimKSil: 2.6,
    grade: G([0.02, 0.015, 0.03], [1, 0.99, 1.0], [1.06, 1.0, 0.92], 0.92, 0.26, 0.36, 0.032) },
  dusk: { env: 0.42, envRot: 2.2, skyI: 0.65, fog: '#7C6A66', hemiK: 0.25, hemiSky: '#C9B5C8', hemiGround: '#241C1E',
    key: '#FFB774', keyI: 3.0, keyEl: 14, keyAz: -70, rim: '#9DB6FF', rimI: 0.9, shadowRadius: 9, ao: 1.1,
    silhouette: 0.05, rimPerson: '#FFC894', rimK: 1.1, rimKSil: 3.0,
    grade: G([0.03, 0.02, 0.05], [1, 0.98, 1.0], [1.08, 0.98, 0.88], 0.95, 0.3, 0.42, 0.036) },
};

// Vai trò vật liệu → vân CC0. Nhận theo MÀU vật liệu của lib3d / tập (thư viện không đặt tên mesh). Vật DỮ LIỆU (DATA_ROLES, kể cả con của
// chúng) và nhân vật KHÔNG BAO GIỜ nhận vân, dù màu trùng bảng. noMap: chỉ normal + roughness; tint: màu nền mới khi phủ vân (null = giữ màu).
// roof.minPx: mái có đường kính chiếu < minPx điểm ảnh (ở 1080) dùng vật liệu trơn (vân ngói ở mái nhỏ đọc thành nhiễu đỏ — giới hạn v4).
export const ROLES = {
  road: { colors: ['#161B23'], repeat: 90, normal: 0.6, tint: '#6E7176' },
  wall: { colors: ['#D9D4C7', '#B8BFCA'], repeat: 1, normal: 0.6, tint: null },
  roof: { colors: ['#8A4B3A', '#5F6B7A'], repeat: 0.5, normal: 0.35, tint: '#B87862', minPx: 260 },
  wood: { colors: ['#3B4A5A', '#8C8C88', '#232A35'], repeat: 1, normal: 0.8, tint: null },
  paper: { colors: ['#E9E3D3', '#5E8C6A', '#4E7A5A', '#C9D8C4', '#E9E2CF'], repeat: 1, normal: 0.35, tint: null, noMap: true },
};

// Khoá màu dữ liệu (F-17 mục 3): vai trò checks coi là DỮ LIỆU; phản xạ môi trường trần của chúng.
export const DATA_ROLES = ['series', 'bar', 'grid'];
export const DATA_ENV_MAX = 0.15;
