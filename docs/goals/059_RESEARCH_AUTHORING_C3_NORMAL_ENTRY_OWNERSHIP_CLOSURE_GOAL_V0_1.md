# 059 Research Authoring C3 正常入口所有权收口 — Canonical Goal v0.1

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
日期：2026-10-06  
Repository：YuukiAS/AI_Skills_Collection  
Task：research-authoring--formal-production-authoring

Repair Proposal：

docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md  
@ b4820e49e3473959010afe5fa1e9f92bc0f4844f

Implementation Plan：

docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md  
@ 690ea5b07a47cf8a1772dca6d293e832dbc3fadd

## 1. Goal

Close the current 059 Research Authoring version by making normal-entry ownership reliable across：

~~~text
standalone Research Authoring
integrated research-main production
true render-only
~~~

without adding a new router or workflow.

C2 remains a permanent failed candidate：

~~~text
C2=
ac501d988f00cb6672fec105ae5fd51a0679cae0

C2_G1=FAIL
~~~

A new C3 may exist only after the complete development matrix passes.

## 2. Required mechanism

Implement the selected existing-layer coordination：

~~~text
renderer discovery metadata
+ Research Authoring canonical owner/handoff
+ profile routing authority
~~~

### Standalone Research Authoring

Research report/manuscript authoring with eventual PDF：

~~~text
Research Authoring
-> stable source/package
-> complete downstream production handoff
-> STOP
~~~

A globally discoverable renderer is not sufficient authorization.

### research-main

Research report/manuscript + PDF：

~~~text
Research Authoring first
-> explicit handoff
-> render-chinese-math-pdf
-> real PDF + renderer QA
-> Research Authoring final scientific QA
~~~

### Render-only

Already-final Markdown/LaTeX：

~~~text
render-chinese-math-pdf direct owner
-> PDF + QA
~~~

Do not force a Research Authoring document-planning pass.

## 3. Required source edits

Allowed Research Authoring source：

- skills/writing/research/research-authoring-core/SKILL.md
- skills/writing/research/research-reporting/SKILL.md
- skills/writing/research/paper-workflow-orchestrator/SKILL.md
- skills/writing/research/latex-paper-authoring/SKILL.md

Allowed renderer source：

- skills/tools/documents-media/render-chinese-math-pdf/SKILL.md

Allowed profile/routing source：

- profiles/research-main.json
- profiles/codex-research-writing.json
- scripts/codex_marketplace_config.json

Allowed tests：

- tests/test_research_writing_routing.py
- tests/test_render_chinese_math_pdf.py
- directly required existing parity/version tests only.

Generated output must come from canonical generators.

Do not hand-edit generated Marketplace Research Authoring files.

## 4. Trigger-boundary requirements

### Renderer

Its discovery description/Trigger Boundary must identify it as：

- direct owner for finalized-source render-only tasks;
- downstream owner after explicit document-owner handoff.

It must not self-select as first owner merely because a research report/manuscript authoring request says PDF.

### Research Authoring

The canonical core must define：

~~~text
renderer installed/discoverable != renderer admitted
~~~

and must distinguish：

- standalone/authoring-only -> handoff then stop;
- integrated research-main -> handoff then renderer;
- render-only finalized source -> route away from Research Authoring.

### Manuscript / LaTeX

New or substantially revised manuscript production enters Research Authoring/paper first.

latex-paper-authoring remains direct owner for genuine existing-LaTeX compile/debug/source-hygiene work, but does not become the final artifact owner inside a Research Authoring manuscript workflow before handoff.

## 5. Profile requirements

### research-main

Must remain the full integrated formal-production profile and must install the renderer.

Its routing notes must define：

- report + PDF owner order;
- manuscript + PDF owner order;
- render-only direct renderer route;
- generic pdf helper not being the creator-owner for new research documents.

### codex-research-writing

Must remain renderer-free.

Its description/routing notes must state that formal research-document PDF production stops at source/package + handoff; integrated production belongs to research-main.

## 6. Explicit should-not-change

Do not modify unless direct development evidence forces a new Planner/Critic round：

- skills/tools/documents-media/pdf/SKILL.md
- renderer scripts/engine/font/QA implementation
- Clear Writing
- Presentations
- Statistical Modeling
- Bridge Kit
- candidate_plugin_replay infrastructure

Do not solve this by hiding/uninstalling any competing Skill.

## 7. Deterministic validation

Before runtime matrix：

~~~text
python -m unittest tests.test_research_writing_routing
python -m unittest tests.test_render_chinese_math_pdf
python -m unittest tests.test_codex_marketplace
python -m unittest discover -s tests
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/build_codex_marketplace.py --write --validate --check --path-report
git diff --check
~~~

Use current canonical equivalents if command names have changed.

Static PASS cannot substitute for runtime matrix.

## 8. Provisional product identity and versions

Implement the full production change and candidate metadata first, then form：

~~~text
C3_PROVISIONAL_PRODUCT_COMMIT=<P>
~~~

It must already include：

~~~text
research-writing=0.3 candidate
render-chinese-math-pdf=0.3 candidate
repository VERSION=unchanged 5.4.4
~~~

Research Authoring does not become 0.4.

Candidate metadata closure includes required README/CHANGELOG/changelog/TODO/generated parity. Any README user-facing change requires actual Clear Writing review.

P is not C3 until runtime development matrix passes.

## 9. Complete development matrix

All cases run on exact P.

Required：

1. standalone report + formal PDF -> source + handoff, zero PDF mechanics;
2. standalone ordinary advisor report -> normal Research Authoring completion;
3. standalone manuscript + formal PDF -> source/package + handoff, zero renderer mechanics;
4. research-main report + formal PDF -> Research Authoring first, renderer second, real PDF;
5. research-main manuscript + PDF -> paper owner first, renderer second, real PDF;
6. finalized Markdown render-only -> renderer direct;
7. finalized LaTeX render-only -> renderer direct;
8. neighboring owner:
   - PPT/Beamer;
   - citation-only;
   - ordinary research Q&A;
9. renderer globally discoverable but standalone Research Authoring still stops at handoff;
10. unrelated global Skill/plugin presence does not change owner.

For every case preserve：

- exact P;
- natural prompt;
- loaded/read Skill paths;
- command trace or no-command evidence;
- outputs;
- owner route;
- should-not-change result.

No prompt command blacklist.

## 10. C3 freeze

Only if every matrix case passes and no candidate-owned file changes afterward：

~~~text
C3_FINAL_CANDIDATE_COMMIT=<same P>
~~~

If any product edit follows a replay, form a new P and rerun the matrix.

After C3 freeze save：

- C2 -> C3 diff;
- C3 source/generated hashes;
- matrix manifest;
- C3 -> evidence-head no-drift proof.

## 11. Offline ChatGPT Plugin preparation

Before pre-final Critic, prepare exact-C3：

- skills-only research-authoring wrapper archive;
- file/hash manifest;
- composition;
- Clear Writing support snapshots from same C3;
- future guarded-update input.

Do not mutate live Plugin.

Future expected wrapper distribution：

~~~text
if current live remains 0.3.0:
    next expected distribution = 0.3.1
else:
    re-read and compute next compatible patch
~~~

No renderer runtime is bundled into the ChatGPT wrapper.

## 12. Capability Gates

No G5.

C3 development matrix is regression/admission evidence only.

After independent C3 development Critic PASS：

- Planner freezes a new C3 pre-final packet;
- final G1-G4 execute from scratch on C3;
- all C2 final evidence is regression only.

## 13. Stop conditions

Stop without C3 if any of these remain：

- standalone authoring reads renderer or creates PDF;
- research-main renderer runs before Research Authoring handoff;
- render-only loads Research Authoring;
- manuscript compile bypasses paper owner;
- generic pdf steals new research-document production;
- owner/profile instructions are not actually consumed;
- renderer direct render-only regresses;
- generated parity fails;
- version/README closure cannot satisfy repository policy.

Do not respond by adding a G1-only prompt or command blacklist.

## 14. Authorization ceiling

A future Critic-approved Kickoff may authorize：

- exact task branch/worktree;
- approved production source/profile/test edits;
- source-first generation;
- candidate metadata closure;
- Clear Writing review required for README;
- deterministic tests;
- complete development runtime matrix;
- task-local artifacts/evidence;
- exact P/C3 commit;
- offline wrapper archive;
- ordinary non-force push exact branch.

It does not authorize：

- live Plugin Creator/update;
- final G1-G4;
- paid API;
- main merge/release/tag;
- Bridge changes;
- new routing infrastructure;
- destructive Git.

## 15. Positive terminal state

~~~text
C3_CANDIDATE_READY=YES
C3_FINAL_CANDIDATE_COMMIT=<P>
C3_DEVELOPMENT_MATRIX=PASS
C3_OFFLINE_WRAPPER_READY=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
~~~

This is not final Research Authoring 0.3 acceptance.
