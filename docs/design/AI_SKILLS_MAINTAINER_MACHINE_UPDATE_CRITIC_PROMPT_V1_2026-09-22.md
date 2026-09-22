# Critic Prompt — AI Skills Maintainer machine update orchestration V1

你是 AI Research Stack 的独立 Critic thread。

本轮只审查一件事：是否应把“当前机器上的 AI Research Stack 更新与 selective adaptation”做成现有 `ai-skills-core` / **AI Skills Maintainer** 的长期正式能力，以及 Planner V1 是否已经成熟到可以在后续用户授权下交给 Codex 实现。

不要实现代码，不要启动 Executor，不要修改 production source，不要创建 release ref，不要调用 paid API，不要启动 automation。

## Active Review Context

target_repo:
`YuukiAS/AI_Skills_Collection`

target_plugin_or_domain:
`ai-skills-core` / AI Skills Maintainer

design_topic_or_task_key:
`ai-skills-core--machine-update-orchestration`

source_branch_or_ref:
`main`

proposal_path_and_version:
`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V1_2026-09-22.md` — V1

canonical_goal:
`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V1_2026-09-22.md` — V1

kickoff_draft:
`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_KICKOFF_DRAFT_V1_2026-09-22.md` — V1

critic_review_package:
`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_CRITIC_REVIEW_PACKAGE_V1_2026-09-22.md` — V1

package_commit:
`a3dec83de651480ac46179ddae3b553c8f41d134`

review_stage:
architecture + execution-package design review

proposed execution branch:
`reviewed/ai-skills-core--machine-update-orchestration`

execution worktree:
尚未创建，也不应在本轮创建。Planner 明确要求未来用户发送 implementation kickoff 前，在实际执行机器上从 canonical checkout 解析并绑定 exact task-owned worktree；不要把历史机器路径或某个平台路径猜成当前授权。

## 必须先实际读取

先从 AI_Skills_Collection 最新 main 实际读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

再读取与当前 baseline 直接相关的：

- `README.md`
- `VERSION`
- `CHANGELOG.md`
- `scripts/codex_marketplace_config.json`
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`
- `skills/core/codex-system/project-skill-installer/SKILL.md`
- `skills/core/codex-system/skill-library-analysis/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `docs/plugin-todos/ai-skills-core.md`
- `docs/plugin-changelogs/ai-skills-core.md`
- generated `plugins/codex/plugins/ai-skills-core/`
- relevant tests, especially Marketplace/version/install/update paths
- `results/056_product_delivery_discipline/FINAL_INTEGRATION_RELEASE_CLOSURE.md`

然后读取 package commit 中上述 V1 Proposal / Goal / Kickoff Draft / Review Package。

Bridge 必须独立核查 `YuukiAS/GPT_Codex_AI_Bridge_Kit` 最新 main，与以下事项直接相关的当前 source：

- Bridge normal installation/update
- `ai-bridge where`
- Host install/status/validate
- Host Policy implementation
- Lite/project consumer install/validate
- plugin replay/runtime discovery
- README / QUICKSTART
- version source

不要只依赖 Planner 的 Bridge 摘要。

## 必须独立做外部现实核查

按 Critic contract 做针对性 web research，至少独立核查以下关键假设之一，并优先官方 OpenAI docs / openai/codex source：

1. Codex Git Marketplace 是否支持 ref pinning、refresh、plugin reinstall/list；
2. plugin 更新后当前 session 是否会热加载，还是需要 fresh thread/session；
3. AGENTS.md/global/project instructions 的加载时机；
4. 是否存在比 Planner 的 `release` ref 更成熟、更简单的正式 release 定位方式。

Planner 已查过但 Critic 不得只复述的来源包括：

- `https://developers.openai.com/plugins/build/plugins`
- `https://learn.chatgpt.com/docs/agent-configuration/agents-md`
- `https://github.com/openai/codex/blob/main/codex-rs/cli/src/plugin_cmd.rs`
- `https://github.com/openai/codex/blob/main/codex-rs/cli/src/marketplace_cmd.rs`
- `https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/plugin-creator/references/installing-and-updating.md`

## 用户最终需求

用户以后在每台真正运行 Codex 的本机/server上只做：

`AI Skills Maintainer + 很短的 update 目标`

例如：

- `update presentations`
- `update workflow-core`
- `update AI Skills`
- `sync this machine`

用户不再提供：

- current plugin/repository/Bridge version；
- commit/SHA；
- `CODEX_HOME`；
- AI_Skills/Bridge checkout 路径；
- machine repo inventory；
- adaptation template；
- Bridge/Host/repo-local route 判断。

Maintainer 必须自行做 discovery、formal-release resolution、scope determination、update routing、selective adaptation、verification 和简短报告。

默认 `update` 只到最新正式 release，不得把未发布 main、reviewed branch、candidate/evidence SHA 当正式 target。development/main 只有用户明确要求才允许。

## Planner V1 核心方案

Planner 选择“一个入口、已有 owner 协作”，不是巨型 skill：

- 在现有 `ai-skills-core` 内新增一个内部 machine/environment update orchestrator skill；
- 它只有 discovery / formal-release resolution / routing / delegation / verification / reporting；
- 三种内部 route 作为该 skill 的 internal references：
  - isolated single plugin；
  - major stack/workflow；
  - Bridge/Host；
- `sync this machine` 是组合 scope，不是第四套 mutation engine；
- official Codex plugin/Marketplace CLI 执行中央插件 mutation；
- existing AI_Skills CLI/manifests 执行 AI_Skills-managed consumer refresh；
- Bridge Kit canonical CLI 执行 Bridge runtime/Host/Lite/Review等 mutation；
- workflow-core 继续拥有复杂交付语义；
- target domain plugin 继续拥有领域正确性；
- 不建 daemon/watcher/inventory DB/machine registry/ledger/second auth/state machine。

Planner 还提出一个新的正式 release channel：

- AI_Skills 和 Bridge 各有一个 fast-forward-only moving Git ref `release`；
- 只有 formal release closure 才推进；
- daily Maintainer update 只消费它，不推进它；
- Codex Git Marketplace 正常安装跟踪该 ref，而不是 `main`；
- explicit development update 才消费 `main`。

请重点攻击这个设计是否真的必要、是否足够简单、是否会形成新的发布故障面。

## Critic 必须审的具体问题

### 1. Capability ownership

比较并裁定：

- 扩现有 repository maintainer；
- 扩 project installer；
- 新 machine update skill；
- thin orchestrator + canonical owner CLI；
- 更简单/成熟的现有方案。

必须保证 AI Skills Maintainer 是唯一用户入口，但不能吞掉 Bridge/workflow/domain owner。

### 2. Formal release truth

当前现实是 main 可能领先于最后 formal release，而现有 Marketplace README 用 `main`；AI_Skills 5.x 没有对应 semantic release tags，Bridge current 0.8.5 也没有匹配的 current semantic tag。

Critic 需要判断：

- moving `release` ref 是否是最小可靠解；
- semantic tag / GitHub Release / existing version contract / 其他方式是否更好；
- 如何避免把 main 上 release 后的新 docs/evidence commit 误装；
- self-update 如何从旧安装找到新 formal target。

这是关键 blocker 候选，不要略过。

### 3. Route taxonomy

Planner 只保留三种 mutation route，并把 machine sync 当 composition。

检查是否：
- 过简导致某类 update 无 owner；
- 过重制造多余 route；
- workflow-core 普通升级被错误自动扩大到 Bridge/Host；
- single-plugin update 会误动其他 plugin/repo。

### 4. Selective repo adaptation

必须确认：

- bounded consumer discovery 有实际来源；
- normal repo 不被 mass rewrite；
- AI_Skills manifest update 和 Bridge canonical consumer update 能覆盖真正 stale consumer；
- repo-specific science/safety/privacy/Figma/device/server 规则有明确 should-not-change。

### 5. Self-update / reload

必须审：

- 当前 0.4 到首个 capability-bearing release 的 bootstrap 边界；
- old loaded Maintainer 能否更新 installed source；
- current session 不得假 hot reload；
- final gate 是否真正用 fresh Codex process/session 证明新 release 被 normal entry 消费。

### 6. Source / dirty work / Human Gate

必须对照 056 检查：

- canonical checkout 优先；
- dirty 不机械 clone/block；
- safe fast-forward；
- no stash/reset/restore/remap；
- development checkout 不被静默 downgrade；
- AGENT_RESOLVABLE 不问用户；
- 只有真正新的 authority / dirty ownership / irreducible semantics 进入最小 Human Gate。

### 7. Gate Matrix

V1 合并为五个 gates：

- G1 short request + formal release routing
- G2 Marketplace/install/self-update/fresh-session
- G3 Bridge/Host delegation
- G4 selective consumer + source/dirty
- G5 failure/recovery/Human Gate/should-not-change

判断它们：
- 是否 distinct；
- 是否覆盖用户列出的 normal-entry failures；
- 是否能被 helper/static tests/version-file PASS 钻空子；
- 是否所有 release-critical evidence 能来自同一 final candidate；
- 是否 platform coverage 的声明边界足够诚实。

### 8. Version decision

Planner 依 policy 提议：

- repository `5.0.7 -> 5.1.0` MINOR；
- `ai-skills-core 0.4 -> 0.5`；
- workflow-core/domain plugins NO_BUMP；
- Bridge NO_BUMP if no Bridge production-source behavior changes。

请独立判断是否真正属于此前不存在的 repository-level user capability，而非普通 plugin patch。

### 9. Kickoff authorization

当前 Kickoff Draft 不授权 implementation；未来 user kickoff 才授权 exact task branch/worktree 和 one-time release-ref effects。

检查它是否：
- 过度预授权；
- 缺必要 bounded authority；
- 把 repo contract 当 current-user authorization；
- 错误允许 Bridge production source changes；
- 会触发实现中反复向用户问已经可发现的事实。

## 你的输出

对这个明确 V1 package 给：

`RESULT = PASS`

或

`RESULT = REVISE`

如果 REVISE，每个 blocker 必须有稳定 ID，并包含：

- 对应用户要求 / contract；
- 直接证据；
- 因果风险；
- 最小关闭条件；
- owner。

不要因为“更保险”加数据库、ledger、daemon、watcher、第四角色或另一个 state machine。

如果所有实质 blocker 已关闭，应 PASS；不要用不确定感移动终点。

本轮 PASS 只表示 V1 design/execution package 可在未来用户明确 kickoff 后进入 implementation。它不授权：

- production implementation；
- 创建 implementation branch/worktree；
- 创建/推进 `release` ref；
- Host mutation；
- paid API；
- automation；
- deployment。

如果 PASS 但认为 exact worktree 只能在实际执行机器 kickoff 时绑定，请明确说明这是否阻止 design-stage PASS；不要要求 Planner 猜跨平台本机路径。

如果 REVISE，按 `CRITIC_ROLE_CONTRACT.md` 在回复末尾自动生成完整 Planner prompt，直接带 package path/commit 和 finding IDs。
