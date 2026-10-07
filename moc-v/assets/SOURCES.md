# Asset sources & licensing — faceless US personal-finance YouTube channel (monetized)

Read on **2026-10-06**. No purchases or sign-ups. The research agent made no content-generating API calls. **Afterwards the coordinating session made ONE Eleven Music call** (`/v1/music`, composition plan `eleven-music/plan.json` → `eleven-music/music.mp3`, 69.6 s; estimated ≈ 1,050 credits at 900 credits/min, charged to the channel's existing ElevenLabs plan — the API key cannot read the plan tier, so commercial eligibility (Starter+) is unconfirmed).

**Legend**
- **READ** = I fetched the governing page from this machine; quotes are verbatim.
- **MIRROR** = the vendor's site was blocked, so I read a verbatim copy from a reachable mirror (GitHub or an npm tarball). The mirror is named.
- **NOT READ** = the page was blocked by the egress proxy. Any figures come from web-search result summaries (third-party blogs). They are **unverified** and must be checked in a browser before use. No quotes are given for these.

## 0. Reachability from this machine (2026-10-06)

| Host | curl | WebFetch | Notes |
|---|---|---|---|
| elevenlabs.io (terms, pricing, docs) | 200 | – | read directly |
| help.elevenlabs.io | 403 | – | blocked |
| raw.githubusercontent.com | 200 | – | Khronos, Poly Haven site source, scancode mirror |
| registry.npmjs.org | 200 | – | search + tarballs |
| api.github.com | 200, repo-scoped only | – | org/repo listing refused |
| **api.polyhaven.com** (`/assets?t=models`) | **000** (`CONNECT tunnel failed, response 403`) | – | **NOT reachable** |
| polyhaven.com, kenney.nl, poly.pizza | 000 / 403 | EGRESS_BLOCKED | blocked |
| pixabay.com, support.google.com, youtube.com | 000 | EGRESS_BLOCKED | blocked |
| epidemicsound.com, artlist.io | 000 | (not tried) | blocked |
| meshy.ai, help.meshy.ai, docs.meshy.ai, tripo3d.ai, lumalabs.ai | 000 | EGRESS_BLOCKED | blocked |
| creativecommons.org, web.archive.org, wikipedia | 000 | – | blocked |

---

## 1–3. ElevenLabs (Music `/v1/music`, Sound Effects `/v1/sound-generation`, general ToS)

### Prices (READ: https://elevenlabs.io/pricing, https://elevenlabs.io/pricing/api)

| Plan | USD/month (monthly billing) | Credits/mo | Music: generation / download limit per month* | Music attribution* | Music streaming-platform rights* |
|---|---|---|---|---|---|
| Free | $0 | 10k | 11 min / **download not permitted** | Required | Prohibited |
| Starter | $6 (promo: $1 first month until Oct 18) | 30k | 17 / 30 min | No | Prohibited |
| Creator | $22 ($11 first month) | 121k | 62 / 250 min | No | Yes |
| Pro | $99 | 600k | 304 / 500 min | No | Yes |
| Scale | $299 (3 seats; < 10 employees) | 1.8M | 1,100 / 1,500 min | No | Yes |
| Business | $990 (10 seats; < 50 employees) | 6M | 4,800 / 4,000 min | No | Yes |
| Enterprise | custom | custom | custom | No | Yes |

\*From the Music Commercial Rights table at https://elevenlabs.io/eleven-music-model-specific-terms (last updated 26 May 2026).
- "Media Rights" for **every** self-serve plan, Free included: "All online and offline commercial use permitted, except film, TV, radio, & Studio Games". This covers YouTube.
- Eligibility: Free, Starter, Creator and Pro are "For Individual Use Only".
- Reseller use and "Music Libraries & Repositories" are Prohibited on all self-serve plans.

**Credit and USD cost (READ)**
- Pricing FAQ: "Eleven Music 900 credits per minute; Sound Effects 200 credits per generation".
- Docs (https://elevenlabs.io/docs/overview/capabilities/sound-effects): "Cost: 40 credits per second when duration is specified". Each SFX generation can be 0.1–30 s.
- API page: Music **$0.15/min**, Sound Effects **$0.12/min**.
- Music length is 3 s to 5 min per generation.
- API page note: "Commercial use licensing on Starter+ plans" (Music). Sound Effects are listed as "Royalty-free sound effects from a text prompt".
- Annual billing works out to monthly price × 10.

### Commercial use on monetized YouTube

| | Free tier | Paid tiers |
|---|---|---|
| **Music** | Conflicting terms. The Music table allows commercial media use, but Free **cannot download** and must credit ElevenLabs. The general ToS says Free = non-commercial. The music-specific terms take precedence (see the order clause below), but no download means Free is effectively **unusable**. | **Yes** from Starter. No film, TV, radio or Studio Games. No attribution. Starter has no rights to music streaming platforms (not relevant for YouTube). |
| **Sound Effects** | **No.** No SFX-specific plan table exists, so the ToS rule applies: Free = non-commercial. | **Yes** (ToS: paid = commercial). SFX outputs may be sublicensed to other users unless you click "Disable". |
| Ownership | User "retain[s] all rights in and to your Output" (ToS 4(c)). Output is not unique, and ElevenLabs gives no title or non-infringement warranty. | same |
| AI training | ElevenLabs receives a perpetual license to your Content (Input **and Output**) to improve its services. You can opt out under Data use. You may **not** use Output to train AI. | same |

### Verbatim quotes

**ToS (non-EEA), Last Updated 31 March 2026**, https://elevenlabs.io/terms-of-use, read 2026-10-06:
> "(i) if you access or use our Services free of charge (such a user, a "Free User"), you may only use the Services for non-commercial purposes; (ii) if you access or use our Services through a paid subscription plan (such a user, a "Paid User"), you may use the Services for commercial purposes, but in either case, your access and use of the Services and any Output must still comply with the Prohibited Use Policy."

The source uses curly quotes; they are shown here as straight quotes.

> "Except as expressly set forth herein, as between you and ElevenLabs, you retain all rights in and to your Output."

> "Due to the nature of machine learning, the Output generated by you using the Services may not be unique across users, as the Services may produce the same or similar Output for you and a third party."

**Music Terms, Last Updated 26 May 2026**, https://elevenlabs.io/music-terms, read 2026-10-06:
> "In the event of any conflict among the following documents, the order of precedence shall be: (A) the Model-Specific Terms; (B) the Service Terms; and (C) the Underlying ElevenLabs Agreement."

> "Customer is expressly prohibited from submitting any of the following as part of the Input: i. any artist's (whether living or deceased) real name or stage name; ... iii. any song title;"

**Eleven Music Model-Specific Terms (v1, v2), Last Updated 26 May 2026**, https://elevenlabs.io/eleven-music-model-specific-terms, read 2026-10-06:
> "Attribution means Customer is required to provide appropriate credit to ElevenLabs when accessing a Music Model free of charge wherever the Output or any derivative version is displayed, distributed, or published on any platform. The credit shall appear in a form substantially similar to: "Created in collaboration with ElevenLabs" or as otherwise approved in writing by ElevenLabs."

> "If you downgrade from the Business plan to the Free plan, you will continue to have access to and the right to use Output you created while a Business plan subscriber, but any new Output you create will be subject to the restrictions and limitations of the Free plan."

**Sound Effects Terms, Last updated 12 February 2026**, https://elevenlabs.io/sound-effects-terms, read 2026-10-06:
> "You may opt out of the sublicensing of your SFX Outputs to third parties (including making SFX Outputs available to other ElevenLabs users) at any time by using the "Disable" functionality on the Sound Effects product page."

**Prohibited Use Policy, Last Updated 17 August 2026**, https://elevenlabs.io/use-policy, read 2026-10-06. This matters for a finance channel if ElevenLabs TTS voices the scripts.
> "Provide tailored professional advice without (i) a qualified professional in that field reviewing the Output before it is made available to a consumer or the general public, and (ii) clear disclosure regarding the use and limitations of AI. This includes without limitation: Financial advice or services, including lending services and cryptocurrency trading;"

> "Using any part of our Services or their Output as input for any machine learning or training of artificial intelligence models."

**Docs**, https://elevenlabs.io/docs/overview/capabilities/music, read 2026-10-06:
> "Eleven Music is cleared for nearly all commercial uses, from film and television to podcasts and social media videos, and from advertisements to gaming."

**Content ID:** none of the pages I read mention YouTube Content ID. The help center (help.elevenlabs.io) returned 403, so I could not read it.

---

## 4. Kenney (CC0) and Poly Pizza (CC0 / CC-BY)

| Source | Price | Commercial YT | Attribution | Restrictions | Status |
|---|---|---|---|---|---|
| Kenney 3D kits | Free (donations optional) | Yes | Not required | None (CC0) | kenney.nl **blocked**. License text read via **MIRROR**. |
| Poly Pizza | Free | Yes (per model) | CC0: none. CC-BY 4.0: credit required. | Per-model license | poly.pizza **blocked. NOT READ.** |

**Kenney (MIRROR).** The license file bundled in the npm package `@anabis/kenney-space-kit-mirror@2.0.0`, file `package/assets/License.txt`, is Kenney's own file ("Space Kit (2.0) ... Created/distributed by Kenney"). Tarball: https://registry.npmjs.org/@anabis/kenney-space-kit-mirror/-/kenney-space-kit-mirror-2.0.0.tgz, read 2026-10-06:
> "License: (Creative Commons Zero, CC0)"

> "This content is free to use in personal, educational and commercial projects. Support us by crediting Kenney or www.kenney.nl (this is not mandatory)"

**Poly Pizza (NOT READ).** I could not read poly.pizza/license or any model page. Search results suggest the site mixes CC0 and CC-BY 4.0 models, labels the license per model, and may have a suggested credit format. Check each model's license field before use. No quote is available.

---

## 5. Poly Haven (CC0)

- **api.polyhaven.com is NOT reachable** from this machine: `curl ... https://api.polyhaven.com/assets?t=models` returned `000` with `curl: (56) CONNECT tunnel failed, response 403`.
- polyhaven.com is also blocked.
- Price: free, Patreon optional. Commercial YouTube use: **yes**. Attribution: **not required**.
- **MIRROR:** the English strings of the site's license page, from Poly Haven's own site source: https://raw.githubusercontent.com/Poly-Haven/polyhaven.com/master/public/locales/en/license.json, read 2026-10-06. Inline markup tags (`<b>`, `<lnk>`) are removed below.

> "Our assets are all licensed as CC0, which is effectively Public Domain even in jurisdictions that do not support the Public Domain."

> "You can use our assets for any purpose, including commercial work."

> "You do not need to give credit or attribution when using them (although it is appreciated)."

---

## 6. Khronos glTF-Sample-Assets (READ)

I read all 150 `Models/*/metadata.json` files listed in https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/model-index.json on 2026-10-06.

| License | Count | Examples |
|---|---|---|
| CC0-1.0 only | 62 | Avocado, Lantern (old wooden street light), Toy Car, Water Bottle, Boom Box, Flight Helmet, SciFi Helmet, Sheen Chair, Corset, Glass Vase with Flowers, Barramundi Fish, Skull, Suzanne |
| CC0-1.0 + LegalMark (Khronos 17 / UX3D 1) / Stanford 2 | 20 | "Compare *" test models, Box With Spaces, Antique Camera, Dragon * |
| CC-BY-4.0 (± CC0 / LegalMark) | 61 | A Beautiful Game, Commercial Refrigerator, GlamVelvetSofa, Chronograph Watch, Sunglasses Khronos, Fox, Traffic Cone, Cesium Man, Cesium Milk Truck, Car Concept, Iridescent Dish with Olives |
| Other (do not use commercially) | 7 | Duck (SCEA), BrainStem (Poser EULA), Damaged Helmet (CC-BY + **CC-BY-NC**), PlaysetLightTest (**CC-BY-NC-SA**), Environment Test (Adobe Stock), **Sponza (CRYENGINE agreement)**, **Virtual City (3DRT testing-only)** |

**House, building, or money-like models:**
- No CC0 or CC-BY house, building, coin, banknote or safe exists.
- The only buildings are **Sponza** (an interior, "Building interior, often used to test lighting", under the CRYENGINE license) and **Virtual City** (3DRT). Neither can be used commercially.
- Closest CC0 props: Lantern, Toy Car, Water Bottle, Boom Box.

Verbatim from https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/LICENSES/LicenseRef-3DRT-Testing.txt, read 2026-10-06:
> "It is for use *only* in testing your glTF tools such as loaders and importers. The model, any portion of the model, the textures and the animation data, may *not* be deployed in a commercial application without the developer purchasing their own license to it."

Note: some CC0 models also carry a "LegalMark" trademark license (Khronos, UX3D, Cesium, DGG). Avoid showing those logos.

---

## 7. npm packages that ship 3D models (READ, registry.npmjs.org, 2026-10-06)

I ran about 20 registry searches. For each hit below I listed the tarball contents (`tar -t`, no extraction).

| Package | License field | Contents | House or building? |
|---|---|---|---|
| `@anabis/kenney-space-kit-mirror@2.0.0` | `CC0-1.0` (Kenney License.txt bundled) | 459 model files (glb/gltf/obj/fbx). Space-themed: hangars, corridors, `structure*.glb`, desks, rovers, monorail | Sci-fi structures and hangars only. **No house.** |
| `mmmm-models@1.0.0` (Mini Mike's Metro Minis) | **`CC-BY-4.0`** | 432 `.dae` (Collada) + png textures, plus `.vox`. City set: `obj_house1…`, `obj_store01–08`, apartments, celltower, cars, characters | **Yes:** suburban houses, storefronts, apartments. Needs attribution and Collada→glTF conversion. |
| `@pmndrs/assets@1.7.0` | `CC0-1.0` | models: only bunny, suzi, pmndrs (base64 .glb.js), plus hdri/matcaps/fonts | No |
| `kenney-hexagon-pack@1.0.0` | `CC0 1.0` | 2D sprites only (`hexagonBuildings_sheet.png`). No 3D models. | 2D buildings only |
| `3dassets-mcp`, `@jgengine/assets`, `threenative-asset-mcp`, `arcane-assets-mcp` | various | Index or downloader tools. They ship no models and fetch from external sites (likely blocked here). | n/a |

Verbatim from `mmmm-models` `package/README.md` (tarball https://registry.npmjs.org/mmmm-models/-/mmmm-models-1.0.0.tgz, read 2026-10-06):
> "These models are licensed under Creative Commons Attribution 4.0 International, which allows you to do pretty much whatever you want, provided you give appropriate credit, a link to the license and indicate if changes were made."

> "For attribution, all you need to do is: in the credits of your project, say something like Additional Artwork by Mike Judge"

---

## 8. Music libraries

| Library | Price (USD/mo) | Commercial YouTube | Attribution | Content ID / restrictions | Status |
|---|---|---|---|---|---|
| YouTube Audio Library | Free | Yes, on YouTube (per Studio track license) | None for "YouTube Audio Library License" tracks; **required** for tracks marked CC BY | Licensed for use in YouTube videos | **NOT READ** (support.google.com blocked). Unverified, from search summaries. |
| Pixabay Music | Free | Yes | Not required | No standalone resale/distribution. Some tracks are registered in Content ID by contributors; Pixabay offers a License Certificate to dispute claims (search summary, unverified). | pixabay.com blocked. License text via **MIRROR** (scancode). |
| Epidemic Sound | Unverified search figures: Creator/Personal ≈ $17.99 monthly or $9.99/mo billed annually; Pro/Commercial ≈ $39.99–$49 monthly | Yes on paid plans (personal plan: 1 channel per platform) | No | Vendor whitelists or clears claims for subscribers (unverified) | **NOT READ** |
| Artlist | Unverified: Music & SFX Social ≈ $14.99 monthly or $9.99/mo annual; Music & SFX Pro ≈ $24.92/mo annual-only | Yes (Social: 1 personal channel per platform; client work needs Pro) | No | License is tied to subscription period terms (unverified) | **NOT READ** |

Pixabay Content License, verbatim from the scancode-toolkit mirror: https://raw.githubusercontent.com/aboutcode-org/scancode-toolkit/develop/src/licensedcode/data/licenses/pixabay-content.LICENSE, read 2026-10-06. Its `homepage_url` is https://pixabay.com/service/terms/#license. **The mirror may be an older revision** of Pixabay's live terms.
> "Under the Pixabay License you are granted an irrevocable, worldwide, non-exclusive and royalty free right to use, download, copy, modify or adapt the Content for commercial or non-commercial purposes. Attribution of the photographer, videographer, musician or Pixabay is not required but is always appreciated."

> "Sale or distribution of Content e.g. as a posters, digital prints, music files or physical products, without adding any additional elements or otherwise adding value"

---

## 9. AI 3D model services. All **NOT READ** (domains blocked); figures are unverified search summaries.

| Service | Price (USD/mo, unverified) | Free tier commercial? (unverified) | Paid tier | Ownership |
|---|---|---|---|---|
| Meshy | Free (≈100 credits/mo). Pro ≈ $20, Studio ≈ $70 (other tiers cited in some summaries), Enterprise custom | Search summaries say free outputs are **CC BY 4.0** (commercial with attribution) | Full commercial use, no attribution, private | Summaries say user owns outputs |
| Tripo3D | Free "Basic" (≈200 credits, ≈8 models). Pro ≈ $19.90 up to ≈ $109.90 | Summaries say free models are public, **CC BY 4.0 and non-commercial**. Contradictory: CC BY itself allows commercial use, so verify. | Commercial rights + private models from Professional | Verify on vendor ToS |
| Luma Genie | Free tier (≈30 generations/mo cited) | **Conflicting** sources: some say commercial with attribution, others say tier-dependent | Unclear | Verify. lumalabs.ai/learning-hub/licensing could not be read. |

Pages to check manually: https://www.meshy.ai/pricing, https://help.meshy.ai/en/articles/16102098-can-i-use-meshy-assets-commercially, https://www.tripo3d.ai/pricing, https://lumalabs.ai/learning-hub/licensing.

---

## Rủi ro quyền

- **Nhạc AI (ElevenLabs) & Content ID:** điều khoản không nhắc tới Content ID. Output "may not be unique", nên người khác có thể tạo bản gần giống rồi đăng ký Content ID. Đồng thời ElevenLabs không bảo đảm non-infringement. Nên lưu prompt, ngày tạo, hóa đơn plan trả phí và file gốc để khiếu nại claim.
- **Gói Free của ElevenLabs:** Music không cho tải xuống và bắt buộc ghi "Created in collaboration with ElevenLabs". Sound Effects ở Free chỉ được dùng phi thương mại theo ToS. Kênh có kiếm tiền thì phải dùng tối thiểu **Starter** và tạo output **trong lúc đang trả phí**. Nếu hạ xuống Free, output tạo sau đó chịu hạn chế của Free.
- **SFX ElevenLabs không độc quyền:** mặc định SFX của bạn có thể được sublicense cho người dùng khác, nên cần bật "Disable". Cấm nhập tên nghệ sĩ hoặc tên bài hát vào prompt nhạc. Cấm dùng output để huấn luyện AI.
- **Kênh tài chính và Prohibited Use Policy:** nếu dùng giọng TTS ElevenLabs cho nội dung "financial advice" mang tính cá nhân hóa, cần người có chuyên môn duyệt và công bố rõ việc dùng AI. Nên định vị nội dung là giáo dục, không phải tư vấn.
- **CC-BY (Poly Pizza, mmmm-models, ~61 model Khronos, track CC BY của YouTube Audio Library):** thiếu credit trong mô tả video là vi phạm license. Cần lập file CREDITS gồm tên tác giả, tên asset, link license và ghi chú "đã chỉnh sửa", rồi dán vào description từng video. Không dùng model NC/NC-SA hoặc model có license riêng (Sponza, Virtual City, Damaged Helmet, Duck…).
- **CC0 (Kenney, Poly Haven, Khronos CC0):** rủi ro thấp. Vẫn tránh logo hoặc trademark (LegalMark Khronos/Cesium) trong khung hình. Bản mirror npm không chính thức, nên đối chiếu với nguồn gốc khi truy cập được.
- **Thư viện nhạc stock (Pixabay, Epidemic, Artlist):** Pixabay có thể bị claim do contributor tự đăng ký Content ID, cần lưu License Certificate. Epidemic và Artlist gắn quyền với gói và kênh (gói cá nhân thường chỉ cho 1 kênh mỗi nền tảng). Giá và điều khoản trong file này **chưa được xác minh** vì trang bị chặn.
- **3D AI (Meshy/Tripo/Luma):** quyền sở hữu output AI chưa chắc được bảo hộ bản quyền ở Mỹ (khi không có tác giả là con người). Gói free thường công khai model dưới CC BY, có thể là phi thương mại (Tripo). Nên dùng gói trả phí khi tạo asset cho kênh kiếm tiền, và đọc lại ToS trực tiếp trước khi dùng.
