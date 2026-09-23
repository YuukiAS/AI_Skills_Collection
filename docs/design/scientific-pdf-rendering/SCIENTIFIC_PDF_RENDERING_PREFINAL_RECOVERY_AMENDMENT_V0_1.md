# Scientific PDF Rendering Reliability — Pre-Final Recovery / Release Amendment v0.1

Date: 2026-09-23  
Status: READY FOR INDEPENDENT CRITIC REVIEW / NOT CODEX RESUME AUTHORIZATION  
Task: `documents-media--scientific-pdf-rendering-reliability`  
Review stage: `PRE_FINAL_RECOVERY`  
Approved architecture package: `fe4351d0606488abfb5247f0bc172cab6c2c5905`  
Current implementation branch: `reviewed/documents-media--scientific-pdf-rendering-reliability`  
Current implementation candidate reviewed: `ccc3ebdc22c85203512e1c6bc84de0e36d4fc8a1`  
Task worktree: `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`  
Latest main verified during Planner recovery: `0f00eec88879a925b623bdde34835f98b0120883`

This is a minimal pre-final recovery and release-identity amendment. It does not replace or reopen the Critic-approved v0.2 architecture:

- `docs/design/scientific-pdf-rendering/SCIENTIFIC_PDF_RENDERING_RELIABILITY_PROPOSAL_V0_2.md`
- `docs/goals/SCIENTIFIC_PDF_RENDERING_RELIABILITY_GOAL_V0_2.md`
- `docs/operations/prompts/SCIENTIFIC_PDF_RENDERING_RELIABILITY_KICKOFF_V0_2.md`

The approved v0.2 Proposal/Goal remain authoritative except where this amendment narrows the four pre-final closure requirements below and updates the release identity to account for the real `main` release collision.

No production source is modified by this Planner package.

## 1. Finding dispositions

### PDF-PREFINAL-001 — ACCEPT

The Critic finding is correct. Current candidate `render_scientific_pdf.py` weakens the frozen G2 contract in two ways:

- `math_anchor_tokens()` drops important structural commands including `hat`, `mathbb`, `sum`, and `int`;
- `generated_tex_math_survival()` passes a formula when **any one** anchor is found;
- `post_transform_math_signature` is currently the source signature copied into the receipt rather than an independently observed post-transform signature.

This is an implementation/evidence repair already required by approved v0.2 G2. It does not change the architecture or Gate taxonomy.

Required repair:

1. Preserve the ordered `Math(mathtype,text)` signature already frozen in v0.2.
2. For each frozen regression formula, declare a fixture-specific ordered set of critical anchors/tokens covering its actual structure. Critical structures such as `\hat`, `\mathbb`, `\sum`, `\int`, gradient/operators, Greek, matrices, subscripts/superscripts, and other frozen regression semantics must participate where present.
3. Generated-TeX survival passes only if **all predeclared critical anchors for that formula** survive, or an equivalently strong fixture-specific exact-content check passes. “At least one token survived” is forbidden.
4. Add a negative regression in which a formula retains only a proper subset of its required anchors; that regression must fail.
5. Do not build a complete TeX parser and do not use OCR.
6. If the production path performs no AST-transform/filter step, the receipt must say so and must not present a copied source signature as independent post-transform evidence. If a Pandoc filter/AST transform is added or used, obtain and compare the actual post-transform AST signature.

Minimum evidence: positive/negative deterministic tests plus the same final-candidate G2 rendered equation evidence.

### PDF-PREFINAL-002 — ACCEPT

The Critic finding is correct. The current direct-`.tex` route constructs `effective_profile` from the canonical JSON and runs the full canonical resource probe. The committed receipt therefore claims TeX Gyre/Noto/25mm canonical identity even though the actual direct-`.tex` PDF uses Latin Modern / Computer Modern.

This is an implementation/evidence repair already required by approved v0.2 authority precedence, G4, and G6. It does not change architecture or add a Gate.

Required repair:

1. Split route identity from canonical-profile identity.
2. `direct-xelatex` and `project-command` receipts must record truthful noncanonical identity:
   - authority and route;
   - source/project command or declared template/class when known;
   - actual/observed PDF metadata when available;
   - source/project-declared page/layout values when explicitly known;
   - `null` / `unknown` for values not established.
3. Never populate canonical TeX Gyre/Noto/margin/profile values into a noncanonical receipt merely because the CLI has a default profile file.
4. Direct `.tex` dependency checks must be route-scoped:
   - require `xelatex` and QA tools actually needed by the route;
   - rely on the source/project compilation to expose its own missing LaTeX packages/fonts;
   - do not require the canonical Noto/TeX Gyre resource bundle unless the source/project contract actually uses it.
5. Canonical font allowlist stays canonical-route-only.
6. Add one repo-safe **actual** project/venue-owned render replay through `project-command` (or an existing documented project/venue command that fits the approved route). The replay must produce a real PDF, truthful route/identity receipt, and applicable glyph/math/layout QA. A string/unit assertion alone is not sufficient.
7. Keep native `.tex` direct-XeLaTeX should-not-change evidence under G6.

### PDF-PREFINAL-003 — ACCEPT

The Critic finding is correct. Current candidate evidence proves profile installation, handoff instructions, and renderer execution separately, but not the frozen G5 normal entry:

`natural Research Authoring request -> research-reporting -> renderer companion -> final formal PDF`

without the user naming the renderer.

This is an implementation/evidence repair already required by v0.2 G5. It does not change architecture or Gate semantics.

Required repair:

1. Install the **exact candidate** `research-main` profile into a clean task-local replay project/environment using the existing AI_Skills installer.
2. Use the repository's existing pinned local Codex candidate/replay infrastructure and existing account identity where applicable. Do not create another replay framework, copy credentials, mutate the live production plugin identity, or use a paid API/Terra.
3. Start a fresh ordinary local Codex child in the task-local project with the installed `research-main` skills visible.
4. Give it a natural representative request such as “整理这份研究材料，输出一份正式 PDF 给导师阅读” **without mentioning** `render-chinese-math-pdf`, `render_scientific_pdf.py`, or another internal route name.
5. Use a repo-safe representative complete report/source that is substantial enough to exercise **multi-page whole-document QA**. Do not turn page count into a fixed benchmark.
6. Preserve:
   - the natural request/source;
   - evidence that the normal entry consumed `research-reporting`;
   - evidence that the handoff consumed the installed renderer companion / canonical renderer;
   - canonical route/receipt evidence;
   - final PDF;
   - complete page renders/montage.
7. A direct renderer invocation or helper-only test is not G5 normal-entry evidence.
8. If the existing supported local Codex normal entry cannot actually be executed in the environment, stop with a precise normal-entry probe blocker; do not substitute a lower-level helper and call G5 PASS.
9. Markdown-only Research Authoring behavior remains unchanged and stays in the should-not-change bank.
10. Update the renderer `SKILL.md` completion wording: `complete` must require the applicable whole-document / all-pages-or-risk-complete visual QA contract, not “first-page visual checks”.

### PDF-PREFINAL-004 — ACCEPT

The Critic finding is correct and is a genuine release-identity overlap.

Verified latest `main` at `0f00eec88879a925b623bdde34835f98b0120883` is already the formal repository release `5.0.7`, with:

- `workflow-core 0.3`;
- `ai-skills-core 0.4`;
- `web-development 0.2`;
- `research-writing 0.1`;
- `presentations 0.3`.

Its `CHANGELOG.md` owns `5.0.7` for 056 Product Delivery Discipline.

The task branch independently also labels itself repository `5.0.7`, but with older `workflow-core 0.2`, `ai-skills-core 0.3`, `web-development 0.1`, and a different 5.0.7 changelog section for scientific PDF rendering. That cannot be released or integrated as-is.

This is the only finding that amends frozen release identity.

## 2. Minimal release amendment

The scientific-PDF architecture and G1–G7 semantics remain unchanged.

At Executor resume preflight:

1. Fetch latest `origin/main` and the exact reviewed branch.
2. Verify the reviewed branch starts from the expected current candidate lineage and that main still contains the approved v0.2 package.
3. Verify current main release identity.
4. If main is still repository `5.0.7` and the relevant released versions remain:
   - workflow-core `0.3`;
   - ai-skills-core `0.4`;
   - web-development `0.2`;
   - research-writing `0.1`;
   - presentations `0.3`;
   then reconcile latest main **into the same reviewed branch** with an ordinary non-force merge. Do not rebase/force-push and do not merge the reviewed branch to main.
5. Resolve release/generated conflicts by preserving current-main released history and versions. Task-local scientific-PDF changes are then reapplied/preserved on top.
6. The scientific-PDF release becomes the next compatible repository patch:
   - repository: `5.0.7 -> 5.0.8`;
   - research-writing: `0.1 -> 0.2`;
   - presentations: `NO_BUMP`;
   - workflow-core: preserve `0.3`;
   - ai-skills-core: preserve `0.4`;
   - web-development: preserve `0.2`;
   - all other central plugins: preserve latest-main released versions;
   - standalone renderer: no plugin version.
7. Keep the existing main `5.0.7` changelog entry exactly as historical release truth. Add a new `5.0.8` scientific-PDF release section above it only after the repaired candidate passes release gates.
8. Rebuild registry/catalog/Marketplace generated layers from the reconciled source. Never restore the stale task-branch generated/version surfaces over newer main state.
9. README closure must be based on latest-main content and preserve all already-released plugin versions, then add only:
   - repository `5.0.8`;
   - Research Authoring `0.2`;
   - truthful research-main / renderer-companion wording.
10. Rerun G7/version/generated/README/profile compatibility on one new final candidate after reconciliation and repairs.

If latest main has advanced to another repository release or there is a new semantic overlap in renderer/research-reporting/research-main/version ownership, stop and return to Planner/Critic. Unrelated docs-only drift with the same release/source identity does not require another architecture review.

## 3. Main reconciliation boundary

Current comparison shows the reviewed branch and main have diverged. Since the task branch base, main changed many unrelated files; the target renderer/research-reporting/research-main production source did not overlap. The relevant overlap is release/generated/test surfaces.

Therefore the approved recovery permits only an ordinary merge of latest main **into** the existing reviewed branch. It does not authorize:

- merging the reviewed branch into main;
- creating a new branch/worktree;
- rebase, force push, history rewrite, branch deletion;
- dropping current-main released changes;
- resolving an unexpected semantic conflict by guessing.

If a conflict appears in an unrelated released area, preserve main. If a conflict reveals new target-production semantics beyond this amendment, stop and return to Planner/Critic.

## 4. New final-candidate requirement

Candidate `ccc3ebdc22c85203512e1c6bc84de0e36d4fc8a1` is no longer eligible as the final release candidate because findings 001–003 require source/evidence repair and finding 004 requires main reconciliation.

After all repairs and main reconciliation:

1. create one new candidate commit on the same reviewed branch;
2. regenerate all release/generated artifacts from that reconciled candidate;
3. run cheap targeted regressions first;
4. rerun all G1–G7 release-critical evidence on that same candidate;
5. G5 must use the actual normal Research Authoring replay defined above;
6. G6 must include actual project/venue route and truthful direct-`.tex` route evidence;
7. G7 must include latest-main released-version preservation plus research-main, presentation-desktop, and server-research-baseline compatibility;
8. save updated `EVIDENCE.md`, receipts, source/request, PDFs and complete page/montage evidence;
9. commit and push the exact reviewed branch and verify remote tip;
10. return to independent pre-final Critic. No release/integration to main occurs before that review.

No evidence from `ccc3ebdc...` may be used to claim a release gate on the new final candidate unless the evidence is rerun or is explicitly non-candidate-bound historical diagnostic evidence.

## 5. Architecture/Gate non-changes

This recovery does **not** reopen:

- standalone renderer ownership;
- canonical slug;
- central plugin count;
- Research Authoring Marketplace membership;
- Pandoc/XeLaTeX vs Typst/Quarto;
- paid review;
- full Research Authoring redesign;
- G1–G7 taxonomy.

PDF-PREFINAL-001/002/003 are repairs to evidence and implementation already demanded by v0.2. PDF-PREFINAL-004 changes only release identity and reconciliation sequencing.

## 6. Version decision after amendment

Repository bump decision: PATCH  
Expected, conditional on main still being 5.0.7 at execution preflight: `5.0.7 -> 5.0.8`

Affected plugins:

- `research-writing`: `0.1 -> 0.2`
  - Reason: the already-approved bounded Research Authoring formal-PDF handoff becomes a verified normal-entry user-visible improvement.
- `presentations`: NO_BUMP
  - Reason: no Presentations production behavior changes; only compatibility is replayed.
- `workflow-core`, `ai-skills-core`, `web-development`, and all other central plugins: preserve latest-main released versions; NO task-specific bump.
- standalone `render-chinese-math-pdf`: no plugin version.

Maturity remains unchanged.

## 7. Recovery stop conditions

Stop and return to Planner/Critic if:

- latest main is no longer the expected 5.0.7 release identity;
- target renderer/research-reporting/research-main production semantics changed on main;
- resolving main requires dropping or redesigning unrelated released behavior;
- G1–G7 semantics would need to change;
- normal Research Authoring replay requires a new credential/provider/private-data/paid scope;
- project/venue replay cannot be performed with a repo-safe route without widening architecture;
- Typst/Quarto migration, slug rename, Marketplace membership change, new central plugin, Presentations production change, Host Policy change, or destructive Git becomes necessary.

Ordinary implementation/test/render failures within this amendment remain Executor-owned.

