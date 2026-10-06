# 059 Research Authoring — G4-C1 Failure Attribution Critic Review

Date: 2026-10-06  
Role: independent Critic  
Review object: G4-C1 failure attribution and minimal recovery  
Attribution package HEAD: `488c55ced4999c750b75ab071ef6104d9ec2b377`

## Result

```text
RESULT=REVISE
G4_CHATGPT_STAGE_FIRST_ATTEMPT=FAIL
FINAL_CANDIDATE_COMMIT=1c37c0715aca0096606f24e56192b7857e72bbd6
PRODUCTION_CANDIDATE_MODIFIED=NO
G1_G3_REOPEN=NO_ON_CURRENT_REVIEW
CODEX_PDF_STAGE_ALLOWED_NOW=NO
```

The Planner is correct that G4-C1 is real and that the current Research Authoring source already contains a clear renderer-owner boundary. However, the proposed attribution and recovery go one step too far: current evidence does not establish that the failure was merely a test-only harness bypass, and the proposed one-off stricter recovery prompt would not by itself prove the normal live ChatGPT entry is fixed.

## Independent live-source verification

The live PRIVATE USER-scope plugin was read directly:

- name: `research-authoring`
- version: `0.3.0`
- plugin id: `plugins_6ac4471b735881918c17cd310f262429`
- release id: `pluginrel_6ac4471c7b90819189bc23af890135f3`

Direct byte comparison against final candidate `1c37c0715aca0096606f24e56192b7857e72bbd6` confirms:

```text
skills/report/SKILL.md == C0 generated report/SKILL.md: YES
skills/report/_src/core/source.md == C0 generated core source: YES
skills/report/_src/report/source.md == C0 generated report source: YES
```

The canonical core explicitly says Research Authoring is not a renderer, excludes fonts/pagination/Pandoc/XeLaTeX/PDF QA/renderer implementation, and routes artifact mechanics to the renderer after semantics are stable.

The report delegate explicitly says not to implement low-level PDF/DOCX/PPTX/LaTeX mechanics, to hand formal PDF mechanics to `render-chinese-math-pdf`, and for standalone Research Authoring not to invent a private XeLaTeX route.

Therefore:

```text
MISSING_RESEARCH_AUTHORING_RENDER_OWNER_RULE=NO
```

## Independent failed-package verification

The uploaded `advisor_update_codex_handoff.zip` has SHA-256:

`afc2efd74b80c7e4675dc7133b4c4b5627f92360d92741354efdfe10d6516879`

`CHATGPT_AUTHORING_QA.md` directly claims:

- local XeLaTeX QA compile;
- a four-page A4 PDF;
- rendering every page to images and visually inspecting them;
- PDF text extraction.

`CODEX_PRODUCTION_HANDOFF.md` separately assigns final compile/render/text-extraction QA to Codex.

Thus the first ChatGPT stage both created the correct downstream Codex contract and prematurely executed part of it. The frozen rubric's no-render requirement was violated. The first attempt remains permanently FAIL.

## Blocker G4-C1-R1 — attribution overstates “test harness” evidence

**Requirement**

A final Gate recovery must test the real normal product entry. Existing repository policy says that when a rule already exists but behavior still fails, first locate whether the caller, entry, consumer, runtime, or product mechanism failed. It does not allow a one-off evaluation prompt to substitute for a production-consumed fix.

**Direct evidence**

The failed run was produced through the live `research-authoring` ChatGPT surface using the frozen natural G4 request. The live source already contained the renderer-owner rule, yet the normal ChatGPT runtime still performed XeLaTeX compile/render/PDF extraction.

The current package does not contain evidence of a separate non-production test harness that forced this behavior. The fact that the wrapper itself contains no renderer runtime only proves the work came from generic ChatGPT/runtime capabilities; those capabilities are present on the normal ChatGPT surface too.

**Causal risk**

Calling this `TEST_RUNTIME_HARNESS_BOUNDARY_BYPASS` without identifying a distinct test-only harness can misclassify a normal-entry consumer failure as evaluation infrastructure.

If the recovery merely adds a special command blacklist to the final-test prompt, the model may pass the known test while ordinary users invoking the same live plugin remain able to hit the same boundary violation.

That would violate the project principle that normal-use behavior matters more than a test-specific PASS.

**Minimum closure**

Planner must identify the exact production-consumed mechanism that will enforce the boundary in normal use.

One of the following must be established:

1. There is an existing always-consumed ChatGPT entry/consumer harness distinct from the frozen natural request, and the first run demonstrably bypassed or misconfigured it. Then the exact harness can be corrected and bound to the production identity without modifying Research Authoring source; or
2. No such production-consumed harness exists. Then this is a normal-entry consumer/product-integration failure and the fix must land in a real production-consumed entry/wrapper/source mechanism, not only in the evaluation prompt.

A one-off recovery prompt that is used only for G4 evaluation does not close this blocker.

**Owner**

Planner.

## Blocker G4-C1-R2 — proposed recovery is output-informed evaluation tuning

**Requirement**

Capability Gate policy requires final evidence to represent the final production identity and forbids proxy/test-specific PASS. Fresh/holdout evidence is only valid after candidate and review criteria are frozen; real infrastructure/reviewer repair must be distinguished from product repair.

**Direct evidence**

The proposed recovery harness was written after observing the exact failed behaviors and adds a command-level blacklist for XeLaTeX, latexmk, PDF creation/opening/rendering, screenshots, pdftotext, pdfinfo, pdffonts, QA/preview/test PDFs.

The proposed rerun would use the same live wrapper, same G2 baseline, same G4 task, and the newly tightened test-only invocation.

**Causal risk**

If this command blacklist is not part of the normal production consumer path, a PASS would only prove that ChatGPT follows an explicit test-specific prohibition after the failure was known. It would not prove that Research Authoring's ordinary live invocation respects its owner boundary.

**Minimum closure**

Before any new G4 run, Planner must state whether the stricter boundary is:

- a real production-consumed ChatGPT entry/consumer rule that will apply outside this test; or
- evaluation-only scaffolding.

If production-consumed, bind its exact identity and explain why it does not modify candidate C or why a new production identity is required. Then Critic can review the invalidation scope.

If evaluation-only, it may be used as a diagnostic probe but **cannot** support final G4 PASS. A real normal-entry repair is still required.

**Owner**

Planner.

## Current evidence-validity ruling

Because no production repair has yet been approved or performed:

- final candidate C remains unchanged;
- G1, G2, G3 remain valid for now;
- live Plugin Creator create/readback evidence remains valid;
- first G4 ChatGPT package remains immutable FAIL;
- no Codex PDF-stage evidence exists, so nothing there needs invalidation yet.

The Planner's proposed final invalidation scope cannot be fully approved until the repair layer is identified. If the eventual fix changes `research-authoring-core`, `research-reporting`, generated routing, or another candidate-owned production path, a new candidate must be formed and same-final-candidate policy applied. If the fix is truly outside candidate C but changes the live wrapper/production consumer identity, its own affected Gate scope must still be frozen and reviewed before rerun.

## Critic decision in plain language

The product documentation/rules are not missing the renderer boundary. The failure is that the real ChatGPT consumer did not obey that boundary.

The Planner now needs to find **where normal ChatGPT invocation is supposed to enforce those existing rules**. It must fix that real entry/consumer path, or prove that an existing production harness was accidentally bypassed.

It is not enough to give the next test a longer “do not run XeLaTeX” prompt and then call the plugin fixed.

No new G4 ChatGPT run is approved yet.
