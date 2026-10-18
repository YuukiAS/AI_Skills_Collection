# Final Report

## What this task solved

这个任务修复了一个很窄但真实的 Presentations 跨主机兼容性问题：当 GitHub runner 缺少 TeX 和 canonical font resource 时，生成器、validator 与测试对“当前最先阻塞渲染的依赖是什么”理解不一致，导致与 Presentations 无关的全仓 CI 也会失败。

修复后，最小 CI 主机可以如实报告缺失依赖，又不会把“无法真实 render”误当成产品成功。该外部 blocker 已不再阻止 Clear Writing 的 required full CI 继续推进。

## What changed

修改仅落在 Presentations 的三份 shared script、对应 generated mirrors 和 `tests/test_presentations.py`。

生成器现在先确定 TeX engine 是否存在。没有 engine 时，primary compile status 为 `BLOCKED_MISSING_TEX_ENGINE`；字体资源状态仍作为 secondary dependency evidence 保留。存在 engine 但 canonical font bundle 缺失时，仍使用 `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`。

两个 validator 只在显式 `--allow-missing-render` 模式中接受 canonical-font missing 这一环境状态。严格模式没有放宽。

## New capabilities / behavior

在没有完整生产渲染环境的 GitHub runner 或其他 minimal host 上：

- 无 TeX engine 时能稳定得到正确的 primary blocker；
- 有 engine 但缺 canonical font bundle 时能得到独立的 typed resource blocker；
- non-render CI 可以继续检查其余 Presentation contract；
- strict production validation 仍要求真实渲染依赖完整。

这使全仓 CI 不再要求把 GitHub runner 伪装成正式 Presentation render host。

## Deliberately not adopted / unchanged

没有安装或 vendor 私有 canonical font bundle，也没有为了 CI 安装完整生产 TeX stack。

没有删除、skip 或弱化原来的 Presentation 测试；没有把 `BLOCKED_FONT_RESOURCE_TOKEN_MISSING`、unexpected font、missing source 等产品/source defect 加入 allowlist。

没有修改模板、布局、视觉质量、字体策略、renderer resource ownership、routing、profile、README、changelog 或版本。

没有修改 Clear Writing 或 Research Authoring。

Issue #98 的 broader shared Beamer core / two-skin 工作没有启动，也没有被本任务关闭。

## Example usage

在 GitHub-hosted runner 上缺少 TeX 时，生成器现在报告 `BLOCKED_MISSING_TEX_ENGINE`；CI 使用显式 `--allow-missing-render` 仍可验证 source、layout、quality-loop 等非像素合同。

在安装了 TeX 但没有 canonical font resource 的机器上，生成器报告 `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`；non-render validator 可以识别这是环境资源缺失，但 strict validator 仍拒绝把它当成真实 render PASS。

如果模板里的 font-resource token 本身损坏，仍然失败，不能借 `--allow-missing-render` 绕过。

## Regression and remaining limitations

独立 Reviewer 实际核对了真实实现 diff、冻结 Plan、Executor RESULT 和 GitHub CI。

当前 final candidate 证据：

- focused dependency-state + 原 CI failure regressions：`6 / 6 PASS`；
- Presentations tests：`48 / 48 PASS`；
- full repository tests：GitHub runner `344 / 344 PASS`；
- source/generated script parity：PASS；
- Marketplace write/validate/check/path-report：PASS；
- second clean/idempotent Marketplace check：PASS；
- skills validate/audit 与 generated-file cleanliness：PASS；
- `git diff --check`：PASS；
- GitHub Actions run `39108825156` 四个 job 全部 PASS。

CI runner 没有安装项目私有 canonical font resources 或完整 TeX production stack，因此该 PASS 直接验证了本任务要修的 portability contract。

剩余限制：本任务不验证真实 deck 的视觉质量，也不代表 Presentations release readiness。下一步只应把这个 exact repair 合法集成到 `main`，再由 Clear Writing successor 消费并重跑其 required full CI。

## Technical appendix

- Task: `presentations--ci-missing-render-contract-repair`
- Reviewed branch: `reviewed/presentations--ci-missing-render-contract-repair`
- Base commit: `38a76797439c6b29098aade7539270cbc51e8836`
- Implementation commit: `bb74e18f44428a12f1fea11b98bf30c10af94040`
- CI handoff commit: `e89b0fffffd9d8c65472d5d017dd56a0adf74ccd`
- Reviewer handoff head: `2ae3b517081983d9577a6efc87249d15c9c0645d`
- GitHub CI: `39108825156`
- Reviewer decision: `PASS`
- Review artifact: `results/presentations--ci-missing-render-contract-repair/REVIEW_1.md`
- Result artifact: `results/presentations--ci-missing-render-contract-repair/RESULT.md`
- Maximum claim: Presentations missing-render portability regression repaired; broader Presentations work and Clear Writing product acceptance remain separate.
