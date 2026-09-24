# Project Thread Handoff Recovery — Codex Kickoff Draft v0.1

Task key：`science-communication--project-thread-handoff-recovery`  
Status：DRAFT_NOT_AUTHORIZED  
Approved design：`docs/design/PROJECT_THREAD_HANDOFF_V5_RECOVERY_PROPOSAL_2026-09-24.md` V5 @ `df0ca1ab809cf53b0d14901782bbf1a0d8a70642`  
Implementation Plan：`docs/design/PROJECT_THREAD_HANDOFF_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-09-24.md` v0.1  
Canonical Goal：`docs/goals/PROJECT_THREAD_HANDOFF_RECOVERY_GOAL_V0_1.md` v0.1

只有独立 Critic 对同版 Proposal + Plan + Goal + Kickoff 返回 `READY_FOR_CODEX=YES` 后，
用户实际发送下面正文，才形成 implementation authorization。

## Kickoff 正文

执行 `science-communication--project-thread-handoff-recovery`。

Repository：
`YuukiAS/AI_Skills_Collection`

严格按：

- `docs/design/PROJECT_THREAD_HANDOFF_V5_RECOVERY_PROPOSAL_2026-09-24.md`
  @ `df0ca1ab809cf53b0d14901782bbf1a0d8a70642`
- `docs/design/PROJECT_THREAD_HANDOFF_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-09-24.md`
- `docs/goals/PROJECT_THREAD_HANDOFF_RECOVERY_GOAL_V0_1.md`

不要重新设计 V5。

Exact branch：

`reviewed/science-communication--project-thread-handoff-recovery`

Exact worktree：

`../AI_Skills_Collection-science-communication-project-thread-handoff-recovery`

我授权本 frozen task 创建/使用上述 exact branch/worktree，以及在该 branch上做普通 task-owned commit
和 ordinary non-force push。不得换 branch/path、`/tmp` clone、第二 worktree、force push或 remote remap。

如果 Host/sandbox仍拒绝 exact sibling worktree creation，不要绕过。只报告：

`NEEDS_HUMAN_WORKTREE_BOOTSTRAP`

并给我一条 exact `git worktree add` 命令；我在 sandbox外创建后，你从同一 Goal继续，不重开任务。

先 `git fetch origin main` 并核 current drift。无关 docs/TODO drift直接吸收；若 Project Thread Handoff
source/version/icon/distribution或 VERSION slot冲突，停止回 Planner。

只修改 Goal/Plan允许的 PTH source、tests/public-safe fixtures、generated parity、VERSION/README/CHANGELOG
与 task results。

实现：

- Mode A current-thread handoff保持 V0.1；
- Mode B same-Project old-thread semantic recovery；
- PTH-06 target-chat provenance；
- strong vs limited recovery；
- cross-Project authority boundary；
- explicit-only；
- no repo-write behavior；
- no MCP/database/CURRENT/history/transcript API/browser extension/external API。

保持 canonical icon bytes：

`skills/science/communication/project-thread-handoff/assets/app-facing.svg`

把 Skill `0.1 -> 0.2`，repository candidate `5.1.0 -> 5.1.1 PATCH`，所有中央 Plugins `NO_BUMP`。
若 current `origin/main:VERSION != 5.1.0`，停止并报告 `VERSION_DRIFT`。

更新
`docs/operations/prompts/PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md`，要求后续 Plugin Creator只更新
现有 PRIVATE / USER-scope / skills-only Project Thread Handoff wrapper，不创建新 Plugin，不加 MCP，
并复用 canonical `app-facing.svg`；bundled icon须与 exact candidate byte-equivalent，target明确不支持
SVG时才 deterministic conversion，禁止 redesign。

在找用户 target acceptance前，自行完成 source、focused tests、generated parity、full relevant tests、
public-safe regressions、icon hash check、version/README/changelog candidate closure、candidate freeze、commit、
exact branch push与 remote verification。

准备：

```text
results/science-communication--project-thread-handoff-recovery/result.md
results/science-communication--project-thread-handoff-recovery/MANIFEST.md
results/science-communication--project-thread-handoff-recovery/target-surface-acceptance.md
```

用户操作前 G1/G2/G3 target部分保持 PENDING。

不要提交真实 old thread全文、完整 private recovery output、private Plugin ID/URL或 unrelated Memory Sources。

只保留 G1/G2/G3。G3 strong PASS必须看到目标 Bridge/SSH old conversation作为 identifiable past-chat
source/equivalent provenance；generic Saved Memory/profile/unsourced recall不能替代。若关键 decision无
target provenance，G3 strong FAIL并回 Planner/Critic，不得靠 Work/Codex/MCP/database救 PASS。

当 final candidate完整且只剩 target Pro regular Chat acceptance时，停止并报告：

`FINAL_CANDIDATE_READY_FOR_TARGET_ACCEPTANCE=YES`

不要更新/创建 personal Plugin，除非后续 target-surface acceptance通过正常 ChatGPT-side入口执行；
本 Kickoff不授权创建新 Plugin，也不替代平台账户确认。

不要 merge main、tag、release、publish或调用 paid API。

只要 G1/G2/G3未对同一 final candidate完成：

`PROJECT_THREAD_HANDOFF_V0_2_READY != YES`
