# Scientific PDF Rendering Reliability — Planner Proposal v0.2

Version: v0.2  
Status: READY FOR INDEPENDENT CRITIC RE-REVIEW / NOT EXECUTION AUTHORIZATION  
Date: 2026-09-21  
Target repository: YuukiAS/AI_Skills_Collection  
Task key: documents-media--scientific-pdf-rendering-reliability  
Source branch/ref: main  
Latest main checked before this revision: 164f028b76da265b117e42cfbda1563cd4abb809  
v0.1 package reviewed by Critic: 9530e7b74d4312b990fa5b97a27f2d3dfaf65c4f  
Planned execution branch: reviewed/documents-media--scientific-pdf-rendering-reliability  
Planned task-owned worktree: /tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability

This file supersedes v0.1 as the Planner proposal but does not overwrite it. It is a planning-only amendment. No production source, profile, generated layer, runtime, test, version, or release file is changed by this package.

## 1. v0.2 decision

The v0.1 architecture direction remains intact:

- render-chinese-math-pdf stays a standalone shared skill;
- no canonical slug rename in this task;
- no new central plugin;
- no fourth Research Authoring Marketplace user skill;
- canonical orchestration moves into repo-owned source;
- Markdown default remains Pandoc + XeLaTeX;
- Chromium remains explicit diagnostic only, never a silent fallback;
- Pandoc AST semantics replace ad-hoc line-shape categories such as tableline;
- math, font, page-identity, and whole-document visual QA are strengthened;
- research-main installs the renderer;
- research-reporting performs a bounded PDF handoff only when a formal PDF is requested;
- Markdown-only requests remain Markdown-only;
- plugin-only Research Authoring without the companion renderer fails closed;
- G1–G7 remain the capability-gate structure;
- if final production behavior and release gates pass, the expected release remains repository 5.0.6 -> 5.0.7 and research-writing 0.1 -> 0.2, with presentations NO_BUMP;
- maturity does not change automatically;
- no paid review;
- no expansion into the unresolved full Research Authoring redesign.

The Critic REVISE identified three execution-contract defects, not a need to reopen these decisions. v0.2 closes exactly those defects and corrects the Typst research description.

## 2. Main drift check

Compared with the v0.1 package commit 9530e7b7, current main has only planning/review documentation drift:

- the v0.1 Critic handoff document;
- Project Thread Handoff V3 design documents.

No renderer, Research Authoring, profile, Marketplace, test, version, or release production source changed. Therefore this revision keeps the v0.1 reality analysis and only re-reads current main sources required by the Planner/Critic contracts.

## 3. Critic blocker closure

### PDF-CRIT-001 — CLOSED: visual defaults become calibration candidates, not pre-approved final values

v0.1 was internally inconsistent: the Proposal allowed evidence-based visual adjustment, while the Goal called A4 / 11pt / 25mm / about 1.15 a frozen baseline and the Kickoff told Executor to implement a frozen profile.

v0.2 replaces that with one consistent rule:

1. A4 / 11pt / 25mm / about 1.15 remain the initial implementation candidate only.
2. They are not a Critic-approved final visual answer.
3. Executor may perform one bounded pre-final calibration cycle using known regression material plus representative complete renders.
4. The calibration sequence is:
   - render the initial candidate on the predeclared representative inputs;
   - inspect the complete artifacts against G3;
   - if needed, make at most one evidence-driven profile adjustment;
   - rerender the same inputs;
   - select and record the final default profile;
   - freeze it before final-candidate identity is declared.
5. After freeze, no further visual tuning is allowed for the final candidate. A post-freeze quality failure returns to the normal repair/review path; it does not justify continuing A/B calibration.
6. Retry stability means the same request and the same resolved/effective profile must keep its page/profile identity.
7. Product semantics that are frozen now, before calibration:
   - no unrequested paper/profile change;
   - no automatic TOC or section-numbering injection unless the resolved contract requests it;
   - no heuristic downscaling of ordinary prose;
   - no fixing table overflow by changing unrelated prose typography;
   - no post-final-candidate visual tuning.

This is calibration inside the approved implementation, not a new workflow, benchmark, or open-ended experiment.

### PDF-CRIT-002 — CLOSED: authority precedence and direct .tex behavior are explicit

v0.2 freezes route authority as:

explicit user / venue / project render contract  
> source-specific explicit render settings  
> canonical formal-note default.

Consequences:

- If a project-owned render command/template is documented, usable, and matches the requested output, it retains first authority.
- Markdown without higher authority uses Markdown -> Pandoc AST -> LaTeX -> XeLaTeX.
- Native .tex continues to compile directly with XeLaTeX under the applicable project/source contract. It must not be round-tripped through Pandoc merely to unify the wrapper.
- The canonical default font allowlist applies only to the canonical formal-note route.
- A project/venue-owned template may use its own class, fonts, margins, numbering, headers/footers, or paper size. Its identity must be traceable, and it still must pass the glyph/math/layout QA that is relevant to that route.
- Retry stability compares the effective/resolved profile for the same request. If the user explicitly changes paper size, venue template, document class, or another format-defining requirement, that is a new profile identity, not a regression.
- G6 gains project-owned-template and direct-.tex should-not-change cases; no new gate is created.

The repo-owned wrapper therefore becomes an orchestrator of route selection and QA, not an authority that overwrites stronger project/venue contracts.

### PDF-CRIT-003 — CLOSED: G2 protects ordered Math payload, not merely node presence

Pandoc Math carries both mathtype and text. v0.2 makes the deterministic regression contract content-preserving:

- each frozen math regression fixture records an ordered semantic signature of Math(mathtype, text);
- comparison is exact for mathtype and math text except non-semantic platform newline normalization when required by the harness;
- source parsing/transformation must preserve the expected ordered payload;
- generated LaTeX survival checks must confirm corresponding formula content or predeclared critical math-token anchors, not merely the existence of a math delimiter/node;
- coverage includes hat, subscript/superscript, sum/integral, gradient/operators, Greek symbols, matrices, mathbb, a long formula, and Chinese-adjacent inline/display math;
- compilation must succeed;
- equation-heavy rendered pages remain the second, visual layer of G2.

This does not require a new TeX parser and does not use OCR. The deterministic layer protects payload; the visual layer catches typesetting/glyph/layout failures after the payload survives.

## 4. Reality and ownership remain unchanged

Current source still shows:

- SKILL.md declares Pandoc + XeLaTeX as the default and prohibits silent Chromium fallback;
- build_chinese_math_header.py defines the current bundle-local TeX Gyre / Noto font chain;
- validate_pdf_layout.py currently checks page count, embedded fonts, CJK extraction/ToUnicode, table survival, and first-page preview, but not the stronger v0.2 contracts;
- the canonical execution logic is still delegated to repo-external render_resources/chinese_math_pdf/scripts/render_markdown_pdf.sh;
- research-main still lacks render-chinese-math-pdf;
- presentation-desktop and server-research-baseline already install it;
- research-reporting explicitly does not own low-level PDF/LaTeX mechanics;
- the current Marketplace topology test keeps renderer outside central plugin membership.

That last test is a topology regression for the current chosen architecture, not a permanent constitutional rule. v0.2 preserves it because this round independently chooses standalone/profile integration; the test does not dictate that choice.

## 5. Target product behavior

A normal user should be able to request a formal scientific/technical PDF and receive, in one normal path:

- the correct resolved render authority;
- semantic Markdown handling rather than line-shape guessing;
- preserved mathematical payload;
- readable math/glyphs/tables;
- stable resolved profile identity;
- coherent typography validated on the complete artifact;
- truthful failure when the required engine/companion is unavailable.

The user should not have to discover that formulas are broken, tell Codex to use XeLaTeX, then discover that prose has been shrunk or paper geometry changed.

## 6. Target architecture

### 6.1 Repo-owned production orchestration

Add a canonical repo-owned entry under render-chinese-math-pdf. It owns:

- route resolution according to the authority precedence in Section 3;
- resource discovery;
- canonical Markdown Pandoc + XeLaTeX execution when no higher route exists;
- QA invocation;
- truthful failure states.

Host-local render_resources continues to provide fonts, texmf, caches, and other local resources. It no longer owns reusable orchestration semantics.

Explicit Chromium rendering remains an opt-in diagnostic route only.

### 6.2 Markdown semantics

For canonical Markdown rendering:

Markdown -> Pandoc reader -> AST -> optional minimal Lua filter -> LaTeX writer -> XeLaTeX -> PDF -> QA.

Use actual Pandoc AST node types, including Header, Para, List, Table, Math, CodeBlock, Figure, and BlockQuote. Do not implement a replacement parser that infers semantic type from extracted line shape.

A Lua filter is optional and only justified for a concrete transformation that the default writer/profile cannot express safely.

### 6.3 Default formal-note profile with bounded calibration

The canonical default profile is version-controlled and declarative.

Starting calibration candidate:

- A4;
- 11pt body;
- 25mm margins;
- approximately 1.15 line spacing;
- no automatic TOC;
- no automatic section numbering;
- no heuristic prose downscaling.

Only the numeric/visual values are calibration candidates. The semantic prohibitions are already frozen.

The final selected values must be recorded by the renderer/profile source and evidence before final-candidate freeze. Retry stability thereafter uses the resolved profile identity.

### 6.4 Authority precedence and native LaTeX

Route resolution is:

1. explicit user / venue / project render contract;
2. source-specific explicit settings;
3. canonical formal-note default.

Native .tex stays direct XeLaTeX unless its own higher-authority project contract says otherwise. The canonical Markdown wrapper must not force native LaTeX through Pandoc.

Project/venue templates keep their own typography. Canonical font allowlist enforcement is scoped to canonical formal-note output only.

### 6.5 Font coordination

Canonical formal-note fonts remain:

- TeX Gyre Termes for Latin;
- TeX Gyre Termes Math for math;
- Noto Serif SC for CJK serif;
- Noto Sans SC for CJK sans/mono support.

fontspec metrics-based Scale=MatchLowercase, MatchUppercase, or MatchAveragecase may be tested during the single bounded calibration cycle. It is not accepted merely because the option exists; it must improve actual complete render quality without regressions.

Unexpected Liberation / DejaVu / Droid fallback fails canonical-default font QA. Project/venue routes use their own declared font identity instead.

### 6.6 Math fidelity

For frozen fixtures, create the ordered Math(mathtype, text) semantic signature before transformations and compare it after the relevant Pandoc stage.

Generated-TeX survival verifies formula content using exact expected snippets or fixture-specific critical-token anchors. The contract is not “a math node still exists”; the mathematical payload must remain meaningfully identical.

The regression bank includes:

- hat;
- subscripts and superscripts;
- sum and integral;
- gradient/operator notation;
- Greek;
- matrix;
- mathbb;
- long formula;
- Chinese-adjacent inline and display math.

Actual equation-heavy pages are then rasterized and visually reviewed.

### 6.7 Complete-artifact QA

Final candidate QA includes:

- pdfinfo;
- pdffonts;
- pdftotext -layout;
- canonical-route font identity;
- math payload evidence;
- table survival;
- relevant overflow/bounding-box checks;
- complete page renders or complete montages;
- qualitative review of typography, hierarchy, density, equations, tables, title/numbering, clipping, and whitespace.

Mechanical font allowlists cannot substitute for G3 visual judgment.

## 7. Research Authoring integration remains bounded

The v0.2 integration statement is deliberately narrow:

Research Authoring document semantics  
-> shared renderer artifact-mechanics handoff.

This does not approve the unresolved full four-component architecture in RESEARCH_WRITING_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-07.md, nor its future artifact-adapter coordinator, Quarto, or Manubot directions.

This round does only:

- add renderer to research-main profile;
- teach research-reporting to delegate an explicitly requested formal PDF after document semantics are stable;
- keep Markdown-only output unchanged;
- fail closed with a clear companion dependency if standalone Marketplace research-writing lacks renderer;
- prevent research-reporting from inventing a private browser/XeLaTeX template as fallback.

Release README/changelog must describe this truthfully. They must not claim that installing the Research Authoring Marketplace plugin alone automatically includes the renderer.

## 8. External research correction and adoption

Planner rechecked current official sources for v0.2.

### Pandoc

Official Pandoc docs confirm:

- reader -> AST -> filter -> writer is a supported architecture;
- Lua filters operate directly on Pandoc AST;
- Math exposes mathtype and text;
- defaults files support stable command/options configuration;
- XeLaTeX supports geometry, papersize, fontsize, CJKmainfont, mathfont, and linestretch.

Decision: ADOPT defaults/templates; SELECTIVELY_ADOPT Lua only where a concrete semantic transform is needed.

Sources:
- https://pandoc.org/MANUAL.html
- https://pandoc.org/filters.html
- https://pandoc.org/lua-filters.html

### fontspec

Current official fontspec documentation supports Scale=MatchLowercase, MatchUppercase, and MatchAveragecase. MatchAveragecase was added in fontspec 2.9a.

Decision: metrics-based scaling remains a bounded calibration candidate, never a mechanical PASS criterion.

Sources:
- https://latex3.github.io/fontspec/fontspec.pdf
- https://latex3.github.io/fontspec/CHANGES.html

### Quarto

Quarto has mature PDF configuration for CJKmainfont, main/math font options, geometry, papersize, and linestretch. Its standard LaTeX PDF route still depends on Pandoc/LaTeX concepts and does not itself fix this task's proven failure that the intended production path was not consumed and QA did not catch bad output.

Decision: REFERENCE_ONLY in this round.

Sources:
- https://quarto.org/docs/reference/formats/pdf.html
- https://quarto.org/docs/output-formats/pdf-basics

### Typst — corrected from v0.1

v0.1 described Typst migration too broadly as necessarily changing Markdown/formula input. Current Pandoc supports a Typst writer and typst as a PDF engine. Pandoc also exposes Typst variables including template, margin, papersize, mainfont, mathfont, fontsize, and linestretch.

Therefore Typst is a more realistic future alternative than v0.1 implied.

However, no current evidence makes XeLaTeX the root cause. The known failures are route non-consumption, ad-hoc block classification, unstable defaults, and insufficient QA; the repository already has XeLaTeX fonts/resources/tests and direct-.tex compatibility.

Decision: REVIEWED_NOT_ADOPTED for this round. If representative complete tasks later show that the frozen XeLaTeX route itself cannot meet quality/reliability requirements, stop and return to Planner/Critic rather than silently migrating.

Source:
- https://pandoc.org/MANUAL.html

No Typst implementation, dependency, or comparative benchmark is added to v0.2.

## 9. Capability Gate Matrix v0.2

| Gate | Capability / normal entry | Required evidence | Failure | Regression / should-not-change | Final candidate |
|---|---|---|---|---|---|
| G1 Production route identity | ordinary formal PDF request uses resolved authority and canonical Pandoc+XeLaTeX when default applies | actual command/route receipt + PDF producer/engine + dependency failure behavior | silent Chromium, host-only orchestration as canonical logic, false success | explicit Chromium diagnostic remains available | YES |
| G2 Math/source/font fidelity | mixed CJK/English/math canonical render | ordered Math(mathtype,text) signatures; generated-TeX content/token survival; compile success; canonical font identity; equation-heavy raster review | changed math payload, lost operator/variable, raw TeX leak, wrong canonical fallback font, bad rendered math | existing CJK extraction/table checks remain | YES |
| G3 Formal typography & semantic blocks | complete research/technical note through canonical default | complete render/montage; semantic Para/Table/Header behavior; bounded calibration evidence; independent qualitative review | prose shrunk by heuristic classifier, repeated title/numbering, poor density/whitespace/font texture, clipping | true table/caption/footnote may use justified typography | YES |
| G4 Stable resolved profile identity | same request rerender / bounded formula repair | recorded effective profile before/after retry; same paper/template/margins/numbering after freeze | unrequested A4/Letter or template/margin/numbering drift | explicit user format/template change creates new identity and is allowed | YES |
| G5 Research Authoring handoff | research-main request for formal PDF without naming renderer | clean research-main install includes renderer; research-reporting delegates; replay uses resolved renderer; missing companion blocks honestly | manual second prompt, ad-hoc renderer/template, silent browser fallback | Markdown-only report remains Markdown-only | YES |
| G6 Input diversity & authority compatibility | English note, CJK/math note, native .tex, project/venue-owned template, generic PDF non-render tasks | representative renders + direct-.tex evidence + project-template identity/QA + trigger/routing checks | native .tex forced through Pandoc, canonical default overwrites venue template, generic PDF extraction misroutes | higher-authority project/template settings preserved | YES |
| G7 Broad/full release integrity | shared skill/profile/plugin-source compatible release | targeted bank -> full tests/validate/audit -> generator parity -> research-main, presentation-desktop, server-research-baseline smoke; all same final candidate | evidence spliced across commits, generated/profile regression, Presentations companion break | ten-plugin topology and Presentations production source/version unchanged | YES |

Gate count remains seven.

Regression mapping remains:

- Chromium bypass -> G1;
- math/font validator miss -> G2;
- visual inconsistency / block misclassification -> G3;
- page-identity drift -> G4;
- Research Authoring handoff -> G5;
- project template/direct .tex/input diversity -> G6;
- full shared/profile release compatibility -> G7.

## 10. Calibration and final-candidate chronology

The implementation chronology is frozen as:

1. implement canonical route and deterministic contracts;
2. run cheap known regressions;
3. render the initial default-profile candidate on predeclared representative complete inputs;
4. perform one bounded calibration cycle, with at most one evidence-driven adjustment;
5. rerender the same representative inputs;
6. record the selected default profile;
7. freeze final-candidate code/profile/fixtures/rubric identity;
8. run G1–G7 release evidence on that same final candidate;
9. pre-final Critic directly inspects representative complete PDF/montage before release conclusion.

Known private historical PDFs remain development evidence and are not fresh final evidence.

## 11. Execution scope

Allowed production scope remains:

- skills/tools/documents-media/render-chinese-math-pdf/**
- skills/writing/research/research-reporting/SKILL.md
- profiles/research-main.json
- directly necessary renderer/research-writing/profile tests and repo-safe fixtures
- scripts/codex_marketplace_config.json only for approved research-writing version change, not renderer membership
- generated registry/catalog/Marketplace artifacts through existing generators
- renderer and research-writing TODO closure records
- docs/plugin-changelogs/research-writing.md
- CHANGELOG.md
- README.md
- task evidence under results/documents-media--scientific-pdf-rendering-reliability/
- private/exports only if already-authorized private render evidence must be retained.

Out of scope:

- slug rename;
- new central plugin;
- renderer Marketplace membership;
- full Research Authoring redesign;
- Clear Writing production changes;
- Presentations production changes;
- Bridge Kit / Host Policy / workflow architecture;
- Typst/Quarto runtime adoption;
- paid API;
- new external resource/font download;
- new schema/ledger/state machine.

## 12. Version / release

If implementation changes research-reporting behavior and the same final candidate passes all release gates:

Repository bump decision: PATCH  
Expected repository: 5.0.6 -> 5.0.7

Affected plugins:
- research-writing: 0.1 -> 0.2
- presentations: NO_BUMP
- all other central plugins: NO_BUMP

Standalone renderer has no invented plugin version.

Presentations is not bumped because its production source is not modified; G7 only protects existing companion compatibility.

README closure is mandatory. README/changelog must describe research-main/companion behavior accurately and must not imply that Marketplace research-writing alone bundles the renderer.

Maturity stays unchanged unless separately justified by real longitudinal evidence; this task does not attempt that.

## 13. Stop / return to Planner-Critic

Stop scope expansion if implementation would require:

- changing canonical slug;
- adding a central plugin or renderer Marketplace entry;
- adopting Typst/Quarto runtime;
- changing Presentations production source;
- changing the unresolved Research Authoring overall architecture;
- new network/font resources;
- new private data/provider/credential scope;
- paid model;
- Host Policy or destructive Git changes;
- changing G1–G7 semantics after approval.

Ordinary implementation/test/render bugs within the approved scope stay with Executor.

## 14. v0.1 -> v0.2 substantive changes

Only four design amendments are made:

1. exact style values change from prematurely frozen defaults to starting calibration candidates with one bounded adjustment before final-candidate freeze;
2. render authority now explicitly preserves user/venue/project contracts and native .tex direct XeLaTeX, and retry stability is defined over the resolved profile identity;
3. G2 math fidelity now preserves ordered Math(mathtype,text) payload and generated-TeX content, not only node existence;
4. Typst external-research description is corrected: Pandoc already supports Typst writer/engine and relevant layout/font variables, but Typst remains not adopted because the current failure evidence does not implicate XeLaTeX itself.

Everything else from the v0.1 architecture remains unchanged.

