# Slurm Workflows — Final Critic Review: Bounded Race Policy

日期：2026-10-04  
角色：AI Research Stack 独立 Critic  
审查阶段：FINAL_IMPLEMENTATION_REVIEW

## 审查对象

- Repository: `YuukiAS/AI_Skills_Collection`
- Task: `hpc--slurm-race-policy-bounded-opt-in`
- Reviewed branch: `reviewed/hpc--slurm-race-policy-bounded-opt-in`
- Exact product candidate: `cf9bfe16d526811525395d66e05035736e6ecc23`
- Evidence/control tip before this review: `65e3cd68fec0992e431405c3da989891f22ac703`
- Formal release baseline reviewed: repository `5.4.3`, `slurm-workflows 0.3`, `origin/release = 03b0281b1f7fbd29621faa6298cd1db2578a0ffc`
- Current main reviewed: `818b7e643210b0115cbb3add91ad9be90d78a8b2`

本轮只审用户已经冻结的 bounded duplicate-race 语义及其发布候选，不重审 Slurm v0.6 architecture、PF1–PF5 或前一 release。

## 结果

```text
RESULT = REVISE
READY_FOR_FINAL_INTEGRATION = NO

RACE-B1 = OPEN
```

版本、CI、scope、site-profile 保持、tracking 和大部分 truth table 都正确。剩余问题不是新产品要求，而是冻结的“bounded race 必须在正式路径上证明完整安全合同”还没有真正闭合。

## 已通过部分

### Scope / no architecture expansion

PASS。

Candidate 相对当前 main 只增加/修改当前 race-policy task 所需 source、tests、version/release surfaces、tracking/control evidence。没有新增 daemon、watcher、queue service、database、state machine 或后台 race controller。没有 Bridge Kit 修改，也没有 DII consumer 修改。

### Version contract

PASS。

Candidate 当前一致为：

```text
Repository = 5.4.4
slurm-workflows = 0.4
central Plugins = NO_BUMP
Bridge Kit = NO CHANGE
```

README、CHANGELOG、VERSION、SKILL metadata、registry/catalog 与 version-dependent tests 对应一致。当前 formal release baseline 仍为 `5.4.3`。

### Site policy truth table

PASS。

`duplicate_race_decision()` 正确实现：

- explicit prohibition + opt-in -> deny；
- no opt-in -> deny；
- missing / UNKNOWN / disabled_by_default / explicit_user_opt_in + opt-in -> eligible；
- explicit allowed + opt-in -> eligible；
- unrecognized policy -> deny。

Longleaf 和 CUHK profile 均继续保持：

`race_execution = disabled_by_default`

没有伪装成管理员明确允许。

### CI / local evidence

PASS for the current candidate identity。

GitHub Actions run `37185949083` 已独立读取：

- workflow = `Codex Marketplace`
- event = `workflow_dispatch`
- head branch = reviewed task branch
- head SHA = `cf9bfe16d526811525395d66e05035736e6ecc23`
- conclusion = success

Required jobs 全部成功：

- `codex-marketplace`
- `windows-sparse-checkout`
- `editable-install-smoke (ubuntu-latest)`
- `editable-install-smoke (windows-latest)`

RESULT 记录的 local full suite 为 330 tests PASS，与 exact candidate CI 没有 identity 冲突。

### Tracking / Clear Writing

PASS with durable execution locators。

Issue #96 仍 OPEN，labels 为：

- `maintenance-track`
- `kind:regression`
- `scope:standalone-skill`
- `area:standalone-skill`

canonical TODO 有 `tracking: #96`，Resolution commit 尚未填写。RESULT 记录 Project Status = DOING。

RESULT 还记录四次 Clear Writing replay run id，并且 README / Issue 实际 reader-facing copy 已完成对应更新；没有看到与该记录冲突的 evidence。

---

## RACE-B1 — bounded race 的最终安全 gate 仍可被不完整合同放行

### 冻结要求

用户冻结的实现合同要求：

- race 最多两个候选 route；
- 两条 route 必须保持同一 workload / scientific contract；
- 两条 route 必须各自满足 hard resource requirements；
- winner / loser cancellation 和 near-simultaneous RUNNING handling 必须在提交前冻结；
- 不允许两个副本静默进行正式计算；
- formal normal path 必须证明完整 bounded race contract，不能只有文字规则或单独 authority helper。

这也是本 candidate 的 SKILL.md 83–98 行对外承诺。

### 直接证据 A：scientific contract 只比较白名单子集

`skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py:482-498`

`_normalized_contract_subset()` 只保留：

- data
- split
- model
- endpoint
- gpus / gpu_type
- allowed_gpu_types
- walltime
- training_budget
- optional workload_scope_digest

随后 `bounded_duplicate_race_decision()` 在 529–546 行只比较这个子集。

因此如果 workload contract 还有其他科学语义，例如 augmentation、loss variant、checkpoint-selection rule、preprocessing variant 或任意未列出的冻结 scientific field，而没有额外提供 `workload_scope_digest`，两个候选可以在这些字段不同的情况下仍被返回：

`allowed = True`

这与 SKILL.md 98 行“不得改变其他 scientific semantics”不一致。

### 直接证据 B：cancellation contract 只要求非空字符串

`slurm_routing.py:522-527`

当前只检查：

- `cancel_loser is True`
- `winner_rule` 非空
- `running_tie_policy` 非空

但没有验证这些值具有安全语义。

例如：

```text
winner_rule = "anything"
running_tie_policy = "keep_both"
cancel_loser = true
```

仍会通过 522–527 行，并在 555–565 行返回 `allowed=True`。

这不能证明 SKILL.md 94 / 98 行冻结的“近乎同时 RUNNING 时不能静默双跑”合同。

### 直接证据 C：低层 authority helper 可以单独返回 allowed=True

`slurm_routing.py:464-479`

`duplicate_race_decision({}, True)` 在没有候选 route、没有 workload contract、没有 cancellation contract 的情况下就返回 `allowed=True`。

作为内部“authority eligibility”判断本身可以存在；但当前命名/返回值是 final-looking `allowed`，而生产代码中没有任何 callsite 强制所有 race authorization 必须经过 `bounded_duplicate_race_decision()`。

仓库内 `bounded_duplicate_race_decision()` 只有定义和测试调用，没有正式生产 callsite。

因此一个正常消费者仍可能把低层 authority result 直接当成 race permission，从而绕过完整 bounded contract。

### 直接证据 D：本轮 normal-entry smoke 没有测试新 race gate

现有 G6 installed normal-entry tests 会：

- 安装 Skill；
- load installed `slurm_routing.py`；
- 验证 route discovery；
- 验证 persistent capacity。

但没有从 installed Skill/helper 调用新的 bounded race decision。

本轮新增的 race regression 在 `tests/test_slurm_workflows.py:127-204` 是 source-helper unit coverage，不是 installed normal-entry race coverage。

因此 RESULT 中：

`NORMAL_ENTRY_SMOKE = PASS`

只证明旧的安装/route/capacity normal entry 仍工作，不能证明本轮新增 race policy 已进入 installed normal path。

### 因果风险

这不是理论上的风格问题。

若上述缺口进入正式 `0.4`：

1. 两个候选可以在未枚举的科学字段上发生漂移仍被判为 race-compatible；
2. 一个不安全的 `running_tie_policy` 可以通过 gate；
3. 消费者可能只调用 `duplicate_race_decision` 获得 `allowed=True`，没有经过完整 bounded safety gate；
4. 当前 normal-entry evidence 无法证明正式安装后会消费完整 gate。

最坏结果就是本轮要避免的真实失败：两个本应只是“候选”的 GPU 作业同时进入正式计算，或两个并非同一科学实验的作业被错误当成 race。

### 最小关闭条件

不要新增新架构。

只做一次 bounded repair：

1. 把低层 site-policy 判断明确收敛为 authority eligibility，不能单独形成最终 race authorization；正式可提交判断必须只由完整 bounded gate 返回。
2. 对 workload/scientific contract 使用完整冻结 identity：
   - 优先要求并比较 canonical `workload_scope_digest`；或
   - 对完整 frozen workload contract 做 deterministic equality，只排除明确的 route-only 字段。
   - 不能继续依赖当前字段白名单而静默忽略未知 scientific fields。
3. hard resource contract 至少覆盖当前 frozen contract 中所有明确 resource requirements；不能只靠 GPU / walltime 的部分字段。
4. cancellation contract 改成 closed / validated semantics：
   - 只接受明确支持的 winner rule；
   - 只接受明确支持的 near-simultaneous RUNNING rule；
   - 任何可能“keep both”或未知 string 都 fail closed。
5. 增加 negative regressions：
   - 未枚举 scientific field mismatch -> deny；
   - memory/CPU 等 hard resource mismatch（若在 frozen contract 中）-> deny；
   - unknown / keep-both tie policy -> deny；
   - authority helper eligibility 不能被当成 final bounded permission。
6. 增加一个 installed G6/normal-entry race smoke：从安装后的 `slurm-workflows` helper 执行完整 bounded race gate，至少验证一个 positive opt-in case 和一个 unsafe-cancellation negative case。
7. 重跑本轮 targeted tests、完整 `tests.test_slurm_workflows`、full suite、generated parity；如果 product/test bytes 改变，冻结新 candidate 并重跑 exact-SHA GitHub CI。

不需要真实 `sbatch` / `salloc` / `scancel`，不需要 DII mutation，不需要 Bridge Kit 修改，不需要新 Planner。

Owner: `slurm-workflows 0.4` bounded race gate。

---

## External standards check

SchedMD 官方资料确认 `scancel` 能取消 PENDING 或 RUNNING job，因此“winner 后取消 loser”在 Slurm primitive 层是可实现的；但 Slurm 本身不替应用定义本任务的 duplicate-race scientific equivalence 或 near-simultaneous winner policy。这些必须由本 Skill 的 bounded contract 自己 fail closed。

参考：

- https://slurm.schedmd.com/pdfs/summary.pdf
- https://slurm.schedmd.com/slurm_design.pdf

## 最终字段

```text
RESULT = REVISE

FINAL_CANDIDATE = cf9bfe16d526811525395d66e05035736e6ecc23
EVIDENCE_TIP = 65e3cd68fec0992e431405c3da989891f22ac703

SCOPE = PASS
VERSION_CONTRACT = PASS
SITE_POLICY_TRUTH_TABLE = PASS
LONGLEAF_PROFILE = PASS
CUHK_PROFILE = PASS
LOCAL_GATES = PASS
GITHUB_CI_EXACT_SHA = PASS
TRACKING = PASS

RACE-B1_COMPLETE_BOUNDED_GATE = OPEN
NORMAL_ENTRY_RACE_CONSUMPTION = FAIL

READY_FOR_FINAL_INTEGRATION = NO
REAL_SLURM_MUTATION_REQUIRED_FOR_REPAIR = NO
BRIDGE_CHANGE_REQUIRED = NO
PLANNER_REENTRY_REQUIRED = NO
```

本 REVISE 不重开 Slurm architecture，不改变用户已经决定的 race policy，也不要求新的 Planner。它只要求把已经冻结的 bounded race contract真正变成一个不能被部分 helper / 任意字符串 / 未枚举科学字段绕过的正式 gate，并补上 installed normal-entry 证据。
