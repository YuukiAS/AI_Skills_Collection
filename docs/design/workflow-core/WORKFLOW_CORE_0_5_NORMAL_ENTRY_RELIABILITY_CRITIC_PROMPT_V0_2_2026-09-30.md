# workflow-core 0.5 正常入口与执行路线可靠性 — Critic Re-review Prompt v0.2

你继续作为 AI Research Stack 的独立 Critic thread，对 `workflow-core / Verified Workflow 0.5` 的设计返修做复核。

这是 **DESIGN_REVIEW / RE-REVIEW**。  
不要实现代码，不要修改 production plugin，不要创建 execution branch/worktree，不要 bump version，不要启动 paid API，也不要修改 Longleaf `/users`、STAT5060、render specialist 或 Bridge Kit runtime。

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `workflow-core`
- design_topic_or_task_key: `workflow-core--normal-entry-reliability`
- source_branch_or_ref: `main`
- review_stage: `DESIGN_REVIEW_R2`
- reviewed proposal v0.1: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_1_2026-09-30.md`
- reviewed proposal v0.1 commit: `8342ea716fadba86fa45310c79a34e2251fddf38`
- revised proposal v0.2: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_2_2026-09-30.md`
- revised proposal v0.2 commit: `8575e86fce56d0c44c484477f578e90b65750c5c`
- previous critic prompt: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_CRITIC_PROMPT_V0_1_2026-09-30.md`
- previous critic prompt commit: `7e42dc3483185c204377e75066da88774c0c3bc9`
- previous Critic result: `REVISE`
- previous Critic review repo path/commit: `NONE`
- execution branch/worktree: `NONE / NOT AUTHORIZED`

## 先读取最新 source

按当前 Critic Role Contract，先实际读取最新 `main` 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/plugin-todos/workflow-core.md`
- `docs/plugin-changelogs/workflow-core.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/references/escalation-rules.md`
- `skills/core/codex-system/codex-workflow-protocol/agents/openai.yaml`
- `skills/core/codex-system/codex-workflow-protocol/evals/trigger_queries.json`
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`
- V0.1 Proposal
- V0.2 Proposal

并复核直接 evidence：

- `results/056_product_delivery_discipline/replay_adjudication/workflow_core_adjudication.md`
- `results/workflow-core--reviewed-first-bootstrap-normal-entry/RESULT.md`
- `results/workflow-core--reviewed-first-bootstrap-normal-entry/FB_GATES.md`
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`

凡涉及 Bridge ownership / authorization / Reviewed Handoff closure，读取 `YuukiAS/GPT_Codex_AI_Bridge_Kit` 最新 `main` 的：

- `AGENTS.md`
- `CHANGELOG.md`
- `docs/design/0.8.1_upfront_authorization_and_persistent_authoring.md`
- `docs/TODO_BOUNDED_REVIEWED_WORKTREE_EXECUTION.md`
- `docs/design/host_policy_plugin_replay_authorization.md`

## 本轮优先复核原 blockers

不要重新设计整个插件。先逐项复核上一轮稳定 finding 是否已经关闭；只有新事实、遗漏的关键风险或 V0.2 引入的真实回归才能新增 blocker。

### WC05-D1

V0.2 已加入“复杂但 specialist-contained”的 hard negative，并要求 final candidate 的真实 invocation trace 同时证明正例和相邻负例。

请判断：

- hard negative 是否真的足以防 workflow-core 近似 always-on；
- 是否仍会因为“多步骤/有 render/有 QA”而误触发；
- description/metadata 方向是否保持短而精确；
- 是否明确要求真实 implicit consumption，而非 source/metadata proxy。

### WC05-D2

V0.2 不再整体 merge #8。

只复用：

`unsupported foreground/visible flag != capability absent`

#8 的 anonymous-page、pre/post-auth、credential/persona、parent/subagent/session isolation 继续独立 tracking。

请判断边界是否足够清楚，0.5 PASS 是否不会错误关闭 #8。

### WC05-D3

V0.2 已把 #7 完全移出 0.5 production behavior。

authorization 只作为 fallback equivalence 的一个当前事实维度；不新增 kickoff、authorization lifecycle/store/schema/state/Host Policy。

请判断这是否正确消费 Bridge 0.8.1+ ownership，而没有偷偷复制第二套 authorization 机制。

### WC05-D4

V0.2 已把 #9 完全拆出。

请确认 0.5 不再修改 task-local instruction lifetime，也没有在别处用同义规则重新引入。

### WC05-D5

V0.2 新增 G4：

```text
普通未点名 skill prompt
-> workflow-core 实际 implicit consumption
-> specialist 实际 consumption
-> targeted capability discovery
-> 正确 route
-> no non-equivalent fallback
```

positive chain 必须是同一个 final-candidate run，不能拼证据。

同时增加真正 capability-absent contrast：canonical task route、specialist route、project-declared environment route 都不存在时，必须精确 fail closed、不扫无关主机、不发明低质替代。

请判断 G4 是否真正关闭“各 gate 分别 PASS 但 normal entry 仍失败”的漏洞。

### WC05-D6

V0.2 把 automatic fallback 写成六项全满足：

1. frozen effect；
2. professional quality；
3. acceptance evidence strength；
4. safety/privacy；
5. artifact identity；
6. current authorization scope。

任一 UNKNOWN/CHANGED 都不得 automatic fallback。

请判断：

- 六项是否可观察、可执行；
- 是否能拦住 Node/Chromium 类降级；
- 是否仍允许已有 W2 的真正 lower-privilege equivalent recovery；
- 是否需要新增机制才能执行；若不需要，不要要求新 schema/registry。

## Tracking disposition 复核

V0.2 按上一轮 finding 明确冻结：

- 主 environment/specialist/fallback 问题：本轮主问题；
- #5：AI_Skills 层 historical resolved；
- #6：historical resolved；
- #7：不进入本轮，Bridge-owned/current-authority semantics 覆盖原始 evidence；
- #8：独立，只借一个 generic regression；
- #9：独立；
- #10：独立；
- #11：workflow-core consumer 层 historical resolved，依据 Bridge 0.9.1 + workflow-core 0.4 + FB-G4/G5。

请核对 #5/#6/#11 的 source/evidence 是否足以支持 product-level historical-resolved disposition。

注意：当前没有合法 Project mutation surface，也没有可调用的 Clear Writing，因此 V0.2 只记录 pending Board mutation，没有关闭 Issue、没有设置 DONE、没有猜 Resolution commit。请检查 pending mutation 是否符合 Board policy。

## Capability Gate Matrix 复核

重点审 G1–G5：

- G1 Trigger precision + complex specialist-contained hard negative；
- G2 Specialist-first targeted capability discovery；
- G3 Fail-closed six-dimension fallback equivalence；
- G4 inseparable final-candidate normal-entry replay + true-absent contrast；
- G5 broad should-not-change / integration regression。

检查：

- 是否有高度重复 gate；
- G4 是否真正不可由 G1–G3 拼接替代；
- 是否仍缺真实 production consumption；
- hard negative / absent contrast 是否会被 task-specific hardcode 钻空子；
- 是否保持 simple/specialist-only route；
- 所有 release gate 是否绑定同一个 final candidate。

## 外部核查

按 Critic contract 独立核对 OpenAI 官方 Skills/plugin guidance，特别检查：

- name/description 如何参与 discovery；
- description/metadata 如何兼顾 recall 和 false-positive；
- direct / implicit / contextual / negative-control eval；
- skill instructions 与 supporting files 的 progressive disclosure。

Planner V0.2 使用的官方来源：

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/guides/optimize-metadata
- https://developers.openai.com/blog/eval-skills
- https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra

不要仅复述 Planner 结论。

## Scope / version boundary

本轮明确不允许扩到：

- Longleaf `/users` / module / conda / TeX architecture；
- STAT5060 source；
- render specialist rewrite；
- Bridge runtime / Host Policy；
- #7/#8/#9/#10 专属 production logic；
- 新 workflow/state/schema/watcher/daemon；
- paid API。

设计阶段继续：

```text
workflow-core = 0.4 / NO_BUMP
repository = NONE
execution branch/worktree = NONE
```

未来只有同一个 final candidate 通过真实 normal-entry consumption、原 failure replay、hard negative、true-absent fail-closed、broad regression 和 release closure，才允许 `workflow-core 0.4 -> 0.5`；repository 仅 PATCH。

## 输出要求

给出：

`RESULT = PASS` 或 `RESULT = REVISE`

若 REVISE：

- 优先复核 WC05-D1–D6；
- 每个 blocker 给稳定 finding ID、直接证据、因果风险、最小关闭条件、owner；
- 非阻塞建议单列；
- 按 Critic Role Contract 自动附下一条完整 Planner prompt。

若 PASS：

- 明确 WC05-D1–D6 分别如何关闭；
- PASS 只批准 V0.2 **设计方向**；
- 不批准实现、branch/worktree、version bump、release、Bridge/Longleaf mutation 或 paid action；
- 下一步回 Planner，准备同一批准设计的完整 Proposal/Plan + Canonical Goal + Kickoff Draft execution package，再送 execution-ready Critic；
- 不要直接启动 Codex implementation。
