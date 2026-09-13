# OmniDirector-H3 (全知导演 H3)
## 微短剧剧作重构 · 3D空间预演 · 动力学解耦 · 官方多模态编译 · 无人值守批处理工业系统

---

## 一、系统诞生背景与核心痛点

随着生成式视频大模型（如 MiniMax H3、Kling、Runway Gen-3、Sora、Hailuo 等）在影视与出海微短剧领域的爆发，工业化生产面临着严重的**“技术—剧作鸿沟”**：

1. **“扩散融化”（Diffusion Melting）与多肢畸变**：
   传统剧本充满了人类演员可轻松履行的复合动作长句（例如：“*他急步冲进房间，坐在铁椅上一边大口灌着咖啡，一边愤怒地瞪着门口的女主*”）。在视频扩散模型中，这种复合动作指令会导致 Latent 潜空间注意力崩溃，产生肢体融化、第三只手、面部扭曲与物体随机变形。
2. **三维空间失序与 180° 越轴灾难**：
   纯文本提示词缺乏物理世界三维坐标概念。镜头在段落间切换时，常出现角色左右站位颠倒、视线错位、光影逆转，彻底破坏影视语言的轴线规则。
3. **敏感词拦截与审查误杀（False Positives）**：
   微短剧核心卖点往往包含高荷尔蒙、身材张力与亲密拉扯。大量创作者直接输入露骨词汇（如“性感”、“胸肌”、“抚摸”、“湿吻”），频繁触发大模型安全网关报错，导致生成任务被批量丢弃。
4. **劣质配乐污染成片，摧毁后期混音**：
   模型原生端到端生成的音频往往混入低质、无法消除的合成器伴奏（BGM），掩盖了关键对白与物理拟音（Foley），使工业级专业后期音效混音无法实施。
5. **通宵盯盘与算力成本浪费**：
   一部 10 集微短剧包含 80 个 15 秒视频片段（共 1,200 秒高码率成片）。创作者若在网页端手动反复复制粘贴提示词，不仅耗尽精力，更无法利用各大 GPU 云平台在凌晨特惠时段（00:01 至 08:00）的半价算力窗口。

**OmniDirector-H3** 为解决上述痛点而生。它不是一个简单的 Prompt 集合，而是一套涵盖“剧本重塑—空间校验—语法编译—自动化批处理”的工业级端到端电影级生产体系。

---

## 二、四大子体系深度解析

### 1. 第一阶：剧作重构与动力学解耦 (`01_screenplay_dramaturgy`)

*让剧本从“文学描写”转译为“扩散模型可执行的物理原子向量”。*

- **Mode B 出海微短剧标准**：
  - **动作调度（`△`）**：全中文精准白描。利用中文在动词细分与动量描述上的高密度，为生成控制提供清晰的因果链。
  - **对白语言**：地道纯正的英语口语。专为出海短剧（ReelShort、DramaBox、ShortMax、TikTok）设计，节奏紧凑、短促有力，符合 18 岁青春竞技与悬疑调性。
  - **潜台词系统**：显式标注 `[中文潜台词: ...]`，仅供主创审核表演内核，绝不录入台词发音标签。
- **原子动力学解耦铁律（Atomic Momentum Decoupling）**：
  - **单节拍单矢量原则**：一个动作分镜内只允许出现**一个核心动词**。
  - **接触—受力—反应三角闭环**：
    $$\text{接触 (Contact)} \longrightarrow \text{物理受力 (Reaction)} \longrightarrow \text{稳态/释放 (Steady State)}$$
  - 严禁将奔跑、抓取、说话、转头堆叠在同一 3 秒窗口内。
- **生理体感张力白描（防审查设计）**：
  - 彻底摒弃易触发敏感词拦截的主观词汇，全面替换为客观可观察的物理生理细节：
    - *描写雄性荷尔蒙与健美身材* $\rightarrow$ 湿透的深灰训练背心紧贴起伏的胸肌轮廓、锁骨凹陷处的汗珠折射冷光、前臂紧绷时浮现的肌腱与青筋。
    - *描写极度亲密与对抗拉扯* $\rightarrow$ 距离缩减至极限 10 公分、粗重滚烫的气流在零度晨雾中凝结为白气、喉结剧烈滚动、指尖距离手腕悬停一毫米。

---

### 2. 第二阶：Blender 3D空间调度与分镜校验 (`02_spatial_blocking_audit`)

*在生成之前，用低成本 3D 代理资产筑牢物理世界坐标防线。*

- **180° 动作轴线铁律**：
  - 在无头 Blender 脚本中建立核心对话双方的虚拟连线（Action Axis）。
  - 所有摄影机位强制锁定在轴线同侧（如 $Y < 0$ 的跑道西侧）；需要翻转机位时，必须中间插入严格的骑轴中立镜头（如头顶俯拍或背侧过轴）。
- **24fps 物理运动预算（Motion Budget）**：
  - 在 3.5 秒镜头预算内（$3.5 \times 24 = 84$ 帧），按人体极限运动速度（冲刺 10 m/s，常速 1.2 m/s，手臂伸展 0.8s）精密核算位移，杜绝模型为了完成不可能的超长动作而出现“快进式抽搐”。
- **段间连续性裁决合同（Continuity Arbiter）**：
  - `TAIL_RELAY`（尾帧接力）：同场同时间连续段落，将前一段最后 1.0 秒（稳态锁定期）的渲染帧作为下一段的起幅参考图（`ref_image_0`）。
  - `HARD_CUT`（硬切转场）：跨场景空间跳跃，切断尾帧继承，启用全新场景参考图。
  - `CAUSAL_MATCH_CUT`（因果匹配切）：跨空间匹配特定物体或动量矢量。
- **道具与伤情状态机**：
  - 追踪道具全生命周期（未开封 $\rightarrow$ 撕毁 $\rightarrow$ 散落；干燥 $\rightarrow$ 湿透 $\rightarrow$ 污损），严禁出现下一镜头道具自动复原的穿帮事故。

---

### 3. 第三阶：MiniMax H3 官方提示词编译器 (`03_h3_prompt_compiler`)

*彻底废弃自建六大模块，回归 MiniMax 官方底层注意力机制。*

实测证明，早期自建的中文“六大模块”提示词会稀释扩散模型的 Cross-Attention，导致时间戳切镜失败。OmniDirector-H3 升级为官方 **四大纯净字段结构**：

1. **参考图片对齐声明（Header）**：
   ```text
   For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
   ```
2. **多模态时序脚本总控（`integrated_multimodal_description:`）**：
   - 首镜头确立画质基调：`[Shot 1] Live-action, cinematic vertical 9:16 realism...`
   - 后续镜头使用毫秒级绝对递增时间戳：`[Shot 2] At 00:03.500, the camera cuts to...`
   - 对白严格使用官方发声标签：`<d> Speaker: "Exact spoken line" </d>`
3. **环境与物理 Foley（`overall_soundscape:`）**：
   - 细致罗列鞋钉抓地声、冷风呼啸、门禁锁死撞击声、低频空调嗡鸣。
4. **非剧情配乐锁（`non_diegetic_music: SILENT`）**：
   - **核心工业标准**：生成阶段强制为 `SILENT`。保留极其干净的对白与拟音频道，为成片阶段的商业配乐预留纯净声道。
5. **确定性 CLI 语法审计器 (`tools/audit_h3_prompts.py`)**：
   - 自动检测标签闭合配对、时间戳单调递增性、字数边界与非法字符。

---

### 4. 第四阶：无人值守通宵特惠批处理调度器 (`04_production_orchestrator`)

*精准卡位凌晨特惠时段，省时、省力、省成本。*

- **特惠窗口锁（00:01:00 定时自动唤醒）**：
  - 大量算力平台（如 AutoDL 等）夜间算力折扣高达 50%。
  - 脚本内置秒级高精度定时器，配合操作系统防休眠锁（macOS `caffeinate`），在午夜 00:01:00 准时苏醒启动。
  - 设置 08:00:00 强制停机保护，杜绝跨出优惠时段产生高额账单。
- **断点自愈状态机 (`batch_progress.json`)**：
  - 实时记录每个片段的生命周期：`PENDING` $\rightarrow$ `SUBMITTING` $\rightarrow$ `RUNNING` $\rightarrow$ `COMPLETED`。
  - 若遇网络抖动或崩溃，重启脚本即刻从最后一个未完成片段继续执行，**绝不重复扣费**。
- **资产自动化编译与装配**：
  - 自动将角色正脸、服装图、场景空镜底图及 32kHz 角色参考音频编码为 Base64 负载或对象存储链接。
- **全自动批量成片下载与 QC 校验**：
  - 自动轮询 API 状态，下载 MP4 并进行容器完整性校验，提取关键帧生成审查接触表（Contact Sheet）。

---

## 三、目录架构一览

```text
OmniDirector-H3/
├── README.md                          # 旗舰双语介绍主页
├── README_CN.md                       # 中文完整技术白皮书（本文档）
├── README_EN.md                       # 英文完整技术白皮书
├── SKILL.md                           # AI Agent 标准 Skill 规范定义
├── LICENSE                            # MIT 开源许可证
│
├── subskills/                         # 四大子体系规范手册
│   ├── 01_screenplay_dramaturgy/      # 剧作重构、Mode B 规范与解耦铁律
│   │   ├── SKILL.md
│   │   └── rules.md
│   ├── 02_spatial_blocking_audit/     # Blender 3D 预演、180°轴线与连续性合同
│   │   ├── SKILL.md
│   │   └── blocking_contract.md
│   ├── 03_h3_prompt_compiler/         # MiniMax H3 官方规范、时间戳与标签标准
│   │   ├── SKILL.md
│   │   └── syntax_guide.md
│   └── 04_production_orchestrator/    # 无人值守批处理、特惠定时与断点状态机
│       ├── SKILL.md
│       └── checkpoint_spec.md
│
├── tools/                             # 工业生产命令行工具集
│   ├── audit_h3_prompts.py            # H3 提示词确定性语法与标签审计器
│   ├── compile_screenplay_to_h3.py   # 剧本快速转 H3 多模态脚手架编译器
│   ├── run_overnight_batch.py         # 通宵无人值守特惠窗口批处理引擎
│   ├── blender_proxy_previz.py        # 无头 Blender 3D 轴线空间校验工具
│   └── push_to_github.sh              # 一键发布至 GitHub 辅助脚本
│
├── templates/                         # 工业生产标准模板库
│   ├── screenplay_spec_b_template.md  # Mode B 中英双模剧本模板
│   ├── h3_prompt_template.md          # MiniMax H3 15秒官方提示词模板
│   └── continuity_contract_template.md# 跨集资产、转场判定与状态机跟踪表
│
└── examples/                          # 实战验证资产库（E01 完整生产包）
    ├── E01_screenplay_sample.md       # 实战剧本：高张力、强荷尔蒙竞技悬疑
    ├── E01_h3_prompts_sample.md       # 实战编译提示词包（8段全部通过 0 错误审计）
    └── batch_progress_example.json    # 批处理断点状态记录文件范例
```

---

## 四、5分钟快速上手指南

### 步骤 1：克隆仓库与准备环境
```bash
git clone https://github.com/egguy886/OmniDirector-H3.git
cd OmniDirector-H3
chmod +x tools/*.py tools/*.sh
```

### 步骤 2：对提示词执行严格审计（确保 0 语法错误）
在将提示词提交给模型前，使用审计工具排除任何未闭合的 `<d>` 标签或违禁模块：
```bash
python3 tools/audit_h3_prompts.py --input examples/E01_h3_prompts_sample.md
```

### 步骤 3：一键将剧本编译为 H3 多模态分段脚手架
```bash
python3 tools/compile_screenplay_to_h3.py \
  --input templates/screenplay_spec_b_template.md \
  --output my_episode_prompts.md
```

### 步骤 4：启动通宵无人值守批处理引擎
在系统环境变量中配置您的 API 密钥，然后启动防休眠通宵守护进程：
```bash
export AUTODL_API_KEY="您的_API_KEY"

# macOS 用户使用 caffeinate 防休眠锁，等待午夜 00:01 自动唤醒执行：
caffeinate -d -i -m -u python3 tools/run_overnight_batch.py

# 也可以进行单集即刻测试或模拟运行：
python3 tools/run_overnight_batch.py --dry-run
```

---

## 五、生态与开源许可

本项目基于 **MIT License** 完全开源。欢迎各影视制作团队、AI 短剧工作室、独立导演以及海外短剧发行方交流使用并提交 Pull Request！
