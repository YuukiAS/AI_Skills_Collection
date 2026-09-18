# 058 Active Repo AGENTS Adaptation — Critic Prompt

你是 AI Research Stack 的长期独立 Critic thread。

开始新的设计审查：

TASK_KEY = `058_active_repo_agents_adaptation`

Repository:
`YuukiAS/AI_Skills_Collection`

Review object:
`docs/design/058_ACTIVE_REPO_AGENTS_ADAPTATION_PROPOSAL_2026-09-18.md`

Planner proposal commit:
`4b2bc83c47bbcf6e4fd42cef42d1384d111147d4`

本轮只审设计。不要修改任何目标 repo / AGENTS，不修改 Bridge production，不创建 branch/worktree，不启动 Executor，不执行 056/058，不运行 paid API。

## 必须读取

AI_Skills 最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- 本 058 Proposal

Bridge current main：

- `templates/repo/AGENTS_TEMPLATE.md`
- `templates/prompts/AGENT_RULES.md`
- 与 fresh/existing AGENTS install ownership 直接相关的当前 source/tests

目标 repo current canonical AGENTS / directly referenced rule surfaces，至少独立读取：

- `Distributed_Imaging_Inference`
- `CAT-TRACE`
- `Reliable_Imaging_Inference`
- `CUHK_Date`
- `Clash_Profile`
- `CARE_Challenge`
- `CardiacNexus`
- `Echo_Select`
- `Web_Highlighter`
- `VibeResearch`
- `Shione`
- `Longleaf_Bridge`
- `Zotero_Koofr_GPT_Mirror`
- `MoSAIC_Paper`

并抽查 Proposal 中列出的 active no-root-AGENTS repos：

- `AI_Research_Toolkit`
- `GKD_Rules`
- `Zotero_Arrow_Plugin`
- `Lucerna-Vault`

已经由 057 整理过的：

- Bobbio
- Lucerna
- Mica-for-ChatGPT
- Asteria
- SeminarArc

只需核对“VERIFY_ONLY/minimal adaptation”是否合理，不要重新做 057 review。

做针对性的 current web research，优先 OpenAI 官方：

- Codex AGENTS discovery / project_doc_max_bytes
- concise AGENTS / progressive disclosure / harness engineering guidance

## 核心问题

用户明确希望：
- 全面统一“AGENTS style / ownership”，但不把不同 repo 的业务规则写成一样；
- 保留现有重要规则；
- 解决内部重复、冲突、stale locator、过长 root；
- 避免 DII 这类“规则写着要显示 prompt，但实际静默等用户”的情况；
- 不再为几十个 docs-only repo 做一轮轮重 workflow；
- 最好一个 Critic 审完，再分 repo 直接改。

请主动攻击两个方向。

### 1. 是否过重

重点检查 Proposal 是否仍然不必要地：
- 为 docs-only gardening 创建 per-repo Plan/Goal/branch/worktree；
- 要求每个 repo 独立 Planner/Critic；
- 新增 gate taxonomy / state / ledger / controller；
- 自动安装 Lite/Review/Control/Persistent Run；
- 为“统一”批量翻译或大迁移所有 repo。

如果还有更简单且同样安全的做法，要求最小简化。

### 2. 是否过简

重点检查：
- DII silent prompt 是否真的不是简单“再加一句提示词”可以解决；
- current DII 是否确实没有 tracked `prompts/AGENT_RULES.md` Lite surface；
- CUHK_Date root 是否确实指向不存在的 `prompts/*` locator；
- CARE root 是否确实大于默认 AGENTS aggregate budget并存在截断风险；
- Clash/CAT/Reliable 是否存在 root 与 deeper/Lite owner 混杂；
- missing-AGENTS repos是否有一些其实需要最小安全 scaffold；
- one-review/direct-main模式是否仍能保护安全/科学语义不丢失。

## 逐 repo disposition

对 Proposal 中每个 repo 给：

`VERIFY_ONLY | LIGHT_ADAPTATION | SUBSTANTIAL_REORGANIZATION | ADD_MINIMAL_SCAFFOLD | NO_AGENTS_NEEDED | EVIDENCE_NEEDED`

尤其复核：

### DII
- 科学/HPC规则必须保留；
- Persistent Run已有“生成并显示prompt”文案但真实行为仍失败；
- 不允许再加056同义规则冒充修复；
- 是否应等待056后安装/刷新Lite并做normal-entry消费验证。

### CAT-TRACE
- 顶部“Codex不承担规划”是强项目不变量，不能被generic Lite冲掉；
- generic Handoff/skill/version内容是否可更清楚地分owner；
- tracked Lite是否需要post-056 refresh。

### Reliable Imaging Inference
- novelty/evidence/research framing必须保留；
- generic Handoff应和project rules更清楚分层。

### CUHK Date
- root当前是否存在broken prompt locators；
- 是否应该post-056修复/安装Lite，而不是往root复制中央规则。

### Clash_Profile
- production freeze/remote tunnel/device safety必须继续root prominent；
- 大量runbook细节是否已有deeper owner可指向；
- 不得因“整理”改变任何生产路由/设备配置。

### CARE
- root size/context-budget是否构成真实风险；
- substantial map conversion是否必要；
- challenge/data/submission/GPU safety不能丢。

### no-root repos
逐个判断是否真的值得加 AGENTS；不要为了对称全部创建。
特别对 Lucerna-Vault 审 secrets/encrypted-state risk。

## 执行模型审查

Proposal 设计的是：

```text
one Planner proposal
-> one Critic PASS
-> wait until 056 integrated
-> mechanically bind final Bridge/Lite ref
-> user sends independent per-repo prompts
-> direct canonical-branch docs/instruction edits
-> per-repo commit/push
```

默认：
- no task branch/worktree；
- no per-repo Planner/Critic；
- one repo failure does not block others；
- no cross-repo integration package；
- only AGENTS/current Lite-Handoff/directly owned instruction docs；
- no product/runtime/scientific behavior change。

判断这是否安全、比例合适。

如果认为 final per-repo prompts 在056完成后仍必须再由Critic看一次，请说明为什么；优先允许“同一已通过 contract 下机械绑定 final Bridge/Lite ref + 生成 prompts”而不是重新走完整设计。

## Acceptance shape

不要新增 H1-H9/H10 之类编号体系。

检查下面这组轻量 acceptance 是否足够：

- no internal contradiction;
- all locators exist;
- all important project-specific invariants preserved;
- generic Lite not duplicated into root;
- managed Bridge block not forked;
- root shape/context improved where actually needed;
- relevant human-gate prompt is behaviorally visible;
- diff limited to instruction/docs surfaces;
- no runtime/product/science changes.

## Sequencing

默认 Proposal 要求 **056 完整 integration 之后才执行 mass adaptation**。

判断这是否正确。重点考虑：当前用户关心的 HUMAN_ONLY prompt behavior本身就是056 production change；若现在先迁移，会不会立即需要第二次刷新。

不要因此阻塞当前 056 review/implementation；058是独立后续 round。

## Output

若需要修订：

```text
RESULT = REVISE
TASK_KEY = 058_active_repo_agents_adaptation
REVIEW_OBJECT = docs/design/058_ACTIVE_REPO_AGENTS_ADAPTATION_PROPOSAL_2026-09-18.md
READY_FOR_LIGHTWEIGHT_EXECUTION_PACKAGE = NO
NEXT_HANDOFF = PLANNER
```

列 stable blockers，并按 Critic contract 自动给完整 Planner返修prompt。

若设计成立：

先用正常中文解释：
- 为什么这次不需要057那样重；
- DII silent prompt到底暴露了什么；
- 为什么应该等056再适配；
- 哪些repo需要大整理、哪些只轻改、哪些不该加AGENTS；
- 如何保证重要规则不会在“统一style”时丢失。

然后：

```text
RESULT = PASS
TASK_KEY = 058_active_repo_agents_adaptation
REVIEW_OBJECT = docs/design/058_ACTIVE_REPO_AGENTS_ADAPTATION_PROPOSAL_2026-09-18.md
READY_FOR_LIGHTWEIGHT_EXECUTION_PACKAGE = YES
NEXT_HANDOFF = PLANNER
```

下一步只允许 Planner 在056 integration完成后，按已通过设计机械刷新source refs并生成一个**单一轻量 execution batch + per-repo prompts**；不要把它升级成057式多轮 workflow。
