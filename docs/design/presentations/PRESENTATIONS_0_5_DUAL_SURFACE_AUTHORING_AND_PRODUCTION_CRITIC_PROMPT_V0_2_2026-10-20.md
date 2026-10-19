# Presentations 0.5 双端作者与生产架构：独立 Critic 审查提示词 V0.2

你现在担任 AI Research Stack 的全新独立 Critic，对 Presentations 0.5 的 ChatGPT–Codex 双端作者与生产架构进行一次实现前中间审查。

这不是继续旧版双模板 Stage 1，也不是验收已经实现的 0.5。旧方案、现有 0.4、STAT5060 本地实现、CAT-TRACE 历史规则和 validator 设计都只是待审证据，不自动获得保留资格或历史 PASS。

本轮最重要的用户要求是：

1. 下一版本必须同时有 ChatGPT 和 Codex 两个正常入口，并明确各自职责与交接；
2. Clear Writing 0.5 已经完成，Presentations 必须真实使用它，不能只复制几条写作规则或写“可以调用”；
3. STAT5060 Tutorial、CAT-TRACE 等真实文稿暴露的大量高亮问题必须在产品生成机制里得到明确归因和部件处理，不能全部留给未来 validator；
4. Codex 正常入口必须直接产出通常能够通过验收器的交付质量；未来通用 validator 和 GPT Work 只负责独立检查遗漏、审美与读者努力，不是替低质量实现擦屁股；
5. 本版本暂不实现通用 validator、项目额外 validator 运行时、盲审校准或最终验收控制器，但不能借此删除生成端本来就应有的作者、构图、模板、语言和内部质量能力。

## 一、Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = presentations
design_topic_or_task_key = presentations--dual-surface-authoring-production
source_branch_or_ref = design/presentations--dual-surface-authoring-production
proposal_path_and_version = docs/design/presentations/PRESENTATIONS_0_5_DUAL_SURFACE_AUTHORING_AND_PRODUCTION_ARCHITECTURE_V0_2_2026-10-20.md
proposal_commit = f818e543efed8278a718c3317695cb9135905c6b
review_stage = INTERMEDIATE_ARCHITECTURE_REVIEW_V0_2
execution_branch_or_worktree = not created
current production baseline at proposal time = main@79eb00ea41348b8b0f3b806c1dc6510cd0122658 / presentations 0.4
```

本轮只允许结论：

```text
PROCEED
REVISE
```

不得给 `PASS`，不得给 `READY_FOR_CODEX=YES`，不得启动 Codex，不得实施、发布、创建最终评估批次或消耗付费审查。`PROCEED` 只表示 Planner 可以继续形成完整 Proposal/Plan、Goal、Kickoff 和 execution-ready package。

## 二、先读治理来源

首先实际读取 `YuukiAS/AI_Skills_Collection` 最新 `main`，至少包括：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

记录实际读取的最新 main commit。若它晚于提案基线，区分治理更新是否影响当前提案；不得静默用旧合同审查。

## 三、必须直接读取的产品与证据

### A. 当前 Presentations 生产实现

至少读取：

- `plugins/codex/plugins/presentations/.codex-plugin/plugin.json`
- `skills/tools/documents-media/presentations/research-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/business-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/shared/chatgpt-web-authoring-contract.md`
- `skills/tools/documents-media/presentations/shared/authoring-production-workflow.md`
- `skills/tools/documents-media/presentations/shared/presentation-end-to-end-pre-execution-runbook.md`
- `skills/tools/documents-media/presentations/shared/pre-execution-cumulative-acceptance-contract.md`
- `skills/tools/documents-media/presentations/shared/template-routing.md`
- `skills/tools/documents-media/presentations/shared/font-policy.md`
- `profiles/presentation-desktop.json`
- `docs/plugin-todos/presentations.md`
- Issue `#98`
- `docs/plugin-changelogs/presentations.md`

检查当前 0.4 正常能力、入口、已有作者合同、路由、模板、revision 和渲染机制究竟哪些真实存在，哪些只有文档声明。

### B. Clear Writing 0.5 与跨插件边界

至少读取：

- `plugins/codex/plugins/writing-style/.codex-plugin/plugin.json`
- `plugins/codex/plugins/writing-style/skills/fidelity/SKILL.md`
- `plugins/codex/plugins/writing-style/skills/sci/SKILL.md`
- `plugins/codex/plugins/writing-style/skills/zh/SKILL.md`
- 需要时读取 `scientific-rewrite` 与 `response-clarity`
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`
- Clear Writing 0.5 release closure 与 PRIVATE ChatGPT plugin parity 的当前正式证据

不要把“Clear Writing 已安装”“Presentations 文档提到 writing skill”当作已经集成。审查必须判断：两个正常入口怎样真正消费同一个 canonical Clear Writing 来源，怎样证明文案实际受影响，怎样避免 Presentations 复制通用语言规则，以及 Clear Writing 不可用或改变受保护语义时怎样失败。

### C. STAT5060、CAT-TRACE 与真实高亮证据

读取架构 V0.2 中列出的高亮/失败追踪矩阵，并独立核实其关键来源。STAT5060 至少检查：

```text
repository = YuukiAS/STAT5060-TA
ref = tutorial@6fc5193653344f0e71c7d9013c22f3a9959405dc
```

至少读取：

- `materials/2026-27/shared/beamer/stat5060-course-standard-beamer-v2.tex`
- `materials/2026-27/tutorial-01/theme/stat5060-student-deck-v14-beamer.tex`
- `materials/2026-27/tutorial-01/releases/student-deck/V14/VERSION.json`
- V14 source/PDF locator、历史 V01–V14、高亮/人工反馈、PageID/feedback registries 中与提案矩阵直接相关的部分
- `docs/authoring/2026-27/STAT5060_TUTORIAL_01_HUMAN_FEEDBACK_MASTER_LEDGER.md`
- 需要核实某个归因时再读取对应原始批注、render 或历史 source，不因文件多而机械全量读取所有无关证据

CAT-TRACE 至少从 `docs/plugin-todos/presentations.md` 和其中列出的真实提交/审查证据核实：first-use、转场、diagram、图内文字、result figure、模型重组、Question、引用、语言和 existing-deck 回归。

对架构矩阵中的每个问题族，判断它是否真的有来源证据，是否被正确归因，还是 Planner 把 validator、来源材料、领域语义、环境问题或一次性项目偏好误写成通用生成器职责。

### D. CUHK 与标准模板来源

若当前 Project/thread 可以访问用户上传的：

- `CUHK Template.pdf`，SHA-256 `a62a4bb5ec2296b875ffe9ff8c1d850b88797e27a74aac7d64f576abb91daa7e`
- `CUHK Template.zip`，SHA-256 `5cbe4a545d8abbab007f5f0aceec405138f8035b9dcb09c617e1e7cf7b525ee9`

则直接查看 PDF 像素与源码，不得只读 Planner 总结。重点核实顶部章节导航、标题页、frame title、字体/字号、底部规则、原生导航、页码、Question/Terminology 等样式与源码中的重复覆盖、硬编码比例、旧 theme 命名和主机字体依赖。

若附件在独立 Critic 环境不可访问，明确写出 `NOT_DIRECTLY_REVIEWED` 的范围。中间架构审查可以继续判断其余机制，但不得声称已经验证模板像素或源码；最终 execution-ready 审查前必须补足。

### E. 旧方案只作输入

按需读取：

- `docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md`
- Stage 1 v1.0–v1.3
- `docs/design/PRESENTATIONS_EXISTING_DECK_CONVERGENCE_ARCHITECTURE_V1_2026-10-06.md`
- `docs/frozen/PRESENTATIONS_VALIDATOR_V1_FROZEN_SPEC_2026-10-06.md`

检查 V0.2 是否选择性复用成熟机制，还是把旧架构换名字后重新引入。不得因为旧方案曾获历史 PASS 就要求保留，也不得因为用户宣布旧实施作废就拒绝复用已经由真实结果证明有价值的部分。

## 四、独立复述用户真正要的产品

在看 Planner 结论前，先用自然中文回答：

1. 用户在 ChatGPT 中怎样开始，最终能得到什么；
2. 用户在 Codex 中怎样直接开始，最终能得到什么；
3. 两端共享什么、各自独有能力是什么；
4. Clear Writing 在何时介入，介入前后谁仍对什么负责；
5. 为什么未来 validator/GPT Work 不应成为第一次完整设计与逐页 QA；
6. 正常情况下怎样观察到“Codex 已经直接产出交付质量”，而不是“审稿器很会找问题”。

若你复述出的正常产品和 V0.2 实际机制不一致，按真实缺口给 `REVISE`。

## 五、重点审查问题

### 1. ChatGPT 与 Codex 双端是否是真实产品，而非文档标签

逐项检查：

- ChatGPT 版的真实分发形态、正常触发、payload、版本、source parity 和文件能力边界是否可实现；
- Codex 版是否既能消费 ChatGPT 作者包，也能在用户直接从 Codex 开始时完成完整 Author phase；
- Codex direct Author 是否仍把受众、故事、page job、copy、构图或来源判断暗中留给用户、GPT Work、validator 或 Producer；
- 两端是否维护一套 canonical authoring source，还是复制两套 prompt/规则后必然漂移；
- `research-presentations`、`business-presentations`、teaching/general mode 和 unified front door 的入口身份是否清楚；是否需要一个统一 orchestrating skill，若需要，提案有没有冻结，而非留给 Codex决定；
- ChatGPT wrapper 与 Codex Marketplace/plugin/profile 的安装、版本、README、发布和正常入口 Gate 是否完整；
- 简单任务是否足够轻，复杂任务是否不会因 ChatGPT/Codex切换丢失权威。

若双端只在架构图里存在，或 Codex direct 只能在用户先给完美作者包时产出好文稿，必须 `REVISE`。

### 2. Clear Writing 是否被真实集成，边界是否正确

检查完整因果链：

```text
Presentations page brief
-> Clear Writing canonical skill/runtime
-> 返回受保护的可见文案
-> Presentations composition/render
-> render-scale bounded language pass
-> final artifact
```

重点判断：

- ChatGPT personal Plugin 怎样获得/调用 Clear Writing：共同安装、canonical co-packaging、wrapper composition 或其他成熟路径必须冻结；不能把关键 packaging 决定留给 Executor；
- Codex Marketplace/profile 怎样确保相关 Clear Writing skills 真实可见并被调用；
- 两端怎样证明实际 invocation，而不是“读取了 SKILL.md”或“遵守了写作原则”；
- Presentations 给 Clear Writing 的输入是否包含受众、page job、证据、精确词、空间预算和禁止变更；
- Clear Writing 返回过长、改变 claim/公式/数字/引用、或不可用时，失败与恢复是否真实；
- Clear Writing 是否越权决定故事、布局、图型、教学内容或科学结论；
- Presentations 是否重复维护普通中文/英文写作规则，造成 rule fork；
- render 后第二次语言 pass 是否有界、可重渲染且不会无限循环。

如果集成仍只是“将来调用 Clear Writing”，必须 `REVISE`。

### 3. 产品生成机制是否覆盖真实高亮，而非把责任推给 validator

逐行审查 V0.2 的“真实高亮/失败到部件追踪矩阵”。至少对每行回答：

```text
source evidence 是否成立
root cause owner 是否正确
负责部件是否已经或可被正常入口消费
生成时实际改变什么决定/实现
什么正向行为证明机制发生
什么失败能阻止候选外送
是否有 should-not-change 反例
```

特别关注：

- first-use 是否覆盖图例、轴、表格、diagram、caption 和 footer；
- 教学充分性是否是真正作者能力，不是五个固定小标题；
- 空白、语义邻近、双栏/纵向、对象尺度是否会被指标 Goodhart；
- 图表、表格、公式、代码和 diagram 的专业 owner 是否正确；
- Question/Answer、Terminology、caption、source、closing 是否既有语义又有响应式几何；
- template chrome、字体、miniframe、footer、duplicate section、4:3/16:9 是否由 shared core承担；
- existing-deck locks、人类拒绝优先、历史反馈换页复发是否属于生产 revision能力；
- 直接 artifact handoff 是否属于完成定义；
- 项目专属统计/课程内容是否被错误编码进中央插件。

不能接受“未来 reviewer 会抓到”作为生产机制。若一项历史高亮只出现在 Gate/检查表，没有改变作者/Producer正常行为，必须要求补机制。

### 4. G10：Codex 是否真的在外部审查前达到交付质量

这是本轮最重要的独立判断。

审查 V0.2 的 pre-validator quality loop 和 `G10 — Pre-validator 生产质量` 是否足以阻止以下坏模式：

```text
Codex build PASS
-> 交给 validator/GPT Work
-> 一次找到大量 P1 / 多页同根因问题
-> 再逐页修
-> 把审稿器当成真正的设计器
```

至少判断：

- Producer/内部 reviewer 是否真的看所有 whole-slide render 与 contact sheet，而不是写同质化 self-review rows；
- known regression bank 是否在外部审查前运行，且不会被 fixture-specific hardcode刷过；
- readiness 是否只是自报字段，还是由可观察产物、正常入口和候选身份支持；
- “known P1=0”怎样避免把未分类问题或新问题藏起来；
- 外部审查发现单个新 P1、少量审美意见、同根因多页P1、历史P1复发、P0时分别如何归因；
- 系统性 P1 cluster 是否会回到 production mechanism owner，而不是只修当前 deck；
- GPT Work仍能做独立审美判断，而不是因为严格限制而被架空；
- Gate 是否错误要求所有 fresh候选“零任何P1”，导致审稿器只能重复产品自评或移动终点。

请给出一个可执行、不过度承诺的发布成功定义。若 V0.2 的定义过松或不可操作，`REVISE`；若只需澄清措辞而主机制成立，可 `PROCEED` 并列出下一 package必须冻结的定量/定性边界。

### 5. AUTHORING PACKAGE 是否完整但不过重

检查 `DECK_BRIEF / PAGE_AUTHORITY / VISIBLE_COPY_AUTHORITY / COMPOSITION_AUTHORITY / REVISION_AUTHORITY / CANDIDATE_MANIFEST`：

- 是否每个对象阻止一个真实失败；
- 是否有重复字段、互相漂移的第二套 ledger/state machine；
- 简单任务能否内存化/紧凑化，不让用户维护治理文件；
- 复杂任务中 Producer是否能仅凭作者包实现，而不重新做语义决策；
- visible copy在新建、minor revision、exact-copy三种情况下的冻结时点是否合理；
- PageID、feedback lifecycle、locks是否只在需要的 revision/recovery中启用；
- existing `deck-plan.schema.json` 的迁移/兼容/退休路线是否需要进一步冻结；
- 作者包和最终 artifact之间怎样证明真实消费，而不是文件存在。

若作者包过重，要求删减；若过简，指出具体哪类真实失败仍会发生。

### 6. Shared Beamer Core + skins 是否可实现、可维护

检查：

- core和skin override边界是否足以保证同角色字体、字号、间距、导航、footer、semantic macro一致；
- CUHK视觉身份、GPL/上游theme、CUHK品牌资产和再分发边界是否有清楚来源；
- standard-academic是否从最终人类接受的STAT5060行为选择性移植，而不是复制当前V14候选或课程内容；
- fixed font/resource policy是否真正由`render-chinese-math-pdf`拥有；
- native Beamer chrome是否被保留，是否仍可能用TikZ/custom glyph追指标；
- 4:3与16:9是geometry adapter还是两套模板；
- component/golden proof是否使用真实内容并在完整任务中实际消费；
- shared core变化是否触发两个皮肤和现有真实deck的broad regression。

若“共享”主要靠文档约定、skin仍可复制/覆盖核心角色，必须 `REVISE`。

### 7. 模式覆盖与职责边界

独立检查 research、teaching、business/editable、existing-deck revision/local edit：

- 各自正常入口、默认格式、模板和交付物；
- 用户模板、显式格式和existing-deck template是否始终优先；
- teaching companion、assessment anti-leakage和student/instructor边界；
- research discussion question、negative result、next decision；
- business route是否仍为真正可编辑对象；
- local edit是否保持轻量，不被迫生成全套作者包；
- major/recovery是否消费完整历史而不重做无关页；
- scientific-visualization、统计/医学/生信domain、Clear Writing、Presentations和rendering owner是否彼此不越权。

### 8. Capability Gates、分包与最终执行可行性

审查 G1–G10 是否：

- 证明不同真实能力而非重复；
- 有 normal entry、正向行为、明确失败、should-not-change、同一final candidate；
- 覆盖ChatGPT wrapper、Codex plugin、Clear Writing实际消费、完整artifact、复杂任务和真实安装身份；
- 正确区分 known regression、development sample、fresh evidence和最终批次；
- 不以schema、文件存在、build、hash、rows、fixture数代替视觉/教学质量；
- 不把未来validator runtime偷偷实现在0.5；
- 不因shared runtime/routing/template/profile变化错误使用narrow gate。

再审查 P0–P6 分包是否能由批准后的一个 Codex Goal真实完成：

- 若需要分阶段提交，如何保证关键决策已冻结、同一final candidate和最终集成；
- 哪些阶段可在同一任务普通返修，哪些语义改变必须回Planner；
- 是否需要先做小型真实探针验证ChatGPT wrapper/Clear Writing invocation/official editable adapter；
- 实施、回归、最终评估的成本/次数/停止条件和恢复owner；
- README、changelog、version、Marketplace/profile、generated parity和发布closure是否完整。

不要用“工作量大”本身阻塞；只有范围不可实现、职责不清、证据不可取得或复杂度明显不值时才要求改架构。

## 六、必须做的反证检查

主动尝试证明 V0.2 会失败，至少覆盖：

1. ChatGPT wrapper只有文档、不能自然触发或不能真正调用Clear Writing；
2. Codex direct Author其实仍是Producer边写边排，没有可冻结的作者阶段；
3. 两端规则复制后漂移；
4. Clear Writing改了科学含义或因空间压力删信息；
5. AUTHORING PACKAGE变成过重账本，简单任务也要维护十几个文件；
6. layout/archetype通过固定字段却仍生成一页卡片墙；
7. whitespace/connector/footer指标诱导renderer hack；
8. standard模板复制了STAT5060候选bug；
9. shared core改变导致CUHK现有能力回归；
10. known历史样本被硬编码，fresh任务仍失败；
11. Producer self-review伪造“所有页已看”，外部审查仍第一次看到明显问题；
12. external validator边界被用来延后first-use、教学充分性、语言、图表、代码或模板生产能力；
13. G10把“外部审查不得发现任何问题”写成不可证伪口号，或反过来允许几十个P1仍称正常；
14. exact candidate/source/render/wrapper/Clear Writing身份无法绑定；
15. 用户最后仍拿不到可直接打开/保存的artifact。

每个成立的反例都必须回指具体设计缺口和最小修订，不要只写“需更多测试”。

## 七、输出要求

先给一屏自然中文摘要，回答：

- 总结论；
- 架构方向是否正确；
- 对用户正常使用最重要的真实增益；
- 当前最危险的缺口；
- 是否需要用户做决定；
- 下一唯一入口。

然后输出正式审查：

### 1. Active Review Context 与已读证据

列出实际 main commit、proposal branch/path/commit、直接查看的关键source/render。无法访问的材料明确标出。

### 2. 用户承诺核对

逐项判断五条用户要求是否被完整保留；不得用局部 blocker替代完整基线。

### 3. Findings

使用稳定编号：

```text
PRES05-ARCH-F01
PRES05-ARCH-F02
...
```

每项必须包含：

- severity：BLOCKER / MAJOR / MINOR；
- 对应用户要求或治理来源；
- 具体证据/路径/章节；
- 为什么真实会失败；
- Planner必须怎样修；
- 怎样验证关闭。

只阻塞真实风险，不阻塞不确定感。可以把不影响中间推进的细节列为非阻塞建议，但不得移动终点。

### 4. 高亮覆盖与归因结论

评价追踪矩阵：

- 哪些问题已由具体生产部件闭环；
- 哪些仍只是检查项或口号；
- 哪些归因错误；
- 哪些项目专属内容应退回项目adapter；
- 是否足以支持“生成器承担主要质量责任”。

### 5. Capability Gate 结论

指出缺失、重复、可刷、过重或错误fresh语义，并给出建议的Gate合并/拆分，不机械追求数量。

### 6. 最终 verdict

只能输出一个：

```text
PROCEED
```

或

```text
REVISE
```

`PROCEED` 时，明确下一步仍需由 Planner 形成同版完整 Proposal/Plan、Canonical Goal、Kickoff Draft、最终Gate批次和execution-ready Critic request；不得暗示可以直接启动Codex。

`REVISE` 时，给出按优先级排序的有界修订清单，不替Planner重写整份方案。

### 7. Repo review artifact

如果当前GitHub写入面可用，只允许在提案分支新增：

```text
results/presentations--dual-surface-authoring-production/CRITIC_REVIEW_V0_2.md
```

不得修改Planner proposal、TODO、Issue、Project、production source或其他文件。提交后在回复中给出commit。若无写入面，直接输出完整审查正文，不要求用户手工维护Project。

Maintenance Board方面，核对proposal中的pending mutation是否准确；当前review verdict不得机械推进Project Status或关闭任何Issue。
