# PDF-only formal release closure: repository 5.4.5

Date: 2026-10-17

Task: `documents-media--pdf-save-as-delivery`

Outcome: `PASS`

## Released identity

- Formal baseline: `origin/release` at `06d135d8a6ee62cd41abb40fc5771fcef7f8db25`, repository `5.4.4`, `render-chinese-math-pdf` `0.2`.
- Isolated release candidate and formal release commit: `39e2f20c53a07936f8dc5a289f3af41a83943b75`.
- Released repository version: `5.4.5`.
- Released standalone skill version: `render-chinese-math-pdf` `0.3`.
- Central plugin versions: `NO_BUMP`.
- Main integration commit: `c42b58f5c37b63f2197d50436f7df23409584641`.
- The formal release commit is an ancestor of the main integration commit.

The release candidate was built from the exact formal baseline rather than from `main`. It contained only these approved paths relative to the baseline:

- `CHANGELOG.md`
- `README.md`
- `VERSION`
- `docs/SKILL_CATALOG.md`
- `docs/skill-todos/render-chinese-math-pdf.md`
- `registry.json`
- `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`
- `skills/tools/documents-media/render-chinese-math-pdf/references/checklists.md`
- `tests/test_central_plugin_icon_assets.py`
- `tests/test_render_chinese_math_pdf.py`
- `tests/test_standalone_skill_baselines.py`

The Marketplace source and generated central-plugin trees were byte-identical to the `5.4.4` formal baseline. The candidate did not include PIE, Research Authoring, Presentations, or other `main`-only production or generated changes.

## Accepted PDF byte identity

The release candidate retained the product bytes independently accepted in `REVIEW_2`:

| Path | Git blob | SHA-256 |
| --- | --- | --- |
| `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md` | `37109d885448a96d423bf664ebf9925714b57a0a` | `dde241640e911374319262a23b90c6fdfa3eb0234aed10f11272d279e1606885` |
| `skills/tools/documents-media/render-chinese-math-pdf/references/checklists.md` | `49dbbdc2cc2283cc2824ed6b32b49716b0a0a7c3` | `2f1815f6c12e2f35ddbaa47823d33be8dbef3302ca3e7c8e787ab41b883538f0` |
| `tests/test_render_chinese_math_pdf.py` | `ae5261e2b10258a7b94ea2a52cfb5b7523461614` | `4f064740bbf1a14d2b3c2652897a02a6909307b735ae82489a8a834b7b0c515b` |
| `skills/tools/documents-media/render-chinese-math-pdf/scripts/render_scientific_pdf.py` | `0598dea9e034b6abd36336e5cf3ba455a81fa27a` | `70b9084a5c51acd6e02f85a0f6ae33531108bb5495f3d37bac9a340e06a148d3` |

Because these product bytes did not change, D1, D2, and D3 were not rerun and `REVIEW_2` was not reopened.

## Release validation

The exact candidate `39e2f20c53a07936f8dc5a289f3af41a83943b75` passed:

- Full repository suite: `333 passed`.
- Focused PDF/version suite: `36 passed`.
- Marketplace generation write, validation, path report, and clean parity checks.
- Skills validation and audit.
- Fresh-install identity smoke on the candidate: installed PDF `0.3`; installed `SKILL.md` SHA-256 matched `dde241640e911374319262a23b90c6fdfa3eb0234aed10f11272d279e1606885`.
- Upgrade identity smoke from exact formal baseline `5.4.4 / PDF 0.2` to the candidate: pre-update PDF `0.2` SHA-256 `73510fd20d9a671d995a7447144a842c46b7478bcc910cafeaefa82fbf244e20`; post-update PDF `0.3` SHA-256 matched the accepted candidate.
- GitHub Actions run `39017846748` at exact candidate head: Marketplace, Ubuntu editable-install smoke, Windows editable-install smoke, and Windows sparse-checkout all passed.

The first local full-suite attempt produced two environment-only failures because a sibling worktree was read-only. The same exact candidate and commands were rerun with normal workspace permissions and passed all 333 tests. This did not change the candidate.

Historical run `38706208966` remains recorded as `FAIL`; it was not relabeled or used as release PASS evidence.

## Release-binding normal-entry delivery smoke

After fresh install and upgrade identity checks, one release-binding smoke used a public-safe minimal Chinese/English/mathematics input and the installed project-local PDF `0.3` skill. The first invocation used the machine PATH Codex `0.142.0` and stopped before product execution because the default model required a newer Codex runtime. It generated no PDF and no completion reply. The allowed wiring retry used the current Codex `0.160.1` against the same installed candidate.

The successful normal-entry run:

- Loaded the installed project-local `render-chinese-math-pdf` `0.3` skill.
- Used the production Pandoc to XeLaTeX route.
- Returned renderer status `complete`.
- Passed equation survival and existing PDF QA with no errors.
- Produced one readable A4 page; every page was visually inspected.
- Began its first completion reply with a real host file entry for that exact QA-passed PDF.

Durable local artifact:

- Path: `private/exports/documents-media--pdf-save-as-delivery/release-5.4.5-smoke/release-delivery-smoke.pdf`
- Size: `27169` bytes
- SHA-256: `dad21e87ad5720aaadfc820f43e281c1e405a0ae646c2f05928a9f4e25df0da3`

The QA warning `CJK text found but no obvious CJK font name was detected in pdffonts` was non-fatal. Direct `pdffonts` inspection found `NotoSerifSC-Regular` embedded, subset, and Unicode-enabled, alongside TeX Gyre Termes and the math font.

## Reader-facing writing check

The installed `writing-style:chinese-prose` instructions were loaded and applied to the changed README region and the Issue #101 closure copy. A bounded `ai-bridge plugin-replay` attempt (`20261017T082801Z-1aa24bb5e492`) stopped before a child run with `WRITE_ISOLATION_NOT_ENFORCEABLE`; no raw nested Codex command was used to bypass that boundary. The current session then performed the required Clear Writing review directly, preserving all release facts and machine strings.

## Publication and integration

The existing `ai-skills-repository-maintainer` formal producer advanced `refs/heads/release` once, non-force and fast-forward-only, from `06d135d8a6ee62cd41abb40fc5771fcef7f8db25` to `39e2f20c53a07936f8dc5a289f3af41a83943b75`. Remote readback confirmed repository `5.4.5` and PDF `0.3`.

The exact release was then merged normally into the latest `main`, preserving all unrelated `main` work. Conflicts were limited to the Goal-approved metadata, TODO, and version-assertion surfaces; there were no product, shared-runtime, or generator semantic conflicts. The resulting remote main integration was `c42b58f5c37b63f2197d50436f7df23409584641`, with the formal release commit as an ancestor. Post-merge focused tests, Marketplace parity, and skills validation passed.

## Maintenance closure and cleanup

- Issue #101 was updated with the real release evidence and closed as completed.
- Project Status: `DONE`.
- Project Area: `standalone-skill`.
- Project Resolution commit: `c42b58f5c37b63f2197d50436f7df23409584641`.
- The task's Reviewed Handoff control, review, design, Goal, and release-closure evidence were retained on `main`.
- Private exports and obsolete combined-5.5.0 metadata were not committed to `main`.
- The release-candidate and Reviewed task worktrees were removed.
- Remote and local branches `release-candidate/documents-media--pdf-save-as-delivery-5.4.5` and `reviewed/documents-media--pdf-save-as-delivery` were deleted after durable evidence and artifact preservation.

`FORMAL_RELEASE_CLOSURE=PASS`
