# Codex：生成 Asteria 双项目 Claude 独立裁决证据包

日期：2026-11-05  
性质：证据打包，不做产品设计，不做新的研究结论，不替 Claude 裁决。

## 0. 先读唯一总控

开始前必须读取：

`YuukiAS/AI_Skills_Collection@design/frontend-feedback-continuity-20261104`

`docs/design/frontend-design/ASTERIA_RECOVERY_FRONTEND_VNEXT_MASTER_PLAN_20261104.md`

本任务是 Phase C 之前新增的独立裁决 Gate：用户不接受 GPT 对“已有 Deep Research、公开 GitHub 轮子、Frontend Design Skill、失败根因”的单方面判断，要求把原始证据打包后交给网页 Claude 独立判断。

你不是裁决者。不得用 GPT/本任务作者的总结替代原始材料，不得删掉与既有结论冲突的证据。

## 1. 唯一目标

生成一份可以直接上传网页 Claude 的、单文件、自包含、可搜索的 PDF：

`/Users/yuukias/Code/Asteria-Phase-A-Evidence/claude-independent-review/ASTERIA_CLAUDE_INDEPENDENT_REVIEW_PACKET_20261105.pdf`

同时在同目录生成仅供本地核验的：

- `MANIFEST.md`
- `SOURCE_INVENTORY.csv`
- `BUILD_REPORT.md`

用户上传给 Claude 时只需要主 PDF。

这份 PDF 要让一个没有参加历史对话的 Claude 能独立回答：

1. Asteria Blueprint 和 Asteria Atlas 当时真正要做什么？
2. 两个项目分别做过哪些 Deep Research？原始 prompt 到底要求研究什么？
3. 这些 Deep Research 实际找到过哪些成熟产品、GitHub 仓库、工具、交互模式或视觉参考？
4. 是否存在“外面根本没有轮子，所以只能从零设计”的证据？还是研究找到了轮子但后续没有真正消费？
5. Atlas 是否缺少一轮专门针对 Obsidian / GitHub 公开插件与成熟产品设计的系统研究？
6. Anthropic / Claude 的 frontend-design 等 Skill 到底能解决什么、不能解决什么？
7. 为什么经过多轮 GPT Pro / Work / Codex / Figma / 原型仍持续产出用户不满意的 dashboard、卡片、流程页、普通图 demo、IDE 模板等结果？
8. 如果由 Claude 接手，Claude 是否有合理机会明显做得更好？前提是什么？哪些部分应该复用，哪些部分必须重新设计？
9. 下一步是否需要补研究；如果需要，只缺什么窄范围研究？不得泛化成“再做一轮大研究”。

## 2. 证据原则

### 2.1 原件优先

证据优先级：

1. 用户原始对话 PDF 与其中的视觉页；
2. Deep Research 原始 prompt；
3. Deep Research 原始结果/裁决/来源登记；
4. 对应历史版本、contact sheet、真实宿主截图与可运行工程说明；
5. 后来的 GPT/Codex 总结与交接文档。

后来的总结不能覆盖前面的原始证据。

### 2.2 不允许为“方便 Claude”改写原文

GitHub Markdown 可以排版成 PDF，但正文必须保持原文，不得摘要替换。

允许增加：
- 来源分隔页；
- 页眉/页脚；
- 原始路径、branch/ref、commit SHA、文件哈希；
- PDF 总页码；
- 目录和交叉索引；
- 明确的证据类型标签。

不得增加：
- “正确结论”；
- “Claude 应该同意什么”；
- 新的产品推荐；
- 对研究质量的主观评分。

### 2.3 OCR 只作搜索辅助

先检查两份原始 PDF 是否已有可用文本层。

- 如果 `pdftotext` / PDF text extraction 足够，禁止整本 OCR。
- 只有扫描页、图片页或乱码页确实无法搜索时，才对必要页做 OCR。
- OCR 文本必须标记为 `OCR_DERIVED`，不能替换原始页面图像。
- 两份原始 PDF 必须原样保留视觉页面并作为 PDF 附录合并，不能只放 OCR 文本。

## 3. 第一层：前置导航，不是结论

主 PDF 最前面制作一个简短的导航部分，建议 8–15 页，内容仅包括：

1. 本包目的：让 Claude 独立判断，不信任任何单一 GPT 总结；
2. 两个项目的一句话事实定义；
3. 完整来源目录；
4. “Deep Research prompt → result → 后续设计版本”的来源映射；
5. 外部公开项目/工具引用登记：只记录“哪份研究提到了什么 URL/项目、当时说它可复用什么”，不替 Claude判断是否真的适合；
6. 当前历史版本索引：Blueprint 36 条、Atlas 12 条；
7. 如何读取：建议 Claude 先看原始 prompt 与原始对话，再看后续 GPT 总结，避免锚定。

不要在导航中写“Blueprint 已经证明有轮子”“Atlas 缺研究”等当前 GPT 结论。只给证据位置。

## 4. 必须收入的原始对话

必须定位并验证两份完整原始对话 PDF：

### Blueprint

`ChatGPT_Asteria-BluePrint-裁决_20261103-1638(2).pdf`

已知历史身份供核对，不得在未验证时直接相信：
- 约 230 页
- 约 7,522,157 bytes
- 历史记录 SHA-256：`47ff028b31224a7f02be81f7b4145198a799d9940d67fce04a51f35464a0e4c4`

### Atlas

`ChatGPT_建立文献地图架构_20261103-1749(1).pdf`

已知历史身份供核对，不得在未验证时直接相信：
- 约 208 页
- 约 5,526,565 bytes
- 历史记录 SHA-256：`25f4271d87d3fe89d428472ea10425ebce1fe8d73e25e8a09a09597b51c3f40a`

优先在 Mac mini 已有 Phase A 证据、历史归档、本地文件或现有工作目录定位。不得从聊天里的临时 `/mnt/data` 路径假定 Mac 上存在。

两份完整 PDF 必须都进入最终主 PDF，保留原始页序和图像。

如果找不到任一原件，任务不得假装完成；在 BUILD_REPORT 中明确 BLOCKER，并仍可先完成其它证据。

## 5. Blueprint：必须系统收集所有相关 Deep Research prompt 与结果

不要只按下面路径机械抓取。先搜索 `YuukiAS/AI_Research_Toolkit`、`YuukiAS/Asteria-Blueprint`、`YuukiAS/AI_Skills_Collection` 中与 Blueprint / complex system showcase / architecture evolution / Asteria Next / design assurance / visual adoption 相关的研究分支和研究文件，建立完整 inventory。

至少覆盖以下已知研究族：

### A. Complex System Showcase

共同任务：
- `YuukiAS/AI_Research_Toolkit@main:docs/research/complex-system-showcase-20261026/00_INDEPENDENT_DESIGN_TASK_ZH.md`

第一轮独立结果分支：
- `research/complex-system-showcase-20261026-gpt6`
- `research/complex-system-showcase-20261026-gpt56`

收集各自完整的：
- `DESIGN_DECISION.md`
- `SOURCE_REGISTER.md` 或等价来源登记
- 最终 research summary / conclusion
- 能证明外部成熟参考实际被调查的文件
- 如结果引用了 prototype 截图，加入少量代表性截图，而不是把整个网站截图几百页

第二轮：
- `docs/research/complex-system-showcase-20261026/01_SECOND_ROUND_QUALITY_EVIDENCE_ZH.md`
- `docs/research/complex-system-showcase-20261026/02_INDEPENDENT_REDESIGN_R2_ZH.md`
- 分支 `research/complex-system-showcase-20261026-r2-gpt6`
- 分支 `research/complex-system-showcase-20261026-r2-gpt56`
- 比较分支 `research/complex-system-showcase-20261026-r2-comparison`
- 必要的最终比较/裁决文件

### B. Architecture Evolution

分支：
- `research/architecture-evolution-system-20261027-pro-a`
- `research/architecture-evolution-system-20261027-pro-b`

自动定位并收入：
- 对应任务 prompt；
- 两个 Pro 的正式研究结论；
- 来源/案例登记；
- 明确列出的成熟工具、系统、产品或 GitHub 参考。

### C. Asteria Next convergence

分支：
- `research/asteria-next-convergence-20261027-pro-a`
- `research/asteria-next-convergence-20261027-pro-b`

自动定位并收入：
- 原始任务 prompt；
- 两个 Pro 的正式结论；
- 与对象稳定、状态、消费者链、来源追踪、修订历史和展示方式有关的研究结果。

### D. Blueprint blind sufficiency / 后续设计研究

至少核对：
- `YuukiAS/Asteria-Blueprint@research/blueprint-blind-sufficiency-20261102-pro-a`
- `...pro-b`

如果这些属于设计审查而不是 Deep Research，仍可收入“必要历史”章节，但必须标记 `SECONDARY_DESIGN_REVIEW`，不要冒充 Deep Research。

### E. 视觉采用、Figma、最终重设计的必要历史

只收入能解释“研究结果后来有没有被真正消费”的必要文件，例如：
- visual adoption contract；
- Figma system architecture 的关键决定；
- final total redesign 的决策说明；
- 版本图库中的 `VERSION_CATALOG.md` / manifest / contact sheet。

不要把全部源码塞进 PDF。

## 6. Atlas：必须系统收集科学 Deep Research 与展示/实现研究

### A. DII Deep Research

必须收入：
- `YuukiAS/Asteria-Atlas@main:sources/dii/DEEP_RESEARCH_BASELINE_ZH.md`
- `YuukiAS/Asteria-Atlas@main:prompts/DII_ATLAS_MVP_PRO_ZH.md`

同时进入：
- `YuukiAS/Distributed_Imaging_Inference@research/dii-literature-map-20261027`

自动搜索并收入真正对应本 Atlas 领域地图的：
- Deep Research 原始 prompt / brief；
- Deep Research 最终结果或冻结报告；
- `FIELD_MAP_ZH.md`
- `KNOWLEDGE_CONSTRUCTION_PROTOCOL_ZH.md`
- `KEY_PAPER_DISCOVERY_PROTOCOL_ZH.md`
- `RELATION_AND_GAP_SYNTHESIS_PROTOCOL_ZH.md`
- 必要的 schema / acceptance criteria；
- 如果原始 Deep Research 只有外部聊天结果而仓库只保存了冻结 baseline，明确写 `ORIGINAL_DEEP_RESEARCH_PROMPT_OR_FULL_RESULT = NOT_FOUND_IN_REPO`，不能补造。

### B. Atlas MVP / 视觉研究结果

核对并收入与“研究如何变成产品”直接有关的正式结论：
- `research/dii-atlas-mvp-gpt56`
- `research/dii-atlas-mvp-gpt6`
- `research/dii-atlas-mvp-work`
- `research/dii-atlas-visual-redesign-sol`
- `research/dii-atlas-visual-v1-gpt56`
- `research/dii-atlas-visual-v1-gpt6`

不需要把每个分支所有文件都塞进去。收入：
- 任务 prompt；
- 最终设计/研究结论；
- 外部参考/来源登记；
- 代表性结果图或 contact sheet；
- 用户/真实 Obsidian 验证后的关键失败证据。

### C. 原生工程底座

收入足以让 Claude判断“是不是必须从零造”的材料：
- `prototype/atlas-native-graph-v1` 的 README / architecture / package manifest / 功能说明；
- 搜索、筛选、Inspector、多层级图等现有能力的说明；
- 1–3 张真实 Obsidian 代表截图。

不要把整个 TypeScript 源码打印进 PDF。

### D. Atlas 外部前端/Obsidian 轮子调查是否存在

必须专门审计仓库中是否已有完整研究，搜索关键词至少包括：
- Obsidian
- plugin
- graph
- Canvas
- Bases
- Dataview
- Breadcrumbs
- Juggl
- Graph Analysis
- Excalibrain
- Minimal
- Border
- Homepage
- Kanban
- knowledge graph
- literature map
- research map

如果找到了正式 prompt + result，收入。

如果只找到零散引用、工具调查或实现使用，但没有一轮完整系统研究，必须在 SOURCE_INVENTORY 中明确标记：
`DEDICATED_ATLAS_PUBLIC_REUSE_RESEARCH = NOT_FOUND`

这只是文件存在性事实，不是产品结论。

## 7. Frontend Design / Claude / 工具研究

为了让 Claude判断“到底有没有专业前端 Skill”和“Skill 能解决多少”，收入：

- `YuukiAS/Asteria-Blueprint@research/claude-independent-pdf-gate-gpt56-20261104:docs/research/claude-handoff-20261104/gpt56/CLAUDE_TOOL_AND_SKILL_DECISION_ZH.md`
- 同目录 `EVIDENCE_AND_RESEARCH_MAP_ZH.md` 与 `EXECUTIVE_DECISION_ZH.md`，但统一放在**后置的 SECONDARY_GPT_ANALYSIS**章节，避免先锚定 Claude；
- 如果能在不增加付费和不改全局配置的情况下读取 Anthropic 官方 `frontend-design` Skill 原文，加入一份只读快照并记录官方来源 URL / commit；读不到就只记录 URL，不阻塞主包。

这些是“已有 GPT 研究/官方资料”，不是 Claude必须接受的结论。

## 8. 最近一次用户历史审阅

收入：
- `/Users/yuukias/Code/Asteria-Phase-A-Evidence/PHASE_B_REVIEW_CONCLUSIONS_20261105.md`
- `PHASE_B_REVIEW_LEDGER.md` 不要整本默认打印；只在 conclusions 引用某个用户新判断而无法从两份原始 PDF 找到时，抽取对应 round 的原话和图片。

这部分必须标记：
`RECENT_USER_REVIEW / DERIVED_FROM_2026-11-04_TO_05_REVIEW`

用户原话与 Codex解释必须区分。

## 9. 外部公开参考登记

从所有 Deep Research / tool research 中抽取实际出现过的外部项目、官方产品和 GitHub repo，做一份机械登记，不下结论。

至少记录：
- 名称；
- URL；
- 出现在哪份 prompt/result；
- 当时研究声称可借鉴什么；
- 是否有证据后续 Asteria 实际采用；
- 如果没有证据，写 `ADOPTION_NOT_VERIFIED`。

重点检查但不限于：
LikeC4、IcePanel、Dagster、DataHub、Structurizr、React Flow / xyflow、D3、ELK，以及 Atlas/Obsidian 相关候选。

不要在打包阶段重新上网替 Claude做新研究；本任务只整理“历史研究到底找过什么”。网页 Claude 后续若有联网能力，再让它独立核查当前状态。

## 10. PDF 编排顺序

为降低锚定，严格按以下顺序：

1. 封面与中立问题清单；
2. 来源目录 / source map；
3. Blueprint Deep Research 原始 prompt；
4. Blueprint Deep Research 原始结果与来源登记；
5. Atlas Deep Research 原始 prompt / baseline /结果；
6. Atlas MVP/视觉研究结果与现有原生工程说明；
7. 外部公开参考机械登记；
8. Blueprint / Atlas 历史 version catalog + contact sheet；
9. 最近一次 Phase B 用户审阅结论；
10. 后来的 GPT/Codex 二次总结、Claude tool/skill research；
11. **附录 A：Blueprint 原始 230 页对话 PDF（完整、原顺序）**；
12. **附录 B：Atlas 原始 208 页对话 PDF（完整、原顺序）**；
13. 最终 source manifest。

注意：两份原始对话必须完整进入 PDF；同时前部的研究材料让 Claude不必先翻 438 页才能知道有哪些研究。

## 11. 每个来源必须有 separator page

每份材料前加入一页来源说明：

- `SOURCE_ID`
- `EVIDENCE_CLASS`：PRIMARY_CONVERSATION / DEEP_RESEARCH_PROMPT / DEEP_RESEARCH_RESULT / HISTORICAL_ARTIFACT / RECENT_USER_REVIEW / SECONDARY_GPT_ANALYSIS / OFFICIAL_SKILL_REFERENCE
- repo
- branch/ref
- path
- commit SHA 或可验证 ref
- 本地文件则记录绝对路径与 SHA-256
- 原始文件页数/字节数
- 是否全文收入
- 若只节选，为什么节选、完整原件在哪里
- 本资料不代表用户接受或 Claude同意

不得在 separator page 写倾向性总结。

## 12. 构建要求

- 优先使用当前机器已经存在的可靠 PDF/Markdown 工具，不为这个任务大量安装软件。
- Markdown 先转换成清晰可搜索的 PDF 页面，再与原始 PDF 合并。
- 中文字体必须正常，不得出现方框或乱码。
- 长 URL 可以自动换行。
- 代码块和路径不得截断。
- 图片按页面宽度缩放，不允许裁掉关键 UI。
- 原始两份 PDF 不要因为重渲染而明显降低清晰度；优先直接合并原 PDF 页面。
- 给最终 PDF 加连续总页码；原始对话 separator page 必须写明“原 PDF 第 1 页对应总包第几页”。
- 给书签/目录时尽量做到每个 SOURCE_ID 可跳转。

如果最终 PDF 体积过大：
1. 先压缩新增截图和中间图；
2. 不压缩 Markdown 文本为低清图片；
3. 不删除原始对话；
4. 不删除 Deep Research prompt/result；
5. 仍过大时生成同内容的 `WEB_OPTIMIZED` 版本，但主交付仍必须保留 full packet；报告两个文件大小。

## 13. 验证

完成后必须：

1. `pdfinfo` 检查页数、文件大小、是否加密；
2. `qpdf --check` 或等价工具检查结构；
3. 随机抽查至少 20 页文字提取；
4. 渲染并肉眼检查：
   - 封面；
   - 目录；
   - 每个主要研究族至少 1 页；
   - 两份 contact sheet；
   - 两份原始 PDF 各至少 5 页，其中包含高图像密度页；
   - 最后一页；
5. 检查中文、URL、代码路径、表格没有明显裁切；
6. 对原始对话 PDF 验证原页数完整映射，无缺页、无重复页；
7. SOURCE_INVENTORY 中所有 `FOUND` 必须能定位到最终 PDF 页码；
8. 所有 `NOT_FOUND` 必须是真的搜索过，不得因为路径猜错就宣布缺失。

## 14. 禁止

- 不修改 Blueprint / Atlas 产品代码；
- 不设计新 UI；
- 不启动 Claude；
- 不新增 Deep Research；
- 不把 GPT 的现有结论写成 PDF 的“正确答案”；
- 不把缺少某个文件解释成“外面没有轮子”；
- 不把 GitHub 搜索不到默认分支文件解释成其它历史分支不存在；
- 不删除与当前 GPT 结论冲突的材料；
- 不因为篇幅长就把两份原始对话换成摘要。

## 15. 完成后只报告

用自然中文简短报告：

- FINAL_PDF =
- PAGE_COUNT =
- FILE_SIZE =
- BLUEPRINT_ORIGINAL_PDF = PASS/FAIL
- ATLAS_ORIGINAL_PDF = PASS/FAIL
- DEEP_RESEARCH_INVENTORY = <找到多少 prompt / result / secondary review>
- MISSING_SOURCES = <若无写 NONE>
- OCR_USED = <哪些页；没有则 NONE>
- PDF_QA = PASS/FAIL
- MANIFEST =
- BUILD_REPORT =

最后明确一句：这份 PDF 只做证据包，没有替 Claude 下任何结论。
