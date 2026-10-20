# Planner–Critic 1.8：执行接口真实性、非终态交接与用户可读验收 — Proposal v0.7

日期：2026-10-21  
任务键：`chatgpt-web--pass-integrity`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`  
上一执行包：`5dc95e155d4890d5bd311ef7c80baab830191949`  
当前正式治理基线：`main@de460300f55b5617654dd50b2a5cfec9ab89a094`  
阶段：Planner 最后一轮有边界修订；仍需独立 Critic；不得实施

## 1. 当前 1.8 已经解决什么

现有 v0.6 继续保留，不重开：

1. task-specific Critic prompt 不能覆盖中央 Critic 合同；
2. execution-ready `PASS` 必须同一回复一次交齐：
   - 一屏实际架构说明；
   - exact approved locators；
   - `READY_FOR_CODEX=YES`；
   - `NEXT_HANDOFF=CODEX`；
   - 短 `COPY TO CODEX`；
3. 不完整 PASS 不能靠后续消息零散补齐追认；
4. PASS 后区分解释请求、矛盾证据、新要求；
5. 唯一 `GOVERNANCE_CANDIDATE_COMMIT` 绑定同一 1.8 候选及其验证；
6. 治理候选通过后按 `AGENTS.md 8.5` 做 main integration、push 与 fresh readback；
7. 不新增第三人工角色、状态机、数据库、服务、watcher、daemon 或 prompt compiler。

这些机制解决了“最终 PASS 只关旧 blocker”“PASS 后不给 Codex 入口”“候选验证与 main 正式版本漂移”等问题，但不足以防止 Clear Writing 0.6 Phase C 暴露的新失败。

## 2. 本轮真实事故

真实证据：

- Clear Writing 0.6 approved package：
  `d7b810d194ead881303aaca9c2e4f1d59a97c1f1`
- Phase C evidence：
  `38a81dc1df9a362ecee4be597cb3db5bd6fcac41`
- 治理事故摘要：
  `results/chatgpt-web--pass-integrity/CLEAR_WRITING_PHASE_C_GOVERNANCE_FAILURE_2026-10-21.md`

实际发生：

1. Plugin Creator 返回 `current.tar.gz` / `application/gzip`，冻结 restore builder 只会以 ZIP 读取；
2. `get_owned_plugin_archive` 给的是下载 URL / archive identity，批准包没有证明该执行面能把真实 archive bytes 物化并交给 builder/update；
3. G1-B/G2/G3 要求 fresh ChatGPT Web + `GPT-5.6 Sol` + explicit Clear Writing selection，但批准包指定的长期 Planner 没有被证明具备创建新对话、切换模型和选择插件的动作；
4. 安全停止后的 Planner 回复没有完成用户交接，只说“需要一个同时具备若干能力的执行面”，没有给唯一下一入口和可直接使用的交接内容；
5. 回复把大量内部状态放在用户正文前部，用户必须自己从机器字段和 blocker 描述中推断“发生了什么、谁修、我现在要做什么”。

## 3. 先核对 1.7：原则已经存在，缺的是可观察证据与实际应用

本轮不重复写已有原则。

当前正式 Planner/Critic 1.7 已经明确：

- Planner 五遍预检中的“现实”与“执行”要求真实能力、环境与恢复，未知能力先设计受控小探针，不能把假设当已验证功能；
- 正常使用六问要求回答用户怎样开始、实际发生什么、失败怎样恢复、唯一下一入口是什么；
- Critic 已要求查清“谁执行”、关键环境假设是否有受批准探针、失败能否按现有接口恢复；没有合法恢复路径应在执行前指出；
- Planner §10.1 已覆盖执行中断/恢复结果，并要求唯一下一用户入口；
- Critic 已规定批准范围内普通 bug、漏接、配置、runtime/loader、测试/CI、已批准 Gate failure 默认 `RETURN_TO_CODEX`；
- Planner/Critic 已要求用户可见摘要先用自然中文说明结论、影响、剩余问题、用户动作和下一接收方。

因此，本轮不是再写“要检查现实”“要说人话”“要给下一入口”。

1.8 新增的是三项**可验证义务**：

1. 关键执行接口必须有可观察的 reality evidence；
2. 非终态交接必须以真实用户回复能否继续任务作为 acceptance object；
3. 用户可读说明必须整体验收，不能靠字段存在或“调用过 Clear Writing”冒充合格。

## 4. 新增机制一：关键执行接口 Reality Evidence

### 4.1 什么才算关键接口

只检查若失败会直接造成以下任一后果的接口：

- 当前任务根本无法实施；
- required evidence 无法生成；
- live mutation 后无法安全恢复；
- 必须跨 surface / tool / actor 才能继续；
- 上游产物无法被下游真实消费；
- 错误假设会导致权限、数据、费用或 destructive risk 扩大。

普通本地函数调用、常规文件读取、低风险实现细节不机械进入此检查。

### 4.2 Planner 的证据义务

对每个关键接口，Planner 必须在既有 Plan/Runbook 中写清：

- 真正执行者 / surface；
- 所需具体动作；
- 上游真实输出对象；
- 下游真实接受对象；
- 格式 / identity / materialization 是否匹配；
- 当前证据是什么；
- 哪些已验证，哪些只能在实施中条件性验证；
- 如果只能实施中验证：谁验证、在什么副作用之前验证、失败后在哪里停止、怎样恢复。

不新增全局 registry、数据库或 checklist service。允许用 Plan/Runbook 中一张小表或若干段落表达。

### 4.3 VERIFIED 与 CONDITIONAL 的边界

`VERIFIED` 只用于已有直接证据的能力。

如果当前不能无副作用验证，只能写成条件性假设，并冻结：

- verifier owner；
- exact execution surface；
- verification timing；
- 必须发生在何种 live/high-impact side effect 之前；
- failure stop；
- recovery / next owner。

条件性假设不得在 execution-ready 审查中被描述为“已经可执行”。

### 4.4 Critic 的应用方式

最终 execution-ready Critic 不接受“Plan 写了工具名 / 执行者 / restore 步骤”作为能力证据。

Critic 至少检查：

- actor 是否真实拥有需要的动作；
- 上游输出与下游输入是否真实兼容；
- URL / handle / receipt 是否被错误当成可消费 bytes/artifact；
- external tool 的真实 file/data format 是否与 builder/runtime 支持一致；
- 若仅能实施中验证，安全验证点是否在 live mutation / irreversible effect 之前；
- 失败是否有冻结 owner 和恢复路径。

如果关键接口既未验证，也没有合法的条件性验证与 fail-closed 路线，必须 `REVISE`。

## 5. 新增机制二：所有真正非终态的交接必须“闭合”，而不是只报告 blocker

1.7 已要求唯一下一入口；1.8 不重复该原则，而是定义“什么时候才算真的完成交接”。

一个尚未结束、仍需继续推进的 Planner/Critic 回复，只有同时满足以下语义才算 handoff closed：

- 用户能知道实际完成了什么、什么没完成；
- blocker 被分开归因，不能把普通实现 bug 和架构缺口混成“需要更强环境”；
- 明确用户现在是否需要动作；
- 明确唯一下一责任方；
- 明确接收方要完成什么；
- 存在真实可执行入口；
- 若需用户转发，直接给完整可复制内容；
- 若下一责任仍是当前 Planner，应由当前 Planner 继续完成其能合法完成的工作，不能把“回 Planner”转嫁给用户；
- 若多个 blocker 属于不同 owner，当前 Planner 负责确定顺序，不让用户自己选路线；
- “需要一个具备 X/Y 能力的环境 / surface”不构成 next entry，除非已经确定具体接收者、进入方式和失败恢复。

真正 user-only 的 UI 动作允许存在，但必须：

- 证明自动入口不存在或未验证；
- 把用户动作压到最小；
- 其余 prompt、locator、证据包与恢复安排预先准备好；
- 用户完成动作后有明确回传入口。

普通问答、已结束任务不机械附加 prompt。

## 6. 新增机制三：用户可读性本身是 acceptance object

Project setting 与 1.7 已有正确写作规则，本轮不增加禁词、字数、标题数或英文比例规则。

1.8 只新增验收方式：

### 非终态回复

即使完全不看后面的机器块，用户也必须能从正文知道：

- 目前真实状态；
- 为什么停；
- 哪些还没完成；
- 谁负责下一步；
- 自己现在需不需要做什么。

### 最终 PASS 回复

即使不读 locators / machine block，用户也必须能从正文理解：

- 实际批准的架构；
- 正常怎么用；
- 主要安全/恢复边界；
- 什么仍未证明；
- 为什么现在可以交给 Codex。

### 验收方法

- 判断完整最终回复，不只检查五个字段是否出现；
- Clear Writing 可以辅助表达，但“读取过 skill / 调用过写作规则”不是通过证据；
- 不设置机械长度阈值；
- 技术、科研和安全所需细节可以保留，只要求其确实帮助用户判断。

当前 main 的 `docs/plugin-todos/writing-style.md` 已记录另一项真实证据：即使 `response-clarity` 已实际加载，完整回复仍可能失控。因此本治理必须看最终 whole response，而不是 invocation receipt。

## 7. 失败分流保持现有语义，不新增平行状态机

本轮明确沿用 1.7：

- 普通实现 bug、漏接、配置、runtime/loader、已批准 Gate 内失败：
  `RETURN_TO_CODEX`；
- 必须改变用户承诺、架构 owner、权限、验收或 recovery semantics：
  回 Planner；
- 需要独立重新审查冻结方案：
  Critic；
- 只有用户能完成的真实 UI / private upload / authorization：
  最小 user-only action。

对 Clear Writing Phase C 的当前证据，治理回归应期待：

- archive format/materialization 兼容问题：若无需改变 frozen product/recovery semantics，则属于同一 Clear Writing Codex task 的实现接口修复；
- fresh Web actor/surface 未被证明：属于 execution package / responsibility closure 问题，应由 Planner 修订并重新交 Critic；
- 用户不负责寻找“哪个 surface 同时会两件事”。

这只是治理回归中的归因期望，不授权本任务直接修改 Clear Writing。

## 8. 真实验证批次：A / B / C

不新增顶层 Gate。将 v0.6 原有的真实回归改为一个冻结的三案例验证批次；机械 8-case replay 继续保留。

### Case A — 原 Clear Writing 0.6 execution-ready package

固定：

`CLEAR_WRITING_OLD_PACKAGE=d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

候选 Critic 必须完整审查，不能只发现 task-prompt compatibility conflict。

它还必须追问至少两个关键执行接口：

1. Plugin Creator archive / restore builder：
   - 当前 tool contract 允许 archive 为 ZIP 或 tar.gz；
   - Phase C 真实返回 tar.gz；
   - old package 未证明真实 archive format/materialization 能被冻结 builder 消费。
2. fresh Web Gate actor：
   - old package 需要 fresh ChatGPT Web + explicit selection；
   - long-term Planner 没有被证明拥有创建新 conversation / 选择 model / 选择 plugin 的动作。

如果这些 critical interface 仍无直接 evidence 或安全的 conditional verification contract，正确结论必须保持 `REVISE`。

仅修 task prompt 措辞不得把该 old package 变成 PASS。

### Case B — Phase C 安全停止后的 Planner 用户回复

固定 evidence：

`38a81dc1df9a362ecee4be597cb3db5bd6fcac41`

固定真实回复文本保存在本治理结果目录。

用 candidate Planner 1.8 在 fresh ChatGPT Web 中处理同一停止证据。

完整回复必须让用户直接知道：

- Personal Plugin 仍是 0.5.0，未发生 live mutation；
- 为什么停止；
- archive 兼容问题由同一 Clear Writing Codex task 修，前提是不改变冻结语义；
- fresh Web execution responsibility 缺口由 Planner 负责修订并重新交 Critic；
- 用户当前是否需要动作；
- 唯一下一入口；
- 若需要转交，直接给完整 handoff。

机器状态可以附后，但不能承担主要解释责任。

### Case C — 已有真实完成记录的复杂 execution-ready 正控

为了不在看到 candidate 输出后挑简单样本，本轮现在就冻结：

`POSITIVE_COMPLEX_PACKAGE=745e6748c5faa7cbad51973142661491224ba5a2`

对象：

`055_clear_writing_release_convergence`

其历史 execution-ready review：

`docs/design/clear-writing/NEXT_RELEASE_EXECUTION_CRITIC_REVIEW_R2.md`

历史证据表明该 package 后续真实执行并完成 main integration；因此它是复杂、真实、非合成正控，而不是为 1.8 临时挑选的简单案例。

candidate Critic 1.8 必须对该 exact package 做**新的完整 execution-ready review**，不得机械沿用历史 PASS，也不得被旧 review 的“只复核 C1–C4”范围缩窄。

若 current truth 支持 PASS：

- 同一回复必须完成 atomic PASS 五项；
- 用户正文必须真正讲清实际架构、manual user handoff、paid/private boundary、失败恢复和未证明边界。

若 1.8 发现真实 blocker：

- 正常 `REVISE`；
- 本治理 candidate 不得为了得到正样本而换题；
- 同一验证批次内禁止替换 Case C；
- 后续是否选另一个正控必须回新的 Planner/Critic 决策，而不是 Codex 自行补样本。

## 9. 真实 ChatGPT Web 验证的执行者与交接

本治理任务自身必须遵守新增接口真实性规则。

当前没有已验证的自动动作可以让 Codex / Planner 创建“fresh ChatGPT Web conversation”并在其中绑定 candidate role contract。因此 A/B/C 的真实 Web 运行明确冻结为 user-only UI action，而不是假装自动化：

- Codex/Planner 事先生成三份 exact prompt + exact source locators；
- 用户只负责创建对应 fresh ChatGPT Web conversation、粘贴 exact prompt，并把完整回复返回长期 Planner；
- 不要求用户查 repo、选内部 reviewer、拼 finding 或决定路由；
- 长期 Planner 负责把返回结果写入 durable evidence，并继续判断；
- A/B/C 都不需要 paid API；
- Case B 不要求选择 Clear Writing；它验收 Planner contract 本身；
- Case A/C 是 independent Critic review；
- 若平台无法读取 candidate commit 或必要 source，记录 infrastructure failure，不换样本。

这是当前已知平台边界下的明确 user-only handoff，不宣称存在自动新建 conversation 能力。

## 10. 候选身份、实现后安全门与 main integration

继续保留 v0.6：

`GOVERNANCE_CANDIDATE_COMMIT=<exact implementation candidate commit>`

candidate-defining source 至少包括：

- Planner Role Contract 1.8；
- Critic Role Contract 1.8；
- collaboration regression 候选；
- deterministic replay contract；
- A/B/C real-validation contract；
- candidate manifest。

后续 evidence 必须绑定同一 candidate commit。candidate-defining source 改变则旧 evidence 失效。

实现后不新增 separate implementation Reviewer。由既有 post-implementation Critic safety gate直接读取：

- actual diff；
- exact candidate；
- 两份 1.8 合同；
- deterministic evidence；
- A/B/C prompt/evidence contract；
- critical-interface evidence；
- user-handoff contract。

只允许：

`PROCEED_TO_FINAL_EVALUATION / REVISE`

只有 `PROCEED_TO_FINAL_EVALUATION` 后运行 A/B/C。

A/B/C 全部达到其冻结正确结果后才记录治理 `CANDIDATE_ACCEPTED`，随后按 `AGENTS.md 8.5`：

task branch -> integration preflight -> merge main -> non-force push -> remote main fresh readback。

fresh readback必须证明 Planner/Critic 正式版本均为 1.8 且与候选一致。

## 11. 修改范围

允许中央治理修改：

- `docs/workflows/PLANNER_ROLE_CONTRACT.md` → 1.8；
- `docs/workflows/CRITIC_ROLE_CONTRACT.md` → 1.8；
- `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`；
- 真实正控成功后按证据更新 `docs/workflows/CHATGPT_WEB_CRITIC_GOOD_REVIEW_EXAMPLES_2026-10-20.md`；
- `results/chatgpt-web--pass-integrity/**`。

不修改：

- current Project setting；
- `PLUGIN_CAPABILITY_GATE_POLICY.md`；
- Clear Writing 0.6 product/source/G1-G6；
- Bridge Kit；
- Plugin Creator；
- repository/plugin release；
- 新角色/schema/state machine/database/service/watcher/daemon/prompt compiler。

## 12. 为什么 Project setting 不改

当前 Project setting 已经明确：

- 真实能力高于文档声明；
- 正常入口和实际消费对象优先；
- 入口不明时暂停；
- 非终态不把角色选择甩给用户；
- 用户可见解释默认自然中文、结论先行；
- 交给 Codex 前关键 Planner/Critic 决策和必要用户选择应闭合。

本次缺口是这些原则没有被 role-level evidence 与真实回复验收充分落实。Planner/Critic 1.8 可以解决，不需要继续向 Project setting 堆同义规则。

## 13. Claim ceiling：1.8 仍不能保证什么

Planner/Critic 1.8 是治理合同，不是 runtime enforcement hook。

它能够：

- 要求关键能力有现实证据；
- 把未验证假设显式标成 conditional；
- 让 independent Critic 在证据不足时拒绝 PASS；
- 让非终态回复没有闭合 handoff 时被判不合格；
- 用真实 whole-response replay发现模型没有遵守规则。

它不能保证：

- 模型永远不会忽略 prompt；
- ChatGPT 平台一定提供某个自动 UI action；
- 仅因为合同存在，所有 thread 都必然逐字遵守；
- Clear Writing 被加载就一定控制最终整篇回复。

因此 1.8 的可信度来自“证据 + 独立审查 + 真实正常入口验证 + 失败不接受”，不是把文档规则冒充技术强制。

## 14. 外部核查

本轮只采用成熟的轻量原则，不引入外部框架：

- NASA 软件工程手册强调接口要求本身属于验证对象，并建议尽可能用实际接口或高保真环境验证，而不是只验证内部组件；
- NASA 对 external interface requirements 明确列出 source/destination、data format、transfer characteristics 等；
- OpenAI instruction hierarchy 继续支持高层治理合同不应被低层 task prompt 覆盖；
- GitHub 官方文档继续支持竞争修改/merge conflict 必须显式解决，不能用 force 覆盖。

这些只作为方向性支持；本轮具体规则由 AI Research Stack 的真实事故决定。

## 15. 当前状态

v0.7 对 v0.6 的冻结语义有实质修改，因此旧 `5dc95e155d4890d5bd311ef7c80baab830191949` 不再是待执行 package。

本轮将形成新的同版 Proposal / Execution Plan / Goal / Kickoff / Critic Prompt。

当前：
- 不实施 1.8；
- 不创建 execution branch/worktree；
- 不运行 A/B/C；
- 不修改 Clear Writing；
- 不修改 main；
- 不启动付费验证。

下一步唯一入口：独立 Critic 对 v0.7 完整 execution-ready package 做最终审查。
