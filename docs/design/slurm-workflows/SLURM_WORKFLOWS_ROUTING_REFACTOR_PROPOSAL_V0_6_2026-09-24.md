# Slurm Workflows Routing Refactor Proposal v0.6

日期：2026-09-24  
角色：AI Research Stack Planner  
状态：AWAITING_INDEPENDENT_CRITIC_RECHECK

## Active Design Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `main@3a5d7dec1bd0eeda20ed22b42a0d5cdbdb499377`
- proposal_path_and_version: 本文件 / v0.6
- previous_proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_5_2026-09-24.md` @ `376d03f0d1f9cde2e425bdba62e53942ec5063c6`
- previous_critic_review: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_5_2026-09-24.md` @ `3a5d7dec1bd0eeda20ed22b42a0d5cdbdb499377`
- future execution branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- future task-owned worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
- execution branch/worktree status: NOT_CREATED

本轮只处理：

`SWR-VER-B1 — repository release direction`

此前所有架构 finding 保持 CLOSED，除非本 Proposal 直接回归其已批准语义：

```text
SWR-B1 = CLOSED
SWR-B2 = CLOSED
SWR-ER-B1 = CLOSED
SWR-ER-B2-A = CLOSED
SWR-ER-B2 = CLOSED
SWR-ER-B3 = CLOSED
SWR-PORT-B1 = CLOSED
```

---

## 1. SWR-VER-B1 disposition

**ACCEPT**

Critic 的版本判断正确。

当前生产路径要求 unknown Slurm site 必须已经有 committed `site-profiles/*.json`；否则：

- explicit unknown `--site` 会报 unknown site profile；
- no-profile detection 得到 `site_id=None`；
- `environment apply` 无法完成 generic site materialization。

v0.5 已批准的新能力则是：

```text
unknown third-party Slurm site
+ no committed profile
+ live Slurm discovery
-> environment detect / plan / apply / doctor
-> installed normal slurm-workflows
```

这不是单个 Skill 文案或内部质量微调，而是整个 collection 的 environment/install path 新增正常 deployment scenario。

因此若**完整 v0.6 capability**最终实现并正式 release：

```text
Repository bump decision: MINOR
```

当前 release-time baseline 若仍为：

`5.1.0`

则：

`5.1.0 -> 5.2.0`

如果正式 release 前 repository VERSION 已变化，则从当时真实 VERSION 计算 next MINOR，不锁死 5.2.0。

Architecture/design docs 本身仍然不 bump。

---

## 2. Product architecture

v0.5 已获 Critic 接受的架构全部保留：

```text
live Slurm discovery
+ optional public site hard-policy overlay
+ user-local site facts / preferences
        ↓
resolved local SiteContext
        ↓
workload intent
-> batch | persistent allocation | debug interactive
        ↓
sticky resource contract
-> CPU | memory | GPU | walltime / availability duration
        ↓
persistent capacity lifecycle when applicable
-> reuse compatible allocation
   or maintain one bounded successor
        ↓
routing
-> ordered preference
-> advisory probe
-> native single-job widening
-> fail closed / guarded duplicate fallback
```

底层 ownership 保持：

```text
live scheduler facts
!=
site hard policy
!=
user/project preference
```

不新增 central cluster registry、scheduler service、daemon、watcher、history DB、ML predictor、dependency-remap system 或 Bridge Kit change。

---

## 3. Open-source SiteContext

### 3.1 Public site profile

`site-profiles/*.json` 是：

- optional public-safe hard-policy overlay；
- optional safe detection hints；
- generic scheduler state无法表达的 public site rule。

它不是：

- supported-server registry；
- university/cluster inventory；
- current partition fact database。

Repo 没有某学校 profile时 generic Skill仍必须工作。

### 3.2 local_site_id and policy_overlay_id

`local_site_id`：

- actual deployment 的 user-local stable identity；
- workload/resource contract 的 site binding；
- capacity family enrollment 的 site binding；
- local override/site context 的 identity。

优先来自：

1. 已有 user-local id；
2. 可安全读取的 Slurm `ClusterName`；
3. 一次性 locally chosen id。

`policy_overlay_id`：

- optional committed public profile identity；
- 只附加 hard policy。

Hostname不是 generic canonical identity。

### 3.3 Generic live discovery

每个 normal routing/planning invocation 只做 bounded read-only discovery。

优先来源：

#### `sinfo`

读取当前用户正常可见的：

- partitions/default partition；
- availability/state；
- CPU；
- memory；
- GRES；
- features；
- time limits；
- PriorityTier where exposed。

实现阶段优先显式 `-o/-O` field whitelist；不把 raw `--json/--yaml` dump 当作天然 privacy-minimal output。

#### `scontrol show partition`

在权限允许时读取：

- Default/State；
- MaxTime/DefaultTime；
- node/resource bounds；
- memory/TRES；
- Allow/Deny Accounts；
- Allow/Deny QOS；
- PriorityTier/PriorityJobFactor；
- ReqResv；
- related partition constraints。

#### `scontrol show config`

只投影与 routing/site capability有关的 fields，例如：

- ClusterName；
- SelectType / SelectTypeParameters；
- SchedulerType / relevant SchedulerParameters；
- PriorityType / PriorityFlags；
- PrivateData；
- accounting capability indicators。

不把 controller/database hostname/private path 等无关 raw data 写入公共 artifact。

#### `sacctmgr show assoc user=$USER`

只有 SlurmDBD/site permission允许时使用。

可读取：

- Cluster；
- Account；
- Partition；
- QOS / DefaultQOS；
- directly relevant association limits。

不可用/被拒绝：

> 对应事实 = UNKNOWN，不把整个环境判死。

### 3.4 Fact provenance

Runtime SiteContext 至少区分：

```text
LIVE_KNOWN
LOCAL_EXPLICIT
PROFILE_POLICY
UNKNOWN
```

UNKNOWN 不用 generic defaults填充。

---

## 4. SiteContext merge semantics

Effective context 顺序保持：

### Step 1 — live scheduler facts

决定：

> 当前 scheduler实际有什么、当前普通用户看得到什么。

### Step 2 — optional hard-policy overlay

决定：

> 站点明确要求/禁止什么。

Hard policy可更严格，但不能凭空制造 live route。

### Step 3 — local explicit facts

补 live无法发现但用户知道的：

- account；
- QOS；
- local site id；
- private module/path；
- local partition/accelerator preferences；
- recurrence/capacity preferences。

Local fact不能放宽 hard policy。

### Step 4 — workload/project contract and preference

决定：

- workload mode；
- accepted resource contract；
- workload/capacity family；
- legal route内的 preference；
- persistent capacity target；
- enrollment scope。

---

## 5. Hard-coding and privacy contract

Generic production source不得包含 deployment-specific routing constants，例如：

- `htzhulab`；
- Longleaf/CUHK partition names；
- Longleaf hostnames；
- site-specific H100/A100 route mappings；
- compute node names；
- site account/QOS constants。

允许出现：

- user-local config；
- optional site-specific profile；
- tests/fixtures；
- clearly non-default examples；
- live discovery evidence。

Generic code可以理解任意 GPU/GRES/feature vocabulary，但不能硬编码：

```text
GPU type -> university partition name
```

Raw discovery dump不写入 tracked project source。

Discovery RPC bounded到完成当前 SiteContext 所需的最少 read-only calls，不 tight-loop。

---

## 6. Sticky workload resource contract

SWR-ER-B1 保持 CLOSED。

Comparable workload family至少由：

```text
project identity
+ entrypoint/job family
+ workload class
+ material scale signature
+ accelerator requirement
```

组成。

日期、seed、output folder、partition route不创建新 family。

Resource precedence：

1. current user/project explicit request；
2. project-owned accepted contract；
3. user-local accepted workload-family contract；
4. 无 accepted contract时才初始 estimate。

Accepted contract至少冻结：

- cpus-per-task；
- memory request + semantics；
- GPU count/type/equivalence requirement；
- batch walltime 或 persistent availability duration。

没有通过 hysteresis的新证据时完全原样复用。

### Memory

- OOM -> increase candidate；
- trustworthy comparable high-water >=85% -> increase candidate；
- candidate约 `1.25 * high-water`；
- one low run不下降；
- >=3 comparable successful low-memory runs且都 <50% current request -> decrease candidate；
- candidate约 `1.5 * recent high-water`；
- multi-task/multi-node MaxRSS不可盲目当 whole-allocation memory。

后续 execution package必须保证：

> OOM increase rounding后的 candidate严格高于 current accepted request。

### CPU

- stable by default；
- `TotalCPU/(Elapsed*AllocCPUS)`只诊断；
- GPU/IO-bound低CPU efficiency不能单独触发CPU削减；
- repeated comparable evidence + real adjustable parallelism才允许 change candidate。

### Walltime

- batch TIMEOUT支持increase；
- one short run不支持decrease；
- persistent duration由availability contract决定，不从training elapsed history派生。

### GPU

- count/type不因queue convenience静默降低；
- accelerator equivalence只有user/project明确允许时才使用。

若 completed-job `sacct Comment` unavailable，则保守匹配；ambiguous history不得auto-right-size。

---

## 7. Workload modes

SWR-ER-B3 保持 CLOSED。

### Batch

finite unattended computation -> `sbatch` / site-approved equivalent。

### Persistent allocation

persistent reusable workspace/capacity -> allocation mode。

优先：

1. reuse compatible RUNNING allocation；
2. 无compatible allocation再走persistent capacity lifecycle；
3. allocation lease 与 scientific command分离。

`salloc --no-shell + srun --jobid`仍是 target-site validated candidate，不宣称已经在Longleaf生产验证，也不宣称绕过queue。

如果该caller/disconnect lifecycle不成立，可研究site-approved allocation-holder backend，但holder只持有capacity。

### Debug interactive

short debugging shell -> site-approved interactive mode。

不硬编码 interact partition/QOS。

### Bridge

`Bridge Kit change = NO`

Bridge Persistent Run提供persistent intent；资源/allocation semantics归当前Goal/task + Slurm owner。

---

## 8. Persistent capacity lifecycle

SWR-ER-B2 / B2-A 保持 CLOSED。

一个 capacity family 至少绑定：

- local_site_id；
- stable capacity_family id；
- persistent mode；
- accepted resource contract；
- allowed resource envelope；
- recurrence/timezone；
- target availability window；
- successor lead time；
- minimum useful duration；
- latest useful end/cutoff；
- max intended successor = 1；
- auto-maintain preference；
- activation scope；
- enrollment/authorized action scope。

### Reuse first

compatible RUNNING allocation如果覆盖目标窗口 + minimum useful duration：

> 直接reuse/attach，job名字属于哪一周不重要。

### Bounded successor

目标：

```text
at most one compatible active allocation
+
at most one lifecycle-owned intended successor
```

已有 compatible pending successor -> 不重复提交。

Earliest uncovered target没有successor时：

- valid enrollment；
- current invocation activates family；
- same authorized scope；

才允许自动补 exactly one successor。

无daemon/watcher。

---

## 9. One-time capacity-family enrollment

Preference不等于authorization：

```text
auto_maintain_successor=true
+ not enrolled
=
read-only proposal mode
```

Enrollment由一次 user-visible explicit action / approved Goal/kickoff建立，并在：

`~/.config/ai-skills/slurm-workflows.toml`

保存当前 bounded scope。

至少冻结：

- local_site_id；
- capacity family；
- activation scope；
- accepted resource contract；
- allowed resource envelope；
- recurrence/window；
- max successor = 1；
- successor-submit permission；
- optional lifecycle-owned stale-successor cancel/retarget permission。

同一scope内新的一周不重新问。

Material scope change：

- site；
- family identity；
- activation scope；
- resource envelope/accelerator requirement；
- recurrence/window；
- broader cancellation rights；
- max successor >1；

使旧 enrollment invalid，需要新的 explicit authorization。

Unrelated Longleaf workload，例如CPU-only AI_Skills/Bridge Kit maintenance，不应激活已enrolled GPU family。

---

## 10. Calendar availability

普通user语义保持：

`BEST_EFFORT_AVAILABILITY`

`target_ready_by` 是desired availability，不是reservation。

`successor_lead_time` 决定 earliest eligibility。

不能把 future BeginTime描述为提前预约或必然提前积累priority age。

Calendar-bounded candidate仍是：

```text
--begin
+ --deadline
+ --time
+ --time-min
```

subject to target-site capability validation。

Unsupported/ambiguous site semantics -> fail closed；不退回fixed-duration late-drift weekly jobs。

Advanced reservation只作为真实guarantee boundary；本任务不获取管理员权限、不创建reservation。

---

## 11. Routing and JobId safety

SWR-B1 / SWR-B2 保持 CLOSED。

Routing顺序：

```text
resolve mode
-> resolve sticky resource contract
-> reuse/reconcile capacity if applicable
-> filter live/legal routes
-> apply local preference
-> advisory probe
-> native widen / fail closed
```

`--test-only`只作advisory；解析失败fail closed。

In-place Partition widening只有target site/job class真实probe后自动启用。

Cancel+resubmit仅限replaceable pending job，并要求state-safe cancellation + old-job inactive confirmation。

Identity-sensitive：

- arrays；
- dependencies；
- external JobId references；

无法安全in-place widen时fail closed。

Duplicate race：

- only site explicit allow；
- plus user/local opt-in；
- unknown site authority -> disabled。

---

## 12. User-local partition and accelerator preference clarification

这不是新的 blocker，也不是 generic hard-code；它只是把已批准的“local preference”在当前用户 Longleaf 上怎样表达说清楚。

用户当前偏好是：

1. PI 专属 partition 优先级最高；
2. 对学校其余 live-discovered legal GPU routes，accelerator preference大致：
   H100 > A100 > V100 > older GPU class。

因此 future local preference model应允许两个独立层：

```text
explicit partition preference tier
then
accelerator-class preference among remaining discovered legal routes
```

例如用户本机可以把其 PI partition写入local preference，并把accelerator class ranking写入local config。

Generic source不包含该partition名，也不包含“Longleaf H100 partition叫什么”。

Candidate ordering必须先：

1. 用live discovery + resource contract过滤合法/兼容route；
2. honor explicitly-local partition preference；
3. 对剩余legal routes按user-local accelerator preference排序。

如果当前 workload contract **要求** H100，而不是“偏好”H100，则H100是resource requirement，不允许fallback到A100/V100。

如果H100/A100/V100属于用户明确允许的equivalence/preference class，才进行这类排序。

这与v0.5 portability一致，不新增gate；后续可作为G2 local-preference fixture覆盖，使用任意虚构partition名称而不是Longleaf常量。

---

## 13. Open-source environment path

SWR-PORT-B1 保持 CLOSED。

Unknown third-party cluster无需repo profile即可：

```text
live Slurm
-> derive/accept local_site_id
-> bounded discovery
-> optional policy overlay
-> local missing facts/preferences
-> environment plan/apply
-> installed slurm-workflows
-> runtime SiteContext
-> normal routing plan
```

Explicit unknown `--site <id>`未来语义是local site id，不再因为repo没有profile直接拒绝。

No live scheduler + insufficient local facts：

- environment doctor报告runtime unavailable；
- 不伪装routing ready；
- mutation fail closed。

---

## 14. Capability Gates

不新增G9。

### G1 — Site isolation + live discovery

保持v0.5已接受扩展：

- no deployment constant leakage；
- third-party no-profile site fixture正常；
- local_site_id可派生/显式；
- live facts形成SiteContext；
- hidden/unavailable facts = UNKNOWN；
- optional profile只作hard policy；
- profile list不是support matrix。

### G2 — Preference routing

保持v0.2/v0.5。

可在future deterministic fixture中加入一个non-blocking representative case：

- arbitrary local PI-like preferred partition；
- arbitrary discovered GPU routes；
- local accelerator preference排序；
- no deployment-specific source constant。

这只是证明已有local preference语义，没有新增gate。

### G3 — Native widening & JobId safety

保持。

### G4 — Duplicate-race authority

保持。

### G5 — Bounded monitoring/replacement safety

保持。

### G6 — Production identity

保持v0.5 portability normal-entry要求：

```text
no committed profile
+ fake live Slurm CLI
+ local id/override
-> environment materialization
-> installed Skill
-> runtime discovery
-> SiteContext
-> local preference
-> routing plan
```

### G7 — Resource-contract stability/right-sizing

保持。

### G8 — Persistent mode + capacity lifecycle + enrollment authority

保持。

---

## 15. Complexity boundaries

继续禁止：

- central server/university registry；
- cloud inventory；
- SSH management；
- automatic university-doc scraping；
- queue-history DB；
- scheduler predictor；
- daemon/watcher；
- custom scheduler；
- dependency-remap system；
- administrator privilege path；
- automatic account/QOS mutation；
- raw hostname ranking core；
- Bridge Kit modification。

Runtime SiteContext是bounded read-only discovery result，不是inventory service。

---

## 16. Later execution-package notes

v0.6 architecture PASS后，下一步才可以重写 execution package。

必须携带的 implementation notes：

1. generic discovery优先显式 `sinfo -o/-O` field whitelist；
2. 不把raw `sinfo --json/--yaml` dump当作privacy-minimal evidence；
3. raw discovery dump绝不进入tracked project source；
4. controller RPC保持bounded，只读取形成当前SiteContext所需的最少信息；
5. private/raw ClusterName如果不适合写tracked repo reference，使用local alias，不泄漏；
6. OOM increase candidate after rounding严格 > current accepted memory；
7. `sacct Comment` unavailable时不从ambiguous evidence auto-right-size；
8. local partition/accelerator preference来自local config/live discovery，不进入generic source。

---

## 17. Version / Release Direction

### Architecture/design stage

本 Proposal 与后续 architecture review本身：

```text
Repository bump decision: NONE
Standalone slurm-workflows bump: NONE
Central Plugins: NO_BUMP
Bridge Kit: NO CHANGE
```

### If the complete approved capability ships

Repository release class：

`MINOR`

Reason：

> collection-level environment/install capability now supports a normal generic Slurm deployment with no committed site profile, which the current production environment path cannot support.

Current actual VERSION：

`5.1.0`

Therefore if release occurs while that remains the release baseline：

`5.1.0 -> 5.2.0`

If repository VERSION changes before release：

> compute next MINOR from the actual release-time VERSION.

Examples：

- `5.1.4 -> 5.2.0`
- `5.2.3 -> 5.3.0`

Do not mechanically use PATCH for this full release.

### Standalone Skill

If implementation + same-final-candidate gates + final review pass：

`slurm-workflows 0.1 -> 0.2`

exactly once.

### Central Plugins

All：

`NO_BUMP`

### Bridge Kit

`NO CHANGE`

### No new version infrastructure

Use existing:

- VERSION；
- setup/package parity；
- README；
- CHANGELOG；
- existing registry/catalog/generator validation。

---

## 18. What passes if v0.6 is approved

The user gains one coherent Slurm product rather than a Longleaf script:

- arbitrary Slurm cluster live discovery；
- optional site policy overlays；
- stable resource contracts；
- batch/persistent/debug workload modes；
- safe partition routing/widening；
- recurring reusable GPU capacity lifecycle；
- one-time bounded recurring authorization；
- local partition/accelerator preferences；
- no site-specific generic constants。

The repository-level new capability is specifically:

> **generic no-profile Slurm environment materialization and installed normal use.**

That is why the repository release class is MINOR.

---

## 19. Planner Final Position

v0.6 does not change Slurm architecture from v0.5.

It only corrects the release contract from:

`PATCH`

to:

`MINOR`

for the complete shipped capability.

The current user-specific Longleaf preference note is also recorded only as local preference semantics:

```text
PI-owned preferred partition
>
remaining legal routes ordered by user-local accelerator preference
```

No Longleaf partition/GPU route name becomes a generic production constant.

Until independent Critic PASS on v0.6:

- do not modify production source/tests；
- do not create execution branch/worktree；
- do not execute real Slurm mutation；
- do not start Executor；
- do not modify Bridge Kit；
- do not bump version。
