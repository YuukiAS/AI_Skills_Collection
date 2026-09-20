# 057 Repo AGENTS Hygiene — Critic Prompt

你是 AI Research Stack 的长期独立 Critic thread。

当前新任务：

TASK_KEY = `057_repo_agents_hygiene`

Repository:
`YuukiAS/AI_Skills_Collection`

Review object:
`docs/design/057_REPO_AGENTS_HYGIENE_PROPOSAL_2026-09-17.md`

本轮只审方案，不修改任何产品 repo，不修改 AGENTS，不启动 Executor，不创建 branch/worktree，不运行 paid API。

## 一、强制读取

先实际读取 AI_Skills_Collection 最新 main：

- `AGENTS.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/design/057_REPO_AGENTS_HYGIENE_PROPOSAL_2026-09-17.md`
- 056 v6 architecture / v0.2 execution package，仅用于确认 057 没有偷改已批准的中央职责分层

再独立读取当前真实 repo instruction surfaces：

### Bobbio develop
- `AGENTS.md`
- `docs/DEVELOPMENT_WORKFLOW.md`
- `docs/PRODUCT_DESIGN_BRIEF.md`
- `docs/design/FIGMA_HANDOFF.md`
- `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md`

### Lucerna main
- `AGENTS.md`
- `prompts/AGENT_RULES.md`
- current screenshot helper / Longleaf locator docs as needed

### Mica-for-ChatGPT main
- `AGENTS.md`
- `docs/PHASE_1_LONG_THREAD_RECOVERY.md`
- `docs/VERSIONING.md`

### Asteria main
- `AGENTS.md`
- `prompts/AGENT_RULES.md`
- `docs/operations/blackbox-audit/UI_BLACKBOX_BROWSER_CONTRACT.md`
- `docs/operations/development/DEVELOPER_VISUAL_SELF_QA_CONTRACT.md`
- `docs/design/SCIENTIFIC_GRAPH_VISUAL_SYSTEM.md`

### SeminarArc main
- `AGENTS.md`
- `prompts/AGENT_RULES.md`
- `docs/DEVICE_TESTING.md`
- relevant project-skill locators

### CUHK Date main
- verify whether root `AGENTS.md` exists
- `docs/design/prototype/AGENTS.md`

## 二、独立外部研究

本轮是实质 design review，必须自己核查当前资料，不只复述 Planner：

- current OpenAI Codex instruction discovery / `project_doc_max_bytes` behavior；
- OpenAI current harness-engineering guidance about AGENTS/context management；
- if you use another agent/repo-instruction practice, prefer primary official source.

重点判断“大 AGENTS 是真实 consumption risk”是否成立，以及 Planner 是否因此过度追求缩短。

## 三、主动攻击两个方向

### 过重

检查 057 是否可能：

- 为了统一风格大规模翻译/重写所有 repo；
- 创建大量新的 docs/index/schema；
- 把安全规则从 root 移出去后反而难发现；
- 一次处理太多 repo，造成 high-risk science/server repo 意外改动；
- 只因为 line count 大就删除必要规则；
- 把 Bridge-managed block 手工 fork；
- 为“风格一致”把项目差异抹平。

### 过简

检查 057 是否可能：

- 只改 heading/格式，没有真正消除重复/冲突；
- Bobbio 仍保留 Figma vs four image authority ambiguity；
- Mica 仍让 real-site manual acceptance 与 automated browser boundary看似冲突；
- Asteria root仍复制整份 black-box/runtime操作手册；
- SeminarArc root仍塞满会过时的环境 snapshot，导致真正安全 invariant 被淹没；
- 移动内容后没有 canonical locator / semantic-preservation evidence；
- 只整理 root AGENTS，却漏掉同 repo 明确委托的 `prompts/AGENT_RULES.md` 与 root之间冲突。

## 四、逐 repo 给 disposition

对每个 repo 给：

`KEEP_AS_IS | LIGHT_EDIT | SUBSTANTIAL_REORGANIZATION | EVIDENCE_NEEDED | OUT_OF_SCOPE`

并说明：

- 哪些内容是重复；
- 哪些是真冲突/authority ambiguity；
- 哪些只是长但必要；
- 哪些应留 root；
- 哪些可 move-to-doc；
- 哪些 generated/managed block 不应手改；
- 是否存在用户安全/产品语义丢失风险。

特别审：

### Bobbio
- Figma current authority vs `images/Bobbio_Design_*` 旧引用；
- GUI/human gate / anti-blocking / pre-user acceptance 三处是否应合并；
- Zotero安全规则是否会因“去重”被削弱。

### Lucerna
- 是否确实只需轻整理；
- Windows/live-provider/screenshot/Longleaf是否都是不同 project invariant，不能误删。

### Mica
- testing budget / tiers / focused-before-full-E2E 是否有可合并重复；
- real long conversation 是否明确是 manual acceptance，而不是自动 authenticated loop。

### Asteria
- root是否过度复制 canonical Browser contract；
- fixed public runtime exact commands是否应移到 deeper operational doc；
- `prompts/AGENT_RULES.md` 已有 visual self-QA/scientific graph/generic-fix，root是否应主要做 locator。

### SeminarArc
- device/environment details是否与 `docs/DEVICE_TESTING.md` 重复；
- 哪些 physical-device constraints必须留 root作为高风险 summary；
- 任何 move 前是否确保详细规则仍有 canonical owner。

### CUHK Date
- 没有 root AGENTS 时是否应保持现状，而不是为统一格式创建一个空壳。

## 五、审 shared style 是否合适

Planner proposes a common structural style but not identical content.

请判断以下原则是否最小充分：

- root AGENTS = map + hard project invariants；
- deeper docs = volatile operational detail / long procedures / historical evidence；
- one concept per bullet；
- explicit canonical locators；
- no bulk translation solely for uniformity；
- managed Bridge blocks不手改；
- no deletion solely to meet line/byte target；
- semantic preservation table before rewrite.

若你认为某项会产生无价值文档工作，要求删除。

## 六、审 validation H1-H6

重点判断 gates 是否证明真实 instruction quality，而不是字数下降：

- H1 semantic preservation；
- H2 no internal contradiction；
- H3 discoverability；
- H4 managed-block integrity；
- H5 context-size improvement without numeric gaming；
- H6 repo-specific regression review。

不要新增一堆机械 gate。

## 七、审与056关系

Planner建议：

- 先不要发送已经 PASS 的056 Kickoff；
- 057作为独立 task先完成；
- 057完成后，对056只做一次 source-drift revalidation；
- semantics-preserving则不重新设计v6；
- 若 057 实质改变056假设，才回 Planner/Critic。

请判断这个 sequencing 是否合理，还是会制造不必要循环。

## 八、结论

如果有 blocker：`RESULT = REVISE`，按 Critic contract 自动附完整 Planner返修prompt。

如果可执行：`RESULT = PASS`，但 PASS 只允许 Planner准备 057 execution package；不代表用户已授权 Codex修改各 repo AGENTS。

最终至少给：

```text
RESULT = PASS | REVISE
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/design/057_REPO_AGENTS_HYGIENE_PROPOSAL_2026-09-17.md
READY_FOR_EXECUTION_PLAN = YES | NO
NEXT_HANDOFF = PLANNER
```
