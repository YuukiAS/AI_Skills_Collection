# Slurm Workflows — Parallel Release / Integration Recovery Plan

日期：2026-10-02  
角色：Planner  
任务：`hpc--slurm-workflows-routing-refactor`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
Reviewed branch：`reviewed/hpc--slurm-workflows-routing-refactor`  
既有 worktree：`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

## 结论

这次不是 Slurm implementation failure，而是两个并行 release 在同一个 repository 的 shared release surfaces 上相撞。

当前事实：

- Slurm R4 repair 已经在远端 reviewed branch 完成：
  - product candidate：`d9da1dde5731f27f029dc1507a457a39b510d610`
  - branch handoff tip：`97f53a14abe24e2fc1813b8003a9162d815c2c94`
- 当前 `main` / `release` 已前进到：
  - `4ce1946ba047ea200c4ab41ae824de999ef535ed`
  - Repository `5.4.1`
  - `workflow-core 0.5`
- latest main 的 workflow-core release 没有修改 Slurm production source / Slurm tests。
- 当前本地 Slurm worktree 的 merge conflict 是旧 reviewed branch release metadata 与新的 workflow-core release metadata 冲突，不是 Slurm calendar/capacity semantic conflict。
- 冲突文件：
  - `CHANGELOG.md`
  - `docs/SKILL_CATALOG.md`
  - `registry.json`
  - `tests/test_candidate_plugin_replay.py`

因此不要让其他 plugin 停下来等 Slurm，也不要让 Slurm 丢掉已完成的 R4 repair。并行开发继续；只在最后 integration / release closure 短暂串行化 shared repository release state。

## 版本重算

旧 Slurm repair package 曾把 Repository target 写成 `5.4.1`。这个绝对版本现在已经被并行完成的 workflow-core release 占用。

Slurm 已批准设计早已冻结的版本原则是：

```text
repository: next PATCH from actual release-time VERSION
```

当前正式 release 已是 `5.4.1`，所以如果 Slurm 是下一个 release：

```text
Repository: 5.4.1 -> 5.4.2
slurm-workflows: 0.2 -> 0.3
workflow-core: stays 0.5
other central Plugins: NO_BUMP
Bridge Kit: NO CHANGE
```

这里改变的是 late-bound repository release number，不是 Slurm product architecture 或 standalone skill version。

## 当前 conflicted worktree 的恢复

不要在当前冲突状态继续实现或逐文件猜 merge。

恢复顺序：

1. 确认当前冲突确实来自这次未完成的 `origin/main` merge，且冲突后没有新的 task-owned implementation edit。
2. `git merge --abort`，回到 merge 前 clean Slurm reviewed state。
3. fetch reviewed remote。
4. fast-forward 当前 reviewed branch/worktree 到：
   `origin/reviewed/hpc--slurm-workflows-routing-refactor`
   当前预期 remote tip：
   `97f53a14abe24e2fc1813b8003a9162d815c2c94`
5. 验证远端已包含：
   - product candidate `d9da1dde5731f27f029dc1507a457a39b510d610`
   - R4 fold/gap repair
   - updated RESULT / Clear Writing tracking artifacts。

若 remote tip 已再次变化，先读取新 tip，不 reset/force。

## 与 latest main 的 integration 规则

恢复 clean branch 后，再做一次 latest-main integration candidate。这里允许 ordinary non-force merge，但 conflict resolution 不按“ours/theirs 全选”，而按 ownership 解决。

### Task-owned Slurm semantic files

Slurm candidate 保留其已经通过 R4 gates 的 source/test semantics：

- `skills/tools/hpc/slurm-workflows/**`
- `tests/test_slurm_workflows.py`
- standalone Slurm version expectation `0.3`
- task result/tracking evidence

如果 latest main 在这些文件出现新 substantive change，则停止并返回 Planner/Critic；当前已确认没有。

### Main-owned unrelated plugin state

workflow-core 已正式 release 的状态必须保留：

- `workflow-core 0.5`
- 其 source/generated payload
- 其 release evidence
- current main 的 unrelated tests / fixes

Slurm integration 不得把 workflow-core 降回 `0.4`。

### Shared release / generated surfaces

这些文件不得用某一 side 整体覆盖：

- `VERSION`
- `README.md`
- `CHANGELOG.md`
- `registry.json`
- `docs/SKILL_CATALOG.md`
- 其他由 generator 管理的 repository-wide metadata

正确做法是从 latest main truth + Slurm release delta 重新计算：

- Repository = `5.4.2`
- README 保留 `workflow-core 0.5`，同时显示 `slurm-workflows 0.3`
- CHANGELOG 保留现有 `5.4.1` workflow-core release 原样，并新增 `5.4.2` Slurm patch entry；不能把两个不同 release 都写成 5.4.1
- generated registry/catalog 使用正常 generator 从 combined source 重建，不手工拼 JSON/生成文件

### `tests/test_candidate_plugin_replay.py`

该文件不属于 Slurm product semantics。Slurm branch 历史上只做过一个 timing-robust 调整，而 current main 已有更新后的 timeout 行为。

冲突解决以 latest main 为准；不要为了 Slurm release 恢复旧的 branch-only timeout 值。之后完整 suite 重新验证 combined candidate。

## Final integration candidate

latest main + Slurm task-owned delta + late-bound 5.4.2 release metadata 合并后，必须重新运行：

- PF5/G8
- 完整 G1-G8
- `tests.test_skill_update`
- repository validate / audit
- generated Marketplace parity
- full unittest suite
- version / README / changelog / generated consistency
- relevant install/normal-entry smoke

然后冻结一个新的 exact combined candidate。旧 `d9da1dde...` 继续作为已验证 Slurm semantic candidate/provenance，但不能冒充最终 5.4.2 integration candidate。

Issue #95 继续 `DOING`，通过 Clear Writing 把 anchor 更新到 combined candidate。

## 并行开发长期规则建议

本次冲突暴露的是 AI_Skills repo workflow 缺口，不是 Bridge Kit 问题。

建议后续对 AI_Skills governance 做一个很小的 reviewed amendment：

1. 多个 reviewed plugin/skill task 继续各自在独立 branch 并行，不因为另一个 release 等待而停止。
2. implementation / Critic 阶段只做 **relevant semantic drift check**；latest main 只修改无关 plugin 或 shared release metadata 时，不强制每轮把 main merge 进 task branch。
3. Repository release **冻结 release class，不冻结绝对 version number**；绝对版本在 integration/release preflight 按当时正式 `VERSION` 计算。
4. root VERSION / root CHANGELOG / README dashboard / registry/catalog/generated parity 属于 **late-bound integration surfaces**。
5. 最终 integration 仍必须短暂串行，因为 `main` / `release` 是单一线性 history；这不影响前面的多个 plugin 同时开发、测试、Critic。
6. shared generated files 冲突时优先重生 combined output，而不是人工 ours/theirs。
7. unrelated plugin tests/conflict 默认采用 current main；task 只保留自己明确拥有且有证据的改动。

这个 amendment 应落在 AI_Skills_Collection 的 AGENTS / version-release workflow；不改 Bridge Kit，不新增 queue、lock service、daemon、registry 或 state machine。
