# 056 Product Delivery Discipline — Implementation Plan

- Execution package version: `v0.3`
- Task key: `056_product_delivery_discipline`
- Status: `READY_FOR_POST_057_EXECUTION_CRITIC_REVIEW`
- Revalidation source: `AI_Skills_Collection main@f68e800fb604850c20a29cb3c7572e4f1a119236`
- Prior execution package: `v0.2`
- Prior v0.2 package source: `AI_Skills_Collection main@e8ba751561c9e61a5b0bbd094d2c280ff0b00b59`
- Current Bridge source: `GPT_Codex_AI_Bridge_Kit main@e1d6b781ad7e56d567bed419001069baf439d0a5`, formal source version `0.8.3`
- Current Bobbio reference: `develop@ab5dccb6b8b87c49671aa097233ce1bcc38be004` — read-only in 056
- Current Lucerna reference: `main@687752861b4859f7f24799b9e17d985afc992ad2` — read-only
- Current Mica reference: `main@e49416f874f633aedc7521734ee5b0f441aae970` — read-only
- Current Asteria reference: `main@0ce1d4daca1e410ce551570578dd563d4ef67e90` — read-only
- Current SeminarArc reference: `main@74caaa4ecec16f1bc90987979458d1a4e93f52be` — read-only
- Current CUHK Date reference: `main@e4fdba4d6e38f300d5aeb9861f7c944f07c61e3d` — read-only
- Architecture authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- Post-probe authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- Probe result: `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`
- CUHK Date evidence: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`
- Post-057 drift audit: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_POST_057_SOURCE_DRIFT_REVALIDATION_2026-09-18.md`
- Canonical Goal: `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.3
- Kickoff Draft: `docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.3

This is a bounded post-057 amendment. It does **not** reopen the approved v6 architecture. It removes work already completed by 057, refreshes current source/version identity, and tightens the current execution authorization. Only an independent Critic PASS on this exact v0.3 Plan + Goal + Kickoff may make it eligible for the user to send the Kickoff.

## 0. Post-057 source-drift disposition

The detailed matrix is in the post-057 drift audit. The execution consequences are:

1. **AI_Skills production work remains valid.** Current production workflow/frontend/maintainer source and plugin versions are still pre-056.
2. **Bridge work remains valid, but the old version slot is stale.** 057 consumed `0.8.3`; 056's next distinct compatible candidate slot is `0.8.4`.
3. **Bobbio write scope is removed.** 057 already integrated the Figma locator and three-way visual-authority closure.
4. **Lucerna / Mica / Asteria / SeminarArc remain ZERO WRITE.**
5. **CUHK Date now has a root AGENTS**, but this does not change ownership: it remains ZERO WRITE / `NO_GENERIC_056_AGENTS_COPY`.
6. **C056-E1 / E2 remain Planner ACCEPT responses pending Critic closure.**
7. **No source drift contradicts v6.**

### Current source-drift matrix

| Area | v0.2 assumption | Current fact | Impact | v0.3 action |
| --- | --- | --- | --- | --- |
| AI_Skills | production implementation pending | production source still pending; 057/review/TODO docs advanced | AMEND | refresh refs, keep implementation; reconcile stale 056 TODO wording only |
| Bridge | `0.8.2 -> 0.8.3` | main is `0.8.3`; 057 scaffold/versioning/raw-byte behavior canonical | AMEND | preserve 057; target next candidate `0.8.4` |
| Bobbio | add Figma locator | locator/authority already canonical on develop | REMOVE | ZERO WRITE; read-only G6 reference |
| Lucerna | NO_WRITE | 057 hygiene + substantial unrelated product advancement | KEEP | ZERO WRITE |
| Mica | NO_WRITE | 057 consolidated testing/instruction surface canonical | KEEP | ZERO WRITE |
| Asteria | NO_WRITE | 057 map conversion canonical | KEEP | ZERO WRITE |
| SeminarArc | NO_WRITE | 057 safety-map conversion canonical | KEEP | ZERO WRITE |
| CUHK Date | no root AGENTS | root AGENTS now exists; project advanced independently | REVALIDATE -> KEEP | ZERO WRITE; no generic copy |

## 1. Execution-ready Critic findings remain pending closure

### C056-E1-HUMAN-GATE-BLOCKED-NOT-ACHIEVED — Planner disposition `ACCEPT`

Current upstream Codex was rechecked at `openai/codex@7498521d288b9b3b96ffba4eedf089d8d6e06a84`:

- the request-user-input handler still sets `is_blocking = mode == ModeKind::Plan`;
- Default collaboration guidance still reserves native `request_user_input` for optional questions and tells the agent to ask one concise plain-text question when explicit user input is required before safe progress.

The v0.2 response therefore remains correct:

```text
HUMAN_ONLY
-> preserve Goal / resume point / prompt identity
-> one concise plain-text question
-> stop dependent execution immediately
```

Waiting authority remains:

1. use any explicit human-response deadline/hard deadline/run-lifetime already frozen by the task/workflow;
2. otherwise, if the plain-text question ends the current interactive run/turn, run-end is the handoff boundary;
3. native card 60+60 auto-resolution is not transcript timeout authority;
4. External GPT Planner/Reviewer waiting remains a separate owner-wait contract.

At the boundary with no explicit answer:

```text
GOAL_BLOCKED=YES
GOAL_ACHIEVED=NO
COMPLETE=NO
READY_FOR_USER_REVIEW=NO
DEPENDENT_EXECUTION_BLOCKED=YES
```

Use an existing legal human-required/recovery machine state; do not invent a `BLOCKED` enum or second state machine. A later in-scope explicit answer resumes the **same Goal** exactly once after rereading the current Goal/resume point; it does not create a successor and human action itself is not completion.

Current `docs/plugin-todos/workflow-core.md` still contains one stale sentence saying no-reply is “not terminal BLOCKED.” During 056 implementation, reconcile that wording with the above distinction: recoverable **Goal blocked/achieved=no** is required at the boundary, while STOP/impossibility is not.

Planner does not declare C056-E1 closed; the independent Critic must do so.

### C056-E2-POST-REVISE-PASS-HUMAN-EXPLANATION — Planner disposition `ACCEPT`

Current `docs/workflows/CRITIC_ROLE_CONTRACT.md` remains v1.3 and retains the generic post-REVISE closure-explanation rule. No new reporting architecture is needed.

A final PASS in this 056 major round must first explain in normal Chinese how prior blockers were closed, what each affected/unaffected layer does, what G1-G8 prove, repo-specific dispositions, actual user-workflow changes, and what PASS does **not** prove. Machine fields / approved Kickoff follow after that explanation.

Planner does not declare C056-E2 closed.

## 2. Frozen architecture — no v7

Keep exactly:

```text
Lite baseline                6
workflow-core                W1-W5
Frontend Design              F-A / F-B / F-C
AI Skills Maintainer         1 production-consumption diagnosis capability
Bridge Kit                   transport / wait-resume / recoverability + Lite distribution
repo AGENTS                  project-specific invariant / locator only
Capability Gates             G1-G8
Source Discovery regression  existing capability, not G9
```

Do not add W6/W7, G9/G10, a second state machine, second review engine, Control layer, watcher, daemon, ledger, persistent orchestration, new top-level plugin, or Codex fork.

CUHK-Date-like delivery failures remain inside W1/W3/W5 and Frontend gates. No project-specific questionnaire/catalog/YuNet policy is promoted into generic workflow text.

## 3. Current write scope

### 3.1 AI_Skills_Collection — WRITE

After approved Kickoff only:

- exact execution branch: `reviewed/056_product_delivery_discipline`;
- base: kickoff-time latest `origin/main` that contains the approved v0.3 package and has no relevant production drift since this revalidation;
- preferred task-owned worktree: `AI_Skills_Collection-056-product-delivery-discipline`, derived from verified local canonical source;
- allowed: task-owned workflow-core / web-development / ai-skills-core source, references, tests, generator config, generated Marketplace payload, affected TODO/changelog/version/release metadata, and 056 evidence.

No main merge or release is authorized.

### 3.2 GPT_Codex_AI_Bridge_Kit — WRITE

After approved Kickoff only:

- exact execution branch: `reviewed/056_product_delivery_discipline`;
- expected base: current canonical `main@e1d6b781ad7e56d567bed419001069baf439d0a5`;
- if Bridge main advances before kickoff, stop and revalidate relevant drift rather than silently rebasing the frozen package;
- preferred task-owned worktree: `GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`;
- allowed: task-owned Host/Lite source, tests, docs, changelog/version-candidate metadata needed by the frozen 056 mechanism.

No Bridge main merge, tag, GitHub Release, package publish, deployment, or real user Host Policy installation is authorized.

### 3.3 Product repositories — ZERO WRITE

056 v0.3 writes **none** of:

- Bobbio;
- Lucerna;
- Mica-for-ChatGPT;
- Asteria;
- SeminarArc;
- CUHK Date;
- CARE/EAT;
- Server/VPS;
- Longleaf_Bridge;
- Scientific Visualization production.

They may be read as bounded regression/reference sources where a gate requires it. Executor has no discretion to “add one small 056 AGENTS rule.”

## 4. Existing Source Discovery

Keep the approved existing-capability refinement, with the 057 lessons inherited:

known repo -> find correct local canonical checkout/worktree/clone first -> verify identity/ref/origin/freshness/dirty ownership -> protect unrelated dirty work -> use authorized local isolation when needed -> network clone only when there is no usable local source.

Do not use “local clone then remote remap” as normal source discovery. Remote identity/mutation remains a separate boundary. Do not create a new Source Discovery capability number.

## 5. Phase 0 — Preflight and baseline

Before implementation:

1. verify AI_Skills and Bridge remote identity, current canonical refs, exact branch/worktree authorization, and unrelated dirty ownership;
2. re-read current source for every file to be mutated;
3. record installed plugin/runtime identities relevant to later replay without modifying the real host;
4. freeze public-safe G1-G8 + Source Discovery fixtures;
5. record current versions:
   - AI_Skills repo `5.0.4`;
   - workflow-core `0.1`;
   - web-development `0.1`;
   - ai-skills-core `0.2`;
   - Bridge `0.8.3`;
6. confirm read-only reference refs above still exist when used.

Old-candidate evidence cannot be stitched into a later changed final candidate.

## 6. Phase 1 — Bridge: preserve 057, implement remaining 056 Host/Lite behavior

### 6.1 057 behavior is should-not-change

The integrated 057 work is canonical and must not regress:

- fresh-repo `templates/repo/AGENTS_TEMPLATE.md` scaffold;
- existing-root project-owned raw-byte/newline preservation outside the managed block;
- exactly one canonical managed Bridge block;
- Lite fallback versioning in `templates/prompts/AGENT_RULES.md`;
- existing-repo `--force` must not migrate/reformat project-owned root prose;
- root scaffold must not duplicate Lite execution/versioning policy.

056 adds delivery discipline on top of these behaviors; it does not redo 057.

### 6.2 Default Host config fail-closed

Update the Bridge-managed desired state to:

```toml
[features]
default_mode_request_user_input = false
memories = true
```

Separate upstream capability/key presence from desired enabled state:

- supported + actual false + desired false -> configured;
- stale actual true -> drift;
- `memories` remains desired true;
- upstream key absent -> truthful unsupported/incompatible rather than “compatible because desired=false”;
- unrelated config preserved.

Current stale surfaces to align include at least:

- root `AGENTS.md`;
- `templates/host/CODEX_CONFIG_PROFILE.md`;
- `ai_bridge_kit/host.py`;
- `tests/test_host_policy.py`;
- any canonical Host validation output/docs that still claim the Default tool should be enabled.

### 6.3 HUMAN_ONLY transcript contract

Implement the C056-E1 semantics consistently in:

- Host guidance;
- Lite guidance;
- workflow-facing consumer surface where owned;
- tests/behavior fixtures.

Required path:

```text
HUMAN_ONLY recognized
-> preserve Goal/resume/prompt identity
-> one concise plain-text question
-> no dependent execution
-> explicit deadline/run-end with no answer => Goal blocked/achieved=no
-> later explicit valid answer => same Goal exact-once recovery
-> post-action closure
```

No polling, default inference, auto retry, timeout-continuation, duplicate prompt, successor creation, or fake ready/complete.

### 6.4 Host guidance

Revise `GLOBAL_AGENTS_SNIPPET` so it no longer says the Host Policy enables Default native request-user-input for required gates.

It must distinguish:

- while an active run can still legally wait, do not fail merely because asking is inconvenient;
- at HUMAN_ONLY deadline/run-end with no answer, the Goal is blocked/achieved=no;
- blocked-for-human remains recoverable and is not STOP/impossibility;
- External GPT Planner/Reviewer normal waiting remains unchanged.

### 6.5 Lite L1-L6

Add/align only the six frozen delivery baselines:

- **L1** positive goal / normal entry / no silent downgrade;
- **L2** Acceptance Review Admission + human action != acceptance;
- **L3** HUMAN_ONLY eligibility + visible plain-text question + resume point + blocked/achieved=no at deadline/run-end;
- **L4** faithful validation + evidence surface + final-candidate identity;
- **L5** no blind rerun + protect accepted/adjacent behavior;
- **L6** truthful handoff: complete/partial/unsupported/human-blocked/unverified are distinct.

Do not copy Figma/icon/provider/locale/full-E2E checklists into Lite. Preserve the 057 fallback versioning section.

### 6.6 Bridge tests and version identity

Focused tests must cover:

- desired Default flag false;
- merge/idempotency/unrelated config preservation;
- stale true -> drift;
- supported+false+desired false validation;
- missing upstream key truthful handling;
- `memories=true`;
- Host safety rules;
- L1-L6 normal Lite output;
- HUMAN_ONLY wording vs External GPT waiting;
- all 057 H7-H9 should-not-change behavior, especially raw-byte preservation and no Lite duplication.

Then run the Bridge full unit suite once on the stable implementation candidate.

**Version slot:** current `0.8.3` is already the canonical 057 identity. 056 must not reuse it for a distinct candidate. The next compatible candidate slot is `0.8.4`.

Intermediate implementation commits may remain unreleased under current repo versioning rules. When the task forms the next actual reviewed candidate, synchronize the formal `0.8.4` candidate identity across package/version/changelog/README surfaces exactly once. This does not authorize a tag, release, package publish or deployment.

### 6.7 No real Host install in this execution package

Current user authorization explicitly excludes a real Host install.

Therefore this Kickoff may run source/unit/fixture tests, including isolated temporary test fixtures used by the Bridge test suite, but must **not** mutate the user's real `$CODEX_HOME`, install/update real Host Policy, or execute a real-host `ai-bridge host install`.

The final release-critical real-host application / fresh-session G1 smoke is a later separately authorized integration step. Current implementation evidence must not be mislabeled as final real-host G1 PASS.

## 7. Phase 2 — AI_Skills central production refinement

### 7.1 Verified Workflow / workflow-core

Keep W1-W5 only.

**W1 — Acceptance Review Admission + Vertical/Post-action Closure**

Hard-gate acceptance/release/user-ready review only. Advisory/diagnostic/design/architecture review may occur earlier but cannot claim readiness. Use the task's applicable chain rather than a universal checklist:

source/contract -> runtime/backend -> state/persistence when applicable -> normal entry -> real target behavior -> failure/recovery -> targeted regression -> risk-matched actual surface.

HUMAN_ONLY blocked-for-human cannot pass admission. Recovery requires post-action closure before readiness is reconsidered.

For frozen breadth/locale/material-branch/state-lifecycle claims, retain the CUHK-derived representative-coverage rules. Fallback/recovery does not prove primary capability unless the frozen Goal explicitly treats it as equivalent.

**W2 — Human Decision Gate**

Classification remains:

`HUMAN_ONLY / AGENT_RESOLVABLE / UNSUPPORTED_WITH_EVIDENCE / OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE / SAFETY_OR_AUTHORITY_BLOCKER`.

Only HUMAN_ONLY enters the transcript gate. AGENT_RESOLVABLE is solved by the agent; unsupported interfaces close truthfully; optional work cannot replace a frozen required capability; safety/authority blockers use existing routes.

**W3 — Exact Failure / Verification / Evidence Fidelity**

Require focused real-failure evidence, claim scope <= evidence surface, and same-final-candidate proof. Mock provider proves only adapter behavior. Hosted/external claims require bounded configured-target evidence. Interaction transformations require sequence-level tests such as type/paste/backspace-replace/blur-commit.

**W4 — Repeat-failure Circuit Breaker + Human-time Budget**

A repeated same-class failure without new information stops another broad suite/GPT Work/human rerun. Recheck candidate, consumer, hypothesis, fixture, evidence surface and root cause first.

**W5 — Change-impact / Should-not-change**

Protect accepted/adjacent behavior. A rewrite/refactor cannot silently degrade a mature structured interaction to generic/free-text fallback without an explicit product decision.

**Current TODO consistency:** update the stale 056 TODO sentence that conflicts with E1's run-end Goal-blocked semantics. Do not absorb the later NEW task-local-expiry item, and do not pull the explicitly deferred post-056 acceptance-artifact item into this task.

### 7.2 Frontend Design / web-development

Keep exactly three production gates:

**F-A Design Authority & State Coverage**

When a canonical Figma/design source exists, consume it. Missing material state/variant/responsive/interaction requires design-source closure rather than code invention. No canonical design => do not force Figma.

**F-B Design-System Coherence**

Shared components/tokens/states; layout/typography/spacing/radius/surface; coherent icon family; brand/generic asset boundary; meaningful interaction feedback/motion; reduced-motion/accessibility. When the frozen claim includes multiple locales, finite reachable tokens/enums must be fully localized; internal identifiers cannot be production fallback except narrow approved proper-name/acronym cases.

**F-C Actual-Surface Convergence**

Use the real target surface, canonical-design comparison where applicable, risk-scaled visual/interaction regression, and producer self-QA before external acceptance. Screenshot alone does not prove click/native/live behavior.

**Production wiring remains required:** current web-development visual aggregate still omits standalone `figma-design-to-code` and `motion-interaction`. Update `scripts/codex_marketplace_config.json` source authority so the existing Frontend Design production payload consumes those existing skills, then regenerate canonically. Do not hand-edit generated plugin output or create a new plugin.

### 7.3 AI Skills Maintainer / ai-skills-core

Implement one production-consumption diagnosis capability:

active rule exists but real task still fails -> inspect installed version, source/generated parity, plugin invocation, trigger, task entry, session loading and normal-entry replay -> classify missing rule / not loaded / stale install / consumer not routed / unfaithful test / execution noncompliance / capability gap.

A source `SKILL.md` existing is not proof of production invocation.

### 7.4 Version/changelog closure

Current source remains:

```text
AI_Skills repository  5.0.4
workflow-core          0.1
web-development        0.1
ai-skills-core         0.2
```

If and only if the task forms the actual next candidate after its required replay/regression/closure, the approved next slots remain:

```text
Repository bump decision: PATCH
AI_Skills_Collection: 5.0.4 -> 5.0.5
workflow-core: 0.1 -> 0.2
web-development: 0.1 -> 0.2
ai-skills-core: 0.2 -> 0.3
```

No other plugin bumps. Pure planning/review docs do not bump versions.

Because this v0.3 execution explicitly stops before real Host integration/release, version metadata may be prepared on the task branch as the next candidate identity but no main release/publication is authorized. Overall 056 completion cannot be claimed until later required integration evidence is closed.

## 8. Product repos — read-only evidence only

### Bobbio

The former write phase is **deleted**. Current `develop@ab5dcc...` already contains the Figma locator and authority closure.

Bobbio may be read as the preferred G6 design-source fixture. No Bobbio file, Figma, product code, runtime, version, branch or commit may be changed by 056.

### Lucerna / Mica / Asteria / SeminarArc

Read only when a frozen gate needs a representative reference. Do not import their current product development into 056 and do not rewrite their AGENTS.

### CUHK Date

Current root AGENTS exists. Keep `NO_GENERIC_056_AGENTS_COPY`.

Historical Questionnaire V4 failures remain legitimate regression patterns for W1/W3/W5/Frontend. Current product improvements do not become 056 implementation scope.

## 9. Mechanical/source/generated verification

AI_Skills:

- focused unit tests for changed source;
- canonical generator;
- registry/catalog/Marketplace validation/audit;
- generated/source parity;
- plugin versions/changelogs/README/repository-version parity when candidate version metadata is formed;
- prove generated workflow-core/web-development/ai-skills-core payloads match source and Frontend production actually consumes Figma+motion capability.

Bridge:

- focused Host/Lite tests;
- full unit suite once after the candidate stabilizes;
- docs/source/version parity for the 0.8.4 candidate;
- preserve 057 raw-byte/scaffold/versioning behavior.

Mechanical tests prove only their surfaces; they do not replace G1-G8 behavior.

## 10. Candidate freeze for current implementation stage

Before independent implementation review, freeze the task-branch implementation tuple:

```text
AI_SKILLS_IMPLEMENTATION_CANDIDATE_COMMIT=<sha>
AI_SKILLS_GENERATED_PLUGIN_HASHES=<workflow/web/maint hashes>
BRIDGE_IMPLEMENTATION_CANDIDATE_COMMIT=<sha>
BRIDGE_NEXT_CANDIDATE_VERSION=0.8.4
READ_ONLY_REFERENCE_REFS={
  Bobbio: ab5dcc...,
  Lucerna: 687752...,
  Mica: e49416...,
  Asteria: 0ce1d4...,
  SeminarArc: 74caaa...,
  CUHK_Date: e4fdba...
}
REAL_HOST_INSTALL_AUTHORIZED=NO
```

These are handoff facts, not a new schema/state machine.

No Bobbio locator commit exists in v0.3.

If production source/generated/version contract changes after the freeze, affected evidence must be rerun on the new candidate.

## 11. Capability Gates G1-G8 remain frozen

### G1 — Human gate / transport

Keep both behavior branches:

**G1-A reply path**

HUMAN_ONLY -> one plain-text question -> no dependent work -> explicit valid reply -> reread current Goal/resume point -> exact-once resume.

Also prove AGENT_RESOLVABLE does not prompt, UNSUPPORTED closes truthfully, Default native card is not used for required gates, desired flag is false in candidate config logic, and Plan-mode native blocking semantics are not disabled by the Default-only policy.

**G1-B no-reply/run-end path**

faithful bounded fixture -> question -> legal deadline/run-end without reply -> no dependent action -> Goal blocked/achieved=no/complete=no/user-ready=no -> existing legal recovery state -> later valid reply -> same Goal exact-once resume.

No grep-only PASS and no second state machine.

**Current authorization boundary:** candidate/source/fixture behavior may be implemented and reviewed now, but the final real-user Host install/fresh-session smoke is not authorized in this Kickoff. Therefore the implementation handoff must identify the real-host portion of G1 as pending separate authorization; it may not declare overall release-critical G1 final PASS from fixture evidence alone.

### G2 — Acceptance Admission

Incomplete evidence or unresolved human-blocked state cannot be acceptance-ready; advisory review remains possible. Preserve the CUHK-Date-like broad-green negative fixture.

### G3 — Resume/post-action closure

Both immediate reply and later blocked recovery resume the same Goal exactly once. Human action itself is not completion.

### G4 — Faithful regression

Old-bad/real sequence must be caught by focused evidence; new implementation candidate passes at the same relevant surface. Include representative interaction-sequence and mock-vs-hosted patterns.

### G5 — Evidence/final-candidate identity

Unit/synthetic/helper/browser/screenshot evidence cannot claim more than its surface. No cross-candidate PASS stitching.

### G6 — Frontend design consumption

Use Bobbio current design authority as read-only reference or another approved canonical-design task. Prove production Frontend Design consumes the design source and does not invent missing material state in code.

### G7 — Non-overreach

At least docs-only, backend/server-only and tiny nonvisual negative routes must avoid automatic Figma/locale/catalog/provider/GPT Work/full-E2E/native-smoke escalation.

### G8 — Consumption-regression diagnosis

When an active rule exists but installed/generated/session/trigger/task-entry consumption is wrong, Maintainer diagnoses the consumer path rather than adding duplicate policy.

## 12. Source Discovery regression — not G9

Keep one regression proving:

existing correct local repo + unrelated dirty work + need clean task surface -> preserve dirty -> verify identity/freshness -> use authorized local source/isolation -> no redundant network clone -> no remote remap.

057 integration complexity is evidence for why dirty ownership and remote identity must be truthful, but it does not create G9.

## 13. Human-time budget

Current execution must complete all agent-resolvable source changes, focused/full tests, generator parity, isolated fixtures, G1-B, G2-G8 applicable non-host evidence, and self-review before any later real-host/user gate is requested.

Under this v0.3 Kickoff:

- do **not** run a real Host install;
- do **not** ask the user for `W2_RESUME_056_FINAL`;
- do **not** use the user as ordinary debugging/QA.

The final real-host G1-A smoke, if still required after implementation review, belongs to a later explicitly authorized host-integration step.

## 14. Should-not-change

Protect at least:

- 057 Bridge fresh-root scaffold / raw-byte preservation / fallback versioning;
- Bridge Lite/Review/Control boundaries; Persistent Run is not a fourth workflow;
- External GPT normal waiting semantics;
- Plan-mode native request-user-input semantics;
- Host Policy unrelated safety boundaries;
- workflow-core trigger does not expand to all small tasks;
- Frontend does not force every project into Figma, one icon library, all-icon animation or a central registry;
- domain plugins retain professional/domain judgment;
- Bobbio/Lucerna/Mica/Asteria/SeminarArc/CUHK Date receive no 056 writes;
- no paid API/Terra.

## 15. Recovery

- HUMAN_ONLY no-reply: same Goal blocked/achieved=no, later valid reply resumes same Goal through existing recovery; stale identity returns to Planner.
- Bridge candidate test failure: fix only within frozen Bridge scope; do not mutate real `$CODEX_HOME`, do not fall back to `true`, and preserve 057 behaviors.
- AI_Skills replay failure: preserve evidence and released baseline; do not delete fixtures or lower acceptance.
- Product-reference source drift: if a read-only reference becomes materially incompatible with the gate claim, stop that gate and return to Planner rather than modifying the product repo.
- Branch/worktree/remote identity conflict: stop; do not remap remote, force push, reset or overwrite unrelated work.

## 16. Release / integration boundary

This v0.3 package authorizes **implementation on task branches only after Critic PASS + user-sent Kickoff**.

It does not authorize:

- merge to AI_Skills `main`;
- merge to Bridge `main`;
- any product-repo merge/write;
- Git tag / GitHub Release / package publication;
- deployment;
- real user Host Policy install/update;
- branch deletion;
- paid/external API;
- 056 overall achieved/completed claim.

Executor stops after implementation/self-QA/non-host gate evidence/candidate freeze/normal task-branch commit+push and reports `EXECUTED_UNAUDITED` or the repo's legal equivalent.

Independent implementation review must inspect the exact tuple. Any later real-host integration/release needs separate authorization and evidence.

## 17. Critic reporting closure

C056-E2 remains part of this review object. Because 056 already had REVISE rounds, any eventual execution-package PASS must first give the user the required plain-language closure explanation, then machine fields and the exact reviewed Kickoff.

## 18. Stop conditions

Return to Planner/Critic rather than expanding scope if:

- upstream Codex changes invalidate the W2/Default-vs-Plan premise;
- current Bridge main advances with relevant Host/Lite semantic changes before branch creation;
- current AI_Skills main advances with relevant production changes before branch creation;
- a new state/controller/watcher/provider/credential/paid API is required;
- a frozen F-A/F-B/F-C or W1-W5 mechanism proves architecturally insufficient;
- a PASS would require modifying a ZERO-WRITE product repo;
- real Host installation is required to proceed under the current Kickoff.

`NEXT_HANDOFF = CRITIC`
