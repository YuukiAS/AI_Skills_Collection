# Slurm Workflows Routing Refactor — Critic Review v0.1

日期：2026-09-24  
角色：AI Research Stack Independent Critic  
审查阶段：PRE_IMPLEMENTATION_DESIGN_REVIEW

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `main@14158d1f11f8b005c40d0e943dddffbe2052a76c`
- proposal_path_and_version: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_1_2026-09-24.md` / v0.1
- proposal_commit: `14158d1f11f8b005c40d0e943dddffbe2052a76c`
- source_baseline_in_proposal: `7c7083015c04a898c2536f7c60ffa79f5bccef1a`
- review_stage: `PRE_IMPLEMENTATION_DESIGN_REVIEW`

核对结果：Proposal baseline 到当前 latest main 之间只有 Proposal 文档本身新增，production source 没有相关 drift。因此本轮不会因为 main 单纯前进而机械要求重审。

## 结论

```text
RESULT = REVISE
```

Proposal 的主方向是正确的，而且复杂度总体合适：Longleaf-specific partition 必须从 generic template 移走；partition priority 应属于 site/user-local preference；`sbatch --test-only` 适合作为 advisory probe；Slurm multi-partition 列表顺序不能表达用户 preference；在 resource contract 相同的情况下，优先考虑一个 multi-partition job，而不是默认提交两个 duplicate jobs；raw hostname ranking 也不应进入通用核心。

我没有发现需要推倒该 layered architecture 的证据，也不建议新增 daemon、watcher、database、registry 或新的 scheduler control plane。

当前有 **2 个真实 blocker**。它们都集中在“队列已经存在以后怎样 widen / duplicate race”这一段，不影响 Proposal 的主体方向。关闭后即可重新审 v0.2，不需要另起大型架构。

---

## 已实际读取的 source

latest main 上实际读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`（v1.4）
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`（v1.4）
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`（v1.1）
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- Proposal v0.1
- `skills/tools/hpc/slurm-workflows/SKILL.md`
- `scripts/skills.py`
- `site-profiles/unc-longleaf.json`
- `site-profiles/cuhk-central-cluster.json`
- `site-profiles/local-overrides.example.toml`
- `docs/LOCAL_CONFIGURATION.md`
- `docs/audits/SERVER_ZIP_INVENTORY.md`
- `tests/test_skill_update.py`
- `schemas/site-profile.schema.json`
- `VERSION` / `setup.py` / `scripts/codex_marketplace_config.json`（只用于核对版本边界）

当前 source 直接确认了 Proposal 的 P1–P5：generic `environment_blank_site_override()` 的确对所有 site 写入 `htzhulab,a100,volta-gpu`；generated site reference 的确没有传播 public `policy`；doctor 的 required fields 的确是全局固定集合；静态 local override example 与 CLI 实际支持的 routing 字段也存在漂移。

---

## 独立 SchedMD 核查

本轮独立检查了 SchedMD 官方资料，结论如下。

### 1. `sbatch --test-only`

SchedMD `sbatch` 文档明确说明：`--test-only` 会验证 batch script，并基于当前队列与 job requirements 返回预计调度时间；**不会实际提交 job**。

因此 Proposal 把它作为 read-only / advisory routing probe 是合理的。但它只能是估计，不能变成启动时间保证。

### 2. Multi-partition 与列表顺序

SchedMD `sbatch --partition=<partition_names>` 明确说明：多个 partition 可以用逗号列出，选择会考虑最早 initiation；**partition name 的书写顺序不表达 preference**。官方同时指出 higher-priority partitions 会被优先考虑。

因此 Proposal 的核心判断正确：用户的 `P1 > P2` preference 不能靠 `--partition=P1,P2` 的列表顺序表达；进入 multi-partition 阶段以后，真正调度仍由 Slurm 的 site scheduler policy 决定。

### 3. `squeue --start` 与 pending reasons

`squeue --start` 可以给 pending job 的 expected start time，但只有配置了 backfill scheduling 时才有该信息。Pending reason 也只是调度器当前遇到的 reason；一个 job 可以实际有多个阻塞原因。

SchedMD 还明确警告：`squeue` 会对 `slurmctld` 发 RPC，不应在 shell/program tight loop 里频繁调用。

因此 Proposal 的 bounded/status-driven monitoring 是正确方向。

### 4. `scontrol` 对 pending job 的修改边界

SchedMD `scontrol` 文档说明，普通用户可以修改自己的 job，但多数 job update 字段只适用于 pending job；`Partition=<name>` 是可更新字段。官方文档没有在该条目中承诺“任何 site 上都可把一个 pending single-partition job 原地更新成 comma-separated multi-partition list”。

所以 Proposal 要求 Longleaf production path 先做最小真实 probe，而不是把该能力当已验证事实，这一点是正确的。

### 5. `--prefer`

官方 `--prefer=<features>` 是 soft feature preference：先尝试 preferred features，不可用时再回到 `--constraint`。这支持 Proposal 的“feature preference 可做 soft preference，raw hostname 不进入 generic ranking core”。

### 6. Multi-partition 的现实 caveat

SchedMD Scheduling Configuration Guide 说明：multi-partition job 会形成多个 job-partition scheduling pair；backfill 可能对多个 pair 都做 reservation，只会启动一个最早的 candidate。官方同时指出，在 partitions 共享节点时，这些 reservation **可能阻碍其他 job，甚至可能让该 job 自己错过更早的低优先级 partition 启动机会**。

这不推翻 Proposal 使用 native multi-partition 的方向，但意味着它应被描述为“一个 Slurm-native、通常比 duplicate race 更简洁的 widening mechanism”，而不是普遍性能保证。

外部资料：

- SchedMD, `sbatch`: https://slurm.schedmd.com/sbatch.html
- SchedMD, `squeue`: https://slurm.schedmd.com/squeue.html
- SchedMD, `scontrol`: https://slurm.schedmd.com/scontrol.html
- SchedMD, Scheduling Configuration Guide: https://slurm.schedmd.com/sched_config.html

---

# BLOCKERS

## SWR-B1 — cancel + resubmit widening 目前会破坏 job identity / dependency 语义，并存在“刚开始运行却被取消”的竞态

### Requirement

Proposal 必须保持当前 `slurm-workflows` 已声明的 job-array / dependency / safe-iteration 能力；routing widening 不能为了换 partition 静默破坏已有 Slurm dependency graph，也不能误杀已经从 PENDING 转成 RUNNING 的 workload。

### Direct evidence

当前 `SKILL.md` 的正常 workflow 明确要求识别 dependency graph，skill description 也把 job arrays 纳入现有能力。

Proposal §7.2 在没有验证 in-place multi-partition update 时给出的 fallback 是：

```text
取消仍 pending 的 P1
-> 重新提交 single multi-partition job
```

Proposal 只明确提到 queue age 会重置，没有冻结 JobId / dependency / array identity 的安全条件。

SchedMD 官方 `sbatch --dependency` 说明 dependency 直接引用 job ID；特别是 `afterok`、`afterany`、`aftercorr` 等语义都依赖原 job identity。官方还明确说明：如果 dependency 因 predecessor 的终止状态而失败，dependent job 之后不会因为 predecessor 被重新执行而自动恢复。

此外，“先看状态是 PENDING，再 scancel”不是原子操作：查询之后 job 可能已经 RUNNING。SchedMD `scontrol hold` 的语义恰好说明了这里的竞态边界：hold 可以阻止 pending job 启动，而对已经 running 的 job 不会 suspend/cancel。

### Why this is a real failure

如果 P1 已经是 downstream job 的 dependency target，cancel 后换成新 JobId 会使现有 graph 指向旧 job；`afterok` 等 dependent job 可能永久无法运行。

如果实现只做 `squeue -> 看见 PENDING -> scancel`，job 可能在两个命令之间启动，于是 routing helper 会取消真实已经开始计算的 workload。

这不是文档洁癖，而是会直接破坏用户已有实验图、浪费计算资源，并违反 Capability Gate Matrix 自己声称的“job arrays/dependencies 能力保留”。

### Minimal closure condition

Planner v0.2 只需冻结一个**最小 safe widening contract**，不需要新 control plane：

1. 已经验证可在目标 site 安全 in-place update 的情况下，可以保留原 JobId 做 widening；
2. 否则 cancel + resubmit 只能用于明确满足“可替换”的 pending job：
   - 没有需要保留的 downstream / external JobId reference；
   - 不是需要保留 identity 的 array/dependency chain/reservation-sensitive workflow；
   - 在取消前采用不会误杀 RUNNING workload 的冻结/复核步骤，例如 hold + recheck，或采用同等安全机制；
3. 如果不能证明可替换，则不自动 cancel+resubmit；保持 primary job，或返回用户当前已授权范围内的安全选择；
4. Gate Matrix 增加一个 should-not-change 负例：带 downstream dependency（以及至少一个 array/dependency identity case）的 pending job 不得被 unsafe widening 换掉 JobId。

不要求 Planner 现在实现 dependency remapping，也不要求新增 state machine。最简单的合法方案就是：**identity-sensitive job 禁止自动 cancel+resubmit widening。**

Owner: Planner.

---

## SWR-B2 — duplicate race 的 site authority 目前把“没有看到禁止”混成了“站点已经允许”

### Requirement

用户/local preference 可以决定“我愿不愿意 race”，但不能把 site hard policy 从 unknown/disabled 状态放宽成 duplicate-job race permission。Shared university/research cluster 上的 duplicate jobs 会真实占 queue entries，并可能同时启动，因此 site permission 必须有可追溯 authority。

### Direct evidence

当前 `slurm-workflows/SKILL.md` 的 Race Policy 是：

> Only use it when the site profile explicitly allows race execution and the user approves the resource cost.

当前 UNC Longleaf 和 CUHK site profiles 都是：

```json
"race_execution": "disabled_by_default"
```

Proposal v0.1 建议把它收敛成 `explicit_user_opt_in`，并把 duplicate-race 条件写成“site 不禁止 + 用户/local opt in”。

但是当前 Proposal 和 current profile source 都没有提供站点管理员/官方 policy 证据，证明 `disabled_by_default` 可以被解释成“站点允许，只差个人 opt-in”。

### Why this is a real failure

如果把 “unknown / disabled by default” 直接迁移为“user opt-in 即可”，local preference 实际上会放宽原本的 site boundary。两个 duplicate jobs 可能同时开始，产生真实 GPU/CPU 占用；这在共享集群上既可能浪费 allocation，也可能违反站点公平使用规则。

而且这个风险没有必要为了核心功能承担：Proposal 已经把普通 race-like widening 优先交给 single multi-partition job；duplicate race 本身就是例外 fallback。

### Minimal closure condition

Planner v0.2 只需把 site authority 做成 fail-closed，不需要新增复杂 schema：

- 清楚区分：
  - site 明确禁止 duplicate race；
  - site 明确允许，但要求 user opt-in；
  - site policy 未知 / disabled by default。
- 只有“site 已明确允许”时，local/user opt-in 才能启用 duplicate race；
- 当前 Longleaf/CUHK profile 若没有新的直接 site-policy 证据，不得仅凭本 Proposal 把 `disabled_by_default` 改写成“已允许”；
- unknown/disabled 仍可使用 single-job multi-partition widening，因为它不是 duplicate-job race；
- G4 增加一个 authority negative case：site policy unknown/disabled 时，即使 local config opt-in，也不能生成 duplicate submissions。

如果 Planner 能取得 Longleaf/CUHK 的管理员/官方 policy，证明 duplicate race 允许，则可把对应 profile 明确标为 allow-with-opt-in；否则保持 disabled 即可。

Owner: Planner.

---

# NON_BLOCKING

## N1 — Multi-partition 是合理默认 widening，但不要把它写成普遍“更快”

Proposal 对列表顺序的理解正确。建议 v0.2 / execution package 补一句：Slurm 的 partition `PriorityTier`、backfill reservation 和 partition node overlap 仍可能影响实际启动；multi-partition 是 native widening mechanism，不是 latency guarantee。

不需要因此新增 scheduler introspection service 或新配置层。

## N2 — `--test-only` parser 必须 fail-closed

`--test-only` 作为 advisory probe 可保留。实现时如果 site/version 输出无法可靠解析，直接进入 Proposal 已定义的 bounded fallback，不要猜时间字符串，也不要把 parse failure 当作“P1 会很晚”。

这不需要新 blocker；Proposal §7.2 已经有正确恢复方向。

## N3 — doctor 改成 site-aware 是正确的，但 requiredness 必须来自 site source，而不是再造一套 global guess

当前全局固定要求 `account/partition/qos/scratch_root/module_init` 的确不合理。

execution package 应明确：真正的“required”由 public site profile 的 hard constraints 声明；没有声明的字段只能是 optional/advisory。特别是有 `partition_priority` 时，不能机械要求同时存在单一 `partition`。

不建议为此再建独立 schema/control plane；现有 site profile + local override 已足够。

## N4 — G6 已经覆盖 normal installed Skill，但 G2/G3 的核心 branch 也应走同一个真实入口

Gate Matrix 没有遗漏 production entry；G6 是必要且方向正确的。

实现 Plan 中最好明确：P1 immediate、P1 delayed/P2 immediate、both delayed -> multi-partition 这三个核心 decision branch，至少在 final candidate 上通过 installed `slurm-workflows` 的正常调用路径消费 generated site reference，而不是只验证 helper 函数生成了正确字符串。

不需要额外增加一堆 gate；可把这三种 case 作为 G2/G3 的 regression bank，并由 G6 证明真实安装 identity。

## N5 — `race_partitions` / `race_cancel_policy` 的收敛方向合理

新 template 不再重复维护 `race_partitions`，默认从 ordered partition preference 派生，是合理简化。

`race_cancel_policy` 不再让每台机器用自由字符串发明 safety semantics，也合理。旧字段兼容读取 + migration warning 足够，不应自动改真实用户 override。

---

## Capability Gate Matrix 审查

整体 Gate 数量和分工是合理的，没有必要继续增加很多 gate。

需要的实质修订只有：

- SWR-B1 对应的 dependency/job-identity should-not-change case，放入 G3/G5 regression boundary；
- SWR-B2 对应的 site-authority negative case，放入 G4；
- G2/G3 的核心 branch 在 final candidate 上至少有 normal installed Skill consumption，而不是只做 helper-level command review。

G1 / G6 很重要，不能删：本轮同时改变 standalone Skill 和 shared environment generator，单纯 source/unit tests 不能证明 CUHK 不再被 Longleaf partition 污染，也不能证明安装后的 Skill 真能读到 site policy。

G4 仍然可以保持 **“只有 duplicate fallback 实际实现时才是 release gate”**。如果 v0.2 决定先只发布 prefer + advisory probe + native multi-partition，duplicate race 保持 disabled，那么不应为了形式强行实现 G4。

---

## Version decision 审查

Proposal 的版本方向合理，但当前设计 review 本身不 bump：

- `slurm-workflows`: 当前 `0.1`；若 production behavior 按批准方案真正修改、normal-entry replay / regression / release closure 都完成，则 `0.1 -> 0.2` 合理。
- Repository: 当前 `5.1.0`；若届时形成正式可安装 release 且没有新的 repository-level capability，按 policy 应走 next PATCH，即当前基线下 `5.1.1`。
- Central Plugins: 本设计不改变中央 Plugin production behavior，全部 `NO_BUMP` 合理。

如果 implementation 开始前 repository VERSION 已变化，则按当时 source 重新计算 next PATCH；不因本 review commit bump。

---

## 还有哪些 Slurm routing 能力值得以后做

以下全部是 **NON_BLOCKING future opportunities**，不应塞进当前 v0.2 造成 scope expansion。

### 1. Resource-feasibility preflight：价值最高

在问“哪个 partition 更快”之前，先回答“这个 resource contract 在该 partition 上到底能不能合法运行”。

可按需读取 partition 的 MaxTime、node/GRES/feature 约束、account/QOS 可用性等，把：

- “只是排队”
- “资源暂时不足”
- “这个请求根本不可能在这里运行”

分开。

这能直接减少无意义 race 和长期 pending，比做更复杂的 queue prediction 更值得。

### 2. Pending-reason-aware routing

把 pending reason 变成“routing 是否可能有帮助”的判断，而不是看到 PENDING 就换路。

例如：

- `Resources` / 某 partition congestion：替代 route 可能有价值；
- dependency 未满足：换 partition 通常没用；
- account/QOS/invalid constraint：应该修 contract，而不是 race；
- node unavailable：根据是否为 hard pin 决定放宽或等待。

这可以继续保持 on-demand/bounded，不需要 watcher。

### 3. Restartability / preemption-aware routing

如果站点有 preemptible / scavenger / short partitions，只有 checkpointable / requeue-safe workload 才应自动把这些 partition 当 fallback；不可恢复的大实验不应为了“更快排到”进入容易被抢占的 route。

这是比 raw hostname ranking 更通用、更贴合 HPC 语义的下一层 preference。

### 4. Deadline-aware routing

用户如果给“今晚前跑完”这类 deadline，可以把 expected start + requested walltime + route constraints 结合起来，给出“哪个 route 有机会在 deadline 前结束”的解释。

只做一次 read-only planning 即可；不需要后台预测服务。

当前不建议优先做：

- raw hostname ranking engine；
- 持续 queue watcher；
- 自研 scheduler score；
- fairshare/priority prediction model；
- daemon/database 记录历史排队时间。

这些要么高度 site-specific，要么容易把 Skill 变成低配 scheduler/control plane，当前没有足够收益证据。

---

## 本轮证明与不证明的内容

本 review 证明：

- Proposal 的 generic/site/local 三层方向正确；
- Planner 对 `--test-only`、multi-partition list ordering、`--prefer`、`squeue --start` 的核心理解基本正确；
- 当前不需要重写 Slurm subsystem，也不需要新 control plane；
- 只要关闭 SWR-B1 / SWR-B2，现有 Proposal 可小幅修订后继续。

本 review **不**：

- 授权修改 production Skill / generator / site profiles；
- 授权提交、取消、hold 或修改任何真实 Slurm job；
- 证明 Longleaf 已支持 pending single-partition -> multi-partition 的 in-place update；
- 证明 Longleaf/CUHK 管理员允许 duplicate-job race；
- 授权 execution branch/worktree、Executor、paid API 或 release。

下一步应由 Planner 对 SWR-B1 / SWR-B2 逐项 `ACCEPT / PARTIAL_ACCEPT / REBUT`，提交完整 Proposal v0.2；不需要先创建 execution branch。
