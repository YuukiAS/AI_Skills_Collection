# Codex：重构 Asteria 双项目 Claude 独立裁决双 PDF

日期：2026-11-05  
性质：证据工程。不是产品设计，不是新的 Deep Research，不是 GPT 结论汇总。

## 0. 先读唯一总控，但不要把总控里的 GPT 结论写进 PDF

开始前读取：

`YuukiAS/AI_Skills_Collection@design/frontend-feedback-continuity-20261104`

`docs/design/frontend-design/ASTERIA_RECOVERY_FRONTEND_VNEXT_MASTER_PLAN_20261104.md`

它只用于确认当前任务位置和禁止事项。

**本次两份 PDF 的目的，是让网页 Claude 独立下结论。不得把总控中的根因判断、GPT Pro 后验结论、Claude 接手方案、推荐路线等写成证据包结论。**

当前已有两份 PDF 已推到：

`YuukiAS/Asteria-Blueprint@archive/asteria-blueprint-version-gallery-20261103`

`docs/design/claude-independent-review/`

- `ASTERIA_CORE_EVIDENCE_20261105.pdf`：当前约 32 页，必读；
- `ASTERIA_SUPPLEMENTARY_READING_20261105.pdf`：当前约 311 页，补充阅读。

从当前版本继续修，不从头另造第三套文件。

## 1. Claude 这一轮到底干什么

Claude 这轮**不设计新 UI**。它只独立回答：

1. Blueprint 与 Atlas 过去到底做过哪些 Deep Research；
2. 原始研究 prompt 要求查什么，研究结果实际找到了什么；
3. 过去是否已经找到成熟 GitHub / 产品 / 工具 /交互模式可复用；
4. 后续版本到底有没有真正消费这些研究结果；
5. Atlas 的科学研究、展示研究、Obsidian 工程分别已经做到什么；
6. Anthropic 官方 frontend-design 等能力实际存在什么、能做什么；
7. 两个项目反复失败的原因到底是什么；
8. Claude 是否认为自己有现实机会把两个项目明显做好；
9. 下一步应直接设计、补一个窄研究，还是先验证现成轮子。

Claude必须自己下结论。PDF 只提供可核查事实。

## 2. 两份 PDF 的角色必须彻底分开

### A. CORE：必读

保留文件名：

`ASTERIA_CORE_EVIDENCE_20261105.pdf`

目标：**Claude 完整读这一份，就能理解问题、知道现有证据分布，并能决定补充包里该查哪几处。**

建议约 25–40 页，但不要为了页数硬裁内容。

CORE 不是总结报告，不替 Claude回答问题。

CORE 只允许包含：

1. **中立任务说明**  
   说明 Claude 要独立判断什么，明确“不要开始设计”。

2. **两个产品的事实性任务定义**  
   优先使用用户原话、原始任务、当前真实产品范围。  
   不用 GPT 后验总结替代。

3. **研究谱系导航**  
   对每个重要研究族只回答机械事实：
   - 原始 prompt 在哪里；
   - 哪些结果分支/文件对应它；
   - 研究实际检查过哪些公开项目/工具/产品；
   - 后续哪些历史版本声称使用/借鉴过它；
   - 对应 Supplement 精确页码。

   这里可以写“研究结果中出现 LikeC4 / Structurizr / Dagster / DataHub”等事实，不能写“所以 Blueprint 已经证明不需要研究”。

4. **最关键原始证据摘录**  
   每个项目只选真正决定 Claude 是否需要继续回源的少量内容：
   - 用户关键原话；
   - Deep Research prompt 的关键任务要求；
   - Deep Research result 中对现成轮子/成熟参考的实际调查记录；
   - 关键正反版本图；
   - 真实宿主/工程底座存在性的直接证据。

5. **最新 Phase B 用户反馈**  
   必须补齐当前遗漏。  
   CORE 只放真正会影响后续产品方向的用户原话与对应图/版本，不放 Codex 的抽象总结替代原话。  
   每条写清对应 Supplement 页码，可回到完整轮次。

6. **官方 frontend-design / Claude 能力的直接证据**  
   优先放 Anthropic 官方 Skill/插件原文的必要片段、来源 URL/commit。  
   不放 GPT 对“这个 Skill 一定好/一定不够”的二手结论。

7. **核心→补充阅读索引**  
   这是本次最重要的结构。

### B. SUPPLEMENT：完整 sourcebook

保留文件名：

`ASTERIA_SUPPLEMENTARY_READING_20261105.pdf`

它不是第二份“长报告”，而是**按来源组织的完整证据库**。

允许很长。不要要求 Claude 从第 1 页读到最后一页。

必须通过目录、书签、来源分隔页和 CORE 的精确索引实现按需阅读。

## 3. CORE 必须给 Supplement 做精确导航

Claude不应该拿到 300+ 页后自己搜索。

CORE 中每个重要证据项至少要有：

- `SOURCE_ID`
- 来源名称
- repo / branch / path 或原始 PDF 身份
- 这份来源是什么：PROMPT / RESULT / USER_CONVERSATION / USER_FEEDBACK / HISTORICAL_ARTIFACT / OFFICIAL_REFERENCE
- **Supplement 页码范围，例如：`SUPP p.083–101`**
- 如果只需要 Claude看其中一段，额外写“优先看 `SUPP p.091–094`”
- 必要时给原始项目 PDF 页码，例如“Blueprint 原对话 p.195–205”

CORE 最前面必须有一个“问题 → 去哪里看”的导航页，例如：

- 想判断 Blueprint 是否已调查成熟轮子 → CORE §X；SUPP p.xxx–yyy
- 想核对 LikeC4 当时到底研究了什么 → SUPP p.xxx–yyy
- 想看 Blueprint 用户为什么否决 Workbench → SUPP p.xxx–yyy；原对话 p.195–205
- 想看 Atlas 的 DII Deep Research → SUPP p.xxx–yyy
- 想看 Atlas 原生 Obsidian 工程是否已经存在 → SUPP p.xxx–yyy
- 想看最新 Phase B 用户逐轮反馈 → SUPP p.xxx–yyy
- 想核对官方 frontend-design Skill → SUPP p.xxx–yyy

最好制作 PDF 内部可点击链接/书签；做不到时，精确页码是硬要求。

**CORE 的价值不是替 Claude总结，而是让 Claude无需在 Supplement 里盲找。**

## 4. 明确删除：不要把这些 GPT 后验结论塞给 Claude

从 CORE 与 SUPPLEMENT 都删除或不再收入以下“后来的二手裁决/接手方案”，除非某个文件本身就是待审对象且用户另有要求：

- `FAILURE_ROOT_CAUSE_ZH.md`
- `EXECUTIVE_DECISION_ZH.md`
- `LOW_COST_PRODUCTION_PLAN_ZH.md`
- GPT 对 Claude 应如何接手的最终路线结论
- GPT 对“Blueprint 已证明有什么 / Atlas 缺什么”的后验总结
- 当前 ChatGPT 对失败根因的任何新总结
- 总控文档中的 GPT 冻结判断

尤其不要设置 `SECONDARY_GPT_ANALYSIS` 大章节让 Claude先读别人答案。

### 例外

**历史 Deep Research 的结果本身必须保留。**

例如：
- Complex System Showcase 的独立研究结果；
- Architecture Evolution 的 Pro-A / Pro-B 研究结果；
- Asteria Next convergence 的研究结果；
- Atlas DII Deep Research baseline；
- Atlas MVP/visual research 的正式结果。

这些不是“这次 GPT 替 Claude下的结论”，而是 Claude需要核查的**历史研究产物**。

## 5. Blueprint Supplement 必须完整覆盖什么

按“Prompt → Result A/B → 来源登记 → 后续产品证据”组织，不要按仓库路径乱堆。

至少包括：

### Complex System Showcase

- 原始共同 prompt；
- GPT-5.6 独立结果；
- GPT-6 独立结果；
- SOURCE_REGISTER / 外部参考登记；
- 第二轮 prompt、两份独立结果、最终比较/收敛材料；
- 代表性原型/截图，只放有判断价值的图。

### Architecture Evolution

- 原始 prompt；
- Pro-A / Pro-B 正式结果；
- `OPEN_SOURCE_RESEARCH.md`；
- `RESEARCH_PROVENANCE.md` / 来源登记；
- 特别保留实际调查 LikeC4、Structurizr、Graphviz、Cytoscape.js、ELK、Tree-sitter、SCIP 等的原始内容。

### Asteria Next

- 原始 prompt；
- Pro-A / Pro-B 结果；
- 与稳定对象、来源、状态、消费者、修订历史有关的原始研究材料。

### 后续必要历史

只放能让 Claude判断“研究有没有真正进入产品”的材料：
- Blueprint 36 版 VERSION_CATALOG / contact sheet；
- 少量关键版本截图；
- Workbench、Figma、Total Redesign 等关键断点；
- 不塞完整源码、build log、CI log。

## 6. Atlas Supplement 必须完整覆盖什么

### DII 科学 Deep Research

必须覆盖：
- 原始 Deep Research prompt / brief（若仓库确实没有，明确 NOT_FOUND，不补造）；
- `sources/dii/DEEP_RESEARCH_BASELINE_ZH.md`；
- `prompts/DII_ATLAS_MVP_PRO_ZH.md`；
- DII literature-map 分支中真正相关的 FIELD_MAP、knowledge construction、paper discovery、relation/gap、schema、acceptance criteria。

### Atlas MVP / Visual research

覆盖：
- MVP GPT-5.6 / GPT-6；
- Work 收敛；
- visual redesign；
- visual v1 GPT-5.6 / GPT-6；
- 后续原生 Graph / Level 0 / Astra / final refinement 中真正影响方向的 prompt/result/截图。

### 原生 Obsidian 工程

用最少但足够的材料证明已有能力：
- README / architecture / package manifest / 功能清单；
- 搜索、筛选、Inspector、多层级图；
- 真实 Obsidian 代表截图。

不要把整个 TypeScript 源码打印进 PDF。

### Atlas 公开轮子调查

机械审计仓库里有没有完整“Obsidian / GitHub 公开插件与成熟产品复用研究”。

搜索至少包括：
Obsidian、Canvas、Bases、Dataview、Breadcrumbs、Juggl、Graph Analysis、Excalibrain、Minimal、Border、Homepage、Kanban、knowledge graph、literature map。

找到正式 prompt + result 就收入。

没找到就只在 inventory 里写：
`DEDICATED_ATLAS_PUBLIC_REUSE_RESEARCH = NOT_FOUND`

这只是存在性事实，不替 Claude得出“应该补研究”。

## 7. 两份原始项目对话怎么处理

两份原始对话必须进入 Supplement，作为最高优先级回源材料：

- Blueprint 原始约 230 页；
- Atlas 原始约 208 页。

优先直接合并原 PDF 页面，保留视觉内容。

Supplement 必须明确记录：
- 原文件名；
- 原页数；
- SHA-256；
- Supplement 中从哪一页开始；
- 原 PDF p.1 对应 Supplement p.X；
- 是否 FULL。

不能只放摘录后声称“原始对话已包含”。

CORE 不放完整对话，只放关键原话 + 原 PDF 页码 + Supplement 精确页码。

## 8. Phase B 最新用户反馈必须完整补进 Supplement

当前提交已经明确承认逐轮反馈未完整收入，这必须修。

从：

`/Users/yuukias/Code/Asteria-Phase-A-Evidence/PHASE_B_REVIEW_LEDGER.md`

以及必要的 review-round 图像中导出完整审阅轨迹。

每轮至少保留：
- 实际给用户看的图；
- 用户原话；
- 对应历史版本；
- 原始 PDF 来源页；
- 必要上下文。

**不要只导出 Codex 的 interpreted decision。**

Codex 自己的 candidate judgment 如果保留，必须和用户原话明显分开，不能冒充用户决定。

CORE 只从这里抽取真正影响未来产品的少量用户原话，并指向 Supplement 完整页码。

## 9. 官方 frontend-design Skill

不要用之前 GPT 的 `CLAUDE_TOOL_AND_SKILL_DECISION_ZH.md` 代替官方资料。

尽量直接收入：
- Anthropic 官方 `frontend-design` Skill / plugin 的当前原文或必要完整片段；
- 官方仓库 URL；
- 读取时的 commit/ref。

如果无法取得完整官方原文，保留官方 URL 和可验证摘要，但明确材料不完整。

Claude自己判断这个 Skill 是否有用。

## 10. Supplement 的排序

建议顺序：

1. Source map / 全目录；
2. Blueprint research：
   - prompt
   - result A/B
   - source register
   - later evidence
3. Atlas research：
   - prompt/baseline
   - MVP/visual results
   - native engineering evidence
4. Official frontend-design reference；
5. Blueprint / Atlas version catalog + contact sheets +关键截图；
6. Phase B 完整逐轮用户反馈；
7. Blueprint 完整原始对话；
8. Atlas 完整原始对话；
9. 最终 source manifest。

不要放“GPT告诉 Claude应该怎么判断”的章节。

## 11. 页码索引必须在最终构建后反向写回 CORE

这是硬要求。

必须先完成 Supplement，取得最终稳定页码；再生成 CORE。

CORE 中所有 `SUPP p.xxx` 必须对应最终 Supplement 真页码，不得先写占位符后忘记更新。

如果 Supplement 后续改变导致页码变化，CORE 必须同步重建。

## 12. 去重原则

Supplement 允许长，但不要浪费 Claude 上下文：

- 同一个 prompt 被两个 RUN_ID 共用：正文只打印一次，列出两个结果分支；
- 通用 README 不重复；
- 相同来源登记不要重复打印；
- build log / CI log / package-lock /长源码不收入；
- 同一图片重复出现在多个历史目录时只收入最有上下文的一次；
- 但**用户原始对话、Deep Research prompt/result、Phase B 用户原话不得为了省页而丢失关键内容。**

## 13. OCR

先检查文本层。

只有真正不可搜索的扫描/图片页才 OCR。

OCR 只做辅助索引，必须保留原始页面。

不得整本 OCR 后用 OCR 版替代原 PDF。

## 14. 最终文件与 GitHub

继续更新这两个文件，不创建第三套：

`docs/design/claude-independent-review/ASTERIA_CORE_EVIDENCE_20261105.pdf`

`docs/design/claude-independent-review/ASTERIA_SUPPLEMENTARY_READING_20261105.pdf`

目标分支：

`archive/asteria-blueprint-version-gallery-20261103`

同时在同目录增加/更新：

- `SOURCE_INVENTORY.md`
- `BUILD_REPORT.md`

可以记录构建脚本/临时文件在本地，但不要把大量中间产物塞进仓库。

## 15. QA

至少验证：

- CORE 页数与文件大小；
- Supplement 页数与文件大小；
- 两份 PDF 均可搜索、未加密；
- CORE 每个 Supplement 页码引用都有效；
- 两份原始对话完整映射，无缺页；
- Phase B 用户反馈不是 excerpt，而是完整导出；
- Deep Research prompt/result 成对可定位；
- 官方 frontend-design 来源可定位；
- 中文、URL、代码路径、图像无明显裁切；
- bookmarks / TOC 可用；
- 随机抽查至少 20 个 CORE→Supplement 跳转点；
- qpdf/pdfinfo 或等价 QA 通过。

## 16. 完成后只向用户报告

自然中文，简短说明：

- CORE 页数 / 大小；
- SUPPLEMENT 页数 / 大小；
- Blueprint Deep Research prompt/result 覆盖情况；
- Atlas Deep Research prompt/result 覆盖情况；
- Phase B 用户反馈是否完整；
- 两份原始对话是否 FULL；
- CORE→Supplement 索引是否 PASS；
- frontend-design 官方资料是否收入；
- OCR 是否使用；
- QA 是否 PASS；
- commit。

最后明确：

**这两份 PDF 没有替 Claude下结论；CORE 负责告诉 Claude“该看什么、去 Supplement 哪一页看”，Supplement 负责保存完整证据。**
