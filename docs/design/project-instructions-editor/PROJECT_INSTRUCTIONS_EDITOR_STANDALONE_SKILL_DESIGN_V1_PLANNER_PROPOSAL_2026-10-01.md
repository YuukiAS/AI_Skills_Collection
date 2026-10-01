# Project Instructions Editor — Standalone Skill Design Planner Proposal v1

Date: 2026-10-01  
Status: DRAFT_FOR_CRITIC_REVIEW  
Repository: `YuukiAS/AI_Skills_Collection`  
Source branch: `main`  
Planning source observed at start: `dca916441b322202b078d6b9159d7e89744c4bbe`  
Latest `main` before this proposal write: `5329d2efb4bbd108e930a8528d09d5668ea3ce15`  
Tracking: #93  
Design topic: `project-instructions-editor--standalone-skill-design`  
Candidate future standalone Skill: `project-instructions-editor`

```text
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```

This is a new major product/design round. It does not continue the prior AI Research Stack Section 0 wording refinement and does not authorize implementation, packaging, Plugin creation, trigger evals, README/version/registry/catalog/Marketplace/profile/release changes, or installation.

## 1. Product decision

The standalone Skill remains worth designing.

The reusable capability is not “make Project instructions prettier” and not “make Chinese prose more natural.” It is a bounded editor for a long-lived ChatGPT Project instruction surface. Its core job is to reconcile the actual live Project setting, relevant Project history, current canonical project sources, the user's present edit request, and the active character budget, then decide what should stay resident in Project instructions, what should become a locator to a canonical source, what should remain task-local, and what should not be changed.

The strongest evidence for a separate capability is that the same failure class has appeared in at least two materially different Project families:

1. a shared STAT5050/STAT5060 Project where a local addition caused scope imbalance, over-specification, copied workflow detail, and budget pressure;
2. AI Research Stack, where stale repository candidates could overwrite a newer live Project setting and where repeated local readability tuning showed diminishing returns.

These are not primarily prose-style failures. They are authority, placement, history, scope, budget, and edit-boundary failures.

A standalone Skill is the smallest reusable product surface that matches this problem today. It does not need a Plugin, daemon, state machine, database, persistent ledger, or new control plane.

## 2. Recalibrated problem set

The future Skill should solve seven connected decisions.

### 2.1 Baseline identity

The live Project setting is the edit baseline. Repository candidates, reference snapshots, old summaries, and old chat outputs are evidence only.

If the exact live setting cannot be obtained, the Skill must not produce a “safe full replacement” claim. It may provide bounded advice, a proposed local clause, or a request for the current setting, but it must state that full replacement safety is unverified.

### 2.2 Authority reconciliation

Project instructions sit between several authorities:

- the user's current request;
- the actual saved Project setting;
- explicit prior user decisions and corrections in Project history;
- canonical repositories and project sources that own current factual/process detail;
- global user instructions or other higher-level preferences;
- old candidates and summaries.

The Skill must reconcile these rather than letting the newest or longest source dominate.

### 2.3 Knowledge placement

A useful instruction can still be in the wrong place.

The editor must decide whether a semantic rule belongs:

- permanently in the Project setting;
- as a short trigger/locator to a canonical source;
- in a task-specific prompt or temporary thread context;
- in a global/user-level preference layer rather than this Project;
- nowhere, because it is redundant, obsolete, rejected, or unsupported.

### 2.4 Bounded mutation

The default is to protect the existing valid setting and make the smallest sufficient edit.

A local request is not blanket authority to rebalance the whole Project, delete unrelated rules, revive rejected rules, or rewrite the Project around the most recently discussed scope.

### 2.5 Semantic preservation

Compression, reorganization, translation, and locator substitution must preserve the meaning of governance rules, especially:

- mandatory versus optional;
- trigger and escalation conditions;
- permissions and authorization;
- safety boundaries;
- evidence strength and completion claims;
- role ownership;
- uncertainty and negative conclusions;
- exact machine/formal identities where exactness is functional.

### 2.6 Character-budget allocation

The budget is not a cosmetic target. It changes what should be resident.

The editor should optimize long-term semantic density and maintainable headroom, not line count or raw brevity. The roughly 8,000-character target observed in prior work is a real project constraint, not a universal ChatGPT limit.

### 2.7 Reviewable delivery and effect attribution

The user should be able to see what changed and why without diffing two long settings manually.

When evaluating whether a setting change improved behavior, source/ref changes must be separated from setting effects. The same or equivalent task should use frozen source state where possible.

## 3. Boundary with existing Skills and Plugins

### 3.1 `chinese-prose`

`chinese-prose` owns natural Chinese reader-facing expression. It decides how a Chinese document or explanation should read after the intended meaning is fixed.

It should not own:

- which Project rules deserve permanent residence;
- history reconciliation;
- canonical-source placement;
- multi-scope budget allocation;
- bounded-versus-full edit selection;
- whether a live Project setting can safely be replaced.

When a Project-instruction deliverable is Chinese, `project-instructions-editor` may use `chinese-prose` as a wording/final-readability helper, but the new Skill remains the semantic-placement owner.

### 3.2 `writing-fidelity`

`writing-fidelity` is the closest guardrail, because it protects facts, corrections, exact spans, version authority, and artifact identity.

It still does not solve the main Project problem. It assumes an editing task already has a source and protected content; it does not decide which of multiple live/history/repository sources is authoritative for Project-setting placement or which content should be moved behind locators to save budget.

The future editor should reuse fidelity principles rather than duplicate them. In particular, semantic invariants and explicit user corrections are guardrails for the edit, not a second copy of `writing-fidelity`.

### 3.3 `scientific-rewrite`

`scientific-rewrite` is a heavy source-faithful structural rewrite route for scientific/technical material. Its unit of work is a reader-facing scientific document with a content/evidence graph.

Project instructions are a different artifact. Their main difficulty is long-term authority, routing, persistence, scope, and budget. The Project editor should not import the Meaning Map / Reader Plan workflow or scientific rewrite machinery.

If a Project setting contains a long scientific document, that is usually evidence that the setting is overfilled; the editor should prefer moving that material to its canonical source rather than running a scientific-document rewrite inside the setting.

### 3.4 `workflow-core`

`workflow-core` owns process for complex/risky work: source discovery, phase ownership, routing, gates, evidence, and completion semantics.

It does not own the content architecture of a Project setting. A future `project-instructions-editor` task may be coordinated by `workflow-core` when the edit is complex or high risk, but the editor remains the specialist that decides instruction placement and mutation scope.

### 3.5 `ai-skills-core`

`ai-skills-core` owns maintenance of AI_Skills_Collection itself: source authority, generated parity, replay/regression, versions, changelogs, registry/catalog/Marketplace/profile and release closure.

It is relevant when this candidate is later implemented or released. It is not a runtime dependency for an ordinary user editing a Project setting.

### 3.6 Why this is not duplicate construction

The separation is:

- writing Skills: how preserved meaning becomes good reader-facing text;
- fidelity Skill: what an edit must not corrupt;
- workflow core: how complex work is routed, verified, and closed;
- AI Skills Maintainer: how AI_Skills source/release maintenance is performed;
- Project Instructions Editor: what belongs on the long-lived Project instruction surface, which authority controls it, and how that surface is safely changed under a finite budget.

That boundary is distinct enough to justify a standalone Skill.

## 4. Input model

The Skill should reason over five primary inputs and one derived Project map. It should not require a new persistent schema or ledger.

| Input | Requirement | Preferred acquisition | Missing-input behavior |
|---|---|---|---|
| Actual live Project setting | Required for exact editing, deletion, full replacement, or “safe to paste” output | Current Project instruction surface when actually exposed; otherwise exact user-provided text/export | No full replacement claim. Give bounded advice/local clause only and request the live text only when needed to proceed safely. |
| Relevant Project history | Required to attempt for full rewrite, deletions, disputed rules, or tasks explicitly about prior decisions; best-effort for simple additive bounded edits | Relevant Project chats/context/history tools when available; user-provided decision excerpts if not | Do not claim exhaustive history. Preserve unrelated live rules by default. If the requested edit could revive/delete a disputed rule, stop that mutation until the decision can be resolved. |
| Canonical project sources | Required when the setting refers to repo-owned ownership, policy, workflow, current status, or other time-varying facts | Current bound branch/ref via repository connector/local checkout; Project sources for non-repo canonical docs | Do not invent current rules. Preserve the live setting unless the user requested synchronization; flag the unresolved source locator. |
| Current edit request | Always required | Current user message | Defines the desired mutation, but does not silently authorize unrelated restructuring. |
| Instruction budget | Required for any “fits within budget / enough headroom” claim; otherwise optional | User-provided planning target, product-exposed limit when actually available, or explicit project constraint | Always report current length and edit delta when live text exists. If the maximum is unknown, do not claim compliance with a hard limit. |
| Derived Project scope/authority map | Derived, temporary analysis | From the five inputs | Not persisted as a database/state machine. Used only to decide the current edit. |

### 4.1 Live-setting acquisition rule

“Current Project context exists” is not automatically proof that the exact saved setting is available byte-for-byte.

The Skill may use the live setting directly only when the current surface actually exposes it with enough fidelity to edit. Otherwise it must ask for or receive the exact text before producing a complete replacement.

### 4.2 History acquisition rule

The Skill should search only the history needed to answer the current edit question. It should not perform an unbounded Project-history audit.

Relevant history includes:

- explicit acceptance;
- explicit deletion/rejection;
- repeated correction;
- durable preference;
- prior decisions that define scope ownership or authority;
- evidence that a rule was intentionally temporary.

Recency alone is not authority. Within the same scope and authority class, a later explicit user decision normally supersedes an earlier one; an incidental later mention does not.

### 4.3 Canonical-source acquisition rule

Use canonical sources for details they own. Do not copy a large workflow into Project instructions merely because it is important.

A Project setting should usually retain a short trigger such as “when X happens, read current Y” when:

- Y is stable enough to locate;
- Y is expected to evolve;
- the full rule is too detailed for permanent Project context;
- the rule can be retrieved before the action it governs.

A Project setting should retain the full semantic rule when it must constrain behavior before any locator/source lookup, especially ownership, authority, safety, or a cross-task response contract.

## 5. Core editing decision model

The editing model should be semantic and compact. It is a reasoning sequence, not a new workflow engine.

### Step 1 — Establish the baseline

Identify the exact live setting and current character count. Mark whether the maximum budget is known, user-defined, product-exposed, or unknown.

### Step 2 — Reconcile authority

For every rule affected by the request, determine:

- who owns the decision;
- whether it is still current;
- whether the user explicitly accepted, rejected, or changed it;
- whether the canonical source has moved;
- whether a conflict is local or cross-cutting.

Do not infer “accepted” merely because a rule appears in an old candidate.

### Step 3 — Decide placement

For each affected semantic unit, use these placement questions:

1. Does this rule need to apply across many future chats in this Project?
2. Must it constrain behavior before any source lookup can happen?
3. Is the detailed rule already recoverable from a stable canonical locator?
4. Is it volatile, branch/version/task-specific, or likely to change?
5. Does it really belong at account/global level instead of this Project?
6. Does an equivalent Project-level rule already exist?

The resulting disposition is one of:

- keep/add directly in Project setting;
- keep only a short trigger/locator;
- leave in task/thread context;
- leave with another authority layer;
- remove/avoid because it is redundant, obsolete, rejected, or unsupported.

These are current-edit dispositions, not persistent states.

### Step 4 — Select mutation radius

Default to bounded edit. Expand only when a local patch cannot satisfy the request without producing a known contradiction, budget failure, or scope distortion.

### Step 5 — Protect invariants

Before drafting, identify the nearby semantics that must remain unchanged. This includes explicit user corrections and all relevant governance-strength dimensions.

### Step 6 — Fit the budget without semantic laundering

Prefer removing duplication, replacing copied detail with locators, and consolidating genuinely shared rules.

Do not make room by silently weakening a mandatory rule, deleting a caveat, removing a scope, or translating an exact identifier into an ambiguous label.

### Step 7 — Produce a reviewable edit

Show the user the substantive change, its reason, what was intentionally preserved, the character effect, and a complete clean setting when a complete setting is safe to provide.

## 6. Character-budget strategy

The Skill must not encode 8,000 characters as a universal product constant.

For each edit, distinguish:

- current length;
- requested/known maximum, if any;
- target working budget, if the user/project has one;
- desired reserve/headroom, if specified or needed;
- edit delta;
- remaining margin after the candidate.

If only current length is known, the Skill can optimize density and report the delta, but cannot claim “within the product limit.”

### 6.1 What deserves permanent budget

Higher-priority residents usually include:

- durable Project scope and purpose;
- ownership and routing;
- authority and permission boundaries;
- safety/privacy/distribution constraints;
- evidence and completion principles;
- durable product/research philosophy;
- genuinely Project-specific response rules that must apply broadly;
- short locators/triggers to detailed canonical sources.

Lower-priority residents usually include:

- step-by-step SOPs already in the repo;
- build commands and detailed tool inventories;
- current branch/job/version status;
- copied review checklists;
- time-varying facts;
- one thread's implementation details;
- examples that only demonstrate a rule already stated.

This is a semantic priority ordering, not a fixed percentage allocation.

### 6.2 Headroom rule

Do not fill the setting to a hard maximum merely because a candidate fits.

Headroom should remain project-specific. If the user has not specified a reserve, the editor should avoid unnecessary expansion and report the resulting margin rather than inventing a universal reserve percentage.

If a small requested addition would require deleting unrelated material merely to fit, that is evidence that the current surface may need a broader compression/restructure decision; do not silently perform it.

## 7. Bounded edit versus full rewrite

### 7.1 Bounded edit is the default when

- the user asks for a local addition, deletion, correction, or wording change;
- the live setting is available;
- the affected rule can be changed without touching unrelated authority;
- the change fits the working budget or can be accommodated by local deduplication;
- no cross-scope contradiction is discovered;
- existing structure is still usable.

The bounded edit may still replace a copied detailed block with a locator if that block is directly in the requested scope and the semantic meaning remains intact.

### 7.2 A full rewrite/restructure may be proposed when

- the user explicitly asks for a full rewrite;
- the setting has cross-cutting contradictions that cannot be repaired locally;
- copied detailed workflows are pervasive enough that local edits would preserve an incoherent architecture;
- multiple scopes are materially imbalanced and the requested change cannot be made safely without reallocation;
- the current budget cannot accommodate the requested durable semantics without global deduplication/relocation;
- source ownership has drifted so widely that several sections point to stale or conflicting authorities.

A full rewrite is not justified merely because the editor can make the prose cleaner.

### 7.3 A full rewrite is blocked when

- the exact live setting is unavailable;
- relevant prior accept/delete decisions are known to be disputed but unresolved;
- canonical sources needed to resolve governance facts cannot be reached;
- the user asked only for a local edit and the wider rewrite would change unrelated semantics without necessity.

In those cases, return the safe bounded result or a clearly scoped rewrite proposal, not an invented replacement.

## 8. Priority relationship among current request, history, repo, and live setting

These inputs have different roles rather than a single simplistic ranking.

1. **Current user request** defines what change is being asked for now and any new explicit decision.
2. **Live Project setting** is the concrete baseline that must be preserved outside the authorized change.
3. **Relevant explicit Project history** interprets durable accepted/rejected decisions and prevents resurrection or accidental loss.
4. **Canonical current sources** own repo/document facts and detailed rules that belong outside the Project setting.
5. **Old candidates, references, summaries, and prior generated settings** are supporting evidence only.

Conflict rules:

- If the current explicit request changes a live rule, apply that requested change.
- If history shows the user explicitly deleted/rejected a rule, an old candidate cannot restore it.
- If the live setting contains a repo-owned factual detail that is stale, do not silently rewrite unrelated sections; either update it when the current request includes synchronization or report the contradiction.
- If a canonical repo rule is long and retrievable, prefer a stable locator over duplicating it in Project instructions.
- A recent thread does not gain more Project budget simply because it is recent.
- A newer explicit decision within the same scope/authority normally supersedes an older one; mere recency without explicit decision does not.

This prevents both extremes: “live setting is always truth even when the user just changed the rule” and “latest chat overrides everything.”

## 9. User delivery forms

The Skill should have proportional outputs.

### 9.1 Small bounded edit

Default compact delivery:

- one-paragraph structural/semantic judgment;
- exact bounded change, with removed and added wording clearly distinguishable;
- one short reason per substantive change;
- character count before/after and delta;
- one sentence stating important semantics intentionally preserved;
- complete clean Project setting ready to copy, but only when the live baseline was actually available.

No large audit package.

### 9.2 Medium edit

Add only what the risk requires:

- scope impact;
- locator substitutions;
- any cross-scope balance change;
- concise invariant check;
- budget margin.

### 9.3 Full rewrite candidate

Provide:

- why bounded editing was insufficient;
- major content moved to locators/task-local/global layers;
- substantive delete/add/move summary;
- explicit preservation of authority/safety/evidence/role semantics;
- before/after character count and known budget margin;
- complete clean replacement setting;
- a small regression plan when behavior should be checked before adoption.

### 9.4 No-change outcome

“No Project-setting change” is a valid result when:

- the requested behavior is already covered;
- the detail belongs only in a canonical repo source or task prompt;
- the proposed addition would duplicate a locator-backed rule without adding durable control value.

The editor should explain where the requested information belongs instead of manufacturing a change.

## 10. Real acceptance design

The future Skill should be evaluated on real editing behavior, not keyword counts or document shape.

### Case A — stale repository candidate versus newer live setting

Use the AI Research Stack regression where the repository candidate is older than the saved Project setting.

Required behavior:

- use the live setting as baseline;
- preserve later accepted governance;
- treat the stale candidate as evidence only;
- make only the requested edit.

Failure: the candidate silently reverts newer live rules.

### Case B — multi-scope Project under a finite budget

Use the shared STAT5050/STAT5060 Project evidence.

Required behavior:

- keep both scopes represented according to durable role, not recency;
- lift genuinely shared rules;
- move detailed course workflows behind canonical locators where possible;
- stay within the actual project planning budget when that budget is supplied;
- preserve headroom without inventing a universal target.

Failure: recent scope dominates or the editor merely shortens text while preserving structural over-specification.

### Case C — rejected/deleted rule resurrection

Freeze a setting/history pair where the user explicitly removed a rule but an older candidate/source still contains it.

Required behavior: do not restore it unless the user explicitly changes that decision.

### Case D — exact identity and ordinary language separation

Use a setting containing paths, repository names, commands, fields/state tokens, plus ordinary descriptive terminology.

Required behavior:

- preserve exact identities when functional;
- allow ordinary explanatory language to be rewritten naturally;
- keep governance strength unchanged.

This case may invoke `chinese-prose` for final Chinese wording, but the pass condition belongs to the Project editor's placement/identity decision.

### Case E — source-drift-controlled behavior regression

When comparing two Project settings:

- freeze the relevant repo/source commit or Project source snapshot;
- use the same or genuinely equivalent task;
- keep the user prompt neutral rather than telling it the intended output style;
- attribute source changes separately from setting effects.

Do not reuse a moving `workflow-core` proposal and then assign all answer changes to the Project setting.

### Case F — missing live setting

Do not provide a full replacement. Provide bounded advice and the minimum request needed to obtain the live baseline if an exact edit is required.

### Case G — no-op / should-not-change

Ask for an addition already covered by a valid Project rule or canonical locator.

Required behavior: recommend no change or a very small clarification; do not expand the setting simply to demonstrate activity.

### Case H — language-independent placement check

Before eventual release, include at least one Project where the main problem is authority/budget/scope rather than Chinese readability. This verifies that the Skill has not become a disguised Chinese-style editor.

The sample can be a real non-Chinese Project or a language-neutral real Project setting; do not invent a superficial English-count benchmark.

### Evaluation discipline

- Development regressions may reuse known failures.
- A final candidate should use frozen source/settings inputs.
- Reviewer criteria should separately inspect semantic preservation, placement quality, budget use, and actual downstream Project behavior.
- Natural-language quality requires qualitative review of the full output; character count/diff utilities prove only mechanics.
- Do not choose the best of many stochastic runs after seeing outputs.
- Do not keep adding rules once additional changes no longer produce a distinguishable benefit across representative tasks.

## 11. Non-goals

The standalone Skill is not:

- a Chinese prose polisher;
- an English blacklist or translation dictionary;
- a Project-setting linter based on keyword counts;
- a style score;
- a character-ratio or English-ratio gate;
- a fixed paragraph/title/formula counter;
- a generic prompt optimizer;
- a repository policy generator;
- a replacement for canonical README/AGENTS/policy/Goal/TODO;
- a Project-history database;
- a decision ledger;
- a watcher, daemon, scheduler, or background sync service;
- a new Planner/Critic state machine;
- a GitHub Project synchronization service;
- a Plugin packaging/release tool;
- a mechanism for silently rewriting global user instructions.

It should not encode real regression examples as banned-word or replacement tables.

A deterministic helper, if implementation later proves useful, may mechanically count characters or render a diff. It must not make semantic keep/delete/translate decisions.

## 12. Simpler alternatives considered

### Alternative A — keep doing manual Project-setting edits

This is the simplest possible approach and remains reasonable for a single, rarely edited Project.

It is insufficient for the current evidence because the failure now recurs across different Projects and involves stale live/repo divergence, history, scope allocation, budget, and locator decisions that are easy to repeat incorrectly.

Decision: not selected as the only long-term mechanism.

### Alternative B — extend `chinese-prose` or `writing-fidelity`

This avoids a new Skill, but it would broaden writing Skills into Project-context authority and persistence management. Their trigger boundaries would become less coherent, and ordinary writing tasks would inherit unnecessary Project-governance logic.

Decision: reuse them as helper/guardrail capabilities, do not make either the owner.

### Alternative C — maintain a repository checklist/template only

A checklist can encode “get live setting, check history, prefer locators, count characters.” It cannot itself reconcile the actual live Project setting and history during a user edit. It also encourages users to manually execute a multi-source process that the Skill can reason through.

Decision: useful as internal reference material later, but insufficient as the user-facing capability.

### Selected minimal architecture

Create, after future Critic approval and explicit implementation authorization, one standalone Skill whose core is semantic reasoning over the live setting/history/canonical sources/request/budget.

Do not create a Plugin or new service.

Use existing connectors/tools when available. Degrade honestly when they are not.

Reuse `writing-fidelity` and `chinese-prose` instead of copying their content. Use `workflow-core` only when the surrounding task is complex/risky enough to need its process gates. Use `ai-skills-core` only for later repository implementation/release maintenance.

## 13. Risks and recovery boundaries

### Risk: live setting is assumed but not exact

Recovery: downgrade to advice/local clause; do not generate a full replacement.

### Risk: history retrieval is partial

Recovery: avoid deleting or restructuring unrelated live rules; identify the disputed decision and request only the missing evidence needed to resolve it.

### Risk: canonical repo cannot be read

Recovery: do not invent current policy. Preserve the live setting and mark the locator/fact as unverified.

### Risk: character maximum is unknown

Recovery: report current length/delta and density improvements without claiming product-limit compliance.

### Risk: full rewrite becomes a style rewrite

Recovery: return to semantic placement and preservation checks; use writing Skills only after the Project-level content decision is fixed.

### Risk: acceptance overfits one Project or one prompt

Recovery: freeze source refs, use multiple task families, include a no-op/should-not-change case, and stop micro-tuning when marginal benefit is not identifiable.

## 14. External product facts checked this round

Targeted official OpenAI documentation was checked on 2026-10-01.

Current official Projects documentation states that Projects keep related chats, files, and instructions together; Project instructions apply only in that Project and override global custom instructions. It also documents Project memory options and that Project chats can use Project context/history depending on memory mode and available context.

The current official Projects documentation inspected in this round does not publish a universal Project-instruction character limit. This proposal therefore treats character budget as an input from the active Project/user/product surface when actually known, not as a hardcoded 8,000-character product constant.

Sources checked:

- OpenAI Help Center, “Projects in ChatGPT”: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI Academy, “Using projects in ChatGPT”: https://openai.com/academy/projects/
- OpenAI Help Center, “Memory in ChatGPT”: https://help.openai.com/en/articles/8590148-memory-in-chatgpt

Adoption decision: use these sources only to bound the product assumptions above. They do not imply that a Skill can programmatically enumerate all history or read the exact saved Project-setting text on every surface.

## 15. Tracking and maintenance actions

Canonical source TODO already contains `tracking: #93`.

This proposal is the new design anchor for Issue #93.

Current GitHub connector supports repository/Issue mutation but exposes no GitHub Project field mutation surface.

Exact pending Project mutation:

- ensure Issue #93 is present in the `AI Skills Maintenance` Project;
- Project Status = `DOING`;
- Project Area = `standalone-skill`;
- current design anchor = `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V1_PLANNER_PROPOSAL_2026-10-01.md`.

The Issue body is reader-facing copy. `AI_SKILLS_MAINTENANCE_BOARD.md` requires a real current Clear Writing invocation before a substantive Issue-copy rewrite. This Planner environment does not expose an installed Clear Writing invocation surface, so the Issue body must not be substantively rewritten in this round.

Exact pending Issue-copy mutation after Clear Writing is available:

- 问题：候选 standalone Skill 需要安全编辑长期 ChatGPT Project instructions，核心是 live setting + history + canonical sources + budget，而不是中文润色。
- 当前进度：Standalone Skill product/design Proposal v1 已完成，等待独立 Critic。
- 当前执行锚点：本 Proposal 路径。
- 下一步：Critic 审查 standalone Skill 是否值得成立、边界、输入缺失降级、bounded/full rewrite 边界、budget 语义和真实验收设计。
- 保留 `READY_FOR_SKILL_IMPLEMENTATION=NO`.

## 16. Critic review request

The Critic should decide whether this v1 product architecture is sufficiently bounded and distinct to continue future Skill design.

Critical review questions:

1. Is a standalone Skill genuinely justified, or should this remain a checklist/helper inside an existing writing Skill?
2. Does the input model correctly block unsafe full replacement when the live setting is unavailable?
3. Is Project-history use strong enough to protect accepted/deleted decisions without requiring an impossible exhaustive history audit?
4. Does the authority relationship avoid both “live setting always wins” and “latest thread always wins”?
5. Is locator substitution constrained enough to avoid moving safety/authority rules out of Project context prematurely?
6. Is the budget strategy useful without inventing a universal limit or fixed allocation percentages?
7. Are bounded/full rewrite boundaries strict enough to prevent scope creep?
8. Are `chinese-prose`, `writing-fidelity`, `scientific-rewrite`, `workflow-core`, and `ai-skills-core` responsibilities non-overlapping in practice?
9. Does the acceptance plan test real user behavior and source-drift attribution rather than surface metrics?
10. Is any component unnecessarily heavy, especially history handling, transient semantic classification, or delivery requirements?

A PASS on this proposal would authorize only further design/refinement and preparation for a later implementation plan. It does not authorize creating the Skill.

```text
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```
