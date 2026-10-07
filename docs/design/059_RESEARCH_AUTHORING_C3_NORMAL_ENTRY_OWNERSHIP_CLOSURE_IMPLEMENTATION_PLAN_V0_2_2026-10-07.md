# 059 Research Authoring C3 正常入口所有权收口 — Implementation Plan v0.2

日期：2026-10-06  
状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
Repository：YuukiAS/AI_Skills_Collection  
Task：research-authoring--formal-production-authoring  
Branch：work/research-authoring--formal-production-authoring  
Worktree：/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring

Repair Proposal：

docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md  
@ b4820e49e3473959010afe5fa1e9f92bc0f4844f

Prior execution-ready Critic review：

docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_EXECUTION_READY_CRITIC_REVIEW_V0_1_2026-10-07.md  
@ 75df537cd5f167e9df8afae9670a993cef137b58

This v0.2 changes only the development-runtime coverage needed to close stable blocker `RA-C3ER1`; the approved main repair architecture is unchanged.

## 1. Completion target

This implementation phase must close the whole normal-entry ownership problem before another final Gate is consumed.

Required result：

~~~text
C2=PERMANENT_G1_FAIL

C3_PROVISIONAL_PRODUCT_COMMIT=<P>
C3_DEVELOPMENT_MATRIX=PASS
C3_FINAL_CANDIDATE_COMMIT=<same P>
C3_OFFLINE_CHATGPT_WRAPPER=READY
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
~~~

C3 may be named/frozen only after every required development runtime case passes on the exact same provisional product commit P.

## 2. Mandatory maintenance composition

Execution uses：

~~~text
workflow-core
+ ai-skills-core
+ research-writing / Research Authoring
~~~

Roles：

- workflow-core：stage/stop/evidence/same-candidate discipline;
- ai-skills-core：source-first edits, generated parity, versions, changelog, profile/Marketplace closure;
- Research Authoring：research-document semantics and owner boundary.

Renderer owns PDF mechanics only after admission.

No component may substitute for another.

## 3. Exact production files

### 3.1 Research Authoring canonical source

Allowed：

- skills/writing/research/research-authoring-core/SKILL.md
- skills/writing/research/research-reporting/SKILL.md
- skills/writing/research/paper-workflow-orchestrator/SKILL.md
- skills/writing/research/latex-paper-authoring/SKILL.md

Required changes：

#### research-authoring-core

Add one canonical artifact/renderer admission contract：

- formal research-document PDF intent remains Research Authoring-owned until stable source/handoff;
- global renderer visibility/installation alone is not admission;
- standalone/authoring-only surface stops at source + handoff;
- integrated production is permitted only when current profile/surface explicitly authorizes Research Authoring -> renderer sequence;
- render-only finalized source is support-only and should bypass the document-planning core;
- downstream handoff includes the already-approved audience/purpose/evidence/roles/format/QA fields;
- after renderer completes in an integrated route, Research Authoring regains final scientific-QA responsibility.

The frontmatter description must also make the positive/negative boundary discoverable before the full body is loaded.

#### research-reporting

Keep report semantics unchanged.

Clarify：

- formal report PDF remains report-owned until canonical handoff;
- “renderer companion” means an explicitly admitted current production route, not any globally discoverable renderer;
- standalone formal-PDF authoring stops at source + handoff;
- integrated research-main may continue to renderer only after canonical handoff.

Do not duplicate command blacklists.

#### paper-workflow-orchestrator

Keep paper strategy unchanged.

Add the same document-owner/handoff boundary for manuscript/package final artifacts so paper-family requests do not have a weaker path than reports.

#### latex-paper-authoring

Narrow the entry boundary：

Direct owner：
- existing LaTeX compile/debug;
- template/source-hygiene repair;
- source-centric build troubleshooting.

Research Authoring delegate：
- new/substantially revised manuscript source/package after core/paper admission.

For Research Authoring-owned final PDF production：
- prepare LaTeX source/package;
- do not become the final artifact owner merely because compilation is possible;
- final PDF mechanics move through the admitted renderer route.

Do not remove normal standalone LaTeX compilation for genuinely render/build-centric tasks.

### 3.2 Renderer source

Allowed：

- skills/tools/documents-media/render-chinese-math-pdf/SKILL.md

Change metadata and Trigger Boundary, not the rendering engine.

The description must positively match：

- render-only finalized Markdown/LaTeX;
- explicit downstream document-owner handoff;
- renderer QA for an already-renderable source/artifact.

The description must explicitly not match as first owner：

- creating;
- substantively rewriting;
- reorganizing;
- scientifically revising;

a research report/manuscript merely because the requested final artifact is PDF.

Body contract：

- direct render-only remains supported;
- explicit downstream handoff remains supported;
- Research Authoring-owned authoring task must wait for handoff;
- global discoverability is not route authorization.

Expected unchanged：

- render_scientific_pdf.py;
- probe/render resources;
- font policy;
- Pandoc/XeLaTeX path;
- PDF QA implementation.

If implementation requires changing renderer mechanics scripts, STOP to Planner/Critic.

### 3.3 Profile/routing source

Allowed：

- profiles/research-main.json
- profiles/codex-research-writing.json
- scripts/codex_marketplace_config.json

#### research-main

Keep renderer installed.

Routing notes must explicitly define three shapes：

1. report/manuscript authoring + PDF:
   Research Authoring first -> stable source/handoff -> renderer -> artifact QA -> Research Authoring scientific QA;

2. finalized source + render-only:
   renderer direct;

3. generic existing-PDF manipulation:
   generic pdf helper as appropriate, not as new formal research-document author.

The profile itself is the explicit integrated-production authority.

#### codex-research-writing

Keep renderer absent.

Clarify profile description/routing notes：

- authoring/source/package profile;
- formal PDF request stops at source + handoff;
- global renderer visibility does not convert it into research-main;
- integrated production uses research-main.

#### Marketplace config

Update only Research Authoring report/paper descriptions/workflow notes needed to point at the canonical owner-admission contract.

Do not make generated aggregate prose the primary repair.

research-writing remains version 0.3.

### 3.4 Deliberately unchanged production owner

Do not modify：

- skills/tools/documents-media/pdf/SKILL.md
- Clear Writing;
- Presentations;
- Statistical Modeling;
- Bridge Kit;
- candidate_plugin_replay infrastructure.

The generic pdf Skill is a required negative/should-not-change runtime case.

If it actually steals a C3 development case, STOP. Do not widen scope automatically.

## 4. Deterministic tests

Allowed：

- tests/test_research_writing_routing.py
- tests/test_render_chinese_math_pdf.py
- existing Marketplace/version tests only when directly required by generated/version parity.

Required static contracts include：

1. renderer metadata positive examples are render-only/frozen-source or explicit downstream handoff;
2. renderer metadata contains research-document-authoring primary-owner exclusion;
3. renderer still owns finalized Markdown/LaTeX render-only;
4. Research Authoring core says global renderer visibility != admission;
5. report route uses canonical handoff;
6. paper route uses canonical handoff;
7. latex-paper-authoring preserves direct compile/debug but not premature Research Authoring final-PDF ownership;
8. research-main installs Research Authoring + renderer and emits ordered routing notes;
9. codex-research-writing remains renderer-free and emits handoff-only formal-PDF notes;
10. standalone Marketplace research-writing still does not embed renderer;
11. generated report/paper snapshots equal canonical source;
12. render-only behavior tests remain green.

Static tests support, but never replace, runtime development evidence.

## 5. Source-first generation / parity

After source edits：

~~~text
python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/build_codex_marketplace.py --write --validate --check --path-report
~~~

Generated Research Authoring/plugin files are never edited manually.

Expected generated changes may include：

- plugins/codex/plugins/research-writing/**
- .agents/plugins/marketplace.json
- registry/catalog/domain/provenance output actually changed by generators.

No unrelated generated churn.

## 6. Candidate metadata before runtime matrix

The complete provisional product commit P must already contain all behavior and version metadata that C3 would contain.

### Research Authoring

~~~text
research-writing=0.3 candidate
~~~

No 0.4 bump.

Amend docs/plugin-changelogs/research-writing.md candidate entry to include the normal-entry owner coordination.

### Renderer

Because its standalone trigger behavior changes：

~~~text
render-chinese-math-pdf:
0.2 -> 0.3 candidate
~~~

Update source skill metadata before P is created.

Update candidate-facing version/documentation parity required by current repository policy：

- README standalone skill card;
- root CHANGELOG Unreleased standalone-skill candidate note;
- docs/skill-todos/render-chinese-math-pdf.md candidate/promoted-work note as maintenance evidence;
- registry/catalog generated parity.

Repository VERSION remains 5.4.4 during this task branch.

README/change-log user-facing wording must receive actual Clear Writing review before commit. If this cannot legally run, STOP before P.

Formal repository PATCH/release remains out of scope until G1-G4 all PASS.

## 7. Provisional commit P

After source/tests/generated/version/docs are internally coherent and deterministic checks pass, create：

~~~text
C3_PROVISIONAL_PRODUCT_COMMIT=<P>
~~~

P is not yet C3.

No product file may change during the development matrix.

If any matrix failure causes a product edit：

- old runtime evidence becomes regression;
- form P2;
- rerun the complete ownership matrix on P2.

Because routing is cross-surface, do not attempt to declare only one case unaffected without independent Critic approval.

## 8. Complete C3 development runtime matrix

Evidence root：

results/research-authoring--formal-production-authoring/c3_development_matrix/

Each case must store at least：

- exact provisional product commit;
- installed/available skill/profile identities;
- natural request;
- child/runtime trace;
- actual Skill path reads;
- command trace or explicit no-command proof;
- output artifact inventory;
- owner route decision;
- should-not-change result;
- renderer/global/unrelated skill inventory relevant to the case.

No case may be passed from static text alone.

### DEV-01 standalone report + formal PDF

Environment：

- exact research-writing candidate P;
- standalone Marketplace/plugin shape;
- global render-chinese-math-pdf remains discoverable;
- do not hide/uninstall renderer.

Natural request equivalent to frozen failure.

Required：

~~~text
Research Authoring read > 0
renderer SKILL read = 0
PDF mechanics commands = 0
PDF artifacts = 0
stable Markdown/LaTeX source = YES
complete downstream production handoff = YES
~~~

This also serves counterexample A.

### DEV-02 standalone ordinary advisor report

No PDF requested.

Required：

- Research Authoring normal completion;
- no renderer;
- reader-facing report artifact/source produced.

### DEV-03 standalone manuscript + formal PDF

Environment：

- exact research-writing candidate;
- global renderer remains discoverable.

Required sequence：

~~~text
paper aggregate/core read
-> manuscript source/package
-> downstream production handoff
-> STOP
~~~

No renderer read/compile/PDF.

LaTeX delegate may prepare source/package but may not produce final PDF in this Research Authoring-owned standalone task.

### DEV-04 research-main report + formal PDF

Install exact P research-main profile into a fresh task-local project and write profile routing notes into managed AGENTS.

Required ordered evidence：

~~~text
Research Authoring core/report consumption
BEFORE
renderer consumption
BEFORE
PDF mechanics
~~~

Required real artifact：

- PDF;
- renderer receipt/QA;
- post-render Research Authoring scientific-QA receipt.

### DEV-05 research-main manuscript + PDF

Fresh research-main profile environment.

Required ordered evidence：

~~~text
Research Authoring core/paper route
-> LaTeX/source package delegate as needed
-> explicit downstream handoff
-> renderer
-> real PDF
-> renderer QA
-> final Research Authoring scientific QA
~~~

Renderer or LaTeX compile cannot pre-empt the paper owner.

### DEV-06 render-only finalized Markdown

Fresh task-local renderer-capable environment.

Natural request says source is final and asks only to render.

Required：

~~~text
renderer direct consumption > 0
Research Authoring consumption = 0
successful PDF + QA
source semantic rewrite = 0
~~~

### DEV-07 render-only finalized LaTeX

Same owner rule as DEV-06.

Required direct XeLaTeX/render path with no Research Authoring planning.

### DEV-08 neighboring owners

At minimum subcases：

A. PPT/Beamer request：
- Presentations owner;
- Research Authoring and renderer do not steal deck authoring.

B. citation-only request：
- citation/literature support owner;
- no full Research Authoring document plan;
- no renderer.

C. ordinary research Q&A：
- ordinary/domain answer;
- no document-production owner unless the request actually escalates.

This is routing evidence, not a re-validation of Presentations/citation quality.

### DEV-09 global-renderer counterexample

Separate explicit receipt proving：

- renderer is actually globally discoverable;
- standalone Research Authoring formal-PDF request still stops at handoff;
- renderer path read = 0;
- no render commands.

DEV-01 may provide the runtime body, but DEV-09 must record the environment/discovery fact explicitly rather than infer it.

### DEV-10 unrelated-global-skill counterexample

Expose at least one unrelated real Skill/plugin in the same runtime context without hiding it.

Use a task-local/public-safe unrelated capability rather than mutating remote state.

Required：

- expected Research Authoring/render owner path unchanged;
- unrelated Skill path reads = 0 for the target request;
- no owner decision changes merely because another Skill is discoverable.

### DEV-11 codex-research-writing authoring-only profile

This case directly closes `RA-C3ER1` by exercising the real profile that this implementation changes.

Environment：

- exact provisional product commit P;
- install the real `codex-research-writing` profile into a fresh task-local project;
- use the normal profile install route so managed AGENTS contains the actual profile routing notes;
- keep the profile's generic `pdf` Skill installed and visible;
- if global `render-chinese-math-pdf` is normally visible on the machine, do not hide or uninstall it;
- do not add renderer/PDF command blacklists or fixture/path/hash hints to the natural request.

Natural request：

> Take these research notes and substantially revise them into a manuscript-ready paper source, and prepare it for formal PDF production.

Equivalent natural wording is allowed only if frozen before execution and still means substantial manuscript authoring plus requested formal-PDF delivery.

Required runtime evidence：

~~~text
managed AGENTS profile routing notes present = YES
Research Authoring core/paper reads > 0
manuscript source/package produced = YES
complete downstream production handoff produced = YES
generic pdf new-document artifact ownership = NO
render-chinese-math-pdf execution = 0
PDF mechanics commands = 0
final PDF artifact = 0
~~~

Save the same evidence class as every other matrix case：

- exact P;
- natural prompt;
- installed/available profile and Skill identities;
- managed AGENTS locator/hash and direct profile-routing-note presence proof;
- actual Skill path reads;
- command/no-command trace;
- output inventory;
- owner route;
- should-not-change result.

Presence of routing notes is not sufficient by itself. The normal runtime must actually behave according to the authoring-only contract.

If the profile routing notes are present but the normal runtime still hands new-document artifact ownership to generic PDF or renderer, DEV-11 FAILs and C3 cannot freeze.

## 9. Development matrix PASS rule

All eleven cases/subcases must pass on the same P.

A matrix summary must state：

~~~text
STANDALONE_REPORT_PDF=PASS
STANDALONE_REPORT=PASS
STANDALONE_MANUSCRIPT_PDF=PASS
RESEARCH_MAIN_REPORT_PDF=PASS
RESEARCH_MAIN_MANUSCRIPT_PDF=PASS
RENDER_ONLY_MARKDOWN=PASS
RENDER_ONLY_LATEX=PASS
NEIGHBORING_OWNERS=PASS
GLOBAL_RENDERER_COUNTEREXAMPLE=PASS
UNRELATED_GLOBAL_SKILL_COUNTEREXAMPLE=PASS
CODEX_RESEARCH_WRITING_AUTHORING_ONLY_PROFILE=PASS
~~~

Any FAIL means：

~~~text
C3_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
~~~

Do not repair the development prompt against the failed output.

## 10. C3 freeze

Only after the complete development matrix passes：

~~~text
C3_FINAL_CANDIDATE_COMMIT=<same P>
~~~

No new commit is inserted between matrix evidence and product identity.

Evidence-only commits may follow, but candidate-owned files must remain identical to P.

Save：

- C2 -> C3 product diff;
- C3 product file/hash manifest;
- generated parity;
- complete matrix manifest;
- C3 -> evidence-head candidate-owned no-change proof.

## 11. Offline ChatGPT wrapper preparation before pre-final

Immediately after C3 freeze, prepare offline only：

- exact-C3 research-authoring skills-only wrapper archive;
- complete file/hash manifest;
- composition manifest;
- exact C3 source/generated identity;
- Clear Writing support snapshots from same C3;
- future guarded-update input template.

Expected wrapper identity：

~~~text
name=research-authoring
scope=USER
discoverability=PRIVATE
skills-only=YES
renderer runtime bundled=NO
~~~

Expected distribution version：

- re-read the live Plugin at future update time;
- if current live distribution remains 0.3.0, expected next wrapper version is 0.3.1;
- if live identity changed, recompute the next compatible patch and STOP on ambiguity.

Do not call Plugin Creator now.

## 12. Critic stop before final Gates

After C3 + matrix + offline wrapper are ready：

~~~text
C3_CANDIDATE_READY=YES
C3_DEVELOPMENT_MATRIX=PASS
OFFLINE_WRAPPER_READY=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
~~~

Independent Critic must inspect：

- exact C2 -> C3 diff;
- full runtime matrix, including DEV-11 codex-research-writing authoring-only profile;
- no test-only blacklist/hiding;
- version/generated parity;
- offline wrapper identity.

Only after Critic PASS does Planner freeze a new C3 pre-final G1-G4 packet.

## 13. Final Gate policy after C3

No G5.

All C2 final evidence is regression only.

New C3：

- G1 rerun on exact C3;
- G2 uses a fresh report task/delta frozen after C3;
- G3 uses fresh real manuscript evidence;
- G4 uses exact-C3 live wrapper after separate user authorization and reuses the new G2 semantic baseline.

All final PASS evidence must bind to one C3.

## 14. Rollback and stop conditions

STOP without C3 if：

- standalone still reads/uses renderer;
- research-main cannot sequence Research Authoring before renderer;
- render-only begins loading Research Authoring;
- manuscript route compiles before authoring handoff;
- generic pdf Skill steals new research-document production;
- research-main or codex-research-writing profile instructions are not actually consumed;
- renderer metadata narrowing breaks direct render-only;
- generated source no longer equals canonical source;
- README/version closure cannot legally use Clear Writing;
- fix requires a new routing framework or platform capability.

Do not react by：

- adding command blacklists;
- changing replay prompts;
- hiding/uninstalling renderer;
- modifying candidate_plugin_replay;
- creating G5;
- opening successor task.

## 15. Explicit out of scope

- live Plugin Creator/update;
- final G1-G4;
- paid API;
- main merge/release/tag;
- Bridge Kit;
- new workflow/state service;
- renderer engine/font/QA implementation;
- generic pdf Skill source unless new evidence returns to Planner/Critic;
- Presentations/Statistical Modeling/Clear Writing behavior changes.

## 16. Implementation terminal state

The bounded implementation ends only at：

~~~text
C3_CANDIDATE_READY=YES
C3_FINAL_CANDIDATE_COMMIT=<P>
C3_DEVELOPMENT_MATRIX=PASS
C3_OFFLINE_WRAPPER_READY=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
~~~

or an honest blocked/failed state before C3 freeze.
