# Scientific PDF Rendering Reliability — Pre-Final Recovery / Release Amendment v0.2

Date: 2026-09-23  
Status: READY FOR INDEPENDENT CRITIC RE-REVIEW / NOT CODEX RESUME AUTHORIZATION  
Task: `documents-media--scientific-pdf-rendering-reliability`  
Review stage: `PRE_FINAL_RECOVERY_R2`  
Approved architecture package: `fe4351d0606488abfb5247f0bc172cab6c2c5905`  
Current implementation candidate: `ccc3ebdc22c85203512e1c6bc84de0e36d4fc8a1`  
Previous recovery package: `cb8cb7873f3cd1818b0b7d1836eedcb6260542ce`  
Execution branch: `reviewed/documents-media--scientific-pdf-rendering-reliability`  
Execution worktree: `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`  
Latest main verified before this revision: `644c4ad62b47d52e3467e42689958630339bea4c`

This v0.2 recovery amendment supersedes the sequencing in
`SCIENTIFIC_PDF_RENDERING_PREFINAL_RECOVERY_AMENDMENT_V0_1.md` without reopening the approved architecture.

Only `PDF-PREFINAL-004` is amended here.  
`PDF-PREFINAL-001`, `PDF-PREFINAL-002`, and `PDF-PREFINAL-003` remain exactly as approved/closed in the previous recovery review and their implementation/evidence requirements are unchanged.

No production source, execution branch, worktree, Gate taxonomy, authorization boundary, plugin topology, renderer architecture, or engine choice is changed by this Planner document.

## 1. Finding disposition

### PDF-PREFINAL-004 — ACCEPT, sequencing corrected

The previous recovery package contained a real final-candidate contradiction:

- it said the new repository `5.0.8` changelog section should be added only after the repaired candidate passed release gates;
- but it also required one frozen final candidate to pass G1–G7 including release/version/README/generated checks.

Those two rules cannot coexist. If release metadata is added after candidate A passes the gates, the result is candidate B, so the actual release metadata was not validated by the same final candidate.

v0.2 corrects only that ordering.

## 2. Corrected release-candidate sequence

The exact sequence is now:

1. **Fetch and reconcile latest main first.**
   - In the existing task worktree, fetch `origin/main` and the exact reviewed branch.
   - If latest main still has the verified release identity:
     - repository `5.0.7`;
     - workflow-core `0.3`;
     - ai-skills-core `0.4`;
     - web-development `0.2`;
     - research-writing `0.1`;
     - presentations `0.3`;
     and target renderer / research-reporting / research-main production semantics remain compatible with the approved recovery, merge latest main into the same reviewed branch with an ordinary non-force merge.
   - Preserve every already-released main version and preserve main's existing `5.0.7` changelog exactly as historical truth.
   - If the release identity or target semantics have changed, stop and return to Planner/Critic.

2. **Perform the already-approved PDF-PREFINAL-001/002/003 repairs.**
   - No requirement for those findings changes in this amendment.

3. **Prepare the intended release metadata before final-candidate freeze.**
   On the reconciled reviewed branch, after implementation/evidence repairs are ready and before the final-candidate commit is frozen, prepare the exact intended release state:
   - repository `VERSION = 5.0.8`;
   - preserve the existing main `5.0.7` changelog section unchanged;
   - add a new `5.0.8` scientific-PDF release section above `5.0.7`;
   - set `research-writing = 0.2`;
   - preserve every other latest-main released plugin version, including:
     - workflow-core `0.3`;
     - ai-skills-core `0.4`;
     - web-development `0.2`;
     - presentations `0.3`;
   - standalone `render-chinese-math-pdf` still has no plugin version;
   - update README to repository `5.0.8`, Research Authoring `0.2`, and the already-approved truthful research-main/renderer-companion wording while preserving all other latest-main plugin versions;
   - regenerate registry/catalog/Marketplace/generated payloads from the reconciled source;
   - preserve latest-main release history instead of copying stale generated/version files from the old candidate.

4. **Freeze one exact final release-candidate commit containing both implementation and intended release metadata.**
   This commit must contain:
   - the PDF-PREFINAL-001/002/003 repairs;
   - tests and repo-safe fixtures;
   - evidence contracts and candidate-bound source/request inputs;
   - the reconciled latest-main state;
   - the intended `5.0.8` release metadata;
   - generated outputs corresponding to that source;
   - README/changelog/plugin-version state intended for release.

5. **Run all G1–G7 release-critical evidence on that exact commit.**
   G7 must directly verify, on the frozen candidate itself:
   - repository version `5.0.8`;
   - research-writing `0.2`;
   - preservation of all other latest-main released plugin versions;
   - preserved historical `5.0.7` changelog;
   - the new `5.0.8` changelog section;
   - README release/version/companion wording;
   - registry/catalog/Marketplace/generated parity;
   - research-main, presentation-desktop, and server-research-baseline compatibility.

6. **Any post-gate change to source or release metadata creates a new candidate.**
   If any release metadata, generated file, README/changelog text, production source, test, profile, or other candidate-bound artifact changes after G1–G7 begin or after a gate has passed, the resulting commit is a new candidate. All gates whose evidence depends on the changed content must be rerun on the new candidate. No cross-candidate release PASS may be assembled.

7. **Return the same exact candidate to independent pre-final Critic.**
   The Critic reviews the candidate that already contains the intended `5.0.8` release metadata and the G1–G7 evidence produced from that same commit.

8. **Only after independent Critic PASS may later integration/release-to-main occur.**
   No merge to main, release integration, branch deletion, or declaration that repository `5.0.8` is released is authorized by this recovery package.

## 3. Release-candidate metadata is not a released-main claim

Putting `VERSION=5.0.8`, the new `5.0.8` changelog section, Research Authoring `0.2`, README `5.0.8`, and matching generated payloads on the reviewed-branch final candidate means only:

> this commit is the exact unreleased release candidate that would become repository 5.0.8 if it later passes independent pre-final review and the separately authorized integration/release step.

It does **not** mean:

- main has already released 5.0.8;
- the candidate may bypass pre-final Critic;
- the reviewed branch may merge itself to main;
- release metadata can be treated as proof of release.

Until later integration occurs, current released main remains repository `5.0.7`.

## 4. Unchanged findings

### PDF-PREFINAL-001 — unchanged

The v0.1 recovery requirement remains binding exactly as previously reviewed:
ordered `Math(mathtype,text)`, strong all-critical-anchor/content survival, partial-formula negative regression, no full TeX parser/OCR, and truthful post-transform evidence semantics.

### PDF-PREFINAL-002 — unchanged

The v0.1 recovery requirement remains binding exactly as previously reviewed:
truthful noncanonical direct-`.tex` / project identity, route-scoped dependencies, canonical font allowlist only on canonical route, real direct-`.tex` replay, and one real repo-safe project/venue render replay.

### PDF-PREFINAL-003 — unchanged

The v0.1 recovery requirement remains binding exactly as previously reviewed:
actual candidate `research-main` normal-entry replay, natural user request without renderer naming, real research-reporting -> renderer consumption evidence, substantial multi-page whole-document QA, Markdown-only preservation, and corrected whole-document completion wording.

## 5. Architecture, Gates, versions and permissions unchanged

This v0.2 amendment does not reopen or change:

- standalone renderer;
- canonical slug;
- central plugin count;
- Research Authoring Marketplace membership;
- Pandoc/XeLaTeX vs Typst/Quarto;
- paid review;
- full Research Authoring redesign;
- G1–G7 taxonomy;
- conditional repository `5.0.8` choice while latest main remains current `5.0.7`;
- research-writing `0.1 -> 0.2`;
- presentations NO_BUMP;
- preservation of workflow-core `0.3`, ai-skills-core `0.4`, web-development `0.2`, and every other latest-main released version;
- ordinary non-force merge of latest main into the same reviewed branch;
- any existing private/provider/credential/network/Host Policy/destructive-Git boundary.

The only semantic change from recovery v0.1 is:

> intended release metadata is prepared **before** final-candidate freeze, so the exact candidate containing that metadata is the one that runs G1–G7 and returns to independent pre-final Critic.

