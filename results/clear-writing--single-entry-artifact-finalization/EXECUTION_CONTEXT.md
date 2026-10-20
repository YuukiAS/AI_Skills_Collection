# Clear Writing 0.6 本地实施定位

task: `clear-writing--single-entry-artifact-finalization`
branch: `design/clear-writing--single-entry-artifact-finalization`
approved proposal: `3eefc626b86566113125a06fc6046a2bec1eafb2`
approved execution package: `d7b810d194ead881303aaca9c2e4f1d59a97c1f1`
starting branch commit: `821bf2334173fcb0fcb1ad956125c3b4b970826f`
tracking: #13

按当前用户的恢复指令，Codex 缺少 Plugin Creator 工具不阻塞本地 implementation。
Runbook Phase A/B 在本任务分支执行；当前账户的 Plugin Creator P0 回读、正式
Personal Plugin 更新及 G1-G6 仍由 Phase C/D 指定的 ChatGPT Web / Planner / 独立
Critic 消费真实工具和完整产物完成。本地缓存和回放不冒充账户回读或真实 Web Gate。

本轮只准备候选，正式 `release` 仍是
`fd79c4be54fc50bd66d9a51bbc1e681f361f6a77`（repository 5.5.1 / writing-style 0.5）。
分支配置中的 writing-style 0.6、Personal wrapper 0.6.0 及 changelog 均为候选身份；
只有 required Gates 与最终完整产物审查通过后才走正式发布收口。

Repository bump decision: NONE (implementation candidate)
Reason: repository PATCH 在 required Gates 通过后按当时 origin/release 后绑定。
Affected plugins:
- writing-style: 0.6 candidate only; formal 0.5 unchanged
- all other central plugins: NO_BUMP

六项专业 Skill 正文及 profile 保持不变。新代码仅拥有 wrapper 编排、确定性投影、
打包/校验与批准的 forward-restore 集合，不复制第二套专业写作规则。
