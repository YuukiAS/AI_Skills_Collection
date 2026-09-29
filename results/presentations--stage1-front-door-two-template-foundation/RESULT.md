---
schema: PRESENTATIONS_STAGE1_EXECUTOR_RESULT_V1
task_key: presentations--stage1-front-door-two-template-foundation
status: A_PHASE_PARTIAL_COMPLETE_WAITING_FOR_CANONICAL_COURSE_STANDARD
---

# Executor Result — Presentations Stage 1 A-Phase

This is not a final Stage 1 PASS, not final G1, and not final G5.

The revised Plan v2 / `plan_revision=1` split the task into:

- A. `CONTINUE_NOW`;
- B. `WAIT_FOR_CANONICAL_COURSE_STANDARD`;
- C. final integration after the independent standard-Beamer task supplies the
  exact canonical course-standard source path, commit, and consumption boundary.

## Completed Now

Implemented and validated A-phase work that does not require owning the final
canonical `course-standard` template body:

- unified Stage 1 front-door routing helper;
- research / teaching / business / editable / local-edit / locked-template /
  plan-only routing infrastructure;
- exactly-two-template identity manifest with unresolved `course-standard`
  source status;
- Marketplace Presentations interface/default prompt routing update;
- source/generated parity through the canonical Marketplace generator;
- `render-chinese-math-pdf` owner-consumption helper for Presentations;
- CUHK generator integration with render-owner-resolved command/resource
  identity;
- CUHK adapter manifest recording `render-chinese-math-pdf` as owner;
- typed `blocked_missing_dependency` helper path;
- unexpected font fallback rejection helper path;
- validator compatibility with the new render-owner probe schema;
- G5 private-review metadata/bundle plumbing that remains `final_g5_ready=false`
  until canonical course-standard source identity is supplied.
- `presentation-desktop` profile description alignment with the Stage 1 front
  door, pending course-standard teaching identity, editable route preservation,
  portable rendering, and visual QA.
- tightened CUHK adapter command discovery so Beamer compile/render commands
  come only from the `render-chinese-math-pdf` probe receipt; Presentations no
  longer falls back to its own `PATH` discovery for formal adapter command
  paths.
- explicit non-branded `beamer` / `tex` output routing now goes through the
  `course-standard` adapter identity while preserving stronger research context
  precedence for `cuhk-research`.
- explicit editable output values now normalize common extension/style spelling
  such as `.pptx` and `google-slides` so the front door preserves the official
  editable surface for explicit PPTX/Slides requests.
- research skill guidance now scopes CUHK defaulting to the Stage 1
  academic/research route only, leaving teaching/courseware to the
  `course-standard` identity and business/company/client work to editable
  PPTX/Slides.
- plan-only routing now takes precedence over existing-deck and external
  locked-template detection when the user explicitly asks for storyline/plan
  only and no generated artifact.
- shared routing documentation and generated Presentations payload now state
  that same plan-only precedence explicitly.
- explicit `plan` / `plan-only` / `deck-plan` output requests now also preserve plan-only
  precedence over `existing_deck=True` and `locked_template=True` caller hints.
- explicit output normalization now treats snake_case values such as
  `google_slides` and `plan_only` the same as their hyphen/space equivalents.
- explicit ratio parsing now recognizes common `16x9`, `16×9`, `16/9`,
  `4x3`, `4×3`, and `4/3` spellings without changing template identity.
- Beamer adapter manifests now record both render-owner `resolved_route` and
  `resolved_profile` identity for CUHK and pending course-standard adapters,
  while still declaring no Presentations-owned discovery route.
- Prompt text such as `LaTeX slides` and `Beamer slides` no longer gets
  misrouted to editable output merely because it contains the word `slides`;
  `google slides` and explicit editable output still route to the official
  editable surface.

No `skills/tools/documents-media/presentations/shared/templates/course-standard`
template body was created or restored.

## Deferred Dependency

Remaining dependency:

```text
WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE
```

Only the items listed in the revised Plan's
`WAIT_FOR_CANONICAL_COURSE_STANDARD` / `FINAL_INTEGRATION` sections remain
deferred, including:

- exact canonical course-standard source path;
- exact candidate commit;
- allowed consumption boundary;
- final course-standard 4:3 / 16:9 source integration;
- course-standard template-specific compile/render/fidelity;
- final two-adapter RP-G1/RP-G5;
- full G1 and full G5 private visual evidence bundle.

## Validation

Passed:

```text
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_presentations
python scripts/skills.py validate
git diff --check
RP-G2 forbidden-path scan over source + generated Presentations payload
course-standard template directory absence check
```

Note: `python -m unittest tests.test_presentations` must be run with write
access to the task worktree because an existing test regenerates
`docs/audits/research_presentation_gold_composition_library/runtime_probe_traces.json`.
The same command passes when run with that normal write access.

Reviewed Handoff repository-wide validation was run and failed only on
pre-existing unrelated historical task metadata:

```text
ai-bridge reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation
```

Observed failures were legacy task-key shape errors for older tasks and an
unrelated `web-development--frontend-design-production-consolidation` RESULT
frontmatter issue. No current task-specific error was reported.

Repository bump decision: NONE

Reason: this is an incomplete A-phase checkpoint, not a production release.

Affected plugins:

- presentations: NO_BUMP
  Reason: final Stage 1 G1/G5/CI/Reviewer gates are still pending on canonical
  `course-standard` integration.
