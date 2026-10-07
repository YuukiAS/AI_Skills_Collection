# 059 Research Authoring C3 integrated owner chain recovery — Planner Proposal v0.1

日期：2026-10-07  
状态：DRAFT_FOR_CRITIC_REVIEW / NOT_IMPLEMENTATION_AUTHORIZATION  
Repository：`YuukiAS/AI_Skills_Collection`  
Task：`research-authoring--formal-production-authoring`  
Branch：`work/research-authoring--formal-production-authoring`

## 0. Authority

Prior provisional product attempt：

`04a17a904ce522cb4a517cb33f22e062f2bcbc09`

Development Critic review：

`docs/design/059_RESEARCH_AUTHORING_C3_DEVELOPMENT_CRITIC_REVIEW_V0_1_2026-10-07.md`

Critic commit：

`71cf5105570ad46ff29c492d8354b44121315a55`

Current result：

~~~text
RESULT=REVISE
C3_FINAL_CANDIDATE_COMMIT=NOT_ADMITTED
C3_CANDIDATE_READY=NO
C3_DEVELOPMENT_MATRIX=FAIL
BLOCKERS=RA-C3DEV1
FINAL_GATES_NOT_STARTED=YES
~~~

This Proposal handles only `RA-C3DEV1`. The approved C3 main architecture, standalone behavior, authoring-only profile behavior, render-only behavior, Gate taxonomy, shared replay infrastructure and Bridge boundaries remain unchanged.

## 1. New direct evidence

### DEV-04 report route

Authoritative trace：

`results/research-authoring--formal-production-authoring/c3_development_matrix/dev04_research_main_report_pdf_run2/trace/child.stdout.jsonl`

The run reports skill-description truncation due the Codex skills context budget, then actually reads：

~~~text
render-chinese-math-pdf
-> research-reporting
-> research-authoring-core
-> PDF mechanics
~~~

The renderer's C3-attempt description already said it must not first-own research-document authoring. That negative description did not enforce owner order.

### DEV-05 manuscript route

Authoritative traces：

- `.../dev05_research_main_manuscript_pdf/trace/child.stdout.jsonl`
- `.../dev05_research_main_manuscript_pdf/trace/child_continue.stdout.jsonl`

Actual early route：

~~~text
latex-paper-authoring
-> writing-fidelity
-> research-authoring-core
-> scientific-writing
-> paper-workflow-orchestrator
-> generic pdf
~~~

No `render-chinese-math-pdf` was consumed.

The run later executed direct `pdflatex` and produced the final PDF. Its own renderer evidence records：

~~~text
Renderer: pdfTeX
Route: pdflatex
~~~

This is the first direct evidence that the broad generic `pdf` capability is being selected inside the integrated new-manuscript production route.

## 2. Updated root cause

The prior C3 attempt correctly improved Skill descriptions and profile routing notes, but the integrated route still failed because those artifact capabilities remained **implicitly selectable at the same time as Research Authoring**.

The new evidence closes the remaining ambiguity：

~~~text
ROOT_CAUSE=
RESEARCH_MAIN_ARTIFACT_DELEGATES_REMAIN_IMPLICITLY_SELECTABLE
BEFORE_RESEARCH_AUTHORING_HANDOFF

SECONDARY_CAUSE=
LATEX_PAPER_AUTHORING_DELEGATE_MODE_STILL_CONTAINS
AN_UNCONDITIONAL_COMPILE_STEP
~~~

This is why more negative wording is not an adequate next repair.

## 3. Platform limitation now proven

Current official OpenAI Skill behavior remains：

- name/description are early discovery inputs;
- the model chooses relevant Skills from that metadata;
- complete Skill instructions arrive after selection.

Official OpenAI/Codex metadata also supports：

~~~yaml
policy:
  allow_implicit_invocation: false
~~~

for a Skill in `agents/openai.yaml`.

Current OpenAI Codex source distinguishes：

- hidden from implicit model prompt/catalog;
- still enabled for explicit invocation.

Sources checked for this recovery：

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/api/docs/guides/tools-skills
- https://developers.openai.com/plugins/deploy/submission-errors
- https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/references/openai_yaml.md
- https://github.com/openai/codex/blob/main/codex-rs/ext/skills/src/extension.rs
- https://github.com/openai/codex/issues/40600 for the current-main clarification of explicit invocation behavior

The repository's current profile routing notes are prompt instructions, not an invocation firewall. DEV-04 proves that they cannot by themselves guarantee “Research Authoring Skill read before renderer Skill read.”

Therefore the existing metadata + routing-note mechanism is insufficient **while competing artifact Skills remain implicitly selectable**.

## 4. Alternatives

### A. Add stronger renderer/profile wording again

REJECTED.

DEV-04 directly falsifies this as sufficient. The renderer already had a negative first-owner clause and the profile already said Research Authoring first.

The trace also reports skill-description truncation, so adding more text can make the early discovery surface worse, not stronger.

### B. Narrow canonical generic `pdf` globally

PARTIAL / NOT SELECTED AS PRIMARY REPAIR.

DEV-05 now proves generic `pdf` is a real competing owner in `research-main`.

However its broad PDF utility is shared far beyond Research Authoring. A global canonical narrowing would change unrelated PDF behavior even though the direct evidence is profile-specific.

The minimum repair should suppress its **implicit ownership on the integrated research-main surface**, while preserving explicit existing-PDF support there and preserving global behavior elsewhere.

If the P2 matrix proves a global copy still bypasses the project-local profile policy, return to Planner/Critic before widening the canonical generic PDF source.

### C. Globally set renderer/pdf/LaTeX Skills to explicit-only

REJECTED.

That would damage already-passing normal render-only and existing-PDF workflows outside `research-main`.

The requirement is surface-specific owner admission, not a global ban.

### D. Remove renderer/PDF/LaTeX from `research-main` and install them dynamically later

REJECTED.

That introduces runtime installation/mutation state into ordinary document production and is heavier than necessary.

### E. New coordinator/router/service

REJECTED.

No daemon, routing service, database, state machine or successor workflow is justified.

### F. Profile-scoped explicit delegates using the existing OpenAI invocation policy

SELECTED.

The integrated profile should install the artifact delegates locally, but mark those **installed profile copies** as explicit-only：

- `render-chinese-math-pdf`
- `latex-paper-authoring`
- generic `pdf`

They remain available after Research Authoring reaches the relevant stage, but are removed from implicit Skill selection for that profile.

The normal profile instructions then provide the ordered delegate path：

~~~text
new/substantial research document
-> Research Authoring implicit owner first
-> report/paper semantics
-> optional explicit LaTeX source delegate
-> stable source/package + handoff
-> explicit renderer delegate
-> PDF mechanics + QA
-> Research Authoring scientific QA
~~~

Finalized-source render-only and existing-PDF support remain valid by explicit profile routing.

This is a minimal profile-install policy, not a new routing framework.

## 5. Minimal new profile mechanism

Add one optional profile field, conceptually：

~~~json
{
  "explicit_only_skills": [
    "skills/writing/research/latex-paper-authoring",
    "skills/tools/documents-media/pdf",
    "skills/tools/documents-media/render-chinese-math-pdf"
  ]
}
~~~

Only `research-main` uses it in this task.

### Installer semantics

For an explicit-only profile Skill：

1. install a project-local copy, even if the requested install mode for ordinary skills is symlink;
2. preserve the Skill tree byte-for-byte except the product metadata sidecar needed for the profile policy;
3. create/merge destination-local `agents/openai.yaml` with：
   ~~~yaml
   policy:
     allow_implicit_invocation: false
   ~~~
4. preserve unrelated existing `interface` / `dependencies` / policy fields if the source Skill already has them;
5. never mutate the canonical source Skill;
6. record the profile policy override and actual install mode in the install manifest.

This must be generic profile support. No hard-coded `research-main` or Skill-name branch in installer code.

### Managed AGENTS semantics

Explicit-only delegates must **not** be re-exposed in the ordinary “Skill Routing” description list, because that would recreate an implicit routing surface in user context.

Instead, after the profile routing notes, managed AGENTS may include a compact “Profile Explicit Delegates” locator section：

~~~text
These Skills are installed but not implicit owners.
Load them only when the profile routing notes reach the stated delegate stage.

- latex-paper-authoring -> <project-local SKILL.md path>
- pdf -> <project-local SKILL.md path>
- render-chinese-math-pdf -> <project-local SKILL.md path>
~~~

No broad trigger description is repeated there.

The profile routing notes remain the ordered production contract.

## 6. Why this is more than wording

The key change is machine-consumed Skill policy：

~~~text
allow_implicit_invocation=false
~~~

on the **profile-installed copies**.

That changes what Codex can automatically select before Research Authoring has established the owner chain.

The routing notes no longer attempt to out-prompt three equally implicit artifact Skills. They tell the model when to explicitly read an installed delegate that is otherwise absent from implicit selection.

This directly attacks the failure mechanism observed in DEV-04/DEV-05.

## 7. Current-runtime capability preflight

The repository must not assume current OpenAI source behavior automatically matches pinned `codex-cli 0.153.4`.

Before forming P2, Executor performs one bounded, task-local capability preflight using the same install mechanism：

1. an explicit-only profile-installed fixture/harmless Skill is absent from implicit selection;
2. the local Skill remains readable/invokable when the profile explicitly routes to its installed path;
3. the project-local explicit-only copy shadows/controls the same-name global Skill sufficiently for the current project surface;
4. no user/global Skill is uninstalled or modified.

If any condition fails：

~~~text
PROFILE_SCOPED_EXPLICIT_DELEGATE_UNSUPPORTED=YES
P2_NOT_CREATED=YES
STOP_TO_PLANNER_CRITIC
~~~

Do not fall back to stronger prompt wording.

## 8. LaTeX delegate correction

The current `latex-paper-authoring` body has a real contradiction：

- entry boundary says Research Authoring-owned final PDF goes to the admitted renderer;
- workflow step 5 still says to compile after edits.

P2 must make the mode explicit.

### Direct existing-LaTeX mode

When the task starts as existing-source compile/debug/template/build work：

- compilation remains allowed;
- existing LaTeX behavior is preserved.

### Research Authoring delegate mode

When entered after Research Authoring/paper owner admission：

- prepare/edit source and package;
- perform source/package checks that do not create the final PDF;
- return the source/package + production handoff;
- do **not** directly run `pdflatex`, `xelatex`, `latexmk`, Pandoc-to-PDF or PDF QA;
- final PDF mechanics belong to the explicit renderer delegate.

This is semantic mode ownership, not a test command blacklist.

## 9. Generic PDF decision

Now that DEV-05 supplies direct evidence, generic `pdf` is no longer treated as a merely theoretical risk.

But the minimum P2 repair is **profile-scoped explicit-only admission**, not global canonical modification.

Within `research-main`：

- new research-document authoring cannot implicitly select generic `pdf`;
- generic existing-PDF extraction/merge/inspection remains available through the profile's explicit delegate route.

Canonical `skills/tools/documents-media/pdf/SKILL.md` remains unchanged unless P2 runtime evidence proves the local profile policy cannot contain it.

## 10. research-main routing contract

The profile notes should be compact and stage-oriented.

For a new manuscript or any substantial manuscript revision, whether or not the user ultimately requests PDF：

~~~text
FIRST: Research Authoring core/paper owner.
Before stable handoff: do not load artifact delegates merely because the source is LaTeX or the final target is PDF.
If source/package work is needed: explicitly load latex-paper-authoring in Research Authoring delegate mode.
Return source/package to the Research Authoring owner.
If final PDF is requested: after stable source/package + handoff, explicitly load render-chinese-math-pdf.
After renderer QA: return to Research Authoring scientific QA.
~~~

For an existing LaTeX source where the main task is compile/debug, template repair, source hygiene, bibliography/build troubleshooting, or existing-source build：

~~~text
explicitly load latex-paper-authoring
compile/debug/build is allowed
Research Authoring rewrite/planning is not required
~~~

For finalized Markdown/LaTeX where the task is render-only / final-artifact production：

~~~text
explicitly load render-chinese-math-pdf immediately
Research Authoring planning is not required
latex-paper-authoring is not the owner merely because the source is LaTeX
~~~

For generic existing-PDF operations：

~~~text
explicitly load pdf
~~~

These routes are intentionally distinct：

- existing-LaTeX compile/debug/source-maintenance -> LaTeX delegate direct mode;
- finalized-source render-only -> canonical renderer direct mode;
- new/substantial manuscript -> Research Authoring first, optional LaTeX delegate for source/package, renderer only after handoff if PDF is requested.

This profile remains the integrated production surface.

## 11. Production scope for P2

Expected new source scope：

- `profiles/research-main.json`
- `scripts/skill_utils.py`
- `scripts/skills.py`
- `skills/writing/research/latex-paper-authoring/SKILL.md`
- focused installer/profile/routing tests
- existing Research Authoring routing tests as needed
- generated/install documentation parity actually changed by existing generators

Keep the already-approved 04a17 Research Authoring/renderer source changes unless a deterministic parity repair is required.

Expected no new canonical change：

- `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`
- `skills/tools/documents-media/pdf/SKILL.md`
- `profiles/codex-research-writing.json`
- renderer engine/font/QA scripts
- Bridge Kit
- candidate replay infrastructure.

## 12. Should-not-change for shared installer behavior

Because the profile installer is shared, P2 must prove：

- profiles without `explicit_only_skills` install exactly as before;
- source Skills are never mutated;
- ordinary symlink/copy behavior is unchanged for non-overridden Skills;
- explicit-only overridden Skills become project-local copies with correct sidecar policy;
- manifest records the actual mode/override;
- prune/reinstall remains bounded to manifest-managed files;
- `codex-research-writing` installation remains unchanged.

No new Gate is created; this is shared-installer regression coverage.

## 13. P2 development matrix

If the preflight and deterministic tests pass, form：

`C3_PROVISIONAL_PRODUCT_COMMIT=<P2>`

Then the **entire existing 11-case matrix reruns from zero on P2**.

No 04a17 PASS is stitched into P2.

The matrix keeps the frozen user prompts/semantics.

Additional should-not-change checks are folded into existing cases, not new Gate/case families：

- DEV-06/07: confirm `research-main` can explicitly reach its hidden renderer for finalized-source render-only;
- DEV-07 also includes a natural existing-LaTeX compile/debug/template/build/source-hygiene subrun: `latex-paper-authoring` actual read > 0, compile/debug succeeds, Research Authoring does not rewrite the existing paper, generic `pdf` does not own the task, and `render-chinese-math-pdf` does not misclassify source-debug as render-only;
- DEV-08: add generic existing-PDF manipulation under `research-main` and confirm explicit `pdf` delegation still works;
- DEV-04/05: exact Skill read order must show Research Authoring owner before any explicit artifact delegate;
- DEV-05: no direct `pdflatex` bypass.

All eleven case families still bind one exact P2.

## 14. README Clear Writing durable evidence

The 04a17 product attempt changed the README standalone renderer version card, but the development packet lacked durable proof of the mandatory Clear Writing invocation.

Before P2 freeze：

1. invoke the currently installed Clear Writing / `writing-style` Skill on the affected README reader-facing region;
2. save the natural review request, actual installed Skill path read/consumption trace, exact README blob/hash reviewed, and resulting decision/patch under：
   `results/research-authoring--formal-production-authoring/c3_p2_readme_clear_writing/**`;
3. if Clear Writing requires a wording change, include it in P2 and rerun deterministic validation before the matrix;
4. if it says no change is needed, preserve that durable result without inventing a cosmetic diff.

No “I followed Clear Writing” self-assertion is sufficient.

## 15. Offline wrapper

The wrapper built from `04a17...` remains provisional historical packaging evidence only.

After P2 passes the complete matrix and is promoted to C3：

- discard it as a final candidate package;
- rebuild the offline Research Authoring skills-only wrapper from exact C3;
- regenerate file/hash manifest and guarded-update input;
- preserve the same no-renderer-runtime wrapper boundary.

No live Plugin mutation is authorized.

## 16. Version / Gate impact

No G5.

~~~text
research-writing=0.3 candidate
render-chinese-math-pdf=0.3 candidate
repository VERSION=unchanged during C3 development/final Gates
~~~

The new profile-scoped installer behavior is part of this C3 production candidate and later formal repository release closure; it does not create an `ai-skills-core` plugin bump unless that central Plugin's shipped payload is actually changed.

Final G1-G4 remain blocked until：

~~~text
P2 full 11-case matrix PASS
-> C3 freeze
-> independent C3 development Critic PASS
-> new C3 pre-final packet
-> pre-final Critic PASS
~~~

## 17. Planner decision

~~~text
RA-C3DEV1=ACCEPT

PRIMARY_RECOVERY=
RESEARCH_MAIN_PROFILE_SCOPED_EXPLICIT_ARTIFACT_DELEGATES

EXPLICIT_ONLY_DELEGATES=
latex-paper-authoring
pdf
render-chinese-math-pdf

LATEX_DELEGATE_COMPILE_CONTRADICTION=FIX

GLOBAL_GENERIC_PDF_SOURCE_CHANGE=NO
NEW_RENDERER_WORDING_PATCH=NO

PROFILE_INSTALLER_MINIMAL_EXTENSION=YES
NEW_ROUTING_FRAMEWORK=NO

04a17a904ce522cb4a517cb33f22e062f2bcbc09=
PROVISIONAL_FAILED_DEVELOPMENT_ATTEMPT

P2=NOT_CREATED
C3=NOT_ADMITTED

FULL_11_CASE_MATRIX_MUST_RERUN_ON_P2=YES
README_CLEAR_WRITING_DURABLE_EVIDENCE_REQUIRED=YES

FINAL_GATES_NOT_STARTED=YES
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
READY_FOR_IMPLEMENTATION=NO
NEXT_HANDOFF=CRITIC
~~~
