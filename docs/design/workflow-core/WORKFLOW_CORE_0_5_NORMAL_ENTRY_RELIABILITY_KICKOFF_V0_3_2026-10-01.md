# workflow-core 0.5 ordinary bounded implementation Kickoff Draft v0.3

仅在 execution-ready Critic 对 Proposal V0.5 + Plan v0.3 + Goal v0.3 + 本 Kickoff 同版 PASS 后发送给 Codex。

我批准执行：

- repo：YuukiAS/AI_Skills_Collection
- Proposal：docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_5_2026-10-01.md
- Plan：docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_3_2026-10-01.md
- Goal：docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_3_2026-10-01.md
- exact branch：work/workflow-core--normal-entry-reliability
- exact worktree：/home/yuukias/AI_Skills_Collection-workflow-core--normal-entry-reliability

这是普通 bounded implementation，不使用 Reviewed Handoff。

我授权：按 Plan preflight 从最新合法 origin/main 创建上述 exact branch/worktree；执行 task-owned commits；运行 zero-paid local tests、candidate replay、G1-G6、full local checks，以及该 exact task branch所需的 zero-paid GitHub CI；为首次远端CI只做该 exact task branch的一次普通 non-force first publication。Qualification PASS后，按 Plan exactly once 将 workflow-core 0.4 -> 0.5，并把 repository从执行时真实正式版本推进一个PATCH。

final candidate只有在同一candidate的G1-G6、broad CI和独立 final Critic全部PASS后，才授权按当前canonical bounded路径把 exact candidate集成到 main、普通 non-force publication、正式 repository PATCH release、当时contract要求的 fast-forward-only release ref closure，以及 workflow-core production identity/install-update smoke。

明确不授权 paid API、force/destructive Git、branch删除、worktree remove/prune、stable tag创建/移动、Bridge/Host Policy/publisher修改、Longleaf/STAT5060/render-specialist修改、consumer-machine adaptation或scope/Gate/architecture expansion。

如果 canonical/bounded publication route失败，不得自动 raw/broader fallback；只阻塞对应publication/release effect并保留已成功local成果。Bridge 0.10不是本任务前置条件，也不得在本任务里修Bridge。

先读取 approved Plan/Goal、当前 AGENTS 和实际 source，再执行 Goal。只有 architecture、Gate semantics、scope、version policy或authority semantics需要变化时才停回 Planner/Critic；普通bug/test/fixture repair自行完成。
