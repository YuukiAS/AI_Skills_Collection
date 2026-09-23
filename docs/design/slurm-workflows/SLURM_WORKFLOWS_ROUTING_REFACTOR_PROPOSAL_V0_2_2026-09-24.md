# Slurm Workflows Routing Refactor Proposal v0.2

日期：2026-09-24  
角色：AI Research Stack Planner  
状态：AWAITING_INDEPENDENT_CRITIC_RECHECK

## Active Design Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `main@723c7097004df7def7d739b0e8b1a037ad3fe950`
- proposal_path_and_version: 本文件 / v0.2
- previous_proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_1_2026-09-24.md` @ `14158d1f11f8b005c40d0e943dddffbe2052a76c`
- critic_review: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_1_2026-09-24.md` @ `723c7097004df7def7d739b0e8b1a037ad3fe950`
- execution_branch/worktree: 尚未创建；本轮仍只做设计

本轮重新读取 latest main 的 `AGENTS.md`、Planner/Critic Role Contract、Capability Gate Policy、Versioning Policy、v0.1 Proposal、Critic review 和必要 current source，并重新核查 SchedMD 官方文档。

---

## 1. Critic findings disposition

### SWR-B1 — pending widening 的 JobId / dependency / running-transition safety

**ACCEPT**

Critic 指出的是实际 Slurm identity 风险，不是额外保险。v0.1 的“取消旧 P1，再提交 multi-partition replacement”会改变 JobId；如果已有 downstream dependency、array identity 或外部系统引用旧 JobId，自动 replacement 会破坏 workflow。仅先查询一次 PENDING 再 `scancel` 也存在 PENDING -> RUNNING 竞态。

v0.2 冻结一个最小 safe widening contract：

1. **优先保留 JobId。** 只有目标 site 的真实 probe 已验证当前 job class 可以安全执行 in-place `Partition` update 时，才允许原地 widening。
2. **cancel + resubmit 只允许 replaceable pending job。** 默认仅限本次 routing invocation 新提交、尚未形成 downstream/external JobId contract、不是需要保留 identity 的 array/dependency workflow 的普通 pending job。
3. **取消必须 state-safe。** 首选 controller-side state-conditioned cancellation（例如 `scancel --state=PENDING <JobId>`）并在 replacement 前确认旧 job 已不再 active；若目标 site/版本不能可靠支持该路径，可采用已验证的 hold + recheck 等同等可靠机制。不能确认旧 job 已安全冻结/取消时，不提交 replacement。
4. **identity-sensitive job fail closed。** 无法安全原地 widening 时，保持现有 job；不得自动 cancel + resubmit，不做 dependency remapping。
5. G3/G5 增加 dependency/array identity 的 should-not-change 负例。

本轮不建立 dependency remapping system、新状态机或 job graph database。

### SWR-B2 — duplicate race 的 site authority

**ACCEPT**

v0.1 的“site 不禁止 + local/user opt-in”过宽。Shared university/research cluster 上，local preference 不能把 unknown/disabled 的 site policy 放宽成 duplicate-job permission。

v0.2 明确三态：

- **explicitly forbidden**：禁止 duplicate-job race；
- **explicitly allowed with user opt-in**：只有在 site authority 已明确允许、且 user/local 再 opt in 时才能 duplicate race；
- **unknown / disabled by default / missing**：视为**没有 duplicate-race 授权**，即使 local opt-in 也不能生成 duplicate submissions。

当前 Longleaf 和 CUHK profile 都是 `race_execution: disabled_by_default`。本轮没有新的管理员/官方证据，因此**不把它们改成 allowed**。

single-job multi-partition 是一个 Slurm job 的 native widening，不属于 duplicate-job race，继续允许在正常 site/resource constraints 内使用。

G4 增加：

> site unknown/disabled + local duplicate-race opt-in -> MUST NOT generate duplicate submissions.

---

## 2. 结论

**DECISION = REFACTOR_REQUIRED**

但不是重写 Slurm subsystem。长期边界仍然是：

```text
generic Slurm Workflows Skill
        +
site hard constraints / site authority
        +
user or machine-local preferences
        ↓
managed university / research Slurm cluster
```

当前要修的是这套已存在架构没有真正闭环：

1. generic environment template 泄漏 Longleaf-specific partitions；
2. installed Skill 看不到完整 site policy；
3. partition preference / native widening / duplicate race 混成一件事；
4. pending widening 没有 JobId/array/dependency safety contract；
5. doctor 用 global guessed required fields，而不是 site hard constraints；
6. routing capability 没有真实 normal-entry regression。

---

## 3. 产品定位与边界

`slurm-workflows` 面向：

> 使用 Slurm 的共享、由学校/研究机构管理员管理的科研/HPC 集群，例如 UNC Longleaf。

它不负责：

- 本地 workstation generic shell；
- Kubernetes / cloud batch；
- 自研 scheduler；
- 持续 queue watcher；
- 站点管理员策略的替代；
- 把某个学校 partition 名当成通用知识。

普通用户应能表达：

> 在这个 Slurm 集群跑这个实验。

Skill 再根据安装后的 site reference 和 local preferences 选择合法 route。

---

## 4. 当前 production 问题

### P1 — Longleaf partition 硬编码进 generic template

当前 `scripts/skills.py::environment_blank_site_override()` 对所有 site 生成：

```text
partition_priority = "htzhulab,a100,volta-gpu"
race_after_minutes = "60"
race_partitions = "htzhulab,a100,volta-gpu"
```

CUHK 或未来 site 因此会拿到 Longleaf-specific 值。这必须删除。

### P2 — static override example 与实际 init 已漂移

`site-profiles/local-overrides.example.toml` 没有展示当前 CLI 已生成/识别的 routing/race 字段，用户看到两套配置模型。

### P3 — generated site reference 没传播 site policy

当前 installed Skill 只得到 public constraints + local prompt policy；`site-profile.json -> policy` 未进入 generated reference。

但当前 Skill 又要求 race 必须由 site profile explicitly allow。这个 contract 目前无法从 installed normal entry 实际消费。

### P4 — race 字段重复且把不同概念混在一起

`partition_priority`、`race_partitions`、`race_after_minutes`、`race_cancel_policy` 把：

- preference；
- single-job widening；
- duplicate-job race；
- loser safety

混成了自由字符串配置。

### P5 — doctor requiredness 是 global guess

当前 `LOCAL_OVERRIDE_REQUIRED_FIELDS` 全局固定要求 account / partition / qos / scratch_root / module_init。站点若没有明确要求 QOS 或显式 partition，也会被误报 missing。

### P6 — 历史要求的 Slurm routing tests 未落地

已有历史设计已经要求 site isolation、partition priority、race authority、loser cancellation 与 output isolation；当前 tests 主要只证明 environment init/apply/doctor 的机械行为。

---

## 5. 外部 Slurm 核查与采用决定

本轮只核查会影响 SWR-B1/B2 的官方语义。

### 5.1 Pending job 的 Partition 可更新，但不是所有 job class 都应自动更新

SchedMD `scontrol` 文档明确：`Partition=<name>` 可用于 job update；FAQ 进一步说明 partition/QOS/reservation 等改变只允许 pending job。

**采用：** in-place widening 是保留 JobId 的优先路线。

**边界：** 官方通用语义不等于 Longleaf 已验证 comma-separated multi-partition update 对我们所有 job class 都安全；因此进入 production path 前仍要做最小真实 site probe。

### 5.2 Job dependency 与 array identity 是真实合同

SchedMD `sbatch` dependency 文档明确：dependency 绑定 job ID；如果 dependency 因 predecessor 的终止状态失败，后续 requeue 也不会自动恢复。Job Array 文档也明确 ArrayJobID / ArrayTaskID 是独立 identity 语义。

**采用：** cancel + resubmit 不得用于需要保留 dependency/array identity 的 job。

### 5.3 Hold / state-filtered cancellation 可用来关闭 PENDING -> RUNNING 竞态

SchedMD `scontrol hold` 会阻止 pending job 开始；对已经 running 的 job不会 suspend/cancel。SchedMD `scancel --state=PENDING` 也提供 controller-side state filter。

**采用：** replacement 前必须使用一种经过目标 site/版本确认的 state-safe 机制，且只有确认旧 job 已不再 active 后才能提交 replacement。

**不采用：** `squeue -> 看见 PENDING -> 无条件 scancel`。

### 5.4 Multi-partition 仍是 native widening，不是 latency promise

单个 job 请求多个 partition 是 Slurm-native widening。实际启动仍受 partition PriorityTier、backfill reservation、node overlap 和其他 scheduler policy 影响。

**采用：** 它比 duplicate submissions 更适合作为普通 widening mechanism。

**不声称：** multi-partition 一定更快。

### 5.5 `--test-only` 继续只作 advisory

如果目标 site/version 的输出无法可靠解析：

- 不猜 start-time 字符串；
- 不把 parse failure 当成“P1 很晚”；
- 进入 conservative fallback。

---

## 6. Authority 与配置模型

不新增 database、registry、daemon 或第二套 scheduler。

继续使用：

```text
public site profile
+
~/.config/ai-skills/local-overrides.toml
+
generated references/_generated/site-profile.md
```

### 6.1 Site profile：hard constraints 与 site authority

site profile 负责：

- scheduler/site hard constraints；
- 哪些 local fields 真正 required；
- duplicate race 的 site authority；
- public-safe capabilities/policy。

本轮要求 generated reference 把这些 policy 真实传播给 installed Skill。

#### Duplicate-race authority

`race_execution` 的消费语义固定为：

| Site profile state | Duplicate submissions |
|---|---|
| explicit `forbidden` | 禁止 |
| explicit `allowed_with_user_opt_in` | 还需 user/local opt-in |
| `disabled_by_default` | 禁止自动 duplicate race；视为没有允许证据 |
| missing / unknown | 禁止自动 duplicate race |

只有管理员/官方或其他可追溯 site authority 证据，才允许把一个 site profile 改成 `allowed_with_user_opt_in`。

**当前 Longleaf/CUHK 保持 `disabled_by_default`。**

### 6.2 Local override：site/user-specific preference

generic template 中不再出现任何真实 partition 名。

v0.2 只需要最小 routing fields：

```toml
partition = ""
partition_priority = ""
widen_after_minutes = ""
duplicate_race_opt_in = "false"
node_feature_preference = ""
```

其中：

- `partition`：固定 route 时使用；
- `partition_priority`：ordered preference，例如用户本机 Longleaf 可配置 `htzhulab,a100`；
- `widen_after_minutes`：可选；没有值时不靠 hardcoded 60 分钟自动 widening；
- `duplicate_race_opt_in`：只是 user/local willingness，**不能覆盖 site authority**；
- `node_feature_preference`：仅支持站点已有 feature label 的软偏好，不建立 hostname ranking engine。

不需要额外 `routing_strategy` 字段；本 Skill 只有一条批准后的 routing algorithm，避免把实现策略做成自由字符串。

#### 旧字段

- `race_partitions`：兼容读取并给 migration warning；新模板不生成；
- `race_after_minutes`：兼容映射到 widening threshold，并提示迁移到 `widen_after_minutes`；
- `race_cancel_policy`：兼容识别但不再让新配置自由决定 safety semantics。

不自动改写用户真实 override。

### 6.3 Doctor requiredness 必须 site-aware

删除“所有 site 都 required”的全局猜测。

doctor 只把 public site hard constraints 明确声明的字段标成 required。例如：

- `slurm_requires_site_account=true` -> `account` required；
- 若未来 profile 明确 `slurm_requires_explicit_partition=true` -> `partition` **或** 非空 `partition_priority` 满足；
- 只有 profile 明确要求 QOS / module init / scratch root 时，对应字段才 required。

未被 site constraint 声明的字段只能是 optional/advisory，不能生成人类输入 blocker。

---

## 7. Routing algorithm

### 7.1 Preference probe

给定 ordered candidates：

```text
P1 > P2 > ...
```

例如某个 Longleaf local override 可是：

```text
htzhulab > a100
```

注意：这些 partition 名不进入 generic Skill 或 public profile。

正常流程：

1. 读取 installed generated site reference；
2. 验证 candidate 没违反 site hard constraints；
3. 对 P1 做 bounded `sbatch --test-only` advisory probe；
4. P1 可立即/在 configured grace 内启动 -> 只提交 P1；
5. P1 明显 delayed，P2 可立即/在 grace 内启动 -> 提交 P2；
6. 两边都 delayed、且同一个 batch resource contract 对候选 route 都合法 -> 进入 native widening；
7. probe 无法可靠解析 -> fail closed，不用猜测结果驱动 route。

### 7.2 Native widening：优先保留 JobId

Native widening 是：

> 从一个可接受 route 扩大到多个可接受 partition，但仍保持一个 Slurm job。

#### 路线 A — in-place update

只有同时满足：

1. job 仍是 PENDING；
2. 目标 site 的真实 probe 已验证当前 job class 支持安全 `Partition` update 到候选集合；
3. update 保留原 JobId；
4. 对 array/dependency 等 identity-sensitive class，只有 probe 明确覆盖该 class 才允许自动 update。

满足时，优先 in-place widening。

#### 路线 B — cancel + resubmit

只有 **replaceable pending job** 才允许。

v0.2 对 replaceable 的定义是：

- job 由当前 Slurm Workflows routing invocation 刚刚创建；
- JobId 尚未作为稳定 handoff 返回给外部系统/后续 workflow；
- 没有已创建的 downstream dependency 指向它；
- 自身不属于需要保持 identity 的 array/dependency chain；
- 当前任务没有其他明确要求必须保留 JobId。

**pre-existing job 默认视为 identity-sensitive，除非当前任务已有充分直接证据证明可替换；Skill 不主动构建 dependency graph 来证明它可替换。**

##### State-safe cancellation

禁止：

```text
query PENDING
-> unconditional scancel
-> resubmit
```

允许的最小机制：

```text
state-conditioned cancel old JobId
-> confirm old JobId no longer active
-> only then submit replacement
```

首选使用目标 site/版本已确认语义的：

```text
scancel --state=PENDING <JobId>
```

如果目标环境不能可靠支持该机制，可以使用已验证的：

```text
hold
-> recheck PENDING + held
-> cancel
-> confirm no longer active
```

或同等可靠机制。

若任何一步发现 job 已 RUNNING / CONFIGURING / cancellation outcome 不确定：

- 不提交 replacement；
- 不杀正在运行 workload；
- 保持当前 job，并报告 widening 已停止。

### 7.3 Identity-sensitive job

以下至少视为 identity-sensitive：

- downstream dependency 已引用原 JobId；
- array / array-task identity 需要保留；
- job 本身处于 dependency chain 且当前实现不能证明 replacement identity 等价；
- JobId 已交给外部 automation / workflow 作为稳定 reference。

如果 site-safe in-place update 不成立：

> 不自动 cancel + resubmit。

本轮不实现 dependency remapping。

### 7.4 Duplicate-job race

duplicate race 不是普通 widening，而是例外 fallback。

只有全部满足才允许：

1. single-job multi-partition 无法表达两个 route 的资源合同；
2. site profile 是**explicit allowed_with_user_opt_in**；
3. user/local 已明确 opt in；
4. candidate 有独立 log/output staging；
5. expensive payload 前有可验证 winner claim；
6. loser 能在 winner claim 后停止；
7. final output 只由 winner promote。

若 site 是 `disabled_by_default` / missing / unknown：

> 即使 local `duplicate_race_opt_in=true`，也 MUST NOT 生成两个 submissions。

当前 Longleaf/CUHK 因没有明确允许证据，本 release claim 不包含“自动 duplicate race 可在这两个 site 启用”。

如果 implementation 决定暂不做 duplicate fallback，核心 prefer + advisory probe + native widening 可以独立发布，G4 保持 NOT_APPLICABLE / disabled capability，而不是为了形式强行实现。

---

## 8. 本轮明确不做的未来能力

以下只记录为 future notes，不进入 v0.2 implementation scope：

### resource-feasibility preflight

未来可以在 routing 前判断 MaxTime、GRES/feature、account/QOS 等是否让某 route 根本不可行。

### pending-reason-aware routing

未来可以区分 Resources、Dependency、QOS/account、node unavailable 等原因，再判断换 partition 是否有帮助。

### restartability / preemption-aware routing

未来若站点有 preemptible/scavenger partition，再结合 checkpoint/requeue safety 做 route selection。

### deadline-aware routing

未来若用户给出 deadline，可结合 expected start + walltime 做一次性 planning。

本轮不做：

- queue-history database；
- fairshare prediction；
- scheduler score model；
- raw hostname ranking；
- daemon/watcher；
- persistent control plane。

---

## 9. Production change scope after Critic PASS

### Core Skill

- `skills/tools/hpc/slurm-workflows/SKILL.md`
- 可新增：
  `skills/tools/hpc/slurm-workflows/references/routing-policy.md`

### Environment overlay

- `scripts/skills.py`
- `site-profiles/local-overrides.example.toml`
- `docs/LOCAL_CONFIGURATION.md`
- `site-profiles/unc-longleaf.json`：默认不改变 race authority；仅在必要时同步 revision/wording
- `site-profiles/cuhk-central-cluster.json`：同上
- `schemas/site-profile.schema.json`：只有实现确需收紧现有 free-form policy/constraint validation 才修改；不为本任务造新 schema hierarchy

### Tests

优先扩展现有：

- `tests/test_skill_update.py`

只有 focused cases 明显降低认知负担时才新增单独 test file。

### Explicit non-goals

禁止修改：

- Longleaf_Bridge production；
- Bridge Kit；
- CAT-TRACE / CARE 等项目实验逻辑；
- 中央 Marketplace topology；
- 其他 standalone Skill；
- 真实 `~/.config/ai-skills/local-overrides.toml`；
- 当前真实 Slurm jobs。

---

## 10. Capability Gate Matrix v0.2

| Gate | Capability / claim | Normal entry / evidence | 明确失败 | Regression / negative cases | Final candidate |
|---|---|---|---|---|---|
| G1 Site isolation & authority propagation | generic template 不泄漏其他 site 值；installed Skill 能看到 site hard policy | CUHK/Longleaf/unknown-site fixture：environment init/apply -> generated site reference | CUHK 出现 Longleaf partitions；site policy 未进入 installed reference | PDF/render overlay 不被破坏；current disabled race authority 保持 fail-closed | YES |
| G2 Preference routing | ordered preference 在真正 normal entry 生效 | final candidate 安装后的 `slurm-workflows` 消费 generated reference，覆盖 P1 immediate、P1 delayed/P2 immediate、probe parse failure | helper-level 字符串正确但 installed Skill 选错 route；parse failure 被猜成 delay | 显式固定 single partition 时不得擅自 widen | YES |
| G3 Native widening & JobId safety | delayed candidates 优先 single-job widening，并安全处理 existing JobId | installed Skill normal entry + deterministic Slurm fixture；另有用户授权时做最小 site probe | 无理由 duplicate submission；unsafe cancel+resubmit；把 multi-partition 当 latency guarantee | downstream dependency 指向原 JobId -> 不替换；array/dependency identity case -> 不换 JobId；RUNNING transition -> 不取消 | YES |
| G4 Duplicate-race authority & isolation | duplicate race 只有 site explicit allow + user opt-in 时才可能启用 | deterministic authority matrix；若 duplicate fallback 实现，再验证 isolated staging/winner/loser contract | unknown/disabled site + local opt-in 仍生成两个 submissions；共享 final output | current Longleaf/CUHK disabled profiles MUST NOT duplicate | YES only if duplicate fallback implemented; otherwise capability remains disabled |
| G5 Bounded monitoring / replacement safety | 不 tight-loop，不 blind resubmit，replacement outcome 可确认 | fixture 覆盖 PENDING->RUNNING transition、cancel outcome unknown、test-only unavailable | query PENDING 后无条件杀 running job；旧 job 状态不明时提交 replacement | dependency/array case 保持原 identity；已有 failure triage 不退化 | YES |
| G6 Production identity | 同一 final candidate 的安装产物真正消费 source + site/local policy | environment apply -> installed Skill + generated reference -> normal routing invocation | unit/helper PASS 但 installed Skill 需要人工重新告诉 partition/site policy | CUHK/其他 site 不受 Longleaf preference 污染 | YES |

### Gate 执行原则

- G2/G3 的核心 routing branches 必须经过 installed Skill 正常入口，不只测 helper。
- deterministic fixture / dry-run 先跑。
- 真实 Slurm submission、hold、cancel、update 仍属于外部副作用；只有 execution package 明确写出 bounded probe 且用户当时授权后才能运行。
- 不需要付费 Reviewer。
- 同一正式 release claim 绑定同一 final candidate。

---

## 11. 最小真实 site probe（未来 execution 阶段，当前不执行）

为了决定 Longleaf 是否可启用 in-place widening，若 Critic PASS 后进入 execution，Plan 可请求一次单独授权的最小 probe：

1. 提交一个明确的、无业务计算的 held/pending test job；
2. 记录 JobId；
3. 对该 test job 尝试目标 `Partition` update；
4. 确认：
   - JobId 不变；
   - 仍 PENDING/held；
   - partition candidate state 与预期一致；
5. 取消 test job；
6. 不触碰用户已有实验 job。

如果用户不授权真实 probe：

- 该 site 的 in-place widening 保持 unverified；
- production path 不自动用它；
- identity-sensitive job fail closed；
- replaceable current-invocation job 只能在 state-safe cancellation contract 下使用 cancel+resubmit。

这不会阻塞 generic Skill 的 site isolation / preference / installed-reference 修复。

---

## 12. 失败恢复

### `--test-only` 无法可靠解析

退回 conservative primary submit / bounded status check，不猜。

### in-place Partition update probe 失败或未授权

不使用 in-place widening。identity-sensitive job 保持原 job；仅 replaceable pending job 才有 cancel+resubmit 候选。

### state-safe cancellation 无法确认

不 resubmit。避免出现 old + replacement 同时 active。

### duplicate race 没有 site allow evidence

保持 disabled。single-job native widening 不受影响。

### duplicate winner isolation 不能证明

不发布 duplicate-race capability；不影响 core prefer + native widening release。

---

## 13. Version / release decision

本 Proposal 本身不 bump。

若批准方案最终形成 production behavior change、通过 final-candidate gates 并完成正式 release：

- standalone Skill `slurm-workflows`: `0.1 -> 0.2`
- Repository: 当前基线 `5.1.0` 下为 next PATCH `5.1.1`
- Central Plugins: 全部 `NO_BUMP`

如果 execution 前 repository VERSION 已变化，按当时 current source 重新计算 next PATCH，不锁死 `5.1.1`。

README 只同步 standalone Skill version / 简短定位，不复制 routing implementation。

---

## 14. 外部资料记录

检查日期：2026-09-24。

1. SchedMD — `scontrol`  
   https://slurm.schedmd.com/scontrol.html  
   采用：pending job 的 Partition 可更新；hold 阻止 pending job 启动；JobId/array update 有明确 identity 语义。

2. SchedMD — FAQ / Managing Jobs  
   https://slurm.schedmd.com/faq.html  
   采用：partition/QOS/reservation 等修改属于 pending-job 路径。

3. SchedMD — `sbatch`  
   https://slurm.schedmd.com/sbatch.html  
   采用：dependency 绑定 JobId；dependency failure 不因 predecessor 后续 requeue 自动恢复；`--test-only` 继续只作 advisory。

4. SchedMD — Job Array Support  
   https://slurm.schedmd.com/job_array.html  
   采用：ArrayJobID / ArrayTaskID 具有独立语义；array/dependency identity 不能被普通 replacement 路线默默破坏。

5. SchedMD — `scancel`  
   https://slurm.schedmd.com/scancel.html  
   采用：`--state=PENDING` 作为可选 state-conditioned cancellation primitive；最终仍要求目标 site/版本实际验证并确认旧 job 不再 active 后才 replacement。

---

## 15. Planner final position

v0.2 保留 v0.1 的核心方向，但把两个真实风险收紧为 fail-closed：

1. **Job identity first**：能安全原地 widen 就保留 JobId；不能时只有明确 replaceable job 才能 cancel+resubmit。
2. **Site authority first**：duplicate race 必须 site 明确允许；local opt-in 只是第二把钥匙。

因此仍然不需要新 scheduler/control plane。当前应由 Critic 只优先复核 SWR-B1、SWR-B2 是否关闭，并检查这些修订是否引入新的直接回归风险。
