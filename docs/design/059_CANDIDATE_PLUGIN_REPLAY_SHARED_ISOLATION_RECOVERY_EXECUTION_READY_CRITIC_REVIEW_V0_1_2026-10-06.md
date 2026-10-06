# 059 Candidate Plugin Replay 共享隔离恢复 — Execution-Ready Critic Review v0.1

日期：2026-10-06  
角色：独立 Critic  
审查阶段：EXECUTION_READY_REVIEW  
Task：`research-authoring--formal-production-authoring`

## 结论

```text
RESULT=PASS
READY_FOR_CODEX=YES
```

本 PASS 只批准 bounded shared replay infrastructure implementation。真正的用户级本地 plugin-cache mutation 只有在用户随后实际发送已批准 Kickoff 时才获得授权。

不批准 Research Authoring production change、live Plugin update、G1-G4 final Gates、G4 ChatGPT、PDF production、paid API、main merge 或 release。

## 批准绑定

Approved Proposal：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_PROPOSAL_V0_2_2026-10-06.md`  
commit：`f479efb4e2ad31eaafe6ec56b9fc0ba3f284c569`

Architecture Critic PASS：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_CRITIC_REVIEW_V0_2_2026-10-06.md`  
commit：`307904418e42b704e8bf6e0f1f27aa93c1368a87`

Implementation Plan：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md`  
commit：`8dbe6b4ee0d359436b231d21632963b4b40346f1`

Canonical Goal：

`docs/goals/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_GOAL_V0_1.md`  
commit：`c2eac9aa677fbeffed5114269dfac93c2bd03590`

Kickoff：

`docs/operations/prompts/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_KICKOFF_V0_1.md`  
commit：`32eae60e7edbd704a9a49df823cd029ce9a831f2`

Package index：

`results/research-authoring--formal-production-authoring/CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_EXECUTION_PACKAGE_V0_1.md`  
commit：`4d6775e1d0fb18d5af3bc533a41cb7a30f8f6d53`

Plan、Goal、Kickoff、package index 在当前 execution branch 的内容与各自声明 commit 完全一致。

从 architecture Critic PASS `307904418...` 到 package commit `4d6775e1...` 的变化仅为本 execution package 文档；没有 shared helper source、Research Authoring production 或 live Plugin mutation提前发生。

## 最新 policy / execution context

审查时核对：

- AI_Skills_Collection main：`8bd44fb792c1b51f30bb3f4cd883e969abfa1518`
- Bridge Kit main：`9d60f4cf949c9da327a154001b13881cfd91233b`

执行包继续复用既有 exact task / branch / worktree：

- task：`research-authoring--formal-production-authoring`
- branch：`work/research-authoring--formal-production-authoring`
- worktree：`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

无需 successor task/branch，也无需 watcher、daemon、数据库、状态机或 Bridge 修改。

## Scope 审查

执行包忠实限制在三个 shared helper 文件：

- `scripts/candidate_plugin_replay.py`
- `tests/test_candidate_plugin_replay.py`
- `docs/workflows/CANDIDATE_PLUGIN_REPLAY.md`

及 task-local recovery evidence。

它明确 ZERO WRITE Research Authoring production、`ac501d98...` product tree、live Plugin、Plugin Creator remote object、Bridge、Host Policy、profiles、Marketplace production payload、versions、README、main/release、G1-G4 frozen semantics。

没有发现 implementation 必须但被遗漏的第四个 production/helper source file。若实际实现证明当前三文件范围不足，Executor 必须停止回 Planner/Critic，不能自行扩大。

## Conflict detection

执行包严格保持已批准的最小 generic signal：

`exact top-level Skill frontmatter name overlap`

不按 `research-writing`、`research-authoring`、`created-by-me-remote` 或 059 特判，也不引入 description similarity、embedding 或 LLM semantic matching。

multi-candidate 的 union / duplicate fail-closed 语义与 Proposal 一致。

## Quarantine / restoration

执行包完整落实 CPR1：

- quarantine 在 plugin discovery/cache root 外；
- resolve original/discovery/quarantine paths；
-拒绝 symlink resolve 回 discovery root；
- destination 不得覆盖已有用户数据；
- mutation 前必须满足 `original.st_dev == quarantine_parent.st_dev`；
- 不满足时 `SAFE_QUARANTINE_UNAVAILABLE`；
-禁止 cache-hidden fallback、copy+delete、cross-filesystem move、CLI uninstall/reinstall、Plugin Creator 或 prompt fallback。

Recovery manifest字段足以在 crash 后识别 package、原/目标路径、身份、hash、filesystem 和 transaction phase。

事务顺序也正确：live package restore 在 candidate cleanup 前完成，之后做 final equality；这样即使 candidate cleanup 本身触发额外 plugin machinery，最终 equality 仍能捕获用户状态漂移。

normal failure/timeout/exception/SIGINT/catchable SIGTERM走 restore；SIGKILL/power loss 由下一 helper entry 先处理 stale manifest。ambiguous 状态不覆盖、不删除、不继续 child。

## Concurrency preflight

执行包没有过度宣称可以证明“绝对无并发”。它只要求只读检查明显共享同一 effective CODEX_HOME 的其他 active Codex consumer。

positive detection时 fail closed，不 quarantine、不 kill/pause/signal/takeover。

这与已批准架构一致，也与当前 Bridge Host 的 read-only `ps` 诊断边界兼容。没有必要增加全局锁服务或进程协调系统。

## Consumption proof

最终 PASS 条件同时要求：

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
```

account-backed original-path rehydration、original read 或 quarantine read 任一发生都强制 replay FAIL，即使 candidate 同时被消费。

因此执行包没有留下“candidate + conflict都被读但仍 PASS”的漏洞。

## Tests / real replay

确定性测试覆盖与风险匹配，不需要机械重跑全部历史任务。

代表性 runtime replay 只包含：

1. 一个已有 public-safe single-plugin replay；
2. 一个已有 `web-development + writing-style` multi-plugin replay；
3. exact 059 `ac501d98...` blocking development replay。

这三类分别覆盖 no-conflict/single、multi-candidate、以及本次真实 competing consumer failure。

059 replay仍禁止通过更强 prompt blacklist制造 PASS。

## Identity / stop state

执行包保持三层 identity：

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

REPLAY_INFRASTRUCTURE_COMMIT=<I>

EVIDENCE_PACKET_HEAD=<E>
```

helper/evidence commit不得成为 Research Authoring product candidate。

即使 exact 059 development replay PASS，Executor也必须：

```text
C2_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```

由 Planner 后续决定是否把 unchanged `ac501d98...`提升为 C2并冻结新的 final packet。

## User-level authorization

Kickoff 已把真正高影响动作写成清楚、限定的一次性授权：

-只在 existing replay lock内；
-只移动自动检测到 exact Skill-overlap 的 conflicting local cached package；
- out-of-discovery、same-filesystem atomic rename；
- bounded read-only concurrency preflight；
- success/failure/timeout exact restore；
- stale recovery；
- ambiguous recovery fail closed；
- temporary quarantine窗口可能让共享同一 CODEX_HOME 的其他本地 Codex暂时看不到该 live Plugin。

同时明确排除 remote Plugin/Plugin Creator、permanent uninstall、其他进程控制、Research Authoring修改、final Gates、PDF、paid API、Bridge/Host、main/release和 destructive Git。

因此用户实际发送该 Kickoff 后，授权范围足够且没有过度扩大。

## Approved fields

```text
APPROVED_PROPOSAL_PATH=docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_PROPOSAL_V0_2_2026-10-06.md
APPROVED_PROPOSAL_COMMIT=f479efb4e2ad31eaafe6ec56b9fc0ba3f284c569

APPROVED_PLAN_PATH=docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md
APPROVED_PLAN_COMMIT=8dbe6b4ee0d359436b231d21632963b4b40346f1

APPROVED_GOAL_PATH=docs/goals/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_GOAL_V0_1.md
APPROVED_GOAL_COMMIT=c2eac9aa677fbeffed5114269dfac93c2bd03590

APPROVED_KICKOFF_PATH=docs/operations/prompts/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_KICKOFF_V0_1.md
APPROVED_KICKOFF_COMMIT=32eae60e7edbd704a9a49df823cd029ce9a831f2

APPROVED_PACKAGE_PATH=results/research-authoring--formal-production-authoring/CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_EXECUTION_PACKAGE_V0_1.md
APPROVED_PACKAGE_COMMIT=4d6775e1d0fb18d5af3bc533a41cb7a30f8f6d53

READY_FOR_CODEX=YES
```
