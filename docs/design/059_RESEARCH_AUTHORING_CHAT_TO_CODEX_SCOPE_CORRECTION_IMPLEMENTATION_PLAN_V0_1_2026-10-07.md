# 059 Research Authoring — ChatGPT to Codex scope correction implementation plan v0.1

Date: 2026-10-07
Task: `research-authoring--formal-production-authoring`
Branch: `work/research-authoring--formal-production-authoring`

## Status

```text
SCOPE_CORRECTION_PLAN=ACTIVE_CURRENT
SUPERSEDES_CURRENT_EXECUTION_SCOPE=059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_3
PRODUCTION_IMPLEMENTATION_AUTHORIZED=NO
FINAL_GATES_AUTHORIZED=NO
```

This plan supersedes the C3 v0.3 `explicit_only_skills` / profile-scoped renderer-containment recovery for the current Research Authoring 0.3 closure. It does not reopen the approved Research Authoring document architecture.

## Authority

- Critic note: `docs/design/059_RESEARCH_AUTHORING_CHAT_TO_CODEX_SCOPE_CORRECTION_CRITIC_NOTE_2026-10-07.md` @ `f45f9e2aca6351b586ddc82cf323421b161e7719`
- Planner handoff: `docs/operations/prompts/059_RESEARCH_AUTHORING_CHAT_TO_CODEX_SCOPE_CORRECTION_PLANNER_HANDOFF_2026-10-07.md` @ `8194480f3c6a734ac391e68cda6601b2fa2aec03`
- Original C3 architecture proposal remains historical authority for Research Authoring source/handoff boundaries: `docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md`
- C2 permanent failure remains immutable: `results/research-authoring--formal-production-authoring/c2_final/C2_FINAL_GATE_STOP_G1_FAIL.md`
- `04a17a904ce522cb4a517cb33f22e062f2bcbc09` remains a failed provisional development attempt.

## Scope correction

```text
RAW_CODEX_AUTHORING_OWNER_COMPETITION=
REMOVED_FROM_CURRENT_0_3_RELEASE_BLOCKER

CHATGPT_RESEARCH_AUTHORING_NORMAL_ENTRY=
REQUIRED

CODEX_HANDOFF_PRODUCTION_CONSUMER=
REQUIRED

PROFILE_SCOPED_EXPLICIT_DELEGATE_RECOVERY=
RETIRED

P2_FROM_FAILED_PREFLIGHT=
NOT_CREATED
```

The current 0.3 product chain is:

```text
ChatGPT Web
-> Research Authoring organizes scientific content
-> stable Markdown / LaTeX / source package
-> complete Codex production handoff
-> Codex consumes exact source + handoff
-> repo-grounded production / LaTeX / renderer / PDF QA
-> final artifact
-> post-render scientific QA
```

The task no longer tries to prove that Codex, when given the original raw scientific authoring request, can always prevent renderer/PDF/LaTeX helpers from being selected before Research Authoring.

## Required cleanup

Retire the uncommitted failed explicit-only implementation attempt:

- no `research-main.explicit_only_skills`;
- no installer policy overlay for profile-scoped explicit delegates;
- no project-local copy suppression of same-name user/global Skills;
- no focused tests that exist only for that mechanism.

Keep all failure evidence, including the P2 preflight failure evidence that proved:

```text
PROFILE_SCOPED_EXPLICIT_DELEGATE_UNSUPPORTED=YES
P2_NOT_CREATED=YES
```

## Development evidence model after correction

Future development/admission evidence must match the product chain:

1. ChatGPT / wrapper authoring side:
   - natural Research Authoring entry;
   - stable source/package;
   - complete Codex production handoff;
   - near-miss boundaries.
2. Codex production side:
   - input is exact source/package + handoff, not raw authoring notes;
   - Codex reads and preserves the scientific source/handoff;
   - Codex performs repo-grounded production, renderer/file QA, and artifact delivery;
   - Codex does not invent or rewrite scientific meaning beyond the authorized edit scope.
3. Existing production helpers:
   - finalized Markdown/LaTeX render-only remains supported;
   - existing LaTeX compile/debug/source-maintenance remains supported;
   - existing PDF operations remain supported.

Do not rerun the old research-main raw natural authoring competition matrix as a release blocker.

## Validation for this scope-correction package

This scope-correction package requires only documentation/config-scope validation:

```bash
git diff --check
python -m unittest tests.test_research_writing_routing
python -m unittest tests.test_codex_marketplace
```

It must also prove:

- failed explicit-only source/test changes are absent from tracked diff;
- historical C2 and 04a17 failure evidence remains present;
- final G1-G4 were not started.

## Terminal state

```text
SCOPE_CORRECTION_READY_FOR_CRITIC=YES
FAILED_EXPLICIT_ONLY_IMPLEMENTATION_RETIRED=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
```
