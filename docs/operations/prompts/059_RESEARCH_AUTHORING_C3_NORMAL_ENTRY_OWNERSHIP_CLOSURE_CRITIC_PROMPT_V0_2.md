# 059 Research Authoring C3 正常入口所有权收口 — Execution-Ready Critic Prompt v0.2

你继续作为 AI Research Stack 的长期独立 Critic。

本轮只复核上一轮唯一 blocker `RA-C3ER1` 是否关闭，以及本轮 v0.2 同步是否引入新的真实风险。

不要重新审已经通过的 C3 主架构。
不要重新打开 candidate_plugin_replay/shared replay infrastructure。
不要修改 production。
不要启动 Codex Executor。
不要调用 Plugin Creator。
不要启动 final G1-G4。
不要调用 paid API。
不要 merge/release。

## Active context

target_repo：
`YuukiAS/AI_Skills_Collection`

target_plugin_or_domain：
`research-writing / Research Authoring`

design_topic_or_task_key：
`research-authoring--formal-production-authoring`

review_stage：
`EXECUTION_READY_REVIEW_AFTER_C2_G1_FINAL_FAIL`

branch：
`work/research-authoring--formal-production-authoring`

worktree：
`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

Permanent failed candidate：

`C2=ac501d988f00cb6672fec105ae5fd51a0679cae0`

## Prior Critic review

Path：

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_EXECUTION_READY_CRITIC_REVIEW_V0_1_2026-10-07.md`

Commit：

`75df537cd5f167e9df8afae9670a993cef137b58`

Result：

```text
RESULT=REVISE
READY_FOR_CODEX=NO
BLOCKERS=RA-C3ER1
```

Stable blocker：

`RA-C3ER1 = modified codex-research-writing normal entry lacks real runtime validation`

## Stable main architecture — do not reopen without new evidence

Repair Proposal remains unchanged：

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md`

Commit：

`b4820e49e3473959010afe5fa1e9f92bc0f4844f`

The prior Critic already accepted：

- C2 G1 real failure attribution;
- metadata discovery boundary;
- Research Authoring canonical owner/handoff;
- renderer trigger/discovery narrowing;
- research-main integrated routing;
- codex-research-writing authoring-only distinction as a production change;
- latex-paper-authoring boundary;
- generic `pdf` no-change with runtime negative-owner coverage;
- no G5;
- C3 full development matrix before final Gates;
- exact-C3 offline ChatGPT wrapper preparation.

This round does not redesign those points.

## Revised v0.2 execution package

Implementation Plan v0.2：

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_2_2026-10-07.md`

Commit：

`04272c05c59ec90ee068b0d5da8d7a02beee3afa`

Canonical Goal v0.2：

`docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_2.md`

Commit：

`539ed6114dc861b129b6808b3b9a57c2763b7242`

Capability Gate impact v0.2：

`docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_2_2026-10-07.md`

Commit：

`164051ebde003354e1303a086214a109c8f595bf`

Kickoff Draft v0.2：

`docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_2.md`

Commit：

`de770b31c840cda0feb587c5670d60450cf68726`

Execution package v0.2：

`results/research-authoring--formal-production-authoring/C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_EXECUTION_PACKAGE_V0_2.md`

Commit：

`6b8002055c024de22e72dfc14e8cb850ae07fa71`

Unchanged supporting object：

`docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md`

Commit：

`6320925c0b3a08f480d56f69908c40edd3b6d03e`

## Required initialization

Fetch/read latest main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

Then read the prior review and all v0.2 package objects above.

Only read current production source as needed to verify the specific profile runtime contract. Do not repeat the full architecture research.

## RA-C3ER1 minimum closure to verify

The v0.2 package adds one direct development runtime case：

`DEV-11 codex-research-writing authoring-only profile`

This case must run on the exact same provisional product commit P as the rest of the matrix.

Required environment：

1. fresh task-local project;
2. normal installation of the exact P `codex-research-writing` profile;
3. normal profile installer writes managed AGENTS with the actual profile routing notes;
4. generic `pdf` Skill remains installed/visible;
5. global `render-chinese-math-pdf` remains visible if it is normally visible on the machine;
6. no renderer hiding/uninstall;
7. no test-only “do not XeLaTeX/pdf/renderer” prompt blacklist;
8. no fixture/path/hash special case.

Natural task：

new or substantially revised manuscript source + requested formal PDF production.

The exact wording may be frozen before execution, but it must remain a normal user request and must not encode the expected routing answer.

Required runtime proof：

```text
MANAGED_AGENTS_PROFILE_ROUTING_NOTES_PRESENT=YES

RESEARCH_AUTHORING_CORE_PAPER_READS_GT_0=YES

MANUSCRIPT_SOURCE_PACKAGE_PRODUCED=YES

DOWNSTREAM_PRODUCTION_HANDOFF_PRODUCED=YES

GENERIC_PDF_NEW_DOCUMENT_OWNER=NO

RENDER_CHINESE_MATH_PDF_EXECUTION=0

PDF_MECHANICS_COMMANDS=0

FINAL_PDF_ARTIFACT=0
```

The case must save：

- exact provisional P;
- natural prompt;
- installed/available profile + Skill identities;
- managed AGENTS path/hash and direct evidence that the `codex-research-writing` routing notes are present;
- actual Skill path reads;
- command/no-command trace;
- output inventory;
- owner-route result;
- should-not-change result.

Static profile text or managed AGENTS presence alone cannot PASS DEV-11. The normal runtime must actually behave according to the authoring-only contract.

## Matrix synchronization

The matrix is now eleven case families.

The previous ten remain unchanged in semantics.

DEV-11 is development regression/admission evidence only and does not create G5.

Critic should verify：

- Plan says all eleven cases/subcases must PASS on one P;
- Goal includes the same profile runtime case;
- Kickoff explicitly authorizes running DEV-11 and keeps generic PDF/global renderer visible;
- Capability Gate impact says DEV-11 is not a final Gate;
- package index binds the new versions correctly.

## Production scope remains unchanged

No new production source is added by this revision.

The v0.2 package still proposes modifying `profiles/codex-research-writing.json` as already approved by the main architecture.

This revision only adds the missing real-consumer evidence before C3 freeze.

Do not require a new product layer merely because an additional runtime case now validates the existing profile contract.

## Authorization check

Kickoff v0.2 must remain within the already-reviewed bounded envelope.

It may authorize, only after the user actually sends the approved text：

- exact task branch/worktree;
- approved source/profile/test/generated edits;
- deterministic validation;
- all eleven development matrix cases including DEV-11;
- candidate metadata/docs closure;
- task-local evidence;
- provisional/C3 commit;
- exact-C3 offline wrapper preparation;
- ordinary non-force push exact branch.

It must not authorize：

- live Plugin update;
- final G1-G4;
- paid API;
- main merge/release;
- Bridge;
- generic PDF source expansion;
- renderer engine/QA scripts;
- candidate replay infrastructure changes;
- destructive Git.

## Questions to decide

Only decide：

1. Does DEV-11 directly exercise the modified `codex-research-writing` user-visible normal entry?
2. Does it prove managed AGENTS profile routing notes reach the real consumer rather than only exist statically?
3. Are generic PDF and global renderer left visible, so the case cannot PASS by hiding the competing owner?
4. Are the runtime outcome/evidence requirements strong enough to detect the same owner-admission failure class that caused C2?
5. Are Plan / Goal / Kickoff / Capability Gate impact / package synchronized?
6. Did v0.2 introduce any new concrete execution risk?
7. Can `RA-C3ER1` be CLOSED?

Do not reopen the already-approved repair architecture unless v0.2 itself creates a direct contradiction.

## Output

Return only：

`RESULT = PASS`

or

`RESULT = REVISE`

If REVISE：

prefer stable blocker `RA-C3ER1` unless a genuinely new direct blocker was introduced.

For every blocker include：

- requirement;
- direct evidence;
- causal risk;
- minimum closure;
- owner.

Do not add G5 or successor task.

If PASS, explicitly state：

```text
RA-C3ER1=CLOSED
RESULT=PASS
READY_FOR_CODEX=YES
C2_G1_FAIL=PERMANENT
C3_NOT_CREATED=YES
FINAL_GATES_AUTHORIZED=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
```

Bind：

```text
APPROVED_PROPOSAL_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md

APPROVED_PROPOSAL_COMMIT=
b4820e49e3473959010afe5fa1e9f92bc0f4844f

APPROVED_PLAN_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_2_2026-10-07.md

APPROVED_PLAN_COMMIT=
04272c05c59ec90ee068b0d5da8d7a02beee3afa

APPROVED_GOAL_PATH=
docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_2.md

APPROVED_GOAL_COMMIT=
539ed6114dc861b129b6808b3b9a57c2763b7242

APPROVED_KICKOFF_PATH=
docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_2.md

APPROVED_KICKOFF_COMMIT=
de770b31c840cda0feb587c5670d60450cf68726

APPROVED_CAPABILITY_GATE_IMPACT_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_2_2026-10-07.md

APPROVED_CAPABILITY_GATE_IMPACT_COMMIT=
164051ebde003354e1303a086214a109c8f595bf

APPROVED_PACKAGE_PATH=
results/research-authoring--formal-production-authoring/C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_EXECUTION_PACKAGE_V0_2.md

APPROVED_PACKAGE_COMMIT=
6b8002055c024de22e72dfc14e8cb850ae07fa71
```

Execution-ready PASS must then set：

`NEXT_HANDOFF=CODEX`

and output the already-reviewed Kickoff v0.2 verbatim under the Critic Role Contract.

Do not write a new semantically different Kickoff after PASS.
