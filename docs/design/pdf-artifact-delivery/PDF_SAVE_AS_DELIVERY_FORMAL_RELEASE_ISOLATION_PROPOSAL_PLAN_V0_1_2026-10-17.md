# PDF Save-as Delivery — Formal Release Isolation Proposal / Plan v0.1

Status: REVISED FOR INDEPENDENT CRITIC R1; NOT AUTHORIZED FOR EXECUTION  
Date: 2026-10-17  
Revision scope: closes only `PDF-REL-B1_RELEASED_NORMAL_ENTRY_DELIVERY_SMOKE`; all other R0-approved release-isolation decisions remain unchanged.

## 1. Active context

- Repository: `YuukiAS/AI_Skills_Collection`
- Existing task: `documents-media--pdf-save-as-delivery`
- Existing task branch: `reviewed/documents-media--pdf-save-as-delivery`
- Existing task worktree: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-documents-media--pdf-save-as-delivery`
- Accepted implementation commit: `5c92bf4f599d378ff68444b0fa85f5d56bbbd628`
- Independent implementation review: `REVIEW_2 = PASS`
- Existing task state: `PASS`
- Accepted standalone Skill target: `render-chinese-math-pdf 0.3`
- Current formal release baseline at this planning round:
  - `origin/release = 06d135d8a6ee62cd41abb40fc5771fcef7f8db25`
  - repository `5.4.4`
  - `render-chinese-math-pdf 0.2`
- Current main has advanced far beyond the formal release line and contains unrelated PIE, Research Authoring, Presentations and other unreleased work. It is not the release candidate for this recovery.
- Tracking Issue: `#101`

This is a release-closure recovery only. It does not reopen PDF product design, D1/D2/D3, REVIEW_2, renderer semantics, privacy boundaries, or the approved PDF artifact identity.

## 2. Core decision

Adopt the already proven **release-line isolation** pattern used by `slurm-workflows 0.4 / repository 5.4.4`.

The Slurm closure proved the required topology:

1. start from the formal `origin/release` baseline rather than current `main`;
2. keep the release target on a line that is a descendant of the formal release ref;
3. include only the reviewed product/release scope;
4. advance `release` only through the canonical fast-forward-only producer;
5. then integrate that already-formal release back into latest `main`, preserving unrelated main development;
6. require the formal release commit to become an ancestor of `main`.

The current PDF task should use the same release topology, but with an even narrower production scope.

### Adopted release

```text
Repository: 5.4.4 -> 5.4.5  (PATCH)
render-chinese-math-pdf: 0.2 -> 0.3
Central Marketplace plugins: NO_BUMP
Bridge Kit: NO_CHANGE
```

Reason: PDF first-response file delivery is a compatible improvement to an existing standalone capability. It does not create a new repository-level user task and therefore does not justify a repository MINOR.

Project Instructions Editor remains unreleased at repository level. Its future repository MINOR remains `5.5.0`, now naturally based on the then-formal `5.4.5` baseline rather than `5.4.4`.

## 3. Rejected alternatives

### A. Wait for all current main work and publish one large 5.5.0

Rejected for this task. It couples an already accepted standalone PDF fix to unrelated owners and has already caused unnecessary release delay.

### B. Treat current main as the 5.4.5 candidate

Rejected. Current main contains unrelated unreleased production/generated work. Publishing that tree would silently release capabilities outside this task.

### C. Cherry-pick arbitrary main or task history onto release

Rejected. Commit history contains task-control, PIE/repository version metadata and unrelated main ancestry. Release scope must be reconstructed from the formal release baseline plus an explicit allowlist, not inferred from commit ancestry or cherry-picked wholesale.

### D. Re-run D1/D2/D3 on a metadata-only release candidate

Rejected unless PDF production bytes actually change. REVIEW_2 already accepted the product. The release task should prove byte identity and release integrity, not consume another product-review cycle.

R0 Critic requires one narrower exception: after the exact 5.4.5 / PDF 0.3 candidate has been freshly installed or upgraded and its identity verified, run **one release-binding normal-entry delivery smoke**. This smoke does not reopen D1–D3; it binds the already accepted D1 behavior to the final installed release candidate identity.

## 4. Exact isolation workspace

After Critic PASS and only when the user sends the approved Kickoff, create exactly one release-isolation workspace:

```text
branch:
release-candidate/documents-media--pdf-save-as-delivery-5.4.5

worktree:
/overflow/htzhu/mingcheng_new/AI_Skills_Collection-documents-media--pdf-save-as-delivery-release-5.4.5
```

This is **not** a successor Reviewed Handoff task. The existing task key remains `documents-media--pdf-save-as-delivery`; its historical `CURRENT.state=PASS` and `REVIEW_2` stay untouched.

Bootstrap rule:

1. fetch current `origin/release` and `origin/main`;
2. verify repository identity;
3. require `origin/release` still resolves to repository `5.4.4` and `render-chinese-math-pdf 0.2`;
4. require the release candidate branch to be created from that exact current `origin/release` commit;
5. if the formal release baseline has already changed, stop before mutation and return to Planner rather than guessing a new version.

The release candidate may be published as a temporary remote branch only as needed for required GitHub CI. It is deleted after successful formal release + main reintegration + maintenance closure.

## 5. Source allowlist and byte identity

### 5.1 Exact reviewed product bytes

The following files must be copied by exact blob identity from accepted implementation `5c92bf4f...`, not rewritten:

| Path | Accepted Git blob SHA |
|---|---|
| `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md` | `37109d885448a96d423bf664ebf9925714b57a0a` |
| `skills/tools/documents-media/render-chinese-math-pdf/references/checklists.md` | `49dbbdc2cc2283cc2824ed6b32b49716b0a0a7c3` |
| `tests/test_render_chinese_math_pdf.py` | `ae5261e2b10258a7b94ea2a52cfb5b7523461614` |

The renderer itself must remain the formal-baseline/reviewed byte identity:

```text
skills/tools/documents-media/render-chinese-math-pdf/scripts/render_scientific_pdf.py
Git blob SHA = 0598dea9e034b6abd36336e5cf3ba455a81fa27a
```

Any mismatch in these production identities is a STOP condition. Do not silently regenerate/rewrite product source and do not rerun D1–D3 as a way to legitimize an accidental production change.

### 5.2 Release-baseline-derived tests

Do **not** copy the accepted task branch's `tests/test_standalone_skill_baselines.py` wholesale, because that file also contains PIE/main-only state.

Start from the formal 5.4.4 release version and make only the release-required literal changes:

- `render-chinese-math-pdf: 0.2 -> 0.3`
- repository expected version `5.4.4 -> 5.4.5`

Likewise, `tests/test_central_plugin_icon_assets.py` starts from the formal 5.4.4 release version and changes only the repository-version expectation to `5.4.5`.

If another release-baseline test fails solely because it hardcodes the repository version or this standalone Skill version, the Executor may change that exact metadata assertion only. Any semantic test change outside PDF/release metadata is out of scope and stops the release.

## 6. Release metadata construction

All release metadata starts from `origin/release`, not current `main`.

Allowed release-facing changes:

- `VERSION` -> `5.4.5`
- `CHANGELOG.md`
  - keep all formal history through `5.4.4`;
  - add one `5.4.5` section for Chinese Math PDF 0.3 only;
  - central plugins remain `NO_BUMP`;
  - do not import PIE / Research Authoring / Presentations unreleased entries from current main.
- `README.md`
  - repository release `5.4.5`;
  - Chinese Math PDF `0.3`;
  - concise first-response delivery description;
  - no PIE card or other main-only unreleased capability.
  - before any README mutation is finalized, actually invoke the installed Clear Writing / `writing-style` production path on the affected reader-facing text. Reading its source or self-editing does not count.
- `docs/SKILL_CATALOG.md`
- `registry.json`
  - both regenerated from the isolated release source using the canonical repository generator;
  - only repository/PDF release deltas are allowed.
- `docs/skill-todos/render-chinese-math-pdf.md`
  - selectively add/update only the Issue #101 entry;
  - `status: PROMOTED_IN_5.4.5`;
  - `tracking: #101`;
  - do not copy unrelated newer TODO entries from main.

Generated central Marketplace payloads, profiles, Presentation/Research Authoring payloads and central plugin versions must remain byte-identical to the 5.4.4 formal baseline. If canonical regeneration tries to change unrelated generated/plugin paths, the candidate fails isolation and must stop.

## 7. Release closure evidence

The isolated release line may add one bounded evidence artifact:

`results/documents-media--pdf-save-as-delivery/FORMAL_RELEASE_CLOSURE_5_4_5.md`

It must record:

- release baseline SHA/version;
- exact release candidate SHA;
- product blob identity checks;
- release diff allowlist;
- deterministic validation and GitHub CI;
- install/update smoke;
- release-binding normal-entry delivery smoke, including installed candidate identity, public-safe input, renderer/QA result, smoke PDF path/size/hash, and the exact first-completion host file entry used for delivery;
- fast-forward release publication readback;
- main reintegration commit/readback;
- Issue #101 / Project closure truth.

Do not copy the entire task-control history into the release line merely for completeness.

## 8. Capability / release gates

### R1 — Formal ancestry and isolation

PASS only if:

- candidate parent history contains current `origin/release`;
- `origin/release..candidate` contains only this Plan's allowlisted PDF product/test/release/evidence paths;
- no PIE, Research Authoring, Presentations, other plugin production, profile, routing, shared runtime or generated payload is present;
- central plugin versions equal the formal 5.4.4 baseline.

A diff that merely “looks small” is not enough; record the actual changed-path set.

### R2 — Accepted PDF byte identity

PASS only if:

- `SKILL.md`, checklist and PDF delivery regression blob identities match the accepted REVIEW_2 product candidate values above;
- renderer script remains `0598dea...`;
- no other PDF production file changed;
- D1/D2/D3 are not rerun because product bytes are unchanged.

Any product-byte mismatch returns to Planner; do not reinterpret REVIEW_2.

### R3 — Version, README and generated parity

PASS only if:

- repository version = `5.4.5`;
- standalone PDF version = `0.3`;
- all central plugins = unchanged;
- README / CHANGELOG / VERSION / registry / catalog agree;
- README affected text has a real Clear Writing invocation record;
- source -> generated check is clean;
- central Marketplace generated payloads remain formal-baseline identical;
- the release line does not contain PIE or other main-only unreleased release metadata.

### R4 — Deterministic release validation + CI + install/update smoke

Because this isolated candidate is built from the known formal release baseline, it must be fully green; the earlier main-vs-candidate differential exception is **not** used here.

At minimum run on the exact release candidate:

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

Then publish the temporary release-candidate branch and require the repository's real release/integration GitHub CI to PASS on that exact SHA.

Install/update smoke must use an isolated temporary Codex home / task-owned fixture and the repository's existing canonical installer/update path:

- fresh install from the 5.4.5 candidate loads Chinese Math PDF 0.3;
- upgrade starting from formal 5.4.4 / Chinese Math PDF 0.2 converges to 0.3;
- installed `SKILL.md` matches the release candidate byte identity;
- no live user/global install is required merely for smoke;
- do not invent a second installer/updater.

### R4.1 — Released normal-entry delivery smoke

This is the only R0 Critic repair and is a **pre-release gate**. It is not D1/D2/D3 rerun and does not create REVIEW_3.

Run it only after the exact 5.4.5 / `render-chinese-math-pdf 0.3` candidate has passed fresh-install / upgrade identity checks.

1. Use one public-safe, minimal mixed Chinese/English + mathematical input.
2. Invoke the **installed candidate's normal PDF production route**. A direct helper-only/script-only invocation is insufficient if it bypasses the installed normal entry.
3. The normal route must render the PDF with the existing renderer and complete the existing PDF QA successfully.
4. Persist the smoke PDF in a task-owned local/private export location outside tracked release payload, for example:
   `private/exports/documents-media--pdf-save-as-delivery/release-5.4.5-smoke/release-delivery-smoke.pdf`.
   Do not commit the binary PDF into the public repository and do not upload it to any external service.
5. Record path, byte size and SHA-256 only to bind artifact identity. Those values are **not** delivery evidence.
6. The installed-candidate smoke's **first completion response** must begin with the real host file entry for this exact QA-passed smoke PDF.
7. A server path, hash, renderer receipt, preview image, `queued` state, or prose such as “the file is at …” is not PASS.
8. The user must not need a second “PDF 呢 / give me the PDF” request before the file entry appears.
9. The host file entry must resolve to the same PDF identity recorded in step 5.
10. Preserve this same smoke PDF for the overall release Goal's final user-visible completion response. The final response after release/main closure must also begin with the real host file entry for this exact smoke PDF, followed only then by the concise release result.
11. The pre-release smoke is PASS only when items 1–9 are directly observed. **Do not advance `release` or close Issue #101 before this pre-release smoke PASS.**
12. If the smoke fails while the frozen product blobs still match REVIEW_2, classify and repair only release/install/load/normal-entry/delivery wiring inside the already authorized release scope, then rerun this one smoke.
13. If closing the smoke requires changing any accepted PDF production blob, stop and return to Planner/Critic. Only then would affected product evidence need reconsideration.
14. Do not rerun D2/D3, renderer/math/font/template qualification, or create another Reviewer round when product blobs remain unchanged.

The existing user's prior confirmation that this Codex host-local file-entry form opens and can be saved remains channel evidence; no extra user confirmation click is required for this smoke.

### R5 — Formal publish

Immediately before moving `release`:

0. require `R4.1 — Released normal-entry delivery smoke = PASS` and preserve the exact smoke PDF for the final user-visible reply;
1. fetch `origin/release`;
2. require it is still the exact baseline used to build the candidate;
3. prove baseline is an ancestor of the exact validated candidate;
4. use the current `ai-skills-repository-maintainer` formal producer path;
5. update `refs/heads/release` non-force / fast-forward-only;
6. verify remote ref equals the exact validated candidate SHA;
7. verify `release/VERSION=5.4.5` and Chinese Math PDF `0.3`.

If the producer entry is unavailable or the ref moved, stop. No raw force push, ref overwrite, rebase, history replacement or alternate release engine.

This follows Git's normal fast-forward safety property: a fast-forward target is a descendant of the previous ref and therefore preserves the previous history.

### R6 — Reintegration to latest main and maintenance closure

After formal 5.4.5 publication:

1. fetch latest `origin/main`;
2. integrate the exact formal 5.4.5 release commit into latest main by ordinary non-force merge/integration;
3. preserve all unrelated main work;
4. resolve shared metadata from the latest main side plus the now-formal 5.4.5 facts:
   - `VERSION=5.4.5`;
   - retain main's PIE/Research Authoring/Presentations unreleased work;
   - retain PIE's future repository MINOR target `5.5.0`;
   - Chinese Math PDF = `0.3`;
   - preserve central plugin versions unless another independently authorized main task already changed them;
   - preserve main-only registry/catalog entries while applying formal 5.4.5 / PDF 0.3 identity.
5. run targeted version/generated parity + PDF/standalone regression on the integrated main result;
6. verify the exact formal 5.4.5 release commit is an ancestor of the final `main`;
7. before deleting the original PDF task branch, preserve its durable control/review/evidence artifacts on final main without importing its obsolete 5.5.0 shared metadata: copy the task-local `automation/reviewed_handoff/tasks/documents-media--pdf-save-as-delivery/**`, the durable `results/documents-media--pdf-save-as-delivery/**` text evidence needed for audit, and this approved design/Goal/Kickoff package; do not copy private exported PDFs or task-branch VERSION/README/CHANGELOG/registry/catalog state;
8. ordinary non-force publish main and verify the formal 5.4.5 release commit is an ancestor of that remote main;
9. only after readback succeeds:
   - actually use Clear Writing before reader-facing Issue #101 closure text;
   - set Issue #101 closed;
   - set Project Status = `DONE`, Area = `standalone-skill`, Resolution commit = final main integration commit;
   - keep canonical TODO `tracking: #101` and `PROMOTED_IN_5.4.5`;
   - remove the exact temporary release-candidate branch/worktree and the original PDF task branch/worktree only when clean/pushed, their required durable evidence is preserved on main, and they are no longer needed.

If Project mutation is unavailable, formal 5.4.5 publication and main integration remain truthful, but the overall maintenance closure must report the exact pending Project mutation and must not falsely claim `DONE`. Do not roll back a valid release merely because the board UI surface is unavailable.

## 9. Main reintegration conflict policy

Expected shared conflicts are release metadata, not product redesign.

Allowed reconciliation areas:

- `VERSION`
- `CHANGELOG.md`
- `README.md`
- `registry.json`
- `docs/SKILL_CATALOG.md`
- standalone/version assertion tests
- canonical PDF TODO Issue #101 entry

For these files, preserve latest-main unrelated content and apply only the formal 5.4.5 / PDF 0.3 facts.

Any conflict in PDF production files, central plugin production files, Presentations, Research Authoring, PIE production source, profiles, shared runtime or generator semantics is not a routine merge conflict. Stop and return to Planner.

Task evidence preservation is allowed only as non-production documentation/control evidence. It must not reintroduce the task branch's obsolete combined-5.5.0 VERSION/README/CHANGELOG/registry/catalog candidate.

## 10. Authorization envelope

The Critic-approved Kickoff may authorize only:

- creation of the exact release-candidate branch/worktree above from `origin/release`;
- source/test/metadata/evidence edits inside the allowlist;
- canonical generator use;
- local deterministic validation;
- temporary candidate branch publication and ordinary CI;
- task-owned isolated install/update smoke;
- one public-safe installed-candidate normal-entry delivery smoke that produces a local task-owned PDF and exposes it only through the current host's real file entry; no external upload;
- one exact fast-forward-only `release` ref advancement after all gates PASS;
- ordinary non-force integration of that released commit into latest `main`;
- Issue #101 / Project closure and exact branch/worktree cleanup after success.

Not authorized:

- force push / force-with-lease;
- rebase of published history;
- reset/clean/restore of unrelated work;
- arbitrary cherry-picking of main history;
- any Product/Research Authoring/Presentations/PIE product modification or review;
- central plugin version bump;
- Bridge Kit modification;
- paid API/model use;
- external/private data transfer;
- D1/D2/D3 rerun unless accepted product bytes changed;
- a successor PDF task or REVIEW_3.

## 11. Recovery / stop conditions

Stop before release ref mutation if any of these occur:

- `origin/release` is no longer the planned 5.4.4 baseline;
- candidate is not a descendant of the current formal release ref;
- allowlist isolation fails;
- accepted PDF product bytes mismatch;
- full release validation or GitHub CI fails;
- install/update smoke fails;
- the pre-release installed-candidate normal-entry delivery smoke fails, or its first completion response lacks the exact QA-passed PDF host file entry;
- Clear Writing required for README is unavailable;
- canonical release producer is unavailable;
- release ref cannot fast-forward;
- release metadata becomes inconsistent.

After release publication, a conflict while integrating into main does not invalidate the formal 5.4.5 release. Preserve the release and stop only the main-integration step if the conflict exceeds the allowed metadata reconciliation boundary.

## 12. Positive completion

This recovery is complete only when all are true:

```text
FORMAL_RELEASE_5_4_5 = PASS
RENDER_CHINESE_MATH_PDF_VERSION = 0.3
CENTRAL_PLUGIN_BUMPS = NONE
PDF_REVIEWED_PRODUCT_BYTES_UNCHANGED = YES
FULL_RELEASE_VALIDATION = PASS
GITHUB_RELEASE_CANDIDATE_CI = PASS
INSTALL_UPDATE_SMOKE = PASS
RELEASED_NORMAL_ENTRY_DELIVERY_SMOKE = PASS
SMOKE_PDF_IDENTITY_BOUND = YES
FINAL_USER_REPLY_STARTS_WITH_SMOKE_PDF_FILE_ENTRY = YES
RELEASE_FAST_FORWARD_VERIFIED = YES
RELEASE_REMOTE_READBACK = PASS
RELEASE_COMMIT_IS_MAIN_ANCESTOR = YES
MAIN_UNRELATED_WORK_PRESERVED = YES
ISSUE_101 = CLOSED
PROJECT_STATUS = DONE
TASK_EVIDENCE_PRESERVED_ON_MAIN = YES
TASK_BRANCH_CLEANUP = COMPLETE
```

If only Project-field mutation is unavailable, report the release/integration as complete and the board mutation as the one explicit remaining administrative item; do not reopen product or release work.

## 13. External practice check

A targeted check of official Git documentation confirms the frozen producer model: a fast-forward update requires the new ref target to descend from the old target and preserves the old history. The design therefore keeps `release` advancement strictly descendant-only and forbids force/non-fast-forward publication.

No external practice changes the repository's stronger owner/version/isolation rules; those remain authoritative.
