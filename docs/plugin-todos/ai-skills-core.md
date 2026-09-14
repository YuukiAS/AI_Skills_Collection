# ai-skills-core — Long-Term TODO

Canonical maintenance inbox for the `ai-skills-core` plugin and repository-maintenance product surface.

## Open candidates

### 已有规则仍失效时，先核实实际调用并去重沉淀
status: NEW
source: 2026-09-14 Bobbio / Lucerna / Mica / SeminarArc 跨项目开发反馈；用户要求以后开发不再反复依赖人工提醒，并询问是否自动沉淀 repo-specific TODO
evidence: [完整修订提案](../design/PRODUCT_DELIVERY_DISCIPLINE_V2_2026-09-14.md)；本仓库现有 `AGENTS.md` 2.1–2.2、`docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md` 及下方已推广的 direct-feedback / production-refinement 条目。Lucerna、Mica 已有真实交互/回归/有限测试规则，Frontend Design 的 Figma 闭环反馈也已存在。
problem: 规则可能已写入源文件或 TODO，却未被实际安装版本、任务入口或执行者消费；继续添加同义规则容易造成文档膨胀而没有用户可见改善。另一方面，把每次产品故障都自动变成通用插件规则，或把中央插件问题再记进项目 TODO，会制造重复维护。
project-specific context: 具体关闭语义、数据源、平台限制、当前 Figma 文件和具体产品 bug 属于各项目。本条不声称每次事故都已确认加载过该插件，不将用户不满意直接归因为中央 production runtime 缺陷。

这是既有 maintenance / direct-feedback 规则的执行验证补充，不是新建第二套流程：

- 处理“已有规则但仍失败”时，先定位任务实际使用的插件/规则入口、版本、安装/生成产物、触发路径和对应证据；按规则缺失、未调用、旧安装、执行不遵守、规则冲突或能力缺失分别归因。不得把阅读源 `SKILL.md` 当作实际 production invocation。
- workflow-core 拥有跨项目交付流程；Frontend Design 拥有 Figma/设计往返与视觉质量；Bridge Kit 拥有底层运行/交互与模板。维护者负责路由、去重和真正的生产回放，不替代领域判断。关联流程候选见 [workflow-core TODO](workflow-core.md)。
- 遇到用户纠正、实际新故障、反复失败或规则冲突时，在已授权文档范围内做小型复盘；没有新教训不强制新建文件。项目 bug/不变量留项目，通用插件反馈直接进入唯一中央 owner TODO，不维护影子清单。
- 已有条目则合并新证据；已存在 active rule 则补执行失败证据，不自动再写同义规则。项目 Executor 记录事实和可能原因，中央 Planner/maintainer 决定抽象、范围和推广。
- 自主记录事实不等于自主修改政策：不自动扩授权、验收、成本、状态机、版本或设计方向；项目 AGENTS 修改也受既有/当前任务授权约束。
- 验收未来修复时，从真实安装与调用入口回放旧失败并做相邻任务回归；不能以新增 TODO、静态字符串检查或生成层 parity 单独声称行为已改善。也不因“验收”自动引入付费 API、用户账户操作或全项目重跑。
- 对外区分“记录了问题”“合并了规则”“升级了本地安装”“真实路径通过”。所有需要用户取得的 AI_Skills 产物留 repo 内，不能公开的放 `private/exports/`，不把 repo 外临时目录作为交付位置。

推广前须证明：一个已有规则失效的真实案例被正确定位并回放；同一问题的新案例合并而非复制；纯项目 bug 未误写中央插件；无新教训的正常任务没有额外长篇复盘；中央不可写时诚实报告未记录而非创建影子 TODO。本轮仅记录，不修改 production、不 bump 版本。

## Recently promoted / established

### AI_Skills production refinement maintenance companion
status: PROMOTED
source: user requirement on 2026-09-01 for task 046
evidence: `ai-skills-core 0.2`, repository `5.0.1`, Marketplace `ai-skills-core` includes `project-skill-installer`, `ai-skills-repository-maintainer`, and `skill-library-analysis`; AGENTS, Reviewed Handoff Planner/Executor/Reviewer prompts, version policy, tests, and generated payload align.
target layer: distribution / maintenance workflow
problem: central plugin refinements could previously change production behavior while bypassing `ai-skills-core`, omit explicit maintenance/domain ownership, treat source `SKILL.md` reading as production invocation evidence, or deliver completed production behavior changes without same-task plugin version/changelog closure.
current behavior: any production central-plugin refinement must use `workflow-core` for process, `ai-skills-core` as maintenance companion, and the target domain plugin for professional judgment. The user-facing display name is `AI Skills Maintainer`, while the compatibility slug remains `ai-skills-core`. `ai-skills-core` enforces source-first edits, TODO/duplicate triage, generated parity, production replay, unrelated regression, version/changelog, and repository release closure, without becoming a domain expert or a second workflow/state/schema.
boundary: do not set global implicit invocation to true, do not create a new top-level plugin, do not copy `codex-workflow-protocol` into `ai-skills-core`, and do not modify domain plugin behavior from this maintenance layer alone.

### Artifact-aware Reviewed Handoff product pass
status: PROMOTED
source: user-reported task 044 regression on 2026-09-01
evidence: user reported that private `rewritten_report.md` still contained reader-facing `provenance`, `estimand`, `scientific gap`, `resource contract`, and `state of the art` language despite the frozen writing requirement; Reviewer did not read the full artifact before PASS. The same maintenance report also identified non-visual Visual Review PASS UI and missing default branch integration closure.
target layer: Reviewed Handoff prompts / visual-review consumer workflow / maintenance closure
problem: process gates and summaries were treated as enough to imply product/artifact quality, obvious frozen writing violations could be pushed to human judgment, non-visual tasks could display Visual Review PASS, and task branches lacked a default integration closure after Reviewer PASS.
current behavior: artifact-dependent acceptance must distinguish `PROCESS PASS` from `PRODUCT / ARTIFACT PASS`; Reviewer must read/view the final repo-safe artifact, or consume Bridge Kit Text Review evidence after that owner lands private/text artifact review. Missing artifact access is `WAITING_FOR_EVIDENCE / NEEDS_REVIEW`, not PASS. Obvious frozen-criteria violations must be REVISE/BLOCK, not human-gated. Non-visual tasks skip the real Visual Review job as `SKIPPED / NOT_REQUIRED`. Reviewer PASS without a real human gate proceeds to integration preflight, merge to `main`, push, and task-branch deletion unless an escalation condition applies.
boundary: do not modify the private 044 scientific text in this maintenance task; do not implement another private/text artifact transport or reviewer in AI_Skills_Collection; route domain writing quality to `writing-style` and bottom-layer private/text artifact review to `GPT_Codex_AI_Bridge_Kit` Text Review.

### Direct plugin-use feedback to the central plugin TODO
status: PROMOTED
source: user correction on 2026-08-31 after TRACE / Presentation real-workflow setup
evidence: root `README.md`, root `TODO.md`, `AGENTS.md`, `docs/plugin-todos/README.md`, `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`, Planner contract; TRACE `AGENTS.md` follows the same rule
target layer: distribution / maintenance workflow
problem: keeping Presentation/plugin problems first in TRACE or another project repo mixes plugin maintenance with the project's own scientific TODOs and creates duplicate records.
current behavior: project-owned research/product/code issues stay in the project repo; issues caused by an AI_Skills plugin are written directly to the corresponding central `docs/plugin-todos/<plugin>.md` as `status: NEW`. The project thread records the real failure and project-specific context; AI_Skills Planner/maintainer later deduplicates, abstracts, and decides whether the item is project-local, a generic candidate, or ready for implementation.
boundary: do not move project science, model choices, dataset interpretation, or project code TODOs into AI_Skills_Collection. Do not require project threads to invent a generic rule before recording a plugin failure.

### Repository 5.0 release epoch with independent plugin versions and changelogs
status: PROMOTED
source: long-term real-world maintenance redesign + user requirement on 2026-08-30
evidence: repository `5.0.0`, root `VERSION`, per-plugin `0.1` versions, root `CHANGELOG.md`, `docs/plugin-changelogs/`, README status table, install smoke and GitHub Actions.

### README release dashboard
status: PROMOTED
source: user requirement on 2026-08-30
evidence: README shows repository release, each central plugin version/status and changelog link; consistency is covered by repository tests.

### Legacy repository release consistency
status: PROMOTED
source: 4.4.2 baseline stabilization
evidence: `CHANGELOG.md` 4.4.2, `setup.py`, `registry.json`, Marketplace config, README and generated plugin metadata were aligned under the old lockstep model.

### Repository release is separate from capability status
status: PROMOTED
source: long-term maintenance redesign
evidence: `AGENTS.md`, `docs/PLUGIN_MATURITY.md`, `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`, README.

### One source-only TODO inbox per central plugin
status: PROMOTED
source: 4.4.2 maintenance consolidation
evidence: `docs/plugin-todos/` contains exactly one inbox for each central Marketplace plugin; regression protects set equality and generated payload exclusion.

## Do not do

- Do not create new top-level plugins to organize TODOs.
- Do not hand-edit generated marketplace/plugin layers.
- Do not turn capability status into another package version.
- Do not bump all ten plugin versions merely because the repository publishes a later patch/minor release.
- Do not restore the legacy rule that every plugin must share the repository version.
- Do not fabricate detailed per-plugin changelog history before repository 5.0.0; preserve earlier history in root CHANGELOG / Git history.
- Do not use three-part plugin versions such as `0.1.0`.
- Do not recreate the superseded “project repo first, central TODO later” plugin-feedback workflow.
