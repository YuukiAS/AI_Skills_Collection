# Result - 052_writing_style_reader_facing_generalization_closure

status: NEEDS_EXPLICIT_USER_AUTHORIZATION_FOR_PRODUCTION_SMOKE

## Summary

052 has a local implementation candidate on branch
`reviewed/052_writing_style_reader_facing_generalization_closure`:

```text
117860f16d3363e90119ed53bd01fa06494f726c
```

This is not a PASS, not `READY_FOR_GPT_REVIEW`, and not `WAITING_FOR_CI`.
The frozen Plan still requires production install/upgrade smoke, GPT Reviewer,
final user ACCEPT, and integration to latest `main`. Those gates have not
completed.

## Implemented

- Added the `scientific-rewrite` heavy-route source skill and generated
  `writing-style` payload from the valid 051 production payload, without copying
  051 task state, private artifacts, paid-review ledgers, or final status.
- Added `SOURCE_PROCESS_FRAME` handling to the heavy-route semantic contract:
  standalone reader-facing candidates must not frame themselves as source
  rewrites using phrases such as `原文指出`, `原文同时提到`, `根据给定材料`,
  `源文`, or `这里保留原文` unless the task explicitly asks for source
  comparison, editing commentary, peer review, provenance, or audit.
- Preserved legitimate attribution: author/literature attribution such as
  `Smith et al. [12] reported ...` remains allowed.
- Added Text Review packet-construction rules to Executor and Reviewer prompts:
  plaintext sent for review must contain only real candidate text, and findings
  that hit only wrapper labels should be classified as
  `REVIEW_PACKET_CONSTRUCTION_FAILURE`.
- Added the small repo-local `AGENTS.md` bootstrap ergonomics rule requested by
  the user: future Reviewed Handoff kickoff/Goal messages should explicitly
  authorize the exact `reviewed/<task_key>` branch and exact task-owned
  temporary worktree up front, without turning `AGENTS.md` into permanent
  branch authorization.

## Local Verification

Passed:

```text
python3 scripts/build_codex_marketplace.py --write --validate --check --path-report
python3 -m unittest tests.test_scientific_rewrite tests.test_reviewed_handoff_prompt_contract -v
python3 scripts/build_codex_marketplace.py --validate --check --path-report
python3 -m unittest tests.test_paid_review_workflows tests.test_reviewed_handoff_visual_target -v
git diff --cached --check
```

Focused evidence added by tests:

- source-process framing in standalone text is rejected;
- legitimate attribution and explicit source-comparison context are allowed;
- stage-package validation includes the standalone reader frame gate;
- Text Review packet rules forbid wrapper labels from reviewed plaintext.

Candidate replay gates now passed:

- Bloom known regression:
  `results/052_writing_style_reader_facing_generalization_closure/known_regression/bloom_known_regression_manifest.json`;
- unrelated light Chinese polish, fidelity-only, and English scientific-prose
  regressions:
  `results/052_writing_style_reader_facing_generalization_closure/unrelated_regressions/unrelated_regressions_manifest.json`;
- exactly two frozen fresh public-safe holdouts:
  `results/052_writing_style_reader_facing_generalization_closure/fresh_holdouts/fresh_holdout_batch_manifest.json`.

The fresh holdout batch was frozen before generation, contains exactly two
different public-safe document families, and used no replacement item. Both
fresh candidates were generated through the canonical candidate replay helper
with `writing-style@ai-skills-candidate` and passed local source-process /
internal-wrapper audits.

## 051 Historical Evidence

051 remains:

```text
STOPPED / NOT_RELEASED / FINAL_TEXT_REVIEW_REVISE
```

Tracked 051 Text Review evidence shows `overall_decision=REVISE` with blocking
findings for both wrapper labels and Bloom source-process leakage. That evidence
is used only as historical known-regression context. 052 did not reopen 051,
rewrite 051 status, consume 051 budget, or copy 051 `CURRENT`, `RESULT`,
`FINAL_REPORT`, paid-review ledger, or private plaintext.

The final 051 private Bloom plaintext reviewed by Terra is not committed in the
repository. Therefore this RESULT does not claim a fresh Bloom replay PASS.

## Maintenance Companion Replay

`ai-bridge plugin-replay` was run for `ai-skills-core@yuukias-ai-skills` with
the 052 `PLAN.md` and `REQUEST.md`.

Run:

```text
20260910T091842Z-39c797e89605
```

Outcome:

```text
BLOCKED_BY_REPLAY_INPUT_SCOPE
```

The replay environment only received copied input files, no repository checkout
or source tree, and could not execute the production refinement. This is useful
negative evidence about replay input scope, not proof that the 052 writing-style
candidate passed or failed.

## Text Review Input

Encrypted input for the single final Terra Text Review has been prepared:

```text
results/052_writing_style_reader_facing_generalization_closure/text_review/payload.age
results/052_writing_style_reader_facing_generalization_closure/text_review/text_inputs.json
```

The temporary plaintext packet is not committed. Its SHA-256 is recorded in the
manifest as:

```text
1ef1c0e09653bd1b16208ef8b4a6888c50e60068ba796ab8cc373f46dd910913
```

The plaintext packet contains only natural document titles plus the Bloom,
Python `re`, and FFT final candidate text. It excludes workflow labels,
review/run identity, hashes, and non-reader-facing HTML comments.

Terra Text Review evidence has landed:

```text
results/052_writing_style_reader_facing_generalization_closure/text_review/TEXT_REVIEW.json
results/052_writing_style_reader_facing_generalization_closure/paid_review_budget.json
```

Result:

```text
overall_decision=PASS
model=gpt-5.6-terra
plaintext_sha256=1ef1c0e09653bd1b16208ef8b4a6888c50e60068ba796ab8cc373f46dd910913
blocking_findings=0
reserved_worst_case_cost_usd=0.056690
actual_model_cost_usd=0.010434
```

## Version Closure

Repository bump decision: PATCH

Reason: 052 improves an existing central plugin's production writing behavior
without adding a new repository-level capability or breaking existing
contracts.

Affected plugins:

- `writing-style`: `0.1` -> `0.2`
  Reason: standalone Chinese scientific/technical rewrites now reject
  source-process framing in reader-facing prose, preserve legitimate
  attribution, and keep Text Review packets free of workflow wrapper labels.

Updated:

```text
VERSION
registry.json
scripts/codex_marketplace_config.json
plugins/codex/plugins/writing-style/.codex-plugin/plugin.json
CHANGELOG.md
docs/plugin-changelogs/writing-style.md
README.md
tests/test_codex_marketplace.py
tests/test_scientific_rewrite.py
```

Local release checks after the version closure:

```text
python3 scripts/build_codex_marketplace.py --write --validate --check --path-report
python3 -m unittest tests.test_codex_marketplace -v
python3 -m unittest tests.test_scientific_rewrite -v
python3 -m unittest discover -s tests
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
```

GitHub full/release CI after version closure:

```text
workflow=Codex Marketplace
run=34492443098
branch=reviewed/052_writing_style_reader_facing_generalization_closure
conclusion=success
jobs=codex-marketplace, windows-sparse-checkout, editable-install-smoke ubuntu-latest, editable-install-smoke windows-latest
```

## Production Smoke Status

`production_install_upgrade_smoke` and `ordinary_production_routing` are still
pending.

Safer alternatives were checked first:

- setting `CODEX_HOME` alone still read the live installed
  `writing-style@yuukias-ai-skills` 0.1 plugin;
- overriding `CODEX_HOME`, `CODEX_PERSISTENT_HOME`, `CODEX_GLOBAL_HOME`,
  `CODEX_HOME_BASE`, and `XDG_CACHE_HOME` still read the same live plugin state;
- process-local marketplace config with `plugins.writing-style@yuukias-ai-skills.enabled=true`
  produced a natural rewrite, but the JSONL showed it consumed the existing
  live `writing-style/0.1` cache rather than the 052 `0.2` payload.

The only currently observed path that would verify the exact production
identity is a bounded live smoke: temporarily point the live
`yuukias-ai-skills` marketplace at this 052 worktree, install
`writing-style@yuukias-ai-skills` 0.2, run one ordinary natural routing smoke,
then restore the previous marketplace source and plugin install. Auto-review
rejected that operation twice, including a version with an `EXIT` restoration
trap, because it mutates live global marketplace/plugin state and requires an
explicit user approval for that side effect.

This is not a product failure and not a release PASS. It is an authorization
gate for the required production smoke.

## Not Completed

The following frozen gates remain pending:

- production install/upgrade smoke;
- ordinary production routing smoke;
- GPT Reviewer;
- final user ACCEPT;
- latest-main integration and task branch cleanup.

## Version Decision

Repository bump decision: PATCH

Reason: 052 changes existing `writing-style` production behavior inside the
current repository contract.

Affected plugins:

- `writing-style`: `0.1` -> `0.2`
  Reason: production behavior changed and the original failure replay,
  unrelated regressions, fresh holdouts, Text Review, and local release checks
  have passed. Full/release CI and production smoke are still pending.
