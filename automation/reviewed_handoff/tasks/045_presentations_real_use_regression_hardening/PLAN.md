---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 045_presentations_real_use_regression_hardening
decision: PLAN_FROZEN
---

# 045 Presentations — real-use regression hardening before CAT-TRACE v5

## Objective and value

先修掉这次已经被真实 CAT-TRACE v4 反复证明的 presentation production 缺口，再回 TRACE 做 v5。目标不是“把 presentation TODO 全部做完”，而是把下一轮最容易重复犯的系统性错误真正挡在交付门外。

长期原则冻结为：**以后不需要每一版 PPT 前都先改 plugin。** 真实项目正常迭代并持续把 plugin 问题写回中央 TODO；只有满足 promotion gate 的重复、严重或用户明确跨项目长期偏好，才插入一个 bounded plugin repair。CAT-TRACE v4 已达到这个门槛，因为多个 active guardrail 在连续多轮真实 render 中仍然失效。

## Frozen decisions

本任务的冻结决策由下面的 Planner triage decisions、items not promoted、implementation scope、replay/regression gates、acceptance gates 和 version decision 共同定义。本节只补齐当前 Reviewed Handoff PLAN 模板要求的结构 anchor，不改变 045 的业务内容或 workflow 状态。

## Planner triage decisions

### A. PROMOTE_NOW — existing-deck revision 必须真正进入 production/QA 路径

当前最大根因不是“规则完全不存在”，而是 TRACE v4 task 主要把 presentation plugin 当成**规则文档**读取，并没有一个稳定的 existing-deck revision production entry 把 accepted-element ledger、用户反馈、真实 render、独立 reviewer 和 bounded repair 串成完成门槛。

本任务必须优先检查并最小修复这个 consumer/runtime gap。

允许的实现方式按优先级：

1. 若当前 shared scripts 已能组合成 existing-deck revision 路径，增加一个薄的正式 entry/wrapper 和文档/测试，把现有能力串起来；
2. 若现有 production entry 可以安全扩展 `mode=existing-deck-revision`，优先扩现有入口；
3. 只有前两者都不合理时才增加一个小型 existing-deck revision helper。

禁止新建另一套 presentation workflow、schema family 或状态机。

完成门槛至少包括：reviewer-seen baseline、accepted elements、targeted feedback、re-render、known-problem high-resolution pages、independent review。Generator/Codex 自报 PASS 不能替代 reviewer。

### B. PROMOTE_NOW — first-use / narrative dependency order 作为整 deck sequence gate

这条 active rule 已存在但真实 production 继续失败，因此按 regression 处理，不新增同义 prose rule。

Executor 必须把它落到 existing-deck revision 的可执行检查中：最终 deck sequence review 必须检查新方法、缩写、数据集、领域术语、estimand 是否在首次作为中心对象前已经获得目标听众所需的解释。

不要为 CAT-TRACE 建词表。实现应使用已有 deck plan / reviewer evidence 的最小扩展；若需要额外内部字段，只能扩现有 artifact，不创建新顶级 schema。

### C. PROMOTE_NOW — rendered scientific-object QA 硬化

把下面几类 v4 失败视为一个共同的 rendered-QA batch，而不是分别再写十条自然语言规则：

1. **Diagram geometry**：内容驱动 node width；避免无意义强制窄框和断词；connector 必须从 semantic anchor 到目标边界，endpoint/clearance 一致；arrowhead 和可见线段在最终投影尺寸可读；已知问题页必须高分辨率单页 review。
2. **Scientific hierarchy / space use**：不允许核心对象很小、一侧拥挤，同时页面还有大块未利用空间；reviewer 必须判断 usable area 是否真正换成了字号、主图尺寸、行距和层级间距。
3. **Figure content readability**：检查图内 axis、tick、legend、panel title、annotation，而不仅是 image object bbox；每个独立图/panel 必须与自己的 caption/label 正确配对。
4. **Footer/source safe zone**：body、source line、footline/navigation 必须存在稳定安全区。全局规则使用 template-relative safe-area contract；CUHK exact Beamer 可以在模板层用真实 render 标定数值，不把同一毫米数硬编码给其他模板。

优先复用/扩展现有 `deck_quality_loop.py`、visual review inputs、CUHK template tokens、shared visual QA。不要创造一个与当前 reviewer 平行的新评分系统。

### D. PROMOTE_NOW — English scientific prose 变成完成门槛，而不是“can use”

Owner 仍然是 `presentations` routing/completion contract；`writing-style/scientific-prose` 是邻接能力。

先做 baseline：从 CAT-TRACE v4 可见英文中抽取少量**不泄露项目机密、但覆盖真实失败类型**的 representative prose，在当前未修改 `scientific-prose` 上跑正常 user-facing rewrite。重点验证 `Failure prevented`、机械 `Example.` 标签、noun-stack/table microcopy、不自然开场能否被当前 skill 正常处理。

- 如果 current `scientific-prose` 已经能改好：不要修改 writing-style；只把 presentations 的 English final-pass handoff 从 optional 改成 existing-deck research presentation 的完成门槛，并要求语言修改后重新 render 检查 layout。
- 如果 current `scientific-prose` 本身仍失败：本任务不要顺手大改 writing-style，进入 `NEEDS_GPT_PLANNER` 或把 writing-style NEW 保持待下一 bounded task。

语言 pass 必须发生在科学结构、公式、claim、citation 和 page function 冻结之后；writing-style 不得改 layout 或科研结构。

## Items not promoted in this batch

以下 v4 反馈仍有价值，但本轮不为了“全部清 TODO”而一起实现：

### CANDIDATE_GENERIC

- table/list/paragraph 的精确 typography 与选择 primitive；
- complex multi-slide model 的 model-closure/reassembly page；
- Question/Background 的统一视觉 primitive；
- slide-level source/figure citation 的完整 house style。

原因：这些都可以在 CAT-TRACE v5 项目层先正确实现，同时继续作为真实证据；目前没有必要为了一个 deck 把全局 presentation layout 固化得过细。若 Executor 发现已有 active primitive 只需很小修复即可解决明显 regression，可以在不扩大语义边界的情况下补 regression test，但不得把这些项升级成大型子项目。

### PROJECT_LOCAL

- CAT-TRACE 不再使用 `taxa` 的具体措辞偏好；
- CAT-TRACE model closure 页具体应该列 finite catalogue、open tail、matching、residual dependence 的哪些公式；
- CAT-TRACE 的 exact page order、theory 内容、真实数据名称和讨论问题。

这些留在 TRACE v5 task，不进入 plugin。

## Implementation scope

允许修改已有 presentation 层中的最小必要文件：

- `plugins/codex/plugins/presentations/skills/research/SKILL.md` 的 source authority 对应文件；
- `references/real-world-presentation-guardrails.md` 的 source authority 对应文件；
- `plugins/codex/plugins/presentations/shared/scripts/` 中现有 production / quality / review helpers；
- exact CUHK Beamer template/style tokens，仅用于 template-relative safe-area 或 canonical connector primitive；
- current presentation schema / validators，仅当不增加新顶级 schema 且确实需要把冻结规则落到可执行门槛；
- existing presentation tests / regression fixtures；
- `docs/plugin-todos/presentations.md`：按本轮真实 replay 更新对应 NEW 状态；
- `docs/plugin-todos/writing-style.md`：只记录 baseline 结论或 owner handoff，不在本任务随意改 writing-style production skill；
- generated Codex/Marketplace presentation plugin layer只能通过现有 generator 重建，禁止手工 patch generated mirror；
- `results/045_presentations_real_use_regression_hardening/` 的非泄露型执行/评审摘要。

如果当前 source authority 路径与 generated mirror 不同，遵守 repository maintainer 规则，从 source 改起再 regenerate。

## Required baseline diagnosis

Executor 在写代码前必须先回答并记录：

1. CAT-TRACE v4 task 实际有没有调用 `generate_research_presentation_production_entry.py` 或等价 production path，还是主要靠人工读取 skill/guardrails 后直接改 `.tex`？
2. current existing-deck revision 是否有正式可调用入口；如果没有，当前 guardrail 为什么没有被 production enforcement 消费？
3. independent visual reviewer 是否实际参与 v4 最终 PASS；如果没有，为什么 Codex self-inspection 能越过 plugin 的“generator must not assign final PASS”合同？
4. current `scientific-prose` 在 representative English slide microcopy 上 baseline 是否已经足够？

诊断必须决定实际修改；不要预设所有问题都需要新代码。

## Replay and regression gates

## Acceptance and regression gates

本任务的验收和回归门槛由本节、后续 `## Acceptance gates`、`## Repository / CI` 和 `## Version decision` 共同定义；不得用 process PASS 替代 artifact/product PASS。

### Known replay: CAT-TRACE v4

从本机 TRACE checkout 读取 v4 source/PDF，不把完整内容提交到公开仓库。修复后至少验证现有路径能够对这些已知问题给出 `REVISE/BLOCKED`，而不是错误 PASS：

- method/acronym 早于必要背景；
- narrow diagram nodes + awkward line breaks；
- connector endpoint/clearance 明显不一致；
- tiny figure internal text/caption pairing；
- large unused space while primary object remains small/crowded；
- body/source/footer safe-zone violation；
- English slide prose 未经过 final scientific-prose handoff。

不要求 045 直接把 CAT-TRACE v4 改成 v5；只证明 plugin/revision path 能识别和阻止这些失败。

### Unrelated regression

至少使用一个当前 repository 已有、与 CAT-TRACE 无关的 research presentation regression / fixture / cached rendered case，验证：

- 不会把所有页面强迫成同一布局；
- legitimate compact diagrams 不会因为 node/arrow 规则被误杀；
- intentionally sparse take-home / transition slide 不会因为 occupancy 规则被机械判失败；
- figure-free math slide 不会被 figure caption 规则误伤；
- English prose handoff 不会改公式、数值、citation 或 claim 强度。

若没有合适 fixture，优先复用现有 four-slide / current-library regression，不要为本任务大建 synthetic benchmark chain。

## Acceptance gates

### Production routing

- existing-deck research revision 有明确、可执行、文档化的 production path；
- natural request “继续按这些批注返修现有科研 PPT” 能进入该路径；
- accepted-element regression、reviewer-seen baseline、targeted feedback 和 final render 都在同一条路径内被消费；
- generator/executor 不得自行给最终 PASS。

### Narrative and audience

- final sequence review 能对 first-use / dependency-order violation 产生可见失败；
- 不需要用户提供项目专用 acronym list 才能工作；
- 不要求每个术语都单独 glossary slide。

### Rendered visual QA

- known diagram endpoint/line-break/readability failures会被挡住；
- figure internal readability和 caption pairing进入 review evidence；
- simultaneous crowding + unused space不能被“no overflow”掩盖；
- exact CUHK safe zone有模板层约束，其他模板不被同一毫米数硬编码。

### English final pass

- current `scientific-prose` baseline 若足够，则 presentations 明确把 English reader-facing final pass 设为完成门槛；
- prose pass 后必须重新 render，再做 overflow/hierarchy regression；
- writing-style 不接管 scientific structure/layout；
- 若 baseline 不足，明确停止并返回 Planner，而不是偷偷写项目禁词表。

### Repository / CI

- source/generated parity 正确；
- relevant unit/regression tests通过；
- repository canonical validate/audit/build 按当前要求通过；
- CI_required=true，因此最终必须有真实 CI 状态；
- 不提交 CAT-TRACE 私有 PDF/全文；
- 不新增顶级 plugin/skill/schema/state。

## TODO state updates expected after implementation

Executor/Reviewer 根据真实结果更新 central TODO，不机械把所有 NEW 改成 PROMOTED：

- existing-deck production path / first-use enforcement / rendered QA / English final-pass：若实现并 replay 通过 → `PROMOTED`；若证据不足 → 保持/降到 `BLOCKED_NEEDS_EVIDENCE`。
- table/list/paragraph、model closure、Question/Background、citation house style：默认整理为 `CANDIDATE_GENERIC`，除非本任务发现已有更强 active rule 已覆盖，则 `SUPERSEDED`。
- CAT-TRACE 专属措辞/结构不得进入 central TODO active generic layer。

## Routing contract

### should-trigger

- “继续按我在 PDF 上的批注返修这份现有组会 PPT，其他已经接受的页别动。”
- “用上一版作为 baseline，只修我指出的问题，然后把整份重新渲染检查。”
- “这个科研 slide deck 继续迭代，不要从头重做。”
- “返修现有 Beamer 组会 PPT，重点检查图、公式、diagram 和 page-to-page regression。”
- “这份英文科研 PPT 内容定了，最后把所有可见英文做一遍自然科研表达终审。”
- “我改了一些页面，帮我确认没有把之前接受的页面和布局改坏。”

### should-not-trigger

- “从这篇论文给我新做一套 20 页 conference talk。” → new-deck production
- “把这个 PPT 的一个框往左挪 5 像素。” → minor object edit
- “只帮我润色这三句英文，不涉及 PPT 结构。” → writing-style/scientific-prose
- “重新设计 CAT-TRACE 的模型和 theorem。” → project scientific reasoning
- “总结这份 PDF。” → summarization/document task

## Out of scope

本任务的 out-of-scope 由上面的 `## Items not promoted in this batch`、`### PROJECT_LOCAL` 和 `### should-not-trigger` 共同约束；不得把这些内容升级为 045 的实现或验收范围。

### neighbor skills

- `scientific-prose`: English reader-facing scientific language final pass; no layout ownership.
- `writing-fidelity`: protects exact facts/claims/citations during rewrite.
- `scientific-visualization`: owns standalone scientific figure construction, not whole-deck revision.
- project-local LaTeX/PDF rendering skills: compile/render mechanics, not presentation reasoning.

### front-door

`presentations` plugin / `research-presentations` existing-deck revision route. Users should not need to name internal scripts or skills.

## Version decision

Repository bump decision: NONE in this task.

Affected plugin:
- `presentations`: NO_BUMP during implementation/replay. If Reviewer PASS confirms a coherent user-visible production improvement batch, version/release is handled afterward under canonical plugin versioning policy, not mixed into repair work.
- `writing-style`: NO_BUMP; only baseline/neighbor evidence in this task unless Planner explicitly reopens scope.
