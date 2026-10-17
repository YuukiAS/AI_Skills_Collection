# PDF delivery CI baseline differential

## Decision

`PASS` for the frozen broad differential regression gate.

This is not an all-green repository result. The historical GitHub Actions run
`38706208966` remains `FAIL`. The result here proves only that the exact PDF
final candidate adds no full-suite failure and does not add or worsen any
generated/publication difference relative to then-current `main`.

## Bound identities

- Then-current main:
  `362a8cab6991120a79600352d070926e2602dcbd`
- Exact PDF final candidate:
  `5c92bf4f599d378ff68444b0fa85f5d56bbbd628`
- Candidate product files were not changed or rebased for this comparison.
- Main and candidate were checked out as separate detached worktrees. Neither
  snapshot was merged into the other.
- The workflow file was byte-identical at both commits:
  `.github/workflows/codex-marketplace.yml`, SHA-256
  `d4f3443b365dfca560bba6a04a84292c369f90686062f0402393f053d7d7834e`.

The baseline was refreshed immediately before execution with
`git fetch --all --prune`. At that point `origin/main` resolved to the main
SHA above. The stronger ordinary all-green route was unavailable because the
same repository-level command on main returned five failures.

## Shared environment and commands

Both snapshots used the same host, interpreter, venv, environment variables,
dependencies, and commands.

- Host: Linux `5.14.0-611.16.1.el9_7.x86_64`
- Python: `3.12.4`
- Git: `2.47.3`
- Shared venv: `/tmp/pdf-save-delivery-diff-venv`
- Environment:
  `LD_LIBRARY_PATH=/nas/longleaf/rhel9/apps/python/3.12.4/lib`,
  `MPLCONFIGDIR=/tmp/pdf-save-delivery-mpl-cache`,
  `PYTHONHASHSEED=0`, `TZ=UTC`, `LC_ALL=C.UTF-8`
- Workflow dependencies:
  `Pillow 12.3.0`, `python-pptx 1.0.2`, `matplotlib 3.11.2`
- GitHub-runner baseline packages needed by discovered tests:
  `setuptools 84.0.0`, `PyYAML 6.0.3`

The first isolated-main preflight lacked `setuptools` and `PyYAML` and
therefore discovered only 328 tests with two environment import/setup errors.
That preflight was discarded. Both authoritative snapshots were rerun from the
beginning after the same shared venv received those GitHub-runner baseline
packages.

Commands reproduced from the real `Codex Marketplace` workflow:

```text
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

The candidate additionally ran the frozen target gate:

```text
python -m unittest tests.test_render_chinese_math_pdf tests.test_standalone_skill_baselines
```

## Target gate

The exact candidate passed all 32 PDF and standalone tests:

```text
................................
----------------------------------------------------------------------
Ran 32 tests in 1.854s

OK
```

The candidate still binds the unchanged product implementation commit and the
previously accepted D1-D3 artifacts. No PDF was rerendered.

## Full-suite comparison

| Snapshot | Tests run | Failure count | Exit |
|---|---:|---:|---:|
| main `362a8cab...` | 338 | 5 | 1 |
| candidate `5c92bf4f...` | 340 | 4 | 1 |

The two extra candidate tests are the task's passing delivery-contract
regressions. Candidate-only failure set: **empty**.

Main-only failure:

```text
FAIL: test_marketplace_keeps_canonical_icon_paths_and_versions
  (test_central_plugin_icon_assets.CentralPluginIconAssetTests.test_marketplace_keeps_canonical_icon_paths_and_versions)
Traceback:
  File "<SNAPSHOT>/tests/test_central_plugin_icon_assets.py", line 49
    self.assertEqual((REPO_ROOT / "VERSION").read_text(encoding="utf-8").strip(), "5.5.0")
AssertionError: '5.4.4' != '5.5.0'
- 5.4.4
+ 5.5.0
```

Normalized diagnostic SHA-256:
`52b3c5a6bd42054c97ea60703da52a1dc1f89bb22f1f3ef6749ea1aa488eff06`.
The candidate does not reproduce this main-side version failure.

The four inherited failures have identical normalized traceback and assertion
diagnostics on main and candidate:

### Central source-only TODO inbox

Diagnostic SHA-256 on both snapshots:
`a78e728c639e0bfd61fae059a59fb33360980e8da2274fd6a38f64ff944fa9de`.

```text
FAIL: test_central_plugins_have_exactly_one_source_only_todo_inbox
  (test_codex_marketplace.CodexMarketplaceTests.test_central_plugins_have_exactly_one_source_only_todo_inbox)
Traceback:
  File "<SNAPSHOT>/tests/test_codex_marketplace.py", line 158
    self.assertEqual(todo_names, plugin_names)
AssertionError: Items in the first set but not the second:
'research-authoring-student-assessment-workflow'
'research-writing-student-audience-and-pre-render-approval'
'reader-facing-document-composition-protocol'
'research-authoring-production-workflow'
'presentations-authoring-production-workflow'
'presentations-core-history-lock'
'research-authoring-layout-convergence-and-human-review-budget'
```

### Generated layer freshness assertion

Diagnostic SHA-256 on both snapshots:
`47f26c970730e18d6384a0aab6a80f0fb34e9955871d88d7fd487f15c65096e9`.

```text
FAIL: test_generated_layer_matches_source_config
  (test_codex_marketplace.CodexMarketplaceTests.test_generated_layer_matches_source_config)
Traceback:
  File "<SNAPSHOT>/tests/test_codex_marketplace.py", line 450
    self.assertEqual(summary["errors"], [])
AssertionError: Lists differ: ['publication layer is not current (16 differences)'] != []

- ['publication layer is not current (16 differences)']
+ []
```

The actual 16 paths and their content-level patches are compared below rather
than treating this count as sufficient evidence.

### Plugin TODO / changelog set

Diagnostic SHA-256 on both snapshots:
`9a209efb08add6c2fa6aceddd2a64c9433eebea1bbdbe3a25b6e1cb58aed3f69`.

```text
FAIL: test_plugin_changelogs_match_marketplace_set_and_versions
  (test_codex_marketplace.CodexMarketplaceTests.test_plugin_changelogs_match_marketplace_set_and_versions)
Traceback:
  File "<SNAPSHOT>/tests/test_codex_marketplace.py", line 355
    self.assertEqual(todo_names, set(CENTRAL_PLUGIN_NAMES))
AssertionError: Items in the first set but not the second:
'research-authoring-student-assessment-workflow'
'research-writing-student-audience-and-pre-render-approval'
'reader-facing-document-composition-protocol'
'research-authoring-production-workflow'
'presentations-authoring-production-workflow'
'presentations-core-history-lock'
'research-authoring-layout-convergence-and-human-review-budget'
```

### Presentations source / mirror mismatch

Diagnostic SHA-256 on both snapshots:
`85e0031c940b42f7dfc13601c3fc6a09f659a5625f2855702c49ec3a79a4e551`.

```text
FAIL: test_research_presentation_todo_consolidation_and_promotions
  (test_presentations.PresentationSharedTests.test_research_presentation_todo_consolidation_and_promotions)
Traceback:
  File "<SNAPSHOT>/tests/test_presentations.py", line 2669
    self.assertEqual(source.read_text(encoding="utf-8"), mirror.read_text(encoding="utf-8"))
AssertionError: '---\\[503 chars]2026-07-28\\nprofile_tags:\\n  - presentations\\n[14707 chars]/`\\n'
 != '---\\[503 chars]2026-10-06\\nprofile_tags:\\n  - presentations\\n[17183 chars]/`\\n'
Diff is 22710 characters long.
```

The assertion truncates its values, so an independent full unified diff was
also generated between:

```text
skills/tools/documents-media/presentations/research-presentations/SKILL.md
plugins/codex/plugins/presentations/skills/research/SKILL.md
```

On both snapshots that diff is exactly 70 lines / 13059 bytes with SHA-256
`e717912cf1ead873d8e2c7a16390e1443e4d8c032cce7f42fe92437d29e14d5d`.
Its content shows the same `last_reviewed` mismatch
(`2026-07-28` versus `2026-10-06`) and the same mirror-only
pre-execution/anti-shortcut/independent-review workflow additions. There is no
candidate-side hunk, size increase, or diagnostic change.

## Generated/publication comparison

Both snapshots were clean before `--write`. On both snapshots:

- `--write`: exit 0
- `--validate`: exit 0
- `--path-report`: exit 0
- `--check`: exit 0
- `skills.py validate`: exit 0; 155 active skills and 18 profiles
- `skills.py audit --all`: exit 0
- final `git diff --exit-code`: exit 1 because the same generated drift
  remains relative to each commit

The complete generated patch is byte-for-byte identical between main and
candidate: 6420 lines / 231120 bytes, SHA-256
`f2e3fae20040761ed78a5ce9b86150df584749f7b57491ed14580428da9c2a14`.

Path-level status, line delta, and content-patch SHA-256 are identical:

| Status | + | - | Patch SHA-256 | Path |
|---|---:|---:|---|---|
| D | 0 | 270 | `e13478636a4eee4d4f8c773db4125a9929db41dec34da993dca11d86d1a8e3f1` | `plugins/codex/plugins/presentations/shared/anti-shortcut-production-contract.md` |
| D | 0 | 616 | `a162c2a4179ee5838a315d4b00875b623685f66f718c2dea1b1071340d467000` | `plugins/codex/plugins/presentations/shared/authoring-production-workflow.md` |
| D | 0 | 189 | `986f9b61a25031d430cc0bdbb22c28a4a0ea9127be3c82916b18d75e77937633` | `plugins/codex/plugins/presentations/shared/chatgpt-web-authoring-contract.md` |
| D | 0 | 230 | `95f63c4295165392ee7088ad192649b55af771d87bc5564d6ee4ffa74775cf54` | `plugins/codex/plugins/presentations/shared/independent-review-contract.md` |
| D | 0 | 321 | `0c9f0062d5282ccf85738cf2f4929d4ee6ced0d60aba9d0c8e1100e0b1e03bf7` | `plugins/codex/plugins/presentations/shared/pre-execution-cumulative-acceptance-contract.md` |
| D | 0 | 1135 | `f6e0f032015f83822d381f90c7c48dc2f7c08ba0a2ab51a7919df5ecf4824980` | `plugins/codex/plugins/presentations/shared/presentation-end-to-end-pre-execution-runbook.md` |
| D | 0 | 350 | `50d97487d899aa30564bc811f72722b4f697075c6b10495510c5b6bbe0a641b7` | `plugins/codex/plugins/presentations/shared/rendered-artifact-positive-ancestry-acceptance-contract.md` |
| M | 7 | 17 | `0c0c7bdec463736cf78c5f82fe1cd7284bccfbe46224fedbfd627a4d15287c4e` | `plugins/codex/plugins/presentations/skills/business/SKILL.md` |
| M | 7 | 19 | `bf29718f6d06784fb33440edb9c7810d568387fc971c157a58fed29a6a2c193f` | `plugins/codex/plugins/presentations/skills/research/SKILL.md` |
| M | 0 | 26 | `02bcc2fefd497879beea11c0fbd9208deacff9aa5f6a4aa9948755e9cffacdb8` | `plugins/codex/plugins/presentations/skills/research/references/real-world-presentation-guardrails.md` |
| D | 0 | 29 | `457db494399f8ad3a7a4781ca3eed83e327f6a33271a78ae771bc9e85a06ff3f` | `plugins/codex/plugins/research-writing/shared/README.md` |
| D | 0 | 542 | `fb0f0efa25e982b9a98f6446a5ad46fc3aed55265a83c7ba15ca2d9e4efa63c8` | `plugins/codex/plugins/research-writing/shared/student-assessment-cumulative-acceptance-contract.md` |
| D | 0 | 320 | `764dcc2419f640c9261d4343e695330692da357a6479d336ca441281a109b55f` | `plugins/codex/plugins/research-writing/shared/student-assessment-delivery-closure-amendment-v1.md` |
| D | 0 | 1414 | `e60693eb2b54ef09edd0068490c413c6542009ca98e8e1c5b7be3f1dd5d8ec3b` | `plugins/codex/plugins/research-writing/shared/student-assessment-end-to-end-pre-execution-runbook.md` |
| D | 0 | 399 | `630d503eeaa74aaefd59039d8e93c58c3fee853656dfa87dfd33811a67617bef` | `plugins/codex/plugins/research-writing/shared/student-assessment-hw1-nonrecurrence-amendment-v1.md` |
| D | 0 | 365 | `c2e26668e03a0d4b20aabb6a4245b8fe3bf5ef6bc5ad316f9a0694a07f87a8bf` | `plugins/codex/plugins/research-writing/shared/student-assessment-semantic-pagination-amendment-v1.md` |

For the three modified files, the identical patches remove the same stale
mirror-only workflow text and restore the same source-owned review dates and
content. For the thirteen deleted files, the identical patches remove the same
stale generated-only files. These are observed baseline differences only; this
PDF task did not apply them to its branch.

Candidate-only generated/publication path set: **empty**. Candidate-side
worsening on a shared path: **none**.

## Scope check

The task implementation range from its frozen base
`1c59199f88c7527f2bd853e606f20146134fda47` to the exact candidate contains
only the PDF skill/checklist/tests, task control/evidence, standalone
version/release metadata, registry/catalog, README/CHANGELOG, and the canonical
PDF TODO backlink. It contains no Presentations, Research Authoring, Bridge
Kit, Slurm, or other plugin production repair.

No generated/publication output produced in the detached comparison worktrees
was copied into the task branch.

## Candidate-minus-main delta and conclusion

- Candidate-only full-suite failures: **0**
- Shared failing assertions with changed diagnostics: **0**
- Shared Presentation full-diff changes: **0**
- Candidate-only generated/publication paths: **0**
- Shared generated/publication patches with changed content: **0**
- Candidate target failures: **0**

Therefore the exact candidate introduces no repository regression relative to
then-current main and passes the revised broad differential gate.

This decision does not repair or waive current-main debt. It does not relabel
run `38706208966`; that run remains `FAIL`. It authorizes only the same PDF
final candidate to proceed to independent `REVIEW_2`.
