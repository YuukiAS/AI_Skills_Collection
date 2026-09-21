# Workflow Identity & Capability Gate Lifecycle — Critic Review v1

- Date: 2026-09-20
- Review role: independent Critic
- Review stage: DESIGN_PROPOSAL
- Reviewed proposal: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_PROPOSAL_2026-09-20.md`
- Reviewed proposal version: `v1`
- Reviewed proposal commit: `deddff2e4903cfaef0dc2a7e4d9d7ebdc91330c3`
- Proposal blob SHA at reviewed commit and current main: `22db6ca68c49b256b3b5752e4f8c74ae178113a6` — unchanged
- AI_Skills current main checked during review: `699fa2ed167270450c2e380a452cb40f39b95393`
- Bridge Kit current main checked during review: `afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Decision: **REVISE**
- Complexity verdict: **APPROPRIATE**
- Scope of this document: design review only; no implementation authorization

## 1. Critic conclusion

The proposal is directionally correct and solves two real problems with one small governance boundary rather than inventing a new control system.

For capability gates, the right long-term model is indeed: **stable user-facing capability dimensions + a growing bank of known regression cases + risk/change-impact-based release depth + safe broad/full fallback when impact cannot be trusted**. A real failure should not automatically create a new top-level gate. The existing 056 post-probe precedent already demonstrates the correct behavior: new CUHK-Date-like failures were assigned to existing G1/G2/G4/G7 or Source Discovery rather than creating G9/G10.

For task identity, replacing the numbered primary identity for **new** tasks is also justified. Current Bridge Kit does not merely document the numeric convention; it enforces it in `ai_bridge_kit/reviewed_handoff.py`, `ai_bridge_kit/cli.py`, and `scripts/validate_handoff_workspace.py`. Therefore a semantic Reviewed Handoff task key cannot be implemented truthfully by AI_Skills documentation alone. A bounded Bridge change is required.

The v1 proposal is not over-engineered: its “Capability Gate Charter / Regression Bank / Release Selection” can remain policy concepts inside existing Plan/policy surfaces, with no new schema, registry, ledger, watcher, database, state machine, or issue-tracker dependency. I do **not** approve turning those labels into three new machine artifacts.

However, v1 still has two design-level ambiguities that can produce wrong production behavior, plus one acceptance-coverage hole. They are small enough to repair in v2 without changing the architecture, but material enough that this exact v1 should not be frozen into an execution package.

## 2. Source reality independently verified

I re-read current AI_Skills main rather than relying on Planner summary, including:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/PLUGIN_MATURITY.md`
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`
- the reviewed v1 proposal
- current 055 proposal / execution-review / Reviewed Handoff identity and final closure evidence
- current `056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` and canonical Goal
- current 057 v2 proposal and integration-recovery proposal
- `PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`

I also re-read Bridge Kit current main, including:

- `ai_bridge_kit/reviewed_handoff.py`
- `ai_bridge_kit/cli.py`
- `scripts/validate_handoff_workspace.py`
- `tests/test_reviewed_handoff.py`
- the task-key / branch-relevant Reviewed Handoff templates
- `docs/design/reviewed_handoff_parallel_task_branches.md`

The critical factual findings are:

1. Bridge current production source hard-codes numeric task keys in three validation surfaces. In `reviewed_handoff.py`, `init_task()` directly rejects a non-numbered key. Therefore AI_Skills cannot legally use the proposed semantic keys through the current canonical Reviewed Handoff normal entry without a Bridge change.
2. Reviewed Handoff already treats `task_key` as a cross-surface identity: task dir, result dir, branch convention, CURRENT/PLAN/RESULT/REVIEW, and text/visual review artifacts all bind to it.
3. Bridge’s parallel-task design explicitly separates **dependency** from task creation order. Tasks may progress concurrently; dependency is represented by actual source/Plan relationships, not by the numeric prefix.
4. Current 056 has two mutable production repositories: AI_Skills and Bridge. It modifies AI_Skills workflow-core, web-development and ai-skills-core, while Bridge changes transport / wait-resume / Lite distribution. Product repos are read-only references. Thus “cross-plugin” and “cross-repo” are both topologically true unless a precedence rule is defined.
5. Current 057 stayed the same task through integration recovery rather than creating a successor. This is strong internal evidence that repair/integration should preserve one task identity.
6. Current 055 has now closed on main while preserving its original task key through multiple candidate/review/recovery stages. The current main advancement after the reviewed proposal is almost entirely 055 execution/closure work; the proposal blob itself has not changed. That source drift does not invalidate the redesign, and it further supports stable task identity across repair.

## 3. Independent external research

### Adopted

**Anthropic — capability vs regression.** Anthropic explicitly distinguishes capability/quality evals from regression evals and says high-performing capability evals can “graduate” into continuously run regression suites. This directly supports the v1 direction that the capability taxonomy need not grow with every real failure; the long-lived regression set should grow instead.

Source:
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

**OpenAI — real failures become bounded evals, then broader regression.** OpenAI’s Tax AI engineering write-up describes grouping recurring real failures into actionable eval targets, fixing them, rerunning targeted evals, and then running broader regression suites. This supports “failure -> existing capability/regression evidence” rather than “failure -> new top-level gate”.

Source:
https://openai.com/index/building-self-improving-tax-agents-with-codex/

**Microsoft — impact selection plus safe full fallback.** Azure Test Impact Analysis selects impacted tests, includes previously failing/new tests, falls back to all tests when impact cannot be understood, and supports periodic full-suite overrides. I adopt the safety principle only: selective regression is valid only when impact is explainable, with a conservative full fallback when it is not.

Source:
https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-impact-analysis?view=azure-devops

**GitHub / Azure — identity, display meaning, dependency and state are separate concerns.** GitHub Actions uses a unique semantic `job_id`, optional displayed `name`, and explicit `needs` dependencies. Azure Boards separately maintains system-assigned immutable IDs, human-readable titles, and workflow state. The transferable lesson is not “every system must use semantic-only IDs”; it is that task meaning, execution dependency, and state should not be conflated into one creation ordinal.

Sources:
https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-jobs
https://learn.microsoft.com/en-us/azure/devops/boards/queries/titles-ids-descriptions?view=azure-devops

**Git ref safety.** Git’s official ref rules reject `..`, spaces, `~`, `^`, `:`, `?`, `*`, `[`, `@{`, backslash, and several leading/trailing forms. The proposed lowercase ASCII kebab components with a single `--` separator avoid those hazards. `--` itself is not a Git ref-format problem. A conservative total-length cap such as 96 characters is reasonable as a project policy, though it is not a Git requirement.

Source:
https://git-scm.com/docs/git-check-ref-format

### Deliberately not adopted

- I do not recommend Microsoft-style dependency-map machinery for AI plugin releases. AI prompt/runtime/model/routing effects are less statically traceable than managed-code dependencies.
- I do not recommend a mandatory periodic paid/manual full run. Full fallback should be triggered by release risk/uncertainty and maturity promotion, not by a fixed paid cadence.
- I do not recommend copying Azure/GitHub’s opaque immutable ID layer into a new UUID/database/issue-number system. This repo already has durable, non-renamed task directories and branch identity; collision rejection plus semantically meaningful disambiguation is enough until real usage proves otherwise.
- I do not recommend GitHub Issues as the canonical task source of truth.

## 4. Capability Gate lifecycle review

### 4.1 What is correct

The core distinction among a stable capability claim, accumulated regression cases, and per-release evaluation depth is necessary and sufficient **as policy semantics**.

The new-failure rule is also correct: a failure belongs under an existing gate when the same user-facing capability claim, evidence semantics and failure verdict already cover it. A new gate is justified only when the product actually claims a distinct capability that cannot be represented without distorting an existing gate.

This does not mean a gate may become an unlimited “miscellaneous failures” bucket. If absorbing a new case changes what the gate claims, requires a materially different evidence type, or makes PASS/FAIL mean something different, the taxonomy must split or add a distinct gate. The v1 criteria already mostly express this and should be retained.

The merge/split/retirement rule is strong enough in principle: versioned Planner/Critic review, explicit mapping of old obligations, preserved historical PASS/FAIL, and explicit product-claim retirement prevent quiet acceptance weakening.

The same-final-candidate requirement is correctly preserved. Risk-based selection may change **depth**, not candidate identity.

### 4.2 What remains too permissive

The weak point is not the existence of risk-based selection; it is the operational boundary for calling a release-critical gate “unaffected”.

“Planner can confidently explain” is not enough as a release rule. Shared prompt/model/runtime/router/normal-entry/assembly changes can have nonlocal effects even when the source diff looks narrow. A light canary on each “unaffected” gate can be insufficient if the impact classification itself is optimistic.

This is a design blocker below. The fix should remain textual/policy-level and should **not** create an impact registry or dependency graph.

### 4.3 Maturity expectation

Maturity should strengthen regression confidence without multiplying top-level gates or paid samples.

For routine mature-plugin patches, a bounded qualitative selection remains appropriate. But maturity promotion should be a broad/full-fallback event: the final candidate should run the complete applicable cheap/deterministic known-regression bank and broad release-critical capability coverage, with fresh evidence where the capability is qualitative/generalization-sensitive. No fixed number of fresh/paid samples is needed.

Thus a mature plugin can keep six or eight stable gate dimensions for years while the known-regression corpus grows substantially.

## 5. Semantic task-key review

### 5.1 The move away from 0xx is justified

Keeping `055_clear_writing...` and relying on the suffix does not fully solve the user problem. The numeric prefix still dominates branch/path scanning, suggests queue/order semantics that the workflow does not have, and contributes nothing to owner/scope/goal understanding.

Current 057-before-056 sequencing is direct evidence: it happened because 057 had an explicit source/ownership dependency with 056, not because 057’s number “comes after” 056. Current parallel-task Bridge policy likewise says concurrency depends on actual source/dependency, not numeric order.

So new semantic primary identity is superior for this repository.

### 5.2 Scope classes are sufficient only with a mutually exclusive precedence rule

The four classes can work:

- `plugin-<canonical-plugin-slug>`
- `cross-plugin`
- `repo`
- `cross-repo`

But v1 classifies by “primary objective”, while current 056 is both cross-plugin and cross-repo. That leaves future Planners free to make the same topology look different based on wording.

The minimum executable rule should be based first on **mutable canonical repo count**, then on AI_Skills plugin scope:

1. more than one mutable canonical repository required for the same task -> `cross-repo`;
2. exactly one mutable repository, and it is AI_Skills with more than one plugin in scope -> `cross-plugin`;
3. exactly one mutable repository and one AI_Skills plugin -> `plugin-<canonical-plugin-slug>`;
4. exactly one mutable repository and the objective is repo-wide/non-plugin -> `repo`.

Read-only evidence/reference repositories do not change the scope class.

Under this rule, current 056 would be:

`cross-repo--product-delivery-discipline`

because AI_Skills **and** Bridge both have necessary production writes. The Plan should then say that the AI_Skills side spans workflow-core, web-development and ai-skills-core. This is causally clearer than `cross-plugin--...`: the same task key is also used on the Bridge task branch, where “cross-plugin” would not describe the local mutation boundary at all.

Current 057 remains `cross-repo--repo-agents-hygiene`.

A future task that changes workflow-core + web-development but never writes outside AI_Skills would be `cross-plugin--...`.

### 5.3 Why not dates, issue numbers, UUIDs, owner IDs or slash hierarchy

- Date/timestamp: unique but still chronological/opaque about scope.
- GitHub issue number: adds another external source of truth.
- UUID: solves collision but destroys scanability; external systems often pair it with a title because humans still need semantics.
- Owner-based key: owner can change and does not say what the work does.
- Slash hierarchy inside task key: unnecessary because `reviewed/<task_key>` and filesystem paths already add hierarchy; avoiding additional `/` keeps task key one portable component.

### 5.4 Separator and collision

Lowercase kebab components and one `--` separator are safe for the current Git branch/path consumers, provided the parser rejects empty components, extra `--` separators, leading/trailing hyphens outside the chosen grammar, and the known Git-invalid forms.

I do **not** require an opaque unique suffix in v1.

Creation should fail if the canonical task identity already exists in any task-owned identity surface relevant to creation. The Planner should then choose a **semantically meaningful** disambiguation that reflects a genuinely different closed objective/release line/component. If the “new” work is actually repair/recovery/integration of the prior objective, it must reuse the existing key instead of creating a successor.

If repeated genuine same-goal collisions become common in real use, a short secondary uniqueness mechanism can be reviewed later. There is no evidence now that justifies adding UUID/sequence machinery preemptively.

### 5.5 Migration boundary

The v1 migration direction is correct and should remain unchanged:

- no rename of 001–057;
- no move of active branches/results/evidence;
- no rewrite of historical PASS/FAIL;
- cutover affects only new creation;
- validation accepts legacy + semantic;
- new creation accepts semantic only;
- no new task merely to “migrate” an old one;
- completion order is never inferred from the old numeric order.

## 6. Ownership review

The ownership split is mostly correct, with one wording refinement.

**Canonical gate-lifecycle policy authority** should remain `PLUGIN_CAPABILITY_GATE_POLICY.md`. AI Skills Maintainer should operationalize it: regression intake/deduplication, source/generated parity, plugin/version/release maintenance, and release closure. It should not become the professional judge of gate meaning.

**Target domain plugin** must keep professional gate semantics and domain correctness.

**workflow-core** should own how an AI_Skills frozen Plan records release selection, same-final-candidate evidence, and narrow-vs-full fallback. It must not become a second task-key parser and must not absorb domain judgment.

**Bridge Kit Reviewed Handoff** is the correct owner of cross-repo task-key lexical syntax, dual-format legacy compatibility, task creation, and propagation because current Bridge runtime already enforces that identity. A local AI_Skills adapter would duplicate the parser and would not make semantic keys legal through the canonical Reviewed Handoff entry.

Bridge should validate task-key syntax and compatibility; AI_Skills policy/Maintainer should decide whether `plugin-writing-style`, `cross-plugin`, `repo`, or `cross-repo` is semantically correct and whether a plugin slug is canonical. Bridge must not import the AI_Skills registry or become a plugin-ownership engine.

The necessary Bridge change is therefore small: task-key grammar/creation/validation/propagation tests and docs only. No Reviewed Handoff state graph, schema, controller, watcher, branch lifecycle, or release engine change is justified by this proposal.

## 7. File organization subproposal

I do **not** approve the proposed `docs/design/<task_key>/...`, `docs/goals/<task_key>/...`, `docs/operations/prompts/<task_key>/...` reorganization as part of this implementation.

It is plausible that task-local grouping would reduce flat-file clutter, but this is not required to solve either user goal, and adopting it only for future tasks creates a second document-layout convention immediately. It also creates avoidable link/prompt churn while the task-key cutover is already touching identity surfaces.

Disposition: **defer as a non-blocking follow-up**. Keep existing document locations for the first semantic-key implementation. Revisit only if actual semantic-key usage still leaves document discovery materially difficult.

No historical file migration is justified.

## 8. Capability Gate Matrix review

### G1 — Semantic identity

Distinct and necessary. It must prove canonical Bridge creation, not a helper/regex unit test only.

Required future evidence: a normal semantic task creation succeeds with no numeric prefix; invalid semantic keys fail cleanly; collision is fail-closed.

### G2 — Identity propagation

Distinct from G1 and necessary.

The current wording is too generic for execution. The implementation package must explicitly cover:

- task directory;
- result directory;
- `reviewed/<task_key>` branch naming/validation;
- CURRENT / PLAN / RESULT / REVIEW / FINAL_REPORT identity;
- visual-review manifest/evidence task identity;
- text-review manifest/evidence task identity;
- task-bound Scheduled GPT / Executor path consumption.

No new gate number is needed; strengthen G2.

### G3 — Scope clarity

Necessary, but currently blocked by the 056 ambiguity. It should test the mutually exclusive scope precedence with representative cases:

- one plugin;
- multiple AI_Skills plugins in one mutable repo;
- repo-wide non-plugin task;
- multiple mutable repos;
- multiple read-only references that **do not** force `cross-repo`.

### G4 — Legacy compatibility

Necessary and correctly aimed.

It must prove both directions simultaneously:

- legacy numbered task remains valid and operable;
- semantic task can be newly created;
- new numeric creation is rejected after cutover;
- legacy + semantic tasks can coexist in one workspace without path/evidence confusion.

### G5 — Gate lifecycle

Necessary and not redundant with G6.

Do not prove it only by adding policy text. Use at least one real historical failure-classification case from current repo evidence, such as the 056 post-probe “no G9/G10” precedent, plus a contrasting truly new-capability example. Gate merge/split/retirement should preserve obligation mapping.

### G6 — Release regression safety

Necessary, but v1’s fallback boundary needs revision. It should prove:

- genuinely isolated affected-gate selection;
- unaffected final-candidate canary;
- mandatory broad/full fallback when impact is uncertain/cross-cutting;
- maturity-promotion broad coverage;
- no old-candidate PASS stitching.

### G7 — No governance bloat

Necessary should-not-change gate. PASS requires no new registry/ledger/controller/watcher/state machine and no second parser. Ordinary small tasks must not inherit an expensive full matrix simply because the lifecycle policy exists.

No additional G8 is needed for the redesign if G1–G7 are strengthened as above.

## 9. Blocking findings

### C-WIGL-01-SCOPE-PRECEDENCE

**Requirement / contract**

The user requires task/branch/path identity to reveal meaningful scope and specifically requires the design to handle 056-like multi-plugin + Bridge cases without ambiguity.

**Observed source/evidence**

Current 056 v0.3 has necessary writes in both `YuukiAS/AI_Skills_Collection` and `YuukiAS/GPT_Codex_AI_Bridge_Kit`. Its AI_Skills side spans workflow-core, web-development and ai-skills-core; product repos are read-only. Proposal v1 nevertheless maps it to `cross-plugin--product-delivery-discipline` using a subjective “primary objective” rule.

**Causal risk**

The categories overlap. The same task topology can be named `cross-plugin` or `cross-repo` depending on Planner prose, and the resulting `cross-plugin--...` branch is misleading inside the Bridge repository itself. The user still cannot infer the actual mutation boundary from the task key.

**Minimum closure**

Define a mutually exclusive precedence rule based first on mutable canonical repo count, then on within-repo plugin scope, as specified in §5.2. Reclassify the 056 example to `cross-repo--product-delivery-discipline`. Keep read-only references out of the scope count.

**Owner**

Planner for proposal v2; AI Skills Maintainer/policy for AI_Skills scope semantics. Bridge only validates syntax.

### C-WIGL-02-IMPACT-FALLBACK-BOUNDARY

**Requirement / contract**

Capability-gate lifecycle must bound cost without allowing mature released capabilities to regress silently. Same-final-candidate coverage must survive risk-based selection, and maturity promotion must have stronger—not weaker—regression expectations.

**Observed source/evidence**

Proposal v1 permits unaffected release-critical gates to use direct final-candidate canaries and says uncertain/cross-cutting impact falls back to a broad/full matrix, but the operational boundary is “Planner cannot confidently explain why a gate is unaffected”. That is too subjective for shared prompt/model/runtime/router/normal-entry/assembly changes.

External evidence reinforces the missing rule: Microsoft TIA uses impacted selection only with safe all-test fallback when impact cannot be understood; Anthropic distinguishes continuously run regression suites from capability evals; OpenAI’s production loop reruns targeted evals and then broader regression suites.

**Causal risk**

An optimistic impact label can reduce an old released capability to a weak canary exactly when a cross-cutting change has nonlocal effects. The policy would then preserve the words “same final candidate” while weakening what that candidate actually proves.

**Minimum closure**

Without adding any schema/registry:

1. add explicit full/broad-fallback triggers for changes to shared generation/prompt assembly, model/runtime/provider/router, normal-entry/installation/invocation plumbing, or any shared layer consumed by multiple release-critical gates;
2. require fallback when consumer impact cannot be traced, a new failure has unresolved/multi-gate attribution, or the evaluation harness/grader change materially changes what previous evidence means;
3. require broad/full release-critical coverage for maturity promotion;
4. allow narrow selection only when isolation is explainable and the complete applicable cheap/deterministic known-regression bank passes, with direct final-candidate evidence for every release-critical gate;
5. do not set a fixed number of fresh/manual/paid samples.

**Owner**

Planner/policy for the rule; workflow-core for execution semantics; AI Skills Maintainer for release application.

### C-WIGL-03-IDENTITY-CUTOVER-COVERAGE

**Requirement / contract**

The cutover must work through normal Reviewed Handoff entry and must preserve all task-key consumers, including branch/result/text/visual identity and legacy coexistence.

**Observed source/evidence**

Bridge current main contains numeric validation in three separate production/validation surfaces. Reviewed Handoff also binds `task_key` into text/visual review manifests/evidence and result/branch paths. Proposal G2 says “review evidence” generically and Phase C says “status/review evidence”, which could be satisfied without explicitly exercising text/visual and both validator paths.

**Causal risk**

The main semantic task can be created while a less-visible consumer still rejects, truncates, or mismatches the key. Mechanical regex PASS would then be mistaken for complete identity propagation.

**Minimum closure**

Strengthen existing G1/G2/G4; do not add a new gate:

- canonical task creation and generic workspace validation both consume one canonical task-key validator;
- semantic task propagation explicitly includes text-review and visual-review manifests/evidence, branch/result paths, CURRENT/PLAN/RESULT/REVIEW/FINAL_REPORT;
- one legacy task and one semantic task coexist in the same validation fixture/workspace;
- new numeric creation fails after cutover while legacy validation continues.

**Owner**

Bridge Kit Reviewed Handoff.

## 10. Non-blocking recommendations

1. Keep “Capability Gate Charter / Regression Bank / Release Selection” as vocabulary/sections only. Do not create files named after them unless an existing Plan naturally needs a small table.
2. In gate-lifecycle wording, replace “complete deterministic bank when practical” with a clearer default: run all **applicable cheap deterministic known regressions**, and require an explicit applicability/infeasibility reason for omission. This matters more as plugin maturity increases.
3. Keep semantic-key collision handling semantic-first; do not add UUID/date/sequence suffixes now.
4. Bridge should own lexical parsing/compatibility; AI_Skills should own whether the selected scope class and plugin slug are semantically valid. Do not make Bridge read the AI_Skills registry.
5. Defer task-local design-doc directory grouping.
6. Keep the current 001–057 history exactly as-is; do not use the new naming design as a reason to create successor tasks or rewrite old results.

## 11. Complexity verdict

**APPROPRIATE**, conditional on the above revision.

What should remain:

- stable capability taxonomy;
- growing regression bank;
- risk/change-impact release depth;
- safe broad/full fallback;
- same-final-candidate rule;
- semantic task key for new creation;
- dual legacy/semantic validation;
- one task identity through review/repair/integration;
- bounded Bridge task-key support.

What should not be added:

- new controller;
- watcher;
- database;
- task registry;
- ACTIVE_WORK ledger;
- new state machine;
- mandatory GitHub Issues;
- historical migration;
- fixed per-gate fresh/paid sample counts;
- automatic opaque suffix on every semantic key;
- new document-directory convention in this same implementation.

## 12. Decision

```text
REVIEWED_PROPOSAL_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_PROPOSAL_2026-09-20.md
REVIEWED_PROPOSAL_VERSION=v1
REVIEWED_PROPOSAL_COMMIT=deddff2e4903cfaef0dc2a7e4d9d7ebdc91330c3
DECISION=REVISE
COMPLEXITY=APPROPRIATE
BLOCKERS=C-WIGL-01-SCOPE-PRECEDENCE,C-WIGL-02-IMPACT-FALLBACK-BOUNDARY,C-WIGL-03-IDENTITY-CUTOVER-COVERAGE
NON_BLOCKING=DEFER_TASK_LOCAL_DOC_GROUPING;KEEP_POLICY_CONCEPTS_NON_MACHINE;NO_OPAQUE_SUFFIX_YET;BRIDGE_SYNTAX_AI_SKILLS_SCOPE_SEMANTICS_SPLIT
READY_FOR_EXECUTION_PLAN=NO
NEXT_HANDOFF=PLANNER
```

## 13. Planner handoff

The next Planner round should be a small v2 revision, not a new task and not a successor workflow. It should preserve the architecture and close only the three blockers above.

Do not prepare an executable Goal/Kickoff until a Critic reviews the exact v2 proposal and returns PASS.
