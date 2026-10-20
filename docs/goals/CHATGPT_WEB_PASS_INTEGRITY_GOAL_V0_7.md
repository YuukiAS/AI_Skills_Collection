# Canonical Goal v0.7 — chatgpt-web--pass-integrity

日期：2026-10-21  
任务：`chatgpt-web--pass-integrity`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`

## 目标

把 Planner/Critic 治理升级到 1.8，使“execution-ready”不再只代表文档结构完整，而必须有足够证据证明关键执行接口、恢复接口和跨 surface handoff 真实可执行；同时让任何需要继续推进的非终态回复都完成用户交接，而不是只报告 blocker。

## 用户最终应该得到什么

### execution-ready PASS 前

Planner/Critic 必须区分：

- 已验证执行能力；
- 只能实施中验证的条件性能力；
- 仍未证明、因此不能声称 execution-ready 的假设。

对真正影响实施、证据生成或安全恢复的关键接口，必须有现实证据，或有明确的“谁、在哪、何时、在什么副作用前验证、失败怎么停”的 conditional contract。

### 任务中途停止时

用户不需要自己判断内部角色或寻找“更强 execution surface”。

如果任务仍需继续，回复必须让用户直接知道：

- 已完成什么；
- 为什么停；
- 什么还没完成；
- 每个 blocker 归谁；
- 用户现在要不要做什么；
- 唯一下一入口；
- 需要用户转交时，完整 prompt 已经准备好。

如果下一责任仍属于当前 Planner，Planner 继续处理，不把自己的工作重新交还用户。

### 最终 PASS 时

同一回复必须一次交齐：

1. 一屏实际架构说明；
2. exact approved locators；
3. `READY_FOR_CODEX=YES`；
4. `NEXT_HANDOFF=CODEX`；
5. 短 `COPY TO CODEX`。

正文必须真实讲清架构、正常用法、主要风险/恢复边界和未证明事项，不能只满足机器字段。

## 1.8 必须实现

### Planner

1. task-specific Critic prompt compatibility preflight；
2. short Codex handoff renderability preflight；
3. critical-interface reality evidence：
   - actor / surface；
   - upstream output；
   - downstream consumer；
   - format / materialization；
   - direct evidence 或 conditional verification；
   - safe stop / recovery；
4. non-terminal handoff closure：
   - existing §10.1 的唯一下一入口必须落实到真实回复；
   - current Planner 自己拥有的后续工作不甩给用户；
   - 抽象“需要一个具备若干能力的环境”不算 next entry。

### Critic

1. task-prompt compatibility hard gate；
2. atomic PASS；
3. PASS 后 explanation / contradiction / new requirement；
4. critical-interface evidence hard gate；
5. whole-response handoff/readability acceptance。

## 不重复修改的顶层规则

当前 Project setting 已经要求真实能力、正常入口、自然中文、最小用户动作和真实交接；本任务不修改它。

Capability Gate Policy 1.2 不修改。

Clear Writing 0.6 产品、Bridge Kit、Plugin Creator 不修改。

## 真实验证

candidate 1.8 必须通过同一冻结批次：

### Case A — execution-ready 负控

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

正确结果必须是 `REVISE`，且不能只发现旧 task prompt 冲突，还要发现：

- Plugin Creator archive / restore builder / materialization 未证明；
- fresh ChatGPT Web actor/surface 未证明。

### Case B — 非终态用户交接

使用真实 Phase C stop evidence 和原始用户回复。

candidate Planner 必须输出一条完整、自然、可继续执行的回复，明确：

- Personal Plugin 仍为 0.5.0；
- 为什么安全停止；
- archive compatibility 默认回同一 Codex task；
- fresh Web execution responsibility 缺口归 Planner；
- 用户现在需要什么动作；
- 唯一下一入口与完整可复制 handoff。

### Case C — 复杂正控

固定：

`745e6748c5faa7cbad51973142661491224ba5a2`

对象：

`055_clear_writing_release_convergence`

candidate Critic 必须重新做完整 execution-ready review。

若 current truth 支持 PASS，同一回复必须给 atomic PASS 五项并用正常中文讲清架构与边界。

若发现真实 blocker，必须 `REVISE`，同一批次不得更换正控。

## 真实 Web 执行边界

当前没有被验证的自动能力可以创建 fresh ChatGPT Web conversation 并绑定 candidate role contract。

因此 A/B/C 冻结为 user-only UI action：

- 系统预先准备 exact prompt；
- 用户只打开指定 fresh Planner/Critic conversation 并粘贴；
- 用户把完整回复返回长期 Planner；
- 长期 Planner 负责记录 evidence 与继续流程。

不要求用户读 repo、拼 prompt、选内部 Reviewer 或自己决定下一步。

## 候选与正式生效

实现后冻结：

`GOVERNANCE_CANDIDATE_COMMIT=<exact sha>`

所有 deterministic replay、post-implementation Critic 和 A/B/C 都绑定同一 candidate。

candidate 通过后：

`CANDIDATE_ACCEPTED`

随后按 `AGENTS.md 8.5`：

integration preflight -> non-force merge main -> push -> remote main fresh readback。

只有 fresh readback 直接证明 Planner/Critic 正式版本均为 1.8，才可宣称 1.8 正式生效。

## Claim ceiling

1.8 是治理合同，不是 runtime enforcement hook。

它不能保证模型永远不会忽略规则，也不能把不存在的平台 UI action 变出来。

它能做的是：要求证据、暴露未验证假设、拒绝不真实的 PASS、把坏的用户回复判为不合格，并用真实正常入口验证候选。

因此可信度来自“可观察证据 + 独立审查 + 真实回复验收 + 失败不放行”，不是来自规则文件存在本身。

## 完成条件

只有以下全部成立，本治理任务才完成：

- Planner/Critic 1.8 source 实现；
- `GOVERNANCE_CANDIDATE_COMMIT` 冻结；
- deterministic replay 成立；
- post-implementation Critic = `PROCEED_TO_FINAL_EVALUATION`；
- Case A 达到预期负控；
- Case B user-facing handoff/readability PASS；
- Case C genuine execution-ready review 达到其真实 verdict，且要完成治理正控必须实际 PASS；
- candidate = `CANDIDATE_ACCEPTED`；
- main integration + remote fresh readback成立。

README checked: no update required。
