# Project Thread Handoff — Codex Kickoff Draft v0.2

Task key：`science-communication--project-thread-handoff`  
Human label：Project Thread Handoff V1 implementation  
Approved Proposal：`docs/design/PROJECT_THREAD_HANDOFF_V3_PROPOSAL_2026-09-21.md` V3 @ `164f028b76da265b117e42cfbda1563cd4abb809`  
Prior execution package：v0.1 @ `e0b519cdc27e12da98ffdea168cf4f0a1dd0ce06`  
Revision scope：只关闭 `PTH-05`  
Implementation Plan：`docs/design/PROJECT_THREAD_HANDOFF_IMPLEMENTATION_PLAN_V0_2_2026-09-21.md` v0.2  
Canonical Goal：`docs/goals/PROJECT_THREAD_HANDOFF_GOAL_V0_2.md` v0.2  
Status：DRAFT_NOT_AUTHORIZED

只有独立 Critic 审完同一 Proposal + Plan + Goal + Kickoff 并返回
`READY_FOR_CODEX=YES` 后，用户实际发送下面正文，才形成 implementation authorization。

## Kickoff 正文

执行 `science-communication--project-thread-handoff`，实现已获 Critic 设计 PASS 的
standalone Skill `Project Thread Handoff` V1。

本 v0.2 只关闭 `PTH-05 — Read-only Skill frontmatter 没有被冻结`。不要重新设计 V3，也不要
改变已接受的 G1/G2/G3、version decision、user-action、privacy、recovery 或 authorization boundary。

严格读取并遵守：

- `docs/design/PROJECT_THREAD_HANDOFF_V3_PROPOSAL_2026-09-21.md`
  @ `164f028b76da265b117e42cfbda1563cd4abb809`
- `docs/design/PROJECT_THREAD_HANDOFF_IMPLEMENTATION_PLAN_V0_2_2026-09-21.md` v0.2
- `docs/goals/PROJECT_THREAD_HANDOFF_GOAL_V0_2.md` v0.2

### 1. 我在这条消息中授权的 exact branch / worktree

Repository：

`YuukiAS/AI_Skills_Collection`

Exact branch：

`reviewed/science-communication--project-thread-handoff`

Exact task-owned worktree：

`../AI_Skills_Collection-science-communication-project-thread-handoff`

该 worktree 必须相对 verified canonical AI_Skills checkout root 解析为父目录 sibling。先确认
`git rev-parse --show-toplevel` 与 origin identity。

允许创建/复用上面唯一 exact branch/worktree。已有 path 只有 repo identity 与 exact branch 都匹配
才可复用；若占用或不匹配，停止并报告。不要改用 `/tmp`、另一个 branch、另一个 worktree 或 clone。

后续同一 frozen task 的普通 task-owned commit / ordinary non-force push 不要重复询问授权。

### 2. Latest-main preflight

先：

`git fetch origin main`

读取 current main 的：

- `AGENTS.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/SKILL_AUTHORING.md`
- current Skill creator/openai metadata contract
- current `scripts/skills.py` new-skill scaffold
- current `scripts/skill_utils.py` registry record defaults

确认 approved V3 commit 仍在 history。

仅有无关 docs/evidence drift则继续。若出现与本 Skill architecture、metadata contract、taxonomy、
version/release semantics 直接冲突的新 source，停止并返回 Planner/Critic。

### 3. 只实现冻结 source scope

新增：

```text
skills/science/communication/project-thread-handoff/SKILL.md
skills/science/communication/project-thread-handoff/agents/openai.yaml
skills/science/communication/project-thread-handoff/evals/trigger_queries.json
tests/test_project_thread_handoff_contract.py
```

只有真实需要时增加最小：

`tests/fixtures/project_thread_handoff/`

不要创建 Plugin、MCP、database、CURRENT、handoff history、state machine、browser extension、
automation/watcher；不要改 Bridge Kit、CAT-TRACE、DII、CardiacNexus、Mica 或中央 Plugin source。

### 4. PTH-05：冻结 SKILL.md frontmatter

最终
`skills/science/communication/project-thread-handoff/SKILL.md`
必须显式具有至少：

```yaml
name: project-thread-handoff
description: <具体 explicit long-thread handoff trigger boundary；排除 ordinary summary>
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: false
executes_code: false
secrets_needed: []
recommended_scope: project
metadata:
  skill-author: AI Skills Collection maintainers
```

不要依赖当前 scaffold 的 `writes_files: true` 默认，也不要依赖
`skill_record(...).get("writes_files", True)` 的 fallback。

`description` 按 current authoring contract 写具体 trigger boundary，尽量保持在当前 repo 的
350-char warning threshold 内。

允许 current repo 标准的非 capability metadata（例如 `last_reviewed`、空 `profile_tags`），
但不得改变上面冻结的 capability values。

普通 `SKILL.md` frontmatter 不得出现：

`allow_implicit_invocation: false`

它继续只属于：

```yaml
# agents/openai.yaml
policy:
  allow_implicit_invocation: false
```

### 5. Focused contract test 必须保护 metadata

`tests/test_project_thread_handoff_contract.py` 至少检查：

- `name == "project-thread-handoff"`
- `status == "active"`
- `provenance == "user-authored"`
- `trusted is false`
- `requires_network is false`
- `writes_files is false`
- `executes_code is false`
- `secrets_needed` 为空
- `recommended_scope == "project"`
- `metadata.skill-author == "AI Skills Collection maintainers"`
- `allow_implicit_invocation` 不在 `SKILL.md` frontmatter
- `agents/openai.yaml -> policy.allow_implicit_invocation == false`

registry 生成后还必须核对正式 `project-thread-handoff` record 至少保持：

`provenance=user-authored`、
`requires_network=false`、
`writes_files=false`、
`executes_code=false`、
`secrets_needed=[]`。

不要为这些断言新增 schema、script 或新 Gate。

### 6. 保持 V3 其余语义

继续实现：

- explicit-only；
- ChatGPT normal entry 不硬编码 `$`/`@`/`/`；
- latest user/frozen decision > assistant brainstorming；
- thread-only delta 只覆盖决策语义；
- CARE 在 DII 中是数据/数据来源，不是当前方法体系；
- canonical facts 主要给 locator，unknown path/SHA 不编造；
- one invocation -> one initialization Prompt；
- no second confirmation；
- no repo write；
- Bridge Kit 非依赖；
- minimum sufficient information。

### 7. 只保留 G1/G2/G3

G1：
Installation / Explicit Invocation Boundary，并包含 source/registry/catalog 的 read-only capability
metadata parity。

G2：
用户当前 Pro ChatGPT regular Chat 的真实 DII target-surface replay。Codex/Work/helper/fixture
不能替代。Skill 必须消费已有 thread context，不要求用户重新粘贴历史。

G3：
CAT-TRACE + CardiacNexus representative generalization / should-not-change，用户介入前完成。

如果需要新增 G4/G5 才能覆盖新的用户能力，停止并返回 Planner/Critic。

### 8. 在找用户之前先全部做完

在要求用户 target-account 操作前，你必须自行完成：

- Skill source；
- frozen PTH-05 frontmatter；
- agents/openai.yaml；
- trigger eval；
- focused metadata/contract tests；
- source-first registry/catalog/provenance/generated parity；
- Marketplace parity check；
- full relevant test suite；
- G3；
- version/README/changelog candidate closure；
- final upload-ready zip；
- archive validation；
- final candidate freeze；
- exact candidate commit；
- ordinary non-force push exact branch；
- remote tip verification。

生成：

`private/exports/project-thread-handoff-v1.zip`

zip 只含单一顶层目录 `project-thread-handoff/`，不得塞入 repo tests/results/design docs。
上传包 `SKILL.md` 必须与 frozen final source byte-equivalent。

记录 SHA-256 与 file list 到 task MANIFEST。不要只留 `/tmp`，且 G1/G2 完成前不要清理
worktree/export。

### 9. Version / README

保持已获 Critic 接受的版本决策：

Repository bump decision：

`MINOR`

planning baseline：

`5.0.6 -> 5.1.0`

所有中央 Plugin：

`NO_BUMP`

修改 version 前重新读 `origin/main:VERSION`。如果不再是 5.0.6，记录 `VERSION_DRIFT` 并停止；
不要覆盖并行 release，也不要自行猜新 target version。

Root README 更新 repository version，并简短说明 Project Thread Handoff 是 standalone Skill，不得
伪装成 Plugin。

检查 `skills/README.md`；没有真实 README-facing 变化就记录
`README checked: no update required`。

### 10. Evidence

写入：

```text
results/science-communication--project-thread-handoff/result.md
results/science-communication--project-thread-handoff/MANIFEST.md
results/science-communication--project-thread-handoff/target-surface-acceptance.md
```

用户操作前：

- result 写完整 implementation/tests/G3/candidate identity；
- target-surface-acceptance 状态保持 PENDING；
- 不把私有科研 thread 全文提交公开 repo。

当所有 pre-user 条件满足后，才报告：

`FINAL_CANDIDATE_READY_FOR_TARGET_ACCEPTANCE=YES`

并只给用户一次最小动作：

“在当前 ChatGPT Skills 页面上传/安装
`private/exports/project-thread-handoff-v1.zip`，然后回到已有 DII regular Chat，用界面实际可见的
正式显式 Skill 入口调用一次 Project Thread Handoff。”

同一次 acceptance session 覆盖 G1 target observation + G2 DII replay；不要让用户重复上传，也不要
要求分别测试 `$`/`@`/`/`。

### 11. G2 hard failure boundary

如果 target regular Chat：

- 无法调用已安装 Skill；
- 只能 Work/Codex 调用；
- 或 Skill 无法使用当前 thread 既有 context；

则 `G2=FAIL`。

保留失败证据并返回 Planner/Critic。不要换 surface、静默 fallback、自动修后继续跑到成功。

### 12. Git / side-effect boundary

我授权本 frozen task 内：

- exact branch/worktree；
- frozen source/docs/tests/generated/version/README/changelog/results edits；
- deterministic tests；
- upload zip generation；
- task-owned commits；
- ordinary non-force push exact task branch；
- public OpenAI Skill docs read。

我没有授权：

- merge main；
- force push / remote remap / destructive Git；
- tag/release/publish；
- 代我上传/安装 ChatGPT Skill；
- paid API/evaluator；
- Bridge Kit write；
- target research repo write；
- central Plugin source write；
- live-global installation outside task-local validation；
- automation/watcher；
- 任何 Plugin/MCP/database/CURRENT/state/history 扩张。

### 13. Stop point

普通开发问题在冻结 scope 内自行修完并重跑测试，不要把半成品交给我验收。

当 final candidate 已完整、metadata/generated identity 正确、push、远端验证，并且只剩 target
ChatGPT regular Chat acceptance 时，停止在：

`FINAL_CANDIDATE_READY_FOR_TARGET_ACCEPTANCE=YES`

不要把 source/metadata/tests/zip/G3/Codex smoke 写成：

`PROJECT_THREAD_HANDOFF_V1_READY=YES`

只有 G1+G2+G3 对同一 final candidate PASS、独立 final review 与后续合法 integration/release closure
完成后，才允许总体 ready claim。
