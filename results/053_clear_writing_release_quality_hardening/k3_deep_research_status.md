# 053 K3 Complete Deep Research Status

Status: FAIL_RENDER_QA_REPLAY_BUDGET_EXHAUSTED

Candidate commit: `fcb20edbe2a738db39e3a9d9ed8c6b451ec66526`

## Authorization and replay count

Provider-trust approval was recorded in:

```text
results/053_clear_writing_release_quality_hardening/k3_provider_trust_approval.md
```

K3 private replay count under the 053 Goal:

| Attempt | Run id | Result | Counts against K3 budget |
| --- | --- | --- | --- |
| 1 | `20260912T142748Z-1585738` | FAIL_CANONICAL_CONSUMPTION_PROOF; old 0.2 diagnostic task prompt hard-coded a stale plugin path, so the output was not accepted as candidate consumption evidence. Cleanup passed. | YES |
| 2 | `20260912T144144Z-1651902` | PASS for canonical candidate consumption and generation; FAIL for private PDF render QA because representative page 7 contains a visibly clipped wide table. Cleanup passed. | YES |

The canonical Goal authorizes at most two 053 candidate replays of the exact
private Deep Research source. That replay budget is now exhausted.

## Private artifact locators

Private plaintext and private renders are intentionally stored only under the
ignored repo-local directory:

```text
private/exports/053_clear_writing_release_quality_hardening/k3_deep_research/
```

Tracked evidence records only non-secret locators, sizes, hashes, and QA status.

## Attempt 2 canonical replay evidence

Run metadata:

```text
.local-runtime/candidate-plugin-replay/runs/20260912T144144Z-1651902/run.json
```

Key facts:

```text
plugin_id = writing-style@ai-skills-candidate-053
actual_consumption.proven = true
actual_consumption.event_type = item.started
candidate_commit = fcb20edbe2a738db39e3a9d9ed8c6b451ec66526
runtime_version = codex-cli 0.153.4
```

Private route identity:

```text
selected_route = scientific-rewrite
ordinary_user_prompt = true
source_sha256 = f447de7acaae76486e42e6281f9280b482c770303a67c0861256ddba67316213
candidate_sha256 = 9d4f673feb0db01326e93cd2ef3438a38358c62d6e312701f8fbb0037c3c7429
generation_scope = complete_source_report_structural_rewrite
terra_review_run = false
gpt_reviewer_run = false
production_plugin_modified = false
```

Cleanup:

```text
candidate cache removed = /overflow/htzhu/mingcheng_new/.codex-global/plugins/cache/ai-skills-candidate-053
post-run candidate cache residue = none observed
post-run candidate marketplace residue = none observed
credential copy/symlink = NO
```

## Private Markdown/PDF QA summary

Private final Markdown:

```text
path = private/exports/053_clear_writing_release_quality_hardening/k3_deep_research/Clear_Writing_Deep_Research_Final.md
bytes = 52904
sha256 = 9d4f673feb0db01326e93cd2ef3438a38358c62d6e312701f8fbb0037c3c7429
chars = 27517
lines = 541
code_fences = 0
formula_text_fences = 0
math_markers = 152
raw_wiki_open = 0
raw_ref_html = 0
source_process_framing = 0
workflow_leakage = 0
ordinary_internal_english_terms = 0
markdown_table_rows = 111
```

Private final PDF:

```text
path = private/exports/053_clear_writing_release_quality_hardening/k3_deep_research/Clear_Writing_Deep_Research_Final.pdf
bytes = 349179
sha256 = f67bc519731cbca6501b452a5537b218da6f43f60230f8f1d520f385fcd83215
renderer = Pandoc -> XeLaTeX
pages = 13
encrypted = no
page_size = A4
```

Embedded fonts include Noto Serif SC, TeX Gyre Termes, TeX Gyre Termes Math,
LM Mono, and NewCMMath.

PDF text extraction:

```text
path = private/exports/053_clear_writing_release_quality_hardening/k3_deep_research/Clear_Writing_Deep_Research_Final.txt
bytes = 60986
sha256 = e2da15cb55bb6b19874896390d5fad60f8ca4f8d4898ab84f5db5ad0afddbb3e
code_fences = 0
formula_text_fences = 0
raw_wiki_open = 0
raw_ref_html = 0
unrendered_latex_commands = 0
source_process_framing = 0
workflow_leakage = 0
ordinary_internal_english_terms = 0
```

Representative private page PNGs:

```text
page-01.png sha256 = e0c753b3adee360cb43f57010a583f124b4ba3ea485affd7d9795d700caa24eb
page-07.png sha256 = fb19d953ed49dd689bf95800a04bfd8e1c2cbe7ca5f5a5238574309f9288e296
page-13.png sha256 = e7721b74553c776a1f7c303273680176da8b08ec16f92ec4a77ea25523307793
```

Visual inspection:

- Page 1: PASS. The opening is reader-facing, uses a real rendered table, and does not expose workflow or source-process framing.
- Page 7: FAIL. A wide table is visibly clipped on the right edge of the PDF page, so the table is not fully readable.
- Because page 7 fails, K3 render QA fails even though Markdown-level and text-extraction scans improved substantially over the 0.2 diagnostic.

## Decision

K3 is not closed. The failure is a real product/render-quality failure under the
canonical Goal, not a replay-infrastructure failure and not a private-provider
authorization issue.

Because both authorized K3 replays have now been consumed, Executor must not run
a third private Deep Research candidate replay under the current frozen 053
scope. Fresh holdouts, final Terra review, release CI, production smoke,
Reviewer handoff, final user acceptance, and latest-main integration cannot
legally proceed until Planner/user provides a new scope decision.
