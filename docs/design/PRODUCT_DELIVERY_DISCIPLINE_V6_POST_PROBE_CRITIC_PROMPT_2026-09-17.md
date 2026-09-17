你是 AI Research Stack 的长期独立 Critic thread。

继续任务：

`TASK_KEY = 056_product_delivery_discipline`

上一轮你已对 `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md` 给出架构 `PASS`，并允许先执行 bounded persistent-user-input capability probe；同时明确 probe 结果会决定 W2 transport，因此当时不能冻结 implementation Plan。

probe 已完成。Planner 没有重开 v7，也没有增加新的顶级 capability，而是提交一个 post-probe addendum，请你做**短的 post-probe review**。

本轮 review object：

- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- supporting result: `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`
- supporting new real-project feedback: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`
- architecture authority remains: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`

这不是 implementation review。不要修改 production skill/plugin、Bridge Kit config/source、项目 AGENTS，不启动 Executor，不创建 Goal/Kickoff/branch，不运行 paid API。

## 1. 必须重新读取

先读取最新 main：

- `AGENTS.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_REVIEW_PACKAGE.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`
- `docs/plugin-todos/workflow-core.md`
- `docs/plugin-todos/web-development.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/references/task-template.md`
- `skills/core/codex-system/codex-workflow-protocol/references/verification-matrix.md`

并重新读取 Bridge Kit current main 中与 host config / user input 直接相关的：

- `templates/host/GLOBAL_AGENTS_SNIPPET.md`
- `templates/host/CODEX_CONFIG_PROFILE.md`
- `ai_bridge_kit/host.py`
- `tests/test_host_policy.py`

## 2. 必须独立核查当前 upstream

独立读取当前 `openai/codex` source / issues，不只接受 Planner 的摘要。至少核查：

- `codex-rs/core/src/tools/handlers/request_user_input.rs`
- `codex-rs/collaboration-mode-templates/templates/default.md`
- `codex-rs/features/src/lib.rs`
- `codex-rs/core/config.schema.json`
- `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs`
- PR `#36410`
- issues `#43759`, `#37472`, `#34455`, `#29702`, `#28969`

重点回答：当前是否真的存在受支持的 `config.toml` / app setting 能让 **Default mode** 的 native `request_user_input` indefinite blocking；如果没有，Planner 的 transcript fallback 是否是当前最小充分路线。

## 3. 审 persistent transport decision

probe 的关键事实是：

```text
Default mode
feature enabled
tool available
114s auto-resolve
empty/default answer returned
native persistent FAIL
durable transcript fallback resume PASS
```

审查 Planner 建议：

1. W2 使用 `DURABLE_TRANSCRIPT_WAIT_RESUME`，不再声称 native persistent prompt；
2. required HUMAN_ONLY gate 用 plain-text visible question + resume point + dependent execution suspend；
3. 用户未回复不继续、不 polling、不 terminal BLOCKED；
4. same-thread明确回复后 exact-once resume；
5. implementation 时优先考虑 Bridge Kit managed config：

```toml
[features]
default_mode_request_user_input = false
```

从 Default mode 移除会 auto-resolve 的 optional-question tool，以 fail-closed 方式降低 HUMAN_ONLY gate 被误用的概率；Plan mode 保持 upstream native behavior。

请攻击两个方向：

- **过简**：plain-text fallback 是否仍可能被 agent写出来后继续执行、丢失 resume point、或下一 turn 重开任务？需要什么最小 gate 才可靠？
- **过重/副作用**：关闭 `default_mode_request_user_input` 是否会破坏合法 Default-mode optional clarification；是否不值得改 config，只靠 workflow rule 已足够？

如果你认为 flag 应保持 true，请说明怎样用真实 normal-entry gate 防止 HUMAN_ONLY 被 non-blocking tool 吞掉，而不是只写“不要误用”。

不要建议 watcher、polling daemon、Persistent Run/tmux、Control、ledger、新状态机或维护 Codex fork，除非有新直接证据证明没有更小路线。

## 4. 审最新 Bridge Kit/source-discovery 反馈

最新真实失败：已有本机 repo/clone 可复用，但 Executor 因 unrelated dirty `.gitignore` 绕去 `/tmp` clone，再试图 remap remote，浪费时间并触发授权拦截。

Planner 把它归入 **已有 Source Discovery / dirty-tree protection 的 enforcement refinement**，不新增 W6/Lite rule。

请判断下面机制是否最小充分：

- 先定位 existing canonical checkout/worktree/clone；
- 核 branch/ref/origin/dirty state；
- unrelated dirty work 要保护，但 dirty 本身不能成为默认另起 clone 的理由；
- isolation 优先从 canonical local repo 建 clean worktree，或复用已经存在的正确 clone；
- 没有可用 local source 才 network clone；
- 不用 local-clone -> remote-remap 制造额外 provenance/授权风险；
- remote mutation 仍需独立授权。

重点检查这是否应该留在 existing source discovery，而不是塞进 Lite/Bridge Kit。

## 5. 审 CUHK Date 新证据

独立审 `PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`。

Planner 不新增 capability，只映射：

```text
representative breadth / branch / state lifecycle / fallback != primary -> W1
real hosted provider / interaction sequence -> W3
protect accepted structured interaction -> W5
localization completeness / surface convergence -> Frontend F-B/F-C
```

请判断：

- 是否足以阻止 demo catalog 冒充完整 catalog；
- mock provider tests 是否不会再冒充 hosted provider；
- final-value schema 是否不会再冒充真实 keystroke sequence；
- material branch 是否有代表性 replay；
- raw enum token 是否能在多 locale claim 下 deterministically fail；
- fallback 是否只证明 recoverability；
- backend capability存在但 hosted config 未消费时是否不能 acceptance-ready；
- rewrite 是否保护已有高质量 interaction；
- 同时 docs/server/small task 是否不会被这些矩阵拖进重流程。

如果这些需要新 W6/W7 才成立，给直接因果证据；否则优先保持 v6 小架构。

## 6. 结论

这轮只判断 post-probe implementation direction 是否可以进入 **Implementation Plan drafting**，不是批准执行。

最终给：

```text
RESULT = PASS | REVISE
TASK_KEY = 056_product_delivery_discipline
REVIEW_OBJECT = docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md
V6_ARCHITECTURE_STILL_VALID = YES | NO
W2_TRANSPORT = DURABLE_TRANSCRIPT_WAIT_RESUME | NATIVE | REVISE
DEFAULT_MODE_REQUEST_USER_INPUT_FLAG = DISABLE | KEEP | REVISE
SOURCE_DISCOVERY_REFINEMENT = PASS | REVISE
CUHK_DATE_REFINEMENTS = PASS | REVISE
READY_FOR_IMPLEMENTATION_PLAN_DRAFT = YES | NO
```

`READY_FOR_IMPLEMENTATION_PLAN_DRAFT=YES` 只允许 Planner 下一步起草完整 Plan + Goal + Kickoff，并再次按 Critic contract 审 execution-ready package；不授权任何 production 修改。

如果 `REVISE`，自动附完整 Planner 返修 prompt。
