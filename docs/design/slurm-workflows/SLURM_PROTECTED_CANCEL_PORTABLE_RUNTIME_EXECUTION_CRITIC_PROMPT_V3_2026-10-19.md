# Execution-ready Critic prompt — Slurm protected cancel portable runtime v3

You are the independent AI Research Stack Critic for the same task.

Do not implement. Do not modify repository files, live `CODEX_HOME`, Slurm, branches/worktrees, Project state, DII or CARE.

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-cancel-production-closure`
- review_stage: `EXECUTION_READY_REVIEW_V3`
- source_branch_or_ref: approved design base `main@23f51b0bebd8a32f49d899f7fae1ee0e5f17e4cd`
- package_commit: `352ff4d02bb41dd89d9335008910880d030de21e`
- proposal_path_and_version:
  `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_PROPOSAL_V3_2026-10-19.md` / v3
- execution_plan:
  `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_EXECUTION_PLAN_V3_2026-10-19.md`
- canonical_goal:
  `docs/goals/hpc--slurm-cancel-production-closure-goal-v3.md`
- kickoff_draft:
  `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_KICKOFF_DRAFT_V3_2026-10-19.md`
- failed historical candidate:
  `work/hpc--slurm-protected-partition-chat-confirmation-v2-1@1b8df2c1f2b93de1605d571f5125cd4aaa99fd20`

The package commit contains the exact v3 Proposal + Plan + Goal + Kickoff to review. Later documentation commits must not silently change the review object.

## Mandatory source reads

First read current AI Skills main versions of:

- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `AGENTS.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- current `VERSION`
- current `skills/tools/hpc/slurm-workflows/SKILL.md`
- current `docs/skill-todos/slurm-workflows.md`

Because Goal/Kickoff uses Reviewed Handoff / branch-worktree authority, also read current:

- `YuukiAS/GPT_Codex_AI_Bridge_Kit/main/AGENTS.md`
- `docs/V0_5_REVIEWED_HANDOFF_IMPLEMENTATION_SPEC.md` from that repository.

Then read the four package files at exact package commit
`352ff4d02bb41dd89d9335008910880d030de21e`.

Read the failed historical candidate only where needed to verify selective-port feasibility, root cause and current implementation surface. Do not treat its old `RESULT.md`, live install or branch state as current authority.

## Facts already established for this review

Unless current direct source contradicts them, do not reopen the old Code Mode investigation:

- nested `tools.exec_command` reaches `ExecCommandHandler`;
- real `Bash PreToolUse` was observed;
- matcher, Hook trust and `CODEX_HOME` were correct;
- the selected Python failed before Hook business logic because its dynamic loader could not find `libpython3.12.so.1.0`;
- the child exited `127`;
- Codex treated that ordinary Hook process failure as non-blocking;
- therefore the root defect is portable Hook runtime selection + fail-open launcher semantics.

The historical branch is verified diverged from the approved design base: ahead 12 / behind 23.

Current formal release at package authoring time was repository `5.5.0`, standalone `slurm-workflows 0.4`.

Current default-branch searches found no active direct `scancel` production path in DII or CARE, so the package freezes both as NO CHANGE unless implementation-time source gives new direct evidence.

## Review the full execution package, not the design alone

The previous Critic PASS approved Proposal v3 architecture. This round must decide whether Proposal + Execution Plan + Goal + Kickoff are now actually executable without Codex having to make new product/architecture/authorization decisions.

Return only:

`PASS`

or

`REVISE`.

### 1. Architecture fidelity

Confirm the package did not weaken the approved design:

- one global user Hook remains the enforcement boundary;
- no `scancel` wrapper, PATH interception, project-local Hook, Direct-mode change or Codex patch;
- `config.toml` inline declaration is the fail-closed root;
- external supervisor expected identity is bound by trusted declaration, not self-read from writable runtime;
- production Hook interpreter is discovered/qualified independently of installer `sys.executable`;
- final sanitized minimal environment is the one actually qualified;
- machine-specific loader state stays private;
- policy moves to JSON / Python 3.9+ without changing protected-cancel semantics;
- PostToolUse reserves before mutation and ambiguous outcomes never auto-retry;
- `slurm_routing.py` is default NO CHANGE.

### 2. Fail-closed completeness

Try to break the proposed root/supervisor contract.

Specifically check whether any of these can still become a raw Hook failure that Codex interprets as non-blocking:

- supervisor missing;
- supervisor hash mismatch;
- Python missing;
- dynamic loader failure;
- child exit 127/nonzero;
- signal;
- child timeout;
- Hook/runtime missing or corrupt;
- malformed/empty/event-incompatible child output;
- host timeout occurring before the supervisor emits deny.

A PASS requires a credible implementation path where `PreToolUse` / `PermissionRequest` yield valid deny and underlying Bash launch count is zero for these failure classes.

Do not require a second incomplete shell parser merely to keep unrelated Bash running during a broken safety runtime.

### 3. Portable installation and atomic activation

Check that G1 cannot activate a half-working Hook:

- runtime qualification happens before live declaration activation;
- qualification uses final production environment;
- existing task-owned live state is backed up/restorable;
- unrelated config/Hooks/trust are preserved;
- failure before activation leaves formal config unchanged;
- failure after attempted activation has a bounded restore path;
- no Longleaf path leaks into public source.

### 4. Real normal-entry evidence

G2 must contain at least one actual Codex Hook normal-entry infrastructure-failure injection; directly running scripts is insufficient.

G4 must first prove `scancel --help` is denied before the real process starts, then use exactly one task-created CPU-only future-BeginTime `htzhulab` Job for both:
- retain;
- fresh confirm + exact cancel once.

Check that the sequence cannot touch another Job and does not use GPU/H100.

### 5. Capability Gate Matrix

The package is allowed exactly five gates:

- G1 portable install/atomic activation;
- G2 infrastructure failure fails closed;
- G3 behavior/should-not-change regression;
- G4 Longleaf real normal entry;
- G5 formal release identity.

Judge whether these five gates are distinct and sufficient under
`PLUGIN_CAPABILITY_GATE_POLICY.md`.

Do not add another gate unless a genuinely different user capability/evidence/failure semantic is missing.

Confirm cheap deterministic regression precedes real mutation and all release-critical evidence binds to one final candidate.

### 6. Workflow / branch / authority

Check the planned post-PASS identity:

- R: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection`
- branch: `reviewed/hpc--slurm-cancel-production-closure`
- W: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-production-closure-v3`

Confirm the Kickoff is a draft, not current authorization, and that after PASS the user can authorize the exact branch/worktree and bounded live effects by sending one short Codex handoff.

Check that the package uses the existing Bridge Reviewed Handoff normal entry and does not create another workflow.

### 7. High-impact bounded authorization

Check that the later user handoff can truthfully authorize, in one bounded scope:

- exact task branch/worktree;
- task-owned repo edits/publication;
- only the protected-cancel block in
  `/users/a/e/aereinh/.codex/config.toml`;
- only
  `/users/a/e/aereinh/.codex/slurm-protected-cancel/`;
- backup/restore and one necessary final trust/reload;
- exactly one minimal CPU-only future `htzhulab` test Job;
- cancellation of that exact created Job only after confirmed flow;
- final normal non-force release closure after gates/review.

No unrelated live config, other machine, existing Job, GPU/H100 allocation, force operation or hidden permission expansion may be implied.

### 8. Version/release closure

Check the version decision against the current version policy.

At package authoring time:
- repository `5.5.0`;
- standalone Skill `0.4`;
- planned compatible release `5.5.1` + `slurm-workflows 0.5`.

The package correctly requires recalculation if formal source advances. Confirm central Marketplace plugins remain NO_BUMP unless actual implementation scope changes.

### 9. DII / CARE

Confirm NO CHANGE is justified by current source and that implementation-time re-opening requires direct evidence of a real bypass, not historical prose.

Reject any plan that pre-emptively copies policy/confirmation logic into consumers.

### 10. Maintenance-board truth

The package deliberately does not fabricate a tracking Issue because this Planner surface lacks both a compliant executable Clear Writing mutation path and GitHub Project mutation surface.

Check that the recorded pending mutation is sufficient and truthful:

- one Issue for the same task;
- `maintenance-track`;
- `kind:new-capability`;
- `scope:standalone-skill`;
- `area:standalone-skill`;
- Project `Status=DOING`, `Area=standalone-skill`;
- current v3 package as anchor;
- execution-ready review as next action;
- canonical TODO backfilled with actual `tracking: #N` only after Issue creation.

This pending bookkeeping must not be misrepresented as already synchronized and must not be delegated to the user manually.

## PASS standard

PASS only if the four-file package is execution-ready as one bounded implementation/release task and Codex no longer needs to decide architecture, Gate structure, branch/worktree identity, consumer scope, version policy or dangerous-effect scope.

PASS must state:

- reviewed object = v3 package at exact commit;
- approved five-Gate matrix;
- approved branch/worktree and bounded authorization envelope;
- `READY_FOR_CODEX=YES`;
- what the PASS does **not** itself authorize.

Then, per current Critic contract, output one short user-visible Codex handoff rather than copying the full Kickoff Draft.

The handoff must reference the approved Proposal/Plan/Goal/Kickoff paths and exact approved commit. It must explicitly include the high-impact effects that require current-user authorization: exact branch/worktree, bounded Longleaf `CODEX_HOME` protected-cancel mutation, exactly one minimal future `htzhulab` test Job, and normal non-force release closure after gates. It must not include `DRAFT_ONLY_NOT_AUTHORIZED` or other pre-approval control prose.

Required shape:

```text
APPROVED_PROPOSAL_PATH=...
APPROVED_GOAL_PATH=...
APPROVED_KICKOFF_PATH=...
APPROVED_COMMIT=...
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
=== COPY TO CODEX BEGIN ===
<short current-user execution handoff>
=== COPY TO CODEX END ===
```

## REVISE standard

Only block on a real execution/safety/product gap.

For every blocker give:

- stable blocker id;
- why it can cause real failure;
- minimum correction;
- evidence that would close it.

Do not reopen already-closed Code Mode questions, demand same-UID OS isolation, add wrapper/daemon/database, add a sixth equivalent Gate, or move the finish line for optional hardening.

After REVISE, automatically provide the complete next Planner prompt under the current Critic contract.
