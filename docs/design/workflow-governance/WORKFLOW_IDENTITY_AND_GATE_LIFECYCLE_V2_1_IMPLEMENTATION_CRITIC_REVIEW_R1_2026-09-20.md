# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Implementation Critic Review R1

- Date: 2026-09-20
- Review role: independent Critic
- Review stage: INDEPENDENT_IMPLEMENTATION_REVIEW
- Human-readable name: **工作流命名与插件回归机制完善（AI_Skills + Bridge）**
- Technical task key: `cross-repo--workflow-identity-gate-lifecycle`
- AI_Skills production candidate: `ce63f50238555849a48256068e6fa0d46e21a97b`
- AI_Skills pushed tip/evidence: `afec7635a57ac625aef68bd25b85f29ae8216cb6`
- Bridge production candidate: `2a842371c35769ce7694c642fde852df57de6679`
- Bridge pushed tip/evidence: `4d4e4070051551c33b9d38c1b922bb8d4d1b32bb`
- AI_Skills latest main inspected: `f0649b7cd68d1cd9929314f389c9b4024e074ae8`
- Bridge latest main inspected: `afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Decision: **REVISE**
- Complexity: **APPROPRIATE**
- Next owner: **CODEX bounded repair on the same two reviewed branches**

## 1. Bottom line

The implementation is close, and the architecture remains valid, but the exact final candidate cannot pass independent review yet.

Two blocking issues were found:

1. the standalone Bridge workspace validator has a real runtime bug caused by shadowing the imported `task_keys` module with a local `set`; this breaks one of the explicitly required validator surfaces even though the full test suite reports green;
2. the AI_Skills candidate plugin replay evidence proves candidate loading/consumption, but it does not preserve or expose the actual model outputs needed to independently judge G3/G5/G6, and the frozen replay inputs do not faithfully exercise the representative cases required by the approved Plan.

Both are ordinary in-scope implementation/evidence defects. They do not require Planner redesign, a new task key, a successor workflow, or a new Gate.

Do not start the historical 056 / “开发交付流程完善（原 056）” execution yet. Repair this candidate first, re-freeze the cross-repo tuple, and repeat independent implementation review. Only after this task passes and is integrated/released should 056 do its required bounded source/version revalidation against the new main.

## 2. Verified good work

### Identity / cutover

Bridge candidate introduces one lexical authority in `ai_bridge_kit/task_keys.py`, semantic-only new Reviewed Handoff creation, dual legacy/semantic validation intent, collision fail-closed behavior, semantic task/result paths, and user-facing authoring updates.

The actual reviewed branch names use the approved semantic key and both remote branch tips match the Executor handoff.

### AI_Skills policy / consumers

AI_Skills candidate updates:

- Gate lifecycle policy;
- Planner/Critic consumer rules;
- workflow-core source/generated payload;
- AI Skills Maintainer source/generated payload;
- plugin/repository version metadata and changelogs.

The source/generated parity path was exercised and both candidate plugins were actually loaded under the candidate marketplace identity.

### Version / main drift

Current AI_Skills main has advanced only through unrelated README-refactor design/package documentation after the reviewed execution baseline; no relevant production source/version slot was consumed. Bridge main remains the same baseline.

The planned candidate versions are still coherent.

## 3. Blocking finding C-WIGL-I1-STANDALONE-VALIDATOR-SHADOWING

**Requirement**

The approved design and execution package explicitly require the three Bridge validation surfaces to share the semantic/legacy task-key authority, including `scripts/validate_handoff_workspace.py`.

**Observed source**

The candidate imports:

```python
from ai_bridge_kit import task_keys
```

but inside `validate()` it later binds:

```python
task_keys = set()
```

and then calls:

```python
task_keys.existing_task_key_error(task_key)
```

At that point `task_keys` is the local `set`, not the imported module.

Python's normal block/name-binding semantics make this a real runtime defect, not a style concern.

**Causal risk**

The standalone validator crashes when it reaches a new-style task file instead of validating semantic/legacy keys. That means one of the cutover validator surfaces required by G2/G4 is broken while the reported `367 tests OK` still passes.

This also proves the current full suite does not execute this exact standalone script path.

**Minimum closure**

On the same Bridge branch:

1. rename the local set so it does not shadow the `task_keys` module;
2. add a regression test that actually executes/imports the standalone validator path with:
   - one semantic task;
   - one existing legacy task;
   - one malformed semantic task negative case;
3. rerun the focused validator tests and full Bridge suite;
4. run the standalone validator normal entry once on an isolated fixture;
5. form a new Bridge production candidate commit.

No parser redesign or new validation layer is needed.

## 4. Blocking finding C-WIGL-I2-REPLAY-CAPABILITY-EVIDENCE

**Requirement**

The approved Plan says mechanical tests and candidate-consumption receipts are not enough. Runtime replay must directly demonstrate:

- G3 scope semantics through representative cases;
- G5 existing-regression-vs-new-capability Gate handling;
- G6 narrow-vs-broad/full behavior and same-final-candidate discipline.

Final review evidence must remain in the repository rather than only in ignored `/tmp` runtime files.

**Observed evidence**

The committed replay artifacts `workflow-core-run.json` and `ai-skills-core-run.json` prove:

- candidate plugin identity;
- candidate version;
- actual SKILL consumption;
- runtime identity.

They do **not** include the model's substantive response. Their `stdout_path` points to ignored `/tmp/.../child.stdout.jsonl` files that this independent review cannot access.

The committed replay fixtures also do not faithfully implement the frozen representative scenarios:

- the workflow-core input mostly states the correct policy rules directly instead of presenting the planned isolated/shared/unresolved/maturity cases for classification;
- the AI Skills Maintainer input does not exercise the planned one-plugin / one-repo-multi-plugin / AI_Skills+Bridge-with-read-only-references scope cases, nor a contrasting existing-Gate regression vs genuinely new capability case.

Therefore the replay evidence currently proves consumption, not the claimed behavior.

**Causal risk**

A plugin can load the correct SKILL and still answer incorrectly. The present evidence cannot support G3/G5/G6 independent PASS and is too close to a prompt that already contains the expected answer.

**Minimum closure**

Treat the existing replay runs as preserved but **invalid/incomplete acceptance evidence**; do not delete or relabel them as fresh PASS.

On the same AI_Skills branch:

1. create the two replay scenarios that were already specified by the frozen Plan:
   - Verified Workflow: actual cases requiring classification of isolated narrow vs mandatory broad/full, including unresolved multi-Gate and maturity-promotion cases;
   - AI Skills Maintainer: actual cases for single plugin, one-repo multi-plugin, cross-repo with read-only references, existing Gate regression, and genuinely new capability;
2. do not add a third scenario;
3. keep the new scenario inputs fixed before the run;
4. persist the public-safe substantive model output for each run into repo-owned evidence (for example extracted final response Markdown/JSON plus the existing consumption receipt), not only a `/tmp` JSONL path;
5. independently compare the output against the frozen expected behavior and record a compact verdict;
6. if a product/consumer defect is found, repair within the already-approved architecture and rerun only the same fixed scenario; preserve all attempts;
7. do not call Terra/OpenAI Responses/private review.

This is fixture/evidence repair to meet the existing Plan, not adaptive sample chasing and not a new Gate.

## 5. Candidate tuple consequence

Because Bridge production source must change for C-WIGL-I1, the currently reviewed cross-repo final tuple is no longer eligible for PASS.

Expected repair shape:

- AI_Skills production candidate may remain `ce63f502...` if no AI production source changes are needed;
- Bridge gets a new production candidate after the validator fix;
- evidence commits on both branches may advance;
- corrected AI candidate replay should be recorded against the final stabilized tuple;
- all affected G1/G2/G4 evidence and the final cross-repo evidence map must reference the new exact tuple.

Do not rewrite or force-push the existing candidate history.

## 6. Decision

```text
DECISION=REVISE
COMPLEXITY=APPROPRIATE
C-WIGL-I1-STANDALONE-VALIDATOR-SHADOWING=OPEN
C-WIGL-I2-REPLAY-CAPABILITY-EVIDENCE=OPEN
AI_SKILLS_REVIEWED_PRODUCTION_CANDIDATE=ce63f50238555849a48256068e6fa0d46e21a97b
AI_SKILLS_REVIEWED_BRANCH_TIP=afec7635a57ac625aef68bd25b85f29ae8216cb6
BRIDGE_REVIEWED_PRODUCTION_CANDIDATE=2a842371c35769ce7694c642fde852df57de6679
BRIDGE_REVIEWED_BRANCH_TIP=4d4e4070051551c33b9d38c1b922bb8d4d1b32bb
READY_FOR_INTEGRATION=NO
START_056_NOW=NO
NEXT_HANDOFF=CODEX_BOUNDED_REPAIR
```

## 7. What should happen next

Repair the two findings on the existing branches under the already-approved execution scope. No new task/branch/worktree and no Planner redesign are needed unless the repair discovers that the approved architecture itself is insufficient.

After the repair:

1. push the new branch tips;
2. report the new Bridge production candidate and any changed AI candidate;
3. provide repository-resident replay outputs/verdicts;
4. rerun affected focused/full tests;
5. return to independent implementation review.

Only after implementation review PASS should this task go through its integration/release boundary. Then the historical 056 / “开发交付流程完善（原 056）” should be revalidated against the newly integrated AI_Skills + Bridge main before execution.
