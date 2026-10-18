# Project Instructions Editor 0.2 — Codex Kickoff Draft v0.2

Status: DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW

Use this prompt only after an independent Critic has approved the same-version Plan + Goal + Kickoff package. Until then, `READY_FOR_CODEX=NO`.

---

在 `YuukiAS/AI_Skills_Collection` 实现已批准的 Project Instructions Editor 0.2 bounded increment。

Canonical package：

- Plan: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_2_IMPLEMENTATION_PLAN_V0_2_2026-10-18.md`
- Goal: `docs/goals/PROJECT_INSTRUCTIONS_EDITOR_0_2_IMPLEMENTATION_GOAL_V0_2.md`
- Task key: `project-instructions-editor--0.2-baseline-diff-contract`
- Branch: `reviewed/project-instructions-editor--0.2-baseline-diff-contract`
- Worktree: `../AI_Skills_Collection-project-instructions-editor--0.2-baseline-diff-contract`

先读取当前 `main` 的 `AGENTS.md`、上述 Plan/Goal、当前 PIE production source、focused tests、版本规范和维护看板规则。使用 `workflow-core` 的执行/验证约束与 `ai-skills-core` / AI Skills Maintainer 的仓库维护合同；PIE 0.1 当前 source 是目标领域合同，不要重新设计 0.1 架构。

用户发送本已批准 Kickoff 后，授权范围仅限：

- 创建/使用上述 branch + worktree；
- 修改 Goal 明确列出的 PIE 0.2 source、focused tests/evals、直接相关 README/CHANGELOG、registry/catalog/provenance 与 evidence；
- 按 Goal 创建新的 0.2 tracking Issue / backlink / Project 状态，但 reader-facing Issue/README 修改前必须真实调用仓库要求的 Clear Writing；不可用时诚实记录 exact pending mutation，不得假称调用；
- 运行本地免费测试、generator、公开安全 candidate replay；
- ordinary non-force Git commit/push；
- 冻结 `FINAL_CANDIDATE_COMMIT=C`，从 C 重跑 G1 development/pre-final diagnostics 与 G2/G3，并准备 G4 pre-final review packet；
- implementation 阶段只能记录 `G1_DEVELOPMENT_EVIDENCE`，不得写最终 `G1=PASS`；`G1_FINAL_LIVE` 必须保持 `PENDING`，直到后续获批的真实 ChatGPT Web / Project normal-entry acceptance。

严格实现已冻结增量：

1. 没有用户在当前任务中提供的完整当前 Project setting 原文时，PIE 不开始分析/压缩/修改/重组/同步/重置，只返回 Goal 中冻结的 exact missing-baseline message。
2. 明确为空是完整 greenfield baseline。
3. explicit reset 仍要求用户 baseline，但不恢复旧 setting semantic-preservation obligation。
4. 每次真实修改同时给：
   - 人类可读 Markdown diff，默认 `~~旧~~**新**`，大改可升到整句/整段/整节；
   - 完整 clean final Project setting。
5. preview 与 clean final 必须来自同一个 user baseline B 和同一个 delta E，保持 `E(B)=C`。
6. diff 只展示已完成的 semantic edit，不得成为第二套编辑器。
7. PIE 0.1 的 protected absence、no-op、ownership/enforcement、locator、budget、semantic invariants 和 mandatory final consistency pass 全部保留。
8. Skill candidate version `0.1 -> 0.2`；repository `VERSION` 和 `release` ref 本 Goal 不推进。

禁止：

- 数据库、ledger、复杂 AST、runtime diff service/script、第二状态机；
- Clear Writing 作为 PIE runtime dependency；
- external finalizer、额外模型、付费 API；
- C11 reader-layer scope；
- Bridge Kit 修改；
- central Plugin behavior/version 修改；
- live ChatGPT private wrapper 更新或发布；
- 实际用户 Project setting 写回；
- force push、rebase、destructive mutation、越界修复 unrelated drift；
- 重开 Issue #93。

先跑 cheap deterministic regression，再做 G1 development/pre-final diagnostics 与 G2/G3；所有候选相关证据必须来自同一 C。生成 G4 pre-final packet 后停止并交独立 implementation review，不要自行做 live Web acceptance 或 release。

PIE02-ER1 的关闭要求必须严格执行：

- fixture/public-safe G1 只能写 `G1_DEVELOPMENT_EVIDENCE=PASS|FAIL`；
- 本 Goal 结束时 `G1_FINAL_LIVE=PENDING`；
- 后续只有在独立 pre-final review 放行并获得用户明确授权后，才能把 exact C 更新到现有 PRIVATE / USER-scope PIE wrapper；
- 真实 Web acceptance 的第一步必须是一个不点名 PIE、且不提供 baseline 的自然 Project-setting 编辑请求；只有它只返回冻结的 exact missing-baseline message 时，才允许最终记录 `G1_FINAL_LIVE=PASS`；
- 随后在同一获批 live acceptance 中提供完整 B + 真实修改请求，产生 live R + clean C，供 G4 定性审查；
- 不创建第五 Gate。

最终必须报告：

```text
FINAL_CANDIDATE_COMMIT=
EVIDENCE_HEAD=
G1_DEVELOPMENT_EVIDENCE=
G1_FINAL_LIVE=PENDING
G2=
G3=
G4_PREFINAL_PACKET_READY=
G4_FINAL_LIVE=PENDING
README_CLEAR_WRITING=
TRACKING_ISSUE=
PROJECT_STATUS_SYNC=
Repository bump decision: NONE
project-instructions-editor: 0.1 -> 0.2 candidate
READY_FOR_INDEPENDENT_IMPLEMENTATION_REVIEW=
READY_FOR_LIVE_WEB_ACCEPTANCE=NO
READY_FOR_RELEASE=NO
```
