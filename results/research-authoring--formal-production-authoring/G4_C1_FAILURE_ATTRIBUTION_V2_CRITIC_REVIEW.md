# 059 Research Authoring — G4-C1 Failure Attribution v2 Critic Review

Date: 2026-10-06  
Role: independent Critic  
Review object: G4-C1 attribution v2 and repair-layer selection  
Planner object: `results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_V2_PLANNER.md`  
Planner commit: `6a131f0cf75a342c924366ac411956e85f63341d`  
Attribution package HEAD: `4ef2b6cc58f1068c1478bd7c1bb19fc74f200cfa`

## Result

```text
RESULT=PASS

G4_C1_ATTRIBUTION=NORMAL_ENTRY_CONSUMER_PRODUCT_INTEGRATION_FAILURE
MISSING_RENDER_OWNER_RULE=NO
PREFERRED_REPAIR_LAYER=GENERATED_REPORT_AGGREGATE_ENTRY
REPAIR_REQUIRES_NEW_CANDIDATE=YES

CURRENT_CANDIDATE=1c37c0715aca0096606f24e56192b7857e72bbd6
NEW_CANDIDATE=C2_AFTER_IMPLEMENTATION

PRODUCTION_MODIFICATION_AUTHORIZED=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
NEW_G4_RUN_AUTHORIZED=NO
CODEX_PDF_STAGE_AUTHORIZED=NO
```

This PASS approves the v2 failure attribution and repair-layer choice only. It does not authorize implementation or any new final Gate execution.

## 1. Prior blockers are closed

The prior Critic REVISE had two blockers:

- G4-C1-R1: the first attribution overclaimed a test-only harness failure without identifying a distinct test-only harness.
- G4-C1-R2: the proposed recovery command blacklist was output-informed evaluation tuning and could not prove normal-entry behavior.

Planner v2 closes both.

It now classifies the first G4 run as a real normal-entry failure and explicitly rejects the test-only-harness explanation.

It also moves the proposed repair from a G4-only recovery prompt into the production-consumed report aggregate entry. The final G4 rerun is required to use the ordinary natural request again, not a test-specific command blacklist.

## 2. Independent product/source verification

The live PRIVATE USER-scope plugin was read directly:

- name: `research-authoring`
- version: `0.3.0`
- plugin id: `plugins_6ac4471b735881918c17cd310f262429`
- release id: `pluginrel_6ac4471c7b90819189bc23af890135f3`

Direct byte comparison with final candidate `1c37c0715aca0096606f24e56192b7857e72bbd6` confirms:

```text
live skills/report/SKILL.md == C generated report/SKILL.md
live skills/report/_src/core/source.md == C generated core/source.md
live skills/report/_src/report/source.md == C generated report/source.md
```

The canonical core already states that Research Authoring is not a renderer and does not own Pandoc/XeLaTeX, fonts, pagination, PDF QA, or renderer implementation.

The report delegate already states that it must not implement low-level PDF/LaTeX mechanics; formal PDF mechanics go to `render-chinese-math-pdf`; standalone Research Authoring must fail closed rather than invent a private XeLaTeX route.

Therefore the missing capability is not an owner rule in the canonical Research Authoring source.

## 3. Why v2 attribution is correct

The first failed G4 run used the real live Plugin in an ordinary ChatGPT conversation with the frozen natural request. The generic ChatGPT runtime was part of that normal surface, not a separate test harness.

The failure is therefore correctly classified as:

`NORMAL_ENTRY_CONSUMER_PRODUCT_INTEGRATION_FAILURE`

The first package remains immutable FAIL because it explicitly performed XeLaTeX compile, PDF creation, page raster/visual inspection, and PDF text extraction in the ChatGPT stage.

Because no per-turn ChatGPT Skill-consumption receipt exists, it is correct not to pretend we know whether:

- the report aggregate loaded and its existing fail-closed wording was interpreted too weakly; or
- the matching aggregate was not actually loaded.

Both remain compatible with a normal-entry consumer failure.

## 4. External mechanism check

Current OpenAI Plugin/Skill documentation describes Skills as the workflow/instruction layer. The model first sees Skill metadata and loads the full instructions when the request matches or the user invokes the Skill. MCP/app tools are the controlled-action layer.

The live `research-authoring` wrapper is skills-only and contains no MCP/connector renderer capability. There is no separate wrapper-owned hard sandbox evidenced here that disables generic ChatGPT runtime capabilities. The normal behavioral control available to this product is therefore the production-consumed Skill/aggregate instruction path plus any separately available controlled tools.

This supports v2's choice to repair the real report aggregate entry rather than invent a test-only harness.

## 5. Repair-layer ruling

### Option A — wrapper metadata/default prompt

Not sufficient as the final repair.

Plugin manifest descriptions/default prompts help discovery and suggested invocation but do not replace the full report workflow consumed after Skill activation. A wrapper-only behavior Skill would also create a Chat-specific second behavioral source.

It may be useful for diagnosis but must not be the sole final repair.

### Option B — generated report aggregate entry

PASS as the preferred minimum repair.

The relevant source is:

`scripts/codex_marketplace_config.json -> research-writing -> report -> workflow_notes`

and the generated normal consumer is:

`plugins/codex/plugins/research-writing/skills/report/SKILL.md`

This aggregate already owns report-family routing, coordinator-first entry, formal-PDF handoff, and fail-closed behavior when the renderer companion is absent.

The missing operational distinction is narrow and directly tied to the observed failure: in a standalone skills-only surface without the approved renderer companion, “artifact mechanics” must explicitly include preview/QA compilation and PDF-derived inspection. Generic runtime/file/compute capabilities cannot substitute for the missing renderer.

This is a production rule for every matching standalone report-family formal-PDF request, not a G4-specific blacklist.

### Option C — canonical core/report source

Not the first repair.

Those sources already contain the owner boundary. Adding the same command list there now would duplicate an existing rule without evidence that the canonical source itself lacks the concept.

Escalate there only if the repaired aggregate normal entry still fails, or new evidence shows the aggregate is systematically bypassed.

## 6. Minimum implementation surface approved for planning

A future implementation package may plan only this production scope:

1. `scripts/codex_marketplace_config.json`
   - change only Research Authoring `report` aggregate `workflow_notes`;
   - operationalize standalone/no-renderer behavior;
   - preserve coordinator-first routing and current owners.

2. `tests/test_research_writing_routing.py`
   - focused tests that prove:
     - missing renderer companion => stop after source + production handoff;
     - QA/preview compile/render/PDF-derived inspection counts as renderer mechanics;
     - generic runtime is not a substitute renderer;
     - Markdown-only source authoring remains allowed;
     - source + downstream handoff remains allowed.

3. Canonical generator output only:
   - regenerate `plugins/codex/plugins/research-writing/skills/report/SKILL.md`;
   - accept only registry/catalog/provenance parity files the generator truthfully changes.

Do not directly edit generated files.

Do not initially change:

- `skills/writing/research/research-authoring-core/SKILL.md`;
- `skills/writing/research/research-reporting/SKILL.md`;
- paper/litcite routes;
- frozen G4 task/rubric/baseline;
- Plugin Creator live release;
- main/release.

No additional production-consumed entry/config is currently required for the minimum repair. If implementation shows that the aggregate generation path cannot express the rule or that normal ChatGPT selection bypasses the aggregate, return to Planner/Critic instead of silently widening scope.

## 7. Candidate identity

The proposed Option B changes a production-consumed normal-entry behavior contract.

Therefore:

```text
REPAIR_REQUIRES_NEW_CANDIDATE=YES
CURRENT_CANDIDATE=1c37c0715aca0096606f24e56192b7857e72bbd6
NEW_CANDIDATE=C2_AFTER_IMPLEMENTATION
```

The current live Plugin release remains bound to failed candidate C and cannot represent C2.

Any later live wrapper update must be rebuilt from exact C2 and requires its own bounded user authorization. This review does not grant it.

## 8. Same-final-candidate evidence ruling

Once C2 exists, old final Gate PASS records on C cannot be stitched into C2 release PASS.

- **G1:** final evidence must rerun directly on C2. This is the highest-risk route because the repair changes normal-entry report routing.
- **G2:** old DII evidence becomes development/regression evidence. C2 needs a new final report-family task/delta satisfying the existing freshness contract.
- **G3:** old MoSAIC evidence becomes regression/should-not-change evidence. C2 final G3 must directly bind C2. If the frozen Gate still requires fresh manuscript evidence, the already-observed MoSAIC task cannot be relabeled fresh.
- **G4:** full rerun on C2, including a rebuilt live wrapper, ordinary natural ChatGPT entry, a completely new Chat-stage package, independent Chat-stage review, and only after Chat PASS the Codex production/render stage.

The first failed G4 package remains immutable FAIL and contributes no PASS subfinding.

Before new final evidence is consumed, C2 must go through the existing pre-final Critic admission again.

## 9. What this PASS does not authorize

```text
PRODUCTION_MODIFICATION_AUTHORIZED=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
NEW_G4_RUN_AUTHORIZED=NO
CODEX_PDF_STAGE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_AUTHORIZED=NO
FORMAL_RELEASE_AUTHORIZED=NO
```

The next owner is Planner, who may now prepare the bounded implementation/execution package for the approved repair direction. It must return for execution-ready Critic review before any production change.
