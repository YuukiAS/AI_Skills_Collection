# Project Instructions Editor implementation review

Date: 2026-10-02  
Result: `REVISE`

Reviewed identities:

```text
FINAL_CANDIDATE_COMMIT=227bb9dbc5e35d546822d27d7985d4d81c371d1c
EXECUTOR_EVIDENCE_HEAD=c5dafa5db724bae2533587fc64f4d68722b1c67d
```

The candidate source, generated/release-candidate metadata, Executor evidence, and candidate-immutability proof were reviewed from the exact task branch.

```text
IMPLEMENTATION_OVERALL=REVISE
G4=REVISE
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO
BLOCKERS=R1,R2,R3
```

## What is already supported

The candidate itself implements the frozen product architecture in a compact instruction/reference-only Skill:

- metadata is read-only/no-network/no-exec as approved;
- the trigger description is specific to long-lived ChatGPT Project instructions and excludes major near-miss families;
- preservation-sensitive / greenfield / explicit-reset modes are present;
- live baseline, targeted history, canonical source, budget, protected absence, semantic ownership/effective enforcement, locator safety, bounded edit, no-op, and proportional delivery are all represented;
- registry/catalog/provenance/README/VERSION/CHANGELOG candidate updates are present;
- `C..E` is evidence-only and does not mutate the frozen candidate.

The visible G2 and G3 evidence is directionally consistent with the frozen contract.

No GitHub Actions/check status was reported for the candidate/evidence commits; the Executor's local deterministic/full-suite evidence remains the available test evidence.

## R1 — G4 full-input evidence is incomplete

Status: blocking.

See `G4_COMPLETE_TASK_REVIEW.md`.

The complete G4 packet lacks the exact natural request, live baseline, targeted-history/deletion input, exact budget input, and actual fourth canonical source (`AGENTS.md`) needed to independently compare a preservation-sensitive complete replacement against its full inputs.

Minimum closure is evidence-only if the original run inputs were preserved; otherwise rerun G4 from the same candidate using a frozen public-safe complete packet.

## R2 — G1 proves positive discovery, but not the frozen near-miss owner boundary

Requirement:

G1 is not only a positive-trigger gate. The frozen claim is that normal unnamed Project-instruction requests enter this Skill while adjacent task families remain with their actual owners.

The approved near-miss boundary includes at least:

- ordinary Chinese prose -> `chinese-prose`;
- ordinary writing fidelity -> `writing-fidelity`;
- scientific/technical structural rewrite -> `scientific-rewrite`;
- AI_Skills repository maintenance -> `ai-skills-core`;
- complex workflow/control -> `workflow-core`;
- generic agent/system prompt -> outside this Skill;
- global Custom Instructions -> outside this Skill.

Direct evidence:

`G1_NORMAL_ENTRY.md` contains one positive fresh-session run and only one near-miss runtime run: ordinary Chinese prose polishing.

The task-local install recorded in `MANIFEST.md` installs only `project-instructions-editor` into the test workspace. The evidence does not establish that the neighboring owner Skills were present and selected for the owner-bearing near-miss families.

Static `trigger_queries.json` contains the broader negatives, but the approved Gate explicitly states that static trigger metadata/queries do not establish G1.

Causal risk:

The current evidence proves “the editor did not trigger for one prose prompt”, but it does not prove the stronger product contract “near-miss tasks continue to route to their frozen owners”.

A broad implicit trigger could still steal repository maintenance, workflow-control, scientific rewrite, fidelity, generic prompt, or global Custom Instructions requests in a realistic installed environment.

Minimum closure:

From the same final candidate, run a bounded normal-entry routing check in an environment where the relevant neighboring owner Skills are actually discoverable.

Record representative fresh-session natural prompts covering the frozen adjacent owner families and show:

- which Skill/owner loaded, when an owner exists;
- that `project-instructions-editor` did not take ownership of non-Project-instruction requests;
- full user-visible outputs or sufficient direct loading/routing evidence.

This is an evidence gap only if no candidate-owned files change.

## R3 — The frozen candidate contains an unrelated test-harness modification outside the approved implementation scope

Requirement:

The implementation package authorizes the frozen Project Instructions Editor source/tests/generated/release-candidate changes. Unrelated test infrastructure must not be modified simply to make the full suite pass.

Direct evidence:

Compared with the approved implementation-package base, `FINAL_CANDIDATE_COMMIT` changes:

`tests/test_candidate_plugin_replay.py`

from:

`timeout_seconds=0.5`

to:

`timeout_seconds=2`

The current main branch still retains the original `0.5` value. This change is not part of the required Project Instructions Editor source, focused contract test, standalone baseline, generated parity, or repository release-version parity work, and the Executor evidence does not explain why this shared replay test needed alteration.

Causal risk:

Changing an unrelated timeout test to accommodate the current run expands the candidate beyond the frozen product scope and can hide a replay/timeout regression unrelated to this Skill. It also makes the final candidate differ from current main in test behavior for a reason not reviewed by the implementation Plan.

Minimum closure:

Return that test to the current-main baseline unless Planner/Critic separately approves a real repository-wide replay-test defect with direct evidence.

Because this is candidate-owned content, reverting it requires a new final candidate commit under the frozen C/C2 rules. Re-run the deterministic/full test suite and regenerate candidate/evidence identity accordingly. Re-run product Gates as required by the frozen same-final-candidate/blast-radius contract; do not stitch the old candidate's PASS claims onto the new candidate without a valid same-candidate proof.

## Non-blocking observations

1. The README standalone card uses unnecessary mixed English such as `live setting` and `canonical source` in reader-facing Chinese. The repository's README policy prefers natural Chinese. If a new candidate is already required for R3, this is worth cleaning up in the same bounded revision, e.g. use “当前设置、既有决定、事实来源和字符预算”. Do not reopen product design for this wording issue.

2. The portable ZIP itself is untracked under `private/exports/` and is not directly readable from this review surface. The manifest records an exact candidate-derived `git archive` command, SHA-256, runtime file hashes, and candidate identity, which is useful mechanical evidence; no separate blocker is added solely for the unavailable binary in this review.

## External fact check

Current OpenAI documentation remains consistent with the implemented Skill shape: a Skill is a directory centered on `SKILL.md`, discovery uses the Skill's name and description, and supporting references/resources may be loaded when the Skill is selected. No external product change invalidates the candidate architecture.

## Next state

This is not a design REVISE. The product/design freeze remains valid.

Return to the same implementation task for bounded repair/evidence closure.

```text
IMPLEMENTATION_OVERALL=REVISE
G1=NEEDS_ADDITIONAL_ROUTING_EVIDENCE
G2=PASS_ON_REVIEWED_EVIDENCE
G3=PASS_ON_REVIEWED_EVIDENCE
G4=REVISE
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO
NEXT_HANDOFF=EXECUTOR_OR_PLANNER_PER_CANDIDATE_CHANGE
```
