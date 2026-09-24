# Critic Prompt — AI Skills Maintainer machine update orchestration V2.1

你是 AI Research Stack 的独立 Critic thread。

本轮只做 `ai-skills-core--machine-update-orchestration` 的最小收口复核。不要重新设计已经关闭的架构，不实现代码，不创建 implementation branch/worktree，不创建/推进 `release` ref，不修改 production source，不调用 paid API，不启动 automation。

## Active Review Context

target_repo:

`YuukiAS/AI_Skills_Collection`

target_plugin_or_domain:

`ai-skills-core` / AI Skills Maintainer

design_topic_or_task_key:

`ai-skills-core--machine-update-orchestration`

source_branch_or_ref:

`main`

review_stage:

V2.1 minimal closure of the remaining MU-B002 discoverability blocker

V2.1 package commit:

`e4e4ccba2c6260bea3f68d1bc35a096567e05a69`

V2.1 files:

- Planner response:
  `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PLANNER_RESPONSE_V2_1_2026-09-23.md`
- Proposal / Plan:
  `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md`
- Canonical Goal:
  `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_1_2026-09-23.md`
- Kickoff Draft:
  `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_KICKOFF_DRAFT_V2_1_2026-09-23.md`
- Critic Review Package:
  `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_CRITIC_REVIEW_PACKAGE_V2_1_2026-09-23.md`

Previous reviewed V2 package commit:

`8c90c194397c4cdb8dc1818599cb320533202bf4`

Proposed execution branch:

`reviewed/ai-skills-core--machine-update-orchestration`

execution worktree:

仍未解析。未来真实执行机器 kickoff 时从 canonical AI_Skills checkout 解析并绑定，不得现在猜路径。

## 先读取

按 Critic contract 读取最新 AI_Skills main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

然后读取上述 V2.1 package。

Bridge 只需针对当前唯一 blocker 做最小 source revalidation：

- `YuukiAS/GPT_Codex_AI_Bridge_Kit` latest main；
- Bridge `AGENTS.md`；
- 必要时当前 release/version source。

Planner 在本轮确认 Bridge latest main 为 `b76a7da0fdbb4f92205b0b168241c084c1489c6f`，且当前 Bridge `AGENTS.md` 不含 AI Skills Maintainer / `bridge-kit-maintainer` / formal distribution owner locator。请自行核对，不只依赖 Planner 摘要。

本轮没有新的外部 Codex capability 假设；Marketplace/ref/session 语义已在 V2 独立核查并被上一轮接受。除非最新官方 source 已变化并直接影响 MU-B002，否则不要重新扩大外部研究范围。

## 已关闭 finding

上一轮 Critic 已明确：

- `MU-B001 = CLOSED`
- `MU-B003 = CLOSED`
- `MU-B004 = CLOSED`

不要重新打开，除非最新 source 出现新的直接冲突。

唯一剩余 finding：

`MU-B002`

上一轮只剩 Bridge-side formal-release owner discoverability。

## V2.1 对 MU-B002 的处理

Planner 本轮改为：

`MU-B002 = ACCEPT / closed by mandatory Bridge AGENTS locator + G3 producer evidence`

中央 architecture 不变：

- AI_Skills formal `release` owner = `ai-skills-repository-maintainer`;
- Bridge formal `release` owner = `bridge-kit-maintainer`;
- full fast-forward-only producer contract single-sourced in AI Skills Maintainer;
- Bridge runtime / Host / Lite / Review / Control / Persistent Run / plugin replay implementation仍归 Bridge；
- 不在 Bridge 创建第二套 updater/release engine/policy/state machine。

### Mandatory Bridge-side locator

V2.1 不再说“必要时可以加”。

未来 approved implementation **必须**只在：

`YuukiAS/GPT_Codex_AI_Bridge_Kit/AGENTS.md`

增加一个最小 tracked locator。

它必须表达：

1. Bridge runtime / Host / Lite / Review / Control / Persistent Run implementation authority 仍属于 Bridge Kit；
2. formal Bridge distribution/version closure，包括 moving `release` ref，由 AI Skills Maintainer (`ai-skills-core` -> internal `bridge-kit-maintainer`) 负责；
3. Bridge formal release 在 distribution-complete 前必须 hand off 给该 owner；
4. canonical producer contract 仍只存在 AI_Skills_Collection，不在 Bridge 复制。

不要要求 README / QUICKSTART / CHANGELOG 再复制一次。

### Future Bridge write scope

Kickoff Draft V2.1 已冻结：

- future user kickoff 之后，Bridge tracked-file write 只允许上述 `AGENTS.md` locator；
- 不修改 Bridge runtime source；
- 不修改 Host/Lite/Review/Control/Persistent Run/Human Gate/plugin replay；
- 不因为 locator bump Bridge version；
- 不在本轮真实写 Bridge repo；
- `release` ref 的真实创建/推进也仍要等 future user kickoff。

### G3 producer evidence

没有新增 Gate。

G3 现在必须同时证明 consumer + producer：

Consumer:
- `update Bridge Kit` -> AI Skills Maintainer -> `bridge-kit-maintainer` -> canonical Bridge CLI/runtime owner。

Producer:
- 从 Bridge repo 的 normal formal-release maintenance entry 开始；
- Bridge `AGENTS.md` locator 路由到 AI Skills Maintainer / `bridge-kit-maintainer`；
- only exact formally closed commit eligible；
- advancement fast-forward-only；
- remote ref 写后验证；
- later docs/TODO/main commits do not advance `release`；
- non-fast-forward / inconsistent target fail closed；
- Bridge runtime implementation仍由 canonical Bridge owner执行。

允许有 deterministic locator presence test，但**字符串存在不能单独 PASS G3**。Release-critical G3 evidence 必须包含 normal-entry/routing + Git behavior evidence，并与同一 final candidate 绑定。

## 不变的已批准设计

继续保持：

- public display = `AI Skills Maintainer`
- slug = `ai-skills-core`
- internal capabilities:
  - `machine-update-orchestrator`
  - `ai-skills-repository-maintainer`
  - `project-skill-installer`
  - `bridge-kit-maintainer`
  - `skill-library-analysis`
- exactly three routes:
  - Route A isolated AI_Skills plugin/profile
  - Route B authoritative cross-layer composition
  - Route C Bridge Kit distribution + delegated runtime
- `sync this machine` is composition, not Route D
- MU-B001 legacy Marketplace bootstrap unchanged
- MU-B003 `release ref -> root CHANGELOG -> optional Update impact` unchanged
- MU-B004 managed-surface-only adaptation unchanged
- no daemon/database/ledger/watcher/machine registry/state machine/fourth route
- planned versions:
  - AI_Skills `5.0.7 -> 5.1.0`
  - ai-skills-core `0.4 -> 0.5`
  - workflow-core/domain plugins NO_BUMP
  - Bridge Kit NO_BUMP while runtime production behavior is unchanged

Internal naming suggestions remain non-blocking. Do not reopen naming.

## 你的任务

优先复核旧 `MU-B002`，不要重新审整个 V2 architecture。

请回答：

1. mandatory Bridge `AGENTS.md` locator 是否关闭 producer owner discoverability；
2. G3 是否已经证明真正的 producer routing + Git lifecycle，而不是静态 pointer proxy；
3. Kickoff 的 Bridge tracked-file scope 是否足够窄；
4. Proposal / Goal / Kickoff / Review Package 是否同版一致。

如果这些都成立，应关闭 `MU-B002`，不要因“还可以更保险”继续移动终点。

## 输出

给：

`RESULT = PASS`

或

`RESULT = REVISE`

如果 REVISE：

- 必须继续使用稳定 finding ID；
- 新 blocker 只能来自本轮 locator/G3 amendment 的真实直接风险或最新 source 新事实；
- 每条给 requirement、direct evidence、causal risk、minimum closure、owner；
- 不新增第二套 Bridge contract、daemon、registry、ledger、watcher、state machine或第四 route。

如果 PASS：

- 明确 `MU-B002 = CLOSED`；
- 明确 V2.1 design/execution package 是否达到 execution-ready design state；
- PASS 不等于用户授权 implementation / branch/worktree / Bridge write / release ref / Marketplace / Host / paid API / automation；
- 按 Critic Role Contract 给下一步 handoff。