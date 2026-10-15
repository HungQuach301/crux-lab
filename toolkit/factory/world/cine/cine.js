// F-17 · LỚP ÁNH SÁNG ĐIỆN ẢNH của nhà máy (opt-in: spine.json có khoá `cine`; mặc định TẮT). Chuyển từ rnd-hybrid/v4/light/cine.js @ ba5d27f8.
// KHÔNG sửa core.js / lib3d.js / scene.js của tập: trang cine.html gọi install(spine.cine) TRƯỚC boot cảnh, prepare(frame) SAU boot.
// install vá THREE.WebGLRenderer.prototype.render bằng accessor: lần gán đầu (three, trong hàm dựng) được cất vào __cineOrig; core.Stage bọc
// renderer.render như cũ → mỗi lần cảnh gọi renderer.render(scene, cam), lớp vẽ qua EffectComposer:
//   RenderPass (MSAA 4, không vẽ vật dữ liệu) → [GTAO, nửa độ phân giải, CHỈ cảnh cận] → [DOF độ sâu nới, CHỈ cảnh cận] → OutputPass (ACES + sRGB)
//   → KHOÁ MÀU DỮ LIỆU → GRADE (curve theo hồi, bão hoà, viền tối, hạt phim tất định; điểm ảnh dữ liệu không qua grade/viền tối).
// Lần render bên trong composer đi thẳng xuống hàm gốc (cờ busy) → nhật ký/khung dọc/dither của core giữ nguyên. Lớp chữ 2D không qua hậu kỳ.
// Tất định: không Math.random lúc vẽ; SimplexNoise của GTAO dựng khi Math.random bị thay tạm bằng LCG có hạt; hạt phim = băm(điểm ảnh, khung).
//
// spine.cine = { look: 'day'|'afternoon'|'dusk', sky?: 0.55, lock?: true, layers?: {hdri,tex,soft,rim,ao,dof,grade,lock},
//   shots?: { <id shot của spine> | '*': { shot: 'close', focus?: 'char'|'center'|<m>, focusXY?, aperture?: 0.9, silhouette?: true, override?: {keyAz…} } },
//   override?: {…tham số hồi}, aoHalf?: true, dofDilate?: true, roofMinPx?, v4?: false }
//   - DOF và AO chỉ bật ở shot khai `shot: 'close'` (v4: mọi shot). AO ở nửa độ phân giải (aoHalf).
//   - Người: giữ màu nhận diện, thêm viền theo hướng đèn chính (phía xa đèn = 0); thân sẫm (bóng tối) chỉ khi shot khai `silhouette: true`.
//   - v4: true = cấu hình nguyên mẫu (AO + DOF mọi shot, không khoá màu, người bóng tối, viền sàn 0,15, bokeh không nới độ sâu) — chỉ để đối chứng.
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { GTAOPass } from 'three/addons/postprocessing/GTAOPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';
import { ShaderPass } from 'three/addons/postprocessing/ShaderPass.js';
import { Pass, FullScreenQuad } from 'three/addons/postprocessing/Pass.js';
import { HDRLoader } from 'three/addons/loaders/HDRLoader.js';
import { LOOKS, ROLES, DATA_ROLES, DATA_ENV_MAX } from './looks.js';

const A = '/toolkit/factory/world/cine/assets/';
let MAN = null;
async function manifest() { return MAN || (MAN = await (await fetch(A + 'manifest.json')).json()); }
// tệp ≤ 2 MB commit ở cc0/; lớn hơn tải lúc dựng vào dl/ (fetch.py, kiểm SHA-256) — .gitignore
const fileUrl = (m) => A + (m.commit ? 'cc0/' : 'dl/') + m.file;
async function bytes(id) { const m = (await manifest())[id]; const r = await fetch(fileUrl(m)); if (!r.ok) throw new Error('cine: thiếu tài sản ' + m.file + ' (chạy fetch.py)'); return r.arrayBuffer(); }
async function texture(id, srgb) {
  const b = await bytes(id), url = URL.createObjectURL(new Blob([b], { type: 'image/jpeg' }));
  const t = await new THREE.TextureLoader().loadAsync(url); URL.revokeObjectURL(url);
  t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = 4; if (srgb) t.colorSpace = THREE.SRGBColorSpace; return t;
}
async function hdri(look) {
  const d = new HDRLoader().parse(await bytes('hdri-' + look)), t = new THREE.DataTexture(d.data, d.width, d.height, THREE.RGBAFormat, d.type);
  t.colorSpace = THREE.LinearSRGBColorSpace; t.mapping = THREE.EquirectangularReflectionMapping; t.flipY = true;
  t.minFilter = t.magFilter = THREE.LinearFilter; t.generateMipmaps = false; t.needsUpdate = true; return t;
}
function seeded(fn, seed = 0xC1E5EED) {   // Math.random tất định trong lúc dựng pass (SimplexNoise của GTAO)
  const r0 = Math.random; let s = seed >>> 0; Math.random = () => ((s = (Math.imul(s, 1664525) + 1013904223) >>> 0) / 4294967296);
  try { return fn(); } finally { Math.random = r0; }
}

// ---------------------------------------------------------------- GRADE: curve theo hồi + bão hoà + viền tối + hạt phim; tLock.a = điểm ảnh dữ liệu
const GradeShader = {
  uniforms: { tDiffuse: { value: null }, tLock: { value: null }, useLock: { value: 0 }, lift: { value: new THREE.Vector3() }, gamma: { value: new THREE.Vector3(1, 1, 1) },
    gain: { value: new THREE.Vector3(1, 1, 1) }, sat: { value: 1 }, contrast: { value: 0 }, vignette: { value: 0 }, grain: { value: 0 }, seed: { value: 0 },
    res: { value: new THREE.Vector2(1920, 1080) } },
  vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
  fragmentShader: `
    uniform sampler2D tDiffuse, tLock; uniform float useLock; uniform vec3 lift, gamma, gain; uniform float sat, contrast, vignette, grain, seed; uniform vec2 res; varying vec2 vUv;
    float h(vec2 p){ p = fract(p * vec2(443.897, 441.423) + seed); p += dot(p, p.yx + 19.19); return fract((p.x + p.y) * p.x); }
    void main(){
      vec3 c0 = texture2D(tDiffuse, vUv).rgb, c = c0;                         // sRGB sau OutputPass
      c = clamp(gain * (c + lift * (1.0 - c)), 0.0, 1.0); c = pow(c, 1.0 / gamma);
      c = mix(c, c * c * (3.0 - 2.0 * c), contrast);
      float l = dot(c, vec3(0.2126, 0.7152, 0.0722)); c = mix(vec3(l), c, sat);
      vec2 q = vUv - 0.5; q.x *= res.x / res.y; c *= 1.0 - vignette * smoothstep(0.35, 1.05, length(q));
      c = mix(c, c0, useLock * texture2D(tLock, vUv).a);                       // khoá màu: điểm ảnh dữ liệu giữ màu trước grade/viền tối
      vec2 px = floor(vUv * res / max(1.0, res.y / 1080.0));
      float n = (h(px) + h(px + 17.0) - 1.0);
      float lc = dot(c, vec3(0.2126, 0.7152, 0.0722)), w = 4.0 * lc * (1.0 - lc) + 0.15;
      gl_FragColor = vec4(c + grain * n * w, 1.0);
    }`,
};

// ---------------------------------------------------------------- DOF có xét độ sâu (thay BokehPass của three, không sửa vendor)
// v4: mẫu GẦN máy hơn điểm đang xét > 0,35 m bị bỏ → nền mờ không mang màu tiền cảnh. F-17 sửa vệt trên đầu: bộ đệm màu MSAA có điểm ảnh mép
// pha tiền cảnh + nền trong khi độ sâu (không MSAA) ghi nền → điểm mép sáng bị nền mờ hút vào thành vệt. Độ sâu được NỚI (lấy điểm gần nhất
// trong ô 3×3) trước khi gom mẫu → điểm mép tính là tiền cảnh (sắc, và bị nền bỏ qua). dilate: false = đúng fragment v4 (đối chứng T8).
const BOKEH_OFFS = (() => { const r1 = [[0, 0.4], [0.15, 0.37], [0.29, 0.29], [-0.37, 0.15], [0.4, 0], [0.37, -0.15], [0.29, -0.29], [-0.15, -0.37], [0, -0.4], [-0.15, 0.37], [-0.29, 0.29], [0.37, 0.15], [-0.4, 0], [-0.37, -0.15], [-0.29, -0.29], [0.15, -0.37]];
  const r9 = [[0.15, 0.37], [-0.37, 0.15], [0.37, -0.15], [-0.15, -0.37], [-0.15, 0.37], [0.37, 0.15], [-0.37, -0.15], [0.15, -0.37]];
  const r7 = [[0.29, 0.29], [0.4, 0], [0.29, -0.29], [0, -0.4], [-0.29, 0.29], [-0.4, 0], [-0.29, -0.29], [0, 0.4]];
  return [...r1.map((o) => [...o, 1]), ...r9.map((o) => [...o, 0.9]), ...r7.map((o) => [...o, 0.7]), ...r7.map((o) => [...o, 0.4])]; })();
const VS = 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }';
const BOKEH_FRAG = `#include <common>
  varying vec2 vUv; uniform sampler2D tColor; uniform sampler2D tDepth; uniform float maxblur, aperture, nearClip, farClip, focus, aspect;
  #include <packing>
  float vz(vec2 p){ return perspectiveDepthToViewZ(unpackRGBAToDepth(texture2D(tDepth, p)), nearClip, farClip); }
  void main(){
    vec2 ac = vec2(1.0, aspect); float z0 = vz(vUv); vec2 b = vec2(clamp((focus + z0) * aperture, -maxblur, maxblur));
    vec4 col = texture2D(tColor, vUv); float wsum = 1.0; vec2 q; float w;
    ${BOKEH_OFFS.map(([x, y, k]) => `q = vUv + vec2(${x.toFixed(2)}, ${y.toFixed(2)}) * ac * b * ${k.toFixed(1)}; w = step(vz(q), z0 + 0.35); col += w * texture2D(tColor, q); wsum += w;`).join('\n    ')}
    gl_FragColor = vec4(col.rgb / wsum, 1.0); }`;
const DILATE_FRAG = `#include <common>
  #include <packing>
  varying vec2 vUv; uniform sampler2D tDepth; uniform vec2 texel;
  void main(){ float d = 1.0;
    for (int i = -1; i <= 1; i++) for (int j = -1; j <= 1; j++) d = min(d, unpackRGBAToDepth(texture2D(tDepth, vUv + vec2(float(i), float(j)) * texel)));
    gl_FragColor = packDepthToRGBA(d); }`;
class DofPass extends Pass {
  constructor(scene, camera, { aperture = 0.0009, maxblur = 0.008, dilate = true } = {}) {
    super();
    this.scene = scene; this.camera = camera; this.dilate = dilate;
    const rt = () => new THREE.WebGLRenderTarget(1, 1, { minFilter: THREE.NearestFilter, magFilter: THREE.NearestFilter, type: THREE.HalfFloatType });
    this.rtDepth = rt(); this.rtDil = rt();
    this.matDepth = new THREE.MeshDepthMaterial({ depthPacking: THREE.RGBADepthPacking, blending: THREE.NoBlending });
    this.matDil = new THREE.ShaderMaterial({ uniforms: { tDepth: { value: this.rtDepth.texture }, texel: { value: new THREE.Vector2() } }, vertexShader: VS, fragmentShader: DILATE_FRAG });
    this.uniforms = { tColor: { value: null }, tDepth: { value: null }, focus: { value: 10 }, aspect: { value: camera.aspect }, aperture: { value: aperture },
      maxblur: { value: maxblur }, nearClip: { value: camera.near }, farClip: { value: camera.far } };
    this.matBokeh = new THREE.ShaderMaterial({ uniforms: this.uniforms, vertexShader: VS, fragmentShader: BOKEH_FRAG });
    this.quad = new FullScreenQuad(this.matBokeh); this.cc = new THREE.Color();
  }
  render(renderer, writeBuffer, readBuffer) {
    renderer.getClearColor(this.cc); const ca = renderer.getClearAlpha(), ac = renderer.autoClear; renderer.autoClear = false;
    this.scene.overrideMaterial = this.matDepth; const bg = this.scene.background; this.scene.background = null;
    renderer.setClearColor(0xffffff, 1); renderer.setRenderTarget(this.rtDepth); renderer.clear(); renderer.__cineOrig(this.scene, this.camera);
    this.scene.overrideMaterial = null; this.scene.background = bg;
    if (this.dilate) { this.quad.material = this.matDil; renderer.setRenderTarget(this.rtDil); this.quad.render(renderer); }
    this.uniforms.tDepth.value = (this.dilate ? this.rtDil : this.rtDepth).texture;
    this.uniforms.tColor.value = readBuffer.texture; this.uniforms.nearClip.value = this.camera.near; this.uniforms.farClip.value = this.camera.far;
    this.uniforms.aspect.value = this.camera.aspect;
    this.quad.material = this.matBokeh; renderer.setRenderTarget(this.renderToScreen ? null : writeBuffer); if (!this.renderToScreen) renderer.clear(); this.quad.render(renderer);
    renderer.setClearColor(this.cc, ca); renderer.autoClear = ac;
  }
  setSize(w, h) { this.rtDepth.setSize(w, h); this.rtDil.setSize(w, h); this.matDil.uniforms.texel.value.set(1 / w, 1 / h); }
}

// ---------------------------------------------------------------- KHOÁ MÀU DỮ LIỆU (F-17 mục 3)
// Vật dữ liệu được vẽ lại dưới ÁNH SÁNG GỐC của cảnh (đèn/sương như khi không có lớp, không HDRI/nền trời) vào một bộ đệm riêng; vật khác chỉ ghi
// độ sâu (che đúng), vật trong suốt khác và đường/sprite không dữ liệu bị ẩn. Ghép sau OutputPass: màu = ảnh lớp × (1 − α) + ảnh khoá (nhân sẵn α).
// Grade/viền tối bỏ qua điểm ảnh có α (GradeShader.tLock). Kết quả: màu dữ liệu sau lớp ≈ trước lớp (luật cine_color.py đo ΔE2000/thứ tự sáng).
const LOCK_FRAG = `varying vec2 vUv; uniform sampler2D tDiffuse, tLock;
  void main(){ vec4 s = texture2D(tDiffuse, vUv), l = texture2D(tLock, vUv); gl_FragColor = vec4(s.rgb * (1.0 - l.a) + l.rgb, s.a); }`;
class LockPass extends Pass {
  constructor(state) {
    super(); this.state = state;
    // vẽ NHƯ RA CANVAS: three chỉ tone-map + mã sRGB trong shader khi đích là màn hình hoặc RT XR → cờ isXRRenderTarget trên RT riêng này
    // (không dùng WebXR) → vật bán trong suốt pha trộn trong không gian sRGB đã tone-map, đúng như trang không lớp (đo lần 1: đường lãi mờ dần
    // pha ở không gian tuyến tính sáng hơn gốc ΔE 15)
    this.rt = new THREE.WebGLRenderTarget(1, 1, { type: THREE.HalfFloatType, samples: 4 }); this.rt.texture.colorSpace = THREE.SRGBColorSpace; this.rt.isXRRenderTarget = true;
    this.mat = new THREE.ShaderMaterial({ uniforms: { tDiffuse: { value: null }, tLock: { value: this.rt.texture } }, vertexShader: VS, fragmentShader: LOCK_FRAG });
    this.quad = new FullScreenQuad(this.mat); this.cc = new THREE.Color();
  }
  render(renderer, writeBuffer, readBuffer) {
    const st = this.state;
    st.baseScene(true, (scene, cam) => {
      renderer.getClearColor(this.cc); const ca = renderer.getClearAlpha();
      renderer.setRenderTarget(this.rt); renderer.setClearColor(0x000000, 0); renderer.clear(); renderer.__cineOrig(scene, cam); renderer.setClearColor(this.cc, ca);
    });
    this.mat.uniforms.tDiffuse.value = readBuffer.texture; renderer.setRenderTarget(this.renderToScreen ? null : writeBuffer); this.quad.render(renderer);
  }
  setSize(w, h) { this.rt.setSize(w, h); }
}

// ---------------------------------------------------------------- người viền sáng (mục 4): giữ Person của lib3d, không mặt
// Viền = Fresnel × max(0, n·hướng tới đèn chính) → phía xa đèn = 0 (v4: sàn 0,15 → viền chạy quanh cả khối, đọc thành "nét dán").
const RIMDIR = new THREE.Vector3(0, 1, 0);   // hướng TỚI đèn chính trong toạ độ máy quay, cập nhật mỗi khung
function rimify(mat, base, rim, strength, power, floor) {
  const m = mat.clone(); if (base) { m.color.set(base); m.roughness = 0.9; m.metalness = 0; } m.envMapIntensity = 0.25;
  const U = { rimColor: { value: new THREE.Color(rim) }, rimK: { value: new THREE.Vector3(strength, power, floor) }, rimDir: { value: RIMDIR } };
  m.userData.rim = U;
  m.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, U);
    sh.fragmentShader = sh.fragmentShader.replace('#include <common>', '#include <common>\nuniform vec3 rimColor; uniform vec3 rimK; uniform vec3 rimDir;')
      .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
        { float fr = 1.0 - abs(dot(normalize(-vViewPosition), normal));
          float side = rimK.z + 1.6 * max(0.0, dot(normal, rimDir));
          totalEmissiveRadiance += rimColor * rimK.x * side * pow(fr, rimK.y); }`);
  };
  m.customProgramCacheKey = () => `rim:${strength}:${power}:${floor}:${!!base}`;
  return m;
}

const isData = (o, roles) => { for (let p = o; p; p = p.parent) { const r = p.userData && p.userData.checks && p.userData.checks.role; if (r && roles.includes(r)) return true; } return false; };
const isChar = (o) => { for (let p = o; p; p = p.parent) if (p.userData && p.userData.checks && p.userData.checks.char) return true; return false; };
const visibleChain = (o) => { for (let p = o; p; p = p.parent) if (!p.visible) return false; return true; };
const opac = (m) => Math.min(...[].concat(m).map((q) => (q.opacity ?? 1)));

export function install(opts = {}) {
  const V4 = !!opts.v4;
  const DEF = { hdri: true, tex: true, soft: true, rim: true, ao: true, dof: true, grade: true, lock: !V4 };
  const O = { look: 'day', sky: 0.55, aoHalf: !V4, dofDilate: !V4, dataRoles: DATA_ROLES, shots: {}, shotList: [], ...opts };
  O.layers = { ...DEF, ...(opts.layers || {}) }; if (opts.lock === false) O.layers.lock = false;
  if (typeof window !== 'undefined' && window.CINE_LAYERS) Object.assign(O.layers, window.CINE_LAYERS);   // đo giờ máy / đối chứng: bật/tắt từng lớp
  if (!opts.off && !LOOKS[O.look]) throw new Error('cine: look ' + O.look);
  const L0 = { ...(LOOKS[O.look] || {}), ...(O.override || {}) };
  const off = !!opts.off || !Object.values(O.layers).some(Boolean);
  const proto = THREE.WebGLRenderer.prototype;
  const orig = function (scene, cam) { return this.__cineOrig(scene, cam); };
  const state = { t: 0, busy: false, comp: null, passes: {}, scene: null, cam: null, renderer: null, key: null, people: [], data: [], roofs: [], orig: null,
    cfg: {}, stats: { roofPlain: 0, roofTex: 0, roofSmallTex: 0 }, cap: null };
  // cấu hình theo shot của spine (t ∈ [t0, t1)) → {shot, focus, aperture, silhouette, override}
  const shotAt = (t) => { const s = O.shotList.find((x) => t >= x.t0 - 1e-6 && t < x.t1 - 1e-6) || O.shotList[O.shotList.length - 1]; return { ...(O.shots['*'] || {}), ...((s && O.shots[s.id]) || {}) }; };

  // trạng thái "gốc" của cảnh để vẽ vật dữ liệu (khoá màu) và mặt nạ đo: đèn/sương/nền như khi không có lớp
  const occ = { 0: new THREE.MeshBasicMaterial({ colorWrite: false, side: THREE.FrontSide }), 1: new THREE.MeshBasicMaterial({ colorWrite: false, side: THREE.BackSide }),
    2: new THREE.MeshBasicMaterial({ colorWrite: false, side: THREE.DoubleSide }) };
  state.baseScene = (keepLight, draw, dataMat) => {
    const sc = state.scene, cam = state.cam, sv = { bg: sc.background, env: sc.environment, fog: sc.fog && sc.fog.color.clone(), fogO: sc.fog };
    const lights = [], mats = [], hid = [];
    sc.background = null; sc.environment = null;
    if (keepLight) {
      if (sc.fog && state.orig.fog) sc.fog.color.copy(state.orig.fog);
      for (const [l, o] of state.orig.lights) { lights.push([l, l.color.clone(), l.intensity, l.groundColor && l.groundColor.clone(), l.position.clone()]); l.color.copy(o.color); l.intensity = o.intensity; if (o.ground) l.groundColor.copy(o.ground); }
      if (state.key && state.keyScenePos) state.key.position.copy(state.keyScenePos);
      // tham số bóng gốc (bóng mềm đổi bias/normalBias/radius → vật dữ liệu tự đổ bóng khác bản gốc: lần build đầu, đoạn a t = 24,1 s, dải tuần tối 8 %)
      if (state.key && state.orig.shadow) { const sh = state.key.shadow; sv.sh = { bias: sh.bias, normalBias: sh.normalBias, radius: sh.radius, blurSamples: sh.blurSamples }; Object.assign(sh, state.orig.shadow); }
    } else sc.fog = null;
    sc.traverse((o) => {
      if (!o.visible) return;
      const data = state.dataSet.has(o);
      if (o.isMesh) {
        if (data) { if (dataMat) { mats.push([o, o.material]); o.material = dataMat(o); } return; }
        const m = o.material; if (!m) return;
        if (opac(m) < 0.99 || [].concat(m).some((q) => q.colorWrite === false)) { o.visible = false; hid.push(o); return; }
        mats.push([o, m]); o.material = occ[[].concat(m)[0].side] || occ[2];
      } else if ((o.isLine || o.isPoints || o.isSprite) && !data) { o.visible = false; hid.push(o); }
    });
    try { draw(sc, cam); } finally {
      for (const [o, m] of mats) o.material = m; for (const o of hid) o.visible = true;
      for (const [l, c, i, g, p] of lights) { l.color.copy(c); l.intensity = i; if (g) l.groundColor.copy(g); l.position.copy(p); }
      sc.background = sv.bg; sc.environment = sv.env; sc.fog = sv.fogO; if (sv.fog && sc.fog) sc.fog.color.copy(sv.fog);
      if (sv.sh && state.key) Object.assign(state.key.shadow, sv.sh);
    }
  };

  const prep = async (renderer, scene, cam) => {
    state.scene = scene; state.cam = cam; state.renderer = renderer;
    const ly = O.layers, L = L0;
    // ánh sáng gốc (trước mọi thay đổi) cho khoá màu
    state.orig = { fog: scene.fog ? scene.fog.color.clone() : null, lights: [], background: scene.background, backgroundIntensity: scene.backgroundIntensity };
    scene.traverse((o) => { if (o.isLight) state.orig.lights.push([o, { color: o.color.clone(), intensity: o.intensity, ground: o.groundColor ? o.groundColor.clone() : null }]); });
    // vật dữ liệu (role series/bar/grid và con của chúng) — không vân, phản xạ ≤ DATA_ENV_MAX
    state.dataSet = new Set(); scene.traverse((o) => { if (isData(o, O.dataRoles)) state.dataSet.add(o); });
    // vật liệu dùng chung giữa vật dữ liệu và vật khác → bản sao riêng cho vật dữ liệu (khoá màu đổi colorWrite của vật liệu dữ liệu)
    const nonData = new Set(); scene.traverse((o) => { if (o.isMesh && !state.dataSet.has(o)) for (const m of [].concat(o.material)) nonData.add(m); });
    for (const o of state.dataSet) if (o.isMesh) {
      if (Array.isArray(o.material)) o.material = o.material.map((m) => (nonData.has(m) ? m.clone() : m)); else if (nonData.has(o.material)) o.material = o.material.clone();
      for (const m of [].concat(o.material)) { if ('envMapIntensity' in m) m.envMapIntensity = Math.min(L.dataEnv ?? DATA_ENV_MAX, DATA_ENV_MAX); }
    }
    // --- HDRI → PMREM + nền trời + sương cùng màu chân trời
    if (ly.hdri) {
      const eq = await hdri(O.look), pm = new THREE.PMREMGenerator(renderer), env = pm.fromEquirectangular(eq).texture; pm.dispose();
      scene.environment = env; scene.environmentIntensity = L.env; scene.environmentRotation = new THREE.Euler(0, L.envRot || 0, 0);
      state.eq = eq;
      if (O.sky > 0) { scene.background = eq; scene.backgroundBlurriness = 0; scene.backgroundIntensity = L.skyI * O.sky; scene.backgroundRotation = new THREE.Euler(0, L.envRot || 0, 0); }
      if (scene.fog && O.sky > 0) scene.fog.color.set(L.fog);
      scene.traverse((o) => { if (o.isHemisphereLight) { o.intensity *= L.hemiK; o.color.set(L.hemiSky); o.groundColor.set(L.hemiGround); }
        if (o.isDirectionalLight && !o.castShadow) { o.color.set(L.rim); o.intensity = L.rimI; } });
    }
    scene.traverse((o) => { if (o.isDirectionalLight && o.castShadow) state.key = o; });
    if (state.key) { const sh = state.key.shadow; state.orig.shadow = { bias: sh.bias, normalBias: sh.normalBias, radius: sh.radius, blurSamples: sh.blurSamples }; }
    if (state.key && ly.hdri) { state.key.color.set(L.key); state.key.intensity = L.keyI; }
    // --- bóng mềm: PCF + đĩa Vogel, bản đồ 2048
    if (ly.soft && state.key) { const s = state.key.shadow; s.mapSize.set(2048, 2048); s.radius = L.shadowRadius; s.blurSamples = 16; s.bias = -0.0004; s.normalBias = 0.02; s.map?.dispose(); s.map = null; }
    // --- vân CC0 theo vai trò (màu gốc → vai trò); vật dữ liệu và nhân vật không bao giờ nhận vân
    if (ly.tex) {
      const T = {}; for (const r of Object.keys(ROLES)) T[r] = { map: await texture(`tex-${r}-diff`, true), normalMap: await texture(`tex-${r}-nor_gl`, false), roughnessMap: await texture(`tex-${r}-rough`, false) };
      const done = new Map();
      scene.traverse((o) => {
        if (!o.isMesh || !o.material || Array.isArray(o.material) || !o.material.isMeshStandardMaterial) return;
        if (state.dataSet.has(o) || isChar(o)) return;
        const hex = '#' + o.material.color.getHexString().toUpperCase(), role = Object.keys(ROLES).find((r) => ROLES[r].colors.includes(hex));
        if (!role) return;
        const R = ROLES[role], key = o.material.uuid + role;
        if (!done.has(key)) {
          const m = o.material.clone();
          for (const k of R.noMap ? ['normalMap', 'roughnessMap'] : ['map', 'normalMap', 'roughnessMap']) { const t = T[role][k].clone(); t.repeat.set(R.repeat, R.repeat); t.needsUpdate = true; m[k] = t; }
          if (R.tint) m.color.set(R.tint); m.normalScale = new THREE.Vector2(R.normal, R.normal); m.roughness = 1; m.needsUpdate = true;
          done.set(key, m);
        }
        if (role === 'roof' && !V4) { o.geometry.computeBoundingSphere(); state.roofs.push({ o, plain: o.material, tex: done.get(key) }); }
        o.material = done.get(key);
      });
    }
    // --- người: viền theo đèn (giữ màu nhận diện) | bóng tối khi shot khai silhouette (v4: luôn bóng tối, viền sàn 0,15)
    if (ly.rim) {
      scene.traverse((o) => {
        if (!(o.userData.checks && o.userData.checks.char)) return;
        // chỉ NGƯỜI (Person của lib3d: thân CapsuleGeometry + đầu SphereGeometry cùng vật liệu) — vật của nhân vật (chồng tiền của Leo cũng mang
        // checks.char) không bị đổi vật liệu (lần đo đầu cảnh g: chồng tiền vàng nhận viền)
        const body = o.children.find((c) => c.isMesh && c.geometry && c.geometry.type === 'CapsuleGeometry'), bodyM = body && body.material;
        if (!bodyM || state.dataSet.has(body) || !o.children.some((c) => c.isMesh && c.material === bodyM && c.geometry.type === 'SphereGeometry')) return;
        const ms = new Map();
        o.traverse((c) => { if (!c.isMesh || c.material !== bodyM) return; const k = c.material.uuid;   // thân/đầu/tay (cùng material thân), không vật cầm tay
          if (!ms.has(k)) { const id = c.material.color.clone(), rc = new THREE.Color(L.rimPerson).lerp(id, 0.25).getStyle();
            ms.set(k, { id: V4 ? null : rimify(c.material, null, rc, L.rimK, 2.6, 0),
              sil: rimify(c.material, id.clone().multiplyScalar(L.silhouette).getStyle(), rc, L.rimKSil, 2.6, V4 ? 0.15 : 0) }); }
          c.userData.cineRim = ms.get(k); });
        state.people.push(o);
      });
    }
    // --- composer
    const W = renderer.domElement.width, H = renderer.domElement.height;
    const rt = new THREE.WebGLRenderTarget(W, H, { type: THREE.HalfFloatType, samples: 4 });
    const comp = new EffectComposer(renderer, rt); comp.setPixelRatio(1);
    const rp = new RenderPass(scene, cam);
    if (ly.lock) {   // khoá màu: ảnh lớp KHÔNG vẽ vật dữ liệu (vẫn đổ bóng: bản đồ bóng không đọc colorWrite) → pass khoá ghép chúng đúng một lần
      const r0 = rp.render.bind(rp);   // (vật bán trong suốt vẽ hai lần thì sáng hơn gốc — lần đo đầu cảnh c, t = 26,4 s)
      rp.render = (...a) => { const sv = [], ms = new Set(); for (const o of state.dataSet) if (o.isMesh) for (const m of [].concat(o.material)) ms.add(m);
        for (const m of ms) { sv.push([m, m.colorWrite, m.depthWrite]); m.colorWrite = false; m.depthWrite = false; }
        try { r0(...a); } finally { for (const [m, c, d] of sv) { m.colorWrite = c; m.depthWrite = d; } } };
    }
    comp.addPass(rp);
    if (ly.ao) { const ao = seeded(() => new GTAOPass(scene, cam, W, H)); ao.output = 0; ao.blendIntensity = L.ao;
      if (O.aoHalf) { const ss = ao.setSize.bind(ao); ao.setSize = (w, h) => ss(Math.ceil(w / 2), Math.ceil(h / 2)); }
      ao.updateGtaoMaterial({ radius: 0.6, distanceExponent: 1.5, thickness: 1.2, scale: 1, samples: 16, distanceFallOff: 1 });
      ao.updatePdMaterial({ lumaPhi: 10, depthPhi: 2, normalPhi: 3, radius: 6, rings: 2, samples: 16 }); comp.addPass(ao); state.passes.ao = ao; }
    if (ly.dof) { const b = new DofPass(scene, cam, { aperture: 0.0009, maxblur: 0.008, dilate: O.dofDilate }); comp.addPass(b); state.passes.dof = b; }
    comp.addPass(new OutputPass());
    if (ly.lock) { const lk = new LockPass(state); comp.addPass(lk); state.passes.lock = lk; }   // ghép sau OutputPass (không gian hiển thị); DOF không làm mờ vật dữ liệu
    if (ly.grade) { const g = new ShaderPass(GradeShader); g.uniforms.res.value.set(W, H); for (const k of ['lift', 'gamma', 'gain']) g.uniforms[k].value.set(...L.grade[k]);
      g.uniforms.sat.value = L.grade.sat; g.uniforms.contrast.value = L.grade.contrast; g.uniforms.vignette.value = L.grade.vignette; g.uniforms.grain.value = L.grade.grain;
      if (state.passes.lock) g.uniforms.tLock.value = state.passes.lock.rt.texture; comp.addPass(g); state.passes.grade = g; }
    comp.setSize(W, H);
    state.comp = comp;
  };
  const ray = new THREE.Raycaster(), v = new THREE.Vector3(), d = new THREE.Vector3(), sph = new THREE.Sphere();
  function focusDist(cam, cfg) {
    const f = cfg.focus ?? O.focus ?? 'center';
    if (typeof f === 'number') return f;
    cam.getWorldDirection(d);
    if (f === 'char' && state.people.length) { const p = state.people[cfg.focusIndex || 0]; p.getWorldPosition(v); v.y += 0.6; return Math.max(0.5, v.sub(cam.position).dot(d)); }
    const xy = cfg.focusXY || O.focusXY || [0, 0];
    ray.setFromCamera(new THREE.Vector2(xy[0], xy[1]), cam);
    const hit = ray.intersectObjects(state.scene.children, true).find((h) => visibleChain(h.object) && h.object.material && !(opac(h.object.material) < 0.5) && h.object.userData.role !== 'bg');
    return hit ? hit.distance : 20;
  }
  // mỗi khung: cấu hình shot → bật/tắt AO/DOF, vật liệu người, vân mái theo cỡ chiếu, đèn chính theo hồi, khoá màu chỉ khi có vật dữ liệu hiện
  function perFrame(renderer, scene, cam) {
    const cfg = state.cfg = shotAt(state.t), close = V4 || cfg.shot === 'close', L = { ...L0, ...(cfg.override || {}) };
    if (state.passes.ao) state.passes.ao.enabled = close;
    if (state.passes.dof) { state.passes.dof.enabled = close && !state._forceDofOff; if (close) { state.passes.dof.uniforms.aperture.value = (cfg.aperture ?? O.aperture ?? 0.9) * 0.001; state.passes.dof.uniforms.focus.value = focusDist(cam, cfg); } }
    // trời theo shot (cfg.sky): shot có vật dữ liệu BÁN TRONG SUỐT trên nền trời khai sky: 0 — trời sáng sau dữ liệu trong suốt làm màu dữ liệu đọc
    // sáng hơn (lần build đầu, đoạn a t = 26,2 s: dải tuần ΔE 6,9 → luật CHẶN)
    if (state.eq) { const sk = cfg.sky ?? O.sky; if (sk > 0) { scene.background = state.eq; scene.backgroundIntensity = L.skyI * sk; } else { scene.background = state.orig.background; scene.backgroundIntensity = state.orig.backgroundIntensity ?? 1; }
      if (scene.fog && state.orig.fog) scene.fog.color.copy(sk > 0 ? new THREE.Color(L.fog) : state.orig.fog); }
    const sil = V4 || cfg.silhouette === true;
    for (const p of state.people) p.traverse((c) => { const r = c.userData.cineRim; if (r) c.material = sil ? r.sil : r.id; });
    if (state.passes.lock) {
      let any = false; for (const o of state.dataSet) if (o.isMesh && !any && visibleChain(o) && opac(o.material) > 0.01) any = true;
      state.passes.lock.enabled = any; if (state.passes.grade) state.passes.grade.uniforms.useLock.value = any ? 1 : 0;
    }
    if (state.roofs.length) {
      const H = renderer.domElement.height, k = H / (2 * Math.tan(cam.fov * Math.PI / 360)), min = (O.roofMinPx ?? ROLES.roof.minPx) * H / 1080;
      for (const r of state.roofs) {
        sph.copy(r.o.geometry.boundingSphere).applyMatrix4(r.o.matrixWorld); const dist = Math.max(0.01, sph.center.distanceTo(cam.position));
        const px = 2 * sph.radius * k / dist, big = px >= min; r.o.material = big ? r.tex : r.plain;
        if (visibleChain(r.o)) { if (big) state.stats.roofTex++; else state.stats.roofPlain++; }
      }
    }
    if (state.key) state.keyScenePos = state.key.position.clone();   // vị trí đèn cảnh đặt (khoá màu vẽ dưới đèn này)
    if (state.key && O.layers.hdri) { const k = state.key, tg = k.target.position; const el = L.keyEl * Math.PI / 180, az = L.keyAz * Math.PI / 180, r = 18;
      k.position.set(tg.x + r * Math.cos(el) * Math.sin(az), tg.y + r * Math.sin(el), tg.z + r * Math.cos(el) * Math.cos(az)); k.target.updateMatrixWorld(); }
    if (state.key) { k2.copy(state.key.position).sub(state.key.target.position).normalize(); RIMDIR.copy(k2).transformDirection(cam.matrixWorldInverse); }
    if (state.passes.grade) state.passes.grade.uniforms.seed.value = (Math.round(state.t * 30) % 997) * 0.618034;
  }
  const k2 = new THREE.Vector3();
  const cineRender = function (scene, cam) {
    if (off || state.busy || !scene || !scene.isScene) { if (scene && scene.isScene) state.renderer = this; return orig.call(this, scene, cam); }
    if (!state.comp) { state.cap = [this, scene, cam]; return orig.call(this, scene, cam); }   // trước prepare: vẽ gốc, bắt (renderer, scene, cam)
    perFrame(this, scene, cam);
    state.busy = true;
    try { state.comp.render(); } finally { state.busy = false; }
  };
  Object.defineProperty(proto, 'render', { configurable: true,
    get() { return cineRender; },
    set(fn) { if (!this.__cineOrig) Object.defineProperty(this, '__cineOrig', { value: fn }); else Object.defineProperty(this, 'render', { value: fn, writable: true, configurable: true }); } });

  // ------------------------------------------------------------ đo (cine_check.js): đọc canvas WebGL thuần (không lớp chữ 2D)
  const canvasPx = (src) => { const W = state.renderer.domElement.width, H = state.renderer.domElement.height, c = document.createElement('canvas'); c.width = W; c.height = H;
    const x = c.getContext('2d', { willReadFrequently: true }); x.drawImage(src, 0, 0, W, H); return x.getImageData(0, 0, W, H).data; };
  // mặt nạ nhóm: vật được chọn vẽ phẳng màu gốc (MeshBasic, không đèn, không sương) vào bộ đệm float, vật khác chỉ che → id theo màu gốc
  function groupMask(pick) {
    const r = state.renderer, W = r.domElement.width, H = r.domElement.height;
    const rt = new THREE.WebGLRenderTarget(W, H, { type: THREE.FloatType, minFilter: THREE.NearestFilter, magFilter: THREE.NearestFilter });
    const buf = new Float32Array(W * H * 4), info = new Map();
    const saveSet = state.dataSet; state.dataSet = new Set(); state.scene.traverse((o) => { if (pick(o)) state.dataSet.add(o); });
    try {
      state.baseScene(false, (scene, cam) => { const cc = new THREE.Color(), ca = r.getClearAlpha(); r.getClearColor(cc);
        r.setRenderTarget(rt); r.setClearColor(0x000000, 0); r.clear(); r.__cineOrig(scene, cam); r.setRenderTarget(null); r.setClearColor(cc, ca); },
      (o) => { const m0 = [].concat(o.material)[0]; if (opac(o.material) < 0.5) return occ[2];
        const m = new THREE.MeshBasicMaterial({ color: m0.color ? m0.color.clone() : 0xffffff, vertexColors: !!m0.vertexColors, side: m0.side, toneMapped: false, fog: false });
        info.set(m.uuid, { role: (() => { for (let p = o; p; p = p.parent) { const k = p.userData && p.userData.checks; if (k && (k.role || k.char)) return k.char ? 'char:' + k.char : k.role; } return '?'; })() });
        return m; });
      r.readRenderTargetPixels(rt, 0, 0, W, H, buf);
    } finally { state.dataSet = saveSet; rt.dispose(); }
    // id theo màu (lượng tử 1e-3, tuyến tính) ; canvas đọc từ trên xuống, bộ đệm GL từ dưới lên
    const ids = new Int32Array(W * H).fill(-1), keys = [];
    const kmap = new Map();
    for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
      const i = ((H - 1 - y) * W + x) * 4; if (buf[i + 3] < 0.5) continue;
      const k = `${buf[i].toFixed(3)},${buf[i + 1].toFixed(3)},${buf[i + 2].toFixed(3)}`;
      let id = kmap.get(k); if (id === undefined) { id = keys.length; kmap.set(k, id); keys.push(k); } ids[y * W + x] = id;
    }
    return { W, H, ids, keys };
  }
  function erode(M, r = 2) {   // điểm ảnh giữ lại khi mọi điểm trong ô (2r+1)² cùng id (bỏ mép MSAA/DOF)
    const { W, H, ids } = M, out = new Int32Array(W * H).fill(-1);
    for (let y = r; y < H - r; y++) for (let x = r; x < W - r; x++) { const id = ids[y * W + x]; if (id < 0) continue; let ok = true;
      for (let dy = -r; dy <= r && ok; dy++) for (let dx = -r; dx <= r; dx++) if (ids[(y + dy) * W + x + dx] !== id) { ok = false; break; }
      if (ok) out[y * W + x] = id; }
    return out;
  }
  const lin2hex = (k) => '#' + k.split(',').map((v) => { const c = +v, s = c <= 0.0031308 ? 12.92 * c : 1.055 * c ** (1 / 2.4) - 0.055; return Math.round(Math.min(1, Math.max(0, s)) * 255).toString(16).padStart(2, '0'); }).join('');
  async function img(url) { const im = new Image(); im.src = url; await im.decode(); return im; }
  const meas = {
    // màu dữ liệu: ảnh gốc (trang không lớp, cùng t, PNG) vs ảnh lớp (canvas WebGL hiện tại) trên mặt nạ vật dữ liệu co 2 px → trung bình sRGB mỗi nhóm
    async data(baseUrl, minPx = 200) {
      const cine = canvasPx(state.renderer.domElement), base = canvasPx(await img(baseUrl));
      const M = groupMask((o) => isData(o, O.dataRoles)), E = erode(M), acc = M.keys.map(() => ({ n: 0, b: [0, 0, 0], c: [0, 0, 0] }));
      for (let i = 0; i < E.length; i++) { const id = E[i]; if (id < 0) continue; const a = acc[id], j = i * 4; a.n++; for (let k = 0; k < 3; k++) { a.b[k] += base[j + k]; a.c[k] += cine[j + k]; } }
      return M.keys.map((k, id) => ({ key: lin2hex(k), n: acc[id].n, base: acc[id].b.map((s) => s / Math.max(1, acc[id].n)), cine: acc[id].c.map((s) => s / Math.max(1, acc[id].n)) })).filter((g) => g.n >= minPx);
    },
    // người: (1) ΔE màu thân (ảnh gốc vs lớp); (2) độ sáng viền thêm (L*, khung viền bật − cùng khung viền tắt) ở điểm ảnh GẦN đèn (n·đèn > 0,2)
    // và XA đèn (n·đèn ≤ 0) — n·đèn đọc từ một pass pháp tuyến của chính khối người (không suy từ hướng trên màn hình)
    async rim(baseUrl, frame) {
      const on = canvasPx(state.renderer.domElement), base = canvasPx(await img(baseUrl));
      const U = []; for (const p of state.people) p.traverse((c) => { const m = c.material; if (m && m.userData && m.userData.rim) U.push(m.userData.rim.rimK.value); });
      const k0 = U.map((u) => u.x); U.forEach((u) => { u.x = 0; }); frame(state.t); const offPx = canvasPx(state.renderer.domElement); U.forEach((u, i) => { u.x = k0[i]; }); frame(state.t);
      const pick = (o) => o.isMesh && !!o.userData.cineRim, M = groupMask(pick), E = erode(M, 1), W = M.W, H = M.H;
      const fm = new THREE.ShaderMaterial({ uniforms: { rimDir: { value: RIMDIR } }, vertexShader: 'varying vec3 vN; void main(){ vN = normalize(normalMatrix * normal); gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
        fragmentShader: 'uniform vec3 rimDir; varying vec3 vN; void main(){ gl_FragColor = vec4(dot(normalize(vN), rimDir), 0.0, 0.0, 1.0); }' });
      const r = state.renderer, rt = new THREE.WebGLRenderTarget(W, H, { type: THREE.FloatType, minFilter: THREE.NearestFilter, magFilter: THREE.NearestFilter }), F = new Float32Array(W * H * 4);
      const saveSet = state.dataSet; state.dataSet = new Set(); state.scene.traverse((o) => { if (pick(o)) state.dataSet.add(o); });
      try { state.baseScene(false, (scene, cam) => { r.setRenderTarget(rt); r.setClearColor(0x000000, 0); r.clear(); r.__cineOrig(scene, cam); r.setRenderTarget(null); }, () => fm);
        r.readRenderTargetPixels(rt, 0, 0, W, H, F); } finally { state.dataSet = saveSet; rt.dispose(); }
      const out = [];
      for (let id = 0; id < M.keys.length; id++) {
        const s = { near: [0, 0], far: [0, 0], farIn: [0, 0], base: [0, 0, 0], cine: [0, 0, 0], n: 0 };
        const nlAt = (x, y) => F[((H - 1 - y) * W + x) * 4];
        for (let i = 0; i < E.length; i++) { if (E[i] !== id) continue; const j = i * 4, x = i % W, y = (i / W) | 0, nl = nlAt(x, y);
          const d = Lstar(on, j) - Lstar(offPx, j); s.n++;
          if (nl > 0.2) { s.near[0] += d; s.near[1]++; } else if (nl <= 0) { s.far[0] += d; s.far[1]++;
            // lõi xa đèn: cả ô 3×3 xa đèn (bỏ điểm mép MSAA nơi tay đè thân — điểm pha màu của khối gần đèn) — chẩn đoán, báo cạnh thước gốc
            let core = true; for (let dy = -1; dy <= 1 && core; dy++) for (let dx = -1; dx <= 1; dx++) if (nlAt(x + dx, y + dy) > 0) { core = false; break; }
            if (core) { s.farIn[0] += d; s.farIn[1]++; } }
          for (let k = 0; k < 3; k++) { s.base[k] += base[j + k]; s.cine[k] += on[j + k]; } }
        if (s.n < 200) continue;
        out.push({ key: lin2hex(M.keys[id]), n: s.n, nearDL: s.near[0] / Math.max(1, s.near[1]), farDL: s.far[0] / Math.max(1, s.far[1]), farCoreDL: s.farIn[0] / Math.max(1, s.farIn[1]), nNear: s.near[1], nFar: s.far[1], nFarCore: s.farIn[1],
          base: s.base.map((v) => v / s.n), cine: s.cine.map((v) => v / s.n) });
      }
      return { chars: out, rimK: k0 };
    },
    // vệt DOF trên đầu: dải 1–6 px trên mép trên khối người (mặt nạ không co); trả ảnh DOF bật (dilate | v4) và tắt để tính ΔL* theo cột ở Python
    async streak(frame) {
      const dof = state.passes.dof; if (!dof) return null;
      const grab = () => canvasPx(state.renderer.domElement);
      const dil0 = dof.dilate;
      dof.dilate = true; frame(state.t); const fixed = grab();
      dof.dilate = false; frame(state.t); const v4 = grab();
      state._forceDofOff = true; frame(state.t); const offI = grab();   // DOF tắt một khung (perFrame đọc cờ)
      state._forceDofOff = false; dof.dilate = dil0; frame(state.t);
      const M = groupMask((o) => o.isMesh && !!o.userData.cineRim), W = M.W, H = M.H, top = new Int32Array(W).fill(-1);
      for (let x = 0; x < W; x++) for (let y = 0; y < H; y++) if (M.ids[y * W + x] >= 0) { top[x] = y; break; }
      const cols = [];
      for (let x = 0; x < W; x++) { if (top[x] < 7) continue; const row = { x, fixed: 0, v4: 0 };
        for (let y = top[x] - 6; y <= top[x] - 1; y++) { const j = (y * W + x) * 4;
          row.fixed += (Lstar(fixed, j) - Lstar(offI, j)) / 6; row.v4 += (Lstar(v4, j) - Lstar(offI, j)) / 6; }
        cols.push(row); }
      return { cols: cols.length, maxFixed: Math.max(0, ...cols.map((c) => c.fixed)), maxV4: Math.max(0, ...cols.map((c) => c.v4)),
        p95Fixed: q95(cols.map((c) => c.fixed)), p95V4: q95(cols.map((c) => c.v4)) };
    },
  };
  const Lstar = (a, j) => { const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
    const Y = 0.2126729 * f(a[j]) + 0.7151522 * f(a[j + 1]) + 0.072175 * f(a[j + 2]); return Y > 216 / 24389 ? 116 * Math.cbrt(Y) - 16 : 24389 / 27 * Y; };
  const q95 = (a) => { if (!a.length) return 0; const s = [...a].sort((x, y) => x - y); return s[Math.floor(0.95 * (s.length - 1))]; };
  return {
    state, opts: O, meas,
    // gọi SAU boot cảnh gốc: render khô một khung (vẽ gốc) để bắt (renderer, scene, cam) thật
    async prepare(frame) {
      if (off) return;
      frame(0);
      if (!state.cap) throw new Error('cine: cảnh không gọi renderer.render');
      await prep(...state.cap);
    },
  };
}
