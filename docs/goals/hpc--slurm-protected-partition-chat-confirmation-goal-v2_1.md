# Slurm protected-partition chat confirmation — Canonical Goal v2.1

Task:
hpc--slurm-cancel-production-closure

Status:
EXECUTION_PACKAGE / AUTHORIZED_ONLY_AFTER_CRITIC_PASS_AND_USER_SEND / PHASE_0_TO_3_ONLY

Architecture authority:
- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_1_2026-10-18.md
- approved Proposal commit: 31910548fe5d08eb8e1f5a8fe44040a2f51b32b9
- approved Proposal blob: 26760ae8bb0a19809f1048436fa14aba0bb4e49a

Execution authority:
- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_EXECUTION_PLAN_V2_1_2026-10-18.md
- next execution-ready Critic binds APPROVED_COMMIT to the final v2.1 package commit
- Critic PASS alone executes nothing
- only the user subsequently sending the exact approved Kickoff authorizes Phase 0–3

Rejected execution packages:
- 4d940d7510e29f74a14c5b5070a1a9671f3f27e7
- 38a76797439c6b29098aade7539270cbc51e8836
- any ER-V2-01 pre-closure execution draft

Never use their Kickoffs or terminal/persisted-confirmed semantics.

## 1. Required product behavior

Longleaf private policy:

protected_cancel_partitions = ["htzhulab"]

Required normal entry:

ordinary scancel exact JobId
-> central guard resolves exact JobId / Partition read-only
-> non-protected: no additional protected-cancel confirmation
-> protected: first attempt never mutates
-> NEEDS_INTERACTIVE_CHAT_CONFIRMATION
-> root interactive Codex native request_user_input
-> explicit dedicated response “确认取消”
-> trusted PostToolUse host Hook
-> verify private binder / capability / runtime authority
-> re-resolve exact JobId / Partition / operation
-> one-time reservation
-> trusted absolute scancel exact target once
-> consumer/controller resumes only to observe state and continue business logic

The user never:
- copies nonce/challenge
- opens a terminal for confirmation
- runs a confirmation wrapper
- manages pending/confirmed state

Do not implement:
- H100/accelerator protection
- current-run ownership
- owned-job-id
- persisted confirmed token
- old three-state safe-cancel
- terminal confirmer
- UserPromptSubmit authorization
- execpolicy prompt/auto_review as human proof
- MCP server
- database/daemon/broker
- fifth Capability Gate

## 2. Exact execution identities

AI_Skills_Collection

R=/overflow/htzhu/mingcheng_new/AI_Skills_Collection
branch=work/hpc--slurm-protected-partition-chat-confirmation-v2-1
W=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation-v2-1
base=exact execution-ready Critic APPROVED_COMMIT

DII

R=/users/a/e/aereinh/Distributed_Imaging_Inference
branch=work/hpc--slurm-protected-partition-chat-confirmation-v2-1
W=/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-protected-partition-chat-confirmation-v2-1
base=747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f

CARE

R=/users/a/e/aereinh/CARE
branch=work/hpc--slurm-protected-partition-chat-confirmation-v2-1
W=/users/a/e/aereinh/CARE-hpc--slurm-protected-partition-chat-confirmation-v2-1
base=75a40e454de43b64e59a0b0b438ff57ef2bb8345

Platform references:

OpenAI Codex reviewed:
8c076942cb70fba8e5c4732c23f1faabc4aed484

Bridge Kit reviewed:
d4b694673501d4933eca5cd68394c740c0cb823d

Bridge source:
NO_CHANGE

Every branch/worktree creation requires exact repo/origin/clean/source/absence preflight.

## 3. Phase 0 is mandatory and comes first

Before product implementation:

- create only AI Skills v2.1 worktree
- keep DII/CARE read-only
- prepare harmless project-local Codex capability/authority probe
- do not touch Slurm

### 3.1 Probe project config

Trusted project .codex/config.toml must:

- enable default_mode_request_user_input=true
- select locked profile extending :workspace
- explicitly deny project .codex to ordinary Codex tool execution

Do not change Bridge source or ordinary user-level CODEX_HOME settings.

The only Phase 0–3 user-level CODEX_HOME side effect authorized by this Goal is the user personally trusting exact task Hook key/current_hash values through the official Codex Hook trust UI. That official UI writes `hooks.state.<key>.trusted_hash` into the current Codex identity's user `$CODEX_HOME/config.toml`. Executor must never edit that file directly or alter unrelated fields.

### 3.2 Probe authority material

Use a harmless private runtime area:

.codex/slurm-protected-cancel-private/

with fake:
- binder
- capability.key
- runtime.json
- consumed/

No Slurm command is permitted.

Prove:
- trusted Host Hook can access it
- ordinary shell/Python/apply_patch/absolute/symlink paths cannot
- auto_review-approved escalation still cannot
- modified Hook becomes Modified and requires real Hook trust
- bypass_hook_trust=false
- fake private binder digest mismatch blocks execution
- fake PATH scontrol/scancel cannot override runtime.json frozen absolute paths

### 3.3 Live Desktop probe

Use a fresh Longleaf Codex Desktop root chat on exact AI Skills W.

Native harmless request_user_input:

“这是聊天确认能力测试。请选择‘确认测试’或‘取消测试’。”

Required evidence:
- Default mode tool visible
- Desktop native UI visible
- explicit user response returns dedicated response
- PostToolUse gets exact input/response/session/turn/tool-use ids
- unanswered request resolves empty
- empty never triggers authority action
- no Slurm or production config is touched, except the bounded official Hook trust UI side effect below if trust is required

Before asking the user to trust any probe/candidate Hook, freeze and show in evidence:
- current Codex identity / CODEX_HOME locator
- project root / task branch
- exact Hook source
- exact stable Hook key
- exact current_hash
- pre-trust exact key state from official readback

The user may trust only that exact key/current_hash through the official Codex Hook trust UI.

After trust:
- hooks/list must show Trusted for that exact hash
- official config readback must show the corresponding hooks.state trusted_hash effect
- Executor must not directly write user config

Probe/candidate Hook trust retention:
- exact task Hook trust may remain through Phase 3 if needed for replay
- once the Hook declaration disappears or changes, the old hash is inert and cannot trust the new declaration
- cleanup/revoke may use only the official Codex Hook trust management entry
- if the current official UI has no revoke/remove action, retain and report the inert exact key/hash; never manually edit user config or use generic config/batchWrite to simulate cleanup

If Executor cannot display the fresh Desktop chat itself:

PROBE_READY_FOR_USER_CHAT

Only ask the user to:
- open one new Longleaf_Codex chat on exact W
- if the exact reviewed probe Hooks require trust, trust only the exact key/current_hash values frozen in evidence; this official UI action writes the corresponding user-level hooks.state trust record
- answer the harmless test once and leave the second request unanswered

Do not ask for a terminal.

### 3.4 should-not-change probe

Locked profile must preserve:
- git status --short
- read-only git diff / rev-parse / remote identity
- representative normal AI Skills tests that do not inherently require model access to .codex

If full .codex deny causes real regression:
STOP -> Planner

Executor cannot loosen it.

### 3.5 headless negative probe

Confirm without Slurm:

HEADLESS_PROTECTED_CANCEL=NEEDS_INTERACTIVE_CHAT_CONFIRMATION

No terminal/approval/auto_review/UserPromptSubmit fallback.

Any Phase 0 failure stops the task before product implementation.

## 4. Phase 1 central implementation

Only after Phase 0 PASS.

Implement in existing slurm-workflows:

### 4.1 thin guard

Supported:
- one exact ordinary JobId
- explicit exact JobId list
- uniquely resolved exact array element

Fail closed:
- array parent/range
- heterogeneous
- job step
- dynamic selectors
- federation/cluster switch
- non-default signal/batch/full

Use:
- scontrol show job -o exact-id primary
- bounded squeue cross-check as needed

Non-protected:
- no additional confirmation
- preserve existing Goal/approval semantics

Protected:
- first attempt zero mutation
- return exact JobId / Partition / normalized operation / opaque question id
- return NEEDS_INTERACTIVE_CHAT_CONFIRMATION
- no persisted confirmed authority

### 4.2 reviewed binder source and private runtime copy

Central source contains reviewed binder implementation.

Runtime authority binder exists only at:

<project-root>/.codex/slurm-protected-cancel-private/bin/slurm-protected-cancel-binder

Candidate setup:
- copies exact reviewed binder
- computes SHA-256
- writes owner-only runtime copy
- writes runtime.json
- generates exact project Hook declaration

No normal central “authority mode” CLI exists.

### 4.3 binder integrity binding

Trusted Hook declaration freezes:
- canonical absolute private binder path
- exact reviewed binder SHA-256
- invocation shape

Before binder execution:
- trusted host absolute hashing executable computes digest
- mismatch => no binder execution / no Slurm

Do not assume Hook declaration hash covers external binder contents.

### 4.4 trusted Slurm absolute executables

runtime.json freezes:
- canonical project root
- binder digest
- canonical absolute scontrol
- canonical absolute scancel

They must be:
- outside workspace
- non-model-writable
- verified during setup

Binder:
- never uses PATH lookup
- never uses alias/function
- never uses relative Slurm executable paths

### 4.5 SessionStart capability

Trusted SessionStart Host Hook:
- root interactive session only
- random >=256-bit capability
- private capability.key
- mode 0600
- bind exact session/project/hook version
- never echo to prompt/tool output/log
- cleanup stale/session end
- missing capability => fail closed

### 4.6 request_user_input contract

Visible question:

“Job <id> 当前位于受保护分区 <partition>。确认取消这个 Job 吗？”

Options:
- 确认取消
- 保留 Job

Only canonical dedicated “确认取消” can continue.

### 4.7 PostToolUse exact execution owner

Synchronous matcher:
^request_user_input$

Before any Slurm mutation binder must verify:
- genuine request_user_input event
- root interactive session
- reviewed private binder digest
- private capability
- runtime.json identity
- canonical question
- canonical explicit confirm response
- fresh session/turn/tool-use/question identity
- exact first-block request identity
- trusted absolute scontrol re-resolution
- exact JobId / Partition / operation unchanged
- Partition remains protected
- target remains valid for ordinary cancellation
- atomic one-time reservation

Then and only then:
trusted absolute scancel <exact JobId>

Duplicate/replay/mismatch:
no mutation.

Crash after reservation before scancel:
fail closed, no automatic replay, fresh confirmation required.

## 5. Anti-tamper requirements

Ordinary Codex normal entry must not be able to:
- read/modify/replace/execute private binder
- read capability
- modify runtime.json
- write/delete/reset consumed ledger
- change private binder permissions
- bypass with Python/apply_patch/absolute/symlink/alias
- bypass with copied binder
- bypass with fabricated PostToolUse JSON
- bypass with auto_review escalation
- bypass by PATH shadowing scontrol/scancel
- modify hooks/config/rules in locked session and preserve original trust

Direct binder invocation must fail before any Slurm query/mutation when private authority is unavailable.

Modified project Hook must be HookTrustStatus::Modified and require real user Hook trust.

Production forbids bypass_hook_trust.

## 6. DII integration

After Phase 0 PASS create DII v2.1 worktree.

Only:
- exact central candidate integration
- project config/hooks/rules
- automation PATH/launcher resolution
- existing business-level cancellation intent

No:
- partition policy logic
- request_user_input parsing
- capability handling
- binder/consumed handling

If current source shows absolute /usr/bin/scancel, SSH scancel or Slurm API bypass:
STOP -> Planner

## 7. CARE integration

After Phase 0 PASS create CARE v2.1 worktree.

Consumers only propagate cancellation outcome.

B1:
- nonzero: do not add cancelled
- propagate blocker and end current cancellation attempt

M7:
- nonzero propagate

M8:
- nonzero propagate

interactive takeover:
- nonzero: no CANCELLED accounting wait
- no launch
- propagate

cascade formal race:
- cancel nonzero ends current watcher round and propagates
- internal interval loop must not swallow blocker

Interactive root Codex asks user.

After confirmed Host Hook performs exact cancellation:
- controller/watcher resume only to observe state and continue existing business logic
- no second scancel to consume confirmation

CARE never parses policy/question/answer/capability.

## 8. Project-local normal-entry enforcement

Each reviewed candidate repo must carry or generate reviewed project-local Codex configuration/rules sufficient to:

- enable native request_user_input only in trusted project scope
- lock .codex for ordinary model tool execution
- register reviewed trusted SessionStart / PostToolUse Hooks
- forbid raw scancel normal-entry bypass
- forbid /usr/bin/scancel normal-entry bypass
- forbid ordinary direct authority-binder invocation shapes
- not blanket-allow guard

Actual config/read, hooks/list and execpolicy check evidence is required.

User ordinary shell remains unrestricted.

## 9. Automation PATH

One automation-only shim:

scancel -> central guard

Do not replace /usr/bin/scancel.
Do not globally change user shell PATH.

For every required consumer prove:
- command -v scancel
- Python shutil.which("scancel")

resolve reviewed shim.

## 10. Gate A-D

Only four gates.

Gate A — partition routing

Must prove:
- non-protected exact job gets no extra protected confirmation
- htzhulab first attempt zero mutation
- explicit multi-target set with any protected target is protected
- initial blanket approval cannot skip first block

Gate B — native fresh chat confirmation + authority boundary

Must prove:
- live Desktop native request_user_input
- dedicated explicit user response
- empty/timeout/retain/Other no mutation
- assistant/auto_review/UserPromptSubmit/subagent no authority
- Host Hook accesses private authority
- ordinary shell/Python/apply_patch/alias/symlink/direct/copied/fabricated paths cannot
- auto_review escalation preserves explicit deny
- private binder digest mismatch blocks execution
- model PATH cannot change trusted Slurm executables
- Modified Hook cannot run as original Trusted Hook
- bypass_hook_trust=false
- re-resolution before mutation
- atomic consumed reservation
- duplicate/replay/target change no mutation

Gate C — consumer/runtime coverage + should-not-change

Must prove:
- project config/hooks/rules really load
- required consumer bare scancel resolves guard
- raw system scancel cannot bypass Codex normal entry
- CARE blocker propagation works
- DII does not copy policy
- headless protected path fail closed
- user ordinary shell remains normal
- locked .codex does not break required git status/read-only diff/identity/representative tests

Gate D — target integrity / claim truth

Must prove:
- exact target semantics
- complex selectors fail closed
- mutation owner re-resolves target
- destructive replay only isolated fake Slurm
- live Longleaf validation does not cancel real jobs
- claim limited to verified interactive Codex/required consumer normal entry
- no same-UID OS hard-isolation claim

No Gate E.

## 11. Testing boundary

Pure/non-destructive:
- config compilation/origin
- Hook discovery/trust
- permission deny
- private binder digest
- runtime absolute path binding
- request schema/response classification
- consumer propagation
- Git/status/test should-not-change
- headless fail closed

Destructive fake replay only under:
- network disabled
- isolated PID namespace
- no production credentials
- no Slurm/MUNGE/controller/socket
- no host control socket
- no production writable mount
- fake Slurm only

If isolation cannot be proven:
BLOCKED_BY_ISOLATION

Never substitute real Longleaf mutation.

## 12. Phase 2 candidate validation

After implementation:
- deterministic tests
- isolated fake Slurm tests
- Gate A-D evidence
- exact AI/DII/CARE commits
- exact binder SHA-256
- exact private runtime layout contract
- exact Hook hashes
- exact config/rules origin
- exact runtime absolute Slurm executable bindings
- should-not-change evidence

Freeze candidate before review.

## 13. Phase 3 independent implementation review

Publish each exact v2.1 task branch at most once, ordinary non-force, same-name origin, only when remote absent.

Before Reviewer handoff, use the exact final candidate binder digest and the same reviewed setup generator to render production Hook identities for all three canonical roots offline only. Do not write production files or activate production Hooks.

Freeze for each canonical production root:
- exact candidate commit
- canonical root
- canonical private binder absolute path
- final binder SHA-256
- exact production SessionStart Hook declaration
- exact production PostToolUse Hook declaration
- exact production stable Hook keys/current_hashes
- expected runtime.json canonical root/digest/trusted absolute Slurm binding
- production project config/rules declaration identity

Candidate worktree Hook hashes are not production Hook hashes.

Reviewer must inspect:
- Proposal v2.1
- Plan/Goal v2.1
- three repo diffs
- live Phase 0 Desktop/authority probe
- Gate A-D
- isolated fake evidence
- private binder/content integrity
- candidate Hook trust
- all three offline production-rendered Hook declarations, keys, current_hashes, canonical roots, binder paths and digests
- absolute Slurm executable binding
- should-not-change regression
- rollback
- production activation package

Reviewer PASS before any production activation.

## 14. Production activation requires a second short user authorization

This Goal does not authorize production activation.

After exact Reviewer PASS, a separate short user authorization must bind both:
- exact reviewed AI Skills/DII/CARE candidate commits
- exact Reviewer-frozen production Hook keys/current_hashes, canonical roots, private binder paths and binder digests

Only that authorization may permit:

- backup task-owned user-local install/private override/project runtime metadata
- exact reviewed central install
- protected_cancel_partitions=["htzhulab"] in actual Longleaf private override, preserving unrelated fields
- exact reviewed AI Skills/DII/CARE project setup
- private binder copy/digest/runtime/capability setup
- exact reviewed project hooks/rules/config
- exact reviewed automation PATH integration
- exact reviewed consumer integration
- after production setup writes canonical project files, read back actual hooks/list key/current_hash for each canonical root and require exact equality with the Reviewer-frozen production values
- only after that equality check, user may trust those exact production Hook hashes through the official Codex Hook trust UI
- this official UI trust write is the only allowed production user-level hooks.state config side effect; Executor never edits user config directly
- read-only production validation
- no real Slurm cancellation test

No Bridge source, ordinary user-level CODEX_HOME setting, global rule, or user-level Hook declaration modification.

Exception: user-personally-triggered official Hook trust UI may write only the exact reviewed `hooks.state.<key>.trusted_hash` records described above.

## 15. Rollback

Before production:
- backup only task-owned changed surfaces
- record nonsecret hashes/identities

Rollback restores:
- prior central install
- prior private override
- prior project config/hooks/rules
- prior private runtime authority state
- prior automation PATH integration
- prior consumer commit state

Hook trust cleanup/rollback may use only the official Codex Hook trust management entry for the exact task key/hash. Executor must not directly edit user config. If the current official UI exposes no revoke/remove action, make the project Hook declaration inactive/removed by normal project rollback so the retained hash is inert, record the exact retained key/hash, and do not claim the trust record was deleted.

Rollback never:
- cancels/requeues/signals/releases Slurm
- kills allocation holders
- alters MUNGE/SSH/Unix identity
- changes Bridge source

## 16. Version/release

Candidate:
Repository bump decision: NONE
slurm-workflows: NO_BUMP
central Marketplace Plugins: NO_BUMP
Bridge Kit: NO_CHANGE

Reason:
candidate is not a formal installable release.

Only after reviewed production activation, required DII/CARE integration, and complete production Gate A-D:

slurm-workflows:
0.4 -> 0.5

Repository bump decision:
PATCH

If release-time VERSION is still 5.4.5:
5.4.6

Otherwise:
actual release-time next PATCH.

central Plugins:
NO_BUMP

Bridge Kit:
NO_CHANGE

README/CHANGELOG/version/generated closure happens last and cannot change behavior.

## 17. Maintenance truth

Current canonical source still says:
tracking issue: PENDING_CLEAR_WRITING

Do not invent:
- tracking Issue
- DOING
- ADAPTING
- DONE

Old H100 TODO language is superseded by user’s protected-partition-only contract.

If Clear Writing/Project capability is still unavailable at technical closure, emit exact pending mutation for the next capable Maintainer. User does not manually maintain it.

## 18. Absolute prohibitions

- rejected old Kickoffs/packages
- terminal confirmation wrapper
- persisted confirmed token for ordinary shell
- H100/current-run/old three-state logic
- UserPromptSubmit as authority
- execpolicy prompt/auto_review as human proof
- MCP server/database/daemon/broker
- fifth Gate
- production Bridge source/global CODEX_HOME modification except the user-triggered official exact Hook trust records described above
- direct Executor edits to user-level $CODEX_HOME/config.toml
- trusting candidate-worktree Hook hashes as production identities
- production setup whose actual hooks/list current_hash differs from the Reviewer-frozen production hash
- real Slurm cancellation/signal/requeue/release/test allocation
- paid model/API
- same-UID hard-isolation claim
