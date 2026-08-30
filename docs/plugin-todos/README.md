# Per-plugin Long-Term TODO Inboxes

这里是十个中央 Marketplace plugin 的唯一长期 TODO 入口。文件只用于维护，不进入普通用户运行时 plugin payload。

- `workflow-core.md`
- `ai-skills-core.md`
- `writing-style.md`
- `research-writing.md`
- `presentations.md`
- `scientific-visualization.md`
- `web-development.md`
- `statistical-modeling.md`
- `bioinformatics.md`
- `medical-imaging.md`

详细 intake/promotion 规则见：

`docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`

## 谁负责写这里

这里保存的是**中央 plugin 的 canonical TODO**，不是每个真实项目的原始问题清单。

- 真实项目 thread / 项目 Codex：在项目自己的 TODO、review、RESULT 或返修记录里保存原始用户反馈和真实 artifact；可以留下 `AI_Skills feedback handoff`，但不负责最终抽象成中央规则。
- AI_Skills Planner / maintainer：负责读取项目反馈、已有 plugin TODO、active skill/QA/runtime 和其他项目证据，完成去重、抽象、状态判断，然后才写或更新这里。
- Executor：可以提供实现分析，但不拥有 `PROJECT_LOCAL / CANDIDATE_GENERIC / PROMOTE_NOW` 的最终判断权。

写入前必须先检查：

1. active capability 是否已经有同类规则；
2. 本 plugin TODO 是否已有同一问题；
3. 是否只是当前项目的科学内容、页面选择或模板决定；
4. 是否已有第二个独立真实项目提供同类证据。

处理规则：

- active rule 已有但真实输出又失败：按 production regression 处理，不再造一个同义 TODO；
- 已有 TODO：合并新的真实证据，不复制近义项；
- 项目专属：留在项目 repo，不进入这里；
- 新的通用候选：由 Planner 建 `CANDIDATE_GENERIC`；
- 满足 promotion gate：由 Planner 升到 `PROMOTE_NOW`；
- 跨多个 plugin：指定一个 owner plugin，其他文件只引用。

## Item format

建议每条开放项使用：

```text
### <short title>
status: NEW | PROJECT_LOCAL | CANDIDATE_GENERIC | PROMOTE_NOW | BLOCKED_NEEDS_EVIDENCE | PROMOTED | REJECTED | SUPERSEDED
source: <real project / artifact / user feedback / issue>
evidence: <repo path / review / render / result>
target layer: routing | reasoning | rendering | qa | writing | distribution | external-runtime
problem: <what actually failed>
candidate action: <smallest plausible generic change>
promotion gate: <what evidence is still required>
```

不要把详细项目科学事实复制进这里；详细内容留在项目 repo 或 `docs/provenance/`，TODO 只保存可维护的抽象和证据定位。

## Cleanup rule

- `PROMOTED` 项在 release 后可以压缩到“Recently promoted”摘要，不永久堆积实现细节。
- `PROJECT_LOCAL`、`REJECTED`、`SUPERSEDED` 若已在项目记录或历史记录中有完整信息，可从活跃区移到短历史区。
- 不允许为同一问题在多个 plugin TODO 重复维护；跨 plugin 问题指定一个 owner plugin，并在其他文件仅做引用。
