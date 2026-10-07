# 059 Research Authoring — ChatGPT to Codex scope correction kickoff v0.1

Status: `DRAFT_FOR_CRITIC_REVIEW / NOT_FINAL_GATE_AUTHORIZATION`
Date: 2026-10-07

## Approved execution boundary

Continue the same 059 task:

```text
Repository=YuukiAS/AI_Skills_Collection
Branch=work/research-authoring--formal-production-authoring
Worktree=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring
Task=research-authoring--formal-production-authoring
```

## Read first

- `docs/design/059_RESEARCH_AUTHORING_CHAT_TO_CODEX_SCOPE_CORRECTION_CRITIC_NOTE_2026-10-07.md`
- `docs/operations/prompts/059_RESEARCH_AUTHORING_CHAT_TO_CODEX_SCOPE_CORRECTION_PLANNER_HANDOFF_2026-10-07.md`
- current scope-corrected Plan / Goal / Gate matrix
- C2 G1 permanent failure evidence
- 04a17 development failure evidence

## Required cleanup

Retire the uncommitted failed explicit-only implementation attempt.

Do not retain:

- `research-main.explicit_only_skills`;
- installer policy overlay / copy-on-policy support for this recovery;
- project-local copy suppression of same-name user/global Skill;
- focused tests that only prove that mechanism.

Do retain:

- failed preflight evidence;
- C2 permanent failure evidence;
- 04a17 development failure evidence;
- Critic/Planner/design history.

## Corrected current release scope

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

The current chain is:

```text
ChatGPT Web
-> Research Authoring completes scientific content/source/handoff
-> Codex consumes exact source/handoff
-> production/render/artifact QA
-> final artifact
-> post-render scientific QA
```

## Do not do

- Do not continue explicit-only/profile-scoped renderer containment.
- Do not modify user/global Skill installation state.
- Do not hide or uninstall global renderer for tests.
- Do not add another renderer wording patch.
- Do not modify Bridge or `candidate_plugin_replay`.
- Do not add router / daemon / state machine / database.
- Do not add G5.
- Do not start final G1-G4.
- Do not call Plugin Creator or mutate live Plugin.
- Do not use paid API.
- Do not merge/release main.

## Required output

- revised current Implementation Plan;
- revised Canonical Goal;
- revised Capability Gate matrix;
- revised Kickoff;
- scope-correction result / manifest.

Run:

```bash
git diff --check
python -m unittest tests.test_research_writing_routing
python -m unittest tests.test_codex_marketplace
```

Then commit, publish the exact task branch through the bounded non-force route, and stop.

## Terminal state

```text
SCOPE_CORRECTION_READY_FOR_CRITIC=YES
FAILED_EXPLICIT_ONLY_IMPLEMENTATION_RETIRED=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
```
