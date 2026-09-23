# Scientific PDF Rendering Reliability — Pre-Final Recovery Critic Handoff v0.1

The recovery package to review is frozen at commit `cb8cb7873f3cd1818b0b7d1836eedcb6260542ce`.

You are the independent Critic thread for AI Research Stack. Review only the bounded pre-final recovery/release amendment for the already-approved task. Do not reopen the approved scientific PDF architecture, do not implement code, do not create or mutate the execution branch/worktree, and do not run paid API or automation.

## Active Review Context

target_repo: `YuukiAS/AI_Skills_Collection`  
target_plugin_or_domain: standalone `render-chinese-math-pdf` + bounded Research Authoring handoff  
design_topic_or_task_key: `documents-media--scientific-pdf-rendering-reliability`  
review_stage: `PRE_FINAL_RECOVERY`  
approved_architecture_package: `fe4351d0606488abfb5247f0bc172cab6c2c5905`  
reviewed_implementation_candidate: `ccc3ebdc22c85203512e1c6bc84de0e36d4fc8a1`  
release_baseline_main_before_recovery_docs: `0f00eec88879a925b623bdde34835f98b0120883`  
recovery_package_commit: `cb8cb7873f3cd1818b0b7d1836eedcb6260542ce`  
execution_branch: `reviewed/documents-media--scientific-pdf-rendering-reliability`  
execution_worktree: `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`

Recovery amendment:
`docs/design/scientific-pdf-rendering/SCIENTIFIC_PDF_RENDERING_PREFINAL_RECOVERY_AMENDMENT_V0_1.md`

Exact bounded Codex resume draft:
`docs/operations/prompts/SCIENTIFIC_PDF_RENDERING_PREFINAL_RECOVERY_RESUME_V0_1.md`

The two recovery documents are planning/control artifacts only. They do not modify production source.

## Required reads

First read latest `main` and actually read:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/PLUGIN_MATURITY.md`

Then read:

- the approved v0.2 Proposal / Goal / Kickoff at package commit `fe4351d0606488abfb5247f0bc172cab6c2c5905`;
- the two recovery package files at `cb8cb7873f3cd1818b0b7d1836eedcb6260542ce`;
- current implementation branch `reviewed/documents-media--scientific-pdf-rendering-reliability`;
- current candidate `ccc3ebdc22c85203512e1c6bc84de0e36d4fc8a1`;
- `results/documents-media--scientific-pdf-rendering-reliability/EVIDENCE.md`;
- current `render_scientific_pdf.py`, renderer `SKILL.md`, `research-reporting/SKILL.md`, relevant tests/receipts;
- latest-main `VERSION`, `scripts/codex_marketplace_config.json`, `CHANGELOG.md`, `README.md`, and research-writing changelog.

The release baseline `0f00eec...` is already repository 5.0.7 for 056. The later recovery-doc commits are docs-only and do not themselves create a new release.

## Stable findings to re-review

Do not reopen findings that are not implicated by this recovery. Re-review these exact IDs:

### PDF-PREFINAL-001

Planner disposition: ACCEPT.

Recovery contract requires:

- ordered `Math(mathtype,text)` preservation;
- all fixture-declared critical anchors/content must survive generated TeX, not merely one token;
- hat/mathbb/sum/integral/gradient/operators/Greek/matrix/subscripts/superscripts and the frozen semantics must participate where present;
- a negative partial-survival regression must fail;
- no full TeX parser and no OCR;
- copied source signature cannot masquerade as independent post-transform evidence; either state no AST transform exists or inspect the real transformed AST.

Check whether this is the minimum sufficient closure of frozen G2 without changing G2 semantics.

### PDF-PREFINAL-002

Planner disposition: ACCEPT.

Recovery contract requires:

- truthful noncanonical route identity for direct `.tex` and project-owned routes;
- unknown/null instead of invented canonical font/margin/profile fields;
- observed PDF metadata and source/project declarations when available;
- direct `.tex` checks only route-required dependencies, not canonical Noto/TeX Gyre resources unless its contract uses them;
- canonical font allowlist remains canonical-only;
- one repo-safe **actual** project/venue-owned render replay plus the native direct-`.tex` should-not-change replay;
- no new Gate.

Check whether this closes the false receipt and route-authority risk without weakening G6.

### PDF-PREFINAL-003

Planner disposition: ACCEPT.

Recovery contract requires a real G5 normal-entry replay:

- exact candidate `research-main` installed into a clean task-local replay project;
- fresh ordinary local Codex child using existing pinned/local replay machinery and existing account identity;
- natural formal-research-PDF request that does **not** name the renderer/internal route;
- evidence of actual `research-reporting` consumption and subsequent renderer companion/canonical renderer consumption;
- a repo-safe representative complete source substantial enough for multi-page whole-document QA, without a fixed page-count benchmark;
- final PDF + complete pages/montage + route receipt;
- helper/direct-render evidence cannot substitute for G5;
- if the supported normal entry cannot run, stop with an exact blocker;
- Markdown-only behavior unchanged;
- stale renderer SKILL completion text must be updated from “first-page visual checks” to the frozen whole-document/risk-complete QA contract.

Check whether the resume draft names a realistic bounded normal-entry proof and does not invent another replay framework.

### PDF-PREFINAL-004

Planner disposition: ACCEPT.

Direct release facts already verified:

- latest release baseline main is repository `5.0.7`;
- main 5.0.7 belongs to 056 Product Delivery Discipline;
- main versions include workflow-core 0.3, ai-skills-core 0.4, web-development 0.2, research-writing 0.1, presentations 0.3;
- candidate branch also claimed repository 5.0.7 but with older workflow/maintainer/web-development versions and a conflicting 5.0.7 scientific-PDF changelog;
- branch and main diverged.

Recovery amendment says:

- preserve approved architecture and G1–G7;
- if execution preflight still sees the same main 5.0.7 release identity, ordinary non-force merge latest main **into the same reviewed branch**;
- preserve every released main plugin version and the existing 5.0.7 changelog;
- this task becomes repository `5.0.8`;
- only research-writing changes `0.1 -> 0.2`;
- presentations NO_BUMP;
- standalone renderer has no plugin version;
- regenerate from reconciled source and rerun all final-candidate gates, with G7/version/README/profile compatibility on the new candidate;
- if main release identity or target production semantics changed, stop instead of inventing another version.

Check that this is the smallest valid release amendment and that merging main into the task branch is safe within the existing authorization boundary. It does **not** authorize merging the task to main.

## Decisions that remain frozen

Do not reopen without a genuinely new fact directly caused by this recovery:

- standalone renderer;
- canonical slug;
- central plugin count;
- Research Authoring Marketplace membership;
- Pandoc/XeLaTeX vs Typst/Quarto;
- paid review;
- full Research Authoring redesign;
- G1–G7 taxonomy.

PDF-PREFINAL-001/002/003 are implementation/evidence repairs already required by v0.2. PDF-PREFINAL-004 is the only release-identity amendment.

## Review standard

For each old finding, give ACCEPT_CLOSED or STILL_OPEN and cite direct current evidence. New blockers are allowed only for a new fact, a previously missed direct release/product risk, or a regression introduced by the recovery amendment. Do not create blockers from package SHA movement caused only by these review docs.

Also review the exact resume draft for:

- same task/branch/worktree;
- bounded main reconciliation;
- no architecture redesign;
- no paid/private/provider/credential expansion;
- no force/rebase/main merge;
- correct 5.0.8 conditional release semantics;
- same-final-candidate G1–G7 rerun;
- actual G5 normal-entry evidence;
- pre-final return to Critic before integration.

If the recovery package is sufficient, return a clear PASS for this recovery amendment and an approved bounded Codex resume. The PASS does not mean the implementation is complete; it only allows Codex to resume the same task and repair the four findings.

If REVISE, keep stable finding IDs (or clearly identify a truly new blocker) and automatically provide the complete next Planner prompt required by the Critic Role Contract.

