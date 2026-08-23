---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 018_presentation_external_method_audit
review_round: 1
decision: REVISE
implementation_commit: 6613d13d81149fbfa2af438ac72d47b7c4429bf6
---

# GPT Review

## Decision

`REVISE`。

018 的总体判断和下一步方向基本成立：当前主要瓶颈确实不是继续增加抽象审美规则，而是缺少把 inspected reference page 转成可执行构图约束的 composition representation；报告也正确把 multi-candidate search、comparative Terra、native PPTX geometry 和 real holdout 放在后续阶段，没有越权提前实现。真实 CI 已成功，且本任务没有修改 active Presentation skill、renderer、Terra、reference corpus 或 plugin exposure。

但冻结 Plan 对 `brycewang-stanford/many-ppt-skills` 有一个明确的证据要求尚未满足：必须检查 `principles/` 中 **8 条原则的原文依据**。当前主报告与 structured matrix 的 `files_actually_inspected` 只记录了：

- `principles/07-render-and-look.md`
- `principles/08-distill-dont-design.md`

并没有记录或证明实际检查：

- `principles/01-show-dont-tell.md`
- `principles/02-anti-ai-slop.md`
- `principles/03-fixed-stage.md`
- `principles/04-constraint-beats-freedom.md`
- `principles/05-progressive-disclosure.md`
- `principles/06-single-file.md`

这不是文案完整性问题，而是冻结 evidence requirement 未闭合。报告目前又使用了 show-don't-tell、anti-slop、constraint 等结论，因此必须补上原文检查，而不能依赖 README、二手总结或先验知识。

## Evidence reviewed

### CI

当前 handoff tip `b055089f135c9c6b1c9d28766f1d265adf4a180c` 的 `reviewed-handoff/ci-summary` 为 `success`，CI locator 指向 GitHub Actions run `32619131986`。

### Audit artifacts

已独立检查：

- `docs/audits/RESEARCH_PRESENTATION_EXTERNAL_METHOD_AUDIT.md`
- `docs/audits/research_presentation_external_method_matrix.json`
- `results/018_presentation_external_method_audit/RESULT.md`
- 冻结 `PLAN.md`

其余主要来源均满足“不是 README-only”的最低证据形态：`frontend-slides`、`high-quality-slides`、`slideweaver`、`manuscript-to-editable-slides`、`academic-paper-image-ppt` 和 `ppt-master` 都记录了实际 skill / layout / renderer / QA 文件；科学汇报指导源也记录了访问与复用边界。当前没有发现未经授权 vendor、复制外部 binary/template 或扩大 active skill 范围的问题。

## Blocking finding

### F-018-01 — `many-ppt-skills` 八条原则的原文审计不完整

**冻结依据**：018 PLAN 的 external audit set 明确要求检查 `many-ppt-skills` 的 registry/comparison method 和 `principles/` 中 8 条原则的原文依据；Evidence requirements 也要求核心项目实际检查多个实现/原则文件。

**观察证据**：matrix 的 `files_actually_inspected` 只列出 principle 07 和 08；主报告对应 source audit 同样只列这两篇。

**为什么阻断**：本任务的目的正是避免凭空写规则。若对最关键的 show-don't-tell、anti-slop、fixed-stage、constraint、progressive-disclosure、single-file 六项没有实际原文审计记录，就不能声称这一来源满足冻结 evidence contract，也不能用它支撑后续架构取舍。

**最小修复**：

1. 实际读取 `principles/01` 至 `principles/06`；
2. 在主报告中补充必要的、与本仓库架构决策直接相关的原文机制核对，不需要把八篇全文重新摘要；
3. 更新 structured matrix 的 `files_actually_inspected`，确保八篇 principles 都真实列出；
4. 若原文检查改变了当前判断，才同步修正机制/复用边界/019 推荐；如果不改变，明确说明结论经八篇原文复核后保持不变；
5. 重新运行本任务原有 validation / CI handoff。

不得借本次返修修改 active Presentation skill、visual QA、renderer、Terra、reference corpus，也不得提前实现 019。

## Non-blocking assessment

当前推荐的 019 方向——`exemplar composition representation`——在现有审计证据下仍是合理候选，不要求因为本次 finding 改方向。返修目标只是把冻结的外部证据链补完整，然后再进行第二次独立审核。
