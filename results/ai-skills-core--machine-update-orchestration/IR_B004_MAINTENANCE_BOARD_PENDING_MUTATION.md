# IR-B004 Maintenance Board Pending Mutation

Task key: `ai-skills-core--machine-update-orchestration`  
Prepared date: 2026-09-25  
Required current lifecycle: `DOING`

## Current limitation

Current `main` requires formal AI_Skills maintenance actions to use `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`.

The canonical source entry already exists:

- file: `docs/plugin-todos/ai-skills-core.md`
- heading: `AI Skills Maintainer machine update orchestration`

No matching open tracking Issue was found by exact title/task searches.

This ChatGPT Planner surface does not expose the installed Codex `Clear Writing` / `writing-style` production invocation that the Maintenance Board requires before creating or materially rewriting reader-facing Issue copy. It also has no writable GitHub Project V2 field-mutation surface.

Therefore:

`CLEAR_WRITING_UNAVAILABLE`

No Issue number is invented, no fake `tracking: #N` is written, and Project synchronization is not claimed.

## Exact pending Issue creation

The next Clear-Writing-capable AI Skills maintenance surface must:

1. re-check that no matching top-level tracking Issue now exists;
2. invoke the currently installed `Clear Writing` (`writing-style`) on the factual Issue draft below;
3. preserve all lifecycle, locator, evidence, and required-consumer facts;
4. create exactly one Issue in `YuukiAS/AI_Skills_Collection`;
5. add label `maintenance-track`;
6. bind the returned Issue number `N` to this maintenance action;
7. add exactly `tracking: #N` to the existing canonical TODO entry, without changing its source maturity/status or other substantive fields.

Suggested natural title for Clear Writing to polish without changing meaning:

`让 AI Skills Maintainer 统一同步当前机器上的 AI Research Stack`

Required Issue body facts:

```text
问题：
AI Skills Maintainer 的 machine update orchestration 已有经过独立审查的产品候选，但 formal promotion、G2 真实 Marketplace 迁移以及后续 required-consumer adaptation 仍需要一个长期 tracking Issue 统一跟踪。

当前进度：
Lifecycle = DOING。Reviewed product candidate = 4b8414733f3efc2d8707c5fbf448cbe8ec7a7d00。IR-B001 / IR-B002 / IR-B003 已关闭；当前只处理 IR-B004 control/board closure。board/docs/TODO/icon-only main drift 不触发 G1/G3/G4/G5 重跑。

当前执行锚点：
branch = reviewed/ai-skills-core--machine-update-orchestration
reviewed product candidate = 4b8414733f3efc2d8707c5fbf448cbe8ec7a7d00
evidence/handoff baseline = fb31f539058c634568401d2376ff3e64af7417bb
runbook = results/ai-skills-core--machine-update-orchestration/POST_REVIEW_PROMOTION_G2_RUNBOOK.md

下一步：
同一 Independent Reviewer 关闭 IR-B004；PASS 后从 latest main 做 overlap preflight，按 non-force approved path 集成 reviewed candidate，保留 workflow-core 0.4 与 ai-skills-core 0.5，形成 repository 5.2.0 formal closure，推进 AI_Skills release，然后执行真实 G2 Marketplace main -> release 迁移、0.5 reinstall 与 fresh-session smoke。central closure 完成后 lifecycle 进入 ADAPTING，而不是 DONE；最终 DONE 按 Maintenance Board required-consumer policy 完成。
```

Clear Writing may improve wording only. It must not change:

- lifecycle = `DOING`;
- Area = `ai-skills-core`;
- branch/candidate/evidence/runbook locators;
- next action;
- later `ADAPTING` transition;
- required-consumer truth;
- final DONE semantics.

## Canonical source backlink mutation

After the real Issue number exists, modify only the existing TODO entry:

`docs/plugin-todos/ai-skills-core.md -> ### AI Skills Maintainer machine update orchestration`

Add:

`tracking: #N`

Do not change `status: PROMOTED`, source, evidence, target layer, problem, current behavior, boundary, or any other substantive field in this locator-only edit.

## Exact pending Project mutation

Project:

- owner: `YuukiAS`
- title: `AI Skills Maintenance`
- Project id: `PVT_kwHOA0Lgf84BkjCU`

After Issue `#N` auto-adds through `maintenance-track`:

- Status = `DOING`
- Area = `ai-skills-core`
- Resolution commit = blank/unset
- current anchor = reviewed branch + product candidate `4b8414733f3efc2d8707c5fbf448cbe8ec7a7d00` + current task docs/evidence tip
- next action = same Independent Reviewer closure -> formal promotion + G2
- keep Issue open

Known field ids from canonical Project readback:

- Project = `PVT_kwHOA0Lgf84BkjCU`
- Status field = `PVTSSF_lAHOA0Lgf84BkjCUzhjTPss`
- DOING option = `5bc96327`
- Area field = `PVTSSF_lAHOA0Lgf84BkjCUzhjTQOI`
- Resolution commit field = `PVTF_lAHOA0Lgf84BkjCUzhjTQOw`

Resolve the live `ai-skills-core` Area option id before mutation; do not guess it.

## Later lifecycle

After canonical integration + formal 5.2.0 release + real G2 central closure:

- record exact central Resolution commit;
- set Project Status `DOING -> ADAPTING`;
- freeze exact current identities/locators for required consumers under then-current authorized access;
- keep the tracking Issue open.

Final DONE requires all required consumers PASS/N/A with durable evidence plus the final Resolution commit and issue-close lifecycle rule.

Do not ask the user to drag cards or manually add `tracking: #N`.
