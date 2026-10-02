# workflow-core 0.5 execution Kickoff Draft v0.2

仅在 execution-ready Critic 对 Proposal V0.4 + Plan v0.2 + Goal v0.2 + 本 Kickoff 同版 PASS 后发送给 Codex。

我批准执行 `workflow-core--normal-entry-reliability` 的已审 package：

- Proposal：`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md`
- Plan：`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_2_2026-10-01.md`
- Goal：`docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_2_2026-10-01.md`
- repo：`YuukiAS/AI_Skills_Collection`
- canonical checkout：`/home/yuukias/AI_Skills_Collection`

我授权以下 bounded execution：

1. Stage A exact Reviewed task：
   - task `workflow-core--normal-entry-reliability`
   - branch `reviewed/workflow-core--normal-entry-reliability`
   - worktree `/home/yuukias/AI_Skills_Collection-workflow-core--normal-entry-reliability`
   - brand-new bootstrap前使用 `git fetch --all --prune` 并绑定 post-sync `origin/main` OID；
   - 使用 Bridge canonical bootstrap/publish-first；
   - 运行 zero-paid implementation、tests、candidate replay、CI和development smoke。

2. Stage A只有在 Reviewed Reviewer PASS 后交给 AI Research Stack Critic做只读 pre-final review。Critic PASS 时，不改 Stage A CURRENT、不集成 main；允许继续 Stage B。Critic REVISE 时停止回 Planner。

3. Stage B仅在 Stage A Reviewed Reviewer PASS + pre-final Critic PASS 后：
   - 从 exact Stage A approved tip创建并切换 exact branch  
     `reviewed/workflow-core--normal-entry-reliability-release`；
   - 继续使用同一 exact worktree；
   - 初始化 exact task `workflow-core--normal-entry-reliability-release`；
   - 首个metadata commit机械绑定 REQUEST的 exact reviewed-worktree locator；
   - 使用 Bridge `task init` / `publish-first` 与当前合法 Reviewed states继续；
   - 不创建第二 worktree、不回落到 `/tmp`/second clone。

4. 两个 Stage 的 Planner transaction必须使用 canonical `automation/reviewed_handoff/prompts/PLANNER.md`，并在 Bridge PLAN中写：
   - `Maintenance companion: ai-skills-core`
   - `Domain owner: workflow-core`

5. `ci_required=true` 后，真实 GitHub CI由 Reviewed Handoff Reviewer读取并拥有 transaction。若没有已验证的 exact task-bound Scheduled Reviewer，就使用独立人工 Reviewer thread读取 `automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md`；不得让 Critic或Executor代写 Reviewer decision，generic watcher也不得冒充 task-bound automation。

6. Stage B内只有 0.4 qualification G1–G5全部 PASS后，才授权 workflow-core exactly-once `0.4 -> 0.5` 与 repository届时真实版本的下一 PATCH metadata；随后 final candidate必须重新完整通过G1–G5、真实CI和Reviewed Reviewer。

7. Stage B Reviewed Reviewer PASS 后再由 AI Research Stack Critic做只读 final review。只有 final Critic PASS 后，才授权：
   - exact final candidate integration到 canonical AI_Skills `main`；
   - ordinary non-force publication；
   - approved repository PATCH formal release；
   - 当前 canonical contract要求时 fast-forward-only `release` ref closure；
   - exact workflow-core production identity / install-update smoke。

8. 若 Stage B PASS human gate需要机械记录 ACCEPT，则只有在 Stage B Reviewed Reviewer PASS + AI Research Stack final Critic PASS均成立时，授权对 exact Stage B task记录一次 `human record --decision ACCEPT`，不得泛化到其他 task或REJECT route。

明确不授权：

- paid API；
- force push / destructive Git；
- Stage A或Stage B reviewed branch deletion；
- reviewed worktree remove/prune；
- arbitrary cleanup；
- 其他 branch/worktree；
- Bridge/Host Policy修改；
- Longleaf/STAT5060/render-specialist mutation；
- consumer-machine adaptation；
- stable tag创建/移动；
- architecture/G1–G5/scope expansion。

正式 product/release closure可以在 reviewed branches 与 worktree保留的情况下完成。以后若要 cleanup，另行取得 bounded authorization。

先读取 approved package、当前 AI_Skills AGENTS 和 Bridge规则，再执行 Goal。若任何 role/state/locator/authority 与 package不一致，停止回 Planner；不得 fallback或临场重设计。
