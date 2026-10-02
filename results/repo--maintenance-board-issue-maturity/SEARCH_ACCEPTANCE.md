# Search Acceptance

Repository: `YuukiAS/AI_Skills_Collection`

Overall: `PASS`

Projection source: `results/repo--maintenance-board-issue-maturity/MIGRATION_CLASSIFICATION.csv`.
Live result source: `gh issue list --state all --search ...`.

| Query | Expected Issues | Actual Issues | Result |
| --- | --- | --- | --- |
| `label:maintenance-track label:kind:regression label:area:presentations` | `[31, 32, 35, 36, 37, 38, 40]` | `[31, 32, 35, 36, 37, 38, 40]` | `PASS` |
| `label:maintenance-track label:kind:governance` | `[4, 5, 6, 7, 9, 10, 11, 19, 21, 25, 29, 92]` | `[4, 5, 6, 7, 9, 10, 11, 19, 21, 25, 29, 92]` | `PASS` |
| `label:maintenance-track label:scope:cross-repo` | `[5]` | `[5]` | `PASS` |
| `label:maintenance-track label:area:workflow-core` | `[5, 6, 7, 8, 9, 10, 11]` | `[5, 6, 7, 8, 9, 10, 11]` | `PASS` |

## Details

### presentations_regressions

Query: `label:maintenance-track label:kind:regression label:area:presentations`

Expected: `[31, 32, 35, 36, 37, 38, 40]`

Actual: `[31, 32, 35, 36, 37, 38, 40]`

Result: `PASS`

Live titles:

- #31: 检查幻灯片句间与页间过渡
- #32: Accent colour and emphasis can drift without a semantic-role contract
- #35: 强化整套研究幻灯片的读者努力审查
- #36: Review coverage can self-certify unresolved reviewer feedback
- #37: Presentations 0.2 completion evidence can still miss obvious rendered regressions
- #38: Deck-wide formula, text and emphasis scale still lacks a stable hierarchy
- #40: Table, list and paragraph primitives still drift across one deck

### governance

Query: `label:maintenance-track label:kind:governance`

Expected: `[4, 5, 6, 7, 9, 10, 11, 19, 21, 25, 29, 92]`

Actual: `[4, 5, 6, 7, 9, 10, 11, 19, 21, 25, 29, 92]`

Result: `PASS`

Live titles:

- #4: 建立 AI_Skills 维护看板和源码追踪
- #5: Keep AI_Skills workflow rules separate from Bridge Kit runtime bugs
- #6: Real-task-driven Reviewed Handoff batches
- #7: Approval-sensitive handoff should emit one bounded kickoff before execution
- #9: 防止任务局部禁令变成全局规则
- #10: Post-056 acceptance artifact packaging / comparison-review fidelity
- #11: 修复 sibling worktree 授权与沙箱执行不一致
- #19: Keep style cleanup downstream of scientific structure
- #21: Keep research authoring separate from the generic language layer
- #25: Distinguish research-document semantics from comparison/render packaging
- #29: CAT-TRACE v13/v14 follow-up feedback is consolidated into the canonical inbox
- #92: 完善 AI Skills Maintenance Board 的 Issue 分类与 intake

### cross_repo

Query: `label:maintenance-track label:scope:cross-repo`

Expected: `[5]`

Actual: `[5]`

Result: `PASS`

Live titles:

- #5: Keep AI_Skills workflow rules separate from Bridge Kit runtime bugs

### workflow_core_area

Query: `label:maintenance-track label:area:workflow-core`

Expected: `[5, 6, 7, 8, 9, 10, 11]`

Actual: `[5, 6, 7, 8, 9, 10, 11]`

Result: `PASS`

Live titles:

- #5: Keep AI_Skills workflow rules separate from Bridge Kit runtime bugs
- #6: Real-task-driven Reviewed Handoff batches
- #7: Approval-sensitive handoff should emit one bounded kickoff before execution
- #8: 按页面语义检查子代理浏览器能力
- #9: 防止任务局部禁令变成全局规则
- #10: Post-056 acceptance artifact packaging / comparison-review fidelity
- #11: 修复 sibling worktree 授权与沙箱执行不一致
