# Slurm Workflows Routing Refactor Proposal v0.1

日期：2026-09-24  
角色：AI Research Stack Planner  
状态：AWAITING_INDEPENDENT_CRITIC_REVIEW

## Active Design Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `main@7c7083015c04a898c2536f7c60ffa79f5bccef1a`
- proposal_path_and_version: 本文件 / v0.1
- execution_branch/worktree: 尚未创建；本轮只做设计，不启动 Executor

本轮实际读取了 latest main 的 `AGENTS.md`、Planner/Critic Role Contract、`PLUGIN_CAPABILITY_GATE_POLICY.md`、当前 `slurm-workflows`、site profiles、environment CLI/override 实现、相关 tests，以及历史 server-overlay 设计证据。外部核查优先使用 SchedMD 官方 Slurm 文档，见文末。

---

## 1. 结论

**需要重构，但不需要重写整个 Slurm 系统。**

当前正确的长期边界其实已经存在：

```text
generic Slurm Workflows Skill
        +
site-level hard constraints / policy
        +
machine/user-local routing preferences
        ↓
managed university / research Slurm cluster
```

问题是当前实现没有真正守住这个边界，而且 routing/race 只完成了一半。最明显的真实错误是：

`scripts/skills.py::environment_blank_site_override()` 对 **所有 site** 都生成：

```text
partition_priority = "htzhulab,a100,volta-gpu"
race_after_minutes = "60"
race_partitions = "htzhulab,a100,volta-gpu"
```

这把 Longleaf-specific partition 名和旧 race 默认值放进了通用 environment template。结果是 CUHK 或任何未来 Slurm site 初始化时都可能得到 Longleaf 路由配置，直接违反当前 Skill 自己的 trigger boundary、`SERVER_ZIP_INVENTORY.md` 的分层决定，以及用户当前明确要求。

因此，本轮不是“给 SKILL.md 多加几句话”，而是修复：

1. generic Skill 与 site-local routing policy 的真实边界；
2. partition preference 与 race 的执行语义；
3. generated site reference 没有传播 site policy 的缺口；
4. environment doctor/config 不能验证 routing policy 的缺口；
5. 当前 race 设计过于粗糙，容易产生重复作业、重复写 output 和无谓资源占用。

---

## 2. 产品定位

### 2.1 这个 Skill 应该服务谁

`slurm-workflows` 的正常对象应收窄为：

> 使用 Slurm 的共享、受管理员管理的科研/HPC 集群，尤其是 Longleaf 这类大学或研究机构服务器。

它不是：

- 本地 workstation 的 generic shell helper；
- 单机 Linux server helper；
- Kubernetes / cloud batch scheduler；
- 用来替代站点管理员 scheduler policy 的工具；
- 把某个学校 partition 名硬编码成通用常识的工具。

### 2.2 用户新增的真实能力

重构后，普通用户应能说：

> 在 Longleaf 跑这个实验。

Skill 随后能够：

1. 读取当前 site 的真实 routing policy；
2. 知道“首选哪个 partition、次选哪个”是用户/机器配置，不是 Skill 常量；
3. 先用 Slurm 自己的调度信息判断哪条路可用；
4. 在首选可合理启动时只走首选；
5. 首选不合适而次选明显可用时走次选；
6. 两边都要等时，优先用 **一个 Slurm job 的 multi-partition request** 打开两条可接受路线；
7. 只有 multi-partition 无法表达两个 route 的资源差异时，才进入受控 duplicate-job race；
8. 不让两个 race candidate 同时写同一个最终 output；
9. 不用紧密 polling 给 slurmctld 制造额外压力；
10. 对当前站点不知道的 partition/account/QOS 不猜。

---

## 3. 已验证的当前问题

### P1 — 通用 template 硬编码 Longleaf partitions

当前：

```python
partition_priority = "htzhulab,a100,volta-gpu"
race_partitions = "htzhulab,a100,volta-gpu"
```

来自通用的 `environment_blank_site_override(site_id)`，不是 Longleaf-specific source。

这是明确的 architecture regression。

### P2 — 当前 static example 与真实 `environment init` 输出已经漂移

`site-profiles/local-overrides.example.toml` 只展示：

```text
account
partition
qos
scratch_root
...
```

而 CLI 实际支持并生成：

```text
partition_priority
qos_priority
race_after_minutes
race_partitions
race_cancel_policy
```

用户看文档和实际 init 得到的是两种配置模型。

### P3 — generated site reference 没有传播 site policy

`environment_site_reference()` 当前生成：

- public constraints
- local_prompt_policy
- module hints

但没有把 `site-profile.json -> policy` 写进 generated reference。

与此同时 `slurm-workflows/SKILL.md` 又规定：

> race 只有 site profile explicitly allows 时才使用。

也就是说，Skill 被要求遵守一项安装后看不到的 policy。

### P4 — race 字段重复且语义不清

当前同时存在：

```text
partition_priority
race_partitions
race_after_minutes
race_cancel_policy
```

其中 `race_partitions` 通常只是重复 `partition_priority`；`race_cancel_policy=cancel_after_first_validated_output` 还可能取消得过晚：若 loser 已经开始昂贵 workload，等到“第一个完整 output validated”才取消并不能阻止重复计算和 output collision。

### P5 — doctor 的 scheduler required fields 是全局硬编码，不是真正 site-aware

当前 `LOCAL_OVERRIDE_REQUIRED_FIELDS` 固定要求：

```text
account
partition
qos
scratch_root
module_init
```

这与 site profile 的真实 constraints 没有闭环。例如某个 site 未必要求显式 QOS；配置 `partition_priority` 也不能满足当前对单一 `partition` 的缺失检查。

这会制造不必要的人类输入和错误诊断。

### P6 — 历史设计要求的 routing/race tests 没有落地

2026-07 的 server-overlay 设计已经明确提出：

- partition priority；
- race allowed/forbidden；
- loser cancellation；
- output isolation；
- 不得在 generic Skill 硬编码 CUHK/UNC partition。

当前 tests 主要检查 environment init/apply/doctor 的机械行为，没有覆盖上述真实 routing capability。

---

## 4. 外部 Slurm 核查及其设计影响

### 4.1 `sbatch --test-only` 可以在不提交 job 的情况下估计启动时间

SchedMD 官方 `sbatch` 文档说明，`--test-only` 会验证 batch script，并基于当前队列估计何时可运行，**不会实际提交 job**。

采用决定：**采用，作为 routing 前的首选 advisory probe。**

它不能被当成启动时间保证，但比仅看 partition 是否有 idle node 更贴近真实 job requirement。

### 4.2 Slurm 原生支持一个 job 请求多个 partitions

官方 `sbatch --partition=p1,p2` 语义是：当 job 可用于多个 partition 时，Slurm 使用能够最早启动它的 partition；**列表顺序本身不表达用户优先级**。

采用决定：

- 不能从一开始就简单写 `-p htzhulab,a100`，因为这会丢掉“先 htzhulab”的用户偏好；
- 但当 routing policy 已经决定“两条路线都可以打开”后，**single-job multi-partition 应优先于 duplicate-job race**。

这是本 Proposal 最重要的简化。

### 4.3 `squeue --start` / pending Reason 适合作为后续 advisory evidence

官方 `squeue` 可以显示 pending reason；`--start` 在 backfill scheduler 可用时可给 expected start time。

采用决定：用于 pending job 的补充判断，不将 expected start 当保证。

### 4.4 不做高频 polling

SchedMD 明确提醒 `squeue` 等命令会向 `slurmctld` 发送 RPC，不应在 tight loop 中反复调用。

采用决定：Skill 只做 bounded/status-driven checks，不引入 watcher/daemon。

### 4.5 机器偏好优先用 Slurm feature preference，而不是随意 pin hostname

官方 `sbatch --prefer=<features>` 提供 soft feature preference；而指定 node list 会变成更强的资源约束。

采用决定：

- v0.2 可以允许 site-local **feature preference**；
- 不建立“任意 node hostname ranking engine”；
- 用户确实要求固定 node 时，把它视为显式 hard constraint，不作为默认 routing。

---

## 5. 比较过的现实路线

### A. 不改，只删除 `htzhulab,a100,volta-gpu`

优点：最小。

拒绝原因：只能关闭 P1，P2–P6 仍然存在；尤其 Skill 仍然看不到 site race policy，也没有可靠 routing semantics。

### B. 所有任务从一开始都用 `--partition=htzhulab,a100`

优点：简单、只有一个 job。

拒绝原因：官方文档明确说明 multi-partition 选择以 earliest initiation 为主，partition 名顺序不表达用户 preference。它不能实现“先 htzhulab、再 a100”。

### C. 一开始就同时提交两个 job，谁先 RUNNING/完成就取消另一个

优点：最接近旧人工习惯。

拒绝原因：

- 占两个 queue entries；
- 两个 job 可能几乎同时开始；
- loser cancellation 有竞态；
- 若共用 output 可能损坏结果；
- 资源浪费比 Slurm 原生 multi-partition 更高。

不应作为默认。

### D. 推荐：prefer → probe → select / widen → guarded duplicate fallback

选择。

核心思想：

1. preference 只在 site/user-local config；
2. 用 `sbatch --test-only` 查看每个候选 route；
3. 首选明显可用时只提交首选；
4. 次选明显更可用时允许 fallback；
5. 都要等且 job resource contract 兼容时，用 **single-job multi-partition**；
6. 只有两个 partition 需要不同 resource/header contract，单 job 无法表达时，才允许 duplicate race。

它保留用户的实际使用习惯，但把最危险的“两个完整 job 同时跑”降为例外。

---

## 6. 推荐配置模型

不新建 database、registry、daemon 或第二套 scheduler。

继续使用当前：

```text
public site profile
+
~/.config/ai-skills/local-overrides.toml
+
generated site-profile reference
```

### 6.1 Public site profile：只保存硬边界，不保存用户 partition 名

Longleaf/CUHK public-safe profile 继续不提交：

- account；
- private QOS；
- personal paths；
- 用户自己的 partition ranking。

但 `policy` 需要有清楚语义，并实际进入 generated reference。

推荐把当前模糊的：

```json
"race_execution": "disabled_by_default"
```

收敛成明确语义，例如：

```json
"race_execution": "explicit_user_opt_in"
```

这里的 race 指 **duplicate-job race**；普通 single-job multi-partition 不是重复资源 race。

若站点明确禁止 duplicate race，则：

```json
"race_execution": "forbidden"
```

local override 不能放宽 `forbidden`。

### 6.2 Local override：用户/机器-specific preference

新模板不再出现任何真实 partition 名。

建议保留/新增的 routing 字段：

```toml
partition = ""
partition_priority = ""
routing_strategy = ""
primary_grace_minutes = ""
race_after_minutes = ""
node_feature_preference = ""
```

推荐策略：

```text
routing_strategy = prefer_then_race
```

Longleaf 的用户本机配置可以是：

```toml
partition_priority = "htzhulab,a100"
routing_strategy = "prefer_then_race"
```

这些值只属于该 site/local override，不进入 generic Skill source。

`primary_grace_minutes` 与 `race_after_minutes` 不在公共仓库硬编码默认值。用户可以一次性配置；缺失时 Skill 使用 scheduler evidence 的保守路径，不反复让用户做日常技术选择。

### 6.3 简化旧字段

`race_partitions`：新模板不再生成。默认 race candidate 直接来自 `partition_priority`。旧配置仍可兼容读取一轮，并由 doctor 提示迁移。

`race_cancel_policy`：不再暴露成随意字符串偏好。duplicate race 的安全停止逻辑应由 Skill contract 固定，不让每台机器自己发明。

---

## 7. Routing 决策语义

### 7.1 正常路径

给定 ordered candidate：

```text
P1 > P2 > ...
```

例如 Longleaf 用户配置：

```text
htzhulab > a100
```

Skill：

1. 验证 workload resource request 在 candidate partition 上语义兼容；
2. 对 P1 运行 bounded `sbatch --test-only`；
3. 若 P1 可立即/在用户 grace 内运行，只提交 P1；
4. 否则 probe P2；
5. 若 P2 明显可立即运行而 P1 不行，提交 P2；
6. 若 P1/P2 都需要等待，且同一 batch resource contract 可用于两者，则提交一个：
   `--partition=P1,P2`
7. Slurm 此时负责真正选择最早可启动的 partition。

重要：

> preference 只在“是否扩大候选集”之前生效。进入 multi-partition 阶段后，不再假装 partition 列表顺序代表优先级。

### 7.2 `--test-only` 不可用或 estimate 不可靠

不静默猜。

Fallback：

- 先提交 P1；
- 用 bounded `squeue` / `squeue --start` / `scontrol show job` 观察；
- 只有配置了 wait threshold 或用户当前明确要求扩大路线时，才 widen。

首版实现**不要假设** Longleaf 一定支持把 pending job 原地更新成 multi-partition list。虽然官方 `scontrol` 允许修改 pending job 的 Partition 字段，但 multi-partition update 的站点实际行为应作为受控 probe 验证后再采用。

未验证前的安全 fallback 是：

- 取消仍 pending 的 P1；
- 重新提交 single multi-partition job；
- 明确报告 queue age 会重置。

不要为了“保留 queue age”偷偷再加一个第二 job。

### 7.3 duplicate-job race 只作 fallback

只有满足全部条件才允许：

1. public site policy 不禁止；
2. 用户已经在当前任务或 local config 明确 opt in；
3. 两个 route 因不同 resource/header contract 无法用一个 multi-partition job 表达；
4. race candidate 有独立 log/output staging；
5. expensive payload 开始前有 winner-claim 机制；
6. loser 在 winner claim 后尽快停止；
7. 最终 output 只由 winner promote。

如果无法保证 4–7，返回“不安全，不能自动 duplicate race”，而不是提交两个完整实验。

本 Proposal 不要求新增常驻 race daemon。

---

## 8. “机器优先级”的边界

当前版本先支持两层：

1. partition priority：稳定、通用、最重要；
2. node feature preference：若站点有可用 feature label，可用 Slurm `--prefer` 做 soft preference。

不把 raw compute hostname 排序做成通用核心功能。

原因：

- Slurm 没有可移植的“hostname soft priority list”语义；
- `--nodelist` 会变成 hard constraint，可能显著增加排队时间；
- 机器型号、feature naming 和可见性都是 site-specific。

以后若 Longleaf 确实需要“cXXXX > cYYYY”这种硬偏好，应留在 local config / 当前任务，并明确这是硬 pin，不伪装成通用 scheduler optimization。

---

## 9. 需要修改的生产层

若 Critic PASS，bounded implementation 预计修改：

### Core Skill

- `skills/tools/hpc/slurm-workflows/SKILL.md`
- 可新增一个短 reference：
  `skills/tools/hpc/slurm-workflows/references/routing-policy.md`

SKILL 保持简洁；详细 routing/race decision table 放 reference。

### Environment overlay

- `scripts/skills.py`
- `site-profiles/local-overrides.example.toml`
- `docs/LOCAL_CONFIGURATION.md`
- `site-profiles/unc-longleaf.json`
- `site-profiles/cuhk-central-cluster.json`（仅 policy 语义/必要 revision；不得写入 Longleaf partition）

### Tests

优先扩展：

- `tests/test_skill_update.py`

如 focused test 独立性更清楚，可以新增一个 Slurm environment/routing test file，但不要造新的 test framework。

### README / version closure

若 production behavior 按本 Proposal 改变并通过 gates：

- `slurm-workflows`: `0.1 -> 0.2`
- Repository：按当前 version policy 做 next PATCH；以本 Proposal 时点为 `5.1.0 -> 5.1.1`
- 中央 Plugins：全部 NO_BUMP

README 只需要同步 standalone Skill 当前版本和一句准确定位，不加入 routing 细节。

---

## 10. 不修改的范围

本轮禁止顺手修改：

- Longleaf_Bridge production；
- Bridge Kit；
- Longleaf tunnel/Bridge A/B 的 `general` partition policy；
- CAT-TRACE / CARE 等项目自己的实验逻辑；
- 中央 Marketplace plugin topology；
- 其他 standalone Skill；
- 自动 watcher / daemon / persistent scheduler；
- 任意付费 API。

Longleaf_Bridge 只可作为当前 Longleaf 环境事实的只读参考，不能把 tunnel 冗余问题混进科研实验 routing。

---

## 11. Capability Gate Matrix

| Gate | Capability / claim | Normal entry / evidence | 明确失败 | Regression boundary | Final candidate |
|---|---|---|---|---|---|
| G1 Site isolation | generic template 不再泄漏其他 site 的 partition/race 值 | 对 CUHK/Longleaf/未知 site 运行 environment init/plan/apply fixture；检查 generated reference | CUHK 出现 htzhulab/a100；site policy 未进入 reference；local values 跨 site 泄漏 | render/PDF overlay 与现有 environment install 不被破坏 | YES |
| G2 Preference routing | ordered partition preference 真正生效 | fake/read-only Slurm probes：P1 immediate、P1 blocked/P2 immediate、两者 delayed | 永远固定 P1；忽略 P2；把 list ordering 当 multi-partition priority | ordinary single-partition submission 仍可用 | YES |
| G3 Native race / widen | 两条都要等时优先一个 multi-partition job，而不是两个完整 job | probe fixture + generated command review；必要时真实 `sbatch --test-only` | 无理由提交 duplicate jobs；multi-partition 使用前没有验证 resource compatibility | 用户显式指定单 partition 时不得扩 route | YES |
| G4 Duplicate-race safety | 只有无法用 single-job 表达时才可 duplicate race，且不重复写 output | deterministic race fixture / script review；winner claim、isolated logs/output、loser stop | 两个 candidate 可同时进入 expensive payload；共享 final output；site/user 未 opt in | 没开 duplicate race 的 site 不受影响 | YES if duplicate fallback implemented |
| G5 Diagnostics / bounded monitoring | pending/failure 有真实分类，不 tight-loop scheduler | Priority/Resources/invalid partition/test-only unavailable fixtures；检查 bounded commands | blind resubmit、紧密 squeue loop、把 estimate 当保证 | 现有 failure triage/job arrays/dependencies 能力保留 | YES |
| G6 Production entry | 安装后的真实 standalone Skill 能消费生成 policy，并在 Longleaf-like site 正常工作 | 同一 final candidate：environment apply -> installed skill/reference -> normal invocation；至少做 read-only Longleaf scheduler probe，真实 submission 另需用户明确授权 | helper/test 能跑但 installed Skill 看不到 policy；需要手工把 partition 写进 prompt | CUHK/其他 site 不被 Longleaf preference 污染 | YES |

### Gate scope 说明

这是 standalone Skill + shared environment generator 的用户可见 routing 行为变化，因此不能只做 SKILL.md 文本测试；必须包含 generator/site isolation 回归。

但本轮不需要付费 reviewer，也不需要为了证明 routing 去提交昂贵真实实验。最终真实 Slurm submission 是否做 smoke，需要用户在 execution 阶段明确授权。

---

## 12. 失败恢复

实现期若发现：

### A. `sbatch --test-only` 在目标 site 不可靠

不推翻整体架构。降级为：

```text
primary submit
-> bounded pending inspection
-> user-configured/explicit widening
```

### B. multi-partition job 不能兼容两个 route 的 GPU/resource contract

进入 duplicate-race gate，不偷偷改资源请求以“让它能跑”。

### C. duplicate race 无法证明 winner isolation

该能力保持 disabled；核心 prefer/fallback/native-multi-partition 仍可独立发布，Critic 决定是否需要缩减 release claim。

### D. local override 已有旧字段

兼容读取，不自动破坏用户文件；doctor 给 migration 提示。不要在用户未授权时修改其真实 `~/.config/ai-skills/local-overrides.toml`。

---

## 13. 外部资料记录

检查日期：2026-09-24。

1. SchedMD, `sbatch`  
   https://slurm.schedmd.com/sbatch.html  
   采用：
   - `--test-only` 做无提交的启动估计；
   - multi-partition request 用作 single-job queue widening；
   - `--prefer` 作为 feature-level soft preference。
   不采用：
   - 从 multi-partition 参数顺序推断优先级。

2. SchedMD, `squeue`  
   https://slurm.schedmd.com/squeue.html  
   采用：
   - pending reason；
   - `--start` advisory start time；
   - 避免 tight polling。

3. SchedMD, `scontrol`  
   https://slurm.schedmd.com/scontrol.html  
   观察到：
   - pending job 的 Partition 可修改；
   - 但本 Proposal 不假定 Longleaf 已验证 multi-partition in-place update，需最小真实 probe 后才能进入 production path。

4. SchedMD, Scheduling Configuration Guide  
   https://slurm.schedmd.com/sched_config.html  
   采用：
   - 理解 multi-partition job 会形成多个 job-partition scheduling candidates；
   - 不将估计 start time 当严格承诺。

---

## 14. Planner 决策

**DECISION = REFACTOR_REQUIRED**

但范围是“修复并完成原本已经选择正确的 layered architecture”，不是建立新的 HPC control plane。

最核心的产品变化只有三条：

1. **partition 名和偏好彻底 site/local 化；**
2. **routing 从粗糙 race 改成 prefer -> probe -> single-job multi-partition -> guarded duplicate fallback；**
3. **site policy 必须真正进入 installed Skill 可消费路径，并有真实 capability gates。**

在 Critic 对本 v0.1 Proposal 给出 PASS 之前：

- 不修改 production Skill；
- 不修改 environment generator；
- 不改真实 Longleaf local override；
- 不提交任何 Slurm job；
- 不创建 execution branch/worktree。
