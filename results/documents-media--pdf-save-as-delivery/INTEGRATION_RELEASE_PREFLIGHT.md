# Integration / Release Preflight — PDF Save-as Delivery

Date: 2026-10-15
Task: `documents-media--pdf-save-as-delivery`
Task branch: `reviewed/documents-media--pdf-save-as-delivery`

## Bound identities

- REVIEW_2 branch tip: `c06bcac136a0bcc87e400c17bc3789299c7551c4`
- PDF product implementation: `5c92bf4f599d378ff68444b0fa85f5d56bbbd628`
- then-current `origin/main`: `362a8cab6991120a79600352d070926e2602dcbd`
- then-current `origin/release`: `06d135d8a6ee62cd41abb40fc5771fcef7f8db25`
- task/main merge base: `1c59199f88c7527f2bd853e606f20146134fda47`
- temporary detached rehearsal merge commit: `2a04ba990be35c830c1f9dfadf322dd1299a39b0`
- temporary rehearsal tree: `e5b353621ae4e22b0e7ab23773b1531b3791794f`

The temporary merge was performed only in
`/tmp/pdf-save-delivery-integration-preflight`. It did not move the task
branch, `main`, or `release`.

## Merge and product-surface result

The history-preserving rehearsal merge completed without conflicts. Current
main added only these four paths relative to the reviewed task tip:

- `docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_EXECUTION_PLAN_V0_3_2026-10-13.md`
- `docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_KICKOFF_DRAFT_V0_3_2026-10-13.md`
- `docs/goals/hpc--slurm-cancel-human-confirmation-goal-draft-v0_3.md`
- `docs/plugin-todos/writing-style.md`

The merge left the PDF source, target tests, `VERSION`, `CHANGELOG.md`,
`README.md`, `registry.json`, generated catalog, and the canonical
`render-chinese-math-pdf` TODO byte-identical to REVIEW_2 commit
`c06bcac1`. D1–D3 and the accepted final PDF identity therefore remain
unchanged.

## Regression rehearsal

Environment and commands matched the accepted differential gate:

- Python 3.12.4 in `/tmp/pdf-save-delivery-diff-venv`
- `LD_LIBRARY_PATH=/nas/longleaf/rhel9/apps/python/3.12.4/lib`
- `MPLCONFIGDIR=/tmp/pdf-save-delivery-integration-mpl`
- `PYTHONHASHSEED=0`, `TZ=UTC`, `LC_ALL=C.UTF-8`

Target gate:

```text
python -m unittest tests.test_render_chinese_math_pdf tests.test_standalone_skill_baselines
Ran 32 tests
OK
```

Full suite:

```text
python -m unittest discover -s tests
Ran 340 tests
FAILED (failures=4)
```

The four failure IDs and normalized diagnostic SHA-256 values exactly match the
accepted REVIEW_2 candidate:

| Failure | Diagnostic SHA-256 |
|---|---|
| `test_central_plugins_have_exactly_one_source_only_todo_inbox` | `a78e728c639e0bfd61fae059a59fb33360980e8da2274fd6a38f64ff944fa9de` |
| `test_generated_layer_matches_source_config` | `47f26c970730e18d6384a0aab6a80f0fb34e9955871d88d7fd487f15c65096e9` |
| `test_plugin_changelogs_match_marketplace_set_and_versions` | `9a209efb08add6c2fa6aceddd2a64c9433eebea1bbdbe3a25b6e1cb58aed3f69` |
| `test_research_presentation_todo_consolidation_and_promotions` | `85e0031c940b42f7dfc13601c3fc6a09f659a5625f2855702c49ec3a79a4e551` |

There is no integration-only failure or diagnostic worsening.

The exact workflow commands below all returned 0:

- `python scripts/build_codex_marketplace.py --write`
- `python scripts/build_codex_marketplace.py --validate`
- `python scripts/build_codex_marketplace.py --path-report`
- `python scripts/build_codex_marketplace.py --check`
- `python scripts/skills.py validate`
- `python scripts/skills.py audit --all`

The post-write Git difference remains the same 16-path inherited publication
difference accepted in REVIEW_2:

- 6,420 lines
- 231,120 bytes
- complete patch SHA-256:
  `f2e3fae20040761ed78a5ce9b86150df584749f7b57491ed14580428da9c2a14`

No generated output was copied back to the task branch.

## Formal-release cleanliness

`origin/release..origin/main` is not limited to non-production documentation
or evidence. It contains unrelated production/generated/plugin/Skill,
distribution, routing, registry, profile, and test changes, including
Project Instructions Editor source and generated Presentations / Research
Authoring payloads.

Under the current formal-release cleanliness contract, this is
`UNRELEASED_PRODUCTION_DRIFT` (class C). This task must not silently absorb
that unrelated work into repository release 5.5.0, revert it, cherry-pick around
it, or move `main` / `release`.

```text
FORMAL_RELEASE_CLEANLINESS_PREFLIGHT=FAIL
WAITING_FOR_FORMAL_RELEASE_BASELINE=YES
READY_FOR_RELEASE=NO
```

This is a release-channel wait, not a PDF product regression. It does not
invalidate D1–D3, the differential gate, REVIEW_2, Chinese Math PDF v0.3
metadata, or the final PDF identity. Historical GitHub Actions run
`38706208966` remains `FAIL`.

Version intent remains:

```text
Repository bump decision: MINOR candidate 5.5.0; not released
Affected central plugins:
- all: NO_BUMP
Standalone skill:
- render-chinese-math-pdf: 0.2 -> 0.3 candidate; accepted but not formally released
```

## Maintenance board and next action

Issue #101 remains open in Project Status `DOING`, Area
`standalone-skill`. Its reader-facing current anchor was updated after a real
Clear Writing review to reference the product implementation, REVIEW_2 PASS,
and this integration-preflight stage. The Issue was not closed and the Project
was not moved to `DONE`.

Next action: wait until the unrelated class-C work completes its own formal
release closure and `origin/release` advances, then refresh both refs and rerun
this same integration preflight. Do not reopen PDF product implementation or
request REVIEW_3 merely because the formal release baseline is waiting.
