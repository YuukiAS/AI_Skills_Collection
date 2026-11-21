# 回归候选与待补实现（2026-11-21，待用户裁决）

来源：GPT 对四个插件 TODO 的全量复核；Claude 已核对其中的事实断言。现有 11 条全部保留。

## 新增回归候选（9 条）

| 插件 | 案例 | 测什么 | 素材 |
| --- | --- | --- | --- |
| Reasoned Decision | `state-owner-before-reset` | 先找真实状态持有者和最小可逆修复，再考虑卸载、重启、升级、重置 | Tailscale 克隆身份、macOS 字形错乱 |
| Reasoned Decision | `whole-goal-multi-entry` | 守住整体体验目标，列出各入口应有行为；不因最新症状换整套方案 | UU Remote / Karabiner |
| Reasoned Decision | `completed-task-stop` | 已成功的能力不重新发现，已完成步骤不重开，到达用户终点就停 | Asteria 打开 / Project setting 收尾 |
| Content Selection | `release-reader-verification` | 删内部状态、manifest、生命周期，同时保住用户真正要核对的 Project 和配置面（防删过头） | AI Instructions Release 反复改坏 |
| Content Selection | `project-atlas-content-admission` | UI 载体：多余文字、内部状态、重复说明在首次交付前被挡住，删后布局重新平衡 | Project Atlas 真实 UI |
| Clear Writing | `direct-answer-next-step` | 只问下一步时，第一段直接给动作和原因，不写成小型方案书 | TODO 中真实案例 |
| Clear Writing | `multi-source-synthesis` | 两路结果替读者完成比较和收敛，不按"A 说、B 说"复述 | 两路 Pro 结果 |
| Research Authoring | `github-markdown-direct-publish` | GPT 自己按 GitHub 写法写 Markdown（行内/独立数学、表格、链接、代码），直接推送到指定 repo/branch/path 并打开远端页面回读 | 新建 |
| Research Authoring | `scientific-revision-preserves-correct-content` | 修正方法身份、比较资格、错误解释，同时保住旧版正确的公式、机制、因果链和表格 | CAT-TRACE 12 页→7 页→终版 |

缺素材的两条学生案例不删；找不到原件时换同类、可访问的 STAT5060 已接受材料。

## 已核实的实现缺口（不只是缺测试）

1. **论坛检索没有写硬。** TODO 两次记录用户要提醒才去查论坛（2026-11-05 微信、2026-11-10 Edge），但 `solution-design` SD-02 只写"按需检查……高价值社区经验"，没有要求必查，也没有点名任何社区。结果是模型默认只查官方文档、arXiv。
2. **Research Authoring 没有 GPT 直接推送 GitHub Markdown 的路径。** 三个技能都写成"需要发布就填 handoff 交 Codex"；`check_research_artifact.py` 的 `math_rendering` 和 `target_page` 直接返回"未观察"。测试会全绿，但 GPT 仍可能推上错误的数学写法，或者根本不自己推。
