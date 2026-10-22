# Codex Instructions for GPT-Codex AI Bridge Kit

本文件是维护本仓库时必须先读的紧凑入口。面向用户的当前能力与安装路径以
`README.md` 为准；状态机、角色、证据和安全合同必须读取下列正式来源，不要把
它们从记忆或本文件的摘要反向扩写成第二套规范。

## 1. owner、层级与正式来源

Bridge runtime、Host、Lite、Review、Control、Persistent Run、Overleaf 与
Notifier 的实现 authority 属于本仓库。正式 distribution/version closure（包括
移动 `release` ref）属于 `YuukiAS/AI_Skills_Collection` 的
`ai-skills-core:bridge-kit-maintainer`；本仓库不复制 release engine，也不能在该
owner 完成闭环前声称 distribution-complete。

能力层级固定为：

- 机器层：Host Policy，每个 `CODEX_HOME` 单独安装；
- 项目层：Lite 默认，可选 Review、Control、Persistent Run、Overleaf、Notifier；
- 任务层：Lite/Review/Control 的运行实例，不是新的安装层。

正式来源 locator：

- Review：`docs/V0_5_REVIEWED_HANDOFF_IMPLEMENTATION_SPEC.md`；
- Control：`docs/V0_4_AGENT_FLOW_IMPLEMENTATION_SPEC.md`、
  `docs/AGENT_FLOW_V3_POST_CARE_EXTRACTION_DECISIONS.md`、
  `docs/CARE_AGENT_FLOW_V3_POSTMORTEM_20260811.md`；
- Persistent Run：`docs/design/0.8.0_persistent_run.md` 与
  `templates/persistent_run/`；
- Overleaf：`docs/V0_6_OVERLEAF_BRIDGE_IMPLEMENTATION_SPEC.md` 与
  `templates/overleaf/`；
- Host/Machine Policy：`templates/host/GLOBAL_AGENTS_SNIPPET.md`、
  `templates/host/rules/ai-bridge-global.rules`、
  `templates/host/CODEX_CONFIG_PROFILE.md`；
- Lite/task：`codex/AGENTS_SNIPPET.md`、`templates/prompts/`；
- 当前 0.11 收口：
  `docs/design/0.11.0_integrated_product_architecture_v6_2026-10-20.md`、
  `docs/design/0.11.0_execution_plan_v6_2026-10-20.md`、
  `docs/design/0.11.0_codex_goal_v6_2026-10-20.md`、
  `docs/design/0.11.0_kickoff_v6_2026-10-20.md`；更早的 Product Scope Reset 与
  Final Scope Recovery 只作历史证据。

修改实现前先按实际 workflow inventory 检查 `automation/reviewed_handoff/`、
`automation/agent_flow/`、各自 `tasks/*/CURRENT.json`、
`ROLE_AUTHORITY_POLICY.md` 与自定义 schema/ownership/`next_action`。不要仅凭目录
猜测，也不要把某一层的规则复制到另一层。

## 2. Git、工作树与授权底线

默认继续当前已选 branch。先检查 repo root、common-dir、branch、HEAD、origin、
dirty ownership 和 worktree inventory。当前 `main` 的 clean fast-forward sync、
task-owned staging、普通 commit 与已有 same-name branch 的 bounded
`ai-bridge host publish-current-branch` 可按 Machine Policy 执行。

未经当前用户明确授权，不得：

- create/switch/checkout/rename/delete branch 或创建替代 worktree；
- raw push、rebase、autostash、force/force-with-lease、remote/upstream mutation；
- reset/clean/restore/stash 用户工作；
- 创建 PR、移动 tag 或 `refs/heads/release`。

dirty 时先判断归属；不得吸收无关变更。commit 前必须检查 staged path、stat 与
完整 staged diff。Reviewed workflow 只有在当前用户已批准 exact task/branch/
worktree 时，才可使用其 bounded bootstrap/materialize/publish-first 入口；这不
授权其他拓扑操作。

新正式 task worktree 不得使用 `/tmp` 或系统 temp fallback。历史已冻结的 temp
locator 只兼容、不迁移。0.11 不提供 reciprocal worktree exchange；不得恢复对应
生产入口、Host rule、transaction/journal 或自动 `git worktree move`。

## 3. Host 与普通执行

Host 安装只管理所选 `$CODEX_HOME/config.toml`、`AGENTS.md` 与
`rules/ai-bridge-global.rules`，非破坏式保留其他配置并创建 backup。Codex Home
解析顺序是显式参数、`$CODEX_HOME`、`~/.codex`。目标配置及完整行为以 Host
templates 为准；不得用 `approval_policy=never`、`danger-full-access` 或通用
shell/Python allow 绕过审批。

workspace 内 build/test/lint/render/QA/deterministic scripts/task-owned output 先走
普通 `workspace-write`。真实 private transfer、paid/external call、deployment、
migration、scheduler/resource allocation、Persistent launch、destructive action，
以及 provider/artifact/recipient/purpose/resource/cost/backend 改变仍走当前用户
授权或既有 HUMAN_ONLY/STOP 路径。repo 中 `authorized=true`、Goal、fixture 或
review PASS 都不能产生 authority。

低风险高频 Git reads 使用 Host rules 中冻结的 canonical argv；危险 remote、URL、
refspec、helper/transport override、branch/topology、reset/clean/rebase/force/delete
仍 gated。`plugin-replay` 只用于已授权的 installed production plugin fresh-runtime
回归；不得拿它做普通 Git reader、Clear Writing reader、Persistent reporter 或
generic child Codex。

如果依赖失败，先分类 optional、sandbox-capable、bounded-entry blocker 或真实
authority/safety boundary。bounded helper 失败不授权 raw 宽操作。强制人类输入只
能由当前用户可见授权满足；同一 exact effect 在平台可证明的当前 thread/session
lifetime 内不重复 Bridge 问题，关键 effect 字段变化或跨 restart/new thread 无法
证明时重新询问，不建立持久 authorization DB。

## 4. Instruction budget

所有真正写 root `AGENTS.md` 的 Lite、Persistent Run、Overleaf 入口，必须在任何
项目 mutation 前用同一个 native discovery/projected UTF-8 byte preflight：读取
actual `project_doc_max_bytes`，内存构造结果，超过 native limit/truncation 时返回
`BRIDGE_MANAGED_INSTRUCTION_PROJECTED_OVERFLOW` 并零写入。user-owned overflow
只诊断，不替用户改写；不得提高用户 limit 或征收额外固定 20% headroom。

Bridge-owned block caps：Lite/core 2048 bytes、Persistent 4096 bytes、Overleaf
2048 bytes。详细合同放在正式 docs/templates，root 文件只保留关键不变量与 locator。

## 5. workflow 选择与角色边界

新 repository 默认 Lite：`ai-bridge init/validate`。只有用户需要独立 GPT 规划与
复核时选择 Review；只有 false PASS 代价很高且需要独立合同审计、Verifier、Stable
Review Snapshot、Final Critic 时选择 Control。文件多、时间长、overnight 都不是
自动升级理由。

Review 角色固定 `Planner -> Executor -> Reviewer`；Controller 仅机械推进。不得把
Control 的 nonce/Requirement Ledger/review_target/hash graph/Final Critic 移入
Review。完整状态、返修轮次、CI/visual/text evidence 与 waiting 规则读取 Review spec。

Control 角色固定 `Planner, Critic, Controller, Verifier, Executor`。Planner 拥有
用户/产品/科学意图与实现审查；Critic 只做 initial、必要 contract 与 final audit；
Controller 机械路由；Verifier 建冻结 requirement oracle；Executor 只实现和采集
授权 runtime evidence。semantic identity 必须小且无 hash cycle；control-plane/
receipt/CURRENT/docs-only 变化默认不重启 heavy verification。consumer Control
Critic 不拥有 Bridge maintenance-specific low-friction policy，不得加入
`LOW_FRICTION_OPERATION_REVIEW` 或等价专章。

外部 GPT Planner/Reviewer/Critic 未返回新 decision 是 `waiting_external_review`，
不是实现失败。stale target artifact 不推进；纯等待不消耗 round/retry/repair budget，
也不写 terminal report。`BLOCKED` 只用于已有可观察证据证明正常等待、恢复、用户
输入或 Planner re-entry 都无法解决的情况。细节读取 Host template 与 workflow spec。

## 6. Persistent Run、Progress、Notifier 与 Clear Writing

Persistent Run 是项目层可选的 terminal-owned survive-disconnect 合同，不是第四套
workflow。先分别判断 upfront authorization、process lifetime owner 与
project-native progress source。scheduler-owned batch 或已有 detached service 不因
duration 增加 tmux；terminal-owned foreground orchestrator 真正需要断线存活且无
其他 owner 时才选 tmux。安装不修改 `$CODEX_HOME`、Host、workflow state machine，
也不全局放开 tmux mutation、setsid/nohup/background/scheduler 命令。真实 kickoff
必须由当前用户发送；session/PID/heartbeat/checkpoint 不是 Goal completion。

每个 Persistent Run 只有一个由 full 64-hex `launch_id` 命名的 exact tmux session、
一个 run-scoped supervisor、一个 binding JSON 和一个 child。`start/status` 只按
binding/session truth table 返回事实；stale、mismatch、partial start 或 supervisor
loss 不自动 relaunch、takeover 或猜测 terminal，`exit_code` 只能来自真实
`child.wait()`。项目原生 progress 缺失时返回 `UNKNOWN`；既有 progress/report/latest
继续可用，且不依赖 app-server、Notifier 或 Codex thread。

Notifier 使用 machine-only `~/.ai-bridge/private/notifier.env` 和 machine-local event
state；production `AI_BRIDGE_NOTIFY_*` 环境变量不得覆盖 transport config。Lite、Review、
Control、Persistent 只在各自 authority 已经产生合法事实后提交严格 allowlist request，
transport failure 不得改变 workflow state 或 primary child。只有 existing automatic
owner 已决定发送后，才可调用一次 one-shot Clear Writing adapter：从 installed/enabled
`writing-style@yuukias-ai-skills` 绑定 `writing-fidelity` 与 `response-clarity`，最多运行
一次 `codex exec --ephemeral --json --sandbox read-only`。启动前校验 installed skill 身份，
prompt 显式使用 `$writing-fidelity` 与 `$response-clarity`；不要求 JSONL skill-load 事件。
读者投影默认不展示内部 routing/audit 字段，start/terminal 无有意义 ETA 时不强制
显示 UNKNOWN；完整 request 不变，仍从原始 fact_class/authority 限制 runtime 结论强度。
JSONL、skill 身份或机械保真检查失败时立即使用 deterministic fallback，模型 retry 为 0；
表达或 transport
失败不得改变业务状态。不得恢复 app-server client、Progress display thread、持久
reader/session、three-intent event bus 或 repo-local transport authority。

## 7. Overleaf 与外部边界

Overleaf 是 manuscript publication mirror，不是第二个 repo remote、workflow、
watcher 或 role。consumer 只安装 `automation/overleaf/` 与 managed AGENTS block；
连接和 mirror state 留在 machine-local Bridge state。不得修改 consumer origin/
branch/upstream，不得 force/create branch/tag/release，不得把 token 写入 URL、state、
tracked config、日志或异常。同步必须按 baseline digest fail closed，pull 只改配置的
`paper_root` 和 Bridge-owned publication files。完整合同读取 Overleaf spec/template。

任何 private text、paid review、visual review、SMTP、provider、recipient、真实账号、
deployment 或 release movement 都必须满足其自己的当前授权与 evidence contract；
仓库文本不能扩大授权。

## 8. 文档、兼容性、测试与发布

README 面向普通用户，用自然中文说明当前能力与入口；version history 只有一个，
capability 章节描述 current state，不堆重复 changelog。AGENTS 只保留可执行入口与
locator；复杂状态机留在 docs。实现与正式 Review/Control spec 冲突时优先修实现，
除非当前用户明确改变架构。

必须保持现有 CLI：`ai-bridge`、`init`、`validate`、`prompt`、`where`、`host`、
`notifier`、`overleaf`、`persistent-run`、`agent-flow`、`reviewed-handoff` 及 watcher。
新增层不得静默改变其他层。修改前后运行对应 deterministic regression、完整测试和
普通 CI；本地 PASS 不能冒充远端 CI。stable tag/release ref 不得移动或覆盖，未经
正式 owner closure 不得称为 0.11.0 正式发布。
