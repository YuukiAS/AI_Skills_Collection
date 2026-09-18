# 056 Product Delivery Discipline — Post-057 Source Drift Revalidation

- Task key: `056_product_delivery_discipline`
- Date: 2026-09-18
- Status: `PLANNER_REVALIDATED_PENDING_CRITIC`
- Revalidation source: `AI_Skills_Collection main@f68e800fb604850c20a29cb3c7572e4f1a119236`
- Prior execution package: v0.2
- Intended amended package: v0.3

## 1. Scope

This is a bounded source-drift revalidation after 057 Repo AGENTS Hygiene was fully integrated. It does **not** redesign Product Delivery Discipline v6, execute 056, create an execution branch/worktree, modify production source, merge/release, install Host Policy, or call a paid API.

The question is limited to:

> Which v0.2 execution assumptions remain valid, which work was already completed by 057, which refs/version slots are stale, and what must be removed or mechanically amended before 056 can be reviewed for execution again?

## 2. Current canonical refs verified

Planner re-read current canonical Git state instead of relying on the historical 057 review-package status text.

| Repository | Current canonical ref used for revalidation | 057 integration status relevant to 056 |
| --- | --- | --- |
| AI_Skills_Collection | `main@f68e800fb604850c20a29cb3c7572e4f1a119236` | M3 `24051588d13f07e7f71e0edf5a723aca36754ed5` is a merge parent/in ancestry |
| GPT_Codex_AI_Bridge_Kit | `main@e1d6b781ad7e56d567bed419001069baf439d0a5` | exact reviewed 057 candidate is canonical |
| Bobbio | `develop@ab5dccb6b8b87c49671aa097233ce1bcc38be004` | exact reviewed 057 candidate is canonical |
| Lucerna | `main@687752861b4859f7f24799b9e17d985afc992ad2` | reviewed 057 candidate `41cd1297af6901531d3135593bc9806bffc38829` is in ancestry |
| Mica-for-ChatGPT | `main@e49416f874f633aedc7521734ee5b0f441aae970` | exact reviewed 057 candidate is canonical |
| Asteria | `main@0ce1d4daca1e410ce551570578dd563d4ef67e90` | exact reviewed 057 candidate is canonical |
| SeminarArc | `main@74caaa4ecec16f1bc90987979458d1a4e93f52be` | exact reviewed 057 candidate is canonical |
| CUHK_Date | `main@e4fdba4d6e38f300d5aeb9861f7c944f07c61e3d` | 057 remained inspect-only; repo advanced independently and now has a root `AGENTS.md` |

057 H1-H9, I1-I6, AGENTS hygiene and integration are inherited as completed facts. They are not reopened here.

## 3. Source-drift matrix

| Area / repo | Old 056 v0.2 assumption | Current verified source | Impact | v0.3 action |
| --- | --- | --- | --- | --- |
| AI_Skills | v0.2 package based on pre-057 main; production workflow/frontend/maintainer source still awaiting 056 | `main@f68e800...`; 057 and review/control docs integrated; 056 production skills/config remain unchanged; workflow TODO gained unrelated/new evidence | **AMEND** | Refresh refs; keep W1-W5/F-A-F-C/Maintainer work; correct stale TODO wording that says no-reply is “not terminal BLOCKED” so it matches E1 Goal-blocked semantics; keep newer task-local-expiry item NEW and post-056 packaging item deferred |
| Bridge | `main@cb77b1...`, version `0.8.2 -> 0.8.3` planned | `main@e1d6b781...`, formal source version `0.8.3`; 057 scaffold/raw-byte/versioning work is now canonical; Host config/docs still say `default_mode_request_user_input=true` | **AMEND** | Preserve all 057 behavior; implement remaining 056 Host/Lite/HUMAN_ONLY changes; next distinct compatible candidate is `0.8.4`, not another `0.8.3` |
| Bobbio | `ADD_MINIMAL_LOCATOR`: add `docs/design/FIGMA_HANDOFF.md` to Product Design reads | `develop@ab5dcc...`; locator already present; Figma/Product Design Brief/old PNG authority already reconciled | **REMOVE** | Bobbio becomes **ZERO WRITE**; keep only read-only G6 design-source reference |
| Lucerna | `NO_WRITE / ALREADY_COVERED` | `main@687752...`; 057 AGENTS hygiene is in ancestry; later product work expanded Lucerna but did not create a new 056 ownership need | **KEEP** | ZERO WRITE; use historical/current Lucerna evidence only as workflow regression context |
| Mica | `NO_WRITE / ALREADY_COVERED` | `main@e49416...`; consolidated testing ladder, diagnostics, manual authenticated acceptance and typing boundaries are canonical | **KEEP** | ZERO WRITE |
| Asteria | `NO_WRITE / ALREADY_COVERED` | `main@0ce1d4...`; root map + Browser locator + GPT Work-before-human + delegated visual rules are canonical | **KEEP** | ZERO WRITE |
| SeminarArc | `NO_CHANGE / EVIDENCE_NEEDED` | `main@74caaa...`; root safety map + detailed `DEVICE_TESTING.md` ownership are canonical | **KEEP** | ZERO WRITE; do not invent a Figma requirement |
| CUHK Date | no tracked root `AGENTS.md`; `NO_GENERIC_056_AGENTS_COPY` | `main@e4fdba...`; root `AGENTS.md` now exists with Handoff protocol + project-specific staging/handoff rules; Questionnaire V4 has substantial independent product advancement | **REVALIDATE -> KEEP** | `NO_GENERIC_056_AGENTS_COPY` still stands; ZERO WRITE; generic V4 failure patterns remain evidence for W1/W3/W5/Frontend rather than project policy |
| C056-E1 | Planner v0.2 ACCEPT, pending Critic | current Codex source still makes Default native request-user-input nonblocking vs Plan; Bridge production still has stale true/old wording | **KEEP** | Preserve v0.2 blocked/achieved=no + same-Goal recovery response; Critic still must close it |
| C056-E2 | Planner v0.2 ACCEPT, pending Critic | `CRITIC_ROLE_CONTRACT.md` v1.3 remains canonical with post-REVISE closure explanation | **KEEP** | No further contract change planned; Critic still must close it |

No current source establishes a contradiction that requires v7 or reopening the v6 architecture.

## 4. AI_Skills drift

Relative to the completed v0.2 planning baseline, current production source for the three 056-owned plugin areas remains materially unchanged:

- repository version remains `5.0.4`;
- `workflow-core` remains `0.1`;
- `web-development` remains `0.1`;
- `ai-skills-core` remains `0.2`;
- the current `web-development` visual aggregate still consumes `frontend-visual-systems`, `visual-direction`, and `design-system-tokens`, but does not yet consume standalone `figma-design-to-code` or `motion-interaction`;
- workflow-core and AI Skills Maintainer production skills have not acquired the 056 W1-W5 / consumption-diagnosis implementation.

Therefore the AI_Skills implementation scope remains valid.

Two newer workflow TODO items must **not** silently expand 056:

1. `Task-local prohibitions must expire...` is a later NEW workflow issue. It is related to human-gate friction but was not part of the frozen v6 package and remains follow-up evidence.
2. `Post-056 acceptance artifact packaging / comparison-review fidelity` explicitly says `DEFER_UNTIL_056_COMPLETE`. It must remain deferred.

One older 056 TODO line is stale against C056-E1: it says a no-reply HUMAN_ONLY handoff should not be terminal BLOCKED. v0.3 should update that TODO wording during 056 implementation so it distinguishes recoverable **Goal blocked/achieved=no** from impossible/STOP, matching the already-approved Planner response. This is source-consistency work inside the existing 056 scope, not a new capability.

## 5. Bridge drift and version slot

Current Bridge `main@e1d6b781...` is the integrated 057 candidate:

- `pyproject.toml` = `0.8.3`;
- `ai_bridge_kit.__version__` = `0.8.3`;
- CHANGELOG contains the 0.8.3 scaffold/raw-byte/Lite-versioning batch;
- `templates/repo/AGENTS_TEMPLATE.md` is canonical for fresh-repo project-owned structure;
- `templates/prompts/AGENT_RULES.md` already contains the approved Lite fallback versioning policy.

The remaining 056 Bridge work is still real:

- `AGENTS.md` still documents `default_mode_request_user_input = true`;
- `templates/host/CODEX_CONFIG_PROFILE.md` still documents `true`;
- `ai_bridge_kit/host.py` still manages desired `true`;
- current host-policy tests still assert `true`;
- `GLOBAL_AGENTS_SNIPPET.md` still says “Because host policy enables ...” and retains the overly broad recoverable-question wording that C056-E1 was written to fix.

Thus 057 did not implement the 056 transport/blocked semantics.

Under the now-canonical Lite versioning rule, a different user-consumable Bridge candidate must not reuse the same formal version. 0.8.3 is already the canonical 057 candidate/source identity. The next compatible 056 candidate is therefore:

`Bridge 0.8.3 -> 0.8.4 PATCH candidate`.

This is a future candidate slot only. This revalidation does not tag, release, publish, deploy, or install it.

## 6. Bobbio drift

Bobbio `develop@ab5dcc...` already contains exactly the old 056 locator work:

- root `AGENTS.md` Product Design reads include `docs/design/FIGMA_HANDOFF.md`;
- root rules identify Figma as current canonical visual design/components/screen-composition source;
- `FIGMA_HANDOFF.md` and `PRODUCT_DESIGN_BRIEF.md` now agree that Figma owns current production visual design, the Brief owns durable product/interaction constraints, and old PNGs are historical/supporting references.

The old Phase 3 Bobbio write is therefore removed completely. Bobbio remains useful as a read-only G6 normal-design-authority fixture, but no 056 Bobbio commit/version change is permitted.

## 7. Lucerna, Mica, Asteria and SeminarArc

057 completed the intended instruction-surface hygiene. Current project-specific rules remain stronger than a copied generic 056 checklist:

- Lucerna retains Windows release/tray lifecycle, live provider truth, matching regression, screenshot and Longleaf boundaries.
- Mica retains one testing ladder, privacy-safe diagnostics, typing-hot-path constraints, no automated authenticated ChatGPT regression, and final manual authenticated acceptance.
- Asteria keeps its root map, canonical Browser contract locator, GPT Work-before-human gate, and delegated visual/scientific rules.
- SeminarArc keeps a prominent physical-device safety summary while `docs/DEVICE_TESTING.md` owns detailed mechanics.

All four remain ZERO WRITE in 056.

Lucerna's substantial post-057 product development is unrelated canonical advancement. It may strengthen the historical evidence that real delivery paths matter, but it is not imported as 056 product scope.

## 8. CUHK Date drift

The old factual statement “no root AGENTS exists” is obsolete. Current `CUHK_Date main@e4fdba...` has a root `AGENTS.md` with:

- the standard Handoff/read-first map;
- project-specific rules, currently including staging handoff URL safety.

This does **not** justify copying Product Delivery Discipline into the project. The central ownership principle is stronger now, not weaker: generic delivery behavior stays in workflow-core / Frontend Design / Bridge Lite; CUHK Date root keeps project-specific invariants.

Current Questionnaire V4 has also advanced substantially: catalog/localization/hosted-state work now has stronger hosted and coverage evidence, while hosted automatic YuNet remains a separately deferred matching gate. Those product outcomes do not erase the historical failure patterns that motivated W1/W3/W5/F-B/F-C, and they do not create a new 056 write requirement.

Disposition remains:

`CUHK Date = NO_GENERIC_056_AGENTS_COPY / ZERO WRITE`.

## 9. C056-E1 / E2 revalidation

### C056-E1 — Planner disposition remains ACCEPT, pending Critic closure

Current upstream Codex was rechecked at `openai/codex@7498521d288b9b3b96ffba4eedf089d8d6e06a84`:

- request-user-input handler still sets `is_blocking = mode == ModeKind::Plan`;
- Default collaboration guidance still says the tool is for optional questions, and required user input should be requested with one concise plain-text question.

No new upstream evidence invalidates the v0.2 durable transcript design.

The v0.3 package therefore keeps:

- no-reply at explicit deadline/current run end -> `GOAL_BLOCKED=YES`, `GOAL_ACHIEVED=NO`, `COMPLETE=NO`, `READY_FOR_USER_REVIEW=NO`;
- existing legal human-required/recovery machine state, no new BLOCKED enum;
- later explicit same-thread answer -> same Goal exact-once recovery + post-action closure;
- External GPT normal waiting semantics unchanged.

### C056-E2 — Planner disposition remains ACCEPT, pending Critic closure

Current `CRITIC_ROLE_CONTRACT.md` remains v1.3 and retains the generic requirement that a final PASS after prior REVISE first explain the closure in user-readable language before machine fields / approved next-role prompt. No new change is required.

Planner does not declare either finding closed. The next independent Critic must close them.

## 10. Current authorization boundary for v0.3

The user's current instruction narrows this execution package relative to v0.2:

- no main/develop merge;
- no release/tag/package publish/deploy;
- no **real user Host Policy install/update**;
- no paid API/Terra;
- no unrelated product work.

This is an execution-stage authorization boundary, not a v6 architecture change.

Therefore v0.3 may implement and test Bridge Host Policy behavior in source/tests and isolated temporary fixtures, but it must not mutate the user's real `$CODEX_HOME` or run a real-host `ai-bridge host install` under this Kickoff. Release-critical real-host application / final G1 host smoke remains a later separately authorized integration step and cannot be falsely reported PASS during the implementation stage.

## 11. Conclusion

`V6_ARCHITECTURE_CONTRADICTION = NO`

Required amendment is bounded:

1. refresh exact refs;
2. remove Bobbio write scope entirely;
3. make all product repos ZERO WRITE;
4. change Bridge future candidate slot from `0.8.3` to `0.8.4`;
5. preserve 057 Bridge scaffold/raw-byte/versioning behavior as should-not-change;
6. preserve E1/E2 responses and current v6 gates;
7. keep later unrelated workflow TODO evidence out of 056;
8. tighten current execution authorization so real Host install/release/integration remains separate.

`NEXT_HANDOFF = EXECUTION_PACKAGE_V0_3_CRITIC_REVIEW`
