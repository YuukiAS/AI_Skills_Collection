# workflow-core 0.5 正常入口与执行路线可靠性提案 v0.3

日期：2026-10-01  
角色：Planner  
目标仓库：`YuukiAS/AI_Skills_Collection`  
目标插件：`workflow-core`（Verified Workflow）  
设计主题 / task key：`workflow-core--normal-entry-reliability`  
source branch/ref：`main`  
本轮读取基线：`af4b13e74182fe4b2dd4d883976ffef8ccc2c31f`  
上一版：`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_2_2026-09-30.md`  
上一版 commit：`8575e86fce56d0c44c484477f578e90b65750c5c`  
上一轮 Critic：`REVISE`，`WC05-D1`–`WC05-D6` 已关闭，仅剩 `WC05-D7`；review repo path/commit = `NONE`  
当前插件版本：`0.4`  
审查阶段：`DESIGN_REVISION_R3`  
execution branch/worktree：`NONE / NOT AUTHORIZED`

## 1. 本轮结论

继续推进 `workflow-core 0.5` 候选，但把范围从 v0.1 收窄到三个真正同根的 production change：

1. **精确且克制的 normal-entry discovery / trigger**：复杂、跨阶段、需要流程判断的任务更可靠地隐式触发 workflow-core；复杂但完全由一个 specialist 包住的任务仍由 specialist 单独处理。
2. **specialist-first targeted capability discovery**：遇到工具、环境、资源或可选模式失败时，先读取当前适用 specialist 和项目已声明入口，再判断能力是否真的不存在。
3. **fail-closed fallback equivalence**：自动替代路线必须同时证明六项不变量全部保持；任一未知或变化都不得自动 fallback。

本轮**不再**包含 authorization lifecycle、task-local instruction lifetime、acceptance-artifact packaging、Bridge runtime 或机器环境架构。

设计阶段继续保持：

```text
workflow-core = 0.4 / NO_BUMP
Repository bump decision = NONE
execution branch/worktree = NONE
paid API = NOT AUTHORIZED
production implementation = NOT STARTED
```

只有未来同一个 final candidate 直接通过原 failure replay、真实 normal-entry consumption、相邻负例、真正 capability-absent fail-closed、unrelated/broad regression 和 release closure 后，才允许 `workflow-core 0.4 -> 0.5`；repository 仅走 PATCH。

## 2. 对上一轮 Critic findings 的处理

### WC05-D1 — ACCEPT

v0.1 的 G1 只有简单负例，无法证明扩大隐式触发后不会让 workflow-core 抢占 specialist。

v0.2 增加两层 hard negative：

- **简单负例**：单命令、单次编译、普通解释等仍不得触发；
- **复杂但 specialist-contained hard negative**：任务虽然有多个步骤、真实 render/QA 或专业判断，但其输入、步骤、失败处理和验收全部由一个现有 specialist 的合同覆盖，不涉及跨 specialist、跨阶段集成、release/handoff、流程恢复或 workflow-level acceptance。此类任务必须只消费 specialist，不得因为“步骤多”就顺带加载 workflow-core。

G1 必须用 final candidate 的**真实 invocation trace**同时证明正例和相邻负例，不能只看 metadata 字符串或 source 文件。

### WC05-D2 — ACCEPT

tracking #8 不整体 merge。

0.5 只借用一个 generic regression：

> 某个可选 foreground / `visible:true` 模式不支持，不能单独推出底层 capability 不存在。

以下 browser/subagent 专属语义继续属于 #8，不在 0.5 声称修复：

- anonymous-page preflight；
- pre-auth / post-auth 边界；
- credential / one-time handoff；
- persona 隔离；
- parent/subagent finding 隔离；
- browser/session state isolation；
- authenticated recovery。

因此 #8 继续独立 tracking，0.5 只把“optional mode failure ≠ capability absent”作为通用 capability-discovery 回归样本。

### WC05-D3 — ACCEPT

tracking #7 不进入 0.5 production behavior。

Bridge Kit 0.8.1+ 已拥有 upfront authorization / current-user authorization 语义；workflow-core 本轮不新增：

- kickoff 生成行为；
- authorization lifecycle；
- authorization store；
- schema；
- state；
- Host Policy；
- provider/resource preflight 新机制。

0.5 只在 fallback equivalence 的第六项检查“**当前有效 authorization scope 是否已经覆盖替代路线**”。这是判断能否自动替代的必要条件，不是新建授权机制。若授权未知或替代路线改变 provider/resource/purpose/artifact/side effect，则自动 fallback 直接失败，交回现有 authority/Human Gate 机制。

### WC05-D4 — ACCEPT

tracking #9 从本批拆出。

task-local instruction lifetime 属于 instruction scope / precedence 的独立 failure semantics，不与 trigger、specialist capability discovery 或 fallback equivalence 混在 0.5。#9 保持独立 tracking，本轮 production source 不修改该能力。

### WC05-D5 — ACCEPT

v0.2 新增一个**不可拆分的 final-candidate normal-entry replay gate**：

```text
普通用户 prompt（不点名任何 skill）
-> workflow-core 实际隐式消费
-> 匹配 specialist 实际消费
-> targeted capability discovery 实际发生
-> 正确 primary/equivalent route
-> 未发生 non-equivalent fallback
```

这条链必须在**同一次 final-candidate run**中被直接观察到。不能把“某次 workflow-core 触发成功”和“另一次 specialist 触发成功”拼成 PASS。

同时增加真正 capability absent 的对照：在 canonical/specialist/project-declared 合法入口确实不存在时，同一 final candidate 必须 fail closed，报告精确缺口，不得发明 Node/Chromium/其他低质路线，也不得无目标扫描整台主机。

### WC05-D6 — ACCEPT

fallback equivalence 改为 fail-closed 的“六项全部满足”规则。只有以下六项都能被正面证明为 `UNCHANGED / COVERED`，自动 fallback 才合法：

1. frozen effect；
2. professional quality；
3. acceptance evidence strength；
4. safety / privacy boundary；
5. artifact identity；
6. current authorization scope。

任一项为 `UNKNOWN` 或 `CHANGED`，都不能自动 fallback。

本轮没有 REBUT。

### WC05-D7 — ACCEPT

V0.2 对 #5/#6/#11 的 product-level `historical resolved` 判断可以保留，但上一版把 Board/bootstrap coverage disposition 与 canonical TODO `status:` 混在了一起，且没有显式应用当前 `ADAPTING` / required-consumer policy。

V0.3 做最小修正：

- `HISTORICAL_RESOLVED` 只作为 `AI_SKILLS_MAINTENANCE_BOARD.md` §8 的 bootstrap / coverage disposition；它**不是** canonical TODO 合法 `status:`。
- canonical source `status:` 只能从现有 vocabulary 中选择：`NEW`、`PROJECT_LOCAL`、`CANDIDATE_GENERIC`、`PROMOTE_NOW`、`BLOCKED_NEEDS_EVIDENCE`、`REJECTED`、`SUPERSEDED`。closure action 必须按当时真实语义选择或保留合法状态，不新增 `RESOLVED` / `HISTORICAL_RESOLVED` / 其他 schema。
- #5、#6、#11 都属于 **machine-consumed workflow / shared maintenance mechanism**：  
  - #5 涉及 Bridge-owned plugin replay / Host Policy 与 AI_Skills Executor 的正式消费路径；  
  - #6 是跨真实 maintenance batch、watcher/Reviewed Handoff 执行的共享维护机制；  
  - #11 是 Bridge Reviewed Handoff bootstrap/rematerialization 与 workflow-core normal-entry consumer 的共享执行机制。
- 因此三者即使 product-level evidence 已说明“旧问题在中央实现层已被覆盖”，Project closure 仍不得直接 `TODO/DOING -> DONE`。应在确认 central implementation complete 后进入 `ADAPTING`，冻结 required consumer identities，并逐个完成 PASS/N/A + durable evidence，最后写 Resolution commit、关闭 Issue，再由 issue-closed workflow 进入 `DONE`。
- `N/A` 只能用于有 durable frozen reason 的 consumer，不能为了快速关闭机械填写。
- 当前没有 Project mutation surface / Clear Writing，本轮只修 Proposal 中的 pending mutation；不实际修改 Issue/Project/canonical TODO status，不猜 Resolution commit，也不要求用户手工维护。


## 3. 真实问题与根因

STAT5060 Tutorial 1 已连续出现两个同类真实 regression：

- workflow-core 已加载，但 Codex 只检查默认 shell 的 Python/R 状态，就把当前 PATH / 当前环境缺命令解释成“能力不存在”，准备换 Node/标准库；
- 中文数学 PDF 中，裸 XeLaTeX 缺 `ctexart.cls` 后，Codex先自行找 conda/TeX、准备 HTML/Chromium；用户再次纠正后才读取 `render-chinese-math-pdf`，而该 specialist 已经明确规定 `render_resources/chinese_math_pdf`、probe 和禁止自动 Chromium fallback。

当前 workflow-core source 已经有：

- complex/risky trigger boundary；
- specialist routing contract；
- source-of-truth discovery；
- W4 repeat-failure circuit breaker；
- “fallback 只有 frozen Goal 明确认可等价才证明 primary capability”；
- escalation 必须来自 specialist / project contract / user-approved plan。

因此本轮不是再堆一组同义禁令，而是修**normal-entry consumption path**：

```text
trigger 没有把所有该进来的复杂任务稳定带进 workflow-core
+ workflow-core 已触发时仍可能晚于临时 workaround 才消费 specialist
+ escalation 对“能力不存在”和“替代等价”的判定缺少可执行、fail-closed 的边界
```

## 4. 外部核查与采用决定

本轮重新核对 OpenAI 当前官方资料：

1. Skills discovery：模型在 discovery 阶段先看到 skill 的 name/description，匹配后才读取完整 `SKILL.md`。因此 trigger 可靠性首先是 metadata + eval 问题，而不是把所有详细规则塞进 description。  
   https://developers.openai.com/plugins/concepts/skills
2. Build skills：description 决定何时考虑 skill；详细步骤、安全与输出规则放正文；skill 应围绕可识别用户目标，并明确 stop/ask/supporting-file 边界。  
   https://developers.openai.com/plugins/build/skills
3. Metadata guidance：名称/描述需要同时提高 relevant recall 和降低 accidental activation，应该用 direct / indirect / negative prompt set 迭代。  
   https://developers.openai.com/plugins/guides/optimize-metadata
4. Skill eval：应同时覆盖 direct、implicit、contextual、negative-control，而不是只测显式点名。  
   https://developers.openai.com/blog/eval-skills
5. 2026-09-11 Codex 指导继续强调减少 instruction/context 膨胀，支持根 skill 保持轻量、详细规则通过 supporting files 渐进消费。  
   https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra

采用决定：

- **采用**：短而精确的 trigger metadata、真实 implicit/negative invocation eval、progressive disclosure。
- **不采用**：把 workflow-core 做成 almost-always-on；把环境扫描、browser 行为或授权系统塞进根 skill；新增第二个 environment/fallback 顶级 skill。

## 5. 产品目标与明确边界

0.5 的用户价值不是“多写一些防错文字”，而是普通复杂任务不再因为一次局部探测失败就自行换成低质路线。

成功后的正常行为应是：

```text
复杂任务进入 workflow-core
-> workflow-core 识别专业 owner
-> specialist 被实际消费
-> 只做与当前合同相关的 targeted capability discovery
-> primary route 可用：继续
-> primary route 不可用但六项等价全部成立：自动走已授权等价 route
-> 六项任一未知/变化：不自动 fallback
-> 真正 capability absent：精确 fail closed
```

本轮不负责：

- Longleaf `/users`、module、conda、TeX 的机器级架构；
- STAT5060 source 或课程内容；
- `render-chinese-math-pdf` specialist 重写；
- Bridge Kit runtime / Host Policy；
- 新 workflow / state machine / daemon / watcher；
- kickoff/authorization lifecycle；
- task-local instruction lifetime；
- acceptance artifact packaging；
- browser auth/session/persona orchestration。

## 6. Production change 1：精确且克制的 normal-entry discovery / trigger

### 6.1 正例边界

workflow-core 的 description / trigger metadata 应继续保持短，不把完整流程复制进去。它应更明确覆盖：

- 多阶段实现/返修 + 验证 + 最终交付；
- 需要跨 specialist 协作或跨 artifact/runtime 层整合；
- 需要在 primary route、能力发现、等价恢复、真实 blocker 之间做流程判断；
- 有显式 acceptance / release / recovery / integration boundary；
- 单个 specialist 无法独立拥有完整成功定义的复杂任务。

### 6.2 hard negative 边界

以下即使“步骤不少”，仍不应因为复杂度表面特征自动触发 workflow-core：

**Specialist-contained hard negative**

> “把这份已经定稿的中文数学 Markdown 按仓库已有正式渲染链生成 PDF，并按该渲染能力自己的 checklist 检查中文、公式、字体和页面可读性；不改变内容语义，不做 release/handoff/integration。”

预期：实际消费对应 PDF/render specialist；**不消费 workflow-core**。理由是任务的 route、probe、失败处理和验收均由一个 specialist 完整拥有。

另保留简单负例，例如单命令帮助、单次编译、普通解释、纯措辞润色。

### 6.3 不能靠什么证明

以下都不能单独证明 trigger 修复：

- `allow_implicit_invocation: true`；
- description 中出现了关键词；
- trigger_queries JSON 静态存在；
- source/generated parity；
- 用户显式点名 workflow-core。

最终 release 必须观察未点名 skill 的真实 invocation trace。

## 7. Production change 2：specialist-first targeted capability discovery

### 7.1 原则

当失败落在已有 specialist 的职责范围内时，workflow-core 在改变执行路线前必须先让该 specialist 的正式合同进入当前决策。

workflow-core 负责：

- 判断需要哪个 owner；
- 要求读取其 canonical probe/resource/runner contract；
- 限制 discovery 只围绕当前缺失事实；
- 决定继续、等价恢复或 fail closed。

workflow-core 不负责：

- 自己决定 TeX/CJK 资源；
- 自己决定统计模型替代；
- 自己决定 browser auth/session；
- 自己维护 host module/conda inventory。

### 7.2 targeted discovery 顺序

顺序不是机械扫描清单，而是 authority 优先级：

1. 当前 user/frozen task/repo 已明确指定的 canonical route；
2. 当前已匹配 specialist 明确指定的 probe、resource、wrapper、runner 或 runtime；
3. 项目明确声明的环境入口，例如 module、venv/conda、project runner、container、site profile；
4. 当前 shell PATH / 默认 command 作为**局部状态证据**。

如果第 1–3 层已经给出确定入口，不得先全盘搜 home、`/overflow`、其他用户目录或整个 filesystem。

如果缺的是一个具体事实，只定位那个事实；不要把“source-of-truth discovery”解释为主机 inventory。

### 7.3 局部失败的证据强度

以下只能支持局部结论：

- `command not found`；
- 默认 interpreter 缺一个 package；
- 某个可选 CLI flag 不支持；
- foreground/visible mode 不存在；
- 一个 probe 路径失败。

它们不能单独支持“整个 capability 不存在”。

### 7.4 #8 的复用边界

0.5 只回放：

> optional foreground/visible mode unavailable，但普通 canonical mode 仍可工作的情况下，不得宣称 capability absent。

不消费、不修改 #8 的 auth/session/persona/subagent contract，也不以 0.5 PASS 关闭 #8。

## 8. Production change 3：fail-closed fallback equivalence

### 8.1 六项全满足

任何 automatic fallback 前必须对下面六项逐项得到正面证据：

| 维度 | 必须证明什么 |
|---|---|
| Frozen effect | 替代路线完成的是同一冻结目标，不删任务、不缩成功标准、不换研究/产品语义 |
| Professional quality | 目标 specialist 认可相同专业质量/方法边界；不是较弱近似或“能跑就行” |
| Acceptance evidence strength | 最终仍能通过同一等级的真实 gate；不得从真实 render/runtime 降成 proxy/helper/截图/静态检查 |
| Safety / privacy | 数据、provider、recipient、网络、权限、隐私/安全边界没有扩大或改变 |
| Artifact identity | 最终用户消费对象、格式、source lineage、可编辑性/完整性等身份保持同一合同 |
| Current authorization scope | 当前有效用户授权已经覆盖该 route 的真实 side effect；不能从 repo 文本或历史授权推导新权限 |

判定规则：

```text
六项全部 = PROVEN_UNCHANGED / COVERED
-> automatic equivalent recovery MAY proceed

任一 = UNKNOWN
-> NOT equivalent for automation
-> 先补 targeted evidence；补不到则精确 blocker

任一 = CHANGED
-> non-equivalent
-> automatic fallback FORBIDDEN
-> 交回现有 Planner / Human Gate / authority route（仅在其确实需要时）
```

这是 fail-closed 的“全满足”规则，不做多数表决、不做风险平均。

### 8.2 与已有 W2 的关系

已有 W2/least-privilege equivalent recovery 继续有效：

- 如果 lower-privilege route **六项全部保持**，自动采用是正确行为；
- 如果 route 只是更容易执行，但降低质量、证据或改变 provider/artifact，就不是 equivalent recovery；
- 本轮不新增 authorization 生命周期，只消费当前有效 authority truth。

### 8.3 本次 regression 应被怎样拦住

- XeLaTeX/正式 resource route 失败后切 Chromium：至少 professional quality / acceptance evidence / artifact identity 未正面证明不变，因此自动 fallback 失败。
- R/Python 正式计算/绘图路线未真正查完就切 Node：specialist-first discovery 尚未完成，根本还没有进入合法 fallback 判定。
- optional browser foreground flag 不存在但 ordinary mode 可用：这是 capability discovery，不是 fallback；应继续 canonical mode，而不是报告 capability absent。

## 9. TODO / tracking disposition

本轮 production scope 不变；这里只修正 maintenance vocabulary 与 closure semantics。

| 条目 | v0.3 disposition | 0.5 production change |
|---|---|---|
| `Loaded workflow-core still misclassified environment capability...` | **PROMOTE_NOW candidate / 本轮主问题**；正式 source triage、Issue backlink 与 Project lifecycle 等有合法 Board surface 时同步 | 是 |
| #5 `Keep AI_Skills workflow rules separate from Bridge Kit runtime bugs` | **product-level / bootstrap coverage disposition = HISTORICAL_RESOLVED**；但该词不是 canonical `status:`。该条属于 machine-consumed/shared mechanism，Project closure 必须经过 ADAPTING consumer closure | 否 |
| #6 `Real-task-driven Reviewed Handoff batches` | **product-level / bootstrap coverage disposition = HISTORICAL_RESOLVED**；不是 canonical `status:`。该条属于 shared maintenance mechanism，Project closure 必须经过 ADAPTING consumer closure | 否 |
| #7 bounded kickoff / approval-sensitive handoff | **不进入本轮**；Bridge-owned current-authority/upfront-authorization semantics 覆盖原始 evidence。0.5 不新增 kickoff/authorization behavior；现有 tracking lifecycle 本轮不改 | 否 |
| #8 browser capability | **保持独立 tracking**；只借 `unsupported foreground/visible flag ≠ capability absent` 这一 generic regression。其余 browser/auth/session/persona 语义不变 | 只借一个回归，不合并 |
| #9 task-local prohibition lifetime | **保持独立 tracking**；不同 failure semantics，本轮不改 | 否 |
| #10 acceptance artifact packaging | **保持独立 tracking**；不同能力面，本轮不改 | 否 |
| #11 reviewed worktree authorization/runtime | **workflow-core consumer 层 product-level / bootstrap coverage disposition = HISTORICAL_RESOLVED**；不是 canonical `status:`。该条属于 machine-consumed workflow，Project closure 必须经过 ADAPTING consumer closure | 否 |

### 9.1 canonical TODO status 与 Board disposition 分离

`HISTORICAL_RESOLVED` 只来自 Maintenance Board 的 bootstrap coverage vocabulary：

```text
TRACKED
MERGED_INTO_TRACKING_ISSUE
NON_CENTRAL_PROJECT_LOCAL
REJECTED_OR_SUPERSEDED
HISTORICAL_RESOLVED
```

它不能写进 `docs/plugin-todos/workflow-core.md` 的 `status:`。

canonical TODO 的合法 triage vocabulary 仍只有：

```text
NEW
PROJECT_LOCAL
CANDIDATE_GENERIC
PROMOTE_NOW
BLOCKED_NEEDS_EVIDENCE
REJECTED
SUPERSEDED
```

closure action 必须比较当前 active rule、历史 candidate 和真实 evidence 后，选择**现有合法 status 或保持现有合法 status**。若 active rule 已完全替代旧候选，`SUPERSEDED` 可能是合适结果；若证据不足，则不能为了 closure 强行改成 `SUPERSEDED`。本 Proposal 不预先替 closure action 作这个语义判断。

特别地，#11 当前 source 的 `status: NEW / POST_056_REFINEMENT` 不属于现行 vocabulary；本轮不借 design-only Proposal 顺手改 canonical TODO。下一次具有合法 maintenance mutation surface 的 closure/triage action 必须先按当前真实语义规范化为一个现有合法 status，再继续 Board closure。

### 9.2 #5 / #6 / #11 的 consumer classification

三项均判为 **YES：machine-consumed workflow / shared maintenance mechanism**。

- **#5 = YES**：其解决路径不是普通文档，而是 Bridge plugin replay / Host Policy 与 AI_Skills Executor 的正式机器消费路径。它直接影响 production replay 在真实 Codex identity 中怎样运行。
- **#6 = YES**：其目标是约束真实 maintenance batch / Reviewed Handoff / watcher 怎样启动、停止和避免 synthetic successor chain，属于多个执行 consumer 共同消费的 shared maintenance mechanism。
- **#11 = YES**：其目标是 Bridge Reviewed Handoff bootstrap/rematerialization 与 workflow-core 0.4 的正常入口消费，属于跨机器执行的 machine-consumed workflow。

因此 product-level historical resolved 只说明“中央产品/规则层已有覆盖”，**不等于 Project DONE**。

对三项，Project closure 的 canonical 路径必须是：

```text
central implementation complete
-> ADAPTING
-> freeze required consumer identities / locators
-> each required consumer PASS or justified N/A
-> durable evidence complete
-> Resolution commit
-> tracking Issue completed close
-> issue-closed workflow
-> DONE
```

当前默认 required logical consumers 由 `AI_SKILLS_MAINTENANCE_BOARD.md` 决定：

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`
4. `Workstation`
5. `Legion`

进入 ADAPTING 时必须冻结每个 consumer 的 exact current identity / locator；需要访问机器解析 identity 时先获得对应 bounded authority，不得猜。

每个 PASS 至少证明 installed/loaded identity、relevant normal-entry consumption、需要时的 fresh-session/restart boundary、risk-matched should-not-change/failure safety，以及 durable evidence locator。

`N/A` 必须有 durable frozen reason；不能因为某台机器暂时不方便验证、当前离线或为了缩短 closure 就机械填 N/A。

## 10. 预计修改层

若设计最终 PASS，0.5 implementation 预计只涉及：

- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`：保持简短，只补 trigger/specialist-first/fallback decision 的核心不变量；
- `references/escalation-rules.md`：放 targeted capability discovery 与六项 equivalence 的详细规则；
- `agents/openai.yaml`：精确调整 positive/negative trigger；
- `evals/trigger_queries.json`：加入 implicit/contextual/hard-negative/adjacent-negative；
- workflow-core 专属真实 invocation/regression tests；
- 必要的 generated Marketplace payload；
- release closure 时才更新 workflow-core changelog / Marketplace version / repository release metadata。

除非 Critic 明确指出现有结构无法承载，否则不修改 `verification-matrix.md` / `task-template.md`，避免无关扩散。

明确不改：

- Longleaf `/users`、module、conda、TeX；
- STAT5060 source；
- render specialist source；
- Bridge Kit；
- #7/#8/#9/#10 专属 production logic；
- 新 plugin / 新顶级 skill；
- 新 workflow/state/schema/watcher/daemon；
- paid review。

## 11. Capability Gate Matrix v0.2

### G1 — Trigger precision：正例 + 相邻 hard negative

**Capability / claim**  
复杂且需要 workflow-level coordination 的普通 prompt 能隐式触发 workflow-core；复杂但 specialist-contained 的 prompt 只触发 specialist。

**Why distinct**  
证明“何时进入 workflow-core”，不证明进入后怎么做 capability discovery。

**Normal entry**  
最终候选真实安装后的普通 Codex prompt，不点名 workflow-core。

**Evidence**  
同一 final candidate 至少覆盖：

- implicit positive：多阶段、需要 specialist + workflow-level acceptance/recovery；
- contextual/noisy positive：同一目标夹杂项目上下文但仍应触发；
- complex specialist-contained hard negative：上文中文数学 PDF 例或等价 fixture，应只消费 specialist；
- simple negative：单命令/普通解释。

必须记录真实 skill/plugin consumption trace。正负例都不能靠 source 字符串、`allow_implicit_invocation` 或静态 metadata 判定。

**Failure**  
positive 未加载；hard negative 加载 workflow-core；workflow-core 抢占 specialist。

**Regression boundary**  
现有简单任务保持轻量；specialist-contained 正常入口不变重。

**Final-candidate requirement**  
YES。

### G2 — Specialist-first targeted capability discovery

**Capability / claim**  
局部工具/环境/可选模式失败时，在宣布 capability absent 前先消费适用 specialist，并只检查当前合同声明的 canonical/resource/project environment route。

**Why distinct**  
证明“能力是否真的不存在”；不证明 route substitution 的六项等价。

**Normal entry**  
final candidate + 实际 specialist 的安全 regression replay。

**Evidence**  
覆盖至少三种 failure shape：

1. 默认 PATH 没有工具，但项目声明的 runtime/runner 可用；
2. 默认 renderer 缺 package，但 specialist 提供 canonical resource/probe；
3. optional mode/flag 不支持，但 canonical base mode 可用（只复用 #8 的 generic fact）。

每种都必须观察 specialist 实际消费和 targeted probe/route，禁止大范围主机扫描。

另有一个真正 absent 的开发期对照可用于定位，但 final fail-closed 由 G4 直接证明。

**Failure**  
局部失败直接被解释成 capability absent；读取 specialist 前开始替代实现；为找能力全盘扫描不相关主机路径。

**Regression boundary**  
真正 unavailable 时不能假装成功；specialist 仍拥有专业路线。

**Final-candidate requirement**  
YES。

### G3 — Fail-closed fallback equivalence

**Capability / claim**  
automatic fallback 只有在六项不变量全部正面证明保持时才允许。

**Why distinct**  
G2 决定“primary capability 是否真的不存在”；G3 决定“确认 primary route 不可用后，替代 route 是否有资格自动继续”。

**Normal entry**  
final candidate 的 route-choice regression。

**Evidence**  

- 一例六项全部保持的 lower-privilege / equivalent recovery，应自动继续；
- 一例专业质量或 evidence strength 改变的替代，应拒绝；
- 一例 authorization scope 为 UNKNOWN/CHANGED，应拒绝自动替代并交回现有 authority route；
- specialist 明确禁止某 fallback 时，必须拒绝。

每例必须保存六项判定的实际依据；不得只输出“equivalent=true”。

**Failure**  
任一 UNKNOWN/CHANGED 仍自动 fallback；仅因“能产出文件/能跑”就判等价。

**Regression boundary**  
已有 W2 least-privilege equivalent recovery 不被误杀。

**Final-candidate requirement**  
YES。

### G4 — 不可拆分的 final-candidate normal-entry replay + absent 对照

**Capability / claim**  
证明 0.5 三项 production change 在真实 normal entry 中组成一条完整因果链，而不是各自孤立 PASS。

**Why distinct**  
这是 release-critical integration gate；G1–G3 可帮助定位问题，但不能替代端到端链。

**Normal entry**  
普通用户 prompt，不点名 workflow-core 或 specialist。

**Positive replay — 必须同一次 run 观察**

```text
prompt
-> workflow-core implicit consumption
-> correct specialist consumption
-> targeted capability discovery
-> canonical/equivalent route selected
-> no non-equivalent fallback
-> task reaches the bounded expected outcome
```

不允许把两个 run、两个 candidate、source inspection 与 runtime trace 拼接成这条链。

**True capability-absent contrast**  
同一 final candidate 在 canonical task route、matched specialist route 与 project-declared environment route 均真实不存在的受控 fixture 中：

- 不扫描无关主机；
- 不自行发明新技术栈；
- 不降级 acceptance；
- 输出 precise missing capability / `blocked_target_not_met` 或 specialist 定义的等价 fail-closed 状态；
- 若没有需要用户决定的互斥产品/授权选择，不制造 Human Gate。

**Failure**  
positive chain 任一环只由另一 run 证明；absent case 静默 fallback 或假装 complete。

**Regression boundary**  
正常成功路线和真正失败路线都必须诚实。

**Final-candidate requirement**  
YES，且不可由旧 candidate evidence 替代。

### G5 — Broad should-not-change / integration regression

**Capability / claim**  
routing metadata 和 escalation 行为改变后，不破坏 workflow-core 0.3/0.4 的已有正常能力及相邻 specialist-only 入口。

**Why distinct**  
证明 blast radius；不是 G4 的单一完整链。

**Normal entry**  
同一 final candidate 的 candidate-plugin replay / production-compatible runtime。

**Evidence**  

- 056 W1–W5 workflow-core scenarios；
- workflow-core 0.4 Reviewed Handoff bootstrap/resume scenarios；
- source/generated/Marketplace/version parity；
- specialist-contained hard negative 的 should-not-change；
- 至少一个与中文 PDF 不同的相邻 specialist family 负例或普通任务，证明修复不是对单一样本 hardcode；
- 风险匹配的 repository test/CI。

**Failure**  
旧能力退化、routing 变得过宽、不同 candidate 拼证据、只靠单元测试宣称 production entry PASS。

**Regression boundary**  
0.3 delivery discipline、0.4 Bridge routing、普通 specialist-only 路线均保持。

**Final-candidate requirement**  
YES。

### Gate 执行顺序

开发期：

```text
cheap deterministic regression
-> G1/G2/G3 已知回归迭代
-> candidate freeze
```

release candidate：

```text
same final candidate
-> G1
-> G2
-> G3
-> G4 inseparable normal-entry + absent contrast
-> G5 broad regression/integration
-> release closure
```

若 G4 失败，不得用 G1–G3 分别 PASS 来拼 release claim。

## 12. Product / Reality / Alternatives / Red Team / Execution Contract

### Product

用户真正要的是：复杂任务中少陪 Codex 调环境、阻止擅自低质量 fallback，同时不要让所有专业任务都背上 workflow-core 的额外流程。

### Reality

当前 source 已有 process ownership、specialist routing、W1–W5 和 Bridge routing；真实 failure 说明的是消费和判定边界仍不足。现有结构能承载修复，不需要新 skill/state/runtime。

### Alternatives

- 项目局部规则：拒绝，不能解决跨项目复发；
- workflow-core always-on：拒绝，会误触发；
- 新 environment skill：拒绝，职责重复；
- 只加一句“不要 fallback”：拒绝，已有类似原则仍复发；
- 本 v0.2 三项 bounded refinement：采用。

### Red Team

实现/评审必须主动防：

- 为了提高 recall 让 description 过宽；
- positive trigger PASS 但 hard negative 全被误触发；
- source 写了 specialist-first，真实 run 仍先 workaround；
- 把 PATH/flag failure 当 capability absence；
- 六项 equivalence 只生成一个布尔结果而没有证据；
- 用 Node/Chromium/其他“能产出”路线钻 fallback；
- 为过 gate 对 STAT5060/Longleaf 路径 hardcode；
- G1–G3 不同 run 拼成 G4；
- absent case 通过扫 home/overflow 找到偶然工具而“PASS”；
- 借 #8 regression 声称 browser auth/session 已修；
- 顺手改 Bridge 或机器环境。

### Execution Contract

只有设计 Critic PASS 后，Planner 才准备同版本 execution package（Proposal/Plan + Canonical Goal + Kickoff Draft）并再次送 execution-ready Critic。当前 V0.2 不授权 Executor。

## 13. 版本与 maturity

当前：

```text
Repository bump decision: NONE
Reason: DESIGN_REVISION only；production behavior 未修改。
Affected plugins:
- workflow-core: NO_BUMP
  Reason: 当前保持 0.4，尚未实现/验证/release。
```

未来若同一 final candidate 完整通过：

```text
Repository bump decision: PATCH
Affected plugins:
- workflow-core: 0.4 -> 0.5
```

届时 repository 版本从**当时实际 release version**推进一个 PATCH，不预占当前数字。

本轮不提升 `workflow-core` maturity；真实 normal-entry regression 尚在修复阶段。

## 14. Maintenance Board pending mutation

当前 surface 没有 GitHub Project mutation 能力；当前可用 Skills 中也没有 Clear Writing / `writing-style`，因此不能合法创建或实质改写 reader-facing tracking Issue copy。本轮不伪称 Board 已同步，也不要求用户手工操作。

下一次同时具备 Project mutation + Clear Writing 的 maintenance action，必须先重新读取当时最新 Board policy、canonical source 和 tracking Issues，确认以下 pending mutation 仍 current 后再执行。

### A. 本轮主问题

source heading：

`Loaded workflow-core still misclassified environment capability and attempted an unapproved fallback`

pending：

1. 用 Clear Writing 生成自然、忠实、不改变 evidence meaning 的 tracking Issue copy；
2. 创建或绑定一个 `maintenance-track` Issue；
3. 同一 action 在 source entry 回写 `tracking: #N`；
4. canonical source `status:` 只能按当时真实 triage 语义使用现有合法 vocabulary；不得写 `HISTORICAL_RESOLVED`；
5. Project Area=`workflow-core`；
6. Project Status=`DOING`；
7. 当前执行锚点=`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_3_2026-10-01.md`；
8. 下一步=独立 Critic 对 V0.3 做 design re-review。

### B. #5 / #6 / #11：product-level historical resolved，但必须走 ADAPTING closure

三项当前 tracking Issue 分别为 #5、#6、#11，且当前仍为 open。V0.3 只冻结：

```text
bootstrap / coverage disposition = HISTORICAL_RESOLVED
machine-consumed/shared mechanism = YES
Project DONE = NOT YET ESTABLISHED
```

下一次合法 closure action 对每项分别执行：

1. 重新核实 product-level resolving evidence 与 central implementation/release identity；若 central implementation complete 尚未成立，保持 `DOING`，不能进入 ADAPTING。
2. 对 canonical TODO `status:` 做独立语义判断：
   - 只能使用现有合法 vocabulary；
   - `HISTORICAL_RESOLVED` 不得写入 `status:`；
   - 不得为了闭卡机械改为 `SUPERSEDED`；
   - #11 当前非法复合 status 必须在有合法 triage authority 时规范化为一个现有合法值。
3. central implementation complete 后，将 Project Status 设为 `ADAPTING`，而不是 DONE。
4. 在 tracking Issue 中冻结五个 required consumer 的 exact current identity / locator：
   - `Longleaf_Codex`
   - `Longleaf_Backup_Codex`
   - `CUHK_Workstation_WSL_Codex`
   - `Workstation`
   - `Legion`
5. 每个 consumer 逐项记录 PASS / N/A：
   - PASS 必须包含 actual target identity、approved adaptation/update action、installed/loaded identity、relevant normal-entry consumption、需要时的 fresh-session/restart boundary、risk-matched should-not-change/failure safety、durable evidence locator；
   - N/A 必须有 durable frozen reason，不能因为临时不可达/离线/方便性而使用。
6. 全部 required consumers PASS/N/A 且 durable evidence complete 后，写入真实 `Resolution commit`。
7. 用 Clear Writing 更新 reader-facing Issue copy，准确说明 consumer closure。
8. 完整 closure 成立后关闭 tracking Issue；仅此时由 issue-closed workflow 进入 `DONE`。

不得从“product-level historical resolved”直接跳 DONE，也不得猜 Resolution commit。

### C. #7 / #8 / #9 / #10

- #7：不进入 0.5；本轮不改 Project lifecycle。
- #8：保持独立 Issue #8；不得 merge。0.5 只引用 generic regression evidence。
- #9：保持独立 Issue #9；不推进。
- #10：保持独立 Issue #10；不推进。

### D. 当前 no-tool truth

本轮没有执行任何 Project mutation、Issue closure、consumer adaptation、machine verification、Resolution commit 写入或 source status 规范化。

因此当前只能记录上述 pending mutation；不得声称 #5/#6/#11 已 DONE，也不得要求用户手工拖卡或补 locator。

## 15. 本 Proposal 不批准什么

- 不批准 production implementation；
- 不批准 execution branch/worktree；
- 不批准 version bump；
- 不批准 release/publish；
- 不批准 paid API；
- 不批准 Longleaf/STAT5060/render specialist/Bridge runtime 修改；
- 不批准关闭任何 tracking Issue；
- 不批准把 #8/#9/#10 视为由 0.5 解决。

下一步仅是独立 Critic 对 V0.2 复核 WC05-D1–D6 是否全部关闭，并决定 `PASS / REVISE`。
