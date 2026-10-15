---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: clear-writing--cross-surface-language-layer
decision: PLAN_FROZEN
---

# Clear Writing 跨 ChatGPT / Codex 通用表达层 — re-plan revision 1

- Repository: `YuukiAS/AI_Skills_Collection`
- Task: `clear-writing--cross-surface-language-layer`
- Execution branch: `reviewed/clear-writing--cross-surface-language-layer`
- Original implementation commit: `cac70c3bfcce6aeeba9c3e80adfa317235b54ee9`
- Approved recovery package: `ac44e1cf07df08e9042bfc53e2b2ab79ec4871ad`
- Recovery Critic review: `results/clear-writing--cross-surface-language-layer/CRITIC_CROSS_SURFACE_RECOVERY_REVIEW_V0_1_2026-10-15.md@befafcdd287c195e37daca18c6db88809fe6e353`
- Plan revision: `1 / 1`
- Review round remains: `1 / 2`
- Maintenance companion: `ai-skills-core`
- Domain owner: `writing-style`

This revision preserves the previously approved Clear Writing v0.3 architecture and materializes only the independently approved 2026-10-15 recovery amendment. It does not authorize PIE 0.2, ChatGPT account mutation, paid review, G7 fresh evaluation, release, main merge, or Presentations / Research Authoring source-semantic changes.

## Objective and value

Keep the existing six-skill Clear Writing architecture, including the implemented `response-clarity` route, and move the task past the two blockers that currently prevent real ChatGPT Web acceptance:

1. turn the five user-observed ChatGPT Web examples into permanent development regressions and test the current candidate before changing it;
2. close the already-identified repository CI baseline failures without weakening the original full-CI requirement or changing adjacent domain semantics.

The recovery is successful only if the resulting reviewed-branch candidate no longer reproduces the frozen known response-clarity failures, preserves the positive example and should-not-change controls, and passes the same required full repository / Marketplace CI. That is still only a recovery/product-development milestone; real ChatGPT Web automatic selection, A/E and B/C matched comparisons, G7 fresh evidence and final release remain later gates.

## Frozen decisions

- Keep `writing-style` / Clear Writing and the existing six-skill architecture. Do not add another skill, router, plugin, state machine, model service or reviewer.
- `response-clarity` remains the owner for ordinary user-facing explanations, conclusions, diagnostics, advice, progress and task-result summaries after domain reasoning.
- Existing specialist ownership remains unchanged:
  - `chinese-prose`: formal Chinese documents / README / reports / final document wording;
  - `scientific-rewrite`: source-faithful structural rewrite of existing Chinese-dominant scientific/technical material;
  - `scientific-prose`: English scientific prose;
  - `product-ui-copy`: wording after product/UI meaning is frozen;
  - `writing-fidelity`: shared fidelity principles.
- The five 2026-10-14/15 Web examples are development / known regression only, primarily G2 response-readability evidence. They are permanently ineligible for G7 fresh/unseen claims.
- `RW-WEB-03` is a positive control: Clear Writing must not collapse into “always be short”; necessary examples, causal explanation and uncertainty must remain when they help the reader.
- Repair semantics, not surface tokens. No banned-word list, English-percentage score, heading/line count, arrow/code-fence ban, fixed answer length or project-specific hard-coding may serve as the product mechanism or PASS oracle.
- The original G0–G7 architecture and later Web A/E, B/C and G7 requirements remain intact.
- Full CI remains mandatory. Narrow tests can support development but cannot substitute for required full repository tests, Marketplace generation/check and reviewed-branch GitHub CI.
- Presentations / Research Authoring recovery permission is generated-only and mechanical. Their canonical `skills/**` source, routing, plugin versions, descriptions/default prompts, profiles, changelogs, README, professional rules and personal Web plugins are not editable in this recovery.

## Positive completion

For this re-plan execution, positive completion requires all of the following on the same reviewed branch:

1. A baseline packet exists for RW-WEB-01..05 generated from the pre-repair `cac70c3...` candidate before production source edits or merging current main.
2. After latest-main synchronization, all five known cases are replayed again; any production repair is limited to generic response-clarity behavior actually demonstrated by those failures.
3. RW-WEB-01, 02, 04 and 05 meet their frozen reader-facing criteria, while RW-WEB-03 retains concrete explanation, useful examples and uncertainty.
4. Explicit should-not-change controls remain correct for:
   - requested complete report / executable prompt / contract;
   - genuinely branched or stepwise processes where structure helps;
   - pure JSON/YAML/code/raw-log exact output;
   - official names and exact machine strings.
5. The previously identified CI baseline categories are closed without test deletion, skip/allowlisting, fake version bump, hidden diff or narrowed CI.
6. Full repository tests, Marketplace generation/check and required GitHub CI pass on the current reviewed-branch candidate.

Maximum claim scope: this proves a clean recovery candidate and known-regression closure. It does not prove ChatGPT Web automatic activation, G7 generalization, PIE 0.2 integration or formal release.

## Non-substitutable semantics

- Preserve facts, numbers, dates, formulas, citations, subjects, negation, uncertainty, completion state, permission/authorization and exact machine identifiers in all response-clarity repairs.
- Preserve the distinction between source-established conclusions and the assistant’s additional recommendation.
- Preserve the user’s actual feedback intent. A writing-quality critique must not be converted into unrelated domain analysis or long self-critique.
- Preserve necessary depth: “clear” means lower reader effort and higher information value, not mechanically shorter output.
- Formatting must be proportional to information structure. Simple linear relations should not be inflated into large visual structures, while genuinely branched workflows, executable steps and machine payloads may remain structured.
- A section after the core answer must add new evidence, decision, requested implementation detail or real comparison value; otherwise the answer should stop.
- The five known cases may be used for development after baseline freeze; once exposed, they can never be relabeled as G7 fresh evidence.
- The baseline replay must precede any Clear Writing production-source repair and precede the merge of current main, so existing candidate capability is not retroactively inferred.
- Latest main may be merged only by normal non-force merge into the existing reviewed branch. No rebase, force push, successor task/branch or history replacement.
- Presentations / Research Authoring generated-only parity is legal only when the existing `scripts/build_codex_marketplace.py` and current canonical source/config uniquely determine the generated bytes. If source and generated forms encode different professional behavior or require a human semantic choice, stop and return to Planner.
- Do not use any personal Research Authoring / Presentations Web plugin as authority for repository canonical source.

## Implementation scope

### Phase A — freeze current-candidate baseline

Before any production edit or merge of current main:

1. confirm the existing task branch and implementation content anchored at `cac70c3bfcce6aeeba9c3e80adfa317235b54ee9`;
2. derive public-safe development fixtures from `results/clear-writing--cross-surface-language-layer/REAL_WEB_REGRESSION_BANK_V1.md`; do not commit private full ChatGPT transcripts;
3. replay all five cases through the existing normal candidate-plugin replay route;
4. preserve all five complete outputs and case-by-case development verdicts;
5. commit the baseline packet before continuing.

A case that already passes must not be changed merely to manufacture a production diff.

### Phase B — synchronize latest main

After Phase A is frozen:

1. fetch current `origin/main`;
2. normal non-force merge it into the same reviewed branch;
3. preserve latest main TODO/feedback and unrelated valid work;
4. mechanically resolve only task-owned Clear Writing conflicts; any conflict requiring a professional semantic choice in another plugin returns to Planner.

### Phase C — bounded response-clarity repair

Replay RW-WEB-01..05 on the synchronized candidate.

If all pass, do not change Clear Writing production semantics.

If failures remain, repairs are limited to the existing response-clarity surface and directly required routing/eval tests. Generic allowed targets are:

- stopping when the user’s question is already answered and later material adds no new decision/evidence;
- matching formatting complexity to information complexity;
- separating source consensus/evidence from assistant synthesis/recommendation;
- responding to writing-feedback intent instead of launching unrelated domain analysis;
- preserving the positive-control need for examples, causal explanation and uncertainty.

No new top-level capability, external model, API, workflow role or sample-specific rule is authorized.

### Phase D — close the known CI baseline categories

1. **Repository version assertion**
   - do not bump `VERSION` merely to satisfy a stale test;
   - repair the test so it validates the current canonical version/release contract rather than hard-coding an unshipped future version.

2. **Central-plugin TODO/changelog assumptions**
   - preserve valid workflow-specific TODO files;
   - scope central-plugin inbox/changelog checks to the canonical central-plugin set rather than treating every Markdown file in the directory as a plugin.

3. **Presentations / Research Authoring generated parity**
   - compare current canonical source/config with generated payload;
   - only generated bytes (and the same generator’s Marketplace snapshot if mechanically required) may change;
   - no edits to Presentations / Research Authoring `skills/**` source;
   - no changes to their source mapping, routing, versions, descriptions/default prompts, profiles, changelogs, README, professional rules or personal Web plugins;
   - rerun the generator after synchronization and require clean parity;
   - any semantic discrepancy or source/config ambiguity immediately returns to Planner.

4. Never delete/skip/allowlist failures, hide diffs, weaken assertions merely to green CI, or substitute another branch’s PASS.

### Phase E — regression and CI

Run:

- response-clarity focused tests;
- RW-WEB-01..05 known regressions;
- the four should-not-change control families above;
- writing-style source/generated parity;
- affected generator/mirror checks;
- full repository unit tests;
- full Marketplace generation/check;
- required GitHub CI on this reviewed branch.

Full-CI PASS is process evidence, not final Web product evidence.

After full CI passes, prepare complete evidence for the existing independent review path and stop. Do not consume the second Reviewer round before full CI PASS.

## Acceptance and regression gates

The original G0–G7 remain the only capability Gate taxonomy. This recovery does not add G8/G9 or reinterpret existing gates.

- **G0 distribution**: unchanged; not completed by this recovery.
- **G1 automatic entry/increment**: unchanged; real Web A/E and B/C remain later.
- **G2 first-answer readability**: RW-WEB-01..05 become known development regressions. PASS requires reader-visible decision, proportional structure, low unnecessary English/process noise, feedback-intent alignment and source-vs-recommendation separation without loss of necessary reasoning.
- **G3 fidelity/bypass**: all exact machine strings and protected meaning remain intact; pure machine output remains bypassed.
- **G4 existing writing skills**: original document/prose/rewrite/fidelity routes must not regress.
- **G5 domain consumers**: this recovery may mechanically restore generated parity only; it does not modify Frontend Design, Presentations or Research Authoring professional semantics.
- **G6 multi-turn/language modes**: unchanged; no new claim from known cases.
- **G7 final candidate/fresh generalization**: not executed here; RW-WEB-01..05 are permanently excluded.

Any failure must still be attributed among product defect, source/evaluation issue, routing/packaging, environment, CI/harness or permission boundary. Do not convert all failures into response-clarity defects.

## Natural-language usage / routing expectations

Examples that should route to `response-clarity` after domain reasoning:

- “这个失败到底意味着什么？我现在需要做什么？”
- “三份研究到底共同说明了什么，差异在哪里？”
- “这段回答为什么读起来这么累？”
- “把测试结果告诉我，别把日志直接堆给我。”

Examples that must stay elsewhere:

- “把这份中文科研报告完整重写，公式和引用不能丢。” → `scientific-rewrite` / document route.
- “Polish this English paper paragraph.” → `scientific-prose`.
- “改这个设置页按钮和错误提示。” → product/UI meaning owner then `product-ui-copy`.
- “Return exactly this JSON / raw log / code.” → machine output bypass.
- “给我完整可执行的 Codex prompt / contract.” → preserve the required complete machine/handoff payload rather than forcing conversational compression.

## Out of scope

This re-plan does not authorize:

- PIE 0.2 or any Project-setting mutation;
- personal ChatGPT plugin creation/update or account changes;
- paid API/model review;
- private transcript publication or transfer;
- G7 fresh/holdout execution;
- repository/plugin release, version bump, merge to `main`, movement of `release`, PR creation or branch cleanup;
- Presentations / Research Authoring source-semantic, routing, version, profile, changelog, README or professional-rule changes;
- new Clear Writing skill/plugin/router/state machine/reviewer;
- Bridge Kit changes;
- external hosted service, MCP finalizer or API key;
- phrase blacklist, English ratio, heading/line/paragraph quotas, arrow/code-fence bans, AI-detector evasion or project-specific hard-coding.

If recovery cannot stay within these boundaries, stop in the existing task and return to Planner rather than creating a successor.
