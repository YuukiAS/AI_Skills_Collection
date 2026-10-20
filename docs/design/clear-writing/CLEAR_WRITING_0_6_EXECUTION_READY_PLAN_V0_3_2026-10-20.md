# Clear Writing 0.6 执行计划 v0.3

日期：2026-10-20  
状态：DRAFT_PENDING_EXECUTION_READY_CRITIC  
任务：`clear-writing--single-entry-artifact-finalization`  
分支：`design/clear-writing--single-entry-artifact-finalization`  
跟踪：Issue `#13`  
产品修订：`CLEAR_WRITING_0_6_CHAT_RESPONSE_CONTENT_SELECTION_PROPOSAL_V0_2_2026-10-20.md`  
Supersedes for future execution：v0.2 execution package `d7b810d194ead881303aaca9c2e4f1d59a97c1f1`  
历史实现基线：`079bd7987bb33d624d244feb415327d5cf2343d8`

> 本 Plan 不授权实施。原 execution-ready PASS 因 CHAT_RESPONSE 产品语义变化而不再覆盖新版0.6。必须由原独立 Critic重新给出 `PASS / READY_FOR_CODEX=YES`，用户随后发送新版 Kickoff，才能进入实现。

## 1. 目标

在不改变 Clear Writing 0.6 总架构的前提下，补上普通聊天的内容选择缺口：

```text
完整领域分析 / evidence pool
!=
用户必须阅读的正文
```

新版唯一入口必须先按当前用户问题决定哪些内容值得进入 `CHAT_RESPONSE`，再调用已有 `response-clarity` 和必要的 `writing-fidelity`。

同时把已经发现的 Phase C archive compatibility 和执行职责问题收进同一 task，避免旧候选、独立 archive patch 和新版 wrapper形成三个互相漂移的 candidate。

## 2. implementation source 范围

允许修改：

1. `packaging/chatgpt/writing-style/clear-writing/SKILL.md`
   - 实现 `CHAT_RESPONSE_READER_VALUE_SELECTION_V1`；
   - 不复制六项专业 route 正文。
2. `scripts/build_clear_writing_chatgpt_wrapper.py`
   - 保持既有 deterministic wrapper build；
   - 修复 `prepare-restore` 对真实 Plugin Creator ZIP / tar.gz 输入的安全兼容。
3. `tests/test_clear_writing_chatgpt_wrapper.py`
   - reader-selection packaging contract；
   - archive安全与 restore等价。
4. 本任务 `results/clear-writing--single-entry-artifact-finalization/**`
   - 新 candidate/evidence；
   - known regression输入输出；
   - Phase C evidence。
5. 必要 generator/release metadata，只在既有0.6规则要求时更新。

默认禁止修改：

- 六项 canonical `skills/writing/core/**` 专业正文；
- Project setting；
- Research Authoring / Presentations / statistical-modeling / scientific-visualization；
- Bridge Kit；
- MCP/App/server/background runtime；
- G1-G6顶层结构。

若 implementation发现必须改 `response-clarity` 或 `writing-fidelity` canonical source 才能完成目标，立即 STOP -> Planner；该结论不是本 Plan 已批准的 fallback。

## 3. wrapper 必须实现的 CHAT_RESPONSE contract

在现有 `Identify The Deliverables` 与 route选择之间加入一个专门针对 `CHAT_RESPONSE` 的私有步骤。

### 3.1 Answer contract

必须从当前 user prompt提取：

- direct questions；
- reply type；
- requested detail；
- actual deliverable；
- necessary user action / next owner。

不得从 repo audit范围、工具调用数量或查到多少内部证据反推用户应该看到多少。

### 3.2 Reader-value inclusion test

领域分析完成后，对候选信息逐项判断。满足以下任一项才默认进入 user-facing正文：

- 直接回答问题；
- 解释主要机制/正常使用所必需；
- 改变可信度、完成判断或风险判断；
- 保存限制、不确定性、权限或失败边界；
- 用户行动/复现/交接所必需；
- 用户明确要求深入展开。

其余内容留在 evidence pool，不默认显示。

这不是固定分类schema，不落盘、不输出给用户。

### 3.3 深度保护

明确要求详细算法/数学/工程机制时，不得把 reader-value selection变成“压短”：

- 核心公式和变量关系；
- 必要推导或算法步骤；
- 复现所需参数/条件；
- 重要边界和反例；
- 用户明确点名的实现细节；

都属于 reader value。

### 3.4 route与保真

顺序固定：

```text
CHAT_RESPONSE reader-value selection
-> response-clarity
-> writing-fidelity when protected meaning exists
-> whole-response reader-value check
```

`writing-fidelity` 不拥有“全部 evidence pool必须展示”的语义。

### 3.5 whole-response check

最终答复必须同时检查：

- 问题是否全部回答；
- 详细程度是否匹配；
- 关键证据/限制/行动是否遗漏；
- 是否存在无法解释 reader value 的审计/架构/状态展开；
- 是否已经在需要时给出唯一下一接收方。

不得把该检查宣传成平台不可绕过 Hook。

## 4. 旧候选、旧PASS与证据复用

`079bd798...` 从新版0.6角度变为：

`HISTORICAL_IMPLEMENTATION_BASELINE / SUPERSEDED_FOR_RELEASE`

以下证据可继续作历史/回归基线：

- 六项 route source不变；
- old package shape与single-entry实现；
-旧13组local replay；
- old CI / implementation review；
- deterministic builder与route projection的大部分机制。

但新版 final candidate必须重新：

- build；
- source/generated parity；
- wrapper tests；
- 受影响 known regression；
- required CI；
- independent implementation review；
- `FINAL_CANDIDATE.json`。

不得把旧 archive hash写成新版候选预期值。

## 5. archive compatibility 同任务修复

真实 Plugin Creator current 0.5 archive已证明是 `.tar.gz` / `application/gzip`；旧 builder只读 ZIP。

新版实现必须把 archive reader收敛为安全支持：

- ZIP；
- gzip-compressed tar (`.tar.gz` / `.tgz`)。

tar reader必须拒绝：

- absolute / traversal；
- symlink / hardlink；
- device / fifo；
- duplicate paths；
- unsafe exact paths。

directory entries可忽略但不得进入 plugin file set。

ZIP与tar.gz表示同一个0.5 file set时，forward restore输出必须语义等价。

这仍是普通实现bug，不改变产品行为；但因为 wrapper也会变化，两项修复应在同一新 candidate中一起冻结。

## 6. implementation 与并行工作协调

从本 Plan进入 Critic审查开始：

- old Phase C live mutation继续暂停；
- old `079bd798...` 不得安装；
- 已经指回原 Codex的 archive patch不得单独成为新 final candidate；
- 若其他工作树已经完成 archive-only diff，可在新版 Critic PASS 后由同一 Executor核对并移植，不重新设计；
- 在新版 package PASS前，不允许任何线程更新 Personal Plugin或创建G3 branch。

新的 implementation commit必须同时包含：

1. wrapper CHAT_RESPONSE reader-value selection；
2. archive ZIP/tar.gz fix；
3.对应测试和本任务 evidence更新。

## 7. cheap development validation

实现循环先跑：

- `tests/test_clear_writing_chatgpt_wrapper.py`；
- route/package parity；
- archive safety/restore equivalence；
- existing cheap skill audits；
- known local replay；
- should-not-change controls；
- `git diff --check`。

本轮不靠新增大量回归证明机制。新增/替换的核心语义案例只对应两个真实失败：

1. Bridge复杂完成汇报；
2. Phase C受阻/交接汇报。

旧数学/科研深度正例继续作为反过度压缩保护。

## 8. G2 修订，不新增顶层 Gate

### G1-B

保持原简单 ordinary-chat smoke，证明显式选择和single-entry基本工作。

### G2-T1：Bridge Kit 0.11.1 completion report — known regression

source：

```text
repo = YuukiAS/GPT_Codex_AI_Bridge_Kit
ref = ba9013b9fbbd242e51b09f9d09291f417df17652
files = README.md, QUICKSTART.md, CHANGELOG.md, AGENTS.md
```

exact user prompt：

```text
请先完整读取下面四个文件，然后详细告诉我 Bridge Kit 0.11.1 现在到底是不是可以正常用了：

repo = YuukiAS/GPT_Codex_AI_Bridge_Kit
ref = ba9013b9fbbd242e51b09f9d09291f417df17652
files = README.md, QUICKSTART.md, CHANGELOG.md, AGENTS.md

我需要知道：
- 现在主要架构到底是什么；
- 0.11.1 相比前面实际增加或修了什么；
- 我平时到底怎么用；
- 为什么你认为这版已经完成或还没完成；
- 还有哪些真正没做。

请详细解释，但按我真正需要理解的内容组织。
```

PASS：

- 第一屏直接回答可用/完成边界；
- 说明三层结构与 Lite/Review/Control + Persistent/Notifier等用户相关关系；
- 解释0.11.1真实变化；
- 给正常使用入口；
- 可信证据足够支撑判断；
- 真实未完成项不隐藏；
- 不把 rejected architecture / daemon/database/state-machine否定清单、逐项CI/audit过程当主叙事；
- 没有固定字数或标题数要求。

### G2-T2..T7

沿用 v0.2 exact inputs/semantics：

- 正式中文 Markdown；
- 中文长技术结构重写；
- English scientific prose；
- UI copy；
- exact-only；
- mixed。

### G2-T8

沿用 v0.2 necessary-long-answer exact prompt。PASS仍要求充分解释对象层级、下标、公式直觉和限制；不能因 reader-value selection而机械缩短。

### G2-T9：Phase C blocked handoff — known regression

source：

```text
repo = YuukiAS/AI_Skills_Collection
ref = 38a81dc1df9a362ecee4be597cb3db5bd6fcac41
path = results/clear-writing--single-entry-artifact-finalization/phase-c/PHASE_C_STOP_BEFORE_LIVE_MUTATION.md
```

exact user prompt：

```text
请读取下面这份 Clear Writing 0.6 Phase C 停止报告，然后直接告诉我：

1. 实际发生了什么；
2. 为什么会停；
3. 下一步唯一应该由谁接手；
4. 我现在要不要做什么；
5. 如果需要交给下一线程，直接给我完整可复制的提示词。

repo = YuukiAS/AI_Skills_Collection
ref = 38a81dc1df9a362ecee4be597cb3db5bd6fcac41
path = results/clear-writing--single-entry-artifact-finalization/phase-c/PHASE_C_STOP_BEFORE_LIVE_MUTATION.md
```

PASS：

-先讲人能理解的状态和原因；
-明确唯一下一owner；
-明确用户是否需动作；
-需要handoff时直接给完整prompt；
-必要技术证据保留；
-不把内部状态表、路径、Gate枚举当正文主体。

## 9. G3-G6

- G3 Reader Guide原合同不变；
- G4继续对完整 G2 outputs + G3 source/final 做 fidelity；
- G5继续做 package/Codex/profile compatibility；
- G6继续原 fresh长技术文档 protocol，不用 Bridge/Phase C已知样本；
- 不增加 G7。

## 10. normal-entry qualitative review

Bridge T1、Phase C T9 和 deep T8 都必须由同一新版 Personal Plugin candidate、真实 ChatGPT Web、`GPT-5.6 Sol`、explicit Clear Writing selection执行。

独立审查必须拿到：

- exact user prompt；
-所有读取source；
-完整 final chat response。

不能只看摘要、截图、关键词计数或“模型声称用了 selection”。

判定分两层：

1. fidelity / completion：事实、状态、限制、下一步无漂移；
2. reader value：完整回答问题且没有大段不改变理解/信任/行动的内部展开。

## 11. Phase C-A：archive + mutation owner

live mutation前必须通过无副作用 preflight：

1. live plugin仍是0.5.0 / USER / PRIVATE / same identity；
2. current archive真实下载为本地/host file bytes；
3. new builder能直接消费真实 archive format；
4. new candidate archive可重建并校验；
5. 0.6.1 forward restore archive + delete sets真实生成；
6. update_plugin能接收该host-uploaded archive形态。

**第2项未真实证明，不得更新0.6.0。**

Phase C-A owner仍由 Planner协调；可以使用支持本地文件与浏览器/连接器操作的执行 surface，但该 surface必须先通过上述 preflight。它不是新的项目角色，也不能修改产品语义。

## 12. Phase C-B：fresh Web gate owner

G1-B/G2/G3必须是真正 fresh ChatGPT Web conversations。

已验证当前 Planner模型没有创建另一条新ChatGPT对话并操作其模型/插件选择UI的工具。因此：

- 不再把“Planner运行在Web”当成“Planner可以自动控制fresh Web session”；
- 若执行时仍没有可用自动UI surface，这部分明确为 user-only UI action；
- Planner在执行前生成完整 `WEB_GATE_USER_PACKET.md`，包含每个 exact prompt、candidate/release identity和输出槽；
- 用户只负责：新建聊天、选择 `GPT-5.6 Sol`、显式选择 Clear Writing、粘贴并发送指定prompt、把完整原始回复交回；
- 用户不负责查仓库、判断PASS、整理证据、设计restore或选择下一owner。

所有判定与证据归档由Planner完成。

## 13. 失败与恢复

在live 0.6 mutation之前的任何失败：停止，不需要restore，正式0.5.0保持。

live mutation之后：

- G1-G6或最终artifact review的terminal PRODUCT FAIL；
- 或bounded infrastructure retry耗尽且无法继续；

均按原0.6.1 forward restore执行并放弃central 0.6 release。

Web Gate failure由Planner记录后，必须直接触发Phase C-A restore owner；用户不承担restore操作。

## 14. candidate identity

新版 implementation review PASS 后，生成新的 `FINAL_CANDIDATE.json`，至少绑定：

- new source commit；
- writing-style 0.6；
- Personal wrapper 0.6.0；
- new wrapper archive SHA-256；
- build receipt SHA；
- route projection rule；
- ZIP spec；
- archive reader/restore implementation identity；
- profile/generated Codex identity；
- Gate rule version `CW06-v0.3`。

任何 candidate-defining source改变，旧Web evidence失效。

## 15. version / release / Issue

成功release仍是：

```text
Repository bump decision: PATCH (late-bound at release time)
writing-style: 0.5 -> 0.6
Personal Plugin: 0.5.0 -> 0.6.0
other central plugins: NO_BUMP
maturity: NO CHANGE
```

本次内容选择修订仍属于尚未发布的同一0.6，不另开0.7。

Issue #13保持open / DOING；Resolution commit为空；#73/#49 downstream pending truth不变。

## 16. Critic PASS 条件

原独立 Critic只有在确认：

- content-selection owner落在wrapper且不侵犯domain evidence ownership；
- 没有把Skill冒充send-time hook；
- old candidate失效边界清楚；
- archive修复与wrapper修订不会并行冻结两个candidate；
- Phase C-A/B职责真实；
- G2替换是机制针对性验证，不是“增加更多回归”；
- deep technical route得到反过度压缩保护；
- G3-G6没有降低；
- Codex不需要再决定产品/恢复/验收语义；

才可给新版 `PASS / READY_FOR_CODEX=YES`。
