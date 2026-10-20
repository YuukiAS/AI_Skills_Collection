# Clear Writing 0.6 — approved-execution Kickoff draft v0.1

> **DRAFT ONLY — NOT AUTHORIZED.**
>
> 只有同一独立 Critic 已对本完整 execution-ready package 给出：
>
> ```text
> PASS
> READY_FOR_CODEX=YES
> ```
>
> 且用户在该 PASS 之后明确发送本 Kickoff，才允许执行。否则不得启动 Codex、更新 Personal Plugin、创建 G3 Gate branch 或运行任何真实 Web Gate。

继续 Clear Writing 0.6：

```text
repo = YuukiAS/AI_Skills_Collection
task = clear-writing--single-entry-artifact-finalization
branch = design/clear-writing--single-entry-artifact-finalization
tracking = #13
```

先读取并严格执行当前批准版本：

- `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_1_2026-10-20.md`
- `docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_1_2026-10-20.md`
- `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_1_2026-10-20.md`
- 批准的 Proposal `@3eefc626b86566113125a06fc6046a2bec1eafb2`
- execution-ready Critic PASS 对应的 exact package commit

实施时显式使用：

`workflow-core + ai-skills-core + writing-style`

目标只有一个：让 ChatGPT Personal Plugin 的 Clear Writing 变成唯一 `clear-writing` 入口，同时保持六项 canonical writing capability 和 Codex direct exposure 不变，并用真实 GitHub Reader Guide 证明“聊天回复 + 外部文档”能够分别完成正确路线、写入和回读。

必须遵守：

1. 先完成只读 P0、repo implementation、deterministic parity、known regression、CI 和 implementation review；正式 Personal Plugin 在 final candidate 冻结前不得修改。
2. final candidate 冻结后，只能更新现有 USER/PRIVATE `writing-style` identity；不得创建第二个同名 plugin。
3. update 必须使用当前 release ID 并执行 Plan 冻结的 exact `delete_paths`；旧六个顶层 Skill 文件不得残留。
4. 0.6 external-finalization 正式 claim 只覆盖 GitHub UTF-8 repository text file；不得外推到 Drive、本地文件或其他 surface。
5. G1-G6 严格按 Runbook。Web task 一个输出，只有无模型输出的基础设施失败可同输入重试一次。
6. G3 必须用真实 ChatGPT Web + explicit Clear Writing + GitHub connector 完成 Reader Guide 全文 read -> candidate -> write -> readback。helper/Codex 脚本不能替代。
7. G3 FAIL 立即停止 0.6 release path；不得继续给 Skill 堆同义规则，不得自行新增 MCP/App。
8. G6 只在 G1-G5 PASS 后，由同一独立 Critic冻结 exactly one fresh source；失败不换题、不追加样本。
9. candidate-defining source 变化会使旧 Gate evidence 失效。
10. 0.6 成功不自动关闭 Issue #13 的 statistical-modeling / scientific-visualization downstream adaptation。
11. release closure 时 `writing-style 0.5 -> 0.6` exactly once，repository 只做 execution-time late-bound PATCH；其他 central plugins NO_BUMP。
12. README 必须检查；若无变化记录 `README checked: no update required`；若修改则真实调用 Clear Writing 审校。

任何 architecture、surface claim、MCP/App、权限或 Gate 语义需要改变时：

`STOP -> Planner -> independent Critic`

不得由 Executor 自己决定。

完成每个阶段只记录真实证据，不把 tests、hash、receipt、Skill load 自述或聊天回复质量冒充最终 artifact PASS。
