# 056 Final Integration / Release Closure — Canonical Goal v0.2

Historical task: `056_product_delivery_discipline`  
Human-readable name: 交付工作流可靠性基线  
Stage: `FINAL_INTEGRATION_AND_RELEASE_CLOSURE`  
Status: `READY_FOR_USER_AUTHORIZATION`


## Authorization presentation

This Goal records the frozen completion contract. It is not, by itself, permission to execute main integration or permanent Host mutation.

After independent Critic PASS, the user may send the exact contents of:

`docs/operations/prompts/056_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_2.md`

as the current user message. Once that exact Kickoff is received, the current user message itself is the bounded authorization for the effects explicitly enumerated there.

At that point:
- do not require a separate repo-local Critic PASS artifact;
- do not treat this Goal's pre-execution readiness status, the Plan, or the Review Package as a second authorization gate;
- do not ask again merely because execution reaches a later step of the same frozen effect;
- ask again only for genuinely new target/scope/destructive/provider/account/credential/cost effects outside the approved Kickoff.

## Frozen candidates

AI_Skills:
- reviewed branch: `reviewed/056_product_delivery_discipline`
- production candidate: `33c30bbe0dd528031a23d379905cd00d6b65bc1f`
- final evidence HEAD: `b6f675869449df8daa86a6abcf527fbb72c66e64`
- release: repo 5.0.7; workflow-core 0.3; web-development 0.2; ai-skills-core 0.4

Bridge:
- reviewed branch: `reviewed/056_product_delivery_discipline`
- production candidate: `96a8ea1b58ebe6f9b7c5c46c43995666251911fe`
- release: 0.8.5

All G1-G8 + Source Discovery and final real-user Human Gate evidence are already PASS. Do not rerun them unless final integration changes production semantics.

## Completion contract

056 is achieved only when all are true:

1. latest-main drift is integrated without changing approved production semantics;
2. AI main is formal release 5.0.7 with source/generated/version/README/changelog parity;
3. Bridge main is formal release 0.8.5 with production bytes equivalent to the reviewed candidate;
4. exact remote main SHAs are verified after push;
5. normal Bridge installation at `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit` is upgraded from the old 0.8.2 identity to the integrated 0.8.5 main identity;
6. exact real Host `c0824.ll.unc.edu`, user `aereinh`, CODEX_HOME `/overflow/htzhu/mingcheng_new/.codex` permanently receives the released 0.8.5 Host desired state with backup and `host validate` PASS;
7. final closure evidence is committed/pushed on AI main;
8. if branch cleanup is performed, only the two exact reviewed branches are deleted after ancestry and closure checks.

## Integration constraints

AI main/reviewed histories are divergent. Preserve both histories with a merge commit; no squash/rebase/cherry-pick. The only pre-audited overlap is `docs/plugin-todos/workflow-core.md`, resolved additively.

Bridge main is a direct ancestor of the candidate and should integrate by fast-forward, followed only by README/CHANGELOG release metadata.

If execution-time drift introduces a new conflict or changes 056 production/version/release surfaces, STOP and return Planner/Critic.

## Release semantics

Formal release here means the existing repository-contract release surface: integrated main + canonical version/changelog/README/generated parity. Do not introduce the first GitHub tag/Release/package publication mechanism for 056.

## Verification

If integrated production trees are candidate-equivalent:
- run focused mechanical parity/normal-main identity checks only;
- do not rerun G1-G8, Terra, paid review, Human Gate smoke, Plan smoke or full suites.

Any production semantic change caused by conflict resolution invalidates this shortcut and requires only the affected minimal replay/regression after Planner/Critic review.

## Permanent Host effect

Successful final Host install remains installed; unlike pre-release smoke, do not restore it.

Failure uses the existing Host backup as bounded recovery when safe. No new restore subsystem is created.

## Forbidden

No tag/GitHub Release/package publish/deploy, paid API/Terra, product repo write, force push, remote remap, history rewrite, new Gate/successor, Persistent Run refinement, or unrelated CODEX_HOME change.

`NEXT_HANDOFF=CRITIC`
