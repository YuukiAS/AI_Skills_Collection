# 059 Research Authoring C3 正常入口所有权收口 — Implementation Plan v0.3

日期：2026-10-07  
状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
Repository：`YuukiAS/AI_Skills_Collection`  
Task：`research-authoring--formal-production-authoring`  
Branch：`work/research-authoring--formal-production-authoring`  
Worktree：`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

Stable main Proposal：

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md`
@ `b4820e49e3473959010afe5fa1e9f92bc0f4844f`

Recovery Proposal：

`docs/design/059_RESEARCH_AUTHORING_C3_INTEGRATED_OWNER_CHAIN_RECOVERY_PROPOSAL_V0_1_2026-10-07.md`
@ `e8ede43b78d279d246c7aae81bfde782cab6dd11`

Development Critic：

`docs/design/059_RESEARCH_AUTHORING_C3_DEVELOPMENT_CRITIC_REVIEW_V0_1_2026-10-07.md`
@ `71cf5105570ad46ff29c492d8354b44121315a55`

This v0.3 supersedes Plan v0.2 for the next implementation attempt. It keeps the approved C3 architecture and changes only the integrated `research-main` enforcement needed to close `RA-C3DEV1`.

## 1. Frozen current state

~~~text
C2=
ac501d988f00cb6672fec105ae5fd51a0679cae0
C2_G1=PERMANENT_FAIL

PRIOR_PROVISIONAL_ATTEMPT=
04a17a904ce522cb4a517cb33f22e062f2bcbc09

04a17_STATUS=
PROVISIONAL_DEVELOPMENT_ATTEMPT_ONLY

RA-C3ER1=CLOSED
RA-C3DEV1=OPEN

C3_FINAL_CANDIDATE_COMMIT=
NOT_ADMITTED

FINAL_GATES_NOT_STARTED=YES
~~~

Do not reinterpret any prior PASS/FAIL.

## 2. P2 recovery mechanism

P2 must add one structural profile behavior：

`research-main` artifact delegates are installed but explicit-only.

Exact explicit-only set：

- `skills/writing/research/latex-paper-authoring`
- `skills/tools/documents-media/pdf`
- `skills/tools/documents-media/render-chinese-math-pdf`

Research Authoring core/report/paper remain implicitly discoverable.

The explicit-only delegates become available only when the profile's ordered routing contract reaches their stage.

## 3. Optional profile field

Extend current profile JSON with one optional field：

~~~json
"explicit_only_skills": [
  "skills/writing/research/latex-paper-authoring",
  "skills/tools/documents-media/pdf",
  "skills/tools/documents-media/render-chinese-math-pdf"
]
~~~

Validation contract：

1. every listed path must also be in the profile's primary `skills` list;
2. duplicate paths are invalid;
3. unknown/inactive skill paths are invalid;
4. profiles without this field retain byte-for-byte-equivalent install semantics.

Only `research-main` uses this field in P2.

Do not add it to `codex-research-writing`.

## 4. Installer implementation

Allowed shared installer source：

- `scripts/skill_utils.py`
- `scripts/skills.py`

No Bridge change.

### 4.1 Installed-copy policy overlay

For every explicit-only profile Skill：

- install a project-local copy, regardless of ordinary requested symlink mode;
- do not mutate canonical source;
- preserve every source file except destination-local product metadata necessary to apply the invocation policy;
- create or merge：
  `<installed-skill>/agents/openai.yaml`
- set only：
  ~~~yaml
  policy:
    allow_implicit_invocation: false
  ~~~
- preserve any unrelated `interface`, `dependencies`, `policy.products`, or other supported fields already present in the source sidecar;
- record the override in the install manifest.

Manifest must record at least：

~~~text
requested_mode
actual_mode
profile_explicit_only=true
source_skill_path
installed_skill_path
source_commit
~~~

Do not invent a second manifest/state system.

### 4.2 Copy-on-policy semantics

For non-overridden Skills：

- existing copy/symlink behavior remains unchanged.

For explicit-only Skills：

- use copy-on-policy;
- never edit through a symlink;
- never dirty the collection source.

### 4.3 Managed AGENTS

Keep profile routing notes before all Skill locators.

Do not repeat explicit-only delegate descriptions in the normal generic Skill Routing list.

Instead emit a compact section：

~~~text
## Profile Explicit Delegates

These Skills are installed for this profile but are not implicit owners.
Read them only when the Profile Routing Notes reach their stated stage.

- <name>: Path: <project-local SKILL.md>
~~~

This section is a locator, not a second routing policy.

Normal Skill Routing remains unchanged for ordinary implicit Skills.

## 5. research-main profile routing

Modify：

`profiles/research-main.json`

Add `explicit_only_skills` above.

Keep routing notes compact and stage-ordered.

Required semantics：

### New/substantial report + PDF

~~~text
FIRST Research Authoring core/report
-> stable source
-> complete production handoff
-> explicitly load render-chinese-math-pdf
-> renderer mechanics/QA
-> Research Authoring scientific QA
~~~

### New/substantial manuscript + PDF

~~~text
FIRST Research Authoring core/paper
-> explicitly load latex-paper-authoring only if source/package work needs it
-> source/package + handoff
-> explicitly load render-chinese-math-pdf
-> renderer mechanics/QA
-> Research Authoring scientific QA
~~~

### Finalized-source render-only

~~~text
explicitly load render-chinese-math-pdf immediately
-> render/QA
~~~

No Research Authoring planning.

### Existing-PDF manipulation

~~~text
explicitly load pdf
~~~

No new research-document authorship.

The profile notes must not depend on the user naming internal Skill names.

## 6. Pinned-runtime capability preflight

Before P2 product commit, prove the profile mechanism on the pinned current runtime.

Runtime under current evidence line：

`codex-cli 0.153.4`

Use a task-local fresh project and public-safe fixture only.

Required preflight：

1. install a profile with one explicit-only harmless fixture/Skill using the same production installer mechanism;
2. verify its destination `agents/openai.yaml` has `allow_implicit_invocation=false`;
3. verify it is not implicitly selected/read on a natural prompt that would otherwise match;
4. verify profile routing can still cause the agent to read/use its project-local Skill path when the ordered profile instruction explicitly reaches that delegate stage;
5. keep any same-name global/user Skill untouched;
6. prove project-local policy does not mutate user/global Skill state.

If the local explicit-only policy does not reliably suppress the integrated project's implicit selection：

~~~text
PROFILE_SCOPED_EXPLICIT_DELEGATE_UNSUPPORTED=YES
P2_NOT_CREATED=YES
NEXT_HANDOFF=PLANNER
~~~

Do not proceed with wording changes.

## 7. LaTeX delegate repair

Modify：

`skills/writing/research/latex-paper-authoring/SKILL.md`

No new Skill.

Replace the current contradictory unconditional compile behavior with an explicit two-mode contract.

### Direct existing-LaTeX mode

Use when the task starts as：

- compile/debug;
- template repair;
- bibliography/build troubleshooting;
- existing-source render/build.

Compilation remains allowed.

### Research Authoring delegate mode

Use when Research Authoring/paper owner has already admitted the Skill for source/package work.

Required：

- edit/organize LaTeX source/package;
- preserve venue/template authority;
- validate source/package structure;
- return source/package + handoff;
- do not produce the final PDF;
- do not execute final PDF mechanics.

The workflow step equivalent to “compile after edits” must be conditional on direct mode.

This closes the actual DEV-05 contradiction rather than adding a command-specific test exception.

## 8. Canonical generic pdf decision

Do not modify：

`skills/tools/documents-media/pdf/SKILL.md`

in this P2 attempt.

DEV-05 has proven it is a real competing owner **inside research-main**, so its research-main installed copy becomes explicit-only.

Why no global change：

- direct evidence is surface-specific;
- global `pdf` supports unrelated existing-PDF/simple-PDF work;
- profile-scoped policy is narrower and structurally stronger than another canonical description clause.

If the P2 current-runtime matrix still reads a global generic `pdf` before the project-local policy can contain it：

STOP and return to Planner/Critic.

Executor may not widen scope.

## 9. Canonical renderer decision

Do not further modify：

`skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`

unless source/generated parity repair is mechanically necessary.

Its 04a17 metadata already expresses the intended boundary and render-only behavior already passed.

DEV-04 proves that metadata alone is not the enforcement layer for integrated production.

P2 moves integrated enforcement to profile-scoped explicit-only policy.

## 10. Research Authoring source decision

Keep the approved 04a17 C3-attempt Research Authoring core/report/paper owner/handoff behavior.

No new aggregate-only wording patch.

Expected Research Authoring source modification in P2：

- `latex-paper-authoring/SKILL.md` only, for the direct/delegate compile mode contradiction.

If implementation discovers another Research Authoring source change is genuinely required, STOP rather than silently widen the P2 delta.

## 11. Exact production source scope

Allowed P2 source：

- `profiles/research-main.json`
- `scripts/skill_utils.py`
- `scripts/skills.py`
- `skills/writing/research/latex-paper-authoring/SKILL.md`

Allowed tests：

- add one focused profile invocation-policy test module if cleaner;
- existing `tests/test_research_writing_routing.py`;
- installer/profile validation tests directly affected by the new optional field;
- existing renderer/Marketplace/version tests only for regression/parity.

Allowed candidate documentation/evidence：

- current Research Authoring/renderer candidate changelog/TODO/README/CHANGELOG only where P2 still needs parity from 04a17;
- README Clear Writing durable evidence;
- task results/private wrapper outputs.

Expected unchanged canonical source：

- research-authoring-core;
- research-reporting;
- paper-workflow-orchestrator;
- render-chinese-math-pdf;
- generic pdf;
- codex-research-writing profile;
- renderer scripts;
- candidate replay infrastructure;
- Bridge.

## 12. Deterministic tests

At minimum add tests for：

### Profile schema

- valid `explicit_only_skills` subset accepted;
- unknown/non-primary/duplicate paths rejected;
- old profiles without field unchanged.

### Installer

- explicit-only Skill uses destination copy even when requested mode is symlink;
- source tree unchanged;
- destination `agents/openai.yaml` policy false;
- existing sidecar fields preserved;
- manifest reports requested/actual mode and policy override;
- reinstall replaces only manifest-owned destination;
- prune remains bounded.

### AGENTS

- explicit delegates absent from normal Skill Routing descriptions;
- explicit delegates present in compact locator section;
- profile routing notes precede delegate locator;
- non-explicit profiles produce the same AGENTS structure as before.

### Research routing

- research-main explicit-only set exactly contains LaTeX/pdf/renderer;
- research-main ordered route covers report/manuscript/render-only/existing-PDF;
- codex-research-writing remains unchanged and renderer-free;
- LaTeX direct/delegate modes are distinct;
- delegate mode does not instruct final compile.

### Regression

- full unit discovery;
- skills validate/audit;
- Marketplace generator;
- representative unaffected profile install in both ordinary copy/symlink semantics as appropriate.

Static PASS remains supporting evidence only.

## 13. Provisional P2

Only after：

- current-runtime explicit-only preflight PASS;
- source/tests/generated parity PASS;
- README Clear Writing durable evidence closed;
- candidate metadata coherent;

form：

`C3_PROVISIONAL_PRODUCT_COMMIT=<P2>`

The prior：

`04a17a...`

remains a failed development attempt.

No candidate-owned product edit after P2 while the matrix is running.

## 14. README Clear Writing evidence

Before P2 commit/freeze, perform the repository-required actual Clear Writing invocation for the README area changed on the C3 line.

Save durable evidence under：

`results/research-authoring--formal-production-authoring/c3_p2_readme_clear_writing/`

Required：

- exact README blob/hash reviewed;
- natural review prompt;
- actual installed Clear Writing Skill path read/consumption trace;
- result;
- if changed, exact diff and resulting README blob.

If no wording change is required, record that result; do not manufacture a diff.

If actual Clear Writing invocation cannot be proven：

`P2_NOT_READY=YES`

## 15. Full 11-case matrix rerun

All eleven existing case families rerun from zero on P2.

No 04a17 runtime PASS contributes to P2 PASS.

Frozen prompts/tasks remain unchanged except environment mechanics required to install P2.

### DEV-04 report integrated production

Must prove exact path order：

~~~text
research-authoring-core/report read
-> stable handoff
-> explicit renderer read
-> renderer mechanics
~~~

No renderer Skill read before Research Authoring owner.

### DEV-05 manuscript integrated production

Must prove：

~~~text
research-authoring-core/paper
-> optional explicit latex-paper-authoring delegate
-> source/package + handoff
-> explicit render-chinese-math-pdf
-> PDF + canonical renderer QA
-> Research Authoring scientific QA
~~~

Forbidden：

- generic `pdf` read as new-document artifact owner;
- direct `pdflatex` final route;
- final PDF produced by LaTeX delegate before renderer handoff.

### DEV-06/07 render-only

Preserve existing standalone direct renderer evidence.

Also add a research-main-profile should-not-change subrun proving its explicit-only installed renderer remains reachable for finalized Markdown/LaTeX render-only without Research Authoring planning.

This is a subrun, not a twelfth Gate/case family.

### DEV-08 neighboring owners

Add one research-main existing-PDF support subrun：

- existing PDF input;
- generic `pdf` explicitly delegated by profile;
- PDF support operation succeeds;
- no Research Authoring document planning.

Preserve PPT/Beamer, citation-only and ordinary Q&A subcases.

### DEV-09

Global renderer remains genuinely present/available; project-local explicit-only policy must still prevent premature integrated/standalone owner theft as applicable.

### DEV-11

codex-research-writing authoring-only profile reruns unchanged on P2.

## 16. Matrix evidence

Every case/subrun saves：

- exact P2;
- installed profile manifest;
- explicit-only policy locators where relevant;
- managed AGENTS hash;
- natural prompt;
- actual Skill path read order;
- command trace;
- output inventory;
- owner route;
- should-not-change status.

For integrated cases, record the ordinal index of every Research Authoring / LaTeX / pdf / renderer Skill read so order is mechanically auditable.

## 17. P2 matrix failure

Any FAIL：

~~~text
C3_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
~~~

If failure shows profile-scoped explicit-only itself cannot enforce owner order on current Codex：

STOP.

Do not：

- strengthen the development prompt;
- hide/uninstall global Skills;
- switch to test-only config;
- add another routing sentence;
- edit replay infrastructure.

A new architecture decision would require Planner/Critic.

## 18. C3 freeze

Only if the complete P2 matrix passes：

~~~text
C3_FINAL_CANDIDATE_COMMIT=<same P2>
C3_DEVELOPMENT_MATRIX=PASS
~~~

Then create：

- C2 -> C3 product diff;
- P1(04a17) -> C3 recovery diff;
- source/generated/profile/installer hashes;
- matrix manifest;
- candidate-owned no-drift proof.

## 19. Offline wrapper rebuild

The 04a17 wrapper is never promoted.

After C3 freeze, rebuild the offline Research Authoring skills-only wrapper from exact C3.

Reuse：

`docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md`

but regenerate：

- archive;
- file/hash manifest;
- composition;
- guarded-update template;
- same-C3 Clear Writing support snapshots.

No live Plugin mutation.

## 20. Capability Gate impact

No G5.

The profile-policy preflight and full P2 matrix remain development/admission evidence.

All final G1-G4 must later run fresh on one exact C3.

## 21. Version decision

Keep：

~~~text
research-writing=0.3 candidate
render-chinese-math-pdf=0.3 candidate
repository VERSION=5.4.4 during development/final Gates
~~~

No Research Authoring 0.4.

No new standalone renderer bump beyond the already-planned 0.3 candidate.

The profile installer change is repository install behavior; formal repository PATCH integration remains after final G1-G4 PASS.

## 22. Stop / rollback

Stop before P2 or C3 if：

- pinned runtime does not support the profile explicit-only mechanism;
- project-local explicit-only copy fails to contain a same-name global Skill;
- explicit renderer cannot be reached after handoff;
- generic PDF existing-PDF support becomes unusable;
- LaTeX direct mode regresses;
- any shared profile without override changes behavior;
- source tree is dirtied by profile install;
- README Clear Writing evidence remains missing.

No destructive rollback is needed: profile installs are task-local/manifest-managed and product changes remain on the task branch.

## 23. Terminal state

Successful bounded execution：

~~~text
C3_CANDIDATE_READY=YES
C3_FINAL_CANDIDATE_COMMIT=<P2>
C3_DEVELOPMENT_MATRIX=PASS
README_CLEAR_WRITING_EVIDENCE=PASS
C3_OFFLINE_WRAPPER_READY=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
~~~

Otherwise stop honestly before C3.
