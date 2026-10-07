# 059 Research Authoring C3 正常入口所有权收口 — Canonical Goal v0.3

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
日期：2026-10-07  
Repository：`YuukiAS/AI_Skills_Collection`  
Task：`research-authoring--formal-production-authoring`

Stable C3 Proposal：

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md`
@ `b4820e49e3473959010afe5fa1e9f92bc0f4844f`

Integrated-owner recovery Proposal：

`docs/design/059_RESEARCH_AUTHORING_C3_INTEGRATED_OWNER_CHAIN_RECOVERY_PROPOSAL_V0_1_2026-10-07.md`
@ `e8ede43b78d279d246c7aae81bfde782cab6dd11`

Implementation Plan：

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_3_2026-10-07.md`
@ `164c204b474839cce35c0d1a45fc86c4e703336c`

Development Critic：

`docs/design/059_RESEARCH_AUTHORING_C3_DEVELOPMENT_CRITIC_REVIEW_V0_1_2026-10-07.md`
@ `71cf5105570ad46ff29c492d8354b44121315a55`

## 1. Goal

Close the only open C3 development blocker：

`RA-C3DEV1 = integrated research-main owner chain failure`

without changing the already-accepted Research Authoring architecture.

The recovery must structurally prevent integrated-profile artifact delegates from implicit selection before Research Authoring handoff.

## 2. Current identities

~~~text
C2=
ac501d988f00cb6672fec105ae5fd51a0679cae0
C2_G1=PERMANENT_FAIL

PRIOR_PROVISIONAL_ATTEMPT=
04a17a904ce522cb4a517cb33f22e062f2bcbc09

04a17_STATUS=
FAILED_DEVELOPMENT_ATTEMPT

C3_FINAL_CANDIDATE_COMMIT=
NOT_ADMITTED
~~~

Do not promote or relabel `04a17...`.

## 3. Required P2 mechanism

Extend the normal profile installer so a profile can declare installed Skills as explicit-only.

For `research-main`, exact explicit-only delegates：

- `latex-paper-authoring`
- `pdf`
- `render-chinese-math-pdf`

Research Authoring owner Skills remain implicit.

The project-local copies of those delegates must receive：

~~~yaml
policy:
  allow_implicit_invocation: false
~~~

in destination-local `agents/openai.yaml`.

Canonical source Skills must not be mutated by installation.

## 4. Profile-installed explicit delegates

The optional profile field is：

`explicit_only_skills`

Only `research-main` gains it in this P2.

Installer must：

- validate entries are primary profile Skills;
- copy overridden Skills locally even when other Skills use symlinks;
- merge only the invocation policy into destination metadata;
- preserve unrelated sidecar metadata;
- record override/actual install mode in the existing manifest;
- keep all profiles without this field behaviorally unchanged.

## 5. Managed AGENTS contract

Profile routing notes stay first.

Explicit-only delegates must not appear in the ordinary Skill Routing description list.

Instead expose only compact delegate locators after routing notes, with a statement that they are not implicit owners and are read only when the routing stage admits them.

Do not duplicate their broad trigger descriptions.

## 6. research-main owner chain

### Report + formal PDF

~~~text
Research Authoring core/report
-> stable source
-> explicit production handoff
-> explicit renderer delegate
-> PDF + renderer QA
-> Research Authoring scientific QA
~~~

### Manuscript + PDF

~~~text
Research Authoring core/paper
-> explicit LaTeX delegate if needed
-> stable source/package + handoff
-> explicit renderer delegate
-> PDF + renderer QA
-> Research Authoring scientific QA
~~~

### Finalized render-only

~~~text
explicit renderer delegate
-> PDF + QA
~~~

No Research Authoring planning.

### Existing PDF operation

~~~text
explicit generic pdf delegate
~~~

No new research-document authorship.

## 7. LaTeX delegate mode fix

Modify canonical `latex-paper-authoring` only enough to remove the contradiction exposed by DEV-05.

Direct existing-LaTeX mode may compile.

Research Authoring delegate mode：

- source/package work only;
- no final PDF compile;
- no direct `pdflatex`/XeLaTeX/latexmk/Pandoc-to-PDF artifact route;
- return handoff for the admitted renderer.

## 8. No new wording patch

Do not further modify canonical `render-chinese-math-pdf` description/body as the primary recovery.

Do not globally modify canonical generic `pdf` in P2.

Their integrated-profile implicit availability is controlled by the project-local profile policy.

If the current runtime bypasses that policy through same-name global Skills, fail closed and return Planner/Critic.

## 9. Current-runtime preflight

Before P2 commit, use the exact production installer mechanism in a fresh task-local project.

Prove on current `codex-cli`：

- explicit-only installed copy is hidden from implicit selection;
- the profile can still route to/read that local delegate at the admitted stage;
- same-name global/user Skill remains untouched;
- local policy does not mutate user/global state.

Failure means no P2.

## 10. Allowed P2 source

Allowed：

- `profiles/research-main.json`
- `scripts/skill_utils.py`
- `scripts/skills.py`
- `skills/writing/research/latex-paper-authoring/SKILL.md`
- focused tests required by those changes
- candidate metadata/docs only as required for parity from the existing C3 line.

Expected unchanged：

- Research Authoring core/report/paper source from `04a17...`;
- canonical renderer Skill from `04a17...`;
- canonical generic pdf;
- `profiles/codex-research-writing.json`;
- renderer engine/QA scripts;
- candidate replay infrastructure;
- Bridge Kit.

## 11. README Clear Writing evidence

Before P2 can freeze, actually invoke current installed Clear Writing on the affected README reader-facing region.

Durable evidence path：

`results/research-authoring--formal-production-authoring/c3_p2_readme_clear_writing/**`

Must include：

- exact README blob/hash;
- natural review prompt;
- actual Clear Writing Skill read/consumption trace;
- decision or patch.

Self-attestation is not evidence.

## 12. P2

Only after preflight + deterministic validation + README evidence：

`C3_PROVISIONAL_PRODUCT_COMMIT=<P2>`

No candidate-owned product change while matrix runs.

Any product edit -> new provisional commit and complete matrix rerun.

## 13. Complete matrix

Rerun all eleven existing development case families on exact P2.

No 04a17 PASS can be stitched.

Critical integrated evidence：

### DEV-04

Research Authoring Skill reads must precede renderer Skill read.

### DEV-05

Research Authoring/paper must precede LaTeX delegate; LaTeX delegate must stop at source/package; renderer must be explicitly consumed after handoff; generic pdf must not own the new manuscript PDF; no direct pdflatex final route.

### DEV-06/07

Preserve standalone render-only PASS and add research-main profile subruns proving explicit-only renderer remains reachable for finalized source.

### DEV-08

Preserve prior neighboring owners and add research-main existing-PDF subrun proving explicit generic pdf support remains functional.

### DEV-11

Rerun the authoring-only `codex-research-writing` profile unchanged.

Every run stores exact P2, installed identity, policy/AGENTS identity, Skill read order, command trace, outputs and owner verdict.

## 14. C3 freeze

Only full P2 matrix PASS allows：

`C3_FINAL_CANDIDATE_COMMIT=<same P2>`

Then save diff/hash/no-drift evidence and regenerate the exact-C3 offline wrapper.

The `04a17...` wrapper is not reusable as final package.

## 15. Capability Gates

No G5.

P2 preflight and matrix remain development/admission evidence.

Final G1-G4 remain not started.

## 16. Version boundary

~~~text
research-writing=0.3 candidate
render-chinese-math-pdf=0.3 candidate
repository VERSION=5.4.4 during development/final Gates
~~~

No Research Authoring 0.4.

No live Plugin update.

## 17. Authorization ceiling

A future Critic-approved Kickoff may authorize：

- exact task branch/worktree;
- P2 source/test/profile-installer changes;
- task-local current-runtime preflight;
- deterministic/full tests;
- actual README Clear Writing invocation;
- complete 11-case matrix;
- P2/C3 commit and task evidence;
- offline exact-C3 wrapper rebuild;
- ordinary non-force push.

It does not authorize：

- final G1-G4;
- Plugin Creator/live update;
- paid API;
- main merge/release;
- global/user Skill mutation;
- canonical generic pdf expansion;
- Bridge;
- replay-infrastructure change;
- daemon/state/routing service.

## 18. Positive terminal state

~~~text
C3_CANDIDATE_READY=YES
C3_FINAL_CANDIDATE_COMMIT=<P2>
C3_DEVELOPMENT_MATRIX=PASS
README_CLEAR_WRITING_EVIDENCE=PASS
C3_OFFLINE_WRAPPER_READY=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
~~~

If the profile-scoped explicit-only mechanism is not reliable on the pinned runtime, stop without C3.
