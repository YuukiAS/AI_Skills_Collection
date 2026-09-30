# workflow-core 0.5 正常入口与执行路线可靠性 — Critic Prompt v0.1

你现在是 AI Research Stack 的独立 Critic thread。

这是 **workflow-core / Verified Workflow 的设计阶段审查**。  
不要实现代码，不要修改 production plugin，不要创建 execution branch/worktree，不要 bump version，不要启动 paid API，不要改 Longleaf `/users`、STAT5060 或 Bridge Kit runtime。

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `workflow-core`
- design_topic_or_task_key: `workflow-core--normal-entry-reliability`
- source_branch_or_ref: `main`
- review_stage: `DESIGN_REVIEW`
- proposal_path_and_version: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_1_2026-09-30.md`
- proposal_commit: `8342ea716fadba86fa45310c79a34e2251fddf38`
- execution_branch/worktree: `NONE / NOT AUTHORIZED`

## 必须先读取

请从最新 `main` 实际读取：

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
- `skills/core/codex-system/codex-workflow-protocol/references/verification-matrix.md`
- `skills/core/codex-system/codex-workflow-protocol/references/task-template.md`
- `skills/core/codex-system/codex-workflow-protocol/agents/openai.yaml`
- `skills/core/codex-system/codex-workflow-protocol/evals/trigger_queries.json`
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`
- `scripts/codex_marketplace_config.json`
- `docs/PLUGIN_MATURITY.md`
- 本轮 Proposal

并读取与旧能力真实性直接相关的 evidence：

- `results/056_product_delivery_discipline/replay_adjudication/workflow_core_adjudication.md`
- `results/workflow-core--reviewed-first-bootstrap-normal-entry/RESULT.md`
- `results/workflow-core--reviewed-first-bootstrap-normal-entry/FB_GATES.md`

涉及 Bridge ownership / upfront authorization / Reviewed Handoff normal entry 的判断时，再实际读取 `YuukiAS/GPT_Codex_AI_Bridge_Kit` 最新 `main`：

- `AGENTS.md`
- `CHANGELOG.md`
- `docs/design/0.8.1_upfront_authorization_and_persistent_authoring.md`
- `docs/TODO_BOUNDED_REVIEWED_WORKTREE_EXECUTION.md`
- `docs/design/host_policy_plugin_replay_authorization.md`

不要用旧聊天摘要替代上述 source。

## 背景：必须独立核实，不要直接接受 Planner 归因

本轮真实 regression 至少包括：

1. STAT5060 Tutorial 1：workflow-core 已实际加载，但 Codex 只看默认 shell 的 Python / R 状态，就把“当前 PATH/当前环境不可用”解释成“能力不存在”，准备改走 Node/标准库绘图；后来发现 Longleaf 的 `python/3.12.4` 与 `r/4.5.0` module 可用。
2. 同一真实任务后续中文数学 PDF：裸 XeLaTeX 缺 `ctexart.cls` 后，Codex先自行搜索 conda/TeX 并准备 HTML/Chromium fallback；直到用户再次指出，才读取 `render-chinese-math-pdf`，而该 specialist 已明确提供 `render_resources/chinese_math_pdf`、probe 和“不得自动 Chromium fallback”的正式路线。
3. tracking #8：子代理把“不支持 foreground / `visible:true`”误判成“浏览器能力不可用”。
4. tracking #9：旧 task-local prohibition 被错误延续到新的明确目标。

请判断这些是否真的指向同一个可复用 workflow capability，还是 Planner 合并过度。

## 独立外部核查

按 Critic contract 做针对性外部核查，优先 OpenAI 官方文档。至少独立核实：

- Codex / Plugin Skills 的 skill discovery / trigger metadata 如何工作；
- description 是否应保持短而精确，是否存在过度触发/上下文负担风险；
- skill eval 是否应包含 explicit、implicit、contextual、negative-control 等不同入口；
- 对环境假设、失败升级与 specialist routing 的成熟做法是否支持本 Proposal 的方向。

Planner 本轮参考的是：

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- https://developers.openai.com/blog/eval-skills

你必须独立检查关键假设，不要只复述 Planner 引用。

## 需要重点攻击的问题

请不要因为“真实失败发生了两次”就默认 0.5 一定值得做。至少逐项审查：

### C1. 是否真的需要新的 workflow-core release

比较：

- 不改 production，只修项目入口；
- 只修 trigger metadata；
- 只修 specialist routing；
- 只扩 `escalation-rules.md`；
- Planner 提出的 bounded 0.5 batch。

判断哪一个最小方案真正解决根因。若现有 active rule 已足够而只是 consumer 没执行，应要求修消费路径，不允许堆同义规则。

### C2. Trigger recall 与 false-positive 风险

Planner 希望复杂、多阶段、带 environment/resource discovery 和 acceptance/recovery 的任务更稳定触发 workflow-core，同时简单单步任务不触发。

检查：

- 是否会让 workflow-core 变成近似 always-on；
- 是否会抢占真正 specialist；
- `allow_implicit_invocation: true` 已存在的情况下，真正缺的是 metadata、eval，还是别的 normal-entry consumer；
- 是否需要真实 production invocation evidence，而不是字符串断言。

### C3. Specialist-first / capability discovery 是否足够且不过重

Planner 提议：

`current/frozen contract -> matched specialist probe/resource/wrapper -> project-declared environment -> current shell PATH`

并把“command not found / 缺一个 package / optional flag 不支持”限定为局部证据。

检查：

- 这个顺序是否过于机械；
- 是否遗漏合理的项目原生入口；
- 是否会导致大范围主机扫描；
- 是否正确保持 workflow-core 只管 process、不管专业实现；
- 是否需要新增 skill/registry（Planner 主张不需要）。

### C4. Fallback equivalence 的边界

Planner 只允许在效果、质量、证据、安全/隐私边界、artifact identity 都保持等价且已授权时自动换 route。

检查：

- 这个判断是否可执行而不是空泛口号；
- 是否会错误阻止合法恢复；
- 是否能拦住本次 Node/Chromium 类降级；
- 是否保持已有 W2 “least-privilege equivalent recovery”；
- specialist 明确禁止 fallback 时，workflow-core 是否应完全尊重。

### C5. #8 是否适合合并

`foreground/visible flag 不支持 -> 浏览器能力不存在` 与 `PATH 缺工具 -> 能力不存在` 是否属于同一 capability-discovery gate？

如果合并会丢失 browser/subagent/session isolation 的关键语义，应 REVISE；如果通用机制足以覆盖，则不要保留重复浏览器大规则。

### C6. #7 是否仍需要进入 0.5

Bridge Kit 0.8.1 已有 upfront authorization preflight；AI_Skills 也已有部分 Reviewed Handoff / plugin-replay consumer。

判断 workflow-core 还缺的是：

- 一个真正的 generic handoff/user-facing capability；
- 还是只是需要消费 Bridge 已有机制；
- 或者 #7 已经事实上解决，不应再进 0.5。

严禁批准第二套 authorization store/schema/state machine。

### C7. #9 是否应和本次同批

task-local instruction lifetime 与 environment/fallback 不是同一 failure surface。Planner认为它们都属于“先确定当前有效合同/真实能力，再判断 blocker”。

请判断同批是否有足够内聚性，还是应该拆成后续小 refinement，避免 0.5 变成 mega-release。

### C8. #10 是否应该继续独立

Planner主张 acceptance artifact packaging 与本次 root cause 不同，因此不进入 0.5。

请检查这是否会遗漏 W1/W3/W4/W5 的关键正常入口；如果现有 0.3 已经覆盖 generic acceptance admission，则应支持 defer，而不是为了“一次做完”强塞进来。

### C9. #5 / #6 / #11 是否真的可以视为 historical resolved

Planner 的候选判断：

- #5：Bridge `plugin-replay` + AI_Skills Executor 已消费；
- #6：continuous refinement + AGENTS 已明确 real-task-driven/bounded batch；
- #11：Bridge 0.9.0/0.9.1 + workflow-core 0.4 的 bootstrap/resume + FB-G4/G5 已覆盖。

逐项核对真实 source 和 normal-entry evidence。只有证据完整时才允许后续 closure；不要因为 Planner 想缩 scope 就机械同意。

### C10. Capability Gate Matrix 是否能证明真实能力

重点检查 Proposal 的 G1–G5：

- G1 normal-entry + specialist composition
- G2 capability discovery + specialist-first
- G3 fallback + authorization
- G4 active contract scope/lifetime
- G5 broad regression/integration

检查是否重复、缺失、可被 prompt hardcode/fixture trick 钻空子，是否需要真实 production plugin consumption，是否所有 release gates 都绑定同一 final candidate。

若 G2/G3 可合并，说明为什么；若必须拆开，说明它们分别证明什么。

### C11. 版本决策

当前只设计，必须：

`workflow-core = 0.4`，repository 不 bump。

只有最终 production behavior change + 原失败 replay + unrelated regression + release closure 全部成立后，才允许：

`workflow-core 0.4 -> 0.5`

repository 走 PATCH，而不是因为单 plugin enhancement 自动 MINOR。

### C12. Scope 防扩张

本轮明确不负责：

- Longleaf `/users` architecture；
- module / conda / TeX 的机器级配置；
- STAT5060 内容或构建；
- `render-chinese-math-pdf` 的专业规则重写；
- Bridge Kit runtime / Host Policy 新功能；
- 新 workflow / state machine / daemon / watcher；
- acceptance artifact #10 的正式实现。

如果 Proposal 实际无法在这些边界内解决核心问题，应 REVISE，而不是允许 Executor 临场扩大 scope。

## Maintenance Board

Planner 本轮无法合法完成 Project mutation：

- 当前 ChatGPT surface 没有 GitHub Project mutation tool；
- 当前可用 Skills 列表没有 Clear Writing / `writing-style`，不能满足 reader-facing tracking Issue copy 的强制前置条件。

因此 Planner 没有伪称 Project 已同步，也没有要求用户手工维护。

请审查 Proposal 中列出的 pending mutation 是否准确。若本设计 PASS，也不要把 Critic PASS 自动当作 Project Status mutation；下一次 Project-capable + Clear-Writing-capable maintenance action 应机械应用仍然 current 的 pending mutation。

## 输出要求

给出：

`RESULT = PASS` 或 `RESULT = REVISE`

若 REVISE，每个 blocker 必须包含：

- stable finding ID；
- 对应要求；
- 直接证据；
- 因果风险；
- 最小关闭条件；
- owner。

非阻塞建议必须单列，不能用“更保险”阻塞。

如果 PASS：

- 明确 PASS 只批准本 v0.1 的设计方向；
- **不批准实现、branch/worktree、版本 bump、release、Bridge/Longleaf mutation 或付费动作**；
- 下一步应回 Planner，根据通过的设计准备同版本的 Proposal/Plan + Canonical Goal + Kickoff Draft execution package，再送 execution-ready Critic；
- 不要直接让 Codex 开始实现。

若 REVISE，按 Critic contract 自动附上可直接发给 Planner 的完整 prompt。
