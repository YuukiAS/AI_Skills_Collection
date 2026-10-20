# Clear Writing 0.6 — execution-ready Critic re-review prompt v0.2

你继续担任同一独立 Critic。上一轮对 package `a6625909c0b5a0bf61904e6c7bc97ecf308f7bee` 的结论是：

```text
DECISION=REVISE
READY_FOR_CODEX=NO
```

本轮 **只复核四个 blocker**：

- `CW06-ER01` route projection package portability；
- `CW06-ER05` G4/G6 循环 + G2-T3 source delivery；
- `CW06-ER08` deterministic raw ZIP identity；
- `CW06-ER09` forward restore。

不要重新打开已经通过的 Clear Writing 0.6 架构、G1/G2/G3/G5 主体、GitHub-only external claim、model/attempt/retry/stop、版本方向和 Issue #13 设计，除非 v0.2 为关闭 blocker 明确破坏了这些已接受约束。

## 1. Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin = writing-style / Clear Writing
task_key = clear-writing--single-entry-artifact-finalization
branch = design/clear-writing--single-entry-artifact-finalization
approved_proposal = 3eefc626b86566113125a06fc6046a2bec1eafb2
reviewed_v0_1_package = a6625909c0b5a0bf61904e6c7bc97ecf308f7bee
review_stage = EXECUTION_READY_REVIEW_V0_2
```

用户会同时给你唯一：

`PACKAGE_COMMIT=<exact v0.2 package commit>`

必须从该 exact commit 读取以下五份 v0.2 文件：

1. `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_2_2026-10-20.md`
2. `docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_2_2026-10-20.md`
3. `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_2_2026-10-20.md`
4. `docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_2_2026-10-20.md`
5. `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_CRITIC_PROMPT_V0_2_2026-10-20.md`

若五份文件不是同一 exact commit 快照，直接 REVISE。

先读取最新 main 的 `AGENTS.md`、Planner/Critic 1.7、Capability Gate Policy 1.2、维护看板、版本规范、writing-style TODO，并只读回查 current Clear Writing 0.5.0 / PIE 0.2.8 Plugin Creator现实。不要实施。

## 2. CW06-ER01 closure

核实 Planner 是否真实审计六项 route 的 package/repo-root locator，而不是只修一个字符串。

v0.2 冻结的唯一 transform 必须是：

`CW06_ROUTE_PROJECTION_V1`

只允许：

1. `skills/writing/core/scientific-rewrite/scripts/rewrite_support.py`
   ->
   `skills/clear-writing/references/routes/scientific-rewrite/scripts/rewrite_support.py`

2. `docs/provenance/WRITING_SKILL_REPOS_2026_07_28.md`
   ->
   `skills/clear-writing/references/routes/scientific-prose/references/provenance/WRITING_SKILL_REPOS_2026_07_28.md`

当前 source 预期各出现 1 次。

检查：

- relative support paths 都在生成包真实存在；
- `chinese-prose/TODO.md` maintenance-only，不进入 runtime；
- provenance file 是 byte-copy；
- transformed ROUTE inverse-transform 后必须 byte-equal canonical SKILL；
- non-transformed ROUTE byte-equal；
- support files byte-equal；
- transform count/source/generated path均 fail closed；
- scientific-rewrite helper使用真实 package-local path；
- runtime若不能执行 helper，heavy route不能假 PASS。

如果还有未处理的真实 package locator，REVISE；不要要求为正文中的示例 path 做无意义 transform。

## 3. CW06-ER05 closure

核实：

- G4 正式 pre-G6 输入只包含 G2 + G3；
- G4 PASS 可进入 G6前置；
- G6自己先 source->final fidelity，fidelity PASS 后才 reader-quality；
- G6 fidelity 不反向加入 G4；
- final independent review只汇总 G4 + G6，不新增第七 Gate。

G2-T3 必须冻结唯一 source delivery：

```text
repo = YuukiAS/AI_Skills_Collection
ref = 1f905d294c3c2e5b0951c9d5e818c285d236cef7
path = docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md
```

exact Web prompt 必须携带 repo/ref/path并要求读取全文。fresh conversation不得用旧聊天、摘要、其他 ref 或临场决定贴全文。

## 4. CW06-ER08 closure

核实唯一 archive identity：

`CW06_DETERMINISTIC_ZIP_V1`

必须固定：

- sorted POSIX file entries；
- no directory entries；
- ZIP_STORED；
- 1980-01-01 00:00:00 timestamp；
- create_system=3；
- regular-file mode 0644；
- empty extra/comments；
- no environment metadata；
- same source two builds raw ZIP bytes identical。

`wrapper_archive_sha256` 必须是 exact raw ZIP bytes 普通 SHA-256，BUILD_RECEIPT记录同值。任何 raw byte drift = FAIL。

不得保留“timestamp 或 canonical hash任选”。

## 5. CW06-ER09 closure

先重新核对 current Plugin Creator contract：

- overlay；
- expected_release_id；
- exact file-only delete_paths；
- upload/delete same path 禁止；
- lower version拒绝；
- no restore-old-release。

### 5.1 重点检查上一轮返修文字中的真实冲突

current 0.5.0 file set没有 root `plugin.json`，而 0.6.0有。若 forward restore 又要求上传一个 0.6.1 root manifest，那么 root `plugin.json` 同时属于 `S06-S05` 和 restore archive。当前工具禁止同一 path 同时 upload + delete。

因此 **不要机械要求一个会被 Plugin Creator 拒绝的 `delete_paths=S06-S05` 调用**。

v0.2 使用两个集合：

- `RESTORE_06_ONLY_PATHS.json: all_06_only_paths=S06-S05`，保留完整审计事实；
- `RESTORE_DELETE_PATHS.json: tool_delete_paths=(S06-S05)-R`，`R` 为 restore archive file set，实际传给工具。

你必须判断这个 tool-valid correction 是否等价关闭原 finding，而没有弱化“所有 stale 0.6 behavior path必须清掉”的要求。

### 5.2 restore archive 与 trigger

核实：

- live mutation前保存完整0.5 archive/file list/current release；
- restore behavior/support bytes与0.5 byte-identical；
- 两 manifest personal version 0.6.1；
- root plugin.json只作为 distribution compatibility；
- same plugin identity + current 0.6 release ID；
- readback验证 no stale 0.6 behavior；
- terminal PRODUCT FAIL（G1-G6或 final artifact review）固定 restore；
- bounded infra retry/wait未耗尽不提前 restore；
- infra最终无法继续时固定 restore，不留未验收0.6.0；
- Plugin Creator不可用时状态 `RESTORE_REQUIRED_BLOCKED_BY_INFRA`，central 0.6 release立即放弃，恢复是工具回来后的唯一下一动作；
- central writing-style 0.6不发布。

若你认为两个集合的修正仍不安全，给出精确 tool-level原因；不要重新设计整个0.6。

## 6. regression check

只检查 v0.2 是否为了四个 blocker 意外破坏以下已通过决定：

- single `clear-writing` ChatGPT entry；
- six canonical writing capabilities；
- Codex six direct exposure；
- GitHub UTF-8-only external-finalization claim；
- Reader Guide G3；
- fresh G6；
- no MCP/App/background/database/state machine；
- model/attempt/retry/stop；
- versions / Issue #13 / README-changelog closure。

没有回归就不要重新审这些架构。

## 7. 禁止

本轮不得：

- 修改 repo/Issue/Project；
- 启动 Codex；
- 更新 Personal Plugin；
- 创建 G3 branch；
- 运行 G1-G6；
- 调用付费模型；
- 把 PASS 当用户执行授权。

## 8. 输出

若四个 blocker全部关闭且无回归：

```text
DECISION=PASS
READY_FOR_CODEX=YES
CW06-ER01=CLOSED
CW06-ER05=CLOSED
CW06-ER08=CLOSED
CW06-ER09=CLOSED
APPROVED_PROPOSAL_COMMIT=3eefc626b86566113125a06fc6046a2bec1eafb2
APPROVED_PACKAGE_COMMIT=<exact PACKAGE_COMMIT>
APPROVED_PLAN=docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_2_2026-10-20.md
APPROVED_GOAL=docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_2_2026-10-20.md
APPROVED_RUNBOOK=docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_2_2026-10-20.md
APPROVED_KICKOFF_DRAFT=docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_2_2026-10-20.md
NEXT_HANDOFF=USER_AUTHORIZATION
```

并明确 PASS 只批准 exact execution package，不是 implementation/Gate/release PASS，用户未发送批准 Kickoff 前不得 mutation。

若仍有 blocker：

```text
DECISION=REVISE
READY_FOR_CODEX=NO
```

只使用原四个 finding ID 或其直接子 finding；附最小返修提示词，不重新设计已通过架构。