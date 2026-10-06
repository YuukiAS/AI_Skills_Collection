# 059 Research Authoring — G4-C1 Failure Attribution v2

Date: 2026-10-06  
Role: Planner  
Task: `research-authoring--formal-production-authoring`  
Branch: `work/research-authoring--formal-production-authoring`  
Current final candidate: `1c37c0715aca0096606f24e56192b7857e72bbd6`  
Prior Critic review: `results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_CRITIC_REVIEW.md`  
Prior Critic commit: `85305c4b8ff4ee1c68ee5efb1407fdd06610ef39`  
Prior result: `REVISE`

This document only refines failure attribution. It does not modify production, the live Plugin, frozen G4 task/rubric/baseline, or any final Gate evidence.

## 0. Decision

```text
G4-C1 = REAL_NORMAL_ENTRY_FAILURE
MISSING_RESEARCH_AUTHORING_RENDER_OWNER_RULE = NO
TEST_ONLY_HARNESS_FAILURE = NO
PRIMARY_ATTRIBUTION = NORMAL_ENTRY_CONSUMER_PRODUCT_INTEGRATION_FAILURE
CURRENT_CANDIDATE_MODIFIED = NO
NEW_G4_RUN_STARTED = NO
CODEX_PDF_STAGE_STARTED = NO
NEXT_HANDOFF = CRITIC
```

The first G4 ChatGPT stage remains permanently FAIL. XeLaTeX compile, PDF creation, page rasterization/visual inspection, and PDF text extraction all count as rendering/renderer QA under the frozen contract.

## 1. What actually enforces a Skill boundary in normal ChatGPT use?

Current OpenAI plugin/skill behavior gives a skills-only Plugin an instruction layer, not a separate capability sandbox.

For a normal installed/selected Plugin:

1. the Plugin exposes its Skills to ChatGPT;
2. the model sees Skill metadata such as name/description;
3. when the request matches a Skill, the model loads and follows its complete Skill instructions;
4. generic ChatGPT capabilities remain part of the surrounding product surface unless a separate controlled tool/app boundary exists.

Therefore there is no hidden hard enforcement layer in this wrapper that can technically prevent a generic runtime from running XeLaTeX. The normal production consumer is the activated Skill itself.

For this exact report-family request, the intended production-consumed entry is:

```text
live research-authoring Plugin
-> skills/report/SKILL.md
   routing_mode = coordinator-first
   coordinator_artifact_id = core
-> skills/report/_src/core/source.md
-> skills/report/_src/report/source.md
```

Canonical source/config locators:

```text
scripts/codex_marketplace_config.json
  research-writing
    -> skills[artifact_id=report]
       type=aggregate
       routing_mode=coordinator-first
       coordinator_artifact_id=core
       workflow_notes=[...]

skills/writing/research/research-authoring-core/SKILL.md
skills/writing/research/research-reporting/SKILL.md

generated:
plugins/codex/plugins/research-writing/skills/report/SKILL.md
plugins/codex/plugins/research-writing/skills/report/_src/core/source.md
plugins/codex/plugins/research-writing/skills/report/_src/report/source.md
```

The live Plugin Creator release contains these generated report files and the prior Critic independently confirmed they are byte-for-byte equal to candidate C.

## 2. Did this mechanism exist for the first G4 run?

Yes, it existed in the live Plugin and the frozen natural request clearly matched its report-family description.

It therefore **should** have been the normal production entry.

However, the first G4 package contains no runtime receipt equivalent to Codex's candidate-plugin replay proving that ChatGPT actually loaded `skills/report/SKILL.md` and then read the coordinator/delegate sources. Direct Plugin selection proves the Plugin was available/selected; it does not give us a per-turn Skill-consumption trace.

So two subcases remain observationally indistinguishable:

### A. Aggregate was loaded, but its fail-closed wording was not operational enough

Current aggregate workflow note says formal PDF mechanics belong to the renderer and standalone Research Authoring must fail closed when the renderer companion is missing.

The lower-level report source additionally says not to implement low-level PDF/LaTeX mechanics and not to invent a private XeLaTeX route.

The failed ChatGPT output nevertheless classified a local compile/render as “authoring-stage QA” while still assigning the “final” PDF to Codex. That is a real semantic loophole in how the normal consumer presented the already-correct owner boundary.

### B. Aggregate was not actually loaded despite the request matching it

Then the normal Plugin/Skill activation path itself failed to consume the required production entry.

Either subcase is a **normal-entry consumer/product-integration failure**. Neither supports the previous `TEST_RUNTIME_HARNESS_BOUNDARY_BYPASS` attribution.

## 3. Why the first failed run is not merely an evaluation-harness problem

The first run used:

- an ordinary ChatGPT conversation without a Project-specific harness;
- the live PRIVATE USER-scope `research-authoring` Plugin;
- the frozen natural G4 user request.

Generic ChatGPT runtime/file/compute capability is part of that real product surface. It is not a test-only executor.

The failure therefore demonstrates that “the source contains the owner rule” is insufficient. The **production-consumed report entry** did not reliably convert that rule into normal surface behavior.

The fix must land in a mechanism ordinary report-family Plugin requests consume, not only in the next Gate prompt.

## 4. Repair-location comparison

### Option A — ChatGPT wrapper entry

Possible surfaces:

- `.codex-plugin/plugin.json` description / longDescription / defaultPrompt;
- a wrapper-only extra Skill.

Assessment: **not preferred**.

Why:

1. `defaultPrompt` is a suggested invocation, not the guaranteed instruction body for arbitrary user prompts.
2. Plugin description/longDescription are discovery/interface metadata, not a reliable workflow enforcement layer.
3. Adding a wrapper-only behavioral Skill would create a Chat-specific behavior source that can drift from the canonical Research Authoring source and conflicts with the approved “one canonical source -> two surfaces” design.

A wrapper-only command blacklist could be useful as a diagnostic probe, but it is not the preferred production fix.

### Option B — generated report aggregate entry

Assessment: **preferred minimum production repair**.

This is the closest existing normal consumer to the failure:

```text
scripts/codex_marketplace_config.json
  -> research-writing
  -> report aggregate
  -> workflow_notes
  -> generated skills/report/SKILL.md
```

The aggregate is already responsible for:

- coordinator-first entry;
- report-family normal routing;
- formal-PDF handoff;
- fail-closed behavior without renderer companion.

The missing operational distinction should be fixed here, not duplicated across core/report prose.

The repair should say, in normal product terms rather than a test blacklist:

> On a surface where the approved renderer companion is unavailable, formal PDF production stops after stable scientific source plus a complete production handoff. “Artifact mechanics” includes compile-derived or PDF-derived QA: local/preview/QA XeLaTeX or Pandoc compile, PDF creation/opening/rendering, page raster/visual inspection, and PDF text/font/page extraction. Generic runtime/file/compute tools are not a substitute for the missing renderer companion. Leave these checks pending for the downstream production owner.

This applies to ordinary users of the standalone skills-only ChatGPT wrapper, not only G4.

A focused test should assert this generated aggregate contract and preserve existing Markdown-only/support-only routing.

### Option C — canonical core / research-reporting source

Assessment: **not first repair**.

The current canonical sources already say:

- Research Authoring is not a renderer;
- it does not own Pandoc/XeLaTeX/fonts/pagination/PDF QA;
- report-family code must not implement low-level PDF/LaTeX mechanics;
- standalone Research Authoring must fail closed rather than invent private XeLaTeX rendering.

Adding the same command list there first would duplicate an owner rule that already exists.

Escalate to canonical source only if a repaired aggregate normal entry still cannot make the live ChatGPT consumer respect the boundary, or if new evidence shows ChatGPT routinely bypasses the aggregate and directly consumes lower-level source.

## 5. Exact proposed production repair surface

No change is made in this Planner turn.

If Critic approves the repair direction, the minimal implementation batch should be limited to:

1. `scripts/codex_marketplace_config.json`
   - strengthen only the Research Authoring `report` aggregate `workflow_notes` for standalone/renderer-missing surfaces;
   - preserve coordinator-first routing and all existing owner boundaries.

2. `tests/test_research_writing_routing.py`
   - add a focused normal-entry contract test proving the report aggregate:
     - fails closed when renderer companion is absent;
     - treats QA/preview compile/render/PDF-derived inspection as renderer mechanics;
     - forbids generic runtime from substituting for the missing renderer;
     - still allows Markdown-only authoring and source/handoff generation.

3. Regenerate current generated outputs through the canonical generator, including at least:
   - `plugins/codex/plugins/research-writing/skills/report/SKILL.md`
   - any registry/catalog/provenance artifacts the generator truthfully changes.

Do **not** hand-edit the generated `skills/report/SKILL.md`.

Do not change:
- `research-authoring-core` initially;
- `research-reporting` initially;
- paper/litcite routes;
- frozen G4 rubric/task/baseline.

## 6. Production identity consequence

This repair changes a production-consumed normal-entry route.

Therefore it cannot remain candidate C.

If implemented:

```text
C = 1c37c0715aca0096606f24e56192b7857e72bbd6  # failed final candidate
C2 = new commit after aggregate consumer repair
```

The live ChatGPT Plugin must subsequently be rebuilt from C2 and updated under a new guarded Plugin Creator release before any final ChatGPT evidence can represent the repaired production identity.

The current live release:

`pluginrel_6ac4471c7b90819189bc23af890135f3`

remains evidence for the failed C identity, not the repaired C2 identity.

Because a live Plugin update is an external account mutation, this Planner turn does not authorize or perform it.

## 7. Evidence invalidation under same-final-candidate policy

No Gate is rerun in this Planner turn. G1-G3 are not re-reviewed now.

Before a C2 repair is actually implemented, their historical PASS records remain truthful statements about C.

Once candidate-owned production behavior changes and C2 is formed, those records cannot be stitched into a C2 release PASS.

Risk-matched consequences:

### G1 — must rerun on C2

Reason: the change is exactly in normal report entry/routing behavior. G1 must directly prove the repaired aggregate is consumed in normal use and near-miss routes remain unchanged.

### G2 — must be re-established on C2 with fresh final evidence

Reason: G2 is report-family authoring and traverses the repaired aggregate entry. The previous DII two-phase task was already observed on C and therefore becomes development/regression evidence after product repair.

A new fresh report-family final task/delta is required under the existing G2 rubric unless Critic approves an equivalent fresh task before execution.

### G3 — must be re-established on C2 because all release Gates must bind one final candidate

The proposed repair does not touch the paper aggregate, so blast radius is low. The prior MoSAIC G3 becomes a high-value regression/should-not-change case, not a C2 final PASS.

The next execution Plan may use a risk-matched G3 rerun, but it still must directly bind C2. If the Gate continues to require fresh manuscript evidence, the already-observed MoSAIC final task cannot be relabeled fresh.

### G4 — full rerun on C2

Required:
- rebuilt/updated live wrapper from C2;
- normal natural Chat entry;
- fresh complete Chat-stage package;
- independent Chat-stage review;
- only after Chat PASS, Codex production/render stage;
- final independent G4 review.

The first G4 package remains immutable FAIL and cannot supply PASS subfindings.

## 8. Why this is not “test-specific prohibition”

The proposed aggregate change is not a G4 prompt patch.

It is generated into the normal installed Research Authoring report Skill and applies whenever:

```text
report-family formal PDF request
+ renderer companion unavailable on current surface
```

That condition is exactly the normal standalone ChatGPT wrapper situation.

The final G4 recovery must then use an ordinary natural request again. It must not depend on an evaluation-only command blacklist to obey the boundary.

A diagnostic prompt may be used during development to reproduce the old failure, but it cannot be the final normal-entry proof.

## 9. Current stop state

```text
G4_C1_ATTRIBUTION_V2_READY=YES
ATTRIBUTION=NORMAL_ENTRY_CONSUMER_PRODUCT_INTEGRATION_FAILURE
PREFERRED_REPAIR_LAYER=GENERATED_REPORT_AGGREGATE_ENTRY
CURRENT_CANDIDATE_MODIFIED=NO
LIVE_PLUGIN_UPDATED=NO
G4_RERUN_STARTED=NO
CODEX_PDF_STAGE_STARTED=NO
G1_G3_REVIEWED_AGAIN=NO
NEXT_HANDOFF=CRITIC
```
