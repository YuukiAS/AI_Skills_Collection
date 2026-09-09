---
name: scientific-rewrite
description: Source-faithful structural rewrite route for existing Chinese or Chinese-dominant scientific/technical material when users ask to reorganize it into clearer Chinese while preserving facts, numbers, formulas, citations, comparisons, conditions, limitations, paths, and exact details.
status: active
provenance: local
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-09-07
profile_tags:
  - writing
  - global
recommended_scope: global
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
license: MIT-compatible local synthesis; architecture baseline from reviewed task 050 clear-language redesign v0.3
---
# Scientific Rewrite

This is the heavy Chinese rewrite route inside `writing-style`. Use it when an
ordinary user provides existing Chinese or Chinese-dominant scientific/technical
material and asks to reorganize, restructure, or rewrite it into clearer Chinese
while preserving exact scientific details. The user does not need to name this
skill or any internal route.

The routing signal is the combination of all three conditions:

- existing Chinese or Chinese-dominant scientific/technical source material;
- a request for reorganization, structural rewrite, or document-level rewrite,
  not only local polishing;
- explicit preservation pressure on facts, numbers, formulas, citations,
  comparisons, conditions, limitations, paths, configuration keys, commands, or
  other exact details.

Do not wait for the user to say `scientific-rewrite`, `Meaning Map`,
`Reader Plan`, `REALIZE_MEANING`, or another internal term. Those are
implementation details, not user-facing activation words.

The ordinary user should not need to name this skill. A natural request such as
"把这份较长科研报告重新组织成自然中文，数字、公式、引用、比较条件和限制都不能丢" should be routed here by the installed
`writing-style` plugin when the source is long enough to need document-level
meaning planning.

## Boundaries

- Host Codex owns semantic extraction, planning, realization, audit, repair,
  assembly, and final prose. Do not call paid OpenAI/Terra generation in these
  stages.
- `rewrite_support.py` is mechanical only. It validates schemas, source-anchor
  coverage, ordinary route selection, exact items, source/repair/assembly
  leakage, and receipts. It does not generate reader-facing prose or certify
  naturalness.
- `chinese-prose` owns `REALIZE_MEANING`: turning an already-fixed semantic
  packet into natural Chinese.
- `writing-fidelity` owns `STRUCTURAL_REWRITE`: preserving the content/evidence
  graph while allowing source headings, paragraph boundaries, and section order
  to change unless the user explicitly protects them.
- Existing `scientific-prose` remains the English scientific prose route.

## Heavy Path

```text
raw source
-> ordinary writing-style route selection
-> source anchors
-> Meaning Map
-> Reader Plan
-> REALIZE_MEANING
-> assembly
-> exact + semantic fidelity audit
-> structured targeted repair when needed
-> re-assembly when needed
-> re-verification
-> final candidate
```

`REALIZE_MEANING` uses soft isolation. The host model may have seen the raw
source earlier in the same task, but the formal realization packet must not
re-present raw source paragraphs, source excerpts, source quotations, source
tails/previews, source-shaped templates, prior rejected candidates, manual
reference output, Latin-span inventories, QA ledgers, or validator fields as
drafting input.

Do not create nested `codex exec`, a second model runtime, or another isolation
system only to claim that the writer forgot the source.

## Route Selection

The installed `writing-style` entrypoint must select this heavy route from an
ordinary user request. The prompt may ask to rewrite a longer Chinese scientific
or technical document naturally while preserving numbers, formulas, citations,
comparisons, conditions, and limitations. The prompt must not name
`scientific-rewrite`, `Meaning Map`, `Reader Plan`, `REALIZE_MEANING`, internal
stage names, or validator names.

Record route evidence in `route_selection.json` before validating the stage
package:

- `schema`: `SCIENTIFIC_REWRITE_ROUTE_SELECTION_V1`;
- `selector_owner`: `writing-style`;
- `selected_route`: `scientific-rewrite`;
- `forced_route`: `false`;
- `ordinary_user_prompt`: `true`;
- `prompt_sha256` and `source_sha256`;
- `prompt_internal_terms`: empty list.

A forced subskill invocation is diagnostic only. It cannot satisfy the ordinary
production route gate.

## Meaning Map

The Meaning Map is meaning-centric and source-auditable. It must include:

- stable source anchors with hashes;
- meanings with `meaning_id`, `kind`, `normalized_meaning`, source anchors, and
  exact items where needed;
- relations when one meaning depends on, qualifies, compares with, or limits
  another;
- exact items whose literal identity matters;
- bidirectional coverage: every substantive source anchor has meaning
  ownership, and every meaning has source authority.

Missing or malformed semantic extraction is a failure/repair condition. The
helper must never fill `normalized_meaning` from source excerpts or continue
with a source-copy fallback.

## Reader Plan

The Reader Plan owns reader-question order, semantic dependencies, bundle
ownership, and information shape. It must not contain raw source prose, source
excerpts, target rewrite sentences, Latin-span QA classifications, seed
templates, or validator language.

Mechanical size limits may only request `NEEDS_SEMANTIC_SPLIT`; they must not
become the production heavy planner. Fixed `4 paragraphs / ~2800 chars`
chunking is not a valid final heavy-route boundary.

## Realization Packet

A `REALIZE_MEANING` packet may contain:

- audience and register;
- bundle purpose and reader question;
- relevant meaning and relation records;
- required exact item identities/formulas;
- neighboring bundle purposes/dependencies;
- information shape;
- optional structured repair instruction.

It must not contain raw source paragraphs, source quotes, source excerpts,
source tails/previews, old candidates, manual reference text, Latin-span
inventories, seed rewrite templates, or self-audit ledgers as drafting input.

## Assembly

Assembly may consume Reader Plan, realized bundles, meaning ownership, bundle
order/dependencies, required exact objects, and terminology established by the
realized bundles. It may add headings/transitions that add no scientific claim,
remove duplicate definitions while preserving ownership, and place formulas,
tables, or lists near their explanation.

Assembly must not receive the raw source as drafting material and must not
become a second whole-document source-conditioned writer.

## Repair

The semantic auditor may read raw source. A repair packet sent back to
`REALIZE_MEANING` may only contain structured corrections:

- bundle id;
- affected meaning IDs;
- finding type;
- required semantic correction;
- required exact-item IDs;
- allowed semantic operations.

It must not contain source prose, source quotations, source sentences, or a
target rewrite sentence. If the Meaning Map is wrong, repair the Meaning Map
first and update the Reader Plan before re-realization.

## Exact Items

An ordinary Latin technical word is not exact-protected merely because it is
Latin script. Exact preservation is for formulas, citations, machine-facing
tokens, paths, commands, config keys, code identifiers, formal algorithm/model
names, datasets, metrics, packages, APIs, and user-explicit protected spans.
Ordinary reasoning, comparison, qualification, and transition language remains
eligible for natural Chinese realization.

## Reader-Facing Relevance Filter

Do not treat repository workflow metadata as reader-facing scientific meaning
merely because it is exact. The heavy route must distinguish scientific
reproduction details from internal execution traces.

Keep exact script, configuration, command, data, model, metric, citation, or
formula identities when they support the scientific/technical argument or
reproducibility contract. For example, a source statement that an experiment
uses `scripts/run_fedfisher.sh` and `configs/mm_fedfisher.yaml` may remain in a
short reproducibility paragraph.

Do not put these in the main reader-facing candidate unless the user explicitly
asks for an audit log or repository handoff:

- Reviewed Handoff state, Gate numbers, Planner/Reviewer/Executor status, CI
  status, test command summaries, or Text Review workflow state;
- Git commit hashes, branch names, GitHub Actions run ids, worktree state, or
  release checklist status;
- task-local paths such as `results/051_*`, `exports/private/*`,
  `automation/reviewed_handoff/*`, `.local-runtime/*`, plugin cache paths, or
  `CURRENT.json` / `RESULT.md` / `FINAL_REPORT.md`;
- statements such as "this round is ready to close", "waiting for external
  planner review", or "the result has passed independent planner review" when
  they are process state rather than scientific content.

If the source mixes a scientific report with workflow/audit metadata, use the
metadata only to avoid false claims and to understand artifact authority. The
final candidate should present the scientific content first and move necessary
technical reproduction details to a short appendix. Irrelevant workflow traces
should be omitted, not "preserved" as prose.

## Completion Standard

This route can claim process completion only when the stage package validates:

- ordinary `writing-style` route selection chose `scientific-rewrite`;
- no raw-source drafting leakage into realization, repair, or assembly;
- complete source-anchor/meaning ownership;
- valid Reader Plan bundle ownership;
- exact items preserved;
- reader-facing candidate has no internal workflow / CI / commit / task-path
  leakage;
- semantic audit has no unresolved critical findings;
- no paid generation dependency;
- no private plaintext committed;
- final candidate hash binds the receipt.

Validate with either current or compatibility command spelling:

```bash
python3 skills/writing/core/scientific-rewrite/scripts/rewrite_support.py validate-host-stage \
  --source SOURCE.md \
  --stage-dir stage_packets \
  --prompt USER_PROMPT.md \
  --receipt stage_packets/stage_receipt.json
```

This is not product-quality PASS. Human artifact acceptance and the task's
Reviewed Handoff gates still own reader-facing quality.
