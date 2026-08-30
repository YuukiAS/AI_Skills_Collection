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

## Item format

建议每条开放项使用：

```text
### <short title>
status: NEW | PROJECT_LOCAL | CANDIDATE_GENERIC | PROMOTE_NOW | BLOCKED_NEEDS_EVIDENCE | PROMOTED | REJECTED | SUPERSEDED
source: <real project / artifact / user feedback / issue>
evidence: <repo path / provenance doc / render / review>
target layer: routing | reasoning | rendering | qa | writing | distribution | external-runtime
problem: <what actually failed>
candidate action: <smallest plausible generic change>
promotion gate: <what evidence is still required>
```

不要把详细项目科学事实复制进这里；详细内容留在项目 repo 或 `docs/provenance/`，TODO 只保存可维护的抽象和证据定位。

## Cleanup rule

- `PROMOTED` 项在 release 后可以压缩到“Recently promoted”摘要，不永久堆积实现细节。
- `PROJECT_LOCAL`、`REJECTED`、`SUPERSEDED` 若已在 provenance 有完整记录，可从活跃区移到短历史区。
- 不允许为同一问题在多个 plugin TODO 重复维护；跨 plugin 问题指定一个 owner plugin，并在其他文件仅做引用。
