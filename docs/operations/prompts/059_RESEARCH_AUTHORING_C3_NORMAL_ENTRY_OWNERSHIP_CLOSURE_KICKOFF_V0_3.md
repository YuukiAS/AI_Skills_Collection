# 059 Research Authoring C3 正常入口所有权收口 — Kickoff Draft v0.3

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_AUTHORIZED  
日期：2026-10-07

Only after independent Critic execution-ready PASS, and only when the user actually sends the approved text below, does this create implementation authorization.

## Bound package

Stable C3 Proposal：

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md`
@ `b4820e49e3473959010afe5fa1e9f92bc0f4844f`

Integrated recovery Proposal：

`docs/design/059_RESEARCH_AUTHORING_C3_INTEGRATED_OWNER_CHAIN_RECOVERY_PROPOSAL_V0_1_2026-10-07.md`
@ `b4cfef6685b232a215d56b942175bf50de415a98`

Implementation Plan v0.3：

`docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_3_2026-10-07.md`
@ `409dedc44931527e02551ac9689521655b328db3`

Canonical Goal v0.3：

`docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_3.md`
@ `89aef6c6454d449b23c953cb5a66b3c7a27a1c5a`

Capability Gate impact v0.3：

`docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_3_2026-10-07.md`
@ `c50f92484161816d9715d9b991e493277521626a`

Development Critic review：

`docs/design/059_RESEARCH_AUTHORING_C3_DEVELOPMENT_CRITIC_REVIEW_V0_1_2026-10-07.md`
@ `71cf5105570ad46ff29c492d8354b44121315a55`

## Approved Kickoff text

Continue the same 059 task.

Repository：

`YuukiAS/AI_Skills_Collection`

Task：

`research-authoring--formal-production-authoring`

Branch：

`work/research-authoring--formal-production-authoring`

Worktree：

`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

Permanent failed final candidate：

`C2=ac501d988f00cb6672fec105ae5fd51a0679cae0`

Failed provisional development attempt：

`04a17a904ce522cb4a517cb33f22e062f2bcbc09`

Do not promote either identity.

### 1. Preflight

Before edits：

1. verify exact repo/origin/branch/worktree/dirty ownership;
2. fetch origin main;
3. read current AGENTS plus approved Proposal/Plan/Goal/Critic objects above;
4. use workflow-core + ai-skills-core + Research Authoring roles;
5. do not modify Bridge or candidate replay infrastructure;
6. do not start final G1-G4.

### 2. First prove the platform mechanism

Before forming P2, run one bounded task-local current-runtime preflight using the production installer path.

Use current pinned Codex runtime and public-safe fixture only.

Prove：

- profile-installed explicit-only Skill gets destination-local `agents/openai.yaml -> policy.allow_implicit_invocation=false`;
- it is absent from implicit normal selection;
- profile routing can still cause the agent to read/use its project-local Skill path at the admitted stage;
- same-name global/user Skill remains untouched;
- project-local install/cleanup is manifest-bounded.

If this fails：

~~~text
PROFILE_SCOPED_EXPLICIT_DELEGATE_UNSUPPORTED=YES
P2_NOT_CREATED=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
~~~

Stop. Do not compensate with stronger prompt wording.

### 3. Authorized P2 source changes

Allowed shared installer/profile source：

- `profiles/research-main.json`
- `scripts/skill_utils.py`
- `scripts/skills.py`

Allowed Research Authoring source：

- `skills/writing/research/latex-paper-authoring/SKILL.md`

Allowed focused tests：

- new focused profile invocation-policy test module if needed;
- `tests/test_research_writing_routing.py`;
- directly affected installer/profile tests;
- existing renderer/Marketplace/version tests only for regression/parity.

Allowed docs/evidence required by current policy：

- candidate changelog/TODO/README/CHANGELOG parity already present on the C3 line;
- durable README Clear Writing evidence;
- task-local results/private wrapper evidence.

### 4. Explicitly unchanged canonical source

Do not further edit unless deterministic source parity itself is broken：

- research-authoring-core;
- research-reporting;
- paper-workflow-orchestrator;
- render-chinese-math-pdf;
- generic pdf;
- codex-research-writing profile;
- renderer scripts/engine/font/QA;
- candidate_plugin_replay;
- Bridge Kit.

If any becomes required for semantic repair, STOP to Planner/Critic.

### 5. Implement generic profile explicit-only support

Add one optional profile field：

`explicit_only_skills`

For `research-main`, exact set：

- `skills/writing/research/latex-paper-authoring`
- `skills/tools/documents-media/pdf`
- `skills/tools/documents-media/render-chinese-math-pdf`

The installer must generically validate and apply it; do not hard-code research-main/Skill names in installer code.

For explicit-only profile Skills：

- install project-local copy;
- never mutate canonical source;
- merge destination-local `agents/openai.yaml`;
- set `policy.allow_implicit_invocation=false`;
- preserve unrelated sidecar fields;
- record requested/actual mode and override in existing manifest.

Non-overridden Skills keep existing install behavior.

### 6. Managed AGENTS

Profile Routing Notes stay first.

Explicit-only delegates must not be repeated in ordinary Skill Routing descriptions.

Add only a compact explicit-delegate locator section, with project-local paths and a statement that these delegates are loaded only when routing notes reach their stage.

### 7. research-main routing

For new/substantial report/manuscript + PDF：

Research Authoring must be the implicit owner first.

Report route：

~~~text
Research Authoring core/report
-> source
-> handoff
-> explicit renderer delegate
-> PDF/QA
-> Research Authoring scientific QA
~~~

New or substantially revised manuscript route, whether or not the final target is PDF：

~~~text
Research Authoring core/paper
-> optional explicit LaTeX delegate only for source/package work
-> return source/package to Research Authoring
-> if final PDF requested: handoff
-> explicit renderer delegate
-> PDF/QA
-> Research Authoring scientific QA
~~~

Existing LaTeX source compile/debug/template/source-hygiene/bibliography/build troubleshooting：

~~~text
explicit latex-paper-authoring delegate directly
-> compile/debug/build allowed
~~~

Do not force Research Authoring to rewrite or re-plan the existing manuscript for this direct source-maintenance route.

Finalized-source render-only：

~~~text
explicit renderer delegate directly
~~~

Do not treat source-debug/template repair as render-only merely because the source is LaTeX.

Existing-PDF operations：

explicit generic pdf delegate directly.

The user prompt must not name internal Skills.

### 8. Fix LaTeX delegate mode

Direct existing-LaTeX compile/debug mode remains compilable.

Research Authoring delegate mode must stop at source/package + handoff.

Remove the unconditional compile requirement from delegate mode.

No final `pdflatex`/XeLaTeX/latexmk/Pandoc-to-PDF route from delegate mode.

### 9. Do not globally rewrite generic pdf or renderer again

DEV-05 direct evidence is handled by research-main profile-scoped explicit-only admission.

Do not globally narrow canonical generic pdf in this P2.

Do not add another renderer wording patch.

If current runtime still selects a global artifact Skill before Research Authoring despite the project-local policy, STOP rather than widen scope.

### 10. Deterministic validation

Run all Plan-required focused tests plus current full unit/skills/profile/Marketplace validation.

Prove profiles without `explicit_only_skills` are unchanged.

Prove source trees are not dirtied by install.

### 11. README Clear Writing

Before P2 commit/freeze, actually invoke current installed Clear Writing / writing-style on the README area changed on the C3 line.

Save durable evidence under：

`results/research-authoring--formal-production-authoring/c3_p2_readme_clear_writing/**`

Include exact README hash, natural request, actual Clear Writing Skill read/consumption trace, and result.

If wording changes, include them in P2 before matrix.

### 12. Form provisional P2

Only after preflight + deterministic validation + README evidence：

`C3_PROVISIONAL_PRODUCT_COMMIT=<P2>`

Ordinary non-force push exact task branch is authorized.

No candidate-owned product edit after P2 during matrix.

### 13. Rerun the full eleven-case matrix from zero

Do not reuse 04a17 PASS as P2 PASS.

All frozen case families rerun on exact P2.

DEV-04 must show：

Research Authoring core/report read before renderer read, then handoff, then renderer mechanics.

DEV-05 must show：

Research Authoring core/paper before LaTeX delegate; LaTeX stops at source/package; explicit renderer after handoff; generic pdf does not own new manuscript PDF; no direct pdflatex final route.

DEV-06/07 must keep standalone render-only PASS and include research-main subruns showing the explicit-only renderer remains reachable for finalized source.

DEV-07 must also include one separate natural research-main existing-LaTeX compile/debug/template/source-hygiene/build subrun. It must prove：

- latex-paper-authoring actual read > 0;
- compile/debug succeeds;
- Research Authoring does not rewrite/re-plan the existing paper;
- generic pdf does not become owner;
- render-chinese-math-pdf does not misclassify source-debug as render-only.

This remains part of DEV-07; do not create DEV-12.

DEV-08 must keep neighboring-owner checks and include research-main existing-PDF support through explicit generic pdf delegate.

DEV-09 must keep global renderer present/available; do not hide/uninstall it.

DEV-11 codex-research-writing authoring-only profile reruns unchanged.

Every run saves exact P2, profile/install policy identity, managed AGENTS hash, natural prompt, actual Skill read order, commands, outputs, owner route and verdict.

No development prompt blacklist.

### 14. Failure rule

Any matrix FAIL：

~~~text
C3_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
~~~

If profile-scoped explicit-only cannot reliably enforce current owner order, STOP and return Planner/Critic.

Do not patch the prompt, hide global Skills, edit candidate replay infrastructure or add more wording.

### 15. C3 freeze

Only full P2 matrix PASS：

`C3_FINAL_CANDIDATE_COMMIT=<same P2>`

Save C2->C3 diff, 04a17->C3 recovery diff, source/generated/profile/installer hashes, matrix manifest and no-drift proof.

### 16. Offline wrapper

The 04a17 wrapper remains historical/provisional only.

After C3 freeze, rebuild exact-C3 Research Authoring skills-only wrapper using：

`docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md`

Regenerate archive/hash manifest/composition/guarded-update input.

Do not call Plugin Creator.

### 17. Authorized terminal state

Success：

~~~text
C3_CANDIDATE_READY=YES
C3_FINAL_CANDIDATE_COMMIT=<P2>
C3_DEVELOPMENT_MATRIX=PASS
README_CLEAR_WRITING_EVIDENCE=PASS
C3_OFFLINE_WRAPPER_READY=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
~~~

### 18. Explicitly not authorized

- final G1-G4;
- live Research Authoring Plugin update;
- Plugin Creator;
- paid API;
- main merge/release/tag;
- global/user Skill mutation;
- canonical generic pdf scope expansion;
- renderer engine/QA changes;
- candidate replay changes;
- Bridge changes;
- new routing service/state/database/daemon/watcher;
- successor task;
- force/destructive Git.
