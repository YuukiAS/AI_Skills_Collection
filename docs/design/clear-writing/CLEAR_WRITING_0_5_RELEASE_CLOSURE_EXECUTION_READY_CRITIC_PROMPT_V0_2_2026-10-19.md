# Clear Writing 0.5 Release Closure — Execution-ready Critic Prompt v0.2

你现在担任 AI Research Stack 的独立 Critic，审查 Clear Writing 0.5 release closure 的同版 execution package。

本轮不是重新审产品设计，而是确认 approved Plan v0.2 已被忠实、完整、可执行地冻结到 Goal + Kickoff Draft。

## Active Review Context

target_repo:
`YuukiAS/AI_Skills_Collection`

target_plugin_or_domain:
`writing-style / Clear Writing`

design_topic_or_task_key:
`clear-writing--release-closure`

source/evidence branch:
`reviewed/clear-writing--scientific-explanation-readability-repair`

review_stage:
`RELEASE_CLOSURE_EXECUTION_READY_REVIEW_V0_2`

approved Plan:
`docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_PLAN_V0_2_2026-10-19.md@6e321ced9ee14c936c06397ead9862f70312bd40`

Canonical Goal:
`docs/goals/CLEAR_WRITING_0_5_RELEASE_CLOSURE_GOAL_V0_2_2026-10-19.md`

Kickoff Draft:
`docs/operations/prompts/CLEAR_WRITING_0_5_RELEASE_CLOSURE_KICKOFF_V0_2_2026-10-19.md`

execution package commit:
`12a8ccd61778cca9a56df826072618cb06a81632`

frozen production candidate:
`fd7a1578a5042a46a55c5b638f6d550655b1096b`

tracking Issue:
`#13`

## 先读取 latest main

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

然后完整读取同一 package commit 中的：

1. approved Plan v0.2
2. Canonical Goal v0.2
3. Kickoff Draft v0.2

不要执行任何 release、install、upgrade、CI、plugin update 或 repository mutation。

## 已批准且不得重开

- repository `5.5.0 -> 5.5.1` PATCH
- writing-style `0.4 -> 0.5`
- all other central plugins / standalone skills NO_BUMP
- maturity NO CHANGE
- Bridge Kit NO CHANGE
- frozen candidate `fd7a157...`
- final 4-answer Web Gate PASS
- W2 不再是 release blocker
- release isolation 从 execution-time formal `origin/release` 构建
- baseline/version drift -> stop + Planner late-bind
- 不 wholesale merge/cherry-pick old evidence branch
- generated layer 只经 canonical generator
- profile exact six-skill exposure
- exact committed clean candidate
- fresh install + formal upgrade smoke
- final deterministic/full/CI checks
- final-candidate independent Critic before release ref
- canonical fast-forward-only formal release producer
- formal release 后 update existing PRIVATE plugin
- plugin_id 保持 `plugins_6ad4fc9abae08191a9ecd81879b2c919`
- Web 0.5.0 / USER / PRIVATE
- full payload readback parity
- truthful formal release 不因 PRIVATE plugin update failure 回滚
- PRIVATE parity 后再 reintegrate exact released commit 到 then-latest main
- Issue #13 formal release 与 DONE 分离
- downstream adaptation 不在本 task 实施

## 1. Plan -> Goal 忠实度

确认 Goal 没有扩大、缩小或改写 approved Plan 的实质语义。

重点检查：

- version decision 完全一致；
- baseline preflight 与 late-bind stop rule 一致；
- release isolation 一致；
- product allowlist 与 frozen candidate authority 一致；
- `codex-writing-style` exact six-skill profile 一致；
- Product UI Copy 只 profile exposure，不改 runtime；
- README Clear Writing real invocation requirement 没被弱化；
- install/upgrade smoke + final CI 完整；
- no Web Gate rerun；
- final-candidate Critic 在 release ref 前；
- PRIVATE plugin parity 与 main reintegration 顺序正确；
- Issue #13 ADAPTING/DONE truth boundary 正确。

若 Goal 引入未批准 product/release scope，应 REVISE。

## 2. Kickoff 是否可直接执行 Stage A

Kickoff 必须让 Codex 在收到用户批准的短 handoff 后，不再需要新的 Planner 设计或用户产品选择，就能直接开始 Stage A。

检查 exact execution location：

- execution branch：
  `reviewed/clear-writing--release-closure`
- task-owned worktree：
  `/tmp/ai-skills-clear-writing-release-closure`

确认：

- 只有 baseline preflight PASS 后才创建/复用；
- existing branch/worktree 不满足 task identity + exact baseline + clean 时 fail closed；
- 不把 source/evidence branch 当 execution branch；
- ordinary non-force push execution branch 合法；
- 不 force/reset unrelated work。

## 3. Stage A candidate construction scope

确认 Kickoff 只允许：

- response-clarity source
- frozen chinese-prose routing delta
- approved writing-style Marketplace exposure/description/defaultPrompt
- exact frozen six-skill profile
- directly related tests
- version/README/changelog/generated release metadata

确认禁止：

- wholesale old branch merge
- W2/control evidence 进入 production
- Product UI Copy runtime modification
- other plugin production behavior
- other version bumps

## 4. Generated / README / version closure

确认：

- generated files不能手改；
- canonical generator 必须真实运行；
- repository `5.5.1` / writing-style `0.5` version surfaces一致；
- README 修改后必须真实调用 installed Clear Writing；
- runtime 没有真实 Clear Writing invocation 时 Stage A 停止，而不是靠读 Skill 伪造；
- changelog profile wording不会把 Product UI Copy exposure冒充新产品行为。

## 5. Exact candidate + install/upgrade smoke

确认所有 release-critical evidence 绑定同一：

- committed
- clean
- exact SHA

确认 candidate 修改后旧 smoke/test/CI 全失效。

Fresh install 必须回读：

- repository 5.5.1
- writing-style 0.5
- response-clarity installed
- exact six-skill profile
- unrelated plugin/standalone versions无 drift

Formal upgrade 必须：

- 从 formal `5.5.0 / writing-style 0.4`
- 使用仓库正式 upgrade path
- 到 exact candidate `5.5.1 / 0.5`
- 不得直接覆盖文件
- 回读同一 identity

确认这仍只是 mechanical release smoke，不是新 Web/product Gate。

## 6. Final deterministic/CI checks

同一 exact SHA 必须执行：

- writing-style focused tests
- source/generated parity
- Marketplace/version/changelog/README consistency
- profile/install identity validation
- full repository test suite
- skill validation
- required GitHub CI

确认：

- FAIL 不得删测试/改 rubric；
- 4-answer Web Gate 不重跑；
- candidate 变更后旧 evidence 不复用。

## 7. Mid-run final-candidate independent Critic gate

检查 Kickoff 的两阶段设计是否合法：

### Stage A

构建 exact candidate、跑 RC1–RC5、生成 evidence，然后：

`READY_FOR_FINAL_CANDIDATE_CRITIC`

并停止一切正式分发副作用。

此时不得：

- advance release
- update PRIVATE plugin
- merge main
- mark Issue #13 DONE

### Stage B

只有同一 exact candidate 获得独立 final-candidate Critic PASS 后才恢复。

恢复时再次检查 `origin/release` baseline；如已移动，回 Planner late-bind。

请判断这个中间人审不会造成未决产品/权限问题：Stage A 已经可以直接执行；Stage B 的行为、权限和 stop rules 已在同一 approved package 中冻结，只等待未来 exact-candidate Critic verdict。

若正确，不应要求另开新的 release-closure 设计 round。

## 8. Stage B formal release 与 PRIVATE plugin

确认：

- canonical `ai-skills-repository-maintainer`
- non-force / fast-forward-only `release`
- target exact approved candidate
- remote SHA/version readback

随后只更新 existing PRIVATE plugin：

`plugins_6ad4fc9abae08191a9ecd81879b2c919`

要求：

- version `0.5.0`
- USER
- PRIVATE
- plugin_id unchanged
- new current_release_id recorded
- six Skills + references/assets/evals + scientific-rewrite script + metadata readback
- formal generated payload parity

确认：

- Codex 无 Plugin Creator surface 时，`PRIVATE_PLUGIN_UPDATE_HANDOFF_REQUIRED` 是合法 fail-closed handoff，而不是自行创建第二 plugin；
- formal release 已真实成功时，PRIVATE update failure 不应回滚 formal release；
- issue remains open until parity/closure truth supports next lifecycle。

## 9. Main reintegration

确认只有 PRIVATE parity PASS 后才：

- fetch then-latest main
- ordinary non-force integrate exact released commit
- preserve unrelated main work
- conflicts only within approved Clear Writing/release metadata surface
- unrelated plugin behavior conflict -> stop Planner
- released commit becomes main ancestor
- focused integration validation
- ordinary non-force push main

## 10. Issue #13 lifecycle

确认：

- formal 0.5 PASS != Issue #13 DONE
- canonical promotion gate + downstream truth 决定 DONE
- downstream required -> `ADAPTING`
- no downstream implementation in this task
- Issue reader-facing copy mutation requires real installed Clear Writing
- Clear Writing unavailable -> no reader-facing mutation
- no Project mutation surface -> exact pending mutation, no user manual bookkeeping

## 11. Authorization envelope

检查 Kickoff 是否只授权：

Stage A：
- repo read/write within approved release scope
- task branch/worktree
- commit
- ordinary non-force execution-branch push
- generator/tests/install/upgrade smoke/required CI

Stage B（only after future exact-candidate Critic PASS）：
- canonical fast-forward-only release advancement
- existing PRIVATE plugin update
- ordinary non-force main reintegration
- truthful Issue/source lifecycle updates

明确禁止：

- force
- destructive unrelated reset
- second plugin
- uninstall/delete
- PUBLIC/UNLISTED
- unrelated plugin changes/version bumps
- maturity changes
- W2/Web Gate
- new writing rules/Skill/router/state machine
- downstream plugin implementation

若 authorization 过宽或有危险动作未冻结，REVISE。

## 12. Execution-ready 判定

只有在 Plan + Goal + Kickoff 三者同版一致，且 Stage A 可以在收到用户短 handoff 后直接开始时，才给 execution-ready PASS。

本 PASS 不等于 final-candidate PASS，也不等于 formal release 已授权立即推进；Stage A 必须先运行并在中间 Critic gate 停止。

## 输出

给 `PASS` 或 `REVISE`。

若 `REVISE`：

- 只列 execution-readiness blocker；
- 使用稳定 finding ID；
- 不重开产品设计；
- 自动生成给 Planner 的完整最小返修 prompt。

若 `PASS`：

按最新 Critic Role Contract 输出：

```text
DECISION=PASS
APPROVED_PLAN_PATH=docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_PLAN_V0_2_2026-10-19.md
APPROVED_GOAL_PATH=docs/goals/CLEAR_WRITING_0_5_RELEASE_CLOSURE_GOAL_V0_2_2026-10-19.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/CLEAR_WRITING_0_5_RELEASE_CLOSURE_KICKOFF_V0_2_2026-10-19.md
APPROVED_PACKAGE_COMMIT=12a8ccd61778cca9a56df826072618cb06a81632
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

并生成一个**简短、可直接发送给 Codex 的 Stage A handoff**，不要全文重贴 Kickoff Draft。

该短 handoff 至少包含：

- task `clear-writing--release-closure`
- approved Plan/Goal/Kickoff locators + package commit
- execution branch `reviewed/clear-writing--release-closure`
- worktree `/tmp/ai-skills-clear-writing-release-closure`
- 用户授权 Codex 执行 Stage A：baseline preflight、构建 isolated candidate、approved release metadata、generator、fresh install、formal upgrade、tests/CI、evidence
- 明确 stop at `READY_FOR_FINAL_CANDIDATE_CRITIC`
- 不推进 release、不更新 PRIVATE plugin、不 merge main

不要把 `DRAFT / NOT AUTHORIZED`、审查历史、完整 Plan/Kickoff 或内部 blocker 文本复制进用户短 handoff。

本 execution-ready PASS 不允许绕过 Stage A 之后的 independent final-candidate Critic gate。
