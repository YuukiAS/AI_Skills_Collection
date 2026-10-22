# Planner–Critic 1.8 v0.13：最终 execution-ready 待审包

日期：2026-10-22  
任务：`chatgpt-web--pass-integrity`  
分支：`design/chatgpt-web--pass-integrity-v0-4`  
阶段：`FINAL_EXECUTION_READY_REVIEW_V0_13`  
当前：`READY_FOR_CODEX=NO`；正式 main 仍为 Planner/Critic 1.7。

本 manifest **不保存自身所在提交 SHA**。调用方在 final Critic prompt 中提供当前分支最新 exact `PACKAGE_COMMIT`。这个 commit 是 Critic 开始审查前已经存在的 immutable package；它不能、也不需要包含审完它之后才产生的 current final Critic reply。

## 1. 当前 immutable PACKAGE_COMMIT 的完整文件

Critic 必须从同一 PACKAGE_COMMIT 读取：

1. `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_13_2026-10-22.md`
2. `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_13_2026-10-22.md`
3. `docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_13.md`
4. `docs/operations/prompts/CHATGPT_WEB_DECISION_VISIBILITY_KICKOFF_DRAFT_V0_13_2026-10-22.md`
5. `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_13_2026-10-22.md`
6. `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_FINAL_CRITIC_PROMPT_V0_13_2026-10-22.md`
7. 本 manifest
8. 已经发生的历史审查 authorities：
   - `results/chatgpt-web--pass-integrity/FINAL_CRITIC_V0_12_USER_FORWARDED_REVISE_2026-10-22.md`
   - `results/chatgpt-web--pass-integrity/FINAL_CRITIC_V0_11_USER_FORWARDED_REVISE_2026-10-22.md`
   - `results/chatgpt-web--pass-integrity/DESIGN_CRITIC_V0_10_USER_FORWARDED_HANDOFF_2026-10-22.md`
9. `results/chatgpt-web--pass-integrity/USER_PARTIALLY_ACCEPTED_MULTIROUND_EXPLANATION_2026-10-22.md`，仅开发参考，不是技术历史/金标准。

**当前 v0.13 final Critic reply 不在以上列表。** 它只会在审查完成后产生。

## 2. v0.13 唯一实质修改：关闭 DV12-01

v0.12 的 DV11-01 / DV11-02 已被独立 Critic确认关闭，本版不重开。

v0.13 只区分：

```text
审查前：
PACKAGE_COMMIT = immutable source
（尚未获得 implementation-approved 身份）

审查后且 Critic真正 PASS + READY：
IMPLEMENTATION_APPROVED_PACKAGE = reviewed_package_commit
BOOTSTRAP_CRITIC_AUTHORITY = post-review approval authority
```

`BOOTSTRAP_CRITIC_AUTHORITY` 由当前正式1.7 final reply/short `COPY TO CODEX` 自包含携带，至少含 review stage、PASS/READY、approved locators、实施授权边界和关键 limitations。它不是新的 workflow state/schema/service，也不属于原 package commit。

当前 Critic `REVISE` → 不存在 implementation-approved package 资格、无 bootstrap authority、不得启动Codex。

当前 Critic `PASS` → exact reviewed package获得 implementation-approved 身份；用户发送带 bootstrap authority 的短 Codex handoff 后，Codex 才可如实记录自己实际收到的 evidence并实施。完整 Critic自然中文全文如之后实际取得，可以另存为 post-review evidence，但不是启动前提，也不能倒填到原 package。

## 3. 其它冻结语义不变

继续完全采用 v0.12 已关闭并独立确认的：
- 全部 P18-0…P18-7；
- 全部 C18-0…C18-7；
- future technical PASS → Planner delivery acceptance → short Codex；
- current bootstrap按正式1.7 direct Codex；
- exact `GOVERNANCE_CANDIDATE_COMMIT` 和 candidate-source drift invalidation；
- current eight-case deterministic replay；
- A/B/C/C2/D/E/F；
- critical-interface reality、pre-side-effect/conditional verification；
- non-terminal handoff；
- whole-response acceptance；
- post-implementation Critic safety gate；
- fresh Web user-only boundary；
- main integration + remote readback；
- F新真实任务出现前 `NOT_VERIFIED` claim ceiling。

历史 v0.7/v0.8/v0.9/v0.10/v0.11/v0.12 只作历史证据，不是当前 implementation authority。

## 4. 当前权限与下一入口

仍只允许独立 Critic进行最终只读审查。未有 `PASS + READY_FOR_CODEX=YES`，不修改正式角色合同、不启动Codex、不修改main或任何产品。

若最终 PASS：Critic按当前正式1.7直接给短 `COPY TO CODEX`；该 handoff必须携带启动所需的 `BOOTSTRAP_CRITIC_AUTHORITY`，但不复制整篇 Critic自然中文全文。用户实际发送后才授权 implementation。

若最终 REVISE：继续同 task key 回 Planner，不产生 implementation-approved identity。

## 5. Maintenance Board

本任务仍属于 repo-level governance maintenance。当前未确认可复用专属 Issue，且当前线程没有可证明的正式 Clear Writing invocation 用于新 reader-facing Issue copy，因此不创建或伪报 Project同步。后续合法维护入口按 Board语义搜索/reuse后再同步；用户无需手工维护。该 metadata 不阻塞本次只读 final Critic review。
