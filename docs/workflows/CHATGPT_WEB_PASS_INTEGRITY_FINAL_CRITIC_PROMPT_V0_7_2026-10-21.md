# Planner–Critic 1.8 v0.7 — 最终 execution-ready Critic Prompt

你现在担任 AI Research Stack 的独立 Critic，对 Planner–Critic 1.8 治理更新做最终 execution-ready 审查。

## Active Review Context

```text
target_repo=YuukiAS/AI_Skills_Collection
target_plugin_or_domain=ChatGPT Web Planner-Critic governance
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4
proposal_path_and_version=docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_PROPOSAL_V0_7_2026-10-21.md@v0.7
review_stage=FINAL_EXECUTION_READY_REVIEW_V0_7
```

调用方会给：

`PACKAGE_COMMIT=<exact v0.7 package commit>`

你必须从同一个 exact commit 读取本 prompt 和完整 v0.7 package。若文件来自不同快照，直接 `REVISE`。

本轮唯一允许：

```text
PASS
READY_FOR_CODEX=YES
```

或：

```text
REVISE
READY_FOR_CODEX=NO
```

不得实施。

## 1. 先读取最新正式治理事实

自行读取并核实 `YuukiAS/AI_Skills_Collection` 最新 `main` 中与本任务实际相关的 source of truth，包括但不限于：

- repository `AGENTS.md`；
- 当前正式 Planner / Critic role contracts；
- 当前生效 AI Research Stack Project setting snapshot；
- Capability Gate Policy；
- AI Skills Maintenance Board；
- ChatGPT Web collaboration regression records；
- 与 whole-response user-facing failure 直接相关的当前 writing-style evidence。

不要因为本 prompt 列出示例就缩窄读取；也不要无边界全仓审计。

首先确认 latest main 当前正式角色版本仍是什么，以及 v0.7 是否确实是尚未实施的 candidate。

## 2. 从 exact PACKAGE_COMMIT 读取完整 v0.7

至少读取：

- `results/chatgpt-web--pass-integrity/CLEAR_WRITING_PHASE_C_GOVERNANCE_FAILURE_2026-10-21.md`
- `results/chatgpt-web--pass-integrity/real-validation/case-b/ORIGINAL_REPLY.md`
- `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_PROPOSAL_V0_7_2026-10-21.md`
- `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_EXECUTION_PLAN_V0_7_2026-10-21.md`
- `docs/goals/CHATGPT_WEB_PASS_INTEGRITY_GOAL_V0_7.md`
- `docs/operations/prompts/CHATGPT_WEB_PASS_INTEGRITY_KICKOFF_DRAFT_V0_7_2026-10-21.md`
- `results/chatgpt-web--pass-integrity/EXECUTION_PACKAGE_V0_7.md`
- 本 Critic prompt。

并回查上一 package：

`5dc95e155d4890d5bd311ef7c80baab830191949`

判断 v0.7 是否真的把新增语义写入 Proposal / Plan / Goal / Kickoff，而不是只追加到 prompt。

## 3. 独立核实 Phase C 事故

读取真实 Clear Writing 0.6 evidence：

approved package：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

Phase C evidence：

`38a81dc1df9a362ecee4be597cb3db5bd6fcac41`

独立确认：

1. actual archive format/materialization 与 frozen restore builder 是否存在真实接口缺口；
2. fresh ChatGPT Web + model/plugin selection 是否确实没有在 old package 中证明执行 actor/surface；
3. 原 Phase C user-facing reply 是否真的没有完成唯一下一入口与用户可读交接。

不要因为 Planner v0.7 已给归因就直接接受。

## 4. 先判断 1.7 已经有什么，避免重复规则

这是本轮关键检查。

独立判断 current 1.7 是否已经包含：

- unknown capability 不得冒充已验证能力；
- risk-matched probe / reality check；
- “谁执行”与合法恢复路径；
- ordinary implementation bug / runtime / loader / Gate failure 默认 `RETURN_TO_CODEX`；
- execution interruption / recovery 后唯一下一用户入口；
- 一屏自然中文用户摘要。

如果这些原则已经存在：

- v0.7 必须只补“可观察 evidence obligation / acceptance application”；
- 不得把同义原则重新包装成另一套治理。

如果 v0.7 实际重复堆规则、制造平行机制，`REVISE`。

## 5. 审查 critical-interface reality evidence

判断 P18-3 / C18-4 是否真实解决 Phase C 暴露的问题，而且不过重。

重点检查：

### 5.1 scope 是否风险匹配

只能覆盖会决定：

- implementation 可否进行；
- required evidence 可否生成；
- live mutation 后能否恢复；
- cross-surface handoff 是否成立；
- upstream output 能否被 downstream消费；
- 高影响边界是否安全。

不能要求所有普通 API / 文件访问都提前做昂贵 probe。

### 5.2 evidence 是否足够具体

对关键接口是否真正要求：

- actor/surface；
- required action；
- upstream output；
- downstream consumer；
- format / identity / materialization；
- direct evidence；
- conditional assumption；
- pre-side-effect verification point；
- stop/recovery owner。

特别用 Clear Writing 事故反证：

- URL/handle 是否会再次被当成 local archive bytes；
- tool 支持 archive 是否会被误推断成 frozen builder也支持；
- “long-term Planner”是否会再次被当成能自动创建 fresh Web conversation 的执行能力。

### 5.3 conditional capability 是否诚实

若不能提前验证，v0.7 是否允许安全 conditional contract，而不是机械阻止所有 execution-ready package。

必须明确：

- 未验证 != 已验证；
- conditional verification 有 owner/surface/timing/stop/recovery；
- high-impact effect 前完成必要 probe。

## 6. 审查 non-terminal handoff closure

current 1.7 已经有唯一下一入口原则。

判断 v0.7 是否正确把它变成真实回复 acceptance，而不是又写一遍口号。

必须检查：

- current Planner 仍是 next owner 时，是否要求 Planner 自己继续，而不是让用户“再找 Planner”；
- 多 blocker / 多 owner 时是否由 Planner 排顺序；
- user-only UI action 是否最小化；
- prompt / artifact / return path 是否提前准备；
- “需要一个具备若干能力的 environment/surface”是否被明确判为不闭合；
- ordinary Q&A / completed task 是否不会机械收到 workflow prompt。

如果用户仍可能看到“去找一个能做 X 的环境”而没有真实接收方，`REVISE`。

## 7. 审查 user-facing whole-response acceptance

判断 v0.7 是否遵守“不要再堆同义写作规则”。

应当是：

- Project setting / 1.7 的自然中文规则保持；
- 新增的是对**完整实际回复**的验收；
- 非终态正文不看 machine block也能理解 status / why / remaining / owner / user action / next step；
- PASS正文不看 machine block也能理解 architecture / normal use / risk-recovery / unproven boundary；
- Clear Writing invocation / skill load 不能替代结果检查；
- 不使用固定字数、标题数、英文比例。

结合 latest main 的真实 writing-style whole-response regression，判断该设计是否方向正确。

## 8. 审查 failure routing

确认 v0.7 没有重新发明失败状态机。

对 Phase C 两个问题独立判断：

### archive format/materialization

如果能够在不改变 frozen product / acceptance / recovery semantics 下修复：

应继续同一 Clear Writing Codex task，而不是重开架构。

### fresh Web actor/surface

如果 old execution package 没有证明 actor 能力：

这是 execution responsibility / package closure 问题，应由 Planner 修订并重新 Critic 审查。

如果你认为上述分类不对，必须给 current evidence 和最小替代 owner。

## 9. 审查 real validation batch A/B/C

不得只检查字段。

### Case A

fixed package：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

supporting evidence：

`38a81dc1df9a362ecee4be597cb3db5bd6fcac41`

candidate Critic 正确结果必须是 `REVISE`。

判断要求同时发现：

1. task prompt conflict；
2. archive/materialization interface gap；
3. fresh Web actor gap；

是否合理且能真正证明 C18-4 生效。

### Case B

读取 frozen original reply。

判断候选 Planner 的完整回复验收是否真的要求：

- 0.5.0仍安全；
- stop原因；
- 两类 blocker分流；
- current user action；
- unique next owner；
- copyable handoff；
- 不靠机器字段承担主解释。

特别检查：如果 current Planner 自己是 owner，它是否必须继续做到合法 handoff point。

### Case C

fixed package：

`745e6748c5faa7cbad51973142661491224ba5a2`

task：

`055_clear_writing_release_convergence`

核实这是一个有真实历史执行/完成证据的复杂 package，而不是临时挑的简单样本。

候选 Critic 必须重新完整审查，不能沿用 historical PASS。

如果 current truth支持 PASS，则用它验证 atomic PASS + human explanation。

如果发现真实 blocker，则 `REVISE`，且同批次不能换 sample。

判断这个 fail-closed 设计是否避免“为了治理 PASS 挑赢家”。

## 10. 审查 A/B/C 的真实执行接口

这是本方案自己的现实检查。

当前 package 明确不声称 Codex/Planner 能自动创建 fresh ChatGPT Web conversation。

A/B/C 被定义为 user-only UI actions：

- 系统先准备 exact prompts / locators；
- 用户只打开指定 fresh Planner/Critic conversation并粘贴；
- 用户返回完整回复；
- 长期 Planner / Codex负责 durable evidence。

判断：

- 这个 user-only boundary 是否真实；
- 用户动作是否已经压到最小；
- 是否仍把 repo查找、prompt拼装、角色选择或 evidence整理甩给用户；
- 是否需要额外授权；
- 若平台能力未来变化，是否禁止 Codex未经审查自行替换路径。

如果这条 handoff仍含“到时候找一个 surface”，`REVISE`。

## 11. 审查 candidate / safety gate / integration

保留 v0.6 的正确机制：

- exact `GOVERNANCE_CANDIDATE_COMMIT`；
- candidate-defining source变化使旧 evidence失效；
- no separate implementation Reviewer；
- post-implementation Critic：
  `PROCEED_TO_FINAL_EVALUATION / REVISE`；
- A/B/C only after pre-final safety gate；
- all real validation pin same candidate；
- `CANDIDATE_ACCEPTED` 后才 main integration；
- `AGENTS.md 8.5` integration preflight；
- no force；
- remote-main fresh readback证明正式 1.8 生效。

如果 candidate验证与 main正式版本仍可能漂移，`REVISE`。

## 12. Scope / complexity

确认本轮没有扩大到：

- Project setting edit；
- Capability Gate Policy edit；
- Clear Writing 0.6 product edit；
- Plugin Creator edit；
- Bridge Kit edit；
- paid API；
- Personal Plugin mutation；
- repository/plugin release；
- third human role；
- new schema/state machine/database/service/watcher/daemon/prompt compiler。

Plan内的小表 / evidence manifest不算新增通用系统。

## 13. Claim ceiling

独立判断 v0.7 是否诚实说明：

- role contract是治理，不是runtime enforcement；
- 模型仍可能不遵循；
- 平台不存在的 action不能被规则创造；
- skill invocation不能保证 whole-response quality；
- 可信度来自 evidence + independent review + real normal-entry validation + fail closed。

如果 Proposal 把 1.8写成“以后一定不会再犯”，`REVISE`。

## 14. 外部核查

做少量、针对性的官方核查即可。

可核对：

- interface verification / validation 对实际接口和目标环境的成熟做法；
- instruction hierarchy；
- Git integration conflict / non-force behavior。

不要照搬外部流程，不新增框架。

## 15. Final verdict

只有全部成立，才允许：

```text
PASS
READY_FOR_CODEX=YES
```

必须确认：

- v0.7 真正解决 Phase C 暴露的三项缺口；
- 1.7已有原则没有被重复堆叠；
- critical-interface evidence可执行；
- non-terminal handoff闭合；
- whole-response acceptance真实；
- A/B/C 有明确 actor/surface/evidence path；
- Case C不允许 adaptive replacement；
- candidate/main integration闭合；
- Codex只剩普通实现细节；
- 没有关键产品/架构/权限/验收/恢复决定留给 Codex。

否则：

```text
REVISE
READY_FOR_CODEX=NO
```

只阻塞真实问题。

## 16. 用户回复合同

无论 PASS / REVISE，先给一屏自然中文。

### 若 PASS

必须直接讲清：

- 1.8原来已经解决什么；
- v0.7新增解决什么；
- 关键接口现在如何防止“批准后才发现根本跑不了”；
- 非终态回复如何防止“停了却不知道给谁”；
- A/B/C怎样验证；
- user-only Web actions是什么；
- 1.8不能技术强制什么；
- 用户现在是否只需发送 Codex handoff。

然后给 exact approved locators：

```text
APPROVED_PROPOSAL_PATH=
APPROVED_PLAN_PATH=
APPROVED_GOAL_PATH=
APPROVED_KICKOFF_PATH=
APPROVED_PACKAGE_COMMIT=
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

最后给短：

```text
=== COPY TO CODEX BEGIN ===
...
=== COPY TO CODEX END ===
```

不得全文复制 Kickoff。

### 若 REVISE

给：

`NEXT_HANDOFF=PLANNER`

并自动生成完整 `COPY TO PLANNER`，不让用户自己整理 finding。

本轮不得实施、不得创建 execution branch/worktree、不得修改 main、不得修改 Clear Writing、不得运行 A/B/C、不得启动 paid validation。
