# Scientific PDF Rendering Reliability — Kickoff Draft v0.2

Use this prompt only after an independent Critic reviews the exact v0.2 Proposal + Goal + this Kickoff and returns READY_FOR_CODEX=YES.

## Kickoff

Repository: YuukiAS/AI_Skills_Collection

Exact task: documents-media--scientific-pdf-rendering-reliability  
Exact execution branch to create from kickoff-time verified compatible origin/main: reviewed/documents-media--scientific-pdf-rendering-reliability  
Exact task-owned worktree: /tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability

Canonical Proposal:
docs/design/scientific-pdf-rendering/SCIENTIFIC_PDF_RENDERING_RELIABILITY_PROPOSAL_V0_2.md

Canonical Goal:
docs/goals/SCIENTIFIC_PDF_RENDERING_RELIABILITY_GOAL_V0_2.md

This is implementation only. Do not redesign the architecture.

First read current AGENTS.md, the approved v0.2 Proposal/Goal, the current Planner/Critic contracts, Capability Gate policy, version policy, target TODO/source/tests/profiles, and verify kickoff-time origin/main has no relevant semantic drift.

## Required implementation

Implement the exact v0.2 contract:

1. make render-chinese-math-pdf use a repo-owned canonical production orchestration path;
2. preserve render authority:
   explicit user / venue / project contract
   > source-specific explicit settings
   > canonical formal-note default;
3. for ordinary Markdown without stronger authority, use Pandoc AST -> LaTeX -> XeLaTeX;
4. keep native .tex on direct XeLaTeX by default; do not round-trip it through Pandoc;
5. keep Chromium/browser rendering as explicit diagnostic only, never silent fallback;
6. use Pandoc semantic node types rather than tableline/line-shape classification;
7. harden ordered Math(mathtype,text) payload preservation, generated-TeX formula-content checks, font QA, resolved-profile identity, and whole-document render QA;
8. add the bounded Research Authoring handoff through research-reporting and install renderer in research-main;
9. keep Markdown-only Research Authoring requests unchanged;
10. if plugin-only Research Authoring lacks renderer, fail closed with the exact companion dependency;
11. keep renderer standalone, do not rename it, and do not add it as a Research Authoring Marketplace skill;
12. run the approved G1–G7 and release/compatibility checks on the same final candidate.

## Default-profile calibration authority

A4 / 11pt / 25mm / approximately 1.15 line spacing are starting calibration candidates, not pre-approved final values.

You are authorized to perform one bounded pre-final calibration cycle only:

1. render the starting candidate on the predeclared known-regression and representative complete inputs;
2. inspect complete artifacts under G3;
3. if evidence shows a real typography problem, make at most one evidence-driven profile adjustment;
4. rerender the same representative inputs;
5. select and record the final default profile;
6. freeze that profile before final-candidate identity is declared.

After final-candidate freeze, do not continue visual tuning.

The following are already frozen and are not calibration variables:

- no unrequested paper/template/profile change;
- no automatic TOC or section-numbering injection unless requested by the effective contract;
- no heuristic downscaling of ordinary prose;
- no fixing one object's overflow by changing unrelated prose typography;
- no post-final-candidate visual tuning.

Do not turn calibration into an open-ended A/B benchmark, new workflow, or sample chase.

## Effective-profile and template rules

Retry stability applies only to the same request resolved to the same effective profile.

Record the applicable route/profile identity, including higher-authority project/venue/source settings when present.

If the user explicitly changes paper size, venue template, class, or another format-defining requirement, treat that as a new effective profile identity; do not report it as a stability regression.

Canonical default font allowlist applies only to the canonical formal-note route.

Project/venue-owned templates may use their own fonts, class, margins, numbering, and paper size. Preserve those higher-authority settings and apply only the glyph/math/layout QA relevant to that route.

## Math-fidelity rules

For frozen regression fixtures:

- record and compare the ordered Math(mathtype,text) semantic signature;
- preserve expected payload through the approved Pandoc transformation path;
- generated LaTeX must contain the corresponding formula content or predeclared critical math-token anchors;
- include regression coverage for hat, subscript/superscript, sum/integral, gradient/operators, Greek, matrix, mathbb, long formula, and Chinese-adjacent inline/display math;
- visually inspect equation-heavy rendered pages after deterministic checks.

Do not claim fidelity from node count or delimiter presence alone.

Do not implement a new full TeX/math parser and do not use OCR as routine math validation.

## Bounded Research Authoring integration

This task freezes only:

Research Authoring document semantics -> shared renderer artifact-mechanics handoff.

Do not implement or claim approval of the broader unresolved Research Authoring redesign.

Do not add renderer to scripts/codex_marketplace_config.json skill membership.

research-main is the complete profile-based PDF workflow in this round. Standalone Marketplace research-writing without the renderer companion must fail closed for formal PDF requests.

Release README/changelog must not imply that Research Authoring plugin installation alone bundles the renderer.

## Validation and final-candidate discipline

Run the Goal v0.2 validation chronology.

At minimum preserve:

- G2 ordered Math payload/content evidence;
- G3 complete-artifact typography review;
- G4 same-effective-profile stability plus deliberate format-change semantics;
- G6 direct-.tex and project/venue-template should-not-change cases;
- G7 full repo + research-main + presentation-desktop + server-research-baseline compatibility.

All release-critical evidence must come from the same final candidate.

Pre-final independent Critic must actually receive and inspect representative complete PDF/montage evidence. Mechanical tests do not substitute for that review.

Known historical private PDFs are development evidence only and are not fresh final evidence.

No paid review is authorized.

## Expected release closure, only if all gates pass

Repository: 5.0.6 -> 5.0.7  
research-writing: 0.1 -> 0.2  
presentations: NO_BUMP  
all other central plugins: NO_BUMP  
maturity: unchanged

Standalone renderer gets no invented plugin version.

README closure is mandatory and must describe profile/companion behavior truthfully.

## Authorized scope when the user sends this approved Kickoff

Allowed:

- ordinary fetch/read of YuukiAS/AI_Skills_Collection;
- creation of the exact branch and exact task-owned worktree above;
- modification only of Goal-approved renderer, research-reporting, research-main, directly necessary tests/fixtures, approved version/release metadata, generated parity files, TODO/changelog/README closure, and task evidence paths;
- local deterministic tests;
- Pandoc/XeLaTeX rendering with already-authorized local resources;
- profile install smokes;
- existing zero-paid CI normally required by the Goal;
- ordinary non-force commits and push of the exact execution branch;
- complete page/montage evidence generation from repo-safe or already-authorized inputs.

Not authorized:

- force push, rebase/history rewrite, branch deletion;
- merge to main or PR unless a later approved integration step authorizes it;
- Host Policy/execpolicy changes;
- Bridge Kit changes;
- paid API/Terra;
- new provider/credential/data scope;
- new network font/resource downloads;
- copying private unpublished research content into public tracked paths;
- changing Presentations or Clear Writing production behavior;
- canonical slug rename;
- new central plugin;
- renderer Marketplace membership;
- Typst/Quarto runtime migration;
- broader Research Authoring redesign;
- changes to approved G1–G7 semantics.

If the approved Pandoc/XeLaTeX route proves inadequate on representative complete artifacts and fixing it would require one of the forbidden scope changes, stop with direct evidence and return to Planner/Critic. Do not silently migrate engines.

Ordinary implementation/test/render bugs inside the frozen scope must be fixed by Executor without asking the user to debug.

Before yielding:

- save all required task evidence in the approved repo paths;
- commit and push all task-owned tracked changes to the exact execution branch;
- verify remote tip equals intended local HEAD;
- report real remaining gates;
- do not claim completion from tests, PDF existence, font embedding, or CI alone.

