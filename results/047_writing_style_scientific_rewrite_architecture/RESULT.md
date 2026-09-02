---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 047_writing_style_scientific_rewrite_architecture
executor: Codex
implementation_commit: ade5a1f653f88df07eb0c70edfd016c744b1611a
status: NEEDS_GPT_PLANNER
ci_status: PENDING
---

# 047 Writing Style Scientific Rewrite Architecture - Result

## Implementation Commit

`ade5a1f653f88df07eb0c70edfd016c744b1611a`

This is the frozen candidate implementation identity. Later commits in this
branch record execution policy clarification and task-local evidence; they do
not change production `writing-style` behavior.

## Implemented

- Added internal `writing-style:scientific-rewrite` under
  `skills/writing/core/scientific-rewrite/`.
- Added a meaning-first rewrite contract, Meaning Card/Fidelity Ledger
  references, a positive-style contract, and 12 metadata-tagged seed
  transformations.
- Added `scripts/rewrite_support.py` for deterministic packet preparation,
  metadata example selection, and exact literal verification.
- Updated `chinese-prose` routing so long-form Chinese scientific/technical
  high-fidelity rewrite requests can route to `scientific-rewrite`.
- Updated `writing-fidelity` to separate literal preservation from semantic
  preservation.
- Regenerated the canonical `writing-style` Marketplace payload through
  `scripts/build_codex_marketplace.py`.
- Added focused tests in `tests/test_scientific_rewrite.py` and minimal
  Marketplace test updates for the new generated payload.
- Recorded selective MIT source adoption in
  `docs/provenance/INTEGRATION_HISTORY.md`.

No top-level plugin was added. No embedding/vector DB, new model vendor,
fine-tuning, phrase blacklist, 044-specific rule set, or presentations behavior
change was introduced.

## Local Verification

Passed before implementation freeze:

```text
python3 scripts/build_codex_marketplace.py --write
python3 scripts/build_codex_marketplace.py --validate
python3 scripts/build_codex_marketplace.py --check
python3 scripts/skills.py validate
python3 -m unittest tests.test_skill_runtime_text_audit tests.test_research_writing_routing tests.test_codex_marketplace tests.test_scientific_rewrite
python3 scripts/verify_server_installation.py --skill scientific-rewrite --mode copy --json
python3 scripts/verify_server_installation.py --mode copy --json
git diff --cached --check
```

Observed results:

```text
marketplace generator: plugins=10 active_skills=27 source_snapshots=65
skills validate: validated 150 active skills, 18 profiles, templates, and trigger eval scaffolds
focused unittest: Ran 52 tests, OK
temporary scientific-rewrite install smoke: ok=true
default temporary install smoke: ok=true
```

The temporary install smokes reported missing optional `latexmk`; that is not
used by this writing-style path.

## Frozen Public Holdout Batch

Frozen public sources were acquired only after implementation freeze and are
recorded in:

```text
results/047_writing_style_scientific_rewrite_architecture/public_holdout_sources/
```

Executor-side outputs and audit reports are recorded in:

```text
results/047_writing_style_scientific_rewrite_architecture/public_holdout_evaluation/
```

Frozen source range identities:

```text
HOLDOUT-UNSEEN-001  92429e9035fd855b4130080a8003d8128ee3b4d267672ccf3a60b87c6eb22477
HOLDOUT-UNSEEN-002  e4f1369cdc23c767943bff613f776e60b02b4689b5134f5574b94639bbddd52a
SNF-CN-TECH-001     2f44f24073713cadb7ad6a012ae3e4959448926a35c66c93e568fc2dd651313b
SNF-CN-SCI-002      18400b402f15f290978c974d01c2fc7f1f0479bd718dece264ff3bd79aced4f8
```

Executor assessment:

- `HOLDOUT-UNSEEN-001`: candidate exact fidelity passed; no critical semantic
  violation observed; reader effort improved clearly relative to baseline.
- `HOLDOUT-UNSEEN-002`: candidate exact fidelity passed; no critical semantic
  violation observed; reader effort improved modestly relative to baseline.
- `SNF-CN-TECH-001`: classified as `NO_DEEP_REWRITE`; unchanged output passed
  exact fidelity.
- `SNF-CN-SCI-002`: classified as `NO_DEEP_REWRITE`; unchanged output preserved
  the product/model/evidence boundary.

This is Executor-side evidence only. It does not replace independent Text
Review or Scheduled GPT Reviewer artifact reading.

## Isolated Production-Like Replay Evidence

Per the user's live-global non-mutation decision, production-entrypoint
verification used an isolated shadow Codex environment:

```text
/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/isolated-codex-047/
```

The isolated environment used the normal Marketplace/plugin mechanism:

```text
plugin marketplace add /tmp/AI_Skills_Collection_047 --json
plugin add writing-style@yuukias-ai-skills --json
plugin list --json
```

Observed installed plugin:

```text
plugin_id=writing-style@yuukias-ai-skills
version=0.1
enabled=true
installed_cache=/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/isolated-codex-047/codex-home/plugins/cache/yuukias-ai-skills/writing-style/0.1
```

Canonical generated payload and isolated cache payload matched:

```text
d6a5821c7f635a459a40d99c8e5ec0b87f459f52871056a65fc8c2b597b844b2  scientific-rewrite/SKILL.md
```

Fresh isolated `codex debug prompt-input` with the ordinary user prompt:

```text
把这份中文科研报告说人话一些，但不要改变事实、数字、公式、引用、专业术语和结论强度。
```

showed `writing-style:scientific-rewrite`,
`writing-style:chinese-prose`, and `writing-style:writing-fidelity` available
from the installed isolated plugin cache. The prompt did not mention the
internal skill path, hidden artifact id, router, benchmark helper, or test
keyword.

Detailed evidence:

```text
results/047_writing_style_scientific_rewrite_architecture/isolated_production_replay/
```

## Planner Revision 1 Auth Replay Attempt

Planner revision 1 authorized a narrow task-local copy of the current Codex
login file into the isolated `CODEX_HOME`, with no symlink and no live global
plugin/cache mutation.

Executor performed only non-secret checks:

- `codex login status` reported an existing ChatGPT login;
- the active `CODEX_HOME` was
  `/overflow/htzhu/mingcheng_new/.codex-homes/Longleaf_Connection_Bridge`;
- an `auth.json` file was present there, but its contents were not read,
  printed, committed, uploaded, or hashed.

Executor copied it once into the isolated task-local `CODEX_HOME` with mode
`0600`. The fresh isolated `codex exec --ephemeral` production replay command
was then rejected by the execution approval layer before it ran, because it
would use the copied Codex login to send the private 044 report to the external
OpenAI endpoint.

Executor did not retry through a workaround, did not run a source-tree skill as
a substitute, did not mutate live global plugin state, and did not send the 044
private report through this attempt. The isolated auth copy was removed
immediately afterwards; the cleanup check reported `auth_copy_removed`.

No model-produced 044 candidate rewrite artifact exists from this attempt.

The user then explicitly authorized one-time replay for:

- artifact scope: 044 known-regression report;
- provider: OpenAI/Codex;
- purpose: 047 isolated production-entrypoint regression replay and required
  review preparation;
- credential mode: task-local temporary `auth.json` copy.

The same live-global prohibitions remained in force: no live global plugin
cache mutation, no committed/pushed auth/token/private 044 plaintext, and no
printed secrets.

Executor re-created the task-local auth copy with mode `0600` and retried the
same fresh isolated production-entrypoint command. The execution approval layer
again rejected the command before it ran, stating that sending the private 044
report to the external OpenAI endpoint is disallowed by tenant policy even
after explicit user authorization. Executor did not attempt a workaround or
indirect execution, and removed the task-local auth copy again
(`auth_copy_removed`).

No model-produced 044 candidate rewrite artifact exists after the authorized
retry.

## Remaining Gap

The 044 fresh private candidate artifact was not produced. This is not an
installation or routing failure. It is an auth boundary in the isolated model
session:

- local `OPENAI_API_KEY`, `OPENAI_REVIEW_API_KEY`, and
  `OPENAI_VISUAL_REVIEW_API_KEY` were absent;
- the isolated fresh `codex exec --ephemeral` probe first hit connection refused
  while inheriting local proxy variables;
- after proxy variables were unset, it reached the OpenAI endpoint and failed
  with `401 Unauthorized: Missing bearer or basic authentication in header`;
- no live auth token or secret was copied from the real Codex home before
  Planner revision 1;
- after Planner revision 1, a task-local auth copy path was attempted but the
  actual external model replay was rejected by the execution approval layer and
  the copy was removed; after explicit user authorization, the approval layer
  rejected the same command again under tenant policy;
- no current live global Codex Marketplace/plugin cache was modified.

Because the final private 044 artifact does not exist, the required encrypted
Text Review payload and manifest cannot be truthfully generated yet. The
Text Review transport itself preflighted locally: `age` and the repository age
recipient are present, the workflow exists, and secret values were not read.

## State Handoff

This branch should not enter `WAITING_FOR_CI` yet. The Executor prompt requires
CI-required text-review tasks to publish encrypted payload + manifest before
`WAITING_FOR_CI`; doing so without the 044 fresh private artifact would
fabricate product evidence.

Therefore this handoff cannot enter `WAITING_FOR_CI` or
`READY_FOR_GPT_REVIEW` truthfully. Since the single allowed plan revision has
already been used, this run requires final human/Planner disposition of the
private 044 production replay gate. Review counters remain unchanged and
`ci_status=PENDING`.

Executor also checked the Reviewed Handoff terminalization path after recording
the final replay boundary. `ai-bridge reviewed-handoff transition plan` reported
that the next conceptual action is `HUMAN_PLAN_DECISION` with next state
`AWAIT_HUMAN_DECISION`, but `transition apply` refused to enter that terminal
state because the required real Text Review input manifest is missing:

```text
text review input manifest missing: results/047_writing_style_scientific_rewrite_architecture/text_review/text_inputs.json
```

Executor did not create a placeholder manifest or encrypted payload because no
model-produced 044 candidate artifact exists. Doing so would fabricate the
artifact identity required by the frozen Plan.

## Planner Question

Under the user's current rule that 047 must not modify or bind the live global
Codex Marketplace/plugin cache, what is the authorized way to complete the 044
fresh model-produced production replay artifact?

The observed options are:

- provide a task-local auth bootstrap for the isolated `CODEX_HOME` without
  copying live global credentials;
- define a GitHub/Bridge Kit path that can run the same isolated production-like
  installed `writing-style` entrypoint using existing repository secrets and
  return only encrypted/repo-safe evidence;
- revise the 047 gate so isolated install + ordinary-prompt routing evidence is
  sufficient for production-entrypoint verification, while keeping 044 Text
  Review pending and not claiming product PASS;
- ask the user for a new explicit live-global authorization, only if no
  equivalent isolated path exists.

No `PASS`, release, version bump, production cutover, or merge-to-main decision
is claimed here.
