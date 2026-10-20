# Clear Writing 0.6 — Phase C archive compatibility bounded repair

你继续执行 **同一个** Clear Writing 0.6 task，不新建任务、不重新设计产品。

```text
repo = YuukiAS/AI_Skills_Collection
branch = design/clear-writing--single-entry-artifact-finalization
task = clear-writing--single-entry-artifact-finalization
approved_execution_package = d7b810d194ead881303aaca9c2e4f1d59a97c1f1
frozen_candidate = 079bd7987bb33d624d244feb415327d5cf2343d8
phase_c_stop_evidence = 38a81dc1df9a362ecee4be597cb3db5bd6fcac41
```

先读取最新 main 的 AGENTS / workflow rules，并读取本任务：

- `results/clear-writing--single-entry-artifact-finalization/phase-c/ROOT_CAUSE_AND_RECOVERY_ANALYSIS.md`
- `docs/design/clear-writing/CLEAR_WRITING_0_6_PHASE_C_EXECUTION_RECOVERY_AMENDMENT_V0_1_2026-10-20.md`
- 原批准 Plan / Runbook v0.2
- `scripts/build_clear_writing_chatgpt_wrapper.py`
- `tests/test_clear_writing_chatgpt_wrapper.py`

显式使用：

`workflow-core + ai-skills-core + writing-style`

## 唯一实现目标

修复已经冻结的 `prepare-restore` archive input compatibility：

真实 Plugin Creator `get_owned_plugin_archive` 当前导出 0.5.0 为 `current.tar.gz` / `application/gzip`，而当前 builder 只用 `zipfile.ZipFile` 读取 baseline。

这属于同一冻结任务内普通实现 bug。不要修改产品架构、wrapper内容、六条 route、manifest语义、Gate、版本方向或 Phase C live state。

## 必须修改

1. 将当前 `read_zip` / `prepare-restore` 输入读取改为一个安全 archive reader，至少正式支持：
   - ZIP；
   - gzip-compressed tar (`.tar.gz` / `.tgz`)。
2. tar reader 必须 fail closed：
   - 拒绝 absolute path / `..` traversal；
   - 拒绝 symlink / hardlink / device / fifo；
   - 拒绝 duplicate file paths；
   - 目录项可以安全忽略，但不得让目录项进入 plugin file set；
   - 所有最终 file path 继续经过现有 exact safe-path contract；
   - 非 ZIP / 非 gzip tar 输入失败。
3. `prepare-restore` 对真实 0.5 baseline 的 frozen file-set contract保持不变：
   - version = 0.5.0；
   - 无 root `plugin.json`；
   - 27-file legacy set；
   - six original top-level Skills。
4. forward restore 0.6.1语义、`RESTORE_06_ONLY_PATHS.json`、`RESTORE_DELETE_PATHS.json`算法不得改变。

## 测试

至少新增/修改测试证明：

- baseline ZIP仍可用；
-等价 baseline tar.gz可用；
- tar.gz内目录项不进入payload；
- tar traversal失败；
- tar symlink失败；
- tar hardlink失败；
- tar duplicate path失败；
- unexpected file-set仍fail closed；
- restore结果对 ZIP与tar.gz baseline完全等价。

不要用只改扩展名的假 tar.gz。

## 候选不允许漂移

本修复不应改变 0.6 Personal Plugin payload。

修复后重新 build frozen wrapper，必须证明 exact raw ZIP：

```text
size = 170866 bytes
SHA-256 = e4c451841583cb6e1ae4212f8d8559b93ef4272f66d687d3f6762f6114a73dc6
```

若 ZIP bytes/hash发生任何变化：

`STOP -> Planner`

不得自行接受新 candidate。

因为 wrapper payload必须 byte-identical，原13组语言 known-regression输出不 reroll；保留原 evidence并明确说明复用依据。

## 验证与审查

只做这次普通实现修复所需验证：

- `tests/test_clear_writing_chatgpt_wrapper.py`；
- 与 archive安全/restore直接相关测试；
- required repository CI；
- `git diff --check`。

不要重跑 G1-G6，不更新 Personal Plugin，不创建G3 branch，不调用付费模型。

修复后交原 independent implementation Reviewer，重点核对：

1. tar.gz是真支持，不是扩展名绕过；
2. archive安全边界；
3. restore语义未变；
4. 0.6 wrapper ZIP bytes/hash完全不变。

Reviewer PASS 后：

- 形成新的 implementation/source commit identity；
- 更新 `FINAL_CANDIDATE.json` 中 source commit / evidence identity，但 wrapper archive SHA保持原值；
- 生成新的 `PHASE_C_HANDOFF.md`，明确 archive-format bug已修，**archive byte materialization和fresh Web execution责任仍等待 Planner/Critic按 amendment闭合**。

不要实施 Phase C live mutation。

最终只报告：

```text
ARCHIVE_COMPAT_REPAIR=PASS|FAIL
WRAPPER_ZIP_SHA256=<sha>
WRAPPER_BYTES_UNCHANGED=YES|NO
IMPLEMENTATION_REVIEW=PASS|REVISE
NEW_IMPLEMENTATION_HEAD=<sha>
NEXT_HANDOFF=PLANNER
```
