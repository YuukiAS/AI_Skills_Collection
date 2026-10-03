# Slurm Workflows — Parallel Release / Integration Recovery Plan v2

日期：2026-10-03  
角色：Planner  
任务：`hpc--slurm-workflows-routing-refactor`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
Reviewed branch：`reviewed/hpc--slurm-workflows-routing-refactor`  
既有 worktree：`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

Previous recovery plan:
`results/hpc--slurm-workflows-routing-refactor/PARALLEL_RELEASE_INTEGRATION_RECOVERY_PLAN_2026-10-02.md`
@ `1da7ac5e334531a15a0d8863c99593c172007b86`

Critic review:
`results/hpc--slurm-workflows-routing-refactor/PARALLEL_RELEASE_INTEGRATION_RECOVERY_CRITIC_REVIEW_2026-10-02.md`
@ `5216bc2166c2f91964b7b7a89e1d5515e5b6cd43`

## Planner disposition

`PRI-B1_REQUIRED_GITHUB_CI = ACCEPT`.

Critic 的其他判断全部保持：

- Repository next patch late-binding：PASS；
- conflict ownership：PASS；
- workflow-core 0.5 preservation：PASS；
- abort-and-clean recovery：PASS，带 fail-closed preflight；
- parallel development / serialized final integration：PASS；
- Bridge Kit：NO CHANGE。

PRI-B1 是 recovery execution contract 的遗漏，不需要重做 Slurm architecture、PF1-PF5、Gate taxonomy 或新增 CI workflow。

## 当前仓库状态

本轮 Planner 重新读取后：

- current `main` = `c4018d25c98c85611321c59246ace2979c6c1cf4`
- current `release` = `4ce1946ba047ea200c4ab41ae824de999ef535ed`
- main `VERSION` = `5.4.1`
- release `VERSION` = `5.4.1`
- `release -> main` 只有 unreleased development/docs drift；formal release baseline 仍是 repository `5.4.1`
- current Slurm reviewed branch 在本 amendment 前 = `5216bc2166c2f91964b7b7a89e1d5515e5b6cd43`

因此当前 concrete next-patch target 仍是：

```text
Repository: 5.4.1 -> 5.4.2
slurm-workflows: 0.2 -> 0.3
workflow-core: remains 0.5
other central Plugins: NO_BUMP
Bridge Kit: NO CHANGE
```

但 `5.4.2` 仍是 late-bound concrete value：Executor 真正恢复时必须重新读取 `release` 与 `VERSION`。如果 formal release 已前进，则从新的 formal release baseline 重新计算 next PATCH，不能机械保留 5.4.2。

当前 `main != release` 已分类为正常 unreleased development drift，而不是第二个已完成 formal release。若执行时出现下列任一情况，则停止并返回 Planner，而不是猜：

- `release` ref 已前进；
- main/release 的 formal VERSION 不一致；
- main 出现新的 Slurm/shared-runtime substantive drift；
- 另一个 release 正处于未完成的 version/ref closure，无法唯一确定 formal baseline。

## Recovery 与 combined candidate

沿用 v1 recovery ownership，不再改变：

1. 对当前 conflicted local worktree 先验证 `MERGE_HEAD`、无未保存 task-owned edit、R4 semantic work 已在远端；
2. 只有上述证明成立才 `git merge --abort`；
3. fetch 并 fast-forward 当前 reviewed worktree 到最新 `origin/reviewed/hpc--slurm-workflows-routing-refactor`；
4. 再 fetch latest main，做 relevant semantic drift check；
5. 以 current main truth + Slurm task-owned delta 构造 ordinary non-force combined candidate；
6. 保留 current main 的 workflow-core 0.5 与其他已发布/已合入 truth；
7. Slurm standalone target 保持 0.3；
8. shared late-bound surfaces 从 combined truth 重算：
   - `VERSION`
   - root `CHANGELOG.md`
   - README release/dashboard
   - registry/catalog/generated outputs
   - deterministic version-consistency tests；
9. `tests/test_candidate_plugin_replay.py` 等 unrelated shared test 采用 current main truth；
10. `tests/test_standalone_skill_baselines.py`、`tests/test_central_plugin_icon_assets.py` 等 version-dependent tests 按 combined repository version 更新；
11. 不 rebase/force，不创建 successor/branch/worktree，不执行真实 Slurm mutation。

## 本地 combined-candidate gates

完成 combined source + release metadata 后，先本地运行并全部 PASS：

- PF5/G8；
- 完整 G1-G8；
- `python -m unittest tests.test_skill_update`；
- `python scripts/skills.py validate`；
- `python scripts/skills.py audit --all`；
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report`；
- `python -m unittest discover -s tests`；
- repository version / README / changelog / registry / catalog / generated consistency；
- relevant install / normal-entry smoke。

这些本地 gates 通过后才允许冻结 exact combined candidate。

## PRI-B1 — exact combined candidate 必须通过正式 GitHub CI

当前 canonical CI 已核实为：

`.github/workflows/codex-marketplace.yml`

触发方式：

```yaml
pull_request:
workflow_dispatch:
```

普通 reviewed-branch push 不会自动运行该 full integration/release matrix。因此本任务必须显式触发已有 `workflow_dispatch`；不要为了 CI 单独创建 PR，也不要新增 workflow。

### CI 顺序

严格顺序：

```text
combined source/release metadata complete
-> local full gates PASS
-> freeze exact candidate commit C
-> ordinary non-force publish reviewed branch, verify remote tip == C
-> workflow_dispatch Codex Marketplace against exact reviewed ref/C
-> all required jobs PASS
-> record workflow run identity + head_sha/ref + required job conclusions
-> only then hand candidate C to independent final Critic
```

如果 CI 之后 candidate bytes 发生任何需要新 commit 的产品、generated、version、release-metadata 或 test 变化，则旧 CI 立即 stale：

```text
candidate changed after CI
=> rerun local affected/full gates as required
=> freeze new exact candidate
=> republish
=> rerun required GitHub CI
```

不能用旧 run 给新 commit 背书。

### Required jobs

对 exact candidate 的现有 `Codex Marketplace` workflow，所有 required job instances 都必须成功，包括至少：

- `codex-marketplace`（Ubuntu full tests + builder/write/validate/path-report/check + skill validate/audit + generated cleanliness）；
- `windows-sparse-checkout`；
- `editable-install-smoke` on Ubuntu；
- `editable-install-smoke` on Windows。

任何 required job FAIL/CANCELLED/TIMED_OUT，candidate 都不能进入 final release Critic PASS。基础设施级失败可以按现有 bounded recovery 重跑；产品/生成层/版本一致性失败必须返回 implementation repair。

### Exact identity requirement

CI evidence 必须明确绑定：

- repository = `YuukiAS/AI_Skills_Collection`
- workflow = `Codex Marketplace`
- reviewed branch = `reviewed/hpc--slurm-workflows-routing-refactor`
- workflow run id / URL locator
- run `head_sha`
- expected exact candidate SHA
- required jobs and conclusions

最终必须验证：

```text
CI head_sha == exact combined candidate SHA
remote reviewed branch tip == exact combined candidate SHA
```

若 workflow_dispatch 后 branch 被另一个 commit 推进，不能仅凭 branch 名认定旧 CI 对当前 candidate 有效；仍以 run `head_sha` 与 frozen SHA 精确比对。

## Final Critic / integration boundary

只有下面全部成立时才进入 independent final Critic：

```text
combined exact candidate frozen
+ local full gates PASS
+ required GitHub CI PASS on same exact SHA
+ Issue #95 anchor current
+ current formal release baseline/version rechecked
+ no new relevant main drift
```

Final Critic PASS 之前：

- 不集成 main；
- 不推进 release ref；
- 不关闭 Issue #95；
- 不填写 Resolution commit；
- 不执行真实 Slurm mutation；
- 不自我批准。

Final Critic 之后的 main/release movement 仍按当时 latest integration preflight 与 fast-forward-only release closure执行；本 plan 不预授权 release advancement。

## Parallel maintenance boundary

PRI-B1 不改变已通过的长期方向：

- 其他 plugin/skill reviewed tasks 继续并行开发、测试、Critic；
- 不要求它们因为本 Slurm task 等 CI 而停止；
- heavyweight GitHub CI 是每个正式 integration/release candidate 的阶段门，不是每次 ordinary push 都跑；
- shared release surfaces 继续 late-bind；
- 最终 main/release integration 仍短暂串行；
- 不新增 queue、lock service、daemon、registry、state machine；
- Bridge Kit 不修改。

如果其他 task 在 Slurm CI 前再次完成 formal release，只需在 Slurm recovery preflight 重新计算 formal baseline/version，并重新构造 combined candidate；不要把并行开发改回全仓串行。
