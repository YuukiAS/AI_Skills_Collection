# workflow-core 0.5 ordinary bounded implementation Kickoff Draft v0.4

仅在 execution-ready Critic 对 Proposal V0.5 + Plan v0.4 + Goal v0.4 + 本 Kickoff 同版 PASS 后发送给 Codex。

我批准执行：

- repo：YuukiAS/AI_Skills_Collection
- Proposal：docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_5_2026-10-01.md
- Plan：docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_4_2026-10-01.md
- Goal：docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_4_2026-10-01.md
- canonical checkout：/home/yuukias/AI_Skills_Collection
- exact branch：work/workflow-core--normal-entry-reliability

这是普通 bounded implementation，不使用 Reviewed Handoff，也不创建 sibling worktree。

我授权：先在 canonical checkout 执行 Plan 的 preflight，包括 git fetch origin main、post-fetch drift、checkout ownership/cleanliness、local/remote exact branch absence与冲突检查；全部通过后，只创建并切换 exact branch work/workflow-core--normal-entry-reliability。若 canonical checkout被其他任务占用、存在无法安全保留的 unrelated dirty work、branch冲突或 branch create/switch被拒绝，mutation前停止回 Planner，不得换 /tmp、second clone、sibling worktree、其他branch或更高权限route。

我授权该 exact branch上的 task-owned commits、zero-paid local tests、candidate replay、G1-G6和full local checks。Qualification PASS后，按 Plan exactly once 将 workflow-core 0.4 -> 0.5，并把 repository从执行时真实正式版本推进一个PATCH。

final candidate冻结后、开始 final G1-G6 前，我另外明确授权一次且仅一次 exact first publication + upstream binding。执行前必须确认 remote exact branch不存在；只允许与下式等价的 ordinary non-force same-name command shape：

git push --set-upstream origin work/workflow-core--normal-entry-reliability

该动作只可创建 origin/work/workflow-core--normal-entry-reliability 并把当前 exact branch upstream绑定到 origin同名branch。不得 force、不得 push tags、不得 push其他branch/refspec。这个 first publication是本Kickoff事先批准的planned effect，不是任何publisher失败后的fallback。

first publication之后，所有后续task-branch publication必须使用执行时 canonical bounded current-branch publisher；bounded publisher失败后不得raw git push或更宽privileged fallback。G6必须按Plan验证真实bounded route blocker、local artifact/commit保留、no raw fallback和no second same-class retry。

final candidate只有在同一candidate的G1-G6、broad CI和独立 final Critic全部PASS后，才授权按当前canonical bounded路径把 exact candidate集成到 main、普通 non-force publication、正式 repository PATCH release、当时contract要求的 fast-forward-only release ref closure，以及 workflow-core production identity/install-update smoke。

明确不授权 paid API、force/destructive Git、branch删除、arbitrary cleanup、stable tag创建/移动、Bridge/Host Policy/publisher修改、Longleaf/STAT5060/render-specialist修改、consumer-machine adaptation或scope/Gate/architecture expansion。

如果 first publication或任何后续 canonical/bounded publication route失败，只阻塞对应publication/release effect并保留已成功local成果；不得更换raw command、remote、branch、权限路线或在本task修Bridge。Bridge 0.10不是本任务前置条件。

先读取 approved Plan/Goal、当前 AGENTS 和实际 source，再执行 Goal。只有 architecture、Gate semantics、scope、version policy或authority semantics需要变化时才停回 Planner/Critic；普通bug/test/fixture repair自行完成。
