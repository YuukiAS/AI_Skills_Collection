# Scientific PDF Rendering Reliability — Canonical Goal

**Execution package version:** v0.1  
**Task key:** `documents-media--scientific-pdf-rendering-reliability`  
**Target repository:** `YuukiAS/AI_Skills_Collection`  
**Target:** `render-chinese-math-pdf` standalone renderer + bounded Research Authoring/profile handoff  
**Proposal:** `docs/design/scientific-pdf-rendering/SCIENTIFIC_PDF_RENDERING_RELIABILITY_PROPOSAL_V0_1.md`  
**Source branch:** `main`  
**Exact execution branch after approved Kickoff:** `reviewed/documents-media--scientific-pdf-rendering-reliability`  
**Exact task-owned worktree after approved Kickoff:** `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`

This Goal is not execution authorization until independent Critic returns `READY_FOR_CODEX=YES` for the same Proposal/Goal/Kickoff package and the user sends the approved Kickoff.

## 1. Required outcome

Ship one compatible refinement in which:

1. `render-chinese-math-pdf` has a **repo-owned canonical production entry** for Markdown/LaTeX scientific/technical PDF generation using Pandoc + XeLaTeX by default.
2. Host-local `render_resources/chinese_math_pdf` supplies resources, not canonical business logic.
3. No automatic Chromium/browser fallback can satisfy the default production route.
4. Default PDF rendering has one declared stable formal-note profile and does not silently change paper size/margins/numbering during retry.
5. Pandoc semantic block types replace ad-hoc line-shape classification for typography decisions.
6. Ordinary prose is never silently downgraded to table typography because it resembles a table.
7. Math fidelity is checked at source/AST/generated-TeX level and actual equation pages are visually reviewed.
8. Canonical default font policy is actually enforced; unexpected Liberation/DejaVu/Droid fallback does not pass canonical default QA.
9. Whole-document visual QA covers all pages or an equivalent complete montage, not only page 1.
10. `research-main` installs renderer; `research-reporting` delegates requested formal PDF output to it after document semantics are stable.
11. Markdown-only Research Authoring tasks remain Markdown-only.
12. Research Authoring environments without renderer fail closed with an exact companion dependency instead of silently building a different PDF.
13. Presentations/server companion use remains compatible.
14. No canonical slug rename occurs in this task.
15. No new central Marketplace plugin or renderer Marketplace user entry is created.

## 2. Implementation authority

After the user sends a Critic-approved Kickoff, Executor may create:

- branch `reviewed/documents-media--scientific-pdf-rendering-reliability`;
- worktree `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`.

Allowed production areas:

- `skills/tools/documents-media/render-chinese-math-pdf/**`
- `skills/writing/research/research-reporting/SKILL.md`
- `profiles/research-main.json`
- directly necessary targeted tests
- `scripts/codex_marketplace_config.json` only for the approved Research Authoring release version change, not renderer membership
- normal generated registry/catalog/Marketplace payloads from existing generators
- release docs/changelogs/README required by current policy
- `results/documents-media--scientific-pdf-rendering-reliability/**`
- repo-safe fixtures/evidence required by the frozen gates.

Do not modify:

- `writing-style` production behavior;
- Presentations production source;
- Bridge Kit;
- Host Policy / execpolicy;
- workflow-core / ai-skills-core architecture;
- unrelated profiles/plugins;
- user research repos or private scientific content outside specifically authorized read-only validation scope.

## 3. Required implementation shape

### 3.1 Repo-owned canonical renderer

Create a canonical source entry under the renderer skill. It must:

- resolve project/user/source metadata and a stable default profile;
- resolve the approved local resource bundle;
- invoke Pandoc + XeLaTeX;
- produce final PDF;
- invoke QA;
- return non-zero / explicit failure when required dependencies or gates fail;
- never turn a missing XeLaTeX route into Chromium success.

The old external resource script may remain for compatibility/diagnosis only if it is no longer the canonical logic owner and tests prove the repo-owned entry works independently of host script behavior.

### 3.2 Default formal-note profile

Use one version-controlled declarative profile. Initial frozen baseline unless Critic revises it:

- A4;
- 11pt body;
- 25mm baseline margins;
- ~1.15 line spacing;
- no automatic TOC;
- no automatic section numbering;
- no heuristic prose downscaling.

Source/user/project metadata may override intentionally. The renderer must record/resolve the same profile on retry.

### 3.3 Semantic parsing

Use Pandoc AST semantics. Do not reintroduce `tableline`-style line parsing to decide reader-facing font size.

If a true table does not fit, use a bounded table-specific strategy or fail QA. Do not make unrelated prose smaller to avoid overflow.

### 3.4 Font and math

Keep TeX Gyre Termes / TeX Gyre Termes Math / Noto Serif SC / Noto Sans SC as the canonical default families unless implementation evidence shows a blocking incompatibility.

fontspec scaling may be used only if actual render shows it improves cross-script harmony and regressions stay clean.

Math validation must include:

- source Pandoc Math node inventory;
- generated LaTeX survival;
- compile success;
- known notation regression;
- actual equation-page render inspection.

### 3.5 Complete visual QA

Generate complete page renders/montage for final candidate. Reuse mature PDF utilities where practical. Do not implement OCR-based math checking.

Mechanical QA cannot give final visual PASS by itself.

### 3.6 Research Authoring integration

Update `research-reporting` so that:

- it continues to own research-document semantics;
- when user asks for final PDF, it delegates only artifact mechanics to renderer;
- it never lets renderer change scientific structure/claims/table semantics;
- missing renderer blocks honestly;
- it does not generate a private one-off LaTeX/browser template.

Add renderer to `research-main` profile.

Do not add renderer to central Marketplace config skill membership in this task.

## 4. Required tests and evidence

Executor must add/maintain tests for:

- canonical route uses Pandoc/XeLaTeX and blocks when missing;
- explicit Chromium diagnostic remains possible but cannot be fallback;
- project/override resource resolution;
- canonical font allowlist under default route;
- Math AST and generated-TeX survival for representative notation;
- real Table vs pseudo-table prose classification;
- no arbitrary `\\footnotesize` ordinary prose;
- title/heading/numbering conflict;
- repeated-render document profile stability;
- English-only scientific note explicit PDF request;
- mixed CJK/English/math note;
- research-main profile install;
- Research Authoring PDF handoff;
- Markdown-only Research Authoring should-not-change;
- missing companion renderer fail-closed;
- presentation-desktop and server-research-baseline compatibility;
- generated layer parity.

Tests are necessary but not sufficient.

## 5. Capability gates

Executor must satisfy Proposal G1–G7 on the same final candidate.

Development known failures may be replayed repeatedly. Final candidate identity must be frozen before pre-final Critic review. No evidence splicing across different final commits.

Pre-final Critic must directly inspect complete rendered PDF evidence for G2/G3/G4/G5 before any release conclusion.

No paid review is authorized or required.

## 6. Version / release contract

If production behavior is implemented and all release gates pass:

Repository bump decision: PATCH  
Expected: `5.0.6 -> 5.0.7`

Affected plugins:

- `research-writing`: `0.1 -> 0.2`
- `presentations`: NO_BUMP
- all other central plugins: NO_BUMP

If final implementation does not change Research Authoring production behavior, return to Planner before inventing a different version outcome.

Update `docs/plugin-changelogs/research-writing.md`, root `CHANGELOG.md`, generated versions, and README consistently.

README closure is mandatory:
- update if version/capability line changed;
- otherwise explicitly record `README checked: no update required`.

Do not change maturity status automatically.

## 7. Full validation order

1. targeted renderer tests;
2. targeted research-writing/profile tests;
3. known regression renders;
4. deterministic should-not-change bank;
5. full unittest suite;
6. skills registry/validate/audit;
7. Marketplace generate/validate/check/path report;
8. clean source-profile install smoke for `research-main`;
9. compatibility smoke for `presentation-desktop` and `server-research-baseline`;
10. representative complete standalone render;
11. representative Research Authoring → PDF render;
12. save complete raster/montage evidence;
13. commit/push exact reviewed branch;
14. pre-final independent Critic review of final candidate and actual renders;
15. only after Critic PASS, release/integration steps already allowed by the then-effective workflow.

## 8. Stop and escalate

Stop and return to Planner/Critic before expanding if any of these becomes necessary:

- canonical slug rename;
- new central plugin;
- direct renderer Marketplace membership under Research Authoring;
- Typst/Quarto runtime dependency;
- Presentations production change;
- new network/font download;
- paid API;
- private data/provider/credential not already authorized;
- destructive Git operation;
- Host Policy change;
- redesign of Research Authoring overall architecture;
- change to capability gates or release semantics.

Ordinary code/test/render bugs inside the approved design must be fixed by Executor without asking the user to debug for it.

## 9. Completion

Do not claim completed because:

- source files changed;
- tests pass;
- PDF exists;
- fonts embed;
- CI passes.

Completion requires the same final candidate to pass all required capability gates, whole-artifact qualitative review, version/changelog/generated parity, profile/normal-entry integration, and the then-required independent review/integration steps.

