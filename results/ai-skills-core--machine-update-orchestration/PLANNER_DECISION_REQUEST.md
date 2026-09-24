# Planner Decision Request - AI Skills Maintainer Machine Update Orchestration

Task key: `ai-skills-core--machine-update-orchestration`  
Status: `WAITING_FOR_PLANNER_DECISION`  
Date: 2026-09-24

This request records the remaining decisions needed before Executor can truthfully claim the V2.1 goal complete. The implementation candidate is source-complete and deterministic-validation-complete, but release-critical G1-G5 evidence is still incomplete.

## Current Candidate

- AI_Skills task branch: `reviewed/ai-skills-core--machine-update-orchestration`
- Verified remote task tip before this request: `92f974fc56e366a1f6091f699e30f27764608a45`
- `origin/main`: `7b76e94ad29cf3bd8547026b942553068754d51f`
- AI_Skills `release`: `7b76e94ad29cf3bd8547026b942553068754d51f`
- Bridge `origin/main` locator commit: `dfe093c6f78cdadb22905e811935a772af5cb034`
- Bridge `release`: `d27259d6706dee951dc0c0ede8c9b03c65f55ca3`
- Implementation evidence: `results/ai-skills-core--machine-update-orchestration/IMPLEMENTATION_EVIDENCE.md`
- Completion audit: `results/ai-skills-core--machine-update-orchestration/COMPLETION_AUDIT.md`

## Completed Executor Work

- Added internal `machine-update-orchestrator` and `bridge-kit-maintainer` skills inside `ai-skills-core`.
- Added Route A/B/C references, the formal `release` / `### Update impact` contract, legacy Marketplace bootstrap rules, Bridge release-channel delegation, managed-consumer adaptation boundaries and Human Gate/failure-recovery rules.
- Updated Maintainer and project installer routing boundaries.
- Updated source config, generated plugin payload, profile, README, root/plugin changelogs, TODO and tests.
- Committed and pushed the mandatory Bridge `AGENTS.md` owner locator only.
- Created and verified the existing formal `release` refs:
  - AI_Skills at `7b76e94ad29cf3bd8547026b942553068754d51f`
  - Bridge at `d27259d6706dee951dc0c0ede8c9b03c65f55ca3`
- Ran deterministic validation:
  - `python scripts/skills.py registry --write`
  - `python scripts/skills.py validate`
  - `python scripts/skills.py audit --all`
  - `python scripts/skills.py catalog --write`
  - `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
  - targeted Maintainer tests
  - `python -m unittest discover -s tests`

## Decision D1 - Fresh Normal-Entry Evidence Under `No paid API`

V2.1 requires fresh-session normal-entry evidence for requests such as `update AI Skills`, `update Bridge Kit` and `sync this machine`. The available candidate replay path launches a fresh Codex child. Host safety review rejected that replay because it could trigger an external model or paid request, and the task explicitly says `No paid API`.

Planner/Reviewer needs to choose one:

1. Authorize a specific no-paid fresh-runtime harness that can load the candidate production plugin and exercise normal-entry routing without model/API spend.
2. Change the user authorization to permit the bounded paid/fresh Codex replay needed for G1/G3.
3. Revise the evidence requirement for this no-paid environment and explicitly accept source/tests plus static plugin payload inspection as degraded evidence.

Executor must not claim G1/G3 PASS from source tests alone without this decision.

## Decision D2 - Capability-Bearing `release` for G2

The real legacy Marketplace is currently configured from AI_Skills `main`, and installed `ai-skills-core` is `0.4`. The current AI_Skills `release` ref also points to repository `5.1.0` with `ai-skills-core 0.4`, not the capability-bearing `0.5` candidate.

If Executor migrates Marketplace `main -> release` now, the result would still install `0.4` and would not satisfy G2.

Planner/Reviewer needs to choose one:

1. Review/integrate the task branch, then advance formal `release` through the approved release path before running G2.
2. Define an explicit release-candidate Marketplace/ref path that may temporarily install this candidate for G2 without misrepresenting formal release state.
3. Keep G2 waiting and mark the current state as source-complete but not release-ready.

Executor must not move AI_Skills `release` to an unreviewed task branch or migrate the user's Marketplace to a non-capability-bearing `release` merely to produce activity.

## Decision D3 - Real G4/G5 Fixture Execution

G4/G5 currently have source contracts and tests, but not release-critical real fixture execution tied to the final candidate. The remaining proof needs managed-consumer, unmanaged-conflict, dirty-overlap Human Gate and failure-restoration behavior without mutating unowned project text.

Planner/Reviewer needs to choose one:

1. Provide or authorize task-owned fixture repositories for managed-consumer and failure-injection execution.
2. Authorize Executor to create local temporary fixture repositories with exact mutation boundaries.
3. Revise G4/G5 evidence requirements for this release and explicitly label them as contract-tested only.

Executor must not mutate unrelated real project repositories or unowned AGENTS/rule text to satisfy these gates.

## Do Not Do Without A Fresh Decision

- Do not report G1-G5 PASS from deterministic tests only.
- Do not perform the real Marketplace migration while AI_Skills `release` still contains `ai-skills-core 0.4`.
- Do not run a fresh child Codex/model replay under the current `No paid API` boundary.
- Do not advance AI_Skills `release` to this task branch without a formal review/release decision.
- Do not modify Bridge runtime/source, Bridge README/QUICKSTART/CHANGELOG, or any Bridge file other than the already committed locator.
- Do not auto-edit unowned project text to fabricate managed-consumer evidence.

## Recommended Next Action

Planner/Reviewer should decide D1-D3 before more Executor work. Until then, the correct task state is:

`WAITING_FOR_PLANNER_DECISION`: source-complete, deterministic-validation-complete, not G1-G5 complete, not release-ready.
