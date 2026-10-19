# ChatGPT Web collaboration regressions — PASS integrity closure plan v0.3

## 目标

在不改写历史的前提下，为 `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md` 追加本轮真实事故与长期关闭机制。

## 要追加的真实证据

### Bridge Kit

设计/执行包多次审查后，用户通过自然追问才发现：

- Notifier 被错误退成每 repo 邮箱配置，而原要求是机器级共享配置；
- Persistent Run 和 Notifier 分别存在，但关键调用链没有真正接通；
- ETA 的安全 UNKNOWN 语义可能被实现成长期永不产生 ETA，导致正向能力名存实亡。

归因：PASS/审查没有稳定绑定完整用户承诺，也没有要求跨组件完整成功链和正向能力实际发生。

### Slurm Workflows

受保护取消检查逻辑存在，但正式 Codex Hook 的 Python/runtime 启动链失败；Hook process failure 没有形成真正阻断，危险底层动作仍可能继续。

归因：组件逻辑存在不能替代正常入口的关键失败链验证；安全承诺必须直接证明边界故障时危险动作不发生。

## 要记录的长期关闭机制

1. Critic 级 PASS 只在 execution-ready 最终审查出现一次。
2. 中间审查使用 PROCEED / REVISE；最终 PASS 不可被窄 handoff prompt 缩小为旧 blocker closure。
3. 首个 Proposal 冻结稳定用户承诺；Capability Gate 要求正向能力、跨组件成功链和风险匹配关键失败链。
4. 每轮 Planner/Critic 回复采用“用户摘要 + 机器交接”两层；用户不读机器块也必须知道本轮发生了什么。
5. 普通实现错误默认 RETURN_TO_CODEX；只有冻结语义变化才回 Planner。
6. 实现后最终评估前安全门继续存在，但不再产生第二个 Critic PASS。

## 不应改变

- 不把上述问题改写成 Bridge Kit 或 workflow-core 的中央职责；
- 不新增 ChatGPT Web 第三人工角色；
- 不新增数据库、watcher、daemon、ledger 或状态机；
- 不删除原十类历史问题。

实施完成后把文件顶部状态更新为：本轮 PASS integrity contract 已实施，待/已完成 Project setting 用户侧应用和最终新鲜场景验证，按真实状态填写。
