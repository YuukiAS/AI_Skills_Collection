# Slurm Workflows Routing Refactor Proposal v0.4

日期：2026-09-24  
角色：AI Research Stack Planner  
状态：AWAITING_INDEPENDENT_CRITIC_RECHECK

## Active Design Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `main@9e63c443ab9204cbf7619b8f0fdd8a81effbafc2`
- proposal_path_and_version: 本文件 / v0.4
- previous_proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_3_2026-09-24.md` @ `f9c0e3abbffaa6677c1f0acec510c47106d66aa1`
- previous_critic_review: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_3_2026-09-24.md` @ `9e63c443ab9204cbf7619b8f0fdd8a81effbafc2`
- future execution branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- future task-owned worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
- execution branch/worktree status: NOT_CREATED

本轮只关闭 `SWR-ER-B2-A`。所有已关闭 finding 保持关闭：

```text
SWR-B1 = CLOSED
SWR-B2 = CLOSED
SWR-ER-B1 = CLOSED
SWR-ER-B3 = CLOSED
```

---

## 1. SWR-ER-B2-A disposition

### SWR-ER-B2-A — automatic successor submission authority

**ACCEPT，且进一步收窄 trigger scope。**

Critic 的核心判断正确：

- `auto_maintain_successor=true` 只能表达 preference；
- 它本身不能成为 Slurm submit/cancel authorization；
- 用户需要对一个 bounded capacity family 做一次明确 enrollment；
- 同一冻结 scope 内后续 recurring successor maintenance 不应每周重复询问。

同时，用户补充了一个重要产品边界：

> 在 Longleaf 跑真正需要 GPU 的实验时，可以顺手检查下一个 GPU successor；但如果只是在 Longleaf 上维护 AI_Skills_Collection、Bridge Kit 等不需要 GPU 的工作，不应因为“当前也在 Longleaf”就自动提交 GPU allocation。

因此 v0.4 **不采用“任意 Slurm Workflows activity 都检查所有 enrolled family”**。

改为：

> 只有当前 invocation 明确指向该 capacity family，或当前 workload/resource intent 与 enrollment 中冻结的 activation scope 匹配时，才允许触发该 family 的 automatic reconciliation。

这比 v0.3 更符合 least privilege，也减少无关 queue side effect。

---

## 2. Overall architecture

v0.3 已获 Critic 接受的主架构全部保留：

```text
workload intent
-> batch | persistent allocation | debug interactive

stable resource contract
-> CPU | memory | GPU | walltime / availability duration

site authority + local preference
-> legal route + local preference + availability target

current allocation state
-> reuse compatible allocation
   or maintain one bounded successor

scheduler evidence
-> advisory probe / native widening / fail closed
```

底层仍是：

```text
generic Slurm Skill
+ site hard authority
+ local preference
+ generated site reference
```

不新增：

- queue-history DB；
- scheduler predictor；
- daemon / watcher；
- dependency-remap system；
- custom scheduler；
- raw hostname ranking core；
- authorization ledger；
- 新 workflow state machine。

---

## 3. Comparable workload family and sticky resource contract

本节保持 v0.3 已接受语义。

### 3.1 Comparable workload family

至少由：

```text
project identity
+ entrypoint / job family
+ workload class
+ material scale signature
+ accelerator requirement
```

组成。

日期、seed、output folder、partition route 不创建新 family。

项目/用户显式 `workload_family` 最高优先；无法判断 comparability 时不合并 accounting evidence。

### 3.2 Resource contract precedence

1. current user/project explicit resource request；
2. project-owned accepted contract；
3. user-local accepted workload-family contract；
4. 无 accepted contract 时才初始估计。

已接受 contract 没有新 evidence 时原样复用：

- `cpus-per-task`
- memory + request semantics
- GPU count/type
- batch walltime 或 persistent availability duration

Routing 不得为了排队更容易而静默缩资源。

### 3.3 Current-state contract

继续使用：

`~/.config/ai-skills/slurm-workflows.toml`

它只保存：

- 当前 accepted workload resource contract；
- 当前 persistent capacity family preferences；
- 当前 enrollment scope；
- 可选的 last-adjustment evidence locator。

不保存历史 accounting corpus；历史运行从 `sacct` 按需读取。

### 3.4 Resource hysteresis

已接受的 v0.3 规则保持：

- OOM -> memory increase candidate；
- trustworthy comparable high-water >= 85% -> increase candidate；
- target 约为 1.25x comparable high-water；
- 一次低利用不下降；
- >=3 comparable successful runs 且都 <50% current request -> decrease candidate；
- decrease target 约为 1.5x recent high-water；
- multi-task/multi-node `MaxRSS` 不可盲目解释为 allocation-total memory；
- CPU stable by default，`TotalCPU/(Elapsed*AllocCPUS)` 仅诊断；
- batch TIMEOUT 是 walltime increase evidence；
- persistent duration 由 availability contract 决定；
- GPU count/type 不因 route preference 静默降低。

执行包后续必须吸收 Critic non-blocking clarifications：

1. OOM increase candidate rounding 后必须严格大于 current accepted memory；
2. completed-job `sacct Comment` 是否可用依赖 site accounting（例如 `AccountingStoreFlags=job_comment`）；不可用时 conservative matching，不能用 ambiguous history 自动 right-size。

---

## 4. Workload-mode routing

保持 v0.3。

### Batch

finite unattended computation -> batch mode，正常使用 `sbatch` / site-approved equivalent。

### Persistent allocation

persistent reusable workspace / Persistent Run capacity -> allocation mode。

优先：

1. reuse compatible RUNNING allocation；
2. 无 compatible allocation 时走 enrolled persistent-capacity lifecycle；
3. scientific command 与 allocation lease 分离。

`salloc --no-shell + srun --jobid` 保持候选 backend，进入 Longleaf production 前要做已计划的 bounded site capability validation。

若该 caller/disconnect lifecycle 不成立，可以研究 site-approved allocation-holder backend，但 holder 只持有 capacity，不把所有 scientific payload 偷偷退回 batch-only 语义。

### Debug interactive

short debugging shell -> site-approved interactive shell mode。

不硬编码 interact partition/QOS，不声称 interactive 绕过 scheduler。

### Bridge boundary

Bridge Kit 保持 `NO CHANGE`。

当前 Bridge Persistent Run 已能表达 persistent intent 和 Resource Boundary；resource/allocation semantics 仍属于原 Goal/task 与 Slurm domain owner。

---

## 5. Persistent capacity family

本节保持 v0.3，新增 authorization/activation fields。

一个 capacity family 至少冻结：

- site id
- stable `capacity_family` id
- workload mode = persistent allocation
- accepted resource contract
- allowed resource envelope
- recurrence
- timezone
- target availability window / `target_ready_by`
- successor lead time
- minimum useful duration
- latest useful end / cutoff
- maximum intended successor = 1
- `auto_maintain_successor` preference
- activation scope
- stale-successor cancel/retarget permission
- enrollment state

这些是 user/project-local contract，不把 Monday/H100/5-days 写死进 generic source。

---

## 6. Preference is not authorization

### 6.1 Inert preference

以下配置：

`auto_maintain_successor = true`

**只表示用户希望这个 family 可以被自动维护。**

如果 family 没有有效 enrollment：

- submit/allocation planning 可以提出 successor；
- monitor/diagnose 可以显示：
  `SUCCESSOR_MISSING`
  和 proposed successor；
- 但 monitor/diagnose 必须保持 read-only；
- 不得提交、取消、retarget 任何 Slurm job。

也就是说：

```text
auto_maintain_successor=true
+
not enrolled
=
proposal only, no mutation
```

---

## 7. One-time capacity-family enrollment

### 7.1 Product action

Enrollment 是一次**用户可见的显式授权动作**。

合法来源：

1. 用户在当前 Slurm Workflows 对话/任务中明确说：
   “为这个 capacity family 开启自动 successor maintenance”；
2. 或当前用户明确批准的 project Goal / kickoff 已经列出同样的 bounded capacity-family scope；
3. 或用户本人明确编辑/确认 Slurm Workflows 生成的 enrollment plan。

Skill 不能因为 TOML 中已经存在一个普通 preference，就自行升级为 enrolled。

Enrollment 完成后，当前 scope 被写入现有：

`~/.config/ai-skills/slurm-workflows.toml`

不新增第二个 authorization store。

### 7.2 Enrollment scope

至少冻结这些 non-secret fields：

```text
site
capacity_family
activation_scope
accepted resource contract
allowed resource envelope
recurrence / target availability window
max intended successor = 1
allow successor submission
allow lifecycle-owned stale-successor cancel/retarget
```

其中：

### accepted resource contract

是当前默认请求。

### allowed resource envelope

是 durable authorization 能覆盖的最大/允许资源边界。

G7 right-sizing 可以在 envelope 内按已批准 hysteresis 更新 accepted contract，而不重复向用户索权。

如果 OOM/right-sizing 需要超出 envelope：

> 生成新 proposal，等待一次新的显式 scope authorization。

GPU count/type/accelerator requirement 变化默认视为 material scope change，除非 enrollment 明确冻结了一个用户批准的等价 accelerator class。

### 7.3 Activation scope

这是 v0.4 针对用户最新需求新增的最小边界。

Enrollment 必须说明**什么当前工作可以激活该 capacity family**。

允许两种简单来源：

1. 当前 workload / Goal 显式引用 `capacity_family=<id>`；
2. enrollment 明确授权 `compatible_resource_match`，仅当当前 workload 的 resolved resource contract 与该 capacity family 的 accelerator/resource envelope 兼容时激活。

因此：

### Longleaf GPU experiment

当前 workload contract 需要 compatible GPU，匹配 enrolled GPU capacity family：

> 本次 Slurm invocation 可以顺手 reconcile 下一个 successor。

### Longleaf 上维护 AI_Skills_Collection / Bridge Kit

当前 workload 不要求该 GPU capacity，也没有显式引用该 family：

> 不激活 GPU family，不提交 GPU successor，不因为“同一 site”产生 Slurm GPU side effect。

这不是 project-name blacklist；判断依据是当前 workload intent/resource contract 与 enrollment scope。

### 7.4 Current-state enrollment record

v0.4 不建 authorization ledger。

每个 family 只保存**当前 enrollment**，例如语义上：

```text
enrolled = true
authorization_source = explicit_user | approved_goal
authorized_actions = submit_successor [, retarget_replaceable_successor]
authorized_scope = <normalized bounded scope>
scope_digest = <digest of normalized mutation-relevant scope>
```

`scope_digest` 不是签名系统，只用于防止 scope 字段改了但 `enrolled=true` 仍被错误沿用。

运行时：

- normalized scope 与 stored digest 匹配 -> enrollment 可继续评估；
- scope mismatch / missing enrollment -> fail closed to read-only proposal mode。

不保留历史 approval log，不记录聊天全文，不引入签名/credential。

### 7.5 Revocation

用户可以显式：

- disable auto-maintain；
- revoke enrollment；
- narrow scope。

Revocation/narrowing 可以立即生效，不要求重新批准。

扩大 scope 才要求新的明确 authorization。

---

## 8. Site hard authority reconciliation

当前 Longleaf/CUHK profile 均含：

`do_not_submit_without_user_confirmation = true`

v0.4 **不删除、不改成 false，也不把它静默解释为“配置文件本身就是授权”。**

冻结解释是：

> 一个 bounded capacity-family enrollment 是 user confirmation 的可复用单位；它授权同一冻结 scope 内的 recurring successor actions。没有 enrollment 时仍然禁止自动 mutation。

这与项目现有授权原则一致：

- authorization 绑定明确 scope；
- 同范围内不机械重复索权；
- material scope change 才重新确认。

因此：

```text
site requires user confirmation
+
explicit bounded family enrollment
=
confirmed recurring scope

site requires user confirmation
+
plain preference only
=
NOT authorized
```

### Stronger future site policy

如果以后站点官方/管理员 evidence 明确要求：

> 每一个 individual submission 都必须单独人工确认

那是比当前 boolean 更强的 site hard policy。

此时 site hard authority 优先，capacity enrollment 不能覆盖；automatic successor maintenance 对该 site 禁用。

当前 Longleaf/CUHK source 没有这项更强语义，因此 v0.4 不凭空新增 per-job confirmation restriction，也不修改现有 boolean profile。

---

## 9. Automatic reconciliation authority

Automatic reconciliation 只有全部满足才允许 mutate：

1. site hard policy 没禁止该 action；
2. family enrollment valid；
3. current invocation 激活该 family；
4. scope digest matches；
5. requested action 在 authorized actions 内；
6. resource request 在 authorized envelope 内；
7. recurrence/availability target 未超 enrollment；
8. lifecycle invariant仍是 at most one intended successor。

否则：

> read-only inspect + proposed action only。

### 9.1 Authorized successor submission

对 enrolled family，在同一 scope 内：

- 当前 invocation发现 earliest uncovered target 没有 successor；
- 可以提交 exactly one successor；
- 不需要因为新的一周/occurrence 又向用户询问同一 authorization。

### 9.2 Authorized stale-successor retarget

只有 enrollment 明确包含：

`allow lifecycle-owned stale-successor cancel/retarget`

且目标 job 同时满足：

- Slurm Workflows lifecycle-owned；
- replaceable pending job；
- v0.2 已批准的 JobId/dependency/array safety；
- state-safe cancellation contract；

才允许 cancel/retarget。

没有该 enrollment right：

> 只报告 stale successor，不 mutation。

### 9.3 Pre-existing jobs

pre-v0.4 或非 lifecycle-owned user jobs 默认不属于 enrollment mutation scope。

即使它们名字看起来像同一 weekly job，也不能自动 cancel/retarget，除非它们独立满足之前已经批准的 replaceable-job + authorization contract。

---

## 10. Persistent capacity lifecycle

v0.3 的 accepted algorithm保持，仅把 authority gate放在 mutation之前。

### Identity

以 persistent capacity family 为 identity，不以 `weekly-h100-YYYYMMDD` job name 为 identity。

### Reuse first

compatible RUNNING allocation若覆盖：

`target_ready_by + minimum_useful_duration`

则当前 target occurrence 已满足，直接 reuse/attach。

### One successor

自动维护：

```text
at most one compatible active allocation
+
at most one lifecycle-owned intended successor
```

### Existing successor

已有 compatible pending successor -> 不重复提交。

### Missing successor

只有：

- enrollment valid；
- current invocation activates family；
- earliest uncovered target缺 successor；

才自动提交一个。

### No background magic

无 daemon/watcher。

如果一段时间完全没有任何 matching Slurm Workflows activity，就不会在后台凭空补 successor。

它是 event-triggered BEST_EFFORT maintenance。

---

## 11. User-facing recurring behavior

用户想要的最终交互是：

### 第一次

用户为某个 Longleaf GPU capacity family 明确一次：

> 这个 family 后续自动维护一个 successor；允许在冻结资源 envelope/availability scope 内提交下一份 allocation；是否允许 stale pending retarget 也在此时一次决定。

系统保存 current enrollment。

### 以后跑匹配的 Longleaf GPU 实验

Slurm Workflows 正常入口：

1. 识别当前 workload匹配 enrolled GPU capacity family；
2. 看 compatible running allocation；
3. 看 intended successor；
4. next uncovered target没 successor -> 自动补一个；
5. 同 scope 不再每周询问。

### 以后只在 Longleaf 修 AI_Skills_Collection / Bridge Kit

当前工作没有 compatible GPU resource requirement，也没显式绑定该 capacity family：

> 不 reconcile GPU successor；不会额外提交 interactive/GPU allocation。

### Unenrolled family

即使 `auto_maintain_successor=true`：

> 只报告“下个窗口缺 successor，要不要 enroll/submit”，不 mutation。

---

## 12. Calendar semantics

v0.3 已接受内容全部保留。

- `target_ready_by` 是 desired availability，不是 guarantee；
- `successor_lead_time` 决定 earliest eligibility；
- `--begin` 不是 reservation；
- future BeginTime 不被描述成自动累积 age，除非 site 明确配置相应 priority semantics；
- candidate calendar-bounded request仍是：
  `--begin + --deadline + --time + --time-min`
  subject to target-site capability validation；
- unsupported/ambiguous -> fail closed，不回到 fixed-duration late-drift weekly jobs；
- Longleaf ordinary-user semantics = BEST_EFFORT；
- 不获取管理员权限、不尝试创建 advanced reservation。

---

## 13. v0.2 routing safety remains frozen

以下原样保留：

- preference -> advisory probe -> native single-job widening；
- `--test-only` parse failure fail closed；
- in-place Partition widening只在 target site/job class真实 probe后自动启用；
- cancel+resubmit只限 replaceable pending jobs；
- state-safe cancellation + old-job inactive confirmation；
- identity-sensitive array/dependency/external JobId fail closed；
- duplicate race只有 site explicit allow + user/local opt-in；
- Longleaf/CUHK `disabled_by_default` 不能被 local opt-in 放宽；
- duplicate fallback可以继续 disabled。

SWR-B1 / SWR-B2 不重新打开。

---

## 14. Capability Gates v0.4

G1–G7全部保持 v0.3。

不新增 G9。

### G8 — Persistent mode & capacity lifecycle

G8 继续证明：

1. finite unattended compute -> batch mode；
2. persistent reusable workspace -> persistent allocation mode；
3. short debug request -> debug interactive mode；
4. compatible RUNNING allocation -> reuse；
5. running allocation可满足next target，无视dated job name；
6. existing compatible pending successor -> no duplicate；
7. bounded horizon -> at most one intended lifecycle successor；
8. `BeginTime != reservation`；
9. target availability = BEST_EFFORT；
10. unsupported calendar-bound site semantics -> fail closed；
11. Bridge persistent intent可消费但Bridge不修改；
12. interactive/allocation mode不宣称queue bypass。

v0.4只扩展 G8 authority cases：

### G8-A — enrolled same scope

```text
valid enrollment
+ current invocation activates family
+ same authorized scope
+ successor missing
->
one bounded successor mutation may execute
without repeat weekly prompt
```

### G8-B — unenrolled

```text
auto_maintain_successor=true
+ no valid enrollment
->
monitor/diagnose remains read-only
no submit
no cancel
```

### G8-C — unrelated Longleaf workload

```text
valid enrolled GPU family
+ current workload does not reference/match its activation scope
->
no GPU-family reconciliation mutation
```

代表 case：

> 在 Longleaf 维护 AI_Skills_Collection / Bridge Kit 的 CPU-only task 不应提交 weekly GPU successor。

### G8-D — material scope change

修改以下任何 mutation-relevant field：

- site；
- capacity family identity；
- activation scope；
- allowed resource envelope / accelerator requirement；
- recurrence / availability window；
- max successor >1；
- broader cancellation right；

使旧 enrollment invalid。

需要新的显式用户 authorization 后才重新自动维护。

### G8-E — enrollment stale/tampered

scope digest mismatch -> fail closed/read-only，不沿用 `enrolled=true`。

---

## 15. Site validation boundary

保持 v0.3。

Architecture review 不执行真实 Slurm。

以后 execution package 才能设计最小、可合并的 bounded probes：

- P-A calendar-bounded request semantics；
- P-B persistent allocation backend；
- P-C in-place Partition widening。

这些概念问题不自动意味着三个真实 job。

Enrollment/authorization本身不需要额外 Slurm probe；它是 product authorization contract。

---

## 16. Production source impact after future PASS

预计仍只属于 AI_Skills_Collection：

- `skills/tools/hpc/slurm-workflows/**`
- 小型 current-state contract parser/planner
- `scripts/skills.py` / local config docs as needed
- focused tests
- release metadata after gates

不修改 Bridge Kit。

Enrollment 可以由 Slurm Workflows normal interaction + current TOML 实现；不要求新 authorization service、database、ledger 或 global workflow role。

---

## 17. External check for this amendment

2026-09-24 本轮针对 authority amendment 做了最小外部核查：

- SchedMD `scancel` 仍明确区分 job owner 与 privileged users，并支持 state filter；这与 lifecycle-owned / state-safe cancel 的已有边界一致。
- SchedMD Quick Start / user permission docs没有“每个 recurring job 必须逐次得到某个 Slurm-level human prompt”的概念；提交授权 cadence 属于本产品/站点 policy 层，而不是 Slurm protocol semantics。
- 当前 site profile 的 `do_not_submit_without_user_confirmation=true` 因此继续由 AI_Skills 的 bounded user authorization contract解释；v0.4没有把它改成 false。

本轮没有新的 Slurm scheduler semantic需要改变 v0.3。

---

## 18. Version / scope

Architecture v0.4本身：

- Repository bump: NONE
- standalone Skill bump: NONE
- central Plugins: NO_BUMP

如果后续 implementation + gates + final review完整：

- `slurm-workflows 0.1 -> 0.2`
- repository next PATCH from actual release-time VERSION
- central Plugins all NO_BUMP
- Bridge Kit NO CHANGE

---

## 19. Planner final position

v0.4 关闭的是一个非常窄的问题：

> recurring capacity maintenance到底在什么时候获得可复用的Slurm mutation authorization。

最终规则：

```text
preference
!=
authorization

explicit one-time bounded enrollment
=
durable authorization for the same capacity-family scope

scope unchanged
->
no weekly repeat prompt

scope changed
->
reauthorize

unenrolled
->
read-only proposal

enrolled but unrelated workload
->
do not touch that capacity family
```

这既满足用户“不想每周手动检查 successor”，也避免“只要我在 Longleaf 做任何事情，就自动给我提交 GPU job”。

在独立 Critic 对 v0.4 PASS 前：

- 不修改 production；
- 不创建 reviewed branch/worktree；
- 不启动 Executor；
- 不执行真实 Slurm mutation；
- 不修改 Bridge Kit；
- 不 bump version。
