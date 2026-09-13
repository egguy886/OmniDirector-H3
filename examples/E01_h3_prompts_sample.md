# E01《认罪书》｜H3 768p 竖版 15 秒分段提示词

## 1. 交付锁定

| 项目 | 本版锁定 |
|---|---|
| 目标模型 | H3 本地大模型；按 MiniMax H3 兼容工作流编写，节点细节待确认 |
| 输出 | 8 段 × 15.0 秒 = 120 秒；每段单独生成、按顺序剪辑 |
| 画幅与分辨率 | 9:16 竖版；768p 竖版预设 |
| 帧率 | 24fps 工作参数；以本地节点实际输出为准 |
| 模型提示词 | 以英文为主，适配 H3；中文潜台词只放在编辑校对卡，不作为角色第二遍对白 |
| 音频 | 优先测试 H3 原生英文对白与环境声；不稳定时保留说话动作，统一后期录音和混音 |
| 声音锁 | 见 [E01 声音连续性合同](./E01_声音连续性合同.md)；Cade／Coach 使用同一批准参考音频或同一 master voice |
| 文字 | 协议、标签、时间戳、门禁状态和签名由后期图形层完成，模型不生成可读文字 |
| 总控文件 | [E01 人读分镜与120秒母提示词](./E01_人读分镜与120秒母提示词.md) 继续作为整集因果和连续性总控 |

## 1.5 视觉资产绑定

- 本集 8 段的候选人物、场景、道具与状态绑定见 [E01–E10 H3 80 段参考输入清单](../视觉资产/E01-E10/E01-E10_H3_80段参考输入清单.md)。
- 当前状态为 `candidate_assets_bound_pending_human_review`：资产已生成并完成静态注册，但没有把候选图当作最终批准图。
- 生产时按段落行读取最小参考集合；`TAIL_RELAY` 只接收上一段通过 QC 的真实尾帧，`HARD_CUT` 不传前空间尾帧。
- 屏幕、名单、文件、代码和成绩只使用空白载体，后期再叠加可读文字。

## 2. 使用规则

1. 每段提示词都必须与下面的“全段共同前缀”一起复制；不要只复制第六模块。
2. 每段输出必须是 15.0 秒。内部时间码是镜头节拍，不是额外时长；最终剪辑按 `H3-01 → H3-08` 顺序连接。
3. 参考图使用[统一视觉资产注册表](../视觉资产/E01-E10/E01-E10_视觉资产注册表.md)中本段绑定的文件；`pending_review` 资产只用于 Blender／零成本预演，不能进入付费批量。表中的 Cxx/Sxx/Pxx 是生产卡映射，不要把这些内部代码粘进模型提示词。
4. 生成前锁定同一批角色参考、服装、光向和随机种子（若本地节点支持）；生成后先看段尾，再看整段。
5. 本版为了便于 H3 单段生成，把对白按整句重新归属到 8 段，不改变剧本台词、人物立场或因果顺序。
6. 若本地 H3 节点不稳定支持同一段内的场景硬切，则保留每段的时间码和出口状态，在后期完成硬切，不补拍不存在的剧情。

## 3. 全段共同前缀

将以下英文前缀粘贴到每一个 H3 分段提示词的最前面：

```text
Create one exact 15.0-second clip for a vertical overseas short drama, 768p vertical preset, aspect ratio 9:16, working at 24 fps. Use cinematic live-action realism, physically grounded motion, cold blue-gray and cold white tones, restrained wet red accents, natural skin texture, realistic contact, weight, breath and fabric response. Keep the same faces, body proportions, hairstyles, clothing, locations, screen direction, light direction and prop states as the adjacent clips. For every named speaker, use the same supplied voice reference or the same locked speaker identity across all clips; never invent a new voice from the face. Speakers explicitly marked post-production must not receive native generated dialogue; preserve clean mouth timing for the post track. If a reference is marked pending human review, use it for test renders only, not final batch output. English dialogue only in generated speech. Any Chinese text below is for the Chinese editor only and must not be spoken. If native audio is disabled, preserve accurate mouth movement, pauses and clean dialogue timing for post-production dubbing. Keep non_diegetic_music: SILENT; use only diegetic environment and dialogue.

Do not generate readable signage, contract text, labels, timestamps, signatures, logos, school emblems, watermarks or random letters. Leave clean blank surfaces for the post-production graphics layer. Do not add narration, inner monologue, a new named character, a visible unknown pursuer, a weapon, blood, supernatural effects, a death countdown or a new plot explanation. Preserve the fixed geography and the exact prop continuity described in this segment.
```

## 4. 15 秒生产单元

### H3-01｜00–15 秒｜速度被门禁截停

> **候选参考绑定｜H3-01**：见 [E01–E10 H3 80 段参考输入清单](../视觉资产/E01-E10/E01-E10_H3_80段参考输入清单.md) 中本集本段对应行；模型只加载该行列出的角色、场景、道具状态与声音参考。

**生产卡**

- 参考输入：Cade、晨训田径场、智能闸机开放态与关闭锁死态状态参考图、运动秒表、旧短跑钉鞋。
- 入口状态：湿红跑道暂时空着，Cade从画外冲入。
- 出口状态：闸机叶门已先完全关闭并锁定，随后资格环扫描失败；Cade仍停在闸机南侧，资格环完整。
- 台词：无。
- 音频重点：鞋钉、湿胶、呼吸、急停摩擦、电子蜂鸣；音乐不盖住实音。

**中文编辑意图**：先让观众爱上 Cade 的速度，再让一盏红灯把他从赛道里切出去。不是摔倒，是权限拒绝。

**可复制给 H3 的提示词（黄金合体版 · 官方 MiniMax H3 规范）**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, cinematic vertical 9:16 realism. Cold blue-gray dawn tones with damp red track accents. A low-angle medium-wide tracking shot frames Cade from behind and slightly to the east side. Cade is an 18-year-old male sprinter with tousled damp dark hair, wearing a sweat-soaked gray training tank, black shorts, and worn black spikes, with an intact black qualification ring on his left wrist. The camera tracks forward smoothly as Cade sprints with explosive athletic form along the wet red track toward a metal smart access gate at the north end. [Shot 2] At 00:04.500, the camera cuts to an extreme low-angle ground insert ten centimeters above the rubber track. A worn black sprint spike plants heavily into the wet track, compressing the rubber and kicking up fine water droplets with a sharp friction scrape. [Shot 3] At 00:05.300, the shot transitions to an eye-level side-rear medium shot returning to the running axis. Cade reaches the south boundary of the gate and executes an upright braking slide; his front foot bites the track while his rear foot slides half a meter, his torso pitching forward before regaining firm balance right before the line. [Shot 4] At 00:08.500, the shot cuts to a chest-height medium close-up facing north. The metal sliding gate finishes closing with a heavy mechanical latch, completely sealing the lane. A small status indicator on the gate terminal illuminates with a sharp red glow. [Shot 5] At 00:10.200, the camera cuts to a close-up of Cade's left forearm and the gate sensor. Cade brings his wrist up and presents the intact black wristband within five centimeters of the reader. A dull electronic denial pulse sounds, and the terminal screen flashes a local red warning. Cade's arm remains steady, absorbing the rejection. [Shot 6] At 00:13.000, the shot transitions to a fixed three-quarter medium shot. The camera holds completely static on Cade standing outside the locked gate in the cold morning mist, chest heaving with deep athletic breath, wrist lowered, facing the closed barrier.

overall_soundscape: Damp track spike traction, heavy rhythmic sprinting breath, shoe friction braking scrape on wet rubber, pneumatic gate sliding and metal latch click, followed by a double-pulse access denial buzz and cold outdoor wind.

non_diegetic_music: SILENT
```

### H3-02｜15–30 秒｜数据交锋与人肉路障

> **候选参考绑定｜H3-02**：见 [E01–E10 H3 80 段参考输入清单](../视觉资产/E01-E10/E01-E10_H3_80段参考输入清单.md) 中本集本段对应行；模型只加载该行列出的角色、场景、道具状态与声音参考。

**生产卡**

- 参考输入：Cade、Coach Draper、Reeve、晨训田径场、智能闸机、运动秒表。
- 入口状态：承接 H3-01 的红灯和锁死声，Cade在闸机南侧。
- 出口状态：Coach把文件从外套内袋取出，文件悬在感应台上方；资格环仍完整。
- 台词：Coach 与 Cade 的前两句。
- 音频重点：群像嘘笑压在后景；Coach 的声音压低、疲惫而公事公办，Cade 的声音带喘息与数据武器。
- API 声音参考：`ref_audio_0`：Coach Draper；`ref_audio_1`：Cade。

**对白与中文潜台词（黄金合体版）**

- Coach Draper: “Step off the rubber, Cade. Your credential isn't pinging the server.”
  - 潜台词：脚从塑胶道上收回去，凯德。不是我拦你，是服务器已经拒绝认领你的身份了。
- Cade: “I ran a 10.12 in Lane 4 on Tuesday, Coach. The roster locked at midnight.”
  - 潜台词：我周二在四号道跑了十秒一二，教练。大名单午夜刚刚系统锁死。

**可复制给 H3 的提示词（黄金合体版 · 官方 MiniMax H3 规范）**

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action, cold dawn light, cinematic 9:16 composition. A compressed 85mm telephoto medium shot looks north past Cade's lowered left wrist toward the track perimeter. Across the west track rail in soft focus, privileged runners in pristine navy warm-ups pause their drills with faint mocking smirks; team captain Reeve stands motionless with arms folded behind the rail, his cool gaze fixed on Cade. [Shot 2] At 00:03.800, the camera cuts to an eye-level profile two-shot from the east walkway. Coach Draper, a tired, weathered coach in a dark windbreaker, walks deliberately into frame and plants his body squarely between Cade and the closed gate, forming a physical human barrier. Coach Draper looks down at Cade without anger and speaks with quiet, bureaucratic fatigue: <d> Coach Draper: "Step off the rubber, Cade. Your credential isn't pinging the server." </d> [Shot 3] At 00:08.200, the camera cuts to a tight medium close-up of Cade from a low eye level. Cade wipes sweat from his temple with the back of his right hand; his jaw muscles tighten, but his posture remains upright, inches from Coach's shoulder. Cade speaks in a low, gravelly, defiant tone: <d> Cade: "I ran a 10.12 in Lane 4 on Tuesday, Coach. The roster locked at midnight." </d> [Shot 4] At 00:12.600, the shot transitions to an over-the-shoulder close-up behind Cade. Coach Draper's face remains emotionless. He reaches into the breast pocket of his dark windbreaker, extracts a crisp folded document with a red administrative header, and raises it into the center of the frame, holding it suspended right above the gate terminal.

overall_soundscape: Muted track chatter and distant snickers across the grass, damp leather soles on concrete, heavy post-sprint breathing, low-pitched close-mic spoken dialogue with crisp consonant delivery, and paper unfolding rustle.

non_diegetic_music: SILENT
```

### H3-03｜30–45 秒｜平账指控与裁决室空间切入

> **候选参考绑定｜H3-03**：见 [E01–E10 H3 80 段参考输入清单](../视觉资产/E01-E10/E01-E10_H3_80段参考输入清单.md) 中本集本段对应行；模型只加载该行列出的角色、场景、道具状态与声音参考。

**生产卡**

- 参考输入：Cade、Coach Draper、Nia、晨训田径场、纪律裁决室、协议文件、黑笔、重型剪刀。
- 入口状态：承接 H3-02，Coach手中的文件悬在闸机感应台上方。
- 出口状态：裁决室空间已经建立，协议、黑笔、剪刀整齐位于桌面，Coach准备提出条件。
- 台词：Coach 的化学试卷指控与免责调解书归入本段。
- 音频重点：文件拍台声成为场切点；裁决室的冷气和荧光灯底噪接入。
- API 声音参考：`ref_audio_0`：Coach Draper；Cade、Nia保持闭唇。

**对白与中文潜台词（黄金合体版）**

- Coach Draper: “It posted with an asterisk. Academic Integrity flagged your chemistry paper. You can argue with the board, or you can walk inside and sign the waiver.”
  - 潜台词：大名单发出来了，但你的名字后面带了个星号。学术诚信处扣了你的化学考卷。你可以去校董会自取其辱，或者现在跟我进屋，把免责放弃书签了。

**可复制给 H3 的提示词（黄金合体版 · 官方 MiniMax H3 规范）**

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 3) aligns with the 08.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action, dawn track exterior. A tight close-up on the metal sensor plate. Coach Draper's hand slaps the folded document flat onto the metal surface; the edge of the paper vibrates with a crisp snap. Coach Draper stays in close frame and delivers his final ultimatum with cold institutional certainty: <d> Coach Draper: "It posted with an asterisk. Academic Integrity flagged your chemistry paper. You can argue with the board, or you can walk inside and sign the waiver." </d> Cade's dark eyes remain locked on Coach, absorbing the trap without stepping back. [Shot 2] At 00:07.000, the camera cuts to a macro insert of Cade's left wrist. The black qualification ring sits tight against his skin over a faint tendon twitch; his fist slowly clenches. [Shot 3] At 00:08.000, a hard causal match-cut snaps into an interior wide shot of the disciplinary hearing room. The room is stark, illuminated by sterile 5600K fluorescent ceiling panels with pale green-gray acoustic wall tiles. At the head of a long brushed-aluminum table on the west side sits Nia, an elegant and rigid 18-year-old female athletic liaison in a tailored black university team blazer, swiping through documents on a tablet without looking up. [Shot 4] At 00:11.200, the shot cuts to a southwest three-quarter medium shot. Coach Draper enters the room from the side and slides the printed waiver form across the metal tabletop toward the empty south chair. Right behind the document, he lays down an all-black heavy metal ballpoint pen and a pair of heavy surgical steel shears. The metal tools slide to a halt with a distinct metallic click. Nia's fingers hover over her screen.

overall_soundscape: Heavy paper slam on metal, sharp English voice ultimatum, abrupt drop in outdoor ambience on the cut, replaced by cold interior air-conditioning rumble, low 60Hz fluorescent light hum, and the sharp slide and clatter of steel shears across an aluminum table.

non_diegetic_music: SILENT
```

### H3-04｜45–60 秒｜条件免责与体制做局

> **候选参考绑定｜H3-04**：见 [E01–E10 H3 80 段参考输入清单](../视觉资产/E01-E10/E01-E10_H3_80段参考输入清单.md) 中本集本段对应行；模型只加载该行列出的角色、场景、道具状态与声音参考。

**生产卡**

- 参考输入：Cade、Coach Draper、Nia、S02 纪律裁决室、P04 协议文件、P05 签字笔、P07 剪刀、P06 资格环。
- 入口状态：裁决室三人关系建立，冷白无影灯反光，Draper 将文件推至桌心。
- 出口状态：Cade 双手撑桌正面质问，Nia 视线从卷宗抬起冷冷锁定 Cade；资格环仍完整。
- 台词：Coach Draper 制度施压 + Cade 核心反击。
- API 声音参考：`ref_audio_0`：Coach Draper；`ref_audio_1`：Cade。

**可复制给 H3 的提示词（黄金合体版 · 官方 MiniMax H3 规范）**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Cold clinical institutional interior in vertical 9:16. Fluorescent glare bounces off a long brushed stainless-steel conference table. Coach Draper slides a crisp paper document across the metal tabletop toward Cade. A heavy stainless-steel medical shears and a black signing pen rest beside the paper. Coach Draper leans forward, his voice a weary, bureaucratic monotone: <d> Coach Draper: "Sign the waiver, Cade. The Board calls it an 'administrative error.' You keep your bed, you keep the meal card. You just don't run." </d> [Shot 2] At 00:06.800, the camera cuts to an eye-level medium close-up of Cade standing at the table's edge. He plants both calloused palms firmly onto the steel surface, his knuckles whitening as tendons knot along his forearms, sweat dripping from his temple onto the metal. Cade speaks with gravelly, focused venom: <d> Cade: "Reeve couldn't beat my split in Lane 4. So you changed the clock into a court." </d> [Shot 3] At 00:11.800, the shot cuts to an over-the-shoulder angle past Cade. Across the table, student representative Nia, in an immaculate charcoal tailored blazer, pauses her fingers over an iPad and raises her icy, unblinking grey eyes directly into Cade's gaze.

overall_soundscape: Paper sliding over polished steel, dull clink of heavy medical shears on metal, weary close-mic male bureaucratic delivery, deep rasping defiant male voice, low fluorescent lighting hum.

non_diegetic_music: SILENT
```

---

### H3-05｜60–75 秒｜Nia审判与Cade耳畔近身压迫（核心荷尔蒙高潮）

> **候选参考绑定｜H3-05**：见 [E01–E10 H3 80 段参考输入清单](../视觉资产/E01-E10/E01-E10_H3_80段参考输入清单.md) 中本集本段对应行；模型只加载该行列出的角色、场景、道具状态与声音参考。

**生产卡**

- 参考输入：Cade、Nia、Coach Draper、S02 纪律裁决室、P04 协议文件、P05 签字笔。
- 入口状态：Nia 视线迎上 Cade，Cade 离开桌沿大步绕桌逼近。
- 出口状态：Cade 俯身于 Nia 耳侧，体温热浪逼迫，右手已握紧黑笔；未落笔。
- 台词：Nia 平账宣判 + Cade 掠食者耳语。
- API 声音参考：`ref_audio_0`：Nia；`ref_audio_1`：Cade。

**可复制给 H3 的提示词（黄金合体版 · 官方 MiniMax H3 规范）**

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Tense eye-level vertical shot. Across the steel conference table, Nia maintains rigid posture in her tailored blazer, her voice icy, unhurried, dripping with institutional authority: <d> Nia: "At 03:14, your terminal hit the exam server. The police can read the log, or this room can bury it. You're not being punished, Cade. You're being balanced." </d> [Shot 2] At 00:06.200, the shot cuts to a dynamic tracking profile. Cade moves with predatory athletic grace, rounding the long table in two explosive strides and invading Nia's space. [Shot 3] At 00:08.500, the camera cuts to an extreme close-up standoff at a suffocating fifteen-centimeter distance. Cade towers over Nia, his damp gray tank top clinging to heavily defined pectoral and shoulder muscles, glistening with beads of sweat; his deep panting breath radiates athletic heat against Nia's porcelain cheek. Nia's throat pulse quickens visibly at her starched collar, yet her defiant grey eyes refuse to look down. [Shot 4] At 00:11.500, Cade leans down, planting a heavy calloused hand on Nia's leather armrest, his lips hovering mere centimeters from her ear as he whispers with low, raspy venom: <d> Cade: "Balance this, Nia: when that gate opens Friday, I'll be in the bleachers. Watching your pedigree lose." </d>

overall_soundscape: Calm, aristocratic female vocal delivery, sudden leather shoe strides, creaking leather armrest under palm pressure, heavy ragged male breath, intimate close-mic rasping whisper near ear, low air conditioner hum.

non_diegetic_music: SILENT
```

---

### H3-06｜75–90 秒｜撕破纸张签字与资格手环剪断

> **候选参考绑定｜H3-06**：见 [E01–E10 H3 80 段参考输入清单](../视觉资产/E01-E10/E01-E10_H3_80段参考输入清单.md) 中本集本段对应行；模型只加载该行列出的角色、场景、道具状态与声音参考。

**生产卡**

- 参考输入：Cade、Nia、Coach Draper、S02 纪律裁决室、P04 协议文件、P05 签字笔、P07 剪刀、P06 资格环。
- 入口状态：Cade 俯身在 Nia 耳侧，右手抓起黑笔。
- 出口状态：手环被剪断成两截落在桌面，Cade 转身大步离场；桌面留下签字残页与断环。
- 台词：无。
- API 声音参考：无台词；聚焦剪刀金属断裂声、笔尖撕纸声与离场脚步声。

**可复制给 H3 的提示词（黄金合体版 · 官方 MiniMax H3 规范）**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Extreme macro close-up of the paper surface. Cade's black ballpoint pen drags violently across the signature line, the sharp metal tip catching and slightly tearing the paper fiber as he signs "CADE" in jagged angular strokes. [Shot 2] At 00:03.500, Cade slams the pen flat onto the metal tabletop with a sharp clatter, straightens his chiseled frame, and thrusts his left wrist directly toward Coach Draper. [Shot 3] At 00:06.000, Coach Draper's hands tremble slightly as he slides the cold blade of the heavy surgical shears under the tight black qualification wristband on Cade's wrist. [Shot 4] At 00:08.500, the shears clamp shut with a sharp metallic snap! The severed composite plastic band splits in two, clattering and bouncing across the steel table to a halt beside Nia's iced coffee cup. [Shot 5] At 00:11.000, a medium tracking shot captures Cade staring at the raw red compression ring on his bare wrist, turning on his heel without a word, and striding out the heavy door like a released predator. Nia sits rigidly frozen in her chair, fingers clutching the armrests, breathing shallowly as she stares at the torn signature sheet.

overall_soundscape: Harsh ballpoint pen tearing paper, pen slamming metal table, cold steel blade scraping skin, sharp mechanical shear snap cutting plastic, plastic pieces bouncing on stainless steel, heavy retreating footsteps, closing door thud.

non_diegetic_music: SILENT
```

---

### H3-07｜90–105 秒｜地下通道储物柜与物资箱

> **候选参考绑定｜H3-07**：见 [E01–E10 H3 80 段参考输入清单](../视觉资产/E01-E10/E01-E10_H3_80段参考输入清单.md) 中本集本段对应行；模型只加载该行列出的角色、场景、道具状态与声音参考。

**生产卡**

- 参考输入：Cade、S03 地下物资装备通道、旧训练包、暴力拆毁储物柜、D-10 退出箱。
- 入口状态：地下通道昏暗阴冷，水管滴水；Cade 提包推门而入，左腕无环。
- 出口状态：Cade 蹲在底层置物架前，左手拨开积灰，手指停在封箱胶带旁。
- 台词：无。
- API 声音参考：无台词；水滴回声、铁门摩擦声、布料摩擦与纸箱积灰。

**可复制给 H3 的提示词（黄金合体版 · 官方 MiniMax H3 规范）**

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Gritty vertical wide shot of a subterranean utility corridor beneath the gym. Flickering fluorescent tubes illuminate peeling paint, exposed steam pipes, and slow rhythmic water droplets dripping into puddles. Cade pushes open a heavy rusted iron door with an abrasive squeak, carrying a worn duffel bag in his bare left hand. [Shot 2] At 00:04.500, the camera cuts to a medium shot following Cade to a row of battered lockers. His locker has had its hasp lock violently pried apart, the bent steel door hanging ajar. Cade pauses, dark eyes narrowing with razor-sharp instinct. [Shot 3] At 00:08.500, a low tracking shot follows Cade crossing the narrow passage toward the opposite storage rack. He drops smoothly onto one knee on the damp concrete floor. [Shot 4] At 00:11.800, an eye-level close-up at floor level shows Cade's calloused fingers wiping a layer of grime and dust from a heavy kraft cardboard carton sealed with industrial brown tape on the bottom shelf, revealing a pristine white blank label affixed to the box front.

overall_soundscape: Rusted iron door squeak and latch, rhythmic water dripping on wet concrete, damp sneaker steps, duffel bag canvas shifting, bent metal locker creak, and the soft swipe of fingers clearing dust from cardboard.

non_diegetic_music: SILENT
```

---

### H3-08｜105–120 秒｜证据成立，监控与脚步反包围

> **候选参考绑定｜H3-08**：见 [E01–E10 H3 80 段参考输入清单](../视觉资产/E01-E10/E01-E10_H3_80段参考输入清单.md) 中本集本段对应行；模型只加载该行列出的角色、场景、道具状态与声音参考。

**生产卡**

- 参考输入：Cade、S03 地下物资装备通道、D-10 退出箱、红外监控探头。
- 入口状态：箱体封好，空白标签朝向 Cade，手指停在封条旁。
- 出口状态：Cade 抬头定住，监控红灯已亮，画外皮鞋脚步逼近；断章黑屏。
- 台词：无；三条标签文字由后期叠加。
- API 声音参考：无台词；极低环境音、监控微型齿轮转动声、三步逼近皮鞋脚步声。

**可复制给 H3 的提示词（黄金合体版 · 官方 MiniMax H3 规范）**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Extreme close-up of Cade's eyes looking down at the blank white label on the sealed box. His pupils contract sharply into pinpricks as he traces the edges of the box, realizing in horror that the exit package was prepared ten days prior to the incident. [Shot 2] At 00:05.500, the shot cuts to a high-angle macro insert above the east shelf. A small black hemispherical infrared security camera emits a tiny mechanical servo click and rotates downward, locking its lens onto Cade; its dormant red LED indicator snaps into a bright solid crimson glow, casting a ruby pinpoint reflection across Cade's iris. [Shot 3] At 00:09.500, a low-angle medium shot frames Cade frozen on one knee, his bare left wrist resting on his knee with a faint red compression welt from where the band was severed, completely ringless. From the darkness of the corridor south end, slow, heavy, polished leather shoe footsteps echo closer: step... step... step. [Shot 4] At 00:12.800, the camera pushes aggressively into Cade's face. He snaps his head up toward the darkness, jaw hardened like granite, eyes blazing with dangerous defiance. At 00:14.800, the frame violently cuts to pitch black.

overall_soundscape: Cardboard fiber rustle, deep silence of underground cavern, tiny mechanical camera servo whir and click, three echoing heavy leather-sole footsteps approaching on concrete, Cade holding his breath, sudden hard cut to silence.

non_diegetic_music: SILENT
```

## 5. 生成后 QC 顺序

### 单段 QC

- 时长是否为 15.0 秒，画幅是否为 9:16。
- 人物脸、发型、服装、左腕资格环状态是否与相邻段一致。
- 镜头是否遵守东侧摄影安全区、南北轴和 180° 表演轴。
- 关键动作是否完成“接触—受力—位移—结果”：急停、拍文件、签字、剪环、拆锁、读取、监控转向。
- H3 原生音频是否为英文、是否出现错词、中文朗读、口型漂移或环境声断裂。
- 是否出现模型生成的乱码、字幕、校徽、品牌、水印或多余人物。

### 八段连续 QC

1. `H3-01` 的红灯和急停能否自然接入 `H3-02` 的群像嘘笑。
2. `H3-02` 文件悬停能否接入 `H3-03` 文件落台；不得重复取文件或让文件消失。
3. `H3-03` 的裁决室桌面是否接入 `H3-04` 的未签协议状态。
4. `H3-04` 的 Nia 判断视线是否接入 `H3-05` 的主动逼近；不得把关系剪成和解。
5. `H3-05` 的黑笔和完整资格环是否接入 `H3-06` 的签字与剪环。
6. `H3-06` 桌面两截资格环是否在 Cade 离场后保持，地下段则明确不再回到手腕。
7. `H3-07` 的封箱和空白标签是否接入 `H3-08` 的读取；箱子全程不打开。
8. `H3-08` 中 D-10 文字是否只由后期叠加，监控红灯是否晚于读取动作，脚步是否始终不露脸。

### 当前状态

`ready_for_h3_segment_prompt` → 待生成 `H3-01`、`H3-02` 试片 → 通过连续性 QC 后批量生成 `H3-03` 至 `H3-08` → 全集 120 秒完整播放 QC。
