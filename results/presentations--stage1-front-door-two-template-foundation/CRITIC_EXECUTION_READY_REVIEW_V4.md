# Presentations Stage 1 v1.2 — Execution-Ready Critic Review

**Date:** 2026-09-29  
**Review stage:** `STAGE1_EXECUTION_READY_V1_2`  
**Target repo:** `YuukiAS/AI_Skills_Collection`  
**Target plugin/domain:** `presentations`  
**Task key:** `presentations--stage1-front-door-two-template-foundation`  
**Reviewed package:** `results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_2.md`  
**Reviewed package commit:** `6fe1b561bcebec7f9a6f677bb6ce3b26b91e6ca1`  
**Current AI_Skills main inspected:** `e2b9809e1326c6d2b072e2bdbabcb368927c5d43`  
**Current Bridge main inspected:** `5a640ec02a20106c778a35ba94eb2164d2b91537`  
**Verdict:** **REVISE**

## 1. User-readable judgment

The v1.2 amendment is directionally sound.

The new #49 scope belongs in Stage 1: opening/title structure, section-aware navigation, bookmarks, footline/page-number behavior, a template-level closing primitive, and 4:3/16:9 identity are template/adapter concerns, not Stage 2 semantic sequencing or Stage 3 composition intelligence.

The package also correctly keeps #50–#53 deferred, treats 16:9 as a parameter of the same `course-standard` template, and updates the Reviewed Handoff chronology to the now-released Bridge 0.9.3 `task publish-first` entry. The old F03 blocker is closed and must not be revived.

However, the package is not yet execution-ready because two concrete execution risks remain:

1. the current Presentations production render path still contains host-specific absolute paths and duplicates environment discovery that is already owned by `render-chinese-math-pdf`; v1.2 does not freeze the cross-server portability/fail-closed contract the user now requires;
2. G5 requires direct inspection of the exact private Chapter1 reference, but the normal Reviewed Handoff Scheduled GPT Reviewer runs through the GitHub connector and explicitly has no target-machine shell access. The package names “Reviewer/human review surface” but does not bind an actual non-paid review surface that can see both the private reference and candidate renders.

These are execution-readiness blockers, not a request to reopen the overall Presentations architecture.

## 2. Passed review areas

### TODO #49

`TODO_49_VERDICT = PASS_STAGE1_TEMPLATE_FOUNDATION_SCOPE`

Current source truth at `docs/plugin-todos/presentations.md` has:

`#49 = PROMOTE_NOW`

The promoted behavior is limited to template structure/navigation and ratio-aware identity. The package does not choose the semantic closing job.

### TODO #50–#53 and adjacent backlog

`TODO_50_53_VERDICT = PASS_DEFERRED`

#50–#53 remain `NEW`. The package does not introduce presenter-learning companion logic, lecture/source pointers, assessment semantics, or semantic closing choice.

#35/#38/#40/#47/#48 are also not pulled into Stage 1 by this amendment.

### Aspect ratio

`ASPECT_RATIO_VERDICT = PASS`

The frozen contract is coherent:

```text
new course-standard no explicit ratio -> 4:3
teaching explicit 16:9 -> course-standard 16:9
existing/local edit -> preserve current ratio
external locked template -> preserve locked ratio
```

16:9 remains the same built-in template identity, not a third template and not a universal schema.

Official Beamer 3.78 supports 4:3 by default and explicit `aspectratio=169`; navigation bars and section-driven PDF bookmarks are available through normal Beamer/Hyperref mechanisms.

References:
- https://ctan.org/pkg/beamer
- https://tug.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf
- https://tug.ctan.org/macros/latex/contrib/hyperref/doc/hyperref-doc.html

### Course-standard structural identity / G5 amendment

`COURSE_STANDARD_STRUCTURE_VERDICT = PASS_SCOPE`

Opening/title frame, section-aware state/navigation, bookmarks, stable footline/page number, distinct closing primitive and ratio-aware identity are template-level fidelity concerns.

G5 correctly separates:
- actual canonical source consumption;
- independent visual/structural fidelity.

For 4:3, exact Chapter1 reference fidelity is required. For 16:9, the package correctly checks ratio plus invariant identity rather than pixel-matching 4:3 dimensions.

### Bridge 0.9.3

`BRIDGE_0_9_3_VERDICT = PASS`

Current Bridge source confirms:

```text
version = 0.9.3
formal release target =
9dad0ba4bfa54e251f345091c5151ae991251ec9
formal distribution complete = YES
```

Production CLI exposes:

```bash
ai-bridge reviewed-handoff task publish-first   --task-key <task_key>   --expected-repo <owner/repo>
```

Current implementation:
- restricts the first commit to exact REQUEST/CURRENT metadata;
- requires the exact task-derived reviewed branch/worktree;
- uses an internal empty-expect lease for atomic create-if-absent;
- validates GitHub HTTPS transport/config/hook boundaries;
- post-reads exact remote SHA before binding upstream;
- leaves raw first push and raw force-with-lease gated.

The v1.2 chronology therefore matches current Bridge production semantics.

Execution-machine freshness remains a legitimate preflight:
`BLOCKED_BRIDGE_RUNTIME_STALE` is an environment prerequisite, not historical F03.

### CI

`CI_VERDICT = PASS`

```text
ci_required = true
visual_review_required = false
text_review_required = false
paid review = NOT AUTHORIZED
```

The package preserves the legal:

`EXECUTING -> WAITING_FOR_CI / PENDING -> real GitHub CI -> implementation review`

chronology.

### Routing / release boundary

`ROUTING_REGRESSION_VERDICT = PASS`

Research, teaching, business/editable, existing/local edit, external locked template and plan-only routes remain coherent and still expose exactly two built-in templates.

`RELEASE_BOUNDARY_VERDICT = PASS`

```text
Repository bump decision = NONE
presentations = NO_BUMP
no production install/release
no main integration
no maturity promotion
```

remains correct for this reviewed-branch candidate stage.

## 3. Blocking findings

### PRES-S1-ER-F04 — Presentations render path is not yet portable across servers and does not exclusively defer environment ownership to render-chinese-math-pdf

**Requirement**

The current user requirement is that the Presentations plugin must work across the user's servers by depending on the installed `render-chinese-math-pdf` capability for render-resource/environment discovery. Reusable Presentations source must not hardcode one machine's `/home/yuukias`, `/overflow`, `/users`, TinyTeX or font paths.

If the active server lacks a required resource/package/font, the production route must fail closed. It must not silently substitute another font, renderer, Chromium route, or lower-fidelity path.

**Direct evidence**

The canonical `render-chinese-math-pdf` skill already has the correct ownership model:

`skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`

states that host-specific resource roots belong in local override/environment configuration, not reusable source. It resolves resources through project/local/environment/namespace/home/ancestor mechanisms.

Its probe requires the expected bundle-local fonts/packages and returns:

`failure_status = blocked_missing_dependency`

when they are unavailable.

Its canonical render entry exits on missing resource/dependency, and canonical PDF QA rejects unexpected fallback fonts. Chromium is diagnostic-only, not an automatic fallback.

But current Presentations production source still contains:

```python
LOCAL_RENDER_RESOURCE_DIR =
    Path("/home/yuukias/render_resources/chinese_math_pdf")
LOCAL_TINYTEX_BIN =
    Path("/home/yuukias/.TinyTeX/bin/x86_64-linux")
```

in:

`skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py`

and the normal production entry:

`generate_research_presentation_production_entry.py`

directly calls that module's `dependency_probe()`, `compile_pdf()` and `render_pdf()`.

The v1.2 Plan/Goal/Kickoff do not freeze removal of these host bindings, do not make `render-chinese-math-pdf` the single environment owner for both Beamer adapters, and do not contain a portability regression gate.

**Causal risk**

The Stage 1 candidate can pass G1/G5 on the YuukiAS workstation while still failing on Longleaf or another configured server solely because Presentations bypasses the correct render-skill resolver.

That would make a “two-template adapter foundation” PASS non-portable and would preserve the exact 0.3-era implementation defect the user just identified.

**Minimum closure condition**

Revise the complete Stage 1 package so Plan + Goal + Kickoff freeze this as a non-substitutable Stage 1 adapter invariant:

1. reusable Presentations production source/generated payload contains no host-specific render-resource, TinyTeX, TeX Live or font absolute path;
2. both built-in Beamer adapters consume `render-chinese-math-pdf` as the environment/resource-resolution owner rather than maintaining a second discovery path;
3. template-specific required resources may be checked by Presentations, but their location must derive from the render-skill resolved environment or explicit host-local override;
4. missing required resource/package/font => fail closed with the real missing dependency;
5. no silent font substitution, Chromium fallback, unrelated system-font lookup, or lower-fidelity adapter is accepted as Stage 1 completion;
6. add risk-matched regressions proving:
   - at least two different configured render-resource roots can be resolved without source changes;
   - no forbidden private host path remains in reusable Presentations source/generated payload;
   - a missing required resource/font causes a typed dependency block;
   - unexpected font fallback cannot satisfy the canonical render gate.

Do **not** redesign `render-chinese-math-pdf`: current source already provides the required portable/fail-closed semantics. Only change that skill if new direct evidence proves a defect in its current contract.

---

### PRES-S1-ER-F05 — G5 private-reference review has no executable reviewer access path

**Requirement**

G5 requires independent pixel-level qualitative review of:
- actual candidate renders;
- the exact private `Chapter1.pdf`.

The package correctly forbids committing/pushing the private reference and correctly does not authorize paid Bridge Visual Review/Terra.

An execution-ready package must therefore identify a real non-paid review surface that can directly access both artifacts.

**Direct evidence**

The v1.2 Goal says:

`Executor and implementation Reviewer must directly inspect the exact file.`

and:

`Reviewer must directly inspect renders and exact Chapter1 reference. Lack of visual access is an evidence blocker.`

The normal current Reviewed Handoff Reviewer surface, however, is explicitly GitHub-only. Current Bridge:

`templates/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md`

states:

> Scheduled GPT 的真实执行面是 GitHub connector，不是目标机器 shell。

That Reviewer can read GitHub-tracked task artifacts and checks, but it cannot directly open the unpushed server-local Chapter1 file.

The package mentions an “independent implementation Reviewer/human review surface” but does not bind a concrete owner, handoff, artifact locator or transition for that human/private review.

**Causal risk**

Execution can correctly reach CI PASS and `READY_FOR_GPT_REVIEW`, then fail deterministically because the scheduled Reviewer cannot inspect the mandatory private reference. The package has a fail-closed sentence but no executable recovery path.

That makes G5 impossible to PASS through the frozen workflow as written.

**Minimum closure condition**

Without adding paid review, freeze one concrete review path that really has direct access to both exact Chapter1 and the candidate renders.

For example, the revised package may define a specific manual/human/ChatGPT review handoff before the Scheduled GPT Reviewer PASS, provided it clearly freezes:

- who owns the G5 visual decision;
- exact private reference/candidate-render locators or transfer surface;
- how identity/hashes bind the reviewed artifacts to the implementation candidate;
- where the qualitative verdict/evidence is durably recorded;
- how the normal Reviewed Handoff Reviewer consumes that evidence without pretending it personally saw inaccessible private pixels;
- fail-closed behavior if that surface is unavailable.

Do not solve this by:
- committing/pushing Chapter1 pages;
- OCR/text-summary substitution;
- self-review by Executor;
- silently enabling paid Visual Review/Terra;
- weakening G5.

## 4. Final verdict

```text
RESULT = REVISE
REVIEW_STAGE = STAGE1_EXECUTION_READY_V1_2

REVIEWED_PACKAGE =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_2.md

REVIEWED_PACKAGE_COMMIT =
6fe1b561bcebec7f9a6f677bb6ce3b26b91e6ca1

APPROVED_PLAN_PATH =
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_2_2026-09-29.md

APPROVED_GOAL_PATH =
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_2.md

APPROVED_KICKOFF_PATH =
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_2.md

TODO_49_VERDICT = PASS_STAGE1_TEMPLATE_FOUNDATION_SCOPE
TODO_50_53_VERDICT = PASS_DEFERRED
ASPECT_RATIO_VERDICT = PASS
COURSE_STANDARD_STRUCTURE_VERDICT = PASS_SCOPE
BRIDGE_0_9_3_VERDICT = PASS
CI_VERDICT = PASS
VISUAL_REVIEW_VERDICT = REVISE_PRIVATE_REFERENCE_REVIEW_PATH_UNBOUND
ROUTING_REGRESSION_VERDICT = PASS
RELEASE_BOUNDARY_VERDICT = PASS

PRES-S1-ER-F01 = CLOSED
PRES-S1-ER-F02 = CLOSED
PRES-S1-ER-F03 = CLOSED
PRES-S1-ER-F04 = STILL_OPEN
PRES-S1-ER-F05 = STILL_OPEN

READY_FOR_CODEX = NO
NEXT_HANDOFF = PLANNER
```

No approved v1.2 Kickoff is emitted while F04/F05 remain open.

## 5. Maintenance Board pending mutation

Project mutation is not claimed from this Critic surface.

```text
Project = AI Skills Maintenance
Area = presentations
Issues = #29-#53
Status = DOING

Current execution anchor =
  results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V4.md
  @ <this review commit>

Next action =
  Planner prepares a complete same-version successor package closing
  PRES-S1-ER-F04 and PRES-S1-ER-F05,
  then independent execution-ready Critic re-review.

Source truth:
  #49 = PROMOTE_NOW
  #50-#53 = NEW
  all other maturity unchanged

Do not mark DONE / implementation-complete.
Do not close issues.
```
