# Canonical Source / Generated Payload Parity Restoration Plan — 2026-10-16

Status: PLANNER_FROZEN_FOR_DIRECT_CODEX_REPAIR
Scope owner: repository maintenance / source authority
Affected domains: presentations, research-writing
Base: main@362a8cab6991120a79600352d070926e2602dcbd

## Objective

Repair a repository source-authority defect that currently blocks Clear Writing full CI.

The defect is not that Presentations or Research Authoring behavior is wrong. The defect is that accepted, already-committed runtime behavior lives only under generated plugin payloads, while canonical source/config does not reproduce it. Running the official generator therefore deletes thousands of lines of already-adopted behavior.

The repair must make canonical source/config reproduce the current generated runtime exactly. It must not redesign either domain and must not change user-visible generated behavior.

## Evidence and authority decision

Presentations:
- `docs/plugin-todos/presentations-authoring-production-workflow.md` is `PROMOTE_NOW / CANONICAL WORKFLOW ADOPTION` and explicitly names the current generated runtime contracts as canonical.
- `docs/design/PRESENTATIONS_RENDER_REGRESSION_POSTMORTEM_AND_HARDENING_2026-10-07.md` says the canonical runtime was hardened with these contracts after a severe real render regression.
- October 6–7 commits deliberately modified `plugins/codex/plugins/presentations/...`, including the business/research skill wrappers and seven shared runtime contracts.

Decision: preserve the current generated Presentations runtime and promote it back into canonical source so regeneration becomes lossless.

Research Authoring:
- `docs/plugin-todos/research-authoring-student-assessment-workflow.md` is `PROMOTE_NOW / IMMEDIATE PROJECT ADOPTION`.
- `docs/skill-todos/course-assessment-authoring-canonical-workflow-promotion.md` also says `PROMOTE_NOW / IMMEDIATE ADOPTION`.
- The current generated `plugins/codex/plugins/research-writing/shared/` contracts were deliberately added and strengthened on October 7 in response to STAT5060 failures.

Decision: preserve the current generated Research Authoring shared runtime and give it a canonical source location plus official packaging mapping so regeneration becomes lossless.

These decisions preserve currently committed runtime behavior. They do not add new semantics beyond what is already in the generated plugin payload.

## Non-substitutable invariant

Before editing, snapshot file-by-file hashes for:
- `plugins/codex/plugins/presentations/`
- `plugins/codex/plugins/research-writing/`

After source restoration and a clean official regeneration:
- every pre-existing generated file in those two plugin trees must be byte-identical to the pre-repair snapshot;
- no generated runtime contract may disappear;
- no skill wording, routing, plugin version, description/default prompt, profile, or professional behavior may change;
- `python scripts/build_codex_marketplace.py --validate --check --path-report` must be clean.

If byte-identical generated preservation cannot be achieved from a clear source-first repair, stop. Do not choose new domain semantics.

## Allowed source restoration

### Presentations

Promote the current generated copies of these seven shared runtime contracts into `skills/tools/documents-media/presentations/shared/`:
- `anti-shortcut-production-contract.md`
- `authoring-production-workflow.md`
- `chatgpt-web-authoring-contract.md`
- `independent-review-contract.md`
- `pre-execution-cumulative-acceptance-contract.md`
- `presentation-end-to-end-pre-execution-runbook.md`
- `rendered-artifact-positive-ancestry-acceptance-contract.md`

Reconcile canonical `business-presentations/SKILL.md` and `research-presentations/SKILL.md` so the official copy generator reproduces the already-committed generated wrappers exactly.

Do not modify Presentations version, routing, default prompts, profiles, templates, renderers, validators, or domain behavior beyond this source-authority restoration.

### Research Writing / Research Authoring

Create a canonical source location for the already-committed generated shared contracts, preferably `skills/writing/research/shared/`, populated from current `plugins/codex/plugins/research-writing/shared/` bytes.

Add the minimum supported `shared` mapping to the existing `research-writing` entry in `scripts/codex_marketplace_config.json` so the official generator reproduces the existing shared directory.

Do not alter current research-writing skills, aggregate composition, routing, version, description/default prompts, profiles, or document semantics.

If the generator cannot reproduce the exact current generated payload with this minimal mapping, stop and report the exact incompatible files.

## Validation

Required before integration:
1. record pre-repair generated tree hashes;
2. run focused generator/config tests;
3. run `python scripts/build_codex_marketplace.py --write --validate --check --path-report`;
4. rerun the same check to prove clean idempotence;
5. compare regenerated Presentations and Research Writing plugin trees to the pre-repair snapshot;
6. require byte-identical preservation for all pre-existing generated files;
7. run directly affected unit tests and full repository unit tests if feasible;
8. run `git diff --check`.

A test or generator failure must be fixed at source. Do not skip or allowlist it.

## Version decision

Repository bump: NONE.
Presentations: NO_BUMP.
Research Writing: NO_BUMP.
Reason: this repair changes canonical source authority and generator reproducibility while preserving the already-committed generated production payload byte-for-byte.

## Integration

Work only on `work/repo--canonical-generated-parity-restoration`.

After validation:
- commit and push the repair;
- merge latest main non-force if main advanced and rerun affected validation;
- integrate the branch back to main only if the generated-payload preservation invariant still passes;
- do not move `release`;
- do not touch the Clear Writing reviewed branch or its CURRENT/PLAN.

After main integration, stop and report the exact main commit. Clear Writing will consume that repaired main in its existing task.