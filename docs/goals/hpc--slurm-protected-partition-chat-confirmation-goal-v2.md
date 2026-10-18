# Slurm protected-partition chat confirmation — Canonical Goal v2

Task: hpc--slurm-cancel-production-closure

Status:
EXECUTION_PACKAGE / AUTHORIZED_ONLY_AFTER_CRITIC_PASS_AND_USER_SEND / PHASE_0_TO_3_ONLY

Architecture authority:
- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_2026-10-18.md
- approved Proposal commit: 5692e7441d33b115df9220bd18d9fd8b872019b8
- approved Proposal blob: bc62264c6010b3e5371885899138f72c03095250

Execution authority:
- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_EXECUTION_PLAN_V2_2026-10-18.md
- next execution-ready Critic must bind APPROVED_COMMIT to the final package commit
- Critic PASS alone executes nothing
- only the user subsequently sending the exact approved Kickoff authorizes Phase 0–3

Rejected package:
4d940d7510e29f74a14c5b5070a1a9671f3f27e7 = REJECTED_FOR_EXECUTION

Do not use its Kickoff, terminal confirmer, or v1 execution semantics.

## 1. Required user-visible product

Longleaf private policy:

protected_cancel_partitions = ["htzhulab"]

Required interaction:

ordinary scancel exact JobId
-> central guard read-only resolves exact JobId / Partition
-> non-protected: no new protected-confirmation requirement
-> protected: first attempt never mutates
-> interactive root Codex asks native request_user_input:
   exact JobId + Partition
   options: “确认取消” / “保留 Job”
-> only explicit dedicated client response “确认取消” confirms
-> next ordinary scancel re-resolves exact target / Partition / operation
-> exact match consumes confirmation once
-> exact /usr/bin/scancel

The user never copies nonce/challenge, never runs a confirmation wrapper, and never manages pending state.

Initial Goal blanket approval, historical authorization, standing race opt-in, auto_review, assistant text, subagent text, UserPromptSubmit, empty auto-resolution, and internal automatic messages cannot confirm a protected cancellation.

Do not add:
- H100/accelerator protection
- current-run ownership
- owned-job-id
- old three-state safe-cancel
- terminal confirmer
- MCP server
- database/daemon/broker
- fifth Capability Gate

## 2. Exact execution identities

AI_Skills_Collection

R=/overflow/htzhu/mingcheng_new/AI_Skills_Collection
branch=work/hpc--slurm-protected-partition-chat-confirmation
W=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation
base=exact execution-ready Critic APPROVED_COMMIT

DII

R=/users/a/e/aereinh/Distributed_Imaging_Inference
branch=work/hpc--slurm-protected-partition-chat-confirmation
W=/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-protected-partition-chat-confirmation
base=747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f

CARE

R=/users/a/e/aereinh/CARE
branch=work/hpc--slurm-protected-partition-chat-confirmation
W=/users/a/e/aereinh/CARE-hpc--slurm-protected-partition-chat-confirmation
base=75a40e454de43b64e59a0b0b438ff57ef2bb8345

Platform references:

OpenAI Codex main reviewed:
8c076942cb70fba8e5c4732c23f1faabc4aed484

Bridge Kit main reviewed:
f67ac9155c1a844f171afbeef03e8169b8eec6fc

Bridge Kit source:
NO_CHANGE

Before any branch/worktree creation, verify exact repo root, origin, clean state, source commit, target branch absence, target W absence, and same-name remote branch absence. Any mismatch fails closed.

## 3. Phase 0 must happen first

No product implementation before Phase 0 PASS.

### 3.1 Probe-only project config

In AI Skills task worktree, add only task-owned probe surfaces:

.codex/config.toml
- enable only features.default_mode_request_user_input=true

.codex/hooks.json
- register only a harmless PostToolUse matcher for ^request_user_input$

probe logger
- write only tool_input / tool_response / session_id / turn_id / tool_use_id into:
  results/hpc--slurm-cancel-production-closure/chat-confirmation-probe/
- no Slurm
- no network
- no confirmation-state mutation

Bridge user-level config remains unchanged.

Verify the project layer actually wins over the user-level false using config/hook origin readback.

### 3.2 Fresh Longleaf Codex Desktop chat probe

Use a fresh interactive root chat opened on the AI Skills task worktree.

The harmless question must be unrelated to Slurm and offer:
- 确认测试
- 取消测试

Evidence required:

1. request_user_input is available in Default mode in this fresh chat.
2. Desktop UI renders the native question.
3. Explicit user choice returns the dedicated response.
4. PostToolUse probe receives the matching tool input and tool response.
5. A separate unanswered request auto-resolves to empty answers.
6. Empty answers never count as confirmation.
7. No Slurm or production config is touched.

If the current executor cannot create the required fresh Desktop chat itself, stop at:

PROBE_READY_FOR_USER_CHAT

and ask the user only to open one new Longleaf_Codex chat on the exact W and send the harmless probe prompt. Do not ask the user to open a terminal.

### 3.3 Headless negative probe

Confirm without Slurm that codex exec cannot complete request_user_input.

Freeze behavior:

HEADLESS_PROTECTED_CANCEL = NEEDS_INTERACTIVE_CHAT_CONFIRMATION

No terminal / auto_review / approval fallback.

### 3.4 Probe failure

Any Phase 0 failure returns Planner.

Do not continue implementation.
Do not change Bridge user-level false.
Do not fallback to terminal confirmer, UserPromptSubmit, MCP server, or approval prompt.

## 4. Central candidate after Phase 0 PASS

Implement inside existing slurm-workflows:

### thin guard

One small executable such as ai-slurm-scancel.

Responsibilities only:

- exact target parsing
- read-only JobId / state / Partition resolution
- protected_cancel_partitions lookup
- protected first-block
- short-lived internal pending record
- confirmed revalidation / one-time consume
- final exact /usr/bin/scancel

Supported:
- ordinary exact JobId
- explicit exact JobId list
- exact array element when uniquely resolved

Fail closed:
- array parent/range
- heterogeneous job
- job step
- dynamic selectors
- federation/cluster switch
- non-default signal/batch/full mutation

Use scontrol show job -o as primary.
Use bounded squeue cross-check when needed.
Re-resolve immediately before mutation.
Clear SCANCEL_* before real scancel.

### internal pending state

User-private, short-lived, atomic.

Fields only:
- opaque nonce
- opaque question id
- exact sorted JobIds
- Partition set
- normalized operation
- created/expiry
- pending/confirmed/consumed
- confirmation session/turn/tool-use ids

No generic CLI can set confirmed.

### native question

When protected:
- return NEEDS_INTERACTIVE_CHAT_CONFIRMATION
- exact JobId / Partition
- opaque question id
- canonical visible question
- labels only: 确认取消 / 保留 Job

### PostToolUse binder

Central binder executable.

Project .codex/hooks.json only registers it for:
^request_user_input$

pending -> confirmed only when:
- exact question id matches
- exact JobId/Partition/operation match
- pending and unexpired
- exact question receives explicit canonical 确认取消

No confirmation for:
- empty answers
- timeout
- 保留 Job
- Other/free text
- wrong question
- expired/consumed record
- malformed response

Hook failure means no confirmed state.

Binder never performs Slurm mutation.

## 5. Project-scoped Codex enablement and bypass control

Do not modify Bridge source or user-level CODEX_HOME config.

For AI Skills, DII and CARE reviewed candidate repos, use trusted project-local:

.codex/config.toml
- default_mode_request_user_input=true

.codex/hooks.json
- central request_user_input binder only

.codex/rules/slurm-protected-cancel.rules
- raw scancel forbidden in Codex normal entry
- actual /usr/bin/scancel forbidden
- direct binder executable forbidden
- point Codex to ai-slurm-scancel

Do not blanket allow ai-slurm-scancel.

Prove with real config/read, hooks/list and execpolicy check or equivalent official entry.

User ordinary shell remains untouched.

## 6. Automation PATH

Provide one automation-only shim:

scancel -> ai-slurm-scancel

Do not replace /usr/bin/scancel.
Do not prepend it globally to the user's ordinary shell PATH.

For every required automation consumer, prove:

command -v scancel

and

Python shutil.which("scancel")

resolve to the exact reviewed shim.

If a launcher cannot inherit it, make only the minimum launcher/executable-resolution repair.

## 7. DII / CARE adaptation

Consumers never parse protected partition, nonce, question, answer, or confirmation.

### DII

Only:
- exact central candidate sync/install in candidate scope
- project-local config/hook/rules adapter
- PATH/launcher resolution if needed
- existing business-level loser-cancel intent remains

If new absolute /usr/bin/scancel, SSH scancel, or Slurm API cancellation appears in current source, stop and return Planner.

### CARE

On protected guard nonzero, the watcher must return control to supervising Codex.

B1:
- nonzero => do not add cancelled
- propagate guard output/nonzero and end current cancellation attempt

M7:
- nonzero => propagate and end current attempt

M8:
- nonzero => propagate and end current attempt

interactive takeover:
- nonzero => do not enter CANCELLED accounting wait or launch
- propagate and end current attempt

cascade formal race:
- cancel nonzero => end current watcher round and propagate
- do not keep internal interval loop swallowing the chat blocker

returncode 0 non-protected behavior stays unchanged.

Interactive root Codex receives NEEDS_INTERACTIVE_CHAT_CONFIRMATION, asks native question, then resume/rerun produces the next ordinary scancel.

## 8. Headless behavior

codex exec:

- non-protected cancellation gets no new confirmation requirement
- protected cancellation fails closed
- report NEEDS_INTERACTIVE_CHAT_CONFIRMATION
- never fallback to terminal, auto_review, UserPromptSubmit, or ordinary approval

## 9. Capability Gates

Only four.

Gate A — partition routing

Gate B — native fresh chat confirmation

Gate C — consumer/runtime coverage

Gate D — target integrity / claim truth

The exact evidence requirements are those in Execution Plan v2.

Do not add Gate E.
Do not reuse rejected old three-state G1–G6 as final evidence.

## 10. Testing boundary

Pure/deterministic:
- parser
- state machine
- binder response classification
- project config/hook/rules matching
- CARE return-code transport
- headless fail-closed behavior

Destructive fake replay only in a proven isolated fake Slurm environment:
- no network
- isolated PID namespace
- no production credentials
- no real Slurm/MUNGE/controller/socket
- no host control socket
- no production writable mount

If isolation cannot be proven:
BLOCKED_BY_ISOLATION

Never substitute real Longleaf cancellation.

## 11. Candidate review stop

After Phase 0 PASS + Phase 1/2 candidate work:

- freeze exact AI/DII/CARE commits
- publish each new same-name task branch at most once, ordinary non-force, only if remote branch absent
- produce Gate A-D evidence
- stop for independent Reviewer

No production deployment before Reviewer PASS.

## 12. Production activation requires a second short user authorization

This Goal does not authorize production activation.

After exact Reviewer PASS, a separate short user authorization may permit only:

- backup current task-owned user-local AI Skills install/private override
- install exact reviewed central candidate
- write protected_cancel_partitions=["htzhulab"] into actual Longleaf private override, preserving unrelated fields
- integrate exact reviewed AI Skills/DII/CARE project-local config/hook/rules + consumer commits
- activate exact reviewed automation PATH shim
- read-only production validation
- no real Slurm cancellation

Do not modify:
- Bridge source
- user-level $CODEX_HOME/config.toml
- ai-bridge-global.rules
- user-level hooks

## 13. Release

Candidate stage:
- Repository NO_BUMP
- slurm-workflows NO_BUMP
- central Plugins NO_BUMP
- Bridge Kit NO_CHANGE

Only after reviewed production activation + DII/CARE integration + production Gate A-D:

- slurm-workflows 0.4 -> 0.5
- Repository release-time next PATCH; if still 5.4.5 then 5.4.6
- central Plugins NO_BUMP
- Bridge Kit NO_CHANGE
- README/CHANGELOG/version/generated release closure last

No behavior changes hidden in release metadata.

## 14. Maintenance truth

Current source:
tracking issue: PENDING_CLEAR_WRITING

Do not invent tracking Issue or DOING/ADAPTING/DONE.

Old H100 TODO wording is superseded by the user's protected-partition-only contract.

If no real Clear Writing/Project capability exists at technical closure, output the exact pending mutation to the next capable Maintainer; do not ask the user to maintain it manually.

## 15. Absolute prohibitions

- use rejected 4d940d package
- terminal confirmation wrapper
- UserPromptSubmit as authorization source
- execpolicy prompt/auto_review as human proof
- H100 protection
- current-run ownership
- old three-state safe-cancel
- MCP server
- database/daemon/broker
- fifth Gate
- production Bridge/global CODEX_HOME modification
- real Slurm cancellation/signal/requeue/release
- test allocation
- paid model/API
- same-UID hard-isolation claim
