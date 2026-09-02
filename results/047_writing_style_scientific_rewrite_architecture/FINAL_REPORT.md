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

The Reviewed Handoff transition planner now points to a human plan decision, but
the strict transition apply step still rejects terminalization because it
requires a real Text Review manifest. No placeholder `payload.age` or
`text_inputs.json` was created, since there is no model-produced 044 candidate
artifact to bind.

## Technical appendix

Important commits:

```text
ade5a1f653f88df07eb0c70edfd016c744b1611a  Implement scientific rewrite architecture
a05e4a67  Clarify isolated plugin production replay
b5d773b937497bedc488b73da81baa1a091a182e  Record 047 isolated replay evidence
265ee7d  Revise 047 plan for isolated authenticated replay
75ec01e  Resume 047 after planner auth replay clarification
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

Current control-plane check:

```text
transition plan: next_action=HUMAN_PLAN_DECISION, next_state=AWAIT_HUMAN_DECISION
transition apply: rejected because text_inputs.json is missing
current state: NEEDS_GPT_PLANNER
```
