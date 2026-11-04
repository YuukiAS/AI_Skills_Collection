# Phase A：Asteria 静态证据包与用户审阅队列

日期：2026-11-04  
状态：PHASE_A_ACTIVE  
用途：在 Claude Stage 1 之前收敛历史证据，减少 API 消耗，并让用户逐项确认真正值得保留的历史资产。  
重要：本文件中的“优先审阅”只是两轮 GPT Pro 与历史证据给出的高信息量排序，**不是用户接受结论**。所有用户裁决均保持 `OPEN`，直到用户亲自确认。

## 1. Claude Stage 1 的硬输入规则

Claude 后续不得为了理解历史去启动 Obsidian、浏览器、Figma、网页预览或自行跑视觉宿主。Phase A 应提前把需要看的视觉证据变成静态文件：
- 原始 PDF 中关键页 / 已归档截图；
- 现有历史图库的静态截图、联系表和必要 GIF；
- 两轮 GPT Pro 的正式结论；
- 已有 Deep Research 的高信号摘要与必要原文入口。

Claude 允许直接读取本地图片/PDF页面像素，但不负责现场操作 UI。真正的浏览器/Obsidian 运行、截图、录制和前后对照由 Codex/GPT 在后续实施与验收阶段准备。

Claude Stage 1 不得：
- 全仓盲扫；
- 重跑 Deep Research；
- 自行打开 Obsidian/浏览器做探索；
- 安装 Skill 大全/MCP 大全；
- 直接开始完整 redesign；
- 把本文件的候选保留意见当作用户 KEEP。

## 2. 已存在的全量视觉入口

### Blueprint
- 全量版本目录：`YuukiAS/Asteria-Blueprint@archive/asteria-blueprint-version-gallery-20261103`
- 版本总表：`docs/design/version-gallery/VERSION_CATALOG.md`
- 结构化清单：`docs/design/version-gallery/manifest.json`
- 原始 230 页 PDF：`docs/design/version-gallery/assets/sources/ChatGPT_Asteria-BluePrint-裁决_20261103-1638.pdf`
- 已恢复 36 个版本，其中 16 个保留真实交互；Phase A 不要求 Claude逐个运行交互。

### Atlas
- 全量视觉历史：`YuukiAS/Asteria-Atlas@archive/atlas-visual-history`
- 联系表：`visual-history/assets/contact-sheet.png`
- 时间线：`visual-history/source/THREAD_TIMELINE_ZH.md`
- 结构化目录：`visual-history/source/CATALOG.json`
- 原始 208 页 PDF：`visual-history/source/ChatGPT_建立文献地图架构_20261103-1749.pdf`
- 12 个主时间线条目均已有静态证据或明确标记“无新视觉成品”。

## 3. 第一批优先审阅：Blueprint

这些版本优先是因为：曾被部分采用、出现过局部正面反馈、承担关键设计转折、或是当前最强候选。仍不代表整版应该保留。

| # | 版本 | 名称 | 历史状态 | 为什么值得先看 | 静态入口 | 交互入口（仅供 GPT/Codex 后续） | 用户裁决 |
|---:|---|---|---|---|---|---|---|
| 1 | `01-asteria-v2-concepts` | Asteria 2.0 · 已采用的视觉概念集 | ACCEPTED_DIRECTION | 仓库明确保存为 Asteria 2.0 的已采用视觉与交互参考；图内科学事实不具有权威。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/01-asteria-v2-concepts/original/B_dark_architecture.png) | — | OPEN |
| 5 | `05-showcase-r2-gpt56` | 复杂系统展示 · R2 GPT-5.6 | PARTIALLY_ADOPTED | 后续收敛保留同图路径、关系探索或状态/手机阅读等能力；独立比较推荐 GPT-6 作基线，不等于用户整版最终接受。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/05-showcase-r2-gpt56/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/05-showcase-r2-gpt56/preview/index.html` | OPEN |
| 6 | `06-showcase-r2-gpt6` | 复杂系统展示 · R2 GPT-6 | PARTIALLY_ADOPTED | 后续收敛保留同图路径、关系探索或状态/手机阅读等能力；独立比较推荐 GPT-6 作基线，不等于用户整版最终接受。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/06-showcase-r2-gpt6/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/06-showcase-r2-gpt6/preview/index.html` | OPEN |
| 9 | `09-evolution-pro-a` | Architecture Evolution · Pro-A | PARTIALLY_ADOPTED | 后续 Next 收敛吸收稳定对象、固定来源、因果修订或类型机制；平行工作集 / Ledger 产品被放弃。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/09-evolution-pro-a/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/09-evolution-pro-a/preview/index.html` | OPEN |
| 10 | `10-evolution-pro-b` | Architecture Evolution · Pro-B | PARTIALLY_ADOPTED | 后续 Next 收敛吸收稳定对象、固定来源、因果修订或类型机制；平行工作集 / Ledger 产品被放弃。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/10-evolution-pro-b/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/10-evolution-pro-b/preview/index.html` | OPEN |
| 11 | `11-next-pro-a` | Asteria Next convergence · Pro-A | PARTIALLY_ADOPTED | 用户暂按推荐保留 A 的对象上下文、适度淡化；B 的状态、消费者与手机载荷阅读被局部吸收。两者的编号机制均不接受。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/11-next-pro-a/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/11-next-pro-a/preview/preview.html` | OPEN |
| 12 | `12-next-pro-b` | Asteria Next convergence · Pro-B | PARTIALLY_ADOPTED | 用户暂按推荐保留 A 的对象上下文、适度淡化；B 的状态、消费者与手机载荷阅读被局部吸收。两者的编号机制均不接受。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/12-next-pro-b/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/12-next-pro-b/preview/index.html` | OPEN |
| 13 | `13-blueprint-blind-pro-a` | Blueprint 盲实施充分性 · Pro-A | PARTIALLY_ADOPTED | 独立 Work 推荐 A 的对象骨架、吸收 B 的类型机制与消费者链；Freeze 范围仍需重做，均未获整版冻结。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/13-blueprint-blind-pro-a/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/13-blueprint-blind-pro-a/preview/index.html` | OPEN |
| 14 | `14-blueprint-blind-pro-b` | Blueprint 盲实施充分性 · Pro-B | PARTIALLY_ADOPTED | 独立 Work 推荐 A 的对象骨架、吸收 B 的类型机制与消费者链；Freeze 范围仍需重做，均未获整版冻结。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/14-blueprint-blind-pro-b/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/14-blueprint-blind-pro-b/preview/index.html` | OPEN |
| 18 | `18-system-direction-1` | System Architecture 三方向 · Editorial / 学术排版 | DIAGNOSTIC_ONLY | 作为后续四方向的视觉研究输入；聊天审查偏向空间图谱，但用户尚未接受，流体色块含义受到质疑。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/18-system-direction-1/screenshots/p172-01-X741.png) | — | OPEN |
| 19 | `19-system-direction-2` | System Architecture 三方向 · 严谨暗色工具 | DIAGNOSTIC_ONLY | 作为后续四方向的视觉研究输入；聊天审查偏向空间图谱，但用户尚未接受，流体色块含义受到质疑。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/19-system-direction-2/screenshots/p172-02-X742.png) | — | OPEN |
| 20 | `20-system-direction-3` | System Architecture 三方向 · 空间系统图谱 | DIAGNOSTIC_ONLY | 作为后续四方向的视觉研究输入；聊天审查偏向空间图谱，但用户尚未接受，流体色块含义受到质疑。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/20-system-direction-3/screenshots/p172-03-X743.png) | — | OPEN |
| 25 | `25-workbench-r1-1` | Research Systems Workbench R1 · 空间镜头工作台 | DIAGNOSTIC_ONLY | 用户否决整屏过载及内部术语；实现台局部获正面反馈，并要求多 binding、可切换和行号可选。该轮随后被正式降为诊断用途。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/25-workbench-r1-1/screenshots/p196-01-X841.png) | — | OPEN |
| 26 | `26-workbench-r1-2` | Research Systems Workbench R1 · 聚焦优先研究 IDE | DIAGNOSTIC_ONLY | 用户否决整屏过载及内部术语；实现台局部获正面反馈，并要求多 binding、可切换和行号可选。该轮随后被正式降为诊断用途。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/26-workbench-r1-2/screenshots/p196-02-X842.png) | — | OPEN |
| 27 | `27-workbench-r1-3` | Research Systems Workbench R1 · 多尺度系统画布 | DIAGNOSTIC_ONLY | 用户否决整屏过载及内部术语；实现台局部获正面反馈，并要求多 binding、可切换和行号可选。该轮随后被正式降为诊断用途。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/27-workbench-r1-3/screenshots/p196-03-X843.png) | — | OPEN |
| 28 | `28-workbench-r1-4` | Research Systems Workbench R1 · 证据中心架构 | DIAGNOSTIC_ONLY | 用户否决整屏过载及内部术语；实现台局部获正面反馈，并要求多 binding、可切换和行号可选。该轮随后被正式降为诊断用途。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/28-workbench-r1-4/screenshots/p196-04-X844.png) | — | OPEN |
| 36 | `36-gpt6pro-total-redesign` | GPT-6 Pro · Total redesign | CURRENT_BEST | 按本次用户指令保存当前最佳完整候选；不是用户最终接受。原 review 亦明确不代表用户接受、完整产品验收或新科研运行结果。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/36-gpt6pro-total-redesign/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/36-gpt6pro-total-redesign/preview/candidate.html` | OPEN |

特别注意：
- 25–28 的 Workbench 整屏并未被接受；历史上真正值得重新看的，是“实现台”局部、多实现 binding、切换与行号按需等能力。
- 18–20 是方向研究，不是已接受视觉；可以用于比较哪些空间/排版语言有潜力。
- 36 是 `CURRENT_BEST`，不是用户最终接受。

## 4. 第一批优先审阅：Atlas

| 版本 | 名称 | 历史状态 | 历史判断 | 静态入口 | 用户裁决 |
|---|---|---|---|---|---|
| V01 | MVP GPT-5.6 | REJECTED | 内容部分保留；主图视觉否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v01-mvp-gpt56/pdf/p088-01.png) | OPEN |
| V02 | MVP GPT-6 | REJECTED | 事实、Bases 与笔记保留；任务卡片矩阵否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v02-mvp-gpt6/source-files/research/dii-atlas-mvp/gpt6/screenshots/canvas-overview.png) | OPEN |
| V03 | Visual Redesign SOL | REJECTED | 语义探索有价值；视觉方案否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v03-visual-redesign-sol/canvas-renders/DII_FIELD_OVERVIEW.png) | OPEN |
| V04 | Visual v1 GPT-5.6 | REJECTED | 局部关系语义可参考；视觉母版资格否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v04-visual-v1-gpt56/source-files/research/dii-atlas-visual-v1/gpt56/01-domain-overview.png) | OPEN |
| V05 | Visual v1 GPT-6 | VISUAL_BASELINE | 后续正式指定的唯一视觉母版；实机缺陷仍需修复。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v05-visual-v1-gpt6/source-files/research/dii-atlas-visual-v1/gpt6/01-domain-overview.png) | OPEN |
| V06 | Native Graph 初版 | ENGINEERING_RETAINED | 原生工程底座保留；初始 Level 0 视觉否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v06-native-graph-initial/pdf/p165-01.png) | OPEN |
| V07 | Native Level 0 Landscape | ENGINEERING_RETAINED | 信息架构改善；可借 UI 框架，主地图视觉不作母版。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v07-native-level0-landscape/pdf/p180-01.png) | OPEN |
| V08 | Astra Ultra / Visual System v2 | REJECTED | 信息架构与实现约束可参考；视觉方案否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v08-astra-visual-system-v2/source-files/design/visual-v2-prototype/evidence/01-landscape-light.png) | OPEN |
| V10 | Final Visual Refinement Pro | CURRENT_DESIGN_CANDIDATE | 最新设计候选，等待用户判断；尚不等于原生实现。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v10-final-visual-refinement/source-files/design/final-visual-refinement/screens/01-field-overview-light.png) | OPEN |

特别注意：
- V05 的“视觉母版”是历史正式指定，不等于用户最终接受；实机可读性已经失败过。
- V06/V07 主要有工程/UI框架价值，不能把工程保留误写成视觉保留。
- V08 是 Astra 结果：信息架构/语义缩放有参考价值，但视觉本身被用户否决。
- V10 是当前设计候选，不是原生 Obsidian 成品。

## 5. 全量历史审阅队列：Blueprint 36 项

以下全部保持 OPEN，避免我的优先级筛选吞掉潜在好东西。

| # | 版本 | 名称 | 历史状态 | 历史原因 | 静态入口 | 交互入口 | 用户裁决 |
|---:|---|---|---|---|---|---|---|
| 1 | `01-asteria-v2-concepts` | Asteria 2.0 · 已采用的视觉概念集 | ACCEPTED_DIRECTION | 仓库明确保存为 Asteria 2.0 的已采用视觉与交互参考；图内科学事实不具有权威。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/01-asteria-v2-concepts/original/B_dark_architecture.png) | — | OPEN |
| 2 | `02-asteria-rc19` | Asteria 2.0.0-rc.19 · 原宿主 | DIAGNOSTIC_ONLY | PDF 将其作为 Next 的真实宿主基线；稳定版尚未发布，未找到最终用户接受结论。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/02-asteria-rc19/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/02-asteria-rc19/preview/index.html` | OPEN |
| 3 | `03-showcase-r1-gpt56` | 复杂系统展示 · 第一轮 GPT-5.6 | REJECTED | 两套首页均未呈现完整架构，转成叙事、步骤和组件说明。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/03-showcase-r1-gpt56/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/03-showcase-r1-gpt56/preview/index.html` | OPEN |
| 4 | `04-showcase-r1-gpt6` | 复杂系统展示 · 第一轮 GPT-6 | REJECTED | 两套首页均未呈现完整架构，转成叙事、步骤和组件说明。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/04-showcase-r1-gpt6/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/04-showcase-r1-gpt6/preview/index.html` | OPEN |
| 5 | `05-showcase-r2-gpt56` | 复杂系统展示 · R2 GPT-5.6 | PARTIALLY_ADOPTED | 后续收敛保留同图路径、关系探索或状态/手机阅读等能力；独立比较推荐 GPT-6 作基线，不等于用户整版最终接受。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/05-showcase-r2-gpt56/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/05-showcase-r2-gpt56/preview/index.html` | OPEN |
| 6 | `06-showcase-r2-gpt6` | 复杂系统展示 · R2 GPT-6 | PARTIALLY_ADOPTED | 后续收敛保留同图路径、关系探索或状态/手机阅读等能力；独立比较推荐 GPT-6 作基线，不等于用户整版最终接受。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/06-showcase-r2-gpt6/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/06-showcase-r2-gpt6/preview/index.html` | OPEN |
| 7 | `07-editorial-gpt56` | 复杂系统展示 · 内容审查修订 GPT-5.6 | DIAGNOSTIC_ONLY | 真实修订副本，用于验证内容删并、信息下沉及手机阅读顺序；不是新的用户接受方向。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/07-editorial-gpt56/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/07-editorial-gpt56/preview/index.html` | OPEN |
| 8 | `08-editorial-gpt6` | 复杂系统展示 · 内容审查修订 GPT-6 | DIAGNOSTIC_ONLY | 真实修订副本，用于验证内容删并、信息下沉及手机阅读顺序；不是新的用户接受方向。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/08-editorial-gpt6/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/08-editorial-gpt6/preview/index.html` | OPEN |
| 9 | `09-evolution-pro-a` | Architecture Evolution · Pro-A | PARTIALLY_ADOPTED | 后续 Next 收敛吸收稳定对象、固定来源、因果修订或类型机制；平行工作集 / Ledger 产品被放弃。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/09-evolution-pro-a/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/09-evolution-pro-a/preview/index.html` | OPEN |
| 10 | `10-evolution-pro-b` | Architecture Evolution · Pro-B | PARTIALLY_ADOPTED | 后续 Next 收敛吸收稳定对象、固定来源、因果修订或类型机制；平行工作集 / Ledger 产品被放弃。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/10-evolution-pro-b/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/10-evolution-pro-b/preview/index.html` | OPEN |
| 11 | `11-next-pro-a` | Asteria Next convergence · Pro-A | PARTIALLY_ADOPTED | 用户暂按推荐保留 A 的对象上下文、适度淡化；B 的状态、消费者与手机载荷阅读被局部吸收。两者的编号机制均不接受。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/11-next-pro-a/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/11-next-pro-a/preview/preview.html` | OPEN |
| 12 | `12-next-pro-b` | Asteria Next convergence · Pro-B | PARTIALLY_ADOPTED | 用户暂按推荐保留 A 的对象上下文、适度淡化；B 的状态、消费者与手机载荷阅读被局部吸收。两者的编号机制均不接受。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/12-next-pro-b/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/12-next-pro-b/preview/index.html` | OPEN |
| 13 | `13-blueprint-blind-pro-a` | Blueprint 盲实施充分性 · Pro-A | PARTIALLY_ADOPTED | 独立 Work 推荐 A 的对象骨架、吸收 B 的类型机制与消费者链；Freeze 范围仍需重做，均未获整版冻结。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/13-blueprint-blind-pro-a/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/13-blueprint-blind-pro-a/preview/index.html` | OPEN |
| 14 | `14-blueprint-blind-pro-b` | Blueprint 盲实施充分性 · Pro-B | PARTIALLY_ADOPTED | 独立 Work 推荐 A 的对象骨架、吸收 B 的类型机制与消费者链；Freeze 范围仍需重做，均未获整版冻结。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/14-blueprint-blind-pro-b/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/14-blueprint-blind-pro-b/preview/index.html` | OPEN |
| 15 | `15-unified-showcase` | Unified showcase · 统一原型 | REJECTED | 用户否决字体、小字、绿色主题及制作语言；旧 READY 后来在仓库正式作废。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/15-unified-showcase/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/15-unified-showcase/preview/index.html` | OPEN |
| 16 | `16-visual-rebuild-gate1` | Visual rebuild · Gate 1 | REJECTED | 用户明确一眼无兴趣；默认组件库风格、空画布、机器术语及机制表达失败。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/16-visual-rebuild-gate1/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/16-visual-rebuild-gate1/preview/index.html` | OPEN |
| 17 | `17-figma-system-architecture` | Figma · System Architecture 12:74 | REJECTED | 用户明确否决；原生可编辑及制作方 PASS 不代表视觉通过。未在 Git 分支发现声明中的新截图与审计文件。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/17-figma-system-architecture/screenshots/p223-01-X947.jpg) | — | OPEN |
| 18 | `18-system-direction-1` | System Architecture 三方向 · Editorial / 学术排版 | DIAGNOSTIC_ONLY | 作为后续四方向的视觉研究输入；聊天审查偏向空间图谱，但用户尚未接受，流体色块含义受到质疑。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/18-system-direction-1/screenshots/p172-01-X741.png) | — | OPEN |
| 19 | `19-system-direction-2` | System Architecture 三方向 · 严谨暗色工具 | DIAGNOSTIC_ONLY | 作为后续四方向的视觉研究输入；聊天审查偏向空间图谱，但用户尚未接受，流体色块含义受到质疑。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/19-system-direction-2/screenshots/p172-02-X742.png) | — | OPEN |
| 20 | `20-system-direction-3` | System Architecture 三方向 · 空间系统图谱 | DIAGNOSTIC_ONLY | 作为后续四方向的视觉研究输入；聊天审查偏向空间图谱，但用户尚未接受，流体色块含义受到质疑。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/20-system-direction-3/screenshots/p172-03-X743.png) | — | OPEN |
| 21 | `21-visual-direction-1` | 后续四张视觉方向 · 1 | REJECTED | 用户远远不满意，反对 AI 味和刻意 SVG；后续认为把产品做成架构海报。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/21-visual-direction-1/screenshots/p186-01-X796.png) | — | OPEN |
| 22 | `22-visual-direction-2` | 后续四张视觉方向 · 2 | REJECTED | 用户远远不满意，反对 AI 味和刻意 SVG；后续认为把产品做成架构海报。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/22-visual-direction-2/screenshots/p186-02-X797.png) | — | OPEN |
| 23 | `23-visual-direction-3` | 后续四张视觉方向 · 3（独立原图未恢复） | REJECTED | 用户远远不满意，反对 AI 味和刻意 SVG；后续认为把产品做成架构海报。 | 无 | — | OPEN |
| 24 | `24-visual-direction-4` | 后续四张视觉方向 · 4 | REJECTED | 用户远远不满意，反对 AI 味和刻意 SVG；后续认为把产品做成架构海报。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/24-visual-direction-4/screenshots/p186-04-X799.png) | — | OPEN |
| 25 | `25-workbench-r1-1` | Research Systems Workbench R1 · 空间镜头工作台 | DIAGNOSTIC_ONLY | 用户否决整屏过载及内部术语；实现台局部获正面反馈，并要求多 binding、可切换和行号可选。该轮随后被正式降为诊断用途。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/25-workbench-r1-1/screenshots/p196-01-X841.png) | — | OPEN |
| 26 | `26-workbench-r1-2` | Research Systems Workbench R1 · 聚焦优先研究 IDE | DIAGNOSTIC_ONLY | 用户否决整屏过载及内部术语；实现台局部获正面反馈，并要求多 binding、可切换和行号可选。该轮随后被正式降为诊断用途。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/26-workbench-r1-2/screenshots/p196-02-X842.png) | — | OPEN |
| 27 | `27-workbench-r1-3` | Research Systems Workbench R1 · 多尺度系统画布 | DIAGNOSTIC_ONLY | 用户否决整屏过载及内部术语；实现台局部获正面反馈，并要求多 binding、可切换和行号可选。该轮随后被正式降为诊断用途。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/27-workbench-r1-3/screenshots/p196-03-X843.png) | — | OPEN |
| 28 | `28-workbench-r1-4` | Research Systems Workbench R1 · 证据中心架构 | DIAGNOSTIC_ONLY | 用户否决整屏过载及内部术语；实现台局部获正面反馈，并要求多 binding、可切换和行号可选。该轮随后被正式降为诊断用途。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/28-workbench-r1-4/screenshots/p196-04-X844.png) | — | OPEN |
| 29 | `29-workbench-r1b-1` | Workbench Round 1B · 可见结果 1 / 系统与对象同屏 | REJECTED | 用户指出又回到模板；实际只见三幅，不能冒充 prompt 要求的六个连续状态；还出现问题式标题和编造实现细节。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/29-workbench-r1b-1/screenshots/p207-01-X886.png) | — | OPEN |
| 30 | `30-workbench-r1b-2` | Workbench Round 1B · 可见结果 2 / 咨询式架构页 | REJECTED | 用户指出又回到模板；实际只见三幅，不能冒充 prompt 要求的六个连续状态；还出现问题式标题和编造实现细节。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/30-workbench-r1b-2/screenshots/p207-02-X887.png) | — | OPEN |
| 31 | `31-workbench-r1b-3` | Workbench Round 1B · 可见结果 3 / Research IDE 实现台 | REJECTED | 用户指出又回到模板；实际只见三幅，不能冒充 prompt 要求的六个连续状态；还出现问题式标题和编造实现细节。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/31-workbench-r1b-3/screenshots/p207-03-X888.png) | — | OPEN |
| 32 | `32-unsolicited-ide-1` | 未授权生成的暗色 IDE 图 · 1 | REJECTED | 用户否决擅自扔图；当时助手声明两图无效。本档案按本次“全部实际产物”要求保留，不恢复其候选权威。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/32-unsolicited-ide-1/screenshots/p222-01-X942.png) | — | OPEN |
| 33 | `33-unsolicited-ide-2` | 未授权生成的暗色 IDE 图 · 2 | REJECTED | 用户否决擅自扔图；当时助手声明两图无效。本档案按本次“全部实际产物”要求保留，不恢复其候选权威。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/33-unsolicited-ide-2/screenshots/p222-02-X943.png) | — | OPEN |
| 34 | `34-cartography-first` | Research Cartography · 第一版 | REJECTED | 制作方自审指出过空、关系线混乱、C04 无故突出，随即重做；最终用户也否决该路线。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/34-cartography-first/screenshots/p227-01-X964.jpg) | — | OPEN |
| 35 | `35-cartography-system-focus` | Research Cartography · 第二版与 C04 聚焦 | REJECTED | 用户否决学术海报式拓扑与硬塞说明区；空间、对象身份、状态、实现和证据等产品价值丢失。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/35-cartography-system-focus/screenshots/p227-02-X965.jpg) | — | OPEN |
| 36 | `36-gpt6pro-total-redesign` | GPT-6 Pro · Total redesign | CURRENT_BEST | 按本次用户指令保存当前最佳完整候选；不是用户最终接受。原 review 亦明确不代表用户接受、完整产品验收或新科研运行结果。 | [截图](https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/versions/36-gpt6pro-total-redesign/screenshots/archive-render-desktop.png) | `docs/design/version-gallery/versions/36-gpt6pro-total-redesign/preview/candidate.html` | OPEN |

## 6. 全量历史审阅队列：Atlas 12 项

| 版本 | 名称 | 历史状态 | 历史判断 | 静态入口 | 用户裁决 |
|---|---|---|---|---|---|
| V01 | MVP GPT-5.6 | REJECTED | 内容部分保留；主图视觉否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v01-mvp-gpt56/pdf/p088-01.png) | OPEN |
| V02 | MVP GPT-6 | REJECTED | 事实、Bases 与笔记保留；任务卡片矩阵否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v02-mvp-gpt6/source-files/research/dii-atlas-mvp/gpt6/screenshots/canvas-overview.png) | OPEN |
| V03 | Visual Redesign SOL | REJECTED | 语义探索有价值；视觉方案否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v03-visual-redesign-sol/canvas-renders/DII_FIELD_OVERVIEW.png) | OPEN |
| V04 | Visual v1 GPT-5.6 | REJECTED | 局部关系语义可参考；视觉母版资格否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v04-visual-v1-gpt56/source-files/research/dii-atlas-visual-v1/gpt56/01-domain-overview.png) | OPEN |
| V05 | Visual v1 GPT-6 | VISUAL_BASELINE | 后续正式指定的唯一视觉母版；实机缺陷仍需修复。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v05-visual-v1-gpt6/source-files/research/dii-atlas-visual-v1/gpt6/01-domain-overview.png) | OPEN |
| V12 | 一次性领域总览概念稿 | REJECTED | 展示后立即作废；不能把 20 篇当整个领域。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v12-one-shot-concept/pdf/p149-01.png) | OPEN |
| V06 | Native Graph 初版 | ENGINEERING_RETAINED | 原生工程底座保留；初始 Level 0 视觉否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v06-native-graph-initial/pdf/p165-01.png) | OPEN |
| V07 | Native Level 0 Landscape | ENGINEERING_RETAINED | 信息架构改善；可借 UI 框架，主地图视觉不作母版。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v07-native-level0-landscape/pdf/p180-01.png) | OPEN |
| V08 | Astra Ultra / Visual System v2 | REJECTED | 信息架构与实现约束可参考；视觉方案否决。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v08-astra-visual-system-v2/source-files/design/visual-v2-prototype/evidence/01-landscape-light.png) | OPEN |
| V09 | Figma v3 / taxonomy-first S01 | REJECTED | 用户明确判定方向错了；停止打磨该 S01。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v09-figma-taxonomy-s01/pdf/p208-01.jpg) | OPEN |
| V10 | Final Visual Refinement Pro | CURRENT_DESIGN_CANDIDATE | 最新设计候选，等待用户判断；尚不等于原生实现。 | [截图](https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/assets/v10-final-visual-refinement/source-files/design/final-visual-refinement/screens/01-field-overview-light.png) | OPEN |
| V11 | Final Visual Real Obsidian Implementation | NO_VISUAL_DELIVERABLE | 实现准备中／尚无可归档的新视觉成品。 | 无 | OPEN |

## 7. 用户审阅时只需要回答什么

对一个版本或局部，不需要写长评语。只需要给以下之一：
- `KEEP`：明确保留该局部/行为/视觉语言；
- `REPAIR`：方向有价值，但必须修；
- `REJECT`：不要再复活；
- `UNSURE`：暂不冻结，留给 Claude Stage 1 对照分析。

必须注明范围，例如“KEEP 实现台，不 KEEP 整屏”“KEEP 空间社区，不 KEEP 大空椭圆”。不得把局部判断扩大成整版判断。

## 8. Phase A 尚需机械补齐的内容

在 Claude Stage 1 前，由 GPT/Codex完成，不消耗 Claude：
1. 为 Blueprint 生成一个类似 Atlas 的静态 contact sheet（若现有图库没有单张总览）；
2. 从 Blueprint / Atlas 原始 PDF 的关键转折页抽出小型静态 page pack，避免 Claude 重读全部 438 页；
3. 把两位 GPT Pro 的最终报告各压成一页“结论 + 分歧 + 来源入口”，原报告仍保留；
4. 核对所有优先审阅截图能在 Mac mini 本地直接读取；
5. 生成 Claude Stage 1 的最终静态输入清单，明确“必读 / 按需 / 不读”。

以上是 Phase A 的机械工作，不包含新的产品设计。
