# 059 Research Authoring C3 正常入口所有权收口 — Execution Package v0.1

状态：READY_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_AUTHORIZED  
日期：2026-10-06

## Failure authority

Permanent failed candidate：

`C2=ac501d988f00cb6672fec105ae5fd51a0679cae0`

Final failure evidence：

`EVIDENCE_HEAD=1aa52fb737735443dee40cc205e083a3492204f7`

Failure review：

`docs/design/059_RESEARCH_AUTHORING_C2_G1_FINAL_FAILURE_CRITIC_REVIEW_V0_1_2026-10-06.md`
@ `15f2009fc4e4d276e7ed5720e92be36fe997f4ed`

Closure requirements：

`docs/design/059_RESEARCH_AUTHORING_C2_G1_FINAL_FAILURE_CLOSURE_REQUIREMENTS_V0_1_2026-10-06.md`
@ `15bba2ff6aa3f65e2301a4e90f2087a25fd95946`

## Same-version execution package

1. Repair Proposal v0.1  
   `docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md`  
   commit：`b4820e49e3473959010afe5fa1e9f92bc0f4844f`

2. Implementation Plan v0.1  
   `docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md`  
   commit：`690ea5b07a47cf8a1772dca6d293e832dbc3fadd`

3. Canonical Goal v0.1  
   `docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_1.md`  
   commit：`da73426374f32426cb2373e19c08ae3f2fdec95d`

4. Capability Gate impact v0.1  
   `docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_1_2026-10-06.md`  
   commit：`0ea6094d2046ae6290ae482131ab732656d85cd3`

5. ChatGPT Plugin offline preparation v0.1  
   `docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md`  
   commit：`6320925c0b3a08f480d56f69908c40edd3b6d03e`

6. Kickoff Draft v0.1  
   `docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_1.md`  
   commit：`4ebcedd7450112c8cec54896307ba577fb0e926b`

These six objects belong to one bounded repair. No object authorizes implementation by itself.

## Selected repair

```text
ROOT_CAUSE=
MISSING_EXECUTABLE_NORMAL_ENTRY_OWNER_ADMISSION

SELECTED_REPAIR=
RESEARCH_AUTHORING_CANONICAL_BOUNDARY
+ RENDERER_DISCOVERY_BOUNDARY
+ PROFILE_ROUTING_COORDINATION
```

The package deliberately rejects another aggregate-only wording patch.

## Three normal-entry contracts

### Standalone Research Authoring

```text
Research Authoring
-> stable scientific source/package
-> complete downstream renderer handoff
-> STOP
```

Global renderer discoverability is not renderer admission.

### research-main integrated production

```text
Research Authoring
-> explicit handoff
-> renderer
-> real PDF + renderer QA
-> Research Authoring final scientific QA
```

### True render-only

```text
finalized Markdown/LaTeX
-> renderer direct
-> PDF + QA
```

No Research Authoring planning is required.

## Platform limitation explicitly acknowledged

Current OpenAI Skills are model-selected from metadata; the model initially sees Skill name/description and reads the full Skill instructions after selecting/matching the Skill.

Current repository profiles install Skills and inject routing notes into managed AGENTS, but no hard conditional capability ACL has been identified that can make a globally installed renderer physically undiscoverable only for standalone Research Authoring while leaving the same renderer available for research-main.

Therefore this package uses the strongest existing mechanism:

```text
metadata discovery boundary
+ canonical owner/handoff
+ profile routing authority
+ actual normal-entry runtime matrix
```

If that mechanism cannot pass the complete development matrix, the task must STOP to Planner/Critic. It may not continue by adding more equivalent prose.

## Expected production scope

Allowed source areas:

- Research Authoring canonical core/report/paper/LaTeX delegate;
- render-chinese-math-pdf SKILL trigger/owner boundary;
- research-main / codex-research-writing profiles;
- Research Authoring Marketplace source config;
- focused routing/renderer tests;
- source-first generated parity;
- candidate version/changelog/README/TODO parity required by current version policy.

Expected renderer scripts/engine/font/PDF-QA code: unchanged.

Generic `pdf` Skill: inspected and deliberately unchanged unless direct development evidence returns the task to Planner/Critic.

## Development matrix

Before C3 freeze all ten matrix families must PASS on the exact same provisional product commit:

1. standalone report + formal PDF;
2. standalone ordinary advisor report;
3. standalone manuscript + formal PDF;
4. research-main report + formal PDF;
5. research-main manuscript + PDF;
6. finalized Markdown render-only;
7. finalized LaTeX render-only;
8. neighboring owners;
9. globally discoverable renderer counterexample;
10. unrelated global Skill/plugin counterexample.

Static tests do not replace runtime evidence.

## Candidate/version contract

```text
C2=PERMANENT_G1_FAIL
C3=NOT_CREATED
research-writing=0.3 candidate
render-chinese-math-pdf=0.3 candidate if the approved trigger change is implemented and the matrix passes
repository VERSION=unchanged during this bounded task
```

Research Authoring does not become 0.4.

Formal repository release integration is out of scope.

## C3 freeze and offline wrapper

Only after full matrix PASS:

`C3_FINAL_CANDIDATE_COMMIT=<same provisional product commit>`

Then prepare exact-C3 offline skills-only Research Authoring wrapper, complete hash manifest and guarded-update input.

No live Plugin mutation occurs here.

## Capability Gates

No G5.

The development matrix is pre-final regression/admission evidence only.

After C3 + matrix + offline wrapper:

```text
C3_CANDIDATE_READY=YES
C3_DEVELOPMENT_MATRIX=PASS
C3_OFFLINE_WRAPPER_READY=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
```

A later independent Critic must approve C3 before Planner freezes a new fresh C3 pre-final G1-G4 packet.

## Explicitly not authorized

- production implementation before execution-ready Critic PASS + user sending approved Kickoff;
- live Plugin Creator/update;
- final G1-G4;
- paid API;
- PDF final Gate production;
- main merge/release/tag;
- Bridge Kit changes;
- new routing framework/state service;
- successor task;
- destructive Git.

Ordinary non-force push of the exact task branch is the only planned publication route once execution is authorized.
