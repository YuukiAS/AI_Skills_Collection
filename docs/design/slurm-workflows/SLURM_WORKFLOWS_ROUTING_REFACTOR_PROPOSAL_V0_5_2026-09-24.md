# Slurm Workflows Routing Refactor Proposal v0.5

日期：2026-09-24  
角色：AI Research Stack Planner  
状态：AWAITING_INDEPENDENT_CRITIC_RECHECK

## Active Design Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `main@14b885b8c272de4c0f2c1b66d8c792d6bed060cc`
- proposal_path_and_version: 本文件 / v0.5
- previous_proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_4_2026-09-24.md` @ `bdc33f27df89c6facf9214ce14e43a7afb8097cf`
- previous_critic_review: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_4_2026-09-24.md` @ `14b885b8c272de4c0f2c1b66d8c792d6bed060cc`
- future execution branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- future task-owned worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
- execution branch/worktree status: NOT_CREATED

本轮只处理新 blocker：

`SWR-PORT-B1 — generic open-source site discovery`

所有旧 finding 保持 CLOSED，除非本 Proposal 直接回归其已批准语义：

```text
SWR-B1 = CLOSED
SWR-B2 = CLOSED
SWR-ER-B1 = CLOSED
SWR-ER-B2-A = CLOSED
SWR-ER-B2 = CLOSED
SWR-ER-B3 = CLOSED
```

---

## 1. SWR-PORT-B1 disposition

**ACCEPT**

Critic 对当前 portability gap 的归因成立。

现有 `scripts/skills.py` 把：

`site-profiles/*.json`

实际当成了 environment apply 的 supported-site registry：

- `environment_detect_profile()` 的显式 `--site` 只能引用 committed profile；
- 未命中 profile 时 `environment apply` 会停止；
- repo 不认识的第三方 Slurm cluster 无法通过正常 environment path 得到完整 installed site context。

这与开源 Skill 的产品定位冲突。

v0.5 冻结的修复不是“继续往 repo 加更多学校 profile”，而是：

> **live Slurm facts 是 generic runtime base；public site profile 只是 optional hard-policy overlay。**

Longleaf、CUHK 是两个 deployment evidence，不是产品边界。

---

## 2. 完整产品架构

v0.4 已批准的整体机制全部保留，并在最底层加入 generic live discovery：

```text
live Slurm discovery
+ optional public site hard-policy overlay
+ user-local site facts / preferences
        ↓
resolved local site context
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
-> preference
-> advisory probe
-> native single-job widening
-> fail closed / guarded duplicate fallback
```

核心 ownership 明确区分：

```text
live scheduler facts
!=
site hard policy
!=
user/project preference
```

这三个层次不得混为一个 “site profile”。

---

## 3. Site Profile 的新定位

### 3.1 site-profiles/*.json 是什么

它是：

> optional public-safe hard-policy overlay + optional safe detection hints.

可以承载：

- 站点公开确认的禁止/要求；
- generic Slurm CLI 无法可靠推断的 public policy；
- public-safe site capability notes；
- safe profile matching hints；
- 站点已公开且长期稳定的约束。

例如现有 Longleaf/CUHK profile 中的：

- `do_not_submit_without_user_confirmation`
- `race_execution=disabled_by_default`
- private paths must use local override

仍然可以保留。

### 3.2 它不是什么

它不是：

> AI_Skills 支持哪些服务器的 central registry。

因此：

- repo 没有某学校 profile ≠ unsupported；
- `environment list-sites` 未来文案应解释为 “known public policy overlays”，不是 supported-cluster list；
- 不因为第三方用户换学校就要求向公共 repo 新增 JSON；
- 不通过长期扩充 hostname/partition catalog 实现“通用”。

### 3.3 Profile 不能创造 live facts

即使某个 optional profile 存在：

> current partition/resource existence 仍以 live scheduler 为准。

Public profile 可以限制或补充 policy，但不能因为文档里写过一个 partition 就让 runtime 假定该 partition 当前存在。

---

## 4. Local Site Identity 与 Policy Overlay Identity 分离

v0.5 明确区分两个 id：

### local_site_id

当前实际 Slurm deployment 的 user-local stable identity。

它用于：

- `local-overrides.toml [sites.<local_site_id>]`
- sticky workload/resource contract 的 site binding；
- persistent capacity family enrollment 的 site binding；
- runtime generated site context identity。

### policy_overlay_id

可选 committed public profile id，例如：

- `unc-longleaf`
- `cuhk-central-cluster`

它只回答：

> 当前 local site 是否有一个已知 public hard-policy overlay 可以附加？

两者可以相同，但**不要求相同**。

这避免把 “repo 里有没有 profile” 与 “当前 scheduler 是谁” 绑定。

---

## 5. Generic local_site_id 如何获得

优先级：

### A. 用户已 locally 指定 stable site id

如果 `local-overrides.toml` 或 Slurm Workflows local config 已绑定：

`local_site_id=<id>`

直接复用。

### B. Live Slurm ClusterName

如果可安全读取：

`scontrol show config`

中的 `ClusterName`，则可把 sanitized cluster name 作为 local identity 候选。

它只留在本机/local generated context；不自动写进公共 repo。

### C. ClusterName 不可用/过于含糊

只询问一次 local stable id。

不要求：

- repo profile；
- hard-coded hostname list；
- 修改公共 source。

### D. Hostname

Hostname 不是 canonical generic site identity。

Public profile 可以用 safe hostname pattern 做 overlay detection hint，但 generic runtime 不应把 hostname catalog 当产品基础。

---

## 6. Generic Live Slurm Discovery Contract

当当前环境可访问 Slurm，不论 repo 是否认识该站点，都先做一次 **bounded read-only discovery**。

默认每个正常 routing/planning invocation 至多执行一轮 discovery；不 tight-loop、不后台轮询。

### 6.1 Discovery readiness

最低要求：

- 当前能调用必要 read-only Slurm CLI；
- scheduler controller可响应最小查询。

如果当前不是 Slurm 环境：

- 不伪造 site facts；
- standalone Skill仍可被安装；
- 但当前 invocation不能声称 Slurm routing ready。

### 6.2 `sinfo` — visible topology/resource facts

优先发现当前用户实际可见的：

- partition names；
- default partition marker；
- partition availability/state；
- node counts/state summary；
- CPU counts；
- memory；
- GRES；
- features；
- partition/default/max time limits；
- partition priority tier where exposed。

推荐使用明确 format fields或 structured output（当前版本支持时），而不是依赖随版本变化的默认 human table。

**不使用 `--all` 去主动扩大到当前用户正常视野之外的 hidden/unavailable partitions。**

`sinfo` 发现 `p1,p2,gpu-x`：

> 只证明这些 route 当前可见；不表示 generic Skill偏好任何一个。

### 6.3 `scontrol show partition` — detailed current partition facts

在普通用户权限可见时，读取：

- Default；
- State；
- MaxTime / DefaultTime；
- MinNodes / MaxNodes；
- DefMem / MaxMem semantics；
- TRES；
- AllowAccounts / DenyAccounts；
- AllowQOS / DenyQOS；
- PriorityTier / PriorityJobFactor；
- ReqResv；
- OverSubscribe / PreemptMode；
- current Nodes/NodeSets only as scheduler facts, not generic preferences。

这些字段用于：

- legal-candidate screening；
- resource-contract compatibility；
- persistent/calendar capability planning。

注意：

> partition-level `AllowAccounts=ALL` / `AllowQOS=ALL` 并不等价于“当前 user一定具有有效 association”。

最终 account/QOS eligibility仍需 association evidence、local fact或 advisory test。

### 6.4 `scontrol show config` — scheduler capability facts

只选择与当前能力有关的 fields，不保存整份 raw config 到公共 artifact。

至少可读取：

- `ClusterName`
- `SelectType`
- `SelectTypeParameters`
- `SchedulerType`
- relevant `SchedulerParameters`
- `PriorityType`
- `PriorityFlags`
- `PrivateData`
- accounting backend是否存在的相关 type/status信息

用途包括：

- local site identity；
- memory/TRES semantics；
- backfill/priority capability判断；
- `ACCRUE_ALWAYS` 等已批准 calendar语义；
- 识别某些 discovery source为何不可见。

不把 controller hostname、database host、private path 等与 routing无关的配置自动传播到公共 artifact。

### 6.5 `sacctmgr show assoc user=$USER` — optional user association facts

只有当前 site / SlurmDBD / permissions允许时才查询。

允许读取当前 user association中的：

- Cluster；
- Account；
- Partition；
- QOS / DefaultQOS；
- 与当前 resource legality直接相关的 limits（必要时）。

如果：

- 没有 SlurmDBD；
- `sacctmgr` 不可用；
- site权限不允许；
- 输出不完整；

则：

> 该层为 UNKNOWN，不把 query failure当成 environment failure。

使用 user-local override / site docs / current explicit user fact补齐。

绝不自动创建/修改 account、association或QOS。

---

## 7. Discovery Provenance：每个事实都有来源状态

Runtime `SiteContext` 中的事实至少分成：

```text
LIVE_KNOWN
LOCAL_EXPLICIT
PROFILE_POLICY
UNKNOWN
```

不能把 UNKNOWN 填成 generic default。

例如：

```text
visible_partitions: LIVE_KNOWN
current_account: UNKNOWN
duplicate_race_authority: PROFILE_POLICY(disabled_by_default)
partition_priority: LOCAL_EXPLICIT
```

这允许 Skill明确知道：

- 哪个是 scheduler事实；
- 哪个是站点政策；
- 哪个只是用户偏好；
- 哪个还不知道。

---

## 8. Runtime SiteContext：不建立服务器数据库

v0.5 不引入 central registry 或 site inventory DB。

### 8.1 Canonical current facts

**live Slurm CLI 永远是 current-fact authority。**

正常入口每次按需生成一个 in-memory `SiteContext`。

不以历史 snapshot替代 live scheduler。

### 8.2 Generated installed reference

当前兼容路径：

`references/_generated/site-profile.md`

继续存在，但其语义变成：

> generated site-context locator / public-policy summary，而不是 current scheduler fact database。

它至少记录：

- `local_site_id`
- optional `policy_overlay_id`
- policy overlay revision
- local override locator
- live discovery required/available status
- public hard-policy summary
- fact/policy/preference ownership说明

正常 routing仍刷新 live facts。

### 8.3 不把 private live facts自动提交到项目repo

特别是：

- private hostname；
- account；
- private path；
- internal controller/db host；
- private QOS；
- site内部敏感信息

不得因为 `environment apply --target repo` 就被自动写成可提交 source。

Public generated reference只允许 public-safe summary / local locator。

如实现需要保留 transient raw discovery evidence，用 user-local runtime/temp路径；它不是 repository tracked source。

---

## 9. Unknown Site 的 Environment CLI 行为

### 9.1 environment detect

未来输出应至少区分：

```text
local_site_id
scheduler = slurm | unavailable
live_discovery = available | unavailable
policy_overlay_id = <optional>
matched_policy_overlays = [...]
```

“没有 profile”不再等于 “unknown unsupported”。

### 9.2 explicit --site

Backward-compatible语义：

- 如果 `--site <id>` 命中 committed profile，可同时把它作为 local identity / policy overlay candidate；
- 如果没有命中 committed profile，`<id>` 被视为 user-local site id，而不是报 `unknown site profile`。

是否附加 public overlay由实际匹配/显式 known profile决定。

### 9.3 automatic no-profile path

如果：

- 没有 committed profile匹配；
- 但 live Slurm discovery成功；

则 environment plan/apply 继续进入：

`GENERIC_LIVE_SLURM`

不要求修改 repo。

### 9.4 environment apply

对 generic live site：

- materialize `slurm-workflows` 和已有环境skill；
- generated reference标明 no public policy overlay；
- local override section使用 `local_site_id`；
- normal installed Skill在真正 routing时刷新 live facts。

### 9.5 no Slurm controller available

如果既没有 usable live scheduler，又没有足够 local site facts：

- `environment apply` 不应伪装成 fully configured Slurm environment；
- 可以引导用户使用普通 standalone install；
- doctor报告 `SLURM_RUNTIME_UNAVAILABLE`；
- routing mutation fail closed。

---

## 10. Known Profile 与 Live Facts 的 Merge

Effective context构造顺序：

### Step 1 — live facts

先看当前 scheduler：

> 当前可见/当前存在/当前 resource shape是什么？

### Step 2 — optional hard-policy overlay

再应用 public profile：

> 哪些动作被站点明确要求/禁止？

Hard policy可以更严格，但不应凭空制造 live partition。

### Step 3 — local explicit facts

补充 live无法发现但用户知道的：

- account；
- QOS；
- local site id；
- partition preference；
- private module/path；
- local recurrence/capacity preferences。

Local fact不能放宽已知 hard policy。

### Step 4 — workload/project preferences

最后决定：

- preferred legal partition order；
- accepted resource contract；
- workload/capacity family；
- persistent capacity target；
- enrollment scope。

---

## 11. Generic Safety Baseline for Unknown Policy

没有 public profile时，不把所有能力都当作“允许”。

同时也不能把普通 Slurm submission全部禁掉，否则 generic open-source path无法工作。

v0.5冻结以下 generic安全基线：

### Normal user-owned submission

需要：

- 当前用户显式 task authorization，或
- v0.4 已批准的 valid enrolled capacity-family authorization；

并且：

- account/QOS/resource request不能靠猜；
- final request由 scheduler/advisory validation接受。

### Duplicate race

unknown site authority -> **disabled**。

只有 explicit site allow + user/local opt-in 才能启用。

### Automatic recurring successor

沿用 v0.4：

- preference不等于authorization；
- valid enrollment才允许同scope recurring mutation；
- known site hard policy可进一步禁止；
- unknown site不会因为普通 TOML preference自动mutation。

### Administrator-level actions

永远不从 generic discovery获得授权。

不尝试：

- create/modify partition；
- create advanced reservation；
- modify association/account/QOS；
- scheduler reconfigure。

---

## 12. FACT != POLICY != PREFERENCE

### Fact example

Live:

```text
partition = gpu-x
GRES = gpu:<site-type>:4
State = UP
MaxTime = ...
```

它说明：

> 当前 scheduler报告了什么。

### Policy example

Optional profile：

```text
duplicate_race = forbidden
```

它说明：

> 站点明确禁止什么。

### Preference example

Local config：

```text
partition_priority = p2,p1
```

它说明：

> 在所有合法可用 route中，用户偏好哪个。

Skill不得把：

`sinfo list order`

当作 preference。

也不得把：

`PriorityTier`

当作用户 preference；它是 scheduler自身 partition scheduling fact。

---

## 13. Hard-coding Rule

Generic production source禁止包含 deployment-specific routing constants。

至少包括：

- `htzhulab`
- `a100` 作为特定 Longleaf route常量
- Longleaf hostname
- CUHK partition names
- site-specific H100 route name
- compute node names
- 其他学校 partition/account/QOS/host constants

### 允许出现的位置

- user-local config；
- optional site-specific public profile；
- tests/fixtures；
- examples，且明确不是 default；
- live-discovered evidence。

### Hardware semantics vs site routing

Generic Skill可以理解：

- GPU count；
- generic GRES/type字段；
- “某 accelerator requirement必须满足”。

但不能写：

> H100一定走某 partition，A100一定走某 partition。

GPU type -> partition mapping必须来自 live facts + site/local context。

---

## 14. Existing v0.4 Architecture Remains Intact

以下不重新设计。

### 14.1 Workload modes

- finite unattended -> batch
- persistent reusable capacity -> persistent allocation
- short debug -> debug interactive

`salloc --no-shell + srun --jobid` 仍是 later target-site validated candidate，不宣称绕过queue。

Bridge Kit：

`NO CHANGE`

### 14.2 Sticky resource contract

Comparable workload family、current-state `slurm-workflows.toml`、G7 hysteresis全部保持。

Deployment/site binding改用：

`local_site_id`

不依赖 committed profile id。

### 14.3 Persistent capacity family

Capacity family enrollment同样绑定：

`local_site_id`

而不是要求 repo预先认识该学校。

One-time enrollment、activation scope、resource envelope、one-successor、read-only unenrolled行为全部保持。

### 14.4 Routing safety

全部保持：

- ordered local preference；
- `--test-only` advisory；
- parse failure fail closed；
- native single-job widening；
- in-place Partition update需 target-site/job-class probe；
- replaceable pending-only cancel+resubmit；
- state-safe cancellation；
- identity-sensitive JobId fail closed；
- duplicate race explicit site allow + user opt-in。

Live discovery只提供 current facts，不绕过这些 safety gates。

---

## 15. Unknown / Private Site Fail-Closed Cases

### Case A — sinfo可用，scontrol partition不可见

使用 `sinfo` 的可见 facts。

详细 partition限制记为 UNKNOWN。

不猜 MaxMem/AllowQOS等。

### Case B — sacctmgr不可用/无SlurmDBD

account/QOS association UNKNOWN。

从：

- user-local override；
- user明确fact；
- site docs（用户提供/未来optional profile）

补齐。

不执行 account/QOS mutation。

### Case C — PrivateData隐藏partition/account detail

只使用当前用户正常可见的数据。

不试图用 privileged command或SSH/管理员路径绕过。

### Case D — public profile存在但 live partition已消失/改名

以 live existence为准。

Profile不能复活 stale partition。

Local preference引用不存在route：

> doctor/routing报告 stale preference；不猜替代。

### Case E — hard policy未知

高风险能力 fail closed，例如 duplicate race。

普通 user-owned submit只有 current user/task 或 enrollment authorization后才能执行。

---

## 16. Interaction with Enrollment and Capacity Lifecycle

Open-source portability不能破坏 v0.4 authority。

一个 enrolled capacity family至少绑定：

- `local_site_id`
- resource envelope
- accelerator requirement
- recurrence/window
- action scope

Live discovery刷新后：

### same site / same compatible facts

正常继续。

### partition renamed/removed

如果 enrollment依赖的 route不再 live-visible：

> 不自动改到“看起来差不多”的 partition。

重新做 legal candidate selection；如果新 route仍在 enrollment resource/action envelope但 local preference需要修改，可提出更新。

Material enrollment scope变化仍按 v0.4 reauthorization。

### cluster identity changed

`local_site_id` mismatch：

> old enrollment不跨site继承。

---

## 17. Alternatives Considered

### A. 给每个学校都加 public profile

拒绝。

会把开源 Skill变成central server registry，而且永远跟不上 site变化。

### B. 只依赖 hostname猜学校

拒绝。

hostname可以私有/变化，也无法发现当前 partition/resources。

### C. 完全不用 public profile，只看 Slurm

拒绝。

Scheduler facts无法表达所有 human/site hard policy，例如 duplicate race是否被当地使用规则允许。

### D. 自动抓学校网站/文档

拒绝本轮。

来源复杂、可能需登录、容易stale，且不是最小 portability机制。

### E. Selected hybrid

```text
live Slurm = current facts
optional profile = public hard policy
local override = missing private fact + user preference
```

这是最小且可扩展的开源结构。

---

## 18. Capability Gates v0.5

不新增 G9。

G2–G5、G7、G8保持已接受语义。

只扩展 G1 与 G6。

### G1 — Site isolation + live discovery

原有 site isolation保留，并新增：

#### G1-A — no deployment leakage

generic production source不包含真实 deployment routing常量。

Static fixture/example中的名称不算 production default，但必须明确是fixture/example。

#### G1-B — unknown live Slurm site works without repo change

用 deterministic fake Slurm CLI模拟：

`third-party-cluster`

repo没有对应 `site-profiles/*.json`。

必须能：

- derive/accept local_site_id；
- discover visible partitions；
- discover current scheduler/resource facts；
- build a valid generic live SiteContext；
- plan/apply generic environment overlay；
- 不要求新增 repo profile。

#### G1-C — hidden facts fail closed

fixture让：

- `scontrol show partition` permission fail，或
- `sacctmgr show assoc` unavailable。

Expected：

- corresponding facts = UNKNOWN；
- no guessed account/QOS/partition policy；
- risky capability不被自动开启。

#### G1-D — optional policy overlay remains stricter authority

Known profile + live facts：

- live scheduler决定 current existence；
- profile hard policy可以限制；
- local preference不能放宽；
- stale profile partition/fact不成为 current route。

#### G1-E — profile list is not support matrix

Third-party generic fixture无需进入 committed profile list仍PASS。

### G6 — Production identity on unknown site

Final candidate必须通过真实 installed normal entry，而不仅helper：

```text
no committed profile
+ fake live Slurm commands
+ local site id / local override
        ↓
environment materialization
        ↓
installed slurm-workflows
        ↓
runtime live discovery
        ↓
resolved SiteContext
        ↓
local preference
        ↓
normal routing plan
```

至少覆盖：

1. no public profile；
2. visible CPU + GPU-like arbitrary GRES/feature strings；
3. user-local preference引用live-discoveredroute；
4. unknown account/QOS时不会猜；
5. no Longleaf/CUHK constant leak；
6. installed Skill依然遵守v0.4 enrollment / v0.2 mutation safety。

主要可用 deterministic fake CLI fixture完成。

不要求第三所学校真实Slurm mutation。

---

## 19. Future Implementation Shape

Critic PASS后未来 execution package可允许：

### A. 一个小型 deterministic discovery helper

位置应属于 `slurm-workflows` / AI_Skills environment层。

职责仅：

- run bounded read-only Slurm commands；
- normalize selected facts；
- tag fact provenance/unknowns；
- return current SiteContext。

不得：

- submit/cancel jobs；
- crawl internet；
- maintain server registry；
- run daemon。

### B. environment CLI semantics update

未来可修改：

- `environment_detect_profile` 不再是整个site detection；
- profile detection变成 optional policy-overlay detection；
- unknown `--site` 可作为 local site id；
- no-profile + live Slurm可 plan/apply；
- doctor支持 generic live site。

### C. generated reference update

`references/_generated/site-profile.md` 继续兼容路径，但明确：

- local site identity；
- optional policy overlay；
- discovery ownership；
- local locator；
- safety/policy summary。

不将private raw facts自动写到tracked project source。

---

## 20. External Official Evidence Checked

检查日期：2026-09-24。

### SchedMD `sinfo`
https://slurm.schedmd.com/sinfo.html

采用：

- partition name/default marker；
- partition availability；
- node/CPU/memory summary；
- GRES；
- features；
- time limits；
- PriorityTier等格式字段；
- 默认不会显示hidden/unavailable-to-group partition；
- 因此不使用 `--all` 扩大normal-user视野。

### SchedMD `scontrol`
https://slurm.schedmd.com/scontrol.html

采用：

- `show partition` 提供 AllowAccounts/AllowQOS、Default、MaxTime、memory/TRES、PriorityTier等详细partition事实；
- `show config` 提供当前 cluster/config信息；
- show命令默认可由普通user使用，但 `PrivateData` 可限制对应信息；
- 权限不足时应当UNKNOWN/fail closed，而不是尝试提权。

### SchedMD `slurm.conf`
https://slurm.schedmd.com/slurm.conf.html

采用：

- `ClusterName` 是 scheduler cluster identity候选；
- `PrivateData` / scheduler/accounting配置是live capability的重要背景；
- local site identity不需要hostname registry。

### SchedMD `sacctmgr`
https://slurm.schedmd.com/sacctmgr.html

采用：

- association由 cluster/account/partition/user构成；
- list/show association可读取 Account、Cluster、Partition、QOS/DefaultQOS等；
- 只在 SlurmDBD/site权限允许时使用；
- 本 Skill绝不自动add/modify/delete association/account/QOS。

### SchedMD Overview / Quick Start
https://slurm.schedmd.com/overview.html
https://slurm.schedmd.com/quickstart.html

采用：

- `sinfo` / `scontrol` / `sacctmgr` 是Slurm原生inspection路径；
- 不需要自建server inventory来发现当前scheduler。

---

## 21. Hard Scope Boundaries

本 v0.5继续禁止：

- central university/cluster registry；
- cloud inventory service；
- SSH management；
- 自动抓取学校文档；
- queue-history DB；
- scheduler ML predictor；
- custom scheduler；
- daemon/watcher；
- administrator privilege；
- automatic account/QOS mutation；
- hard-coded node ranking；
- Bridge Kit修改。

Live discovery是read-only inspection能力，不是新的control plane。

---

## 22. Version / Release Direction

Architecture v0.5本身：

- Repository bump: NONE
- standalone Skill bump: NONE
- central Plugins: NO_BUMP
- Bridge Kit: NO CHANGE

如果后续实现、同一final candidate gates、final review和release closure都通过：

- `slurm-workflows 0.1 -> 0.2`
- repository next PATCH from actual release-time `VERSION`
- central Plugins all `NO_BUMP`

Open-source generic discovery属于现有 standalone Slurm/environment product的兼容增强，不新增中央 Plugin。

---

## 23. Planner Final Position

v0.5把 Slurm Workflows 的底层产品边界改正为：

> **The Skill knows Slurm, not your university.**

正常使用不应该先问：

> “repo有没有这个学校？”

而应该：

1. 当前是不是可访问 Slurm；
2. live scheduler当前显示什么；
3. 有没有optional public hard-policy overlay；
4. 当前user/local还补了哪些private事实；
5. 用户对合法route有什么preference；
6. 当前workload/resource/capacity contract是什么。

Longleaf、CUHK与任意第三方cluster都走同一个generic path；有profile只是多一层policy证据，不是获得“支持资格”。

因此当前最终 composition 是：

```text
live facts
+ optional policy overlay
+ local facts/preferences
+ sticky workload/capacity contract
+ bounded authorization
-> portable Slurm Workflows
```

在独立 Critic 对 v0.5 PASS 前：

- 不修改 production source/tests；
- 不创建 execution branch/worktree；
- 不执行真实 Slurm mutation；
- 不启动 Executor；
- 不修改 Bridge Kit；
- 不 bump version。
