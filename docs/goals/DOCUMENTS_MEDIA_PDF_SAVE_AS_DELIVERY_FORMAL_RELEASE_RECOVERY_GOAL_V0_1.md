# PDF Save-as Delivery — Formal Release Recovery Goal v0.1

Status: REVISED FOR CRITIC R1; DO NOT EXECUTE BEFORE CRITIC PASS

Revision scope: close only `PDF-REL-B1_RELEASED_NORMAL_ENTRY_DELIVERY_SMOKE`; all other 5.4.5 isolation, version, producer, product-byte and maintenance decisions remain unchanged.

## Goal

Formally release the already REVIEW_2-PASS standalone Chinese Math PDF delivery improvement without waiting for or publishing unrelated current-main production work.

The release must produce:

```text
AI_Skills_Collection formal repository release: 5.4.5
render-chinese-math-pdf: 0.3
central Marketplace plugins: NO_BUMP
Bridge Kit: NO_CHANGE
```

Then integrate that exact formal release back into latest `main` while preserving all unrelated main development.

Canonical design authority:

`docs/design/pdf-artifact-delivery/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_ISOLATION_PROPOSAL_PLAN_V0_1_2026-10-17.md`

Existing product authority remains:

- task: `documents-media--pdf-save-as-delivery`
- accepted implementation: `5c92bf4f599d378ff68444b0fa85f5d56bbbd628`
- REVIEW_2: PASS
- existing task state: PASS
- Issue: #101

This Goal changes release topology only. It does not change the PDF product contract.

## Required starting state

Before mutation, refresh and verify:

- repository = `YuukiAS/AI_Skills_Collection`;
- `origin/release` is still the formal repository `5.4.4` line;
- `render-chinese-math-pdf` on `origin/release` is `0.2`;
- accepted PDF task branch and implementation commit remain readable;
- existing REVIEW_2 remains PASS;
- no new evidence contradicts D1/D2/D3.

If the formal release baseline has changed from this state, stop before creating the release candidate and return to Planner.

## Exact release-isolation workspace

Create only after the Critic-approved Kickoff is sent:

```text
branch = release-candidate/documents-media--pdf-save-as-delivery-5.4.5
worktree = /overflow/htzhu/mingcheng_new/AI_Skills_Collection-documents-media--pdf-save-as-delivery-release-5.4.5
base = current exact origin/release
```

This is a release candidate workspace, not a new Reviewed Handoff task and not a successor PDF task.

## Product bytes

The release candidate must use exact accepted blobs:

```text
SKILL.md
37109d885448a96d423bf664ebf9925714b57a0a

references/checklists.md
49dbbdc2cc2283cc2824ed6b32b49716b0a0a7c3

tests/test_render_chinese_math_pdf.py
ae5261e2b10258a7b94ea2a52cfb5b7523461614

render_scientific_pdf.py
0598dea9e034b6abd36336e5cf3ba455a81fa27a
```

The renderer identity is unchanged. D1/D2/D3 are not rerun when these product identities remain exact.

A product-byte mismatch is not a release repair. Stop and return to Planner.

## Release candidate construction

Build from the formal 5.4.4 release tree.

Allowed changes are limited to:

- exact accepted PDF product/checklist/test bytes above;
- release-baseline-derived standalone/version assertion tests required for:
  - repository `5.4.5`;
  - Chinese Math PDF `0.3`;
- `VERSION`;
- `CHANGELOG.md`;
- `README.md`;
- `docs/SKILL_CATALOG.md`;
- `registry.json`;
- canonical PDF TODO entry for Issue #101;
- one bounded formal-release closure evidence file.

Do not copy the task branch's shared release files wholesale when they contain PIE/main-only state.

In particular:

- `tests/test_standalone_skill_baselines.py` must start from formal 5.4.4 and change only the PDF version plus repository-version assertion;
- `tests/test_central_plugin_icon_assets.py` must start from formal 5.4.4 and change only the repository-version assertion;
- any further test edit is permitted only when it is a literal release/PDF version assertion required by the formal-baseline tree.

## Version and metadata contract

Repository bump decision: PATCH  
Reason: this is a compatible improvement to an existing standalone capability.

```text
Repository: 5.4.4 -> 5.4.5
render-chinese-math-pdf: 0.2 -> 0.3
all central plugins: NO_BUMP
project-thread-handoff: unchanged
slurm-workflows: unchanged
Bridge Kit: NO_CHANGE
```

The isolated release must not include Project Instructions Editor, Research Authoring or Presentations unreleased production/metadata from current main.

The future PIE repository MINOR remains `5.5.0`, now based on formal `5.4.5`.

README changes require a real installed Clear Writing invocation before publication.

Generated registry/catalog output must come from the canonical generator. Any unrelated central-plugin/generated change fails release isolation.

## Required release gates

### G1 — release ancestry / scope isolation

Prove the candidate descends from the current formal release and that `origin/release..candidate` contains only the approved allowlist. Prove unrelated main production work is absent.

### G2 — accepted product identity

Prove the accepted PDF product blobs are exact and the renderer remains unchanged. No D1/D2/D3 rerun if identity is preserved.

### G3 — version / changelog / README / generated parity

Prove repository 5.4.5, PDF 0.3, central plugin NO_BUMP, clean source/generated parity, and no main-only unreleased metadata. Record the real Clear Writing README check.

### G4 — full isolated release validation

On the exact final candidate:

```text
python -m unittest tests.test_render_chinese_math_pdf tests.test_standalone_skill_baselines
python -m unittest discover -s tests
python scripts/build_codex_marketplace.py --write
python scripts/build_codex_marketplace.py --validate
python scripts/build_codex_marketplace.py --path-report
python scripts/build_codex_marketplace.py --check
python scripts/skills.py validate
python scripts/skills.py audit --all
git diff --exit-code
git status --short
```

All required checks must be green.

Publish the temporary candidate branch and require real GitHub CI PASS on the exact SHA.

Run isolated install/update smoke:

- fresh candidate install yields PDF 0.3;
- upgrade from formal 5.4.4 / PDF 0.2 yields 0.3;
- installed skill bytes match the release candidate;
- use existing canonical installer/update surfaces only.

Then, before any `release` ref movement, run exactly one **released normal-entry delivery smoke** on that installed candidate:

- use one public-safe minimal Chinese/English + math input;
- invoke the installed candidate through its normal PDF production route, not a helper-only bypass;
- renderer + existing QA must PASS;
- save the produced smoke PDF in a task-owned local/private export path outside tracked release payload;
- record path/size/SHA-256 only for artifact identity;
- the smoke's first completion response must begin with the real host file entry for that exact QA-passed PDF;
- server path/hash/receipt/preview/`queued`/“文件位于 xxx” are not delivery PASS;
- no second user request may be needed before the file entry appears;
- preserve this same smoke PDF for the overall Goal's final user-visible completion reply, which must also begin with its real host file entry;
- do not advance `release` or close Issue #101 before this smoke PASS.

If product blobs still match REVIEW_2 and this smoke fails, repair only release/install/load/normal-entry/delivery wiring within the existing release scope and rerun this one smoke. If a product-byte change is required, stop and return to Planner/Critic. Do not rerun D2/D3 or create REVIEW_3 while product bytes remain unchanged.

### G4.1 — installed-candidate normal-entry delivery smoke

PASS only when the exact installed 5.4.5 / PDF 0.3 candidate produces one public-safe QA-passed smoke PDF through the normal production route and the **first completion response** begins with the real host file entry for that same PDF. Artifact path/size/hash bind identity only and cannot substitute for delivery. Preserve that PDF for the final Goal reply. No release movement or Issue #101 closure is allowed before this Gate PASS.

This Gate binds the final distribution identity to the already accepted D1 behavior. It does not reopen D1–D3 and does not add another Reviewer round.

### G5 — formal release publication

Immediately before publication:

- require G4.1 PASS and preserve the exact smoke PDF for final user delivery;
- fetch and re-read `origin/release`;
- require it has not moved from the baseline used to build the candidate;
- prove it is an ancestor of the validated candidate;
- use `ai-skills-repository-maintainer` formal release producer;
- advance `refs/heads/release` fast-forward-only / non-force;
- read back the remote exact SHA and version identities.

No force, rebase, tag, GitHub Release, registry publication or alternate release engine is authorized.

### G6 — latest-main reintegration and maintenance closure

After formal 5.4.5 exists:

- fetch latest main;
- integrate the exact formal release commit into latest main by ordinary non-force merge/integration;
- preserve all unrelated main work;
- reconcile only shared release metadata/version assertions;
- retain PIE/Research Authoring/Presentations unreleased work;
- set main repository formal version identity to 5.4.5 while PIE remains the future 5.5.0 minor;
- keep Chinese Math PDF 0.3;
- validate PDF/standalone/version/generated parity;
- prove the exact release commit is an ancestor of final main;
- before deleting the original PDF task branch, preserve its durable Reviewed Handoff control/review/evidence artifacts and this approved release-recovery package on final main, while explicitly excluding private exports and the task branch's obsolete combined-5.5.0 shared release metadata;
- publish main non-force, verify remote readback, and prove the exact formal 5.4.5 release commit is an ancestor of remote main.

Only then perform maintenance closure:

- real Clear Writing invocation for reader-facing Issue #101 closure;
- Issue #101 closed;
- Project Status DONE;
- Area `standalone-skill`;
- Resolution commit = final main integration commit;
- canonical PDF TODO = `PROMOTED_IN_5.4.5`, `tracking: #101`;
- clean and delete the exact temporary release-candidate workspace and the original PDF task branch/worktree only after their required durable evidence has been preserved on main.

If Project-field mutation is unavailable, do not falsely claim DONE; record the exact pending Project mutation. The successful formal release/main integration remains valid and is not rolled back.

## Main conflict boundary

Routine metadata reconciliation is limited to:

- VERSION
- CHANGELOG
- README
- registry
- catalog
- repository/standalone version assertion tests
- Issue #101 PDF TODO entry

Any conflict in PDF product bytes, PIE/Research Authoring/Presentations production bytes, central plugin source, profile/routing/shared runtime or generator semantics stops main integration and returns to Planner.

A post-release main-integration conflict does not invalidate the already-published 5.4.5 release.

## Forbidden

Do not:

- reopen REVIEW_2;
- create REVIEW_3;
- create a successor PDF task;
- rerun D1/D2/D3 with unchanged product bytes;
- merge current main into the release candidate;
- cherry-pick arbitrary main/task history;
- modify or review PIE, Research Authoring or Presentations product behavior;
- bump central plugins;
- change Bridge Kit;
- use force / force-with-lease / history rewrite;
- publish tags or a GitHub Release;
- use paid models/APIs;
- transfer private data;
- replace the canonical release producer.

## Positive completion

The Goal is complete when:

- formal `release` is exactly repository 5.4.5 with Chinese Math PDF 0.3;
- release candidate product bytes equal the accepted REVIEW_2 bytes;
- full release validation, GitHub CI and install/update smoke pass;
- the installed-candidate normal-entry delivery smoke PASSes before release movement;
- the exact smoke PDF remains available for the final user-visible completion reply;
- the final user-visible completion reply begins with that PDF's real host file entry, without requiring a second request;
- release advancement is verified fast-forward-only;
- release commit is an ancestor of latest main after reintegration;
- unrelated main work is preserved;
- Issue #101 is closed and Project is DONE, or the only explicitly reported remainder is an unavailable Project-field mutation surface;
- required task control/review/evidence files are durably preserved on main without importing obsolete 5.5.0 shared metadata;
- release-candidate and PDF task branches/worktrees are cleaned only after all required remote state is safely preserved.

Do not claim PIE, Research Authoring or Presentations are formally released by this Goal.
