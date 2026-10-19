# Presentations 0.5：ChatGPT–Codex 双端作者与生产架构 V0.2

日期：2026-10-20  
状态：Planner 中间架构提案，等待独立 Critic 审查  
结论类型：`PROPOSED_FOR_CRITIC`；不是实施授权，不得据此启动 Codex、发布或消耗最终评估样本

## Active Design Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = presentations
design_topic_or_task_key = presentations--dual-surface-authoring-production
source_branch_or_ref = main@79eb00ea41348b8b0f3b806c1dc6510cd0122658
proposal_branch = design/presentations--dual-surface-authoring-production
proposal_path_and_version = docs/design/presentations/PRESENTATIONS_0_5_DUAL_SURFACE_AUTHORING_AND_PRODUCTION_ARCHITECTURE_V0_2_2026-10-20.md
execution_branch_or_worktree = not created
review_stage = intermediate architecture review
planner_verdict = PROPOSED_FOR_CRITIC
ready_for_codex = NO
```

## 0. 本轮相对 V0.1 的实质变化

V0.1 只给出了作者系统、双模板和若干版式原则，仍不足以交给 Critic，更不足以形成执行包。V0.2 做了四项根本补充：

1. 冻结 ChatGPT 与 Codex 两个正常产品入口，不再把“ChatGPT 作者、Codex 排版”写成一句抽象边界；明确 Codex 直接入口也必须具备完整作者阶段，不能要求用户先准备完美规格。
2. 把已经正式发布的 Clear Writing 0.5 变成 Presentations 的必经伴随能力，写清调用时点、输入合同、输出合同、失败语义和双方不可越权的内容。
3. 新增“STAT5060/CAT-TRACE 真实失败 → 根因 → 生产部件 → 正常路径动作 → 证明方式”的详细追踪矩阵。验收器不会替生成器补作者判断；每类已知高亮必须先由 0.5 的作者与生产机制主动处理。
4. 把“Codex 应直接产出可过验收的质量”冻结为发布承诺：GPT Work 与后续通用验收器只负责发现遗漏和独立把关，不能成为每次替低质量候选列出大批 P1、再由 Codex 逐页打补丁的常规生产方式。

## 1. 稳定用户承诺基线

后续修订不得静默弱化以下承诺，除非用户明确改变要求。

### 1.1 两个正式入口

下一版本必须同时提供：

- **ChatGPT 版**：普通 ChatGPT Web / Project 对话中的作者、规划、反馈消化、可见文案与 Codex 交接入口；
- **Codex 版**：普通 Codex 任务中的直接作者与生产入口，既能消费 ChatGPT 已冻结的作者包，也能在用户直接从 Codex 开始时自行完成同一质量标准的作者阶段。

两端不是两个互相漂移的产品。它们共享一套 canonical authoring contract、页面语义、Clear Writing 交接和模板/质量规则；只因运行能力不同而承担不同职责。

### 1.2 Codex 不是低质量排版器

Codex 版必须在正式入口完成：来源读取、受众和目标判断、叙事、页面职责、可见文案、构图、模板实现、图表/公式/代码处理、构建、逐页渲染、整套节奏检查和有界返修。用户不提供 ChatGPT 作者包时，Codex 不能把缺失规格解释为允许临场随便写。

正式候选在进入 GPT Work 或未来通用验收器前，应已经是**正常情况下可被接受的成品**。独立审查发现以下任一情况时，必须判为产品机制失败而不是普通“审稿器帮忙完善”：

- 任一 P0；
- 任何已知、已映射的历史 P1 再次出现；
- 同一根因在多页形成一组 P1；
- 候选仍需要大规模重写故事、页面职责、可见文案、模板或主要构图；
- 审稿器实际承担了第一次完整逐页视觉/教学设计。

### 1.3 验收器与 GPT Work 的角色

本版本不实现通用 Presentation 验收器，也不实现每份演示文稿的额外验收器运行时。后续架构固定为：

```text
Presentations 0.5 作者与生产机制
    -> 直接产出高质量候选
    -> 通用验收器检查通用遗漏/回归
    -> 项目额外验收器检查项目专属要求
    -> GPT Work 做最终审美、读者努力与教学/沟通独立判断
```

验收器和 GPT Work 都不修改候选、不替 Codex补作者决定、不把一个系统性差候选通过“发现 30 个 P1 后逐页修”变成产品能力。

### 1.4 TODO 收口边界

除通用验收器、独立评审运行时、盲审校准、保留集和裁决聚合外，当前 `docs/plugin-todos/presentations.md` 中具有充分真实证据的作者、路由、模板、版式、语言、图表、代码、教学、引用、现有文稿返修和交付问题都进入 0.5。候选状态条目若已有当前真实证据支持，也在本轮正式归因和实现；不因为旧文件曾标 `CANDIDATE_GENERIC` 就继续无限延后。

## 2. 已核实的当前事实与来源锁

### 2.1 中央仓库

- `AI_Skills_Collection main`：`79eb00ea41348b8b0f3b806c1dc6510cd0122658`。
- 当前 Codex Presentations 插件：`plugins/codex/plugins/presentations/.codex-plugin/plugin.json`，版本 `0.4`。
- 当前 ChatGPT 作者合同：`skills/tools/documents-media/presentations/shared/chatgpt-web-authoring-contract.md`。
- 当前统一作者/生产合同：`skills/tools/documents-media/presentations/shared/authoring-production-workflow.md`。
- 当前长程问题清单：`docs/plugin-todos/presentations.md`。
- 当前双模板共享问题：Issue `#98`。

现有 0.4 已有来源保真、CUHK Beamer、渲染/候选身份和 existing-deck 基础，不能以重构为名删除。当前插件的默认提示和描述仍明显偏研究组会，并没有形成 ChatGPT/Codex 双端完整产品。

### 2.2 Clear Writing

- Codex 插件身份：`writing-style` 0.5，显示名 `Clear Writing`。
- 正式能力包括 `writing-fidelity`、`scientific-prose`、`chinese-prose`、`scientific-rewrite`、`response-clarity` 和 `product-ui-copy`。
- `scientific-prose` 明确覆盖 slide text，但不负责布局、故事或引用核验。
- `chinese-prose` 明确覆盖幻灯片文案终审，但不负责事实核查、结构性科研重写或格式实现。
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md` 已冻结核心原则：Presentations 决定受众、页面职责、证据、首次出现、转场和空间约束；Clear Writing 在这些语义稳定后处理面向读者的局部表达；文案返回后 Presentations 仍负责渲染尺度、节奏和整套连贯性。

本轮不修改 Clear Writing 0.5 的生产语义。若 Presentations 集成暴露 Clear Writing 自身缺陷，只记录证据并交回其 owner；不得在 0.5 中复制一套“更适合幻灯片”的通用写作规则。

### 2.3 CUHK 模板

用户提供：

```text
CUHK Template.pdf
sha256 = a62a4bb5ec2296b875ffe9ff8c1d850b88797e27a74aac7d64f576abb91daa7e

CUHK Template.zip
sha256 = 5cbe4a545d8abbab007f5f0aceec405138f8035b9dcb09c617e1e7cf7b525ee9
```

视觉身份包括顶部完整章节导航、白色主体、CUHK 紫色标题与底部细线、右下原生导航/页码、品牌标题页与品牌结束页。源码存在重复覆盖、旧 `sintef` 命名、硬编码比例、Times New Roman/Caladea/Carlito 主机依赖和两套 footline/frametitle 定义。采用决定：

```text
visual identity = SELECTIVELY_PORTED
licensed theme source = SELECTIVELY_PORTED_WITH_PROVENANCE
legacy duplicate implementation = REJECTED
host font resolution = REJECTED
brand assets = RUNTIME_DEPENDENCY_WITH_USAGE_BOUNDARY
```

### 2.4 STAT5060 标准 Beamer 来源

当前读取的 Tutorial 分支：`YuukiAS/STAT5060-TA@tutorial`，提交 `6fc5193653344f0e71c7d9013c22f3a9959405dc`。

关键来源：

- `materials/2026-27/shared/beamer/stat5060-course-standard-beamer-v2.tex`；
- `materials/2026-27/tutorial-01/theme/stat5060-student-deck-v14-beamer.tex`；
- `materials/2026-27/tutorial-01/releases/student-deck/V14/VERSION.json`；
- V14 source/PDF、历史 V01–V14、人工反馈和页面 registry。

V14 manifest 仍标 `CANDIDATE`，且写明 `producer_boundary = not independently audited`。因此 Codex 实施不得把“V14 最新”当作“V14 所有局部实现均获人类接受”。标准模板的来源策略是：

- 从最终被人类接受的 STAT5060 主题和共享 core 中提取稳定行为；
- 用 CUHK 模板作为同角色样式、字号、字体、导航和几何对齐参考；
- 移除课程名称、绝对资源路径、`\tiny` 代码、候选临时修补和项目页码；
- 由同一 shared core 重建，而不是把 STAT5060 文件改名复制。

## 3. 产品形态：一个能力源，两个正式表面

### 3.1 Canonical source ownership

建议 source 结构：

```text
skills/tools/documents-media/presentations/
  shared/
    authoring/
      deck-brief-contract.md
      page-authority-contract.md
      visible-copy-handoff.md
      composition-contract.md
      revision-authority-contract.md
      candidate-manifest.schema.json
    clear-writing/
      handoff-contract.md
      surface-routing.md
    templates/
      beamer/core/
      beamer/skins/cuhk-research/
      beamer/skins/standard-academic/
    references/
      failure-to-component-map.md
      layout-archetypes.md
      teaching-authoring.md
      research-authoring.md
      delivery-contract.md
  research-presentations/
  business-presentations/
```

现有 source paths 可在实施时采用最小迁移；这里冻结的是 ownership，不强制一次性改名全部历史路径。生成层继续由 Marketplace generator 产生，禁止手工双写。

### 3.2 ChatGPT 版

ChatGPT 版建议是 PRIVATE / USER-scope / skills-only personal Plugin wrapper，或平台支持的等价 skills distribution shell。它不增加 MCP、外部服务或付费 API。canonical source 仍在本仓库；wrapper 只打包 ChatGPT 真正可消费的作者子集和必要引用。

ChatGPT 版正常入口：

```text
用户上传/指向来源并提出演示文稿需求
-> Presentations 自动/显式触发
-> 任务分类与来源边界
-> 受众/目标/故事/页面职责
-> Clear Writing 文案实现与保真检查
-> 页面构图语义和模板/格式选择
-> 形成 AUTHORING PACKAGE
-> 若当前环境可生成简单 artifact，可作为预览而非替代正式生产
-> 复杂/正式任务交给 Codex
```

ChatGPT 版负责：

- 读论文、讲义、代码结果、已有 PDF/PPT、用户批注和历史版本；
- 决定受众、目的、时长、输出格式、模板、比例和交付物；
- 决定叙事、章节、页面数量或范围、稳定 PageID、每页职责和主要对象；
- 决定来源/证据边界、首次出现、符号/术语、页面间转场；
- 决定学生/听众页面、speaker notes、教师学习材料和内部规划边界；
- 生成或批准 visible copy，并真实调用 Clear Writing；
- 决定布局关系与页面原型，而不是坐标级实现；
- 消化累计人类反馈、锁和 supersession；
- 检查 Codex render 是否符合语义规格；
- 给用户展示过滤后的真实候选或变更范围；
- 生成可直接执行的 Codex Goal。

ChatGPT 版不负责：

- 在没有正式文件工具时假装完成 `.tex`/PPTX；
- 编译、渲染、运行 R/Python、生成数据结果或修改仓库；
- 决定 TeX 坐标、具体换行、对象尺寸和 renderer fallback；
- 用截图或整页图片冒充可编辑 PPTX；
- 把“给了 Codex prompt”声称为文稿已完成。

ChatGPT 输出的 AUTHORING PACKAGE 至少包含：

```text
DECK_BRIEF
SOURCE_AND_BASELINE_MANIFEST
PAGE_AUTHORITY
VISIBLE_COPY_AUTHORITY
COMPOSITION_AUTHORITY
TEMPLATE_AND_DELIVERY_AUTHORITY
REVISION_AND_LOCK_AUTHORITY        # revision only
CLEAR_WRITING_RECEIPT
CODEX_PRODUCTION_GOAL
```

### 3.3 Codex 版

Codex 版是 Marketplace 中正式的 `presentations` 插件。它支持两种入口，不能只支持“已有完美规格”。

#### A. 消费 ChatGPT 作者包

```text
AUTHORING PACKAGE
-> 验证完整性与冲突
-> 不重新发明内容/故事
-> 实现图、表、公式、代码与模板
-> build/render
-> producer self-review
-> bounded repair
-> independent review handoff
```

缺失的是实现细节时 Codex自行解决；缺失的是受众、证据、页面职责、可见文案或科学结论时，必须返回一个最小语义问题，不能猜。

#### B. Codex 直接作者入口

```text
用户直接在 Codex 中提出演示文稿任务
-> Codex Author phase 读取同一 canonical authoring contracts
-> 完成来源、受众、故事、页面职责、copy 和 composition freeze
-> 调用 Clear Writing companion
-> 内部冻结 AUTHORING PACKAGE
-> Producer phase 实现
-> build/render/self-review/repair
```

Codex direct Author 不是 Producer 临场写字。实现时至少保持逻辑分离：先形成可审查的作者包，再开始广泛生成；作者包冻结后，Producer 不能因排版压力随意删改内容。普通任务可在同一 Goal 自动完成；真正高风险、重大重构或用户历史冲突才回 Planner/Critic。

Codex 版负责：

- 在 direct mode 完成与 ChatGPT 相同的作者判断；
- 调用 `writing-style`/Clear Writing 对可见文案做规定的语言 pass；
- 生成/修改 `.tex`、PPTX/Slides、图表、表格和资源；
- 通过 `render-chinese-math-pdf` 获取编译器、字体和 PDF QA 环境；
- 选择性调用 `scientific-visualization` 和领域插件，禁止自造低配替代；
- 按 frozen composition 选择尺寸、换行、间距、裁切和响应式 fallback；
- 逐页渲染、整套 contact sheet、文本层、字体、代码复制、导航和来源检查；
- 在候选交给外部审查前完成内部全套质量循环；
- 输出真实可打开的 PDF/PPTX、可编辑源、必要资源和 provenance。

Codex 版不得：

- 把固定 schema 填满当作作者质量；
- 用“无溢出”代替版式与教学质量；
- 为了排版删掉困难内容、缩成不可读小字或填入无关 prose；
- 让 Producer 修改 validator、测试或评分标准来通过；
- 以 `READY_FOR_REVIEW` 代替真正看过全套 render；
- 把 GPT Work/validator findings 当作常规设计清单来源。

### 3.4 两端 parity

发布时必须建立 surface parity matrix：

| 能力 | ChatGPT 版 | Codex 版 | canonical owner |
|---|---|---|---|
| 来源读取与受众判断 | 是 | 是 | authoring core |
| 故事/页面职责/首次出现 | 是 | 是 | authoring core |
| Clear Writing 文案 | 是 | 是 | Clear Writing + handoff |
| 构图语义 | 是 | 是 | composition contract |
| 源码/PPTX 实现 | 否 | 是 | Codex adapter |
| 编译/渲染/工具 QA | 否 | 是 | Codex runtime |
| 查看 render 后语义复核 | 是 | 是 | Presentations |
| 最终用户细微偏好 | 用户 | 用户 | user |

两端允许不同 prompt 和 payload 大小，但任何共同作者行为不得维护两份不同规则。ChatGPT wrapper 和 Codex plugin 均必须记录 canonical source commit/file hashes；release 不能只验证文件存在，必须用自然请求证明两端正常调用。

## 4. Presentations 与 Clear Writing 的冻结边界

### 4.1 Presentations 先决定什么

在调用 Clear Writing 前，Presentations 必须提供：

```text
audience
page_job
prerequisite_context
claim_or_teaching_point
evidence_boundary
required_exact_terms
required_numbers/formulas/citations
visible_role
space_budget
spoken_or_reading_function
allowed_structural_freedom
forbidden_semantic_changes
```

Presentations 对以下内容负责且不能转交：

- 是否需要这一页；
- 该页放什么科学/教学对象；
- 页序、首次出现和转场；
- 结论强度、证据和不确定性；
- 图/表/公式/代码还是文字；
- Question 是否值得问、谁能回答、会改变什么决定；
- 学生可见与教师/讲者材料边界；
- 页面可见文字的角色和长度预算。

### 4.2 Clear Writing 负责什么

Clear Writing 接收已经固定的 page brief 后负责：

- 中文去翻译腔、模板腔、内部流程腔和不必要英文；
- 英文科研文字的自然、精确、非防御式表达；
- 句间局部连接、公式附近解释、caption/annotation/Question/Answer 的 wording；
- 术语首次解释的自然表达；
- 保留数字、公式、引用、限定、否定、不确定性和精确机器字符串；
- 返回超过空间预算或语义冲突的明确诊断，不自行删除事实。

Clear Writing 不负责：

- 改故事、换页面职责、删页面；
- 选择图型、比较轴或布局；
- 改公式、模型、统计结论或来源关系；
- 因页面太挤而缩短/删除必要内容；
- 把 project-specific reviewer rule 固化成通用语言规则。

### 4.3 双重调用时点

每个非平凡文稿至少有两个写作时点：

1. **预实现文案 pass**：页面职责、证据和空间预算冻结后，生成/修订 visible copy；
2. **最终 render 语言 pass**：在实际整页尺度读取可见文本，检查机械标题、孤立句、连字符、内部语言、图内标签和相邻页转场。若修文案，必须重新渲染。

第二次 pass 不是让 Clear Writing 自己做 visual review。Presentations 先指出该页/相邻页在实际 render 中的语言问题，再给 Clear Writing bounded wording task；Presentations 对最终 fit 和 deck coherence 负责。

### 4.4 失败与恢复

- Clear Writing 不可用：正式 0.5 任务返回 `BLOCKED_CLEAR_WRITING_UNAVAILABLE`，不得静默用旧 `scientific-prose` 文本或 Producer 自行润色冒充集成成功。
- 返回文案改变受保护语义：拒绝候选，保留原稿并记录 fidelity failure；若属于 Clear Writing 缺陷，交回其 owner。
- 文案正确但放不下：返回 composition 层，按页面 fallback 处理，不让 Clear Writing继续压缩到失真。
- render 后仍显机械：Presentations 提供具体读者问题和空间约束，再做一次 bounded pass；禁止无限重写。

## 5. 作者权威包：少而完整，不再堆互相漂移的 ledger

本版本不把旧 `deck-plan` 无限加字段。建议定义一个可拆分但逻辑上统一的 AUTHORING PACKAGE。简单任务可只生成内存对象和一份紧凑 Markdown；复杂/正式任务落盘为少量文件。

### 5.1 Deck Brief

```yaml
deck_id: ...
mode: research | teaching | business | revision
purpose: ...
audience:
  identity: ...
  prior_knowledge: [...]
  decisions_or_learning_outcomes: [...]
duration_minutes: ...
language: en | zh | mixed
format: beamer | pptx | google-slides | plan-only
template_route: cuhk-research | standard-academic | business-editable | user-locked | preserve-existing
aspect_ratio: 16:9 | 4:3 | preserve
main_thesis: ...
source_boundary: ...
delivery_artifacts: [...]
```

### 5.2 Page Authority

每页记录：

```yaml
page_id: stable semantic identity
section: ...
page_job: ...
audience_before: ...
audience_after: ...
primary_object: ...
claim_or_teaching_point: ...
source_anchors: [...]
prerequisites: [...]
first_use_items: [...]
required_visible_content: [...]
forbidden_visible_content: [...]
notes_or_instructor_content: [...]
incoming_need: ...
outgoing_need: ...
```

### 5.3 Visible Copy Authority

保存最终允许出现的 title、body、Question、Answer、labels、table cells、figure annotations、caption/source 和 code text。对 exact-copy 任务逐字符串锁定；普通新建任务允许在规定阶段由 Clear Writing 修订，但 Authoring Package freeze 后不得由 Producer改写。

### 5.4 Composition Authority

```yaml
semantic_relation: focal | sequential | causal | peer-compare | evidence-interpretation | question-answer | overview-reassembly
archetype: ...
reading_order: [...]
primary_scale_priority: ...
semantic_groups: [...]
allowed_fallbacks: [...]
forbidden_fallbacks: [...]
role_tokens: [...]
```

不在这里写任意坐标。Producer可在共享 token 和 archetype内做排版，但不能更换语义关系。

### 5.5 Revision Authority

revision/recovery 任务额外保存：准确 reviewer-seen baseline、稳定 PageID 祖先、active human guards、supersession、semantic/copy/visual locks、当前允许修改范围和依赖消费者。人类明确拒绝高于旧自动 PASS。

### 5.6 Candidate Manifest

只记录候选事实，不含模型裁决：source/template/output hashes、page count、route、aspect ratio、authoring package identity、Clear Writing identity、render set、contact sheet、fonts、text extraction、changed PageIDs 和可供未来 validator 使用的 extra-validator refs。

## 6. 页面生产系统：作者决定与实现部件

### 6.1 页面首先是一项认知任务

每页必须在写文案/排版前回答：

- 听众进入这一页时知道什么；
- 这一页只改变什么；
- 哪个对象承担主要解释；
- 哪些信息只支持主要对象；
- 讲完后听众能复述什么；
- 为什么下一页自然跟上。

若不能回答，不能生成页面。禁止用默认卡片、标题+段落或随机双栏填补未决作者问题。

### 6.2 页面原型不是固定模板截图

共享原型按语义关系组织：

- `FOCAL_CLAIM_EVIDENCE`
- `CONCEPT_EXAMPLE_INTERPRETATION`
- `SEQUENTIAL_MECHANISM`
- `PEER_COMPARISON`
- `EVIDENCE_INTERPRETATION`
- `MODEL_COMPONENT`
- `MODEL_REASSEMBLY`
- `RESULT_FIGURE`
- `FORMULA_WALKTHROUGH`
- `QUESTION_ANSWER`
- `CODE_WORKFLOW`
- `ASSESSMENT_INTRO`
- `RECAP_CLOSE`

原型只冻结阅读路径、对象角色、相对空间和 fallback。不同内容不强制长成同一页。

### 6.3 响应式 fallback

每个原型必须定义有序 fallback：

```text
去重同义内容
-> 放大/重排主要对象
-> peer columns 改合理比例
-> sequential columns 改纵向
-> figure/table 重新生成 presentation-specific 版本
-> 拆成两个独立 page jobs
-> 把次要内容移到 notes/backup
-> 在角色允许范围内做小幅字号调整
-> fail with layout conflict
```

禁止直接 `\tiny`、删掉解释、把文本塞进图框、使用整页截图或把结论推到页底只为满足空白指标。

### 6.4 空白与语义邻近

空白判断必须先过内容充分性，再看构图。主体可用区域排除 headline、frame title、source、footline。规则：

- 标题/章节/结束页允许结构性空白；
- 普通页若核心概念尚未解释完，空白是可用教学预算；
- 内容完整且主要对象足够大时，空白可保留；
- evidence 与 interpretation 必须形成一个语义组，不能被 `\vfill` 或底部占用率目标拆开；
- 页面既局部拥挤又整体空，必须重排而不是称为 clean；
- 百分比、像素 gap 仅作诊断，不是允许 renderer hack 的实现目标。

### 6.5 语义样式系统

共享 core 定义：

- title、subtitle、body、subheading、secondary text；
- Question、Answer、Terminology、Example、Takeaway、Limitation、Warning；
- core formula、support formula、code、table、caption、source；
- process、layer、comparison peer、annotation。

普通 prose 默认为中性。主色只用于稳定角色，不得整句随机着色。红/橙/绿只能表达跨模板一致的风险、提醒、支持性语义；品牌皮肤不得重新解释这些颜色。

### 6.6 图表、表格、公式、代码与 diagram

- **图表**：围绕页面 claim 重绘；论文分析图若投影不可读，必须生成 presentation-specific 图；外层图片大小通过不等于图内轴/图例可读。
- **表格**：只在精确比较需要时使用；行列含义、单位、精度和关键比较清楚；解释紧邻表格。
- **公式**：先说回答什么，再展示公式；首次符号和 conditioning level明确；core/supporting math有角色层级；多页模型最后在需要时重组。
- **代码**：展示 runnable context（imports/data object/call/output/interpretation）；普通 Beamer code使用固定 `\scriptsize` 角色，禁止 `\tiny`；PDF 提取保留 ASCII quotes/operators/underscores。
- **diagram**：先证明图比文字/公式更快；节点是真实对象，边是真实关系；边界到边界连接、可见箭身、标签 clearance、peer geometry一致；空间不足转纵向编号流程。
- **caption**：采用 `REQUIRED / OPTIONAL / REMOVE` 语义判断。科学对象需要说明统计量/比较/参考线；明显情境图不加“Crab image: context only”式元标题；来源单独保留。

## 7. Shared Beamer Core + 两个皮肤

### 7.1 目录与 ownership

```text
shared/templates/beamer/
  core/
    resources.tex
    typography.tex
    geometry.tex
    navigation.tex
    footline-source.tex
    semantic-roles.tex
    layout-primitives.tex
    figures-tables-code.tex
    title-section-closing.tex
  skins/
    cuhk-research/
      colors.tex
      brand-assets/
      title-background.tex
    standard-academic/
      colors.tex
      identity.tex
  fixtures/
    component-4x3.tex
    component-16x9.tex
    long-sections.tex
    dense-math-code.tex
```

模板 chrome 由原生 Beamer负责，禁止 TikZ 重画导航/页脚来追像素指标；TikZ 只负责概念 diagram。字体/资源发现由 `render-chinese-math-pdf` 唯一拥有。

### 7.2 共享不变量

除品牌主色、校徽/课程身份、标题品牌背景外，两皮肤共享：

- TeX Gyre Termes + TeX Gyre Termes Math +限定 New Computer Modern Math + Noto CJK + Latin Modern Mono；
- 同角色字号、字重、行距、页边距和 source safe zone；
- 原生完整 section name、miniframe 大小/state/contrast/clickability；
- frame title、Question/Answer/Terminology/Caption/Source/Code；
- footline action set、光学对齐和 `x/N`；
- title/section/closing 特殊行为；
- 4:3/16:9 geometry adapter；
- duplicate `\section`、重复宏定义、host fallback、unexpected font、title/closing chrome leakage 检查。

### 7.3 CUHK 皮肤

保留用户提供模板的品牌身份：CUHK 紫色、校徽/校名、标题背景、顶部紫色导航、紫色 frame title 和底部规则。清除旧 theme 名、重复覆盖和 host font。当前模板的视觉身份不是用于所有页的固定内容布局。

### 7.4 标准皮肤

从人类接受的 STAT5060 设计中选择性移植：完整章节导航、成熟 footline、Question/Answer/Terminology、caption/source、代码角色和教学 closing。标准皮肤不带 CUHK 品牌，主色可按任务/课程配置；但主色变化不能改变角色、字号、间距和行为。

### 7.5 模板证明

实施时先以真实内容做 component/golden proof，而不是 Lorem ipsum。至少覆盖：短/长 section、10+ frames、公式、图、表、代码、Question/Answer、术语、source、title、section divider、closing、4:3 和 16:9。证明后才进入完整任务。

## 8. Teaching / research / business / revision 模式

### 8.1 研究模式

重点是研究问题、证据、失败、限制、下一实验和导师决定。内部分支名、版本、audit、当前 construction 等不得成为受众文案。Discussion 问题必须改变真实决定，记录讲者倾向、可能追问和准备回答；可见页只保留问题和必要背景/选项。

### 8.2 教学模式

学生文稿、speaker notes 和 instructor-learning companion 分离。首次介绍方法时，根据课程层级回答：为什么需要、模型/estimand怎样变、核心参数/机制是什么意思、结果如何解释、哪个假设/失败模式重要。空白不能在概念未讲清时被当成美德，也不能用 API/包依赖/内部 provenance 填充。

Assessment introduction 只讲目的、广义交付、能力目标和已确认/待公布事项；不得提供答案映射、rubric 内部逻辑或模型逐题提示。未确认信息用正常课程语言，不用 release blocker 语气。

### 8.3 商业/可编辑模式

无格式指定的 business/executive 仍默认 editable PPTX/Slides，不因双 Beamer 架构改成 Beamer。页面作者合同、Clear Writing、构图与质量标准仍共享；adapter 必须生成可编辑对象，不能用 whole-slide images冒充。

### 8.4 现有文稿修改

分类：local edit、bounded revision、major revision、failed-version recovery。局部任务保持原格式/模板，仅修改明确对象并检查依赖消费者。major/recovery 必须加载完整人类反馈、PageID 祖先、锁和 supersession；不允许“只看最新 PDF 重新做一套”。

## 9. 真实高亮/失败到部件的追踪矩阵

下表不是未来 validator rubric，而是 0.5 的生产职责。每一行都要求正常作者/生产路径主动避免或修复，不得等审稿器第一次发现。

| 真实问题族 | 根因归属 | 0.5 负责部件 | 正常路径如何处理 | 为什么能处理 / 发布证明 |
|---|---|---|---|---|
| 方法名、NB2、符号在正文前或图例中提前出现 | 作者顺序 | Page Authority + all-visible first-use registry | 扫描 title/body/legend/axis/caption/table/diagram/source；为每项设 first allowed anchor | 历史图例先用 fixture 必须在作者阶段失败；新任务 final render 无未授权 first-use |
| 页面各句正确但没有逻辑链，相邻页跳跃 | 叙事 | incoming/outgoing state + transition map + Clear Writing | 记录上一页未决问题和下一页必要性；最终 render做相邻页 wording pass | CAT-TRACE 转场回放 + fresh deck 能说明每页为何跟上 |
| `V1`、`current construction`、`Prerequisite:`、audit/API plumbing 暴露 | 受众边界/语言 | audience-role firewall + Clear Writing | visible text 每项必须属于 teaching/claim/interpret/source/instruction 角色；内部内容转 notes/internal | 历史 anti-meta fixtures失败；Clear Writing handoff 在两端真实消费 |
| rate/offset、NB2、随机截距、真实 slope、kappa、PPC 等讲不明 | 教学作者 | pedagogical sufficiency brief | first-introduction mini-sequence必须覆盖动机、变化、参数、结果解释和适用假设 | 公式+结果但无机制的历史页失败；修复页在无新增 QA prose 情况下通过 |
| 教师不懂，但学生页不应继续堆字 | artifact boundary | instructor-learning companion | learning annotation路由至教师材料；只有明确教学理由才升级可见页 | 同一 student slide保持不变、教师 companion 补足的回放 |
| 空白很大、主对象却小或内容仍欠解释 | 构图/内容充分性 | archetype-aware composition + pedagogy-before-whitespace | 先判断概念是否完整，再放大对象/补直接解释/换原型/拆页 | sparse-complete 通过，sparse-underexplained 与 filler-filled均失败 |
| 底部空白指标通过，但图/表与解释相距很远 | 构图 | semantic group/proximity | evidence+interpretation绑定同一组；stretch glue仅在独立组间 | STAT5060 P18/P35 型回放失败；修复后保持邻近 |
| 顺序推理被硬塞双栏，产生宽空沟 | 构图语义 | relation classifier | 仅 `PEER_COMPARE` 使用列；causal/sequential/denominator dependency转纵向 | 顺序 fixture双栏失败，同级 R/Python 比较保留 |
| 同一页卡片+图+段落重复表达 | 信息形态 | primitive selection | paragraph/list/table/diagram按关系选一种主表达，限制容器种类 | 历史重复 catalogue 页回放；fresh 页面无多容器同义重复 |
| 公式大小、正文、caption、图内字逐页漂移 | style core | role-driven typography scale | 角色 token + primary-object scale；禁止局部任意字号 | 两皮肤同 fixture token parity；大空白中小公式触发重排 |
| Question/Answer 线条超高、挤窄栏、连字符难看 | semantic primitive | measured Q/A macro + responsive fallback | rule跟随实际 text box；窄栏改 full-width；短 block禁 awkward hyphenation | 一行/多行/长问题 fixture；V04/V05 型失败回放 |
| Terminology/Example/Takeaway/普通句随意用主色 | semantic style | role contract | 普通 prose中性；accent只由角色调用；Clear Writing不决定颜色 | deck-wide role scan + rendered fixture |
| 论文图直接缩小，轴/图例不可读 | scientific object | figure communication contract + visualization handoff | 判断 claim，裁白边、重画/简化图、扩大内部字体与 legend | zoom可读但 whole-slide不可读的历史图必须失败 |
| 图和 caption 只是“Data plot/Context only” | caption semantics | REQUIRED/OPTIONAL/REMOVE | 科学对象说明比较/编码；明显情境图可无 caption；来源独立 | meta-caption 被拒、真实统计 caption通过 |
| result figure 没围绕听众需要的 claim | scientific object | claim-first figure brief | Presentations定义 claim和比较，scientific-visualization决定编码 | CAT-TRACE log-MSE/overprediction 类型回放 + unrelated result task |
| diagram 节点/箭头语义弱、短、脱离、穿字 | diagram authoring/rendering | semantic graph + geometry tokens | 先判断必要性；边界连接、可见 shaft、clearance；不足则纵向 | CAT-TRACE/STAT5060 短箭 fixture；不新建低配万能 geometry engine |
| 复杂模型拆多页后听众拼不回整体 | 叙事/科学对象 | model reassembly requirement | Page Authority判断 section结束是否需要 closure；用稳定对象关系重组 | multi-page model case 能在 closure页恢复整体，不重复空流程图 |
| oracle DGP 检查与 fitted recovery混成一个结论 | 科学语义 | experiment/simulation page job | domain owner固定 experiment role；title/takeaway/caption保持不同证据强度 | 已知 simulation fixture + fresh simulation task |
| 表格孤立、行标签乱换行、与图硬并排 | 构图 | table object contract + responsive archetype | 表只用于精确比较；解释相邻；短 label有空间不换行；图表非 peer不并排 | STAT5060/TRACE table regressions回放 |
| 代码只有片段、对象未创建、包名矩阵替代工作流 | teaching/code | runnable-code page contract | imports/data/call/output/meaning；shared backend与参数差异诚实说明 | R/Python teaching case语法/smoke + visible interpretation |
| PDF 代码引号变弯、不可复制 | delivery | text-layer/code extraction QA | TeX literals/字体/ToUnicode；`pdftotext`和语法抽取 | 历史 curly-quote fixture失败；final PDF可复制 |
| 代码被正文尺码审稿误杀或被压到 `\tiny` | typography | distinct code role | code默认 `\scriptsize`；QA看投影可读、换行、裁切，不与 body等大 | scriptsize positive + tiny/clipped negative fixtures |
| source/Data/Figure 标签不一致、参考题名被改写 | citation | three-layer citation contract | slide credit role统一；bibliography来自权威 metadata；文本层校验 | 真实 metadata生成 references；错误/简称题名失败 |
| duplicate `\section` 但页数/链接检测仍过 | template core | logical section manifest + rendered navigation | 一逻辑 section一声明；核对可见 label sequence和frame membership | Rich Edition duplicate label fixture失败 |
| header miniframe 太小、inactive contrast差 | template core | native miniframe shared tokens | 原生尺寸/state/contrast；1920x1080 whole-slide header proof | 长/短 section与10+ frame fixture |
| footer按钮、source、页码光学不齐，后续字体改动又回归 | template core | shared footline + dependency invalidation | template/font/page-count变化自动重跑 representative crops | 注入 offset失败；两皮肤同 core通过 |
| title/closing页泄露普通导航 | template core | page-archetype chrome policy | title/section/closing抑制或调整普通 chrome | 三类特殊页 fixture |
| 结束页总是 Thanks 或生成式问题 | authoring | purpose-driven closing | research recap+decision；teaching recap+next/contact；外部报告按场景 | closing job对齐 deck purpose 的完整任务 |
| 作业介绍像答案 scaffold 或暴露 rubric | teaching boundary | assessment-introduction contract | 只讲目的/交付/能力/确认状态；答案/评分逻辑留内部 | 历史 answer-mapping slide失败 |
| provisional 日期/政策写成内部 blocker | teaching language | audience admin role + Clear Writing | 正常课程语言说明待公布，不展示治理状态 | student-facing anti-meta pass |
| existing deck局部修复改坏已接受页 | revision authority | stable PageID + semantic/copy/visual locks | current allowlist外 body pixels/source保持；依赖 consumers显式 rerender | accepted-element replay + unrelated-page unchanged |
| 人类拒绝后旧自动 PASS仍被当权威 | revision lifecycle | human rejection precedence | 旧 PASS降为历史证据；任何可见改动生成新候选 | rejection-after-PASS replay |
| 旧反馈换页后复发 | cumulative guard | semantic feedback guards + ancestry | feedback绑定语义角色/PageID祖先，不只页码 | known pattern moved page fixture |
| 最终文件只给 repo path，用户打不开 | delivery | direct artifact handoff | host支持时附真实 PDF/PPTX/source；路径/hash只作 provenance | 一次 Beamer和一次 editable PPTX正常交付 |
| CUHK/standard 字体随主机漂移 | resource core | fixed font policy + renderer resource owner | exact bundled files、`pdffonts` allowlist、missing resource fail | 两资源根配置一致；注入 fallback失败 |
| CUHK 与 standard 同角色字号/宏继续分叉 | shared core | core + skin-only override boundary | skin只覆写品牌 token；source assertion禁止 role override | cross-template role-token parity + visual fixtures |
| Reviewer/validator发现整套大量 P1 | 产品成熟度 | pre-review readiness gate | Codex producer必须全页 render review、修 known classes，非平凡 P1 cluster阻止外送 | fresh tasks中外部审查不得成为首次系统设计；否则 release gate失败 |

## 10. 生产内部质量循环：在外部验收前完成

### 10.1 阶段

```text
Author
-> Clear Writing
-> Authoring Package freeze
-> Producer implementation
-> deterministic preflight
-> whole-slide render review
-> contact-sheet/deck-rhythm review
-> bounded root-cause repair
-> rerender all affected consumers
-> pre-review readiness decision
-> external validator / GPT Work
```

普通任务可自动完成这一循环。复杂任务默认最多两次有根因的内部修复；若仍存在系统性问题，停止并返回具体 owner，不无限刷候选。

### 10.2 Producer 自查不是最终独立验收，但必须有质量责任

Producer 的自查不能签最终 PASS，却必须真实查看所有页面的 whole-slide render和contact sheet，并逐页确认页面职责、主要对象、阅读路径、空白、字体、figure内部、caption、source、first-use 和语言角色。只有文件存在、build成功、无 overflow不构成 readiness。

### 10.3 Pre-review readiness

`READY_FOR_INDEPENDENT_REVIEW` 只有在以下条件均成立时可输出：

- 作者包全部 required page jobs实现；
- 已知回归 bank无复发；
- 所有页面 whole-slide可读；
- 没有待外部 reviewer替作者决定的故事/copy/layout；
- known P0/P1=0；
- candidate/source/render identity一致；
- Clear Writing已在实际文案路径消费；
- 用户可直接打开主要 artifact。

这不是最终 PASS；但若外部审查立即发现大量已知 P1，则 readiness mechanism本身失败，必须修插件而非只修当前页。

## 11. 本版本与未来通用验收器的准确边界

### 11.1 0.5 必须实现

- 生成正确候选所需的作者、语言、构图、模板、工具和内部质量机制；
- known regression bank；
- candidate manifest 和 exact identity；
- whole-slide/contact-sheet 自查；
- fail-closed build/resource/text-layer checks；
- external review package准备；
- external finding回到正确 owner的修复入口。

### 11.2 后续通用验收器实现

- 独立 reviewer runtime与模型/图像能力要求；
- blind calibration、sentinel和holdout隔离；
- reviewer实际像素消费证明；
- visual与teaching/domain角色隔离、verdict isolation；
- independent result ingestion和non-override aggregator；
- `NOT_INDEPENDENTLY_VERIFIED` 等验收状态；
- project-specific额外 validator组合；
- final acceptance controller。

### 11.3 不能用边界逃避的事项

“属于 validator”只意味着**独立判定机制以后实现**，不意味着 Presentations 可以不解决生成根因。header太小、语义不足、双栏错误、代码不可复制、first-use错误、AI语言等全部属于 0.5 生产能力；validator以后只是独立发现它们是否仍遗漏。

## 12. 路由矩阵

| 自然请求 | ChatGPT 版行为 | Codex 版行为 | 默认产物 |
|---|---|---|---|
| 研究组会/进展/导师讨论，无格式 | 作者包 + CUHK route + Codex handoff | direct Author+Producer | `.tex` + PDF + renders + source |
| seminar/paper talk/QE/defense | 同上，按受众调整 | 同上 | CUHK 或用户/venue模板 |
| tutorial/lecture/课程讲解 | 教学作者包+学生/教师边界 | direct teaching author+standard skin | `.tex` + PDF + optional companion |
| business/executive/product | 作者/故事/文案，editable route | editable adapter | PPTX/Slides + render |
| 明确 PPTX/Slides/editable | 保持可编辑 | official editable adapter | editable artifact |
| 用户提供模板 | 锁定模板权威 | 适配并保留 | supplied format |
| existing deck + feedback | 读 baseline/history/locks | bounded revision/recovery | 保持原格式 |
| 一个局部文字/对齐/颜色 | 冻结 exact edit和保护范围 | fast local edit | affected render + original format |
| 只要逐页计划/讲稿 | 直接交付 plan/notes | 可停在 authoring package | no fake artifact claim |

## 13. Capability Gate Matrix

### G1 — 双端正常入口与路由

- **能力**：自然 presentation 请求能在 ChatGPT和Codex分别触发正确作者能力，并选择正确格式/模板/mode。
- **证据**：真实 ChatGPT personal Plugin wrapper与真实安装的 Codex plugin；自然请求不点内部 skill。
- **失败**：任一端只会研究组会；Codex direct绕过 Author；business被改成Beamer；local edit跑全量重做。
- **最终候选**：YES。

### G2 — 作者语义与来源保真

- **能力**：受众、故事、PageID、page job、证据、首次出现、转场、可见/notes边界完整，并在两端一致。
- **证据**：完整 research、teaching和一个非学术 editable任务；authoring package与final deck对应。
- **失败**：内部语言泄漏、符号先用后讲、页面无职责、结论超过来源、Codex临场改语义。
- **最终候选**：YES。

### G3 — Clear Writing 实际集成

- **能力**：两端在冻结语义后真实调用 Clear Writing，输出影响实际 slide copy且不改变受保护意义。
- **证据**：调用/身份记录、before/after、final render；中文和英文任务各至少一个。
- **失败**：只读 skill、不调用；Presentations复制通用写作规则；文案改变数字/公式/claim；render后机械语言仍普遍存在。
- **最终候选**：YES。

### G4 — 页面构图与读者努力

- **能力**：relation-driven archetype、semantic proximity、空白、层级、responsive fallback和整套节奏直接产生可投影页面。
- **证据**：包含公式/图/表/代码/Question/顺序与同级比较的完整任务；whole-slide和contact sheet。
- **失败**：局部拥挤+整体空、顺序双栏、主对象小、证据远离解释、靠小字/填充解决。
- **最终候选**：YES；独立 qualitative judgment required。

### G5 — 科学/教学对象质量

- **能力**：图表、模型、diagram、公式、simulation和教学首次介绍服务真实 claim/学习目标。
- **证据**：research与teaching完整任务，领域 owner可核对。
- **失败**：论文图缩贴、diagram只是prose boxes、模型无法重组、oracle/fitted混淆、教学机制缺失。
- **最终候选**：YES。

### G6 — Shared Beamer Core 与双皮肤

- **能力**：两个皮肤真实加载同一 core；只品牌 token不同；4:3/16:9和native chrome成熟。
- **证据**：source consumption、role-token parity、component fixtures、完整CUHK/standard deck。
- **失败**：两套字体/字号/宏分叉、duplicate section、小 miniframe、footer漂移、host font fallback、TikZ chrome。
- **最终候选**：YES。

### G7 — Teaching、assessment 与 instructor companion

- **能力**：学生文稿教学充分且不泄露答案，教师学习材料独立，closing与课程目的一致。
- **证据**：fresh teaching task + STAT5060 known regression replay。
- **失败**：公式结果无解释、API plumbing占位、assessment scaffold、教师内容塞学生页、generic closing。
- **最终候选**：YES。

### G8 — Existing-deck 收敛与人类权威

- **能力**：局部修改保护accepted work；重大返修消费完整历史并单调收敛。
- **证据**：真实 revision/recovery replay，feedback换页复发和human rejection after PASS。
- **失败**：重生成无关页、旧问题复发、exact copy破坏、人类拒绝被旧PASS覆盖。
- **最终候选**：YES。

### G9 — 引用、文本层、代码与直接交付

- **能力**：引用/书目真实，PDF文本与代码可复制，用户直接获得文件和可编辑源。
- **证据**：Beamer和editable各一项真实交付。
- **失败**：题名改写、乱码、curly quotes、不可打开、只给路径、源与render不一致。
- **最终候选**：YES。

### G10 — Pre-validator 生产质量

- **能力**：Codex在外部审查前主动关闭所有已知生产问题，外部 validator/GPT Work只发现少量真实遗漏而非首次完成设计。
- **证据**：known regression bank先跑；fresh full tasks上独立审查不出现系统性P1 cluster；同一final candidate。
- **失败**：P0、历史P1复发、同根因多页P1、外部审查要求重写故事/模板/大量页面。
- **最终候选**：YES；这是0.5发布的核心 Gate。

### 横向规则

- cheap deterministic known regressions先于fresh/付费审查；
- 所有发布 Gate绑定同一 final candidate和真实安装身份；
- ChatGPT wrapper、Codex plugin、canonical source、Clear Writing版本、模板 source、artifact/render可追踪；
- 已用于设计/修复的 STAT5060、CAT-TRACE材料只算known regression；fresh任务在候选/rubric冻结后选择；
- README/changelog/version/profile/Marketplace parity属于release closure，不冒充能力。

## 14. 实施分包

最终可以由一个 Codex Goal自动编排，但语义上拆成以下包；任何包改变冻结架构需回 Planner/Critic。

### P0 — 来源锁、TODO/Issue disposition 与回归 bank

- 锁定 central、CUHK、STAT5060、Clear Writing来源；
- 为每个非-validator TODO写 `implemented by / regression / Gate / non-goal`；
- 合并重复问题，不因每个高亮新增 gate；
- 冻结 positive/negative/should-not-change样本。

### P1 — Canonical authoring core 与双端分发

- 定义 AUTHORING PACKAGE；
- ChatGPT wrapper payload与触发；
- Codex direct Author + consume-frozen-package；
- source/generated parity；
- 真实双端正常入口。

### P2 — Clear Writing integration

- 定义 handoff contract和两次调用；
- ChatGPT/Codex companion packaging/profile；
- fidelity/space conflict/failure semantics；
- 中英文真实回放。

### P3 — Composition 与 scientific/teaching object system

- relation/archetype/fallback；
- whitespace/proximity/style roles；
- figure/table/formula/code/diagram/model closure；
- teaching、assessment、instructor companion。

### P4 — Shared Beamer Core + skins

- 选择性移植；
- fixed resources；
- native navigation/footer；
- semantic macros；
- 4:3/16:9；
- real-content component proof与cross-skin parity。

### P5 — Revision/recovery 与交付

- stable PageID、locks、human feedback/supersession；
- local edit escalation；
- citation/text layer/code copyability；
- direct artifact handoff；
- candidate manifest。

### P6 — 集成、Capability Gates 与release closure

- full known bank；
- representative development tasks；
- pre-final Critic检查；
- frozen fresh batch；
- external review；
- README、changelog、version、Marketplace/profile、private ChatGPT wrapper和Codex发布。

## 15. 版本、README 与发布身份

本设计文件不决定最终 repository版本号。默认 proposal：

```text
presentations Codex plugin: 0.4 -> 0.5
ChatGPT personal Plugin: dedicated wrapper version, capability identity = presentations 0.5
repository: release-time semantic decision
```

ChatGPT wrapper版本号服从 Plugin Creator/现有wrapper规则，不在架构阶段伪造当前版本；但发布证据必须记录 wrapper identity、文件hash和实际ChatGPT Web调用。README至少要更新产品用途、两个入口、默认路由、Clear Writing companion、双模板和交付方式；内部 Gate/Reviewer字段不堆给普通读者。

## 16. 风险、停止条件与恢复

1. **范围过大**：不得以删掉用户明确要求收缩；应通过复用 canonical source和分包控制。若一个新组件没有对应真实失败，删除组件。
2. **Authoring Package过重**：简单任务可紧凑/内存化；若用户需维护多套ledger才用得动，设计失败。
3. **Codex direct Author不可靠**：必须用正常入口证明；若只能在ChatGPT预先写完才成功，G1/G10失败。
4. **Clear Writing未被实际调用**：fail closed，不用“已遵守语言规则”代替。
5. **模板共享是假共享**：若skin能覆盖字体/字号/role macro，或两模板复制core，G6失败。
6. **过拟合 STAT5060/CAT-TRACE**：known样本只作开发；fresh跨任务验证。
7. **指标 Goodhart**：whitespace/pixel/font measurements只作诊断；不得为了数字重画低质chrome。
8. **审稿器擦屁股**：若external findings形成系统性P1批次，停止当前artifact patch，回对应production owner修机制。
9. **0.4回归**：正式0.4保持稳定，0.5未通过全部Gate不发布；可丢弃candidate而不影响release。

## 17. 正常使用六问

1. **怎样开始**：用户在ChatGPT或Codex自然提出演示文稿任务并提供来源/已有文稿；无需知道内部skill。
2. **发生什么**：先作者判断和Clear Writing，再实现/渲染/自查；ChatGPT任务需要正式文件时交Codex。
3. **默认与配置**：研究默认CUHK Beamer、教学默认standard-academic、business默认editable；显式格式/用户模板/现有文稿优先。
4. **危险动作**：本插件不自行发布、发送外部数据或消耗付费模型；外部副作用服从宿主和用户授权。
5. **失败恢复**：缺来源/语义返回一个精确问题；缺资源/工具返回具体依赖；系统性质量失败回部件owner，不无限刷页。
6. **阶段结束入口**：本设计下一入口为独立Critic；只有最终execution-ready `PASS` + `READY_FOR_CODEX=YES` 后才给Codex实现。

## 18. 与旧方案的关系

以下文件只作证据和可复用设计输入，不再自动具有执行权：

- `PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md`；
- Stage 1 v1.0–v1.3；
- `PRESENTATIONS_EXISTING_DECK_CONVERGENCE_ARCHITECTURE_V1_2026-10-06.md`；
- validator frozen spec；
- STAT5060 project-local controller/reviewer。

保留：统一前门、user template优先、双模板/shared core方向、累计反馈、stable PageID、exact candidate、native Beamer、render-chinese-math-pdf。重设计：分阶段但长期未落地的作者/模板架构、ChatGPT-only author assumption、validator与production混合、过重ledger和把审稿器当生产补丁循环。

## 19. Maintenance Board 与跟踪

当前 ChatGPT surface可写仓库文件和Issue，但没有 GitHub Project字段 mutation surface；而 Maintenance Board 要求 reader-facing Issue copy在 mutation前真实调用 Clear Writing。本轮环境没有可核验的 Clear Writing invocation surface，因此没有冒充已更新 Project/Issue。

待下一具备 Clear Writing + Project mutation能力的 AI Skills Maintainer执行：

```text
Create/reuse one top-level tracking Issue for:
  Presentations 0.5 dual-surface authoring and production
Status = DOING
Area = presentations
Execution anchor = this proposal branch/path/commit
Next action = independent Critic review of V0.2

Keep existing #29–#48/#98 source issue history.
Do not mark validator-only items DONE or merge their semantics into 0.5.
Update canonical TODO entries only after Critic confirms final disposition.
```

用户不需要手工维护。

## 20. Critic 必须重点反证

1. ChatGPT/Codex双端是否真正共享一个能力源；Codex direct是否仍把关键作者判断留给用户或审稿器。
2. Clear Writing集成是否可正常运行、确实改变最终文案、又不越权接管故事/科学/布局。
3. 高亮追踪矩阵是否覆盖真实 STAT5060/CAT-TRACE问题，是否存在“写了规则但正常入口不消费”的空白。
4. G10是否足以阻止“Codex先交烂稿，validator/GPT Work列几十个P1”的产品模式；是否过度依赖自报 readiness。
5. AUTHORING PACKAGE是否足够完整但不过重，是否会演变成另一套ledger/state machine。
6. shared Beamer core与skin boundary是否实现可行；标准模板是否错误复制候选V14或CUHK品牌。
7. production checks与future validator边界是否把独立审查推迟的同时遗漏生成根因。
8. Scope是否可由一个批准后的Codex任务真实完成；若需拆分，怎样仍保证一个final candidate和不把关键决定留给后续Executor。
9. Capability Gates是否可被fixture/schema/文件存在刷过，fresh/known/should-not-change语义是否正确。
10. 旧0.4正常研究/business/editable/existing-deck能力是否得到真实回归保护。

```text
PLANNER_STAGE=INTERMEDIATE_ARCHITECTURE_PROPOSAL
READY_FOR_CODEX=NO
NEXT_HANDOFF=CRITIC
```
