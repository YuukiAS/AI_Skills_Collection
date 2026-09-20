# 056 Product Delivery Discipline — Canonical Goal

- Execution package version: `v0.3`
- Exact task: `056_product_delivery_discipline`
- Status: `READY_FOR_POST_057_EXECUTION_CRITIC_REVIEW`
- Plan: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.3
- Kickoff: `docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.3
- Architecture authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- Post-probe authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- Post-057 revalidation: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_POST_057_SOURCE_DRIFT_REVALIDATION_2026-09-18.md`
- Revalidation source: `AI_Skills_Collection main@f68e800fb604850c20a29cb3c7572e4f1a119236`

This Goal is not executable until an independent Critic reviews this exact v0.3 Plan + Goal + Kickoff, closes or revises the pending execution-package findings, returns `READY_FOR_CODEX=YES`, and the user then sends the approved Kickoff.

## 1. Positive target

Connect the already-approved Product Delivery Discipline v6 to the real central production path so that complex/risky development normally behaves as follows:

- the agent completes agent-resolvable implementation, faithful testing, actual-surface/self-QA and repair before asking for acceptance;
- only genuine `HUMAN_ONLY` dependencies ask the user;
- Default required human input uses a durable plain-text transcript handoff rather than the auto-resolving native card;
- no-reply at the legal deadline/current run end becomes an honest recoverable Goal block with achieved=no;
- acceptance/release/user-ready claims require applicable vertical closure and faithful evidence;
- Frontend Design consumes canonical design sources where they exist;
- when a rule exists but production still fails, AI Skills Maintainer diagnoses the real installed/generated/invocation/session/consumer path before adding another rule.

Completion is defined by observable normal-entry behavior and same-candidate evidence, not by more policy text.

## 2. Frozen architecture

The architecture remains:

```text
Lite L1-L6
workflow-core W1-W5
Frontend Design F-A / F-B / F-C
AI Skills Maintainer: production-consumption diagnosis
Bridge: transport / wait-resume / recovery + Lite distribution
G1-G8
Existing Source Discovery regression, not G9
```

No W6/W7, G9/G10, second state machine/review engine, Control layer, watcher, daemon, ledger, new top-level plugin or Codex fork.

## 3. Post-057 current source facts

Current canonical facts verified for this Goal:

- AI_Skills main: `f68e800fb604850c20a29cb3c7572e4f1a119236`;
- Bridge main: `e1d6b781ad7e56d567bed419001069baf439d0a5`, current formal source version `0.8.3`;
- Bobbio develop: `ab5dccb6b8b87c49671aa097233ce1bcc38be004`;
- Lucerna main: `687752861b4859f7f24799b9e17d985afc992ad2`;
- Mica main: `e49416f874f633aedc7521734ee5b0f441aae970`;
- Asteria main: `0ce1d4daca1e410ce551570578dd563d4ef67e90`;
- SeminarArc main: `74caaa4ecec16f1bc90987979458d1a4e93f52be`;
- CUHK Date main: `e4fdba4d6e38f300d5aeb9861f7c944f07c61e3d`.

057 H1-H9 and integration are inherited as complete and are not reopened.

## 4. Authorized implementation scope after an approved Kickoff

### AI_Skills_Collection — WRITE

On exact task branch:

`reviewed/056_product_delivery_discipline`

Implement:

- workflow-core W1-W5 + existing Source Discovery enforcement;
- Frontend Design F-A/F-B/F-C and production wiring of existing Figma handoff + motion capabilities;
- AI Skills Maintainer production-consumption diagnosis;
- G1-G8/source-discovery regression fixtures and evidence;
- source/generated parity, affected TODO/changelog/version-candidate closure.

Current next release slots remain:

```text
AI_Skills repository: 5.0.4 -> 5.0.5 PATCH
workflow-core:        0.1 -> 0.2
web-development:     0.1 -> 0.2
ai-skills-core:      0.2 -> 0.3
```

These are candidate/release slots, not permission to merge or publish.

### GPT_Codex_AI_Bridge_Kit — WRITE

On exact task branch:

`reviewed/056_product_delivery_discipline`

Preserve all integrated 057 scaffold/raw-byte/versioning behavior and implement:

- Lite L1-L6;
- managed desired `default_mode_request_user_input=false`;
- supported-key vs desired-state validation;
- HUMAN_ONLY plain-text blocked/recovery semantics;
- Host guidance/docs/tests consistency;
- next distinct compatible candidate slot `0.8.4`.

Current `0.8.3` is already the canonical 057 identity and must not be reused for a different 056 user-consumable candidate.

### All product repositories — ZERO WRITE

056 v0.3 does not modify:

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

Bobbio's former locator task is removed because 057 already completed it. Bobbio is read-only G6 design-source evidence only.

CUHK Date now has a root AGENTS, but `NO_GENERIC_056_AGENTS_COPY` remains the disposition.

## 5. HUMAN_ONLY contract / C056-E1 response

Planner disposition remains `ACCEPT`, pending independent Critic closure.

Required semantics:

```text
HUMAN_ONLY
-> preserve current Goal/resume point/prompt identity
-> one concise plain-text question
-> stop dependent execution
```

No reply by explicit human deadline/current run end:

```text
GOAL_BLOCKED=YES
GOAL_ACHIEVED=NO
COMPLETE=NO
READY_FOR_USER_REVIEW=NO
DEPENDENT_EXECUTION_BLOCKED=YES
```

Use an existing legal human-required/recovery state. Do not invent a BLOCKED enum. Later explicit valid reply resumes the same Goal exactly once after rereading scope/identity; no successor, repeated prompt, polling, default inference or timeout continuation.

External GPT normal waiting is not changed.

Current upstream Codex still makes native request-user-input blocking only in Plan mode and tells Default mode to use one plain-text question when explicit input is required, so the v0.2 response remains technically valid.

## 6. Critic reporting / C056-E2 response

Planner disposition remains `ACCEPT`, pending independent Critic closure.

Current `CRITIC_ROLE_CONTRACT.md` v1.3 retains the generic rule: when the same major round previously received REVISE, final PASS must first explain the closure in normal Chinese before machine-readable fields and the approved next-role prompt/Kickoff.

No new reporting mechanism is added.

## 7. Verified Workflow contract

Keep:

- **W1** Acceptance Review Admission + applicable vertical/post-action closure;
- **W2** Human Decision Gate classification:
  `HUMAN_ONLY / AGENT_RESOLVABLE / UNSUPPORTED_WITH_EVIDENCE / OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE / SAFETY_OR_AUTHORITY_BLOCKER`;
- **W3** exact failure / evidence-surface fidelity / same-candidate proof;
- **W4** repeat-failure circuit breaker + human-time budget;
- **W5** change-impact / should-not-change.

Current workflow TODO consistency must be repaired where older wording contradicts E1's recoverable Goal-blocked semantics. Newer task-local-expiry evidence remains a separate NEW item; post-056 acceptance-artifact packaging remains explicitly deferred.

## 8. Frontend Design contract

Keep:

- **F-A** canonical design authority/state coverage;
- **F-B** design-system coherence, icon/motion/accessibility and finite-token localization when claimed;
- **F-C** actual-surface convergence and producer self-QA.

Current web-development production aggregate still does not include standalone `figma-design-to-code` and `motion-interaction`; 056 must wire those existing capabilities through the canonical marketplace config/generator rather than hand-edit generated output or create another plugin.

## 9. AI Skills Maintainer contract

Active rule exists but real task still fails -> inspect installed identity, source/generated parity, invocation, trigger, task entry, session loading and normal-entry replay before deciding whether the issue is missing rule, stale install, wrong consumer, unfaithful test, execution noncompliance or real capability gap.

## 10. G1-G8

The eight gates stay frozen.

- **G1** HUMAN_ONLY recognition + reply and no-reply/recovery branches; Default native card not used for required gate; desired flag false; Plan mode not broken.
- **G2** incomplete/human-blocked candidate cannot be acceptance-ready; advisory review still allowed.
- **G3** same-Goal exact-once resume + post-action closure.
- **G4** faithful old-bad/new-good regression at the relevant surface.
- **G5** claim scope <= evidence scope + same implementation candidate.
- **G6** real Frontend Design consumption of canonical design source, preferably Bobbio read-only authority.
- **G7** non-overreach on docs-only/backend-server/tiny-nonvisual tasks.
- **G8** production consumption-regression diagnosis.
- Existing Source Discovery regression remains separate and is not G9.

### Current Host-install boundary

This v0.3 Kickoff does **not** authorize mutation of the user's real `$CODEX_HOME` or a real Host Policy install/update.

Source/unit/isolated temporary fixture testing is allowed. The final release-critical real-host application and live G1 Host smoke, if still required, remain a later separately authorized integration step.

Therefore current implementation review must not treat isolated evidence as final real-host G1 PASS, and 056 overall cannot be called achieved while that required integration boundary remains open.

## 11. Git/source contract

After approved Kickoff:

- create only the two exact task branches/worktrees authorized for AI_Skills and Bridge;
- base AI_Skills on kickoff-time latest compatible main containing approved v0.3;
- base Bridge on `e1d6b781...` unless Bridge main has materially changed, in which case stop for bounded revalidation;
- source discovery is local-first, with real identity/freshness/dirty ownership checks;
- unrelated dirty work is protected;
- no remote remap, force push, PR, main/develop merge or branch deletion.

No product repo branch/worktree is created for 056.

## 12. Execution-stage completion

Under this v0.3 authorization, Executor completion means:

- frozen implementation changes are complete on AI_Skills and Bridge task branches;
- self-QA/tests/source-generated parity and authorized G1-G8 non-host evidence are produced;
- current implementation tuple is frozen and pushed;
- ZERO-WRITE repos are unchanged;
- real Host integration/release boundaries are reported truthfully as pending if still required;
- handoff is `EXECUTED_UNAUDITED` (or legal equivalent), not overall 056 achieved.

Independent implementation review follows.

## 13. Explicit prohibitions

Do not:

- merge AI_Skills or Bridge to main;
- modify any product repo;
- tag/release/package-publish/deploy;
- install/update real Host Policy or mutate the user's real `$CODEX_HOME`;
- call paid/external model API/Terra;
- run the final live `W2_RESUME_056_FINAL` user smoke under this Kickoff;
- add W6/W7/G9/G10/state/schema/ledger/controller/watcher;
- claim 056 overall achieved.

`NEXT_HANDOFF = CRITIC`
