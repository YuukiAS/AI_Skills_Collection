# Positive example: compressing a long technical audit into a human decision

Date: 2026-10-31  
Route: Clear Writing / `response-clarity`  
Status: user-confirmed positive example

## Why this example is kept

The raw Karabiner audit was technically correct but exhausting to read: 59 rule groups, 47 enabled groups, 12 disabled groups, 88 manipulators, seven merge batches, repeated exclusion conditions, and several misleading descriptions.

The user did not need another audit table. They needed a human judgment: what the configuration really means, what is worth changing, and what can safely be ignored.

The good response did four things:

1. converted raw counts into a simple model of the real problem;
2. separated reversible cleanup from behavior-changing work;
3. made an actual recommendation instead of hiding behind “cannot prove it will never be needed”;
4. stopped once the user could decide what to do next.

## Good response

会。把这份 3 屏技术报告压成人话，其实结论很简单：

**你现在的 Karabiner 不是“59 个不同需求”，而是大概 24 个真正的功能，被历史配置拆成了 59 组。** 其中 12 组已经关闭，实际上不影响你现在使用；另外 47 组里有 30 组可以安全地并回 7 个大组。也就是说，整理完以后完全可以从 **59 组缩到大约 24 组**，而且不需要改变任何你正在用的快捷键。

最重要的是，审计里“12 个禁用规则 0 个可以直接删除”的结论太保守了。它是在用“我无法证明用户永远不需要”作为标准。但这是 Git 仓库，不是不可恢复的生产数据库。**规则已经禁用，本来就不参与当前行为；删掉也不会改变你现在任何快捷键，而且 Git 历史随时能找回来。**

所以按人的判断：

- **12 个禁用规则全部从当前配置删掉。** 不需要保留所谓“备用规则”。以后真想恢复 Alt+F4、Finder F2 重命名之类，直接从 Git 历史拿回来。
- **47 个正在工作的规则不要删功能，只做整理。** 最值得合并的是 7 批：常用 Windows 编辑快捷键、Notion、Home/End、窗口操作、Edge、Terminal/iTerm、Ctrl+T/B/I 这批 Windows 风格快捷键。
- 描述写错的顺手修正；同一排除列表里重复的 VMware Horizon 条目直接去重。
- 浏览器匹配范围和德语键盘布局分支属于可能改变行为的内容，不要和“纯整理”混在一起；应另行确认。

所以后续整理目标可以概括成一句话：

**59 组 → 删除 12 个禁用历史项 → 合并 30 个碎片规则 → 最终约 24 个清晰的启用规则组；快捷键行为保持不变。**

这说明当前配置值得整理，但不需要重新设计键位。真正的问题是历史垃圾和碎片结构，不是功能本身。

## Reusable lesson

When a long technical audit is correct but hard to use:

1. State the actual shape of the problem before listing evidence.
2. Convert raw counts into a smaller set of human concepts and decisions.
3. Distinguish reversible cleanup from changes that can alter behavior.
4. Include recovery cost in the recommendation. Cheaply recoverable Git history should not be treated like irreversible production data.
5. Make a recommendation when the evidence is sufficient; do not push every low-risk choice back to the user.
6. Preserve only the uncertainty that would materially change behavior.
7. Stop once the user can make the next decision.
