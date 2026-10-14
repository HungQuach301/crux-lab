// R&D v4 · LỚP ÁNH SÁNG ĐIỆN ẢNH (opt-in, đề xuất F-17). KHÔNG sửa core.js / lib3d.js / scene.js của tập: chỉ import.
// Cách gắn: một scene.js bọc (rnd-hybrid/v4/ep7/<cảnh>/scene.js) gọi install(opts) TRƯỚC khi boot cảnh gốc. install vá
// THREE.WebGLRenderer.prototype.render → Stage() của core bind render0 vào hàm đã vá → mỗi lần cảnh gọi renderer.render(scene, cam)
// lần đầu, lớp dựng một lần (HDRI → PMREM, vân, bóng mềm, người viền sáng) rồi vẽ qua EffectComposer:
//   RenderPass (MSAA 4) → GTAOPass (AO) → BokehPass (độ sâu trường ảnh theo chủ thể) → OutputPass (ACES + sRGB) → GRADE (curve theo hồi,
//   ngả màu, bão hoà, viền tối, hạt phim tất định theo t).
// Các lần renderer.render bên trong composer đi thẳng xuống hàm gốc (cờ busy) → nhật ký/khung dọc/dither của core giữ nguyên.
// Tất định: không Math.random lúc vẽ; SimplexNoise của GTAO dựng khi Math.random bị thay tạm bằng LCG có hạt; hạt phim = băm(điểm ảnh, t).
// Lớp chữ 2D (Overlay) KHÔNG đi qua hậu kỳ: chữ, nhãn, chrome sắc như cũ.
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { GTAOPass } from 'three/addons/postprocessing/GTAOPass.js';
import { BokehPass } from 'three/addons/postprocessing/BokehPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';
import { ShaderPass } from 'three/addons/postprocessing/ShaderPass.js';
import { HDRLoader } from 'three/addons/loaders/HDRLoader.js';
import { LOOKS, ROLES } from './looks.js';

const A = '/rnd-hybrid/v4/assets/';
let MAN = null;
async function manifest() { return MAN || (MAN = await (await fetch(A + 'manifest.json')).json()); }
async function texture(id, srgb) {
  const m = (await manifest())[id], b = await (await fetch(A + 'cc0/' + m.file)).arrayBuffer();
  const url = URL.createObjectURL(new Blob([b], { type: 'image/jpeg' }));
  const t = await new THREE.TextureLoader().loadAsync(url); URL.revokeObjectURL(url);
  t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = 4; if (srgb) t.colorSpace = THREE.SRGBColorSpace; return t;
}
async function hdri(look) {
  const m = (await manifest())['hdri-' + look], b = await (await fetch(A + 'cc0/' + m.file)).arrayBuffer();
  const d = new HDRLoader().parse(b), t = new THREE.DataTexture(d.data, d.width, d.height, THREE.RGBAFormat, d.type);
  t.colorSpace = THREE.LinearSRGBColorSpace; t.mapping = THREE.EquirectangularReflectionMapping; t.flipY = true;
  t.minFilter = t.magFilter = THREE.LinearFilter; t.generateMipmaps = false; t.needsUpdate = true; return t;
}
function seeded(fn, seed = 0xC1E5EED) {   // Math.random tất định trong lúc dựng pass (SimplexNoise của GTAO)
  const r0 = Math.random; let s = seed >>> 0; Math.random = () => ((s = (Math.imul(s, 1664525) + 1013904223) >>> 0) / 4294967296);
  try { return fn(); } finally { Math.random = r0; }
}

// ---------------------------------------------------------------- GRADE: curve theo hồi + ngả màu + bão hoà + viền tối + hạt phim
const GradeShader = {
  uniforms: { tDiffuse: { value: null }, lift: { value: new THREE.Vector3() }, gamma: { value: new THREE.Vector3(1, 1, 1) }, gain: { value: new THREE.Vector3(1, 1, 1) },
    sat: { value: 1 }, contrast: { value: 0 }, vignette: { value: 0 }, grain: { value: 0 }, seed: { value: 0 }, res: { value: new THREE.Vector2(1920, 1080) } },
  vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
  fragmentShader: `
    uniform sampler2D tDiffuse; uniform vec3 lift, gamma, gain; uniform float sat, contrast, vignette, grain, seed; uniform vec2 res; varying vec2 vUv;
    float h(vec2 p){ p = fract(p * vec2(443.897, 441.423) + seed); p += dot(p, p.yx + 19.19); return fract((p.x + p.y) * p.x); }
    void main(){
      vec3 c = texture2D(tDiffuse, vUv).rgb;                                  // sRGB sau OutputPass
      c = clamp(gain * (c + lift * (1.0 - c)), 0.0, 1.0); c = pow(c, 1.0 / gamma);   // lift / gamma / gain (ASC-CDL kiểu đơn giản)
      c = mix(c, c * c * (3.0 - 2.0 * c), contrast);                          // S-curve
      float l = dot(c, vec3(0.2126, 0.7152, 0.0722)); c = mix(vec3(l), c, sat);
      vec2 q = vUv - 0.5; q.x *= res.x / res.y; c *= 1.0 - vignette * smoothstep(0.35, 1.05, length(q));
      vec2 px = floor(vUv * res / max(1.0, res.y / 1080.0));                 // hạt 1 px ở 1080 (cùng cỡ hạt ở mọi độ phân giải)
      float n = (h(px) + h(px + 17.0) - 1.0);                                 // tam giác, trung bình 0
      float w = 4.0 * l * (1.0 - l) + 0.15;                                   // hạt rõ ở trung độ, nhẹ ở đen/trắng
      gl_FragColor = vec4(c + grain * n * w, 1.0);
    }`,
};

// ---------------------------------------------------------------- người viền sáng (2a): giữ Person của lib3d, không mặt
const RIMDIR = new THREE.Vector3(0, 1, 0);   // hướng TỚI đèn chính trong toạ độ máy quay, cập nhật mỗi khung
function rimify(mat, base, rim, strength, power) {
  const m = mat.clone(); m.color.set(base); m.roughness = 0.9; m.metalness = 0; m.envMapIntensity = 0.25;
  m.userData.rim = { color: new THREE.Color(rim), strength, power };
  m.onBeforeCompile = (sh) => {
    sh.uniforms.rimColor = { value: m.userData.rim.color }; sh.uniforms.rimK = { value: new THREE.Vector2(strength, power) }; sh.uniforms.rimDir = { value: RIMDIR };
    sh.fragmentShader = sh.fragmentShader.replace('#include <common>', '#include <common>\nuniform vec3 rimColor; uniform vec2 rimK; uniform vec3 rimDir;')
      .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
        { float fr = 1.0 - abs(dot(normalize(-vViewPosition), normal));          // Fresnel: mép khối
          float side = 0.15 + 1.6 * max(0.0, dot(normal, rimDir));                  // mạnh ở phía đèn chính (ngược sáng thật), yếu phía kia
          totalEmissiveRadiance += rimColor * rimK.x * side * pow(fr, rimK.y); }`);
  };
  m.customProgramCacheKey = () => 'rim' + strength + ':' + power;
  return m;
}

export function install(opts = {}) {
  const O = { look: 'day', layers: { hdri: true, tex: true, soft: true, rim: true, ao: true, dof: true, grade: true }, focus: 'center', aperture: 0.6,
    sky: 0.55, ...opts }; O.layers = { ...{ hdri: true, tex: true, soft: true, rim: true, ao: true, dof: true, grade: true }, ...(opts.layers || {}) };
  if (typeof window !== 'undefined' && window.CINE_LAYERS) Object.assign(O.layers, window.CINE_LAYERS);   // trang đo giờ máy bật/tắt từng lớp
  if (!LOOKS[O.look]) throw new Error('look ' + O.look);
  const L = { ...LOOKS[O.look], ...(O.override || {}) };   // chỉnh theo cảnh (vd keyAz ngược sáng cho cảnh cận)
  const off = !Object.values(O.layers).some(Boolean);
  // three gán this.render = function… TRONG hàm dựng (thuộc tính riêng) → vá bằng accessor trên prototype: lần gán đầu (của three) được cất
  // vào __cineOrig, getter trả hàm bọc; lần gán sau (core.Stage bọc renderer.render) thành thuộc tính riêng như bình thường.
  const proto = THREE.WebGLRenderer.prototype;
  const orig = function (scene, cam) { return this.__cineOrig(scene, cam); };
  const state = { t: 0, ready: null, busy: false, comp: null, passes: {}, scene: null, cam: null, key: null, people: [], stats: {} };
  const prep = async (renderer, scene, cam) => {
    state.scene = scene; state.cam = cam;
    const ly = O.layers;
    // --- HDRI → PMREM (ánh sáng + phản xạ môi trường) + nền trời mờ + sương cùng màu chân trời
    if (ly.hdri) {
      const eq = await hdri(O.look), pm = new THREE.PMREMGenerator(renderer), env = pm.fromEquirectangular(eq).texture; pm.dispose();
      scene.environment = env; scene.environmentIntensity = L.env; scene.environmentRotation = new THREE.Euler(0, L.envRot || 0, 0);
      if (O.sky > 0) { scene.background = eq; scene.backgroundBlurriness = 0; scene.backgroundIntensity = L.skyI * O.sky; scene.backgroundRotation = new THREE.Euler(0, L.envRot || 0, 0); }
      if (scene.fog && O.sky > 0) scene.fog.color.set(L.fog);   // khoảng sương do cảnh đặt mỗi khung (modeLook); nền tối giữ sương gốc
      scene.traverse((o) => { if (o.isHemisphereLight) { o.intensity *= L.hemiK; o.color.set(L.hemiSky); o.groundColor.set(L.hemiGround); }
        if (o.isDirectionalLight && !o.castShadow) { o.color.set(L.rim); o.intensity = L.rimI; } });
    }
    scene.traverse((o) => { if (o.isDirectionalLight && o.castShadow) state.key = o; });
    // vật DỮ LIỆU (userData.checks.role series/bar): phản xạ môi trường thấp → độ sáng/tối mang nghĩa (lit/dark) không bị trời làm nhạt
    if (ly.hdri) scene.traverse((o) => { const r = o.userData.checks && o.userData.checks.role; if (r !== 'series' && r !== 'bar') return;
      o.traverse((c) => { if (c.isMesh) for (const m of [].concat(c.material)) if (m.isMeshStandardMaterial) m.envMapIntensity = L.dataEnv ?? 0.15; }); });
    if (state.key && ly.hdri) { state.key.color.set(L.key); state.key.intensity = L.keyI; }
    // --- bóng mềm: PCF + đĩa Vogel (shadow.radius), bản đồ 2048
    if (ly.soft && state.key) { const s = state.key.shadow; s.mapSize.set(2048, 2048); s.radius = L.shadowRadius; s.blurSamples = 16; s.bias = -0.0004; s.normalBias = 0.02; s.map?.dispose(); s.map = null; }
    // --- vân CC0 theo vai trò vật liệu (màu gốc của lib3d/tập → vai trò; màu dữ liệu KHÔNG đổi)
    if (ly.tex) {
      const T = {}; for (const r of Object.keys(ROLES)) T[r] = { map: await texture(`tex-${r}-diff`, true), normalMap: await texture(`tex-${r}-nor_gl`, false), roughnessMap: await texture(`tex-${r}-rough`, false) };
      const done = new Map();
      scene.traverse((o) => {
        if (!o.isMesh || !o.material || Array.isArray(o.material) || !o.material.isMeshStandardMaterial) return;
        const hex = '#' + o.material.color.getHexString().toUpperCase(), role = Object.keys(ROLES).find((r) => ROLES[r].colors.includes(hex));
        if (!role) return;
        if (o.userData.checks && o.userData.checks.char) return;
        const R = ROLES[role], key = o.material.uuid + role;
        if (!done.has(key)) {
          const m = o.material.clone(), rep = R.repeat;
          for (const k of R.noMap ? ['normalMap', 'roughnessMap'] : ['map', 'normalMap', 'roughnessMap']) { const t = T[role][k].clone(); t.repeat.set(rep, rep); t.needsUpdate = true; m[k] = t; }
          if (R.tint) m.color.set(R.tint); m.normalScale = new THREE.Vector2(R.normal, R.normal); m.roughness = 1; m.needsUpdate = true;
          // giữ ánh xạ opacity: tập gọi setOpacity(obj) trên vật → cùng đối tượng material (clone này) nên vẫn chạy
          done.set(key, m);
        }
        o.material = done.get(key);
      });
    }
    // --- người viền sáng (Person của lib3d: thân viên nang + đầu cầu; tay của c4kit cùng material)
    if (ly.rim) {
      scene.traverse((o) => {
        if (!(o.userData.checks && o.userData.checks.char)) return;
        const ms = new Map(), body = o.children.find((c) => c.isMesh), bodyM = body && body.material;
        o.traverse((c) => { if (!c.isMesh || c.material !== bodyM) return; const k = c.material.uuid;   // chỉ thân/đầu/tay (cùng material thân), không vật cầm tay
          if (!ms.has(k)) { const id = c.material.color.clone(); ms.set(k, rimify(c.material, id.clone().multiplyScalar(L.silhouette).getStyle(), new THREE.Color(L.rimPerson).lerp(id, 0.25).getStyle(), L.rimK, 2.6)); }
          c.material = ms.get(k); });
        state.people.push(o);
      });
    }
    // --- composer
    const W = renderer.domElement.width, H = renderer.domElement.height;
    const rt = new THREE.WebGLRenderTarget(W, H, { type: THREE.HalfFloatType, samples: 4 });
    const comp = new EffectComposer(renderer, rt); comp.setPixelRatio(1); comp.setSize(W, H);
    comp.addPass(new RenderPass(scene, cam));
    if (ly.ao) { const ao = seeded(() => new GTAOPass(scene, cam, W, H)); ao.output = 0; ao.blendIntensity = L.ao;
      ao.updateGtaoMaterial({ radius: 0.6, distanceExponent: 1.5, thickness: 1.2, scale: 1, samples: 16, distanceFallOff: 1 });
      ao.updatePdMaterial({ lumaPhi: 10, depthPhi: 2, normalPhi: 3, radius: 6, rings: 2, samples: 16 }); comp.addPass(ao); state.passes.ao = ao; }
    if (ly.dof) { const b = new BokehPass(scene, cam, { focus: 10, aperture: O.aperture * 0.001, maxblur: 0.008 }); comp.addPass(b); state.passes.dof = b; }
    comp.addPass(new OutputPass());
    if (ly.grade) { const g = new ShaderPass(GradeShader); g.uniforms.res.value.set(W, H); for (const k of ['lift', 'gamma', 'gain']) g.uniforms[k].value.set(...L.grade[k]);
      g.uniforms.sat.value = L.grade.sat; g.uniforms.contrast.value = L.grade.contrast; g.uniforms.vignette.value = L.grade.vignette; g.uniforms.grain.value = L.grade.grain;
      comp.addPass(g); state.passes.grade = g; }
    state.comp = comp;
  };
  const ray = new THREE.Raycaster(), v = new THREE.Vector3(), d = new THREE.Vector3();
  function focusDist(cam) {
    if (typeof O.focus === 'number') return O.focus;
    cam.getWorldDirection(d);
    if (O.focus === 'char' && state.people.length) { const p = state.people[O.focusIndex || 0]; p.getWorldPosition(v); v.y += 0.6; return Math.max(0.5, v.sub(cam.position).dot(d)); }
    ray.setFromCamera(new THREE.Vector2(O.focusXY ? O.focusXY[0] : 0, O.focusXY ? O.focusXY[1] : 0), cam);
    const hit = ray.intersectObjects(state.scene.children, true).find((h) => h.object.visible && h.object.material && !(h.object.material.opacity < 0.5) && h.object.userData.role !== 'bg');
    return hit ? hit.distance : 20;
  }
  const cineRender = function (scene, cam) {
    if (off || state.busy || !scene || !scene.isScene) return orig.call(this, scene, cam);
    if (!state.comp) { state.cap = [this, scene, cam]; return orig.call(this, scene, cam); }   // trước prepare: vẽ gốc, bắt (renderer, scene, cam)
    // máy quay có thể đổi mỗi khung → theo dõi đèn chính: giữ phương đèn của hồi (độ cao/phương vị) quanh điểm nhìn của cảnh
    if (state.key && O.layers.hdri) { const k = state.key, tg = k.target.position; const el = L.keyEl * Math.PI / 180, az = L.keyAz * Math.PI / 180, r = 18;
      k.position.set(tg.x + r * Math.cos(el) * Math.sin(az), tg.y + r * Math.sin(el), tg.z + r * Math.cos(el) * Math.cos(az)); k.target.updateMatrixWorld(); }
    if (state.key) RIMDIR.copy(state.key.position).sub(state.key.target.position).normalize().transformDirection(cam.matrixWorldInverse);
    if (O.posture) O.posture(state, state.t);
    if (state.passes.dof) state.passes.dof.uniforms.focus.value = focusDist(cam);
    if (state.passes.grade) state.passes.grade.uniforms.seed.value = (Math.round(state.t * 30) % 997) * 0.618034;
    state.busy = true;
    try { state.comp.render(); } finally { state.busy = false; }
  };
  Object.defineProperty(proto, 'render', { configurable: true,
    get() { return cineRender; },
    set(fn) { if (!this.__cineOrig) Object.defineProperty(this, '__cineOrig', { value: fn }); else Object.defineProperty(this, 'render', { value: fn, writable: true, configurable: true }); } });
  return {
    state, opts: O,
    // gọi SAU boot cảnh gốc: render khô một khung (vẽ gốc) để bắt (renderer, scene, cam) thật
    async prepare(frame) {
      if (off) return;
      frame(0);
      if (!state.cap) throw new Error('cine: cảnh không gọi renderer.render');
      await prep(...state.cap);
    },
  };
}

// bọc boot của cảnh gốc
export function wrap(innerBoot, opts) {
  return async (res) => {
    const L = install(opts);
    const S = await innerBoot(res);
    await L.prepare(S.frame);
    if (typeof window !== 'undefined') window.CINE = L;
    return { canvas: S.canvas, frame: (t) => { L.state.t = t; return S.frame(t); }, cine: L };
  };
}
