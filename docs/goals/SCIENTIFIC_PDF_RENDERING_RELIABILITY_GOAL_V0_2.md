# Scientific PDF Rendering Reliability — Canonical Goal v0.2

Execution package version: v0.2  
Task key: documents-media--scientific-pdf-rendering-reliability  
Target repository: YuukiAS/AI_Skills_Collection  
Target: standalone render-chinese-math-pdf + bounded Research Authoring/profile handoff  
Proposal: docs/design/scientific-pdf-rendering/SCIENTIFIC_PDF_RENDERING_RELIABILITY_PROPOSAL_V0_2.md  
Source branch: main  
Exact execution branch after approved Kickoff: reviewed/documents-media--scientific-pdf-rendering-reliability  
Exact task-owned worktree after approved Kickoff: /tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability

This Goal is not execution authorization until independent Critic reviews the exact v0.2 Proposal + Goal + Kickoff and returns READY_FOR_CODEX=YES, and the user then sends that approved Kickoff.

## 1. Required outcome

Ship one compatible refinement in which:

1. render-chinese-math-pdf has a repo-owned canonical production entry.
2. Host-local render_resources supplies resources, not canonical reusable orchestration logic.
3. Default Markdown rendering uses Pandoc AST -> LaTeX -> XeLaTeX when no stronger render authority applies.
4. Chromium/browser rendering is explicit diagnostic only and never a silent fallback.
5. Native .tex remains a direct XeLaTeX route under its applicable source/project contract; it is not forced through Pandoc.
6. Render authority is resolved in this order:
   - explicit user / venue / project render contract;
   - source-specific explicit render settings;
   - canonical formal-note default.
7. Canonical Markdown typography is driven by Pandoc semantic node types, not ad-hoc line-shape categories such as tableline.
8. Ordinary prose is never silently shrunk merely because it resembles a table or because another object overflows.
9. Math fidelity protects the ordered Math(mathtype,text) payload through the Pandoc transformation path and verifies corresponding generated-TeX content/critical tokens.
10. Equation-heavy pages are visually inspected after deterministic payload checks.
11. Canonical formal-note font identity is enforced only on the canonical route; project/venue-owned templates retain their own declared fonts/classes/layout.
12. Whole-document visual QA covers all pages or equivalent complete montages, not just the first page.
13. research-main installs render-chinese-math-pdf.
14. research-reporting delegates artifact mechanics to the renderer when a final formal PDF is explicitly requested and document semantics are stable.
15. Markdown-only Research Authoring requests remain Markdown-only.
16. Standalone Marketplace research-writing without the renderer companion fails closed with a clear dependency and does not invent a browser/XeLaTeX fallback.
17. Presentations/server companion use remains compatible.
18. No canonical slug rename, new central plugin, or renderer Marketplace user skill is created.

## 2. Visual-profile calibration contract

The following are starting implementation candidates only, not frozen final values:

- A4;
- 11pt body;
- 25mm margins;
- approximately 1.15 line spacing.

Executor may perform exactly one bounded pre-final calibration cycle:

1. render the starting candidate on the predeclared known-regression and representative complete inputs;
2. inspect complete artifacts under G3;
3. if evidence shows a real typography problem, make at most one profile adjustment;
4. rerender the same representative inputs;
5. select and record the final default profile;
6. freeze it before declaring final-candidate identity.

No further visual tuning is allowed after final-candidate freeze.

The following product semantics are already frozen and are not calibration variables:

- no unrequested change of paper/template/profile identity;
- no automatic TOC/section numbering injection unless the effective contract requests it;
- no heuristic downscaling of ordinary prose;
- no solving table/object overflow by changing unrelated prose typography;
- no post-freeze visual tuning.

## 3. Effective/resolved profile identity

For each render, record enough information to identify the effective route/profile, including as applicable:

- authority source: user / venue / project / source settings / canonical default;
- renderer route and engine;
- project/venue template or class identity;
- paper size/orientation;
- margins/layout settings;
- TOC/numbering policy;
- body/font policy;
- relevant line-spacing/profile settings.

Retry stability is evaluated only when the request resolves to the same effective profile.

If the user explicitly changes paper size, venue template, class, or another format-defining requirement, the renderer creates a new effective profile identity. G4 must not classify that deliberate change as a regression.

## 4. Route authority and should-not-change behavior

### 4.1 Markdown

If there is no stronger project/venue/user contract:

Markdown -> Pandoc AST -> optional minimal semantic Lua filter -> LaTeX -> XeLaTeX -> PDF -> QA.

If a project-owned render command/template is documented, usable, and matches the requested output, it has higher authority than the canonical default.

### 4.2 Native .tex

Native .tex defaults to direct XeLaTeX using the applicable project/source environment and resources.

Do not round-trip native LaTeX through Pandoc merely to share the canonical Markdown wrapper.

### 4.3 Project/venue templates

A project/venue-owned template may use its own:

- fonts;
- document class;
- margins;
- paper size;
- numbering;
- headers/footers;
- other layout rules.

The canonical default font allowlist does not override this higher-authority route.

The final route/template/font identity must still be traceable and must pass the glyph/math/layout checks that are applicable to that route.

## 5. Math payload fidelity contract

For each frozen regression fixture with math:

1. parse the source through Pandoc and capture the ordered Math(mathtype,text) semantic signature;
2. compare it with the expected frozen fixture signature;
3. after approved transformations, verify the ordered payload has not changed semantically;
4. generated LaTeX must preserve corresponding formula content or predeclared critical math-token anchors;
5. compilation must succeed;
6. render the relevant equation-heavy pages and inspect them visually.

The regression bank must cover at least:

- hat;
- subscript/superscript;
- sum;
- integral;
- gradient/operator;
- Greek;
- matrix;
- mathbb;
- long formula;
- Chinese-adjacent inline math;
- Chinese-adjacent display math.

Do not satisfy this by checking only Math node counts, delimiters, or formula existence.

Do not implement a new full TeX/math parser and do not use OCR for routine math validation.

## 6. Font and typography contract

Canonical formal-note route defaults remain based on the current bundle:

- TeX Gyre Termes;
- TeX Gyre Termes Math;
- Noto Serif SC;
- Noto Sans SC.

Unexpected Liberation / DejaVu / Droid fallback fails canonical-route QA.

fontspec Scale=MatchLowercase, MatchUppercase, or MatchAveragecase may be evaluated only during the bounded calibration cycle. It is accepted only if actual complete renders improve and regressions remain clean.

G3 qualitative review, not font-name matching, decides whether mixed Latin/CJK/math typography is visually coherent.

## 7. Research Authoring integration contract

This task freezes only:

Research Authoring document semantics -> shared renderer artifact-mechanics handoff.

It does not approve the unresolved full architecture in RESEARCH_WRITING_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-07.md.

Required bounded changes:

- research-main installs render-chinese-math-pdf;
- research-reporting keeps ownership of scientific/document semantics;
- formal PDF requests delegate low-level artifact mechanics to the renderer after semantic structure is stable;
- renderer cannot change claims, evidence selection, table semantics, or document scientific organization;
- Markdown-only requests do not trigger PDF;
- if standalone Marketplace research-writing lacks renderer, report the exact companion dependency and stop;
- do not silently use Chromium or create another local LaTeX template.

Do not add renderer to Research Authoring Marketplace skill membership.

The current topology test that keeps renderer out of central Marketplace config remains a regression for this chosen v0.2 architecture; it is not declared a permanent product constitution.

## 8. Required implementation scope

After the user sends a Critic-approved v0.2 Kickoff, Executor may modify:

- skills/tools/documents-media/render-chinese-math-pdf/**
- skills/writing/research/research-reporting/SKILL.md
- profiles/research-main.json
- directly necessary renderer/research-writing/profile tests and repo-safe fixtures
- scripts/codex_marketplace_config.json only for the approved research-writing version bump, not renderer skill membership
- normal generated registry/catalog/Marketplace files through existing generators
- docs/skill-todos/render-chinese-math-pdf.md
- docs/plugin-todos/research-writing.md
- docs/plugin-changelogs/research-writing.md
- CHANGELOG.md
- README.md
- task evidence under results/documents-media--scientific-pdf-rendering-reliability/
- already-authorized private evidence under private/exports if genuinely needed.

Do not modify:

- Clear Writing production behavior;
- Presentations production source;
- Bridge Kit;
- Host Policy/execpolicy;
- workflow-core / ai-skills-core architecture;
- unrelated profiles/plugins;
- the full Research Authoring redesign;
- user research repos/private scientific content outside separately authorized read scope.

## 9. Required tests and regression evidence

Targeted tests/evidence must include:

- canonical Markdown route uses Pandoc/XeLaTeX and blocks on missing required engine/resources;
- explicit Chromium diagnostic remains possible but cannot be fallback;
- project/override resource resolution;
- ordered Math(mathtype,text) payload preservation;
- generated-TeX formula content/critical-token survival;
- representative notation coverage listed in Section 5;
- canonical default font allowlist;
- semantic Table vs pseudo-table Para handling;
- no arbitrary ordinary-prose footnotesize/small downscaling;
- title/heading/numbering conflict handling;
- same-effective-profile retry stability;
- explicit format/template change recognized as new effective profile;
- English-only scientific note canonical render;
- mixed CJK/English/math canonical render;
- native .tex direct-XeLaTeX should-not-change case;
- project/venue-owned template should-not-change case;
- research-main clean install includes renderer;
- Research Authoring formal-PDF handoff;
- Research Authoring Markdown-only should-not-change;
- missing companion renderer fail closed;
- generic existing-PDF non-render request remains with generic PDF tooling;
- presentation-desktop and server-research-baseline compatibility;
- generated layer parity.

Tests are necessary but not sufficient.

## 10. Capability Gates v0.2

Executor must satisfy Proposal v0.2 G1–G7 on the same final candidate.

Specific amendments relative to v0.1:

- G2 includes ordered Math payload and generated-TeX content preservation.
- G4 evaluates same-request stability over the effective/resolved profile and explicitly allows a user-requested new format/profile identity.
- G6 includes direct .tex and project/venue template should-not-change cases.
- G7 remains full shared/profile/release compatibility.

G3 must be judged on complete actual artifacts. Font allowlists, tests, page counts, or schema cannot substitute for typography judgment.

## 11. Validation chronology

1. targeted implementation tests;
2. cheap known regression bank;
3. render initial profile candidate on predeclared representative complete inputs;
4. one bounded calibration cycle, with at most one evidence-driven adjustment;
5. rerender the same representative inputs;
6. record selected final default profile;
7. freeze final-candidate code/profile/fixture/rubric identity;
8. run targeted renderer/research-writing/profile tests;
9. run full unittest suite;
10. run skills registry/validate/audit;
11. run Marketplace generate/validate/check/path report;
12. clean research-main install smoke;
13. presentation-desktop and server-research-baseline compatibility smoke;
14. complete standalone and Research Authoring->PDF representative renders;
15. save complete page/montage evidence;
16. commit/push the exact reviewed branch;
17. pre-final independent Critic directly reviews the same final candidate and actual representative PDF/montage;
18. only after the then-required review/integration gates may release closure be completed.

No release evidence may be spliced across different final commits.

Known historical private PDFs are development regressions, not fresh final evidence.

No paid review is authorized or required.

## 12. Version and release contract

If production implementation changes research-reporting behavior and the same final candidate passes all required gates:

Repository bump decision: PATCH  
Expected: 5.0.6 -> 5.0.7

Affected plugins:

- research-writing: 0.1 -> 0.2
- presentations: NO_BUMP
- all other central plugins: NO_BUMP

Standalone render-chinese-math-pdf gets no invented plugin version.

README closure is mandatory.

README/changelog must not claim that installing the standalone Research Authoring Marketplace plugin automatically bundles the renderer. The complete normal PDF workflow approved here is research-main + installed renderer companion; standalone plugin-only PDF requests fail closed when the companion is missing.

Maturity remains unchanged.

## 13. Stop and return to Planner/Critic

Stop before scope expansion if implementation would require:

- canonical slug rename;
- new central plugin;
- renderer Marketplace membership under Research Authoring;
- Typst/Quarto runtime adoption;
- Presentations production change;
- full Research Authoring redesign;
- new network/font/resource download;
- new private data/provider/credential scope;
- paid API;
- Host Policy/destructive Git change;
- changing G1–G7 semantics.

Ordinary code/test/render bugs inside the approved design remain Executor responsibility and are not user debugging tasks.

## 14. Completion

Do not claim completion merely because source changed, PDF exists, fonts embed, tests pass, or CI passes.

Completion requires the same final candidate to pass G1–G7, complete-artifact visual judgment, profile/install compatibility, generated parity, version/changelog/README closure, and the then-required independent review/integration steps.

