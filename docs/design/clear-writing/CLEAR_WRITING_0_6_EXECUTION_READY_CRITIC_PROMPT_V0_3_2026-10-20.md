# Clear Writing 0.6 — execution-ready Critic final re-review prompt v0.3

本轮修复的是最终 Critic 入口，不重新设计 Clear Writing 0.6 产品。

上一版 package：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

上一版 task-specific Critic prompt 错误地把最终 execution-ready 审查缩成只复核四个 blocker，并且 PASS 输出停在 `NEXT_HANDOFF=USER_AUTHORIZATION`，没有按最新 Critic Role Contract 1.7 重新审完整执行包并直接交付短 Codex handoff。该旧 prompt 不再作为本轮审查合同。

## 1. Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin = writing-style / Clear Writing
task_key = clear-writing--single-entry-artifact-finalization
branch = design/clear-writing--single-entry-artifact-finalization
approved_proposal = 3eefc626b86566113125a06fc6046a2bec1eafb2
base_v0_2_package = d7b810d194ead881303aaca9c2e4f1d59a97c1f1
review_stage = EXECUTION_READY_FINAL_REVIEW_V0_3
```

用户会提供：

`PACKAGE_COMMIT=<exact current branch commit>`

从该 exact commit 读取：

1. `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_2_2026-10-20.md`
2. `docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_2_2026-10-20.md`
3. `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_2_2026-10-20.md`
4. `docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_2_2026-10-20.md`
5. 本文件。

核对 `base_v0_2_package..PACKAGE_COMMIT`：除新增本 v0.3 Critic prompt 外，Proposal、Plan、Goal、Runbook、Kickoff 和产品设计不得发生漂移。若发生其他变化，先判断是否改变冻结语义；改变则 REVISE。

## 2. 强制读取与优先级

先读取最新 `AI_Skills_Collection/main`：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/project-settings/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_SNAPSHOT_2026-10-19.md`
- 维护看板、版本规则和 `writing-style` 当前 TODO。

最新中央角色合同优先于旧 task-specific prompt。最终 execution-ready 审查不得被缩成旧 blocker closure；必须重新核对完整用户承诺、完整执行包、正常成功链、关键失败链、恢复和授权边界。

## 3. 完整产品承诺复核

独立确认以下内容已经闭合，不能只复核上一轮四个 finding：

1. ChatGPT Personal Plugin 只有一个顶层 `clear-writing` 入口；六项 canonical writing capability 仍由唯一 source 投影，Codex 六项直接入口保持不变。
2. 0.6 的外部产物最终化正式声明只覆盖：用户显式选择 Clear Writing 后，通过 GitHub connector 处理 UTF-8 repository text file；不得外推成所有插件、所有写入或所有外部 surface 的全局强制拦截。
3. G3 必须真实证明：

```text
fresh ChatGPT Web conversation
→ explicit Clear Writing selection
→ fetch_file 读取目标全文并保存目标 identity
→ Clear Writing 形成唯一完整终审 candidate 及 identity/hash
→ 写入前再次读取并确认目标未漂移
→ update_file 写入同一完整 candidate
→ 记录 returned commit/content identity
→ fetch_file 回读实际 repo 文件
→ readback 与 candidate 完全一致
→ 独立阅读全文做保真与可读性审查
```

缺全文读取、缺完整 candidate、只输出 diff、只改局部、缺写前 identity 检查、缺写入、缺回读、回读不等于 candidate、或只检查聊天回复，G3 必须 FAIL。

这个合同已经足以证明“显式 Clear Writing 正常入口写入的 repo 文件就是该次终审 candidate”。不要自行新增 `create_blob`、MCP、App、写入网关或平台级全局拦截；除非当前包事实上无法满足上述已冻结产品声明，并给出精确矛盾证据。

4. G1–G6 各自证明的能力、顺序、同一 final candidate、known regression 与唯一 fresh G6 已闭合；G4/G6 无循环；G6 失败不能换题。
5. 包装投影、deterministic ZIP、Personal Plugin overlay/update、恢复集合、0.5 baseline 保存、forward restore 和 terminal failure 行为已闭合。
6. 模型、attempt、retry、stop、版本、Issue #13、README/changelog/release 边界已闭合。
7. Codex 不需要自行决定产品声明、外部 surface、包装、Gate、失败恢复、版本或权限边界；只剩普通实现细节和执行时真实验证。

## 4. 上一轮四个 blocker 的优先复核

完整复核基础上，再重点确认：

- `CW06-ER01`：`CW06_ROUTE_PROJECTION_V1` 的两项 transform、support/provenance parity、helper 可运行性和 fail-closed。
- `CW06-ER05`：G4/G6 无循环，G2-T3 source delivery 固定为唯一 repo/ref/path。
- `CW06-ER08`：`CW06_DETERMINISTIC_ZIP_V1` 是唯一 raw ZIP identity。
- `CW06-ER09`：Plugin Creator 当前 overlay/delete/version 现实、两个 restore set、完整 forward restore 和 infrastructure-blocked recovery。

这四项是优先检查，不是最终审查范围上限。

## 5. 用户问题与范围纪律

用户要求解释“怎么工作”“怎么验收”“如何保证写入 repo 的文件经过 Clear Writing”时，先依据已批准包用自然中文回答当前机制。

不要把解释请求自动升级为新产品需求；不要为了显得更严格临场增加 `create_blob`、MCP、App、daemon、database、state machine 或全局写入拦截。只有解释过程发现当前包与冻结用户承诺存在真实矛盾，才可 REVISE，并给出精确证据和最小修订。

## 6. Verdict

只能给：

```text
PASS
READY_FOR_CODEX=YES
```

或：

```text
REVISE
READY_FOR_CODEX=NO
```

PASS 仅在完整执行包和完整用户承诺均已闭合时允许。它不是 implementation/Gate/release PASS，也不代替用户授权。

## 7. PASS 的用户可见输出

PASS 回复必须严格分两层。

### 第一层：一屏中文说明

必须直接说明：

- 这次批准的产品架构到底是什么；
- 单入口、六项能力和 GitHub 文件最终化怎样工作；
- G3 如何证明 repo 最终文件就是 Clear Writing 终审 candidate；
- G1–G6 分别证明什么；
- 失败后何时停止、何时恢复 0.5；
- 当前仍未证明什么；
- 用户下一步只需发送哪一段给 Codex。

不得用 finding、路径、哈希或 Gate 编号堆砌代替解释。

### 第二层：短 Codex handoff

必须直接输出可复制的短 handoff，不得停在 `NEXT_HANDOFF=USER_AUTHORIZATION`，不得全文复制 Kickoff Draft，也不得把批准前的 `DRAFT / NOT_AUTHORIZED / 等待 PASS` 控制面带入用户执行入口。

固定结构：

```text
APPROVED_PROPOSAL_PATH=docs/design/clear-writing/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_PROPOSAL_V0_1_2026-10-20.md
APPROVED_PLAN_PATH=docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_2_2026-10-20.md
APPROVED_GOAL_PATH=docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_2_2026-10-20.md
APPROVED_RUNBOOK_PATH=docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_2_2026-10-20.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_2_2026-10-20.md
APPROVED_COMMIT=<exact PACKAGE_COMMIT>
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
=== COPY TO CODEX BEGIN ===
执行同一任务 `clear-writing--single-entry-artifact-finalization`。严格读取上述 approved package，在批准范围内实现 Clear Writing 0.6，完成 repository implementation、独立实现审查、final candidate freeze、现有 USER/PRIVATE Personal Plugin 更新、G1–G6、完整产物审查和 release closure。允许 task-owned add/commit 与普通 non-force push；不得修改 Project setting、其他插件产品、Bridge Kit，或新增 MCP/App/后台服务/数据库/状态机。普通实现、测试、运行时或冻结 Gate 失败在同一任务内修复；只有用户承诺、架构、外部 surface、权限、Gate 成功定义或恢复语义必须改变时才停止并回 Planner。任何批准包规定的 terminal failure 按 Runbook 停止并执行恢复；全部 required Gate 和最终完整产物审查通过前，不得宣称 0.6 完成或发布。
=== COPY TO CODEX END ===
```

若短 handoff 无法在不猜测、不丢授权、不改变 scope 的情况下生成，必须 REVISE，不能把完整 Kickoff Draft 倒给用户。

## 8. REVISE 输出

先用一屏中文说明真正问题和用户影响，再给稳定 blocker、最小关闭条件及完整 Planner prompt。

不得重新设计已经通过且未被真实证据推翻的部分。

## 9. 禁止

本轮不得：

- 实施或修改产品代码；
- 更新 Personal Plugin；
- 创建 G3 branch；
- 运行 G1–G6；
- 调用付费模型；
- 修改 Project setting；
- 把 PASS 当成用户尚未发送的执行授权。
