# Scientific PDF Rendering Reliability — Pre-Final Recovery Resume Draft v0.1

Use this resume only after the independent Critic reviews the exact recovery amendment + this resume draft and approves it. This is not a new architecture kickoff.

Repository: `YuukiAS/AI_Skills_Collection`  
Task: `documents-media--scientific-pdf-rendering-reliability`  
Review stage: `PRE_FINAL_RECOVERY`  
Same execution branch: `reviewed/documents-media--scientific-pdf-rendering-reliability`  
Same task-owned worktree: `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`  
Reviewed implementation candidate: `ccc3ebdc22c85203512e1c6bc84de0e36d4fc8a1`  
Approved architecture package: `fe4351d0606488abfb5247f0bc172cab6c2c5905`  
Recovery amendment: `docs/design/scientific-pdf-rendering/SCIENTIFIC_PDF_RENDERING_PREFINAL_RECOVERY_AMENDMENT_V0_1.md`

Do not redesign the renderer or G1–G7.

## 1. Preflight and main reconciliation

1. In the existing task worktree, fetch `origin/main` and the exact reviewed branch.
2. Confirm the reviewed branch is the expected task lineage and inspect latest main release/source identity.
3. If latest main is still repository `5.0.7` with relevant released versions:
   - workflow-core 0.3
   - ai-skills-core 0.4
   - web-development 0.2
   - research-writing 0.1
   - presentations 0.3
   and target renderer/research-reporting/research-main semantics have not changed, merge latest `origin/main` into the existing reviewed branch with an ordinary non-force merge.
4. Preserve main's existing 5.0.7 release history and every released plugin version. Do not rebase, force push, or merge this task to main.
5. If main has a new release or relevant semantic overlap, stop and return to Planner/Critic instead of inventing another release number.

After reconciliation, this task's expected compatible release is repository `5.0.8`, with only `research-writing 0.1 -> 0.2` as the affected central plugin. Presentations remains NO_BUMP. Standalone renderer has no plugin version.

## 2. Repair PDF-PREFINAL-001

In the existing repo-owned renderer:

- keep ordered `Math(mathtype,text)` signatures;
- make generated-TeX survival require **all** fixture-declared critical anchors/content, not any one surviving token;
- ensure structural semantics including hat, mathbb, sum, integral, gradient/operators, Greek, matrices, subscripts/superscripts and the other frozen regression cases participate when present;
- add a negative regression where only part of a formula survives and verify it fails;
- do not add a full TeX parser or OCR;
- remove the false implication that a copied source signature is independent post-transform evidence:
  - if no AST transform/filter runs, record that no post-transform AST stage exists;
  - if a filter/transform runs, inspect its actual output AST and compare the real post-transform signature.

Update receipts/EVIDENCE accordingly.

## 3. Repair PDF-PREFINAL-002

For `direct-xelatex` and `project-command`:

- record truthful noncanonical effective identity;
- do not populate canonical profile id/fonts/margins/line spacing into those routes unless explicitly declared by the actual source/project contract;
- prefer observed PDF metadata and source/project declarations; use null/unknown when not established;
- direct `.tex` must probe only route-required generic dependencies such as XeLaTeX and applicable PDF QA tools; do not require the canonical Noto/TeX Gyre resource bundle unless the source/project actually uses it;
- keep the canonical font allowlist canonical-route-only;
- rerun the real direct-`.tex` should-not-change case;
- add one repo-safe **actual project/venue-owned render route** replay through the existing project-command path or a documented equivalent, producing a real PDF, truthful receipt, and applicable QA.

Do not add a new Gate.

## 4. Repair PDF-PREFINAL-003

Prove G5 through the actual normal Research Authoring workflow.

1. Create/retain a repo-safe representative complete research-report input substantial enough to generate a multi-page artifact and exercise whole-document QA. Do not set a page-count benchmark.
2. Install the exact candidate `research-main` into a clean task-local replay project using the existing AI_Skills installer.
3. Use the existing pinned local Codex runtime / existing account identity for a fresh ordinary local child. Do not create another replay framework, copy credentials, mutate live production identity, call paid API/Terra, or require the user to debug it.
4. Send a natural user request for a formal advisor-facing research PDF **without naming** `render-chinese-math-pdf`, `render_scientific_pdf.py`, or an internal route.
5. Preserve repo-safe evidence of:
   - the natural request and source;
   - actual consumption of `research-reporting`;
   - the handoff consuming the installed renderer companion / canonical renderer;
   - canonical route/receipt identity;
   - final multi-page PDF;
   - complete page renders or montage.
6. A direct helper/render call does not close G5.
7. If the supported ordinary local Codex entry cannot actually execute, stop with a precise normal-entry probe blocker; do not substitute a lower-level helper and report G5 PASS.
8. Preserve Markdown-only should-not-change behavior.
9. Update `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`: replace stale “first-page visual checks” completion wording with the frozen applicable whole-document / all-pages-or-risk-complete visual QA requirement.

## 5. Release/version reconciliation — PDF-PREFINAL-004

On the reconciled branch:

- VERSION becomes `5.0.8` only if main preflight remains the approved `5.0.7` identity;
- preserve workflow-core `0.3`;
- preserve ai-skills-core `0.4`;
- preserve web-development `0.2`;
- set research-writing `0.2`;
- preserve presentations `0.3`;
- preserve all other latest-main plugin versions;
- keep main's existing 5.0.7 changelog section unchanged;
- add a new 5.0.8 scientific-PDF release section above it only after the repaired candidate passes release gates;
- regenerate registry/catalog/Marketplace payloads from reconciled source;
- update README from latest-main baseline to repository 5.0.8 + Research Authoring 0.2 while preserving all other released versions and truthful research-main/renderer-companion wording.

Do not copy stale branch release/generated surfaces over newer main state.

## 6. New final candidate and validation

The old candidate `ccc3ebdc...` is diagnostic history, not the new final candidate.

After repairs:

1. run targeted deterministic tests and the known regression bank;
2. rerun real direct-`.tex` and project/venue should-not-change evidence;
3. rerun the actual G5 normal Research Authoring replay;
4. freeze one new candidate commit;
5. on that same candidate rerun all G1–G7 release-critical evidence, including:
   - G2 math payload/content + rendered equations;
   - G3 complete-artifact typography/whole-document render;
   - G4 resolved-profile stability;
   - G5 normal Research Authoring entry;
   - G6 input/route authority compatibility;
   - G7 full unittest, skills validate/audit, generated parity, release/version/README checks, and research-main + presentation-desktop + server-research-baseline compatibility;
6. do not splice old-candidate gate evidence into release PASS;
7. update `results/documents-media--scientific-pdf-rendering-reliability/EVIDENCE.md` and store repo-safe request/source/receipts/PDF/page-montage evidence;
8. commit and ordinary non-force push to the exact reviewed branch;
9. verify remote tip equals intended candidate;
10. return to independent pre-final Critic with the new candidate and actual artifacts.

No merge to main, PR, branch deletion, paid API, Terra, new provider/credential/private-data scope, Host Policy change, Bridge Kit change, slug rename, new plugin, Marketplace renderer membership, Typst/Quarto migration, Presentations production change, Research Authoring redesign, or G1–G7 redesign is authorized.

If any such change becomes necessary, stop and return to Planner/Critic.

