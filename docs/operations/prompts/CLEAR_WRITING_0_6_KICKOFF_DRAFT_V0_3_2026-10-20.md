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

## 本轮用户追加的同版实现边界（仅在新版Critic PASS及用户发送Kickoff后生效）

在`CHAT_RESPONSE_READER_VALUE_SELECTION_V1`基础上，按CAT-TRACE真实解释与Bridge失败的对照记录，优化**读者理解所需概念、例子、变量/公式和限制**的进入时机，而不是增加禁词/长度规定。只在现有`clear-writing`包装入口内完成，不改六个专业route源码，也不复制私有CAT资料进入插件。正式写作源的模型与实际用户问法要保持分离。

同一个用户请求涉及GitHub UTF-8文本时，源全文/正式写作路线/完整候选的事实及读者质量检查与聊天答复的处理必须**独立完成**。按新批准合同支持已存在文件expected-blob修改和受控新文件的非覆盖`create_file`及全文回读；缺读者质量或保真不能仅凭文件写入成功报完成。保持G3-A Reader Guide真实修改与聊天，新增G3-B受控新建文件与聊天，仍在同一个G3，不新建Gate或其他外部surface。

实现阶段同时合并已经移交原Codex的安全tar.gz归档兼容修复；新版正式候选只有一个，旧`079bd798...`不再可安装。G2-T8-A CAT科研解释与T8-B原传感器深度控制必须防止修成机械短答。具体输入、Gate顺序、发布和恢复边界只按同一提交的v0.3 Plan/Runbook；正式Personal Plugin在Phase C-A真实归档字节与恢复准备完全证明前不能更新。

## 2026-10-22 仅在批准后实施的最小补强

在原`CHAT_RESPONSE_READER_VALUE_SELECTION_V1`中补上读者疑问的因果衔接，并按本次Proposal §10、Plan §18**直接在总入口SKILL.md里**放入一对简短的脱敏正反示例。目标是让用户未要求“参考CAT-TRACE”时，普通工程技术汇报仍能说明“问题→机制→用户效果→必要证据/限制”，而不只是筛掉英文日志。不得新增可发现Skill、私有CAT素材或重复的专业规则，也不得造多一步模型审校。G2-T1现有prompt不提CAT，完整Web结果须按更新的Runbook §17作读者理解质量判定。原G2-T8数学深度、G3-A/B文件质量、同一候选、真实恢复准备、版本和Phase C执行职责保持不变。
