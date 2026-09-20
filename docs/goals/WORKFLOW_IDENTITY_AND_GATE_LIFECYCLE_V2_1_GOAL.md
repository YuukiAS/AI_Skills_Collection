# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Canonical Goal v2.1

- Execution package version: `v2.1`
- Human-readable name: **工作流命名与插件回归机制完善（AI_Skills + Bridge）**
- Technical task key: `cross-repo--workflow-identity-gate-lifecycle`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Implementation Plan: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_PLAN_2026-09-20.md` v2.1
- Approved design: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md` v2.1
- Approved design commit: `ba2fc85f9c58b9b332eb07f821d1756b417fe1d1`
- Design Critic PASS: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_CRITIC_REVIEW_2026-09-20.md`
- Design Critic PASS commit: `1427c7060776719e2e1ae191b681ab2e1a608705`
- Execution is not authorized until an independent Critic passes this exact Plan + Goal + Kickoff package and the user sends the approved Kickoff.

## 1. 最终目标

把已批准 v2.1 真正接入 AI_Skills 与 Bridge 的正常生产路径，使以后新的 workflow 同时满足：

1. **机器身份清楚**：新 Reviewed Handoff canonical creation 使用 semantic task key；旧 numbered task 原样兼容，不迁移历史。
2. **人看到的名字简单**：technical task key 只在 branch/path/evidence 等必要 locator 中出现；普通 prompt、Goal、review/report heading 和交流使用短的人类名称。
3. **Gate 不随每个失败无限增长**：稳定 Gate taxonomy 下持续积累 regression bank；真正新增独立 capability 才新增/拆分 Gate。
4. **release 既防回归又不过度昂贵**：所有 release 先跑 applicable cheap deterministic known regressions；只有 isolation 可解释时才 narrow；shared/cross-cutting/impact 不清/maturity promotion 等情况强制 broad/full fallback；所有 release-critical Gate 都绑定同一 final candidate。
5. **职责不串层**：Bridge 只拥有 lexical validation/compatibility/propagation；AI Skills Maintainer 管 AI_Skills scope/regression/release closure；workflow-core 管执行语义，不实现第二 parser；domain plugin 保留专业判断。

本任务完成的对象是一个经过独立 review 的**跨 repo release candidate tuple**，不是一次文档声明。

## 2. 冻结不变量

执行不得改变以下设计：

- semantic scope precedence：
  - 多于一个 mutable canonical repo -> `cross-repo`
  - 一个 mutable AI_Skills repo + 多个中央 production plugin -> `cross-plugin`
  - 一个中央 plugin -> `plugin-<canonical-plugin-slug>`
  - 单 repo 非 plugin-wide -> `repo`
  - read-only references 不计入；
- canonical new task creation semantic-only；
- legacy validation dual-format；
- 001–057 以及其他现有 numbered task/result/branch/evidence 不 rename/migrate；
- repair/review/integration 沿用同一个 task key；
- collision fail-closed，优先 semantic disambiguation，不自动追加 UUID/date/sequence；
- G1–G7，不新增 G8；
- same-final-candidate；
- stable Gate taxonomy + growing regression bank；
- Gate merge/split/retirement 保留历史 obligation；
- narrow/broad-full fallback 的批准触发条件；
- no task `display_name` schema/registry/title service；
- 不新增 controller/watcher/database/registry/ledger/state machine；
- 不做 docs directory reorganization；
- 不控制 ChatGPT/Codex 客户端自动 conversation/sidebar title。

## 3. 执行前 source/version preflight

用户发送获批 Kickoff 后，在任何 production mutation 之前重新核对：

### AI_Skills

Expected baseline compatible with:

`main@1427c7060776719e2e1ae191b681ab2e1a608705`

Expected versions:

```text
Repository 5.0.5
workflow-core 0.1
ai-skills-core 0.2
```

### Bridge

Expected baseline compatible with:

`main@afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`

Expected version:

`0.8.3`

如果 kickoff 时相关 source/version 已被 056 或其他任务实质改变，或计划版本槽已经被占用：

```text
STOP_BEFORE_MUTATION=YES
NEXT_OWNER=GPT_PLANNER
```

不得自行换版本号、静默合并两个方案或边执行边“适配”新架构。

## 4. 执行边界

Critic PASS 后，用户发送 approved Kickoff 时才授权创建：

### AI_Skills_Collection

- branch: `reviewed/cross-repo--workflow-identity-gate-lifecycle`
- worktree: `/tmp/ai-skills-workflow-identity-gate-lifecycle`

### GPT_Codex_AI_Bridge_Kit

- branch: `reviewed/cross-repo--workflow-identity-gate-lifecycle`
- worktree: `/tmp/bridge-workflow-identity-gate-lifecycle`

只允许 ordinary non-force push 到这两个 exact task branches。

不创建 PR，不 merge main，不改 remote/upstream，不 force push，不 tag/release/publish/deploy，不删除 branch。

### Cutover bootstrap

当前 Bridge 尚不能 canonical-create semantic Reviewed Handoff task。因此本 cutover implementation：

- 不创建新的 0xx task 来绕过；
- 不伪造 semantic CURRENT；
- 用获批 Plan/Goal/Kickoff + exact semantic branches 作为本轮执行合同；
- Bridge candidate 完成后，只在 isolated temporary fixture repo 中用 candidate CLI 证明 semantic normal entry；
- 不为了“自举”给本任务补一个历史式 numeric identity。

## 5. Bridge 必须完成的实现

只改 semantic/legacy lexical validation、canonical creation、generic validation 与 identity propagation。

必须：

1. 建立一个 canonical task-key lexical authority/helper 或等价单一实现，供 creation/validation consumers 复用；
2. lexical semantic key 支持 `<scope-token>--<goal-token>` 的 lowercase kebab components、唯一分隔、长度/path/Git 安全边界；
3. Bridge 不判断 AI_Skills plugin slug 或 semantic scope；
4. `reviewed-handoff task init` 新建只接受 semantic key，拒绝 numeric new key；
5. generic/existing-workspace validation 接受 legacy + semantic；
6. collision fail closed；
7. semantic key 无损进入：
   - task directory
   - result directory
   - `reviewed/<task_key>`
   - CURRENT / PLAN / RESULT / REVIEW / FINAL_REPORT
   - task-bound Planner/Reviewer/Executor consumers
   - Text Review manifest/evidence
   - Visual Review manifest/evidence；
8. 最小更新正常 authoring docs/templates，使新任务默认不再写 0xx；
9. 历史 numbered examples/tasks 留作 legacy compatibility，不 mass-rename；
10. 不修改 Review roles/states/schema。

## 6. AI_Skills 必须完成的实现

### Capability Gate policy

`PLUGIN_CAPABILITY_GATE_POLICY.md` 必须正式吸收 v2.1：

- stable Gate taxonomy / growing regression bank；
- existing capability failure 默认进已有 Gate regression；
- 真正不同 capability/evidence/failure semantics 才新增或拆 Gate；
- merge/split/retirement obligation mapping；
- applicable cheap deterministic bank；
- narrow eligibility；
- mandatory broad/full fallback triggers；
- same-final-candidate；
- grader/eval semantics change handling；
- no fixed fresh/manual/paid count；
- no impact registry/dependency DB/ledger。

### AI_Skills scope + human naming

`AGENTS.md`、Planner/Critic contracts 只增加必要 consumer rules：

- scope precedence；
- technical key 作为 locator；
- human-readable short label 作为可控正文/heading 默认名称；
- frozen single-plugin release 可用 `Clear Writing 0.4`；
- unfrozen release 用 `Clear Writing 发布收口`；
- broad workflow 可用 `开发交付流程完善（AI_Skills + Bridge）`；
- 不新增 task display-name 数据模型；
- 不声称控制客户端自动 title。

### workflow-core

Verified Workflow 必须能够执行：

- affected Gate 识别；
- cheap bank first；
- narrow eligibility；
- mandatory broad/full fallback；
- same-final-candidate；
- should-not-change；
- human-readable reporting；
- domain routing。

其 reusable task template 不再把 `<id>_<short_slug>` 当作新任务 contract；只引用 canonical Bridge task-key contract。

workflow-core 不实现 parser。

### AI Skills Maintainer

必须能够：

- 应用 AI_Skills scope precedence；
- triage regression into existing Gate before proposing new Gate；
- 识别真正需要 Gate redesign 的新 capability；
- 应用 narrow/broad release selection；
- 保持 source/generated/version/changelog/replay closure；
- 普通文字用 human short label；
- 专业判断仍交 domain plugin。

## 7. 本轮 release selection

本任务自身属于：

`BROAD_FULL_FALLBACK`

原因：同时修改 normal-entry task creation/validation、shared workflow policy、workflow-core 与 maintenance consumer，并跨 AI_Skills + Bridge。

不得改成 narrow。

## 8. G1–G7 验收

### G1 — Semantic creation & lexical identity

在 isolated temp repo 用 candidate Bridge 正常命令证明：

- semantic task init PASS；
- malformed semantic FAIL；
- collision FAIL；
- new numeric init FAIL。

### G2 — Identity propagation

同一个 semantic key 必须无损覆盖：

```text
automation/reviewed_handoff/tasks/<task_key>/
results/<task_key>/
reviewed/<task_key>
CURRENT
PLAN
RESULT
REVIEW
FINAL_REPORT
Text Review manifest/evidence
Visual Review manifest/evidence
task-bound Planner/Reviewer/Executor paths
```

### G3 — Scope clarity

AI_Skills consumer evidence必须覆盖：

- one plugin；
- one repo / multi plugin；
- repo-wide non-plugin；
- multi mutable repo；
- multiple read-only refs 不升级 scope；
- 056-like case -> `cross-repo`。

Bridge 不判断 semantic ownership。

### G4 — Legacy coexistence

同一 isolated workspace：

- seeded legal legacy numbered task 可 validation；
- semantic task 可 normal create；
- generic validation PASS；
- new numeric canonical create FAIL。

### G5 — Gate lifecycle

必须证明：

- existing-capability regression 加入现有 Gate，不机械新增 Gate；
- contrasting genuinely new capability 会触发 Gate redesign consideration；
- merge/split/retirement 不删除 obligation。

### G6 — Release regression safety

必须证明：

- isolated local change 可以在满足条件时 narrow；
- shared prompt/assembly、model/runtime/provider/router、normal entry/install/invocation、multi-Gate shared layer、impact 不清、新 failure 未归因、grader/eval semantics change、maturity promotion均触发 broad/full；
- same-final-candidate 不被 canary/旧 PASS 替代。

### G7 — No governance bloat

最终 diff 必须证明没有新增：

- controller
- watcher
- database
- registry
- ledger
- state machine
- task display-name service/schema
- second task-key parser
- docs layout migration。

## 9. AI_Skills production replay

在 candidate source/generated layer 稳定后，最多两次 public-safe candidate plugin replay：

1. **Verified Workflow**：验证 narrow vs broad/full、same-final-candidate、不固定 paid/fresh count；
2. **AI Skills Maintainer**：验证 scope precedence、Gate regression triage、human label vs technical locator、domain ownership。

不使用 private data，不调用 Terra/OpenAI Responses，不增加 paid-review budget。

若 replay 失败，只能按 frozen architecture 修复并重跑受影响 replay；不得扩样本追赢家。

## 10. 测试与生成层

### Bridge

必须完成：

- focused semantic/legacy/cutover tests；
- reviewed-runner/Text Review/Visual Review affected regressions；
- generic workspace validation compatibility；
- full unit suite；
- version/docs consistency。

### AI_Skills

必须完成：

- focused workflow identity/Gate lifecycle contract tests；
- source/generated parity；
- canonical Marketplace generator；
- `scripts/skills.py validate`；
- `scripts/skills.py audit --all`；
- affected version/changelog consistency；
- full unit suite；
- 两次 bounded candidate plugin replay。

机械 tests 只能证明对应机械性质，不能代替 replay 与独立 review。

## 11. Final candidate tuple

生产 source、generated payload、version metadata 冻结后记录：

```text
AI_SKILLS_FINAL_CANDIDATE_COMMIT=<sha>
BRIDGE_FINAL_CANDIDATE_COMMIT=<sha>
```

G1–G7 的 release-critical evidence 必须绑定该 exact tuple。

冻结后如果任一 repo 再改 production/source/generated/version/acceptance semantics，旧 tuple 失效；不得拼接旧证据。

## 12. Version closure

若 kickoff preflight 仍是当前 tuple：

### AI_Skills

```text
Repository: 5.0.5 -> 5.0.6 PATCH
workflow-core: 0.1 -> 0.2
ai-skills-core: 0.2 -> 0.3
all other plugins: NO_BUMP
```

必须更新 affected plugin changelogs、root release metadata、README/generated parity。

### Bridge

`0.8.3 -> 0.8.4` compatible candidate。

不得因为 slot 被占用自行选择下一版本；发生 drift 返回 Planner。

## 13. 人类可读验收

普通报告/标题默认写：

**工作流命名与插件回归机制完善（AI_Skills + Bridge）**

而不是把：

`cross-repo--workflow-identity-gate-lifecycle`

当作主标题反复展示。

technical key 可以在一次 locator block、branch/path、evidence appendix 中精确出现。

不验证、不声称控制客户端自动 sidebar/conversation title。

## 14. 恢复规则

- source/version drift before mutation -> stop, Planner；
- frozen scope 内普通 bug/test failure -> Executor 修；
- semantic propagation failure -> G2 implementation repair；
- legacy validation regression -> G4 repair，不迁历史；
- candidate replay failure -> 先查 source/generated/install/consumer/fixture，再做 bounded repair；
- 需要改变 Gate taxonomy/ownership/parser responsibility/state/recovery semantics -> stop, Planner/Critic；
- unrelated suite failure -> 归因，不顺手扩大产品范围；
- 不 blind retry，不 adaptive sample chasing。

## 15. Executor 停止点

本次 Kickoff 授权到**implementation candidate + evidence + push + independent review handoff**，不授权集成发布。

Executor 只有在以下完成后才可停止并报告：

- 两 repo exact task branches/worktrees已按批准范围使用；
- source/generated/version candidate完整；
- G1–G7 evidence完整；
- full tests与两次 bounded replay完成；
- final candidate tuple冻结；
- task-owned evidence已进入 repo；
- exact task branches已普通 non-force push；
- remote tips等于 intended candidate；
- working trees不含未说明 task-owned更改；
- ZERO forbidden side effects。

随后：

`NEXT_OWNER=INDEPENDENT_IMPLEMENTATION_REVIEW`

不得声称 main release/overall deployment complete。

## 16. 本 Goal 明确不做

- 不迁 001–057；
- 不修改 056；
- 不改 domain plugin 专业行为；
- 不新增第二 parser；
- 不新增 registry/database/ledger/controller/watcher/state machine；
- 不做 docs directory reorganization；
- 不新增 task display_name field/title service；
- 不 hack client title；
- 不用 paid API；
- 不改真实 Host Policy；
- 不创建 PR；
- 不 merge main；
- 不 tag/release/publish/deploy；
- 不 force push / remote mutation / destructive Git；
- 不把 final artifact/evidence只留在 `/tmp`。
