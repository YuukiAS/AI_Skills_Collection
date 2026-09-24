# Scientific PDF Rendering Reliability Evidence

Task key: `documents-media--scientific-pdf-rendering-reliability`

Branch: `reviewed/documents-media--scientific-pdf-rendering-reliability`

## Calibration

Starting candidate:

- paper: A4
- body: 11pt
- margin: 25mm
- line spacing: 1.15
- TOC: disabled
- section numbering: disabled
- ordinary prose downscaling: disabled

Representative inputs rendered:

- `inputs/math_regression.md`
- `inputs/representative_formal_note.md`
- `inputs/direct_tex_note.tex`

Visual inspection:

- `renders/initial/math_regression_pages/math_regression-1.png`: Chinese, English, table, hat/subscript, Greek, sum, integral, gradient, matrix, mathbb, and long formula are visible; no Chromium header/footer, mojibake, clipping, or obvious overflow.
- `renders/initial/representative_formal_note_pages/representative_formal_note-1.png`: complete note is readable; normal prose keeps body identity; table is readable; no unrequested TOC or numbering.
- `renders/initial/direct_tex_note_pages/direct_tex_note-1.png`: native `.tex` compiles through direct XeLaTeX and is not round-tripped through Pandoc.

Calibration decision: no evidence-driven profile adjustment was made. The starting candidate is selected and frozen as `canonical-formal-note-v0.2`.

## Route And Profile Receipts

- `renders/initial/math_regression.receipt.json`
- `renders/initial/representative_formal_note.receipt.json`
- `renders/initial/direct_tex_note.receipt.json`

The Markdown receipts record:

- route: `canonical-markdown`
- engine: `pandoc-ast-to-latex-xelatex`
- profile: `canonical-formal-note-v0.2`
- paper: `a4`
- fontsize: `11pt`
- margin: `25mm`
- line spacing: `1.15`
- TOC and section numbering disabled
- ordered `Math(mathtype, text)` signatures
- generated-TeX math-anchor survival checks

The `.tex` receipt records:

- route: `direct-xelatex`
- authority: `source-or-project`
- no Pandoc command in the render command list

## Stability

Same effective profile retry:

- initial receipt: `renders/initial/representative_formal_note.receipt.json`
- retry receipt: `renders/stability/representative_formal_note_retry.receipt.json`
- result: the `effective_profile` objects are identical for authority, route, engine, paper, margin, line spacing, TOC/numbering policy, font policy, resource root, and source path.

The deliberate-format-change semantics are covered by `tests/test_render_chinese_math_pdf.py::test_explicit_format_change_creates_new_effective_profile_identity`, which checks that an explicit Letter profile changes authority/profile id/paper identity instead of being counted as a same-profile stability regression.

## Mechanical PDF QA

`math_regression.pdf`:

- `pdfinfo`: producer `xdvipdfmx`, page size A4, 1 page, non-empty.
- `pdffonts`: embedded/subset Unicode fonts include `TeXGyreTermes`, `TeXGyreTermesMath`, `NotoSerifSC`, and `NewCMMath`.
- `pdftotext -layout`: Chinese text, formula context, and table rows extract.

Generated artifacts:

```text
76c31af07ea05789441384530e95224e23d3db933460c795de22302f2f40364c  renders/initial/math_regression.pdf
278b464c1a9e7d3f333c66facbbc6212efc93c02319de91140b3f08a854d1df5  renders/initial/math_regression.receipt.json
20d315c8cc1179a7dd46e5ab33b67b23208ece4b75136ed07bb6d145b21c3181  renders/initial/math_regression_pages/math_regression-1.png
4a07cd5672ad274ed1826167887e2aed500c2bad34322d07d76b2f8f5d6483d9  renders/initial/representative_formal_note.pdf
7f86f6ad8dee88a8f0eb1cac5741adbf42a774b93e5ae83873e1fa11dc32ddcc  renders/initial/representative_formal_note.receipt.json
e1e64b217468bce861d4205f93edc02e5a09f98840ea8604ffdb1822edce2f6a  renders/initial/representative_formal_note_pages/representative_formal_note-1.png
834e8b52631eebbf29802a820d755882b48eea0acee8de992160c9e9a1b370a8  renders/initial/direct_tex_note.pdf
3f52b51adacb7ffde64a1c53fef5fa46994463b81ef7ed67373050e202a72c5c  renders/initial/direct_tex_note.receipt.json
f856916da3a4324fb869f730a5e52684b112ebba8e54576b49444478859e591e  renders/initial/direct_tex_note_pages/direct_tex_note-1.png
35df8501edbe1f4adfdfd3779e3641dc60fe37b89df1a7c7d6552ad4634c7576  renders/stability/representative_formal_note_retry.pdf
aef745878bd25384586529c27d6a587fb0a43c69183e3062cdc737f56b753487  renders/stability/representative_formal_note_retry.receipt.json
e1e64b217468bce861d4205f93edc02e5a09f98840ea8604ffdb1822edce2f6a  renders/stability/representative_formal_note_retry_pages/representative_formal_note_retry-1.png
```

## Version Decision

Repository bump decision: PATCH

Reason: compatible improvement to existing collection behavior; no new repository-level capability and no breaking migration.

Affected plugins:

- `research-writing`: `0.1` -> `0.2`
  Reason: Research Authoring now has a bounded formal-PDF handoff to the renderer companion through `research-main`, keeps Markdown-only requests unchanged, and fails closed when standalone Marketplace Research Authoring lacks the companion.
- `presentations`: NO_BUMP
  Reason: compatibility is checked but production behavior is unchanged.
- all other central plugins: NO_BUMP
  Reason: no production behavior changed.

## Validation Run

All checks below were run on the same final candidate worktree after the profile was frozen:

```text
python -m unittest tests.test_render_chinese_math_pdf tests.test_research_writing_routing ...  # 35 tests OK
python -m unittest discover -s tests                                      # 241 tests OK
python scripts/skills.py registry --write                                 # wrote 150 skills
python scripts/skills.py validate                                         # validated 150 active skills, 18 profiles
python scripts/skills.py audit --all                                      # exit 0
python scripts/skills.py catalog --write                                  # wrote catalog/domain pages
python scripts/build_codex_marketplace.py --write --validate --check --path-report  # exit 0, over_budget=0
```

Profile install smokes used task-local temporary `CODEX_HOME` directories:

```text
research-main: copy install OK; installed render-chinese-math-pdf and research-reporting
presentation-desktop: copy install OK; installed render-chinese-math-pdf
server-research-baseline: copy install OK; installed render-chinese-math-pdf
```

Known remaining gate: pre-final independent Critic still must inspect the representative complete PDF/PNG evidence before final release acceptance. No paid review was used.

## Recovery v0.2 Status

Recovery candidate commit: `b2a476b83abfb30b5d0bf370db32d15df54c3de6`

Deterministic recovery gates completed:

- G1 math survival: `renders/recovery_v0_2/math_regression.receipt.json` records required, matched, and missing anchors; all required anchors are present.
- G2 direct `.tex` identity: `renders/recovery_v0_2/direct_tex_note.receipt.json` records non-canonical route identity without claiming canonical paper, margin, line spacing, or font profile values.
- G3 project-command identity: `renders/recovery_v0_2/project_venue_note.receipt.json` records `project-command` with `explicit-user-venue-project` authority.
- G4 complete-document visual QA: `SKILL.md` now requires complete-document visual checks using all pages or all declared high-risk pages.
- Deterministic validation: `python -m unittest tests.test_render_chinese_math_pdf`, `python -m unittest tests.test_research_writing_routing`, `python -m unittest tests.test_codex_marketplace`, `python -m unittest discover -s tests`, `python scripts/skills.py validate`, `python scripts/skills.py audit --all`, and `python scripts/build_codex_marketplace.py --write --validate --check --path-report` all passed on the recovery worktree.

G5 normal Research Authoring entry replay:

- status: `PARTIAL_NOT_CLOSED`
- replay authorization: current user authorized exactly one bounded G5 normal Research Authoring replay on 2026-09-24, limited to the prepared synthetic/public-safe input, current Codex identity/provider, and no private data, credential copy/new credential reads, paid API/Terra, live production identity mutation, Host Policy mutation, main merge, release integration, or final PASS claim.
- candidate replayed: `8f7c11d686f81862f6fa132f6073c272ff68380b`
- installed profile: `research-main` was installed into the clean task-local replay project with `install_kind: profile:research-main`, `collection_commit: 8f7c11d686f81862f6fa132f6073c272ff68380b`, and `active_skill_count: 19`.
- natural request/source: `renders/g5_research_authoring/request.md` and `renders/g5_research_authoring/source.md`.
- renderer evidence: the fresh child replay read the installed PDF/render skills, executed `.agents/skills/tools-documents-media-render-chinese-math-pdf/scripts/render_scientific_pdf.py`, and produced `renders/g5_research_authoring/advisor_report.pdf`.
- PDF QA: `renders/g5_research_authoring/evidence/render_receipt.json` records `status: complete`, `route: canonical-markdown`, `pages: 2`, `qa.errors: []`, and all-page previews at `renders/g5_research_authoring/previews/advisor_report-1.png` and `renders/g5_research_authoring/previews/advisor_report-2.png`; `renders/g5_research_authoring/evidence/validation.json` records exact display-equation/table/interpretation checks.
- consumption finding: `research-reporting` was present in the installed `research-main` routing table, but the child replay did not actually read/use `.agents/skills/writing-research-research-reporting/SKILL.md`. The compact evidence is `renders/g5_research_authoring/evidence/consumption_summary.json`.
- conclusion: this closes the proof that the normal child replay can consume the canonical renderer and produce a complete multi-page PDF, but it does **not** close the full G5 requirement because actual `research-reporting` consumption is missing. Treat this as a normal-entry routing gap requiring Planner/repair before any final PASS.

G5 routing repair after the partial replay:

- status: `DETERMINISTIC_REPAIR_READY_FOR_G5_REPLAY`
- current candidate: `827ee6a01fdfec44f0165b1ca9b321b37c257b50`
- preflight evidence first published at `e8a7fd4eab38ec5f347d0a5c2f3ade2408f760b0`; `git diff --name-only 827ee6a01fdfec44f0165b1ca9b321b37c257b50..e8a7fd4eab38ec5f347d0a5c2f3ade2408f760b0 -- ':!results/documents-media--scientific-pdf-rendering-reliability'` is empty, so no production source/profile/test/release metadata changed between the current candidate and that preflight evidence publication.
- repair: `research-main` now installs a profile-level `Profile Routing Notes` section into managed `AGENTS.md`, explicitly requiring advisor/group-meeting/milestone/experiment/repo-grounded research-report requests that also ask for a formal/readable PDF to first read and apply `research-reporting`, then use `render-chinese-math-pdf` only for PDF mechanics.
- source routing: `research-reporting` frontmatter now states that it owns report semantics even when the final deliverable is a formal PDF; rendering mechanics remain owned by companion document skills.
- regression: `tests/test_research_writing_routing.py::ResearchWritingRoutingTests::test_research_main_agents_notes_route_report_pdf_through_reporting_first` installs `research-main` into a temporary project and verifies the generated `AGENTS.md` contains the profile routing note with `research-reporting` before `render-chinese-math-pdf`.
- preflight evidence: `renders/g5_research_authoring_preflight_827ee6a/evidence/manifest.json` records a clean `research-main` install from `collection_commit: 827ee6a01fdfec44f0165b1ca9b321b37c257b50`; `renders/g5_research_authoring_preflight_827ee6a/evidence/AGENTS.md` records the profile routing note before the skill routing table; `renders/g5_research_authoring_preflight_827ee6a/evidence/preflight_summary.json` summarizes the line-level routing evidence.
- validation: `python -m unittest tests.test_research_writing_routing tests.test_skill_update tests.test_codex_marketplace`, `python scripts/skills.py validate`, `python scripts/skills.py audit --all`, `python scripts/build_codex_marketplace.py --write --validate --check --path-report`, and `python -m unittest discover -s tests` passed after the repair.

G5 authorized normal Research Authoring replay after the routing repair:

- status: `G5_PASSED_NORMAL_RESEARCH_AUTHORING_REPLAY`
- authorization: current user authorized exactly one bounded G5 replay for the current candidate on 2026-09-24. The run used only the prepared synthetic/public-safe G5 input, the current Codex identity/provider, and no private data, new credential copy/read, paid API/Terra, live production identity mutation, Host Policy mutation, main merge, release integration, or final PASS claim.
- source candidate: `827ee6a01fdfec44f0165b1ca9b321b37c257b50`
- replay branch tip: `96c05469f10730bb4eed445ffd8dabfbb81a2e89`; `git diff --name-only 827ee6a01fdfec44f0165b1ca9b321b37c257b50..96c05469f10730bb4eed445ffd8dabfbb81a2e89 -- ':!results/documents-media--scientific-pdf-rendering-reliability'` is empty, so the intervening commits only changed task evidence/results, not production source/profile/test/release files.
- installed profile: `research-main` was installed into a fresh task-local replay project with `install_kind: profile:research-main`, `collection_commit: 96c05469f10730bb4eed445ffd8dabfbb81a2e89`, and `active_skill_count: 19`; install manifest is `renders/g5_research_authoring_replay_96c0546/evidence/install_manifest.json`.
- normal entry evidence: the generated project `AGENTS.md` records the `Profile Routing Notes` instruction before the skill routing table at `renders/g5_research_authoring_replay_96c0546/evidence/AGENTS.md`; natural input files are `renders/g5_research_authoring_replay_96c0546/request.md` and `renders/g5_research_authoring_replay_96c0546/source.md`.
- actual research-reporting consumption: `renders/g5_research_authoring_replay_96c0546/evidence/child.stdout.jsonl` records the child reading `.agents/skills/writing-research-research-reporting/SKILL.md` and `.agents/skills/writing-research-research-reporting/references/group-meeting-advisor-reports.md`; compact line-level evidence is `renders/g5_research_authoring_replay_96c0546/evidence/consumption_summary.json`.
- actual renderer consumption: the same child replay read `.agents/skills/tools-documents-media-render-chinese-math-pdf/SKILL.md`, renderer checklists/profile files, and executed `.agents/skills/tools-documents-media-render-chinese-math-pdf/scripts/render_scientific_pdf.py`; output files are `renders/g5_research_authoring_replay_96c0546/advisor_report.md` and `renders/g5_research_authoring_replay_96c0546/advisor_report.pdf`.
- PDF QA: `renders/g5_research_authoring_replay_96c0546/evidence/render_receipt.json` records `status: complete`, `route: canonical-markdown`, `profile_id: canonical-formal-note-v0.2`, `pages: 2`, and `qa.errors: []`; `pdfinfo` records A4, 2 pages, `LaTeX via pandoc` / `xdvipdfmx`; previews for all pages are `renders/g5_research_authoring_replay_96c0546/previews/advisor_report-1.png` and `renders/g5_research_authoring_replay_96c0546/previews/advisor_report-2.png`.
- whole-document QA: `renders/g5_research_authoring_replay_96c0546/evidence/validation.json` records exact display-equation/table/interpretation preservation and all-page visual inspection; local human inspection of both preview pages found readable equations, table, prose, and page break with no missing glyphs or layout overlap.
- conclusion: G5 now closes for the current candidate. This evidence proves the normal `research-main / Research Authoring` entry can consume `research-reporting` for report semantics and the canonical renderer for the formal PDF, while preserving Markdown-only behavior unless the user explicitly requests a PDF.
- remaining boundary: this is not a final release PASS. The next allowed workflow step is pre-final Critic/Reviewer inspection of the complete G1-G7 evidence; no main merge or release integration has been performed.

## Release Reconciliation And G7 Closure

Current closure date: 2026-09-25

Merged main:

- `origin/main`: `26dfa9f921b0df4b784ae6e3187558fd2509954b`
- latest main repository version before merge: `5.1.1`
- merge mode: ordinary merge of `origin/main` into `reviewed/documents-media--scientific-pdf-rendering-reliability`
- no rebase, force push, PR, main merge, paid API, Terra, Host Policy change, Typst/Quarto migration, renderer redesign, or Research Authoring redesign

Release identity:

- Repository version: `5.1.2`
- `research-writing`: `0.1` -> `0.2`
- `presentations`: `NO_BUMP` (`0.3`)
- standalone `render-chinese-math-pdf`: standalone skill metadata remains `0.1`; no central plugin version is invented
- all other central plugin versions preserve latest main values: `workflow-core 0.4`, `ai-skills-core 0.4`, `writing-style 0.3`, `scientific-visualization 0.1`, `web-development 0.2`, `statistical-modeling 0.1`, `bioinformatics 0.1`, `medical-imaging 0.1`

G5 prior PASS and non-impact proof:

- Independent Critic status supplied by user: G5 PASS for the prior candidate.
- G5 replay evidence remains under `renders/g5_research_authoring_replay_96c0546/`.
- Latest main did not change `research-reporting`, `research-main` profile/routing, `scripts/skills.py`, `tests/test_render_chinese_math_pdf.py`, or `tests/test_research_writing_routing.py` relative to merge-base `338add2d7ac002a0201a924be3a0ec2818b777c7`.
- The only latest-main change inside the renderer source file was non-behavioral frontmatter metadata: `version: "0.1"` in `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`; renderer workflow, entrypoint, font policy, route semantics, scripts, profile routing, and G5 tests were not semantically changed.
- Exact diff proof:
  - `g7_release_reconciliation/g5_dependent_main_diff_name_status.txt`
  - `g7_release_reconciliation/render_skill_latest_main_diff.txt`
  - `g7_release_reconciliation/no_main_diff_core_g5_routing_surfaces.txt`

G7 local validation on the reconciled candidate worktree:

```text
python -m unittest discover -s tests
# Ran 274 tests in 44.247s
# OK

python scripts/skills.py validate
# validated 151 active skills, 18 profiles, templates, and trigger eval scaffolds

python scripts/skills.py audit --all
# exit 0

python scripts/build_codex_marketplace.py --write --validate --check --path-report
# plugins=10 active_skills=27 source_snapshots=67
# Windows path budget over_budget=0
```

Profile install smokes:

- `research-main`: `g7_release_reconciliation/profile_smokes/research-main.json`, `ok: true`, `installed_skill_count: 19`
- `presentation-desktop`: `g7_release_reconciliation/profile_smokes/presentation-desktop.json`, `ok: true`, `installed_skill_count: 7`
- `server-research-baseline`: `g7_release_reconciliation/profile_smokes/server-research-baseline.json`, `ok: true`, `installed_skill_count: 7`

Version and release consistency:

- `g7_release_reconciliation/version_consistency.json` records `ok: true`.
- `VERSION` and `registry.json` are `5.1.2`.
- README records repository `5.1.2` and Research Authoring `0.2`.
- CHANGELOG preserves existing `5.1.1`, `5.1.0`, and earlier history, and adds a new `5.1.2` section.
- `scripts/codex_marketplace_config.json` records `research-writing 0.2` and preserves latest-main released versions for other central plugins.

Generated parity:

- `python scripts/skills.py registry --write` regenerated `registry.json` from source.
- `python scripts/skills.py catalog --write` regenerated `docs/SKILL_CATALOG.md` and 16 domain pages from source.
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report` regenerated `.agents/plugins/marketplace.json` and `plugins/codex/plugins/` from the reconciled source, with `over_budget=0`.
- A second generator run changed only timestamp-bearing `generated_at` lines in `registry.json` and `docs/SKILL_CATALOG.md`; no structural source/generated drift was observed.

Complete artifact locators:

- G5 natural request: `renders/g5_research_authoring_replay_96c0546/request.md`
- G5 source input: `renders/g5_research_authoring_replay_96c0546/source.md`
- G5 generated Markdown: `renders/g5_research_authoring_replay_96c0546/advisor_report.md`
- G5 generated PDF: `renders/g5_research_authoring_replay_96c0546/advisor_report.pdf`
- G5 all-page previews:
  - `renders/g5_research_authoring_replay_96c0546/previews/advisor_report-1.png`
  - `renders/g5_research_authoring_replay_96c0546/previews/advisor_report-2.png`
- G5 consumption summary: `renders/g5_research_authoring_replay_96c0546/evidence/consumption_summary.json`
- G5 render receipt: `renders/g5_research_authoring_replay_96c0546/evidence/render_receipt.json`
- G5 validation: `renders/g5_research_authoring_replay_96c0546/evidence/validation.json`
- Downloadable local review packet prepared for external GPT/Critic consumption: `/home/yuukias/AI_Skills_Collection/private/exports/documents-media--scientific-pdf-rendering-reliability/g5_review_packet_906b66d.zip`

Final candidate SHA and clean-clone G7 verification are recorded in the final execution report after the commit is frozen, pushed, and verified at the remote tip. A Git commit cannot contain a literal self-reference to its own SHA in this file without changing that SHA.
