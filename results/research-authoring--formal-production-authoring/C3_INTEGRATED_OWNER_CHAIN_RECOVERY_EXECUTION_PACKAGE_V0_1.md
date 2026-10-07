# 059 Research Authoring C3 integrated owner-chain recovery — Execution Package v0.1

状态：READY_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_AUTHORIZED  
日期：2026-10-07

## Triggering development review

`docs/design/059_RESEARCH_AUTHORING_C3_DEVELOPMENT_CRITIC_REVIEW_V0_1_2026-10-07.md`
@ `71cf5105570ad46ff29c492d8354b44121315a55`

Stable blocker：

`RA-C3DEV1`

Prior provisional attempt：

`04a17a904ce522cb4a517cb33f22e062f2bcbc09`

Status：

`FAILED_PROVISIONAL_DEVELOPMENT_ATTEMPT`

## Stable main architecture

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md`
@ `b4820e49e3473959010afe5fa1e9f92bc0f4844f`

Main architecture is not reopened.

## Recovery package

1. Recovery Proposal  
   `docs/design/059_RESEARCH_AUTHORING_C3_INTEGRATED_OWNER_CHAIN_RECOVERY_PROPOSAL_V0_1_2026-10-07.md`  
   @ `e8ede43b78d279d246c7aae81bfde782cab6dd11`

2. Implementation Plan v0.3  
   `docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_3_2026-10-07.md`  
   @ `164c204b474839cce35c0d1a45fc86c4e703336c`

3. Canonical Goal v0.3  
   `docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_3.md`  
   @ `04b5172fde45491b2dca8907c4eca31a5ebea92e`

4. Capability Gate impact v0.3  
   `docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_3_2026-10-07.md`  
   @ `c50f92484161816d9715d9b991e493277521626a`

5. Kickoff Draft v0.3  
   `docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_3.md`  
   @ `5cef1c89ea92cd8210f80f0d2ec13003085e727a`

6. Existing exact-C3 ChatGPT wrapper preparation plan  
   `docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md`  
   @ `6320925c0b3a08f480d56f69908c40edd3b6d03e`

## Selected recovery

~~~text
PRIMARY_RECOVERY=
RESEARCH_MAIN_PROFILE_SCOPED_EXPLICIT_ARTIFACT_DELEGATES

EXPLICIT_ONLY_DELEGATES=
latex-paper-authoring
pdf
render-chinese-math-pdf

LATEX_DELEGATE_MODE_FIX=YES

GLOBAL_GENERIC_PDF_SOURCE_CHANGE=NO
NEW_RENDERER_WORDING_PATCH=NO
NEW_ROUTING_FRAMEWORK=NO
~~~

## Minimal new production mechanism

One optional profile field：

`explicit_only_skills`

The normal profile installer materializes the selected project-local Skill copies with destination-local：

~~~yaml
policy:
  allow_implicit_invocation: false
~~~

Canonical source Skills remain unchanged by installation.

Managed AGENTS provides ordered routing notes plus compact explicit-delegate path locators, without repeating those delegates as ordinary implicit Skill descriptions.

## Why this is necessary

DEV-04 proved renderer metadata + routing prose still allowed renderer Skill selection before Research Authoring.

DEV-05 proved：

- LaTeX delegate entered early;
- generic pdf was actually read;
- canonical renderer was not read;
- direct pdflatex produced final PDF.

Therefore another metadata wording pass is not accepted as the recovery.

## P2

No P2 exists yet.

The future Executor must first prove the profile explicit-only mechanism on the pinned local Codex runtime.

Only then may the bounded source changes form：

`C3_PROVISIONAL_PRODUCT_COMMIT=<P2>`

The complete eleven-case development matrix reruns from zero on P2.

## README evidence

P2 admission also requires durable actual Clear Writing invocation evidence for the README region changed on the C3 line.

## Wrapper

The wrapper built from `04a17...` is not final.

Only exact C3 after P2 matrix PASS may produce the offline wrapper used for later G4 preparation.

## Gate boundary

~~~text
ADD_G5=NO
FINAL_GATES_NOT_STARTED=YES
LIVE_PLUGIN_MUTATION_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
~~~

This package itself authorizes no implementation.

Only independent execution-ready Critic PASS followed by the user actually sending the approved v0.3 Kickoff can authorize P2 execution.
