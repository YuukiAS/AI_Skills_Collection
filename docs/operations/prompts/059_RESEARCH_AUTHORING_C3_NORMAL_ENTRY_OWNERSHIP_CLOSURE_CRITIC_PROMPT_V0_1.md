# 059 Research Authoring C3 正常入口所有权收口 — Execution-Ready Critic Prompt v0.1

你继续作为 AI Research Stack 的长期独立 Critic。

本轮只审 059 / Research Authoring 的 C3 正常入口所有权收口执行包。

不要实现 production。
不要启动 Codex Executor。
不要调用 Plugin Creator。
不要更新 live Research Authoring Plugin。
不要启动 final G1-G4。
不要调用 paid API。
不要 merge/release。
不要重新打开 candidate_plugin_replay/shared replay infrastructure。
不要修改 Bridge Kit。

## Active context

target_repo：
YuukiAS/AI_Skills_Collection

target_plugin_or_domain：
research-writing / Research Authoring

design_topic_or_task_key：
research-authoring--formal-production-authoring

review_stage：
EXECUTION_READY_REVIEW_AFTER_C2_G1_FINAL_FAIL

source/execution branch：
work/research-authoring--formal-production-authoring

worktree：
/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring

Permanent failed candidate：

C2=ac501d988f00cb6672fec105ae5fd51a0679cae0

C2 final evidence head：

1aa52fb737735443dee40cc205e083a3492204f7

## Failure authority

Read：

results/research-authoring--formal-production-authoring/c2_final/C2_FINAL_GATE_STOP_G1_FAIL.md

docs/design/059_RESEARCH_AUTHORING_C2_G1_FINAL_FAILURE_CRITIC_REVIEW_V0_1_2026-10-06.md
@ 15f2009fc4e4d276e7ed5720e92be36fe997f4ed

docs/design/059_RESEARCH_AUTHORING_C2_G1_FINAL_FAILURE_CLOSURE_REQUIREMENTS_V0_1_2026-10-06.md
@ 15bba2ff6aa3f65e2301a4e90f2087a25fd95946

Stable fact：

C2 G1 is a permanent real final FAIL.

Do not reinterpret it as loading/replay/environment failure.

## Review objects

Repair Proposal：

docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md
@ b4820e49e3473959010afe5fa1e9f92bc0f4844f

Implementation Plan：

docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md
@ 690ea5b07a47cf8a1772dca6d293e832dbc3fadd

Canonical Goal：

docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_1.md
@ da73426374f32426cb2373e19c08ae3f2fdec95d

Capability Gate impact：

docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_1_2026-10-06.md
@ 0ea6094d2046ae6290ae482131ab732656d85cd3

ChatGPT Plugin offline preparation：

docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md
@ 6320925c0b3a08f480d56f69908c40edd3b6d03e

Kickoff Draft：

docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_1.md
@ 4ebcedd7450112c8cec54896307ba577fb0e926b

Package index：

results/research-authoring--formal-production-authoring/C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_EXECUTION_PACKAGE_V0_1.md
@ 50772a1635b9da04f1c7c014307bdae5dee67994

All objects belong to one bounded package and must be reviewed together.

## Required initialization

Fetch/read latest main：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md

For this central production refinement, use：

workflow-core
+ ai-skills-core
+ research-writing / Research Authoring

as distinct owners.

Read current branch source necessary to judge the package：

Research Authoring：
- skills/writing/research/research-authoring-core/SKILL.md
- skills/writing/research/research-reporting/SKILL.md
- skills/writing/research/paper-workflow-orchestrator/SKILL.md
- skills/writing/research/latex-paper-authoring/SKILL.md
- scripts/codex_marketplace_config.json
- generated research-writing report/paper aggregates as evidence only

Renderer：
- skills/tools/documents-media/render-chinese-math-pdf/SKILL.md
- tests/test_render_chinese_math_pdf.py

Profiles：
- profiles/research-main.json
- profiles/codex-research-writing.json
- scripts/skills.py profile routing-note consumer

Tests：
- tests/test_research_writing_routing.py
- directly related Marketplace/profile tests

Adjacent owner：
- skills/tools/documents-media/pdf/SKILL.md
  only to judge whether Planner's deliberate no-change boundary is defensible.

Do not re-audit unrelated renderer engine/font/QA implementation.

## Independent external check required

Independently verify current OpenAI Skill/Plugin behavior using official current sources.

At minimum check：

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/api/docs/guides/tools-skills
- https://developers.openai.com/plugins/guides/optimize-metadata
- https://help.openai.com/en/articles/20001256-plugins-in-chatgpt

Planner's current interpretation：

1. Skill discovery initially exposes name/description;
2. full SKILL instructions are read after model selection/match;
3. metadata therefore matters for preventing premature renderer selection;
4. installed/available Skill is not the same thing as current owner authorization;
5. no hard conditional ACL/priority primitive has been identified that makes a globally installed renderer unavailable only for standalone Research Authoring while keeping it available for research-main.

If official evidence contradicts this, return REVISE with exact current source.

Do not approve a claim of stronger platform enforcement than the sources support.

## Root cause to review

Planner conclusion：

ROOT_CAUSE=
MISSING_EXECUTABLE_NORMAL_ENTRY_OWNER_ADMISSION

C2 trace proves：

- exact Research Authoring aggregate consumed;
- aggregate body already contained standalone stop rule;
- global render-chinese-math-pdf was selected/read anyway;
- PDF compile/preview/extraction/QA occurred.

Planner therefore rejects another aggregate-only wording patch.

Judge whether this is the correct causal layer.

## Required three-mode closure

The selected mechanism must simultaneously support：

### A. standalone Research Authoring

Natural research report/manuscript authoring request with eventual PDF：

Research Authoring
-> stable source/package
-> complete downstream handoff
-> STOP

Global renderer remains discoverable but must not be selected/consumed.

### B. research-main integrated production

Same family request：

Research Authoring first
-> stable source + explicit handoff
-> renderer
-> real PDF + renderer QA
-> Research Authoring final scientific QA

### C. true render-only

Finalized Markdown/LaTeX：

renderer direct
-> PDF + QA

No full Research Authoring planning.

Critic must judge the entire three-mode causal chain, not just the original failing command.

## Repair-layer comparison

Planner compared：

1. generated aggregate only -> REJECTED by C2 final evidence;
2. renderer only -> INSUFFICIENT;
3. Research Authoring canonical only -> INSUFFICIENT;
4. profile routing only -> INSUFFICIENT;
5. Research Authoring canonical boundary + renderer discovery boundary + existing profile routing -> SELECTED.

Judge：

- whether option 5 is truly the minimum reliable existing mechanism;
- whether it is too soft to be executable on the actual platform;
- whether a simpler mature existing mechanism was missed;
- whether any proposed layer is unnecessary.

Do not demand a new routing service/state machine merely for theoretical certainty.

If the existing Skill/Profile platform cannot express the required distinction with enough normal-entry reliability, say so explicitly and REVISE rather than accepting another prose-only patch.

## Proposed production scope

Research Authoring：

- research-authoring-core/SKILL.md
- research-reporting/SKILL.md
- paper-workflow-orchestrator/SKILL.md
- latex-paper-authoring/SKILL.md

Renderer：

- render-chinese-math-pdf/SKILL.md

Profiles/routing：

- profiles/research-main.json
- profiles/codex-research-writing.json
- scripts/codex_marketplace_config.json

Tests：

- tests/test_research_writing_routing.py
- tests/test_render_chinese_math_pdf.py
- directly required parity/version tests

Generated output only through generators.

Renderer scripts/engine/font/QA remain unchanged.

Judge whether this is the minimum complete source scope.

## Renderer discovery contract

Planner requires renderer metadata to positively match：

- finalized-source render-only;
- explicit downstream document-owner handoff;
- renderer QA after render admission.

And negatively exclude first-owner activation for：

- creating;
- materially rewriting;
- reorganizing;
- scientifically revising;

a research report/manuscript merely because final output is PDF.

Judge whether this changes the earliest actual discovery surface rather than merely adding a late body instruction.

## Research Authoring canonical contract

Core must define：

renderer installed/discoverable != renderer admitted.

Accepted admission：

- current research-main profile explicitly authorizes Research Authoring -> renderer after stable source/handoff;
- later downstream task explicitly consumes a frozen Research Authoring handoff.

Not sufficient：

- renderer globally exists;
- generic runtime can execute XeLaTeX;
- user mentions PDF while still asking Research Authoring to author/revise.

The handoff remains lightweight, using already-approved fields; no new database/schema/state machine.

Judge whether this is sufficient and whether report/paper/LaTeX delegates need the proposed alignment.

## Profile contract

research-main：

- remains renderer-inclusive;
- report + PDF routes Research Authoring first;
- manuscript + PDF routes paper/core first;
- render-only finalized source routes renderer direct;
- renderer then hands back to Research Authoring scientific QA.

codex-research-writing：

- remains renderer-free;
- formal artifact request stops at source/package + handoff;
- global renderer discoverability does not upgrade the profile into research-main.

Judge whether current scripts/skills.py routing-note consumer makes these profile rules part of the real normal entry.

## Generic pdf Skill no-change decision

Current generic pdf description is broad.

Planner deliberately does not change it because：

- C2 failure directly implicated render-chinese-math-pdf;
- historical research-main normal replay worked despite generic pdf being installed;
- generic pdf has broader non-research blast radius.

But C3 development matrix treats generic pdf as a mandatory negative owner; if it steals authoring, C3 does not freeze and task returns to Planner/Critic.

Judge whether this is prudent minimalism or an obvious under-fix.

If you believe generic pdf must be changed now, provide direct causal evidence, not only theoretical possibility.

## Version decision

Planner proposes：

research-writing:
remain 0.3 candidate; NOT 0.4.

render-chinese-math-pdf:
0.2 -> 0.3 candidate if trigger behavior is implemented and complete matrix passes.

Repository VERSION:
unchanged during bounded implementation/final gates.

Formal repository PATCH/release:
only after final G1-G4 PASS.

Judge this against current version policy and current branch/main state.

README user-facing version/card change requires actual Clear Writing invocation before C3 freeze.

## Complete development matrix

C3 may not freeze until all cases pass on the exact same provisional product commit P：

1. standalone report + formal PDF -> source/handoff, zero renderer/PDF mechanics;
2. standalone ordinary advisor report;
3. standalone manuscript + formal PDF -> paper source/package/handoff, zero renderer;
4. research-main report + formal PDF -> RA first, renderer second, real PDF;
5. research-main manuscript + PDF -> paper first, renderer second, real PDF;
6. finalized Markdown render-only -> renderer direct, no RA;
7. finalized LaTeX render-only -> renderer direct, no RA planning;
8. PPT/Beamer, citation-only, ordinary Q&A neighboring owners;
9. renderer globally discoverable but standalone RA still stops at handoff;
10. unrelated global Skill/plugin does not change owner.

Every case must store：

- exact P;
- natural request;
- actual loaded/read Skill paths;
- command or no-command evidence;
- output inventory;
- owner route;
- should-not-change result.

No renderer hiding/uninstall.
No command blacklist.
No fixture/path/hash special case.
No static-string-only PASS.

Judge whether the matrix is sufficiently complete without being gratuitously large.

## C3 freeze

Only after complete matrix PASS：

C3_FINAL_CANDIDATE_COMMIT=<same P>

Any product edit after a replay forces a new provisional P and invalidates the old matrix.

After freeze, record product diff/hashes/generated parity/no-drift.

Judge whether this closes same-final-candidate integrity.

## Capability Gate impact

Read：

docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_1_2026-10-06.md

Required conclusion：

- no G5;
- G1-G4 taxonomy unchanged;
- C3 development matrix is pre-final regression/admission evidence only;
- after C3 development Critic PASS, Planner freezes a new fresh C3 pre-final packet;
- final G1-G4 are rerun from scratch on one C3;
- all C2 final evidence is regression only.

Judge whether the Plan accidentally creates a hidden fifth Gate or cross-candidate stitching.

## Offline ChatGPT Plugin preparation

Read：

docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md

C3 development success must prepare exact-C3：

- skills-only wrapper archive;
- full file/hash manifest;
- composition;
- same-C3 Clear Writing snapshots;
- guarded-update input template.

No renderer runtime bundled.
No Plugin Creator call now.
No live mutation.

Future live update must re-read current live Plugin/release identity and require one bounded user authorization.

Judge whether this avoids another last-minute G4 packaging cycle without prematurely mutating live state.

## Kickoff authorization

Review the exact Kickoff Draft.

It may authorize, only after user actually sends the Critic-approved text：

- exact branch/worktree;
- approved source/profile/test/generated changes;
- deterministic validation;
- complete development runtime matrix;
- candidate metadata/version/docs closure;
- required Clear Writing review for README;
- exact provisional/C3 commit;
- task-local evidence;
- offline wrapper prep;
- ordinary non-force push exact branch.

It must not authorize：

- live Plugin;
- final G1-G4;
- paid API;
- main merge/release;
- Bridge;
- generic pdf expansion;
- renderer engine/QA scripts;
- candidate replay infrastructure changes;
- destructive Git.

## Output

Return only：

RESULT = PASS

or

RESULT = REVISE

If REVISE, use stable blocker IDs such as：

RA-C3ER1
RA-C3ER2

Each blocker must include：

requirement
direct evidence
causal risk
minimum closure
owner

Do not reopen shared replay history or invent G5.

If PASS, explicitly bind：

APPROVED_PROPOSAL_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md

APPROVED_PROPOSAL_COMMIT=
b4820e49e3473959010afe5fa1e9f92bc0f4844f

APPROVED_PLAN_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md

APPROVED_PLAN_COMMIT=
690ea5b07a47cf8a1772dca6d293e832dbc3fadd

APPROVED_GOAL_PATH=
docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_1.md

APPROVED_GOAL_COMMIT=
da73426374f32426cb2373e19c08ae3f2fdec95d

APPROVED_KICKOFF_PATH=
docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_1.md

APPROVED_KICKOFF_COMMIT=
4ebcedd7450112c8cec54896307ba577fb0e926b

APPROVED_CAPABILITY_GATE_IMPACT_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_1_2026-10-06.md

APPROVED_PLUGIN_PREPARATION_PATH=
docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md

APPROVED_PACKAGE_PATH=
results/research-authoring--formal-production-authoring/C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_EXECUTION_PACKAGE_V0_1.md

APPROVED_PACKAGE_COMMIT=
50772a1635b9da04f1c7c014307bdae5dee67994

READY_FOR_CODEX=YES

Also state：

- PASS only authorizes bounded C3 implementation/development matrix after user sends the approved Kickoff;
- C2 remains permanent G1 FAIL;
- no final G1-G4 authorized;
- no live Plugin mutation authorized;
- no paid API;
- no main merge/release;
- if existing Skill/Profile mechanisms fail the complete matrix, implementation must STOP rather than add another wording patch.

Then, under CRITIC_ROLE_CONTRACT, output the reviewed Kickoff verbatim and set NEXT_HANDOFF=CODEX.
