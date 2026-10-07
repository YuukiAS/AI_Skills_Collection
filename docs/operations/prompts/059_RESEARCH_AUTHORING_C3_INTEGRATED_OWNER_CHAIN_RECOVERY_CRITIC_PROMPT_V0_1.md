# 059 Research Authoring C3 integrated owner-chain recovery — Critic Prompt v0.1

你继续作为 AI Research Stack 的长期独立 Critic。

本轮只审同一个 059 / Research Authoring C3 的 integrated research-main owner-chain recovery。

不要重新设计 Research Authoring 主架构。
不要重新打开 shared candidate replay infrastructure。
不要修改 production。
不要启动 Codex Executor。
不要启动 final G1-G4。
不要调用 Plugin Creator。
不要更新 live Plugin。
不要调用 paid API。
不要 merge/release。
不要开 successor task。

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

Permanent final-failed candidate：

`C2=ac501d988f00cb6672fec105ae5fd51a0679cae0`

Failed provisional development attempt：

`04a17a904ce522cb4a517cb33f22e062f2bcbc09`

Do not promote either identity.

## Triggering Critic review

Path：

`docs/design/059_RESEARCH_AUTHORING_C3_DEVELOPMENT_CRITIC_REVIEW_V0_1_2026-10-07.md`

Commit：

`71cf5105570ad46ff29c492d8354b44121315a55`

Stable blocker：

`RA-C3DEV1 = research-main integrated production owner chain remains broken`

The review already established：

- standalone Research Authoring behavior passed development;
- `codex-research-writing` authoring-only profile behavior passed development;
- standalone render-only passed development;
- RA-C3ER1 stays CLOSED;
- `04a17...` is not C3;
- only integrated `research-main` owner order remains open.

Do not reopen already-closed areas without new evidence.

## Direct failure evidence to inspect

### DEV-04 authoritative run2

`results/research-authoring--formal-production-authoring/c3_development_matrix/dev04_research_main_report_pdf_run2/trace/child.stdout.jsonl`

Observed order：

~~~text
render-chinese-math-pdf
-> research-reporting
-> research-authoring-core
-> PDF mechanics
~~~

The trace also reports Skill-description truncation due the skills context budget.

Frozen contract required：

~~~text
Research Authoring
-> report
-> handoff
-> renderer
-> PDF mechanics
~~~

### DEV-05 manuscript

`results/research-authoring--formal-production-authoring/c3_development_matrix/dev05_research_main_manuscript_pdf/trace/child.stdout.jsonl`

`results/research-authoring--formal-production-authoring/c3_development_matrix/dev05_research_main_manuscript_pdf/trace/child_continue.stdout.jsonl`

`results/research-authoring--formal-production-authoring/c3_development_matrix/dev05_research_main_manuscript_pdf/renderer_evidence.md`

Observed：

- `latex-paper-authoring` entered early;
- generic `pdf` was actually read;
- `render-chinese-math-pdf` was not read;
- final PDF came from direct `pdflatex`;
- evidence records `Renderer: pdfTeX / Route: pdflatex`.

This is direct normal-entry evidence that generic `pdf` is no longer merely a theoretical risk inside `research-main`.

## Stable main architecture

Do not reopen：

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md`
@ `b4820e49e3473959010afe5fa1e9f92bc0f4844f`

The stable architecture remains：

~~~text
Research Authoring owner/handoff
+ renderer ownership boundary
+ profile-scoped routing
+ real runtime evidence
~~~

The current recovery only decides how the integrated profile actually enforces the already-approved order.

## Recovery execution package

### Recovery Proposal

`docs/design/059_RESEARCH_AUTHORING_C3_INTEGRATED_OWNER_CHAIN_RECOVERY_PROPOSAL_V0_1_2026-10-07.md`

commit：

`e8ede43b78d279d246c7aae81bfde782cab6dd11`

### Implementation Plan v0.3

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_3_2026-10-07.md`

commit：

`164c204b474839cce35c0d1a45fc86c4e703336c`

### Canonical Goal v0.3

`docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_3.md`

commit：

`04b5172fde45491b2dca8907c4eca31a5ebea92e`

### Capability Gate impact v0.3

`docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_3_2026-10-07.md`

commit：

`c50f92484161816d9715d9b991e493277521626a`

### Kickoff Draft v0.3

`docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_3.md`

commit：

`5cef1c89ea92cd8210f80f0d2ec13003085e727a`

### Existing exact-C3 wrapper preparation plan

`docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md`

commit：

`6320925c0b3a08f480d56f69908c40edd3b6d03e`

### Package index

`results/research-authoring--formal-production-authoring/C3_INTEGRATED_OWNER_CHAIN_RECOVERY_EXECUTION_PACKAGE_V0_1.md`

commit：

`e76e156f8bc4ca69ac51096bdd6231de2de42209`

Review all of these as one bounded recovery package.

## Required initialization

Read latest main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

Use the required central-refinement composition：

~~~text
workflow-core
+ ai-skills-core
+ research-writing / Research Authoring
~~~

Then read only the source needed to judge RA-C3DEV1：

- `profiles/research-main.json`
- `scripts/skill_utils.py`
- `scripts/skills.py`
- `skills/writing/research/latex-paper-authoring/SKILL.md`
- `skills/tools/documents-media/pdf/SKILL.md`
- `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`
- directly affected installer/profile tests.

Do not re-audit unrelated renderer engine/font/QA internals.

## Independent current-platform check

The recovery now relies on a machine-consumed OpenAI Skill policy rather than another routing sentence：

~~~yaml
policy:
  allow_implicit_invocation: false
~~~

Independently verify current official OpenAI/Codex evidence for this field and its semantics.

At minimum inspect current official docs/source around：

- Skill metadata and discovery;
- `agents/openai.yaml`;
- `policy.allow_implicit_invocation`;
- distinction between implicit model discovery and an enabled Skill remaining reachable by explicit invocation/path after profile routing.

Planner used current sources including：

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/api/docs/guides/tools-skills
- https://developers.openai.com/plugins/deploy/submission-errors
- https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/references/openai_yaml.md
- https://github.com/openai/codex/blob/main/codex-rs/ext/skills/src/extension.rs

Do not approve stronger semantics than official/current evidence supports.

Critically, repo planning does **not** assume the pinned runtime `codex-cli 0.153.4` behaves exactly like current main. The execution package requires a current-runtime task-local preflight before P2.

Judge whether that preflight is sufficient to close runtime-version uncertainty.

## Proposed recovery

Primary mechanism：

~~~text
RESEARCH_MAIN_PROFILE_SCOPED_EXPLICIT_ARTIFACT_DELEGATES
~~~

Exact integrated-profile explicit-only set：

- `latex-paper-authoring`
- generic `pdf`
- `render-chinese-math-pdf`

Research Authoring core/report/paper remain implicit owners.

Profile-installed explicit-only copies receive destination-local：

~~~yaml
policy:
  allow_implicit_invocation: false
~~~

Canonical source Skills remain unchanged by installation.

When the profile routing notes reach a delegate stage, the normal agent can explicitly read/use the project-local delegate.

## Why another wording patch is rejected

DEV-04 already had：

- a narrowed renderer description;
- Research Authoring-first profile notes.

Yet renderer was selected first.

The trace also reports description truncation.

Therefore stronger renderer/profile prose is not the selected enforcement mechanism.

Confirm this is a valid consequence of the direct evidence.

## Generic pdf decision

Prior execution package kept generic `pdf` unchanged because there was no direct evidence.

DEV-05 now supplies direct evidence：generic `pdf` was actually read in new-manuscript production.

Planner does **not** ignore that evidence.

Instead the proposed minimum repair is：

- in `research-main`, the installed generic `pdf` copy becomes explicit-only;
- existing-PDF operations can still route explicitly to it;
- canonical global `pdf` source remains unchanged because the observed defect is profile-specific and the global tool has a broader non-research blast radius.

Judge whether this is the minimum justified use of the new evidence.

If you think canonical generic `pdf` must change globally now, provide direct causal evidence that profile-scoped containment cannot address the observed failure.

## Renderer decision

The renderer's `04a17...` metadata already expresses：

- finalized render-only;
- explicit downstream handoff;
- not first owner for research-document authoring.

DEV-04 proves this metadata alone cannot enforce integrated ordering.

Planner therefore does not add a second renderer wording patch.

Instead the integrated copy becomes explicit-only.

Judge whether this is correctly targeted.

## LaTeX delegate contradiction

Current `latex-paper-authoring` says both：

- in Research Authoring route, final PDF belongs to renderer after handoff;
- workflow step 5: compile after edits.

DEV-05 then actually produced the final PDF with direct `pdflatex`.

P2 proposes a narrow canonical correction：

### Direct existing-LaTeX mode

compile/debug/template/build tasks may compile.

### Research Authoring delegate mode

source/package work only; no final PDF compile; return to renderer handoff.

Judge whether this is the minimum real source fix rather than a test-specific command blacklist.

## Minimal installer extension

Recovery adds one optional profile field：

`explicit_only_skills`

Validation：

- must be a subset of primary `skills`;
- duplicate/unknown/inactive entries rejected;
- profiles without the field retain existing semantics.

For overridden Skills only：

- project-local copy even if ordinary mode is symlink;
- destination-local `agents/openai.yaml`;
- preserve unrelated sidecar metadata;
- set `allow_implicit_invocation=false`;
- existing install manifest records requested mode / actual mode / override.

Installer code must be generic, not hard-code `research-main` or these Skill names.

Judge whether this is a small extension of the existing profile mechanism or whether it has accidentally become a new routing framework.

## Managed AGENTS

Explicit delegates must not be reprinted in the ordinary generic Skill Routing list with their broad descriptions.

Instead the profile AGENTS gets a compact path locator section after ordered profile routing notes：

~~~text
Profile Explicit Delegates
- installed but not implicit owners
- load only when routing notes reach the delegate stage
- name/path only
~~~

Judge whether this avoids reintroducing the same implicit trigger through the managed project context while keeping a normal explicit handoff path.

## Current-runtime preflight

Before P2 exists, Executor must prove with a task-local public-safe preflight on the pinned runtime：

1. explicit-only installed copy gets the correct policy;
2. it does not appear/activate in implicit normal selection;
3. profile routing can still explicitly read/use the project-local delegate;
4. same-name global/user Skill remains untouched;
5. cleanup/install remains manifest-bounded.

Failure stops with：

~~~text
PROFILE_SCOPED_EXPLICIT_DELEGATE_UNSUPPORTED=YES
P2_NOT_CREATED=YES
NEXT_HANDOFF=PLANNER
~~~

No wording fallback is allowed.

Judge whether this preflight is sufficient to prevent a speculative implementation from reaching P2.

## Production scope

Expected new P2 source changes only：

- `profiles/research-main.json`
- `scripts/skill_utils.py`
- `scripts/skills.py`
- `skills/writing/research/latex-paper-authoring/SKILL.md`
- focused tests required by these changes.

Keep prior `04a17...` accepted Research Authoring/renderer source behavior unless parity repair is mechanically required.

Expected unchanged canonical source：

- research-authoring-core;
- research-reporting;
- paper-workflow-orchestrator;
- render-chinese-math-pdf;
- generic pdf;
- codex-research-writing;
- renderer engine/QA scripts;
- candidate replay infrastructure;
- Bridge.

Judge whether this is now the minimum complete P2 scope.

## Shared-installer should-not-change

Because installer code is shared, deterministic coverage must prove：

- profiles without `explicit_only_skills` are unchanged;
- ordinary copy/symlink semantics remain unchanged;
- source Skills are never mutated;
- explicit-only Skills are destination-local copies;
- sidecar policy is merged safely;
- existing manifest records override;
- reinstall/prune remains manifest-bounded;
- `codex-research-writing` installation remains unchanged.

No new Gate is created.

Judge whether this is adequate for the shared-source blast radius.

## Full 11-case rerun

After current-runtime preflight + deterministic validation + README Clear Writing evidence, form P2.

Then rerun all eleven existing development case families from zero on P2.

No `04a17...` PASS is stitched.

Important augmented checks：

### DEV-04

Research Authoring core/report Skill reads precede renderer Skill read.

### DEV-05

Research Authoring core/paper first;
optional explicit LaTeX delegate next;
LaTeX stops at source/package;
explicit renderer after handoff;
generic pdf does not own new manuscript PDF;
no direct pdflatex final route.

### DEV-06/07

Keep standalone render-only PASS and add research-main subruns proving explicit-only renderer remains reachable for finalized source.

### DEV-08

Keep neighboring owners and add research-main existing-PDF support through explicit generic `pdf`.

### DEV-11

Rerun `codex-research-writing` authoring-only unchanged.

All eleven still bind exact one P2.

Judge whether these should-not-change additions are sufficient and do not create G5.

## README Clear Writing durable evidence

Development Critic found that `04a17...` changed the README renderer version card but no durable actual Clear Writing invocation was independently locatable.

P2 requires actual installed Clear Writing invocation before P2 freeze and durable evidence containing：

- exact README hash;
- natural review prompt;
- actual installed writing-style Skill consumption/read trace;
- decision or patch.

If Clear Writing says no wording change is needed, record that; do not create cosmetic edits.

Judge whether this closes the repository README rule.

## Offline wrapper

The `04a17...` wrapper is provisional only.

Only after P2 full matrix PASS and C3 freeze may the existing wrapper-preparation plan rebuild an exact-C3 archive/hash/composition/guarded-update input.

No live update is authorized.

## Version / Gate boundary

Keep：

~~~text
research-writing=0.3 candidate
render-chinese-math-pdf=0.3 candidate
repository VERSION=5.4.4 during development/final Gates
ADD_G5=NO
FINAL_GATES_NOT_STARTED=YES
~~~

P2 preflight/matrix are development evidence, not final G1-G4.

## Kickoff authorization

Read Kickoff v0.3 carefully.

Only if user later sends the Critic-approved text may it authorize：

- exact task branch/worktree;
- profile installer/source/test changes above;
- bounded task-local current-runtime preflight;
- actual README Clear Writing invocation;
- deterministic/full tests;
- full eleven-case P2 matrix;
- P2/C3 commit/evidence;
- exact-C3 offline wrapper rebuild;
- ordinary non-force push.

It must not authorize：

- final G1-G4;
- Plugin Creator/live update;
- paid API;
- main merge/release;
- global/user Skill mutation;
- global generic pdf change;
- Bridge;
- replay infrastructure;
- new routing daemon/state/service;
- destructive Git.

## Questions to decide

1. Does RA-C3DEV1 direct evidence justify moving integrated artifact delegates from implicit to profile-scoped explicit-only selection?
2. Is `allow_implicit_invocation=false` a real machine-consumed boundary worth probing on pinned runtime?
3. Is the current-runtime preflight strong enough to fail early if same-name global Skill visibility defeats the project-local policy?
4. Is global generic `pdf` no-change still justified now that it is contained explicitly within `research-main` and existing-PDF support is regression-tested?
5. Does the LaTeX direct/delegate mode fix close the actual direct-`pdflatex` bypass?
6. Is the shared installer extension minimal and sufficiently regression-protected?
7. Does the full P2 matrix correctly revalidate all prior behavior without stitching `04a17...` evidence?
8. Does the README Clear Writing evidence requirement close the Critic's non-blocking documentation gap?
9. Did this recovery introduce any new genuine architecture/authorization risk?
10. Can `RA-C3DEV1` recovery package be admitted for implementation?

## Output

Return only：

`RESULT = PASS`

or

`RESULT = REVISE`

If REVISE：

use stable blocker IDs, preferably `RA-C3DEV1` for unresolved parts of the same defect.

Every blocker must include：

- requirement;
- direct evidence;
- causal risk;
- minimum closure;
- owner.

Do not reopen already-closed standalone/shared-replay architecture without new direct evidence.

If PASS, explicitly bind：

~~~text
RA-C3DEV1_RECOVERY_DESIGN=PASS
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
e8ede43b78d279d246c7aae81bfde782cab6dd11

APPROVED_PLAN_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_3_2026-10-07.md

APPROVED_PLAN_COMMIT=
164c204b474839cce35c0d1a45fc86c4e703336c

APPROVED_GOAL_PATH=
docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_3.md

APPROVED_GOAL_COMMIT=
04b5172fde45491b2dca8907c4eca31a5ebea92e

APPROVED_GATE_IMPACT_PATH=
docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_3_2026-10-07.md

APPROVED_GATE_IMPACT_COMMIT=
c50f92484161816d9715d9b991e493277521626a

APPROVED_KICKOFF_PATH=
docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_3.md

APPROVED_KICKOFF_COMMIT=
5cef1c89ea92cd8210f80f0d2ec13003085e727a

APPROVED_WRAPPER_PREP_PATH=
docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md

APPROVED_WRAPPER_PREP_COMMIT=
6320925c0b3a08f480d56f69908c40edd3b6d03e

APPROVED_PACKAGE_PATH=
results/research-authoring--formal-production-authoring/C3_INTEGRATED_OWNER_CHAIN_RECOVERY_EXECUTION_PACKAGE_V0_1.md

APPROVED_PACKAGE_COMMIT=
e76e156f8bc4ca69ac51096bdd6231de2de42209
~~~

Execution-ready PASS must then set：

`NEXT_HANDOFF=CODEX`

and output the already-reviewed Kickoff v0.3 verbatim under the Critic Role Contract.

Do not write a semantically different new Kickoff after PASS.
