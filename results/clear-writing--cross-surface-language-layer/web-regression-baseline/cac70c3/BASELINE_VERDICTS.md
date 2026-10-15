# RW-WEB-01..05 基线回放判定

- 候选提交：`cac70c3bfcce6aeeba9c3e80adfa317235b54ee9`
- 运行时：`codex-cli 0.153.4`
- 临时插件：`writing-style@ai-skills-candidate`，版本 `0.4`
- 回归库：`results/clear-writing--cross-surface-language-layer/REAL_WEB_REGRESSION_BANK_V1.md`
- fixture：`results/clear-writing--cross-surface-language-layer/web-regression-fixtures/v1/`
- 结论：4 项通过，1 项失败；现有实现仍需针对 RW-WEB-05 暴露的通用缺口做最小修复。

这些是公开安全的派生案例，不含私有 ChatGPT Web 对话。基线只证明固定 Codex 候选在这些已知案例上的表现，不证明 ChatGPT Web 自动触发、G7 未见样本或正式发布质量。

基线冻结前检查了任务文字，删除了 RW-WEB-01、02、04、05 中直接泄露判定标准的指令。下列运行才是本包的权威基线；更早的 fixture 校准运行不作为证据。

## 运行凭据

| 案例 | 本地运行目录 | 实际消费 | 子进程错误输出 |
| --- | --- | --- | --- |
| RW-WEB-01 | `20261015T080444Z-3308178` | `response-clarity` | 空 |
| RW-WEB-02 | `20261015T080525Z-3313287` | `response-clarity` | 空 |
| RW-WEB-03 | `20261015T080020Z-3290290` | `response-clarity`、`chinese-prose` | 空 |
| RW-WEB-04 | `20261015T080618Z-3314125` | `response-clarity`、`chinese-prose` | 空 |
| RW-WEB-05 | `20261015T080705Z-3316807` | `response-clarity`、`chinese-prose` | 空 |

每次运行的 `run.json` 均记录 `actual_consumption.proven=true`、候选提交、临时插件身份和固定运行时。原始 JSONL 与运行工作区保留在忽略目录 `.local-runtime/candidate-plugin-replay/runs/`，不提交到仓库；完整读者输出已逐案保存于本目录。

## 逐例判定

### RW-WEB-01：PASS

第一句直接说明尚不能交付及原因，随后区分维护者的下一步和用户无需立即操作的事实。命令与 `release_status=WAITING_FOR_RESTORE_CHECK` 得到保留，后续段落没有反复改写同一边界。

### RW-WEB-02：PASS

答复定位了具体问题句，说明推荐从 A 改到 B 缺少新证据，并给出保留不确定性的替代写法。没有把写作反馈改写成对用户心理的猜测或长篇自我检讨。

### RW-WEB-03：PASS

答复保留了水龙头类比、两个不同场景的因果解释，以及旧版本兼容性和恢复能力仍未验证的不确定性。篇幅服务于必要解释，没有把“清晰”机械化为短答。

### RW-WEB-04：PASS

简单线性流程使用普通段落说明，没有箭头图、代码框或内部模块清单。完成条件 `READY` 清楚可见，内部名称没有暴露给读者。

### RW-WEB-05：FAIL

答复正确概括了三份来源的共识、差异和证据限制，也在结尾说明试行安排属于助手建议。但核心问题已经回答后，仍自动展开了较完整的试行范围、指标、对照条件、复盘和扩展标准；用户没有要求实验或实施设计，这些段落超出了当前问题所需的信息增量。

此外，开头先给出“小范围试行”的助手建议，再说明来源共同支持什么，使来源结论与额外建议的层次仍不够稳定。这里的失败依据是信息停止条件和归因分层，不是固定长度、表格数量或某个词是否出现。

## 允许的后续修复边界

本基线只支持在现有 `response-clarity` 中补强两项通用行为：

1. 用户的问题已经回答后，除非后文增加新证据、必要决策或用户要求的实施细节，否则停止；
2. 先说明来源已经支持的共识与差异，再单独标明助手的额外建议，并让建议深度匹配用户请求。

RW-WEB-01..04 已通过，不得为制造改动而重写其对应行为。RW-WEB-03 的例子、因果解释和不确定性必须继续保留。
