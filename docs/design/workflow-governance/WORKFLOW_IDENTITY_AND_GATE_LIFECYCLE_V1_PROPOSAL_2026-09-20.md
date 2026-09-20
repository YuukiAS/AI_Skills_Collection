# Workflow Identity & Capability Gate Lifecycle — Planner Proposal v1

- Date: 2026-09-20
- Status: DRAFT_FOR_CRITIC_REVIEW
- Primary repo: `YuukiAS/AI_Skills_Collection`
- Primary source: `main@f034f5666b30fe0b8d7e5df717fc0a299f2d5dc0`
- Cross-repo source inspected: `YuukiAS/GPT_Codex_AI_Bridge_Kit main@afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Design topic: `workflow-identity-and-gate-lifecycle`
- Proposed owners: AI Skills Maintainer for AI_Skills maintenance policy; workflow-core for execution semantics; Bridge Kit Reviewed Handoff for cross-repo task-key syntax/validation
- Execution branch/worktree: NONE — design review only
- This proposal does not rename or modify active 055/056/057 tasks, does not change production source, and does not authorize implementation.

## 1. Bottom line

There are two separate problems that should be redesigned together because they meet at the same long-term workflow boundary.

First, capability gates should **not** grow one-for-one with every new regression. As a plugin matures, the gate taxonomy should converge around stable user-facing capability claims, while the regression cases underneath those gates should keep accumulating. New real failures should normally become new regression cases inside an existing gate. A new gate is justified only when the plugin has gained or exposed a genuinely distinct capability claim or failure mode that the existing taxonomy cannot represent without becoming misleading.

Second, new Reviewed Handoff workflows should stop using opaque sequential identifiers such as `055`, `056`, `057` as their primary human identity. Those numbers encode creation order, but concurrent workflows do not execute or finish in that order. The current repo already demonstrates the problem: 055 is a Clear Writing release-convergence task, 056 is a broad product-delivery discipline change, and 057 is a cross-repository AGENTS hygiene task; 057 can materially advance before 055 or 056 closes. The number therefore makes the active workflow harder, not easier, to identify.

The proposed replacement is:

```text
stable semantic task key
+ explicit scope/affected-plugin declaration in the frozen Plan
+ legacy compatibility for all existing numbered tasks
```

No global task registry, active-work ledger, database, watcher, second state machine, or GitHub Issues dependency is proposed.

## 2. Verified current reality

### 2.1 Capability gates already point toward a stable taxonomy

The current `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md` explicitly says gate count is driven by distinct user capabilities rather than a fixed number, and Critic should require merging/deletion when gates duplicate one another.

The existing Product Delivery Discipline design has already used the right pattern once: `PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md` explicitly says not to create G9/G10 when later evidence arrives; new scenarios are folded into existing gates where they represent the same capability.

The missing piece is a lifecycle rule explaining what happens after a plugin has been through many releases: which things stay stable, what grows, what may be merged/retired, and how final-candidate regression evidence can remain strong without turning every release into an ever-expanding paid/manual matrix.

### 2.2 The numbered task key is not only a documentation habit; Bridge Kit enforces it

Current Bridge Kit source contains:

```python
TASK_KEY_RE = re.compile(r"^\d+_[A-Za-z0-9]+(?:_[A-Za-z0-9]+){0,2}$")
```

and task creation rejects any key that does not look like `<id>_<1-3-word_slug>`. Equivalent numeric-key validation also exists in `ai_bridge_kit/cli.py` and `scripts/validate_handoff_workspace.py`.

Reviewed Handoff then reuses the same `task_key` across:

- `automation/reviewed_handoff/tasks/<task_key>/`;
- `results/<task_key>/`;
- `reviewed/<task_key>` branches;
- visual/text review identity;
- result/review/final-report artifacts.

Therefore AI_Skills cannot truthfully solve the new-name problem only by changing README wording. If new non-numbered task keys are to be normal Reviewed Handoff identities, Bridge Kit must support them at the canonical parser/validator layer. This is a cross-repo reusable handoff capability and belongs in Bridge Kit, not in an AI_Skills-only regex fork.

### 2.3 055 / 056 / 057 are materially different scopes

Current source confirms:

- `055_clear_writing_release_convergence`: single-plugin Clear Writing / writing-style release convergence.
- `056_product_delivery_discipline`: a broad change whose current execution plan writes AI_Skills workflow-core / web-development / ai-skills-core and Bridge Kit while treating Bobbio, Lucerna, Mica, Asteria, SeminarArc and CUHK Date as bounded read-only references.
- `057_repo_agents_hygiene`: a cross-repository AGENTS/scaffold hygiene program whose integration preceded a bounded 056 source-drift revalidation.

This is exactly the case where a global sequence number is misleading: ordering is creation history, not dependency, owner, scope, priority, or completion state.

## 3. External reality check

This proposal adopts only a few external lessons, without importing another framework.

1. Anthropic's 2026 agent-evaluation guidance separates capability/quality evals from regression evals. When a capability eval becomes saturated, it can “graduate” into a continuously run regression suite. The same guidance recommends converting production/user failures into test cases and maintaining eval suites as living artifacts. This supports a stable capability taxonomy with a growing regression bank rather than endless top-level gate proliferation.
2. Microsoft Test Impact Analysis addresses mature regression suites by selecting impacted tests for fast feedback, but it has a safe fallback to the full suite when impact cannot be understood and supports periodic full runs. For AI plugins, dependency inference is less reliable than ordinary managed code, so this proposal borrows the **safe-fallback principle**, not Microsoft's implementation.
3. GitHub's current issue/project model separates human-readable titles from structured type/labels/fields. The useful lesson is that “what work is this?” and “when was it created?” do not need to be collapsed into one opaque ordinal. This proposal does not make GitHub Issues the source of truth.

References for Critic to re-check independently:

- Anthropic, *Demystifying evals for AI agents*, 2026-01-09.
- Microsoft Learn, *Use Test Impact Analysis*, current 2026 documentation.
- GitHub Docs, issue creation / issue fields / workflow display titles, current 2026 documentation.

## 4. Proposal A — Capability Gate lifecycle

### 4.1 Separate three concepts

The policy should distinguish three concepts without introducing a new machine schema.

**Capability Gate Charter**

A relatively stable set of user-facing capability claims and distinct failure classes. A gate exists because it proves something meaningfully different from the other gates.

**Regression Bank**

The known cases attached to those gates: prior real failures, should-change / should-not-change pairs, representative artifacts, deterministic checks, and previously accepted edge cases. This bank is expected to grow as the plugin is used.

**Release Selection**

The bounded subset and evaluation depth used for a particular candidate. It is chosen from risk and change impact, but it may never erase the underlying regression obligation.

These can remain sections/tables in the existing Proposal/Plan/policy. No registry, database, ledger, or new state machine is required.

### 4.2 New-failure rule: regression first, gate second

Whenever a real project exposes a new failure, Planner must first ask:

> Which existing capability claim failed?

If an existing gate already represents that capability, the new evidence becomes a regression case under that gate. It does **not** create G9/G10 merely because the example is new.

A new gate is allowed only when all are true:

1. the failure/claim is user-visible and materially distinct;
2. no existing gate can represent it without conflating different success/failure semantics;
3. it requires meaningfully different evidence or a meaningfully different failure verdict;
4. the plugin actually claims or must claim this capability in normal use.

Examples:

- A new formula-corruption example under an existing “structured technical fidelity” gate is a new regression case, not a new gate.
- A plugin that newly starts producing editable PPTX artifacts may need a distinct editability/export gate if no existing gate covers that product claim.

### 4.3 Gate merge/split/retirement rule

Gates are not immortal, but they cannot be casually deleted to make release easier.

A merge, split, or retirement requires a versioned Planner/Critic design decision that explains:

- old capability claim(s);
- new destination gate(s), if any;
- where every important regression obligation moves;
- whether the product claim itself was intentionally retired;
- why the change reduces duplication or reflects a real architecture/product change rather than weakening acceptance.

Historical evidence remains historical; do not rewrite old PASS/FAIL records.

No new permanent migration ledger is required. The change can live in the reviewed proposal/policy revision and plugin changelog when it affects release behavior.

### 4.4 Final-candidate regression depth

“All release-critical gates must be passed by the same final candidate” remains unchanged.

However, this should not mean “every historical qualitative sample must receive a new paid/manual review on every release.” The execution depth is:

1. **Cheap/deterministic known regression**: run the complete applicable automated bank when practical.
2. **Affected/high-risk gates**: run their representative real artifacts and qualitative checks at the depth needed to prove the changed behavior.
3. **Unaffected release-critical gates**: require direct final-candidate canary evidence sufficient to show the gate still works; old candidate PASS cannot substitute for this.
4. **Cross-cutting or uncertain impact**: fall back to the broad/full release matrix rather than claiming a narrow impact analysis that cannot be trusted.
5. **Fresh generalization**: use a frozen fresh batch when a release adds substantial behavior, changes model/runtime/routing/shared generation logic, seeks a maturity promotion, or leaves material generalization uncertainty. A fresh case that is inspected and used for repair becomes a regression case afterward.
6. **Paid/external review**: only when the frozen acceptance/risk model actually requires it; it is not multiplied automatically by gate count.

Impact selection is an optimization, not an exemption. If Planner cannot confidently explain why a gate is unaffected, that gate is treated as impacted for release purposes.

### 4.5 Expected long-term shape

A mature plugin may still have roughly the same 6–10 capability dimensions it had at `0.x`, while each gate's regression bank becomes much richer.

That is the intended evolution:

```text
gate taxonomy -> converges
regression bank -> grows
fresh evidence -> renewed when warranted
paid/manual burden -> bounded by risk, not by historical case count
```

If a plugin adds two or three top-level gates every release, Critic should treat that as a design smell unless the product scope really expanded by two or three distinct capabilities.

## 5. Proposal B — Replace new 0xx task identities with semantic keys

### 5.1 New task-key format

For **new** Reviewed Handoff tasks after cutover, use a semantic key:

```text
<scope>--<goal>
```

Both components are lowercase kebab-case. The double hyphen separates stable scope from the concrete goal.

Allowed scope forms:

```text
plugin-<canonical-plugin-slug>
cross-plugin
repo
cross-repo
```

Examples:

```text
plugin-writing-style--release-convergence
plugin-presentations--visual-quality-hardening
cross-plugin--product-delivery-discipline
cross-repo--repo-agents-hygiene
repo--workflow-identity-rework
```

The canonical plugin slug, not the display name, is used in a single-plugin task key so that “Clear Writing” maps unambiguously to `writing-style`.

### 5.2 What the key does and does not encode

The key should answer, at a glance:

- is this one plugin, several plugins, repo maintenance, or a cross-repo program?
- what is the substantive goal?

It should **not** try to encode:

- creation order;
- priority;
- current state;
- every affected repository;
- every affected plugin;
- review round;
- candidate version;
- date;
- successor count.

Those change independently and already have proper locations in Plan/CURRENT/history.

For a `cross-plugin` task, the frozen Proposal/Plan must explicitly list affected plugins and say which one owns each professional decision. For a `cross-repo` task, it must list mutable/read-only repositories and owners. This is human-readable contract text, not a new CURRENT schema.

### 5.3 How 056 should be represented under the new scheme

The current 056 objective is primarily a cross-plugin AI_Skills delivery-discipline change, with Bridge Kit as a supporting cross-repo runtime owner. Under this proposal its human task identity would therefore be:

```text
cross-plugin--product-delivery-discipline
```

and the frozen Plan would explicitly state:

```text
affected plugins:
- workflow-core
- web-development
- ai-skills-core

supporting mutable repo:
- GPT_Codex_AI_Bridge_Kit

read-only product references:
- Bobbio
- Lucerna
- Mica
- Asteria
- SeminarArc
- CUHK Date
```

This is preferable to embedding every plugin/repository in the key, because the key would become long and unstable when a supporting surface is removed or becomes read-only.

By contrast, 057's *primary objective itself* is cross-repository instruction hygiene, so its semantic form would be `cross-repo--repo-agents-hygiene`.

These are examples only. Existing 056/057 identities are not renamed.

### 5.4 Semantic key syntax and compatibility

Bridge Kit should own one canonical parser with two accepted classes:

```text
LEGACY_TASK_KEY
  current numbered form, validation-only for existing tasks

SEMANTIC_TASK_KEY
  new <scope>--<goal> form
```

Recommended semantic constraints for Critic review:

- lowercase ASCII letters/digits/hyphen only inside components;
- one `--` separator;
- one of the four scope forms above;
- non-empty goal, normally 2–6 words;
- bounded total length (for example <= 96 characters) so branches, worktrees and artifact paths remain practical.

New-task creation should accept only semantic keys after cutover. Workspace validation must continue accepting legacy numbered tasks indefinitely unless a future separately reviewed migration is justified.

No existing task directory, result path, branch, artifact identity, review evidence, or historical document is renamed.

### 5.5 Same task identity through repair and integration

The semantic key stays stable for the same major objective through:

- design revisions;
- implementation-plan revisions;
- Critic rounds;
- repair cycles;
- CI recovery;
- evidence correction;
- integration.

Those are revisions/stages of the same task, not successor IDs.

A genuinely new task gets a new semantic goal only when the old objective has closed or the product/architecture scope has materially changed. This directly reduces the current tendency for chronology-like IDs to look like an ordered queue when they are actually independent workflows.

### 5.6 Branch and artifact paths remain unchanged structurally

Keep the existing generic layout:

```text
reviewed/<task_key>
automation/reviewed_handoff/tasks/<task_key>/
results/<task_key>/
```

For new AI_Skills design artifacts, adopt task-local grouping rather than growing more flat prefixed filenames:

```text
docs/design/<task_key>/PROPOSAL.md
docs/design/<task_key>/IMPLEMENTATION_PLAN.md
docs/design/<task_key>/CRITIC_PROMPT.md
docs/goals/<task_key>/GOAL.md
docs/operations/prompts/<task_key>/KICKOFF.md
```

This grouping is proposed only for new tasks. Do not migrate old 0xx artifacts merely for aesthetics.

Critic should explicitly decide whether this path cleanup is useful or unnecessary scope. It is separable from semantic task-key support.

## 6. Ownership split

### AI Skills Maintainer

Owns AI_Skills-specific maintenance policy:

- gate lifecycle rule;
- regression-bank intake/deduplication;
- plugin/version/release closure;
- choosing the AI_Skills semantic scope class;
- ensuring single-plugin tasks use canonical plugin slugs;
- ensuring cross-plugin Plans list affected plugins and domain owners.

It does not become the professional judge of writing, presentations, statistics, imaging, etc.

### Target domain plugin

Owns what the capability gates mean professionally and whether a regression case is scientifically/domain-correct.

### workflow-core

Owns AI_Skills execution semantics:

- how a frozen Plan declares scope and affected owners;
- how release selection / final-candidate verification is executed;
- how narrow-vs-full regression fallback is handled without claiming untested readiness.

It should not reimplement Bridge Kit task-key parsing.

### Bridge Kit Reviewed Handoff

Owns cross-repo task-key syntax and compatibility because its runtime currently enforces the numeric regex and carries `task_key` across branches, task directories and review evidence.

It should:

- add semantic-key support;
- keep legacy-key validation;
- update canonical task-creation validation and tests;
- keep `reviewed/<task_key>` and artifact identity semantics unchanged.

This is a justified Bridge Kit change because the capability is genuinely cross-repo Reviewed Handoff identity, not an AI_Skills-only convention.

## 7. Alternatives considered

### A. Keep 0xx and only improve titles

Rejected as the primary solution. Titles help humans reading one file, but branch names, result directories, prompts and task references remain dominated by opaque ordinals. The current 055/056/057 concurrency problem remains.

### B. Replace 0xx with dates/timestamps

Rejected. A date is a better collision key but still does not say which plugin/scope the workflow belongs to, and it still encourages chronology to masquerade as workflow identity.

### C. Put every affected plugin/repository in the task key

Rejected. Broad tasks like current 056 would produce long, unstable keys and would need renaming when a repo becomes read-only or a supporting plugin is removed. Scope detail belongs in the frozen Plan.

### D. Make GitHub Issues the canonical workflow identity

Rejected for now. It would add an external tracker dependency and another source of truth. Current repo-local Reviewed Handoff already has durable task identity; the problem is the naming convention, not absence of a tracker.

### E. Add an ACTIVE_WORK registry/dashboard

Rejected by default. It would become another state surface that can go stale and would duplicate CURRENT/branches. Semantic branch/task names should solve most of the human discoverability problem without creating a ledger. If later real usage proves branch/task discovery still inadequate, that should be a separate evidence-backed proposal.

### F. Change only AI_Skills validators and ignore Bridge Kit

Rejected. Bridge Kit currently owns and enforces the task-key regex across repos. A local fork would violate the existing ownership boundary and create inconsistent task identities.

## 8. Red-team risks

### Risk 1 — semantic key collisions

Two new tasks might independently choose the same key.

Mitigation: creation fails if the task directory/branch identity already exists. Planner must make the goal slug more specific; do not append an arbitrary sequence number merely to bypass collision.

### Risk 2 — `cross-plugin` becomes a vague bucket

A broad task could hide unclear ownership behind one generic key.

Mitigation: every cross-plugin Proposal/Plan must list affected plugins, identify domain owner(s), and distinguish mutable vs read-only supporting repos. Critic should reject “cross-plugin” when the work is actually one plugin plus incidental references.

### Risk 3 — current 055/056/057 workflows break during cutover

Mitigation: no rename and no migration. Bridge validation becomes dual-format; creation becomes semantic-only. Existing active tasks finish under their original identities.

### Risk 4 — risk-based regression selection becomes an excuse to skip old capability

Mitigation: all release-critical gates still require same-final-candidate direct evidence; uncertain/cross-cutting impact falls back to broad/full release matrix. Narrow selection must explain why omitted cases are redundant or unaffected.

### Risk 5 — regression bank grows without bound

Mitigation: deduplicate only when cases prove the same failure mechanism and removing one does not erase a distinct input family, should-not-change boundary, or prior real failure. Cheap automated cases can remain numerous; expensive qualitative cases are represented by bounded release selection.

### Risk 6 — gate taxonomy freezes too early

Mitigation: stable does not mean immutable. New product capability can create a gate; genuine duplication can merge gates. The restriction is against accidental gate inflation or convenience deletion, not against evidence-based redesign.

### Risk 7 — path grouping creates unnecessary churn

Mitigation: only new tasks adopt it, and Critic may remove this subproposal while keeping semantic keys. No legacy artifact migration is required.

## 9. Capability Gate Matrix for this redesign

These gates describe what a future implementation would have to prove. They are design gates, not current PASS.

| Gate | Capability / claim | Normal entry & evidence | Failure | Final candidate / regression boundary |
| --- | --- | --- | --- | --- |
| G1 Semantic identity | A new Reviewed Handoff task can be created with a human-readable semantic key and no numeric prefix | canonical Bridge task creation + validation using a semantic key such as `plugin-writing-style--...` | creation still requires a number; local-only parser hack | exact Bridge final candidate |
| G2 Identity propagation | The same semantic key survives task dir, result dir, branch, CURRENT, review evidence and task-bound runtime without remapping | end-to-end reviewed-handoff fixture/smoke across normal paths | any consumer truncates/rejects/remaps it | exact final candidate; existing task identity semantics preserved |
| G3 Scope clarity | Single-plugin tasks bind the canonical plugin slug; cross-plugin/cross-repo tasks expose affected owners without bloating the key | representative single-plugin, cross-plugin and cross-repo task plans reviewed by normal Planner/Critic entry | key is human-readable but owner/scope remains ambiguous | AI_Skills policy + workflow-core final candidate |
| G4 Legacy compatibility | Existing 001–057-style tasks still validate and continue without rename | legacy fixtures and at least one existing Reviewed Handoff task replay | migration required; old result/evidence path invalid; legacy creation silently continues | validation accepts legacy; new creation semantic-only |
| G5 Gate lifecycle | A new real failure is normally added to an existing capability gate's regression bank, while genuinely new capability can add a gate and retirement cannot erase obligations | policy examples + representative triage cases | every failure adds a top-level gate; or gates can be deleted for convenience | AI_Skills policy final candidate |
| G6 Release regression safety | Mature plugins can use impact-based regression depth without losing same-final-candidate gate coverage | affected-gate case, unaffected-canary case, and uncertain-impact full-fallback case | old candidate PASS substitutes for final candidate; “unaffected” asserted without basis | workflow-core/maintainer final candidate |
| G7 No governance bloat | The redesign does not add a new registry, tracker, watcher, state machine, or mandatory ceremony for small tasks | source diff + normal small-task replay | ACTIVE_WORK ledger, duplicated parser, new controller/state appears | should-not-change across Bridge + AI_Skills |

## 10. Proposed implementation sequence after Critic PASS

This section is not authorization to execute.

### Phase A — Bridge Kit semantic task-key support

- update the canonical task-key parser/validator to distinguish legacy and semantic keys;
- new creation: semantic only;
- existing workspace validation: semantic + legacy;
- update tests, templates/examples and branch/task identity documentation;
- do not rename any existing task;
- verify normal Reviewed Handoff consumers accept the new key.

Because this changes Bridge Kit production behavior, a real implementation Plan must follow Bridge version/release rules and current user authorization boundaries.

### Phase B — AI_Skills policy and consumer alignment

- amend `PLUGIN_CAPABILITY_GATE_POLICY.md` with lifecycle/regression-bank/final-candidate selection rules;
- amend only the minimum AGENTS / Planner / workflow-core / AI Skills Maintainer surfaces that actually consume the new rule;
- update tests/examples for single-plugin and cross-plugin task identity;
- adopt semantic keys only for **new** tasks after the cutover;
- optionally adopt the new task-local design-doc grouping if Critic approves it.

### Phase C — normal-entry validation

- create one safe non-production semantic-key Reviewed Handoff fixture/task in an isolated test context;
- validate task directory, branch naming, status/review evidence and legacy coexistence;
- validate gate-lifecycle examples against at least one single-plugin and one cross-plugin release plan;
- do not use 055/056/057 as migration targets.

## 11. What this proposal deliberately does not do

- no production edits in this design round;
- no new Reviewed Handoff state;
- no new schema/ledger/controller/watcher;
- no renaming of 001–057 or active branches/results;
- no new GitHub Issue/Project dependency;
- no automatic gate deletion;
- no weakening of same-final-candidate requirements;
- no rule that every release must run every historical expensive/manual case;
- no rule that every new real failure creates a new gate;
- no attempt to make AI Skills Maintainer a domain expert;
- no duplicate task-key parser in AI_Skills.

## 12. Questions the Critic must resolve

1. Is the “stable gate taxonomy + growing regression bank + risk-based release selection + full fallback when uncertain” model strong enough to prevent regression without turning mature plugins into ever-growing manual gate matrices?
2. Is the proposed narrow-vs-full release selection too permissive? If so, what is the minimum stronger rule that does not require every historical qualitative/paid case every release?
3. Is the semantic task-key format simple enough and expressive enough? Are the four scopes `plugin-<slug>`, `cross-plugin`, `repo`, `cross-repo` sufficient, or do they create ambiguity?
4. Is current 056 correctly conceptualized as `cross-plugin--product-delivery-discipline` with Bridge as a supporting mutable repo, or would a different primary-scope rule be clearer?
5. Should new design artifacts be grouped under `docs/design/<task_key>/`, or is that unnecessary churn beyond the user's naming problem?
6. Is Bridge Kit truly the correct owner for semantic task-key syntax given the current hard-coded regex and cross-repo Reviewed Handoff behavior?
7. Is AI Skills Maintainer the right owner for gate lifecycle / plugin-scope maintenance, with workflow-core limited to execution semantics and target plugins retaining domain judgment?
8. Does the proposal preserve legacy tasks strongly enough without letting the old numeric pattern remain the default forever?
9. Is any part of this design over-engineered, and can it be removed without reintroducing the user's two concrete problems?
10. Is any part under-specified enough that implementation would likely recreate opaque identities, gate inflation, or regression holes?
