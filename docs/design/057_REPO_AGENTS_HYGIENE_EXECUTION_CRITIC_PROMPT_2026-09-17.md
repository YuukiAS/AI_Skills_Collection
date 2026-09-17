# 057 Repo AGENTS Hygiene — Execution Package Critic Prompt

你是 AI Research Stack 的长期独立 Critic thread。

继续：

`TASK_KEY = 057_repo_agents_hygiene`

本轮审查阶段：execution-ready package review。

当前 design authority：

`docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`

当前 exact execution review objects：

1. `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` v0.1
2. `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` v0.1
3. `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md` v0.1
4. `docs/design/057_REPO_AGENTS_HYGIENE_REVIEW_PACKAGE.md`

本轮只审 execution package。不要修改产品 repo/AGENTS，不修改 Bridge Kit production，不创建 branch/worktree，不启动 Executor，不运行 paid API，不代用户发送 Kickoff。

只有你明确给出：

```text
RESULT = PASS
READY_FOR_CODEX = YES
```

并且用户之后实际发送你审过的 exact Kickoff，才允许执行。

## 一、强制读取 current authority

先读取 AI_Skills_Collection 最新 main：

- `AGENTS.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- `docs/design/057_REPO_AGENTS_HYGIENE_REVIEW_PACKAGE.md`
- `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md`
- `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md`
- `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md`

同时读取 056 current v0.2 package，仅用于确认 057 sequencing/overlap 边界没有偷改已经批准的 056 架构；不要重新设计 056。

## 二、重新核对真实 repo source

### Bridge Kit current main

至少读取：

- `AGENTS.md`
- `ai_bridge_kit/cli.py`
- `ai_bridge_kit/__init__.py`
- `codex/AGENTS_SNIPPET.md`
- `templates/prompts/AGENT_RULES.md`
- relevant init/validate tests
- README / CHANGELOG current version policy

重点确认：

- fresh repo 当前确实只有 managed block；
- existing repo 当前只 append/update managed block；
- proposed scaffold wiring不需要新 migration engine；
- current version仍适合以 compatible PATCH 形成 `0.8.3` candidate；
- `--force` 不应获得重写 user-owned AGENTS 的新语义。

### Bobbio current develop

至少读取：

- `AGENTS.md`
- `docs/DEVELOPMENT_WORKFLOW.md`
- `docs/design/FIGMA_HANDOFF.md`
- `docs/PRODUCT_DESIGN_BRIEF.md`
- `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md`

检查 execution scope 是否能解决 Figma-vs-old-images authority ambiguity，又不删除 Zotero/native/knowledge/iPad rules。

### Lucerna current main

- `AGENTS.md`
- `prompts/AGENT_RULES.md`

确认 package 的 light-edit disposition 没有误删 distinct Windows/provider/screenshot/Longleaf owners。

### Mica current main

- `AGENTS.md`
- `docs/PHASE_1_LONG_THREAD_RECOVERY.md`
- `docs/VERSIONING.md`

确认 testing consolidation 可以减少重复，又保留 real-site/account/typing boundaries。

### Asteria current main

至少：

- `AGENTS.md`
- `prompts/AGENT_RULES.md`
- `docs/operations/blackbox-audit/UI_BLACKBOX_BROWSER_CONTRACT.md`
- `docs/operations/development/DEVELOPER_VISUAL_SELF_QA_CONTRACT.md`
- `docs/design/SCIENTIFIC_GRAPH_VISUAL_SYSTEM.md`
- current `docs/operations/development/` inventory

重点审新 `docs/operations/development/RUNTIME_OPERATIONS.md` 是否是必要且最小的 canonical owner，而不是新建第二份手册。

### SeminarArc current main

至少：

- `AGENTS.md`
- `prompts/AGENT_RULES.md`
- `docs/DEVICE_TESTING.md`

确认详细 device/environment/safety内容移到现有 `DEVICE_TESTING.md` 能保留所有 unique protections；若不能，不应允许 Executor自行再造第三份 environment policy。

### CUHK Date current main

- 确认 root `AGENTS.md` 是否存在
- 读取 `docs/design/prototype/AGENTS.md`

确认 inspect-only/no-root-creation 仍正确。

## 三、独立外部核查

本轮仍是 substantive execution review。独立核查当前 OpenAI/Codex primary sources，至少确认：

- current Codex project instruction / AGENTS context behavior；
- current OpenAI harness-engineering guidance 对 short root map / deeper docs 的现实依据。

不要因为“短 AGENTS”流行就接受任何 safety-rule deletion。外部资料只用于判断 progressive disclosure 的合理边界。

## 四、审 execution scope 是否最小充分

重点攻击两边。

### 过重风险

- 7 个 repo task branch/worktree 是否不必要；
- Bobbio 本来 normal work走develop，057是否确实因 repo-wide policy rewrite值得临时隔离；
- Asteria是否不必要地创建新 operations doc；
- SeminarArc是否把一个现有 DEVICE_TESTING 又拆出新手册；
- Bridge scaffold是否变成新的 policy engine；
- 是否大规模翻译/统一措辞而没有真实收益；
- H1–H9 是否变成机械 paperwork。

### 过简风险

- preservation table只填表不真正追踪所有 hard rules；
- Bobbio authority conflict仍可能残留；
- Asteria/SeminarArc move后 detail丢失；
- Mica只是删段落但测试语义仍冲突；
- Bridge template存在但真实 `ai-bridge init` 不消费；
- force init仍可能重写 existing project-owned prose；
- root scaffold又复制 `prompts/AGENT_RULES.md`。

如果有更简单办法可以保持独立 review/rollback和语义安全，请要求最小修订。

## 五、审 Git/source strategy

Package拟在执行授权后创建：

- AI_Skills `reviewed/057_repo_agents_hygiene`
- Bridge `reviewed/057_repo_agents_hygiene`
- Bobbio `reviewed/057_repo_agents_hygiene` from develop
- Lucerna/Mica/Asteria/SeminarArc 同名 task branch from current main

CUHK Date read-only。

审：

- branch isolation是否和各 repo policy兼容；
- ordinary commit/push是否被严格限定到 exact task branch；
- no merge before independent implementation review是否足够安全；
- local-first source discovery是否保护 unrelated dirty state；
- 不得 remote remap/force push/history rewrite。

如果某 repo 的 branch policy不允许该隔离方式，给最小替代；不要顺便重构其 Git workflow。

## 六、审 Bridge scaffold contract

必须证明真实 normal entry，不是文件存在：

### Fresh repo

`ai-bridge init -> ai-bridge validate`

应该得到：

- canonical scaffold；
- exactly one managed Bridge block；
- `prompts/AGENT_RULES.md` locator；
- 无 fabricated project facts；
- 无 Lite duplication。

### Existing repo

normal init 和 force init：

- project-owned root prose byte-for-byte保留（managed block之外）；
- 不自动 scaffold migration/reformat；
- managed block仍由 canonical snippet生成；
- second init idempotent。

判断 `templates/repo/AGENTS_TEMPLATE.md` + 小幅 `cli.py` 修改是否最小充分。禁止通过新 migration subsystem 实现。

## 七、逐 repo审 preservation / authority closure

### Bobbio

必须看到 package明确要求：

- Figma handoff = current canonical visual source；
- Product Design Brief = durable product/interaction contract；
- old PNGs = historical/supporting references；
- general GUI/human/pre-user repetition可以合并；
- Zotero/native/knowledge/iPad safety/invariants必须保留。

### Lucerna

light edit only；distinct project owners不被 generic 化。

### Mica

focused/full-E2E重复收敛；manual authenticated final acceptance与禁止automated authenticated loop被明确区分。

### Asteria

root变成 map，但 fixed public entry / browser contract / GPT Work-before-human / visual-scientific locator仍显眼；runtime detail新doc是单一 canonical owner。

### SeminarArc

root仍显眼保留 protected-device hard summary；DEVICE_TESTING收纳 detail后不会导致 agent必须先猜 locator才能知道高风险禁令。

### CUHK Date

no change；不因scaffold存在就retroactively创建root。

## 八、审 H1–H9 是否证明不同真实行为

H1 semantic preservation
H2 no internal contradiction
H3 discoverability
H4 managed-block integrity
H5 context quality
H6 repo-specific regression
H7 fresh scaffold normal entry
H8 existing-repo should-not-change
H9 no Lite duplication

重点：

- H1不能只数preservation-table行；必须对final diff有语义映射；
- H3不能只检查path字符串存在；Reviewer应能从root实际定位canonical owner；
- H5 line/byte下降不是quality proxy；
- H7/H8必须走真实 init behavior；
- H9确保未来不会出现 root Lite + prompts Lite 两份authority。

不要新增 H10，除非有明确独立 failure mode。

## 九、审 version/release boundary

Current Bridge version是 `0.8.2`。

Plan拟：

- 只有 scaffold normal entry、existing preservation、full regression通过后才形成 `0.8.3` candidate；
- product repos不bump runtime version；
- AI_Skills不做 repository/plugin release；
- task branches不直接 merge/release。

判断这是否符合 current Bridge release policy。

如果 057最终使用 `0.8.3`，056以后应通过 source-drift revalidation选择 next valid Bridge patch，不得复用同一version slot。

## 十、审与056的 sequencing

确认 execution package严格保持：

```text
057 implementation
-> independent implementation review
-> separately approved integration
-> Planner bounded 056 source-drift revalidation
-> amend duplicate work/source refs/version slot
-> no v6 redesign unless frozen assumption actually false
```

057 Executor不得编辑/执行056。

Critic若认为这个 sequencing会造成无价值循环，必须指出具体可以省掉哪一步而不牺牲 source identity / review safety。

## 十一、final candidate / recovery

审跨 repo final manifest是否足够：

- Bridge commit/version
- Bobbio/Lucerna/Mica/Asteria/SeminarArc commits
- CUHK Date inspected ref
- AI_Skills result commit
- H1–H9 evidence locators

检查 recovery：

- preservation不能证明时保留pre-057 baseline；
- dirty instruction files不覆盖；
- managed-block drift不手改；
- H7/H8/H9失败不bump Bridge；
- 不通过降低semantic bar制造“更短”的PASS。

## 十二、结论

若 package 仍需实质修改：

```text
RESULT = REVISE
TASK_KEY = 057_repo_agents_hygiene
REVIEW_PACKAGE_VERSION = v0.1
READY_FOR_CODEX = NO
NEXT_HANDOFF = PLANNER
```

并按 Critic contract自动附完整 Planner返修prompt。

若 package 可执行：

先用正常中文说明这个 execution package最终会怎样整理各 repo、Bridge scaffold怎样工作、H1–H9分别证明什么，以及用户发送Kickoff后仍不会发生什么（无product/runtime、无main merge、无056执行）。

然后给：

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_PACKAGE_VERSION = v0.1
PLAN = docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md
GOAL = docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md
KICKOFF = docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md
READY_FOR_CODEX = YES
```

并逐字返回已审 Kickoff 的 `## Kickoff` 正文：

```text
=== APPROVED 057 KICKOFF BEGIN ===
<verbatim reviewed kickoff>
=== APPROVED 057 KICKOFF END ===
```

不要 PASS 后临场改写一份新的 Kickoff。

`NEXT_HANDOFF = USER_SENDS_APPROVED_KICKOFF`
