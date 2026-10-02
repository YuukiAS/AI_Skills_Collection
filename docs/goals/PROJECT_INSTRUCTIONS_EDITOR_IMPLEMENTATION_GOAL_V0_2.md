# Project Instructions Editor — Implementation Goal v0.2

Status: DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW  
Task key: `project-instructions-editor--standalone-skill-implementation`  
Implementation Plan: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md`  
Supersedes: `docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_1.md`

## Goal

Implement and validate the frozen standalone Skill `project-instructions-editor` without redesigning the approved product contract.

The Executor must deliver one exact final candidate commit `C` that:

1. exists at `skills/core/codex-system/project-instructions-editor/`;
2. naturally triggers for long-lived ChatGPT Project-instruction editing requests;
3. preserves the frozen near-miss ownership boundaries;
4. implements preservation-sensitive / greenfield / explicit-reset modes;
5. handles live setting, targeted history, canonical sources, character budget, missing-input degradation, semantic ownership/effective enforcement, locator safety, protected absence, bounded/full edit and no-op;
6. produces proportional user-facing edits/candidates rather than audit-heavy output;
7. passes G1, G2 and G3 on the same exact candidate `C`;
8. produces a complete G4 packet from `C` for independent qualitative review;
9. is source/generated/provenance/install/version/README/changelog consistent as a standalone Skill release candidate;
10. is packaged from `C` for independent review;
11. stops before `main` merge or formal release publication.

The independent Reviewer, not the Executor, owns G4 qualitative PASS/REVISE and implementation overall PASS/REVISE.

## Frozen product authority

Do not redesign:

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DESIGN_FREEZE_CLOSURE_2026-10-02.md`

If implementation evidence contradicts these contracts, return to Planner/Critic.

## Exact implementation identity

```text
repository = YuukiAS/AI_Skills_Collection
task_key = project-instructions-editor--standalone-skill-implementation
branch = work/project-instructions-editor--standalone-skill-implementation
worktree = ../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation
```

## Required source

Create:

```text
skills/core/codex-system/project-instructions-editor/SKILL.md
skills/core/codex-system/project-instructions-editor/agents/openai.yaml
skills/core/codex-system/project-instructions-editor/references/editor-contract.md
skills/core/codex-system/project-instructions-editor/evals/trigger_queries.json
skills/core/codex-system/project-instructions-editor/assets/app-facing.svg
tests/test_project_instructions_editor_contract.py
```

Update:

```text
tests/test_standalone_skill_baselines.py
```

Only add the smallest public-safe fixture if focused tests truly require it.

Do not add runtime scripts unless a new Planner/Critic decision explicitly changes the frozen instruction/reference-only capability.

## Required metadata

Standalone version starts at `0.1`.

```text
provenance = user-authored
trusted = false
requires_network = false
writes_files = false
executes_code = false
secrets_needed = []
recommended_scope = global
```

Natural invocation must be allowed. Static trigger metadata alone is never Gate PASS.

## Positive completion

Executor positive completion is not “all four Gates PASS”.

Executor positive completion requires:

```text
FINAL_CANDIDATE_COMMIT=C
G1=PASS
G2=PASS
G3=PASS
G4_READY_FOR_INDEPENDENT_REVIEW=YES
EVIDENCE_HEAD=E
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

with:

- G1–G3 produced from exact candidate `C`;
- a complete representative G4 input/source/output packet produced from `C`;
- portable package produced from `C`;
- `C..E` containing only allowed evidence/result/review-handoff paths;
- all candidate-owned content unchanged after `C`.

The Executor must not claim:

```text
G4=PASS
IMPLEMENTATION_OVERALL=PASS
RELEASED
PRODUCTION_READY
5.5.0_PUBLISHED
```

The independent Reviewer owns G4 qualitative judgment and implementation overall judgment.

Tests, CI, file existence, package validation, character counts, diff output and route receipts are evidence, not product completion authority.

## Non-substitutable semantics

Do not replace or weaken:

- bounded edit as default;
- preservation-sensitive / greenfield / explicit-reset;
- live-baseline requirement for preservation-sensitive full replacement;
- targeted history rather than exhaustive history;
- protected absence;
- semantic ownership versus effective enforcement;
- Project-resident bridge when lookup-before-action semantics require it;
- no-op as a valid result;
- missing-input honest degradation;
- exact identifier protection;
- authorization/safety/evidence-strength preservation;
- natural normal entry and frozen near-miss owners;
- full-output qualitative review by an independent Reviewer.

Do not substitute blacklist/rule-count/English-ratio/keyword scoring for semantic judgment.

## Candidate-owned content

Before candidate commit `C`, complete and stabilize:

- Skill runtime source/reference/evals/assets;
- focused test and standalone baseline declarations;
- generated registry/catalog/provenance/runtime identity;
- README candidate;
- VERSION candidate;
- CHANGELOG candidate;
- any current repository parity source required for the release candidate.

After `C`, these are frozen.

If any candidate-owned content changes after `C`, old Gate evidence cannot support final PASS. Create `C2`, re-run affected Gate evidence according to blast radius, and bind final review only to the latest candidate.

Do not stitch PASS evidence across candidates.

## Capability gates

### G1 — Normal entry / routing

Executor-owned before independent review.

Use an actual installed runtime from exact candidate `C` in a fresh normal Codex session. Natural Project-instruction editing prompts must trigger the Skill without naming it, while near-miss tasks stay with their frozen owners.

### G2 — Core editing semantics

Executor-owned before independent review.

Exercise:

- three edit modes;
- missing inputs;
- ownership/enforcement;
- locator;
- protected absence;
- budget;
- bounded/full/no-op;

using real historical repository evidence and public-safe equivalents.

All outputs must be produced by `C`.

### G3 — Fidelity / authority / should-not-change

Executor-owned before independent review.

Directly compare baseline/source/output for:

- mandatory/optional;
- authorization;
- safety;
- permission;
- evidence strength;
- uncertainty;
- exact identifiers;
- explicit deletion/correction;
- unrelated scope;
- near-miss owner.

All outputs must be produced by `C`.

### G4 — Representative complete task + qualitative final artifact

Executor does not own G4 PASS.

Executor must:

1. run representative complete tasks from `C`;
2. freeze complete input/source/output;
3. write:
   `results/project-instructions-editor--standalone-skill-implementation/G4_COMPLETE_TASK_PACKET.md`;
4. mark:
   `G4_READY_FOR_INDEPENDENT_REVIEW=YES`;
5. never label a self-check as G4 PASS.

Independent Reviewer must read:

- final Skill source @ `C`;
- exact candidate/package identity;
- G1–G3 evidence;
- full G4 packet;
- complete user artifact;
- README/VERSION/CHANGELOG candidate;
- candidate immutability proof `C..E`;

and then write:

```text
G4=PASS|REVISE
IMPLEMENTATION_OVERALL=PASS|REVISE
```

A–L remain task/regression families, not Gate count.

## Exact candidate / evidence sequence

The implementation must use this order:

```text
finish all candidate-owned content
-> deterministic preflight/tests
-> create FINAL_CANDIDATE_COMMIT=C
-> install standalone Skill from C
-> run G1
-> run G2
-> run G3
-> create G4_COMPLETE_TASK_PACKET.md from C outputs
-> build portable zip from C runtime tree
-> commit only evidence/result/handoff files
-> set EVIDENCE_HEAD=E
-> prove C..E contains no candidate-owned changes
-> independent Reviewer
```

The final reviewer handoff must report:

```text
FINAL_CANDIDATE_COMMIT=C
EVIDENCE_HEAD=E
```

and include a machine-checkable or directly inspectable `C..E` diff proving only evidence paths changed.

## Validation before C

At minimum run current repository equivalents of:

```bash
python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_project_instructions_editor_contract
python -m unittest tests.test_standalone_skill_baselines
python -m unittest discover -s tests
```

These preflight checks happen before `C` and must be stable before the exact candidate is frozen.

## Runtime validation after C

From exact `C`:

- perform task-local standalone install;
- run fresh-session normal-entry G1;
- run G2/G3;
- generate G4 complete packet;
- build portable package from `C`.

If a runtime Gate exposes a candidate-owned defect, repair candidate-owned content and create a new candidate commit before re-running relevant evidence.

## Release-candidate closure

Current accepted planning decision:

```text
Repository bump decision: MINOR
Expected if origin/main remains 5.4.0: 5.4.0 -> 5.5.0
Affected central plugins: all NO_BUMP
project-instructions-editor standalone version: 0.1
```

If `origin/main:VERSION` changes before release-candidate metadata is written:

```text
VERSION_DRIFT
```

Stop that portion and return to Planner. Do not guess a new release number.

Update candidate-owned README standalone card, root CHANGELOG, VERSION/parity sources, registry/catalog/provenance and standalone baseline evidence. Do not add a central Plugin or profile.

## Evidence

Executor-owned public-safe evidence:

```text
results/project-instructions-editor--standalone-skill-implementation/
├── RESULT.md
├── MANIFEST.md
├── G1_NORMAL_ENTRY.md
├── G2_CORE_SEMANTICS.md
├── G3_FIDELITY.md
└── G4_COMPLETE_TASK_PACKET.md
```

Reviewer-owned later evidence:

```text
results/project-instructions-editor--standalone-skill-implementation/
├── G4_COMPLETE_TASK_REVIEW.md
└── IMPLEMENTATION_REVIEW.md
```

Generate:

```text
private/exports/project-instructions-editor-v0.1.zip
```

The zip must be generated from exact candidate `C` runtime tree and MANIFEST must record:

- `FINAL_CANDIDATE_COMMIT=C`;
- zip SHA-256;
- archive file list;
- runtime tree identity/hash;
- generation method.

## Privacy and source safety

Do not commit private ChatGPT Project threads or private Project settings. Use repository evidence and public-safe fixtures/equivalents.

No paid API/model review is authorized.

## Stop point

Commit and ordinary non-force push exact task branch after:

- `C` exists;
- G1/G2/G3 PASS on `C`;
- G4 packet ready;
- zip from `C`;
- evidence commits exist;
- `EVIDENCE_HEAD=E`;
- `C..E` candidate-owned diff is empty;
- remote branch tip is verified.

Stop at:

```text
G4_READY_FOR_INDEPENDENT_REVIEW=YES
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

Do not merge `main`, advance `release`, tag, publish, create a GitHub Release, create a Plugin wrapper, or claim repository `5.5.0` is released.

```text
READY_FOR_CODEX=NO
```
