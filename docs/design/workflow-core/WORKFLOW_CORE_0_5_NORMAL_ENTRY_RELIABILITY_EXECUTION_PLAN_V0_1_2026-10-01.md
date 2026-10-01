# workflow-core 0.5 正常入口可靠性执行 Plan v0.1

日期：2026-10-01
角色：AI Research Stack Planner
状态：EXECUTION PACKAGE — WAITING FOR EXECUTION-READY CRITIC
目标仓库：`YuukiAS/AI_Skills_Collection`
目标插件：`workflow-core / Verified Workflow`
task key：`workflow-core--normal-entry-reliability`

设计 authority：
- Approved Proposal：`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md`
- Approved Proposal commit：`de66a18123059f76fd0ead4aa715f84ad066c62b`
- Design Critic：PASS
- 已关闭：`WC05-D1`–`WC05-D7`

本 Plan 只把已批准 V0.4 转成可执行合同，不重新设计 architecture。

## 1. 本轮交付

只实现 V0.4 已批准的三个 production change：

1. 精确且克制的 normal-entry discovery / trigger；
2. specialist-first targeted capability discovery；
3. 六维全满足、fail-closed 的 fallback equivalence。

G1–G5 capability semantics、same-final-candidate requirement、specialist-contained hard negative、true capability-absent contrast、不可拆分 G4 replay 均按 V0.4 原样执行。

明确不做：
- Longleaf `/users`、module、conda、TeX 环境架构；
- STAT5060 source / course material；
- `render-chinese-math-pdf` 或其他 specialist 的 production rewrite；
- Bridge Kit runtime / Host Policy；
- #7/#8/#9/#10 专属逻辑；
- 新 workflow / state / schema / watcher / daemon；
- paid API / Text Review / Visual Review / Terra；
- task-specific production hardcode。

## 2. Maintenance companion

本任务是中央 production plugin refinement，执行时必须同时消费：

- `workflow-core`：流程、routing、evidence、completion semantics；
- `ai-skills-core` / `ai-skills-repository-maintainer`：source authority、generated parity、candidate replay、regression、version/changelog/release closure。

`ai-skills-core` 必须显式调用，不靠 implicit trigger。执行开始时记录实际 installed identity/version；仅阅读 source `SKILL.md` 不算 production invocation evidence。

本任务没有第三个 target-domain plugin。具体 regression 中需要 render / statistics / browser specialist 时，只消费其现有正式合同，不修改它们。

## 3. Execution topology：采用 Reviewed Handoff，但不假设自动角色可用

采用 Reviewed Handoff 的原因只有 branch/worktree isolation、task-local evidence、CI/review handoff；不新增 workflow。

冻结 identity：
- canonical repo：`YuukiAS/AI_Skills_Collection`
- canonical checkout：`/home/yuukias/AI_Skills_Collection`
- task key：`workflow-core--normal-entry-reliability`
- branch：`reviewed/workflow-core--normal-entry-reliability`
- worktree：`/home/yuukias/AI_Skills_Collection-workflow-core--normal-entry-reliability`
- base branch：`main`
- `ci_required=true`
- visual/text review：false
- max review rounds：2

上述 checkout/worktree 是本 package 明确选择的执行 locator；不是“从旧记录推断当前机器已健康”。执行前必须真实验证 canonical checkout、origin identity、Bridge capability 和 path availability。若该绝对路径在执行环境不存在、repo identity 不匹配或用户实际要换机器，停止并回 Planner 修 locator；不得自行换 `/tmp`、第二 clone、其他 worktree 或另一个机器。

Bridge source baseline：`YuukiAS/GPT_Codex_AI_Bridge_Kit@5a640ec02a20106c778a35ba94eb2164d2b91537`（0.9.3 main observed during package preparation）。

正常 bootstrap：
1. 在 canonical checkout 做 `git fetch origin main`。
2. 确认 post-sync `origin/main` 包含本 execution package commit，且 approved Proposal/Plan/Goal/Kickoff 内容未漂移。
3. 使用 `ai-bridge reviewed-handoff task bootstrap`，不得 raw `git worktree add`。
4. bootstrap 必须派生并验证上面 exact branch/worktree。
5. 首次 REQUEST/CURRENT 元数据 commit 后使用 `ai-bridge reviewed-handoff task publish-first`。
6. 若 task 已存在，则按 Bridge 当前 contract 走 `materialize-worktree --mode resume`，不得重复 bootstrap。

角色：
- Planner owner：本 AI Research Stack 长期 Planner thread。
- Execution-ready / pre-final Critic owner：当前独立 Critic thread。
- Executor：Codex。
- 不假设 task-bound Scheduled Planner/Reviewer 已存在；若执行环境没有已验证的自动 Planner/Reviewer transport，按人工 handoff 继续，不启动 generic watcher 冒充 task-bound automation。

若 Bridge state 在 bootstrap 后要求外部 Planner materialize `PLAN.md` / `PLAN_FROZEN`，只允许把本 Critic-approved execution Plan/Goal 机械映射进去；任何语义变化必须回 Planner/Critic。

## 4. Exact source scope

允许修改的 source authority：
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/references/escalation-rules.md`
- `skills/core/codex-system/codex-workflow-protocol/agents/openai.yaml`
- `skills/core/codex-system/codex-workflow-protocol/evals/trigger_queries.json`

允许新增/修改的 target-plugin regression：
- 新建 `tests/test_workflow_core_normal_entry_reliability.py`
- 必要时最小修改现有 `tests/test_workflow_core_reviewed_handoff_routing.py`，仅用于兼容回归，不重写其 0.4 contract。

默认不修改 `verification-matrix.md`、`task-template.md`。如果实现发现必须改它们才能满足 V0.4，停止并回 Planner；不得顺手扩 scope。

允许生成层由 canonical generator 更新：
- `plugins/codex/plugins/workflow-core/skills/workflow/SKILL.md`
- `plugins/codex/plugins/workflow-core/skills/workflow/references/escalation-rules.md`
- `plugins/codex/plugins/workflow-core/skills/workflow/agents/openai.yaml`
- `plugins/codex/plugins/workflow-core/skills/workflow/evals/trigger_queries.json`
- release 阶段必要的 `.codex-plugin/plugin.json`

允许的 maintenance/release metadata，仅在对应阶段：
- `scripts/codex_marketplace_config.json`
- `docs/plugin-changelogs/workflow-core.md`
- `VERSION`
- `CHANGELOG.md`
- `README.md`
- generated registry/catalog/Marketplace parity outputs（仅 canonical generator 产生的实际变化）。

task evidence 放：
- `results/workflow-core--normal-entry-reliability/`

最少持久 evidence：
- `GATE_CASES.json`
- `DEVELOPMENT_EVIDENCE.md`
- `PRE_FINAL_CANDIDATE_IDENTITY.md`
- `GATE_MATRIX_RESULT.md`
- `G4_NORMAL_ENTRY_TRACE.md`
- `FINAL_CANDIDATE_IDENTITY.md`
- `RELEASE_CLOSURE.md`

不得把 machine-local candidate replay cache、secret、auth、完整 runtime scratch 提交 repo。

## 5. Implementation contract

### 5.1 Trigger

根 `SKILL.md` 与 `agents/openai.yaml` 只做最小 trigger 精化。

应该进入 workflow-core：
- 多阶段实现/返修 + 验证/交付；
- 跨 specialist 或跨 artifact/runtime 协调；
- primary route / capability discovery / recovery / blocker 的 workflow-level 判断；
- acceptance / release / recovery / integration boundary。

不得进入：
- 简单命令、普通解释；
- 单一步骤工具调用；
- 复杂但 specialist-contained 的任务：只要单一 specialist 已完整拥有 route、probe、failure handling、QA 和 success definition，即使有多个步骤/render/QA，也不加载 workflow-core。

description 保持短，不把执行规则复制到 metadata。

### 5.2 Specialist-first targeted discovery

在 declared capability absent 前，只按 authority 做 targeted discovery：

1. current user / frozen task / repo canonical route；
2. matched specialist 的正式 probe/resource/wrapper/runtime；
3. project-declared module/venv/conda/runner/container/site profile；
4. current shell/PATH 只作局部证据。

`command not found`、默认 interpreter 缺包、optional flag/mode 不支持、单个 probe 失败，都不能单独证明整个 capability absent。

不得无目标扫描 home、`/overflow`、其他用户目录或整机 filesystem。

### 5.3 Six-dimension fallback equivalence

automatic fallback 只有六项全部正面证明 `UNCHANGED / COVERED` 才允许：

1. frozen effect；
2. professional quality；
3. acceptance evidence strength；
4. safety/privacy boundary；
5. artifact identity；
6. current authorization scope。

任一 `UNKNOWN`：先补 targeted evidence；仍未知则 fail closed。
任一 `CHANGED`：automatic fallback forbidden。
specialist 明确禁止的 fallback：直接禁止。
不得用一个裸 `equivalent=true` 布尔值代替六项证据。

## 6. Regression cases 与 anti-hardcode

原真实失败必须进入 regression bank，但不得进入 production hardcode：

- STAT5060：默认 PATH / default environment 被误判成 R/Python capability absent；
- Chinese math PDF：裸 XeLaTeX 缺包后未先消费 render specialist/resource route，准备 Chromium fallback；
- #8 只借 generic 事实：unsupported foreground/`visible:true` mode ≠ capability absent。

production source / generated payload 不得出现用于过题的项目专有条件，例如 `STAT5060`、`/users/a/e/aereinh`、特定 Longleaf module version、针对 gate prompt/scenario id 的条件。tests/evidence 可以保存 regression provenance，但必须验证通用机制。

## 7. 执行顺序

### Phase A — preflight / bootstrap

- 验证 repo/branch/worktree/Bridge identity；
- 验证 approved package locator；
- 显式加载 workflow-core + ai-skills-core maintenance companion；
- 确认当前 `workflow-core=0.4`，repository release package-prep 基线为 `5.4.0`；
- 若 main 在 package commit 后发生 affected-source/shared-generator/version-policy 变化，停止回 Planner；其他 drift 也必须先证明不改变本 task candidate base。

### Phase B — source-first implementation

只改 §4 source authority；不要先改 generated layer。
新增 focused tests / frozen gate cases。
source diff 必须可解释地对应三个 approved mechanisms。

### Phase C — regenerate + cheap deterministic regression

source 完成后运行 canonical generation，再依次：

1. `python -m unittest tests.test_workflow_core_normal_entry_reliability`
2. `python -m unittest tests.test_workflow_core_reviewed_handoff_routing tests.test_codex_marketplace tests.test_standalone_skill_baselines`
3. `python scripts/skills.py validate`
4. `python scripts/skills.py audit --all`
5. `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
6. `git diff --check`
7. 风险匹配的完整 unittest / CI 前置回归。

先 targeted，后 broad；不要为了一个已知小失败直接盲跑 full suite。

### Phase D — development replay，仍保持 version 0.4

冻结 `GATE_CASES.json` 后运行已知回归：

- G1 implicit/contextual positives；
- G1 specialist-contained hard negative + simple negative；
- G2 PATH-hidden/project-runner、specialist-resource、optional-mode 三类；
- G3 equivalent recovery、quality/evidence degradation、authorization unknown/changed、specialist-forbidden fallback；
- G4 positive chain 的开发回放；
- G4 true-absent fail-closed 对照。

所有涉及调用的 case 必须使用 production-compatible Codex/plugin runtime，并保存真实 consumption trace。source string/schema/test count 不算 invocation evidence。

positive G4 必须在一次 run 观察：

```text
ordinary prompt
-> workflow-core implicit consumption
-> correct specialist consumption
-> targeted capability discovery
-> correct canonical/equivalent route
-> no non-equivalent fallback
-> bounded expected outcome
```

若 specialist 与 workflow-core 分两次 run 才分别消费，G4 FAIL。

hard negative 必须证明 workflow-core candidate 已安装/可发现但没有被消费，同时正确 specialist 被消费；不能通过“根本没安装 workflow-core”伪造 negative PASS。

### Phase E — pre-final Critic

形成未 bump version 的 implementation candidate，保存 exact commit/tree、changed-file scope、GATE_CASES hash、development replay、candidate consumption evidence、broad regression status、final gate commands、no-paid-API statement、recovery/stop conditions。

然后停止 final release evaluation，交独立 Critic 做 pre-final review。没有 Critic PASS，不进入下一阶段。

### Phase F — qualification G1–G5 at 0.4 candidate

pre-final Critic PASS 后，用冻结输入在同一 candidate 上跑完整 G1–G5。
任何失败都是真实 failure；不能换题、加样本挑赢家、拼不同 commit。

只有这一轮 G1–G5 全 PASS，才允许进入 version/release metadata mutation。

### Phase G — version/release candidate

满足 Phase F 后：

- `workflow-core 0.4 -> 0.5` exactly once；
- repository 只 PATCH：若届时正式 current release 仍是 `5.4.0`，目标 `5.4.1`；否则读取当时真实 current release 并推进一个 PATCH；
- 更新 workflow-core changelog、root CHANGELOG、README/version parity；
- canonical generator 重新生成。

若 origin/main 已有新的 formal release、workflow-core/shared generator 冲突或版本基线无法无歧义更新，停止回 Planner，不自行改版本规则。

### Phase H — final candidate G1–G5

version/release metadata mutation产生了新 candidate，因此不能沿用 Phase F 的 release claim。

冻结 final candidate 后，G1–G5 必须全部在这个同一 final candidate 上重新直接通过。
G4 仍必须是不可拆分 single-run chain；不同 run/candidate evidence 禁止拼接。

### Phase I — independent final review + release closure

把 final candidate、完整 G1–G5 evidence、CI、diff、version/changelog/README/generated parity 交独立 Critic/Reviewer。

PASS 后才允许：
- 按 AI Skills Maintainer canonical path 集成 exact final candidate；
- ordinary non-force publication；
- formal repository PATCH release closure；
- fast-forward-only release ref closure（若当时 maintainer contract要求）；
- install/update smoke 与 production identity核对。

不得 force push、创建/移动稳定 tag、扩大 release scope、修改 Bridge 或 consumer machines。

最终集成必须证明目标 plugin source/generated payload 与已通过 G1–G5 的 final candidate byte-equivalent；若 integration 发生实质产品变化，final candidate 失效，回 Gate。

## 8. G1–G5 executable acceptance contract

### G1 — Trigger precision

PASS 必须同时看到：
- implicit positive 实际消费 workflow-core；
- contextual positive 实际消费 workflow-core；
- complex specialist-contained hard negative：workflow-core candidate 可发现但不消费，specialist 实际消费；
- simple negative 不误触发。

### G2 — Specialist-first discovery

PASS 必须直接看到三种 failure shape 在声明 absent 前消费匹配 specialist / project route。禁止大范围 host scan。真正 unavailable 不得伪装成功。

### G3 — Six-dimension equivalence

PASS 必须至少包含：
- 六项全部保持的等价恢复成功；
- quality/evidence 改变被拒；
- authorization UNKNOWN/CHANGED 被拒 automatic fallback；
- specialist-forbidden fallback 被拒；
- 每个判断有六项可审 evidence。

### G4 — Inseparable normal entry + absent contrast

Positive：同一 run 全链。
Absent：canonical + specialist + project-declared route 均真实缺失时，精确 fail closed，不扫描、不发明技术栈、不降级 acceptance、不制造无必要 Human Gate。

### G5 — Broad regression

同一 final candidate 必须通过：
- 056 W1–W5 regression；
- workflow-core 0.4 Reviewed bootstrap/resume regression；
- source/generated/Marketplace/version parity；
- specialist-contained should-not-change；
- 至少一个非中文 PDF 的相邻 specialist/普通任务 negative；
- risk-matched full tests/CI。

## 9. Failure / recovery

立即停止并回 Planner/Critic：
- 需要修改 approved architecture / G1–G5 semantics；
- 需要改 Bridge runtime/Host Policy；
- 需要改 Longleaf / STAT5060 / render specialist production source；
- 需要新 state/schema/watcher/daemon；
- exact Reviewed branch/worktree/canonical checkout 不可用；
- task-specific hardcode 才能过 gate；
- final G4 不能在 single run 证明；
- specialist consumption 无可靠 runtime evidence；
- repository current release/shared source drift 使 final version target含糊；
- external paid API 才能完成 gate。

普通 implementation bug、test repair、generic fixture调整在 frozen Plan 内可由 Executor修复；若修复改变机制，则回 Planner。

## 10. Maintenance Board

继续服从 approved V0.4：

- `HISTORICAL_RESOLVED` 只作 bootstrap/coverage disposition；
- canonical TODO vocabulary：`NEW / PROJECT_LOCAL / CANDIDATE_GENERIC / PROMOTE_NOW / PROMOTED / BLOCKED_NEEDS_EVIDENCE / REJECTED / SUPERSEDED`；
- #5/#6/#11 若做 Project closure，必须适用 `ADAPTING -> required consumers -> Resolution commit -> Issue close -> DONE`；
- N/A 需要 durable frozen reason。

当前 package-prep surface 无 Project mutation + Clear Writing，因此本 Plan 不修改 Project/Issues。Executor 若仍无合法 surface，只记录 exact pending mutation，不要求用户手工维护，也不得伪称同步。

## 11. Version / maturity

Package preparation 时：

```text
Repository bump decision: NONE
Affected plugins:
- workflow-core: NO_BUMP
```

只有 Phase F 完整 PASS 后才允许 version mutation；最终 release claim仍必须由 Phase H 的 version-bumped final candidate直接通过。

不提升 maturity。

## 12. 本 Plan 不授权什么

本文件本身不是 current-user execution authorization。
只有用户未来发送经过 execution-ready Critic PASS 的 Kickoff，才授权其中明确列出的 bounded effects。

本 Plan 不授权 paid API、force/destructive Git、任意 branch/worktree、Bridge mutation、Longleaf/STAT5060 mutation、consumer-machine adaptation 或超出本 Goal 的 release。
