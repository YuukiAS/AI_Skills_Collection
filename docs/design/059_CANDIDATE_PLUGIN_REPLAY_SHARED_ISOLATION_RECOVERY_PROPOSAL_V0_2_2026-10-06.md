# 059 Candidate Plugin Replay 共享隔离恢复 — Planner Proposal v0.2

日期：2026-10-06  
状态：DRAFT_FOR_CRITIC_REVIEW / NOT_IMPLEMENTATION_AUTHORIZATION  
Prior Critic review：`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_CRITIC_REVIEW_V0_1_2026-10-06.md`  
Prior Critic commit：`71335266e169eccca892417f21577edfd4546697`  
Prior Critic result：`REVISE`  
Stable blocker：`CPR1`  
Repository：`YuukiAS/AI_Skills_Collection`  
Branch：`work/research-authoring--formal-production-authoring`  
Triggering task：`research-authoring--formal-production-authoring`  
Shared infrastructure owner：AI_Skills candidate replay tooling  
Human workflow number：059

## 0. 当前身份与不可变事实

Research Authoring bounded repair 已完成于：

```text
REPAIRED_PRODUCT_COMMIT =
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

最新 replay-isolation 证据：

```text
EVIDENCE_COMMIT =
0cedb8a3d025c6320de47afac77eac5f7722f675
```

当前事实：

```text
CANDIDATE_REPLAY_ISOLATION_UNAVAILABLE=YES
SHARED_REPLAY_HELPER_CHANGE_MAY_BE_REQUIRED=YES
PRODUCTION_CANDIDATE_CHANGE_REQUIRED=NO
FINAL_GATES_NOT_STARTED=YES
```

本轮禁止修改 Research Authoring production，也不把 helper repair 混入 Research Authoring product identity。

在 shared replay infrastructure 真实修复并让 required development replay 有效通过之前：

`ac501d988f00cb6672fec105ae5fd51a0679cae0`

只能称：

`REPAIRED_PRODUCT_COMMIT`

不能称 ready C2。


### 0.1 CPR1 disposition — ACCEPT

Critic 指出的风险成立：把 quarantine 放在 `$CODEX_HOME/plugins/cache/**` 内，即使目录名是隐藏目录，也不能证明 Codex 不会继续扫描/读取该 package。059 已经证明 process-local `enabled=false` 不能阻止 account-backed live cache 被读取，因此 v0.2 不再依赖“隐藏目录不会被发现”的假设。

v0.2 只修 CPR1，不重新打开已接受结论：

- ROOT_CAUSE 保持 `SHARED_CANDIDATE_REPLAY_CONSUMER_ISOLATION_GAP`；
- preferred approach 保持 temporary local conflicting-plugin suppression + exact restoration；
- exact top-level Skill `name` overlap 继续作为第一版通用 conflict signal；
- Route A/C/D 继续不作为当前 recovery；
- Research Authoring production 不改；
- `REPAIRED_PRODUCT_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0` 保持；
- deterministic tests + single-plugin replay + multi-plugin replay + 059 exact replay 保持；
- 三层 identity 保持。

## 1. ROOT_CAUSE

根因不是 Research Authoring，也不是 G4 prompt。

当前 `scripts/candidate_plugin_replay.py` 做的是**候选命名空间隔离**，不是**候选消费隔离**：

1. exact committed candidate 被安装为：
   `<plugin>@ai-skills-candidate`；
2. child 使用 `codex exec --ignore-user-config`；
3. child process-local 启用 candidate plugin id；
4. helper 只从 child JSONL 中证明 candidate path 的 `SKILL.md` 被实际读取；
5. finally 删除 candidate，并检查 pre-existing **same-name** production plugin snapshot 没变化。

这个机制在没有竞争 consumer 时真实成功过，但它没有保证：

> child runtime 只能看 candidate，或者相同 Skill 路由不会被另一个已安装 Plugin 抢走。

059 暴露出的具体通用缺口是：

```text
candidate plugin identity:
research-writing@ai-skills-candidate

conflicting live wrapper identity:
research-authoring@created-by-me-remote

candidate top-level skills:
research-reporting / research-paper-workflow / literature-and-citations

live wrapper:
暴露相同 Research Authoring skill family
```

当前 helper 的 `same_name_installed_snapshot(..., plugin_name)` 只围绕 candidate 的 plugin name 建立保护边界；`research-writing` 与 `research-authoring` 名字不同，因此这个 live wrapper 不属于 helper 的 conflict/snapshot model。

更关键的是，current Codex child 实际可以读取：

`$CODEX_HOME/plugins/cache/created-by-me-remote/research-authoring/0.3.0/**`

即使：

```text
plugins.research-writing@ai-skills-candidate.enabled=true
plugins.research-authoring@created-by-me-remote.enabled=false
```

process-local override 也没有阻止它。

真实结果：

```text
candidate reads = 0
live wrapper reads = 6
```

所以根因是：

`SHARED_CANDIDATE_REPLAY_CONSUMER_ISOLATION_GAP`

具体是“多个已安装 Plugin 暴露重叠 Skill/路由时，helper 没有通用 conflict detection 和真实消费隔离”。

## 2. 为什么这是 shared infrastructure gap

这不是 059 特判。

历史证据说明同一类 replay-control 问题已经跨插件出现：

### Clear Writing 052

052 的真实 production smoke 发现：

- 单纯换 `CODEX_HOME` / process-local marketplace config 仍会读取已有 live `writing-style 0.1`；
- 最后使用了用户明确授权的 bounded live production identity swap：
  临时把 `yuukias-ai-skills` 指向 candidate、安装 `writing-style 0.2`、跑 normal smoke、再恢复原 marketplace/plugin；
- before/after marketplace source、plugin version/path 都被验证恢复。

这说明“live plugin 抢 candidate”早于 059 存在。

### Clear Writing 055

`candidate_plugin_replay` 曾因 child hang 无法产出有效 receipt。
修复 commit `028ff02f...` 只改 shared child lifecycle/timeout/cleanup，没有把 helper commit算进 Clear Writing product candidate。
修复后同一个 C6 candidate replay成功。

这个历史已经建立了正确 identity split：

```text
product candidate
!=
shared replay infrastructure repair
!=
evidence head
```

### workflow-core / ai-skills-core / web-development

现有 helper 已真实成功证明：

- `workflow-core@ai-skills-candidate` consumption；
- `ai-skills-core@ai-skills-candidate` consumption；
- `web-development@ai-skills-candidate` consumption；
- web-development + writing-style same-session candidate consumption。

这些成功说明 helper主体仍有价值，不应另造 replay framework；059 暴露的是“存在重叠 live consumer 时”的缺失分支。

## 3. Current-runtime / external evidence

当前 pinned runtime 为：

`codex-cli 0.153.4`

059 已保存真实 CLI help 和真实运行证据。

当前 help 暴露：
- `-c/--config`
- `--profile`
- `--ignore-user-config`
- plugin add/list/remove/marketplace commands

但没有暴露独立的：
- plugin store root；
- plugin cache root；
- plugin registry root；
- “only load these plugins” child option。

真实 process-local disable probe已经失败，因此不能继续重复同一种 config override。

OpenAI 当前 Plugin 文档说明 local installs会落在 `~/.codex/plugins/cache/<marketplace>/<plugin>/<version>/`，repo config可以启停 local-marketplace plugin；remote/workspace-managed Plugin 状态并不由同一个 repo-local enable/disable机制统一控制。这个事实与 059 的 `created-by-me-remote` 行为一致。

另有当前 0.153.4 fixture证明：独立 `CODEX_HOME` 可以承载独立 marketplace metadata；但仓库没有真实证据证明“authenticated `codex exec` + isolated CODEX_HOME + candidate only”在不复制/重定向 credential 的前提下可完成 candidate replay，更没有证明 account-backed personal Plugin不会重新出现。

因此 Route A 不能仅凭“理论上 CODEX_HOME 可换”作为本轮主方案。

## 4. 四条现实路线比较

| 路线 | 当前真实证据 | 优点 | 主要风险 | 决策 |
|---|---|---|---|---|
| A. 独立 candidate plugin store / runtime identity | process-local disable失败；0.153.4只证明 isolated CODEX_HOME 可隔离 marketplace metadata，未证明 authenticated candidate replay；052 还出现 fresh CODEX_HOME 仍读取 live plugin 的历史 | 理论上最干净，无 live cache mutation | 需要新的 credential/auth 处理或未证明的 store selector；可能仍同步 account-backed plugin | **REJECT_FOR_CURRENT_RECOVERY**，除非以后官方 runtime提供并真实证明独立 plugin-store/profile |
| B. replay lock 内 temporary local live-plugin suppression + exact restoration | 052 已证明 bounded live-state替换+恢复模式可行；当前 helper已有 lock/finally/timeout/production snapshot | 不复制 credential、不改 remote Plugin；最小扩展现有 helper；直接解决竞争 consumer | crash时可能暂时留下 suppressed cache；remote plugin可能自动 rehydrate | **RECOMMENDED**，但必须有 generic conflict detection、事务式 restore和真实 probe |
| C. candidate-side identity/shadowing | 当前无证据证明不同 marketplace 下同名/近名 candidate会稳定胜过 `created-by-me-remote`；现有 process-local enable已失败 | 不需要 live-state mutation | 可能仍被 live wrapper抢；如果 repack成 wrapper identity可能不再是 exact central candidate payload | **REJECT**，不能靠命名/提示词制造 normal-entry PASS |
| D. Bridge `ai-bridge plugin-replay` 或其他现有 production replay | Bridge 明确定位为“已安装 production plugin fresh replay”，使用当前 Codex identity；Bridge 0.9 又明确不复活 candidate-plugin-replay | 成熟、Host Policy边界清楚 | 测的是已安装 production identity，不是未发布 candidate；无法解决 candidate-vs-live冲突 | **REJECT_FOR_CANDIDATE_REPLAY**；继续用于它原本的 production-plugin boundary |

## 5. 推荐路线：B，但只做通用 shared-helper 扩展

建议修改现有：

`scripts/candidate_plugin_replay.py`

而不是新增第二套 replay framework。

核心机制：

```text
replay lock
-> recover any stale suppression transaction
-> stage/install exact candidate
-> derive candidate top-level Skill identities
-> discover pre-existing cached Plugin packages exposing overlapping Skill identities
-> snapshot exact local plugin state
-> atomically quarantine only conflicting local cache packages
-> launch fresh child
-> prove candidate SKILL consumption
-> prove zero conflicting-package SKILL consumption
-> restore quarantined packages in finally
-> verify before/after persistent state equality
-> remove candidate
-> only then return PASS receipt
```

这里的“冲突”按实际 consumer能力检测，不按 059 plugin name硬编码。

### 5.1 Generic conflict detection

候选侧：

- 读取 staged candidate各 top-level `skills/*/SKILL.md` frontmatter `name`；
- 对多 plugin replay取 union；
- candidate-candidate若出现无法消歧的重复 public Skill name，fail closed，不让模型随机选择。

live侧：

- 扫描当前 `$CODEX_HOME/plugins/cache/<marketplace>/<plugin>/<version>/skills/*/SKILL.md`；
- 排除本轮 `ai-skills-candidate`；
- 读取 top-level Skill `name`；
- 与 candidate skill names 有交集的 package标记为 `CONFLICTING_CONSUMER`。

这能通用发现：

```text
research-writing candidate
vs
research-authoring personal wrapper
```

即使二者 plugin name不同、remote wrapper不出现在 `codex plugin list --json`。

不要按 `research-authoring`、`created-by-me-remote` 或 059 路径特判。

### 5.2 Suppression mechanism

优先使用**同一 filesystem 内 atomic rename/quarantine**，但 quarantine **必须位于 Codex plugin discovery/cache root 之外**。

原 live package 的典型位置是：

```text
$CODEX_HOME/plugins/cache/<marketplace>/<plugin>/<version>/
```

quarantine root 不能放在：

```text
$CODEX_HOME/plugins/cache/**
```

包括隐藏子目录也不允许作为设计保证。

推荐形态只是示例：

```text
$CODEX_HOME/.candidate-plugin-replay-quarantine/<run-id>/
```

实现不得机械假定这个路径一定安全。mutation 前必须实际解析：

- original package resolved path；
- plugin discovery/cache resolved root；
- quarantine parent resolved path。

并验证：

1. quarantine parent 不在 plugin discovery/cache root 内；
2. quarantine parent 与 original package 位于同一 filesystem：
   `original.st_dev == quarantine_parent.st_dev`；
3. quarantine path 不通过 symlink resolve 回 discovery root；
4. quarantine path 不与已有用户数据冲突。

若找不到**同 filesystem且位于 plugin discovery root之外**的安全 quarantine root：

```text
SAFE_QUARANTINE_UNAVAILABLE
```

Route B 必须 fail closed，返回 Planner/Critic。

不得退回：

- `plugins/cache/.hidden/**`；
- copy + delete；
- cross-filesystem move；
- CLI uninstall/reinstall；
- prompt blacklist。

atomic rename 只允许在上述 preflight 全部成立后执行。

不得移动：

- candidate package；
- auth/credential；
- config；
- marketplace remote object；
- 不冲突 Plugin。

### 5.3 Runtime rehydration boundary

account-backed Plugin 可能在 child 运行期间重新 hydrate 回 original path。v0.2 不假设 quarantine 一次移动就能永久阻止 runtime恢复缓存。

因此 child 结束后的消费证据必须同时满足：

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
```

此外，只要运行期间观察到：

- original conflict path重新出现；
- original conflict path被读取；
- quarantine path被读取；

整次 replay 立即视为 isolation FAIL，即使 candidate也被读取。

finally仍优先恢复并核验用户原始状态；不得因为 replay 已失败就跳过 restoration。

## 6. Restoration contract

这是本方案的核心 Gate，不是附属 cleanup。

### 6.1 Before snapshot

在任何 suppression 前保存：

- normalized `codex plugin list --json`；
- plugin discovery/cache resolved root；
- quarantine parent resolved path；
- `original.st_dev` 与 `quarantine_parent.st_dev`；
- 每个 conflict package：
  - exact original path；
  - exact quarantine path；
  - original marketplace/plugin/version identity；
  - overlapping top-level Skill names；
  -完整 tree SHA256 manifest；
  - plugin manifest hash；
- `$CODEX_HOME/config.toml` hash（存在时）；
- candidate marketplace/installed-path identity；
- durable quarantine transaction manifest。

recovery manifest 必须能在进程重启后独立回答“哪个 package 从哪里移动到哪里、原始 identity/hash 是什么”。

### 6.2 Transaction order

```text
resolve + validate discovery root / quarantine root
-> verify same filesystem (st_dev equal)
-> write durable recovery manifest
-> fsync manifest + parent
-> atomic rename original live conflict package -> out-of-discovery quarantine
-> fsync affected parents where supported
-> launch child
-> collect candidate/conflict/quarantine consumption evidence
-> restore quarantine -> exact original path
-> verify hashes/state
-> remove candidate
-> final equality check
```

recovery manifest只是 crash-recovery journal，不新增长期状态机。

### 6.3 Normal exception / timeout

当前 helper已经用 `finally` 清理 candidate。
扩展后 suppression context必须包住 child执行，任何：

- child return non-zero；
- ReplayError；
- timeout；
- ordinary exception；
- KeyboardInterrupt / SIGINT；
- 可捕获 SIGTERM；

都先恢复 conflict packages，再返回失败。

### 6.4 SIGKILL / power loss

SIGKILL / power loss无法承诺即时 restore，因此 helper每次入口在 candidate install/cleanup前必须先检查 stale quarantine/recovery manifest。

仅当：

```text
original path missing
AND
quarantine path exists
AND
quarantine tree/manifest hash == recorded before hash
AND
recorded original/quarantine provenance is valid
```

才允许先原子 restore。

若：

- original与quarantine同时存在；
- quarantine hash不匹配；
- original path被别的内容占用；
- original/quarantine provenance不确定；
- current filesystem/discovery assumptions与 manifest不一致；

则：

```text
RESTORATION_AMBIGUOUS
```

fail closed；
不覆盖；
不删除任一 side；
不启动 child。

### 6.5 Before/after equality

Replay只有在以下全部成立时才可返回成功：

- candidate已移除；
-所有 conflict package回 exact original path；
-每个 conflict tree hash与 before一致；
- plugin manifest hash一致；
- original marketplace/plugin/version identity一致；
- overlapping Skill identity snapshot一致；
- normalized plugin list中所有 pre-existing记录与 before一致；
- config hash未变化；
-没有 stale quarantine entry；
- child JSONL中 candidate actual consumption proven；
- `ORIGINAL_CONFLICT_PATH_READS=0`；
- `QUARANTINE_PATH_READS=0`。

任何 restoration失败优先于 product输出，整次 replay FAIL。

### 6.6 Shared-CODEX_HOME concurrency boundary

`candidate_plugin_replay` 的文件锁只能串行化 helper 自己，不能阻止其他本地 Codex进程同时访问同一个用户级 `CODEX_HOME`。

因此后续 execution package / Kickoff 必须把 temporary quarantine明确定义为：

> 短暂的用户级本地 plugin-cache mutation；在 mutation窗口内，被 quarantine 的冲突 live Plugin 对共享同一 `CODEX_HOME` 的其他本地 Codex进程可能暂时不可用。

mutation前必须做**最小并发 preflight**：

- 检查明显正在使用同一 `CODEX_HOME` 的其他活跃 Codex consumer/process；
- 若能直接判断存在并发消费者，fail closed；
- 不开始 quarantine；
- 不尝试杀掉、暂停或接管其他进程。

这个 preflight 只做 bounded safety check，不新增 watcher、daemon、全局锁服务或长期状态机。

## 7. Why not temporary CLI uninstall/reinstall as default

052 的 bounded live smoke证明“临时安装 candidate normal identity + restore”可以作为**明确授权的 production smoke**。

但 shared candidate helper默认不应把每次 replay变成：
- uninstall live plugin；
- network reinstall；
- remote marketplace refresh。

原因：
- remote/personal wrapper未必能通过 CLI `plugin list/remove/add`完整管理；
- 会扩大 network/account side effects；
- restoration依赖外部源仍可用；
- 比本地 cache atomic quarantine更难保证 exact restore。

所以 B 的默认实现是 local cache suppression；CLI uninstall/reinstall只保留为未来单独授权 production smoke，不进入 candidate replay helper。

## 8. Exact files / scope if Critic PASS

Shared infrastructure source：

1. `scripts/candidate_plugin_replay.py`
   - generic Skill-overlap conflict discovery；
   - local cache quarantine/restore transaction；
   - stale transaction recovery；
   - conflict-consumption zero-read proof；
   - expanded persistent-state equality。

2. `tests/test_candidate_plugin_replay.py`
   - focused unit/fixture coverage。

3. `docs/workflows/CANDIDATE_PLUGIN_REPLAY.md`
   -把“same-name production unchanged”升级为“overlapping live consumer隔离 + exact restore”合同；
   -说明 temporary local cache suppression；
   -明确不改 remote Plugin，不是 production `plugin-replay` 的替代。

Evidence only：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/**`

默认不修改：
- Research Authoring source/config/test/generated files；
- `ac501d98...`；
- live Research Authoring Plugin；
- Bridge Kit；
- Host Policy；
- profiles；
- Marketplace product payload；
- root/plugin versions；
- README；
- main/release。

## 9. Required tests

### 9.1 Deterministic unit/fixture tests

至少新增：

1. **different plugin name / same Skill name conflict**
   - candidate `alpha` 暴露 `shared-skill`
   - live cache `beta@remote` 也暴露 `shared-skill`
   - helper发现 beta为 conflict。

2. **no-conflict**
   -无 Skill overlap；
   -不 quarantine任何 live package；
   -现有行为不退化。

3. **same-name production conflict**
   -保留过去 `writing-style@yuukias-ai-skills` 类场景。

4. **multi-candidate replay**
   - candidate union detection正确；
   -两个 candidate自己暴露冲突 public skill时 fail closed。

5. **success restoration**
   - suppression -> child -> restore；
   - before/after hash/list/config equality。

6. **child non-zero restoration**

7. **timeout restoration**

8. **ordinary exception restoration**

9. **simulated stale quarantine recovery**
   -模拟进程在rename后死亡；
   -下一次入口先恢复再做任何 replay。

10. **ambiguous recovery fail-closed**
    - original/quarantine同时存在且不一致；
    -不覆盖、不删除、不启动child。

11. **conflict rehydration/read detection**
    - child期间 original conflict path重新出现或被读取；
    - replay FAIL，即使 candidate也被读；
    - finally仍恢复并核验原状态。

12. **quarantine discovery-root exclusion / same-filesystem**
    - quarantine resolved path必须位于 plugin discovery/cache root之外；
    - `original.st_dev == quarantine_parent.st_dev`；
    -不同 filesystem时 fail closed；
    -不得 copy + delete；
    -不得退回 `plugins/cache/**` 内隐藏目录。

13. **path/symlink safety**
    - quarantine resolved path不得通过 symlink落回 plugin discovery root；
    -拒绝越界、已有冲突路径与不可验证 provenance。

14. **quarantine path consumption proof**
    - `CANDIDATE_PATH_READS > 0`；
    - `ORIGINAL_CONFLICT_PATH_READS = 0`；
    - `QUARANTINE_PATH_READS = 0`。

15. **concurrency preflight**
    -明显存在共享同一 `CODEX_HOME` 的其他活跃 Codex consumer时 fail closed；
    -无并发时不退化；
    -不 kill/pause其他进程；
    -不新增 watcher/daemon。

16. **remote-object non-mutation**
    - helper不得调用 Plugin Creator；
    -不修改 user config/remote Plugin identity。

### 9.2 Existing-helper should-not-change

保留现有 tests：
- actual-consumption parser；
- candidate cleanup；
- timeout child-tree kill；
- multiple candidate plugins；
- repo-relative input/writable scope；
- candidate marketplace staging。

并用历史真实任务做 risk-matched replay，不机械重跑所有历史大任务：

A. 一个 single-plugin central candidate replay：
   优先 `workflow-core` 或 `ai-skills-core` 的已有 public-safe fixture；
   证明已有成功路径仍能消费 candidate并restore live counterpart。

B. 一个 multi-plugin replay：
   复用 `web-development + writing-style` 的 public-safe same-session fixture；
   证明 multi-plugin能力不退化。

C. 059 blocking replay：
   对 exact `ac501d98...` Research Authoring development task重新运行；
   这次必须：
   - candidate reads > 0；
   - conflicting live wrapper reads = 0；
   - no PDF/render mechanics；
   - before/after plugin state equality PASS。

052/055历史只作为 regression provenance，不重新消耗其 fresh/paid Gate。

## 10. Infrastructure candidate vs Research Authoring candidate

必须分三层身份。

### Product identity

```text
REPAIRED_PRODUCT_COMMIT =
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

shared helper变化不改变它。

当 shared replay修复通过、059 required development replay首次有效 PASS后，Planner/下一 pre-final packet才可以把同一个 commit提升为：

```text
PRODUCT_CANDIDATE_COMMIT =
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

即 C2 的产品身份仍是 ac501d98，而不是 helper commit。

### Replay infrastructure identity

未来 helper实现形成独立：

```text
REPLAY_INFRASTRUCTURE_COMMIT =
<commit containing only candidate_plugin_replay shared source/test/docs>
```

它是验证基础设施版本，不是 Research Authoring product candidate。

### Evidence identity

执行 shared helper tests + historical should-not-change + 059 replay后：

```text
EVIDENCE_PACKET_HEAD =
<latest evidence-only commit after REPLAY_INFRASTRUCTURE_COMMIT>
```

pre-final Critic必须同时绑定：

```text
PRODUCT_CANDIDATE_COMMIT
REPLAY_INFRASTRUCTURE_COMMIT
EVIDENCE_PACKET_HEAD
```

但“同一 final candidate”政策中的 product candidate仍只指 Research Authoring production tree，不把验证 helper commit冒充产品变更。

## 11. 059 如何恢复

Critic PASS -> 后续 bounded infrastructure execution package 才允许实现 shared helper。

实现/验证顺序：

```text
shared helper implementation
-> helper deterministic tests
-> representative historical should-not-change replays
-> exact 059 replay using REPAIRED_PRODUCT_COMMIT=ac501d98...
-> if candidate actual consumption proven
   and live conflict reads=0
   and G4-C1 development regression behavior PASS
   and restore equality PASS
-> record infrastructure/evidence identities
-> return to 059 Planner
-> promote ac501d98 to PRODUCT_CANDIDATE_COMMIT (C2)
-> freeze new C2 G1/G2/G3 final packet
-> pre-final Critic
-> only then final Gates
```

不重新修改 Research Authoring production。

如果 shared helper repair后 059 仍被 live wrapper读取：
- infrastructure approach FAIL；
-不得改 prompt追 PASS；
-不得修改 Research Authoring绕过；
-回 Planner/Critic重新考虑 isolation architecture。

## 12. Safety / restoration authorization boundary

本 Proposal本身不授权 temporary live cache suppression。

如果 Critic PASS，下一步必须准备同版本 bounded infrastructure execution package，并在 Kickoff中明确让用户授权：

-只在 `candidate_plugin_replay` lock内；
-只对检测到 Skill-overlap 的 local cached package做 temporary quarantine；
- quarantine必须位于 plugin discovery root之外且与 original同 filesystem；
- mutation窗口是短暂的用户级本地 cache mutation，共享同一 CODEX_HOME 的其他本地 Codex进程可能暂时无法使用该 live Plugin；
- suppression前执行最小并发 preflight；发现明显其他活跃 consumer时 fail closed；
-不调用 Plugin Creator；
-不改 remote Plugin；
-不永久 uninstall；
-不 kill/pause其他 Codex进程；
-任何成功/失败/timeout都restore；
- crash后下次入口先restore；
- ambiguous recovery fail closed；
- original/quarantine任何一侧被 child消费都使 replay FAIL；
- ordinary non-force push task branch；
-无 main/release。

没有 execution-ready Critic PASS + 用户实际发送 approved Kickoff，不执行 suppression probe或helper修改。

## 13. Maintenance ownership

这个缺口属于 AI_Skills shared replay infrastructure，不属于 Research Authoring product TODO。

059 Issue #99继续记录 Research Authoring因 replay infrastructure blocked，不能把 helper缺陷写成新的 Research Authoring规则。

若后续进入 shared helper implementation tracking，应优先绑定 AI_Skills maintenance / replay tooling owner，而不是新增 Research Authoring capability Gate。

不新增 G5，不修改 G1-G4 taxonomy。

## 14. Planner recommendation

```text
ROOT_CAUSE=SHARED_CANDIDATE_REPLAY_CONSUMER_ISOLATION_GAP
RECOMMENDED_ROUTE=B_TEMPORARY_LOCAL_CACHE_SUPPRESSION_WITH_EXACT_RESTORE
MODIFY_SHARED_CANDIDATE_PLUGIN_REPLAY=YES
MODIFY_RESEARCH_AUTHORING_PRODUCTION=NO
REPAIRED_PRODUCT_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0
REPLAY_INFRASTRUCTURE_COMMIT=NOT_CREATED
EVIDENCE_PACKET_HEAD=0cedb8a3d025c6320de47afac77eac5f7722f675
FINAL_GATES_NOT_STARTED=YES
READY_FOR_INFRASTRUCTURE_IMPLEMENTATION=NO
NEXT_HANDOFF=CRITIC
```

Critic本轮优先复核 CPR1 是否关闭：
- quarantine是否真实位于 plugin discovery root之外；
- same-filesystem `st_dev` gate是否足以保持 atomic rename；
- original conflict path + quarantine path 双 zero-read 是否关闭“换路径仍被读”的漏洞；
- account-backed rehydration是否明确 fail closed；
- shared CODEX_HOME并发风险是否在 execution package前置为 bounded preflight，而没有新增 watcher/daemon；
- 其余已接受的 Route B、Skill-name overlap、A/C/D rejection、tests与三层 identity 不应无新证据重开。
