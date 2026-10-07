# C3 ChatGPT to Codex scope correction result

Date: 2026-10-07
Task: `research-authoring--formal-production-authoring`

## Result

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

SCOPE_CORRECTION_READY_FOR_CRITIC=YES
FAILED_EXPLICIT_ONLY_IMPLEMENTATION_RETIRED=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
```

## Cleanup

The uncommitted explicit-only implementation attempt was removed from tracked source/test files. The retired attempt did not create a candidate commit.

Removed from the current tracked diff:

- `profiles/research-main.json` explicit-only profile field;
- `scripts/skills.py` profile explicit-only installer/policy overlay;
- `skills/writing/research/latex-paper-authoring/SKILL.md` delegate-mode patch made only for explicit-only recovery;
- `tests/test_research_writing_routing.py` explicit-only assertions;
- `tests/test_profile_explicit_only.py`.

Preserved evidence:

- `results/research-authoring--formal-production-authoring/c3_p2_explicit_only_preflight/PREFLIGHT_RESULT.md`
- `results/research-authoring--formal-production-authoring/c2_final/C2_FINAL_GATE_STOP_G1_FAIL.md`
- `docs/design/059_RESEARCH_AUTHORING_C3_DEVELOPMENT_CRITIC_REVIEW_V0_1_2026-10-07.md`

## Current scope-corrected package

- Plan: `docs/design/059_RESEARCH_AUTHORING_CHAT_TO_CODEX_SCOPE_CORRECTION_IMPLEMENTATION_PLAN_V0_1_2026-10-07.md`
- Goal: `docs/goals/059_RESEARCH_AUTHORING_CHAT_TO_CODEX_SCOPE_CORRECTION_GOAL_V0_1.md`
- Gate matrix: `docs/design/059_RESEARCH_AUTHORING_CHAT_TO_CODEX_CAPABILITY_GATE_MATRIX_V0_1_2026-10-07.md`
- Kickoff: `docs/operations/prompts/059_RESEARCH_AUTHORING_CHAT_TO_CODEX_SCOPE_CORRECTION_KICKOFF_V0_1.md`

## Validation

To be filled by the Executor before commit:

```text
git diff --check=PASS
tests.test_research_writing_routing=PASS
tests.test_codex_marketplace=PASS
```
