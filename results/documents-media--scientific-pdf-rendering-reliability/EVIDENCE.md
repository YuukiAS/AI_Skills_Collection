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

- status: `NOT_TESTED`
- reason: running the pinned Codex child replay with current Codex identity was rejected by Auto-review as an external model action that requires current explicit user authorization for this specific data/provider/purpose. The subsequent interactive authorization prompt returned an empty answer, which is not consent under repository policy.
- pre-request evidence: both failed child invocations exited before model output or requested artifact generation; `outputs/` remained empty.
- recovery: rerun the same isolated `research-main` G5 replay only after explicit user authorization for the synthetic/public-safe G5 input, current Codex identity/provider, and one bounded child replay for this task.
