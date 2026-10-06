# 059 Candidate Plugin Replay 共享隔离恢复 — Critic Review v0.1

日期：2026-10-06  
角色：独立 Critic  
审查阶段：SHARED_REPLAY_INFRASTRUCTURE_RECOVERY_ARCHITECTURE_REVIEW  
Proposal：
`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_PROPOSAL_V0_1_2026-10-06.md`  
Proposal commit：
`4e437523e2de8e6435fc87950dae9bd5cc5e9438`

## 结论

```text
RESULT=REVISE

ROOT_CAUSE=
SHARED_CANDIDATE_REPLAY_CONSUMER_ISOLATION_GAP

MODIFY_RESEARCH_AUTHORING_PRODUCTION=NO

REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

REPLAY_INFRASTRUCTURE_COMMIT=
NOT_CREATED

FINAL_GATES_MAY_START=
NO
```

Planner 对根因、身份分层和“继续复用现有 candidate replay helper，而不是再造第二套框架”的方向基本正确。Route A/C/D 当前都没有比 B 更成熟、已验证的替代证据。

但 Route B 的 quarantine 位置仍有一个会直接破坏隔离证明的 blocker。修正这一点后，不需要重新讨论 Research Authoring，也不需要重做整个 proposal。

## 已独立确认的事实

当前 helper 确实只建立了候选命名空间和 same-name production snapshot，没有建立 Skill-level consumer isolation。

059 已证明：

```text
candidate = research-writing@ai-skills-candidate
candidate reads = 0

conflicting live wrapper =
research-authoring@created-by-me-remote
live reads = 6
```

即使 child process-local 设置：

```text
plugins.research-writing@ai-skills-candidate.enabled=true
plugins.research-authoring@created-by-me-remote.enabled=false
```

也没有隔离 live wrapper。

历史证据也支持这是 shared replay infrastructure gap：

- 052 Clear Writing 曾出现 fresh CODEX_HOME / marketplace override 仍读取 live plugin，最后只能通过一次明确授权的 temporary production identity swap 做真实 smoke；
- 055 的 replay child lifecycle blocker曾通过只修 shared helper、保持 product candidate不变而关闭；
- workflow-core、ai-skills-core、web-development 已证明当前 helper在没有这种竞争 consumer 时仍然有真实价值。

所以不应废弃 helper，也不应把本问题写回 Research Authoring production source。

官方当前插件文档还明确说明：本地安装的插件副本位于 `~/.codex/plugins/cache/$MARKETPLACE/$PLUGIN/$VERSION/`，运行时从安装后的 cache 副本加载；repo-local enable/disable 只覆盖受支持的 local-marketplace plugin，并不等价于 workspace/account-managed plugin 的统一 hard isolation。

## CPR1 — quarantine 不能放在 plugin cache discovery root 内

**requirement**

Temporary suppression 的核心目标不是“把目录换个名字”，而是让冲突插件在 child runtime 中真正不可消费，同时保留可原子恢复的本地副本。

quarantine 本身不能继续处于 Codex 的已安装 plugin cache discovery tree 中。

**direct evidence**

Proposal 当前建议：

```text
$CODEX_HOME/plugins/cache/.candidate-replay-quarantine/<run-id>/
```

并把 live cache package atomic rename 到这个位置。

但当前官方插件行为明确把：

```text
~/.codex/plugins/cache/<marketplace>/<plugin>/<version>/
```

作为已安装插件副本的加载位置。

059 本次失败本身又已经证明：即使 process-local `enabled=false`，account-backed live wrapper 仍会从 cache tree 被 child 读取。

因此，现有证据不足以证明“只要目录名字前面加一个隐藏 quarantine 目录，runtime 就一定不会继续发现/读取它”。

Proposal 当前的 zero-read 规则主要围绕 conflict package cache prefix，但没有冻结“quarantine 新路径本身也必须被视为 forbidden consumer path”。

**causal risk**

如果 quarantined package 仍被 runtime扫描或加载：

1. helper 看起来已经“suppressed original path”；
2. child却可能从 quarantine 新路径读取同一个 live skill；
3. candidate可能仍然没有被正常消费；
4. 或 candidate/live两者同时被消费；
5. isolation Gate得到假阴性或假 PASS。

更糟的是，这会把我们正在修的“cache consumer isolation”问题重新藏进另一个 cache 子目录。

**minimum closure**

Proposal v0.2 只需要改这一处设计：

1. quarantine root 必须在 **plugin discovery/cache root 之外**；
2. 仍要求和原 package 位于同一 filesystem，并在 mutation 前实际验证 `st_dev` 相同，确保 atomic rename成立；
3. 推荐形态例如：
   `$CODEX_HOME/.candidate-plugin-replay-quarantine/<run-id>/...`
   或其他经真实 probe 证明不属于 plugin discovery tree 的同 filesystem 路径；
4. recovery manifest要保存 original path和quarantine path；
5. child evidence必须同时断言：
   - original conflict path reads = 0；
   - quarantine path reads = 0；
   - candidate path reads > 0；
6. 如果无法找到同 filesystem 且不属于 plugin discovery tree 的安全 quarantine root，则 Route B fail closed，不能退回 cache 内隐藏目录。

不要求本轮实现，不要求现在执行 suppression probe。

**owner**

Planner。

## 非阻塞建议：并发影响要在 execution package 里说清楚

Route B 会短暂移动用户级 live plugin cache。现有 replay lock只能串行化 `candidate_plugin_replay.py` 自己，不能让其他同时运行的 Codex进程自动遵守它。

这不需要新增 watcher/daemon/state machine，也不足以否决 Route B；但后续 execution package / Kickoff 必须明确：

- temporary quarantine是用户级本地 cache mutation；
- mutation窗口内冲突 live plugin对共享同一 CODEX_HOME 的其他本地 Codex进程可能暂时不可用；
- 在 suppression 前做最小并发 preflight，并在发现明显的其他活跃 Codex consumer 时 fail closed；
- 用户授权只覆盖这个短暂、可恢复窗口。

不要为了这个建议再造全局进程协调系统。

## 其他 Proposal 判断

### Route A

当前不作为主路线是合理的。

现有 0.153.4 证据没有证明一个 authenticated、candidate-only、不会重新出现 account-backed personal plugin 的独立 plugin store/home。052 还提供了反例方向证据。不能拿理论上的 CODEX_HOME 隔离代替真实 candidate replay。

### Route C

拒绝合理。

把 candidate改名/重包装成 live wrapper identity会弱化 exact candidate identity，并且没有当前 runtime证据证明 shadowing优先级稳定。

### Route D

拒绝合理。

Bridge 的 `ai-bridge plugin-replay` 是已安装 production plugin 的 fresh replay入口，不是未发布 candidate isolation工具。当前不应为了059修改 Bridge。

### Skill-name overlap

Exact top-level Skill `name` overlap 是当前已知失败的最小、确定性 conflict signal，可以作为本修复的第一版通用检测。

不要求加入 description相似度或LLM语义匹配；那会把简单隔离问题变成不稳定启发式。

但文档应把保证范围写清楚：本轮关闭的是“exact public Skill identity overlap导致的 competing consumer”，不是宣称已经检测所有语义相似但 Skill name不同的潜在竞争。

### Restoration contract

Proposal 的总体恢复合同方向正确：

- durable manifest；
- fsync；
- atomic rename；
- finally restore；
- timeout/exception/SIGINT恢复；
- stale transaction先恢复；
- ambiguous recovery fail closed；
- before/after tree/config/plugin state equality。

不需要新增数据库、daemon或长期状态机。

### Required tests

当前 proposed deterministic tests + 一个 single-plugin历史 replay + 一个 multi-plugin历史 replay + 059 exact blocking replay，风险匹配，数量不过重。

不需要把所有历史插件全部重跑。

### Identity separation

三层 identity是正确的：

```text
REPAIRED_PRODUCT_COMMIT =
ac501d988f00cb6672fec105ae5fd51a0679cae0

REPLAY_INFRASTRUCTURE_COMMIT =
<future helper-only commit>

EVIDENCE_PACKET_HEAD =
<future evidence head>
```

shared helper change不应混入 Research Authoring product candidate identity。

在 helper修复和059 development replay第一次真实 PASS前，`ac501d98...` 继续只能称 `REPAIRED_PRODUCT_COMMIT`，不能提前叫 ready C2。

## 当前授权

```text
MODIFY_SHARED_CANDIDATE_PLUGIN_REPLAY=NO
TEMPORARY_LIVE_CACHE_SUPPRESSION_AUTHORIZED=NO
MODIFY_RESEARCH_AUTHORING_PRODUCTION=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
FINAL_GATES_MAY_START=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
```

Planner只需提交 v0.2 proposal关闭 CPR1，然后再次交 Critic。不要开始 implementation。
