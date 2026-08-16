# Reviewed Handoff Request — 001_research_writing

## Objective

根据已经通过 GPT Reviewer 的现有技能库能力与调用审计，先整理“科研论文写作 + 文献检索/引用”这一批高频能力的调用边界，使技能安装后可以根据用户自然语言稳定进入正确能力；本任务不扩大到全库，不新增外部资源。

## User-provided inputs

- `docs/audits/ACTIVE_SKILL_CAPABILITY_MAP.md`
- `docs/audits/ACTIVE_SKILL_CALLING_AUDIT.md`
- `docs/audits/ACTIVE_SKILL_CALLING_AUDIT.json`
- 当前 `research-writing` marketplace aggregate 与相关 source skills。

## User constraints

- 本轮先理顺现有库，再处理 Notion 新候选。
- GPT Planner 决定技能边界、入口和自然语言调用契约；Codex Executor 不得自行改变这些语义。
- 不新增顶级 plugin，不新增外部 skill，不删除或停用现有 skill；若后续仍确认需要合并/删除，另开独立 Reviewed Handoff task。
- 不处理 Notion `AI Resources > Skills Collection`，也不处理 `Type=Research` 候选。
- 不改 branch 拓扑；使用当前已授权 `main`。
- 用户不需要再次参与，除非工作流进入 `AWAIT_HUMAN_DECISION` 或 `BLOCKED`。
