# PIE 0.1 Final Acceptance And Branch Cleanup Status

Date: 2026-10-07

Current branch: `work/project-instructions-editor--0.1-closure`

Current local integration head after merging latest `origin/main`:
`c4f3a7b9880ba7974352fc30a99d216c741a4664`

## PIE 0.1 State

- PIE v0.1 source, README, icon, registry, catalog, provenance, contact sheet,
  tests, `VERSION=5.5.0`, and `CHANGELOG.md` are present on the closure branch.
- The closure branch has absorbed latest `origin/main` so current Research
  Authoring work is preserved.
- Server+VPS Web acceptance has not yet been run against an updated Web wrapper.
- Main/release are not claimed to contain a completed PIE 0.1 release.

## Wrapper Update Package

Archive:

```text
private/exports/project-instructions-editor--0.1-closure/project-instructions-editor-v0.1-wrapper-update.zip
```

SHA-256:

```text
b0f37935187a9f54dc0389598e3b6aa37d312ef4ab7a63120d6febd37614b8ea
```

Manifest:

```text
private/exports/project-instructions-editor--0.1-closure/project-instructions-editor-v0.1-wrapper-update.MANIFEST.json
```

Manifest SHA-256:

```text
edcad6c2aec6d61892f8a2532bea6977ebb36dd00041e5a6d8274d95f3f5b8e4
```

The package contains only the standalone PIE Skill payload. It does not update
the live ChatGPT Web wrapper by itself.

## Branch Cleanup Disposition

Deleted remote branches already confirmed as `origin/main` ancestors:

```text
reviewed/hpc--slurm-race-policy-bounded-opt-in
reviewed/hpc--slurm-workflows-routing-refactor
reviewed/product-ui-copy--cross-plugin-production-integration
reviewed/repo--maintenance-board-lifecycle
reviewed/science-communication--project-thread-handoff-recovery-integration
work/workflow-core--normal-entry-reliability
```

Deleted remote branches after preserving or confirming durable closure evidence:

```text
planner/reader-layer-finalization-v0.1
reviewed/ai-skills-core--machine-update-orchestration
reviewed/science-communication--project-thread-handoff
reviewed/science-communication--project-thread-handoff-recovery
reviewed/workflow-core--first-remote-publication-gate
reviewed/workflow-core--first-remote-publication-repair-gate
work/presentations-validator-v1
work/project-instructions-editor--standalone-skill-implementation
```

Evidence preserved from deleted branches:

```text
results/ai-skills-core--machine-update-orchestration/FINAL_ADAPTATION_CLOSURE.md
results/ai-skills-core--machine-update-orchestration/FINAL_ADAPTATION_CLOSURE.json
results/ai-skills-core--machine-update-orchestration/ADAPTING_CONSUMER_STATUS.md

docs/implementation/presentations-validator-v1/IMPLEMENTATION_CANDIDATE.md
docs/implementation/presentations-validator-v1/AUDITOR1_FINDINGS.md
docs/implementation/presentations-validator-v1/AUDITOR2_FINDINGS.md
docs/implementation/presentations-validator-v1/AUDITOR3_FINDINGS.md

results/project-instructions-editor--standalone-skill-implementation/C5_REAL_USER_ACCEPTANCE_CRITIC_REVIEW.md
results/project-instructions-editor--standalone-skill-implementation/C7_G4_REPLAY_CRITIC_REVIEW.md
results/project-instructions-editor--standalone-skill-implementation/C9_FINAL_GATE_CRITIC_REVIEW.md
results/project-instructions-editor--standalone-skill-implementation/C10_IMPLEMENTATION_CRITIC_REVIEW.md
results/project-instructions-editor--standalone-skill-implementation/c10_b3_stage_separation_probe/PROBE_RESULT.md
results/project-instructions-editor--standalone-skill-implementation/C11_SIMPLE_FORMAL_CORE_CLOSURE.md
results/project-instructions-editor--standalone-skill-implementation/C11_READER_BASELINE_GATE_CRITIC_REVIEW.md
```

Additional stale branch disposition:

```text
reviewed/repo--maintenance-board-issue-maturity
```

`origin/main` already contains the later v7 final closure result:
`V7_ISSUE_MATURITY = COMPLETE`, `DUPLICATE_FALSE_DONE = FIXED`, and
`METADATA_AUDIT = PASS`. The old branch tip is an intermediate blocker state
and is superseded by main.

```text
reviewed/presentations--stage1-front-door-two-template-foundation
```

This branch is not a final accepted production release. Its deleted remote tip
was `66762e83`. It records an A-phase checkpoint with
`WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE`, explicitly does not claim
final Stage 1 PASS, final G1, final G5, CI completion, or Reviewer approval.
The cleanup decision preserves that disposition here rather than integrating
the branch's incomplete production source:

```text
status = A_PHASE_PARTIAL_COMPLETE_WAITING_FOR_CANONICAL_COURSE_STANDARD
repository bump = NONE
presentations bump = NO_BUMP
remaining dependency = WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE
```

Remote branches intentionally preserved for active work:

```text
work/project-instructions-editor--0.1-closure
work/research-authoring--formal-production-authoring
work/research-authoring--student-facing-authority-todo
work/research-authoring--table-wrap-readability-todo
```

`work/research-authoring--student-facing-authority-todo` and
`work/research-authoring--table-wrap-readability-todo` each contain unmerged
`docs/plugin-todos/research-writing.md` entries, so they are not stale
main-ancestor branches.

## PR / Issue Tracking

- PR #100 was closed without merge, and branch
  `planner/reader-layer-finalization-v0.1` was deleted.
- Issue #13 remains open for future Clear Writing reader-layer work.
- Issue #93 remains open until the Web wrapper is updated and fresh Server+VPS
  non-reader acceptance passes.

## Server+VPS Acceptance

Final ChatGPT Web Server+VPS acceptance is still pending because this Codex
environment cannot mutate the live ChatGPT Web wrapper or open the private
Server+VPS Project thread. The only remaining user action is to update the
existing `project-instructions-editor` Web wrapper from the package above, then
run one fresh-thread non-reader acceptance using PIE 0.1 scope.

Reader-layer natural Chinese continuity is out of scope for PIE 0.1 acceptance.
C11 reader-layer failure remains historical failure evidence and is not
reclassified as PASS.

## Validation Snapshot

Passed after latest main merge:

```text
python -m unittest tests.test_project_instructions_editor_contract
python -m unittest tests.test_standalone_skill_baselines
```

Known unrelated generated drift remains:

```text
python scripts/build_codex_marketplace.py --validate --check --path-report
```

Current result:

```text
publication layer is not current (13 differences)
```

The reported differences are confined to current Research Authoring /
Presentations generated payload state and are not fixed in the PIE cleanup.

C11 reader-layer failure preserved; not reclassified as PASS.
