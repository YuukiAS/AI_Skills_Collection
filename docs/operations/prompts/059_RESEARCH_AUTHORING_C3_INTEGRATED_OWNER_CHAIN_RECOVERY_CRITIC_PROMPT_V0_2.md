# 059 Research Authoring C3 integrated owner-chain recovery — Critic Prompt v0.2

你继续作为 AI Research Stack 的长期独立 Critic。

本轮只复核上一轮唯一 blocker `RA-C3DEV1` 是否关闭，以及这次最小同步有没有引入新的真实风险。

不要重新审 Research Authoring 主架构。
不要重新打开 shared replay / Bridge。
不要修改 production。
不要启动 Codex。
不要启动 final G1-G4。
不要调用 Plugin Creator / paid API。
不要 merge/release。
不要新增 G5 或 successor task。

## Active context

target_repo：
`YuukiAS/AI_Skills_Collection`

target_plugin_or_domain：
`research-writing / Research Authoring`

design_topic_or_task_key：
`research-authoring--formal-production-authoring`

review_stage：
`EXECUTION_READY_REVIEW_AFTER_C3_DEVELOPMENT_FAIL`

branch：
`work/research-authoring--formal-production-authoring`

worktree：
`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

Permanent failed final candidate：

`C2=ac501d988f00cb6672fec105ae5fd51a0679cae0`

Failed provisional development attempt：

`04a17a904ce522cb4a517cb33f22e062f2bcbc09`

## Prior Critic review

Path：

`docs/design/059_RESEARCH_AUTHORING_C3_INTEGRATED_OWNER_CHAIN_RECOVERY_CRITIC_REVIEW_V0_1_2026-10-07.md`

Commit：

`e24ae290647456200c7f66c555caf61a56278d3c`

Result：

~~~text
RESULT=REVISE
RA-C3DEV1_RECOVERY_DESIGN=REVISE
READY_FOR_CODEX=NO
BLOCKERS=RA-C3DEV1
~~~

The prior Critic already accepted：

- profile-scoped `allow_implicit_invocation=false` as the structural recovery;
- current-runtime preflight;
- profile-scoped generic `pdf` containment;
- profile-scoped renderer containment;
- LaTeX direct/delegate two-mode repair;
- full 11-case P2 rerun;
- README Clear Writing durable evidence;
- exact-C3 offline wrapper rebuild;
- no G5;
- no Bridge/shared replay/global generic-pdf change.

Do not reopen these without new direct evidence.

## The only prior gap

The prior package made `latex-paper-authoring` explicit-only in `research-main`, but it did not define/validate the original direct existing-LaTeX normal entry：

~~~text
existing LaTeX source
+ compile/debug/template repair/source hygiene/bibliography/build troubleshooting
-> explicitly load latex-paper-authoring
-> compile/debug allowed
~~~

That route must remain distinct from：

~~~text
finalized Markdown/LaTeX render-only
-> explicitly load render-chinese-math-pdf
~~~

And new/substantially revised manuscripts must remain：

~~~text
Research Authoring first
-> optional LaTeX source/package delegate
-> renderer only after handoff if final PDF is requested
~~~

## Revised objects

Stable main C3 Proposal remains unchanged：

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md`
@ `b4820e49e3473959010afe5fa1e9f92bc0f4844f`

Recovery Proposal, same path, minimally synchronized：

`docs/design/059_RESEARCH_AUTHORING_C3_INTEGRATED_OWNER_CHAIN_RECOVERY_PROPOSAL_V0_1_2026-10-07.md`
@ `b4cfef6685b232a215d56b942175bf50de415a98`

Implementation Plan v0.3, same path：

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_3_2026-10-07.md`
@ `409dedc44931527e02551ac9689521655b328db3`

Canonical Goal v0.3：

`docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_3.md`
@ `89aef6c6454d449b23c953cb5a66b3c7a27a1c5a`

Kickoff v0.3：

`docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_3.md`
@ `30c6e3d733126b8862c0592cced3e969b685df66`

Capability Gate impact v0.3：

`docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_3_2026-10-07.md`
@ `c66a7be9b81d976e65ad54081326c4d3ad5fb687`

Package index：

`results/research-authoring--formal-production-authoring/C3_INTEGRATED_OWNER_CHAIN_RECOVERY_EXECUTION_PACKAGE_V0_1.md`
@ `fedbca2e9ffe5356dc384408a9fb9ce578213399`

Unchanged exact-C3 wrapper preparation plan：

`docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md`
@ `6320925c0b3a08f480d56f69908c40edd3b6d03e`

## What changed

Only the missing direct-LaTeX route and regression coverage were added.

### research-main route contract

The package now explicitly distinguishes：

1. **existing LaTeX compile/debug/source-maintenance**
   ~~~text
   explicitly load latex-paper-authoring
   -> compile/debug/build allowed
   ~~~

2. **finalized-source render-only**
   ~~~text
   explicitly load render-chinese-math-pdf
   -> final render/QA
   ~~~

3. **new/substantially revised manuscript, with or without PDF**
   ~~~text
   Research Authoring core/paper first
   -> optional explicit latex-paper-authoring for source/package
   -> return to Research Authoring
   -> if PDF requested, explicit renderer after handoff
   ~~~

No internal Skill name is required in the user's natural request.

### Development regression

No DEV-12 was added.

The direct existing-LaTeX should-not-change run is folded into DEV-07.

Required natural subrun：

~~~text
research-main
+ existing LaTeX source
+ natural compile/debug/template/source-hygiene/bibliography/build request
-> latex-paper-authoring actual read > 0
-> compile/debug succeeds
-> Research Authoring does not rewrite/re-plan the existing paper
-> generic pdf does not become owner
-> render-chinese-math-pdf does not misclassify source-debug as render-only
~~~

The existing DEV-07 render-only subrun remains separately required and must route to the renderer.

This distinction is the point of the closure.

## Required review

Only decide：

1. Does the updated profile contract preserve direct existing-LaTeX compile/debug/source-maintenance after making `latex-paper-authoring` explicit-only?
2. Is that route clearly distinguished from finalized-source render-only?
3. Does the package still force every new/substantially revised manuscript through Research Authoring first, regardless of whether PDF is requested?
4. Does DEV-07 now provide real normal-entry should-not-change evidence without adding a twelfth case or G5?
5. Do Plan / Goal / Kickoff / Gate impact / package index express the same route and same regression?
6. Did the minimal sync introduce any new execution or authorization risk?
7. Can `RA-C3DEV1` now be closed at execution-ready design stage?

Do not require unrelated new tests or reopen already-accepted mechanisms unless the revised package directly contradicts them.

## Output

Return only：

`RESULT = PASS`

or

`RESULT = REVISE`

If REVISE, continue using `RA-C3DEV1` unless a genuinely independent new blocker was introduced.

Every blocker must include：

- requirement;
- direct evidence;
- causal risk;
- minimum closure;
- owner.

If PASS, explicitly state：

~~~text
RA-C3DEV1=CLOSED
RESULT=PASS
READY_FOR_CODEX=YES

C2_G1_FAIL=PERMANENT
04a17a904ce522cb4a517cb33f22e062f2bcbc09=
FAILED_PROVISIONAL_DEVELOPMENT_ATTEMPT

P2=NOT_CREATED
C3_FINAL_CANDIDATE_COMMIT=NOT_ADMITTED

FINAL_GATES_AUTHORIZED=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
~~~

Bind exact reviewed objects：

~~~text
APPROVED_STABLE_PROPOSAL_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md

APPROVED_STABLE_PROPOSAL_COMMIT=
b4820e49e3473959010afe5fa1e9f92bc0f4844f

APPROVED_RECOVERY_PROPOSAL_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_INTEGRATED_OWNER_CHAIN_RECOVERY_PROPOSAL_V0_1_2026-10-07.md

APPROVED_RECOVERY_PROPOSAL_COMMIT=
b4cfef6685b232a215d56b942175bf50de415a98

APPROVED_PLAN_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_3_2026-10-07.md

APPROVED_PLAN_COMMIT=
409dedc44931527e02551ac9689521655b328db3

APPROVED_GOAL_PATH=
docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_3.md

APPROVED_GOAL_COMMIT=
89aef6c6454d449b23c953cb5a66b3c7a27a1c5a

APPROVED_KICKOFF_PATH=
docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_3.md

APPROVED_KICKOFF_COMMIT=
30c6e3d733126b8862c0592cced3e969b685df66

APPROVED_GATE_IMPACT_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_3_2026-10-07.md

APPROVED_GATE_IMPACT_COMMIT=
c66a7be9b81d976e65ad54081326c4d3ad5fb687

APPROVED_PACKAGE_PATH=
results/research-authoring--formal-production-authoring/C3_INTEGRATED_OWNER_CHAIN_RECOVERY_EXECUTION_PACKAGE_V0_1.md

APPROVED_PACKAGE_COMMIT=
fedbca2e9ffe5356dc384408a9fb9ce578213399
~~~

Execution-ready PASS must set：

`NEXT_HANDOFF=CODEX`

and output the reviewed Kickoff v0.3 verbatim under the Critic Role Contract.

Do not rewrite a semantically different Kickoff after PASS.
