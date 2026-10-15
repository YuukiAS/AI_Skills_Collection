# Clear Writing 2026-10-15 恢复与真实网页回归执行计划 v0.1

Date: 2026-10-15  
Status: PLANNER_PACKAGE_FOR_CRITIC  
Task: `clear-writing--cross-surface-language-layer`  
Execution branch: `reviewed/clear-writing--cross-surface-language-layer`  
Current implementation anchor: `cac70c3bfcce6aeeba9c3e80adfa317235b54ee9`  
Current task state before this package: `NEEDS_GPT_PLANNER / ci_status=FAIL / review_round=1 / plan_revision=0`

## 1. Decision

Keep the existing Clear Writing cross-surface architecture and the already-implemented `response-clarity` skill. Do not redesign the plugin, add another skill, add a new Gate, or start PIE 0.2.

This recovery does two things before any ChatGPT Web fresh acceptance:

1. turn the five user-observed Web examples into a frozen known-regression bank and replay the current candidate against them before editing;
2. close the repository-level CI baseline blockers that prevented the task from reaching Web acceptance, using the smallest cross-owner maintenance permission that does not change Research Authoring or Presentations source semantics.

The existing G0–G7 taxonomy remains unchanged. These Web examples belong to development / known regression, primarily G2 response readability; they are not G7 fresh evidence.

## 2. Why a Critic is required

The real-case regression work itself is already inside the frozen Clear Writing Plan and would not need a new architecture review.

However, the 2026-10-13 recovery Critic explicitly did NOT authorize this Clear Writing task to modify Presentations or Research Authoring packaged payloads. The full CI failure still includes stale generated/mirror differences in those areas, while the current main still contains the hard-coded repository-version assertion and the central-plugin TODO-set assumption.

To make progress without waiting indefinitely for unrelated future releases, this package requests one narrow expansion:

- repository-maintenance tests may be corrected where they encode stale repository assumptions;
- generated payloads for Presentations / Research Authoring may be synchronized ONLY when the current canonical source already determines the result mechanically and source behavior is unchanged;
- any semantic source choice, domain-content choice or source edit remains forbidden and returns to Planner.

That is a real cross-owner recovery-boundary change, so this package must receive independent Critic PASS before Codex executes it.

## 3. Frozen real-case regression bank

Canonical development rubric:

`results/clear-writing--cross-surface-language-layer/REAL_WEB_REGRESSION_BANK_V1.md`

Source evidence is the user-confirmed feedback recorded on current main at:

`docs/plugin-todos/writing-style.md@1c59199f88c7527f2bd853e606f20146134fda47`

The bank contains exactly five currently frozen cases:

- RW-WEB-01: long answer buries the decision — negative;
- RW-WEB-02: pseudo-clarification / self-critique — negative;
- RW-WEB-03: concrete explanation with examples — positive control;
- RW-WEB-04: pseudo-structure / arrow-code-block overload — negative;
- RW-WEB-05: synthesis expands into a mini architecture memo — negative.

No additional exposed case may be appended during this execution merely to chase a PASS. New user feedback after execution begins is recorded for the next development cycle.

## 4. Execution order

### Phase A — preserve the current candidate baseline

Before changing production source or merging current main:

1. fetch the exact reviewed branch and confirm the implementation content corresponding to `cac70c3b...`;
2. create public-safe derived fixtures for RW-WEB-01..05 from the frozen regression descriptions; do not commit private full transcripts;
3. replay the existing `writing-style` candidate through the normal candidate replay route for those fixtures;
4. save all five baseline outputs and a case-by-case development assessment;
5. do not edit `response-clarity` until this baseline packet is committed.

The purpose is to learn what the existing candidate already handles. A case that already passes must not be changed merely to manufacture a code diff.

### Phase B — synchronize current main safely

After the baseline packet is frozen:

1. fetch current `origin/main`;
2. merge current main into the same reviewed branch using a normal non-force merge; do not rebase, create a successor branch, or discard the task implementation;
3. preserve the latest main feedback/TODO records and unrelated current-main work;
4. resolve conflicts by keeping the task-owned `response-clarity` candidate plus latest main truth; any semantic conflict in another plugin stops for Planner.

### Phase C — minimal known-regression repair

Run RW-WEB-01..05 against the synchronized candidate.

If all five pass, do not modify Clear Writing production semantics.

If one or more fail, allow a bounded repair only in the existing response-clarity surface and directly required routing/eval tests. The repair may add generic behavior for:

- stopping when the user’s question is already answered and later sections add no new decision/evidence;
- matching formatting complexity to information complexity;
- separating source consensus from assistant synthesis/recommendation;
- responding to writing-feedback intent instead of launching unrelated domain analysis;
- preserving the positive-control need for examples, causal explanation and uncertainty.

Do NOT implement:
- banned-word lists;
- English-percentage scoring;
- arrow/code-fence bans;
- fixed heading/paragraph/line limits;
- sample-specific project names or phrases;
- a new skill, router, state machine, reviewer, external model or API.

### Phase D — close the known full-CI baseline defects

The prior full CI had 341 tests with five failures. Recovery is limited to the already identified failure families.

1. Repository version test:
   - do not bump `VERSION` to satisfy a stale assertion;
   - make the test validate the current canonical version/release contract rather than hard-code an unshipped future version.

2. Central-plugin TODO/changelog tests:
   - keep all valid workflow-specific TODO files;
   - scope “exactly one central plugin inbox/changelog” checks to the canonical central-plugin set rather than treating every Markdown file in the directory as a central plugin.

3. Presentations / Research Authoring generated parity:
   - first compare current canonical source, generator config and generated payload;
   - if the generated change is a deterministic regeneration of unchanged canonical source with no semantic choice, generated-only synchronization is allowed under this proposed recovery;
   - do not edit Presentations or Research Authoring source semantics, routing, professional rules, versions or user-facing capability;
   - if regeneration would choose between substantively different source/generated behavior, STOP and return `NEEDS_GPT_PLANNER`.

4. Do not hide failures, delete tests, mark known failures as allowed, exclude test files, or weaken the full-CI gate.

### Phase E — regression and full CI

Required before the task can leave repair:

- current response-clarity focused tests;
- RW-WEB-01..05 known-regression outputs, with RW-WEB-03 positive control preserved;
- explicit should-not-change cases for:
  - requested full report / full executable prompt;
  - genuinely branched process where arrows/structure help;
  - pure JSON/YAML/code/raw-log exact-output requests;
  - necessary official names and machine strings;
- source/generated parity for affected writing-style files;
- full repository unit tests;
- full Marketplace generation/check;
- the same required GitHub CI on the reviewed branch.

A full-CI PASS is still process evidence, not product quality proof.

## 5. Product acceptance after this recovery

This recovery does not claim ChatGPT Web success.

After known regressions and full CI pass, the existing frozen Clear Writing Plan still requires real ChatGPT Web evidence:

- matched project A/E and B/C comparisons;
- no explicit `@Clear Writing` as proof of automatic activation;
- real first-answer readability and fidelity;
- later G7 fresh/unseen tasks that were not used in this development cycle.

The five RW-WEB cases are permanently ineligible for G7.

PIE 0.2 remains out of scope until Clear Writing Web demonstrates that a thin Project bridge adds stable value over the Project baseline.

## 6. External reality check

Current OpenAI documentation says a Skill is considered from its metadata and the model loads full instructions when the request matches; installed skills can be used automatically when helpful. Project instructions apply within the Project and override global custom instructions. This supports the current test design: Project text alone must not be assumed to force plugin use, and explicit `@` invocation is diagnostic rather than proof of normal automatic selection.

References:
- https://developers.openai.com/plugins/concepts/skills
- https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- https://help.openai.com/en/articles/20001066-skills-in-chatgpt

## 7. Version / release

This is still development/recovery.

- Repository bump: NONE during repair.
- `writing-style`: keep current development version until the original final release gates pass; no early bump.
- Other central plugins: NO_BUMP.
- Presentations / Research Authoring: source behavior and versions unchanged.

## 8. Stop conditions

Stop and return to Planner without consuming the final Reviewer round if:

- any required repair needs a Presentations or Research Authoring source-semantic change;
- the regression bank reveals a conflict that cannot be solved inside the existing response-clarity boundary;
- a new CI failure is not attributable to the frozen known baseline or the current task diff;
- fixing CI would require weakening tests or changing the original full-CI acceptance rule;
- a new account, paid API, credential, personal ChatGPT plugin mutation or user private transcript transfer becomes necessary.

No paid calls and no personal ChatGPT account mutation are authorized by this recovery package.
