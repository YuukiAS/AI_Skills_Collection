# 059 Research Authoring — ChatGPT to Codex scope correction goal v0.1

Status: `CURRENT_SCOPE_CORRECTION_GOAL`
Date: 2026-10-07
Task: `research-authoring--formal-production-authoring`

## Objective

Restore the current Research Authoring 0.3 closure to the user-approved product chain:

```text
ChatGPT Web
-> Research Authoring authoring/source/handoff
-> Codex production/render/artifact QA
```

The current Goal is not to make Codex prove Research Authoring-vs-renderer owner competition when Codex receives the original raw scientific authoring request.

## Fixed identities

```text
C2=ac501d988f00cb6672fec105ae5fd51a0679cae0
C2_G1=PERMANENT_FAIL

PRIOR_PROVISIONAL_ATTEMPT=04a17a904ce522cb4a517cb33f22e062f2bcbc09
04a17_STATUS=FAILED_PROVISIONAL_DEVELOPMENT_ATTEMPT

UNCOMMITTED_EXPLICIT_ONLY_INSTALLER_ATTEMPT=RETIRED
P2_FROM_FAILED_PREFLIGHT=NOT_CREATED
C3_FINAL_CANDIDATE_COMMIT=NOT_ADMITTED
FINAL_GATES_NOT_STARTED=YES
```

## Required scope statements

```text
RAW_CODEX_AUTHORING_OWNER_COMPETITION=
REMOVED_FROM_CURRENT_0_3_RELEASE_BLOCKER

CHATGPT_RESEARCH_AUTHORING_NORMAL_ENTRY=
REQUIRED

CODEX_HANDOFF_PRODUCTION_CONSUMER=
REQUIRED

PROFILE_SCOPED_EXPLICIT_DELEGATE_RECOVERY=
RETIRED
```

## Product contract

ChatGPT Research Authoring must:

- understand audience and purpose;
- organize scientific content;
- preserve evidence authority and claim strength;
- produce stable Markdown / LaTeX / source package;
- produce a complete Codex production handoff;
- not pretend to run the renderer runtime.

Codex production must consume:

- exact stable source/package;
- document family;
- audience and purpose;
- evidence authority;
- allowed edit scope;
- table/figure/formula roles;
- citation authority;
- venue/project authority;
- requested production route;
- requested final artifact;
- post-render scientific QA requirement.

Codex must then produce repo-grounded files/artifacts, run appropriate production/render/file QA, and preserve scientific meaning.

## Future enhancement, not current blocker

Direct Codex standalone Research Authoring from raw scientific notes remains a known future enhancement. The observed same-name user/global renderer collision may be tracked there, but it must not block the current 0.3 ChatGPT -> Codex production chain.

## This turn

Only:

- retire the failed explicit-only implementation attempt;
- revise Plan / Goal / Gate / Kickoff scope;
- write a scope-correction result / manifest;
- run docs/config deterministic checks;
- commit and publish the exact task branch.

Do not:

- modify Research Authoring production source;
- modify Bridge or candidate replay infrastructure;
- modify user/global Skill state;
- start final G1-G4;
- call Plugin Creator or mutate live Plugin;
- merge/release main.

## Terminal state

```text
SCOPE_CORRECTION_READY_FOR_CRITIC=YES
FAILED_EXPLICIT_ONLY_IMPLEMENTATION_RETIRED=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
```
