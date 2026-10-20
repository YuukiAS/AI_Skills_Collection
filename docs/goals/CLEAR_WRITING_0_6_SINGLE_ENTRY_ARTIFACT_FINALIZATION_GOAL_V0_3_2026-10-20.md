# Goal：Clear Writing 0.6 单入口、最终产物绑定与聊天内容选择 v0.3

日期：2026-10-20  
状态：DRAFT_PENDING_EXECUTION_READY_CRITIC  
任务：`clear-writing--single-entry-artifact-finalization`  
仓库：`YuukiAS/AI_Skills_Collection`  
分支：`design/clear-writing--single-entry-artifact-finalization`  
跟踪：Issue `#13`

## 用户结果

完成后的0.6必须让用户在 ChatGPT 中只选择一次 **Clear Writing**，然后：

1. 普通聊天先按当前问题决定“用户真正需要读什么”，再组织表达；领域分析可以很深，但内部证据不自动全部进入正文。
2. 复杂产品完成汇报必须详细说明完成状态、主要机制、正常使用、可信依据、真实限制和剩余项，但不再把审计过程、被否决架构和重复内部实现清单倾倒给用户。
3. 受阻/交接报告必须直接说明发生了什么、下一责任方、用户是否需要操作；需要 handoff 时直接给完整可复制 prompt。
4. 真正需要算法、数学、工程细节时，仍完整保留公式、推导、条件、参数、复现信息和重要限制；“清晰”不能退化成“删短”。
5. 正式中文文档、长技术重写、英文科研、UI文案、exact-only/mixed等0.6既有路线保持。
6. GitHub UTF-8外部文档仍只有 full read -> final candidate -> expected-blob write -> matching readback 才能声称finalized。
7. 六项 canonical writing capability和Codex direct exposure保持，不把Clear Writing变成领域判断owner。
8. 0.6仍是skills-only plugin，不声称拥有不可绕过发送前Hook。

## CHAT_RESPONSE 新机制

唯一入口实现：

`CHAT_RESPONSE_READER_VALUE_SELECTION_V1`

进入正文的内容必须至少满足一项：

-直接回答当前问题；
-理解主要机制/正常使用所必需；
-改变完成、可信度或风险判断；
-保存重要限制/不确定性/权限边界；
-支持用户行动/复现/交接；
-用户明确要求深入解释。

随后才交给 `response-clarity` 和必要的 `writing-fidelity`。

没有固定字数、标题数、英文比例或禁词。

## 当前候选关系

`079bd7987bb33d624d244feb415327d5cf2343d8` 保留为历史实现基线，但因缺少新 CHAT_RESPONSE 语义，不再是新版0.6 release candidate。

正式 Personal Plugin继续保持0.5.0，直到新版candidate、restore路径和真实Web Gate前置全部就绪。

## 同任务额外必须关闭

- `prepare-restore` 必须安全支持真实 Plugin Creator ZIP/tar.gz archive；
- Phase C不再假设一个Planner surface同时能materialize archive并自动控制fresh Web chat；
- live mutation owner与fresh Web gate owner可拆分，但必须绑定同一个candidate/release并保留同一restore owner。

## 验收

继续 `CW06-G1..G6`，不新增顶层 Gate。

G2中：

- T1 = Bridge Kit 0.11.1 complex completion report known regression；
- T9 = Phase C blocked handoff known regression；
- T8 = necessary-long-answer depth protection；
-其他路线覆盖保持。

Bridge/Phase C都是已见样本，不能冒充fresh。G6保持原fresh长技术文档。

最终PASS必须基于真实ChatGPT Web、`GPT-5.6 Sol`、explicit Clear Writing、完整最终回复，而不是local replay、字符串扫描或skill自述。

## 版本

成功release方向保持：

- `writing-style 0.5 -> 0.6`
- Personal Plugin `0.5.0 -> 0.6.0`
- repository PATCH 在release时late-bind
- other central plugins NO_BUMP
- maturity NO CHANGE

0.6成功也不自动关闭Issue #13的#73/#49 downstream adaptation。
