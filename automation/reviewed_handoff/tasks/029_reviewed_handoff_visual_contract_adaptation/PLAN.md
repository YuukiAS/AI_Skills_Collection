---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 029_reviewed_handoff_visual_contract_adaptation
decision: PLAN_FROZEN
---

# 029 Reviewed Handoff Visual Contract Consumer Adaptation — Plan

## Frozen decisions

029 是 control-plane consumer adaptation，不是新的 Presentation quality stage，也不属于 027 的第三轮返修。它只把 AI_Skills_Collection 现有 GitHub Visual Review workflow 接到 Bridge Kit 已经发布的 task-local Reviewed Handoff visual contract 上。

不得改变 Reviewed Handoff 角色模型、状态机、review 次数、Planner/Executor authority、Terra 判定语义或 Presentation mature bar。不得通过新增 repository-level 固定 manifest/output vars 继续维持单任务假设。

当前 Bridge Kit 已有合同：视觉型 task 可在 `CURRENT.json` 声明 `visual_review_required=true`、`visual_review_manifest_path` 与 `visual_review_evidence_path`；当 task 已发布真实输入但 evidence 尚未写回时，属于 `waiting_visual_review_evidence`，不消耗 review round，也不是 BLOCKED。029 只让当前 consumer workflow 真正尊重这一合同。

## Objective and value

解决 027/028 已证实的真实问题：AI_Skills_Collection 当前 Visual Review workflow 在普通 push 下没有 task-local manifest/output 输入，会显示 workflow success 但 live review 实际 skip。改造后，视觉型 task 的发布、GitHub visual review 与 evidence writeback 应形成零人工 dispatch 的正常路径。

## Implementation scope

### 1. Add deterministic task-local visual target resolution

实现一个小型、可测试的 consumer-side resolver（优先放在现有 `scripts/` 或其他普通项目脚本位置，不修改 Bridge Kit package 本身），在 repository checkout 后读取：

- `automation/reviewed_handoff/tasks/*/CURRENT.json`
- 每个候选 task 的 `visual_review_required`
- `visual_review_manifest_path`
- `visual_review_evidence_path`
- state / implementation commit
- task-local manifest/evidence freshness

resolver 只允许把以下 task 视为 push-mode live review 候选：

- `visual_review_required=true`；
- 当前已处于外部视觉证据应接管的合法阶段，至少支持 Bridge Kit 当前 contract 的 `READY_FOR_GPT_REVIEW` + pending evidence；
- manifest 路径为 repository-relative，文件真实存在且可解析；
- manifest 的 `task_key`、`workflow_type=reviewed_handoff` 与 `identity_bindings.implementation_commit` 跟 CURRENT 一致；
- 当前 evidence 不存在或不是与该 manifest/implementation 对应的 fresh evidence。

结果必须是三态：

1. **0 个 eligible task**：正常 no-op，不运行 Terra；
2. **恰好 1 个 eligible task**：输出该 task 的 manifest/output path 给 workflow；
3. **>1 个 eligible task 或候选 manifest 非法/身份冲突**：fail closed，给出明确错误，不猜 task、不任选第一个。

不得引入新的 tracked workflow state、receipt、hash graph 或 persistent task registry。

### 2. Wire push-mode GitHub Actions to the resolver

修改 `.github/workflows/ai-bridge-visual-review.yml`，保留现有手工 `workflow_dispatch` 作为调试/恢复入口，但普通 push 不再依赖 `vars.AI_BRIDGE_VISUAL_REVIEW_MANIFEST` / `vars.AI_BRIDGE_VISUAL_REVIEW_OUTPUT` 才能知道当前 task。

push path 应在安装当前 Bridge Kit visual-review extra 后运行 resolver：

- 0 eligible task：workflow 明确记录 no task-local visual review pending，并正常结束；
- 1 eligible task：把 resolver 输出的 manifest/output path 注入后续 `ai-bridge visual-review run`；
- resolver fail closed：job 明确失败，不把 skip 当 success。

`workflow_dispatch` 的显式 inputs 仍具有最高优先级，不被自动 resolver 覆盖。

### 3. Use a current Bridge Kit revision compatible with the contract

当前 workflow pin 仍指向旧 Bridge Kit commit。029 应将 GitHub Actions 使用的 Bridge Kit visual-review extra 固定到当前已验证包含 task-local Reviewed Handoff visual contract 的稳定 revision（至少不早于 `79c1a36defb725a0b66973eb04a222839d7ad09a`，优先使用当前 main 已验证的 `647f63c49ccea828a0ac76a6e9adce026531c906` 或执行时更新后的等价稳定 revision），不得使用浮动未验证分支。

这只是 consumer dependency pin 更新，不允许顺便把 Bridge Kit 其他新功能 wholesale adapt 进 AI_Skills_Collection。

### 4. Deterministic regression coverage

增加最小回归，至少覆盖：

- 无 visual-review task -> resolver no-op；
- 单一合法 pending task -> 返回正确 task-local manifest/evidence path；
- evidence 已 fresh -> no-op，不重复审同一 identity；
- manifest task key / implementation commit 不匹配 -> fail closed；
- 两个同时 eligible task -> fail closed，不随机选择；
- workflow_dispatch 显式输入继续可用；
- 普通 push 不再因为 repository-level vars 为空而静默 skip 唯一合法 task-local review。

测试可以使用 synthetic JSON/PNG fixture，不需要真实调用 Terra，也不新增 API 成本。

### 5. Validation and handoff

至少运行：

- resolver targeted tests；
- Reviewed Handoff relevant tests（如 consumer repo 有对应测试）；
- `python -m unittest discover -s tests`；
- `python scripts/skills.py validate`；
- marketplace validate/check/path-report；
- Reviewed Handoff repository validation；
- workflow syntax / deterministic helper validation；
- `git diff --check`。

`ci_required=true`。Executor 只完成 consumer adaptation 和本地验证，按标准 Reviewed Handoff 交给 watcher 发布并等待真实 CI；029 本身不要求 Terra visual review。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 029：

1. push-mode workflow 能从 tracked task-local Reviewed Handoff CURRENT/manifest 自动解析唯一 pending visual-review target；
2. 不再依赖 repository-level 固定 vars 才能处理普通视觉 task；
3. 0 task no-op、1 task执行、>1 task或非法 identity fail closed 的行为有确定性回归；
4. evidence fresh 时不会重复调用同一 visual identity；
5. explicit `workflow_dispatch` 仍可用于人工恢复且不被破坏；
6. workflow 使用支持当前 task-local contract 的稳定 Bridge Kit pin；
7. 没有修改 Reviewed Handoff 状态机/角色 authority/review budget；
8. 没有修改 Presentation 027 页面、gold library、CUHK layout 或 Terra reviewer semantics；
9. required tests / validation / real CI 全部通过；
10. RESULT 说明 consumer contract、0/1/many 行为与 remaining limitations。

029 PASS 后，Planner 才创建下一项 bounded Stage 3 visual-maturity recovery，并在其 CURRENT 中真实启用 `visual_review_required` 与 task-local manifest/evidence path。

## Natural-language usage / routing expectations

正常用户不需要感知 029。后续一个视觉型 Reviewed Handoff task 只需要由 Planner 冻结 visual contract，Codex 生成真实 render 和 task-local `visual_inputs.json`；watcher 发布后，GitHub Actions 自动找到该唯一待审 task并写回 `VISUAL_REVIEW.json`。用户不应再因为“push workflow 成功但 Terra 实际 skip”而手工运行 `gh workflow run`。

## Stop condition

以下全部成立即停止，不继续扩控制面：

- task-local push discovery 可工作；
- 0/1/many/invalid/fresh-evidence regression 全部覆盖；
- manual dispatch 保留；
- real CI PASS。

随后交回 Planner，不开始 Stage 3 页面返修。

## Out of scope

029 不得：

- 修改 027/028 历史 REVIEW/CURRENT/FINAL_REPORT；
- 修改任何 Stage 3 页面、renderer、layout primitive、gold composition、canonical CUHK theme；
- 修复 slide 3/4/6/7 的视觉 blocker；
- 创建新的 Reviewed Handoff state、role、receipt 或 semantic hash graph；
- 修改 Terra 核心模型调用或质量 rubric；
- 修改 GitHub secret 内容；
- 开始 Stage 4 one-call production entry 或 Stage 5 holdout；
- 宣告 Stage 3 PASS 或 `PROGRAM_MATURE`。
