# 059 Research Authoring G4-C1 Consumer Repair — Execution-Ready Critic Review v0.1

Date: 2026-10-06  
Role: independent Critic  
Review stage: EXECUTION_READY_REVIEW  
Task: `research-authoring--formal-production-authoring`

## Result

```text
RESULT=PASS
READY_FOR_CODEX=YES
```

This PASS approves only the bounded C2 consumer-repair implementation package. It does not approve any C2 final Gate, live Plugin update, G4 ChatGPT rerun, Codex final PDF production, paid API call, main merge, or formal release.

## Reviewed package

Repair authority:

`results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_V2_CRITIC_REVIEW.md`  
commit: `8aa5a2b9bdac737254e6e8527e57ff1750154b09`

Plan:

`docs/design/059_RESEARCH_AUTHORING_G4_C1_CONSUMER_REPAIR_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md`  
commit: `d60c039e294fbbf6afc9a7aff9edbba76d45e349`

Goal:

`docs/goals/059_RESEARCH_AUTHORING_G4_C1_CONSUMER_REPAIR_GOAL_V0_1.md`  
commit: `bb4d03c20d48ea1d1ecdafdd0bee9d19d3d3c2c4`

Kickoff:

`docs/operations/prompts/059_RESEARCH_AUTHORING_G4_C1_CONSUMER_REPAIR_KICKOFF_V0_1.md`  
commit: `f85ed54ec75cc9e987915de208d4b231949928ab`

Package index:

`results/research-authoring--formal-production-authoring/G4_C1_CONSUMER_REPAIR_EXECUTION_PACKAGE_V0_1.md`  
commit: `35c61b6cfdcb30db1bfc8985ad324efb6d6b9eb1`

All four package objects were re-read at the execution branch and at their declared commits. Their current file contents match the declared versions byte-for-byte. Before this review the execution branch tip was exactly the package commit `35c61b6cfdcb30db1bfc8985ad324efb6d6b9eb1`.

The diff from the attribution Critic PASS commit to the package commit contains only the Plan, Goal, Kickoff, and package-index documents. No candidate-owned production source was changed before execution authorization.

## Current policy / branch context

Latest AI_Skills_Collection main checked during review:

`5827c340d4caac37d8256d639acfad8d9fbd9bfc`

Latest Bridge Kit main checked during review:

`9d60f4cf949c9da327a154001b13881cfd91233b`

The package correctly reuses the already-authorized task identity:

- branch: `work/research-authoring--formal-production-authoring`
- worktree: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

No successor task/branch, watcher, daemon, database, state machine, or Reviewed-Handoff automation is required.

The Kickoff binds the exact existing branch/worktree and authorizes task-owned ordinary non-force publication only after the user actually sends the approved Kickoff. This is compatible with the current repository/Bridge publication contract; the Executor must still follow the current Host/Bridge normal publication route rather than broaden a failed bounded route into a force/destructive/raw fallback.

## Repair scope

The implementation package faithfully implements the approved v2 attribution.

The only production behavior source that may change is:

`scripts/codex_marketplace_config.json`

and only:

`research-writing -> report -> workflow_notes`

The planned rule is normal-product behavior, not a G4-only test blacklist. It applies whenever the standalone/skills-only Research Authoring report surface lacks the approved renderer companion.

It correctly operationalizes that the ChatGPT-side Research Authoring stage stops after:

`stable scientific source + complete downstream production handoff`

and that renderer mechanics include preview/QA/local compile, XeLaTeX/latexmk/Pandoc-to-PDF, PDF creation/open/render, page raster/visual inspection, and PDF-derived text/font/page QA. Generic runtime/file/compute capability is not a substitute renderer.

Markdown/LaTeX source authoring, source-only semantic/fidelity QA, and the full downstream handoff remain allowed.

The package correctly keeps canonical `research-authoring-core` and `research-reporting` source at ZERO WRITE initially. Those sources already contain the owner boundary; duplicating the command-level rule there is not justified by current evidence.

If implementation shows that the aggregate cannot express the rule or that the normal runtime does not consume the aggregate, the Executor must stop and return to Planner/Critic.

## Tests and development replay

The proposed focused changes to `tests/test_research_writing_routing.py` are appropriate deterministic contract regression. They verify the generated entry contract and should-not-change routing, but the package explicitly does not treat those string/contract checks as final capability evidence.

The known G4-C1 development replay is also correctly positioned before C2 freeze:

- standalone candidate only;
- renderer companion absent;
- ordinary formal-PDF report request;
- no test-specific “do not XeLaTeX/pdftotext” blacklist;
- candidate/aggregate consumption must be evidenced;
- source + downstream handoff is allowed;
- PDF/compile/render/PDF-derived QA must not occur.

If the repaired aggregate is consumed but the runtime still renders, or if the aggregate is not consumed, the package correctly stops instead of tuning the replay prompt until it passes.

## Generated authority

The package follows the repository authority model:

`source config -> canonical generator -> generated parity`

It forbids direct edits to `plugins/codex/plugins/**` and `.agents/plugins/marketplace.json`.

Only generated files truthfully changed by the current generator may remain in the candidate diff. No extra registry/catalog/provenance churn is required.

## Candidate/version/docs decision

The repair changes production-consumed normal-entry behavior, so a new exact candidate C2 is required.

However, `research-writing 0.3` has not been formally released. This is a repair inside the same approved 0.3 improvement batch, so:

- canonical plugin candidate remains `research-writing 0.3`;
- no `0.4` bump is justified;
- repository `VERSION` remains unchanged;
- maturity remains `unclassified`.

The existing README and candidate changelog already state the intended renderer ownership/fail-closed behavior. Therefore “README checked: no update required” and “plugin changelog checked: no update required” are valid defaults for this bounded repair. If implementation discovers a direct factual conflict, it must stop rather than silently expand docs scope.

The future ChatGPT distribution wrapper may use the next semver patch (currently expected `0.3.1`) when C2 is later prepared for live update. That distribution version is separate from the two-part canonical `research-writing 0.3` version.

## C2 stop and final-evidence invalidation

The Executor must stop after bounded repair, deterministic regression, development replay, and exact C2 commit/push.

Required first stop:

```text
BOUNDED_REPAIR_IMPLEMENTED=YES
C2_CANDIDATE_READY=YES
FINAL_CANDIDATE_COMMIT=<C2>
DEVELOPMENT_G4_C1_REGRESSION=PASS
FINAL_GATES_NOT_STARTED=YES
FINAL_TASKS_NEED_PLANNER_FREEZE=YES
NEXT_HANDOFF=PLANNER
```

It may not choose new final holdouts itself.

Planner then freezes the new C2 final packet and sends C2 + the packet to independent pre-final Critic before any final Gate starts.

Once C2 exists, previous C final Gate records remain historical truth about C but cannot be stitched into a C2 release PASS:

- G1 must run directly on C2;
- old DII G2 becomes development/regression evidence; C2 gets a newly frozen fresh report task/delta;
- old MoSAIC G3 becomes regression/should-not-change evidence; C2 must establish direct final G3 evidence under the unchanged G3 contract;
- G4 fully restarts from the C2 live wrapper after separately authorized Plugin update;
- the first failed G4 package remains immutable FAIL and contributes no PASS subfinding.

This follows the current same-final-candidate policy and the already-approved v2 Critic ruling.

## Authorization boundary

The approved Kickoff authorizes, only when the user actually sends it:

- exact existing task/branch/worktree;
- the bounded report-aggregate source change;
- focused tests;
- canonical generation/parity;
- deterministic validation;
- repo-safe G4-C1 development replay;
- exact C2 candidate commit;
- task-owned ordinary non-force push;
- task-local results/private exports;
- offline C2 wrapper preparation;
- stop at C2 -> Planner.

It does not authorize:

- Plugin Creator live update;
- new final G1-G4 execution;
- new G4 ChatGPT run;
- Codex final PDF;
- paid API;
- main merge/release/tag;
- private/sensitive external upload;
- canonical core/report source expansion;
- other plugin/domain changes;
- force/destructive Git;
- watcher/daemon/database/ledger/state machine.

## Approved bindings

```text
APPROVED_REPAIR_AUTHORITY=results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_V2_CRITIC_REVIEW.md

APPROVED_PLAN_PATH=docs/design/059_RESEARCH_AUTHORING_G4_C1_CONSUMER_REPAIR_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md
APPROVED_PLAN_COMMIT=d60c039e294fbbf6afc9a7aff9edbba76d45e349

APPROVED_GOAL_PATH=docs/goals/059_RESEARCH_AUTHORING_G4_C1_CONSUMER_REPAIR_GOAL_V0_1.md
APPROVED_GOAL_COMMIT=bb4d03c20d48ea1d1ecdafdd0bee9d19d3d3c2c4

APPROVED_KICKOFF_PATH=docs/operations/prompts/059_RESEARCH_AUTHORING_G4_C1_CONSUMER_REPAIR_KICKOFF_V0_1.md
APPROVED_KICKOFF_COMMIT=f85ed54ec75cc9e987915de208d4b231949928ab

APPROVED_PACKAGE_PATH=results/research-authoring--formal-production-authoring/G4_C1_CONSUMER_REPAIR_EXECUTION_PACKAGE_V0_1.md
APPROVED_PACKAGE_COMMIT=35c61b6cfdcb30db1bfc8985ad324efb6d6b9eb1

READY_FOR_CODEX=YES
```
