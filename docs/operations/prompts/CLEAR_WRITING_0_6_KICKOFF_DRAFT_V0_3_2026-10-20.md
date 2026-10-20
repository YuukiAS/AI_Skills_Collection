# Clear Writing 0.6 — revised implementation Kickoff draft v0.3

> DRAFT ONLY — NOT AUTHORIZED.
>
> 只有原独立 Critic 对本 revised 0.6 package 给出 `PASS / READY_FOR_CODEX=YES`，并且用户随后发送本 Kickoff，才允许实现。Critic PASS 前不得修改正式 Personal Plugin、运行G1-G6或恢复Phase C live mutation。

继续**同一个** Clear Writing 0.6 task：

```text
repo = YuukiAS/AI_Skills_Collection
branch = design/clear-writing--single-entry-artifact-finalization
task = clear-writing--single-entry-artifact-finalization
tracking = #13
```

先读取批准的：

- `docs/design/clear-writing/CLEAR_WRITING_0_6_CHAT_RESPONSE_CONTENT_SELECTION_PROPOSAL_V0_2_2026-10-20.md`
- `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_3_2026-10-20.md`
- `docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_3_2026-10-20.md`
- `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_3_2026-10-20.md`
- Critic PASS绑定的 exact package commit。

显式使用：

`workflow-core + ai-skills-core + writing-style`

## 本轮实现只做两件事

### 1. CHAT_RESPONSE reader-value selection

修改：

`packaging/chatgpt/writing-style/clear-writing/SKILL.md`

加入批准的 `CHAT_RESPONSE_READER_VALUE_SELECTION_V1`。

不要默认改六项 canonical route正文。若发现必须修改 `response-clarity` / `writing-fidelity` source才能完成目标，STOP -> Planner。

### 2. archive compatibility

修改批准builder，使 `prepare-restore` 安全支持：

- ZIP；
-真实 gzip tar.gz/tgz；

并按Plan测试 traversal/link/duplicate/device/fifo。

不改变 forward restore语义。

## candidate规则

旧 `079bd798...` 只作历史基线，不再是release candidate。

本轮必须形成一个新的 implementation candidate，wrapper content-selection change与archive fix必须在同一candidate里。

不得让archive-only patch、old wrapper和new wrapper分别形成竞争candidate。

## development验证

先cheap deterministic tests，再known regressions：

- Bridge completion；
- Phase C handoff；
- necessary-long-answer depth protection；
- existing route/should-not-change controls。

然后required CI + independent implementation review。

不运行正式G1-G6，不更新Personal Plugin。

## 实现后

Reviewer PASS后：

1. 生成新的 `FINAL_CANDIDATE.json`；
2. 生成新的candidate ZIP/BUILD_RECEIPT；
3. 更新同任务 `PHASE_C_HANDOFF.md`，明确：
   - content-selection source已实现；
   - archive ZIP/tar.gz repair已实现；
   - live 0.5仍未修改；
   - Phase C-A必须先真实materialize old archive；
   - fresh Web Gate按v0.3职责执行。
4. STOP，交回Planner。

禁止：

- 修改Project setting；
- 新建task/version；
- 新增MCP/App/model/service；
- 更新Personal Plugin；
- 创建G3 branch；
-运行G1-G6；
-调用付费模型；
-发布central0.6。

最终报告：

```text
CHAT_RESPONSE_SELECTION_IMPLEMENTED=YES|NO
ARCHIVE_COMPAT_REPAIR=PASS|FAIL
NEW_FINAL_CANDIDATE_COMMIT=<sha or NONE>
IMPLEMENTATION_REVIEW=PASS|REVISE
LIVE_PERSONAL_PLUGIN_MUTATED=NO
NEXT_HANDOFF=PLANNER
```
