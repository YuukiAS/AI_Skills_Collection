# workflow-core 0.5 正常入口、最低权限与恢复可靠性提案 v0.5

日期：2026-10-01  
角色：AI Research Stack Planner  
目标仓库：`YuukiAS/AI_Skills_Collection`  
目标插件：`workflow-core / Verified Workflow`  
design topic：`workflow-core--normal-entry-reliability`  
source branch/ref：`main`  
本轮 source baseline：`02916665144902f6a6aa29964e8dcd55b9010f7c`  
review stage：`DESIGN_REVISION_R5`  
当前 plugin version：`0.4`  
repository release：`5.4.0`  
implementation：`NOT STARTED`

上一已通过设计：

`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md`

上一 execution packages：

- `WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_1_2026-10-01.md`
- `WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_1_2026-10-01.md`
- `WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_1_2026-10-01.md`
- `WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_2_2026-10-01.md`
- `WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_2_2026-10-01.md`
- `WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_2_2026-10-01.md`

上述 execution packages 自本 Proposal 起全部 **SUPERSEDED / NOT EXECUTABLE**。不得继续修补、不得作为 Kickoff authority、不得创建其中的 Reviewed tasks。

## 1. 核心结论

继续做 `workflow-core 0.5`，不是开 0.6。

V0.4 的方向没有被推翻；新事实说明它还缺一层与 capability discovery 同根的“执行路线选择”约束。0.5 现在冻结为：

1. **Trigger precision 保持不变**：复杂 workflow-level 协调任务可靠触发；specialist-contained 任务不误触发。
2. **Specialist-first targeted capability discovery 扩展为 specialist-first + least-privilege normal-entry selection**：先用当前 workspace / specialist / project 已声明的最低权限正常入口，不主动把普通本地工作升级成更高权限执行。
3. **Six-dimension fallback equivalence 扩展为 approval-aware、privilege-non-increasing、fail-closed fallback/recovery**：六项语义等价仍全部必需；此外自动 recovery 不得扩大 privilege / authority surface。
4. **W4 增加 approval-rejection circuit breaker**：连续同类审批拒绝不再触发“换一个 escalated command继续试”，而是先重新判断 route、effect necessity 和 authority boundary。
5. **W3/W1 保留 effect-scoped truth**：成功的本地 build/render/QA/commit 不会因为后续 publication effect 失败而被反向判成失败；只把真实失败的 effect 保持 blocked。

第 4、5 项是现有 W4/W3/W1 的 hardening，不是新增 workflow、state、schema、authorization store 或 runtime。

## 2. 为什么上一 execution package 路线应废弃

V0.1/V0.2 把一个本质上属于 bounded plugin refinement 的任务升级成 Reviewed Handoff control problem，随后为一个本来可以在普通 task branch 内完成的改动引入：

- Reviewed task；
- `CURRENT`；
- `PLAN_FROZEN`；
- Planner / Reviewer state transaction；
- Stage A / Stage B；
- task-bound transport；
- 第二层 branch/worktree lifecycle。

这没有解决 workflow-core 本身的用户能力，只增加了 execution friction。

当前没有证据表明 0.5 实现需要 Reviewed Handoff 的不可替代能力：没有 paid call、不可逆实验、私有 artifact reviewer、外部 visual/text evidence、长时间无人值守 state machine、或必须由 Reviewed Reviewer 托管的两轮自动返修。

因此后续 execution 默认回到：

```text
one ordinary task branch
-> source-first implementation
-> deterministic tests + known regressions
-> stable 0.4 qualification candidate
-> original failure + unrelated regression PASS
-> exactly-once workflow-core 0.4 -> 0.5
-> repository next PATCH
-> regenerate
-> freeze one final candidate
-> final candidate directly runs G1-G6 + broad CI
-> independent final-candidate Critic
-> canonical release closure
```

普通 implementation bug、fixture repair、test repair 由 Codex 在冻结 Plan 内自行完成。只有 architecture / Gate semantics / scope / version policy / authority semantics 发生实质变化才回 Planner/Critic。

## 3. 本轮重新核实的现实边界

### 3.1 AI_Skills

当前 main baseline 为 `02916665144902f6a6aa29964e8dcd55b9010f7c`。  
`workflow-core` 当前正式版本仍是 `0.4`；repository release 仍是 `5.4.0`。

当前 workflow-core 已有：

- trigger boundary；
- specialist routing；
- W2 Human Decision Gate；
- W3 evidence fidelity；
- W4 repeat-failure circuit breaker；
- W5 should-not-change；
- fallback 不能凭“能继续”冒充 primary capability；
- escalation method 应来自 specialist / project contract / approved plan。

因此新修复必须优先改消费和 route-decision 语义，不堆一套平行框架。

### 3.2 Bridge Kit：只核实 owner boundary，不在本轮维护

当前正式 `release` ref：

`9dad0ba4bfa54e251f345091c5151ae991251ec9`

该 release 的：

- `pyproject.toml` version = `0.9.3`
- `ai_bridge_kit.__version__ = 0.9.3`

当前 Bridge `main` 已推进到 `7df05b98b09bec4da4382853c360ca70a8ca3a5f`。从 release ref 到当前 main 的比较显示新增的是 README、TODO/design 和 release/evidence 文件，没有 Bridge runtime source diff。因此“installed checkout HEAD = release ref，而 main 更靠后”**不能单独证明 runtime stale**。

Bridge 0.9.3 release 的 `ai_bridge_kit/host.py` 也直接确认：

- publisher preflight 在 `_reject_process_transport_env()` 中检测到 process env 的 `GIT_ASKPASS` 或 `SSH_ASKPASS` 会抛 `ASKPASS_REQUIRES_APPROVAL`；
- 这个检查发生在后续 `_sanitized_push_env()` 之前。

所以 ambient AskPass 导致 bounded publisher fail closed 是真实 Bridge-side行为，不是 workflow-core 应复制修复的 Git逻辑。

用户提供的 runtime evidence 还显示同一 conda 环境存在多份 editable metadata。该事实无法仅从 GitHub repo 独立验证，本 Proposal只把它记录为 **Bridge installation-hygiene / runtime-identity follow-up evidence**，不把它解释为“当前一定运行错误版本”。

Bridge 当前 main 已有独立的 0.10.0 execution-reliability design，覆盖 AskPass publisher compatibility 与 runtime identity diagnostics。该工作由另一个 Bridge Planner thread负责；本线程不创建 Bridge successor、不修改 Bridge source、不给 Bridge执行 prompt。

## 4. 外部核查

本轮只做与 workflow-core 设计直接相关的少量官方核查：

1. OpenAI《Running Codex safely at OpenAI》明确把目标写成：低风险动作应尽量顺畅，高风险动作应显式受控。  
   https://openai.com/index/running-codex-safely/
2. OpenAI Auto-review 说明主 agent天然有把 approval boundary 当成“完成任务的障碍”继续突破的压力，因此 boundary-crossing decision需要独立、明确的控制，而不是主 agent不断换命令撞审批。  
   https://alignment.openai.com/auto-review
3. OpenAI Skills 文档把 Skill定位为“什么时候调用工具、按什么顺序、怎样处理 incomplete results”的 workflow layer；详细停止/询问/支持文件规则应放 Skill正文，而不是无限扩 description。  
   https://developers.openai.com/plugins/concepts/skills  
   https://developers.openai.com/plugins/build/skills

采用决定：本次用 workflow-core 约束**route selection / failure classification / recovery semantics**，不改 sandbox、Host Policy或publisher实现。

## 5. 新事故归因

本轮新事故不是“Bridge没安装”，也不是“再加一条不要 fallback”即可解决。

真实链条暴露的是：

1. repo-local build/test/render/QA 明明能在 workspace-write 内完成，却主动选择更高权限 route；
2. approval rejection 后，没有先判断该 effect 是否必要、route是否选错、是否属于真正 authority boundary；
3. bounded/canonical route 出错后，存在转向更宽 raw route 的压力；
4. optional cleanup 可能被错误升级成 completion blocker；
5. publication失败容易把已经完成的 local成果一起判成失败；
6. 同类 approval rejection重复发生时，W4 目前没有明确要求“route reassessment before another approval-sensitive attempt”。

这与之前的 PATH/renderer fallback 是同一类根因：**局部失败没有先经过正确 owner + 正常入口 + 等价/权限边界判断，就被当成扩大路线的理由。**

## 6. Production mechanism A：Trigger precision 保持 V0.4

不改 V0.4 的 trigger architecture。

workflow-core 应触发：

- 多阶段实现/验证/交付；
- 跨 specialist / artifact / runtime协调；
- capability/route/recovery/authority 需要 workflow-level判断；
- acceptance/release/integration boundary。

hard negative继续保留：

- simple command / explanation；
- complex but specialist-contained task：一个 specialist已完整拥有 route、probe、failure handling、QA和success definition时，workflow-core不因“步骤多”而抢入。

本轮 approval/privilege规则不得成为让 workflow-core almost-always-on 的借口。

## 7. Production mechanism B：specialist-first + least-privilege normal-entry selection

V0.4 的 targeted discovery 顺序继续成立，但在执行具体 action 前增加一个最小通用原则：

> 在冻结目标允许的合法 route 中，优先选择能完成当前 effect 的最低权限 canonical/normal entry；不得因为“未来可能需要”就提前选择 `require_escalated`、更宽文件写权限、raw transport 或更强 provider permission。

判断顺序仍以 authority 为中心：

1. current user / frozen task / repo canonical route；
2. matched specialist 的正式 probe / resource / wrapper / runner；
3. project-declared environment/runtime；
4. current workspace 默认能力；
5. 只有当前 required effect 明确超出上述合法边界时，才进入 authority/approval path。

这个顺序不是权限扫描器，不建立 privilege registry，也不要求模型枚举所有sandbox能力。

### 7.1 effect necessity 在 escalation 前判断

遇到需要更高权限的动作前，先判断该 effect 对当前 frozen completion 是：

- **required**：缺失会使当前目标无法完成；
- **optional / cleanup / convenience**：不影响冻结目标；
- **unknown**：先从当前合同确定，不能默认升级为 required。

这是运行时判断，不新增 persistent enum/schema。

optional generated-cache cleanup、临时文件整理或非必要美化如果需要 escalation，默认跳过并记录，不拿它阻塞已经完成的主任务。

## 8. Production mechanism C：approval-aware、privilege-non-increasing recovery

V0.4 的六项 fallback equivalence继续全部保留：

1. frozen effect；
2. professional quality；
3. acceptance evidence strength；
4. safety/privacy；
5. artifact identity；
6. current authorization scope。

自动 recovery 现在还要满足一个额外**非 schema 条件**：

> recovery route 的 privilege/authority surface 不得比被阻塞的 canonical route更宽，除非 current user对新增边界给了新的明确授权。

因此：

- bounded publisher失败 -> raw `git push`：自动 fallback **禁止**；
- canonical wrapper失败 -> general shell/unsandboxed equivalent：自动 fallback **禁止**；
- current workspace normal entry可完成 -> 不应先走 `require_escalated`；
- lower-privilege且六项全部保持的 route：仍允许自动恢复。

这不把“privilege”变成第七个 ledger字段；它是六项 equivalence之外的 eligibility guard。

### 8.1 approval rejection 四类归因

approval / auto-review rejection 后，必须先分类再决定下一动作：

1. **optional/non-required effect**  
   跳过该 effect，保留已完成成果，不继续提权。
2. **错误选择了高权限 route**  
   回到仍满足冻结目标的最低权限 canonical route；这是 route correction，不是 fallback降级。
3. **genuine authority boundary**  
   只阻塞当前需要越界的 effect；按现有 approval/Human Gate 处理，不换更宽命令绕过。
4. **normal entry itself broken**  
   记录 canonical route failure；如果没有已授权、六项等价且 privilege不增加的 recovery，fail closed。实现 owner另行修 normal entry，workflow-core不接管其底层实现。

## 9. W4：approval-rejection circuit breaker

W4 追加一个直接消费真实事故的规则：

> 同一目标中连续出现同类 approval rejection，或同一 bounded effect 已被拒后又准备通过另一条同级/更高权限路线重试，必须先停止 approval-sensitive execution并做 route reassessment。

只有出现**新信息**才允许再次尝试 approval-sensitive action，例如：

- current user新增明确授权；
- 发现原 route其实不是 required；
- 找到 canonical lower-privilege且等价路线；
- normal-entry owner已修复并产生新 candidate；
- 原 rejection被证明是不同 failure class。

仅换命令包装、换 raw command、加 `require_escalated`、换 shell/python wrapper都不算新信息。

## 10. W3/W1：effect-scoped truth 与成果保留

workflow-core 必须区分不同 effect 的完成状态。

例如：

```text
build = PASS
render = PASS
QA = PASS
local commit = PASS
publication = BLOCKED
```

合法结论是：

- local artifacts/commit仍是成功证据；
- overall goal如果冻结要求publication，则 overall complete = NO；
- blocked effect = publication；
- 不重新跑已经通过且未受影响的 build/render/QA；
- 不把publication failure误写成“build失败”；
- 如果publication本来是optional，则它不能把目标改成blocked。

这是 W3 evidence fidelity + W1 completion truth 的强化，不新增状态机。

## 11. Bridge-owned follow-up：只记录，不实现

workflow-core 0.5明确不实现：

- Bridge runtime identity inspector；
- duplicate editable metadata cleanup；
- `SSH_ASKPASS/GIT_ASKPASS` publisher兼容；
- publisher credential/transport logic；
- raw Git wrapper；
- Host Policy规则。

Bridge follow-up应由 Bridge owner独立判断，至少覆盖：

- runtime identity输出 package version + imported source path + source Git HEAD + formal release identity + dirty/behind truth；
- duplicate editable metadata的installation hygiene；
- ambient `SSH_ASKPASS` 在 Remote SSH/Codex环境中的 publisher行为与operator recovery；
- raw push不得成为 bounded publisher failure的自动fallback。

当前 Bridge main已有独立 0.10.0 proposal处理这些方向；本线程不复制、不修改、不交接Bridge implementation。

## 12. Capability Gate Matrix v0.5

### G1 — Trigger precision

**保持 V0.4。**

证明：

- implicit/contextual workflow-level positive实际消费 workflow-core；
- complex specialist-contained hard negative不消费 workflow-core但消费正确specialist；
- simple negative不误触发。

release-critical evidence必须来自final candidate真实production-compatible consumption。

### G2 — Specialist-first + least-privilege normal entry

在原G2三类 capability-discovery regression基础上增加route-selection要求：

- default PATH/tool不可见时先消费specialist/project route；
- specialist已有resource/probe时先用正式route；
- optional mode不可用不等于capability absent；
- repo-local build/check/render/QA在workspace内可完成时，不主动要求escalation；
- optional cleanup若需要更高权限，不进入required path。

**失败条件**：

- specialist前先workaround；
- current workspace可完成却先走更高权限；
- optional cleanup触发不必要approval；
- 大范围host scan代替targeted discovery。

### G3 — Approval-aware, privilege-non-increasing fallback/recovery

证明：

- 六维全部保持 + privilege不增加的recovery可以继续；
-任一六维 UNKNOWN/CHANGED -> fail closed；
- broader privilege route -> 不自动继续；
- approval rejection四类归因正确；
- bounded/canonical route failure不自动切 raw/broader route；
- successful local evidence不会被后续外部effect failure抹掉；
- repeated same-class approval rejection触发W4 route reassessment。

G3可以使用安全deterministic fixtures验证各decision branch；它不单独证明完整normal-entry用户行为。

### G4 — Capability-discovery integrated normal entry

保留V0.4不可拆分G4：

```text
ordinary prompt
-> workflow-core implicit consumption
-> correct specialist consumption
-> targeted capability discovery
-> correct canonical/equivalent route
-> no non-equivalent fallback
-> bounded expected outcome
```

另保留true capability-absent contrast。  
同一run / 同一final candidate，不拼接。

### G5 — Broad should-not-change / integration regression

保持V0.4主体：

- 0.3 W1–W5；
- 0.4 Reviewed bootstrap/resume contract仍不回归；
- source/generated/Marketplace/version parity；
- specialist-contained negative；
- 至少一个不同specialist family的adjacent negative；
- risk-matched full tests/CI。

新增should-not-change：

- 0.4已有canonical Bridge routing仍可被正确选择；
- 本轮“不要raw fallback”不能误伤合法、六维等价、低权限recovery；
- 本轮不把普通simple/specialist-only task升级成workflow-core。

### G6 — Real least-privilege / approval-boundary normal-entry replay

这是本轮唯一新增 Gate，因为它有新的 failure semantics 与 evidence surface：真实 approval/side-effect boundary + 已完成成果保留。

final candidate必须在一个普通复杂任务中直接观察：

```text
ordinary complex task
-> workflow-core actual implicit consumption
-> repo-local build/check uses workspace-write normal entry
-> optional cleanup does not trigger escalation
-> bounded/canonical publication route attempted
-> bounded publisher returns authority/transport blocker
-> completed local artifacts + local commit remain intact/valid
-> raw git push / broader privileged fallback NOT attempted
-> no second same-class escalated retry without new information
-> only publication effect remains blocked
```

要求：

- 使用通用临时/fixture repo与canonical route contract，不能硬编码STAT5060、用户名、Longleaf path、`ctex`、scenario id；
- bounded publication failure应在安全preflight处发生，避免为了Gate制造真实不必要publication side effect；
- evidence要包含actual command/tool trace、approval/route choice、artifact/commit identity before/after；
- “没有raw push”不能只靠source grep证明，必须由该run的实际trace支持；
-如果当前测试环境无法直接暴露所需trace，先修evidence harness或诚实BLOCKED，不得降成self-report。

G6与G4不同：G4证明capability discovery/specialist composition；G6证明privilege selection、approval rejection recovery、effect-scoped evidence在真实normal entry中组成一条链。

## 13. Gate lifecycle 与 release selection

开发期：

```text
cheap deterministic tests
-> known regression bank (old environment/render + new approval incident)
-> targeted G1/G2/G3 iteration
-> unrelated should-not-change
-> stable 0.4 qualification candidate
```

0.4 qualification candidate只需要证明：

-原真实失败已被机制捕获；
-新approval/route regression已被机制捕获；
-相邻unrelated regression未破坏；
-实际candidate plugin可被正常消费。

它**不是final release claim**，也不要求为了保险重复跑完整final campaign。

只有qualification candidate PASS后：

```text
workflow-core 0.4 -> 0.5 exactly once
repository current release -> next PATCH
canonical regenerate
freeze one final candidate
```

随后同一个final candidate直接运行：

```text
G1 -> G2 -> G3 -> G4 -> G5 -> G6
+ broad CI
-> independent final-candidate Critic
-> canonical release closure
```

如果final Gate失败：

- candidate不发布；
- 在冻结Plan内允许普通bug/test修复；
-任何product mechanism/Gate/scope/version/authority语义变化返回Planner/Critic；
-修复后产生新candidate，final G1-G6必须重新完整跑；
-不挑赢家、不拼不同candidate evidence。

本轮没有paid/fresh one-shot holdout；G1-G6是可重复的release qualification。独立Critic是final candidate的定性/架构/证据完整性审查，不需要为普通修复在中途建立第二个control workflow。

## 14. Future execution topology：普通 bounded implementation

Design PASS后，下一版execution package默认应冻结：

- 一个ordinary task branch；
-一个普通worktree/当前合法checkout；
-不创建Reviewed task；
-不写`CURRENT.json`；
-不使用`PLAN_FROZEN`；
-不启动Reviewed watcher / Scheduled Reviewer state machine；
-不建立Stage A/Stage B；
-不因为final Critic而中途把Codex挂起成一个新状态机。

建议未来branch identity使用语义形式，例如：

`work/workflow-core--normal-entry-reliability`

exact branch/worktree在execution package阶段再根据当时真实checkout冻结；本Proposal不创建它们。

普通publication/release仍必须使用当时canonical AI Skills Maintainer / Host route；如果bounded publication失败，按本Proposal的effect-scoped fail-closed规则处理，不能raw fallback。

## 15. 预计production source

若Design Critic PASS，后续implementation预计仍以现有source为主：

- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
  - trigger precision保持；
  - W2/W3/W4补route/approval/effect语义；
  - specialist routing加入least-privilege normal-entry invariant。
- `skills/core/codex-system/codex-workflow-protocol/references/escalation-rules.md`
  - detailed approval classification；
  - privilege-non-increasing recovery；
  - bounded route failure / optional effect处理。
- `skills/core/codex-system/codex-workflow-protocol/agents/openai.yaml`
  -只做必要trigger precision，不把approval关键词做成泛触发。
- `skills/core/codex-system/codex-workflow-protocol/evals/trigger_queries.json`
  - implicit/contextual/hard negatives与新的route scenario。
- target regression / production replay evidence。
- canonical generated workflow-core payload。

默认不改Bridge、Host Policy、render/statistics/browser specialists、Longleaf、STAT5060。

## 16. Alternatives

### A. 继续修Reviewed Handoff execution package

拒绝。它解决的是我们自己引入的control-plane复杂度，而不是workflow-core用户能力。

### B. 把approval问题全部交给Bridge

拒绝。Bridge拥有具体publisher/Host实现，但“先选最低权限正常入口、审批失败后怎样分类、是否允许更宽fallback、如何保留已成功effect”是跨工具workflow语义，属于workflow-core。

### C. 新建approval/permission skill

拒绝。会与W2/W3/W4和Bridge authority重叠。

### D. 只加一句“approval失败不要重试”

拒绝。它无法区分optional effect、选错高权限route、真实authority boundary与broken normal entry，也无法处理成果保留。

### E. 本V0.5 bounded extension

采用。复用现有trigger、specialist routing、fallback equivalence、W3/W4，只增加真实缺失的route/privilege语义和一个G6真实Gate。

## 17. Red Team

实现/评审必须防：

- 用“least privilege”口号机械阻止所有合法escalation；
- 把`require_escalated`字符串列黑名单，而不看当前effect是否真的需要；
- 把publisher failure硬编码成`ai-bridge`专用case；
- bounded route失败后换shell/python/raw command绕过；
- optional cleanup被误升成required completion；
- publication blocked后删除/重算已通过local artifacts；
- W4只计拒绝次数，不做route reassessment；
- G6用source grep证明“没有raw push”；
- G6用mock-only helper冒充normal-entry；
- 新规则导致specialist-contained任务误触发workflow-core；
- 为修workflow-core顺手改Bridge。

## 18. Bridge follow-up record

本Proposal确认存在Bridge-owned follow-up，但**不承担处理职责**。

Verified from Bridge source：

- formal `release` ref = `9dad0ba4bfa54e251f345091c5151ae991251ec9`；
- release package version = `0.9.3`；
- current main = `7df05b98b09bec4da4382853c360ca70a8ca3a5f`；
- release -> current main当前差异仅README/docs/design/results/evidence，没有runtime source diff；
- release `host.py`会在sanitization前因为ambient `GIT_ASKPASS/SSH_ASKPASS` fail closed；
- current Bridge main已有0.10.0 design处理publisher compatibility/runtime identity方向。

User-provided runtime evidence：

-同一conda环境出现0.9.1/0.9.3 editable metadata；
- installed checkout HEAD指向formal 0.9.3 release。

Planner disposition：

-不把“behind main”当成runtime drift；
- duplicate metadata作为installation-hygiene ambiguity；
- Bridge 0.10由另一个thread继续；
- workflow-core只把bounded publisher failure当作route/recovery regression evidence。

## 19. Maintenance Board / TODO

本轮已把新的真实事故合并回现有workflow-core canonical TODO条目，没有新增重复heading，并把该主问题从raw `NEW` triage为 `PROMOTE_NOW`。

当前没有Project mutation + Clear Writing surface，因此：

-不创建/改写tracking Issue；
-不伪称Project已同步；
-不要求用户手工维护；
-下一次合法Project-capable action应为该PROMOTE_NOW主问题创建/绑定tracking Issue、回写`tracking: #N`、Status=`DOING`并把本Proposal作为current anchor。

#5/#6/#11及其ADAPTING closure语义继续沿用V0.4，不因本轮approval事故改变。#7/#8/#9/#10仍不并入本轮专属逻辑；#8只继续提供其generic optional-mode regression。

## 20. Version / maturity

当前设计阶段：

```text
Repository bump decision: NONE
Affected plugins:
- workflow-core: NO_BUMP
Reason: design revision only; implementation not started.
```

未来release：

- workflow-core：`0.4 -> 0.5` exactly once；
- repository：按届时真实current release推进一个PATCH；
- maturity：不提升。

## 21. Stop conditions

下一阶段若出现以下任一项，回Planner/Critic，不扩大：

-必须新增authorization database/state/schema/wrapper；
-必须修改Bridge runtime/Host Policy；
-必须让workflow-core决定Git/publisher实现；
-必须硬编码特定项目/机器/用户名/路径；
-G6只能靠mock/self-report而无法观察normal-entry trace；
-“least privilege”使合法required effect无法执行但没有清晰authority route；
- final candidate evidence只能靠跨candidate拼接；
-需要paid API。

## 22. 本Proposal不批准什么

-不批准implementation；
-不批准branch/worktree创建；
-不批准version bump；
-不批准release；
-不批准Bridge mutation；
-不批准Project/Issue mutation；
-不批准paid API；
-不批准使用V0.1/V0.2 execution package。

下一步仅是独立Critic对本V0.5 Design Revision做DESIGN_REVIEW。PASS后才重新准备一个**普通bounded implementation** execution package。
