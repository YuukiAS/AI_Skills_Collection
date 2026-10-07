# 059 Research Authoring C3 正常入口所有权收口 — Execution-Ready Critic Review v0.2

日期：2026-10-07  
角色：独立 Critic  
审查阶段：EXECUTION_READY_REVIEW_AFTER_C2_G1_FINAL_FAIL  
Task：`research-authoring--formal-production-authoring`

## 结论

```text
RA-C3ER1=CLOSED
RESULT=PASS
READY_FOR_CODEX=YES

C2_G1_FAIL=PERMANENT
C3_NOT_CREATED=YES

FINAL_GATES_AUTHORIZED=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
```

v0.2 已关闭上一轮唯一 blocker，没有引入新的 production scope、Gate、权限或架构变化。

本 PASS 只批准 C3 bounded implementation、deterministic validation、完整 11-case development runtime matrix、candidate metadata/docs closure、exact-C3 offline wrapper preparation，以及 exact task branch 的普通 non-force push。

真正实现授权只有用户随后实际发送本次逐字批准的 Kickoff v0.2 后才成立。

## RA-C3ER1 closure

上一轮 blocker 是：

`profiles/codex-research-writing.json` 将被修改为 authoring/source/package-only profile，但原 matrix 没有任何真实 normal-entry case直接消费这个 profile。

v0.2 新增 `DEV-11 codex-research-writing authoring-only profile`，并把它与其他 development cases绑定到同一个 provisional product commit P。

DEV-11 的环境要求直接覆盖 blocker中的真实竞争条件：

- fresh task-local project；
- 正常安装 exact P 的真实 `codex-research-writing` profile；
- 通过 repository normal profile install path写入 managed AGENTS routing notes；
- generic `pdf` Skill保持安装/可见；
- 当前机器若正常可见 `render-chinese-math-pdf`，不得隐藏或卸载；
- 不允许 renderer/PDF command blacklist、fixture/path/hash特判。

它还要求真实 runtime 同时证明：

- managed AGENTS routing notes确实存在；
- Research Authoring core/paper实际读取；
- manuscript source/package真实产生；
- downstream production handoff真实产生；
- generic `pdf` 没有成为新科研文档 artifact owner；
- `render-chinese-math-pdf` 没有执行；
- PDF mechanics command为零；
- final PDF artifact为零。

因此它不只是静态 profile检查，而是真实消费与负向 owner证据。

`RA-C3ER1=CLOSED`。

## v0.2 synchronization

已核对：

- Implementation Plan v0.2包含 DEV-11、证据要求、11-case same-P PASS规则；
- Canonical Goal v0.2包含相同 profile case与 stop semantics；
- Kickoff v0.2授权运行 DEV-11，并明确 generic pdf / global renderer保持真实可见且不得通过隐藏/卸载/blacklist过关；
- Capability Gate impact v0.2明确 DEV-11只是 pre-final development evidence，不是 G5，也不替代 final G1；
- Execution package v0.2的 locator、commit、matrix identity一致；
- Proposal v0.1和 ChatGPT Plugin offline preparation v0.1保持不变。

所有上述对象在当前 branch 与其声明 commit内容逐字一致。

## Production drift check

比较上一轮 Critic commit：

`75df537cd5f167e9df8afae9670a993cef137b58`

到当前 handoff HEAD：

`eed628c1186b04208e8f42dce396edf4c151dec7`

仅新增本轮 v0.2 design/goal/kickoff/package/handoff文档。

没有 `skills/**`、`plugins/**`、`profiles/**`、`scripts/**`、`tests/**`、`README.md`、`CHANGELOG.md` 或 `VERSION` production变化。

因此本轮 review仍然是纯 execution-package复核，没有提前实现。

## Architecture / scope carry-forward

上一轮已经通过且本轮未重新打开的结论继续成立：

- C2 G1是真实永久 FAIL；
- 根因是 Research Authoring 与 renderer之间缺少可执行的 normal-entry owner admission；
- 修复层为 Research Authoring canonical boundary + renderer discovery boundary + existing profile routing；
- aggregate-only修复不再接受；
- `latex-paper-authoring` 的提前 artifact-owner风险需要一起收口；
- generic `pdf` 当前只作为 runtime negative owner验证，不预先扩大 source修改；
- renderer engine/font/PDF-QA scripts不改；
- 不新增 G5；
- shared candidate replay / Bridge不改。

如果 11-case matrix中 generic pdf实际抢 owner、profile routing notes没有被正常入口消费、standalone仍然使用 renderer、research-main顺序错误、render-only开始加载 Research Authoring，Executor必须 STOP；不得自行扩 scope或继续堆 wording patch。

## Same-candidate / candidate freeze

完整 source/tests/generated/version/docs先形成：

`C3_PROVISIONAL_PRODUCT_COMMIT=<P>`

11个 development case全部在 exact same P 上运行。

只有全部 PASS，且期间没有 candidate-owned product变化，才允许：

`C3_FINAL_CANDIDATE_COMMIT=<same P>`

任何 product edit都会使旧 matrix evidence降为 regression，并要求形成新 P 后完整重跑 matrix。

因此没有跨 candidate拼接风险。

## Gate boundary

```text
ADD_G5=NO
G1_G4_TAXONOMY_CHANGED=NO
C3_DEVELOPMENT_MATRIX=PRE_FINAL_REGRESSION_ONLY
FINAL_GATES_NOT_STARTED=YES
```

C3 development PASS仍不等于 G1 PASS，也不等于 Research Authoring 0.3完成。

C3形成并通过后续独立 development review后，Planner仍需冻结新的 C3 pre-final packet；最终 G1-G4必须从头绑定同一 C3。

## Version / offline Plugin preparation

批准当前 candidate策略：

- `research-writing` 继续同一未发布 `0.3` candidate line，不机械升到 0.4；
- 如果 `render-chinese-math-pdf` discovery/trigger behavior真实修改且完整 matrix PASS，则 standalone Skill形成 `0.3` candidate；
- repository `VERSION=5.4.4` 在本 bounded implementation期间不变；
- formal repository PATCH只在最终 G1-G4全部通过后的 release closure决定。

C3 freeze后必须提前准备 exact-C3 skills-only `research-authoring` offline wrapper、完整 file/hash manifest、same-C3 Clear Writing snapshots和未来 guarded-update input。

本 PASS不授权 Plugin Creator或 live Plugin update。

## Maintenance tracking

Issue #99 reader-facing内容仍旧落后于真实状态。该问题不阻断 execution-ready PASS。

由于 Issue实质改写必须先真实调用 Clear Writing，本 Critic线程不直接改写。

下一次具备合法 Clear Writing + Issue/Project mutation能力的维护动作应同步当前 C2 permanent FAIL / C3 implementation状态，Project lifecycle继续 `DOING`，不得提前 DONE。

## Approved package

```text
APPROVED_PROPOSAL_PATH=docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md
APPROVED_PROPOSAL_COMMIT=b4820e49e3473959010afe5fa1e9f92bc0f4844f

APPROVED_PLAN_PATH=docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_2_2026-10-07.md
APPROVED_PLAN_COMMIT=04272c05c59ec90ee068b0d5da8d7a02beee3afa

APPROVED_GOAL_PATH=docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_2.md
APPROVED_GOAL_COMMIT=539ed6114dc861b129b6808b3b9a57c2763b7242

APPROVED_KICKOFF_PATH=docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_2.md
APPROVED_KICKOFF_COMMIT=de770b31c840cda0feb587c5670d60450cf68726

APPROVED_CAPABILITY_GATE_IMPACT_PATH=docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_2_2026-10-07.md
APPROVED_CAPABILITY_GATE_IMPACT_COMMIT=164051ebde003354e1303a086214a109c8f595bf

APPROVED_PACKAGE_PATH=results/research-authoring--formal-production-authoring/C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_EXECUTION_PACKAGE_V0_2.md
APPROVED_PACKAGE_COMMIT=6b8002055c024de22e72dfc14e8cb850ae07fa71

APPROVED_PLUGIN_PREPARATION_PATH=docs/operations/059_RESEARCH_AUTHORING_C3_CHATGPT_PLUGIN_PREPARATION_V0_1.md
APPROVED_PLUGIN_PREPARATION_COMMIT=6320925c0b3a08f480d56f69908c40edd3b6d03e

READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```
