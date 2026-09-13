# 跨集资产与段间连续性管理合同

## 1. 角色视觉与声线锁定表

| 角色 ID | 角色名 | 视觉资产锁定文件 | 声线锁定文件 (32kHz WAV) | Voice 控制描述词 |
|---|---|---|---|---|
| C01 | Cade | `assets/C01_Cade_reference_v1.png` | `VOICE_CADE_v2_age18_h3_32k.wav` | youthful low tenor; late-teen resonance; restrained rough edge; quiet intensity; neutral international English |
| C02 | Reeve | `assets/C02_Reeve_reference_v1.png` | `VOICE_REEVE_v2_age18_h3_32k.wav` | youthful baritone-tenor; polished diction; controlled confidence; faint amused edge |

---

## 2. 段间转场与继承判定矩阵

| 段落编号 | 起止时间 | 场景 ID | 转场类型 | 尾帧继承源 | 轴线方向 (180° Rule) |
|---|---|---|---|---|---|
| H3-01 | 00s - 15s | S01 黎明跑道 | `HARD_CUT` | 独立起幅（参考场景基底） | 镜头在跑道西侧（Y < 0） |
| H3-02 | 15s - 30s | S01 黎明跑道 | `TAIL_RELAY` | 继承 H3-01 尾帧（t=14.5s） | 镜头保持在跑道西侧（Y < 0） |
| H3-03 | 30s - 45s | S02 听证大厅 | `HARD_CUT` | 空间切换，无尾帧继承 | 室内中轴线东侧 |

---

## 3. 道具与损伤状态机

| 道具 / 伤情 | 初始状态（E01） | 转变事件 | 后续状态（E02+） | 规则约束 |
|---|---|---|---|---|
| 牛皮纸听证档案 | 密封带火漆印 | E01_H3-05 撕开火漆 | 封面破损，白纸外露 | 不得在新镜头中自动复原为未拆封状态 |
| 训练服湿透程度 | 干燥无汗渍 | E01_H3-02 高强度冲刺 | 领口与胸骨处深色汗浸浸润 | 10分钟剧情内不得自动风干 |
