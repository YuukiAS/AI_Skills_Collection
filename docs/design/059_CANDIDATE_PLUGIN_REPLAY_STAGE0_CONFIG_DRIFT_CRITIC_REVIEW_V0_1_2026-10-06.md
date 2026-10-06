# 059 Candidate Plugin Replay Stage 0 config drift — Critic Review v0.1

日期：2026-10-06  
角色：独立 Critic  
审查阶段：STAGE0_RECOVERY_FAILURE_ATTRIBUTION

## 结论

```text
RESULT=REVISE
FAILURE_CLASS=OVER_BROAD_RESTORATION_INVARIANT
ISOLATION=WORKED
PACKAGE_EQUIVALENCE=PROVEN
NORMALIZED_PLUGIN_STATE_EQUIVALENT=YES
ONLY_BLOCKER=FULL_CONFIG_FILE_HASH_DRIFT
MODIFY_RESEARCH_AUTHORING_PRODUCTION=NO
FINAL_GATES_MAY_START=NO
```

本次 Stage 0 停止是正确的，但新证据说明冻结的“整个 `config.toml` 文件 hash 必须与旧 transaction 完全一致”这一条件过宽，不能继续作为 quarantine duplicate cleanup 的 hard gate。

## 直接证据

Stage 0 evidence：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/stage0_equivalent_rehydration_recovery/STAGE0_EQUIVALENT_REHYDRATION_RECOVERY.json`

确认：

- `research-authoring` original tree hash == quarantine tree hash == recorded pre-run tree hash；
- original plugin manifest hash == quarantine manifest hash == recorded hash；
- marketplace/plugin/version/path identity unchanged；
- quarantine transaction ownership proven；
- candidate path reads > 0；
- original conflict path reads = 0；
- quarantine path reads = 0；
- current normalized plugin state == recorded normalized plugin state；
- 唯一 mismatch 是：
  `recorded_config_hash=b98403...`
  vs
  `current_config_hash=ca3bf9...`。

因此当前证据不支持“cache package 或 plugin identity发生不确定变化”。它只证明用户级 config 文件在 transaction 之后某个时点发生过其他变化。

## CPR-CFG1 — full config-file hash 不应阻断 transaction-owned duplicate cleanup

**requirement**

Recovery gate必须验证 helper实际拥有和可能破坏的状态，而不能要求整个用户级配置文件在数小时后的 Stage 0 仍逐字节等于 replay 开始时。

**direct evidence**

当前 helper从未修改 `$CODEX_HOME/config.toml`。Stage 0同时证明：

- plugin package内容完全等价；
- plugin manifest完全等价；
- plugin identity/path完全等价；
- normalized plugin state完全等价；
- live conflict没有被child消费；
- quarantine是本transaction所有。

只有完整 config 文件hash变化。

**causal risk**

继续把完整 config hash 作为 hard gate，会把与 candidate replay无关的合法用户/Host配置变化永久解释为 recovery ambiguity。

由于旧 manifest只保存了整文件 hash，没有保存 config内容或“plugin-relevant config projection”，当前 historical transaction之后也无法再反推出是哪一项配置变化。

这意味着按旧规则继续等待不会获得新证据，只会永久卡住这笔 transaction。

**minimum closure**

Planner只需做一个很窄的 amendment：

1. 删除“整个 config.toml hash必须相等”作为 equivalent-rehydration cleanup 的必要条件；
2. config hash继续记录为 diagnostic/provenance，但 drift本身不阻断 cleanup；
3. hard gate继续绑定 helper真正需要恢复的状态：
   - exact original/quarantine/recorded tree hash equality；
   - plugin manifest hash equality；
   - marketplace/plugin/version/path identity；
   - transaction ownership；
   - candidate consumed；
   - original/quarantine read count = 0；
   - normalized non-candidate plugin state equality；
   - final original package + normalized plugin state equality；
4. 如果未来确实需要判断 plugin-relevant config，必须在新transaction开始前保存一个明确、最小的 plugin-relevant projection；不得用整个 config文件hash代替；
5. 对当前 stale transaction，由于没有历史 config内容快照，不要求事后推测 config diff；
6. 当前旧 multi replay继续永久 FAIL，不retroactive PASS；
7. cleanup后形成新 I2，再重新跑 deterministic + single + multi + 059 development replay。

**owner**

Planner。

## 当前安全边界

在新的 execution-ready amendment通过并获得用户授权前：

- 不删除当前 quarantine；
- 不启动新 replay；
- 不修改 Research Authoring；
- 不启动 final Gates。

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

CURRENT_REPLAY_INFRASTRUCTURE_HEAD=
3ec2714e5f7ea386833ee54c365e923235603819

STAGE0_EVIDENCE_COMMIT=
a76d7c36d45e52eaf6b771fd604b691c7b67244c

NEXT_HANDOFF=PLANNER
```
