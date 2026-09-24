# Slurm Workflows Routing Refactor Proposal v0.3

日期：2026-09-24  
角色：AI Research Stack Planner  
状态：AWAITING_INDEPENDENT_CRITIC_REVIEW

## Active Design Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `main@b211db38bdcff8772c1be493d81b95a5b04a9059`
- proposal_path_and_version: 本文件 / v0.3
- approved_previous_architecture: v0.2 @ `b1d516c173ce838fd5eb9f39ae0a117bcb7f517e`
- previous_architecture_critic_pass: `08c598f748903ec48c07b96fd1b35dc96561699d`
- execution_ready_revise: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-24.md` @ `b211db38bdcff8772c1be493d81b95a5b04a9059`
- future execution branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- future task-owned worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
- execution branch/worktree status: NOT_CREATED

本轮只做 architecture amendment。SWR-B1 / SWR-B2 保持 CLOSED，不重新打开。

---

## 1. 新 Critic findings disposition

### SWR-ER-B1 — stable workload resource contract

**PARTIAL_ACCEPT**

接受：

- 必须有 sticky resource contract；
- 同一 comparable workload family 没有新证据时必须复用完全相同的 CPU / memory / GPU / walltime；
- user/project 明确值优先；
- 只读使用 Slurm accounting，不建 history DB；
- 需要 hysteresis；
- GPU count/type 与 routing 完全分离；
- persistent allocation 的 duration 不能由 batch training elapsed history 决定。

不直接照抄 Critic heuristic 的地方：

1. `MaxRSS` 在 Slurm accounting 中是 task/step 层面的最大 RSS；对 multi-task / multi-node job，不能无条件把它当作整个 allocation 的总内存高水位。因此 85% / 1.25x 等规则只能在 accounting metric 与 requested-memory semantics 可比时自动应用。
2. CPU efficiency `TotalCPU/(Elapsed*AllocCPUS)` 只作诊断，v0.3 不允许它单独自动改 `cpus-per-task`。
3. Critic 给出的 85%、1.25x、3 runs、50%、1.5x 作为 **初始默认 hysteresis heuristic** 接受，但不是 site policy，也不是不可覆盖的硬常量。项目明确 contract 优先；不满足可比性条件时保持原值。

### SWR-ER-B2 — weekly GPU availability lifecycle

**ACCEPT**

当前一串 `weekly-h100-YYYYMMDD` + fixed-duration future `BeginTime` job 不是正确产品对象。

v0.3 把它改为：

> persistent capacity family + target availability window + one-active/one-successor reconciliation.

额外吸收用户本轮明确偏好：

> 不要依赖用户周末人工检查。只要 Slurm Workflows 正常执行 submit / attach / resume / monitor 等操作，就顺手检查启用自动维护的 capacity family；若下一目标窗口缺少 successor，自动补一个。无 daemon、无 watcher。

这是 event-triggered reconciliation，不是后台 scheduler service。

### SWR-ER-B3 — persistent vs batch workload mode

**ACCEPT**

新增最小 workload-mode routing：

- finite unattended compute -> batch mode
- persistent reusable workspace / capacity -> persistent allocation mode
- short debugging shell -> debug interactive mode

不声称 interactive 更快，不硬编码 Longleaf interact partition/QOS。

Bridge Kit 不改。当前 Bridge Persistent Run contract 已经能表达 `Persistent execution: REQUIRED` 与 Resource Boundary，并明确资源语义仍归原 Goal/task owner；Slurm Workflows 可以消费这个 intent。只有以后真实 consumer 证明 intent 无法传递，才另开 Bridge 设计。

Bridge source adoption decision for this task:

`REVIEWED_NOT_ADOPTED_FOR_CHANGE` — 读取并采用职责边界，不修改 Bridge Kit。

---

## 2. v0.3 总体架构

v0.2 的 routing 架构保持：

```text
generic Slurm Skill
+ site hard authority
+ local preference
+ generated site reference
```

v0.3 在它前面增加两个小决策层：

```text
workload intent
-> batch | persistent allocation | debug interactive

stable resource contract
-> CPU | memory | GPU | walltime/availability duration

site authority + local preference
-> legal partition/QOS/race + target availability preferences

current scheduler/allocation state
-> reuse compatible allocation
   or maintain one bounded successor

scheduler evidence
-> advisory probe / native widening / fail closed
```

不新增 scheduler service、daemon、watcher、history DB、ML predictor 或 dependency-remap system。

---

## 3. 为什么需要一个小的 persistent contract file

“同一 workload 下周仍用同一资源”和“每周一附近保持 H100 capacity”都不能依赖聊天记忆。

v0.3 选择一个新的、很小的 **current-state configuration file**：

```text
~/.config/ai-skills/slurm-workflows.toml
```

它不是 queue-history database。

它只保存：

1. 当前 accepted workload resource contracts；
2. 当前 persistent capacity family preferences；
3. 最后一次 contract adjustment 的原因/证据 locator（可选）。

历史运行指标不复制进该文件；需要时从 `sacct` 现查。

职责继续分开：

```text
site-profiles/*.json
    = public site hard authority

~/.config/ai-skills/local-overrides.toml
    = site/user account, partition/QOS/path 等 local facts

~/.config/ai-skills/slurm-workflows.toml
    = workload/capacity current contracts and preferences
```

不把 project-specific workload contract 塞进 site profile，也不把 account/path/token 塞进 slurm-workflows contract。

项目或 Goal 已有明确资源 contract 时，它优先于 user-local default。

---

## 4. Comparable workload family

资源统计不能只按 partition 或 job name 聚合。

一个 workload family 至少由以下稳定语义构成：

```text
project identity
+ entrypoint / job family
+ workload class
+ material scale signature
+ accelerator requirement
```

### 4.1 Material scale signature

只有确实会改变 resource footprint 的维度进入 signature，例如：

- model variant / parameter scale；
- dataset size class；
- batch-size regime；
- number of parallel tasks/workers；
- GPU count/type requirement；
- materially different preprocessing mode。

纯日期、随机 seed、output folder、partition route 不应产生新 family。

### 4.2 Explicit family id

项目/用户可以显式给 stable `workload_family`，这是最高优先。

若没有显式 id，Skill 可从 repo/entrypoint/scale signature 派生；如果当前输入无法判断两个 run 是否 comparable，**不合并 accounting evidence**，保持 accepted contract 或询问一次必要分类。

### 4.3 Scheduler-side marker

对 Slurm Workflows 自己提交的新 job，优先使用 Slurm user-settable `--comment` 写入非敏感 stable family marker，例如：

```text
ai-skills-family=<opaque-id>
```

SchedMD 当前 `sbatch` / `salloc` 均允许 arbitrary `--comment`，`sacct` / `squeue` 可读 Comment。

marker 不包含 token、account、private path 或完整 sensitive command。

旧 job 没 marker 时，可用 JobName / WorkDir / SubmitLine 等 accounting evidence 做保守匹配；不确定则不自动 right-size。

---

## 5. Sticky resource contract

### 5.1 Precedence

每次提交前：

1. current user/project explicit resource request；
2. project-owned accepted contract；
3. user-local accepted workload-family contract；
4. 仅在没有 accepted contract 时才做初始 estimate。

Routing 不能为了让某 partition 更容易排到而静默缩 CPU、memory 或 GPU。

### 5.2 Accepted contract fields

至少：

- `cpus_per_task`
- memory request + request semantics（per-node / per-cpu / per-gpu as applicable）
- GPU count
- GPU type / accepted equivalence class
- batch walltime，或 persistent availability duration

一旦 accepted：

> 没有通过 hysteresis 的新证据，下一次完全原样复用。

### 5.3 Accounting source

允许按需读取 `sacct` 当前可用字段：

- ReqMem
- MaxRSS / TRES usage when semantically comparable
- ReqCPUS / AllocCPUS
- TotalCPU
- Elapsed / Timelimit
- ReqTRES / AllocTRES
- State
- OOM / timeout evidence
- Submit / Start / End / Partition / Comment

不建立本地历史数据库。

### 5.4 Memory hysteresis

初始默认：

#### Immediate increase

- `OUT_OF_MEMORY` / equivalent OOM evidence -> next contract eligible for immediate increase。
- 若可信 comparable high-water 存在：
  `next >= ceil_up(1.25 * recent comparable high-water)`
- 若 OOM 但可信 high-water 不存在：
  `next >= ceil_up(1.25 * current request)`

#### Soft increase

一个 successful comparable run 若可信 memory high-water >= 85% current request，可触发 increase candidate：

`next ~= ceil_up(1.25 * high-water)`

如果 rounding 后并未高于 current，保持 current。

#### Decrease

不能因为一次低利用下降。

只有最近至少 3 个 comparable successful runs 都有可信 high-water，并且都 < 50% current request，才允许 decrease candidate：

`next ~= ceil_up(1.5 * max(recent high-water))`

并且不得低于 project/user 明确 floor。

#### Comparability guard

若当前 memory request semantics 与 accounting metric 不可直接比较：

- 不自动增减；
- 保持 contract；
- 只报告 evidence gap。

特别是 multi-task / multi-node job 不得仅拿单 task `MaxRSS` 当作整个 allocation memory high-water。

### 5.5 CPU hysteresis

v0.3 默认 **stable first**：

- accepted `cpus-per-task` 原样复用；
- `TotalCPU/(Elapsed*AllocCPUS)` 只作 diagnostics；
- GPU-bound / IO-bound workload 不因低 CPU efficiency 自动减 CPU；
- 只有 repeated comparable evidence + workload 明确具备可调整 parallelism 时才产生 change candidate；
- user/project 声明的 thread/worker requirement 优先；
- 本轮不建立 CPU autotuner。

### 5.6 Batch walltime hysteresis

- accepted batch walltime 原样复用；
- TIMEOUT -> immediate increase evidence；
- successful elapsed high-water 只在 comparable runs 中使用；
- 至少 3 个 comparable successful runs 都明显低于 current limit 时，才允许 decrease；
- 默认 decrease target 约为 `1.5 * recent elapsed high-water`；
- 不因为单次短 run 缩 walltime。

Persistent capacity 的 duration 不走此规则，见 §7。

### 5.7 GPU contract

- GPU count/type 是 workload contract，不是 routing preference；
- 不为排队更快静默降 GPU count/type；
- 只有 user/project 明确声明等价 accelerator class 时才允许 route across equivalent types；
- H100/A100 等具体偏好留在 local/project contract，不进 generic source。

---

## 6. Workload-mode routing

### 6.1 Batch mode

适用：

> finite unattended computation with a clear completion artifact.

默认 allocation frontend：

`sbatch`

继续使用 v0.2 的 preference/probe/native widening/identity safety。

### 6.2 Persistent allocation mode

适用：

- persistent reusable GPU workspace；
- long-lived allocation that will receive multiple job steps；
- Bridge Kit Persistent Run / long Goal 明确需要 reusable compute capacity。

核心语义：

> resource allocation 与具体 scientific command 分离；先取得/复用 allocation，再在 allocation 内启动 steps。

优先行为：

1. 先找 compatible RUNNING allocation；
2. 有则 reuse / attach；
3. 无则按 persistent capacity lifecycle 请求 allocation；
4. 后续 task 使用相同 allocation identity，不因为新聊天/新 run 自动申请新 GPU。

SchedMD `salloc --no-shell` + later `srun --jobid` 是首选候选 backend，因为官方文档明确它可以保留一个没有 active shell/task 的 allocation，并允许后续对同一 JobId 启动 `srun` step。

但 v0.3 **不宣称 Longleaf 已验证该 caller lifecycle**。

进入 production 自动使用前必须验证：

- Longleaf 当前 Slurm 版本/配置支持所需选项；
- pending acquisition 的 caller lifetime / disconnect behavior；
- later `srun --jobid` 能从正常 consumer lifecycle 可靠 attach；
- allocation cleanup 可控；
- 不需要管理员权限。

如果 `salloc --no-shell` 无法满足 detached successor acquisition，允许研究一个 site-approved **allocation-holder backend**（可由 `sbatch` 持有 allocation），但它只能是 capacity lease backend，不能重新退化成“scientific payload 都作为 batch holder 跑”。

backend 选择属于 site capability，不改变 workload-mode product semantics。

### 6.3 Debug interactive mode

适用：

> short-lived debugging / shell inspection.

可以使用 site-approved interactive `salloc` / shell mechanism。

不硬编码 partition/QOS。

不声称 interactive priority 更高。

### 6.4 Bridge Kit boundary

Bridge Persistent Run 当前 source 已明确：

- Persistent execution 是 Goal-owned intent；
- resource boundary/semantics 由原 Goal/task owner；
- Bridge 可 reuse existing interactive Slurm allocation；
- Bridge 不自动申请/取消资源。

因此本轮：

`Bridge Kit change = NO`

Slurm Workflows 消费 upstream `Persistent execution: REQUIRED` / Resource Boundary 即可。

---

## 7. Persistent capacity family

Workload family 与 capacity family 分开。

Workload family 回答：

> 这类计算通常需要多少资源？

Capacity family 回答：

> 我希望什么类型的 reusable allocation 在什么时间窗口可用？

一个 capacity family 至少有：

- site id
- stable family id
- persistent mode
- accepted resource contract
- recurrence / target window
- timezone
- target_ready_by
- successor_lead_time
- minimum_useful_duration
- latest_useful_end / cutoff
- `auto_maintain_successor`

这些值属于 user-local contract，不写死 Monday/H100/5 days 到 generic source。

用户当前 Longleaf 周一需求将来可以在本地配置中表达；本 Proposal 只冻结机制，不把真实值提交到公共 repo。

---

## 8. Event-triggered successor reconciliation

这是对用户“不要周末手动查”的直接回答。

不建 daemon。

当某个 capacity family 设置：

`auto_maintain_successor = true`

则每次 Slurm Workflows 的正常：

- submit
- allocation request
- attach/resume
- monitor/diagnose

入口，都执行一次 bounded reconciliation。

### 8.1 Live state source

只读查询当前 Slurm state，按 stable family marker 识别：

- compatible RUNNING allocation(s)
- compatible PENDING successor(s)

不靠 calendar job name 判断“属于哪周”。

### 8.2 Invariant

自动维护目标：

```text
at most one primary compatible active allocation
+
at most one lifecycle-owned intended successor
```

如果发现旧系统已经堆了多个 future jobs：

- 本 architecture 只报告 migration/cleanup plan；
- 不因为安装 v0.3 就自动取消用户 pre-existing jobs；
- 真实 cleanup 需要后续明确 execution authorization。

### 8.3 Reuse first

先计算 next target occurrence。

若一个 compatible RUNNING allocation 在 `target_ready_by` 仍有效，并且能覆盖至少 `minimum_useful_duration`：

> 它就是本 target window 的 capacity，直接 reuse/attach。

job name 即使写着“上周”也不重要。

### 8.4 Earliest uncovered target

如果 current active 已覆盖 next target，则 successor 的目标应滚到**下一次尚未覆盖的 recurrence**。

这解决 late-start drift：

- late-start allocation 不再因为名字属于上周就被丢弃；
- pending successor 不再机械绑定“下一周 job name”；
- lifecycle 按实际 coverage 决定 target occurrence。

### 8.5 Existing successor

已有 compatible PENDING successor：

- 不再提交第二个；
- 若它已因 current active coverage 变成 stale/redundant，并且它是 lifecycle-owned replaceable pending job，允许复用 v0.2 的 state-safe cancellation contract 后 retarget；
- pre-existing / identity-sensitive pending job 不自动 cancel。

### 8.6 Missing successor

如果 earliest uncovered target 没有 compatible successor：

> 当前 Slurm invocation 自动提交 **一个** successor request。

这就是用户希望的行为：

> 平时只要继续跑 Slurm 实验，Skill 会顺手确认下一个目标窗口已有 successor；没有就补上，不需要周末人工巡检。

如果一段时间完全没有任何 Slurm Workflows activity，则不会有后台 watcher 来补 job；因此这是 BEST_EFFORT maintenance，不是假装保证。

---

## 9. Calendar availability semantics

### 9.1 Product meaning

`target_ready_by`：

> 希望到这个时间附近 capacity 已经可用。

不是 reservation。

`successor_lead_time`：

> successor 从 target_ready_by 之前多久开始变成 eligible。

因此：

```text
earliest_eligibility = target_ready_by - successor_lead_time
```

successor 可以更早被创建，但在 `--begin` 之前通常仍不 eligible。

SchedMD 当前文档明确：priority age 通常在 eligible waiting time 增长；只有 site 开启 `PriorityFlags=ACCRUE_ALWAYS` 等配置时，future BeginTime/hold/ineligible 状态也累积 age。

因此：

> 提前几周创建一个 BeginTime job 不等于提前几周积累排队年龄。

v0.3 不再把 months-ahead submission 当优化。

### 9.2 Prevent late-start drift

Persistent capacity 不能再使用：

> fixed duration from actual start with no calendar end bound

作为唯一策略。

v0.3 冻结一个 **calendar-bounded allocation requirement**：

- earliest eligibility
- target ready time
- desired maximum availability duration
- minimum useful duration
- latest useful end / cutoff

首选候选 Slurm backend：

```text
--begin=<earliest eligibility>
--deadline=<latest useful end>
--time=<desired maximum duration>
--time-min=<minimum useful duration>
```

SchedMD 当前语义：

- `--begin` 只推迟 eligibility；
- `--deadline` 在 job 已无法在 deadline 前结束时移除 job；
- `--time-min` 允许 backfill 在必要时把 time limit 降到不低于 minimum，以便更早启动；
- allocation 获得后 time limit 不再由 `time-min` 动态变化。

这组语义很适合解决“晚开始 -> 固定 5d 再往后漂”的问题，但**进入 Longleaf production 前必须做 target-site capability validation**。

### 9.3 Fail-closed fallback

如果 Longleaf/site 无法验证上述 calendar-bounded semantics：

- 不静默恢复为无限 calendar drift 的旧 fixed-duration weekly jobs；
- automatic calendar successor remains unverified/fail-closed；
- Skill 可以继续 reuse existing active allocation，并给出 best-effort/manual alternative；
- 不在本轮引入 post-grant TimeLimit mutator、cron、daemon 作为偷偷 fallback。

以后若确需“grant 后缩短 allocation”，另用直接 site evidence设计；不在本 v0.3 预先冻结。

### 9.4 Best effort vs guarantee

普通 user path：

`BEST_EFFORT_AVAILABILITY`

即使 target_ready_by 是 Monday afternoon，scheduler 仍可能晚启动。

真正 guarantee future GPU availability 需要已有 site/lab advanced reservation 或等价管理员机制。SchedMD advanced reservation 的创建属于 root/SlurmUser authority。

用户本轮已明确：

> 学校服务器永远不要把“去拿管理员权限”当解决方案。

因此 Longleaf v0.3：

- 不尝试创建 reservation；
- 不建议提权；
- 若 site/lab 已经给了可用 reservation，可以消费；
- 否则所有 Monday-ready 语义明确标为 BEST_EFFORT。

---

## 10. Resource contract vs routing

v0.2 的 routing 全部保留，但顺序变成：

```text
classify mode
-> resolve sticky resource contract
-> reconcile reusable capacity when applicable
-> apply site authority/local route preference
-> advisory probe
-> native widen / fail closed
```

Routing 绝不能反向偷偷改 resource contract。

例如：

- P1 排不到 1xH100 + 32G；
- P2 容易排到 1xH100 + 16G；

Skill 不能为了选择 P2 把 memory 从 32G 改到 16G，除非 resource-contract evidence 本身独立支持该改变。

SWR-B1 / SWR-B2 的 JobId safety 与 duplicate-race authority原样保持。

---

## 11. Alternatives considered

### A. 每次从 sacct 重新算 CPU/memory

拒绝。没有 sticky state，会继续产生 week-to-week flapping。

### B. 建 queue/resource history DB

拒绝。当前需要的是当前 accepted contract + live Slurm accounting，不需要数据库。

### C. 把 workload contract 塞进 site local-overrides

拒绝。site/account/partition 与 project/workload semantics 是不同 owner。

### D. 每周提前创建很多 BeginTime jobs

拒绝。不能保证 target readiness，通常也不会在 future BeginTime 前获得 age priority，而且会重新制造 stale future queue。

### E. cron/watcher 每周末检查

拒绝。本轮没有必要。用户正常 Slurm activity 本身可作为 reconciliation trigger。

### F. always salloc because “interactive faster”

拒绝。interactive allocation 仍由 scheduler 分配，只有 site-specific partition/QOS 才可能不同。

### G. selected

- one small current-state Slurm contract file；
- live sacct/squeue/scontrol evidence；
- sticky resource contract；
- explicit workload mode；
- event-triggered one-active/one-successor capacity lifecycle；
- calendar-bounded best-effort successor；
- existing v0.2 routing/safety。

---

## 12. Capability Gate Matrix v0.3

G1–G6 从 v0.2 原样保留；routing 输入改为已经解析好的 sticky resource contract。

### G1 — Site isolation & authority propagation

保持 v0.2。

### G2 — Preference routing

保持 v0.2；额外明确 route 不得改变 resource contract 来制造“更容易排”。

### G3 — Native widening & JobId safety

保持 v0.2；SWR-B1 仍 CLOSED。

### G4 — Duplicate-race authority & isolation

保持 v0.2；SWR-B2 仍 CLOSED。

### G5 — Bounded monitoring / replacement safety

保持 v0.2。

### G6 — Production identity

保持 v0.2，并要求 installed Skill 可读取当前 slurm-workflows contract source。

### G7 — Resource-contract stability & right-sizing

Distinct capability：

> 同一 comparable workload 的资源 contract 在没有新 evidence 时稳定；新 evidence 只通过 hysteresis 改变。

Final-candidate cases 至少：

1. same family repeated, no new evidence -> CPU/mem/GPU/walltime byte-for-byte equivalent request；
2. explicit user/project override wins；
3. OOM -> memory increase candidate；
4. trustworthy high-memory case -> bounded increase；
5. one low-memory run -> NO decrease；
6. >=3 comparable low-memory successes -> decrease candidate；
7. multi-task MaxRSS not comparable -> NO automatic memory resize；
8. GPU/IO-bound low CPU efficiency -> NO automatic CPU cut；
9. TIMEOUT -> batch walltime increase evidence；
10. route preference cannot silently downgrade GPU/memory/CPU contract。

### G8 — Persistent mode & capacity lifecycle

Distinct capability：

> persistent intent becomes reusable capacity lifecycle rather than blind batch-only submission.

Final-candidate cases 至少：

1. finite unattended compute -> batch mode；
2. Persistent Run / reusable workspace -> persistent allocation mode；
3. short debug request -> debug interactive mode；
4. compatible RUNNING allocation -> reuse/attach；
5. current active covers next target -> that target is considered satisfied regardless of calendar job name；
6. existing compatible PENDING successor -> no duplicate；
7. missing successor + auto-maintain enabled -> one successor plan/submission only；
8. bounded horizon -> never more than one intended lifecycle successor；
9. future BeginTime described only as earliest eligibility；
10. calendar target labeled BEST_EFFORT, not guarantee；
11. unsupported/ambiguous deadline/time-min site capability -> fail closed, no old drifting fallback；
12. Bridge Persistent Run intent can be consumed without modifying Bridge Kit；
13. site/local partition/QOS still controls legal route；
14. salloc/allocation backend does not claim queue bypass.

G7/G8 are new because failure semantics are genuinely different from routing safety; forcing them into G2/G3 would hide the new user-visible capabilities.

---

## 13. Site validation needed before production use

Architecture v0.3 PASS would authorize a later execution package to propose small bounded probes, not run them now.

At minimum Longleaf production enablement should validate:

### P-A — calendar-bound request semantics

Read-only first:

- Slurm version/help supports `--begin`, `--deadline`, `--time`, `--time-min`；
- `sbatch --test-only` accepts a representative bounded request without actual submission.

Only if necessary, a later user-authorized held/no-op job can verify controller-visible Begin/Deadline/TimeMin/TimeLimit fields.

### P-B — persistent allocation backend

Need one bounded harmless capability probe before claiming automatic `salloc --no-shell + srun --jobid` reuse on Longleaf:

- minimal resource;
- no research payload;
- verify allocation JobId lifecycle;
- verify later step attach;
- cleanup;
- no attempt to obtain/administer special QOS or partition.

If P-B fails, persistent mode backend remains disabled/unverified; do not silently return to batch-compute semantics.

### P-C — v0.2 in-place Partition widening

Previous approved bounded probe semantics remain; it is separate from P-A/P-B and only needed if automatic in-place widening will be enabled.

The later execution package must minimize/combine probes where one harmless allocation can safely answer multiple questions; it must not mechanically run three separate jobs just because three probe labels exist.

---

## 14. Production source scope after future Critic PASS

Likely implementation owners:

### Slurm Skill

- `skills/tools/hpc/slurm-workflows/SKILL.md`
- references for routing / resource contract / persistent capacity
- a small deterministic skill-local helper is allowed for:
  - parsing current contract file;
  - workload/capacity family markers;
  - accounting normalization;
  - hysteresis decision;
  - reconciliation planning.

It must not become daemon/service.

### Environment/local config

- `scripts/skills.py`
- `site-profiles/local-overrides.example.toml`
- `docs/LOCAL_CONFIGURATION.md`
- creation/documentation of `~/.config/ai-skills/slurm-workflows.toml`
- schema only if existing validation requires a small extension.

### Tests

Existing tests plus focused deterministic routing/resource/lifecycle tests.

### No Bridge source changes

`YuukiAS/GPT_Codex_AI_Bridge_Kit` remains read-only for this task.

---

## 15. Version / release direction

Architecture docs themselves do not bump versions.

If v0.3 is later implemented, same-final-candidate gates pass, and release closure completes:

- standalone `slurm-workflows`: `0.1 -> 0.2`
- repository: next PATCH from actual release-time `VERSION`
- central Plugins: all `NO_BUMP`

The added resource/persistent capability is still an improvement of the existing standalone Slurm/environment product, not a new central Plugin or incompatible repository contract.

---

## 16. External sources checked

Checked 2026-09-24.

1. SchedMD `sacct`  
   https://slurm.schedmd.com/sacct.html  
   Adopted:
   - ReqMem / MaxRSS / ReqCPUS / AllocCPUS / TotalCPU / Elapsed / Timelimit / ReqTRES / AllocTRES / State / Comment are available accounting inputs.
   - MaxRSS is task/step-oriented; do not blindly treat it as allocation-total memory.

2. SchedMD `sbatch`  
   https://slurm.schedmd.com/sbatch.html  
   Adopted:
   - `--comment` arbitrary user marker;
   - `--begin` is eligibility delay;
   - `--deadline` removes jobs that can no longer finish before deadline;
   - `--time-min` allows bounded time-limit reduction for earlier backfill start.

3. SchedMD Multifactor Priority / `slurm.conf`  
   https://slurm.schedmd.com/priority_multifactor.html  
   https://slurm.schedmd.com/slurm.conf.html  
   Adopted:
   - age normally grows while eligible;
   - `PriorityFlags=ACCRUE_ALWAYS` is the exception that can accrue despite future begin/holds/dependencies;
   - do not claim early future submission automatically gains age.

4. SchedMD `salloc`  
   https://slurm.schedmd.com/salloc.html  
   Adopted:
   - `--no-shell` can leave an active allocation with a JobId and no task;
   - later `srun --jobid` may use that allocation;
   - still subject to normal job limits/scheduler constraints.

5. SchedMD Quick Start / FAQ  
   https://slurm.schedmd.com/quickstart.html  
   https://slurm.schedmd.com/faq.html  
   Adopted:
   - allocation + job steps is a distinct normal Slurm mode;
   - interactive allocation does not imply bypassing scheduler.

6. SchedMD Advanced Reservations  
   https://slurm.schedmd.com/reservations.html  
   Adopted only as truth boundary:
   - advanced reservation is the real future-resource guarantee mechanism;
   - reservation create/update/delete is root/SlurmUser authority.
   - This task will not seek admin privilege or attempt reservation creation.

7. Bridge Kit current main read-only:
   - `docs/design/0.8.0_persistent_run.md`
   - `templates/persistent_run/CONTRACT_TEMPLATE.md`
   - `templates/persistent_run/AGENTS_SNIPPET.md`

   Adopted:
   - Persistent Run owns execution lifetime, not scientific/resource semantics;
   - existing interactive Slurm allocation may be reused;
   - resource scope remains Goal/task owner;
   - current Bridge contract is sufficient as an intent source; no Bridge modification proposed.

---

## 17. Planner final position

v0.3 is still a small Slurm-domain architecture.

The important change is conceptual:

> Don't ask “what sbatch line should I create this week?” first.

Ask in order:

1. **What kind of workload is this?**
2. **What stable resource contract does this workload/capacity family already have?**
3. **Is there already compatible capacity I should reuse?**
4. **Does the next target window already have one successor?**
5. **Only then: which legal Slurm route should this exact contract use?**

For the user's recurring Longleaf GPU case, the intended future normal behavior is:

> whenever the user is already using Slurm Workflows, reconcile the weekly persistent capacity family; reuse a still-useful running allocation, keep at most one successor for the earliest uncovered target window, and automatically create that successor if missing. Monday readiness is best-effort, bounded by a real calendar window, and never represented as an administrator-style reservation.

Until independent Critic PASS on this v0.3:

- do not modify production;
- do not create execution branch/worktree;
- do not start Executor;
- do not mutate real Slurm state;
- do not bump versions.
