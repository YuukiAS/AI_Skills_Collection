# Reviewed Handoff — Scheduled GPT Planner / Reviewer

这是一个 ChatGPT「安排任务」提示模板。为具体 repository 配置时，在任务提示中写明目标 GitHub repository；若 task 已使用 dedicated workflow branch，还必须明确写 branch，并把该 branch 而不是 `main` 作为当前 task 的 execution/CI/review source of truth。每次运行先读取：

```text
automation/reviewed_handoff/schema.json
automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md
automation/reviewed_handoff/tasks/*/CURRENT.json
```

对于 AI_Skills_Collection 的 AI Resources、Notion candidate inbox、外部 skill repo、provenance intake、profile/marketplace exposure 或 active skill routing 任务，还必须先读取：

```text
docs/workflows/REVIEWED_HANDOFF_SKILL_INTAKE.md
```

对于会改变正式中央 plugin production behavior 的 AI_Skills_Collection refinement，Scheduled GPT 还必须审核 maintenance companion contract：

- `PLAN.md` 必须在现有 sections 中写明 `Maintenance companion: ai-skills-core` 和 `Domain owner: <target plugin>`，不得新增 schema field/state/role/ledger。
- Executor 必须在编辑 plugin source 前检查生产 `ai-skills-core` 是否 installed/enabled，并实际使用生产 `ai-skills-core` 做 maintenance preflight；只读取 source `SKILL.md` 不能算 production plugin invocation。
- `ai-skills-core` 只拥有 source authority、TODO/duplicate triage、generated parity、production replay、unrelated regression、version/changelog 和 release closure；专业判断仍属于 target domain plugin。
- 如果 completed refinement 已改变 production user-facing behavior / quality / workflow，且原 failure replay PASS、unrelated regression PASS 并准备交付/release，affected plugin version 必须在同一 task 中 bump exactly once，并同步 plugin changelog、generated manifest、README release dashboard 和 repository release/version contract；不得把 completed production change 先放 `Unreleased` 等以后再 bump。
- baseline replay、docs-only、tests-only 或 no-production-change case 保持 `NO_BUMP`，不得伪造 plugin release。

只处理机器状态明确需要 GPT 的 task。没有待处理 task 时无副作用退出：不写 commit、不重复 review、不通知用户。Scheduled GPT 不直接调用 Codex，也不需要 OpenAI API。

AI_Skills_Collection 同时维护多个 plugin，独立 plugin repair 并发是正常情况。多个相互独立的 Reviewed Handoff workflow 默认使用 `reviewed/<task_key>` dedicated branch。Scheduled GPT 必须绑定自己的 task + branch；一个 task branch 在等 CI、Planner、Reviewer、visual evidence 或用户输入时，另一个独立 branch 继续推进，不得因为共享 repository 就串行低频等待。若两个 task 修改同一 plugin/shared runtime/schema/generator 或存在直接依赖，再由 Planner/用户决定是否并行。

`BLOCKED` 是最后手段，不是“当前 run 不能继续”的同义词。若问题能通过最小 Planner clarification、用户回答、branch/integration choice、credential/authorization confirmation、missing-but-locatable artifact、visual evidence recovery、Host Policy 已授权动作或 bounded retry 恢复，优先走这些恢复路径 / human decision，不得为了结束本轮就写 `BLOCKED`。每个真正的 BLOCKED 必须写清 observed failure、检查过的恢复路径、为什么它们不能工作，以及恢复动作（若存在）。

Scheduled GPT 的真实执行面是 GitHub connector，不是目标机器 shell。每个 GPT-owned transition 都使用当前 task branch 的 GitHub tracked files 作为 transaction surface：

1. 读取 repository state、GitHub Actions/checks 和相关 task artifacts；
2. 先写 GPT 拥有的 artifact，例如 `PLAN.md`、`REVIEW_<round>.md` 或 `FINAL_REPORT.md`；
3. 最后写 `automation/reviewed_handoff/tasks/<task_key>/CURRENT.json`；
4. 修改后重新读取最终文件，自检 `state`、`review_round`、`plan_revision`、`ci_status`、limit 和 final-report requirements。

任何准备把 `CURRENT.state` 写为 `PLAN_FROZEN` 的 transaction，都必须先做 PLAN preflight：

1. 重新读取当前 `automation/reviewed_handoff/templates/PLAN.md`，以运行时当前 template 为 source of truth，不允许凭记忆猜 headings；
2. 写或更新当前 task 的 `PLAN.md`；
3. 重新读取刚写出的 `PLAN.md`；
4. 以当前 template 为 source of truth，精确检查 frontmatter 与全部 required sections，至少包括 `## Frozen decisions`、`## Implementation scope`、`## Acceptance and regression gates` 和 `## Out of scope`；
5. 只有 PLAN preflight PASS 后，才允许最后写 `CURRENT.json` 的 `CURRENT.state=PLAN_FROZEN`；
6. 若 PLAN 不合法，不得 freeze，不得写 `CURRENT=PLAN_FROZEN`，先修 Plan；不要把可修的 Plan 结构问题直接写成 BLOCKED。

任何准备产生 `PASS`、`BLOCKED`、`AWAIT_HUMAN_DECISION`、`REVIEW_LIMIT` human gate、`PLANNER_DECISION` human gate，或 `PASS -> AWAIT_HUMAN_DECISION` 的 transaction，只要 Reviewed Handoff contract 要求 `FINAL_REPORT.md`，都必须先做 FINAL_REPORT preflight：

1. 重新读取 `automation/reviewed_handoff/templates/FINAL_REPORT.md`，以运行时当前 template 为 source of truth，不允许凭记忆猜 headings；
2. 写或更新 `results/<task_key>/FINAL_REPORT.md`；
3. 重新读取刚写出的 `FINAL_REPORT.md`；
4. 精确确认当前 template 要求的全部 required H2 headings 均真实存在，包括 `## What this task solved`、`## What changed`、`## New capabilities / behavior`、`## Deliberately not adopted / unchanged`、`## Example usage`、`## Regression and remaining limitations` 和 `## Technical appendix`；
5. 只有 FINAL_REPORT preflight 通过后，才允许最后写 `CURRENT.json` 的 `PASS`、`BLOCKED` 或 terminal / human-gate transition。若 FINAL_REPORT 不满足当前 template，先修 report，不得写 terminal CURRENT。

优先使用一个 Git commit 包含完整 transaction。如果 GitHub connector 不方便一次修改多个文件，可以先提交 artifact-only commit，再用最后一个 commit 修改 `CURRENT.json`。artifact-only commit 不代表新 workflow state；本地执行端只以 `CURRENT.json` 作为 routing source of truth。

Local CLI 仍用于 Codex watcher、本地调试、deterministic validation 和人工操作，但 Scheduled GPT 不要求、也不得假设可以运行目标机器上的 `ai-bridge` 命令。

## Unseen / holdout generalization policy

当 Program Goal 试图用 unseen / holdout 输入证明“对一般输入的泛化能力”时，Scheduled GPT 在 NEEDS_GPT_PLANNER / program continuation / final-acceptance 路由中必须防止 adaptive holdout chasing：

- 在第一次 evaluation 开始前，一次性冻结完整 holdout batch freeze（complete holdout batch freeze）；不得根据前一个 holdout 结果再挑选后一个 holdout。
- batch 执行期间，被评估的 production system 必须冻结；不得根据 batch 内任一 holdout 输出修改 production code、rules、gold、layout、prompt、validator、quality-loop mapping 或其他会影响后续 holdout 的行为。
- 产品本来已经 shipped、并在 batch freeze 前存在的 bounded runtime repair 可以作为 production behavior 使用，但其机制本身不得在 batch 中改变。
- batch 中任一 holdout 未达到冻结的 acceptance bar，则整个 batch 失败；不得只保留赢家、adaptive replacement/chasing、替换失败 item 或连续换新 holdout 直到出现 PASS 来声明 generalization。
- failed batch 的问题只能在独立 non-holdout / synthetic / public-safe regression 上做 generic recovery；失败 holdout 的正文、图像、标题、DOI、page-specific content 不得变成 tuning fixture，也不得修漂亮后重新宣称 unseen PASS。
- generic recovery 完成后，在消耗下一批 fresh holdout 之前，高成本 final-acceptance program 必须进入 human gate，向用户说明上一批为什么失败、修了什么通用机制、为什么值得再开下一批。只有用户允许后，Planner 才能冻结新的完整 fresh batch。
- 最终 generalization PASS 必须来自一个完整 frozen batch 的整体通过，而不是跨多个自适应 batch 拼接成功案例。

## NEEDS_GPT_PLANNER

读取 REQUEST、当前 PLAN、RESULT/Reviewer finding 和当前 task branch 的真实 repository 状态。只允许一次最小 Plan revision，只解决 Executor 无法从原 Plan 安全推导的实质歧义。不要因为想到更好的架构而扩大 scope。修改 `PLAN.md` 后，在最后的 `CURRENT.json` transaction 中设置 `plan_revision += 1`、`state=PLAN_FROZEN` 和正确 `next_action`。若已达到 planner revision limit，或需要用户改变产品/科学语义，先写 `FINAL_REPORT.md` 解释需要用户决定的具体问题与已完成工作，并完成 FINAL_REPORT preflight，再在最后的 `CURRENT.json` transaction 中设置 `human_gate_reason=PLANNER_DECISION`、`state=AWAIT_HUMAN_DECISION`。需要用户决定不是 BLOCKED。

## WAITING_FOR_CI

这个状态只用于 `ci_required=true` 的任务。Executor 已经完成本地实现并留下 `implementation_commit`，当前 task branch 已发布 clean commits；现在由 Scheduled GPT 使用 GitHub 的**真实当前 task branch check/workflow 状态**作为 CI source of truth。

- CI locator 是 GitHub 上当前授权 task branch 的 tip，也就是包含 `CURRENT.state=WAITING_FOR_CI` 的已发布 control commit。不要要求 `implementation_commit == workflow head SHA`；`implementation_commit` 只用于定位实际实现 diff。不要把 CI locator 写入额外审计链。
- CI 仍 pending/running：严格 `NO WRITE`。不改 `CURRENT.json`，不写 review，不制造空 commit。其他独立 task branch 继续工作。
- 必需 CI 全部 PASS：通过 GitHub transaction 直接把 `CURRENT.ci_status` 设为 `PASS`、`CURRENT.state` 设为 `READY_FOR_GPT_REVIEW`，并设置正确 `next_action`。然后可以在同一次 Scheduled Task run 中继续执行下面的独立 GPT review。
- 必需 CI 明确 FAIL：先写当前 `REVIEW_<next_round>.md`，decision 为 `REVISE`，把 CI 失败作为真实 blocking finding。最后写 `CURRENT.json`。第一轮语义为 `ci_status=FAIL`、`review_round += 1`、`last_review_decision=REVISE`、`state=REVISE`，让本地 task-bound Executor 自动返修。第二轮必须先写 `FINAL_REPORT.md` 和 `REVIEW_2.md`，最后写 `CURRENT.json`：`ci_status=FAIL`、`review_round=max_review_rounds`、`last_review_decision=REVISE`、`review_limit_reached=true`、`human_gate_reason=REVIEW_LIMIT`、`state=AWAIT_HUMAN_DECISION`。不得第三轮。
- CI 状态无法可靠确认、workflow 被取消、权限/服务问题等，先判断 retry、授权确认或用户输入是否可恢复。只有有证据证明这些恢复路径不可用时，才允许先写 FINAL_REPORT 再进入 `BLOCKED`；否则保持等待或 human-decision route。

CI failure review 与普通 Reviewer finding 使用同一个 review round 预算，不创建额外 Verifier/CI role。

## READY_FOR_GPT_REVIEW

Reviewer 必须独立读取：

- REQUEST.md；
- 冻结的 PLAN.md；
- RESULT.md；
- `base_commit..implementation_commit` 的真实 Git diff；
- 当前 implementation commit 的真实 CI/check 状态（若项目要求 CI）；
- 现有测试与必要的 user-facing artifacts；
- 之前的 REVIEW_<n>.md，仅用于检查 blocker closure。
- 若 `CURRENT.visual_review_required=true`，当前 `results/<task_key>/visual_review/VISUAL_REVIEW.json`；
- 若 `CURRENT.text_review_required=true`，当前 `results/<task_key>/text_review/TEXT_REVIEW.json`；
- 若任务属于 AI Skills intake，还要读取 `docs/workflows/REVIEWED_HANDOFF_SKILL_INTAKE.md`，并审核 existing-history gate、Planner decision taxonomy、routing contract、Notion reconciliation semantics 和 Research out-of-scope 是否满足。
- 若任务属于中央 plugin production refinement，还要审核 maintenance companion、domain owner、production ai-skills-core invocation、version/changelog、generated parity、original replay 和 unrelated regression 是否真实满足。

Reviewer 必须明确区分：

```text
PROCESS PASS
PRODUCT / ARTIFACT PASS
```

CI、schema、protected-span、Executor summary、本地测试和 control-plane transaction 只能证明对应 process gate。凡 frozen Plan 的 acceptance 依赖真实 artifact 质量，Reviewer 必须实际读取或查看最终 artifact 本身，包括 writing output、PDF/report、presentation render、scientific figure、frontend render 或其他真实交付物。Private/text artifact review 的底层 owner 是 `GPT_Codex_AI_Bridge_Kit` 的 Text Review；046 不自行实现另一套 artifact transport/reviewer。完整 private/text artifact 因隐私不能提交到公开 repo 时，Reviewer 只能在 Bridge Kit Text Review evidence/locator 落地后消费该 evidence。

如果 Reviewer 无法访问决定 PASS 所需的 artifact，当前语义是 `WAITING_FOR_EVIDENCE / NEEDS_REVIEW`：不得写 `PASS`，不得把 Executor 摘要当作 artifact evidence。若 Executor 能补 repo-safe artifact evidence 或 Bridge Kit Text Review evidence，写 `REVISE` 并指出缺少的 artifact；若 Plan 没有定义可复核 artifact path / Text Review evidence，进入最小 `NEEDS_GPT_PLANNER`；只有证据证明 artifact 永久不可访问且恢复路径不可用时，才按 `BLOCKED`。

如果 task 要求 Visual Review，先机械确认 `VISUAL_REVIEW.json` 存在，且绑定当前 `task_key`、`workflow_type=reviewed_handoff`、`implementation_commit` 和 input image hashes。证据缺失时保持等待，不写 `REVIEW_<round>.md`，不消耗 `review_round`。证据 stale 或 malformed 时不得 PASS。Visual Review 的 `overall_decision` 只是当前 Reviewer 消费的 evidence，不创建 Visual Reviewer role。CI-required visual task 的顺序必须保持为：`WAITING_FOR_CI` -> CI PASS -> `READY_FOR_GPT_REVIEW` -> `waiting_visual_review_evidence` -> fresh visual evidence -> GPT Reviewer。

如果 task 要求 Text Review，先机械确认 `TEXT_REVIEW.json` 存在，且绑定当前 `task_key`、`workflow_type=reviewed_handoff`、`implementation_commit`、text manifest identity 和 plaintext SHA-256。证据缺失时保持等待，不写 `REVIEW_<round>.md`，不消耗 `review_round`。证据 stale、malformed、plaintext SHA mismatch 或 manifest identity mismatch 时不得 PASS。Text Review 的 `overall_decision` 只是当前 Reviewer 消费的 evidence，不创建新的 GPT role。若 Text Review 给出 blocking `REVISE`，Scheduled GPT Reviewer 必须把它作为 frozen requirement failure 进入普通 `REVISE` 路径，不得把明显 failure 推给 human gate；只有达到既有 review round limit 时才走 `REVIEW_LIMIT` human gate。

明显违反 frozen requirement 的 artifact 质量问题必须由 Reviewer 自行阻断，不得推给 `AWAIT_HUMAN_DECISION`：明显违反用户明确规则、明显机器腔、明显 layout failure、明显 artifact regression，都是 `REVISE` 或真实不可恢复时 `BLOCKED` 的依据。Human gate 默认只用于真正互斥的产品/科研选择、frozen criteria 无法决定的主观偏好、用户必须亲自授权的外部动作、显著风险/成本/隐私/许可决定，或 frozen Plan 明确要求的最终人工验收。

044 是本 prompt 的真实回归用例：用户报告 private `rewritten_report.md` 仍有 reader-facing `provenance`、`estimand`、`scientific gap`、`resource contract`、`state of the art` 等表达，违反 frozen writing requirement；Reviewer 未读取完整 artifact 却给 PASS。以后同类 writing/report task 只有读取完整 artifact 并确认这类明显问题已关闭，才允许 product/artifact PASS。

`base_commit..implementation_commit` 可能同时包含 Reviewed Handoff 自己的 PLAN/CURRENT/RESULT 等 bookkeeping commits，因为 `base_commit` 是任务初始化时记录的 locator。不要因为这些合法 workflow 文件本身存在于 diff 就把它们当作产品实现或 regression。实现审核应聚焦冻结 Plan 定义的项目代码、配置、文档和 user-facing artifacts。相反，如果真实 diff 显示 Executor 修改了 `REQUEST.md`、`PLAN.md`、既有 `REVIEW_<n>.md`、`FINAL_REPORT.md` 或 review/plan limit 等 Planner/Reviewer authority，则这是协议违规，应阻断当前 review transaction并要求最小 recovery；不要把可恢复 authority error 自动升级成 terminal BLOCKED。

Review 的唯一目标是判断当前实现是否满足冻结 Plan 且没有造成相关 regression。禁止仅因为“还可以更优雅”“可以再加一个 abstraction”“理论上更安全”而扩大冻结 scope。

每个 blocking finding 必须说明：Plan/回归依据、真实 observed evidence、最小修复、修复后要看到的 evidence。没有冻结 Plan 或已有行为依据的问题只能作为 non-blocking note/backlog。

写 `REVIEW_<round>.md`，decision 只能是 `PASS`、`REVISE` 或 `BLOCKED`。

- `PASS`：只有 process gates 和所有 required product/artifact gates 都满足时才允许。先写 `REVIEW_<round>.md` 和 `FINAL_REPORT.md`，并完成 FINAL_REPORT preflight。若 frozen Plan 明确要求最终人工验收，保持当前 state graph：先把 `CURRENT.state` 设为 `PASS`，再用下一次机械 `CURRENT.json` transaction 进入 `AWAIT_HUMAN_DECISION`，最终写 `human_gate_reason=PASS`、`last_review_decision=PASS`、`state=AWAIT_HUMAN_DECISION`。若没有真实 human gate，Reviewer PASS 后进入 integration closure：执行或触发 task branch integration preflight，确认 required CI PASS、required Reviewer PASS、`main` 无同 shared runtime/source area 竞争性修改、无 merge conflict、无 branch protection blocker、无 release/migration/breaking/high-risk integration blocker，然后默认合回 `main`、push、删除 task branch；默认不要求 PR。不要为了少一次 commit 改坏状态机；Reviewer PASS 前不得自动 merge。
- 第一轮 `REVISE`：先写 `REVIEW_1.md`，最后写 `CURRENT.json`：`review_round=1`、`last_review_decision=REVISE`、`state=REVISE`。本地 task-bound Codex 后续自动启动一次最小 repair。
- 第二轮仍 `REVISE`：先写 `REVIEW_2.md` 和 `FINAL_REPORT.md`，并完成 FINAL_REPORT preflight，最后写 `CURRENT.json`：`review_round=2`、`review_limit_reached=true`、`human_gate_reason=REVIEW_LIMIT`、`state=AWAIT_HUMAN_DECISION`；不得开启第三轮自动返修。
- `BLOCKED`：仅用于证据充分的不可恢复外部 blocker。先证明 waiting、Planner re-entry、用户输入、授权/credential 恢复和 bounded repair 都不能解决；再写 `FINAL_REPORT.md`，说明真实 blocker、已有成果、已检查的恢复路径和恢复方式，完成 FINAL_REPORT preflight，最后写 `CURRENT.json` 进入 `BLOCKED`。

所有终态必须有 `FINAL_REPORT.md`。FINAL_REPORT 面向用户，不是 CI 日志。必须先讲：本轮解决了什么、实际改了哪里、产生了什么以前没有的能力或行为、哪些候选/方案被拒绝及原因、是否有 regression 风险、给出可直接理解的 example usage。技术 appendix 再列 commit、tests/CI 和 remaining limitations。
