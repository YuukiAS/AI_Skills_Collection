# Project Thread Handoff — Canonical Goal v0.1

Task key：`science-communication--project-thread-handoff`  
Human label：Project Thread Handoff V1 implementation  
Status：AWAITING_EXECUTION_READY_CRITIC  
Approved Proposal：`docs/design/PROJECT_THREAD_HANDOFF_V3_PROPOSAL_2026-09-21.md` V3  
Approved Proposal commit：`164f028b76da265b117e42cfbda1563cd4abb809`  
Implementation Plan：`docs/design/PROJECT_THREAD_HANDOFF_IMPLEMENTATION_PLAN_V0_1_2026-09-21.md` v0.1  
Kickoff：`docs/operations/prompts/PROJECT_THREAD_HANDOFF_KICKOFF_V0_1.md` v0.1

本 Goal 只有在独立 Critic 对 Proposal + Plan + Goal + Kickoff 同版给出
`READY_FOR_CODEX=YES`，且用户实际发送 approved Kickoff 后才可执行。

## 1. Positive outcome

交付一个可安装的 standalone Skill `Project Thread Handoff`，让用户在已有长期
ChatGPT regular Chat thread 中通过账号真实提供的显式 Skill 入口调用一次，即可获得一份
最小充分、可直接初始化新 thread 的 continuation Prompt。

正常用户不需要：

- 重贴整段聊天；
- 再解释 CARE/DII 等实体角色；
- 回答第二轮确认；
- 让 Skill 写科研 repo；
- 切到 Work/Codex 才能完成目标。

## 2. Frozen execution identity

Exact task key：

`science-communication--project-thread-handoff`

Exact branch：

`reviewed/science-communication--project-thread-handoff`

Exact task-owned worktree：

`../AI_Skills_Collection-science-communication-project-thread-handoff`

worktree 以 verified canonical AI_Skills checkout root 为基准解析到父目录 sibling。不得替换成
`/tmp`、第二个 worktree 或其他 branch。已存在 locator 只有 repo+branch identity 都匹配时复用；
否则停止。

## 3. Required source

必须新增：

```text
skills/science/communication/project-thread-handoff/SKILL.md
skills/science/communication/project-thread-handoff/agents/openai.yaml
skills/science/communication/project-thread-handoff/evals/trigger_queries.json
tests/test_project_thread_handoff_contract.py
```

最小 fixture 仅在真实需要时允许：

`tests/fixtures/project_thread_handoff/`

不得新增 Plugin、MCP、database、CURRENT、history、state machine、browser extension、
automation/watcher、Bridge production change 或科研项目 write。

## 4. Non-substitutable semantics

以下不能被弱化：

1. standalone Skill 身份；
2. explicit-only invocation，`policy.allow_implicit_invocation: false` 位于
   `agents/openai.yaml`；
3. ChatGPT regular Chat normal entry 不硬编码某个字符语法；
4. latest explicit user/frozen decision 不被较晚 assistant brainstorming 覆盖；
5. thread-only delta 只覆盖决策语义，不伪造实验/代码/runtime facts；
6. CARE 在 DII acceptance 中是数据/数据来源，不是当前方法体系；
7. canonical facts 主要给 locator，unknown path/SHA 不编造；
8. output 只有一份 initialization Prompt；
9. no second confirmation；
10. no repo write；
11. Bridge Kit 非依赖；
12. Work/Codex PASS 不能替代 target ChatGPT regular Chat PASS。

## 5. Capability Gates

只允许 G1 / G2 / G3。

### G1 — Installation / Explicit Invocation Boundary

同一 final candidate 必须证明：

- source/generated/provenance/registry/catalog parity；
- `agents/openai.yaml` 合法；
- upload-ready package；
- target Pro account 安装成功；
- target ChatGPT regular Chat 有正式显式 Skill entry；
- ordinary project chat 不靠 implicit routing 自动进入。

### G2 — Core Handoff Semantics / DII Target-Surface Replay

同一 final candidate 必须在用户当前 Pro ChatGPT regular Chat 的已有长 DII thread 中实际调用，
且不要求用户重贴历史。

必须证明：

- DII 是当前方法学项目；
- CARE 是当前数据/数据来源；
- CARE challenge models 不恢复为当前方法候选；
- latest user/frozen decision 覆盖较早 assistant exploration；
- thread-only delta 正确；
- canonical facts 主要给 locator；
- unknown path/SHA 不编造；
- 单一 initialization Prompt；
- no second confirmation；
- no repo write；
- Skill 能消费当前 thread context。

regular Chat 无法调用、只能 Work/Codex 或无法消费 current thread context => `G2=FAIL`，
停止并返回 Planner/Critic。

### G3 — Generalization / Should-not-change

用户介入前完成：

- CAT-TRACE：后期冻结决定覆盖早期探索，superseded route 不复活；
- CardiacNexus：代码/pipeline/实验数字主要重新读 repo，handoff 只传最近判断/open question/下一步；
- 不 hardcode DII/CARE；
- 不依赖 Bridge Kit。

不得新增 G4/G5；若出现三 Gate 无法覆盖的新真实能力风险，返回 Planner/Critic。

## 6. Pre-user completion requirements

在要求用户任何 target-account 操作前，Executor 必须完成：

- production source；
- agents metadata；
- trigger eval；
- focused contract tests；
- registry/catalog/provenance/generated parity；
- Marketplace parity check；
- full relevant repository test suite；
- G3；
- version/README/changelog candidate closure；
- `private/exports/project-thread-handoff-v1.zip`；
- local archive validation；
- final candidate freeze；
- exact candidate commit + ordinary non-force push；
- remote exact task branch tip verification。

只有之后可报告：

`FINAL_CANDIDATE_READY_FOR_TARGET_ACCEPTANCE=YES`

## 7. Single target-surface acceptance session

用户只承担一次计划内 target action：

1. 在当前 ChatGPT Skills 页面上传/安装 final zip；
2. 回到已有 DII regular Chat；
3. 用该账号当前真实可见的正式显式 Skill 入口调用一次 Project Thread Handoff。

同一次 session 完成 G1 target observation + G2 DII replay。

不要求 `$`/`@`/`/` 各测试一次，不要求第二次上传。

若 G1/G2 FAIL，保留失败并返回 Planner/Critic；不得换 Work/Codex 宣布 PASS。

## 8. Upload package

必须存在：

`private/exports/project-thread-handoff-v1.zip`

zip 只包含一个顶层目录：

`project-thread-handoff/`

且至少包含：

- `SKILL.md`
- `agents/openai.yaml`
- `evals/trigger_queries.json`

在请求用户前解包验证并记录 SHA-256/file list。不得只留 `/tmp`。

## 9. Evidence

```text
results/science-communication--project-thread-handoff/result.md
results/science-communication--project-thread-handoff/MANIFEST.md
results/science-communication--project-thread-handoff/target-surface-acceptance.md
results/science-communication--project-thread-handoff/review.md
```

不得公开提交 DII/CAT-TRACE/CardiacNexus 私有 thread 全文。Target-surface receipt 只写最小非敏感
PASS/FAIL、candidate identity、surface 与 invocation entry。

## 10. Version / README

Repository bump decision：`MINOR`

Planning-baseline target：

`5.0.6 -> 5.1.0`

理由：新增正式 standalone user workflow，使 collection 能完成此前 5.0.x 没有的长期 thread handoff
用户任务，符合 repository-level user capability / important formal user workflow。

Affected central plugins：

- all central plugins: `NO_BUMP`

若 implementation preflight 发现 `origin/main:VERSION != 5.0.6`，不得覆盖或自行猜新版本；
记录 `VERSION_DRIFT` 并返回 Planner 做最小 amendment。

Root README 必须同步 repository version并简短介绍 standalone Project Thread Handoff，不把它列成
中央 Plugin。

`skills/README.md` 必须检查；当前预计 `README checked: no update required`，除非实现后发现
现文会误导安装/定位。

## 11. Authorized implementation boundary after Kickoff

允许：

- exact branch/worktree；
- source/docs/tests/generated/version/README/changelog/results 的冻结范围修改；
- deterministic local tests；
- archive generation；
- ordinary task-owned commits；
- ordinary non-force push exact task branch；
- public OpenAI Skill docs read。

禁止：

- merge main / tag / release / publish；
- force push / remote remap / destructive Git；
- ChatGPT account upload/install；
- paid evaluator/API；
- Bridge Kit write；
- target research repo write；
- central Plugin source write；
- automation/watcher；
- Plugin/MCP/database/CURRENT/state/history expansion。

## 12. Overall completion

以下都不是 overall completion：

- source written；
- tests green；
- zip built；
- G3 PASS；
- branch pushed；
- Codex compatibility PASS。

只要 G1/G2 target acceptance 未完成：

`PROJECT_THREAD_HANDOFF_V1_READY != YES`

只有同一 final candidate 的 G1+G2+G3 PASS、独立 final review 与合法 integration/release closure
完成后，才允许总体 ready claim。
