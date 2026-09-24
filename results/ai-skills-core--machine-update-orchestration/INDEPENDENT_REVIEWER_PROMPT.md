# Independent Reviewer Prompt - IR-B004 Third-Round Minimal Closure

Task: `ai-skills-core--machine-update-orchestration`

Do not redesign V2.1. Do not reopen already closed product findings unless this control-doc repair unexpectedly changed production/generated payload.

## Reviewed identities

- repository: `YuukiAS/AI_Skills_Collection`
- branch: `reviewed/ai-skills-core--machine-update-orchestration`
- reviewed product candidate: `4b8414733f3efc2d8707c5fbf448cbe8ec7a7d00`
- prior evidence/handoff tip: `fb31f539058c634568401d2376ff3e64af7417bb`
- current handoff tip: verify the final docs-only task-branch tip

Finding state:

- `IR-B001 = CLOSED`
- `IR-B002 = CLOSED`
- `IR-B003 = CLOSED`
- `IR-B004 = REVIEW THIS CONTROL CLOSURE ONLY`

## Read

From latest `main`:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

From the task branch:

- `results/ai-skills-core--machine-update-orchestration/REVIEWER_HANDOFF.md`
- `results/ai-skills-core--machine-update-orchestration/POST_REVIEW_PROMOTION_G2_RUNBOOK.md`
- `results/ai-skills-core--machine-update-orchestration/IR_B004_MAINTENANCE_BOARD_PENDING_MUTATION.md`
- `docs/plugin-todos/ai-skills-core.md`

## Verify only IR-B004

1. The runbook uses reviewed product candidate `4b8414733f3efc2d8707c5fbf448cbe8ec7a7d00`, not stale `12ca08dc...`.
2. Promotion fetches latest main and checks for new ai-skills-core production/version/release overlap before integration.
3. Non-overlapping board/docs/TODO/icon drift does not rebuild the accepted product candidate or rerun G1/G3/G4/G5.
4. The runbook preserves accepted `workflow-core 0.4`, task `ai-skills-core 0.5`, and repository formal candidate `5.2.0`.
5. Integration/push/release advancement is non-force and AI_Skills `release` advances only to the exact formally closed integrated 5.2.0 commit.
6. G2 remains post-Reviewer promotion work; no Bridge `release` advancement, paid API, automation, or Bridge runtime/source mutation is introduced.
7. Central G2 closure transitions the Maintenance Board lifecycle to `ADAPTING`, not DONE.
8. This repair changed docs/control only; no product replay is required unless diff inspection proves otherwise.
9. Board handling is truthful under current tool limits:
   - no tracking Issue number was invented;
   - no fake `tracking: #N` was written;
   - Project synchronization is not claimed;
   - `CLEAR_WRITING_UNAVAILABLE` is recorded because current board policy requires a real installed Clear Writing invocation before reader-facing Issue creation;
   - the exact pending Issue/source/Project mutation is preserved for the next capable maintenance surface;
   - the user is not asked to drag a Project card or manually add the locator.

If board policy requires actual Issue/backlink/Project mutation before IR-B004 can close, return the **same stable IR-B004** with only that minimum mechanical next action. Do not reopen IR-B001/2/3 or require product replay.

## Output

Return:

`IMPLEMENTATION_REVIEW_PASS_FOR_PRE_RELEASE_PROMOTION`

or

`REVISE`

Do not declare the overall Goal complete. G2 and later Maintenance Board ADAPTING remain future work.
