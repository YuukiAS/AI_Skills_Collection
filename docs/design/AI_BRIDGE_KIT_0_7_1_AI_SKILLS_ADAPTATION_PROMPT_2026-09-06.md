# Bridge Kit 0.7.1 → AI_Skills_Collection 适配 Prompt

状态：可执行 Prompt；只处理 Bridge Kit / Reviewed Handoff / Host Policy / consumer pin 基础设施，不处理任何 domain plugin。

目标上游：`YuukiAS/GPT_Codex_AI_Bridge_Kit`

目标版本：`0.7.1`

目标 commit：`3b061167794d593b113ca8f4a8a43c4c8000fc01`

AI_Skills_Collection 当前 `main` 在本 Prompt 写入时为：`50963b7d0dd6a723b3589460e1023f20d429dfb1`。执行时必须重新 `fetch`，以真实最新 `origin/main` 为准。

---

你现在只做一件事：

> 把 Bridge Kit `0.7.1` 的 Reviewed Handoff / Goal Fidelity / Host Policy / active consumer pin 安全适配到 `YuukiAS/AI_Skills_Collection`，保留 AI_Skills 已有 repository-specific 定制，并验证历史 V1 PLAN 兼容路径在真实 consumer repo 中工作。

不要处理 `writing-style`、`clear-language`、050、research-writing、presentations、statistical-modeling、scientific-visualization、medical-imaging、bioinformatics 或任何其他 domain plugin。

## 0. 严格范围

允许修改：

- `automation/reviewed_handoff/**`
- `.github/workflows/*ai-bridge*`
- 其他明确依赖 Bridge Kit active pin 的 workflow
- Bridge Kit consumer / Reviewed Handoff 相关 tests
- Bridge Kit pin 相关 fixture builder
- Bridge Kit integration docs
- 本机 Bridge Kit 安装
- 当前 Codex identity 的 Host Policy

禁止修改：

- `skills/**`
- `plugins/codex/plugins/**`
- `profiles/**`
- `scripts/codex_marketplace_config.json`
- `docs/plugin-todos/**`
- `docs/plugin-changelogs/**`
- plugin version
- repository version
- 任何 domain plugin production behavior

禁止 `git reset --hard`、`git clean`、force push。不要为了本任务处理 050 的 dirty worktree；使用安全、干净的 `main` checkout/worktree。

## 1. 先读取真实状态

AI_Skills：

```bash
git fetch origin
git status --short
git branch --show-current
git rev-parse HEAD
git rev-parse origin/main
```

Bridge Kit：确认当前远端 `main` 为：

```text
3b061167794d593b113ca8f4a8a43c4c8000fc01
version = 0.7.1
```

读取 Bridge Kit 至少：

- `README.md`
- `CHANGELOG.md`
- `ai_bridge_kit/reviewed_handoff.py`
- `templates/reviewed_handoff/templates/PLAN.md`
- `templates/reviewed_handoff/prompts/PLANNER.md`
- `templates/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `templates/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md`
- `tests/test_reviewed_handoff.py`
- `tests/test_reviewed_runner.py`

读取 AI_Skills 至少：

- `AGENTS.md`
- `automation/reviewed_handoff/templates/PLAN.md`
- `automation/reviewed_handoff/prompts/PLANNER.md`
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md`
- 必要的 `automation/reviewed_handoff/tasks/*/CURRENT.json`
- 必要的历史 `PLAN.md`
- 所有 active Bridge Kit pin 位置

## 2. 第一件事：用 0.7.1 当前源码做真实只读 consumer 验证

在任何 AI_Skills source 写入、本机 package 安装或 pin 修改之前，直接使用 Bridge Kit `0.7.1` 当前源码运行：

```bash
python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target <AI_Skills_Collection>
```

如果仓库实际 CLI module 入口不同，以 Bridge Kit 0.7.1 当前源码为准；不要猜命令。

预期：

- exit code = 0；
- 旧 `AI_BRIDGE_REVIEWED_PLAN_V1` task 可以得到 legacy compatibility warning；
- 不能再出现 0.7.0 的 46 个“缺 `Positive completion` / `Non-substitutable semantics`”错误；
- validation 前后 AI_Skills 文件内容不变化。

如果真实 consumer validation 仍失败，先定位第二类兼容问题。此时禁止开始安装或写 repo，返回：

`BRIDGE_KIT_0_7_1_AI_SKILLS_PREFLIGHT_BLOCKED`

并给出 exact error / affected task / upstream owner。

## 3. 明确 0.7.1 的 V1/V2 语义

必须按 Bridge Kit `0.7.1` 当前实现保留以下语义：

- `AI_BRIDGE_REVIEWED_PLAN_V1` = legacy historical PLAN；repository audit 可以接受合法 V1；
- `AI_BRIDGE_REVIEWED_PLAN_V2` = 当前 Goal Fidelity PLAN；
- 当前新 template 必须生成 V2；
- 任何**现在发生的** `... -> PLAN_FROZEN` 或 re-freeze 必须走 current-freeze validation，不能用 V1 绕过；
- unknown schema / malformed V1 仍失败；
- 不批量改写历史 V1 PLAN；
- 不新增 migration ledger / role / state / workflow。

不要重新实现这套兼容逻辑到 AI_Skills 私有 Python 中。底层 owner 是 Bridge Kit；AI_Skills 只适配自己的 repository templates/prompts/consumer pin。

## 4. 不要 `--force` 覆盖 AI_Skills 定制

AI_Skills 当前 Reviewed Handoff 有 repository-specific contract，至少包括：

- `ai-skills-core` maintenance companion；
- Domain owner；
- production plugin refinement gate；
- artifact-aware review；
- private Text Review 边界；
- paid-review safety；
- candidate-frozen heavyweight CI；
- plugin version/changelog contract；
- real-project feedback triage；
- holdout/generalization policy；
- dedicated task branch；
- watcher-owned publication；
- production plugin replay contract。

因此不得先运行：

```bash
ai-bridge reviewed-handoff install --force
```

正确方式是三方语义合并：

```text
Bridge Kit 0.7.1 generic Review contract
+
AI_Skills 当前 custom Review contract
=
AI_Skills 新 Review contract
```

## 5. 适配 canonical PLAN template

AI_Skills 当前 canonical `PLAN.md` 仍是 V1 风格。把**未来新 Plan**模板升级为 Bridge Kit 0.7.1 的 V2：

frontmatter：

```text
schema: AI_BRIDGE_REVIEWED_PLAN_V2
```

必须包含：

- `## Frozen decisions`
- `## Positive completion`
- `## Non-substitutable semantics`
- `## Implementation scope`
- `## Acceptance and regression gates`
- `## Natural-language usage / routing expectations`
- `## Out of scope`

AI_Skills 自己的 Planner 以后生成/修订 Plan 时必须以运行时当前 template 为 source of truth。

不要改任何历史 task 的 V1 PLAN。

## 6. 合并 0.7.1 Planner / Executor / Reviewer Goal Fidelity

在保留 AI_Skills 现有定制的前提下，吸收 Bridge Kit 0.7.1 generic 语义：

### Planner

必须先冻结：

- Positive completion：真实用户/产品/科研/仓库结果；
- claim scope：证据最多支持什么；
- non-substitutable semantics：哪些 data / method / model/source / scale / execution entry / artifact / renderer / quality bar 不可偷偷降级；
- evidence requirements。

对定性、科学、视觉、语言质量，不得发明 fake numeric threshold。

Plan revision/re-freeze 只能写 V2。

### Executor

不得把以下较弱路径当原目标完成：

- proxy
- toy/synthetic
- helper-only
- handmade artifact
- reduced scale
- lower quality bar
- blacklist-only check

除非冻结 Plan 明确授权 equivalence 且给出等价证据。

### Reviewer

必须问：

- positive completion 是否真的观察到；
- non-substitutable semantics 是否被弱化；
- claim scope 是否超过 evidence scope；
- 当前 evidence 是否同样能由 Plan 不允许的更弱实现解释。

如果能，则不能 PASS。

测试/CI/schema/validator/文件存在/没有命中 blacklist 只算各自 process evidence，不能自动变成 Product PASS。

## 7. 保留 AI_Skills custom clauses

三方合并时逐项确认以下内容没有被 upstream vanilla template 覆盖掉：

1. `ai-skills-core` maintenance companion；
2. Domain owner；
3. artifact-aware review；
4. private Text Review；
5. paid external review safety；
6. heavyweight CI 是 candidate frozen 后 phase gate，而不是 per-commit ritual；
7. plugin refinement / TODO / versioning；
8. real-project feedback triage；
9. unseen/holdout batch freeze；
10. dedicated task branch；
11. watcher-owned publication；
12. production `plugin-replay` 使用边界。

不要为了同步 upstream 删除更具体、且不与 0.7.1 冲突的 AI_Skills repository policy。

## 8. 更新 active Bridge Kit pin

搜索整个 AI_Skills repo 中旧 active pin：

```text
6968a84b689d6e5589d068aee7dd101b12fd7700
```

逐个分类：

- `ACTIVE_CONSUMER_PIN`
- `ACTIVE_TEST_OR_FIXTURE_EXPECTATION`
- `HISTORICAL_EVIDENCE_IDENTITY`

只把前两类更新为：

```text
3b061167794d593b113ca8f4a8a43c4c8000fc01
```

历史 RESULT / manifest / VISUAL_REVIEW / benchmark evidence 必须保留当时真实 SHA，禁止全仓机械替换。

至少检查：

- `.github/workflows/ai-bridge-text-review.yml`
- `.github/workflows/ai-bridge-visual-review.yml`
- presentation 相关 active visual-review workflow
- `tests/test_paid_review_workflows.py`
- 当前 active fixture builder / test expectation

## 9. 更新本机 Bridge Kit 到 0.7.1

先记录：

```bash
which ai-bridge
ai-bridge --version
python -m pip show gpt-codex-ai-bridge-kit
```

确认 canonical Bridge Kit checkout / package identity。安全 fast-forward 或按正常 package 路径安装精确 commit：

```text
3b061167794d593b113ca8f4a8a43c4c8000fc01
```

不得覆盖 unknown dirty work，不要制造随机重复 clone。

安装后必须确认：

```text
ai-bridge --version = 0.7.1
```

## 10. 刷新当前 Codex identity 的 Host Policy

检查：

```bash
ai-bridge host status
```

必要时使用正常非破坏路径：

```bash
ai-bridge host install
ai-bridge host validate
```

要求：

- 不切换 `CODEX_HOME`；
- 不覆盖用户自定义配置；
- 不放宽危险 Git；
- `plugin-replay` 当前安全边界保持有效。

## 11. 真实 repo 验证

更新后再次运行真实 installed 0.7.1：

```bash
ai-bridge reviewed-handoff validate --target <AI_Skills_Collection>
```

要求 exit 0。Legacy V1 warning 可以存在；不能把 warning 当 error，也不能为了消除 warning 去改历史 Plan。

## 12. Targeted regression

至少验证：

- canonical future PLAN 已是 V2；
- 新 V2 缺 Positive completion 不能 freeze；
- 新 V2 缺 Non-substitutable semantics 不能 freeze；
- historical valid V1 repository audit 仍 PASS；
- malformed V1 / unknown schema 仍 fail；
- 新 task 不能用 V1 freeze；
- re-plan 不能用 V1 re-freeze；
- AI_Skills custom Planner/Executor/Reviewer clauses 没丢；
- active consumer pin 全部是 `3b061167...`；
- historical evidence pin 没改。

运行当前真实相关 test module，不要为了迎合本 Prompt 发明不存在的测试名。

Targeted PASS 后，若成本合理，再运行：

```bash
python -m unittest discover -s tests
```

并运行相关 zero-paid repository validation，例如：

```bash
python scripts/skills.py validate
```

不要运行 Terra / OpenAI paid review / Text Review paid call / Visual Review paid call / plugin replay / writing-style replay。

## 13. Diff 审计

提交前：

```bash
git status --short
git diff --stat
git diff
git diff --check
```

必须证明：

- 没有 `skills/**` 变化；
- 没有 `plugins/codex/plugins/**` 变化；
- 没有 plugin version 变化；
- 没有 repository version 变化；
- 没有 050 变化；
- 没有 private material；
- 没有 unrelated change。

## 14. 提交与停止

安全完成后，只提交本轮 Bridge Kit consumer adaptation，按 AI_Skills 当前授权 publication contract 正常 push。禁止 force push。

最终状态只能是：

```text
BRIDGE_KIT_0_7_1_AI_SKILLS_ADAPTED
```

或：

```text
BRIDGE_KIT_0_7_1_AI_SKILLS_ADAPTATION_BLOCKED
```

最终报告：

1. AI_Skills 起始 commit；
2. Bridge Kit commit/version；
3. 写入前 0.7.1 real consumer validation 结果；
4. legacy V1 warnings 数量与是否有 errors；
5. AI_Skills 实际修改文件；
6. V2 PLAN / Goal Fidelity 如何合并；
7. AI_Skills custom clauses 保留证明；
8. active pin 更新清单；
9. historical pin 保留清单；
10. `ai-bridge` 更新前/后版本；
11. Host Policy validate；
12. targeted tests；
13. repository-wide Reviewed Handoff validate；
14. full local tests（若执行）；
15. diff scope proof；
16. commit/push；
17. 最终状态。

然后停止。不要进入任何 plugin 工作。
