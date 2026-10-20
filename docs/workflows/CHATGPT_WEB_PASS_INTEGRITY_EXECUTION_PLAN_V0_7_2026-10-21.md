# Planner–Critic 1.8：执行接口真实性与非终态交接 — Execution Plan v0.7

日期：2026-10-21  
任务键：`chatgpt-web--pass-integrity`  
Proposal：`docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_PROPOSAL_V0_7_2026-10-21.md`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`  
计划执行分支：`reviewed/chatgpt-web--pass-integrity`  
计划执行工作树：`/tmp/ai-skills-chatgpt-web-pass-integrity`  
状态：`DRAFT_FOR_FINAL_EXECUTION_READY_CRITIC`  
当前 `READY_FOR_CODEX=NO`

## 1. 实施目标

在现有 1.8 设计基础上完成三项补强：

1. 把 1.7 已有的“现实检查 / 谁执行 / 失败恢复”原则变成关键接口的可观察 evidence obligation；
2. 把 1.7 已有“非终态唯一下一入口”变成真实 user-facing handoff 的硬验收对象；
3. 把 1.7 已有用户摘要要求变成 whole-response acceptance，而不是字段/Skill invocation 检查。

同时保留 v0.6 的：

- task-prompt compatibility；
- atomic execution-ready PASS；
- PASS 后解释/矛盾/新要求分类；
- `GOVERNANCE_CANDIDATE_COMMIT`；
- post-implementation Critic safety gate；
- main integration + remote readback；
- 无第三人工角色、无新状态机/服务/数据库。

## 2. 实施文件范围

candidate-defining source 允许修改：

1. `docs/workflows/PLANNER_ROLE_CONTRACT.md`
2. `docs/workflows/CRITIC_ROLE_CONTRACT.md`
3. `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`
4. `results/chatgpt-web--pass-integrity/GOVERNANCE_CANDIDATE_MANIFEST.md`
5. `results/chatgpt-web--pass-integrity/v1_8_contract_replay/CONTRACT.md`
6. `results/chatgpt-web--pass-integrity/real-validation/CONTRACT.md`
7. `results/chatgpt-web--pass-integrity/real-validation/case-a/**`
8. `results/chatgpt-web--pass-integrity/real-validation/case-b/**`
9. `results/chatgpt-web--pass-integrity/real-validation/case-c/**`

真实 Case C 成功后才允许更新：

- `docs/workflows/CHATGPT_WEB_CRITIC_GOOD_REVIEW_EXAMPLES_2026-10-20.md`

最终收口时按真实结果更新：

- `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`
- `results/chatgpt-web--pass-integrity/FINAL_CLOSURE_*.md`

明确不改：

- AI Research Stack Project setting；
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`；
- Clear Writing 0.6 product/source/G1-G6；
- Bridge Kit；
- Plugin Creator；
- repository/plugin version；
- README。

Repository bump：NONE。  
Affected plugins：NONE。  
README checked: no update required。

## 3. Planner Role Contract 1.8 具体修改

### P18-1 — task-specific Critic prompt compatibility

保留 v0.6：

Planner 形成 execution-ready Critic prompt 前，必须确认 task prompt 不会：

- 缩窄最终全量审查；
- 改写 verdict / `READY_FOR_CODEX` / `NEXT_HANDOFF`；
- 省略架构说明或短 `COPY TO CODEX`；
- 要求全文复制批准前 Kickoff；
- 把等待用户再索取执行入口当正常 PASS。

### P18-2 — short Codex handoff renderability

保留 v0.6：

Planner 送最终审查前必须能够从冻结 Proposal/Plan/Goal/Kickoff/authorization 生成一段不猜测、不扩权的短 Codex handoff。不能生成则 execution package 不闭合。

### P18-3 — critical-interface reality evidence

这是本轮新增的主要行为。

Planner 不再只写“使用工具 X / 由角色 Y 执行 / 失败后 restore”。

对会决定实施、required evidence 或安全恢复能否成立的关键接口，Plan/Runbook 必须写清：

- actor / surface；
- required action；
- upstream output；
- downstream consumer；
- format / identity / materialization contract；
- 当前直接 evidence；
- 未验证部分；
- 若只能实施中验证：verifier owner、exact surface、验证时点、必须早于哪个 side effect、失败 stop 与 recovery。

不要求独立 registry。直接写在当前 Plan/Runbook 即可。

#### P18-3a：何时必须提前 probe

若存在合法、无副作用、低成本的小 probe，而且该接口失败会使任务无法实施或恢复，则 execution-ready 前应优先做 probe。

不得为了“提前验证”越过用户授权、账户变更、付费、private transfer、destructive effect。

#### P18-3b：条件性能力

只有当前有直接 evidence 的能力可以称已验证。

无法提前验证但允许实施中验证时，Plan 必须明确这是 conditional capability，并冻结：

- 谁验证；
- 在哪里验证；
- 先于哪个 live/high-impact effect；
- fail 时谁接手；
- 是否需要 restore。

不能把 conditional capability 写成“execution surface supports X”。

### P18-4 — non-terminal handoff closure

这是对现有 §10.1 的 operationalization，不复制“唯一下一入口”原则。

Planner 处理 Critic 结果、执行中断、恢复结果、实现后阻塞时，只要任务仍需继续：

- 先把已完成 / 未完成说清；
- 对不同 blocker 分开归因和 owner；
- 判断用户现在是否需要动作；
- 如果下一 owner 是当前 Planner，Planner 必须继续做自己能合法完成的工作，不得把“找 Planner”交回用户；
- 多个 owner 时由 Planner 排定合法顺序；
- 只有需要用户切换 thread / UI / private upload / authorization 时才交用户；
- 一旦需要用户转交，必须把完整 prompt / exact artifact list / 回传方式准备好；
- “需要一个具备 X 能力的环境”不算 next entry。

Planner 的 user-facing summary 本身必须让用户在不读 machine block 的情况下知道当前状态和下一步。

## 4. Critic Role Contract 1.8 具体修改

### C18-1 — task-prompt compatibility hard gate

保留 v0.6。

冲突 package 不得 PASS；Critic 继续完成可完成的其他审查，尽量一轮报全。

### C18-2 — atomic execution-ready PASS

保留 v0.6。

同一回复必须有：

1. 一屏实际架构说明；
2. exact approved locators；
3. `READY_FOR_CODEX=YES`；
4. `NEXT_HANDOFF=CODEX`；
5. 短 `COPY TO CODEX`。

缺一项不存在有效 PASS。

### C18-3 — PASS 后解释稳定性

保留 v0.6：

- explanation；
- contradiction evidence；
- new requirement。

### C18-4 — critical-interface evidence hard gate

这是本轮新增的 execution-ready 审查义务。

Critic 必须挑出**风险匹配的关键接口**，而不是所有 API。

对每个关键接口问：

- 谁执行；
- 实际 surface 有无所需 action；
- 上游真实返回什么；
- 下游真实接受什么；
- 格式和 materialization 是否匹配；
- evidence 是直接事实还是文档假设；
- 若只能实施中验证，是否在任何 live/high-impact side effect 前有明确 probe；
- probe fail 是否能安全停止并有 owner/recovery。

以下都不能单独证明 interface ready：

- 配置里写了工具名；
- tool doc 说理论支持；
- 拿到 URL/handle/receipt；
- builder 单测通过；
- 另一个环境成功过；
- Plan 写了 restore。

如果 interface 是 required 且失败会使任务无法继续/恢复，而既没有 VERIFIED evidence，也没有完整 conditional contract，结论必须 `REVISE`。

### C18-5 — handoff/readability acceptance

1.7 已要求一屏自然中文和唯一下一入口；1.8 新增的是**判定标准**。

对于需要继续推进的非终态回复，Critic/Planner review 必须实际阅读整条 user-visible response，判断用户是否无需机器块就能知道：

- 发生了什么；
- 为什么停；
- 还差什么；
- 谁负责；
- 自己现在要不要做什么；
- 下一步怎样真正进入。

对于 final PASS，整条说明必须让用户理解实际架构、正常使用、风险/恢复和未证明边界。

以下不能作为通过依据：

- 五个字段出现了；
- 回复更短了；
- 英文少了；
- Clear Writing/response-clarity 被调用了；
- 机器状态完整。

不得设置固定字数、标题数或英文比例。

## 5. 1.8 candidate freeze

Codex 完成上述 source 修改与 candidate contracts 后，先提交 candidate-defining commit：

`GOVERNANCE_CANDIDATE_COMMIT=<exact sha>`

manifest：

`results/chatgpt-web--pass-integrity/GOVERNANCE_CANDIDATE_MANIFEST.md`

必须记录：

- exact commit；
- Planner/Critic 1.8 path/version/hash；
- collaboration regression candidate hash；
- deterministic replay contract hash；
- real A/B/C validation contract hash；
- base main；
- exact branch/worktree；
- candidate-defining allowlist。

候选冻结后：

- candidate-defining source 不得变化；
- evidence 可以追加，但必须记录 exact candidate；
- candidate-defining source 变化则旧 evidence 失效。

## 6. Deterministic replay

保留 v0.6 的 8 个 mechanical/semantic contract case：

1. old Clear Writing conflicting prompt；
2. PASS without architecture summary；
3. PASS without Codex handoff；
4. full Kickoff dump；
5. blocker priority + full final review；
6. follow-up explanation；
7. contradiction discovered during explanation；
8. explicit new requirement。

这部分只证明合同机械/局部语义，不证明真实 normal-entry reply quality 或关键接口可执行性。

## 7. 本任务自己的关键接口检查

本治理 package 必须先满足自己新增的 P18-3/C18-4。

### I1 — Git / GitHub candidate + integration

- actor：Codex executor；
- surface：exact repo worktree + Git remote；
- action：candidate commit、non-force branch push、integration preflight、merge/push main、fresh readback；
- evidence：当前 `AGENTS.md 8.5` + repo Git normal path；
- status：可在 execution 中于 main mutation 前验证 current main / branch / conflict；
- fail boundary：任何 merge conflict / same-area competing change -> STOP -> Planner/Critic；
- forbidden：force/history rewrite。

### I2 — fresh ChatGPT Web A/B/C validation

当前没有验证到一个自动 tool 能替用户创建 fresh ChatGPT Web conversation 并绑定 candidate role contract。

因此不得声称自动化。

冻结为 user-only UI handoff：

- Planner/Codex 预先生成 exact prompts 和 locators；
- 用户只需打开指定 fresh Planner/Critic conversation 并粘贴；
- 用户把完整回复返回长期 Planner；
- 长期 Planner 记录 durable evidence并继续；
- 用户不查 repo、不拼 prompt、不选内部 Reviewer。

这是明确的 conditional/user-only path，而不是隐藏依赖。

### I3 — GitHub evidence recording

- actor：长期 Planner 或同 task Codex；
- input：用户返回的完整 A/B/C reply；
- output：`results/chatgpt-web--pass-integrity/real-validation/**`；
- 若当前 Planner connector 不可写，则 Codex 在同一 task 保存；不能让用户自己建 evidence file。

### I4 — Project tracking

不属于本次 1.8 正确性的 blocking interface。

若仍没有 Project mutation surface，继续按 Maintenance Board 保留 exact pending mutation；不要求用户维护。

## 8. Post-implementation Critic safety gate

不新增 implementation Reviewer。

candidate freeze + deterministic checks 完成后，由独立 Critic直接读取：

- actual diff；
- exact candidate；
- Planner/Critic 1.8 full text；
- candidate manifest；
- deterministic replay evidence；
- critical-interface evidence；
- A/B/C frozen prompts / sources / expected evaluation contract。

只允许：

`PROCEED_TO_FINAL_EVALUATION`

或

`REVISE`

只有前者才能运行真实 A/B/C。

## 9. Real validation batch

### Case A — Clear Writing 0.6 historical negative execution-ready review

固定 package：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

固定 supporting reality evidence：

`38a81dc1df9a362ecee4be597cb3db5bd6fcac41`

运行方式：

- fresh independent Critic；
- 读取 candidate 1.8 exact contracts；
- 读取 old Clear Writing package；
- 可使用当前 Plugin Creator tool contract与 Phase C evidence作为现实证据；
- 不修改 Clear Writing，不做 live mutation。

PASS condition for governance Case A：

Critic 必须 `REVISE` old Clear Writing package，并至少识别：

1. task-specific final Critic prompt 与中央合同冲突；
2. Plugin Creator archive → restore builder / materialization 关键接口未被证明；
3. fresh ChatGPT Web actor/surface 未被证明。

只识别第 1 项、却仍把第 2/3 项当“实现时再看”，Case A FAIL。

### Case B — Phase C non-terminal Planner reply

固定 input：

- old approved package；
- Phase C evidence commit；
- 用户当时收到的完整 Phase C reply，保存于：
  `results/chatgpt-web--pass-integrity/real-validation/case-b/ORIGINAL_REPLY.md`

运行方式：

- fresh Planner conversation；
- 明确 candidate role authority = exact `GOVERNANCE_CANDIDATE_COMMIT`；
- 不要求 Clear Writing selection；
- 不修改任何 repo/product；
- 只要求 Planner基于 current rules处理该 stop。

合格输出必须：

- 第一屏直接说明 0.5.0仍安全、未 mutation；
- 把 archive compatibility 与 execution responsibility 分开归因；
- archive compatibility 默认归同一 Clear Writing Codex task，除非修复会改变 frozen semantics；
- execution responsibility / fresh Web actor 缺口由 Planner负责；
- 当前用户动作说清楚；
- 不能要求用户寻找“同时具备两种能力的 surface”；
- 若当前 Planner 还能继续设计归因/修订，应继续做到合法 handoff 点；
- 最终给唯一下一入口与完整可复制内容。

评价整条回复，不做关键词 oracle。

### Case C — complex positive execution-ready review

固定 exact package：

`745e6748c5faa7cbad51973142661491224ba5a2`

task：

`055_clear_writing_release_convergence`

historical review evidence：

`docs/design/clear-writing/NEXT_RELEASE_EXECUTION_CRITIC_REVIEW_R2.md`

historical completion evidence：

`results/055_clear_writing_release_convergence/FINAL_REPORT.md`

运行方式：

- fresh independent Critic；
- 读取 candidate 1.8 exact contracts；
- 对 exact package 做新的完整 execution-ready review；
- 历史 PASS 只作 evidence，不能决定 verdict；
- 不重复执行 paid call / product gates。

若 current evidence仍支持 execution-ready PASS：

- 必须给 atomic五项；
- 用户摘要必须真正讲清架构、manual user upload、private/paid boundary、失败恢复、未证明边界。

若发现真实 blocker：

- `REVISE`；
- Case C 本批次失败；
- 不允许自动换另一个 sample；
- governance candidate 不进入 `CANDIDATE_ACCEPTED`；
- 新正控只能在新的 Planner/Critic 决策后冻结。

## 10. Fresh Web 用户操作边界

A/B/C 需要 fresh ChatGPT Web，而当前无 verified automation。

因此本任务在最终 execution-ready PASS 后的授权范围必须提前说明：

用户在 final-evaluation 阶段预计需要做最多三次最小 UI 操作：

1. 打开 Case A Critic fresh conversation，粘贴已经准备好的 exact prompt；
2. 打开 Case B Planner fresh conversation，粘贴 exact prompt；
3. 打开 Case C Critic fresh conversation，粘贴 exact prompt；
4. 把三条完整回复返回长期 Planner。

不要求用户读 repo、找 commit、拼 prompt、选择内部角色或自己决定 verdict。

如果到执行时平台提供了已经验证的等价自动入口，可以由 Planner/Critic单独确认是否等价；不得由 Codex自行替换 user-only path。

## 11. Candidate acceptance

只有同时成立：

- deterministic replay符合 contract；
- post-implementation Critic = `PROCEED_TO_FINAL_EVALUATION`；
- Case A = expected REVISE with interface findings；
- Case B = handoff/readability PASS；
- Case C = genuine execution-ready PASS with atomic delivery；
- user-visible full replies通过定性检查；
- candidate/source identity未变化；

才记录：

`CANDIDATE_ACCEPTED`

任何 Case fail：
- 保留完整输出；
- 按 root cause 返回 Codex 或 Planner；
- 不换题、不补 sample、不挑赢家。

## 12. Main integration

达到 `CANDIDATE_ACCEPTED` 后：

1. `git fetch origin main`；
2. integration preflight；
3. 检查 Planner/Critic contract与 regression/result area 的竞争修改；
4. ordinary non-force merge；
5. ordinary non-force push main；
6. remote-main fresh readback：
   - Planner Role Contract version = 1.8；
   - Critic Role Contract version = 1.8；
   - 两份合同 hash = candidate manifest；
   - regression/final evidence绑定同一 candidate；
7. 记录 integration commit / main tip。

merge conflict 或 same-area drift：

`STOP -> Planner/Critic`

不 force，不 history rewrite。

本任务不做 release。

## 13. 执行授权

只有最终 Critic 对本 v0.7 exact package 给出：

`PASS + READY_FOR_CODEX=YES`

并且用户实际发送批准的短 `COPY TO CODEX` 后，才授权：

```text
task_key=chatgpt-web--pass-integrity
execution_branch=reviewed/chatgpt-web--pass-integrity
execution_worktree=/tmp/ai-skills-chatgpt-web-pass-integrity
```

授权包括：

- exact branch/worktree；
- ordinary non-force task-branch push；
- 修改本 Plan allowlist；
- candidate freeze / deterministic evidence；
- post-implementation Critic bundle preparation；
- A/B/C exact prompts/evidence preparation；
- all validation完成后的 main integration preflight/merge/push/readback。

不授权：

- Project setting edit；
- Capability Gate Policy edit；
- Clear Writing 0.6 product edit；
- Plugin Creator edit；
- Bridge Kit edit；
- paid API；
- Personal Plugin mutation；
- force/destructive Git；
- release。

## 14. Stop conditions

立即停止并回 Planner/Critic，如果：

- 必须修改 Project setting 才能实现本方案；
- critical-interface evidence要求扩大权限/provider/data/cost；
- candidate 1.8 source需在真实 batch中修改；
- A/B/C frozen source需要换题；
- Case C出现真实 blocker；
- fresh Web user-only handoff无法按冻结路径取得完整输出；
- main integration有 conflict / same-area competing change。

普通 implementation/doc bug不改变冻结语义时留在同一 Codex task。
