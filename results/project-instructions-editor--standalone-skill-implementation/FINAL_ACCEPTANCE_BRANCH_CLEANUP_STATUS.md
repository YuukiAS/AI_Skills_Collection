# PIE 0.1 Final Acceptance And Branch Cleanup Status

Date: 2026-10-07

Current branch: `work/project-instructions-editor--0.1-closure`

Closure branch start:
`a9de50f384922105ce3903576046c473539da28e`

Origin main start for final integration:
`c1a7740768ea13d717323e348cd0fcdeec27961d`

## PIE 0.1 State

- PIE v0.1 source, README, icon, registry, catalog, provenance, and tests are
  ready for main integration.
- The accepted runtime subtree is the exact historical runtime source from
  `6c098ce07d9a01e2d2e353841443d2f13a943dc6`.
- The closure integration keeps repository `VERSION=5.4.4` because this task
  does not advance the `release` ref.
- `CHANGELOG.md` records Project Instructions Editor v0.1 under `Unreleased`
  with `MINOR_FOR_NEXT_FORMAL_RELEASE`.
- Server+VPS Web acceptance has passed through explicit invocation of the live
  wrapper.
- Main integration is authorized; release ref mutation is not authorized.

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

The package contains only the standalone PIE Skill payload. The live ChatGPT Web
wrapper was updated separately and read back as exact runtime source.

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
reviewed/repo--maintenance-board-issue-maturity
reviewed/presentations--stage1-front-door-two-template-foundation
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
- Issue #93 is ready for resolution after final main integration records the
  resolution commit. Issue #13 remains open for future Clear Writing /
  reader-layer work.

## Server+VPS Acceptance

Final ChatGPT Web Server+VPS acceptance has passed.

```text
PIE_0_1_EXPLICIT_WEB_ACCEPTANCE=PASS
LIVE_WRAPPER_VERSION=0.2.7
```

The accepted contract is explicit invocation when the user needs PIE. Automatic
implicit invocation is not a PIE v0.1 release gate.

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
