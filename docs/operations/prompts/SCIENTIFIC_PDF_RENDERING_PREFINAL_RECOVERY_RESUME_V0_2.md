# Scientific PDF Rendering Reliability — Pre-Final Recovery Resume Draft v0.2

Use this resume only after independent Critic approval of the exact v0.2 recovery amendment + this resume draft.

Repository: `YuukiAS/AI_Skills_Collection`  
Task: `documents-media--scientific-pdf-rendering-reliability`  
Review stage: `PRE_FINAL_RECOVERY_R2`  
Same execution branch: `reviewed/documents-media--scientific-pdf-rendering-reliability`  
Same task-owned worktree: `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`  
Reviewed implementation candidate: `ccc3ebdc22c85203512e1c6bc84de0e36d4fc8a1`  
Approved architecture package: `fe4351d0606488abfb5247f0bc172cab6c2c5905`  
Previous recovery package: `cb8cb7873f3cd1818b0b7d1836eedcb6260542ce`  
Revised recovery amendment: `docs/design/scientific-pdf-rendering/SCIENTIFIC_PDF_RENDERING_PREFINAL_RECOVERY_AMENDMENT_V0_2.md`

Do not redesign the renderer, Research Authoring integration, or G1–G7.

## 1. Preflight and main reconciliation

1. In the existing task worktree, fetch latest `origin/main` and the exact reviewed branch.
2. Confirm the branch is the expected task lineage and inspect latest main release/source identity.
3. If latest main still has:
   - repository `5.0.7`;
   - workflow-core `0.3`;
   - ai-skills-core `0.4`;
   - web-development `0.2`;
   - research-writing `0.1`;
   - presentations `0.3`;
   and target renderer / research-reporting / research-main semantics remain compatible, merge latest `origin/main` into the existing reviewed branch with an ordinary non-force merge.
4. Preserve every current-main released plugin version and preserve main's existing `5.0.7` changelog section unchanged.
5. Do not rebase, force push, rewrite history, create a replacement execution branch/worktree, or merge this task to main.
6. If latest main has another release identity or relevant target semantic overlap, stop and return to Planner/Critic.

Expected task release after that reconciliation remains:
- repository `5.0.8`;
- research-writing `0.2`;
- presentations NO_BUMP;
- standalone renderer no plugin version;
- every other central plugin preserves latest-main released version.

## 2. Repair PDF-PREFINAL-001 — unchanged from recovery v0.1

In the existing repo-owned renderer:

- keep ordered `Math(mathtype,text)` signatures;
- generated-TeX survival must require all fixture-declared critical anchors/content, not one surviving token;
- include hat, mathbb, sum, integral, gradient/operators, Greek, matrices, subscripts/superscripts and the other frozen regression semantics when present;
- add a negative regression where only a proper subset of required formula content survives and verify it fails;
- do not add a full TeX parser or OCR;
- if no AST transform/filter runs, record that there is no independently observed post-transform AST stage rather than copying source signature as independent evidence;
- if a filter/transform runs, inspect its actual output AST.

Update receipts and EVIDENCE accordingly.

## 3. Repair PDF-PREFINAL-002 — unchanged from recovery v0.1

For `direct-xelatex` and `project-command`:

- record truthful noncanonical effective identity;
- do not fill canonical profile id/fonts/margins/line spacing unless explicitly established by the actual source/project contract;
- prefer observed PDF metadata and source/project declarations; use null/unknown for unknown values;
- direct `.tex` probes only dependencies genuinely needed for its route/project contract and does not require canonical Noto/TeX Gyre resources unless the source/project actually uses them;
- keep canonical font allowlist canonical-route-only;
- rerun the real direct-`.tex` should-not-change case;
- add one repo-safe actual project/venue-owned render replay that produces a real PDF, truthful receipt and applicable QA;
- do not add a new Gate.

## 4. Repair PDF-PREFINAL-003 — unchanged from recovery v0.1

Prove G5 through the actual normal Research Authoring workflow:

1. use a repo-safe representative complete research-report input substantial enough to exercise multi-page whole-document QA, without a fixed page-count benchmark;
2. install the exact candidate `research-main` into a clean task-local replay project using the existing AI_Skills installer;
3. use the existing pinned local Codex runtime / existing account identity for a fresh ordinary local child; do not create another replay framework, copy credentials, mutate live production identity, or use paid API/Terra;
4. send a natural formal advisor-facing research-PDF request without naming `render-chinese-math-pdf`, `render_scientific_pdf.py`, or another internal route;
5. preserve repo-safe evidence of:
   - natural request and source;
   - actual `research-reporting` consumption;
   - renderer companion / canonical renderer consumption;
   - route/receipt identity;
   - final multi-page PDF;
   - complete pages or montage;
6. direct helper/render calls do not close G5;
7. if supported normal entry cannot execute, stop with a precise blocker instead of substituting a helper;
8. preserve Markdown-only behavior;
9. update renderer `SKILL.md` completion wording from stale `first-page visual checks` to the frozen applicable whole-document / all-pages-or-risk-complete QA contract.

## 5. Prepare intended release metadata before final-candidate freeze — corrected PDF-PREFINAL-004 sequencing

After main reconciliation and repairs 001/002/003 are ready, but **before** final-candidate freeze:

1. set repository `VERSION` to `5.0.8`;
2. preserve main's existing `5.0.7` changelog section unchanged;
3. add the new `5.0.8` scientific-PDF release section above `5.0.7`;
4. set `research-writing` to `0.2`;
5. preserve:
   - workflow-core `0.3`;
   - ai-skills-core `0.4`;
   - web-development `0.2`;
   - presentations `0.3`;
   - every other latest-main released plugin version;
6. do not invent a standalone renderer plugin version;
7. update README to repository `5.0.8`, Research Authoring `0.2`, and truthful research-main/renderer-companion wording while preserving every other latest-main released plugin version;
8. regenerate registry, catalog, Marketplace and generated plugin payloads from the reconciled source;
9. verify generated/source version parity before freezing the candidate;
10. do not copy stale release/generated files from `ccc3ebdc...` over newer main content.

These files represent the intended **unreleased release candidate**. They do not claim main has already released 5.0.8.

## 6. Freeze one exact final candidate containing implementation + intended release metadata

Only after Sections 1–5 are complete:

1. commit the full reconciled state to the same reviewed branch;
2. this exact commit becomes the proposed final candidate;
3. record its SHA in EVIDENCE;
4. from this point, candidate-bound source, profile, tests, evidence contracts, VERSION, changelog, README and generated payloads are frozen for gate execution.

The old candidate `ccc3ebdc...` remains diagnostic history and cannot be the release candidate.

## 7. Run G1–G7 on that exact commit

Run all required release-critical gates against the exact final-candidate commit from Section 6.

At minimum:

- G1 canonical production-route identity;
- G2 strong Math payload/content preservation plus rendered equation evidence;
- G3 complete-artifact typography/whole-document render;
- G4 resolved-profile stability;
- G5 actual normal Research Authoring entry;
- G6 direct `.tex`, actual project/venue route, and authority compatibility;
- G7 full repo/release integrity including:
  - repository `5.0.8`;
  - research-writing `0.2`;
  - preservation of every other latest-main released plugin version;
  - preserved main `5.0.7` changelog;
  - new `5.0.8` changelog section;
  - README version/companion wording;
  - registry/catalog/Marketplace/generated parity;
  - full unittest / skills validate/audit as required;
  - research-main, presentation-desktop and server-research-baseline compatibility.

All release-critical evidence must be from this one commit.

## 8. Any later change creates a new candidate

If, after candidate freeze or after any candidate-bound gate has run, you change any:

- production source;
- profile;
- test or fixture relevant to the gate;
- evidence contract;
- VERSION;
- plugin version;
- CHANGELOG;
- README;
- registry/catalog/Marketplace/generated payload;
- other candidate-bound release metadata,

then the changed commit is a new candidate.

Rerun every required gate whose evidence depends on that changed content. Do not combine evidence from multiple candidate commits into one release PASS.

## 9. Return the same candidate to pre-final Critic

After the exact candidate passes its required G1–G7 evidence:

- update task EVIDENCE with the exact candidate SHA and artifact/receipt/montage locators;
- ordinary non-force push the same reviewed branch;
- verify remote tip equals that candidate;
- return that exact commit to independent pre-final Critic.

Do not modify source or release metadata merely to make the review look cleaner after gates have run. Any such modification creates a new candidate and triggers the rule in Section 8.

## 10. Release boundary

Having `VERSION=5.0.8`, a `5.0.8` changelog section, Research Authoring `0.2`, README `5.0.8`, and regenerated payloads on the reviewed branch means only that the branch contains the intended unreleased release candidate.

Until a later authorized integration/release step succeeds:

- main remains released at `5.0.7`;
- do not claim repository 5.0.8 is released;
- do not merge this branch to main;
- do not open/merge a PR unless later explicitly authorized;
- do not delete the branch.

Only after independent pre-final Critic PASS may later integration/release-to-main occur.

## 11. Authorization boundaries unchanged

No merge to main, PR integration, branch deletion, paid API, Terra, new provider/credential/private-data scope, new network resource/font download, Host Policy change, Bridge Kit change, force push, rebase/history rewrite, slug rename, new plugin, Marketplace renderer membership, Typst/Quarto migration, Presentations production change, Research Authoring redesign, or G1–G7 redesign is authorized.

Ordinary implementation/test/render failures inside the already-approved recovery remain Executor-owned.

