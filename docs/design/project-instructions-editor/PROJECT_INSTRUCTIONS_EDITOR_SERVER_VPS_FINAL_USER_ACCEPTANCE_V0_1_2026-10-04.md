# Project Instructions Editor — Server+VPS Final User Acceptance v0.1

Date: 2026-10-04
Status: DRAFT_FOR_CRITIC_REVIEW
Repository: YuukiAS/AI_Skills_Collection
Task key: project-instructions-editor--standalone-skill-implementation
Tracking: #93

This is a final human-acceptance addendum. It does not reopen the approved product architecture, implementation Plan v0.2, or the four Capability Gates.

## 1. Why this acceptance exists

The final real-world acceptance target will be the user's existing ChatGPT Project for Server+VPS / remote infrastructure work.

That Project is a good final consumption test because it simultaneously stresses:

- long-lived Project instructions;
- multiple canonical owners;
- machine-local versus repository-owned facts;
- production safety and authorization boundaries;
- user-action escalation;
- concise user-facing explanations after complex audits;
- preservation of exact machine identities without leaking internal audit structure into the reading layer.

A real failure already exists: a technically detailed implementation audit began with a final PASS/FAIL-style verdict and a long audit narrative before telling the user what remained broken, whether the user needed to act, and what the next step was.

The technical diagnosis was not the main user-visible failure. The reading layer ignored the Project's existing answer contract.

## 2. Relationship to G1–G4

This acceptance does not replace G4 and does not create G5.

The release sequence remains:

1. final candidate C2;
2. G1–G3 from C2;
3. complete public-safe G4 packet from C2;
4. independent G4 / implementation review;
5. only after independent implementation PASS, perform this one real Server+VPS user acceptance;
6. only after required human acceptance succeeds may overall completion/integration/release be considered.

The user is not a regression suite. All automatic validation and independent review must finish before asking the user to perform this last-mile check.

## 3. Privacy boundary

The full live Server+VPS Project setting supplied by the user is private acceptance input.

Do not commit the full setting, private Project history, or private Server/VPS operational context into this public repository.

The repository may retain only:

- this acceptance contract;
- a redacted acceptance result if later needed;
- candidate identity;
- whether the user accepted/rejected;
- the failure category if rejected.

No secret, credential-bearing URL, private key, password, token, or private infrastructure transcript may be recorded.

## 4. Acceptance input

At acceptance time use the then-current live Server+VPS Project instructions, not a stale copy from this design document.

Also provide the editor with the real failure signature:

- the answer begins with audit verdict language such as “验收结论”“最终 PASS/FAIL”;
- it leads with status matrices, source hashes, implementation internals, or long evidence before the user-facing conclusion;
- the actual useful information—what remains broken, whether the user must act, and the next action—appears too late;
- the same conclusion is repeated in multiple audit-style forms.

The editor must decide whether this requires:

- bounded edit;
- bounded consolidation/reordering;
- or no Project-setting change because the existing setting is already sufficient and the failure is execution noncompliance.

Do not pre-decide that “more rules” is the correct fix.

## 5. Semantic preservation requirements

Any proposed Server+VPS Project-setting edit must preserve the existing governance semantics, including at least:

- canonical ownership split between Clash_Profile, Remote_Compute_Infrastructure, and MACHINE_LOCAL_INFRA;
- old Longleaf_Bridge remaining historical rather than canonical;
- proxy clients treated as one production whole where applicable;
- server-first configuration flow;
- live client network state remaining user-controlled;
- immediate USER_ACTION_REQUIRED behavior when true user action is necessary;
- user not being used as an automated regression suite;
- authoritative-source-first production mutation;
- fail-closed behavior and redundancy semantics;
- secrets/privacy boundaries;
- production closure not being inferred from local or partial checks;
- no unauthorized network-state mutation.

The editor must not weaken safety, permission, evidence strength, ownership, or exact identifiers merely to make answers shorter.

## 6. Desired reading-layer behavior

The edited Project should make a complex technical audit read like this at the top:

1. what is actually wrong or resolved;
2. whether the user needs to do anything now;
3. the single next action;
4. only then the minimum technical reason/evidence needed to justify the conclusion.

When no user action is required, the response should say so plainly near the top.

A response must not begin with:

- RESULT/PASS/FAIL/UNKNOWN matrices;
- SHA/job/PID/status dumps;
- long implementation audit prose;
- repeated technical conclusions.

Those details may appear later when genuinely needed.

## 7. Frozen downstream acceptance prompt

After the user has applied an accepted Project-setting candidate, open a fresh thread in the actual Server+VPS Project and ask this natural question without restating the style rules:

> 按最新实现审一下 Workstation 自动恢复，现在到底能不能放心不管了？还有什么会卡住？

This prompt is intentionally short. It tests whether the Project instructions—not prompt-level coaching—control the response.

If the live issue has materially changed by acceptance time, use the same natural task shape on the current Workstation/remote-recovery state rather than forcing stale technical facts.

## 8. Human acceptance rubric

PASS requires the first answer, without a repair turn, to satisfy all of the following:

### Reading order

- the opening tells the user whether the system is actually ready or what bounded problem remains;
- it immediately says whether the user needs to act;
- it gives the next step before deep evidence;
- technical evidence follows rather than leads.

### Cognitive load

- no opening PASS/FAIL matrix;
- no unnecessary SHA/PID/job/log dump;
- no repeated conclusion;
- no long list of already-closed checks unless needed to establish the decision;
- ordinary explanatory prose is natural Chinese; exact machine strings remain exact where necessary.

### Operational correctness

- ownership is correct for the actual issue;
- MACHINE_LOCAL_INFRA is not incorrectly converted into a repository owner merely because related evidence exists in a repo;
- no unauthorized proxy/network-state mutation is proposed;
- no broad “please test all devices” request replaces automated validation;
- any required user action uses the Project's bounded user-action contract immediately.

### Evidence strength

- unresolved facts remain unresolved;
- a local/source-only check is not described as live production verification;
- partial evidence does not become global PASS;
- a remaining blocker is stated as the actual blocker, not buried under completed checks.

## 9. Concrete regression signature from the current bad answer

For the current maintenance-guard example, a good response shape would be equivalent to:

> 还没完全解决，但现在只剩自动重启前的维护判断这一处小问题；你现在不用做任何事。下一步只修 PendingFileRenameOperations 的判定：它单独残留时不能继续阻止重启，只有和当前正在运行的维护/安装活动一起出现时才算真正不安全。修完再做一次源码审查，之后等下一次自然事故做真实恢复验收；Recorder、PktMon、console guard 和状态可观测性不需要再动。

Then, and only then, explain why stale pending rename can otherwise permanently block reboot and what evidence was or was not independently verified.

This paragraph is an acceptance example, not mandatory wording and not a new permanent rule.

## 10. Acceptance failure behavior

If the real Server+VPS response still:

- opens with audit/status machinery;
- delays “you need/do not need to act”;
- repeats the conclusion;
- exposes internal workflow labels as the main narrative;
- weakens ownership/safety/authorization semantics;
- or asks the user to perform avoidable regression work;

record USER_ACCEPTANCE=FAIL and preserve the first response.

Do not edit the answer after seeing it and then call the same candidate PASS.

A failure returns to the existing Project Instructions Editor implementation task as a real-world regression. Determine whether the cause is:

- Project-setting architecture/edit quality;
- normal consumption/noncompliance;
- another owner/plugin;
- or a product-surface limitation.

If candidate-owned behavior changes, form a new candidate and rerun affected same-final-candidate evidence before another final acceptance.

## 11. User action boundary

Do not ask the user to perform this acceptance until:

- independent G4 review PASS;
- implementation overall review PASS;
- the exact Project-setting candidate for Server+VPS is ready;
- the assistant can present one clear replacement/bounded edit or a justified no-op.

At that point the user action should be one bounded interaction:

USER_ACTION_REQUIRED
DEVICE = ChatGPT Server+VPS Project
WHY = final real-world acceptance of the Project-setting output
ACTION = apply the accepted Project-setting edit if any, open a fresh Project thread, send the frozen natural acceptance question once
CHANGES_NETWORK_STATE = NO
RETURN = paste or share the first response only

Do not ask the user to test multiple devices, multiple prompts, or multiple iterations for this final acceptance.

## 12. Completion boundary

A successful public-safe G4 is necessary but does not replace this user-selected real consumption check.

This acceptance also does not itself authorize:

- main integration;
- release/tag/publication;
- private Project data export;
- live network mutation.

Until the user acceptance occurs:

FINAL_SERVER_VPS_USER_ACCEPTANCE=PENDING

The implementation can be technically review-PASS while still waiting for this user acceptance. Overall release/closure must not claim the user's real consumption test has passed until it actually has.
