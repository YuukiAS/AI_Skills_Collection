# Slurm Workflows — Parallel Release / Integration Recovery Critic Review R2

日期：2026-10-03  
角色：AI Research Stack 独立 Critic  
审查阶段：PARALLEL_RELEASE_INTEGRATION_RECOVERY_REVIEW_R2

## 审查对象

- Repository: `YuukiAS/AI_Skills_Collection`
- Task: `hpc--slurm-workflows-routing-refactor`
- Branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- Previous recovery plan: `results/hpc--slurm-workflows-routing-refactor/PARALLEL_RELEASE_INTEGRATION_RECOVERY_PLAN_2026-10-02.md` @ `1da7ac5e334531a15a0d8863c99593c172007b86`
- Previous Critic review: `results/hpc--slurm-workflows-routing-refactor/PARALLEL_RELEASE_INTEGRATION_RECOVERY_CRITIC_REVIEW_2026-10-02.md` @ `5216bc2166c2f91964b7b7a89e1d5515e5b6cd43`
- Amended recovery plan: `results/hpc--slurm-workflows-routing-refactor/PARALLEL_RELEASE_INTEGRATION_RECOVERY_PLAN_V2_2026-10-03.md`
- Amendment commit: `86318691fee8411c77d6eedce91eea397c08a35d`

本轮只复核 `PRI-B1_REQUIRED_GITHUB_CI` 及 amendment 是否引入新的直接执行 blocker；不重审 Slurm v0.6 architecture、PF1–PF5 或上一轮已经 PASS 的 recovery 判断。

## 当前事实复核

审查时实际读取：

- current `main = c4018d25c98c85611321c59246ace2979c6c1cf4`
- current `release = 4ce1946ba047ea200c4ab41ae824de999ef535ed`
- `main VERSION = 5.4.1`
- `release VERSION = 5.4.1`
- main 与 release 的当前差异只有 Project Instructions Editor 设计/恢复文档，以及 research-writing / project-instructions-editor TODO 更新；未发现新的 Slurm production、shared runtime、version 或 generated semantic drift。
- `workflow-core = 0.5` 在 main/release 一致。

因此当前 formal release baseline 仍为 repository `5.4.1`。如果 recovery 真正执行前 release 未再次前进，当前 concrete next PATCH 仍为 `5.4.2`；如果 release 已前进，则必须重新 late-bind。

## 结果

```text
RESULT = PASS
READY_FOR_RECOVERY_EXECUTION = YES

PRI-B1_REQUIRED_GITHUB_CI = CLOSED
```

## PRI-B1 关闭理由

v2 已把上一轮缺失的正式 GitHub CI gate 写入 exact combined candidate closure：

```text
combined source/release metadata complete
-> local full gates PASS
-> freeze exact candidate C
-> publish reviewed branch and verify remote tip == C
-> workflow_dispatch existing Codex Marketplace workflow on reviewed ref
-> required GitHub CI PASS
-> verify run head_sha == C
-> independent final Critic
```

这满足 AI Skills Maintainer 当前 formal release contract：正式 release 除本地/full gate 外，还必须有 relevant install/upgrade smoke、version/changelog/README consistency、generated-layer parity 和 required GitHub CI。

当前 `.github/workflows/codex-marketplace.yml` 已实际核实包含：

- `codex-marketplace`，Ubuntu；
- `windows-sparse-checkout`；
- `editable-install-smoke` matrix:
  - `ubuntu-latest`
  - `windows-latest`

因此 v2 列出的 required job instances 与当前 workflow 一致。

GitHub 官方 `workflow_dispatch` 语义也支持该路径：

- workflow file 必须存在于 default branch；
- 可通过 `--ref BRANCH` / REST `ref` 在非默认 branch 上手动运行；
- `workflow_dispatch` 的 `GITHUB_SHA` 是收到 dispatch 的 branch/tag 的最后 commit。

因此：

```text
remote reviewed tip == C
+
dispatch reviewed branch
+
run head_sha == C
```

可以作为 exact candidate CI identity，而不需要为了 CI 新建 PR、branch 或 workflow。

官方参考：
- https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows

## Amendment 未引入新的直接 blocker

### 1. 版本 late-binding

PASS。

v2 不再把 `5.4.2` 当永久固定值，而是在真正 recovery preflight 重新读取 formal `release` / `VERSION`。这正确处理了并行 release。

### 2. main != release

PASS。

v2 明确区分：

- formal release baseline；
- main 上正常 unreleased development drift。

当前实际 diff 与该分类一致。若 execution 时出现新的 formal release、VERSION 不能唯一解释、Slurm/shared-runtime substantive drift 或未完成 release closure，v2 会停止而不是猜测。

### 3. Combined shared surfaces

PASS。

`VERSION`、root CHANGELOG、README dashboard、registry/catalog/generated outputs 及 version-dependent regression tests 被统一作为 combined/late-bound integration surfaces。

特别地：

- `tests/test_standalone_skill_baselines.py` 最终必须同时反映 current repository target、`slurm-workflows 0.3`、`workflow-core 0.5`；
- `tests/test_central_plugin_icon_assets.py` 的 repository version expectation 随 combined target 更新；
- unrelated `tests/test_candidate_plugin_replay.py` 采用 current main truth。

这与上一轮 Critic 的 conflict ownership 一致。

### 4. CI stale protection

PASS。

v2 明确规定，只要 CI 后发生需要新 commit 的 product/generated/version/test/release-metadata 变化，旧 CI 立即 stale，必须冻结新 SHA 并重跑。

这也适用于 final Critic 前后出现的新正式 release/shared release drift：若 integration preflight 迫使 combined candidate 改变，则 prior CI / prior final review 不能继续给新 candidate 背书，必须回到新 exact candidate closure。

不需要为此增加 lock service 或 queue。

### 5. Bridge ownership

PASS。

本问题属于 AI_Skills repository 的并行 maintenance / release composition，不需要修改 Bridge Kit。Bridge 的 Reviewed Handoff branch/authority contract与当前方案没有冲突。

## 非阻塞执行提醒

1. `workflow_dispatch` 应使用 reviewed branch ref；随后以 GitHub run 的实际 `head_sha` 对 frozen candidate C 做精确相等检查，不要仅凭 branch name。
2. CI workflow 本身如果在 dispatch 前已被 default branch 改动，应在 execution preflight 重新读取 current workflow/job matrix；required jobs 以届时 canonical workflow 为准。
3. final Critic PASS 之后仍必须做 latest integration preflight。若该 preflight 导致 release-critical candidate bytes 改变，则 prior CI/Final Critic 对新 candidate 均视为 stale。
4. Critic PASS 不改变 Issue #95 lifecycle；在 recovery/integration/release closure 完成前继续保持 `DOING`。

## 最终字段

```text
RESULT = PASS
PASS_OBJECT = PARALLEL_RELEASE_INTEGRATION_RECOVERY_PLAN_V2_2026-10-03
PASS_OBJECT_COMMIT = 86318691fee8411c77d6eedce91eea397c08a35d

PRI-B1_REQUIRED_GITHUB_CI = CLOSED

VERSION_LATE_BINDING = PASS
CONFLICT_OWNERSHIP = PASS
WORKFLOW_CORE_0_5_PRESERVATION = PASS
ABORT_AND_CLEAN_RECOVERY = PASS
COMBINED_FULL_GATES = PASS
EXACT_SHA_GITHUB_CI = PASS
PARALLEL_MAINTENANCE_DIRECTION = PASS
BRIDGE_CHANGE_REQUIRED = NO

READY_FOR_RECOVERY_EXECUTION = YES
REAL_SLURM_MUTATION_REQUIRED = NO
MAIN_INTEGRATION_AUTHORIZED_BY_THIS_REVIEW = NO
RELEASE_ADVANCEMENT_AUTHORIZED_BY_THIS_REVIEW = NO
```

本 PASS 只批准 v2 recovery execution contract；不等于 final Slurm release PASS，也不授权 main integration、release ref advancement、Issue #95 closure 或真实 Slurm mutation。
