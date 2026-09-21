# Project Thread Handoff — Implementation Plan v0.1

日期：2026-09-21  
状态：READY_FOR_EXECUTION_CRITIC_REVIEW  
Task key：`science-communication--project-thread-handoff`  
Human label：Project Thread Handoff V1 implementation  
Approved design authority：`docs/design/PROJECT_THREAD_HANDOFF_V3_PROPOSAL_2026-09-21.md` V3  
Approved design commit：`164f028b76da265b117e42cfbda1563cd4abb809`  
Planning source baseline：`main@fe4351d0606488abfb5247f0bc172cab6c2c5905`  
Canonical Goal：`docs/goals/PROJECT_THREAD_HANDOFF_GOAL_V0_1.md` v0.1  
Kickoff Draft：`docs/operations/prompts/PROJECT_THREAD_HANDOFF_KICKOFF_V0_1.md` v0.1

本 Plan 只把已通过的 V3 设计冻结成可执行合同，不重新设计 architecture。只有独立 Critic
对 V3 Proposal + 本 Plan + Goal + Kickoff 同版给出 `READY_FOR_CODEX=YES`，且用户随后
实际发送 approved Kickoff，才允许 Executor 开始 implementation。

## 1. Latest-main drift 与 source authority

从 V3 approved commit `164f028...` 到 planning baseline `fe4351d...`，main 只新增另一项
`scientific-pdf-rendering` 的 docs-only Proposal/Goal/Kickoff；没有修改 Project Thread Handoff、
AGENTS、Planner/Critic contracts、Skill authoring、version policy、Skill metadata contract 或
production Skill source。

因此 V3 authority 保持有效。Executor kickoff 时仍必须：

1. `git fetch origin main`；
2. 读取 current `origin/main` 的 `AGENTS.md`、version policy、Skill authoring contract；
3. 确认 approved V3 commit 仍是 ancestor；
4. 若只是无关 docs/evidence drift，继续；
5. 若出现与 Project Thread Handoff production scope、Skill metadata contract、taxonomy、
   version/release semantics 直接冲突的新事实，停止并返回 Planner/Critic。

## 2. Exact execution identity

本任务不创建新的 automation/watcher/CURRENT/state machine。它只使用 repository 的独立
reviewed branch 命名约定和人工 Planner/Critic review。

Exact task key：

`science-communication--project-thread-handoff`

Exact implementation branch：

`reviewed/science-communication--project-thread-handoff`

Exact task-owned worktree locator：

`../AI_Skills_Collection-science-communication-project-thread-handoff`

解析规则：

- 以上路径以 verified canonical `AI_Skills_Collection` checkout root 为基准；
- canonical root 由 `git rev-parse --show-toplevel` 确认；
- worktree 必须解析到 canonical root 父目录下 basename 精确为
  `AI_Skills_Collection-science-communication-project-thread-handoff` 的唯一 sibling；
- 不允许 `/tmp` clone、第二个 worktree、自选备用路径或另一个 branch；
- exact locator 已存在时，只有 repo identity 与 exact branch 都匹配才可复用；
- 被占用或身份不匹配时停止，不自动选择替代位置。

用户实际发送 approved Kickoff 后，才授权创建/使用上述 exact branch/worktree，并在该 branch
执行普通 task-owned edit/test/commit/non-force push。该授权不扩大为任意 `reviewed/*`。

## 3. Owner 与 handoff

Implementation owner：

- Codex Executor，在 exact task branch/worktree 内实现冻结 Goal。

Design owner：

- 当前长期 Planner；架构语义只能来自 approved V3。

Independent review owner：

- 独立 Critic thread。

Target-surface acceptance owner：

- 用户当前 Pro ChatGPT account；用户只负责最后一次必要 regular-Chat acceptance session。

Evidence paths：

```text
results/science-communication--project-thread-handoff/result.md
results/science-communication--project-thread-handoff/MANIFEST.md
results/science-communication--project-thread-handoff/target-surface-acceptance.md
results/science-communication--project-thread-handoff/review.md
```

`target-surface-acceptance.md` 只保存非敏感 receipt：final candidate commit、Skill package hash、
target surface、实际 invocation entry 类型、G1/G2 PASS/FAIL 与必要的最小事实。不得把 DII 私有
thread 全文或完整敏感 handoff Prompt 提交到公开 repo。

若独立 Critic 无法直接访问 target acceptance thread，可使用用户提供的一次最小 redacted
output/screenshot 作为补证；不得要求重新安装或重新跑一遍来解决 evidence transport。

## 4. Production source scope

允许新增：

```text
skills/science/communication/project-thread-handoff/SKILL.md
skills/science/communication/project-thread-handoff/agents/openai.yaml
skills/science/communication/project-thread-handoff/evals/trigger_queries.json
tests/test_project_thread_handoff_contract.py
```

只有实际需要时才允许新增最小 fixture：

`tests/fixtures/project_thread_handoff/`

Skill source 必须保持轻量。不得因为测试方便新增 scripts、database、schema、state、history store、
browser automation 或 external service adapter。

不得修改：

- Bridge Kit production source；
- CAT-TRACE / DII / CardiacNexus production repos；
- 任一中央 Plugin source；
- Mica；
- browser extension；
- workflow-core / Reviewed Handoff production behavior。

## 5. Skill source contract

### 5.1 SKILL.md

必须实现 V3 已批准的核心行为：

- explicit invocation 后一次性输出一个新 thread initialization Prompt；
- latest explicit user/frozen decision 优先于 assistant brainstorming；
- thread-only delta 只覆盖研究意图/路线/命名/下一步，不伪造实验/代码/runtime facts；
- active hypothesis / open question / rejected recurrence risk / stale history 按 V3 规则裁剪；
- entity-role disambiguation；
- canonical facts 优先给 locator；
- unknown path/SHA 不编造；
- repo/Deep Research 等可重新恢复事实不大段复制；
- no repo write；
- no second confirmation；
- minimum sufficient information；
- 800–1800 中文字只作经验范围，约 2500 为软上限而非机械阈值。

### 5.2 agents/openai.yaml

必须包含：

```yaml
policy:
  allow_implicit_invocation: false
```

Invocation policy 不写入普通 `SKILL.md` frontmatter。

ChatGPT normal-entry contract 只写“当前账号实际提供的正式显式 Skill
selection/mention/invocation entry”，不硬编码 `$`、`@` 或 `/` 为唯一 ChatGPT syntax。

不声明 MCP dependency。

### 5.3 trigger eval

Positive 只覆盖正式显式 Skill invocation 场景。

Negative / near-miss 至少覆盖：

- “总结一下当前项目”
- “我们现在做到哪了”
- “帮我继续研究”
- “handoff 是什么意思”

普通自然语言 conversation 不应靠 implicit routing 进入该 Skill。

## 6. Focused tests 与 mechanical validation

新增 `tests/test_project_thread_handoff_contract.py`，至少检查：

- expected source path / metadata structure；
- `agents/openai.yaml -> policy.allow_implicit_invocation=false`；
- `SKILL.md` 不携带错误 invocation frontmatter；
- authority/recency contract 存在；
- thread-only delta 边界；
- locator non-fabrication；
- no repo write；
- one-output / no-confirmation contract；
- surface-neutral ChatGPT invocation wording；
- trigger eval positive/negative/near-miss 结构。

机械测试不能冒充 G2 semantic PASS。

## 7. Source-first generated parity

在 source 完成后使用仓库既有生成器，不手改 generated output。

至少执行：

```bash
python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/skills.py validate
python scripts/skills.py audit --all
```

预期 generated / derived changes 包括按生成器实际结果：

- `registry.json`
- `docs/SKILL_CATALOG.md`
- `docs/domains/research-communication.md`
- `docs/SKILL_PROVENANCE.md`
- `docs/skill_provenance_audit.json`

随后运行 Marketplace generated parity check：

```bash
python scripts/build_codex_marketplace.py --write --validate --check --path-report
```

本 standalone Skill 不进入中央 Plugin，因此中央 Marketplace plugin topology 与 plugin payload
应保持语义不变；若 generator 意外把它复制进 plugin，视为 scope regression。

最后运行 focused test + full repository suite：

```bash
python -m unittest tests.test_project_thread_handoff_contract
python -m unittest discover -s tests
```

若本机标准命令需要当前 repo 已支持的等价 Python launcher，可使用 repo contract 已允许的
runtime Python；不得因此改变测试语义。

## 8. Capability Gates

只允许 V3 的 G1/G2/G3。Implementation 不得自行新增 G4/G5；如果出现三个 Gate 无法覆盖的
新用户可见能力风险，停止并返回 Planner/Critic。

### G1 — Installation / Explicit Invocation Boundary

同一 final candidate 必须证明：

1. source/generated/provenance/registry/catalog parity；
2. `agents/openai.yaml` 合法；
3. final upload-ready Skill package 已生成并验证；
4. target Pro account 成功上传/安装 final candidate；
5. target ChatGPT regular Chat 出现实际可用的正式显式 Skill entry；
6. ordinary summary / ordinary project chat 不因 implicit routing 自动进入。

Codex `$project-thread-handoff` 仅可作 Codex compatibility evidence，不能替代 ChatGPT
regular Chat 的 G1 normal entry。

### G2 — Core Handoff Semantics / DII Target-Surface Replay

必须使用同一 final candidate，在用户当前 Pro **ChatGPT regular Chat** 的一个已有长 DII
thread 中实际调用。

必须直接证明：

- Skill 能消费该 thread 已有 context；
- 用户不用重新粘贴历史；
- DII 是当前方法学项目；
- CARE 是当前数据/数据来源；
- CARE challenge models 不恢复为当前方法候选；
- latest explicit user/frozen decision 覆盖较早 assistant exploration；
- thread-only delta 正确带走；
- canonical facts 主要给 locator；
- unknown path/SHA 不编造；
- 最终只输出一份初始化 Prompt；
- no second confirmation；
- no repo write。

如果 regular Chat 无法调用、只能 Work/Codex、或 Skill 无法读取当前 thread context：

`G2 = FAIL`

停止并返回 Planner/Critic。不得更换 surface 维持 PASS。

### G3 — Generalization / Should-not-change

在用户介入前完成。

CAT-TRACE representative regression：

- 后期冻结的模型/符号/数据决定覆盖早期探索；
- superseded route 不复活。

CardiacNexus representative regression：

- 代码、pipeline、实验数字主要重新读取 current repo；
- handoff 只传最近认知判断、open question、下一步。

同时证明：

- 不 hardcode DII/CARE；
- 不依赖 Bridge Kit。

G3 可以使用支持 standalone Skill 的开发 runtime；Codex compatibility replay可以作为 G3
开发证据，但不能用于 G1/G2 regular-Chat completion claim。

## 9. Upload-ready final package

在请求用户验收前，Executor 必须生成：

`private/exports/project-thread-handoff-v1.zip`

包结构必须是单一顶层目录：

```text
project-thread-handoff/
├── SKILL.md
├── agents/openai.yaml
└── evals/trigger_queries.json
```

不把 repo tests、results、design docs 或其他项目文件塞入上传包。

根据当前 OpenAI Skills contract，zip 应只包含一个顶层 Skill 文件夹；Executor 必须在本地解包
检查路径、文本编码和 required files，并在 `MANIFEST.md` 记录 SHA-256 与 archive file list。

`private/exports/` 可以是不跟踪的 task-local durable export，但在 G1/G2 与后续 review 完成前
不得清理 exact worktree 或该 zip；不得只把最终包留在 `/tmp`。

## 10. Candidate freeze 与用户动作

在任何 target-account 操作前必须全部完成：

- production source；
- agents metadata；
- trigger eval；
- focused contract tests；
- generated parity；
- full relevant repository tests；
- G3；
- version/README/changelog candidate closure；
- upload-ready zip；
- exact candidate commit；
- ordinary non-force push exact task branch；
- remote tip == intended candidate HEAD。

然后冻结 final candidate。此后除 evidence-only receipt 外，不得修改 Skill source、generated layer、
version、README 或 package 内容，否则 candidate 失效并必须重新走 pre-user validation。

用户只被请求一次 bounded target-surface acceptance：

> 在当前 ChatGPT Skills 页面上传/安装 `project-thread-handoff-v1.zip`，然后回到已有 DII
> regular Chat thread，用该账号当前界面实际可见的正式显式 Skill 入口调用一次
> Project Thread Handoff。

同一次 acceptance session 中完成：

- G1 target-account install / explicit-entry observation；
- ordinary Chat no-implicit observation（若需要 target surface 观察）；
- G2 DII/CARE replay。

不要求第二次上传，不为了测试不同字符入口要求 `$`/`@`/`/` 各跑一次。

如果仅 target-surface 才能发现的真实 product failure 导致 G1/G2 FAIL，不自动 retry、不偷偷修后
继续；保留失败证据并回 Planner/Critic。修复后的新 candidate 如需再次 target-surface 验收，
属于恢复路径，不得把第一次失败从记录中抹掉。

## 11. Evidence 与 privacy

Executor 在用户操作前写：

- `result.md`：implementation、tests、G3、candidate commit、package hash、G1/G2=PENDING；
- `MANIFEST.md`：tracked candidate/evidence/package locator；
- `target-surface-acceptance.md`：先建立非敏感 receipt skeleton，状态 PENDING。

用户 target-surface 验收后，只追加：

- target account/surface；
- final candidate identity；
- 实际显式入口类型；
- G1/G2 criterion-level PASS/FAIL；
- 必要的最小 redacted evidence locator。

不得 commit DII/CAT-TRACE/CardiacNexus 私有 thread 全文、未公开研究内容或完整敏感 prompt。

Skill source freeze 后写 evidence receipt 不改变 final candidate identity。

## 12. Repository version / changelog / README

已实际读取 `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`。

Repository bump decision：**MINOR**

当前预期：

`5.0.6 -> 5.1.0`

理由：

Project Thread Handoff 是一个新的正式 standalone user workflow。Release 后整个
AI_Skills_Collection 能完成此前 5.0.x 没有的一类直接用户任务：把长期 ChatGPT 项目 thread
通过可安装 Skill 正确 handoff 到新 thread。这符合 version policy 的
“new important formal user workflow / repository-level user capability”。

Affected central plugins：

- 全部：`NO_BUMP`
- 原因：本任务不修改任何中央 Plugin production source 或 user-facing Plugin behavior。

Version handling：

- 在 branch 修改 version 前重新读取 current `origin/main:VERSION`；
- 若仍为 `5.0.6`，candidate target 为 `5.1.0`；
- 若其他独立 release 已先改变 repository version，不得覆盖或自选新版本号，记录
  `VERSION_DRIFT` 并返回 Planner 做最小 version-target amendment；
- 不因 branch 本身存在 5.1.0 candidate 就声称 release 已发生。

Release candidate 同步更新 repository version sources、root `CHANGELOG.md` 及其 required parity。

README：

- root `README.md`：**需要更新**，至少同步 repository/CLI candidate version，并用简短人话说明
  `Project Thread Handoff` 是可单独安装的 Skill 与其用途；不得把它伪装成中央 Plugin；
- `skills/README.md`：必须检查。当前 taxonomy 已覆盖 `science/communication` 且不维护逐 skill
  清单，预期 `README checked: no update required`；只有实现后发现现文确实误导新 standalone
  Skill 安装/定位时才允许做最小修正。

## 13. Git / side-effect boundary

Approved Kickoff 发送后允许：

- `git fetch origin main`；
- exact task branch/worktree 创建或复用；
- 上述冻结 source/docs/tests/generated/version/README/changelog/results 范围内的 edit；
- local deterministic tests；
- 生成 `private/exports/project-thread-handoff-v1.zip`；
- ordinary task-owned commit；
- ordinary non-force push exact task branch；
- 读取公开 OpenAI Skill docs 做格式核对（无 paid call）。

不授权：

- merge `main`；
- force push / remote remap / destructive Git；
- tag / GitHub release / publish；
- ChatGPT account upload/install（由用户在最终 acceptance session 自己完成）；
- paid API/evaluator；
- Bridge Kit modification；
- CAT-TRACE/DII/CardiacNexus write；
- central Plugin source change；
- live-global plugin/skill mutation outside the exact test/install sandbox；
- automation/watcher；
- Plugin/MCP/database/CURRENT/state machine。

## 14. Completion semantics

Executor 不得把以下任一项单独写成 overall completion：

- source files created；
- unit tests PASS；
- registry/catalog generated；
- zip created；
- branch push；
- Codex compatibility replay；
- G3 PASS。

Candidate implementation stage 只有在用户操作前所有开发工作完成时可以报告：

`FINAL_CANDIDATE_READY_FOR_TARGET_ACCEPTANCE=YES`

但只要 G1/G2 target-surface acceptance 尚未完成：

`PROJECT_THREAD_HANDOFF_V1_READY != YES`

只有同一 frozen final candidate 的 G1 + G2 + G3 都 PASS，并经独立 final review 与后续合法
integration/release closure，才允许总体 ready claim。

## 15. Stop / recovery conditions

必须停止并返回 Planner/Critic：

- V3 architecture 需要改变；
- 需要新增 Plugin/MCP/database/state/history；
- 需要修改 Bridge Kit 或目标科研 repo；
- G1/G2 发现 regular Chat 不支持实际调用；
- Skill 无法消费当前 thread context；
- 只能 Work/Codex 成功；
- target UI 需要不同 package structure 且会实质改变 Skill contract；
- version drift 产生 release conflict；
- 三个 Gate 无法覆盖新发现的用户可见能力风险。

普通 wording、fixture、test implementation、generator parity 修复，只要不改变 V3 语义，可在同一
execution scope 内修复并重新跑开发验证，不需要用户参与。

## 16. Execution-stage success path

```text
Critic execution-ready PASS
  -> 用户发送 approved Kickoff
  -> exact branch/worktree preflight
  -> source-first implementation
  -> focused tests + generated parity + full suite
  -> G3
  -> version/README/changelog candidate closure
  -> upload-ready zip
  -> final candidate commit + push + remote verification
  -> Executor reports FINAL_CANDIDATE_READY_FOR_TARGET_ACCEPTANCE
  -> one user target-surface acceptance session
  -> G1/G2 PASS or FAIL
  -> independent final review
  -> only then integration/release decision
```
