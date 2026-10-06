# 059 Research Authoring — G4-C1 Failure Attribution v2 Critic Prompt

你继续作为 AI Research Stack 的长期独立 Critic。

本轮只复核 G4-C1 failure attribution v2 与 repair-layer 选择。

不要修改 production。
不要更新 live Plugin。
不要重新跑 G4。
不要启动 Codex PDF。
不要重新审核 G1-G3 的旧产物。
不要修改 frozen G4 rubric/task/baseline。
不要调用 paid API。
不要 merge/release。

## Active context

Repository:
`YuukiAS/AI_Skills_Collection`

Branch:
`work/research-authoring--formal-production-authoring`

Current failed final candidate:
`1c37c0715aca0096606f24e56192b7857e72bbd6`

Prior Critic review:
`results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_CRITIC_REVIEW.md`

Prior Critic commit:
`85305c4b8ff4ee1c68ee5efb1407fdd06610ef39`

Review object:
`results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_V2_PLANNER.md`

## Stable facts — do not reopen

The live Plugin Creator release is:

```text
name = research-authoring
version = 0.3.0
plugin_id = plugins_6ac4471b735881918c17cd310f262429
release_id = pluginrel_6ac4471c7b90819189bc23af890135f3
scope = USER
discoverability = PRIVATE
```

Prior Critic independently established:

- live `skills/report/SKILL.md` equals C generated source;
- live `skills/report/_src/core/source.md` equals C generated source;
- live `skills/report/_src/report/source.md` equals C generated source;
- canonical source already says Research Authoring is not a renderer;
- canonical source excludes XeLaTeX/Pandoc/fonts/pagination/PDF QA;
- formal PDF mechanics belong downstream;
- standalone Research Authoring must not invent a private XeLaTeX route.

Therefore:

`MISSING_RESEARCH_AUTHORING_RENDER_OWNER_RULE=NO`

The first G4 ChatGPT stage is permanently FAIL.

Do not reinterpret QA/preview compile as non-rendering.

## Required reads

Read:

- `results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_V2_PLANNER.md`
- `results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_CRITIC_REVIEW.md`
- `results/research-authoring--formal-production-authoring/G4_CHATGPT_STAGE_REVIEW.md`

Frozen G4:

- `private/exports/research-authoring--formal-production-authoring/final_tasks/G4/REUSED_TASK_DECISION.md`
- `private/exports/research-authoring--formal-production-authoring/final_tasks/G4/CHAT_CODEX_HANDOFF_RUBRIC.md`
- `private/exports/research-authoring--formal-production-authoring/final_tasks/G4/G4_CHATGPT_INPUT_BASELINE.md`

Production source/config at C:

- `scripts/codex_marketplace_config.json`
- `tests/test_research_writing_routing.py`
- `plugins/codex/plugins/research-writing/skills/report/SKILL.md`
- `skills/writing/research/research-authoring-core/SKILL.md`
- `skills/writing/research/research-reporting/SKILL.md`

Read the actual live Plugin source again only if needed to verify a disputed locator.

Also independently confirm current OpenAI Plugin/Skill semantics if needed:
Skills are instruction/workflow layers loaded by the model based on metadata/matching; a skills-only Plugin is not itself a capability sandbox for generic ChatGPT runtime tools.

## Planner v2 attribution

Planner no longer calls the failure test-only harness bypass.

Current attribution:

```text
G4-C1 = REAL_NORMAL_ENTRY_FAILURE
PRIMARY_ATTRIBUTION = NORMAL_ENTRY_CONSUMER_PRODUCT_INTEGRATION_FAILURE
MISSING_RESEARCH_AUTHORING_RENDER_OWNER_RULE = NO
```

Planner identifies the intended normal production consumer for this request as:

```text
live research-authoring plugin
-> skills/report/SKILL.md
   routing_mode=coordinator-first
   coordinator_artifact_id=core
-> _src/core/source.md
-> _src/report/source.md
```

The source/config locator is:

`scripts/codex_marketplace_config.json -> research-writing -> report aggregate`

The report aggregate existed in the first live wrapper and should have matched the frozen advisor-PDF request.

However the first package has no per-turn runtime receipt proving whether ChatGPT actually loaded the aggregate instructions.

Therefore two possibilities remain:

A.
aggregate loaded but “fail closed / artifact mechanics” was interpreted narrowly enough to permit “authoring-stage QA render”;

B.
aggregate was not actually loaded despite the natural request matching it.

Either case is a normal-entry consumer/integration failure.

## Repair alternatives to judge

### A. Wrapper entry only

Planner rejects as primary repair because:

- plugin `defaultPrompt` is a suggested invocation, not guaranteed workflow instructions for arbitrary user prompts;
- manifest description/longDescription are discovery/interface metadata;
- a wrapper-only behavioral Skill would create Chat-specific behavior source drift from the approved one-canonical-source architecture.

It may be diagnostic, not final repair.

### B. Generated report aggregate entry

Planner prefers this.

Exact source:

`scripts/codex_marketplace_config.json`

Research Authoring:
`research-writing -> skills[artifact_id=report] -> workflow_notes`

Generated consumer:

`plugins/codex/plugins/research-writing/skills/report/SKILL.md`

Current aggregate already owns:

- coordinator-first report route;
- formal PDF handoff;
- renderer-companion presence/absence behavior.

Proposed normal production rule:

When the approved renderer companion is unavailable,
formal PDF production stops at stable source + complete production handoff.

“Artifact mechanics” explicitly includes:

- compile-derived QA;
- preview/QA PDF compile;
- PDF creation/opening/rendering;
- page raster/visual inspection;
- PDF text/font/page extraction.

Generic ChatGPT runtime/file/compute capability must not substitute for the missing renderer companion.

These checks remain pending for the downstream production owner.

This is a normal aggregate rule, not a G4-only command blacklist.

### C. Canonical core/report source

Planner rejects as first repair because those sources already contain the owner rule.

Only escalate there if aggregate repair still fails or new evidence shows normal ChatGPT systematically bypasses the aggregate.

## Candidate identity

Planner says any Option-B implementation changes candidate-owned production behavior:

- `scripts/codex_marketplace_config.json`;
- focused routing test(s);
- generated `plugins/.../report/SKILL.md`;
- any truthfully changed generated parity outputs.

Therefore repaired product must become C2.

No implementation is authorized in this review.

The current live Plugin cannot represent C2. A future Plugin Creator update from C2 would require its own bounded authorization and new release identity.

## Evidence invalidation proposed by Planner

Do not rerun anything now. Only review the policy consequence.

If C2 is implemented:

### G1
Must rerun on C2 because normal entry/routing behavior changed.

### G2
Must be re-established on C2.
The previous DII final task/output has been seen and becomes development/regression evidence rather than fresh final evidence.

### G3
The paper aggregate is outside the narrow behavior change, but current Capability Gate policy still requires all release Gates to bind one final candidate.
Therefore old G3 PASS cannot be stitched into C2 release PASS.
MoSAIC remains high-value regression/should-not-change evidence; any C2 final G3 must directly bind C2 under the frozen Gate policy.

### G4
Must be fully rerun from a rebuilt/updated live C2 wrapper.
The first package remains immutable FAIL.

Judge whether this interpretation of same-final-candidate policy is correct or unnecessarily broad.

## Questions to decide

Only decide:

1. Is it correct that no hard ChatGPT capability-enforcement layer exists in this skills-only wrapper beyond normal Skill consumption?
2. Is `skills/report/SKILL.md` / the generated report aggregate the actual normal production-consumed entry closest to this failure?
3. Given no runtime receipt from the failed Chat turn, is it correct not to claim whether the aggregate was loaded vs skipped?
4. Does this make the failure a normal-entry consumer/product-integration failure rather than test-only harness failure?
5. Is Option B the minimum correct repair layer?
6. Would Option A be too weak/drift-prone for final production evidence?
7. Would Option C duplicate an already-existing canonical rule?
8. Does Option-B implementation require C2?
9. Is the proposed G1-G4 invalidation/re-establishment scope consistent with same-final-candidate policy?
10. Are any additional production-owned files necessarily in the repair scope that Planner missed?

## Output

Only:

`RESULT = PASS`

or

`RESULT = REVISE`

If PASS, explicitly record:

```text
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

Then state the exact minimum repair files/areas and the exact Gate evidence invalidation/re-establishment requirements.

Finally generate the next Planner prompt required by `CRITIC_ROLE_CONTRACT`.
Do not generate a Codex implementation prompt yet unless this review itself is explicitly execution-ready and user authorization has been separately obtained.

If REVISE, use stable blocker IDs and include:
- requirement;
- direct evidence;
- causal risk;
- minimum closure;
- owner.

Do not reopen Research Authoring architecture or add a fifth Gate.
