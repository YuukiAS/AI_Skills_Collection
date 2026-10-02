# Planner Response — Presentations 双模板生产架构 V1.1

Design topic / task key: presentations--two-template-production-redesign
Planner revision stage: architecture_revision_after_critic_v1
Source branch/ref: main
Critic review: results/presentations--two-template-production-redesign/CRITIC_REVIEW_V1.md @ 21c739b270105c222f523fd5625993fa5902e00f
V1.1 proposal: docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md
V1.1 proposal commit: f71e97c06938ab2ce175ccf3b4ac19da9309fda1

## Result

Planner disposition: all four stable blockers ACCEPTED and addressed in the complete V1.1.

This file records the response to the Critic findings. It does not approve V1.1, does not authorize implementation, and does not change production source or TODO maturity.

## PRES-V1-F01 — ACCEPT

Critic finding:
The universal Presentations front door was not bound to the actual discovery/routing consumers, and V1.0 could regress business/editable defaults into Beamer.

V1.1 closure:
- freezes the normal-entry causal chain from natural request -> installed Presentations plugin discovery/intake -> mode/deliverable/template -> shared core/local-edit -> official Presentation/Slides or Beamer adapter;
- names scripts/codex_marketplace_config.json as canonical plugin interface/packaging source;
- names source research/business skills plus shared routing as canonical internal dispatch source;
- names presentation-desktop as installation/composition profile rather than alternate route authority;
- keeps generated layers generator-only;
- replaces “minor edit does not trigger presentations” with “minor edit passes Presentations intake, then uses local-edit fast path”;
- gives a full default deliverable matrix;
- explicitly preserves business/executive no-format -> editable PPTX/Slides and explicit PPTX/Slides -> official editable adapter;
- requires G1 evidence from a real installed plugin natural request, not a helper.

Planner judgment:
Closed at architecture level. Stage 1 must fail closed if the actual platform cannot deliver natural-request discovery through the existing plugin surfaces; V1.1 does not authorize a new top-level skill or implicit-invocation hack.

## PRES-V1-F02 — ACCEPT

Critic finding:
V1.0 partly promoted evidence-gated #45–#48 merely to claim full TODO coverage.

V1.1 closure:
- #44 remains BLOCKED_NEEDS_EVIDENCE;
- #45 remains CANDIDATE_GENERIC with no new dedicated deck-wide consistency mechanism;
- #46 remains CANDIDATE_GENERIC with no new dedicated theory hierarchy mechanism;
- #47 remains CANDIDATE_GENERIC with no new simulation-specific schema/production mechanism;
- #48 remains CANDIDATE_GENERIC; 045 English final pass and #29/#31/#34 handoff behavior may continue, but do not solve/promote #48;
- all canonical TODO source maturity values stay unchanged;
- candidate-only items are observation/future-amendment inputs, not current implementation requirements.

Planner judgment:
Closed. “Cover all TODO” now means every item has a truthful implementation/evidence/future disposition, not that every item is promoted.

## PRES-V1-F03 — ACCEPT

Critic finding:
G9/G10 mixed cross-cutting evidence/release rules with user capability Gates and duplicated other Gates.

V1.1 closure:
- product Gates are G1–G9;
- H1 handles scope-honest independent review/no self-sign/full artifact access;
- H2 handles same-final-candidate/no evidence stitching;
- H3 handles regression bank/fresh evidence integrity;
- H4 handles source/runtime/render identity;
- G2 is only semantic dependency/storyline;
- G8 is only final language/spoken reader effort;
- G3 remains generic composition/readability;
- G4 remains domain/scientific-object representation;
- G5 keeps one Gate but requires two non-compensating evidence streams: actual canonical template consumption and visual fidelity;
- G9 is only cross-mode normal-entry/generalization/production integration;
- README/changelog/version/Marketplace/profile release metadata are release closure, not a product Gate.

Planner judgment:
Closed. The taxonomy no longer rewards generating control artifacts as if they were new user capabilities.

## PRES-V1-F04 — ACCEPT

Critic finding:
V1.0 Package B/C were too large to be bounded execution packages.

V1.1 closure:
six independent implementation stages now exist:

1. Front door + routing + two-template adapter foundation.
2. Semantic sequence core.
3. Composition + approved visual/object regressions.
4. Citation/text layer + final language handoff.
5. Existing-deck revision runtime + preservation.
6. Cross-mode integration/generalization + release closure.

Each stage now states:
- one observable new user capability;
- dependencies;
- scope and explicit non-goals;
- stop conditions;
- recovery path;
- primary Capability Gate(s).

Candidate-only #44–#48 are not silently implemented in these stages.

Planner judgment:
Closed at architecture level. After Critic PASS, Stage 1 gets its own execution package and execution-ready review; the six stages must not be collapsed into one Executor Goal.

## Accepted Critic architecture retained without redesign

V1.1 deliberately keeps:
- exactly two built-in templates;
- external locked input outside the built-in registry;
- existing-deck template preservation;
- strict semantic-storyboard / page-composition separation;
- teaching as shared-core mode;
- research/business triggers for at least one compatibility release;
- #43 merged into #33;
- #44 evidence-gated;
- 045-promoted failures in the regression bank;
- Beamer as current primary TeX route;
- no ltx-talk migration in this round.

## External targeted re-check

Rechecked on 2026-09-28 using CTAN:
- Beamer 3.78, dated 2026-08-20; CTAN marks Tagged PDF unsupported.
- ltx-talk 0.6.7, dated 2026-09-26; package remains explicitly experimental and prioritizes tagging/functionality over design.

Decision unchanged:
- Beamer remains adopted for this round.
- ltx-talk remains reviewed but not adopted.
- no PDF/UA claim.

Official references:
- https://ctan.org/pkg/beamer
- https://ctan.org/pkg/ltx-talk
- https://ctan.org/ctan-ann/pkg/ltx-talk

## Version / production status

Repository bump decision: NONE
Affected plugins:
- presentations: NO_BUMP
- writing-style: NO_BUMP
- workflow-core: NO_BUMP
- ai-skills-core: NO_BUMP

Reason:
This revision changes design/review documents only. No production plugin behavior changed.

## Maintenance Board

Canonical Issues #29–#48 keep current source maturity.

This Planner surface has not mutated the GitHub Project because reader-facing Project mutation requires a real Clear Writing invocation and this surface does not expose that required capability. Project sync is therefore NOT CLAIMED.

Exact pending mutation after V1.1:
- Project: AI Skills Maintenance
- Area: presentations
- Issues: #29–#48
- Status: DOING
- Current execution anchor:
  docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md
  @ f71e97c06938ab2ce175ccf3b4ac19da9309fda1
- Next action:
  independent Critic V1.1 review, prioritizing PRES-V1-F01 through PRES-V1-F04
- Do not change source maturity, mark PROMOTED/DONE, or close issues.

## Next handoff

NEXT_HANDOFF=CRITIC

Critic should:
- review the complete V1.1, not a diff;
- first re-check PRES-V1-F01 through PRES-V1-F04;
- only add new blockers from new facts, prior missed critical risks, or V1.1-introduced regression;
- decide whether the architecture is ready for a separate Stage 1 execution package;
- not authorize implementation, paid review, branch/worktree, install, or release merely from architecture PASS.
