# 059 Candidate Plugin Replay Stage 0 config drift — Execution-Ready Critic Review v0.1

日期：2026-10-06  
角色：独立 Critic  
审查阶段：EXECUTION_READY_REVIEW  
Task：`research-authoring--formal-production-authoring`

## 结论

```text
RESULT=PASS
READY_FOR_CODEX=YES
```

本 PASS 只批准 Stage 0 config-drift recovery amendment 的 bounded implementation、当前 preserved transaction 的 conditional cleanup、后续 I2 验证与三类 risk-matched replay。

真正的 quarantine duplicate 删除权限，只有在用户实际发送本审查逐字批准的 Kickoff 后才成立。

不批准 Research Authoring production change、live Plugin update、Bridge/Host change、G1-G4 final Gates、G4 ChatGPT、PDF production、paid API、main merge 或 release。

## 批准绑定

Recovery amendment：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_RECOVERY_AMENDMENT_V0_1_2026-10-06.md`

Goal amendment：

`docs/goals/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_GOAL_AMENDMENT_V0_1.md`

Kickoff amendment：

`docs/operations/prompts/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_KICKOFF_AMENDMENT_V0_1.md`

Package commit：

`d5bbe357f280d4a80c95206dbda57c6ac7be530d`

以上三份文件在当前 branch 与 package commit 内容完全一致。

## Stage 0 证据裁定

已读取：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/stage0_equivalent_rehydration_recovery/STAGE0_EQUIVALENT_REHYDRATION_RECOVERY.json`

当前 Stage 0 已直接证明：

- original tree hash == quarantine tree hash == recorded pre-run tree hash；
- original plugin manifest hash == quarantine manifest hash == recorded pre-run manifest hash；
- marketplace/plugin/version/path identity unchanged；
- quarantine transaction ownership proven；
- candidate actual consumption proven；
- original conflict path reads = 0；
- quarantine path reads = 0；
- current normalized plugin state == recorded normalized plugin state。

唯一 mismatch 是整个 `$CODEX_HOME/config.toml` 文件 hash 漂移。

由于 helper既不拥有也不恢复整个用户配置文件，且历史 transaction没有保存 config内容或 plugin-relevant projection，因此完整 config-file hash不应继续作为 duplicate cleanup hard gate。

## Amendment correctness

本 amendment 正确地把 full config hash 降为 diagnostic/provenance，而不是直接删除所有 config safety。

Hard gates继续严格绑定 helper真正拥有和需要恢复的状态：

- exact package tree；
- plugin manifest；
- marketplace/plugin/version/path identity；
- transaction ownership；
- candidate/live read evidence；
- normalized non-candidate plugin state。

cleanup 后还必须重新验证：

- rehydrated original tree/manifest/identity；
- normalized plugin state与 cleanup-precondition state相等；
- quarantine duplicate已不存在；
- recovery manifest只在最终验证成功后删除。

任何 hard gate 或 final verification缺失/不一致，仍返回 `RESTORATION_AMBIGUOUS`，不得删除、覆盖、继续 replay或 claim PASS。

## Future config handling

如果未来确实需要 plugin-relevant config invariant，必须在新 transaction 开始前保存明确、最小的 projection。

不得重新用整个 `config.toml` hash作为替代。

当前历史 transaction没有 config内容快照，因此不要求 Executor事后猜测 config diff。

## Validation / identity

实现后形成新的：

`REPLAY_INFRASTRUCTURE_COMMIT=<I2>`

旧 multi replay继续永久：

`FAIL / RESTORATION_AMBIGUOUS`

I2 必须重新依次通过：

1. deterministic tests；
2. representative single-plugin replay；
3. `web-development + writing-style` multi-plugin replay；
4. multi PASS后 exact 059 `ac501d98...` development replay。

旧 single PASS不能跨 infrastructure candidate拼接为 I2 PASS。

Research Authoring product identity继续：

`ac501d988f00cb6672fec105ae5fd51a0679cae0`

即使全部 development replay PASS，Executor仍不得自行宣称 C2 ready，必须停止给 Planner。

## Approved fields

```text
APPROVED_AMENDMENT_PATH=docs/design/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_RECOVERY_AMENDMENT_V0_1_2026-10-06.md
APPROVED_GOAL_AMENDMENT_PATH=docs/goals/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_GOAL_AMENDMENT_V0_1.md
APPROVED_KICKOFF_AMENDMENT_PATH=docs/operations/prompts/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_KICKOFF_AMENDMENT_V0_1.md
APPROVED_PACKAGE_COMMIT=d5bbe357f280d4a80c95206dbda57c6ac7be530d
READY_FOR_CODEX=YES
```
