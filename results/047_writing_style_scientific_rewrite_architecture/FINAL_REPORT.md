# Final Report

## What this task solved

047 built and locally validated a bounded `writing-style` architecture for
Chinese scientific rewrite requests. The new path gives `writing-style` an
internal `scientific-rewrite` route for long-form, high-fidelity Chinese
scientific/technical revision without creating a new top-level plugin.

The task did not reach product PASS. The remaining required 044 private
production-entrypoint replay artifact could not be generated under the current
execution policy, so the branch cannot truthfully enter CI, Text Review, or
Scheduled Reviewer PASS.

## What changed

The frozen implementation commit is:

```text
ade5a1f653f88df07eb0c70edfd016c744b1611a
```

That commit added the source `scientific-rewrite` skill under
`skills/writing/core/scientific-rewrite/`, regenerated the canonical
`writing-style` Marketplace payload, updated routing in `chinese-prose`, added
supporting fidelity/rewrite references, and added focused tests.

A later policy clarification commit updated `AGENTS.md` to make isolated
production replay the default for central plugin refinement entrypoint checks.
Later evidence commits only record task state and replay evidence; they do not
change production `writing-style` behavior.

## New capabilities / behavior

The candidate implementation can route ordinary long-form Chinese scientific
rewrite requests through `writing-style` into a meaning-first rewrite path that
uses:

- source unit cards and Meaning Cards;
- a Fidelity Ledger for literal and semantic invariants;
- metadata-selected rewrite examples without embeddings or vector databases;
- exact literal checks for numbers, citations, paths, code, equations, and
  formal identifiers.

Example user-facing requests that should now route to the new path include:

```text
把这份中文科研报告说人话一些，但不要改变事实、数字、公式、引用、专业术语和结论强度。
```

```text
帮我把这段实验结果改得更像自然中文科研汇报，保留所有数字、模型名和失败结论。
```

## Deliberately not adopted / unchanged

047 did not add a new top-level plugin, did not change `presentations`,
`research-writing`, or adjacent plugin behavior, and did not vendor another
writing repository wholesale.

It also did not use embeddings, vector databases, new model vendors,
fine-tuning, 044-specific phrase blacklists, AI-detector evasion, or personal
voice learning from historical documents.

The current live global Codex Marketplace installation and plugin cache were
not modified for replay.

## Example usage

普通用户仍然从 `writing-style` 入口表达需求：

```text
把这份报告改得更顺一些，但保留所有实验事实、数字、公式和引用。
```

```text
这段中文技术总结读起来像机器翻译，请改成自然科研中文，不要改结论强度。
```

```text
只帮我检查数字、路径、公式和引用有没有被改坏。
```

The first two requests target scientific rewrite behavior; the last request
should stay in fidelity-audit behavior rather than trigger heavy rewrite.

## Regression and remaining limitations

Local process verification passed for marketplace generation, source/generated
parity, active skill validation, focused unit tests, and temporary install
smokes.

The frozen public holdout batch was executed after implementation freeze.
Executor-side evidence recorded two positive public holdouts with no observed
critical fidelity violations, plus two should-not-fix controls that avoided
over-rewrite.

The required private 044 known-regression model-produced artifact remains
unavailable. The isolated Marketplace install and ordinary prompt routing were
verified, but fresh `codex exec --ephemeral` could not be run on the private 044
report under execution policy. The command was rejected before model execution
even after the user gave explicit one-time authorization for the exact
artifact/provider/purpose/credential scope.

Because the 044 artifact does not exist, the encrypted Text Review payload and
manifest were not produced. `TEXT_REVIEW.json` is therefore absent by design,
not stale, and no product PASS is claimed.

The Reviewed Handoff transition planner pointed to a human plan decision, while
the local strict transition helper initially refused terminalization because it
validated the missing Text Review manifest even when that missing artifact was
itself the reason for the human gate. No placeholder `payload.age` or
`text_inputs.json` was created, since there is no model-produced 044 candidate
artifact to bind. The final control-plane repair sets the terminal decision as
`AWAIT_HUMAN_DECISION / PLANNER_DECISION` and disables Text Review as a pending
evidence producer for this terminal Planner decision; this is not a Text Review
PASS.

## Planner final disposition

The single allowed Plan revision has already been consumed. That revision
provided the narrowest safe authenticated isolated-replay path: a task-local
copy of the existing Codex login, no live Marketplace/plugin mutation, no
credential disclosure, and no change to the frozen implementation. Executor
then retried the exact private 044 replay after explicit user authorization.
The execution approval layer rejected the external model call under tenant
policy before model execution.

This is now an external execution-policy boundary, not a remaining ambiguity in
the scientific-rewrite architecture and not a reason to weaken the frozen 044
artifact gate. Planner therefore makes no second re-plan and does not fabricate
a Text Review manifest. The task must stop before CI/Reviewer product PASS and
enter human decision with these facts fixed:

1. Implementation remains frozen at
   `ade5a1f653f88df07eb0c70edfd016c744b1611a`.
2. The public frozen batch is useful experimental evidence only. It is still
   Executor-side evidence and has not been promoted to independent PRODUCT /
   ARTIFACT PASS.
3. The 044 known-regression gate remains unproven because no fresh
   model-produced private candidate exists.
4. `writing-style` remains `NO_BUMP`; repository bump remains `NONE`.
5. 047 must not merge to `main` on the current evidence.

A future human decision may choose one of three clean continuations without
rewriting history:

- supply the missing 044 candidate/Text Review through an execution surface that
  is actually permitted to send that private artifact to the authorized model,
  while keeping the frozen implementation unchanged;
- close 047 as an experimental architecture result with no production cutover;
- if the desired acceptance criteria themselves should change (for example,
  waiving the 044 private artifact gate), start a new planning task rather than
  consuming a nonexistent second 047 Plan revision.

The execution-policy failure does not justify live-global plugin mutation,
secret extraction, indirect policy bypass, placeholder evidence, or another
044-specific repair cycle.

## Technical appendix

Important commits:

```text
ade5a1f653f88df07eb0c70edfd016c744b1611a  Implement scientific rewrite architecture
a05e4a67  Clarify isolated plugin production replay
b5d773b937497bedc488b73da81baa1a091a182e  Record 047 isolated replay evidence
265ee7d  Revise 047 plan for isolated authenticated replay
75ec01e  Resume 047 after planner auth replay clarification
b97ffa5557c4b564d702daf2fef6a844827c7eec  Record 047 terminalization evidence
```

Important artifacts:

```text
automation/reviewed_handoff/tasks/047_writing_style_scientific_rewrite_architecture/PLAN.md
automation/reviewed_handoff/tasks/047_writing_style_scientific_rewrite_architecture/CURRENT.json
results/047_writing_style_scientific_rewrite_architecture/RESULT.md
results/047_writing_style_scientific_rewrite_architecture/isolated_production_replay/ISOLATED_PRODUCTION_REPLAY.md
results/047_writing_style_scientific_rewrite_architecture/isolated_production_replay/ISOLATED_PRODUCTION_REPLAY.json
results/047_writing_style_scientific_rewrite_architecture/public_holdout_evaluation/
```

Local verification commands recorded in `RESULT.md` passed before the
implementation freeze. GitHub CI was not entered because the required private
Text Review input artifacts could not be generated.

Planner disposition:

```text
state: AWAIT_HUMAN_DECISION
human_gate_reason: PLANNER_DECISION
text_review_required: false
reason: one Plan revision exhausted; required private 044 replay is blocked by execution policy; no evidence may be fabricated
product pass: NO
release: NONE / writing-style NO_BUMP
merge main: NO
```
