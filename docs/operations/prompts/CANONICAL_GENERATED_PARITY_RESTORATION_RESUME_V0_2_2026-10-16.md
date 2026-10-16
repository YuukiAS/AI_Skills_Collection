继续当前 `work/repo--canonical-generated-parity-restoration`，不要重开任务，也不要丢掉现在工作树里已经完成但尚未提交的 source/config 修复。

先执行：
`git fetch origin`

然后读取远端最新 Planner amendment：
`docs/design/source-authority/CANONICAL_GENERATED_PARITY_RESTORATION_AMENDMENT_V0_2_2026-10-16.md`

当前远端该 amendment 已提交；如果本地分支仍停在旧 head，优先普通 fast-forward 当前同名远端分支。若 dirty worktree 会被覆盖，立即停止，不要 reset/clean/stash 丢数据；保留现有工作并报告冲突路径。

这次不要把 4 个 full-test failure 当成同一类问题：

1. Presentations 的 `accepted_element_ledger` 失败：
   - 不改/删这个测试；
   - 它证明 v0.1 的“generated wrapper 全字节不变”约束对 wrapper 过严；
   - canonical research-presentation source 里已有 `accepted_element_ledger`，必须保留；
   - 当前 generated wrapper 里 October 6–7 新增的 runbook / cumulative acceptance / anti-shortcut / independent validation / monotone convergence 也必须全部保留；
   - 正确做法是把两边已接受语义合并回 canonical source，再重新生成；
   - generated `skills/research/SKILL.md` 允许因此变化，但只能恢复 source 已有 guard，不能丢任何 generated-only hardening；
   - business wrapper 同理：source 语义全部保留，并吸收 generated-only hardening；若 byte 无需变化则不强行改。

2. `VERSION == 5.5.0` 失败：
   - 不改 `VERSION`；
   - 删除 `tests/test_central_plugin_icon_assets.py` 中与该 icon/plugin-version test 无关的硬编码 repository version 断言；
   - repository release/version 一致性继续由现有专门 version tests 负责。

3. `docs/plugin-todos/*.md` 两个失败：
   - 不删除任何合法 workflow/domain TODO；
   - `test_central_plugins_have_exactly_one_source_only_todo_inbox` 改为：十个 central plugin 各自必须存在对应 canonical TODO 文件，但允许目录中额外存在 workflow/domain-specific notes；
   - `test_plugin_changelogs_match_marketplace_set_and_versions` 继续要求 changelog 集合精确等于 central plugins，但 TODO 只要求 central plugins 是 todo_names 的子集。

完成这些修改后重新验证：
- focused Presentations / Marketplace tests；
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report`；
- 再跑一次 generator check，必须 idempotent clean；
- 对照 pre-repair generated snapshot：除 Presentations wrapper SKILL 文件按 amendment 允许的语义恢复外，其余 pre-existing generated files 必须保持 byte-identical；Research Writing generated tree 必须 byte-identical；
- full repository unit tests；
- `git diff --check`。

如果这 4 个已知 failure 全部关闭且没有新的语义 blocker，就按原 v0.1 授权继续：commit + push repair branch；若 main 已前进，普通 non-force merge latest main 后重跑关键验证；然后普通 non-force 集成回 main；不要移动 release。

不要修改 `reviewed/clear-writing--cross-surface-language-layer` 的 PLAN/CURRENT。不要扩大到新的 Presentations / Research Authoring 设计。

最后只回报：final main commit、这 4 个 failure 是否全部关闭、generator/full tests 是否 PASS、是否还剩 blocker。