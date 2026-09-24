# Critic Prompt — AI Skills Maintainer machine update orchestration V2

你是 AI Research Stack 的独立 Critic thread。

本轮只审查 V2：关闭上一轮 `MU-B001`–`MU-B004`，并审查用户新增的 Bridge Kit maintenance ownership 设计。

不要实现代码，不要创建 implementation branch/worktree，不要创建/推进 `release` ref，不要修改 production source，不要调用 paid API，不要启动 automation。

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
V1 REVISE closure + architecture/execution-package design review

V2 package commit:
`8c90c194397c4cdb8dc1818599cb320533202bf4`

V2 files:

- Planner response:
  `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PLANNER_RESPONSE_V2_2026-09-23.md`
- Proposal / Plan:
  `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_2026-09-23.md`
- Canonical Goal:
  `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_2026-09-23.md`
- Kickoff Draft:
  `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_KICKOFF_DRAFT_V2_2026-09-23.md`
- Critic Review Package:
  `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_CRITIC_REVIEW_PACKAGE_V2_2026-09-23.md`

Previous V1 package commit:
`a3dec83de651480ac46179ddae3b553c8f41d134`

Previous findings:

- `MU-B001` — legacy main-pinned Marketplace bootstrap
- `MU-B002` — release-ref lifecycle producer
- `MU-B003` — authoritative cross-layer update impact
- `MU-B004` — unowned repo text mutation boundary

Proposed execution branch:
`reviewed/ai-skills-core--machine-update-orchestration`

Execution worktree:
仍未创建。exact task-owned worktree 只能在未来真实执行机器上从 canonical checkout 解析，并在 current-user kickoff 中绑定。不要把这一点重新当 design blocker，除非 V2 自己要求提前猜路径。

## 先重新读取最新 source

按 Critic contract 先读 AI_Skills_Collection 最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

再读本轮必要 baseline：

- `README.md`
- `VERSION`
- `CHANGELOG.md`
- `docs/INSTALLATION.md`
- `scripts/codex_marketplace_config.json`
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`
- `skills/core/codex-system/project-skill-installer/SKILL.md`
- `skills/core/codex-system/skill-library-analysis/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `docs/plugin-todos/ai-skills-core.md`
- `docs/plugin-changelogs/ai-skills-core.md`
- generated ai-skills-core payload
- relevant Marketplace/install/update/version tests
- `results/056_product_delivery_discipline/FINAL_INTEGRATION_RELEASE_CLOSURE.md`

然后读 V2 package。

Bridge 独立读取 `YuukiAS/GPT_Codex_AI_Bridge_Kit` 最新 main，至少：

- AGENTS / README / QUICKSTART
- `pyproject.toml`
- `ai_bridge_kit/__init__.py`
- `ai_bridge_kit/cli.py`
- `ai_bridge_kit/host.py`
- `ai_bridge_kit/plugin_replay.py`
- current CHANGELOG
- normal Host/Lite/Review/install/update/runtime discovery surfaces

不要仅依赖 Planner 摘要。

## 独立外部核查

按 Critic contract 自己核查当前 OpenAI/Codex reality，重点任选至少一个关键假设并优先官方 docs/source：

- Git Marketplace `--ref` / add/list/upgrade/remove；
- same marketplace source/ref identity 与 source replacement；
- plugin add/list/reinstall；
- source removal config-layer fail-closed semantics；
- fresh thread/session loading boundary；
- AGENTS/instruction load timing。

Planner 本轮参考过：

- `https://developers.openai.com/plugins/build/plugins`
- `https://developers.openai.com/api/docs/guides/latest-model`
- `https://github.com/openai/codex/blob/main/codex-rs/cli/src/plugin_cmd.rs`
- `https://github.com/openai/codex/blob/main/codex-rs/cli/src/marketplace_cmd.rs`
- `https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/marketplace_remove.rs`
- `https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/plugin-creator/references/installing-and-updating.md`

不要只复述 Planner 结论。

## 用户新增要求

在 V1 Critic 之后，用户进一步明确：

> Bridge Kit 也应该由 AI Skills Maintainer 维护；可以在插件里加一个 skill 负责，不要给 Bridge Kit 自己增加重量。本质上 Maintainer 应能 adapt skill/profile、plugin/repository 和 Bridge Kit version。

V2 因此新增内部：

`bridge-kit-maintainer`

请把这视为用户当前要求，不要用 V1 的旧 owner 假设否定它。

但仍必须守住：

- Bridge runtime/Host implementation 继续归 Bridge Kit；
- AI Skills Maintainer 只拥有 Bridge source/version/distribution/release-channel maintenance 与 delegation；
- 不复制 Bridge Host/Lite/Review/Human Gate/plugin replay logic；
- 不给 Bridge 新增 updater/daemon/watcher/state machine。

## 优先复核旧 blocker

### MU-B001

V2 已加入完整一次性 legacy bootstrap：

- real marketplace source/ref/sparse/config-layer discovery；
- exact legacy metadata capture；
- release ref/payload preflight；
- official CLI source replacement；
- restore old source when replacement itself fails；
- non-user/system config owner fail closed；
- 0.4 明确不冒充拥有新能力；
- G2 从真实 `0.4 + main-pinned Marketplace` 开始；
- fresh session closure。

请判断旧风险是否关闭。

不要因为“还可以更自动”继续阻塞；只看是否仍存在会让旧机器无法正确迁移/恢复的直接风险。

### MU-B002

V2 接受 producer contract 必须存在，但对“完整合同必须复制到两个 repo”提出 PARTIAL_ACCEPT + REBUT。

新的中央 owner：

- AI_Skills release ref -> `ai-skills-repository-maintainer`
- Bridge release ref -> 新 `bridge-kit-maintainer`

完整 fast-forward-only producer contract single-source 在 ai-skills-core。

Bridge 只允许在确有 discoverability 缺口时加一个最小 pointer，不实现第二份 release mechanism。

请独立判断：

1. 这是否已经解决“谁推进、何时推进、如何验证”的生命周期风险；
2. 是否真的必须把完整 contract 再复制到 Bridge repo；
3. 如果 Bridge-side locator 必须存在，最小是否只需要一个指向中央 Maintainer owner 的短 locator，而不是第二套 release contract。

如果你坚持 REVISE，必须说明缺少 Bridge-side 哪个具体入口会导致未来正式 Bridge release 无法调用中央 owner，以及最小 locator 是什么。不要以“更保险”为由要求 duplicated policy。

### MU-B003

V2 定义：

`release ref -> root CHANGELOG matching release entry -> optional ### Update impact`

- absence = isolated；
- root release entry alone can expand mutation scope；
- component changelog detail only；
- arbitrary diff/TODO/commit prose/model inference cannot expand；
- conflict fail closed；
- G1/G3 direct coverage。

检查是否关闭旧 blocker。

### MU-B004

V2 只允许 automatic mutation 到 ownership-proven managed surfaces。

Unmanaged AGENTS/copied/science/safety/privacy/Figma/deployment/device/server rules diagnosis-only。

G4 明确要求 unmanaged apparently-conflicting AGENTS byte-for-byte unchanged。

检查是否关闭旧 blocker。

## 审查新增 bridge-kit-maintainer

判断新增 internal skill 是否：

- 真的减少 giant orchestrator complexity；
- 与 `ai-skills-repository-maintainer` / project installer 边界清楚；
- 只维护 Bridge distribution/version/source；
- 仍通过 canonical `ai-bridge` 执行 Host/runtime mutations；
- 没有暗中把 Bridge production behavior owner 搬到 AI_Skills；
- 没有形成第四 route。

V2 仍只有：

- Route A isolated AI_Skills plugin/profile
- Route B cross-layer composition
- Route C Bridge Kit distribution/runtime

`sync this machine` 仍只是 composition。

## Gate Matrix

继续审 G1–G5，不机械新增 gate：

- G1 short request + formal release/update-impact routing
- G2 legacy Marketplace bootstrap + install/self-update/fresh-session
- G3 Bridge Kit maintenance + canonical Bridge delegation
- G4 selective managed consumer + unmanaged preservation + dirty safety
- G5 failure/recovery/Human Gate/should-not-change

重点检查是否可以被 static test/parity/helper PASS 钻空子，以及 release-critical evidence 是否要求同一 final candidate。

## Version

V2 仍提议：

- AI_Skills repository `5.0.7 -> 5.1.0` MINOR
- `ai-skills-core 0.4 -> 0.5`
- workflow-core/domain plugins NO_BUMP
- Bridge Kit NO_BUMP if Bridge production runtime behavior unchanged

新增 `bridge-kit-maintainer` 属于 ai-skills-core 的 user-facing capability扩展，不等于修改 Bridge runtime。

如果你认为 Bridge docs pointer / release ref 本身要求 Bridge bump，必须先从 Bridge 当前版本合同给出直接依据；不能只因跨 repo 发生了 Git ref/doc change就机械 bump。

## 输出

对 V2 package 给：

`RESULT = PASS`

或

`RESULT = REVISE`

优先按旧 finding ID 复核。

已足够关闭的旧 blocker应明确关闭。

新增 blocker 只能来自：

- 最新 source 新事实；
- V1 Critic 漏掉的直接重大风险；
- V2 的 `bridge-kit-maintainer` amendment 引入的真实回归。

不要换措辞移动终点。

如果 REVISE，每个 blocker仍必须有：

- requirement；
- direct evidence；
- causal risk；
- minimum closure；
- owner。

不要新增 daemon/database/ledger/watcher/state machine/第四 route。

本轮 design PASS 不授权：

- production implementation；
- implementation branch/worktree creation；
- remote `release` ref mutation；
- real Marketplace migration；
- Host mutation；
- paid API；
- automation；
- deployment。

若 PASS，按 Critic contract 给下一步 Planner/execution-package handoff；如果你认为 V2 的 Proposal/Goal/Kickoff 已可作为同版 execution package，也要明确说明 design-stage PASS 证明什么、不证明什么。
